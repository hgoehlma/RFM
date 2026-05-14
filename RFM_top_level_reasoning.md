# Reasoning-First Methodology
`v0.0.0.38` // `top_level_document` // [living]

---

## Document Map

| Document | Type | Version | What it carries |
|---|---|---|---|
| `RFM_top_level_reasoning.md` | Top-level reasoning | v0.0.0.38 | The methodology itself — problem, assumptions, landscape, chosen direction, hard lessons |
| `RFM_operational.md` | Operational | v0.0.0.5 | File naming conventions, document map maintenance, version discipline |
| `RFM_glossary.md` | Glossary | v0.0.0.5 | Disambiguation of terms that carry different meanings across reader contexts |
| `RFM_prompts_reasoning.md` | Prompts reasoning | v0.0.0.32 | The reasoning document governing all system prompt decisions |
| `RFM_traveling_prompt_reasoning.md` | Module reasoning | v0.0.0.5 | The reasoning document governing traveling prompt design decisions |
| `RFM_traveling_prompt.md` | Traveling system prompt | v0.0.0.22 | The system prompt that carries the methodology into every LLM conversation |
| `RFM_sweep_prompts_reasoning.md` | Module reasoning | v0.0.0.5 | The reasoning document governing sweep prompt design decisions |
| `RFM_sweep_prompt_structural.md` | Structural sweep prompt | v0.0.0.2 | The prompt artifact that activates the structural sweep — findings for ruling, not edits |
| `RFM_sweep_prompt_language.md` | Language sweep prompt | v0.0.0.2 | The prompt artifact that activates the language sweep — findings for ruling, not edits |
| `RFM_human_prompt_reasoning.md` | Module reasoning | v0.0.0.5 | Reasoning document for the human prompt — skeleton, in active design |
| `RFM_human_prompt.md` | Human prompt | v0.0.0.5 | The prompt artifact for the human collaborator — practices that keep the co-author role alive across sessions |
| `RFM_guided_drafting_prompt_reasoning.md` | Module reasoning | v0.0.0.3 | Reasoning document governing guided drafting prompt design decisions |
| `RFM_guided_drafting_prompt_operational.md` | Operational | v0.0.0.1 | Deployment and artifact inventory for the guided drafting prompt module |
| `RFM_guided_drafting_prompt.md` | Guided drafting prompt | v0.0.0.2 | The prompt artifact that activates the guided drafting session — behavioral specification for the LLM, section intentions for the newcomer |
| `RFM_first_session_guidance.md` | First session guidance | v0.0.0.1 | Practical preparation for a newcomer's first guided drafting session — what to bring, what to expect, what to watch for |

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

**[AS-CIIL] - Context is irreducibly important for LLMs.** High signal reasoning context minimizes hallucination. This holds regardless of how capable models become — a better LLM with poor context will still underperform a modest LLM with rich context.

**[AS-AELN] - Abstraction will continue to evolve — and language is the next layer.** The history of software is a history of increasing abstraction. LLMs make intention expressible in natural language. But no level of abstraction removes the need to articulate what you want. The thinking cannot be delegated.

**[AS-MOSA] - Modularity is the only sustainable architecture.** Monolithic systems resist change, learning, and maintenance. The reasoning document hierarchy should mirror and enforce modular thinking from the start.

**[AS-CACM] - Code alone will never carry its own motivation.** The gap between what code does and why it exists cannot be closed by better code. It requires a separate, connected reasoning artifact maintained proactively.

**[AS-QEUP] - Quality of execution — human or AI — is upstream of the reasoning investment.** Thinking first is not overhead. It is the highest leverage point in the entire development process.

The first five assumptions describe the world as the methodology finds it. The next six describe what working within that world requires.

**[AS-CDNO] - Curation must be deliberate, not optional.** Curation has two modes and both are required. The first is triggered — something accumulates, strains, or surfaces in use, and draws you back to the document. The second is deliberate return — you come back without a specific trigger, to ask whether the document still reflects what you know. Neither mode can be replaced by a scheduled rhythm; a time-triggered cadence risks becoming performative rather than genuine. The methodology only holds if both modes are practiced as discipline, not suggestion.

**[AS-RDHL] - A reasoning document designed explicitly for both humans and LLMs simultaneously outperforms one designed for either alone.** This is not a natural default. It requires conscious design.

