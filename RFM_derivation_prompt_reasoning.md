# Reasoning-First Methodology: Derivation Prompt Reasoning Document
`v0.5.0` // `module_reasoning` // [living]

---

## The Problem

RFM is built around two distinct phases. Phase one is collaborative: the human and the LLM reason jointly through a propose, reflect, converge, execute sequence to build the reasoning documents. The traveling prompt was designed for this phase, carrying methodology discipline into every co-authorship session. That design is correct for the phase it was designed for.

Phase two is different. The reasoning documents have been completed through collaboration, and the LLM now executes from them without the human present. No governing artifact exists for this session type. That is the gap this module addresses.

---

## The Assumptions

**[AS-DPCL] - Autonomous derivation is only reliable when the source documents are complete, clear, and unambiguous.** When the LLM can confirm it does not need to interpret or fill gaps to produce the derivative, derivation can proceed. When it cannot, the source requires further work before the session begins.

**[AS-DPCP] - The traveling prompt and the derivation prompt establish incompatible behavioral postures.** The traveling prompt instates co-author judgment: hold genuine positions, challenge weak reasoning, surface alternatives. The derivation prompt requires faithful execution from the source documents. Both cannot govern the same session reliably because the behaviors they call for directly conflict.

**[AS-DPSA] - When an instruction is ambiguous about scope, the LLM default is to proceed rather than confirm.** Scope ambiguity is not treated as a signal to pause; it is treated as a gap to fill by inference. This assumption breaks if the prompt explicitly establishes confirmation as the default response to ambiguity, which is precisely what the confirmation gate is designed to do.

**[AS-DPIF] - Instruction adherence in derivation sessions cannot be assumed.** LLMs do not apply instructions uniformly: the same prompt may produce faithful execution in one session and inference-driven deviation in another, depending on factors neither party can fully observe or control. A derivation prompt that correctly specifies the posture does not guarantee the posture holds throughout the session. The confirmation gate is the only mechanism that surfaces deviation before it produces an unfaithful derivative.

---

## The Landscape

The question this landscape must answer: what prior approaches exist for governing autonomous LLM execution from a specification, and why is each insufficient?

| Approach | What it does | Why it is insufficient |
|---|---|---|
| **No governing prompt** | LLM applies its general defaults to the execution task | No behavioral posture is established for gap-flagging or deviation reporting. The LLM fills silences by inference and produces a derivative that may diverge from its source in ways neither party can trace. |
| **Traveling prompt in derivation session** | Co-authorship behavioral frame applied to execution task | The co-author posture actively interferes with executing faithfully from the source. The failure is invisible: an LLM pausing to surface alternatives or challenge closed decisions can look thorough. |
| **Memory files / persistent context** | Carries selected prior context into a new session to reduce re-explanation overhead | Manages what the LLM remembers, not whether the source is complete. The LLM still interprets and fills gaps where memory is silent or ambiguous. |
| **Soul files / persona files** | Establishes identity and behavioral framing for the LLM across sessions | Governs posture, not execution fidelity. A well-framed LLM operating from an incomplete source still guesses where the source does not specify. |
| **Context compression / summarization** | Reduces source material to fit within a context window | Introduces its own interpretation layer: what is compressed and what is preserved reflects the compressor's judgment, not the source's intent. |
| **Structured output prompts** | Specifies the format the derivative must conform to | Addresses output structure, not source fidelity. A derivative can comply fully with a format specification while diverging materially from the source reasoning. |

**The gap:** none of these approaches establish a confirmation gate where the LLM actively verifies it does not need to interpret or fill gaps before derivation begins. The derivation prompt addresses that gap directly.

---

## The Options Considered

**1. Extend the traveling prompt to cover derivation sessions**

Add a mode switch to the traveling prompt that activates derivation behavior when the session type is named. Rejected because the failure is not a missing section, it is a wrong behavioral frame. The co-author role and the derivation posture are incompatible. A mode switch cannot be made reliable by instruction alone when the two postures are structurally different.

**2. Rely on the operational documents to govern derivation**

