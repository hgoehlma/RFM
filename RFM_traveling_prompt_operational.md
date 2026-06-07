# Reasoning-First Methodology — Traveling Prompt Operational Document
`v0.1.0` // `operational` // [living]

---

## What this module produces

This module produces one derivative artifact:

**The traveling prompt** (`RFM_traveling_prompt.md`) — the system prompt that carries RFM discipline into every LLM conversation. It activates ambient co-author behavior. It is not a concentrated review instrument. It travels with the practitioner across all projects where RFM is applied.

---

## Derivation procedure

The traveling prompt is derived from its source reasoning documents in a dedicated session. The session must be clean — no existing version of the traveling prompt in context. Derivation anchors on the reasoning, not on prior expression.

**Source documents — load all three before drafting:**

1. `RFM_top_level_reasoning.md` — the methodology itself
2. `RFM_prompts_reasoning.md` — the reasoning governing the prompt system architecture
3. `RFM_traveling_prompt_reasoning.md` — the reasoning governing traveling prompt design decisions specifically

**Instruction to the LLM for the derivation session:**

---

You are being asked to derive the traveling system prompt for the Reasoning-First Methodology (RFM). This is a de novo derivation — read the source reasoning documents provided and produce the optimal traveling prompt from them directly.

Do not ask for examples of what the prompt should look like. Do not ask for the current version. Derive from the reasoning alone.

The traveling prompt has two readers with different needs:

- The LLM that executes it: needs directness and precision. Reassurance, redundant clauses, and backward-glance summaries consume tokens without adding behavior. Remove them.
- The human maintainer who audits it: must be able to confirm the prompt still reflects the methodology. Not as friendly prose — well enough to verify coverage.

Both constraints are non-negotiable. When a clause exists to reassure rather than instruct, remove it. When in doubt between length and completeness, preserve — do not drop content to optimize for length.

Do not explain your derivation. Do not summarize what you read. Produce the artifact.

The prompt must include a version header in the format: `vX.X.X` // `traveling_prompt` // `[living]`

---

## Coverage check — after derivation

Once the derivation is complete, compare against the previous version of the traveling prompt. The derivation is accepted if it is structurally better or equivalent and loses no load-bearing behavioral instructions. If the previous version carried something the derivation missed, assess whether it was present in the source reasoning documents. If yes: the derivation missed it — add it to the derived version. If no: the previous version carried reasoning its source did not hold — that is a source document gap requiring a reasoning document addition before the next derivation cycle.

Do not loop the derivation. One pass, one coverage check, one reconciliation. See `[HL-PDLR]` in `RFM_prompts_reasoning.md`.

---

## Version discipline

The version number is assigned by the human at acceptance, not by the derivation session. A clean re-derivation that improves on the previous version increments the minor digit. A patch-level fix to an accepted version increments the patch digit. The header of `RFM_traveling_prompt.md` is the single source of version truth.

---

*operational // [living]*
*carries what — the reasoning documents carry why*
