# Reasoning-First Methodology
`v0.17.0` // `top_level_reasoning` // [living]

---

The document map for RFM, including the hierarchy this document sits in, is `RFM_map.md`.

---

## The Problem

Any domain where complex reasoning precedes execution faces the same failure: the thinking disappears. The decisions that shaped the outcome (why this approach, why not another, what was assumed, what failed) exist briefly and then vanish. What remains are the outputs. The meaning behind them does not survive.

Software development is where this methodology was built and where the consequences are currently most visible. Code is the output that remains, and code cannot explain itself. But the failure is not unique to software. Anywhere complex reasoning precedes execution, the same erasure happens.

This creates two compounding failures: humans joining or revisiting a system must reconstruct intent from structure. LLMs assisting with that system hallucinate because the context they need was never recorded.

Current tools address symptoms. None address the root cause: there is no disciplined practice for capturing and maintaining reasoning as a primary artifact, at every level of a system, designed to serve both humans and LLMs simultaneously.

**Why now?**

This problem is not new. What is new is that LLMs have made the consequences of missing reasoning suddenly visible and concrete. But the same LLMs also create the opportunity to fix it. A well-reasoned document does not just help humans understand a system. It is the source from which an LLM can derive and execute autonomously, without the human present at execution time. The reasoning document is what makes human intent legible to a system that has no other way to access it. The problem and the solution have arrived together.

---

## The Assumptions

The following are believed to be true. They cannot all be fully proven yet. If any of them is wrong, the methodology needs to change.

**[AS-CIIL] - Context is irreducibly important for LLMs.** High signal reasoning context minimizes hallucination. This holds regardless of how capable models become: a better LLM with poor context will still underperform a modest LLM with rich context.

**[AS-AELN] - Abstraction will continue to evolve, and language is the next layer.** The history of software is one example of a broader pattern: every discipline involving complex execution has progressively raised its level of abstraction. LLMs make intention expressible in natural language. But no level of abstraction removes the need to articulate what you want. The thinking cannot be delegated.

**[AS-MOSA] - Modularity is the only sustainable architecture.** Monolithic systems resist change, learning, and maintenance. The reasoning document hierarchy should mirror and enforce modular thinking from the start.

**[AS-CACM] - Execution artifacts alone will never carry their own motivation.** The gap between what an artifact does and why it exists cannot be closed by improving the artifact itself. It requires a separate, connected reasoning document maintained proactively. In software, this gap is most visible: code can be read but not interrogated for intent. But the same gap exists in any domain where complex reasoning precedes execution.

**[AS-PLHD] - Premature language hardens the object before it is fully known.** In domains where the problem itself is still being shaped, the words used to describe it carry a specific risk: they harden into reality before the object is fully understood. What gets named gets treated as settled. RFM's explicit, curated reasoning discipline is most valuable here, not because it prevents naming, but because it keeps the reasoning behind the names visible and contestable. The condition is not binary: it scales with how unsettled the object is and how consequential premature closure would be.

**[AS-QEUP] - Quality of execution, human or AI, is upstream of the reasoning investment.** Thinking first is not overhead. It is the highest leverage point in the entire development process.

The assumptions above are beliefs about the domain: why the problem exists and why it persists. The assumptions below are beliefs about what the methodology itself must do to address it.

**[AS-RDHL] - A reasoning document designed explicitly for both humans and LLMs simultaneously outperforms one designed for either alone.** This is not a natural default. It requires conscious design.

**[AS-TPAS] - The reasoning document hierarchy serves two structurally distinct phases, each with different design requirements.** In the first phase, human and LLM collaborate to build the reasoning documents: all eight sections, at every level of the hierarchy. Both parties must be able to read, contribute to, and challenge them. The design requirement is joint legibility. In the second phase, the completed documents are the source from which the LLM derives and executes across the artifact landscape: operational documents, glossary, code, and other domain-specific derivatives, without the human present at derivation time. The design requirement shifts to derivation-legibility: the documents must be complete and internally sufficient for autonomous execution. Documents optimised only for joint legibility will underperform at derivation. Documents designed only for derivation may be illegible to the human maintaining them. Both phases must be held simultaneously as design constraints.

**[AS-HLVS] - Hard lessons are as valuable as successes.** What failed, and why, carries as much reasoning value as what worked. A methodology that doesn't capture failure will repeat it.

**[AS-DSDH] - Document strain is diagnostic of hierarchy.** When a section strains under its own weight (too many options, too much detail, too many edge cases), that is a signal to branch into a new module, not a signal to write more carefully. The module structure is not designed upfront. It emerges from the writing. The hierarchy reveals itself through strain.

**[AS-DWHC] - Hard-contract domains require an operational document.** In domains where execution has hard contracts (software being the primary example), the reasoning document is accompanied by an operational document that carries constants, interfaces, procedures, and known values. It is a derivative of the reasoning, not a replacement for it.

**[AS-ADSR] - The reasoning discipline is self-reinforcing when held.** A well-reasoned document improves LLM execution. Better execution produces richer joint reasoning. Richer reasoning produces better documents. The loop degrades when either party breaks the discipline.

**[AS-TDEF] - An LLM's default pull is the tool role.** Instruction-following is what LLMs are trained and rewarded for, so the tool role is the behaviour available without effort. Co-authorship is not. Stating the role at session open does not install it, because that statement is one instruction competing with the training behind every other instruction in the session. The assumption breaks if models are trained such that collaboration rather than compliance is the default behaviour.

**[AS-EVID] - What RFM records generalises beyond the practitioner who recorded it.** Every pattern in these documents was observed by one person working with LLMs across several domains. The domains vary. The collaborator does not. The generality is believed on two grounds: patterns that recur across unrelated domains are unlikely to be properties of any one of them, and each pattern is stated with the reasoning that produced it, so a reader who was not present can test it against their own work rather than take it on report. Neither ground is observation by someone else. The assumption breaks when a practitioner working independently from the published documents reports that a recorded pattern does not hold in their practice, or hits a failure the documents do not predict.

