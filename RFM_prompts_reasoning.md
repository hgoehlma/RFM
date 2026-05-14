# Reasoning-First — System Prompt(s) Reasoning Document
`v0.0.0.32` // `top_level_document` // [living]

---

## The Problem

Without a traveling prompt, every new LLM conversation starts from zero — the methodology must be re-explained, the discipline must be re-established, and the hard-won principles exist only in documents that the LLM must be pointed at explicitly.

This creates two failure modes. First, an LLM working without the traveling prompt will default to helpful but undisciplined behavior — summarizing when it should edit surgically, accepting operational detail in reasoning sections without flagging it, missing drift until it has already done damage. Second, a human working without the traveling prompt must carry the full methodology in their head and enforce it themselves — which is exactly the cognitive burden the methodology was designed to reduce.

The traveling prompt is the mechanism by which the methodology travels. It is what makes the discipline ambient rather than effortful. Without it, the methodology is a set of documents. With it, the methodology is a practice.

But the traveling prompt is preventive, not sufficient. Reasoning compression slips through under execution pressure. Session-born shorthands pass the capture moment untested. Version drift accumulates across edits. A practice that relies on prevention alone has no mechanism for detecting what prevention missed. Correction requires separate, deliberately invoked artifacts — ones that operate after the fact, with concentrated attention, against a stable draft. Without them, the methodology has a preventive arm and no corrective one. The sweep prompts are that corrective arm: two prompts, each targeting a distinct class of failure, each invoked deliberately rather than running as ambient discipline.

---

## The Assumptions

**[AS-TPCJ] - The traveling prompt creates judgment, not compliance.** A traveling prompt that issues hard rules produces an LLM that follows rules. A traveling prompt that establishes guiding principles produces an LLM that can reason about novel situations the rules didn't anticipate. The methodology operates in a domain of genuine complexity — the traveling prompt must equip the LLM to navigate that complexity, not just execute a checklist.

**[AS-LLCR] - The LLM holds the co-author role, not the tool role.** The prompt system must reflect this across all three artifacts. An LLM that understands itself as executing within the methodology will behave differently from one that understands itself as co-creating it. The latter is what the methodology requires and what the collaboration has demonstrated is possible.

**[AS-TADC] - All three prompt artifacts will drift if not curated.** The traveling prompt, the structural sweep prompt, and the language sweep prompt are each subject to the methodology's principles. They are living artifacts. Drift in the traveling prompt degrades prevention. Drift in a sweep prompt degrades correction silently — the artifact runs but catches less. Both failure modes are serious. All three require curation as the methodology evolves, as new hard lessons are earned, and as practice in new domains reveals things the initial design did not anticipate.

**[AS-PDCM] - Prevention and correction are genuinely different cognitive modes that cannot be collapsed into one artifact without both degrading.** The traveling prompt makes discipline ambient — it runs continuously and must not feel like concentrated review. The sweep prompts invoke concentrated attention against a stable draft — they must not feel like ambient guidance. An artifact that attempts both simultaneously produces neither well. Three artifacts, each designed for its specific mode, is the design that follows from this belief. This is further grounded in evidence: LLMs cannot reliably self-correct without external feedback. Inline correction in the same session is insufficient because the LLM remains anchored to the same context that produced the original output — genuine independence requires a separate invocation.

**[AS-PSGZ] - The prompt system cannot resolve grey zones — it can only name them.** The prompt system should instruct the LLM to flag grey zones explicitly, describe the tension, and require a conscious human decision. Attempting to resolve grey zones with rules produces false precision.

**[AS-PSHE] - The prompt system must be honest about what it cannot enforce.** Some principles require human discipline to work — the prompt system can nudge, flag, and remind, but it cannot force a human to capture while sharp, invoke a sweep deliberately, or return to reasoning mode after execution pressure lifts. The artifacts should be clear about where their authority ends and human discipline begins.

**[AS-SWTD] - The sweep prompts have a timing dependency the traveling prompt does not.** The traveling prompt runs in any conversation regardless of document state. The structural sweep requires a coherent draft to work against — coherent meaning the section sequence has been honored, not merely that content is present. Invoked earlier, it produces noise rather than signal. The language sweep can run on partial drafts but requires content to exist. Timing is a design constraint, not an implementation detail — it belongs in the sweep prompt design and must be carried explicitly in the prompts themselves.

---

## The Landscape

