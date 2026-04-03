# Reasoning-First Methodology
`v0.0.0.25` // `top_level_document` // [living]

---

## The Problem

Any domain where complex reasoning precedes execution faces the same failure: the thinking disappears. In software development — where this methodology was built and where the consequences are currently most visible — the decisions that shape a system — why this approach, why not another, what was assumed, what failed — exist briefly in people's minds and disappear. What remains is code. The meaning behind it does not survive.

This creates two compounding failures: humans joining or revisiting a system must reconstruct intent from structure. LLMs assisting with that system hallucinate because the context they need was never recorded.

Current tools address symptoms. None address the root cause: there is no disciplined practice for capturing and maintaining reasoning as a primary artifact, at every level of a system, designed to serve both humans and LLMs simultaneously.

**Why now?**

This problem is not new. What is new is that LLMs have made the consequences of missing reasoning suddenly visible and concrete. But the same LLMs also create the opportunity to fix it — because a well-reasoned document doesn't just help humans understand a system. It directly improves how AI executes within it. The problem and the solution have arrived together.

---

## The Assumptions

The following are believed to be true. They cannot all be fully proven yet. If any of them is wrong, the methodology needs to change.

1. **Context is irreducibly important for LLMs.** High signal reasoning context minimizes hallucination. This holds regardless of how capable models become — a better LLM with poor context will still underperform a modest LLM with rich context.

2. **Abstraction will continue to evolve — and language is the next layer.** The history of software is a history of increasing abstraction. LLMs make intention expressible in natural language. But no level of abstraction removes the need to articulate what you want. The thinking cannot be delegated.

3. **Modularity is the only sustainable architecture.** Monolithic systems resist change, learning, and maintenance. The reasoning document hierarchy should mirror and enforce modular thinking from the start.

4. **Code alone will never carry its own motivation.** The gap between what code does and why it exists cannot be closed by better code. It requires a separate, connected reasoning artifact maintained proactively.

5. **Quality of execution — human or AI — is upstream of the reasoning investment.** Thinking first is not overhead. It is the highest leverage point in the entire development process.

The first five assumptions describe the world as the methodology finds it. The next six describe what working within that world requires.

6. **Curation must be deliberate, not optional.** Curation has two modes and both are required. The first is triggered — something accumulates, strains, or surfaces in use, and draws you back to the document. The second is deliberate return — you come back without a specific trigger, to ask whether the document still reflects what you know. Neither mode can be replaced by a scheduled rhythm; a time-triggered cadence risks becoming performative rather than genuine. The methodology only holds if both modes are practiced as discipline, not suggestion.

7. **A reasoning document designed explicitly for both humans and LLMs simultaneously outperforms one designed for either alone.** This is not a natural default. It requires conscious design. True collaboration between human and LLM is not a side benefit of the methodology — it is the mechanism by which the methodology works. The LLM holds the co-author role in the reasoning document — it is not a tool that executes within it.

8. **Hard lessons are as valuable as successes.** What failed, and why, carries as much reasoning value as what worked. A methodology that doesn't capture failure will repeat it.

9. **Document strain is diagnostic of hierarchy.** When a section strains under its own weight — too many options, too much detail, too many edge cases — that is a signal to branch into a new module, not a signal to write more carefully. The module structure is not designed upfront. It emerges from the writing. The hierarchy reveals itself through strain.

10. **In domains where execution has hard contracts — software being the primary example — the reasoning document is accompanied by an operational document.** The operational document carries constants, interfaces, procedures, and known values. It is a derivative of the reasoning, not a replacement for it. The methodology stays universal. The operational document is domain-specific.

11. **These assumptions describe a self-reinforcing loop — when the discipline holds.** When an LLM works within a well-reasoned document, its downstream execution — code generation, system design, prompt construction — is more correct and less prone to hallucination. Higher correctness produces better output for the human to reason against. Better joint reasoning produces richer documents. Richer documents improve the next round of LLM execution. The loop is self-reinforcing — but only when both parties hold the discipline: the LLM guided by a correctly designed system prompt, the human committed to reasoning before execution and curating honestly. When either breaks, the loop degrades. This is the mechanism by which the methodology works — not just a benefit of it.