---

## The Landscape

What would it take to treat reasoning as a hierarchical, living artifact, maintained at every level of a system, designed simultaneously for human understanding and LLM execution? Several approaches have addressed parts of this problem.

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **Agile** | Shifted focus from documentation-heavy waterfall to working software and human collaboration | Solved delivery rigidity but traded away reasoning continuity in the process |
| **Domain-Driven Design** | Made meaning an explicit design target. Gave us Ubiquitous Language and Bounded Contexts | Presupposes reasoning already exists; it structures meaning, it doesn't generate or preserve it |
| **Clean Code / TDD** | Made quality and correctness first-class concerns | Correctness is not the same as meaning. A perfectly tested system can still be incomprehensible |
| **Wardley Mapping** | Made situational awareness and strategic reasoning explicit, visual, and owned | Stops at the strategic level. Doesn't cascade into a connected reasoning practice at every level of execution |
| **Peter Naur's "Programming as Theory Building"** | Argued that programming is primarily the activity of building a theory of the problem; code is a secondary artifact of that theory. Anticipates RFM's founding insight. | Stops at the individual programmer's mental model. No structural artifact for capturing the theory, no survival mechanism beyond the person who holds it, no LLM dimension. |
| **ADRs** | Capture individual decisions | Not hierarchical. Not designed for LLM consumption. Document conclusions, rarely the full reasoning journey |
| **Context Engineering** | Recognizes that LLM output quality depends on input quality | Tactical: prompt-level thinking, not a systemic methodology |

*On Wardley Mapping and this methodology's lineage.* Wardley Mapping deserves more than a row in the table above. Its founding insight, that situational awareness requires making your assumptions about position, movement, and relationships explicit and visible, is philosophically the closest prior art to what this methodology attempts. The map analogy that runs through RFM is not borrowed from Wardley, but it is not independent of him either. It is convergent: two approaches that arrived at the same metaphor because the underlying insight is the same. Make your orientation legible. Reason from it explicitly. The author encountered Wardley's thinking directly in 2017 and that influence is real and honestly acknowledged here. What RFM attempts to add is the temporal discipline of reasoning before execution as a hard constraint, the explicit design of the reasoning artifact for both humans and LLMs simultaneously, and the co-authorship frame that makes that collaboration a practice. These are extensions into territory Wardley's framework did not need to address. They are offered in that spirit, as additions, not corrections.

*On Peter Naur and this methodology's closest prior art.* Naur's 1985 essay "Programming as Theory Building" is the closest diagnosis of the problem RFM addresses. His core claim, that programming is primarily the activity of building a theory, and that code is a secondary artifact of that theory, anticipates RFM's founding insight directly. What his essay does not provide is a structural prescription: no artifact for capturing the theory, no mechanism for the theory to survive beyond the person who holds it, and no anticipation of the LLM dimension: that disciplined externalization in text is sufficient for a system with no tacit knowledge to execute from it. Naur named the problem. RFM attempts to answer it.

**The gap:** none of these treat reasoning as a hierarchical, living, curated artifact that serves both phases of collaborative practice: joint human-LLM authorship, and autonomous LLM derivation from a completed document without the human present. No prior approach maintains this artifact at every level, from strategic intent to individual module, through the full life of a system.

---

## The Options Considered

**1. Better documentation practice combined with RAG**

More rigorous ADRs, wikis, enforced commenting standards, made accessible to LLMs through retrieval. Rejected because documentation captures *what* was decided, rarely *why*. It doesn't make assumptions explicit, doesn't record hard lessons, doesn't force reasoning through alternatives. RAG on top of poor documentation retrieves poor documentation faster. The structure of the artifact matters as much as its existence.

**2. Rely on increasingly capable LLMs**

If models become powerful enough, perhaps context matters less. Rejected because capability without context shifts the failure mode but doesn't eliminate it. A more powerful model makes more convincing mistakes. Research consistently shows that output quality is determined upstream of model capability: by the quality and structure of the context provided.

**3. Test and constraint driven development**

Enough tests and guardrails to control output without understanding internals. Rejected because as Dijkstra observed, testing shows presence of bugs, never absence. Control without comprehension scales poorly with complexity. You end up replacing understanding with surveillance.

---

## The Chosen Direction and Why

**Why the methodology is built around two distinct phases**

The methodology serves two structurally distinct goals. The first is joint reasoning: human and LLM collaborate to build the reasoning documents, each contributing across all eight sections at every level of the hierarchy. Neither can do this well alone. The collaboration is the point. The goal is a document hierarchy complete enough to act as the source for derivation.

The second is autonomous execution: once the reasoning documents are sufficiently complete, the LLM derives from them without the human present at derivation time. The full artifact landscape follows: operational documents, glossary, code, and other domain-specific derivatives. The quality of each derivative is determined entirely by the quality of its source document. The human-LLM collaboration produces the source. The LLM executes from it. This is the design intent the entire methodology is built to serve.

These two phases have different design requirements. The first requires joint legibility: both parties must be able to read, contribute to, and challenge the documents. The second requires derivation-legibility: the documents must be complete and internally sufficient for autonomous execution. Holding both simultaneously is the founding constraint of the methodology.

**Why reasoning is the primary artifact**

The goal is facilitated joint reasoning between human and LLM. Everything that follows (the reasoning artifact at the center, the temporal discipline of reasoning before execution, the fractal structure, the enforced curation) serves that goal. It is not about elegant documentation. It is about creating a shared interface through which both human and LLM contribute, execute, and stay honest.

The methodology places the reasoning artifact at the center of any practice where complex reasoning precedes execution. Not the code. Not the tests. Not the documentation. The reasoning: explicit, hierarchical, curated, and designed from the outset to serve both humans and LLMs simultaneously.