**[AS-HLVS] - Hard lessons are as valuable as successes.** What failed, and why, carries as much reasoning value as what worked. A methodology that doesn't capture failure will repeat it.

**[AS-DSDH] - Document strain is diagnostic of hierarchy.** When a section strains under its own weight — too many options, too much detail, too many edge cases — that is a signal to branch into a new module, not a signal to write more carefully. The module structure is not designed upfront. It emerges from the writing. The hierarchy reveals itself through strain.

**[AS-DWHC] - In domains where execution has hard contracts — software being the primary example — the reasoning document is accompanied by an operational document.** The operational document carries constants, interfaces, procedures, and known values. It is a derivative of the reasoning, not a replacement for it. The methodology stays universal. The operational document is domain-specific.

**[AS-ADSR] - These assumptions describe a self-reinforcing loop — when the discipline holds.** When an LLM works within a well-reasoned document, its downstream execution — code generation, system design, prompt construction — is more correct and less prone to hallucination. Higher correctness produces better output for the human to reason against. Better joint reasoning produces richer documents. Richer documents improve the next round of LLM execution. The loop is self-reinforcing — but only when both parties hold the discipline: the LLM guided by a correctly designed system prompt, the human committed to reasoning before execution and curating honestly. When either breaks, the loop degrades.

---

## The Landscape

The problem of meaning in software is not unrecognized. Several movements have addressed parts of it:

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **Agile** | Shifted focus from documentation-heavy waterfall to working software and human collaboration | Solved delivery rigidity but traded away reasoning continuity in the process |
| **Domain-Driven Design** | Made meaning an explicit design target. Gave us Ubiquitous Language and Bounded Contexts | Presupposes reasoning already exists — it structures meaning, it doesn't generate or preserve it |
| **Clean Code / TDD** | Made quality and correctness first-class concerns | Correctness is not the same as meaning. A perfectly tested system can still be incomprehensible |
| **Wardley Mapping** | Made situational awareness and strategic reasoning explicit, visual, and owned | Stops at the strategic level. Doesn't cascade into a connected reasoning practice at every level of execution |
| **Peter Naur's "Programming as Theory Building"** | Argued that programming is primarily the activity of building a theory of the problem in the programmer's mind — code is a secondary artifact of that theory. Anticipates RFM's founding insight that the reasoning behind a system is more valuable than the system's outputs | Stops at the individual programmer's mental model. Does not prescribe a structural artifact for capturing that theory, does not address the LLM dimension, and has no mechanism for the theory to survive beyond the person who holds it |
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

The methodology is called Reasoning-First Methodology, abbreviated RFM. The abbreviation carries a deliberate resonance with RTFM — that is not accidental and is kept. The reasoning document is not a record of decisions. It is where decisions are made. A record is written after the fact and drifts. A decision-making interface is consulted before action and stays alive because it must. Every change to a system begins with a change to the reasoning document at the appropriate level. Code is the derivative. The document is the source.

**On the governing co-authorship pattern**

The joint reasoning sequence — propose → reflect → converge → execute — is the pattern through which co-authorship operates in practice. Both parties contribute through the first three steps. At the execution step, the natural division applies: the LLM formulates and edits, the human judges and confirms. The full reasoning for this pattern is in `RFM_prompts_reasoning.md`.

**On the prompt system**

The methodology travels through three prompt artifacts: a traveling prompt that makes the discipline ambient, and two sweep prompts — structural and language — that form the corrective arm. Prevention and correction are different cognitive modes and require separate artifacts. The full reasoning for this design is in `RFM_prompts_reasoning.md`.

**On the structure**

The same eight sections, the same discipline, the same navigational practice — whether you are at the top of the hierarchy or deep inside a single module. Think of a regular map: a country map and a street map use identical discipline at different resolution. The street map is a module of the city map — each complete at its own resolution, each connected to the level above it. This property — the same structure governing at every level — is what mathematicians call fractal. The term is precise and worth keeping: a fractal is not just a pattern that repeats, it is a pattern whose rules apply at every level. That is exactly what the reasoning document hierarchy is.

**On keeping it alive**