---

## The Landscape

The problem of meaning in software is not unrecognized. Several movements have addressed parts of it:

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **Agile** | Shifted focus from documentation-heavy waterfall to working software and human collaboration | Solved delivery rigidity but traded away reasoning continuity in the process — in part because "working software over comprehensive documentation" was routinely misread as license to abandon reasoning capture entirely, a misreading that spread widely enough to become cultural default in many teams |
| **Domain-Driven Design** | Made meaning an explicit design target. Gave us Ubiquitous Language and Bounded Contexts | Presupposes reasoning already exists — it structures meaning, it doesn't generate or preserve it |
| **Clean Code / TDD** | Made quality and correctness first-class concerns | Correctness is not the same as meaning. A perfectly tested system can still be incomprehensible |
| **Wardley Mapping** | Made situational awareness and strategic reasoning explicit, visual, and owned | Stops at the strategic level. Doesn't cascade into a connected reasoning practice at every level of execution |
| **ADRs** | Capture individual decisions | Not hierarchical. Not designed for LLM consumption. Document conclusions, rarely the full reasoning journey |
| **Context Engineering** | Recognizes that LLM output quality depends on input quality | Tactical — prompt-level thinking, not a systemic methodology |

*On Wardley Mapping and this methodology's lineage.* Wardley Mapping deserves more than a row in the table above. Its founding insight — that situational awareness requires making your assumptions about position, movement, and relationships explicit and visible — is philosophically the closest prior art to what this methodology attempts. The map analogy that runs through RFM is not borrowed from Wardley, but it is not independent of him either. It is convergent: two approaches that arrived at the same metaphor because the underlying insight is the same. Make your orientation legible. Reason from it explicitly. The author encountered Wardley's thinking directly in 2017 and that influence is real and honestly acknowledged here. What RFM attempts to add is the temporal discipline of reasoning before execution as a hard constraint, the explicit design of the reasoning artifact for both humans and LLMs simultaneously, and the co-authorship frame that makes that collaboration a practice. These are extensions into territory Wardley's framework did not need to address. They are offered in that spirit — as additions, not corrections.

**The gap:** none of these treat reasoning as a hierarchical, living, curated artifact designed simultaneously for human understanding and LLM execution — maintained at every level, from strategic intent to individual module, through the full life of a system.

---

## The Options Considered

**1. Better documentation practice combined with RAG**

More rigorous ADRs, wikis, enforced commenting standards, made accessible to LLMs through retrieval. Rejected because documentation captures *what* was decided, rarely *why*. It doesn't make assumptions explicit, doesn't record hard lessons, doesn't force reasoning through alternatives. RAG on top of poor documentation retrieves poor documentation faster. The structure of the artifact matters as much as its existence.

**2. Rely on increasingly capable LLMs**

If models become powerful enough, perhaps context matters less. Rejected because capability without context shifts the failure mode but doesn't eliminate it. A more powerful model makes more convincing mistakes. Research consistently shows that output quality is determined upstream of model capability — by the quality and structure of the context provided.

**3. Test and constraint driven development**

Enough tests and guardrails to control output without understanding internals. Rejected because as Dijkstra observed, testing shows presence of bugs, never absence. Control without comprehension scales poorly with complexity. You end up replacing understanding with surveillance.

---

## The Chosen Direction and Why

**On the central commitment**

The goal is facilitated joint reasoning between human and LLM. Everything that follows — the reasoning artifact at the center, the temporal discipline of reasoning before execution, the fractal structure, the enforced curation — serves that goal. It is not about elegant documentation. It is about creating a shared interface through which both human and LLM contribute, execute, and stay honest.

