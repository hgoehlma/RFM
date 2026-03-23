# Reasoning-First Methodology
`v0.0.0.20` // `top_level_document` // [living]

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

6. **Curation must be deliberate, not optional.** Curation has two modes and both are required. The first is triggered — something accumulates, strains, or surfaces in use, and draws you back to the document. The second is deliberate return — you come back without a specific trigger, to ask whether the document still reflects what you know. Neither mode can be replaced by a scheduled rhythm; a time-triggered cadence risks becoming performative rather than genuine. The methodology only holds if both modes are practiced as discipline, not suggestion.

7. **A reasoning document designed explicitly for both humans and LLMs simultaneously outperforms one designed for either alone.** This is not a natural default. It requires conscious design. True collaboration between human and LLM is not a side benefit of the methodology — it is the mechanism by which the methodology works. The LLM holds the co-author role in the reasoning document — it is not a tool that executes within it.

8. **Hard lessons are as valuable as successes.** What failed, and why, carries as much reasoning value as what worked. A methodology that doesn't capture failure will repeat it.

9. **Document strain is diagnostic of hierarchy.** When a section strains under its own weight — too many options, too much detail, too many edge cases — that is a signal to branch into a new module, not a signal to write more carefully. The module structure is not designed upfront. It emerges from the writing. The hierarchy reveals itself through strain.

10. **In domains where execution has hard contracts — software being the primary example — the reasoning document is accompanied by an operational document.** The operational document carries constants, interfaces, procedures, and known values. It is a derivative of the reasoning, not a replacement for it. The methodology stays universal. The operational document is domain-specific.

11. **Rich reasoning context creates a virtuous cycle — when the discipline holds.** When an LLM works within a well-reasoned document, its downstream execution — code generation, system design, prompt construction — is more correct and less prone to hallucination. Higher correctness produces better output for the human to reason against. Better joint reasoning produces richer documents. Richer documents improve the next round of LLM execution. The loop is self-reinforcing — but only when both parties hold the discipline: the LLM guided by a correctly designed system prompt, the human committed to reasoning before execution and curating honestly. When either breaks, the loop degrades. This is the mechanism by which the methodology works — not just a benefit of it.

---

## The Landscape

The problem of meaning in software is not unrecognized. Several movements have addressed parts of it:

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **Agile** | Shifted focus from documentation-heavy waterfall to working software and human collaboration | Solved delivery rigidity but traded away reasoning continuity in the process |
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

The goal is facilitated joint reasoning between human and LLM. Everything that follows — the reasoning artifact at the center, the temporal discipline of reasoning before execution, the fractal structure, the enforced curation — serves that goal. It is not about elegant documentation. It is about creating a shared interface through which both human and LLM contribute, execute, and stay honest.

The methodology places the reasoning artifact at the center of software development practice. Not the code. Not the tests. Not the documentation. The reasoning — explicit, hierarchical, curated, and designed from the outset to serve both humans and LLMs simultaneously.

Every change to a system begins with a change to the reasoning document at the appropriate level. Code is the derivative. The document is the source.

The reasoning document is not a record of decisions. It is where decisions are made. This distinction matters: a record is written after the fact and drifts. A decision-making interface is consulted before action and stays alive because it must.

The same eight sections, the same discipline, the same navigational practice — whether you are at the top of the hierarchy or deep inside a single module. A useful image: a regular map. A country map and a street map use identical discipline at different resolution. You always know where you are, what the boundaries are, what connects to what. Zoom in and the practice is identical — and the maps connect. The street map is a module of the city map. This is what the reasoning document hierarchy is: a nested set of maps, each complete at its own resolution, each connected to the level above it. This property — the same structure governing at every level of resolution — is what mathematicians call fractal. The term is precise and worth keeping: a fractal is not just a pattern that repeats, it is a pattern whose rules apply at every level. That is exactly what the reasoning document hierarchy is.

The document is kept alive through enforced curation. Not just addition but reduction. What has evolved? What can be removed? What needs replacing? A document that only grows is a document that is already dying. The pressure of constraint is a feature, not a limitation.

A healthy document breathes — it expands when new signal arrives and contracts when old signal has been metabolized. Contraction has two legitimate forms: graduation, where a hard lesson or open question has been fully absorbed and transforms into an assumption or a change to Chosen Direction; and expiry, where an entry described a stage the project has passed and is honestly removed. Both are curation. Neither is loss.