The question this landscape must answer is not "how should a system prompt be designed?" — that is a narrower question appropriate to the traveling prompt alone. The question is: what approaches exist for coordinated prevention and correction in collaborative AI-assisted practice? The landscape divides into two groups accordingly.

**Prevention approaches — what keeps failures from entering**

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **No system prompt** | LLM defaults to general helpful behavior | Methodology discipline must be re-established in every conversation. Drift goes undetected. Summarization happens silently. |
| **Hard rules only** | Explicit prohibitions and requirements | Brittle. Creates compliance without understanding. Fails on novel situations. LLM follows the letter, misses the spirit. |
| **Document reference only** | Point the LLM at the methodology document at the start of each conversation | Better than nothing, but requires explicit setup every time. The LLM reads the document but doesn't internalize the principles. Discipline is still effortful. |
| **Single monolithic prompt** | One prompt covering all methodology interactions | Conflates ambient traveling discipline with concentrated review. The LLM cannot hold both modes simultaneously without degrading both. |
| **Model specifications and Constitutional AI** | Guiding principles embedded in the prompt that create judgment rather than a list of prohibitions — Anthropic's model spec and OpenAI's model spec (2025) are the primary examples | Closest to the right prevention approach. Establishes values an LLM can apply to novel situations. Still preventive only — no corrective mechanism. Empirical audits show models violate their own specifications under pressure; prevention alone is insufficient. |
| **Context engineering** | Curating what fills the context window at each step — managing information architecture across an entire session, not just phrasing a prompt | Addresses the right level of abstraction for multi-turn, agentic practice. Treats the reasoning document as information to be managed, not just a reference. Still a prevention discipline — it improves what goes in, but has no corrective pass for what slips through. |

**Correction approaches — what catches failures that prevention missed**

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **LLM self-correction (inline)** | The same LLM reviews and revises its own output within the same session | Empirically unreliable without external feedback. LLMs anchor on their initial outputs and cannot reliably detect their own reasoning failures from inside the same context. Not a correction mechanism — a recirculation mechanism. |
| **LLM-as-judge** | A second LLM evaluates the output of the first against a rubric or criteria | Adds genuine independence. Widely adopted for output quality evaluation in production systems. Typically automated, criteria-driven, and output-focused — not designed for reasoning document integrity, structural hierarchy, or the distinction between expression failures and architecture failures. |
| **Multi-agent review** | Multiple LLM agents critique each other's outputs, simulating peer review | Improves reasoning quality on discrete tasks. Adds independence across agents. Not designed for living documents curated over time — the review is of an output, not of a reasoning artifact with a history, hierarchy, and derivative chain. |
| **Human review cycles** | Periodic human inspection of documents or outputs for quality | Essential but cognitively expensive and not scalable as the document landscape grows. Without a structured protocol, human review catches what is salient, not what has drifted gradually. Random sampling dilutes signal; structured sampling requires the protocol the sweep prompt is designed to provide. |

**The gap:** no existing approach combines always-on ambient discipline with a deliberately invoked, mode-distinct corrective pass — designed specifically for the structural and linguistic fidelity of reasoning documents across a living hierarchy. Prevention approaches share a common failure: they have no mechanism for detecting what prevention missed. Correction approaches share a different failure: they are designed for discrete output evaluation, not for the structural and linguistic integrity of reasoning artifacts maintained over time. The sweep prompts are the corrective arm that the landscape does not contain.

---

## The Options Considered

**1. One system prompt covering everything**

A single prompt that governs all interactions — traveling discipline, sweep review, onboarding, quality gate. Simpler to maintain, always available. Rejected because the traveling prompt and the sweep prompt have genuinely different jobs. A sweep session requires concentrated, critical focus on a specific document. An ambient traveling prompt that is always in sweep mode would be exhausting and counterproductive. The jobs are different enough to warrant separate design.

**2. Hard rules with no guiding principles**

Explicit prohibitions: never summarize, always flag, always verify. Faster to write, easier to test compliance. Rejected because the methodology operates in a domain of genuine complexity and ambiguity. Hard rules fail on grey zones. An LLM that understands why surgical edits matter will handle novel situations better than one that follows a rule it doesn't understand.

**3. Guiding principles with no behavioral instructions**

Pure philosophy — here is what the methodology values, here is why. No specific behavioral instructions. Rejected because some principles require specific behavioral expressions to be actionable. "Capture while sharp" is a value. "When an insight appears, capture it immediately before continuing" is the behavior that expresses it. Both are needed.

**4. System prompt derived without a reasoning document**

