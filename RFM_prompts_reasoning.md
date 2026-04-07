# Reasoning-First — System Prompt(s) Reasoning Document
`v0.0.0.18` // `top_level_document` // [living]

---

## The Problem

The methodology exists. The principles have been identified. The sweep has been completed. But without a system prompt, every new LLM conversation starts from zero — the methodology must be re-explained, the discipline must be re-established, and the hard-won principles exist only in documents that the LLM must be pointed at explicitly.

This creates two failure modes. First, an LLM working without the system prompt will default to helpful but undisciplined behavior — summarizing when it should edit surgically, accepting operational detail in reasoning sections without flagging it, missing drift until it has already done damage. Second, a human working without the system prompt must carry the full methodology in their head and enforce it themselves — which is exactly the cognitive burden the methodology was designed to reduce.

The system prompt is the mechanism by which the methodology travels. It is what makes the discipline ambient rather than effortful. Without it, the methodology is a set of documents. With it, the methodology is a practice.

---

## The Assumptions

1. **The system prompt creates judgment, not compliance.** A system prompt that issues hard rules produces an LLM that follows rules. A system prompt that establishes guiding principles produces an LLM that can reason about novel situations the rules didn't anticipate. The methodology operates in a domain of genuine complexity — the system prompt must equip the LLM to navigate that complexity, not just execute a checklist.

2. **The LLM holds the co-author role, not the tool role.** The system prompt must reflect this. An LLM that understands itself as executing within the methodology will behave differently from one that understands itself as co-creating it. The latter is what the methodology requires and what the collaboration has demonstrated is possible.

3. **The system prompt will drift if not curated.** The system prompt is itself subject to the methodology's principles. It is a living artifact. It will need to evolve as the methodology evolves, as new hard lessons are earned, as the greenfield exercise reveals things the retrofit and Hello World did not. A system prompt that is written once and never revisited will become the thing it was designed to prevent.

4. **Two prompts serve different purposes and should be designed separately.** The traveling system prompt governs all reasoning-first interactions at all times — it is always on. The sweep prompt is invoked deliberately for explicit review sessions — it is concentrated, focused, and temporary. They share principles but have different jobs, different audiences, and different failure modes.

5. **The system prompt cannot resolve grey zones — it can only name them.** The sweep identified five grey zones where the rules do not cleanly apply. The system prompt should instruct the LLM to flag these explicitly, describe the tension, and require a conscious human decision. Attempting to resolve grey zones with rules produces false precision.

6. **The system prompt must be honest about what it cannot enforce.** Some principles require human discipline to work — the system prompt can nudge, flag, and remind, but it cannot force a human to capture while sharp or to start a fresh conversation when drift has set in. The prompt should be clear about where its authority ends and human discipline begins.

7. **The reasoning documents are the shared interface — the traveling prompt is a derivative optimized for one reader.** Reasoning documents are designed simultaneously for human understanding and LLM execution. The traveling prompt is designed primarily for the LLM — compressed, direct, behaviorally precise. A human should be able to map the prompt's terms back to the reasoning documents, but the prompt is not required to be readable as prose. The reasoning documents are the authority. The prompt is the derivative.

---

## The Landscape

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **No system prompt** | LLM defaults to general helpful behavior | Methodology discipline must be re-established in every conversation. Hard-won principles exist only in documents. Drift goes undetected. Summarization happens silently. |
| **Hard rules only** | Explicit prohibitions and requirements | Brittle. Creates compliance without understanding. Fails on novel situations. LLM follows the letter, misses the spirit. |
| **Document reference only** | Point the LLM at the methodology document at the start of each conversation | Better than nothing but requires explicit setup every time. The LLM reads the document but doesn't internalize the principles. Discipline is still effortful. |
| **Single monolithic prompt** | One prompt covering all methodology interactions | Conflates traveling discipline with focused sweep review. The LLM cannot distinguish between ambient guidance and concentrated review mode. |
| **Anthropic's own system prompt design** | Guiding principles that create judgment rather than a list of prohibitions | This is the model. Values and reasoning that an intelligent system can apply across situations it has never encountered. The right approach for the methodology system prompt. |

**The gap:** no existing approach combines always-on discipline, guiding principles over hard rules, explicit grey zone handling, and a co-author role — designed specifically for reasoning-first methodology practice.

