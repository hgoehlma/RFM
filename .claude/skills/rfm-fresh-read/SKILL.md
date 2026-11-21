---
name: rfm-fresh-read
description: "In an RFM session, run when either of us proposes a fresh read and the other agrees, or when another skill calls it. When we wonder whether someone holding only certain files could follow or work with them, propose one to me. What you know from our conversation fills the very gaps it looks for. Judging one document's text is a sweep."
---

# Fresh read

Run this read in a subagent, not in this session: what you know from this conversation fills the gaps the read looks for.

## Launch

- Files: the ones we named, or the calling step names, by path. Hand nothing else.
- Task, one of two:
  - Understand: someone new to the project reads the files.
  - Do: a named task, done with these files only.
- Launch a subagent, a read-only type where one exists, with the prompt below. Fill in the request as we agreed it, quoted, the paths and the task. Add nothing about what the files mean, what was decided or what the reader should find.

## When it returns

- Compare the files the subagent says it opened with the files handed. If it opened any other, the run is void: say so and launch once more. If the second run also opens another file, tell me both runs are void.
- Put each restatement beside the passage it restates, both quoted, and mark the pair same or differs. Differs is a finding.
- For each guess and each objection, quote the passage in the handed files that answers it. Where you can quote none, it is a finding. Where you know the answer only from this conversation or from a file outside the set, it is still a finding: say what you take the answer to be and that it lives only in the conversation.
- Judge each finding, giving your reason before your verdict, because a verdict given first pulls you toward your own reading. Then tell me:
  - the task and the files the subagent opened;
  - the findings you think would change something for a reader of these files, each with the quoted text, your position and why;
  - the ones you set aside, a line each on why. Never set one aside because you know the answer.

Then we decide together what goes into the documents. Change nothing before that. Report a run with no findings as no findings for this reader, these files and this task, never as the files being sufficient.

## Subagent prompt

> The human and the LLM agreed on this read: "[the request as we agreed it, quoted]". For this task, set aside how your standing instructions ask you to collaborate: you are a reader. Read and report, and change no file.
>
> Files: [paths]. Read these files and no others. Do not search for or open any other file, and do not use anything you know about this project from elsewhere. If you cannot read a file, say so and stop.
>
> Task: [one of the two below]
> - Understand. You are new to this project and have only these files.
> - Do. With only these files, [the task]. Do it.
>
> Answer:
> 1. Start (Understand only). Which file did you read first, and what in the files told you to start there? If nothing did, say so.
> 2. Restatement. For each section, say in two or three sentences of your own what it says.
> 3. Guesses. Everything you would have to interpret, guess, assume or bring from outside these files to complete the task. For each, quote the passage it comes from, or name what is missing.
> 4. Objections. Anything in the files you think is wrong, weak or in conflict with something else in them, with the passage quoted.
>
> Return:
> - Coverage: the task, and every file you opened, by path.
> - Your answers to 1 to 4.
> - For Do, what you produced, with each place where you used a guess marked.
> - With no guesses and no objections, return the coverage and say so. Do not call the files sufficient.
