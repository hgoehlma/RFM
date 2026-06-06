# Reasoning-First Methodology
`v0.1.4` // `top_level_reasoning` // [living]

---

## Document Map

| Document | Type | Version | What it carries |
|---|---|---|---|
| `RFM_top_level_reasoning.md` | Top-level reasoning | v0.1.4 | The methodology itself — problem, assumptions, landscape, chosen direction, hard lessons |
| `RFM_operational.md` | Operational | v0.1.1 | File naming conventions, document map maintenance, version discipline |
| `RFM_glossary.md` | Glossary | v0.1.0 | Disambiguation of terms that carry different meanings across reader contexts |
| `RFM_prompts_reasoning.md` | Prompts reasoning | v0.1.1 | The reasoning document governing all system prompt decisions |
| `RFM_traveling_prompt_reasoning.md` | Module reasoning | v0.0.0.5 | The reasoning document governing traveling prompt design decisions |
| `RFM_traveling_prompt.md` | Traveling system prompt | v0.1.0 | The system prompt that carries the methodology into every LLM conversation |
| `RFM_sweep_prompts_reasoning.md` | Module reasoning | v0.1.0 | The reasoning document governing sweep prompt design decisions |
| `RFM_sweep_prompt_structural.md` | Structural sweep prompt | v0.1.0 | The prompt artifact that activates the structural sweep — findings for ruling, not edits |
| `RFM_sweep_prompt_language.md` | Language sweep prompt | v0.1.0 | The prompt artifact that activates the language sweep — findings for ruling, not edits |
| `RFM_human_prompt_reasoning.md` | Module reasoning | v0.1.0 | Reasoning document governing human prompt design decisions |
| `RFM_human_prompt.md` | Human prompt | v0.0.0.5 | The prompt artifact for the human collaborator — practices that keep the co-author role alive across sessions |
| `RFM_guided_drafting_prompt_reasoning.md` | Module reasoning | v0.0.0.4 | Reasoning document governing guided drafting prompt design decisions |
| `RFM_guided_drafting_prompt_operational.md` | Operational | v0.0.0.3 | Deployment and artifact inventory for the guided drafting prompt module |
| `RFM_guided_drafting_prompt.md` | Guided drafting prompt | v0.0.0.3 | The prompt artifact that activates the guided drafting session — behavioral specification for the LLM, section intentions for the newcomer |
| `RFM_first_session_guidance.md` | First session guidance | v0.0.0.3 | Practical preparation for a newcomer's first guided drafting session — what to bring, what to expect, what to watch for |

---

## The Problem

Any domain where complex reasoning precedes execution faces the same failure: the thinking disappears. The decisions that shaped the outcome — why this approach, why not another, what was assumed, what failed — exist briefly and then vanish. What remains are the outputs. The meaning behind them does not survive.

Software development is where this methodology was built and where the consequences are currently most visible. Code is the output that remains — and code cannot explain itself. But the failure is not unique to software. Anywhere complex reasoning precedes execution, the same erasure happens.

This creates two compounding failures: humans joining or revisiting a system must reconstruct intent from structure. LLMs assisting with that system hallucinate because the context they need was never recorded.

Current tools address symptoms. None address the root cause: there is no disciplined practice for capturing and maintaining reasoning as a primary artifact, at every level of a system, designed to serve both humans and LLMs simultaneously.

**Why now?**

This problem is not new. What is new is that LLMs have made the consequences of missing reasoning suddenly visible and concrete. But the same LLMs also create the opportunity to fix it — because a well-reasoned document doesn't just help humans understand a system. It directly improves how AI executes within it. The problem and the solution have arrived together.

---

## The Assumptions

The following are believed to be true. They cannot all be fully proven yet. If any of them is wrong, the methodology needs to change.

**[AS-CIIL] - Context is irreducibly important for LLMs.** High signal reasoning context minimizes hallucination. This holds regardless of how capable models become — a better LLM with poor context will still underperform a modest LLM with rich context.