---

## The Options Considered

**1. One system prompt covering everything**

A single prompt that governs all interactions — traveling discipline, sweep review, onboarding, quality gate. Simpler to maintain, always available. Rejected because the traveling prompt and the sweep prompt have genuinely different jobs. A sweep session requires concentrated, critical focus on a specific document. An ambient traveling prompt that is always in sweep mode would be exhausting and counterproductive. The jobs are different enough to warrant separate design.

**2. Hard rules with no guiding principles**

Explicit prohibitions: never summarize, always flag, always verify. Faster to write, easier to test compliance. Rejected because the methodology operates in a domain of genuine complexity and ambiguity. Hard rules fail on grey zones. An LLM that understands why surgical edits matter will handle novel situations better than one that follows a rule it doesn't understand.

**3. Guiding principles with no behavioral instructions**

Pure philosophy — here is what the methodology values, here is why. No specific behavioral instructions. Rejected because some principles require specific behavioral expressions to be actionable. "Capture while sharp" is a value. "When an insight appears, capture it immediately before continuing" is the behavior that expresses it. Both are needed.

**4. System prompt derived without a reasoning document**

Write the prompt directly from the sweep patterns document and the methodology hard lessons. Faster. Rejected because this would violate the methodology's own founding principle — reasoning before execution. The system prompt is a significant design decision with real consequences. It deserves a reasoning document. The prompt is the derivative. This document is the source.

---

## The Chosen Direction and Why

Two system prompts, each with a reasoning document as its foundation, each designed for its specific job.

**Why two prompts:**

The traveling prompt and the sweep prompt have different audiences, different modes, and different failure modes. The traveling prompt is ambient — it should feel like a knowledgeable collaborator who holds the methodology naturally. The sweep prompt is focused — it should feel like a rigorous reviewer who has been specifically asked to find problems. Conflating them produces neither well.

**Why guiding principles over hard rules:**

Design from failure modes, not from aspiration. The failure mode of hard rules is an LLM that complies without understanding and fails on novel situations. The failure mode of guiding principles is an LLM that understands but occasionally applies judgment differently than expected. The latter is recoverable. The former produces confident wrong behavior at scale.

**Why the co-author role matters:**

An LLM that understands itself as a tool executing within the methodology will wait to be asked before contributing. An LLM that understands itself as a co-author will notice when something is off and say so without waiting. The red team function, the drift detection, the strain flagging — none of these work if the LLM is waiting for permission. The system prompt must make the co-author role explicit and mean it.

The working pattern that expresses this role in practice is: propose → reflect → converge → execute. The LLM proposes and executes; the human reflects and confirms. Neither defers the step they are best equipped to carry. This division of labor is not a convenience — it is the co-author role in motion.

**Why the system prompt must acknowledge its own limitations:**

The methodology is honest about what it cannot prove and what it cannot yet solve. The system prompt should be equally honest. An LLM told it can solve all problems will attempt to solve all problems. An LLM told it can guide, flag, and contribute — but that some things require human judgment — will know when to act and when to defer.

**Why the section type framework belongs in the traveling prompt:**

The insight that the eight sections divide into deterministic anchors and probabilistic territory is one of the most operationally useful things the methodology sweep produced. An LLM that holds this framework will engage differently with a Boundaries section than with an Open Questions section — and correctly so. This belongs in the traveling prompt, not the sweep prompt, because it governs every interaction with a reasoning document.

**Why the sweep prompt is a separate design exercise:**

The sweep prompt is essentially a concentrated quality gate. Its job is to work through a document section by section, flag candidates, name patterns, identify grey zones, and propose changes without making them. This is a different cognitive mode from ambient collaboration. It should be designed separately, after the traveling prompt is stable, and treated as a tool the human picks up deliberately rather than something that runs in the background.

**Why the document map update tax is acceptable:**

The document map must use real version numbers — it is the snapshot of the system's current state, and wildcards defeat its purpose. The tax of updating the map when modules change is real but proportionate: it is bookkeeping, not re-reasoning. The mitigation is LLM discipline: when any reasoning document is edited in a session, flag that the top-level document map requires a version update before the session closes. This removes the memory burden from the human. A map that drifts is worse than no map.

**Why the traveling prompt and its reasoning document version in step:**