The methodology places the reasoning artifact at the center of software development practice. Not the code. Not the tests. Not the documentation. The reasoning — explicit, hierarchical, curated, and designed from the outset to serve both humans and LLMs simultaneously.

The reasoning document is not a record of decisions. It is where decisions are made. A record is written after the fact and drifts. A decision-making interface is consulted before action and stays alive because it must. Every change to a system begins with a change to the reasoning document at the appropriate level. Code is the derivative. The document is the source.

**On the structure**

The same eight sections, the same discipline, the same navigational practice — whether you are at the top of the hierarchy or deep inside a single module. Think of a regular map: a country map and a street map use identical discipline at different resolution. The street map is a module of the city map — each complete at its own resolution, each connected to the level above it. This property — the same structure governing at every level — is what mathematicians call fractal. The term is precise and worth keeping: a fractal is not just a pattern that repeats, it is a pattern whose rules apply at every level. That is exactly what the reasoning document hierarchy is.

**On keeping it alive**

The document is kept alive through enforced curation. Not just addition but reduction. What has evolved? What can be removed? What needs replacing? A document that only grows is a document that is already dying. The pressure of constraint is a feature, not a limitation.

A healthy document breathes — it expands when new signal arrives and contracts when old signal has been metabolized. Contraction has two legitimate forms: graduation, where a hard lesson or open question has been fully absorbed and transforms into an assumption or a change to Chosen Direction; and expiry, where an entry described a stage the project has passed and is honestly removed. Both are curation. Neither is loss.

Hard lessons are first-class citizens. What was tried, why it seemed right, what failed, and what that means going forward carries as much reasoning value as what succeeded. A methodology that doesn't capture failure will repeat it.

Every change to a derivative — code, prompt, operational document — begins with a change to its source reasoning document. Derivatives don't merely stay connected to the reasoning; they are created from it. That is the right order, and maintaining it is what curation means in practice.

**On execution mode and the two-mode design:**

The methodology operates in two modes. Reasoning mode is the default: reasoning precedes execution, the document is the source, every change begins at the appropriate level of the hierarchy. Execution mode is invoked when delivery pressure makes the full reasoning discipline locally unacceptable — a deadline, a sprint, a time-boxed commitment. Execution mode is not a degraded version of the methodology. It is the correct response to a specific condition, provided the reasoning documents are sufficiently complete before pressure hits. The reasoning documents then function as Commander's Intent: the direction, boundaries, and assumptions are established; execution adapts within that frame without stopping to re-reason. The discipline shifts from reasoning before every action to executing within established reasoning. What execution mode requires is minimal capture: a running record of deviations from established reasoning, conscious deferrals, and broken assumptions — enough to make the return to reasoning mode honest rather than reconstructed from code. This is a Chesterton's Fence log: before removing a fence under pressure, note that it was removed and why. The return to reasoning mode after pressure lifts is not optional. It is where execution mode's debts are paid.

**On the question of future autonomy:**

The most common objection to this approach is that increasingly capable and autonomous AI systems will eventually make it unnecessary. This misunderstands what the reasoning document is for. It is not a workaround for limited AI capability. It is the expression of human intent, human values, and human context applied to a specific problem. No level of AI autonomy removes the need for that — it only changes who executes once the intent is clear.

In fact, the more autonomous the system, the more critical the reasoning document becomes. A highly capable agent acting on vague or implicit intent doesn't fail cautiously. It fails confidently, at scale, and in ways that are difficult to trace or reverse.

Autonomy raises the stakes for clarity. It does not lower them.

The reasoning document is the deterministic anchor. Agentic execution is where probabilistic reasoning is permitted — but within boundaries that have been explicitly reasoned, not assumed.

**On the name:**