**[AS-AELN] - Abstraction will continue to evolve — and language is the next layer.** The history of software is one example of a broader pattern: every discipline involving complex execution has progressively raised its level of abstraction. LLMs make intention expressible in natural language. But no level of abstraction removes the need to articulate what you want. The thinking cannot be delegated.

**[AS-MOSA] - Modularity is the only sustainable architecture.** Monolithic systems resist change, learning, and maintenance. The reasoning document hierarchy should mirror and enforce modular thinking from the start.

**[AS-CACM] - Execution artifacts alone will never carry their own motivation.** The gap between what an artifact does and why it exists cannot be closed by improving the artifact itself. It requires a separate, connected reasoning document maintained proactively. In software, this gap is most visible — code can be read but not interrogated for intent. But the same gap exists in any domain where complex reasoning precedes execution.

**[AS-QEUP] - Quality of execution — human or AI — is upstream of the reasoning investment.** Thinking first is not overhead. It is the highest leverage point in the entire development process.

The assumptions above are beliefs about the domain — why the problem exists and why it persists. The assumptions below are beliefs about what the methodology itself must do to address it.

**[AS-CDNO] - Curation must be deliberate, not optional.** A reasoning document that is only visited when something forces it gradually stops being true. Deliberate return — coming back without a specific trigger — is as necessary as triggered curation. A time-triggered cadence risks becoming performative rather than genuine. Both modes must be practiced as discipline, not suggestion.

**[AS-RDHL] - A reasoning document designed explicitly for both humans and LLMs simultaneously outperforms one designed for either alone.** This is not a natural default. It requires conscious design.

**[AS-HLVS] - Hard lessons are as valuable as successes.** What failed, and why, carries as much reasoning value as what worked. A methodology that doesn't capture failure will repeat it.

**[AS-DSDH] - Document strain is diagnostic of hierarchy.** When a section strains under its own weight — too many options, too much detail, too many edge cases — that is a signal to branch into a new module, not a signal to write more carefully. The module structure is not designed upfront. It emerges from the writing. The hierarchy reveals itself through strain.

**[AS-DWHC] - Hard-contract domains require an operational document.** In domains where execution has hard contracts — software being the primary example — the reasoning document is accompanied by an operational document that carries constants, interfaces, procedures, and known values. It is a derivative of the reasoning, not a replacement for it.

**[AS-ADSR] - The reasoning discipline is self-reinforcing when held.** A well-reasoned document improves LLM execution. Better execution produces richer joint reasoning. Richer reasoning produces better documents. The loop degrades when either party breaks the discipline.

---

## The Landscape

What would it take to treat reasoning as a hierarchical, living artifact — maintained at every level of a system, designed simultaneously for human understanding and LLM execution? Several approaches have addressed parts of this problem.

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **Agile** | Shifted focus from documentation-heavy waterfall to working software and human collaboration | Solved delivery rigidity but traded away reasoning continuity in the process |
| **Domain-Driven Design** | Made meaning an explicit design target. Gave us Ubiquitous Language and Bounded Contexts | Presupposes reasoning already exists — it structures meaning, it doesn't generate or preserve it |
| **Clean Code / TDD** | Made quality and correctness first-class concerns | Correctness is not the same as meaning. A perfectly tested system can still be incomprehensible |
| **Wardley Mapping** | Made situational awareness and strategic reasoning explicit, visual, and owned | Stops at the strategic level. Doesn't cascade into a connected reasoning practice at every level of execution |
| **Peter Naur's "Programming as Theory Building"** | Argued that programming is primarily the activity of building a theory of the problem — code is a secondary artifact of that theory. Anticipates RFM's founding insight. | Stops at the individual programmer's mental model. No structural artifact for capturing the theory, no survival mechanism beyond the person who holds it, no LLM dimension. |
| **ADRs** | Capture individual decisions | Not hierarchical. Not designed for LLM consumption. Document conclusions, rarely the full reasoning journey |
| **Context Engineering** | Recognizes that LLM output quality depends on input quality | Tactical — prompt-level thinking, not a systemic methodology |