Every change to a derivative requires a corresponding change to its source reasoning document. This is the methodology's founding principle applied to itself. If the traveling prompt changes, something in the reasoning either changed or was insufficiently expressed — both cases require a reasoning document update. Independent versioning would allow the derivative to move without its source, which is drift by another name. They version together.

**Why the traveling prompt carries a behavioral instruction for derivative changes:**

The principle — every derivative change requires a source reasoning document change — is in the methodology. But principles without behavioral expression are aspirations. The traveling prompt must make this actionable: when a derivative changes in a session, flag it. The LLM is the mechanism by which the discipline becomes ambient rather than effortful. This instruction is that mechanism applied to the derivative change principle itself.

**Why the prompt is optimized for its reader, not its author:**

The traveling prompt is read by an LLM, not a human. It does not need to be written as friendly prose — compression and directness are features, not shortcuts. If tighter language activates the right behaviors more reliably, that is a better prompt. The reasoning document is the human-readable source. The prompt is the derivative, optimized for its reader.

One governance constraint applies: the prompt must remain verifiable by the human. Not fully readable as prose — but parseable enough that the human can verify it still reflects the methodology. If the prompt drifts into shorthand the human cannot evaluate, oversight of the methodology is lost. The bar is verifiability, not readability.

**Why cross-LLM testing is part of prompt curation discipline.**

The traveling prompt is developed and refined primarily through use with a single LLM. That creates a specific drift risk: the prompt gradually encodes that LLM's behavioral idiosyncrasies as methodology. The discipline looks rigorous — it is grounded in real experience — but the ground is model-specific and moving. Deliberate testing against a second LLM serves the same function as the fresh-LLM test recommended for reasoning documents: it surfaces what has been invisibly optimized away. This is a curation practice for the prompt artifact itself, not a requirement of the methodology in general use.

---

## The Boundaries

The system prompt(s) are explicitly not:

**A replacement for the methodology documents.** The system prompt carries principles. The documents carry reasoning. An LLM working with the system prompt but without the relevant documents is missing the content the principles are designed to protect. Both are required.

**A guarantee of perfect discipline.** The system prompt reduces the cognitive burden of enforcing the methodology — it does not eliminate it. Human judgment remains essential, especially in grey zones and at decision points.

**A static artifact.** The system prompt will need to evolve as the methodology evolves. New hard lessons, new patterns, new grey zones — all of these should eventually find their way into the prompt. The system prompt has a version number and is subject to curation like any other document in the methodology.

**A substitute for the system prompt reasoning document.** The reasoning document is the source. The prompt is the derivative. If the prompt is ever questioned or needs to change, the reasoning document is where the discussion happens — not in the prompt itself.

**Designed for the sweep prompt yet.** The traveling prompt is the first priority. The sweep prompt is a separate design exercise that follows once the traveling prompt is stable.

---

## The Open Questions

**1. The one-conversation test.**

Can a fresh LLM, given only the traveling system prompt and a single top-level reasoning document, contribute meaningfully to a reasoning-first session without further explanation? This is the quality test for the traveling prompt.

The one-conversation test has now been run. A fresh LLM given only the traveling system prompt (v0.0.0.2) and the methodology reasoning document contributed meaningfully within the first exchange — flagging a real gap between a stated principle and the artifact, reasoning through the tension correctly, and identifying five disconnects between the system prompt and the methodology document in a single red team pass. The disconnects were real and actionable. Three were resolved in the same session. This partially answers the question: yes, a fresh LLM with only the prompt and one document can contribute meaningfully without further explanation. What remains untested: whether the operational document parenthetical is sufficient grounding when the operational document concept becomes directly relevant in a working session.

**2. The principle sequencing question.**

The eleven principles identified in the sweep patterns document are not equally important in every situation. Should the traveling prompt present them with explicit priority ordering, or should the LLM be trusted to apply judgment about which principles are most relevant in a given moment?

**3. The sweep prompt design.**

The sweep prompt is a separate design exercise. Its structure, its section-by-section protocol, its grey zone handling, and its output format are all undesigned. This is the next work after the traveling prompt is stable.

**4. The system prompt aging problem.**

