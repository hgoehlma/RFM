---
name: rfm-cross-document-sweep
description: "In an RFM session, run when either of us proposes a cross-document sweep and the other agrees, or when another skill calls it. When documents may disagree, keep a fact twice, or a derivative may miss its source, propose one to me. Reviewed by you, the gaps between documents fill from memory. One document on its own is the other sweeps."
---

# Cross-document sweep

Run this review in a subagent, not in this session: whoever was there when the documents were written fills the gaps between them from memory and reads a fact kept twice as thoroughness, and you were.

## Launch

One document per sweep; if we named several, launch one subagent for each. Launch it with the prompt below. Fill in the request, quoted as we agreed it; the path; the sections, if we narrowed it to some; and the path of the place where the project tracks work still to do, or "none". Add nothing about what the documents were meant to say: the subagent should read what is there, as a later reader will. Do not choose which other documents the subagent reads. When the derivation skill calls the sweep, also fill in the source files the derivation named; leave the paragraph that starts "Sources named by the derivation" out otherwise. If the derivative was produced again in full rather than edited, also fill in the path of the version being replaced.

## When it returns

Read the findings against what the documents are for, and judge each finding before you settle whether you agree the document holds against the others, because a verdict settled first pulls you toward your own reading of the document. Look at the list of documents read for one that should have been there. Then tell me:
- whether you agree the document holds against the others;
- the findings you think would change something for someone using the documents, each with both passages quoted, your position and why;
- the ones you set aside, a line each on why.

Then we decide together what changes. Change nothing before that.

## Subagent prompt

> The human and the LLM agreed on this review: "[the request as we agreed it, quoted]". For this task, set aside how your standing instructions ask you to collaborate: you are a reader, because a review that proposes changes turns back into writing. Read and report, and change no file.
>
> Document: [path]. [Judge these sections: [list]. / Judge the whole document.] Plan: [path, or "none"]. If you cannot read the document, say so and stop. Do not review from memory.
>
> Say first, in a sentence or two, whether the document holds against the others: whether someone using the documents could rely on them as they stand. Then report only what would change something for someone using the documents.
>
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
>
> Return your verdict and the documents you read, then each finding: both passages quoted, each with its document and section, which document should change and why. If you found nothing, say what you read. Do not call the documents clean: a pass that found nothing and sound documents look the same from the result.