The document is kept alive through enforced curation. Not just addition but reduction. What has evolved? What can be removed? What needs replacing? A document that only grows is a document that is already dying. The pressure of constraint is a feature, not a limitation.

A healthy document breathes — it expands when new signal arrives and contracts when old signal has been metabolized. Contraction has two legitimate forms: graduation, where a hard lesson or open question has been fully absorbed and transforms into an assumption or a change to Chosen Direction; and expiry, where an entry described a stage the project has passed and is honestly removed. Both are curation. Neither is loss.

Hard lessons are first-class citizens. What was tried, why it seemed right, what failed, and what that means going forward carries as much reasoning value as what succeeded. A methodology that doesn't capture failure will repeat it.

Every change to a derivative — code, prompt, operational document — begins with a change to its source reasoning document. Derivatives don't merely stay connected to the reasoning; they are created from it. That is the right order, and maintaining it is what curation means in practice.

**On the glossary as a named document type**

The methodology generates its own disambiguation need. Terms like co-author, derivative, compression, and sweep appear across all RFM documents and carry meanings that diverge from their everyday use. A glossary is warranted not by domain-specific conditions but by the methodology's existence — it travels with RFM regardless of the domain it is applied in. The glossary is a reasoning artifact, not a reference artifact: it records why a term means what it means here, not just what it means. It is subject to the same curation discipline as any reasoning document.

**On execution mode and the two-mode design**

The methodology operates in two modes. Reasoning mode is the default: reasoning precedes execution, the document is the source, every change begins at the appropriate level of the hierarchy. Execution mode is invoked when delivery pressure makes the full reasoning discipline locally unacceptable — a deadline, a sprint, a time-boxed commitment. Execution mode is not a degraded version of the methodology. It is the correct response to a specific condition, provided the reasoning documents are sufficiently complete before pressure hits.

The reasoning documents then function as Commander's Intent — a military doctrine principle in which the commander's direction, boundaries, and assumptions are established in advance so that execution can adapt within that frame without stopping to re-reason at every decision point. The discipline shifts from reasoning before every action to executing within established reasoning. What execution mode requires is minimal capture: a running record of deviations from established reasoning, conscious deferrals, and broken assumptions — enough to make the return to reasoning mode honest rather than reconstructed from code.

This running record is a Chesterton's Fence log. Chesterton's Fence is the principle that you should not remove a fence until you understand why it was built. Under execution pressure, fences do get removed — the log ensures that each removal is noted and why. The return to reasoning mode after pressure lifts is not optional. It is where execution mode's debts are paid.

**On the question of future autonomy**

The most common objection to this approach is that increasingly capable and autonomous AI systems will eventually make it unnecessary. This misunderstands what the reasoning document is for. It is not a workaround for limited AI capability. It is the expression of human intent, human values, and human context applied to a specific problem. No level of AI autonomy removes the need for that — it only changes who executes once the intent is clear.

In fact, the more autonomous the system, the more critical the reasoning document becomes. A highly capable agent acting on vague or implicit intent doesn't fail cautiously. It fails confidently, at scale, and in ways that are difficult to trace or reverse.

Autonomy raises the stakes for clarity. It does not lower them.

The reasoning document is the deterministic anchor — the fixed, explicitly reasoned reference point against which agentic execution is measured. Agentic execution is where probabilistic reasoning is permitted — but within boundaries that have been explicitly reasoned, not assumed.

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

**[OQ-DRFT] The drift problem.**

How does the reasoning document stay connected to the system it describes? The methodology is designed to prevent documentation drift — but it is not immune to it. What mechanisms, rituals, or technical constraints ensure the document evolves with the system rather than describing a past that no longer exists? This is the hardest open question.

Applying the methodology from inception — reasoning before any code exists — is the only reliable prevention. Reconstructing reasoning from existing code produces plausible documents, but not necessarily true ones. There is no reliable cure for drift once it has set in. Whether the discipline holds at scale and over time remains genuinely open.

**[OQ-MVDC] The minimum viable document.**

How short can a reasoning document be and still work? The methodology must not become a bureaucratic burden. There is a minimum below which the document loses its value — and a maximum above which it becomes the thing it was designed to replace. Where are those boundaries in practice?

**[OQ-ONBQ] The onboarding question.**

