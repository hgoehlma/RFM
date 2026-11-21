# RFM: Fresh-Read Skill, Reasoning
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

A reasoning document is written by people who were in the conversation that produced it. When they read it back, that conversation fills whatever the text leaves out, and the document reads as complete to them. A reader who was not there has only the text: someone joining the project later, someone returning after months, or a model deriving from the documents.

That reader fails in two ways. Where the text leaves something out, the reader fills the gap with a guess. The guess reads as faithful to the document, so neither the reader nor anyone checking their work sees it as a guess. A model deriving code or a skill builds on the guess as firmly as on what is written.

In the second failure, the reader misreads a passage with confidence, for example taking two ideas the document keeps apart as one. Nothing feels missing, so the reader has nothing to report. The misreading shows only later, in what the reader builds.

The writers cannot find either failure by reading their own document again. The context that filled a gap the first time fills it again, and they read each passage as they meant it.

## The Assumptions

**[AS-READER] - A model handed only the files hits the gaps a person new to the project would hit.** Neither has the conversation that produced the documents, so where the text leaves something out, both have to guess. This breaks if the model's general knowledge differs from the newcomer's enough to change where they stumble: the model fills from wide reading what a newcomer would have to ask about, or stumbles over what anyone in the field would know. It also breaks if the reader reaches documents it was not handed.

**[AS-NOTICE] - A reader asked to list what it had to interpret or guess finds most of the places where the text leaves something out.** A gap is usually felt while reading: a step with no reason given, a term used without meaning, two passages that do not fit together. Asked directly, a model names these. This breaks if models fill gaps without registering them, so that the list comes back short while the files still leave gaps a reader would fill.

**[AS-RESTATE] - A reader that restates each section in a few sentences of its own shows how it understood the section.** Saying a section in two or three sentences forces the reader to choose what the section holds and how its parts relate. Where the reader has merged two ideas into one, the restatement carries one where the source has two. This breaks if the reader echoes the source's wording closely enough that restatement and source look the same while the understanding behind them differs.

**[AS-COMPARE] - The LLM that helped write the files can tell a restatement that merged two ideas from its source when both are quoted side by side.** The LLM reads the source as it was meant, so it cannot find a merge by reading the source alone. Side by side, the merge is in the text: one idea where the source has two. This breaks if the LLM marks merged restatements as same, and the human, holding the same context, passes them too.

## The Landscape

What exists for finding where a document leaves gaps that a reader without the writers' context would fill?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Reader tests of documentation, such as the User Edit method in technical writing | A reader follows the documentation on the real product and marks or says aloud where it fails: missing steps, undefined terms, wrong instructions | Needs a human participant and something to perform the task on. Tests procedures, not reasoning. |
| Teach-back, from clinical practice | The listener explains in their own words what they were told, and the explainer treats a wrong explanation as a fault in how it was explained | Runs in conversation with the explainer present, who corrects on the spot. Nothing comes back as a list of what the explanation left out. |
| Clarification steps in spec-driven development, such as Spec Kit's clarify | Before planning, a model scans a spec against a fixed list of categories and asks the author about what is unclear or missing | Runs in the session that holds the writing context, so that context can fill the gaps. Finds gaps only in the categories it names. |
| Divergence checks in code generation, such as ClarifyGPT | Several implementations of one requirement are generated and run on the same inputs; different results mark the requirement as ambiguous | Needs output with behavior that can be tested. Works on a single requirement, not on a set of reasoning documents. |

**The gap:** nothing reads a set of documents in a context that holds only them and returns both what the reader had to guess and how it understood each part, without a human participant or runnable tests.

## The Options Considered

*No Options Considered at this time.*

## The Chosen Direction and Why

**Why a separate context**

The context of the session in which the documents were written fills the gaps the test looks for. A reader in that session reads past each gap as the writers do. So the read runs in a subagent that is handed only the files.

**Why the reader lists every file it opened**