Hard lessons are first-class citizens. What was tried, why it seemed right, what failed, and what that means going forward carries as much reasoning value as what succeeded. A methodology that doesn't capture failure will repeat it.

Every change to a derivative — code, prompt, operational document — requires a corresponding change to its source reasoning document. A derivative that has moved without its source is drift by another name.

**On execution mode and the two-mode design:**

The methodology operates in two modes. Reasoning mode is the default: reasoning precedes execution, the document is the source, every change begins at the appropriate level of the hierarchy. Execution mode is invoked when delivery pressure makes the full reasoning discipline locally unacceptable — a deadline, a sprint, a time-boxed commitment. Execution mode is not a degraded version of the methodology. It is the correct response to a specific condition, provided the reasoning documents are sufficiently complete before pressure hits. The reasoning documents then function as Commander's Intent: the direction, boundaries, and assumptions are established; execution adapts within that frame without stopping to re-reason. The discipline shifts from reasoning before every action to executing within established reasoning. What execution mode requires is minimal capture: a running record of deviations from established reasoning, conscious deferrals, and broken assumptions — enough to make the return to reasoning mode honest rather than reconstructed from code. This is a Chesterton's Fence log: before removing a fence under pressure, note that it was removed and why. The return to reasoning mode after pressure lifts is not optional. It is where execution mode's debts are paid.

**On the question of future autonomy:**

The most common objection to this approach is that increasingly capable and autonomous AI systems will eventually make it unnecessary. This misunderstands what the reasoning document is for. It is not a workaround for limited AI capability. It is the expression of human intent, human values, and human context applied to a specific problem. No level of AI autonomy removes the need for that — it only changes who executes once the intent is clear.

In fact, the more autonomous the system, the more critical the reasoning document becomes. A highly capable agent acting on vague or implicit intent doesn't fail cautiously. It fails confidently, at scale, and in ways that are difficult to trace or reverse.

Autonomy raises the stakes for clarity. It does not lower them.

The reasoning document is the deterministic anchor. Agentic execution is where probabilistic reasoning is permitted — but within boundaries that have been explicitly reasoned, not assumed.

**On the top-level document in every session:**

The top-level reasoning document should always be present in any working session. It is the map, the anchor, and the update target. Without it, module-level work proceeds without orientation, and the document map cannot be updated when changes are made.

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

How does the reasoning document stay connected to the code that follows? The methodology is designed to solve documentation drift — but it is not immune to it. What mechanisms, rituals, or technical constraints ensure the document evolves with the system rather than describing a past that no longer exists? This is the hardest open question.

A retrofit exercise — applying the methodology to existing code — demonstrated the most severe form of this problem: reasoning reconstructed from code rather than code derived from reasoning. Reconstruction produces plausible documents but not necessarily true ones. The discipline of reasoning-first is the only prevention. There is no reliable cure. Two validation exercises are complete — Hello World (reasoning only, no code) and a small software retrofit. The greenfield exercise is now complete: reasoning first, then code, with the chain holding in both directions. Drift prevention rather than drift management is now demonstrated — but whether the discipline holds at scale and over time remains the open question.

**2. The minimum viable document.**

How short can a reasoning document be and still work? The methodology must not become a bureaucratic burden. There is a minimum below which the document loses its value — and a maximum above which it becomes the thing it was designed to replace. Where are those boundaries in practice?

**3. The onboarding question.**

How does someone encounter this methodology for the first time and understand its value quickly enough to adopt it? The feedback loop for good reasoning is slow and invisible. The feedback loop for coding is fast and visible. Bridging that gap is a change management challenge that the methodology does not yet fully answer.

The document map — a lightweight navigation table at the top of every top-level reasoning document — is a partial answer. It gives a new collaborator immediate orientation without requiring them to read everything first. A more powerful component is the LLM itself — a partner with a well-designed system prompt that understands the methodology and can guide a newcomer through it actively. The LLM becomes part of the onboarding infrastructure, not just a tool within it. The deeper question — how to convey the value of the methodology quickly enough to motivate adoption — remains open.

The deepest layer of the onboarding question is not about understanding the methodology — it is about developing the collaborative posture that makes the methodology's value accessible. The methodology currently assumes a human who already works in a particular way: thinking out loud rather than stating destinations, giving permission to uncertainty rather than demanding confident answers, pushing back with genuine curiosity rather than authority, asking "so what?" of their own best ideas before anyone else can. These are not personality traits — they are practices, and practices can be taught. A methodology that describes what documents to write but not how to show up to the collaboration is incomplete. This layer of the onboarding question is undesigned.

