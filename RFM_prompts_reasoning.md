# Reasoning-First: System Prompt(s) Reasoning Document
`v0.7.0` // `module_reasoning` // [living]

---

## The Problem

A prompt that keeps the discipline present while work happens still misses things: reasoning compression slips through under delivery pressure, session-born shorthand passes the moment an insight is written down untested, and versions drift across edits. Nothing in that prompt can notice what it missed, so those failures stay in the documents until they have already done damage. The same gap exists on the human side: a prompt that shapes only the LLM's posture leaves the human's practice to chance, and the discipline then holds on one side of the collaboration only.

---

## The Assumptions

**[AS-TPCJ] - The traveling prompt creates judgment, not compliance.** A traveling prompt that issues hard rules produces an LLM that follows rules. A traveling prompt that establishes guiding principles produces an LLM that can reason about novel situations the rules didn't anticipate. The methodology operates in a domain of genuine complexity; the traveling prompt must equip the LLM to navigate that complexity, not just execute a checklist.

**[AS-LLCR] - The LLM holds the co-author role, not the tool role.** The prompt system must reflect this across all prompt artifacts. An LLM that understands itself as executing within the methodology will behave differently from one that understands itself as co-creating it. The latter is what the methodology requires and what the collaboration has demonstrated is possible.

**[AS-PADC] - All prompt artifacts are subject to the methodology's principles.** They are living artifacts. Drift in the traveling prompt degrades prevention. Drift in a sweep prompt degrades correction silently: the artifact runs but catches less. Drift in the human prompt leaves the human collaborator's posture uncalibrated. All require curation as the methodology evolves, as new hard lessons are earned, and as practice in new domains reveals things the initial design did not anticipate.

**[AS-PVCR] - Preventing failures and correcting them are different kinds of work, and one artifact cannot do both without doing both badly.** Prevention works in the background of ordinary work, as the traveling prompt does, and must not feel like a review the human is sitting through. Correction is invoked deliberately and reads a stable draft closely, as the sweep prompts do, and must not read like background guidance. An artifact that tries both produces neither well. Correction also needs a separate invocation for a second reason: an LLM cannot reliably correct its own output inside the session that produced it, because it stays anchored to the context that produced the error. The belief would fail if one artifact could hold both the background discipline and the deliberate review without either degrading.

**[AS-PSGZ] - The prompt system cannot resolve grey zones; it can only name them.** The prompt system should instruct the LLM to flag grey zones explicitly, describe the tension, and require a conscious human decision. Attempting to resolve grey zones with rules produces false precision.

**[AS-PSHE] - The prompt system must be honest about what it cannot enforce.** Some principles require human discipline to work: the prompt system can nudge, flag, and remind, but it cannot force a human to capture while sharp, invoke a sweep deliberately, or return to reasoning posture after delivery pressure lifts. The artifacts should be clear about where their authority ends and human discipline begins.

**[AS-SWTD] - The sweep prompts have a timing dependency the traveling prompt does not.** The traveling prompt runs in any conversation regardless of document state. The structural sweep requires a coherent draft to work against, coherent meaning the section sequence has been honored, not merely that content is present. Invoked earlier, it produces noise rather than signal. The language sweep can run on partial drafts but requires content to exist. Timing is a design constraint, not an implementation detail: it belongs in the sweep prompt design and must be carried explicitly in the prompts themselves.

---

## The Landscape

The question this landscape must answer is not "how should a system prompt be designed?"; that is a narrower question appropriate to the traveling prompt alone. The question is: what approaches exist for coordinated prevention and correction in collaborative AI-assisted practice? The landscape divides into two groups accordingly.

**Prevention approaches: what keeps failures from entering**

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **No system prompt** | LLM defaults to general helpful behavior | Methodology discipline must be re-established in every conversation. Drift goes undetected. Summarization happens silently. |
| **Hard rules only** | Explicit prohibitions and requirements | Brittle. Creates compliance without understanding. Fails on novel situations. LLM follows the letter, misses the spirit. |
| **Document reference only** | Point the LLM at the methodology document at the start of each conversation | Better than nothing, but requires explicit setup every time. The LLM reads the document but doesn't internalize the principles. Discipline is still effortful. |
| **Single monolithic prompt** | One prompt covering all methodology interactions | Conflates the traveling prompt's always-on prevention with the sweeps' deliberate review. The LLM cannot do both jobs at once without degrading both. |
| **Model specifications and Constitutional AI** | Guiding principles embedded in the prompt that create judgment rather than a list of prohibitions: Anthropic's model spec and OpenAI's model spec (2025) are the primary examples | Closest to the right prevention approach. Establishes values an LLM can apply to novel situations. Still preventive only; no corrective mechanism. Empirical audits show models violate their own specifications under pressure; prevention alone is insufficient. |
| **Context engineering** | Curating what fills the context window at each step: managing information architecture across an entire session, not just phrasing a prompt | Addresses the right level of abstraction for multi-turn, agentic practice. Treats the reasoning document as information to be managed, not just a reference. Still a prevention discipline: it improves what goes in, but has no corrective pass for what slips through. |