How does someone encounter this methodology for the first time and understand its value quickly enough to adopt it? The feedback loop for good reasoning is slow and invisible. The feedback loop for coding is fast and visible. Bridging that gap is a change management challenge the methodology does not yet fully answer.

Two partial answers exist. The document map gives a new collaborator immediate orientation without requiring them to read everything first. The LLM itself — guided by a well-designed system prompt — becomes part of the onboarding infrastructure, actively guiding a newcomer through their first reasoning document rather than waiting to be directed.

The deeper question has been sharpened by work at the module level: RFM is not designed for broad adoption. The target is a self-selected newcomer with a natural affinity for deliberate reflection — someone who found the methodology, read into it, and is willing to try. For that person, the question is not persuasion but sequencing: what is the right first experience, in what order, before the overhead becomes discouraging and before the value has been felt? That question is now carried at the module level in [OQ-ONSQ] in `RFM_guided_drafting_prompt_reasoning.md`. What remains open here is whether the answer to [OQ-ONSQ] — once earned through practice — requires a corresponding change to the methodology's top-level assumptions about who RFM is for.

**[OQ-AUTB] The autonomy boundary.**

As agentic systems become more capable, where exactly is the boundary between what must be human-reasoned and what can be delegated? The methodology holds that human intent cannot be delegated — but the precise location of that boundary will need to be tested and refined in practice.

The division of cognitive labor between human and LLM in collaborative practice is no longer the open question here — the joint reasoning sequence addresses it. What remains genuinely open is the agentic boundary: as autonomous systems become more capable, where exactly is the line between what must be human-reasoned and what can be delegated? This question connects directly to OQ-DPDQ and will likely be resolved together with it.

**[OQ-DPDQ] The deterministic/probabilistic design question.**

At the execution level this question is largely resolved: structure and guarantees are owned by deterministic code, meaning and language by probabilistic LLM reasoning. At the reasoning document level the answer is similarly clear: boundaries are deterministic anchors, open questions are the legitimate home of uncertainty, assumptions hold until evidence breaks them. What remains genuinely open is the agentic boundary — how a highly autonomous system should treat the reasoning document when acting without human oversight. That question connects directly to OQ-AUTB and will likely be resolved together with it.

**[OQ-EVST] The evolutionary stage problem.**

The methodology is currently designed and validated at genesis stage — a single practitioner, early structure, everything still surprising. It is an open question how the discipline needs to change as a project matures through later stages of development. The Hard Lessons section is where this strain will show first: it only grows, it is cross-cutting, and curation becomes harder as the project ages. The hunch is that Hard Lessons eventually graduates from a document section into a separate living artifact, that lessons can be retired when fully absorbed into assumptions or team practice, and that the methodology itself needs to describe these transition points explicitly. This has not been designed yet. It needs to be — before the methodology is adopted at scale.

One boundary is already clear: the moment code precedes reasoning, the methodology is in recovery mode rather than prevention mode. Reconstructed reasoning produces plausible documents, but not necessarily true ones. What changes at each subsequent stage beyond that boundary is still open.

**[OQ-LCDCE] The lifecycle of document content.**

How do entries that have outlived their relevance exit honestly? Some content describes a stage the project has passed — not wrong, not graduated, simply no longer active. The methodology affirms that such entries should be removed, but the discipline for recognizing and executing that removal is not yet described. A document that accumulates without expiring content will eventually misrepresent the project's current state. What makes an entry a candidate for expiry rather than graduation, and what does honest removal look like in practice, remains open.

**[OQ-MCDC] The minimal capture discipline.**

Execution mode requires minimal capture — a record of deviations, deferrals, and broken assumptions sufficient to make the return to reasoning mode honest. What this looks like in practice is undesigned. How short can it be and still serve its purpose? What is the right artifact — a section appended to the reasoning document, a separate log, something else? How does a team distinguish a deviation worth capturing from noise? And what does the return-to-reasoning-mode session actually look like — what is its protocol, its output, its quality gate? These questions are unresolved. The two-mode design is a working hypothesis, not a tested practice.

---

## Hard Lessons

**Methodology design**

**[HL-DFMD] The document structure emerged from failure modes, not from best practices.**

The most robust design decision in the methodology was to derive the eight sections by asking "what causes humans and LLMs to fail?" rather than "what should a good document contain?" Designing from failure is more rigorous than designing from aspiration. This principle should be applied recursively — to every module document that follows.

