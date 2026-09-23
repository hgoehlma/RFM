# Reasoning-First Methodology: Derivation Prompt Reasoning Document
`v0.8.0` // `module_reasoning` // [living]

---

## The Problem

RFM is built around two distinct phases. Phase one is collaborative: the human and the LLM reason jointly through a propose, reflect, converge, execute sequence to build the reasoning documents. The traveling prompt was designed for this phase, carrying methodology discipline into every co-authorship session. That design is correct for the phase it was designed for.

Phase two is different. The reasoning documents have been completed through collaboration, and the LLM now executes from them without the human present. No governing artifact exists for this session type. That is the gap this module addresses.

---

## The Assumptions

**[AS-DPCL] - Autonomous derivation is only reliable when the source documents are complete, clear, and unambiguous.** When the LLM can confirm it does not need to interpret or fill gaps to produce the derivative, derivation can proceed. When it cannot, the source requires further work before the session begins. This assumption breaks if reliable derivation turns out to be possible from incomplete or ambiguous source documents, for instance if an LLM could resolve genuine gaps correctly without inference risk. Nothing in current practice suggests this: the confirmation gate exists because unresolved gaps have consistently meant either invented content or a stalled session, not successful derivation.

**[AS-DPCP] - The traveling prompt and the derivation prompt establish incompatible behavioral postures.** The traveling prompt instates co-author judgment: hold genuine positions, challenge weak reasoning, surface alternatives. The derivation prompt requires faithful execution from the source documents. Both cannot govern the same session reliably because the behaviors they call for directly conflict. This assumption breaks if a single governing artifact could hold both postures reliably within one session, for example if instruction-following became precise enough to switch registers on command without drift. Nothing observed so far supports this. The suppression-and-separate-artifact design in `RFM_derivation_session_guidance.md` exists precisely because a same-level instruction cannot make the switch cleanly.

**[AS-DPSA] - When an instruction is ambiguous about scope, the LLM default is to proceed rather than confirm.** Scope ambiguity is not treated as a signal to pause; it is treated as a gap to fill by inference. This assumption breaks if the prompt explicitly establishes confirmation as the default response to ambiguity, which is precisely what the confirmation gate is designed to do.

**[AS-DPIF] - Instruction adherence in derivation sessions cannot be assumed.** LLMs do not apply instructions uniformly: the same prompt may produce faithful execution in one session and inference-driven deviation in another, depending on factors neither party can fully observe or control. A derivation prompt that correctly specifies the posture does not guarantee the posture holds throughout the session. The confirmation gate is the only mechanism that surfaces deviation before it produces an unfaithful derivative. This assumption breaks if instruction adherence becomes reliably predictable, for instance if a mechanism is found that guarantees a session holds its posture throughout rather than only surfacing deviation after it has already occurred. The confirmation gate reduces the risk; it does not eliminate the uncertainty this assumption describes.

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

**1. Rely on the operational documents to govern derivation**

Derivation procedures for specific artifacts already exist in operational documents: the constants, interfaces, and procedures a derivation session needs. Rejected because operational documents specify what to derive, not the behavioral posture during derivation. An LLM reading operational content with no governing prompt still defaults to inference when that content is ambiguous. The operational document and the prompt solve different problems.

---

## The Chosen Direction and Why

**Why the prompt is generic**

The derivation prompt activates behavior, not knowledge. What the LLM needs to know about the domain, the artifact, and the specific choices already made lives in the reasoning and operational documents. The prompt's job is to establish the posture from which the LLM reads those documents and executes from them. Mixing content into the prompt conflates two distinct layers and makes both harder to maintain.

**Why the derivative type is not specified in the prompt**

What is being derived, code, text, a presentation, a document, is domain and project specific. That belongs in the operational documents, not in a generic behavioral artifact. A prompt that specifies derivative type must be rewritten for every new context and is no longer generic.

**Why posture and behavior are the prompt's exclusive job**

The confirmation gate, gap-flagging, and the faithful rendering frame are what the prompt must establish. These behaviors cannot be sourced from the reasoning or operational documents at session start, they must be active before the LLM reads anything. Everything else follows from the documents. A prompt that tries to do more than establish posture and behavior conflates its role with the documents it is designed to activate.

**Why mid-session drift monitoring is the human's responsibility**

The derivation prompt establishes the posture at session start, through the confirmation gate. It cannot supervise the session as it runs. If the LLM drifts from that posture partway through, back toward inference or the co-author habits the traveling prompt trained, nothing internal to the prompt catches it. The LLM cannot reliably self-report a state it has already drifted out of. The human present during the session is the only party positioned to notice, so mid-session monitoring falls to them by elimination, not by design choice.

**Why the suppression instruction belongs in practitioner guidance, not the prompt**

The structural conflict named in [AS-DPCP] does not resolve by instruction alone inside the prompt artifact. A suppression instruction in the derivation prompt cannot cleanly override a co-author posture established at the same system level. What works is a practitioner ruling in the human turn before derivation begins. The design consequence is settled: the suppression instruction belongs in practitioner guidance, not baked into the derivation prompt. Repeated sessions confirm the approach holds without drift, observed across more than one LLM, Sonnet 5 and GPT-5.5, with no conflict seen between the derivation posture and the traveling prompt's reasoning habits in either.

**Why the prompt carries no domain knowledge or output specification**

The derivation prompt is intentionally minimal: posture and behavior only. Everything substantive comes from the reasoning and operational documents. What is not in those documents will not be built. That constraint is a feature, not a limitation, it enforces the discipline that the documents are the source.

**Why the derivation prompt optimizes for LLM activation with a verifiability floor**