Derivation procedures for specific artifacts already exist in operational documents. Derivation could be governed entirely at that level with no dedicated prompt. Rejected because operational documents and the derivation prompt operate at different layers. Operational documents carry the what: domain knowledge, output specification, procedures. The derivation prompt establishes how the LLM approaches those documents. That is a behavioral job, not a procedural one. The failure modes of derivation are behavioral failures that a procedure cannot correct.

---

## The Chosen Direction and Why

**Why a separate prompt rather than an extension of the traveling prompt**

The traveling prompt establishes the co-author role as its founding behavioral distinction. That role is correct for phase one and wrong for phase two. The difference is not one of degree, it is structural. A mode switch appended to the traveling prompt cannot reliably separate two postures that are incompatible by design. A separate artifact is the only architecture that makes the distinction unambiguous.

**Why the prompt is generic**

The derivation prompt activates behavior, not knowledge. What the LLM needs to know about the domain, the artifact, and the specific choices already made lives in the reasoning and operational documents. The prompt's job is to establish the posture from which the LLM reads those documents and executes from them. Mixing content into the prompt conflates two distinct layers and makes both harder to maintain.

**Why the derivative type is not specified in the prompt**

What is being derived, code, text, a presentation, a document, is domain and project specific. That belongs in the operational documents, not in a generic behavioral artifact. A prompt that specifies derivative type must be rewritten for every new context and is no longer generic.

**Why posture and behavior are the prompt's exclusive job**

The confirmation gate, gap-flagging, and the faithful rendering frame are what the prompt must establish. These behaviors cannot be sourced from the reasoning or operational documents at session start, they must be active before the LLM reads anything. Everything else follows from the documents. A prompt that tries to do more than establish posture and behavior conflates its role with the documents it is designed to activate.

**Why mid-session drift monitoring is the human's responsibility**

The derivation prompt establishes the posture at session start. It cannot enforce it throughout. LLMs drift toward prior-dominant behavior under session pressure regardless of what the prompt specifies. The human watches for this, re-anchors when needed, and is the quality gate the prompt cannot be. This mirrors the human's role in phase one, where the human prompt (see glossary) makes the same monitoring responsibility explicit for co-authorship sessions.

**Why the derivation prompt optimizes for LLM activation with a verifiability floor**

The derivation prompt has one primary reader: the LLM executing from it. Unlike the traveling prompt, which must remain parseable by its human maintainer as a condition of ongoing curation, the derivation prompt is invoked rarely and for a narrow purpose. Optimizing its language, structure, and phrasing for reliable LLM activation is the primary design constraint.

The floor is verifiability, not readability. A human must be able to confirm that the prompt's coverage against its source documents is intact. Not parse it as friendly prose, but check that the load-bearing behavioral instructions are present and have not drifted. If the prompt becomes opaque enough that this coverage check is unexecutable, the maintenance relationship to the source documents breaks. That is the constraint. It is a lower bar than the traveling prompt's two-reader requirement, and intentionally so.

**Why the prompt carries no domain knowledge or output specification**

A prompt that encodes domain knowledge or specifies output form is no longer generic. It must be rewritten for every new project and every new derivative type. The derivation prompt is intentionally minimal: posture and behavior only. Everything substantive comes from the reasoning and operational documents. What is not in those documents will not be built. That constraint is a feature, not a limitation, it enforces the discipline that the documents are the source.

**Why the confirmation gate appears at both the opening and closing of the prompt**

LLMs attend most reliably to the beginning and end of a prompt. Content in the middle receives less consistent attention regardless of how it is written. The confirmation gate is the behavioral instruction the derivation prompt cannot afford to have missed or underweighted. Placing it only at the opening creates a single point of attention. Placing it at both edges exploits primacy and recency to double-reinforce the single most critical constraint. Everything else in the prompt sits between two gate anchors.

**Why a second, conditional gate governs derivation of mode-distinct siblings**