*On Wardley Mapping and this methodology's lineage.* Wardley Mapping deserves more than a row in the table above. Its founding insight — that situational awareness requires making your assumptions about position, movement, and relationships explicit and visible — is philosophically the closest prior art to what this methodology attempts. The map analogy that runs through RFM is not borrowed from Wardley, but it is not independent of him either. It is convergent: two approaches that arrived at the same metaphor because the underlying insight is the same. Make your orientation legible. Reason from it explicitly. The author encountered Wardley's thinking directly in 2017 and that influence is real and honestly acknowledged here. What RFM attempts to add is the temporal discipline of reasoning before execution as a hard constraint, the explicit design of the reasoning artifact for both humans and LLMs simultaneously, and the co-authorship frame that makes that collaboration a practice. These are extensions into territory Wardley's framework did not need to address. They are offered in that spirit — as additions, not corrections.

*On Peter Naur and this methodology's closest prior art.* Naur's 1985 essay "Programming as Theory Building" is the closest diagnosis of the problem RFM addresses. His core claim — that programming is primarily the activity of building a theory, and that code is a secondary artifact of that theory — anticipates RFM's founding insight directly. What his essay does not provide is a structural prescription: no artifact for capturing the theory, no mechanism for the theory to survive beyond the person who holds it, and no anticipation of the LLM dimension — that disciplined externalization in text is sufficient for a system with no tacit knowledge to execute from it. Naur named the problem. RFM attempts to answer it.

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

The methodology places the reasoning artifact at the center of any practice where complex reasoning precedes execution. Not the code. Not the tests. Not the documentation. The reasoning — explicit, hierarchical, curated, and designed from the outset to serve both humans and LLMs simultaneously.

The methodology is called Reasoning-First Methodology, abbreviated RFM. The abbreviation carries a deliberate resonance with RTFM — the exasperated instruction issued when someone acts without reading first. That resonance is not accidental and is kept. The reasoning document is not a record of decisions. It is where decisions are made. A record is written after the fact and drifts. A decision-making interface is consulted before action and stays alive because it must. Every change to a system begins with a change to the reasoning document at the appropriate level. The execution artifact is the derivative. The document is the source.

**On the governing co-authorship pattern**

The joint reasoning sequence — propose → reflect → converge → execute — is the governing pattern through which co-authorship operates in practice. Both parties contribute through the first three steps. At the execution step, the natural division applies: the LLM formulates and edits, the human judges and confirms. This sequence is not a convenience — it is what keeps co-authorship from collapsing into either deference or unilateral authorship. The full reasoning for its design is in `RFM_prompts_reasoning.md`.

**On the prompt system**

The methodology travels through a core pair of ambient artifacts and a corrective arm. The traveling prompt carries the discipline into every LLM conversation. The human prompt calibrates the human collaborator's posture across sessions. Together they ensure both sides of the collaboration are actively held. The two sweep prompts — structural and language — form the corrective arm: invoked deliberately during curation, each targeting a distinct failure class. Prevention and correction are different cognitive modes and require separate artifacts.

A fifth artifact exists for specific session types: the guided drafting prompt walks a newcomer through their first reasoning document section by section. It is not part of the ongoing methodology system — it serves a bounded use case.

The full reasoning for the prompt system design is in `RFM_prompts_reasoning.md`.

**On the structure**

The same eight sections, the same discipline, the same navigational practice — whether you are at the top of the hierarchy or deep inside a single module. Think of a geographic map: a country map and a street map use identical discipline at different resolution. The street map is a module of the country map — each complete at its own resolution, each connected to the level above it. This property — the same structure governing at every level — is what mathematicians call fractal. The term is precise and worth keeping: a fractal is not just a pattern that repeats, it is a pattern whose rules apply at every level. That is exactly what the reasoning document hierarchy is.

**On keeping it alive**

The document is kept alive through enforced curation. Not just addition but reduction. What has evolved? What can be removed? What needs replacing? A document that only grows is a document that is already dying. The pressure of constraint is a feature, not a limitation.

