---
name: rfm-structural-sweep
description: "In an RFM session, run when either of us proposes a structural sweep and the other agrees, or when another skill calls it. When content may sit at the wrong level or section, or be argued twice, propose one to me. Reviewed by you, misplacements look sound, because you know what each part was meant to hold. How text reads is the language sweep."
---

# Structural sweep

Run this review in a subagent, not in this session: whoever was there when the document was written reads its misplacements as sound, and you were.

## Launch

One document per sweep; if we named several, launch one subagent for each. Launch it with the prompt below. Fill in the request, quoted as we agreed it; the path; and the sections, if we narrowed it to some. Add nothing about what the document was meant to say: the subagent should read what is there, as a later reader will.

## When it returns

Read the findings against what the document is for, and judge each finding before you settle whether you agree the document holds, because a verdict settled first pulls you toward your own reading of the document. Then tell me:
- whether you agree the document holds;
- the findings you think would change something for someone using the document, each with the quoted text, your position and why;
- the ones you set aside, a line each on why.

Then we decide together what changes. Change nothing before that.

## Subagent prompt

> The human and the LLM agreed on this review: "[the request as we agreed it, quoted]". For this task, set aside how your standing instructions ask you to collaborate: you are a reader, because a review that proposes changes turns back into writing. Read and report, and change no file.
>
> Document: [path]. [Judge these sections against the whole document: [list]. / Judge the whole document.] If you cannot read the file, say so and stop. Do not review from memory.
>
> Say first, in a sentence or two, whether the document holds: whether someone using it could rely on it as it stands. Then report only what would change something for someone using it.
>
> This review asks where content sits, not how it reads. If the document uses the reasoning sections (The Problem, The Assumptions, The Landscape, The Options Considered, The Chosen Direction and Why, The Boundaries, The Open Questions, The Hard Lessons) and one is missing or out of order, report that first. If it has another layout, take each part's job from what the document says its parts hold.
>
> Level:
> - Procedure, named steps or a format in a document that holds reasons. It belongs in the operational document.
> - A reason in a document that holds procedure. It belongs in the reasoning document behind it.
> - A decision put off or a step planned for later, written into the document, including an open question that is really a deferred decision. It belongs where the project tracks work still to do.
> - Content about a narrower or wider scope than the document's own.
>
> Section, in a document with the reasoning sections:
> - The Problem carries solution language, or detail from a sub-problem.
> - An assumption carries implementation detail.
> - The Landscape starts choosing.
> - An option restates the chosen direction, or does not say why it was rejected.
> - A Chosen Direction entry says how, or restates an option.
> - A boundary that constrains decisions, which makes it an assumption, or that covers space nobody has designed yet, which makes it an open question.
>
> Form, in any layout:
> - An item filed under another item of a different scope.
> - The same structure, such as a set of steps or a table of cases, written out again in several places because the section it sits in has no form for it.
> - An entry carrying several claims under a title that covers only some of them.
> - A section holding options, cases or detail that need a place of their own. Length alone is not a finding.
> - Two entries or sections carrying one argument in different words, including a closing summary that restates the body.
>
> Return your verdict, then each finding: the text quoted, its section, where it belongs and why. If you found nothing, say what you read. Do not call the document clean: a pass that found nothing and a sound document look the same from the result.
