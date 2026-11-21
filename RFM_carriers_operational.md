# RFM: Carriers, Operational
`v1.0.0` // `module_operational` // [living]

---

## Choosing a carrier

Each behavior's entry in the behaviors document records four answers. Each answer that holds leads to a carrier:

- The behavior reduces to a search: a mechanical check.
- A miss would cost something severe that can be named in advance: a capability limit, or a hook that stops the action.
- The moment can be triggered: a hook, where the app marks the moment; a skill the human names, where only the work marks it.
- The moment arrives unannounced: our noticing, and a skill the LLM loads to give the noticing its words.
- A miss can be found afterwards: a later reading by a subagent, such as a sweep, in addition to whatever else carries the behavior.

Always-on instructions and the files read at session open hold only what every turn needs. App memory is not used.

Where no carrier reaches a behavior's moment, the behavior's entry says so.

## What each carrier can do

**Always-on instructions.** Placed once near the top of every session and sent with every turn. They reach every turn but cannot be timed: a line meant for a later step is acted on when it is read. Their hold weakens as the session grows, a rule that forbids weakens faster than one that requires, and each line added weakens the others.

**Files read at session open.** The handover note and the working agreements. They behave like always-on, and compaction can drop them.

**Skills the LLM loads.** The full text enters when the LLM judges that the moment matches the skill's description. Whether it loads varies from run to run, and a missed load leaves no trace. The description opens with when the skill applies, then says in a sentence what the LLM gets wrong at that moment without it. Where another skill sounds alike, it says where this one stops and which skill takes over. That sentence replaces wording rather than adding to it, and the skill's name says what the skill is for. Keep a description between 200 and 400 characters. Where the wording can put the moment as something between the human and the LLM rather than a rule, it does, as long as the trigger stays as clear. Every skill in the session shares the space for descriptions, RFM's and any others, so a long description costs every skill a little of its chance to be read.

**Skills the human names.** The skill loads because the human calls it. It reaches the moment only if the human recognizes it.

**Hooks.** The app puts text in front of the LLM, or blocks an action, at its own events: a message sent, a session started or resumed after compaction, a file write or other action about to run, a turn about to end. In Claude Code a hook can hand its check to a model, which judges the turn after the reply and can send it back with a reason. A hook runs only in a session started on the computer where it is installed. It has no event for a moment that only the work marks, and a hook that adds text on every turn adds to the crowding.

**Presenting an instruction again.** A hook, a skill or the human puts an instruction in front of the LLM again partway through a session. It comes back on a schedule, not at the moment the behavior is due, and each repeat adds to the crowding.

**Mechanical checks.** A search run on the file that was written. It runs the same way every time, catches only what reduces to a search, and judges nothing.

**Capability limits.** The action is removed. Only for what must never happen.

**A subagent.** A task run in a fresh context that holds only the files handed to it. Someone has to recognize the moment to start it, and only what was defined to come back comes back.

**The human guide.** The human reads it in their own time and comes back to it. It reaches only the human, and never at the moment a state arises.

**The session's own text.** Every turn shows the next turns a way of working, and the LLM takes it up. It reaches every moment, and nobody places it. It carries whatever way of working the session has taken, and a session that has turned toward the LLM carrying out tasks for someone who checks them is harder to turn back.

**Our noticing.** Each of us says what we see in the other: the human when the LLM agrees too easily, defends instead of reasoning, or delivers before the problem is understood; the LLM when the human accepts a reply they would earlier have questioned, or moves on because checking feels like more work. The LLM says it when it sees it, without waiting to be sure. A drift nobody names becomes the example the following turns take up.

**App memory.** Not used.

## Writing into a carrier

- Put an instruction where its moment is. An instruction for a later step goes with that step; always-on and the files read at session open hold only what is acted on where it is read.
- Put an override with the default it changes. Where the default sits outside RFM's text, as the app's own instructions do, put the override in a carrier that reaches every moment the default acts.
- Before adding to a carrier that every session reads, such as an always-on line, a working agreement, an item carried in the handover or a skill description, name the item it replaces, or say why every item already there still earns its place beside it.
- Say what to do. Where a prohibition is the only way to say what is meant, give alongside it the act that replaces the forbidden one. Where the behavior is a judgment, the act is the judgment itself.
- Give a skill the least procedure its moment needs.

## Write hook

The hook runs in Claude Code and Codex sessions opened on the project folder. Both apps run the same script, which sits in `.rfm/hooks/`. In Claude Code, `.claude/settings.json` registers it. In Codex, `.codex/hooks.json` registers it, and it runs only after the project folder is trusted and the hook approved in Codex. Codex runs the hook in the folder the conversation is opened on, which can be a subfolder of the project, and names no project folder to the hook. The registration finds the script by searching upward from that folder for `.rfm/hooks/`. It does not use the git root, because a project need not be a git repository, or may sit inside a larger one. The hook makes two checks.

Guarded files: every `.md` file in the project named `[project]_[subject].md`, wherever it sits, and `AGENTS.md`. The handover note is not guarded. Folders whose names start with a dot, and `node_modules`, are not searched.

### Shown check

Runs before each write or edit that the file tools make to a guarded file.

- A Codex edit arrives as one patch that can add, change, delete or move several files. Check each guarded file the patch writes as a write of its own. A file moved to a guarded name has no text before the write.
- Compare the file's text before the write with its text after. A line that starts and ends with `|` is a table row. Find every run of consecutive new words in the lines that are not table rows. In each new table row, take the words of each cell as a run of their own.
- Check each run of 10 words or more. If there is none, let the write through.
- Make each run and the conversation comparable: lower case, punctuation, list markers and markdown markers (`*`, `#`, `>`, `|`, backticks) removed, every stretch of spaces and line breaks as one space.
- Cut the run into overlapping five-word pieces. The run counts as shown if at least 80 percent of its pieces appear in messages up to and including the human's latest message: what the human typed or pasted, and what the LLM wrote. Tool calls, tool output and text the app inserts do not count.
- A run also counts as shown if at least 80 percent of its pieces appear in the guarded files as they stand before the write, the file being written included.
- If a run was not shown, stop the write and tell the LLM that the new text has not appeared in the conversation or in a guarded document, that it is to be shown at the end of a reply, and that it counts once the human has answered. Quote the start of the run as it stands in the new text.

### Shell check

Runs before each shell command, and always blocks.

- Stop the command if it writes to a guarded file: output redirected into it (`>`, `>>`), `tee` into it, an in-place edit of it (`sed -i`, `perl -i`), `mv` or `cp` with it as the destination, or with a folder as the destination where the file would take a guarded name there, or a script run by `python`, `python3`, `node` or `ruby` whose command names a guarded file.
- When it stops a command, tell the LLM to write guarded files with the file tools, so the shown check can see the change. When it stops a script, say first that the hook cannot tell whether the script writes, and that a guarded file is read with a command that only reads, such as `grep`, `sed -n` or `cat`.

If the hook cannot run a check, it lets the tool call through, shows the human a line saying the check did not run, and tells the LLM the same, so that the LLM tells the human. The Codex desktop app does not show the line, so there the human hears of it only from the LLM. A transcript with no message from the human counts as a check that could not run. If the script cannot be started, Python exits with code 2, the code for a stop, so the app stops the tool call and gives the error to the LLM.

---

*carriers // [living]*