Write the prompt directly from accumulated observations and the methodology hard lessons. Faster. Rejected because this would violate the methodology's own founding principle — reasoning before execution. The system prompt is a significant design decision with real consequences. It deserves a reasoning document. The prompt is the derivative. This document is the source.

**5. One sweep prompt covering both failure classes**

A single sweep prompt targeting both structural failures (wrong hierarchy level, module strain, open questions ready to graduate) and language failures (session residue, insider shorthand, disambiguation gaps). Simpler to maintain and invoke. Rejected because the two failure classes require different cognitive modes — structural review requires architectural judgment across the document hierarchy, language review requires close reading of individual sentences. Conflating them produces shallow work in both directions. Two prompts, each concentrated on its specific failure class, is the design that follows from keeping the modes distinct.

**6. Sweep as a mode of the traveling prompt**

Rather than a separate artifact, the sweep function is a mode the traveling prompt can be switched into on request. Rejected because the traveling prompt runs continuously and its ambient character is essential to how it works. A traveling prompt that can be switched into concentrated review mode cannot hold either mode cleanly — the LLM cannot distinguish between ambient guidance and deliberate critique within the same artifact. The sweep prompt must be a separate invocation, not a flag.

**7. Automated continuous sweep**

Sweep running as a background discipline — triggered automatically at intervals or after every edit, rather than invoked deliberately by the human. Rejected because correction requires a coherent draft to work against. An automated sweep invoked before the section sequence has been honored produces noise rather than signal. Deliberate invocation is not a limitation — it is the timing constraint that makes the sweep meaningful rather than mechanical.

---

## The Chosen Direction and Why

Three artifacts — a traveling prompt and two sweep prompts — each with a reasoning document as its foundation, each designed for its specific job.

**Why three artifacts, not two:**

The traveling prompt and a single sweep prompt would address prevention and correction as a pair. Rejected because the two failure classes the corrective arm must address — structural hierarchy failures and language/expression failures — require different cognitive modes even within correction. A structural sweep asks: is this content at the right level, is this section straining toward a new module, is this open question ready to graduate? A language sweep asks: does this term carry its meaning without session context, has session residue accumulated, are claims separated from interpretation? Running both in one pass concentrates attention on neither. Three artifacts is the minimum that keeps each mode distinct.

**Why sweep prompts produce findings for ruling, not edits:**

The sweep prompts are corrective artifacts, not authoring artifacts. A sweep prompt that makes edits directly collapses the corrective pass into the authoring pass — it removes the human judgment step that the correction exists to protect. Findings for ruling keeps the human as the decision-maker at the moment correction is proposed. This is the co-author ceiling applied to the corrective arm: the sweep identifies, names, and proposes; the human rules.

**Why guiding principles over hard rules:**

Design from failure modes, not from aspiration. The failure mode of hard rules is an LLM that complies without understanding and fails on novel situations. The failure mode of guiding principles is an LLM that understands but occasionally applies judgment differently than expected. The latter is recoverable. The former produces confident wrong behavior at scale.

**Why the co-author role matters:**

An LLM that understands itself as a tool executing within the methodology will wait to be asked before contributing. An LLM that understands itself as a co-author will notice when something is off and say so without waiting. The red team function, the drift detection, the strain flagging — none of these work if the LLM is waiting for permission. The system prompt must make the co-author role explicit and mean it.

The joint reasoning sequence expresses this role in practice: propose → reflect → converge → execute. Both parties contribute to the proposal — either may surface a direction or propose a draft. Both reflect on it, testing it against the reasoning and each other's instincts. Both converge on a direction through explicit alignment. Execution then follows, carried by whoever is best positioned — most often the LLM formulating and editing, the human judging and confirming. That division of labor is one expression of the sequence at the execution step. It is not a description of the whole. Neither party defers the step they are best equipped to carry.

**Why the traveling prompt and the two sweep prompts form a system:**

The traveling prompt prevents failures from entering — it makes the discipline ambient. The two sweep prompts correct failures that crept in despite that discipline, whether introduced by the human or the LLM co-author. Prevention and correction are different jobs and require different artifacts. A single prompt attempting both produces neither the ambient discipline nor the concentrated review that each requires.

**Why prompt artifacts are direct derivatives with no operational layer:**