The derivation prompt has one primary reader: the LLM executing from it. It does not need to read as friendly prose. Compression and directness that activate the right behavior reliably are what matter. One constraint applies regardless: the prompt must stay verifiable by the human maintaining it, parseable enough to confirm it still reflects the methodology, even if not fully readable as prose. The floor is verifiability, not readability.

**Why the confirmation gate appears at both the opening and closing of the prompt**

What governs whether an instruction still holds is not where it sits in the prompt, but how much has accumulated between the instruction being given and the moment it needs to apply. The gate at the opening establishes the posture before any source material is read, but a full derivation session can accumulate a great deal between that first read and the moment fidelity matters most: partway through producing the derivative. Restating the gate at the closing, as a standing check rather than a one-time question, keeps it close to the moment it's needed rather than relying on an instruction read once and never revisited.

**Why the coverage check follows derivation rather than preceding it**

Derivation is probabilistic: the same source can produce meaningfully different renderings depending on what the LLM attends to first. Reading the previous version of the artifact before deriving anchors the LLM on that version's own expression, narrowing the variance toward refining what already exists rather than reasoning fresh from source. Deriving clean first, with no prior version in view, uses that variance instead of suppressing it. The LLM reasons from the reasoning and operational documents alone. The coverage check that follows catches what that pass missed against the prior artifact.

**Why the coverage check after derivation is a traceability check, not a quality comparison**

The coverage check verifies that what the reasoning and operational documents require is actually present in the derivative. It does not ask whether the new derivative reads better than the version it replaces. Framing it as a quality comparison pulls the check toward the prior version's phrasing, structure, and emphasis, whether or not those choices were sound. That is the same failure that turns derivation into an unproductive loop, showing up earlier, at the check itself rather than after several rounds of comparison.

**Why derivation does not loop: one pass, one coverage check, one reconciliation**

Comparing repeated derivations against each other generates new variation each time, not convergence toward a better result. Reconciling successive derivations until the output "feels right" means the expression has settled, not that the prompt or the derivative improved. Each additional loop costs comparison effort and risks something worse: replacing instructions that reliably activate the right behavior with language that merely reads more cleanly and activates less reliably. The stopping condition is structural, not a feeling: the items the source requires are present, the structure reads cleaner than the previous version, and the content is shorter without losing substance. That condition is reachable in one derivation pass plus one reconciliation, which is why the process stops there.

**Why a second, conditional gate governs derivation of mode-distinct siblings**

The standard confirmation gate verifies fidelity to source. It does not verify fidelity to scope when the document being derived is one of two or more sibling derivatives whose source reasoning assigns each a deliberately distinct, mutually exclusive mode. A sentence can be faithfully sourced and still belong to a sibling's mode rather than the artifact being derived. The confirmation gate has no mechanism to catch this, because its questions ask whether content is grounded, not whether it is grounded in the right artifact.

This does not weaken the confirmation gate's binary character. The gate's questions are universal: every derivation answers them, no exceptions. A sibling-scope check is not universal in that sense, it only has content when siblings with assigned modes exist. Folding it into the same gate would either dilute the gate's binary clarity or apply a check with nothing to test against in the common case where no such siblings exist. The check is therefore sequential and conditional rather than parallel: it activates only after the confirmation gate passes, and only when mode-distinct siblings exist. The mechanics of how the check runs belong with the derivation prompt's procedural design, not here.

---

## The Boundaries

**Not a substitute for domain knowledge.** The derivation prompt cannot compensate for a practitioner who has not done the reasoning work. If the reasoning and operational documents are thin because the domain was not understood well enough to specify it, the derivation session will surface that gap, not fill it.

**Not an output specification tool.** Exactly how a derivative looks, its layout, its visual design, its structural choices, is not the prompt's concern. Those decisions belong in the operational documents or are outside RFM's current ambition. The prompt establishes how the LLM behaves, not what the output looks like.

**Not a quality guarantee.** The derivation prompt ensures the right posture and behavior during the session. It does not guarantee the resulting derivative is good. A faithful derivative from a weak source is still a weak derivative. Quality is a function of the source documents, not of the prompt that governed the session.

---

## The Open Questions

**[OQ-DPAG] The derivation prompt in agentic settings.**

The Chosen Direction places mid-session drift monitoring with the human. In an agentic setup the human is not present during execution and only sees the result. Whether the derivation prompt as designed provides sufficient governance without a human monitor, or whether agentic derivation requires additional mechanisms, is an open question.

**[OQ-DPTP] Whether the practitioner-ruling approach generalizes beyond the LLMs and conditions it has been observed on.**

The observation behind the Chosen Direction is the practitioner's own, across repeated use, not systematic testing: it has not been checked across a broader model set, under adversarial conditions, or by anyone other than the practitioner who designed the approach. Whether it holds that way more generally remains open.

**[OQ-DPGV] Whether the confirmation gate reliably stabilizes derivation behavior.**

The confirmation gate is designed to anchor the LLM in the instruction-faithful regime before derivation begins. Whether a successful confirmation actually prevents drift toward prior-dominant behavior during the session, or whether regime shifts occur regardless, has not been empirically tested in RFM derivation sessions. Its reliability under real conditions remains unverified.

**[OQ-DPSC] Whether the sequential sibling-scope gate reliably catches mode contamination in practice.**

The gate is designed to activate after the confirmation gate passes, and only when mode-distinct sibling derivatives exist. Its design follows directly from the contamination it was created to catch. Whether it actually catches that contamination reliably, across repeated derivation sessions and across different sibling sets, has not been tested. The original confirmation gate carries the same open question in `[OQ-DPGV]`, earned through actual use across multiple sessions. The sibling-scope gate carries it from design alone, with no use yet behind it.

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
