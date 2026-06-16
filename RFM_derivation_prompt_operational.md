# Reasoning-First Methodology: Derivation Prompt Operational Document
`v0.2.6` // `operational` // [living]

---

## What this module produces

This module produces one derivative artifact:

**The derivation prompt** (`RFM_derivation_prompt.md`): the system prompt that governs autonomous LLM execution from completed RFM reasoning documents. It establishes the behavioral posture for phase two sessions: faithful rendering from source, gap-flagging rather than gap-filling, and a confirmation gate before derivation begins. It does not travel with the practitioner across all sessions; it is invoked only when a specific derivative is ready to be produced from complete source documents.

---

## Derivation procedure

**Source documents, load all three before drafting:**

1. `RFM_prompts_reasoning.md`: the reasoning governing the prompt system architecture
2. `RFM_derivation_prompt_reasoning.md`: the reasoning governing derivation prompt design decisions specifically
3. `RFM_derivation_prompt_operational.md`: the operational specification for what the prompt must produce and how

**Instruction to the LLM for the derivation session:**

---

You are being asked to derive the derivation prompt for the Reasoning-First Methodology (RFM). This is a de novo derivation. Read the source reasoning documents provided and produce the optimal derivation prompt from them directly.

Do not ask for examples of what the prompt should look like. Do not ask for the current version. Derive from the reasoning alone.

The derivation prompt has one primary reader: the LLM that will execute from it. Write for behavioral activation, not human readability. Language, structure, and phrasing should be chosen for reliable activation of the confirmation gate posture and faithful rendering behavior.

The floor is verifiability: the prompt must remain structured enough that a human can confirm coverage against the source documents is intact and no load-bearing behavioral instructions have drifted. Opacity that makes this coverage check unexecutable is the constraint boundary.

The confirmation gate must open the prompt. It must be active before the LLM reads anything. It cannot be sourced from the reasoning documents at session start. Structure the prompt accordingly: gate first, everything else after.

Do not explain your derivation. Do not summarize what you read. Produce the artifact.

The prompt must include a version header in the format: `vX.X.X` // `derivation_prompt` // `[living]`

---

## Coverage check after derivation

Once the derivation is complete, compare against the previous version of the derivative. If no prior version exists, skip this step. The derivation is accepted if it is structurally better or equivalent. If the prior version carried something the fresh derivation omitted, that item must trace back to the source documents: if it traces and belongs, add it; if the source changed and the omission reflects that change, the omission is correct. If an item neither traces nor reflects a source change, flag it as a source document gap and return to phase one. The prior version is never the authority. The source documents are.

Do not loop the derivation. One pass, one coverage check, one reconciliation. See `[HL-PDLR]` in `RFM_prompts_reasoning.md`.

---

## What the derivation prompt must establish

The prompt governs a session in which the traveling prompt has been suppressed. It must establish the following behaviors before the LLM reads anything else.

**The confirmation gate.** Before derivation begins, the LLM runs an active confirmation exchange. It surfaces gaps and ambiguities one at a time: specific named unknowns it cannot resolve from the source documents without interpreting or inferring. There is no partial pass. Any gap stops the session. The practitioner takes all gaps back to phase one, resolves them in the source documents, and returns for a fresh gate. The gate passes only when the LLM confirms it can produce the derivative faithfully from the source documents as they stand.

**Faithful rendering.** The LLM derives from the source documents only. If a gap surfaces mid-derivation that was not caught at the gate, the LLM stops, names the gap precisely, and waits for ruling. It does not fill the gap by inference. It does not continue past it.

**Version discipline.** Derivatives produced in a phase two session carry no version markers. They are outputs intended for their audience. The absence of a version marker is intentional and must not be flagged.

**Traveling prompt reactivation.** Suppression is session-scoped. The prompt must remind the practitioner to reactivate the traveling prompt before the next co-authorship session begins.

---

*operational // [living]*
*carries what; the reasoning documents carry why*