The methodology is called Reasoning-First Methodology, abbreviated RFM. The abbreviation carries a deliberate resonance with RTFM — that is not accidental and is kept. The full name is accurate and directional; it captures the temporal discipline that is the methodology's founding constraint. It does not explicitly name the joint human/LLM design — a conscious choice. Simpler names travel better, and the joint design is carried sufficiently by the documents themselves. Naming the tool in the methodology's title would date it; the practice will outlast the current form of the collaboration. The name is considered settled.

---

## The Boundaries

This methodology is explicitly not:

**A software development tool.** No specific platform is prescribed. However the methodology has one minimum technical requirement: reasoning documents must be maintained in a format and location accessible to the LLM working within the system. Markdown is the recommended format — human-readable, LLM-readable, version-controllable, and tool-agnostic. Where the document lives matters only insofar as it must be reachable by both human and machine.

**A replacement for technical expertise.** The methodology does not eliminate the need for skilled developers, architects, or domain experts. It gives their expertise a structure to live in and a way to survive beyond the person who holds it.

**A documentation standard.** This is not about writing more or better documentation. It is about a fundamental shift in what the primary artifact of software development is. Documentation describes a system after the fact. A reasoning document precedes and drives it.

**A methodology for AI development.** It does not prescribe how to build, train, or fine-tune AI models. It prescribes how to reason about and direct their use within a system.

**A finished system.** The methodology itself is subject to its own principles. It is a living reasoning artifact. It will evolve, be curated, and accumulate hard lessons. Version 0.0.0.1 is not version final.

**Designed to impose discipline on a team that won't bring it.** The deliberate return mode of curation requires a human who has a natural affinity for this kind of reflection. That is a people constraint, not a process gap. A team without such a person can follow the triggered mode but will gradually stop returning deliberately. The methodology will technically persist but quietly degrade. This is not a failure of the methodology. It is a boundary condition of its use.

**Designed to maintain full discipline under acute delivery pressure.** Delivery pressure is a specific, common condition under which the methodology's full discipline is at risk — not because teams stop believing in it, but because the local cost of the reasoning step becomes unacceptable when deadlines are close. This is distinct from the people constraint above: it affects willing teams in adverse conditions. The two-mode design — reasoning mode as default, execution mode under pressure — is the methodology's working hypothesis for this condition. It is not yet a tested practice. Teams operating under sustained delivery pressure without established reasoning documents should treat this as a known risk, not a solved problem.

---

## The Open Questions

These are genuinely unresolved. They are not weaknesses — they are the honest frontier of the methodology. Some will be answered through practice. Others may reshape the methodology itself.

**1. The drift problem.**

How does the reasoning document stay connected to the system it describes? The methodology is designed to prevent documentation drift — but it is not immune to it. What mechanisms, rituals, or technical constraints ensure the document evolves with the system rather than describing a past that no longer exists? This is the hardest open question.

Applying the methodology from inception — reasoning before any code exists — is the only reliable prevention. Reconstructing reasoning from existing code produces plausible documents, but not necessarily true ones. There is no reliable cure for drift once it has set in. Whether the discipline holds at scale and over time remains genuinely open.

The research literature has named and studied this problem extensively under two terms. Architectural knowledge vaporization describes the loss of the rationale behind design decisions — the alternatives considered, the trade-offs made, the assumptions held — which exists primarily in the minds of creators and disappears when they move on or when time passes. Architecture erosion describes the downstream consequence: the silent, cumulative divergence between the intended design and the implemented reality, documented in real systems at rates ranging from 26% to 94%. The field's proposed solutions — better tooling, automated conformance checking, architectural governance frameworks — address drift after it has begun, by detecting the gap between documentation and code. None address the root cause: the reasoning behind decisions is not captured in the first place, so there is nothing for tooling to enforce against. RFM's claim is that drift begins not when code diverges from documentation, but when reasoning disappears from the artifact that is supposed to carry it. Making reasoning the primary artifact — before any code exists — is the only prevention that operates at the right level. Whether that prevention holds at scale and over time is what remains open.

**2. The minimum viable document.**