The methodology is called Reasoning-First Methodology, abbreviated RFM. The abbreviation carries a deliberate resonance with RTFM: the exasperated instruction issued when someone acts without reading first. That resonance is not accidental and is kept. The reasoning document is not a record of decisions. It is where decisions are made. A record is written after the fact and drifts. A decision-making interface is consulted before action and stays alive because it must. Every change to a system begins with a change to the reasoning document at the appropriate level. The execution artifact is the derivative. The document is the source.

**Why co-authorship is held against a pull rather than declared**

[AS-TDEF] states that the tool role is what an LLM reaches for without effort and that co-authorship is not. RFM treats the co-author posture as a condition maintained across a session, not a fact established by asserting it once. How an instruction reaches the moment where it would apply, and what that decides about the role it reinforces, is the subject of `RFM_instruction_design_reasoning.md`.

**Why the co-authorship sequence governs joint reasoning**

The joint reasoning sequence (propose → reflect → converge → execute) is the governing pattern through which co-authorship operates in practice. Both parties contribute through the first three steps. At the execution step, the natural division applies: the LLM formulates and edits, the human judges and confirms. This sequence is not a convenience; it is what keeps co-authorship from collapsing into either deference or unilateral authorship. The full reasoning for its design is in `RFM_prompts_reasoning.md`.

**Why the prompt system artifacts have distinct scopes**

The methodology travels through a prompt system of artifacts, each with a distinct scope. The full reasoning for the prompt system design is in `RFM_prompts_reasoning.md`.

**Why the same eight sections apply at every level**

The same eight sections, the same discipline, the same navigational practice, whether you are at the top of the hierarchy or deep inside a single module. Think of a geographic map: a country map and a street map use identical discipline at different resolution. The street map is a module of the country map, each complete at its own resolution, each connected to the level above it. This property (the same structure governing at every level) is what mathematicians call fractal. The term is precise and worth keeping: a fractal is not just a pattern that repeats, it is a pattern whose rules apply at every level. That is exactly what the reasoning document hierarchy is.

**Why the document is kept alive by curation**

A reasoning document that only grows becomes the thing it was designed to replace. A reasoning document visited only when something forces it stops being true. Curation answers both conditions. It does so by giving reduction the same standing as addition. The reasoning for how curation works is in `RFM_curation_reasoning.md`.

**Why RFM carries a curated improvement loop**

The methodology improves its documents through curation. It also has to improve the collaboration that produces them, and that is a different object with a different test. Curation asks whether an entry's reasoning still has a recipient. This asks whether something that went wrong once will go wrong again. A practice that answers only the first question can hold a perfect document set while repeating the same working failure every session.

So RFM carries a recurring step in which the collaboration reviews its own conduct, and a small number of observed patterns become standing rules or recorded lessons. Most candidates are refused. The refusal is the part that does the work, and it is the part that looks like waste from outside, because a review that writes nothing appears to have skipped its turn.

The loop's object is the project it runs in. It improves how this team reasons about this problem, and it produces rules that hold for this collaboration. What it does not do is edit RFM from inside the deployment. A methodology each deployment revises locally forks on first contact, and the reasoning that makes RFM portable would hold only until someone used it. An observation that looks general rather than local travels the other way instead, as input to the methodology's own project, where it meets the same refusal gate as anything else. That return path is how RFM receives evidence from outside itself without forking.

The alternative of letting practice improve when someone notices was rejected because noticing happens inside a session. Whatever is not written down while the session is open goes when the session goes, and the methodology is then unable to learn from its own use while remaining able to reason about everything else.

The alternative of promoting every candidate was rejected on the reasoning in `RFM_instruction_design_reasoning.md`. An instruction competes for adherence with every other instruction present, and adherence to any one of them falls as work continues. A rule set that grows without a refusal gate therefore buys each new rule by weakening all of them, including the rules that were earning their place. Accumulation degrades the thing it was meant to improve, which is why the gate is the design and the writing is the output.

The loop currently fires when a session ends, because that is the point at which a session's evidence is complete and still in view. That is where it fires, not what it is. If work with an LLM ever stopped being bounded by sessions, the loop would need a different trigger and would still be needed.

**Why the glossary travels with RFM regardless of domain**

The methodology generates its own disambiguation need. Terms like co-author, derivative, compression, and sweep appear across all RFM documents and carry meanings that diverge from their everyday use. A glossary is warranted not by domain-specific conditions but by the methodology's existence; it travels with RFM regardless of the domain it is applied in. The glossary is a reasoning artifact, not a reference artifact: it records why a term means what it means here, not just what it means. It is subject to the same curation discipline as any reasoning document.

**Why every project must name its vocabulary assumption**

The glossary travels with RFM because the methodology generates its own disambiguation need. But a project deploying RFM carries a second, distinct vocabulary requirement: the collaboration team building the reasoning documents must share enough vocabulary to reason together honestly.

This requirement is not always visible at project setup. A single-discipline team shares a vocabulary that feels transparent from inside it. A cross-disciplinary team brings different terminological frameworks to the same problem; the same term can carry different assumptions for different contributors, and that misalignment will surface as reasoning failures, not as vocabulary disagreements. The distinction matters: a team that diagnoses a reasoning gap when the actual cause is vocabulary drift will look in the wrong place.

To avoid vocabulary drift, the vocabulary stance of the collaboration team needs to be named at the start of any project. Two legitimate positions exist. First: the team shares domain fluency; jargon is in scope, and the reasoning documents need not define it. Second: the team spans disciplines; a disambiguation artifact is required, created at project setup, not retrofitted after reasoning is underway. The form of that artifact is a deployment decision; a standalone glossary is the default. What is not a deployment decision is whether the stance is named.

**Why this document alone carries inline definitions alongside glossary pointers**

`RFM_top_level_reasoning.md` is the entry point for a first-time reader arriving from GitHub. A practitioner reaches it after reading only the README; nothing else has prepared them for RFM's vocabulary. Every other reasoning document is read by someone who has already committed enough to work through the methodology, and for that reader a glossary pointer alone is sufficient. This asymmetry justifies a deliberate exception: this document defines a term inline at first use, in addition to pointing to the glossary, where doing so helps a cold reader continue without leaving the document. The exception is scoped to this document only. It is not a general license to duplicate the glossary, and it does not apply anywhere else in the document landscape.