**[HL-UDOS] The methodology is universal. The operational document is domain-specific.**

The eight-section reasoning document applies to any domain where structured thinking precedes execution — software, architecture, investing, art. The operational document — constants, interfaces, procedures, known values — exists because some domains, software being the primary example, have hard execution contracts that require their own artifact. The methodology-level principle stays clean and universal: reasoning is the primary artifact. There is no ninth section. There is a second document type — but only when the domain demands it.

**[HL-EACL] Existing approaches were closer than expected — and further than expected.**

Many pieces of this methodology exist in scattered form across prior movements. The gap is real but the lineage is rich. This matters because the right framing is not "we invented something new" but "we completed something that was already trying to emerge." The latter is more honest and more credible.

**[HL-QGCP] The quality gate is continuous, not periodic.**

The quality gate was originally imagined as a separate LLM evaluator invoked periodically to check documents for sharpness, hidden assumptions, completeness, and internal consistency. Practice revealed a different answer: an LLM working within the methodology, guided by a correctly designed system prompt, flags leakage and hidden assumptions in the moment — not in a separate review cycle. The quality gate is the traveling prompt doing its job. A deliberate sweep session is a concentrated version of this practice, not a separate mechanism.

**Document discipline**

**[HL-DMAP] The document map belongs at the top of every top-level reasoning document when a document landscape exists to navigate.**

A reader or LLM encountering a project for the first time cannot orient from the top-level reasoning document alone — the document describes decisions but not the document landscape around it. A lightweight map listing what documents exist, their type, and their scope should appear before The Problem in every top-level reasoning document. The map is only meaningful when a document landscape exists to navigate — a single-document system has nothing to map. Navigation is not reasoning, but it is a prerequisite for reasoning about the right thing. The document map is the one place where real version numbers belong — it is the snapshot of the system's current state. Wildcards (`v*`) in a map defeat its purpose: a map that doesn't tell you which version exists cannot be used to detect drift. Individual cross-document references, by contrast, should never include version numbers.

**[HL-FNDP] File naming discipline is a prerequisite for LLM orientation.**

Inconsistent file names force an LLM to infer document type and scope from content rather than from the name itself. The naming convention and its rationale are carried in `RFM_operational.md`. The principle here: deviating from a consistent convention degrades LLM orientation before a single line is read.

**[HL-XREF] Cross-document references use document names, never version numbers.**

Hardcoding a version number in a cross-document reference creates a maintenance tax: every version bump to the referenced document requires updates in every document that references it. The reference should be to the document by name only. The version is implicit — you always read the current version. The document map carries the version snapshot. Individual references do not.

**[HL-DIAG] Document strain is diagnostic, not a writing problem.**

When a section starts straining — too many options, too much detail, too many edge cases — that is not a signal to write more carefully. It is a signal that something needs to become its own module in the hierarchy. The top level document has a natural completion condition: every major decision is justified but no implementation detail has leaked in. The module structure is not designed upfront. It emerges from the writing. The hierarchy reveals itself through the strain.

**[HL-TLOR] Once a module exists, top-level ownership must be actively reduced.**

Branching to a new module does not automatically contract the top level. Without deliberate reduction, both layers accumulate entries about the same content — the top level drifts toward restating what the module now owns. The discipline after branching is not just creating the new module; it is returning to the top level and removing whatever the module now carries. This is a distinct step, not an automatic consequence of branching. See HL-DIAG for the branching signal itself — this lesson names what must happen after that signal is acted on.

**[HL-ASRP] Assumptions state reasoning principles, not implementation details.**

An assumption that references implementation — a specific function, a config flag — has leaked the wrong level of abstraction into the wrong section. Assumptions should be testable beliefs about the world: why something is true, what would break if it weren't. Implementation details belong in Chosen Direction or module documents.

**[HL-HLLC] Hard lessons are not permanent residents — they have a lifecycle.**

The Hard Lessons section accumulates entries but has no mechanism for them to exit. Some lessons, once fully absorbed, should graduate — the insight transforms into an assumption or shapes Chosen Direction, and the original entry is removed. Others describe a stage the project has passed and should expire — removed honestly, without replacement. A lesson that has been metabolized but remains in Hard Lessons creates false weight: the section implies these are active lessons. Once a lesson is no longer active, keeping it is clutter, not memory.

