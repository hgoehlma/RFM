# Reasoning-First Methodology — Guided Drafting Prompt Operational Document
`v0.0.0.3` // `operational` // [living]

---

## Artifacts this module produces

This module produces two derivative artifacts:

**The LLM prompt** (`RFM_guided_drafting_prompt.md`) — a behavioral specification the LLM reads at session start. It governs Socratic mode, the revision loop after the Landscape, and the co-author posture throughout the session. The newcomer reads it too — not as instruction to themselves, but as a description of how the session will work.

**The First Session Guidance** — a short document the newcomer reads immediately before starting. Its job is narrow: surface the one failure mode most likely to undermine the session, and give the newcomer a concrete move to counter it. It is not an introduction to RFM. It is not a summary of the human prompt. It is session-specific preparation.

The reasoning document produced in the session follows the formatting conventions specified in `RFM_operational.md`.

---

## Deployment

The LLM prompt is pasted as the opening message of a dedicated session — separate from any existing RFM authoring session. The traveling prompt governs the session's collaborative posture. The LLM prompt narrows the session's focus within that posture. It does not replace the traveling prompt.

The First Session Guidance is read by the newcomer before pasting the LLM prompt. The sequence is: read First Session Guidance → open a new session with the traveling prompt as system prompt → paste the LLM prompt as the opening message → begin.

---

## The failure mode the newcomer must hold

The session is longer and more cognitively demanding than a typical RFM session. The newcomer has not yet internalized the drift-correction practices from the human prompt. Under that combination, the LLM will drift from Socratic questioning toward producing answers — agreeable, elaborating, filling sections rather than drawing reasoning out. This is the primary failure mode of the guided drafting session.

The newcomer's counter-move: when responses feel like answers rather than questions, name it directly — "you are in tool mode, not co-author mode" — and ask the LLM to return to questions. At each section boundary, before moving forward, say explicitly: "hold your co-author role."

---

## Output delivery

The session produces a reasoning document section by section. After each section is confirmed by the newcomer, consolidate all drafted sections into a single clean markdown block and present it. Do not wait until session end — a session that breaks early should not cost the newcomer their work.

The markdown block is the artifact the newcomer saves. It is not a summary. It is the exact drafted text of each confirmed section, formatted as a reasoning document in progress.

---

## What this module does not yet have

The First Session Guidance document has not been drafted. It depends on [OQ-ONSQ] being sufficiently resolved to know what a willing newcomer needs to hold before their first session. Until that question has been tested in practice, the First Session Guidance remains a named but unproduced artifact.

---

*operational // [living]*
*carries what — the reasoning documents carry why*