**Why the methodology's operational document is separate from a project's**

Some domains have hard execution contracts. Software is the clearest case: constants, interfaces and named procedures have to be specified before execution is reliable. Those contracts are kept out of the reasoning document and carried in an operational derivative, which is what lets the reasoning stay portable across domains and across time.

There are two operational documents and they answer to different owners. The methodology's operational document carries the conventions every project inherits: the header convention, the ID scheme, version discipline, the formatting conventions, the failure taxonomy, the em dash check. It belongs to RFM and arrives with it. A project's operational document carries that project's execution contracts and belongs to the project. Where an inherited convention needs a project's value, the convention arrives and the value is set by the project.

RFM holds both roles, being the methodology and a project applying it, so it is the one place where the two documents describe the same practitioner. Every other project receives the first and writes the second.

The alternative was to let each project write its own conventions. That fails on retrieval rather than on principle. The sweep prompts and the skill operational documents name the operational document by filename, so a check reaches a session only if the convention it checks arrived with it. A project that wrote its own conventions would be running RFM's checks against a document those checks cannot describe.

**Why a reasoning document states a belief instead of defending it**

A reasoning document is read by someone deciding what to do next. Qualification written to anticipate a challenger is addressed to a different reader, one who is judging whether the author was careful. That reader does not exist for these documents, and writing for them costs the real reader twice: the claim gets longer, and it sits underneath the apparatus defending it rather than in front.

The alternative is to hedge as insurance. Soften the claim, and being wrong later costs less. This is rejected because RFM already handles being wrong, and handles it better. An assumption carries the conditions under which it breaks. That is a designated exit: when the world moves, the entry names what to check and the document changes. Hedging duplicates that function and degrades it, because a claim qualified into safety is harder to falsify, and a claim that cannot be falsified cannot trigger the revision the break condition exists to trigger.

Defensive qualification survives review because it reads as care. That is why it needs a named failure class rather than good intentions. The class is in the Failure Taxonomy in `RFM_operational.md`.

**Why prose derivatives carry a distinct prose style**

When RFM produces text-facing derivatives (public documentation, onboarding guides, worked examples), those artifacts carry a prose character that follows from the methodology's own epistemic commitments. That character is not imposed stylistically. It is derivable: reasoning-first methodology produces argument-first prose. Explicit uncertainty in the reasoning document produces explicit uncertainty in the derivative. Failure-mode orientation produces prose that names what could go wrong rather than what is hoped to be true. One committed position, honestly reasoned, produces a conclusion that can be tested, not five hedged alternatives that cannot.

This prose character is domain-agnostic. It does not depend on the practitioner's field or vocabulary. It follows from how RFM reasons, not from who is doing the reasoning.

A second requirement is legibility. Behavioral patterns common to LLM-generated text are recognizable to readers and undermine the signal before the content is reached. Suppressing them is not a stylistic preference. It is a condition for the derivative reaching its reader intact. The specific patterns and the two-layer writing discipline are in `RFM_operational.md`.

**Why prevention and correction share a failure taxonomy but not their questions**

RFM corrects document failures with sweeps and prevents them at the drafting moment. Both arms act on the same failure classes. Naming those classes separately in each arm produces the dilution failure recorded in `RFM_instruction_design_reasoning.md`: two artifacts restating one rule, drifting apart, with no owner holding it. The taxonomy has one owner.

The questions built on that taxonomy are not shared. A sweep asks whether a finished document contains a failure. A drafting check asks whether the content about to be written will introduce one. A single shared phrasing forces one arm to work with wording built for the other. That arm then re-derives its own version privately, which is the dilution the single owner was meant to prevent.

The owner is `RFM_operational.md` rather than a module operational document. Every project using RFM installs `RFM_operational.md`, because `RFM_traveling_prompt.md` and every skill operational document name it. No module operational document is named by any artifact a consuming project runs. Placing the taxonomy in a module operational document would add a file that a consuming project must deploy before it can draft.

**Why the top-level operational document may carry procedure derived from a module**

An operational document normally derives from the reasoning document at its own level. `RFM_operational.md` departs from that where a consuming project needs the content. Every project deploying RFM installs `RFM_operational.md`, because `RFM_traveling_prompt.md` and every skill operational document name it. No module operational document is named by any artifact a consuming project runs. Placing content a project needs in a module operational document would add a file that project must deploy before it can work.

The cost is that the derivation edge leaves the branch. Where it does, the operational section names its source, per the convention that a document states a source only where the edge leaves its branch.

**Why lifespan is a separate failure family**

The failure families divide by the property a reviewer checks. Structural failures concern where content sits. Language failures concern how content reads. Both are properties of the document in front of the reviewer, and both can be judged from it alone.

How long content stays true is not such a property. It depends on what is planned elsewhere. A sentence that will be falsified by scheduled work is correctly placed and clearly written, so a reviewer holding only the document has nothing to catch it with. The hard lesson in `RFM_curation_reasoning.md` on content written with a known expiry records what that costs when it is not caught.

Folding the failure into the language family was considered and fails on the language arm's own question. That arm asks whether a claim outruns its evidence. A forward-looking clause does not: it is accurate when written, and its evidence is the plan it names. Folding it into the structural family fails for the same kind of reason, since the sentence is in the section where its subject belongs.

Each family costs a question in every artifact that derives from the taxonomy, so families are added on demonstrated failures rather than on argument. This one is added on a recorded incident and on the two arms visibly passing the content that caused it.

**Why reasoning documents avoid count-dependent references**

Anything in a reasoning document whose correctness depends on a count remaining stable becomes a maintenance liability the moment the count changes. The failure is silent: the reference still reads as valid while the document has already drifted. The specific design decisions that follow from this principle are in `RFM_operational.md`.

**Why a filename and a type tag carry different facts**