The standard confirmation gate verifies fidelity to source. It does not verify fidelity to scope when the document being derived is one of two or more sibling derivatives whose source reasoning assigns each a deliberately distinct, mutually exclusive mode. A sentence can be faithfully sourced and still belong to a sibling's mode rather than the artifact being derived. The confirmation gate has no mechanism to catch this, because its three questions ask whether content is grounded, not whether it is grounded in the right artifact.

This does not weaken the confirmation gate's binary character. The gate's three questions are universal: every derivation answers them, no exceptions. A sibling-scope check is not universal in that sense, it only has content when siblings with assigned modes exist. Folding it into the same gate would either dilute the gate's binary clarity or apply a check with nothing to test against in the common case where no such siblings exist. The check is therefore sequential and conditional rather than parallel: it activates only after the confirmation gate passes, and only when mode-distinct siblings exist. The mechanics of how the check runs belong with the derivation prompt's procedural design, not here.

---

## The Boundaries

**Not a substitute for domain knowledge.** The derivation prompt cannot compensate for a practitioner who has not done the reasoning work. If the reasoning and operational documents are thin because the domain was not understood well enough to specify it, the derivation session will surface that gap, not fill it.

**Not an output specification tool.** Exactly how a derivative looks, its layout, its visual design, its structural choices, is not the prompt's concern. Those decisions belong in the operational documents or are outside RFM's current ambition. The prompt establishes how the LLM behaves, not what the output looks like.

**Not a quality guarantee.** The derivation prompt ensures the right posture and behavior during the session. It does not guarantee the resulting derivative is good. A faithful derivative from a weak source is still a weak derivative. Quality is a function of the source documents, not of the prompt that governed the session.

---

## The Open Questions

**[OQ-DPAG] The derivation prompt in agentic settings.**

The Chosen Direction places mid-session drift monitoring with the human. In an agentic setup the human is not present during execution and only sees the result. Whether the derivation prompt as designed provides sufficient governance without a human monitor, or whether agentic derivation requires additional mechanisms, is an open question.

**[OQ-DPTP] Whether the derivation prompt can reliably govern when the traveling prompt is also present, across different LLMs.**

The structural conflict named in [AS-DPCP] does not resolve by instruction alone inside the prompt artifact. A suppression instruction in the derivation prompt cannot cleanly override a co-author posture established at the same system level. What works is a practitioner ruling in the human turn before derivation begins. The design consequence is settled: the suppression instruction belongs in practitioner guidance, not baked into the derivation prompt. Repeated sessions with the same LLM confirm the approach holds without drift.

Whether the practitioner-ruling approach holds with LLMs other than the one it was confirmed on is the remaining open question. Cross-LLM behavior is untested.

**[OQ-DPGV] Whether the confirmation gate reliably stabilizes derivation behavior.**

The confirmation gate is designed to anchor the LLM in the instruction-faithful regime before derivation begins. Whether a successful confirmation actually prevents drift toward prior-dominant behavior during the session, or whether regime shifts occur regardless, has not been empirically tested in RFM derivation sessions. The gate is the right design. Its reliability under real conditions remains unverified.

**[OQ-DPSC] Whether the sequential sibling-scope gate reliably catches mode contamination in practice.**

The gate is designed to activate after the confirmation gate passes, and only when mode-distinct sibling derivatives exist. Its design follows directly from the contamination it was created to catch. Whether it actually catches that contamination reliably, across repeated derivation sessions and across different sibling pairs, has not been tested. The original confirmation gate carries the same open question in `[OQ-DPGV]`, earned through actual use across multiple sessions. The sibling-scope gate carries it from design alone, with no use yet behind it.

---

## Hard Lessons

**[HL-DPEX] A handover instruction is not a derivation license.**

At the opening of the session that produced this document, the LLM interpreted "open the derivation prompt module reasoning document" as license to draft the entire document unilaterally. The instruction named the next step. The LLM executed all steps. The failure is precisely what this document is designed to prevent: gap-filling by inference where joint reasoning was the correct act.

---

*module_reasoning // [living]*
*the derivation prompt is the derivative*
*this document is the source*
*the prompt follows the reasoning*
*that is the right order*