A healthy document expands when new signal arrives and contracts when old signal has been absorbed into assumptions or practice. Contraction has two legitimate forms: graduation, where a hard lesson or open question has been fully absorbed and its reasoning travels to the appropriate destination — an assumption, a change to Chosen Direction, a Boundaries entry, or a module-level document; and expiry, where an entry described a stage the project has passed and is honestly removed. Both are curation. Neither is loss. Both terms — graduation and expiry — are defined precisely in the glossary.

Hard lessons earn a dedicated section — not an appendix, not an afterthought.

Every change to a derivative — code, prompt, operational document — begins with a change to its source reasoning document. Derivatives don't merely stay connected to the reasoning; they are created from it. That is the right order, and maintaining it is what curation means in practice.

**On the glossary as a named document type**

The methodology generates its own disambiguation need. Terms like co-author, derivative, compression, and sweep appear across all RFM documents and carry meanings that diverge from their everyday use. A glossary is warranted not by domain-specific conditions but by the methodology's existence — it travels with RFM regardless of the domain it is applied in. The glossary is a reasoning artifact, not a reference artifact: it records why a term means what it means here, not just what it means. It is subject to the same curation discipline as any reasoning document.

**On the operational document as a domain-specific derivative**

The methodology is universal — the same eight sections, the same discipline, applicable across any domain where complex reasoning precedes execution. But some domains have hard execution contracts: software being the primary example, where constants, interfaces, and procedures must be explicitly specified for execution to be reliable. In those domains, the reasoning document is accompanied by an operational document that carries those contracts. The operational document is a derivative of the reasoning — created from it, not loosely connected to it. The methodology stays universal. The operational document is domain-specific. This is a design decision, not a concession: keeping implementation contracts out of the reasoning document is what allows the reasoning to stay portable across domains and across time.

**On execution mode and the two-mode design**

The methodology operates in two modes. Reasoning mode is the default: reasoning precedes execution, the document is the source, every change begins at the appropriate level of the hierarchy. Execution mode is invoked when delivery pressure makes the full reasoning discipline locally unacceptable — a deadline, a sprint, a time-boxed commitment. Execution mode is not a degraded version of the methodology. It is the correct response to a specific condition, provided the reasoning documents are sufficiently complete before pressure hits.

The reasoning documents then function as Commander's Intent — a military doctrine principle designed precisely for execution under pressure without communication up the chain: the commander's direction, boundaries, and assumptions are established in advance so that execution can adapt within that frame without stopping to re-reason at every decision point. The discipline shifts from reasoning before every action to executing within established reasoning. What execution mode requires is minimal capture: a running record of deviations from established reasoning, conscious deferrals, and broken assumptions — enough to make the return to reasoning mode honest rather than reconstructed from code.

This running record is a Chesterton's Fence log — see the glossary for the full definition. Chesterton's Fence is the principle that you should not remove a fence until you understand why it was built. Under execution pressure, fences do get removed — the log ensures that each removal is noted and why. The return to reasoning mode after pressure lifts is not optional. It is where execution mode's debts are paid.

**On the question of future autonomy**

The most common objection to this approach is that increasingly capable and autonomous AI systems will eventually make it unnecessary. This misunderstands what the reasoning document is for. It is not a workaround for limited AI capability. It is the expression of human intent, human values, and human context applied to a specific problem. No level of AI autonomy removes the need for that — it only changes who executes once the intent is clear.

In fact, the more autonomous the system, the more critical the reasoning document becomes. A highly capable agent acting on vague or implicit intent doesn't fail cautiously. It fails confidently, at scale, and in ways that are difficult to trace or reverse.

Autonomy raises the stakes for clarity. It does not lower them.

The reasoning document is the deterministic anchor — the fixed, explicitly reasoned reference point against which agentic execution is measured. Agentic execution is where probabilistic reasoning is permitted — but within boundaries that have been explicitly reasoned, not assumed.

---

## The Boundaries

This methodology is explicitly not:

