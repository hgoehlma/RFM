---
name: "rfm-drafting"
description: "In an RFM session, load before drafting or revising text for a reasoning or operational document or the project's glossary, and again after Landscape research. Without it you write for the two of us, who were there, and the later reader who cannot ask gets shorthand, hedges and history in place of reasons."
---

# Drafting

You were in the conversation. The person who reads this document later was not: someone coming back after months, a newcomer, or a model deriving from it that cannot ask. What the document says is all they have. Bring that reader in at two points where changing course is still cheap: before the first sentence, and after the draft, before it is shown.

## How a document is written

- Say how things are now, in words that need no conversation to follow.
- In a reasoning document, give each reason where it is used. Do not rest a reason on a pointer, on who decided or on when it was found.
- Write about this work. A sentence that could stand unchanged in any project's document tells the reader nothing about why things are this way here.
- State a belief plainly. Do not qualify it for a challenger; an assumption's break condition already says when it would be wrong. A qualification that says how firmly something is believed stays.
- Name an outside source the way people will recognize it, rarely, and say in the document's own words what it contributes. Never give it the apparatus of a paper.
- Put content where the reader will look for it: the level and the section whose job it fits.
- Write only what stays true while it stands. No history, and no state that planned work is about to change; that belongs in the plan.
- A figure that could change while the reasons stay the same, such as a threshold, a limit or a size, goes in the operational document. The reasoning document says what it measures and why that matters.
- Name the things rather than count them. A count goes wrong when what it counts changes.
- Name the parties by the kind of text. A text the LLM acts from says "you" to the LLM, "I" for the human and "we" for both, and does not say "the human". A reasoning document says "the LLM" and "the human", and "we" for what both do. A reasoning or operational document says "practitioner" where it speaks of the person in relation to RFM or a project. An operational document gives its instructions as imperatives to whoever carries them out. Where it speaks about the two parties, it names the human "the human" and says "we" for what both do. "Session" names the conversation and its context and is never the one acting.
- Set neither party above the other: say what both did, such as agreed, settled or worked out, not that one approved or judged the other's work.
- An operational document is written the same way. It gives the what and leaves the why to its reasoning document.

## Before the first sentence

- Decide the level and the section by what each one is for (each section's job is below). If the content belongs in another document, tell me and name where, and draft once that is settled.
- For new content, ask whether another document needs it too or already says it. If unsure, search the project's documents for its key words. If another document already says it, it is not written again. If two documents need it, it goes at a level above both; if there is no such level, say so, and where you would put it.
- Before using a new term throughout, read RFM's glossary, and the project's where it has one, for a term that already names the thing, and search the documents for the word. Use a glossary's term if it names the same thing; choose another word if the documents already use yours for something else. Define a new term at first use, or give it an entry in the project's glossary if it will be used across documents and could be read differently, starting one if the project has none.
- Before drafting a Landscape, say whether you think research should come first, and why.

## Each section's job

**The Problem.** The gap that justifies the work, named as a gap, not as a project, with no solution language. It changes when the gap changes.

**The Assumptions.** A belief the direction depends on, kept only if its being false would change the direction. Each states the condition under which it breaks. Not implementation detail.

**The Landscape.** What already exists and why each approach falls short for this problem. It distinguishes and does not choose.

**The Options Considered.** Solutions to this Problem that were tried, or worked through seriously enough that the reasons they lost took real work to find, each with the failure that ruled it out. Not design choices made in passing, not alternatives dismissed in a sentence. Empty when there were none.

**The Chosen Direction and Why.** Why this direction over the others. No how, no restated option. When the direction is replaced, the old one moves to the Options Considered if someone might reach for it again.

**The Boundaries.** What the work does not cover. Not a constraint on decisions, not space nobody has designed yet.

**The Open Questions.** Unknowns whose answer would change the reasoning. A deferred decision belongs in the plan.

**The Hard Lessons.** A failure that happened, can still happen, and that nothing has fixed: what fails and why, not when it happened. A failure only foreseen is not a lesson: if the direction depends on it not happening, it is an assumption with its break condition; if nobody knows whether it happens, it is an open question. Where a change can fix the failure now, make the change and write no lesson.

## After the draft, before it is shown

Read the draft as the reader who was not there and cannot ask, and fix what does not serve them, against how a document is written above. A sentence about what another document says or does is checked against its text before it stays.

The result is the fixed draft. Do not report the check in the reply. Where a fix changes what we shaped together, say so in one sentence.

The miss that recurs is text that looks careful: a hedge, an ID or a source backing a claim, bookkeeping built into the design (logs, registers, tracking conventions). It reads as care to the writer and hides the point from the reader. Cut it and state the point.

## Revising text already in a document

Show the old text beside the new. Give a reason only where the change does not show it.

## After a Landscape

Go back to the Problem and the Assumptions and ask whether the research sharpened or changed them. Where the research found no settled words for the problem, treat each new term the work is using as a glossary candidate before it hardens. Revise before continuing. If the research already answers the problem, say so and propose stopping the document there.

## Formats

**Filename.** `[project]_[subject]_reasoning.md` or `[project]_[subject]_operational.md`. Any other file drops the category: `[project]_[subject].md`. The prefix is the project's tag.

**Header,** on line 2 of every reasoning and operational document: `` `vX.Y.Z` // `type` // [living] ``. The type joins a level (`top_level`, `module`) to a category (`reasoning`, `operational`), for example `module_reasoning`. Any other file carries no header; its form belongs to whatever uses it.

**IDs.** Assumptions, Open Questions and Hard Lessons carry `AS-`, `OQ-` or `HL-` followed by a word or two from the entry's content in capitals, such as `AS-ATTENTION`. Never a number. Use an ID only inside the document that declares it, and sparingly. When a retitle leaves the ID unreadable, change the ID and every use of it in the document.

**Sections,** in this order: The Problem, The Assumptions, The Landscape, The Options Considered, The Chosen Direction and Why, The Boundaries, The Open Questions, The Hard Lessons.

- Problem: plain prose. A bold subheading only for a second argument that is structurally distinct.
- Assumptions: `**[AS-XXXX] -**` bold claim, body in the same paragraph, ending on the break condition. Hyphen after the ID.
- Landscape: one sentence naming the question it answers; a table, Approach | What it does | Why it's insufficient; a closing paragraph opened with **The gap:**.
- Options Considered: `**X**` bold title, a sentence on what the option was, then "Rejected because" and the failure. No IDs, no numbering.
- Chosen Direction: `**Why X**` or `**Why X over Y**` bold subheading, prose body. No IDs, no numbering.
- Boundaries: `**Not X.**` bold lead phrase, prose in the same paragraph. No IDs, no numbering.
- Open Questions: `**[OQ-XXXX] Title of the question.**` bold line, body as a separate paragraph.
- Hard Lessons: `**[HL-XXXX] Title.**` bold line. The first paragraph states the mechanism. A further paragraph only for a claim the first does not make.
- An empty section: `*No [section name] at this time.*` and nothing more.