How short can a reasoning document be and still work? The methodology must not become a bureaucratic burden. There is a minimum below which the document loses its value — and a maximum above which it becomes the thing it was designed to replace. Where are those boundaries in practice?

In practice, the binding constraint is rarely the floor. Empirical evidence from software practice points to a different dominant failure mode: documentation is most commonly abandoned not because too little was written, but because too much was written for the wrong reason — created to satisfy a requirement, not to capture reasoning, and consequently never maintained. This pattern is well-documented across industries under the name compliance theater: the appearance of discipline without its substance. A document produced because it was required will be treated as a deliverable. A document produced because the reasoning demanded it will be treated as a living artifact. RFM's founding constraint — reasoning before execution — is the structural answer to this failure mode. A document that emerges from genuine reasoning has a reason to stay alive: every change to the system begins with a change to it. A compliance document has no such anchor. It is written once, filed, and quietly abandoned. The minimum viable document question is therefore not primarily about length. It is about origin: was this document reasoned into existence, or required into existence?

**3. The onboarding question.**

How does someone encounter this methodology for the first time and understand its value quickly enough to adopt it? The feedback loop for good reasoning is slow and invisible. The feedback loop for coding is fast and visible. Bridging that gap is a change management challenge that the methodology does not yet fully answer.

The document map — a lightweight navigation table at the top of every top-level reasoning document — is a partial answer. It gives a new collaborator immediate orientation without requiring them to read everything first. A more powerful component is the LLM itself — a partner with a well-designed system prompt that understands the methodology and can guide a newcomer through it actively. The LLM becomes part of the onboarding infrastructure, not just a tool within it. The deeper question — how to convey the value of the methodology quickly enough to motivate adoption — remains open.

The deepest layer of the onboarding question is not about understanding the methodology — it is about developing the collaborative posture that makes the methodology's value accessible. The methodology currently assumes a human who already works in a particular way: thinking out loud rather than stating destinations, giving permission to uncertainty rather than demanding confident answers, pushing back with genuine curiosity rather than authority, asking "so what?" of their own best ideas before anyone else can. These are not personality traits — they are practices, and practices can be taught. A methodology that describes what documents to write but not how to show up to the collaboration is incomplete. This layer of the onboarding question is undesigned.

A related and more immediate question is the division of labor between human and LLM in the drafting process itself. The LLM is faster and more precise at formulating and editing text. The human holds the judgment about whether a word or phrase actually lands for a first-time reader. The natural working mode — LLM proposes and executes, human judges and confirms — plays to both strengths. Whether this division should be explicitly described in the methodology, or left as an emergent practice, is unresolved.

**4. The autonomy boundary.**

As agentic systems become more capable, where exactly is the boundary between what must be human-reasoned and what can be delegated? The methodology holds that human intent cannot be delegated — but the precise location of that boundary will need to be tested and refined in practice.

Collaboration between human and LLM reveals this boundary more concretely than theory can. The LLM contributes landscape knowledge, structure, red teaming, and pattern recognition. The human contributes instinct, synthesis, judgment, and the discipline to challenge their own best ideas. The boundary is not a line — it is a division of cognitive labor that emerges from the work itself. Formalizing that division is still open.

**5. The deterministic/probabilistic design question.**

At the execution level this question is largely resolved: structure and guarantees are owned by deterministic code, meaning and language by probabilistic LLM reasoning. At the reasoning document level the answer is similarly clear: boundaries are deterministic anchors, open questions are the legitimate home of uncertainty, assumptions hold until evidence breaks them. What remains genuinely open is the agentic boundary — how a highly autonomous system should treat the reasoning document when acting without human oversight. That question connects directly to Open Question 4 and will likely be resolved together with it.

**6. The evolutionary stage problem.**