A related and more immediate question is the division of labor between human and LLM in the drafting process itself. The LLM is faster and more precise at formulating and editing text. The human holds the judgment about whether a word or phrase actually lands for a first-time reader. The natural working mode — LLM proposes and executes, human judges and confirms — plays to both strengths. Whether this division should be explicitly described in the methodology, or left as an emergent practice, is unresolved.

**4. The quality gate.**

The quality gate was originally imagined as a separate LLM evaluator invoked periodically to check documents for sharpness, hidden assumptions, completeness, and internal consistency. The sweep work revealed a different answer: the quality gate is the system prompt doing its job continuously. An LLM working within the methodology, guided by the right principles, flags leakage and hidden assumptions in the moment — not in a separate review cycle. The sweep prompt is a concentrated version of this for explicit review sessions. The design of both remains open — but the architecture is clearer than it was.

**5. The autonomy boundary.**

As agentic systems become more capable, where exactly is the boundary between what must be human-reasoned and what can be delegated? The methodology holds that human intent cannot be delegated — but the precise location of that boundary will need to be tested and refined in practice.

The work of building this methodology in collaboration with an LLM is itself evidence about the autonomy boundary. The LLM contributed landscape knowledge, structure, red teaming, and pattern recognition. The human contributed instinct, synthesis, judgment, and the courage to say "so what?" The boundary was not a line — it was a division of cognitive labor that emerged from the work itself. Formalizing that division is still open.

**6. The deterministic/probabilistic design question.**

At the execution level this question is largely resolved: structure and guarantees are owned by deterministic code, meaning and language by probabilistic LLM reasoning. At the reasoning document level the answer is emerging: boundaries are deterministic anchors, open questions are the legitimate home of uncertainty, assumptions hold until evidence breaks them, hard lessons are deterministic once written. What remains genuinely open is the agentic boundary — how a highly autonomous system should treat the reasoning document when acting without human oversight. That question connects directly to Open Question 5 and will likely be resolved together with it.

**7. The evolutionary stage problem.**

