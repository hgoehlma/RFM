# Reasoning-First Methodology: Derivation Prompt Reasoning Document
`v0.6.1` // `module_reasoning` // [living]

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

*No options considered at this time.*

---

## The Chosen Direction and Why

**Why the prompt is generic**

The derivation prompt activates behavior, not knowledge. What the LLM needs to know about the domain, the artifact, and the specific choices already made lives in the reasoning and operational documents. The prompt's job is to establish the posture from which the LLM reads those documents and executes from them. Mixing content into the prompt conflates two distinct layers and makes both harder to maintain.

**Why the derivative type is not specified in the prompt**

What is being derived, code, text, a presentation, a document, is domain and project specific. That belongs in the operational documents, not in a generic behavioral artifact. A prompt that specifies derivative type must be rewritten for every new context and is no longer generic.

**Why posture and behavior are the prompt's exclusive job**

The confirmation gate, gap-flagging, and the faithful rendering frame are what the prompt must establish. These behaviors cannot be sourced from the reasoning or operational documents at session start, they must be active before the LLM reads anything. Everything else follows from the documents. A prompt that tries to do more than establish posture and behavior conflates its role with the documents it is designed to activate.

**Why the prompt carries no domain knowledge or output specification**

A prompt that encodes domain knowledge or specifies output form is no longer generic. It must be rewritten for every new project and every new derivative type. The derivation prompt is intentionally minimal: posture and behavior only. Everything substantive comes from the reasoning and operational documents. What is not in those documents will not be built. That constraint is a feature, not a limitation, it enforces the discipline that the documents are the source.

---

## The Boundaries

**Not a substitute for domain knowledge.** The derivation prompt cannot compensate for a practitioner who has not done the reasoning work. If the reasoning and operational documents are thin because the domain was not understood well enough to specify it, the derivation session will surface that gap, not fill it.

**Not an output specification tool.** Exactly how a derivative looks, its layout, its visual design, its structural choices, is not the prompt's concern. Those decisions belong in the operational documents or are outside RFM's current ambition. The prompt establishes how the LLM behaves, not what the output looks like.

**Not a quality guarantee.** The derivation prompt ensures the right posture and behavior during the session. It does not guarantee the resulting derivative is good. A faithful derivative from a weak source is still a weak derivative. Quality is a function of the source documents, not of the prompt that governed the session.

---

## The Open Questions

**[OQ-DPAG] The derivation prompt in agentic settings.**

The Chosen Direction places mid-session drift monitoring with the human. In an agentic setup the human is not present during execution and only sees the result. Whether the derivation prompt as designed provides sufficient governance without a human monitor, or whether agentic derivation requires additional mechanisms, is an open question.

**[OQ-DPGV] Whether the confirmation gate reliably stabilizes derivation behavior.**

The confirmation gate is designed to anchor the LLM in the instruction-faithful regime before derivation begins. Whether a successful confirmation actually prevents drift toward prior-dominant behavior during the session, or whether regime shifts occur regardless, has not been empirically tested in RFM derivation sessions. The gate is the right design. Its reliability under real conditions remains unverified.

---

## Hard Lessons

*No hard lessons at this time.*

---

*module_reasoning // [living]*
*the derivation prompt is the derivative*
*this document is the source*
*the prompt follows the reasoning*
*that is the right order*
