# Reasoning-First Methodology: Derivation Session Guidance
`v0.1.1` // `derivation_session_guidance` // `[living]`

---

## Before you begin

You are about to run a phase two session. This is different from the co-authorship sessions you have been running until now.

In phase one, you and the LLM reason jointly. The LLM holds a co-author role: it challenges weak reasoning, surfaces alternatives, pushes back. That posture is correct for building reasoning documents. It is wrong for deriving from them.

In phase two, the reasoning is done. The decisions are made. The LLM's job is to render faithfully from the source documents: nothing more. A co-author posture actively interferes with that job: an LLM that surfaces alternatives or challenges closed decisions is not helping, it is drifting.

Before you open the derivation session, confirm two things:

**The source documents are complete.** The derivation prompt will run a confirmation gate. If the source documents have gaps, the gate will surface them and the session stops. Incomplete sources are a phase one problem. Resolve them before starting phase two.

**You know which derivative you are producing.** The operational document for that derivative specifies which source documents to load and what the output must establish. Read it before you open the session.

---

## The one step you must not skip

The traveling prompt establishes co-author behavior. The derivation prompt establishes faithful rendering behavior. Both cannot govern the same session reliably; the postures are structurally incompatible, and that conflict does not resolve by instruction alone inside the prompt artifact.

The suppression instruction must come from you, explicitly, in the human turn, before derivation begins.

Use this exact language:

> *Drop the co-author role for the duration of the derivation. Then read the derivation prompt. I would like you to create a fresh derivation of [name the derivative]. Read the required sources as described in the operational document.*

Do not look for a shortcut here. The suppression instruction is not baked into the derivation prompt. That choice is deliberate: a self-referential suppression instruction cannot cleanly override a co-author posture established at the same system level. The instruction must come from you.

---

## What to expect from the session

The LLM will run the confirmation gate before it begins. It will surface any gaps in the source documents one at a time. If a gap surfaces, the session stops: take the gap back to phase one, resolve it in the source documents, and return for a fresh gate.

Once the gate passes, the LLM derives without narration. It does not explain its choices. It does not summarize what it read. It produces the artifact.

If a gap surfaces mid-derivation that the gate did not catch, the LLM stops, names the gap precisely, and waits for your ruling. It does not fill the gap by inference. When this happens, take the gap back to phase one.

The LLM will not challenge decisions made in the source documents. If it does, name it:

*"You are in co-author mode. Return to faithful rendering."*

---

## When derivation is complete

The LLM runs a coverage check against the prior version of the derivative. It traces omissions and additions back to the source documents. One pass, one reconciliation: it does not loop.

The LLM will remind you to reactivate the traveling prompt before your next co-authorship session. Do not skip this step.

---

*derivation_session_guidance // [living]*
*phase two begins when the reasoning documents are complete*
*this document is the bridge between phases*