**[HL-DRIFT] The drift problem is not solved by the methodology — it is the methodology's greatest vulnerability.**

The methodology was designed to prevent documentation drift. But the reasoning document itself can drift from the system it describes. Naming this problem is not solving it. This lesson must stay visible until a genuine answer exists.

**LLM behavior**

**[HL-SRGO] LLMs must never summarize reasoning documents unless explicitly asked.**

When an LLM edits a reasoning document, there is a structural tendency to tidy, condense, and inadvertently lose nuance in the process. A summarized reasoning document is a degraded reasoning document — it may read more cleanly but it carries less signal. In larger projects this tendency can derail work subtly and cumulatively, with important details lost across multiple edit cycles. The methodology requires that any LLM working with reasoning documents makes surgical edits only — touching exclusively what was explicitly requested, showing what changed, and leaving everything else intact.

**[HL-LCAD] Long conversations with LLMs accumulate drift.**

Even a disciplined LLM develops bias over a long conversation — toward ideas that emerged in that conversation, toward framings that felt productive, toward connections that feel natural but weren't explicitly decided. This is subtle and hard to detect from inside the conversation. Drift is more dangerous than context window limits — it is invisible and cumulative. Two mitigations: first, the reasoning document should be complete enough to onboard a fresh LLM without loss — if it can't, the document isn't finished. Second, deliberately starting a new conversation with only the reasoning document as context is a useful quality check. A fresh LLM that misunderstands the direction reveals a gap in the document, not a gap in the conversation.

**[HL-VDOC] The LLM must verify against the document before asserting absence.**

In a long conversation, the LLM accumulates conversational context that can substitute for document content without either party noticing. The failure mode is subtle: the LLM flags a gap that isn't there, or confirms something that has drifted from the document. Before asserting that something is missing or present, verify against the document directly. Conversational memory is not a reliable proxy for document content.

**[HL-MASP] Methodology assumptions belong in a system prompt, not in every document.**

An early instinct when applying the methodology is to inherit methodology-level assumptions into every reasoning document. This creates noise, not signal. Assumptions that are constant across all documents — the rules of the methodology itself — should live in a single LLM system prompt that travels silently with every interaction. Only assumptions that are genuinely local and specific to a particular decision belong in the reasoning document. This keeps documents lean, focused, and honest.

**Human-LLM collaboration**

**[HL-ERTA] Enthusiasm without red teaming produces fragile thinking.**

A methodology — or any reasoning document — only becomes robust when honest criticism is made explicit: not just "does this work?" but "what would break this?" The red team function must be built into the process, not added later. A reasoning document that has never been challenged is a reasoning document that hasn't been tested.

**[HL-CWSH] Capture while sharp — capture is not the same as processing.**

An insight that is parked rather than captured immediately degrades. What returns later is a blurred version of the original thought, or nothing at all. The discipline is: capture immediately in the right place — a single sentence is enough to hold the signal. Processing — deciding what it means, where it goes, how it connects — can wait. The document holds the thought so the conversation can continue. Parking is not the same as noting.

**[HL-SBSC] Session-born shorthands are candidates for the document, not automatic entries.**

A session-born shorthand is a term that emerged between two collaborators and carries the session context that gave it meaning. When it enters a document, it meets a reader who wasn't in that session. Before capturing one, apply this test: does it carry its meaning without the conversation behind it? If not, spell it out instead. Terms that feel precise inside a session can be opaque to every reader since — the test must be applied at the moment of capture, not assumed to have been passed. This applies equally to shorthands introduced by the human — a term you coined feels self-evident to you in a way that masks how opaque it is to anyone else. The test is the same regardless of who introduced the term.

**[HL-WENO] The worked example is never optional — at any stage of the methodology's development.**

Theory without ground truth is hypothesis. Applying the methodology from inception — reasoning before any code exists — proves the chain in both directions: reasoning document to operational document to code, with traceability at every step and no undocumented judgment calls made during implementation. Applying it to existing systems reveals that reconstructed reasoning produces plausible documents but not necessarily true ones. Both directions of experience are necessary. The worked example is never optional — at any stage of the methodology's development.