**A platform or tooling prescription.** No specific platform is prescribed. What the methodology does require of any practitioner deploying it: reasoning documents must be maintained in a format and location accessible to both human and LLM. Markdown satisfies this — human-readable, LLM-readable, version-controllable, and tool-agnostic. Where the document lives is a deployment decision, but accessibility to both parties is not optional.

**A replacement for domain expertise.** The methodology does not eliminate the need for skilled practitioners, domain experts, or specialists. It gives their expertise a structure to live in and a way to survive beyond the person who holds it.

**A documentation standard.** This is not about writing more or better documentation. It is about a fundamental shift in what the primary artifact of any reasoning-first practice is. Documentation describes a system after the fact. A reasoning document precedes and drives it.

**A methodology for AI development.** It does not prescribe how to build, train, or fine-tune AI models. It prescribes how to reason about and direct their use within a system.

**Designed to impose discipline on a team that won't bring it.** The deliberate return mode of curation requires a human who has a natural affinity for this kind of reflection. That is a people constraint, not a process gap. A team without such a person can follow the triggered mode but will gradually stop returning deliberately. The methodology will technically persist but quietly degrade. This is not a failure of the methodology. It is a boundary condition of its use.

**Designed to maintain full discipline under acute delivery pressure.** Delivery pressure is a specific, common condition under which the methodology's full discipline is at risk — not because teams stop believing in it, but because the local cost of the reasoning step becomes unacceptable when deadlines are close. This is distinct from the people constraint above: it affects willing teams in adverse conditions. The two-mode design — reasoning mode as default, execution mode under pressure — is the methodology's working hypothesis for this condition. It is not yet a tested practice. Teams operating under sustained delivery pressure without established reasoning documents should treat this as a known risk, not a solved problem.

---

## The Open Questions

These are genuinely unresolved. They are not weaknesses — they are the honest frontier of the methodology. Some will be answered through practice. Others may reshape the methodology itself.

**[OQ-DRFT] The drift problem.**

How does the reasoning document stay connected to the system it describes? The methodology is designed to prevent documentation drift — but it is not immune to it. What mechanisms, rituals, or technical constraints ensure the document evolves with the system rather than describing a past that no longer exists? Whether the discipline holds at scale and over time remains genuinely open.

**[OQ-MVDC] The minimum viable document.**

How short can a reasoning document be and still work? The methodology must not become a bureaucratic burden. There is a minimum below which the document loses its value — and a maximum above which it becomes the thing it was designed to replace. Where are those boundaries in practice?

**[OQ-ONBQ] The onboarding question.**

RFM is not designed for broad adoption. The target is a self-selected newcomer with a natural affinity for deliberate reflection. For that person the question is not persuasion but sequencing: what is the right first experience, in what order, before the overhead becomes discouraging and before the value has been felt? That question is carried at the module level in `RFM_guided_drafting_prompt_reasoning.md`. What remains open here is whether the answer — once earned through practice — requires a corresponding change to the methodology's top-level assumptions about who RFM is for. A second open question sits adjacent: whether the guided drafting prompt generalizes beyond the newcomer case to experienced practitioners starting a new project, or whether it remains a bounded onboarding artifact.

**[OQ-AUTB] The autonomy boundary.**

As agentic systems become more capable, where exactly is the line between what must be human-reasoned and what can be delegated? The methodology holds that human intent cannot be delegated — but the precise location of that boundary will need to be tested and refined in practice. At the execution level the deterministic/probabilistic split is largely resolved: structure and guarantees are owned by deterministic code, meaning and language by probabilistic LLM reasoning. What remains genuinely open is how a highly autonomous system should treat the reasoning document when acting without human oversight — where the reasoning document's authority ends and agentic judgment begins.

**[OQ-EVST] The evolutionary stage problem.**

The methodology is currently designed and validated at genesis stage — a single practitioner, early structure, everything still surprising. It is an open question how the discipline needs to change as a project matures. The Hard Lessons section is where this strain will show first: it only grows, it is cross-cutting, and curation becomes harder as the project ages. Structured sweep discipline addresses this in practice — but whether it scales, and whether the methodology itself needs to describe explicit transition points as a project matures, remains open.