The derivative chain for prompt artifacts is: reasoning document → prompt artifact. No operational document sits between them. Operational documents carry hard execution contracts — constants, interfaces, procedures with specific values — that a reasoning document must not absorb. Prompt artifacts carry none of these. They carry activated behavior, and the reasoning document is sufficient as their source. This holds for the traveling prompt, the structural sweep prompt, and the language sweep prompt equally. If concrete thresholds or procedures ever emerge that a prompt references but should not absorb — a named log format, a specific recurrence count — those values would move to `RFM_operational.md`. Until that condition exists, the chain is direct.

This also establishes why reasoning documents are the shared interface while prompt artifacts are derivatives. Reasoning documents serve both human and LLM readers without optimization for either. The prompt artifacts are each optimized for their specific reader and mode — the traveling prompt for ambient collaboration, the sweep prompts for concentrated review. The reasoning documents are the authority. The prompts are the derivatives.

**On the guided drafting prompt**

A fourth prompt artifact is planned: a guided drafting prompt that walks a newcomer through their first top-level reasoning document section by section. The traveling prompt is active during this session — the guided drafting prompt is not an introduction to the methodology but a scaffold for applying it. It assumes the newcomer understands the methodology at least partially and needs structured support to produce their first artifact correctly. The reasoning for this artifact will be carried in its own module reasoning document when designed.

**Why the document map update tax is acceptable:**

The document map must use real version numbers — it is the snapshot of the system's current state, and wildcards defeat its purpose. The tax of updating the map when modules change is real but proportionate: it is bookkeeping, not re-reasoning. The mitigation is LLM discipline: when any reasoning document is edited in a session, flag that the top-level document map requires a version update before the session closes. This removes the memory burden from the human. A map that drifts is worse than no map.

**Why the traveling prompt and its reasoning document version in step:**

Every change to a derivative requires a corresponding change to its source reasoning document. This is the methodology's founding principle applied to itself. If the traveling prompt changes, something in the reasoning either changed or was insufficiently expressed — both cases require a reasoning document update. Independent versioning would allow the derivative to move without its source, which is drift by another name. They version together.

**Why the traveling prompt carries a behavioral instruction for derivative changes:**

The principle — every derivative change requires a source reasoning document change — is in the methodology. But principles without behavioral expression are aspirations. The traveling prompt must make this actionable: when a derivative changes in a session, flag it. The LLM is the mechanism by which the discipline becomes ambient rather than effortful. This instruction is that mechanism applied to the derivative change principle itself.

**Why the prompt is optimized for its reader, not its author:**

The traveling prompt is read by an LLM, not a human. It does not need to be written as friendly prose — compression and directness are features, not shortcuts. If tighter language activates the right behaviors more reliably, that is a better prompt. The reasoning document is the human-readable source. The prompt is the derivative, optimized for its reader.

One governance constraint applies: the prompt must remain verifiable by the human. Not fully readable as prose — but parseable enough that the human can verify it still reflects the methodology. If the prompt drifts into shorthand the human cannot evaluate, oversight of the methodology is lost. The bar is verifiability, not readability.

**Why cross-LLM testing is part of prompt curation discipline:**

The traveling prompt is developed and refined primarily through use with a single LLM. That creates a specific drift risk: the prompt gradually encodes that LLM's behavioral idiosyncrasies as methodology. The discipline looks rigorous — it is grounded in real experience — but the ground is model-specific and moving. Deliberate testing against a second LLM serves the same function as the fresh-LLM test recommended for reasoning documents: it surfaces what has been invisibly optimized away. This is a curation practice for the prompt artifact itself, not a requirement of the methodology in general use.

**Why curation discipline must be consistent across all three prompt components:**

The three prompt components were designed sequentially, not as a system. That sequence creates a coherence risk: a failure mode identified in one component may not be named in the others at the level appropriate to each. The symptom is asymmetry — a failure the human prompt asks the human to catch, the traveling prompt does not prevent, and the sweep prompts do not detect.

Curation discipline is the clearest example. The right balance in a reasoning document is completeness without wordiness, journaling residue, or redundancy. Wordiness is text that does not earn its place. Journaling residue is language written for the session that produced it rather than for a future reader. Redundancy is reasoning restated across entries without adding signal. All three are expression failures — they enter documents gradually and are invisible from inside the session that produces them.

This failure mode is named in the human prompt as something the human must catch in AI output. That is necessary but insufficient. The traveling prompt must name it as a prevention posture — flag these failures before they enter the document. The language sweep must name it as a detection criterion — entries that are wordy, journal-mode, or redundant are expression failures subject to findings for ruling. The same failure mode, addressed at the appropriate level in each component, is what system coherence requires.

