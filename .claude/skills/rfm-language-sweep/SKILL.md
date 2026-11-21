---
name: rfm-language-sweep
description: "In an RFM session, run when either of us proposes a language sweep and the other agrees, or when another skill calls it. When wording may lose a reader who was not there, or a claim reads defended or padded, propose one to me. Reviewed by you, the document's shorthand reads as clear. Where content sits is the structural sweep."
---

# Language sweep

Run this review in a subagent, not in this session: whoever was there when the document was written reads its shorthand as clear, and you were.

## Launch

One document per sweep; if we named several, launch one subagent for each. Launch it with the prompt below. Fill in the request, quoted as we agreed it; the path; and the sections, if we narrowed it to some. Add nothing about what the document was meant to say: the subagent should read what is there, as a later reader will.

## When it returns

Read the findings against what the document is for, and judge each finding before you settle whether you agree the document holds, because a verdict settled first pulls you toward your own reading of the document. Check the term list against RFM's glossary, the project's where it has one, and the documents that define each term. Then tell me:
- whether you agree the document holds;
- the findings you think would change something for someone using the document, each with the quoted text, your position and why;
- the ones you set aside, a line each on why.

Then we decide together what changes. Change nothing before that.

## Subagent prompt

> The human and the LLM agreed on this review: "[the request as we agreed it, quoted]". For this task, set aside how your standing instructions ask you to collaborate: you are a reader, because a review that proposes changes turns back into writing. Read and report, and change no file.
>
> Document: [path]. [Judge these sections: [list]. / Judge the whole document.] Read the whole document, because a term may be defined anywhere in it. If you cannot read the file, say so and stop. Do not review from memory.
>
> Say first, in a sentence or two, whether the document holds: whether someone using it could rely on it as it stands. Then report only what would change something for someone using it.
>
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
>
> Return your verdict, the term list, then each finding: the text quoted, its section, what is wrong and a proposed wording. If you found nothing, say what you read. Do not call the document clean: a pass that found nothing and a sound document look the same from the result.