The methodology is currently designed and validated at genesis stage — a single practitioner, early structure, everything still surprising. It is an open question how the discipline needs to change as a project matures through later stages of development. The Hard Lessons section is where this strain will show first: it only grows, it is cross-cutting, and curation becomes harder as the project ages. The hunch is that Hard Lessons eventually graduates from a document section into a separate living artifact, that lessons can be retired when fully absorbed into assumptions or team practice, and that the methodology itself needs to describe these transition points explicitly. This has not been designed yet. It needs to be — before the methodology is adopted at scale.

One boundary is already clear: the moment code precedes reasoning, the methodology is in recovery mode rather than prevention mode. Reconstructed reasoning produces plausible documents, but not necessarily true ones. What changes at each subsequent stage beyond that boundary is still open.

Research on software project lifecycles confirms the general pattern: practices and structures designed for genesis stage break in characteristic ways as teams and projects scale. What works for five engineers often fails at twenty; what holds in inception frequently requires redesign by growth stage. But that research addresses team structure, process frameworks, and tooling — none of it asks what happens to reasoning discipline specifically as a project matures, because none of it treats reasoning as the primary artifact. RFM is the first framework that makes this a distinct, nameable question. The fractal structure is the intended answer: as documents strain, new modules emerge; as modules emerge, sub-teams take them on with the top-level reasoning as anchor and adjacent module documents as context. The reasoning load is distributed by design, not concentrated. But whether this mechanism actually holds under real team growth — whether curation discipline survives handoffs, whether the fractal structure remains navigable as the hierarchy deepens, whether new contributors reason the way the methodology requires rather than drift toward execution — is precisely what has not been tested. These are open research questions that RFM surfaces and prior work has not studied, because they only become visible when reasoning is treated as the governing artifact rather than a byproduct of development.

**7. The lifecycle of document content.**

How does content exit or transform within a reasoning document over time? Hard lessons elevate into principles, open questions resolve and close, assumptions break or prove out. The direction of travel for individual entries is implicit in the curation principle but not yet described. A methodology that only adds content will eventually become the thing it was designed to replace. The explicit lifecycle — how entries graduate, transform, and exit — needs to be designed before the methodology is adopted at scale.

**8. The minimal capture discipline.**

Execution mode requires minimal capture — a record of deviations, deferrals, and broken assumptions sufficient to make the return to reasoning mode honest. What this looks like in practice is undesigned. How short can it be and still serve its purpose? What is the right artifact — a section appended to the reasoning document, a separate log, something else? How does a team distinguish a deviation worth capturing from noise? And what does the return-to-reasoning-mode session actually look like — what is its protocol, its output, its quality gate? These questions are unresolved. The two-mode design is a working hypothesis, not a tested practice.

**9. The sweep prompt design.**

The sweep prompt — a concentrated version of the traveling prompt designed for explicit document review sessions — has not yet been formally designed. The practice of deliberate return with critical intent is clear; the artifact that supports it is not. This is the next design work after the traveling prompt is stable.

---

## Hard Lessons

**Methodology design**

**1. The document structure emerged from failure modes, not from best practices.**

The most robust design decision in the methodology was to derive the eight sections by asking "what causes humans and LLMs to fail?" rather than "what should a good document contain?" Designing from failure is more rigorous than designing from aspiration. This principle should be applied recursively — to every module document that follows.

**2. The methodology is universal. The operational document is domain-specific.**

The eight-section reasoning document applies to any domain where structured thinking precedes execution — software, architecture, investing, art. The operational document — constants, interfaces, procedures, known values — exists because some domains, software being the primary example, have hard execution contracts that require their own artifact. The methodology-level principle stays clean and universal: reasoning is the primary artifact. There is no ninth section. There is a second document type — but only when the domain demands it.

**3. Existing approaches were closer than expected — and further than expected.**

Many pieces of this methodology exist in scattered form across prior movements. The gap is real but the lineage is rich. This matters because the right framing is not "we invented something new" but "we completed something that was already trying to emerge." The latter is more honest and more credible.

**4. The quality gate is continuous, not periodic.**