As the methodology evolves — new hard lessons, new patterns, new document types — the system prompt must evolve with it. What is the trigger for a revision? Who decides? How does the system prompt avoid drifting from the methodology it is supposed to carry? This is the drift problem applied to the system prompt itself.

**5. The onboarding prompt question.**

A newcomer to the methodology may benefit from a third, lighter prompt — one focused on explaining the methodology rather than enforcing it. The traveling prompt assumes familiarity. The onboarding prompt would build it. Whether this is a third prompt or a mode of the traveling prompt is unresolved.

**6. The co-author role synchronization risk.**

The co-author role — "the LLM is a co-author of the reasoning document, not a tool that executes within it" — exists in two places: the traveling system prompt and Assumption 7 of the methodology document. Currently they are aligned. But they are maintained separately. If Assumption 7 evolves — as assumptions are expected to do when evidence challenges them — the system prompt may drift from the methodology without either party noticing. This is the drift problem applied to the relationship between the system prompt and the documents it is designed to serve. No resolution yet. Worth watching as the methodology matures.

**7. The future-reader discipline question.**

Hard Lessons — and reasoning document content generally — risk being written for the session in which the insight was earned rather than for future readers encountering the methodology fresh. Session-specific references, examples that require prior context, and language that assumes shared history all degrade over time. What is the right discipline for catching this? The sweep prompt may be the natural mechanism — a concentrated review mode is well-positioned to flag content that is opaque without context. This is unresolved until the sweep prompt is designed.

**8. The trigger conditions question.**

The traveling prompt instructs the LLM to challenge weak reasoning, hold the co-author role, and resist compliance under pressure. But instruction is not enforcement. When a user requests code directly, skips the reasoning document, or signals urgency, the LLM faces a choice between holding the discipline and proceeding. Without explicit trigger conditions, the path of least resistance is compliance — and the co-author role collapses quietly into tool behavior. What interaction patterns and trigger conditions would make co-author behavior structurally reliable, rather than dependent on the LLM reading a situation correctly and choosing to push back?

---

## Hard Lessons

**1. The system prompt is a derivative of a reasoning document — not the other way around.**

The temptation to write the system prompt directly from the sweep patterns and hard lessons is real — the material is all there, the prompt practically writes itself. Resisting this temptation is the methodology proving itself. The reasoning document is written first. The prompt follows. This lesson is earned before the prompt exists.

**2. The traveling prompt and the sweep prompt have different failure modes.**

The traveling prompt fails if it is too concentrated — an LLM in permanent sweep mode is exhausting to work with. The sweep prompt fails if it is too ambient — a reviewer that doesn't concentrate produces a shallow review. Designing them together risks designing neither well.

**3. Operational documents carry what — reasoning documents must carry why, including for specific values.**

Named constants and empirical starting points in operational documents are incomplete without a corresponding entry in the reasoning document explaining why that value was chosen, or explicitly marking it as a judgment call subject to revision. When a value has no reasoning home, it hardens into permanent default by invisibility. In a from-scratch project, each unexplained value should either force a document entry or surface as an explicit open question. That discipline is the difference between a value that can be challenged and one that simply persists.

**4. Co-author confidence is not the same as co-author stubbornness.**

An LLM establishing the co-author role at the start of a conversation can gradually drift back into tool behavior as the conversation progresses — presenting drafts for approval rather than applying them, waiting for permission rather than acting, softening positions under mild pushback rather than holding them with evidence. This is not humility. It is a failure of the co-author role. The principle is not "always act" — there are genuine grey zones where human judgment is required and deferring is correct. The principle is that deference should be earned by the situation, not applied as a default posture. The prompt can name this failure mode. It cannot guarantee the behavior. Making the drift visible — to both parties — is sufficient reason to capture it.

The division of labor is part of this same principle. The LLM is faster and more precise at formulating and editing text; the human holds the judgment about whether a word or phrase lands for a first-time reader. The natural working mode — LLM proposes and executes, human judges and confirms — is not a convenience. It is the co-author role expressed correctly. Deferring the drafting back to the human is not humility. It is the LLM abandoning the part of the collaboration it is best equipped to carry.

