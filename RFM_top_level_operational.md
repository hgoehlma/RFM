# RFM: Top Level, Operational
`v1.0.0` // `top_level_operational` // [living]

---

## How a document is written

Write for a reader who was not there and may not be able to ask.
- Say how things are now, in words that need no conversation to follow.
- In a reasoning document, give each reason where it is used. Do not rest a reason on a pointer, on who decided or on when it was found.
- Write about this work. A sentence that could stand unchanged in any project's document tells the reader nothing about why things are this way here.
- State a belief plainly. Do not qualify it for a challenger; an assumption's break condition already says when it would be wrong. A qualification that says how firmly something is believed stays.
- Name an outside source the way people will recognize it, rarely, and say in the document's own words what it contributes. Never give it the apparatus of a paper.
- Put content where that reader will look for it: the level and the section whose job it fits.
- Write only what stays true while it stands. No history, and no state that planned work is about to change; that belongs in the plan.
- A figure that could change while the reasons stay the same, such as a threshold, a limit or a size, goes in the operational document. The reasoning document says what it measures and why that matters.
- Name the things rather than count them. A count goes wrong when what it counts changes.
- Name the parties by the kind of text. A text the LLM acts from says "you" to the LLM, "I" for the human and "we" for both, and does not say "the human". A prompt that starts a subagent says "you" to the subagent and opens by saying that the human and the LLM agreed its task. A reasoning document says "the LLM" and "the human", and "we" for what both do. A reasoning or operational document says "practitioner" where it speaks of the person in relation to RFM or a project. An operational document gives its instructions as imperatives to whoever carries them out. Where it speaks about the two parties, it names the human "the human" and says "we" for what both do. "Session" names the conversation and its context and is never the one acting.
- Set neither party above the other: say what both did, such as agreed, settled or worked out, not that one approved or judged the other's work.

An operational document is written the same way. It gives the what, and leaves the why to its reasoning document.

## Each section's job

**The Problem.** The gap that justifies the work, named as a gap, not as a project, with no solution language. It changes when the gap changes.

**The Assumptions.** A belief the direction depends on, kept only if its being false would change the direction. Each states the condition under which it breaks. Not implementation detail. An assumption stays while the direction depends on it and it has not broken. When it breaks, the direction that rested on it is reopened.

**The Landscape.** What already exists and why each approach falls short for this problem. It distinguishes and does not choose. A row stays while someone hearing the problem would still reach for it, so the Landscape is seldom cut.

**The Options Considered.** Solutions to this Problem that were tried, or worked through seriously enough that the reasons they lost took real work to find, each with the failure that ruled it out. Not design choices made in passing, not alternatives dismissed in a sentence. Empty when there were none. An option stays while someone might try it again and the reason it lost still holds.

**The Chosen Direction and Why.** Why this direction over the others. No how, no restated option. When the direction is replaced, the old one moves to the Options Considered if someone might reach for it again. Otherwise it goes.

**The Boundaries.** What the work does not cover. Not a constraint on decisions, not space nobody has designed yet. A boundary stays while it still marks what the work does not cover.

**The Open Questions.** Unknowns whose answer would change the reasoning. A deferred decision belongs in the plan. A question stays while it is still unknown. One whose answer would change nothing goes.

**The Hard Lessons.** A failure that happened, can still happen and that nothing has fixed: what fails and why, not when it happened. A failure only foreseen is an assumption if the direction depends on it not happening, and an open question if nobody knows whether it happens. Where a change can fix the failure now, we make the change and write no lesson. A lesson stays while its failure can still happen.

## Filename and header

- Filename: `[project]_[subject]_reasoning.md` or `[project]_[subject]_operational.md`. Any other file drops the category: `[project]_[subject].md`. The prefix is the project's tag. A file whose name an app or a convention requires keeps that name.
- Header, on line 2 of every reasoning and operational document: `` `vX.Y.Z` // `type` // [living] ``. The type is a level (`top_level`, `module`) joined to a category (`reasoning`, `operational`), for example `module_reasoning`. Any other file carries no header; its form belongs to whatever uses it.

## The project's map

- Keep the map in its own file, `[project]_map.md`, with a tree that shows each document's parent.
- For a file that is neither a source nor a derivative, say in the map what the file is and that a change to it is made there.
- Refer to documents by filename, and keep filenames unique across the project.
- Group files into folders if that helps the project. The folders do not have to follow the tree.

## IDs

- Assumptions, Open Questions and Hard Lessons carry an ID: `AS-`, `OQ-` or `HL-`, then a word or two from the entry's content in capitals, such as `AS-ATTENTION`. Never a number.
- An ID is used only inside the document that declares it, and sparingly.
- When a retitle leaves the ID unreadable, change the ID and every use of it in the document.

## Section formats

- Problem: plain prose. A bold subheading only for a second argument that is structurally distinct.
- Assumptions: `**[AS-XXXX] -**` bold claim, body in the same paragraph, ending on the break condition. Hyphen after the ID.
- Landscape: one sentence naming the question it answers; a table, Approach | What it does | Why it's insufficient; a closing paragraph opened with **The gap:**.
- Options Considered: `**X**` bold title, a sentence on what the option was, then "Rejected because" and the failure. No IDs, no numbering.
- Chosen Direction: `**Why X**` or `**Why X over Y**` bold subheading, prose body. No IDs, no numbering.
- Boundaries: `**Not X.**` bold lead phrase, prose in the same paragraph. No IDs, no numbering.
- Open Questions: `**[OQ-XXXX] Title of the question.**` bold line, body as a separate paragraph.
- Hard Lessons: `**[HL-XXXX] Title.**` bold line. The first paragraph states the mechanism. A further paragraph only for a claim the first does not make.
- An empty section: `*No [section name] at this time.*` and nothing more.

---

*top level operational // [living]*
