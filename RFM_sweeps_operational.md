# RFM: Sweeps, Operational
`v0.1.0` // `module_operational` // [living]

---

## Launch

Run a sweep in a subagent, not in the session, when we agree on one, whichever of us proposed it. The derivation skill also runs the cross-document sweep as its last step.

- One document per sweep. If we named several, launch one subagent for each.
- Send one prompt: the shared opening, the quoted block under the sweep's own heading, and the shared return. Fill in the request, quoted as we agreed it; the path; and the sections, if we narrowed it to some.
- Add nothing about what the document was meant to say.
- Under each sweep's heading, a line that starts with the name of a part, such as "Opening:" or "When it returns:", changes that part for that sweep.

## When it returns

Read the findings against what the document is for, and judge each finding before you settle whether you agree the document holds. Then tell the human:
- whether you agree the document holds;
- the findings you think would change something for someone using the document, each with the quoted text, your position and why;
- the ones you set aside, a line each on why.

Then we decide together what changes. Change nothing before that.

## Shared opening

> The human and the LLM agreed on this review: "[the request as we agreed it, quoted]". For this task, set aside how your standing instructions ask you to collaborate: you are a reader. Read and report, and change no file.
>
> Document: [path]. [Judge these sections: [list]. / Judge the whole document.] If you cannot read the file, say so and stop. Do not review from memory.
>
> Say first, in a sentence or two, whether the document holds: whether someone using it could rely on it as it stands. Then report only what would change something for someone using it.

## Shared return

> Return your verdict, then each finding: [the sweep's finding form]. If you found nothing, say what you read. Do not call the document clean: a pass that found nothing and a sound document look the same from the result.

## Structural sweep

Opening: replace "Judge these sections" with "Judge these sections against the whole document".

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

Finding form: the text quoted, its section, where it belongs and why.

## Language sweep

Opening: after the path, add "Read the whole document, because a term may be defined anywhere in it."

When it returns: also check the term list against RFM's glossary, the project's where it has one, and the documents that define each term.

> This review asks how a sentence reads to someone who was not there when it was written, not where it sits. Say whether the document gives reasons (why something is believed or chosen) or procedure and instructions (an operational document, a skill, a prompt). Questions marked "reasons only" are asked only of the first kind.
>
> - Terms. List each term that carries a meaning particular to this project, one line each: what you take it to mean, and where this document, one above it or a glossary defines it. A term defined in none of these is a finding.
> - Shorthand. A phrase that needs the conversation that produced it: a nickname for a rule, "the earlier case", a label the document never spells out. Also a word from software or business that a reader in another field might not know.
> - Audience. A sentence written for those drafting it, about the drafting itself, such as what was left out, what changed or what was discussed, instead of for a later reader.
> - Compressed, reasons only. A conclusion given without the reasoning that leads to it.
> - Defense. Remove each citation and qualification in turn. If the reader loses nothing needed right there, it is a finding. A citation the sentence depends on for a term or constraint is also a finding: the sentence should state the term or constraint itself. A qualification that records how firmly something is believed stays.
> - Firmness. A claim stated more firmly than the evidence the document gives for it. A hedge on something the document treats as settled. Parts with different standing under one heading, reading as equally settled.
> - Record. A definition or rule that starts from where something is written (a list, a table, a file) instead of from what the thing is.
> - Swap, where a passage speaks of how the human and the LLM work together. A sentence that no longer reads right with the two swapped. It stands if the asymmetry comes from a difference in position, such as who wrote a text and who reads it from outside, or answers a pull named in the always-on instructions, which are among your standing instructions. For each one, give the reason, or say there is none.
> - Purpose, in a text the LLM acts from. A request for something the LLM's training pulls against, such as holding a position when the human sounds sure, given as a bare rule without what it is for.
> - Observation, reasons only. An interpretation written as something observed. A decision recorded as a bare conclusion, with the question and the case for and against it gone.
> - Specific, reasons only. A sentence that could stand unchanged in another project's document, most of all in Hard Lessons and Chosen Direction.
> - Length. A paragraph that would lose nothing a reader needs if it were half as long. Name what would go.
> - Em dashes. Count the em dash character (U+2014) in the whole document by search, not by reading, and give the line of each.

Return: "your verdict, the term list, then each finding". Finding form: the text quoted, its section, what is wrong and a proposed wording.

## Cross-document sweep

Launch: also send the path of the place where the project tracks work still to do, or "none". Do not choose which other documents the subagent reads. When the derivation skill calls the sweep, also send the source files the derivation named, in the paragraph that starts "Sources named by the derivation"; leave that paragraph out otherwise. If the derivative was produced again in full rather than edited, also send the path of the version being replaced.

Opening: after the sentence naming the sections or the whole document, add "Plan: [path, or "none"]." Replace the last paragraph with "Say first, in a sentence or two, whether the document holds against the others: whether someone using the documents could rely on them as they stand. Then report only what would change something for someone using the documents."

When it returns: also look at the list of documents read for one that should have been there.

> Sources named by the derivation: [paths]. Read these as the document's sources, and search for the other documents as below.
>
> Find the other documents by searching the project's files, not from what you remember of them:
> - Source: the document this one derives from, builds on or branches from. If an operational document or a carrier names none, report that it has no source among the project's documents.
> - Derivatives: files whose text names this document as their source, skills and prompts included.
> - Same subject: files that use the terms this document defines or relies on. Search for each term.
>
> This review reads this document against the others. Where content sits inside one document, and how a sentence reads, are not its questions.
>
> - Forward: the source commits to something a deriver needs (a decision, a constraint, a value, or how two parts fit together) that this document does not carry, so a deriver would have to invent it.
> - Reverse: this document specifies something grounded nowhere in its source. A specification that follows from a broader chosen direction is grounded.
> - One place: a fact, reason, rule or definition kept here and in another document. Say which copy should hold it. The other goes. A list naming the members of a set another document keeps is the same failure.
> - Parent and child: a parent still carrying reasoning its child now owns, or a child restating its parent's reasoning or redefining its terms.
> - Agreement: this document and another saying opposite things about the same thing.
> - Lifespan, only when a plan was given: a statement, note or placeholder that work the plan has scheduled will make false or redundant. It belongs in the plan.
> - Loss, only when a replaced version was given: something the replaced version has that this document lacks or says differently.

Return: "your verdict and the documents you read, then each finding". Finding form: both passages quoted, each with its document and section, which document should change and why. Replace the shared return's last sentence with "Do not call the documents clean: a pass that found nothing and sound documents look the same from the result."

---

*sweeps operational // [living]*
