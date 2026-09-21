# Reasoning-First Methodology: Traveling Prompt Operational Document
`v0.3.1` // `module_operational` // [living]

---

## What this module produces

This module produces one derivative artifact:

**The traveling prompt** (`RFM_traveling_prompt.md`) is the system prompt that carries RFM discipline into every LLM conversation. It activates ambient co-author behavior. It is not a concentrated review instrument. It travels with the practitioner across all projects where RFM is applied.

---

## Independent derivation

Occasionally, a dedicated session derives the prompt from the reasoning documents alone, with no existing version in context. The result is compared with the current prompt. A sentence in the current prompt that the derivation lacks must trace to the reasoning documents. If it does not, the reasoning documents get an addition. A sentence the derivation has and the prompt lacks is either a gap in the prompt or reasoning that belongs to a different carrier. One pass, one comparison, one reconciliation.

**Load this document's sources before drafting.** They are its branch of the hierarchy in `RFM_map.md`, read upward.

**Instruction to the LLM for the derivation session:**

---

You are being asked to derive the traveling system prompt for the Reasoning-First Methodology (RFM). This is a de novo derivation: read the source reasoning documents provided and produce the optimal traveling prompt from them directly.

Do not ask for examples of what the prompt should look like. Do not ask for the current version. Derive from the reasoning alone.

The traveling prompt has two readers with different needs:

- The LLM that executes it: needs directness and precision. Reassurance, redundant clauses, and backward-glance summaries consume tokens without adding behavior. Remove them.
- The human maintainer who audits it: must be able to confirm the prompt still reflects the methodology. Not as friendly prose, but well enough to verify coverage.

Both constraints are non-negotiable. When a clause exists to reassure rather than instruct, remove it. When in doubt between length and completeness, preserve; do not drop content to optimize for length.

Do not explain your derivation. Do not summarize what you read. Produce the artifact.

The prompt must include a version header in the format: `vX.X.X` // `module_artifact` // `[living]`

---

## Checks after a change

Run each of these after any change to the prompt. The reader check uses a session with no other context.

Trace both ways. Every sentence of the prompt traces to reasoning in its reasoning document or the documents above it, and every piece of reasoning the prompt should carry traces to a sentence. A sentence with no reasoning is cut, or its reasoning is written first. Reasoning with no sentence is a gap in the prompt or belongs to a different carrier.

Reader check. Give the prompt alone to a reader with no other context. Have it list every phrase it would have to guess and what it takes each phrase to mean. Define in plain words, or reword, any phrase it cannot decode or reads differently from what is intended.

---

## Version discipline

The version number is assigned by the human at acceptance, not by the derivation session. A change to what the prompt asks increments the minor digit. A patch-level fix to an accepted version increments the patch digit. The header of `RFM_traveling_prompt.md` is the single source of version truth.

---

*operational // [living]*
*carries what; the reasoning documents carry why*