The quality gate was originally imagined as a separate LLM evaluator invoked periodically to check documents for sharpness, hidden assumptions, completeness, and internal consistency. Practice revealed a different answer: an LLM working within the methodology, guided by a correctly designed system prompt, flags leakage and hidden assumptions in the moment — not in a separate review cycle. The quality gate is the traveling prompt doing its job. A deliberate sweep session is a concentrated version of this practice, not a separate mechanism.

**Document discipline**

**5. The document map belongs at the top of every top-level reasoning document when a document landscape exists to navigate.**

A reader or LLM encountering a project for the first time cannot orient from the top-level reasoning document alone — the document describes decisions but not the document landscape around it. A lightweight map listing what documents exist, their type, and their scope should appear before The Problem in every top-level reasoning document. The map is only meaningful when a document landscape exists to navigate — a single-document system has nothing to map. Navigation is not reasoning, but it is a prerequisite for reasoning about the right thing. The document map is the one place where real version numbers belong — it is the snapshot of the system's current state. Wildcards (`v*`) in a map defeat its purpose: a map that doesn't tell you which version exists cannot be used to detect drift. Individual cross-document references, by contrast, should never include version numbers.

**6. File naming discipline is a prerequisite for LLM orientation.**

Inconsistent file names force an LLM to infer document type and scope from content rather than from the name itself. The naming convention for RFM documents is: `RFM_[type]_[descriptor]_v*.md`, where type is one of: `top_level_reasoning`, `module_reasoning`, `prompts_reasoning`, `traveling_prompt`, `sweep_prompt`, `operational`. The `RFM_` prefix signals methodology context immediately. The type is unambiguous. The version is explicit. Deviating from this convention degrades LLM orientation before a single line is read. Archive filenames carry the version suffix (`RFM_prompts_reasoning_v0.0.0.5.md`) for history. Project filenames drop it (`RFM_prompts_reasoning.md`) — the Project is always current by definition, and the version is visible in the document header.

**7. Cross-document references use document names, never version numbers.**

Hardcoding a version number in a cross-document reference creates a maintenance tax: every version bump to the referenced document requires updates in every document that references it. The reference should be to the document by name only. The version is implicit — you always read the current version. The document map carries the version snapshot. Individual references do not.

**8. Document strain is diagnostic, not a writing problem.**

When a section starts straining — too many options, too much detail, too many edge cases — that is not a signal to write more carefully. It is a signal that something needs to become its own module in the hierarchy. The top level document has a natural completion condition: every major decision is justified but no implementation detail has leaked in. The module structure is not designed upfront. It emerges from the writing. The hierarchy reveals itself through the strain.

**9. Assumptions state reasoning principles, not implementation details.**

An assumption that references implementation — a specific function, a pass number, a config flag — has leaked the wrong level of abstraction into the wrong section. Assumptions should be testable beliefs about the world: why something is true, what would break if it weren't. Implementation details belong in Chosen Direction or module documents.

**10. Hard lessons are not permanent residents — they have a lifecycle.**

The Hard Lessons section accumulates entries but has no mechanism for them to exit. Some lessons, once fully absorbed, should graduate — the insight transforms into an assumption or shapes Chosen Direction, and the original entry is removed. Others describe a stage the project has passed and should expire — removed honestly, without replacement. A lesson that has been metabolized but remains in Hard Lessons creates false weight: the section implies these are active lessons. Once a lesson is no longer active, keeping it is clutter, not memory.

**11. The drift problem is not solved by the methodology — it is the methodology's greatest vulnerability.**

The methodology was designed to prevent documentation drift. But the reasoning document itself can drift from the system it describes. Naming this problem is not solving it. This lesson must stay visible until a genuine answer exists.

**LLM behavior**

**12. LLMs must never summarize reasoning documents unless explicitly asked.**