A reader told to read only the handed files can still open others. A list of the files it opened can be compared with the files it was handed. A run that opened anything else is void, because its findings may rest on what it read there.

**Why the LLM adds only the request, the files and the task**

Anything the LLM writes into the prompt about what the files mean, what was decided or what the reader should find reaches the reader and fills the gaps again. The rest of the prompt is fixed text, the same on every run.

**Why one question for two tasks**

A fresh read is run for one of two tasks: understanding the files as someone new to the project, or doing a named task with them. Each asks the same thing of the files: what the reader would have to interpret, guess or bring from outside them. One question keeps one prompt for both, and the task tells the reader what it is reading for. In the do task, doing the task is how the reader finds where the files fail it, so it does the task and marks each place where it used a guess.

**Why a short restatement and a separate list of objections**

A reader that misreads with confidence reports no guess, because nothing felt missing. Restating each section in two or three sentences of its own shows how the reader understood it. The LLM puts each restatement beside the passage it restates, and a restatement that differs from its source is a finding. A fresh reader also sometimes meets a gap and reports it as a fault in the document: a step that seems wrong, or two passages that seem to conflict. The objections come back as a list of their own, and each is treated as a possible gap.

**Why the reader sets aside how the standing instructions ask it to collaborate**

Inside a project, the reader carries the project's standing instructions, and in an RFM project those ask it to challenge, propose and discuss. A reader acting on them argues with the documents instead of reporting what it could not follow. The prompt sets aside only how the instructions ask the reader to work, and the reader reports. The weighing happens in the session.

**Why the LLM gives its view on each finding, and why a finding closes only on a quoted passage**

The LLM cannot find these gaps itself, but it knows what the documents are for and can judge a finding put in front of it. If it passed the findings on untouched, the human would sort them alone while the LLM kept its view to itself. So the LLM says for each finding what it thinks and why, and we decide together what changes. The LLM's view has one limit here. Its context is what fills the gaps, so a finding it judges clear may be clear only to those who were there. A finding closes only where the LLM can quote the passage in the handed files that answers it. Where the LLM knows the answer but cannot quote it, it says what it takes the answer to be and that the answer lives only in the conversation, and we decide whether it goes into the documents.

**Why a clean run says nothing about whether the files are sufficient**

A run with no findings shows that this reader, holding these files, found nothing to guess for this task. Another reader or another task can find gaps this one did not. The return always states the task and every file opened, and a run with no findings is reported as such, never as a verdict that the files are sufficient.

**Why it runs when we agree**

Gaps cost most when someone who was not there is about to rely on a document. Either of us can see when that point has come, so the read runs when one of us proposes it and the other agrees. A model about to derive from the documents meets the same gaps, but the derivation skill's subagent marks them as it derives, so a read beforehand would find what the derivation finds anyway.

## The Boundaries

**Not documents against each other.** Whether documents disagree, keep a fact twice, or whether a derivative covers its source is the cross-document sweep's question. A fresh read compares what the files say with what a reader needs, not one file with another.

**Not wording.** Terms, shorthand and phrasing a later reader cannot follow are the language sweep's job, which also asks what the reader takes each project term to mean. A fresh read reports a term only where the reader would have to guess its meaning to do the task.

**Not deriving.** A derivation runs under the derivation skill, whose subagent derives from the sources alone and marks each guess as it goes.

**Not the changes.** A fresh read changes no file. What goes into the documents is decided together afterwards, and carried out like any agreed work.

## The Open Questions

**[OQ-LOAD] Does a model in another project load the skill when the human asks for a fresh read?**

The skill's description names the requests that should load it. If a model in another project answers the request in its own session instead, the read runs in the very context it is meant to avoid, and the skill needs another way in.

**[OQ-PROPOSE] Does the LLM propose a fresh read at the moments it would help?**

If it proposes them too often, or not at all, the proposal needs a clearer moment, or it goes.

## The Hard Lessons

*No Hard Lessons at this time.*

---

*fresh-read skill reasoning // [living]*