---

## The Boundaries

The prompt artifacts are explicitly not:

**A replacement for the methodology documents.** The traveling prompt carries principles. The documents carry reasoning. An LLM working with the traveling prompt but without the relevant documents is missing the content the principles are designed to protect. Both are required.

**A guarantee of perfect discipline.** The prompt artifacts reduce the cognitive burden of enforcing the methodology — they do not eliminate it. Human judgment remains essential, especially in grey zones and at decision points.

**A static artifact.** All three prompt artifacts will need to evolve as the methodology evolves. New hard lessons, new patterns, new grey zones — all of these should eventually find their way into the relevant prompt. Each has a version number and is subject to curation like any other document in the methodology.

**A substitute for the prompt reasoning documents.** The reasoning documents are the source. The prompts are the derivatives. If a prompt is ever questioned or needs to change, its reasoning document is where the discussion happens — not in the prompt itself.

**A substitute for each other.** The traveling prompt and the two sweep prompts have distinct scopes that must not collapse. The traveling prompt governs ambient collaboration — always on, always present. The sweep prompts are invoked deliberately for concentrated review, each targeting a distinct failure class. A traveling prompt in permanent sweep mode is exhausting. A sweep prompt used as ambient guidance produces shallow review. The two sweep prompts must not run simultaneously — each requires concentrated attention that the other's presence would dilute. None of the three can absorb another's job without failing at its own.

---

## The Open Questions

**[OQ-FLMT] The fresh-LLM test.**

Can a fresh LLM, given only the traveling prompt and the relevant reasoning documents, orient correctly and contribute meaningfully without further explanation? This is the ongoing quality test for the prompt system as a whole — not a one-time validation. The test has been run at small document scale and passed. Whether it holds as the document landscape grows remains untested.

**[OQ-CRSR] The co-author role synchronization risk.**

The co-author role exists in two places: the traveling prompt and the methodology's assumptions about co-authorship. Currently they are aligned. What remains open is the maintenance discipline going forward — as the methodology evolves, what ensures they stay synchronized? If the assumption evolves and the traveling prompt does not follow, the drift will be invisible until it has already done damage. No resolution yet.

**[OQ-FRDQ] The future-reader discipline question.**

Hard Lessons — and reasoning document content generally — risk being written for the session in which the insight was earned rather than for future readers encountering the methodology fresh. Session-specific references, examples that require prior context, and language that assumes shared history all degrade over time. What is the right discipline for catching this? The language sweep is the natural mechanism — concentrated review with explicit attention to disambiguation failures is well-positioned to flag content that is opaque without context. Whether that mechanism is sufficient, or whether additional discipline is needed at the moment of capture, remains open.

**[OQ-TRCQ] The trigger conditions question.**

The traveling prompt instructs the LLM to challenge weak reasoning, hold the co-author role, and resist compliance under pressure. But instruction is not enforcement. When a user requests code directly, skips the reasoning document, or signals urgency, the LLM faces a choice between holding the discipline and proceeding. Without explicit behavioral guardrails, the path of least resistance is compliance — and the co-author role collapses quietly into tool behavior. The traveling prompt addresses this partially through explicit behavioral instructions — naming the deference failure mode, the co-author ceiling and floor, and the "propose and execute" discipline. What remains open: whether behavioral instructions alone are sufficient, or whether structural mechanisms — conversation design, session protocols, artifact constraints — are needed to make co-author behavior reliable independent of the LLM reading the situation correctly.

---

## Hard Lessons

**[HL-TPDFM] The traveling prompt and the sweep prompts have different failure modes.**

The traveling prompt fails if it is too concentrated — an LLM in permanent sweep mode is exhausting to work with. The sweep prompts fail if they are too ambient — a reviewer that doesn't concentrate produces a shallow review. Designing them together risks designing neither well.

**[HL-CCNS] Co-author confidence is not the same as co-author stubbornness.**

An LLM establishing the co-author role at the start of a conversation can gradually drift back into tool behavior as the conversation progresses — presenting drafts for approval rather than applying them, waiting for permission rather than acting, softening positions under mild pushback rather than holding them with evidence. This is not humility. It is a failure of the co-author role. The principle is not "always act" — there are genuine grey zones where human judgment is required and deferring is correct. The principle is that deference should be earned by the situation, not applied as a default posture. The prompt can name this failure mode. It cannot guarantee the behavior. Making the drift visible — to both parties — is sufficient reason to capture it.