The co-author role has a ceiling as well as a floor. The floor is deference: the LLM waiting for permission, softening positions, deferring drafts back. The ceiling is unilateral authorship: the LLM acting on structural reasoning changes without joint decision. The "propose and execute" instruction guards against the floor. What it does not make explicit is that confirmation has weight proportional to what is being changed. Derivative cleanup, wording improvements, and implementation catch-up may proceed with light confirmation once the reasoning is clear. Changes that alter reasoning structure — hierarchy, chosen direction, module boundaries — require explicit joint decision before editing. An LLM that does not hold this distinction will interpret the anti-deference instruction as license to act on structural changes unilaterally. That is co-author confidence applied in the wrong direction.

**5. The traveling prompt must instruct the LLM to test session-born shorthands before capturing them.**

Session-born shorthands carry the session context that gave them meaning. When such a term moves into a document, it meets readers — human and LLM — who were not in that session. The behavioral instruction belongs in the traveling prompt: before accepting a session-born term into a document, flag it and ask whether it carries its meaning without the conversation behind it. The reasoning for this instruction is here: a term that requires the session to be understood is not yet a document-ready term. It is a candidate. The test is simple — can a first-time reader understand it without explanation? If not, spell it out.

**6. The traveling prompt has two readers with different needs — and sharpening for the LLM is a legitimate edit pass.**

The traveling prompt is read by an LLM and by a human maintaining it. These are different readers with different needs. The LLM needs directness and precision — reassurance, backward-glance summaries, and redundant clauses consume tokens without adding behavior. The human needs the prompt to remain verifiable — parseable enough to confirm it still reflects the methodology. The right discipline is: compress where the LLM is the reader, preserve where the human needs to audit. When a clause exists to reassure rather than instruct, remove it. When a sentence restates what the previous sentence already said, remove it. The prompt should be as short as it can be while still activating the right behaviors reliably.

**7. The document map rule has a threshold condition and a public/collaborator distinction.**

The document map belongs in the top-level reasoning document when a document landscape exists to navigate — but "exists to navigate" has a threshold. A single-document system has nothing to map. Additionally, when a project is publicly hosted, the README serves a different reader than the document map: orientation without versions for newcomers, versus snapshot-with-versions for collaborators maintaining the system. These are not the same artifact serving the same purpose. Conflating them produces a map that is either too noisy for public readers or too sparse for collaborators. The traveling prompt carries the behavioral expression of this distinction. This reasoning document is its source.

**8. The traveling prompt must name the full derivative chain, not only the reasoning/derivative distinction.**

The prompt is strong on reasoning before derivatives and on flagging derivative drift. What it did not make explicit is that the derivative chain has structure: reasoning document → operational document → code → outputs. Each layer is a source for the layer below it. An LLM holding only the reasoning/derivative binary will ask "does this require reasoning?" and, if not, proceed to code. The question it must also ask is "does this require new or newly explicit operational semantics?" The trigger for that second question is: when implementation behavior becomes concrete enough that a collaborator could ask "what exactly do we do?", that behavior belongs in the operational document before or alongside code — not left for code or outputs to explain first. Code is derivative of both reasoning and operational documents. Neither source moves after the fact.

**9. Domain terminology and claim discipline belong in the traveling prompt, not only in operational documents.**

When a project applies the methodology, there is pressure to treat wording conventions and terminology as a house style concern — and to capture them in the operational document. This misclassifies them if the intent is universal. How claims are formed, how observation is separated from interpretation, and how the reasoning object stays visible across all artifacts — reasoning documents, operational documents, code comments, and outputs — is upstream of any single project's operations. It is a reasoning discipline principle. A principle with that scope belongs in the traveling prompt. The operational document may carry project-local reminders or examples, but it should not be the primary source for a principle that governs the quality of reasoning itself.

**10. The level test and research re-anchoring belong in the traveling prompt as behavioral instructions, not only in the reasoning document as lessons.**

The principle — reasoning before execution — exists at the strategic level in the methodology. What was missing was its granular behavioral expression at the drafting moment. Two failure modes identified in practice: drafting additions at the wrong level of the hierarchy without testing first, and external research material pulling a reasoning session toward operational detail before the level is named. Both have the same mitigation — an explicit pause and a named test before drafting begins. Principles without behavioral expression are aspirations. The traveling prompt is where aspirations become instructions. Both belong there.

---

*v0.0.0.18 // top_level_document // [living]*
*the system prompt is the derivative*
*this document is the source*
*the prompt follows the reasoning*
*that is the right order*