The methodology is currently designed and validated at genesis stage — a single practitioner, early structure, everything still surprising. It is an open question how the discipline needs to change as a project matures through custom built, product, and commodity stages (borrowing Wardley's evolution axis). The Hard Lessons section is the place where this strain will show first: it only grows, it is cross-cutting, and curation becomes harder as the project ages. The hunch is that Hard Lessons eventually graduates from a document section into a separate living artifact, that lessons can be retired when they are fully absorbed into assumptions or team practice, and that the methodology itself needs to describe these transition points explicitly. This has not been designed yet. It needs to be — before the methodology is adopted at scale.

The retrofit exercise added a new data point: a system past genesis stage, where reasoning documents are built from existing code, produces reconstructed reasoning rather than original reasoning. The quality difference is real but subtle — plausible rather than true. This suggests the evolutionary stage problem has a sharp early boundary: the moment code precedes reasoning, the methodology is already in recovery mode rather than prevention mode. What changes at each subsequent stage is still open — but the genesis boundary is now well-defined.

**8. The lifecycle of document content.**

How does content exit or transform within a reasoning document over time? Hard lessons elevate into principles, open questions resolve and close, assumptions break or prove out. The direction of travel for individual entries is implicit in the curation principle but not yet described. A methodology that only adds content will eventually become the thing it was designed to replace. The explicit lifecycle — how entries graduate, transform, and exit — needs to be designed before the methodology is adopted at scale.

**9. The minimal capture discipline.**

Execution mode requires minimal capture — a record of deviations, deferrals, and broken assumptions sufficient to make the return to reasoning mode honest. What this looks like in practice is undesigned. How short can it be and still serve its purpose? What is the right artifact — a section appended to the reasoning document, a separate log, something else? How does a team distinguish a deviation worth capturing from noise? And what does the return-to-reasoning-mode session actually look like — what is its protocol, its output, its quality gate? These questions are unresolved. The two-mode design is a working hypothesis, not a tested practice.

---

## Hard Lessons

**1. Enthusiasm without red teaming produces fragile thinking.**

Early in developing this methodology the ideas felt exciting and momentum built quickly. The methodology only became more robust when honest criticism was made explicit — asking not just "does this work?" but "what would break this?" The red team function must be built into the process, not added later. A reasoning document that has never been challenged is a reasoning document that hasn't been tested.

*Informed system prompt design.*

**2. The drift problem is not solved by the methodology — it is the methodology's greatest vulnerability.**

This methodology was designed to prevent documentation drift. But the reasoning document itself can drift from the system it describes. We named this problem but have not yet resolved it. Naming a problem is not solving it. This lesson must stay visible until a genuine answer exists.

**3. Existing approaches were closer than expected — and further than expected.**

Early assumption: nothing like this exists. Reality: many pieces exist in scattered form. The gap is real but the lineage is rich. This matters because it changes the pitch from "we invented something new" to "we completed something that was already trying to emerge." The latter is more honest and more credible.

**4. The name matters more than expected.**

The naming question was treated as secondary. It turned out to feel increasingly urgent as the methodology took shape. An idea without a name is hard to share, hard to remember, and hard to build community around. This should not be deprioritized.

**5. The document structure emerged from failure modes, not from best practices.**

The most robust design decision made was to derive the eight sections by asking "what causes humans and LLMs to fail?" rather than "what should a good document contain?" Designing from failure is more rigorous than designing from aspiration. This principle should be applied recursively — to every module document that follows.

*Informed system prompt design.*

**6. The worked example is never optional — at any stage of the methodology's development.**

Theory without ground truth is hypothesis. Two worked examples now exist — Hello World proved the document structure and fractal property with reasoning only; a software retrofit proved the methodology applies to existing systems and revealed that reconstruction is harder than prevention. The greenfield exercise is now complete — Hello World, built as working software derived directly from reasoning documents through an operational document. The chain held: reasoning document → operational document → code, with traceability in both directions and no undocumented judgment calls made during implementation. The operational document proved its weight as the clean interface between *why* and *how*. The worked example is never optional — at any stage of the methodology's development.

**7. Methodology assumptions belong in a system prompt, not in every document.**

When building the first worked example, an early instinct was to inherit methodology-level assumptions into every reasoning document. This creates noise, not signal. Assumptions that are constant across all documents — the rules of the methodology itself — should live in a single LLM system prompt that travels silently with every interaction. Only assumptions that are genuinely local and specific to a particular decision belong in the reasoning document. This keeps documents lean, focused, and honest. Discovered during the first worked example.

*Informed system prompt design.*

**8. LLMs must never summarize reasoning documents unless explicitly asked.**

When an LLM edits a reasoning document, there is a structural tendency to tidy, condense, and inadvertently lose nuance in the process. A summarized reasoning document is a degraded reasoning document — it may read more cleanly but it carries less signal. In larger projects this tendency can derail work subtly and cumulatively, with important details lost across multiple edit cycles. The methodology requires that any LLM working with reasoning documents makes surgical edits only — touching exclusively what was explicitly requested, showing what changed, and leaving everything else intact. This constraint should be part of the methodology system prompt.

*Informed system prompt design.*

**9. Document strain is diagnostic, not a writing problem.**

When a section starts straining — too many options, too much detail, too many edge cases — that is not a signal to write more carefully. It is a signal that something needs to become its own module in the hierarchy. The top level document has a natural completion condition: every major decision is justified but no implementation detail has leaked in. The module structure is not designed upfront. It emerges from the writing. The hierarchy reveals itself through the strain.

*Informed system prompt design and assumption.*

**10. Long conversations with LLMs accumulate drift.**

Even a disciplined LLM develops bias over a long conversation — toward ideas that emerged in that conversation, toward framings that felt productive, toward connections that feel natural but weren't explicitly decided. This is subtle and hard to detect from inside the conversation. Drift is more dangerous than context window limits — it is invisible and cumulative. Two mitigations: first, the reasoning document should be complete enough to onboard a fresh LLM without loss — if it can't, the document isn't finished. Second, deliberately starting a new conversation with only the reasoning document as context is a useful quality check. A fresh LLM that misunderstands the direction reveals a gap in the document, not a gap in the conversation.

*Informed system prompt design.*

**11. The LLM must verify against the document before asserting absence.**

In a long conversation, the LLM accumulates conversational context that can substitute for document content without either party noticing. The failure mode is subtle: the LLM flags a gap that isn't there, or confirms something that has drifted from the document. Before asserting that something is missing or present, verify against the document directly. Conversational memory is not a reliable proxy for document content. This has a direct implication for the system prompt: the LLM should be explicitly instructed to reread the relevant document before making claims about its contents.

*Informed system prompt design.*

**12. Capture while sharp — capture is not the same as processing.**

An insight that is parked rather than captured immediately degrades. What returns later is a blurred version of the original thought, or nothing at all. The discipline is: capture immediately in the right place — a single sentence is enough to hold the signal. Processing — deciding what it means, where it goes, how it connects — can wait. The document holds the thought so the conversation can continue. Parking is not the same as noting.

*Informed system prompt design.*

**13. Assumptions state reasoning principles, not implementation details.**

An assumption that references implementation — a specific function, a pass number, a config flag — has leaked the wrong level of abstraction into the wrong section. Assumptions should be testable beliefs about the world: why something is true, what would break if it weren't. Implementation details belong in Chosen Direction or module documents.

*Informed system prompt design.*

**14. The methodology is universal. The operational document is domain-specific.**

The eight-section reasoning document applies to any domain where structured thinking precedes execution — software, architecture, investing, art. The operational document — constants, interfaces, procedures, known values — is a software-specific derivative. It exists because software execution has hard contracts that other domains may not. The methodology-level principle stays clean and universal: reasoning is the primary artifact. The operational document is what that principle produces in domains where execution has hard contracts. There is no ninth section. There is a second document type — but only when the domain demands it.

*Informed system prompt design and assumption.*

**15. The document map belongs at the top of every top-level reasoning document when a document landscape exists to navigate.**

A reader or LLM encountering a project for the first time cannot orient from the top-level reasoning document alone — the document describes decisions but not the document landscape around it. A lightweight map listing what documents exist, their type, and their scope should appear before The Problem in every top-level reasoning document. The map is only meaningful when a document landscape exists to navigate — a single-document system has nothing to map. Navigation is not reasoning, but it is a prerequisite for reasoning about the right thing. The document map is the one place where real version numbers belong — it is the snapshot of the system's current state. Wildcards (`v*`) in a map defeat its purpose: a map that doesn't tell you which version exists cannot be used to detect drift. Individual cross-document references, by contrast, should never include version numbers — see Hard Lesson 17.

*Informed system prompt design.*

**16. File naming discipline is a prerequisite for LLM orientation.**

Inconsistent file names force an LLM to infer document type and scope from content rather than from the name itself. The naming convention for RFM documents is: `RFM_[type]_[descriptor]_v*.md`, where type is one of: `top_level_reasoning`, `module_reasoning`, `prompts_reasoning`, `traveling_prompt`, `sweep_prompt`, `operational`. The `RFM_` prefix signals methodology context immediately. The type is unambiguous. The version is explicit. Deviating from this convention degrades LLM orientation before a single line is read. Archive filenames carry the version suffix (`RFM_prompts_reasoning_v0.0.0.5.md`) for history. Project filenames drop it (`RFM_prompts_reasoning.md`) — the Project is always current by definition, and the version is visible in the document header.

**17. Cross-document references use document names, never version numbers.**

Hardcoding a version number in a cross-document reference creates a maintenance tax: every version bump to the referenced document requires updates in every document that references it. The reference should be to the document by name only. The version is implicit — you always read the current version. The document map carries the version snapshot. Individual references do not.

**18. Hard lessons are not permanent residents — they have a lifecycle.**

The Hard Lessons section accumulates entries but has no mechanism for them to exit. Some lessons, once fully absorbed, should graduate — the insight transforms into an assumption or shapes Chosen Direction, and the original entry is removed. Others describe a stage the project has passed and should expire — removed honestly, without replacement. A lesson that has been metabolized but remains in Hard Lessons creates false weight: the section implies these are active lessons. Once a lesson is no longer active, keeping it is clutter, not memory.

**19. Session-born shorthands are candidates for the document, not automatic entries.**

A session-born shorthand is a term that emerged between two collaborators and carries the session context that gave it meaning. When it enters a document, it meets a reader who wasn't in that session. Before capturing one, apply this test: does it carry its meaning without the conversation behind it? If not, spell it out instead. "Fractal" and "deterministic anchor" are examples of session-born shorthands that did useful work in session and were promoted into documents without that test being applied.

---

*v0.0.0.20 // top_level_document // [living]*
*the reasoning arrived before the structure did*
*that was the right order*