**[OQ-LCDCE] The lifecycle of document content.**

How do entries that have outlived their relevance exit honestly? Some content describes a stage the project has passed — not wrong, not graduated, simply no longer active. The methodology affirms that such entries should be removed, but the discipline for recognizing and executing that removal is not yet described. A document that accumulates without expiring content will eventually misrepresent the project's current state. What makes an entry a candidate for expiry rather than graduation, and what does honest removal look like in practice, remains open.

**[OQ-MCDC] The minimal capture discipline.**

Execution mode requires minimal capture — a record of deviations, deferrals, and broken assumptions sufficient to make the return to reasoning mode honest. What this looks like in practice is undesigned. How short can it be and still serve its purpose? What is the right artifact — a section appended to the reasoning document, a separate log, something else? How does a team distinguish a deviation worth capturing from noise? And what does the return-to-reasoning-mode session actually look like — what is its protocol, its output, its quality gate? These questions are unresolved. The two-mode design is a working hypothesis, not a tested practice.

---

## Hard Lessons

**Methodology design**

**[HL-DFMD] The document structure emerged from failure modes, not from best practices.**

The most robust design decision in the methodology was to derive the eight sections by asking "what causes humans and LLMs to fail?" rather than "what should a good document contain?" Designing from failure is more rigorous than designing from aspiration. This principle should be applied recursively — to every module document that follows.

**Document discipline**

**[HL-DMAP] The document map belongs at the top of every top-level reasoning document when a document landscape exists to navigate.**

A reader or LLM encountering a project for the first time cannot orient from the top-level reasoning document alone. The map is only meaningful when a document landscape exists to navigate — a single-document system has nothing to map. Navigation is not reasoning, but it is a prerequisite for reasoning about the right thing. The document map and the public-facing entry point for new readers serve different audiences and must not be conflated: the map carries real version numbers for practitioners detecting drift; the entry point carries orientation without versions for readers encountering the project fresh. Neither substitutes for the other.

**[HL-TLOR] Once a module exists, top-level ownership must be actively reduced.**

Branching to a new module does not automatically contract the top level. Without deliberate reduction, both layers accumulate entries about the same content — the top level drifts toward restating what the module now owns. The discipline after branching is not just creating the new module; it is returning to the top level and removing whatever the module now carries. This is a distinct step, not an automatic consequence of branching. See [AS-DSDH] for the branching signal itself — this lesson names what must happen after that signal is acted on.

**[HL-CPSC] Compressing a reasoning document feels like curation — it is structural change.**

Removing or condensing articulated reasoning can present as tidying up: cutting redundancy, tightening prose, removing what feels obvious. None of those framings change what is actually happening. When reasoning is compressed, signal is lost that cannot be recovered — the distinctions that felt obvious in the session that produced them are precisely what a future reader or a fresh LLM cannot reconstruct. The danger is that compression is invisible from inside the session that performs it: the compressor holds the missing context and cannot perceive the gap they are creating. Any proposed reduction of articulated reasoning — however it is framed — is a structural change to the document, and requires the same joint decision that any structural change requires.

**[HL-DRIFT] The drift problem is not solved by the methodology — it is the methodology's greatest vulnerability.**

The methodology was designed to prevent documentation drift. But the reasoning document itself can drift from the system it describes. Naming this problem is not solving it. This lesson must stay visible until a genuine answer exists. The methodology's own curation discipline — triggered and deliberate return — addresses drift in principle but cannot guarantee it in practice. No structural mechanism yet exists to detect that failure from inside the system. One asymmetry is known: applying the methodology from inception is the only reliable prevention — reconstructed reasoning produces plausible documents, but not necessarily true ones. The sweep prompts — deliberately invoked corrective artifacts — reduce the risk of undetected drift, but require honest and regular application to do so. A team that invokes them performatively rather than genuinely will produce documents that appear current while describing a past state. Structural mechanisms for detecting that failure from inside the system remain an open question.

