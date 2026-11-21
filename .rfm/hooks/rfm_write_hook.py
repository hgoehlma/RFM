#!/usr/bin/env python3
"""RFM write hook, derived from the Write hook section of RFM_carriers_operational.md.

That document and its reasons, in RFM_carriers_reasoning.md, are RFM's own.
They sit in the RFM repository, https://github.com/hgoehlma/RFM, not in your
project. The values below come from the operational document, so a change to
them starts there, in RFM's own project.

Runs as a PreToolUse hook in Claude Code and in Codex. Reads the hook input as
JSON on stdin. Exit 0 lets the tool call through; exit 2 stops it and shows
stderr to the LLM.
"""
import difflib
import json
import math
import os
import re
import shlex
import sys

MIN_RUN = 10
PIECE = 5
SHARE = 0.8

HOOK_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(os.path.dirname(HOOK_DIR))
GUARDED_NAME = re.compile(r"^[^_]+_.+\.md$")  # [project]_[subject].md
GUARDED_ALWAYS = "AGENTS.md"
NOT_GUARDED_ENDING = "_handover.md"
SKIPPED_FOLDER = "node_modules"  # as well as folders whose names start with a dot


class CheckFailed(Exception):
    pass


def resolve(path, cwd):
    path = os.path.expanduser(path.strip("'\""))
    return os.path.normpath(os.path.join(cwd, path))


def guarded_name(name):
    if name == GUARDED_ALWAYS:
        return True
    return bool(GUARDED_NAME.match(name)) and not name.endswith(NOT_GUARDED_ENDING)


def skipped_folder(name):
    return name.startswith(".") or name == SKIPPED_FOLDER


def guarded(path):
    rel = os.path.relpath(path, PROJECT)
    parts = rel.split(os.sep)
    if parts[0] == os.pardir or any(skipped_folder(p) for p in parts[:-1]):
        return False
    return guarded_name(parts[-1])


def guarded_paths():
    for folder, subfolders, names in os.walk(PROJECT):
        subfolders[:] = [s for s in subfolders if not skipped_folder(s)]
        for name in names:
            if guarded_name(name):
                yield os.path.join(folder, name)


# Shown check

TOKEN = re.compile(r"[^\W_]+")


def tokens(text):
    # Lower case; punctuation, list markers and markdown markers fall away.
    # Each word keeps where it stands in the text, so a stop can quote it.
    return [(m.group().lower(), m.start(), m.end()) for m in TOKEN.finditer(text)]


def words(text):
    return [w for w, _, _ in tokens(text)]


def quote(text, toks):
    # The start of a run as it stands in the new text.
    end = toks[min(len(toks), 10) - 1][2]
    return " ".join(text[toks[0][1]:end].split())


def table_row(line):
    line = line.strip()
    return len(line) > 1 and line.startswith("|") and line.endswith("|")


def new_runs(before, after):
    """Each run of new words, as (words, quote). Table rows are matched cell by cell."""
    before_lines, after_lines = before.splitlines(), after.splitlines()
    old_text = "\n".join(l for l in before_lines if not table_row(l))
    new_text = "\n".join(l for l in after_lines if not table_row(l))
    old, new = words(old_text), tokens(new_text)
    matcher = difflib.SequenceMatcher(None, old, [w for w, _, _ in new], autojunk=False)
    runs = [new[j1:j2] for op, _, _, j1, j2 in matcher.get_opcodes()
            if op in ("insert", "replace") and j2 - j1 >= MIN_RUN]
    result = [([w for w, _, _ in r], quote(new_text, r)) for r in runs]
    old_rows = {l.strip() for l in before_lines if table_row(l)}
    for line in after_lines:
        if table_row(line) and line.strip() not in old_rows:
            for cell in line.strip()[1:-1].split("|"):
                toks = tokens(cell)
                if len(toks) >= MIN_RUN:
                    result.append(([w for w, _, _ in toks], quote(cell, toks)))
    return result


def pieces(ws):
    return {tuple(ws[i:i + PIECE]) for i in range(len(ws) - PIECE + 1)}


def strip_inserted(text):
    # Text the app adds inside a human message does not count as shown.
    return re.sub(r"<(system-reminder|command-[a-z]+)>.*?</\1>", " ", text, flags=re.S)


def content_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(b.get("text", "") for b in content
                        if isinstance(b, dict) and b.get("type") in ("text", "Text"))
    return ""