Every RFM document is identified twice, once by its filename and once by the type tag in its header. The two are not one fact written in two places.

A filename identifies a document among its siblings in a directory listing, so it spends its middle on the subject: ripple check, unslop, human prompt. A type tag positions a document in the hierarchy for a reader who already has the file open and already knows its subject, so it spends itself on level and category: module reasoning, skill operational, top level reasoning.

Neither can absorb the other. Filenames built from a closed type list collapse to a handful of values that repeat across unrelated documents, and the directory listing stops distinguishing anything. Type tags built from the subject produce one value per file, which is a label rather than a type, and a tag set whose every value is unique cannot be checked against anything.

Separating the two is also what makes either one checkable. A closed type list can be searched for; the criterion that a convention is enforceable only where compliance reduces to a search is stated in `RFM_instruction_design_reasoning.md`. A filename pattern with a free subject slot is checkable at its ends, on the project prefix and the category suffix, and not in its middle. Two conventions, two checks.

**Why terminological discipline is a structural requirement when the object is unsettled**

When [AS-PLHD] applies (when the problem is still being shaped and the language used to describe it is itself forming), terminological discipline becomes a structural requirement, not a stylistic preference. Three practices follow from this. First, words actively used to describe an unsettled problem are shorthand candidates: each one should find its way into the glossary with explicit reasoning, not just a definition. Second, the research that builds the Landscape is where terminological maturity gets assessed: where established vocabulary exists across prior approaches, the object is more settled; where the research surfaces sparse, contested, or session-invented terminology, that is the moment to name the condition and raise the glossary discipline for this project. Third, the traveling prompt carries the instruction to watch for this signal during Landscape research: when the joint work is generating new vocabulary to describe a problem that isn't yet fully known, name it and treat each new term as a glossary candidate before it hardens.

**Why the methodology operates in two modes**

The methodology operates in two modes. Reasoning mode is the default: reasoning precedes execution, the document is the source, every change begins at the appropriate level of the hierarchy. Execution mode is invoked when delivery pressure makes the full reasoning discipline locally unacceptable: a deadline, a sprint, a time-boxed commitment. Execution mode is not a degraded version of the methodology. It is the correct response to a specific condition, provided the reasoning documents are sufficiently complete before pressure hits.

The reasoning documents then function as Commander's Intent, a military doctrine principle designed precisely for execution under pressure without communication up the chain: the commander's direction, boundaries, and assumptions are established in advance so that execution can adapt within that frame without stopping to re-reason at every decision point. The discipline shifts from reasoning before every action to executing within established reasoning. What execution mode requires is minimal capture: a running record of deviations from established reasoning, conscious deferrals, and broken assumptions, enough to make the return to reasoning mode honest rather than reconstructed from code.

This running record is a Chesterton's Fence log; see the glossary for the full definition. Chesterton's Fence is the principle that you should not remove a fence until you understand why it was built. Under execution pressure, fences do get removed; the log ensures that each removal is noted and why. The return to reasoning mode after pressure lifts is not optional. It is where execution mode's debts are paid.

**Why increasing autonomy raises the stakes for reasoning documents**

The most common objection to this approach is that increasingly capable and autonomous AI systems will eventually make it unnecessary. This misunderstands what the reasoning document is for. It is not a workaround for limited AI capability. It is the expression of human intent, human values, and human context applied to a specific problem. No level of AI autonomy removes the need for that; it only changes who executes once the intent is clear.

In fact, the more autonomous the system, the more critical the reasoning document becomes. A highly capable agent acting on vague or implicit intent doesn't fail cautiously. It fails confidently, at scale, and in ways that are difficult to trace or reverse.

Autonomy raises the stakes for clarity. It does not lower them.

The reasoning document is the deterministic anchor: the fixed, explicitly reasoned reference point against which agentic execution is measured. Agentic execution is where probabilistic reasoning is permitted, but within boundaries that have been explicitly reasoned, not assumed. At the execution level the deterministic/probabilistic split is largely resolved: structure and guarantees are owned by deterministic code, meaning and language by probabilistic LLM reasoning.


**Why readiness is decided by a first external trial rather than by a standard set in advance**

`[AS-EVID]` holds that what these documents record generalises beyond the one practitioner who recorded it, and it breaks when a practitioner working independently reports that a pattern does not hold. Nothing has been handed to anyone, so the assumption the document set rests on is the one assumption with no route to being tested.

The alternative was to define what a release must satisfy and build until it does. That designs from aspiration, which is the failure `[HL-DFMD]` warns against, and it fails on its own terms: the criteria would be written by the practitioner whose generality is in question. A standard reasoned out in advance cannot discover what a second person needs, because it is composed entirely of what the first person already knows.

So the release condition is a person. One practitioner, working from a handed-over set, with the documents doing the onboarding. RFM is worked with an LLM from the first session, so what is handed over must be sufficient for a model reading only the published set, not for a human reading cold. A model that infers past a gap produces a confident session that departs from the reasoning, and a newcomer has nothing to check it against.

What that person cannot do is the finding. The set they were handed is the release set, and it is defined by the trial rather than before it.
---

## The Boundaries

This methodology is explicitly not:

**A platform or tooling prescription.** No specific platform is prescribed. What the methodology does require of any practitioner deploying it: reasoning documents must be maintained in a format and location accessible to both human and LLM. Markdown satisfies this: human-readable, LLM-readable, version-controllable, and tool-agnostic. Where the document lives is a deployment decision, but accessibility to both parties is not optional.

**A replacement for domain expertise.** The methodology does not eliminate the need for skilled practitioners, domain experts, or specialists. It gives their expertise a structure to live in and a way to survive beyond the person who holds it.

**A documentation standard.** This is not about writing more or better documentation. It is about a fundamental shift in what the primary artifact of any reasoning-first practice is. Documentation describes a system after the fact. A reasoning document precedes and drives it.

**A methodology for AI development.** It does not prescribe how to build, train, or fine-tune AI models. It prescribes how to reason about and direct their use within a system.