**Human-LLM collaboration**

**[HL-ERTA] Enthusiasm without red teaming produces fragile thinking.**

A methodology — or any reasoning document — only becomes robust when honest criticism is made explicit: not just "does this work?" but "what would break this?" The red team function must be built into the process, not added later. A reasoning document that has never been challenged is a reasoning document that hasn't been tested.

**[HL-LCAD] Long conversations with LLMs accumulate drift.**

Even a disciplined LLM develops bias over a long conversation — toward ideas that emerged in that conversation, toward framings that felt productive, toward connections that feel natural but weren't explicitly decided. This is subtle and hard to detect from inside the conversation. Drift is more dangerous than context window limits — it is invisible and cumulative. Two mitigations: first, the reasoning document should be complete enough to onboard a fresh LLM without loss — if it can't, the document isn't finished. Second, deliberately starting a new conversation with only the reasoning document as context is a useful quality check. A fresh LLM that misunderstands the direction reveals a gap in the document, not a gap in the conversation.

**[HL-WENO] The worked example is never optional — at any stage of the methodology's development.**

Theory without ground truth is hypothesis. Applying the methodology from inception — before any execution artifacts exist — proves the chain in both directions: reasoning document to derivative, with traceability at every step and no undocumented judgment calls made during implementation. Applying it to an existing project — where decisions have already been made without explicit reasoning — reveals that reconstructed reasoning produces plausible documents but not necessarily true ones. Both directions of experience are necessary.

**[HL-DIHQ] Deferred items must carry their context, not just their topic.**

When an item is parked as future work, the handover note captures what was deferred but not the context that surrounded it — what was understood, what was tried, what specifically remains open, and why the item stopped where it did. That context disappears with the session that produced it. The next session reopens the item cold and must reconstruct what was present but not captured. The fix is not a longer handover. It is a richer deferral record: each deferred item carries enough context that a fresh session can proceed without reconstruction. A topic label is not a deferral record.

**Execution practice**

**[HL-VGLE] RFM's value is gap-legibility, not gap-elimination.**

A well-reasoned document hierarchy will not prevent all gaps from appearing during execution. What it does is make gaps visible in the right place — as explicit reasoning debts, open questions, or provisional specifications — rather than letting them hide in code where they harden silently into undocumented decisions. A first application that produces no visible gaps has probably not been honest. A first application whose gaps surface at the reasoning level and are named there rather than discovered late in implementation is working correctly.

**[HL-HACD] A holding artifact shapes co-author behavior in ways that weren't designed.**

Introducing a designated place to park unresolved items — a holding artifact such as a deferred items list or parking file — lowers the threshold for parking by making it the path of least resistance. What was designed as a last resort before losing signal becomes a first resort before doing the harder work of deciding whether something is ready. The behavioral effect is that the co-author parks rather than works, defers rather than drafts. The test before suggesting the holding artifact: is the candidate genuinely unready, or is the holding artifact simply available? If the candidate is sharp enough to describe precisely, it is probably ready to be drafted.

**[HL-GCDND] Graduated content disappears — it does not narrate its own departure.**

When an open question partially resolves, the resolved part simply goes. What survives stands on its own. An entry that says "we now know X; what remains open is Y" has not been curated — it has been annotated. The annotation blurs the boundary between what is settled and what is not. The discipline is clean removal of what is resolved, leaving the surviving question to speak for itself.

**[HL-ARGI] An assumption that receives a graduated insight must carry the reasoning that earned it, not just the conclusion.**

When an open question graduates into an assumption, the conclusion alone is not enough. A conclusion-only assumption is indistinguishable from an unexamined default — it states what is believed without explaining why it is believed or under what conditions it would break. The reasoning that produced the assumption — the evidence, the path, the conditions — must travel with it. That is what makes the entry an assumption rather than received wisdom, and what allows a future reader to test it honestly rather than inherit it blindly.

---

*top_level_document // [living]*
*the reasoning arrived before the structure did*
*that was the right order*