def classify(e):
    """Return ("human", text), ("llm", text) or None for one transcript entry."""
    # Claude Code: the human's own messages carry origin.kind "human".
    if e.get("isSidechain") or e.get("isMeta"):
        return None
    kind = e.get("type")
    if kind == "user" and (e.get("origin") or {}).get("kind") == "human":
        return "human", content_text(e.get("message", {}).get("content"))
    if kind == "assistant":
        return "llm", content_text(e.get("message", {}).get("content"))
    # Codex: the human's own messages are UserMessage items, the LLM's AgentMessage.
    # Entries the app inserts under the role "user" are never these items.
    if kind == "event_msg":
        p = e.get("payload") or {}
        item = p.get("item") or {}
        if p.get("type") == "item_completed":
            if item.get("type") == "UserMessage":
                return "human", content_text(item.get("content"))
            if item.get("type") == "AgentMessage":
                return "llm", content_text(item.get("content"))
    return None


def shown_pieces(transcript_path):
    """Pieces from messages before the human's latest message."""
    shown_msgs, current, human_seen = [], [], False
    with open(transcript_path, encoding="utf-8") as f:
        for line in f:
            try:
                e = json.loads(line)
            except ValueError:
                continue
            found = classify(e)
            if found is None:
                continue
            who, text = found
            if who == "human":
                # A new human message: everything up to it now counts as shown.
                shown_msgs.extend(current)
                current = [strip_inserted(text)]
                human_seen = True
            else:
                current.append(text)
    # current holds the human's latest message and what followed it.
    # The latest message itself counts; what followed it does not.
    if not human_seen:
        raise CheckFailed("no message from the human found in the transcript")
    shown_msgs.append(current[0])
    result = set()
    for text in shown_msgs:
        result |= pieces(words(text))
    return result


def guarded_pieces():
    """Pieces from the guarded files as they stand before the write."""
    result = set()
    for p in guarded_paths():
        with open(p, encoding="utf-8", errors="replace") as f:
            result |= pieces(words(f.read()))
    return result


def after_text(tool, inp, before):
    if tool == "Write":
        return inp.get("content", "")
    edits = inp.get("edits") if tool == "MultiEdit" else [inp]
    text = before
    for ed in edits or []:
        old, new = ed.get("old_string", ""), ed.get("new_string", "")
        text = text.replace(old, new) if ed.get("replace_all") else text.replace(old, new, 1)
    return text


def read_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def verdict(data, writes):
    """writes: (path, runs) for each guarded file. Stop on the first unshown run."""
    writes = [(p, r) for p, r in writes if r]
    if not writes:
        return 0
    shown = shown_pieces(data.get("transcript_path", "")) | guarded_pieces()
    for path, runs in writes:
        for run, start in runs:
            ps = [tuple(run[i:i + PIECE]) for i in range(len(run) - PIECE + 1)]
            if sum(p in shown for p in ps) < math.ceil(SHARE * len(ps)):
                rel = os.path.relpath(path, PROJECT)
                sys.stderr.write(
                    f"Stopped: new text for {rel} has not appeared in the conversation or in a "
                    f"guarded document, starting \"{start}\". "
                    "Show it to the human at the end of your reply; "
                    "it counts once the human has answered.\n")
                return 2
    return 0


def shown_check(data):
    inp = data.get("tool_input", {})
    path = resolve(inp.get("file_path", ""), data.get("cwd", PROJECT))
    if not guarded(path):
        return 0
    before = read_file(path)
    runs = new_runs(before, after_text(data.get("tool_name"), inp, before))
    return verdict(data, [(path, runs)])


# Codex patch

PATCH_FILE = re.compile(r"^\*\*\* (Add|Update|Delete) File: (.+)$")
MOVE_TO = re.compile(r"^\*\*\* Move to: (.+)$")


def parse_patch(text):
    """Yield one dict per file the patch touches: kind, path, move_to, hunks.
    A hunk is (old lines, new lines); an added file is one hunk with no old lines."""
    op = None
    for line in text.splitlines():
        m = PATCH_FILE.match(line)
        if m:
            if op:
                yield op
            op = {"kind": m.group(1), "path": m.group(2).strip(), "move_to": None,
                  "hunks": [([], [])]}
            continue
        if op is None or line.startswith("*** "):
            m = MOVE_TO.match(line)
            if op and m:
                op["move_to"] = m.group(1).strip()
            continue
        if line.startswith("@@"):
            op["hunks"].append(([], []))
            continue
        old, new = op["hunks"][-1]
        if line.startswith("+"):
            new.append(line[1:])
        elif line.startswith("-"):
            old.append(line[1:])
        else:  # a context line, in both
            old.append(line[1:] if line.startswith(" ") else line)
            new.append(line[1:] if line.startswith(" ") else line)
    if op:
        yield op