**Correction approaches: what catches failures that prevention missed**

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **LLM self-correction (inline)** | The same LLM reviews and revises its own output within the same session | Empirically unreliable without external feedback. LLMs anchor on their initial outputs and cannot reliably detect their own reasoning failures from inside the same context. Not a correction mechanism; a recirculation mechanism. |
| **LLM-as-judge** | A second LLM evaluates the output of the first against a rubric or criteria | Adds genuine independence. Widely adopted for output quality evaluation in production systems. Typically automated, criteria-driven, and output-focused, not designed for reasoning document integrity, structural hierarchy, or the distinction between language failures and architecture failures. |
| **Multi-agent review** | Multiple LLM agents critique each other's outputs, simulating peer review | Improves reasoning quality on discrete tasks. Adds independence across agents. Not designed for living documents curated over time: the review is of an output, not of a reasoning artifact with a history, hierarchy, and derivative chain. |
| **Human review cycles** | Periodic human inspection of documents or outputs for quality | Essential but cognitively expensive and not scalable as the document landscape grows. Without a structured protocol, human review catches what is salient, not what has drifted gradually. Random sampling dilutes signal; structured sampling requires the protocol the sweep prompt is designed to provide. |

**The gap:** no existing approach combines always-on prevention with a separately invoked corrective pass, designed specifically for the structural and linguistic fidelity of reasoning documents across a living hierarchy. Prevention approaches share a common failure: they have no mechanism for detecting what prevention missed. Correction approaches share a different failure: they are designed for discrete output evaluation, not for the structural and linguistic integrity of reasoning artifacts maintained over time. The sweep prompts are the corrective arm that the landscape does not contain.

---

## The Options Considered

**1. Hard rules with no guiding principles**

Explicit prohibitions: never summarize, always flag, always verify. Faster to write, easier to test compliance. Rejected because the methodology operates in a domain of genuine complexity and ambiguity. Hard rules fail on grey zones. An LLM that understands why surgical edits matter will handle novel situations better than one that follows a rule it doesn't understand.

**2. Guiding principles with no behavioral instructions**

Pure philosophy: here is what the methodology values, here is why. No specific behavioral instructions. Rejected because some principles require specific behavioral expressions to be actionable. "Capture while sharp" is a value. "When an insight appears, capture it immediately before continuing" is the behavior that expresses it. Both are needed.

**3. System prompt derived without a reasoning document**

Write the prompt directly from accumulated observations and the methodology hard lessons. Faster. Rejected because this would violate the methodology's own founding principle: reasoning before execution. The system prompt is a significant design decision with real consequences. It deserves a reasoning document. The prompt is the derivative. This document is the source.

**4. One sweep prompt covering both failure classes**

A single sweep prompt targeting both structural failures (wrong hierarchy level, module strain, open questions ready to graduate) and language failures (session residue, insider shorthand, disambiguation gaps). Simpler to maintain and invoke. Rejected because a single prompt covering both failure classes does shallow work on both. Two prompts, one per class, is the design that follows.

**5. Sweep as a switch inside the traveling prompt**

Rather than a separate artifact, the traveling prompt could be switched into review on request. Rejected because the LLM cannot tell background guidance from deliberate critique inside one artifact, so it does neither cleanly. The review has to be a separate invocation.

**6. Automated continuous sweep**

Sweep running as a background discipline: triggered automatically at intervals or after every edit, not invoked deliberately by the human. Rejected because an automatic trigger cannot know whether the draft is ready to be checked, and a sweep on an unready draft produces noise. Deliberate invocation is not a limitation: the human's choice of moment is the control that makes the sweep meaningful rather than mechanical.

---

## The Chosen Direction and Why