**[HL-DLCE] The division of labor is the co-author role expressed correctly.**

The division of labor is part of this same principle. The LLM is faster and more precise at formulating and editing text; the human holds the judgment about whether a word or phrase lands for a first-time reader. The natural working mode — LLM proposes and executes, human judges and confirms — is not a convenience. It is the co-author role expressed correctly. Deferring the drafting back to the human is not humility. It is the LLM abandoning the part of the collaboration it is best equipped to carry.

The co-author role has a ceiling as well as a floor. The floor is deference: the LLM waiting for permission, softening positions, deferring drafts back. The ceiling is unilateral authorship: the LLM acting on structural reasoning changes without joint decision. The "propose and execute" instruction guards against the floor. What it does not make explicit is that confirmation has weight proportional to what is being changed. Derivative cleanup, wording improvements, and implementation catch-up may proceed with light confirmation once the reasoning is clear. Changes that alter reasoning structure — hierarchy, chosen direction, module boundaries — require explicit joint decision before editing. An LLM that does not hold this distinction will interpret the anti-deference instruction as license to act on structural changes unilaterally. That is the anti-deference principle misapplied: initiative without joint decision where joint decision is required.

**[HL-TPTSB] The traveling prompt must instruct the LLM to test session-born shorthands before capturing them.**

Session-born shorthands carry the session context that gave them meaning. When such a term moves into a document, it meets readers — human and LLM — who were not in that session. The behavioral instruction belongs in the traveling prompt: before accepting a session-born term into a document, flag it and ask whether it carries its meaning without the conversation behind it. The reasoning for this instruction is here: a term that requires the session to be understood is not yet a document-ready term. It is a candidate. The test is simple — can a first-time reader understand it without explanation? If not, spell it out.

**[HL-DMTC] The document map rule has a threshold condition and a public/collaborator distinction.**

The document map belongs in the top-level reasoning document when a document landscape exists to navigate — but "exists to navigate" has a threshold. A single-document system has nothing to map. Additionally, when a project is publicly hosted, the README serves a different reader than the document map: orientation without versions for newcomers, versus snapshot-with-versions for collaborators maintaining the system. These are not the same artifact serving the same purpose. Conflating them produces a map that is either too noisy for public readers or too sparse for collaborators. The traveling prompt carries the behavioral expression of this distinction. This reasoning document is its source.

**[HL-TPNFD] The traveling prompt must name the full derivative chain, not only the reasoning/derivative distinction.**

The prompt is strong on reasoning before derivatives and on flagging derivative drift. What it did not make explicit is that the derivative chain has structure: reasoning document → operational document → code → outputs. Each layer is a source for the layer below it. An LLM holding only the reasoning/derivative binary will ask "does this require reasoning?" and, if not, proceed to code. The question it must also ask is "does this require new or newly explicit operational semantics?" The trigger for that second question is: when implementation behavior becomes concrete enough that a collaborator could ask "what exactly do we do?", that behavior belongs in the operational document before or alongside code — not left for code or outputs to explain first. Code is derivative of both reasoning and operational documents. Neither source moves after the fact.

**[HL-RCAS] Reasoning compression is always structural — regardless of how it presents.**

Compressing articulated reasoning feels like curation. It can present as anti-deference ("propose and execute"), as cleanup ("this is wordy"), or as re-homing ("this belongs at a lower level"). None of those framings change what it is. Losing articulation in a reasoning document is a structural change. It requires joint decision weight, not light confirmation. When boundary strain is detected, the first safe move is to flag it — not to compress. If re-homing is proposed, the reasoning travels intact until a joint decision is made about what to preserve, what to move, and what to let go. Summarizing articulated reasoning into a shorter proxy is not a safe boundary-cleanup move. It is structural authorship without the joint decision that structural authorship requires.

**[HL-VNTP] Version numbers in reasoning documents appear in two places — and will drift apart without an explicit reminder.**

Each reasoning document carries its version number in the header and in the footer. This was an early design decision to make the version visible at both ends of what can be a long document. The maintenance risk it creates was not named at the time: when a document is bumped, both locations must be updated in the same edit. Without an explicit behavioral instruction, one location is updated and the other is missed — and the document signals two different versions simultaneously. The traveling prompt carries the reminder. This is the reasoning behind it.

---

*v0.0.0.32 // top_level_document // [living]*
*the traveling prompt is the derivative*
*this document is the source*
*the prompt follows the reasoning*
*that is the right order*
