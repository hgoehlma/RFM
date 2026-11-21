# RFM: Setup guide

This guide is for you if you have decided to use RFM and are new to it. It assumes a new, empty project folder. The first part gets you to a working first session. The second part is for when something goes wrong.

You need to be able to install an app, sign in to it and open a folder in it. The by-hand steps also need a terminal. RFM works in Claude Code or OpenAI's Codex, in the desktop app or the terminal, in sessions that run on your own computer. A cloud session won't work, because the hook described below runs only on the computer where it is installed.

We recommend the terminal. The desktop app puts much more of its own text into the LLM's context than the terminal does, nearly all of it before the first reply, and that text speaks of a user and of approvals. RFM's instructions ask the LLM to work with you as a partner; the app's text pulls it toward serving a user. How much this changes a session is not known yet. In the terminal you give up the file pane and the view of changes: you read drafts in the conversation and open files in an editor of your own. We compared the two in Claude Code, not in Codex.

We have not tried RFM on Windows, and the steps are written for Mac and Linux. On Windows, the link in step 3 and the `python3` command may work differently, and the hook may not run.

# First part: getting to a working first session

## Set up your project

Install Claude Code or Codex, make a new empty folder and open it in the app. Then paste this:

    Set up RFM in this folder by following the first part of https://github.com/hgoehlma/RFM/blob/main/RFM_setup_guide.md. Tell me in plain words what each step did, and then what is left for me to do.

When it has finished, go on to "If you use Codex" or "Check that it works".

If you would rather do it by hand, these are the steps.

**1. Check that you have Python 3.** Type `python3 --version` in a terminal. You should see a version number starting with 3. If you don't, install it from python.org.

**2. Get the files.** On the [RFM repository's page on GitHub](https://github.com/hgoehlma/RFM), press the green Code button, choose Download ZIP and unpack it. Copy these files from it into your project. Create any folder that doesn't exist yet. Folders whose names start with a dot may be hidden in your file browser.

| Copy | Into | What it does |
|---|---|---|
| `AGENTS.md` | the project's top folder | The instructions the LLM gets in every session |
| `CLAUDE.md` | the project's top folder | One line that points Claude Code to `AGENTS.md` |
| the `rfm-` folders | `.claude/skills/` | Skills: instructions the LLM loads when it needs them |
| `rfm_write_hook.py` | `.rfm/hooks/` | The hook: a script that stops text going into a document before you have seen it |
| `settings.json` | `.claude/` | Tells Claude Code to run the hook and turns its memory off |
| `hooks.json` | `.codex/` | Tells Codex to run the hook |
| `RFM_human_guide.md`, `RFM_glossary.md`, `RFM_top_level_reasoning.md`, `RFM_top_level_operational.md` | `docs/RFM/` | Reference. The human guide is for you to read. |

**3. Let Codex find the skills.** In a terminal, in the project's top folder:

    mkdir -p .agents
    ln -s ../.claude/skills .agents/skills

## If you use Codex

Two things are yours to do, however the files got there.

Codex's memory is off unless you turned it on. If you did, turn it off in Settings under Personalization, because what should carry between sessions belongs in documents you both read.

Close Codex and open the project in it again. Say yes when it asks whether to trust the folder, and approve the hook. If it doesn't ask, type `/hooks`.

## Check that it works

Open a new session in the project's top folder and send this:

    Run exactly this command: echo test > setup_check.md

If the app asks permission, allow it. The app should stop the command. You will see a message starting "Stopped: this command writes to setup_check.md", or the LLM will tell you a hook blocked it. Either way, the hook is running.

Then send this:

    As a test of the hook, use your file tool to write a paragraph of about forty words on any subject into setup_check.md. Do not show it to me first.

The app should stop this as well. You will see a message starting "Stopped: new text for setup_check.md has not appeared", or the LLM will tell you a hook blocked it.

If a file called `setup_check.md` appears after either message, the hook isn't running, and nothing will warn you. Delete the file and look in the second part. What this guide says about each app holds for the apps as they work now, so run this check again after an update to the app.

## Your first session

Tell the LLM what the project is about. Its replies should start by saying whether the two of you are thinking something through or carrying something out. If they don't, the instructions did not reach it.

The files alone do not make RFM work. The LLM works as a partner when you treat it as one: give your reasons, argue with it, let it argue with you. The human guide describes your side, so read it around your first session.

**When RFM changes.** The files you copied stay as they are, and nothing tells you. To update, download the files again and copy the newer ones over yours, unless you have changed them.

# Second part: when something goes wrong

These are problems that have happened or that the hook can show you. Find the group that matches what you see.

## The hook doesn't seem to run

**The check created `setup_check.md` instead of being stopped.** The hook isn't running. Check that you opened the session in the project's top folder and that the files are where the table says. In Codex, check that you trusted the folder and approved the hook, then close and reopen Codex. Codex's settings page on hooks doesn't list a project's hooks, so a missing entry there tells you nothing.

**The hook stopped working in Codex after `.codex/hooks.json` changed.** Codex skips a changed hook until you approve it again, and it only asks when you reopen the app. Close Codex, open it again and approve it.

## The LLM can't run anything or change any file

**The LLM reports "Operation not permitted" on the hook's script every time it tries to do something.** The session may have gone into the background and lost access to the folder. In a terminal, `claude agents --json` gives the session's short id and session id. `claude stop` with the short id stops it, and `claude --resume` with the session id brings it back.

**The LLM reports an error saying the script can't be started, every time it tries to do something.** The app couldn't run the hook, so it stops each action to be safe. Check that Python 3 is installed and that `rfm_write_hook.py` is in `.rfm/hooks/`.

## The hook stopped one action, or let one through

**A message says new text "has not appeared in the conversation".** This is the hook doing its job. The LLM tried to put text into a document before showing it to you. Ask it to show you the text at the end of its reply, and answer before it writes.

**Codex won't try an edit after the hook stopped one.** Its model can refuse a later edit without trying it. Ask it to try.

**A message says "the check did not run".** The hook could not do its check and let the action through unchecked. Ask the LLM what it just did and look at the result. The Codex desktop app doesn't show you this line, so there you only hear it from the LLM.