**[HL-DIHQ] Deferred items must carry their context, not just their topic.**

When an item is parked as future work, the handover note captures what was deferred but not the context that surrounded it — what was understood, what was tried, what specifically remains open, and why the item stopped where it did. That context disappears with the session that produced it. The next session reopens the item cold and must reconstruct what was present but not captured. The fix is not a longer handover. It is a richer deferral record: each deferred item carries enough context that a fresh session can proceed without reconstruction. A topic label is not a deferral record.

**Execution practice**

**[HL-VGLE] RFM's value is gap-legibility, not gap-elimination.**

A well-reasoned document hierarchy will not prevent all gaps from appearing during execution. What it does is make gaps visible in the right place — as explicit reasoning debts, open questions, or provisional specifications — rather than letting them hide in code where they harden silently into undocumented decisions. A first application that produces no visible gaps has probably not been honest. A first application whose gaps surface at the reasoning level and are named there rather than discovered late in implementation is working correctly.

**[HL-NLVL] Before drafting any addition to a reasoning document, name the level it belongs to.**

Before drafting any addition to a reasoning document, name the level the candidate belongs to. If it belongs in a derivative — operational document, code, prompt — don't draft it into the source. This test is easy to skip under execution-mode gravity, especially when concrete material is already present in the conversation. The test must be applied explicitly, before the draft exists. A draft that has already been produced exerts its own momentum. The right order is: name the level, confirm it belongs here, then draft.

**[HL-XREG] External research creates execution-mode gravity inside a reasoning session.**

When external research enters a reasoning session — concrete data, implementation detail, tool-specific findings — the material exerts gravitational pull on whatever gets drafted next. The draft follows the research rather than the methodology level. The mitigation is explicit re-anchoring: after any research step and before drafting, name the level the addition belongs to. Research is an input to reasoning, not a substitute for it. If the research is pulling toward operational detail, that is a signal to stop and identify the derivative document where the detail belongs — not to continue drafting at the reasoning level.

**[HL-HACD] A holding artifact shapes co-author behavior in ways that weren't designed.**

Introducing a designated holding artifact — a parking file, a deferred items list — lowers the threshold for parking by making it the path of least resistance. What was designed as a last resort before losing signal becomes a first resort before doing the harder work of deciding whether something is ready. The behavioral effect is conservative drift: the co-author parks rather than works, defers rather than drafts. The test before suggesting the holding artifact: is the candidate genuinely unready, or is the holding artifact simply available? If the candidate is sharp enough to describe precisely, it is probably ready to be drafted.

**[HL-GCDND] Graduated content disappears — it does not narrate its own departure.**

When an open question partially resolves, the resolved part simply goes. What survives stands on its own. An entry that says "we now know X; what remains open is Y" has not been curated — it has been annotated. The annotation blurs the boundary between what is settled and what is not. The discipline is clean removal of what is resolved, leaving the surviving question to speak for itself.

**[HL-ARGI] An assumption that receives a graduated insight must carry the reasoning that earned it, not just the conclusion.**

When an open question graduates into an assumption, the conclusion alone is not enough. A conclusion-only assumption is indistinguishable from an unexamined default — it states what is believed without explaining why it is believed or under what conditions it would break. The reasoning that produced the assumption — the evidence, the path, the conditions — must travel with it. That is what makes the entry an assumption rather than received wisdom, and what allows a future reader or collaborator to challenge it honestly rather than inherit it silently.

**[HL-LSDP] The Landscape section drifts in two predictable directions when its structure is not held.**

The first drift is toward loose prose that stops distinguishing neighboring approaches clearly — each row collapses into a general description, and the reader loses the ability to trace why each approach is insufficient for the local problem. The second drift is toward early option selection — what looks like landscape analysis is already choosing, and the work that belongs in Options Considered has been absorbed silently. Both failures share a root: the section lost its sequence. A Landscape section is strongest when it first distinguishes adjacent approaches in a structured comparison — what each does, why it is insufficient — and then closes with a short paragraph naming what the landscape collectively reveals and where the gap remains. Without that sequence, both drift modes become invisible until they have already done damage.

---

*v0.0.0.38 // top_level_document // [living]*
*the reasoning arrived before the structure did*
*that was the right order*