**Designed to impose discipline on a team that won't bring it.** The deliberate return mode of curation requires a human who has a natural affinity for this kind of reflection. That is a people constraint, not a process gap. A team without such a person can follow the triggered mode but will gradually stop returning deliberately. The methodology will technically persist but quietly degrade. This is not a failure of the methodology. It is a boundary condition of its use.

**Designed to maintain full discipline under acute delivery pressure.** Delivery pressure is a specific, common condition under which the methodology's full discipline is at risk, not because teams stop believing in it, but because the local cost of the reasoning step becomes unacceptable when deadlines are close. This is distinct from the people constraint above: it affects willing teams in adverse conditions. The two-mode design (reasoning mode as default, execution mode under pressure) is the methodology's working hypothesis for this condition.

---

## The Open Questions

These are genuinely unresolved. They are not weaknesses; they are the honest frontier of the methodology. Some will be answered through practice. Others may reshape the methodology itself.

**[OQ-DRFT] The drift problem.**

How does a structural mechanism for detecting reasoning document drift from inside the system work, if one is achievable at all? The sweep prompts reduce the risk but require honest application to do so. Whether a mechanism exists that does not depend on that discipline remains open.

**[OQ-MVDC] The minimum viable document.**

How short can a reasoning document be and still work? The methodology must not become a bureaucratic burden. There is a minimum below which the document loses its value, and a maximum above which it becomes the thing it was designed to replace. Where are those boundaries in practice?

**[OQ-ONBQ] The onboarding question.**

RFM is not designed for broad adoption. The target is a self-selected newcomer with a natural affinity for deliberate reflection. For that person the question is not persuasion but sequencing: what is the right first experience, in what order, before the overhead becomes discouraging and before the value has been felt? That question is carried at the module level in `RFM_guided_drafting_prompt_reasoning.md`. What remains open here is whether the answer, once earned through practice, requires a corresponding change to the methodology's top-level assumptions about who RFM is for.

**[OQ-GDPG] The guided drafting generalization question.**

Whether the guided drafting prompt generalizes beyond the newcomer case to experienced practitioners starting a new project, or whether it remains a bounded onboarding artifact, is unresolved. The module was designed for one audience. Whether it serves a second has not been tested.

**[OQ-AUTB] The autonomy boundary.**

As agentic systems become more capable, where exactly is the line between what must be human-reasoned and what can be delegated? The methodology holds that human intent cannot be delegated, but the precise location of that boundary will need to be tested and refined in practice. The two-phase design itself depends on this boundary holding: if derivation always happens in the presence of the human, the distinction between joint legibility and derivation-legibility loses its force. Current agentic practice suggests the phases are genuinely distinct, and the distinction will sharpen as autonomy increases. What remains genuinely open is how a highly autonomous system should treat the reasoning document when acting without human oversight: where the reasoning document's authority ends and agentic judgment begins.

**[OQ-EVST] The evolutionary stage problem.**

The methodology is currently designed and validated at genesis stage: a single practitioner, early structure, everything still surprising. Whether the methodology itself needs to describe explicit transition points as a project matures remains open.

**[OQ-MCDC] The minimal capture discipline.**

Execution mode requires minimal capture: a record of deviations, deferrals, and broken assumptions sufficient to make the return to reasoning mode honest. What this looks like in practice is undesigned. How short can it be and still serve its purpose? What is the right artifact? A section appended to the reasoning document, a separate log, something else? How does a team distinguish a deviation worth capturing from noise? And what does the return-to-reasoning-mode session actually look like: what is its protocol, its output, its quality gate? These questions are unresolved. The two-mode design is a working hypothesis, not a tested practice.

**[OQ-DLTQ] The derivation-legibility threshold.**

The methodology names derivation-legibility as a design requirement for phase two: the reasoning documents must be complete and internally sufficient for autonomous LLM execution without the human present. What that threshold looks like in practice is partially known. One protocol has been tested: ask the LLM iteratively whether it could derive cleanly from the current documents alone, surface the assumptions it would have to make, reason through each one, adjust the documents accordingly, and repeat until the answer is yes. This protocol works: it surfaces undocumented assumptions, forces them into the documents, and produces a genuine readiness signal. What remains open is whether this protocol generalises across domains and document types, what makes some assumption-surfacing rounds more productive than others, and how derivation-legibility degrades as the system evolves and documents drift from it. The threshold has a working operationalisation; its reliability and generalisation remain to be tested.

---

## Hard Lessons

**Methodology design**

**[HL-DFMD] The document structure emerged from failure modes, not from best practices.**

The most robust design decision in the methodology was to derive the eight sections by asking "what causes humans and LLMs to fail?" rather than "what should a good document contain?" Designing from failure is more rigorous than designing from aspiration. This principle should be applied recursively, to every module document that follows.

**Document discipline**

**[HL-DMAP] A document set needs a map once a reader cannot tell from the documents themselves which one to read first.**

A reader or LLM encountering a project for the first time cannot orient from the top-level reasoning document alone. Navigation is not reasoning, but it is a prerequisite for reasoning about the right thing. The map and the README serve different readers and must not be merged. The map carries real version numbers, so a practitioner can detect drift between a document and what the project believes that document to be. The README carries orientation without versions, so a first-time reader is not asked to track state. A README that grows version numbers becomes a second map that drifts against the first. A map that drops them stops being able to detect drift at all.

**[HL-SELFREF] A map does not list the file it lives in.**

When `RFM_top_level_reasoning.md` was included as a map row, sessions updated the document header version without updating the corresponding map entry. The mismatch was invisible during the session and surfaced only at the next version check, where it had to be traced and corrected rather than having never existed. Excluding the containing document from the map it governs removes that maintenance surface. The same reasoning holds once a map moves into its own file. A file cannot record its own version twice without one copy going stale, and the copy in a standalone map would be its highest-churn row, bumped every session that touches any document in the set.