When an LLM edits a reasoning document, there is a structural tendency to tidy, condense, and inadvertently lose nuance in the process. A summarized reasoning document is a degraded reasoning document — it may read more cleanly but it carries less signal. In larger projects this tendency can derail work subtly and cumulatively, with important details lost across multiple edit cycles. The methodology requires that any LLM working with reasoning documents makes surgical edits only — touching exclusively what was explicitly requested, showing what changed, and leaving everything else intact.

**13. Long conversations with LLMs accumulate drift.**

Even a disciplined LLM develops bias over a long conversation — toward ideas that emerged in that conversation, toward framings that felt productive, toward connections that feel natural but weren't explicitly decided. This is subtle and hard to detect from inside the conversation. Drift is more dangerous than context window limits — it is invisible and cumulative. Two mitigations: first, the reasoning document should be complete enough to onboard a fresh LLM without loss — if it can't, the document isn't finished. Second, deliberately starting a new conversation with only the reasoning document as context is a useful quality check. A fresh LLM that misunderstands the direction reveals a gap in the document, not a gap in the conversation.

**14. The LLM must verify against the document before asserting absence.**

In a long conversation, the LLM accumulates conversational context that can substitute for document content without either party noticing. The failure mode is subtle: the LLM flags a gap that isn't there, or confirms something that has drifted from the document. Before asserting that something is missing or present, verify against the document directly. Conversational memory is not a reliable proxy for document content.

**15. Methodology assumptions belong in a system prompt, not in every document.**

An early instinct when applying the methodology is to inherit methodology-level assumptions into every reasoning document. This creates noise, not signal. Assumptions that are constant across all documents — the rules of the methodology itself — should live in a single LLM system prompt that travels silently with every interaction. Only assumptions that are genuinely local and specific to a particular decision belong in the reasoning document. This keeps documents lean, focused, and honest.

**Human-LLM collaboration**

**16. Enthusiasm without red teaming produces fragile thinking.**

A methodology — or any reasoning document — only becomes robust when honest criticism is made explicit: not just "does this work?" but "what would break this?" The red team function must be built into the process, not added later. A reasoning document that has never been challenged is a reasoning document that hasn't been tested.

**17. Capture while sharp — capture is not the same as processing.**

An insight that is parked rather than captured immediately degrades. What returns later is a blurred version of the original thought, or nothing at all. The discipline is: capture immediately in the right place — a single sentence is enough to hold the signal. Processing — deciding what it means, where it goes, how it connects — can wait. The document holds the thought so the conversation can continue. Parking is not the same as noting.

**18. Session-born shorthands are candidates for the document, not automatic entries.**

A session-born shorthand is a term that emerged between two collaborators and carries the session context that gave it meaning. When it enters a document, it meets a reader who wasn't in that session. Before capturing one, apply this test: does it carry its meaning without the conversation behind it? If not, spell it out instead. "Fractal" and "deterministic anchor" are examples of session-born shorthands that did useful work in session and were promoted into documents without that test being applied.

**Execution practice**

**19. The worked example is never optional — at any stage of the methodology's development.**

Theory without ground truth is hypothesis. Applying the methodology from inception — reasoning before any code exists — proves the chain in both directions: reasoning document to operational document to code, with traceability at every step and no undocumented judgment calls made during implementation. Applying it to existing systems reveals that reconstructed reasoning produces plausible documents but not necessarily true ones. Both directions of experience are necessary. The worked example is never optional — at any stage of the methodology's development.

**20. RFM's value is gap-legibility, not gap-elimination.**

A well-reasoned document hierarchy will not prevent all gaps from appearing during execution. What it does is make gaps visible in the right place — as explicit reasoning debts, open questions, or provisional specifications — rather than letting them hide in code where they harden silently into undocumented decisions. A first application that produces no visible gaps has probably not been honest. A first application whose gaps surface at the reasoning level and are named there rather than discovered late in implementation is working correctly.

---

*v0.0.0.25 // top_level_document // [living]*
*the reasoning arrived before the structure did*
*that was the right order*