def patch_check(data):
    cwd = data.get("cwd", PROJECT)
    writes = []
    for op in parse_patch(data.get("tool_input", {}).get("command", "")):
        if op["kind"] == "Delete":
            continue
        source = resolve(op["path"], cwd)
        target = resolve(op["move_to"], cwd) if op["move_to"] else source
        if not guarded(target):
            continue
        # Each hunk's old and new lines show what is new. Text moved within the
        # file is found in the file as it stood, which counts as shown.
        runs = []
        for old, new in op["hunks"]:
            runs += new_runs("\n".join(old), "\n".join(new))
        if op["move_to"] and target != source:
            # A file moved to a guarded name has no text before the write.
            runs += new_runs("", read_file(source))
        writes.append((target, runs))
    return verdict(data, writes)


# Shell check

SEGMENT = re.compile(r"\|\||&&|[;|\n]")
REDIRECT = re.compile(r"(?:&|\d)?>>?\|?\s*([^\s;&|<>]+)")
INTERPRETERS = ("python", "python3", "node", "ruby")


def guarded_names():
    return {os.path.basename(p) for p in guarded_paths()}


def shell_targets(command, cwd):
    targets = [m.group(1) for m in REDIRECT.finditer(command)
               if not m.group(1).startswith("&")]
    scripted = False
    for seg in SEGMENT.split(command):
        try:
            toks = shlex.split(seg)
        except ValueError:
            toks = seg.split()
        if not toks:
            continue
        name, args = os.path.basename(toks[0]), toks[1:]
        plain = [a for a in args if not a.startswith("-")]
        if name == "tee":
            targets += plain
        elif name in ("sed", "perl") and any(a.startswith("-i") or a == "--in-place" for a in args):
            targets += plain
        elif name in ("mv", "cp"):
            if "-t" in args and args.index("-t") + 1 < len(args):
                dest = args[args.index("-t") + 1]
                sources = [a for a in plain if a != dest]
            elif plain:
                dest, sources = plain[-1], plain[:-1]
            else:
                continue
            targets.append(dest)
            if os.path.isdir(resolve(dest, cwd)):
                # A folder as the destination: the file takes its own name there.
                targets += [os.path.join(dest, os.path.basename(s)) for s in sources]
        elif name in INTERPRETERS:
            scripted = True
    hits = [t for t in targets if guarded(resolve(t, cwd))]
    named = []
    if scripted:
        # The hook sees a script's text, not what it does, so naming a guarded file is enough.
        named = [n for n in guarded_names() if n in command and n not in hits]
    return hits, named


def shell_check(data):
    command = data.get("tool_input", {}).get("command", "")
    hits, named = shell_targets(command, data.get("cwd", PROJECT))
    if not hits and not named:
        return 0
    if hits:
        first = f"Stopped: this command writes to {', '.join(hits)}. "
    else:
        first = (f"Stopped: this command runs a script that names {', '.join(named)}, and the "
                 "hook cannot tell whether the script writes. A guarded file is read with a "
                 "command that only reads, such as grep, sed -n or cat. ")
    sys.stderr.write(
        first + "Guarded files are written with the file tools (Write and Edit in Claude Code, "
        "apply_patch in Codex), so the shown check can see the change.\n")
    return 2


def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get("tool_name")
        if tool in ("Write", "Edit", "MultiEdit"):
            return shown_check(data)
        if tool == "apply_patch":
            return patch_check(data)
        if tool == "Bash":
            return shell_check(data)
    except Exception as exc:  # a fault lets the call through and tells the human
        reason = str(exc) if isinstance(exc, CheckFailed) else f"{type(exc).__name__}: {exc}"
        line = f"RFM write hook: the check did not run ({reason})."
        # systemMessage is shown to the human where the app shows it; the Codex
        # desktop app does not, so the LLM is told too and passes it on.
        print(json.dumps({
            "systemMessage": line,
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": line + " Tell the human in your next message.",
            },
        }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