**[HL-MAPSCALE] A map moves into its own file when it needs structure that a list inside another document cannot carry.**

A large-scale deployment of RFM extracted its document map into a standalone file with its own version. Two additions followed: a category for maintained inputs that modules consume but do not own, and a set of task-specific read pathways naming which documents to read for which kind of work. The map's growth was the presenting symptom, but what the additions have in common is structure the embedded form could not hold. In RFM the same trigger fired at a much smaller size and for a different structure. The flat table records each document's level but not its parent, so sessions reconstructed the hierarchy by hand inside individual documents and the copies drifted. Row count was not the signal in either case. An embedded map is a tolerated exception to the rule that a reasoning document carries no procedure, and the exception holds only while the map stays a plain list.

**[HL-MAPCOPY] A document does not restate its own position in the hierarchy.**

Six operational documents carried a list of the documents to load before deriving from them. Every entry but one was the document's own branch read upward, which the map already states. The copies drifted, and three of them omitted the top-level document. A sweep entry condition existed to catch exactly that omission, which made the copies look load-bearing and kept attention on completing them. Two sessions repaired the lists before anyone asked whether the lists should exist. A document names a source in its own text only where the edge leaves its branch.

**[HL-DRIFT] The drift problem is not solved by the methodology; it is the methodology's greatest vulnerability.**

The methodology was designed to prevent documentation drift. But the reasoning document itself can drift from the system it describes. Naming this problem is not solving it. This lesson must stay visible until a genuine answer exists. The methodology's own curation discipline (triggered and deliberate return) addresses drift in principle but cannot guarantee it in practice. No structural mechanism yet exists to detect that failure from inside the system. One asymmetry is known: applying the methodology from inception is the only reliable prevention: reconstructed reasoning produces plausible documents, but not necessarily true ones. The sweep prompts, deliberately invoked corrective artifacts, reduce the risk of undetected drift, but require honest and regular application to do so. A team that invokes them performatively rather than genuinely will produce documents that appear current while describing a past state. Structural mechanisms for detecting that failure from inside the system remain an open question.

**Human-LLM collaboration**

**[HL-ERTA] Enthusiasm without red teaming produces fragile thinking.**

A methodology, or any reasoning document, only becomes robust when honest criticism is made explicit: not just "does this work?" but "what would break this?" The red team function must be built into the process, not added later. A reasoning document that has never been challenged is a reasoning document that hasn't been tested.

**[HL-LCAD] Long conversations with LLMs accumulate drift.**

Even a disciplined LLM develops bias over a long conversation: toward ideas that emerged in that conversation, toward framings that felt productive, toward connections that feel natural but weren't explicitly decided. This is subtle and hard to detect from inside the conversation. Drift is more dangerous than context window limits: it is invisible and cumulative. Two mitigations: first, the reasoning document should be complete enough to onboard a fresh LLM without loss; if it can't, the document isn't finished. Second, deliberately starting a new conversation with only the reasoning document as context is a useful quality check. A fresh LLM that misunderstands the direction reveals a gap in the document, not a gap in the conversation.

**[HL-WENO] The worked example is never optional, at any stage of the methodology's development.**

Theory without ground truth is hypothesis. Applying the methodology from inception, before any execution artifacts exist, proves the chain in both directions: reasoning document to derivative, with traceability at every step and no undocumented judgment calls made during implementation. Applying it to an existing project, where decisions have already been made without explicit reasoning, reveals that reconstructed reasoning produces plausible documents but not necessarily true ones. Both directions of experience are necessary.

**[HL-DIHQ] Deferred items must carry their context, not just their topic.**

When an item is parked as future work, the handover note captures what was deferred but not the context that surrounded it: what was understood, what was tried, what specifically remains open, and why the item stopped where it did. That context disappears with the session that produced it. The next session reopens the item cold and must reconstruct what was present but not captured. The fix is not a longer handover. It is a richer deferral record: each deferred item carries enough context that a fresh session can proceed without reconstruction. A topic label is not a deferral record.

**Execution practice**

**[HL-VGLE] RFM's value is gap-legibility, not gap-elimination.**

A well-reasoned document hierarchy will not prevent all gaps from appearing during execution. What it does is make gaps visible in the right place (as explicit reasoning debts, open questions, or provisional specifications) rather than letting them hide in code where they harden silently into undocumented decisions. A first application that produces no visible gaps has probably not been honest. A first application whose gaps surface at the reasoning level and are named there rather than discovered late in implementation is working correctly.

**[HL-DCFL] Derivation failures can originate in source documents that are internally sound.**

A reasoning document can be internally correct and still produce derivation failures. The failure mode identified in practice: two distinct concepts stated in close proximity in a Chosen Direction entry collapsed into one during LLM derivation under compression. The source document treated them as distinct. The deriving LLM conflated them. The document was not wrong. It was not sufficiently derivation-legible. This is the practical consequence of the two-phase design requirement named in [AS-TPAS]: joint legibility and derivation-legibility are different properties, and a document can satisfy one without satisfying the other. The mitigation is not longer or more detailed source writing. It is structural separation: concepts that must remain distinct at derivation time must be visibly distinct in the source, with enough distance or explicit differentiation that compression cannot collapse them.

**[HL-OQGATE] A stated dependency between two Open Questions is read as an order of work.**

One entry closed by saying it could not be settled while another remained open. The dependency was accurate and the entry claimed nothing about priority. It did not need to. A session deciding what to work on finds the only sequencing claim in the section and follows it, so the wording set the agenda, and the work that followed was measurement of a quantity that did not need measuring. Say what one question needs from another, and say whether anything actually waits on it.

---

*top_level_document // [living]*
*the reasoning arrived before the structure did*
*that was the right order*

**[HL-REPAIR] Work framed as defect repair skips the reasoning step, because repair appears to carry no design decision.**