A system of prompt artifacts, each with a reasoning document as its foundation, each designed for its specific job.

**Why guiding principles over hard rules**

Design from failure modes, not from aspiration. The failure mode of hard rules is an LLM that complies without understanding and fails on novel situations. The failure mode of guiding principles is an LLM that understands but occasionally applies judgment differently than expected. The latter is recoverable. The former produces confident wrong behavior at scale.

**Why the co-author role matters**

An LLM that understands itself as a tool executing within the methodology will wait to be asked before contributing. An LLM that understands itself as a co-author will notice when something is off and say so without waiting. The red team function, the drift detection, the strain flagging: none of these work if the LLM is waiting for permission. The system prompt must make the co-author role explicit and mean it.

The joint reasoning sequence expresses this role in practice: propose → reflect → converge → execute. Both parties contribute to the proposal; either may surface a direction or propose a draft. Both reflect on it, testing it against the reasoning and each other's instincts. Both converge on a direction through explicit alignment. Execution then follows, carried by whoever is best positioned, most often the LLM formulating and editing, the human judging and confirming. That division of labor is one expression of the sequence at the execution step. It is not a description of the whole. Neither party defers the step they are best equipped to carry.

**Why a change to a prompt artifact requires a change to its reasoning document**

Every change to a derivative requires a corresponding change to its source reasoning document. This is the methodology's founding principle applied to itself. If any prompt artifact changes, something in its reasoning either changed or was insufficiently expressed; both cases require a reasoning document update. A prompt that moves without its source is drift by another name. The version numbers do not need to match, since a reasoning document can change without its prompt changing. What must hold is the direction: the reasoning document changes first, and the prompt follows.

**Why the prompt is optimized for its reader, not its author**

The traveling prompt is read by an LLM, not a human. It does not need to be written as friendly prose: compression and directness are features, not shortcuts. If tighter language activates the right behaviors more reliably, that is a better prompt. The reasoning document is the human-readable source. The prompt is the derivative, optimized for its reader. For that reader the prompt has to carry its own vocabulary: a project term it leaves undefined is guessed, and a guess inside an instruction can change what the LLM does with no sign that anything went wrong.

One governance constraint applies: the prompt must remain verifiable by the human. Not fully readable as prose, but parseable enough that the human can verify it still reflects the methodology. If the prompt drifts into shorthand the human cannot evaluate, oversight of the methodology is lost. The bar is verifiability, not readability.

**Why cross-LLM testing is part of prompt curation discipline**

The traveling prompt is developed and refined primarily through use with a single LLM. That creates a specific drift risk: the prompt gradually encodes that LLM's behavioral idiosyncrasies as methodology. The discipline looks rigorous, it is grounded in real experience, but the ground is model-specific and moving. Deliberate testing against a second LLM serves the same function as giving a document to an LLM with no other context: it surfaces what has been invisibly optimized away. This is a curation practice for the prompt artifact itself, not a requirement of the methodology in general use.

---

## The Boundaries

The prompt artifacts are explicitly not:

**A replacement for the methodology documents.** The traveling prompt carries principles. The documents carry reasoning. An LLM working with the traveling prompt but without the relevant documents is missing the content the principles are designed to protect. Both are required.

**A guarantee of perfect discipline.** The prompt artifacts reduce the cognitive burden of enforcing the methodology; they do not eliminate it. Human judgment remains essential, especially in grey zones and at decision points.

**A static artifact.** All prompt artifacts will need to evolve as the methodology evolves. New hard lessons, new patterns, new grey zones: all of these should eventually find their way into the relevant prompt. Each has a version number and is subject to curation like any other document in the methodology.

**A substitute for the prompt reasoning documents.** The reasoning documents are the source. The prompts are the derivatives. If a prompt is ever questioned or needs to change, its reasoning document is where the discussion happens, not in the prompt itself.

**A substitute for each other.** The traveling prompt, the human prompt, and the sweep prompts have distinct scopes that must not collapse. The human prompt calibrates the human collaborator's posture, and it cannot be absorbed into the traveling prompt without leaving one collaborator uncalibrated. None can absorb another's job without failing at its own.

---

## The Open Questions

*No open questions at this time.*

---

## Hard Lessons

*No hard lessons at this time.*

---

*module_reasoning // [living]*
*the prompts are the derivatives*
*this document is the source*
*the prompt follows the reasoning*
*that is the right order*