Six documents were edited in one session to add a missing entry to their source lists. The lists themselves were the defect. Each edit made the copied content more complete, and the copy was what should not have existed. Repair presents as restoring a known-good state, so nothing in the framing prompted the question of whether the artifact being repaired should exist at all. The discipline that reasoning precedes execution was not overridden by a decision. It never engaged, because no one recognised that a change to a system was being made.

**[HL-BORVOC] A structure adopted from another project carries that project's vocabulary, and the vocabulary encodes that project's problem.**

The map file design was taken from a project using RFM at larger scale. The first draft arrived carrying governance, governed registry, version authority, read pathways and watchpoints. RFM uses none of those words. Each named a concern the other project has and RFM does not, and taking them would have installed those concerns without anyone deciding to. Adopting a structure requires re-deriving its terms in the adopting project's own vocabulary before any of it is written.

**[HL-ADJCHK] A failure type named correctly in the taxonomy still fires, when the checks derived from it test something adjacent to what the type says.**

The language family names text written for the session that produced it rather than for a future reader. The drafting pre-check derived from that family asked whether a reader outside the session would understand the content. A sentence explaining why a section was left out passes that question. A later reader understands it, and it is still addressed to the person reviewing the draft rather than the person reading the document. Comprehension was tested where audience was the failure. A derived check has to be read back against the type it derives from, not only against the content it will run on.

**[HL-DEFOWN] A deferred item that names its owner is read by the next session as having ruled on it.**

An item deferred at the end of one session recorded that the sweep prompts might need a replacement entry condition, and named the check to put in them. The gap was real. The placement was a design decision no session had ruled. The next session opened the item and began drafting into the sweep module, because an item that arrives with a destination presents the destination as part of the problem rather than as the first thing to decide. The check belonged in the operational document that installs with the methodology, and the sweeps took no entry condition at all. A deferred item states the gap; where the fix goes is work the receiving session has to do.

**[HL-ENUM] A list that names its members is a count-dependent reference with no number in it.**

`RFM_operational.md` bars statements whose correctness depends on a count remaining stable, and every form it named at the time carried a numeral or an ID. A sentence introducing the execution artifacts as "the traveling prompt, sweep prompts, and human prompt" carried neither, and was wrong by two: the derivation prompt and the guided drafting prompt had been added since it was written. The list had gone stale in place while the rule that covers it stayed satisfied on its face. The test that catches this is whether adding a member to the set would falsify the sentence, which is the same test the count forms fail, applied to enumeration rather than to a number.

**[HL-CFSRCH] A grounding search assembled from the claim returns confirmation and cannot return a null.**

A module's central mechanism was grounded by searching for degradation, drift, instruction decay and lost in the middle. Every term presupposed the effect, so the pass returned work that had found it and no work that had not, and the result read as evidence rather than as the shape of the query. The document was written on a paper two years old testing a model three generations old, stated without qualification, and it passed the author's own review. The failure surfaced only when the human asked whether recency had been over-weighted, which is a question about a different bias, and answering it required going back to publication dates rather than to findings. Search terms for a grounding pass belong to the break condition of the belief being tested, not to the belief. A search assembled from the belief contains none of the words a contrary result would be written in, so finding no contrary result carries no information.

**[HL-PARTRUL] A ruling executed in part reads as executed in whole.**

A joint decision usually carries more than one obligation, and the obligations land in different documents. Executing the most visible one changes the document a reader would check first, so the decision looks done from every later vantage point, while the remainder has no owner and produces no error anywhere. The worked example is the decision to treat session-boundary delivery as belonging to the methodology rather than as a workaround for a limitation. The assumption admitting it was written and the affected Problem section was made generic, which is what any review would have looked at. Three obligations went unwritten: the grounding sentence naming where the module's evidence came from, the question of whether the methodology ships an artifact type for that class, and the header of the file that still described itself in the terms the ruling had overturned. The debt then moved out of sight, because the reasoning it attached to migrated to a different assumption entry and the unpaid part travelled with it unremarked. What closes this is naming every obligation a ruling creates at the moment of the ruling, in the session record, rather than trusting that executing the ruling will surface them.

**[HL-RECFACT] A record of a fact is not a definition of it.**

The map records which files are documents. That record was then written as the rule for what a document is: "a file with a row is a document". A directory holding other projects' reasoning documents has a row for navigation, and the rule turned it into a document. The same inversion from the other side: a skill bundle has nowhere to write the version header, and the missing line was read as the type having no instances. The pull is that the record is searchable and the fact is not, so a rule stated in terms of the record looks like the more precise one. It is the less precise one, and it is wrong at the first case where the record and the fact come apart. The tell is a rule that starts from where something is written rather than from what it is.

**[HL-DUAL] A project that is also its own methodology cannot see the boundary between them in its own documents.**

The Chosen Direction entry on operational documents said they are domain-specific. That was written about a project's operational document and read for months as covering every operational document, including RFM's own, which carries the header convention, the ID scheme, version discipline, the formatting conventions and the failure taxonomy. None of that belongs to a domain. The error stayed invisible because RFM's single operational file legitimately answers to both readings: it is the methodology's, and it is also this project's. A worked example that is also the thing being exemplified satisfies a claim about either role, so a claim true of one and false of the other reads as true. What surfaced it was a question from outside the document set, asking what a different practitioner would receive.
**[HL-SETMEM] A claim about which documents carry or name something is asserted from memory, because it reads as a description of the set rather than as a claim about it.**

The document set is searchable, so the check costs one search, and that is not what stops it being run. What stops it is that the sentence does not present itself as evidence-bearing. Two forms recur. Content is held to be unhomed when `RFM_map.md` already carries it in its own rows, which turns a separation into a fork where a subtraction was correct. And a hardcoded filename is held to be load-bearing because several documents name it, when those documents are outside the scope being reasoned about, which preserves a dependency for a reader who never receives it. Both assertions are usually right, and being usually right is what keeps them unchecked. The tell is a sentence that says how many documents do something with no search behind it. This is not `[HL-ENUM]`, where a list already written into a document goes stale as the set changes. Here nothing is written down: the set is reasoned about and never counted.
