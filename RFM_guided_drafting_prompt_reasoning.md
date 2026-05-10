# Reasoning-First Methodology — Guided Drafting Prompt Reasoning Document
`v0.0.0.1` // `module_reasoning` // [living]

---

## The Problem

The traveling prompt calibrates the LLM's collaborative posture. The human prompt calibrates the human's. Neither is designed for a newcomer encountering RFM for the first time and attempting to produce their first reasoning document.

A newcomer who reads the methodology can understand what a reasoning document is. What they cannot get from reading is the experience of reasoning through one — the discipline of recognizing what belongs in each section and what doesn't, the discipline of staying in a section before moving to the next, the difference between an assumption and a description, between a boundary and a constraint. That understanding only comes from doing it, with guidance that teaches the intention behind each section rather than its definition.

Without a guided drafting prompt, the newcomer's first reasoning document is produced either alone — with the section definitions as the only guide, which tends toward checklist behavior — or in an unstructured conversation with an LLM that has no mandate to teach the reasoning discipline. Both paths produce a document that looks correct and reasons poorly. The guided drafting prompt closes that gap: it walks a newcomer through their first reasoning document section by section, teaching intention, not form.

The guided drafting prompt is a deliberate response to a specific risk: that RFM, encountered for the first time, can look overwhelming. A methodology with eight sections, a document hierarchy, and a co-authorship frame asks a lot of a newcomer before they have produced anything. The prompt exists to lower that entry cost — not by simplifying the methodology, but by absorbing the structural difficulty. The newcomer brings a genuine problem and honest thinking. The prompt supplies the structure and the questions; the co-author holds the discipline.

---

## The Assumptions

**[AS-AWCP] — The newcomer understands the methodology at least partially before the session begins.** The guided drafting prompt is not an introduction to RFM. It assumes the newcomer has read the README and the top-level reasoning document — enough to know what a reasoning document is and why it exists. A reader who has not done that groundwork will find the prompt's section-by-section guidance unanchored. That is a prerequisite condition, not a failure of the prompt.

**[AS-CBID] - Checklist behavior is the default failure mode for a first-time author.** Without active guidance on intention, a newcomer will treat the eight sections as boxes to fill — producing content that satisfies the section definition without reasoning through it. The prompt must actively resist this tendency, not assume the newcomer will resist it themselves.

**[AS-LREG] - The Landscape section requires grounding in current external knowledge that the newcomer may not have.** Every other section can be drafted from the newcomer's own reasoning. The Landscape requires knowing what approaches already exist in the relevant domain. Without that knowledge — or without a mechanism to acquire it during the session — the Landscape will either be thin or invented.

**[AS-CBTM] - Understanding the methodology does not resolve the cost/benefit timing mismatch of the first document.** A newcomer who knows what a reasoning document is may still stall when the first section proves harder than expected and the benefit feels distant.

**[AS-LLNB] - The "livingness" of RFM documents substantially lowers the barrier for a newcomer — if it is made explicit.** A newcomer who understands that the first document does not need to be complete, correct, or final — only honest and structured — faces a different task than one who believes the artifact must be authoritative before it is useful. RFM's founding commitment to living, curated documents means the first version is a starting point, not a deliverable.

---

## The Landscape

The question this landscape must answer is: what approaches exist for guiding a newcomer through their first structured reasoning artifact — section by section, with the intention behind each section taught rather than its definition?

| Approach | What it does | Why it's insufficient for the guided drafting prompt |
|---|---|---|
| **Scaffolded writing pedagogy** (SFL genre-based pedagogy, Teaching and Learning Cycle) | Makes the stages of a structured artifact explicit — their goals, their language, their sequence — and supports learners through modelling and guided practice. The strongest evidence base for structured first-document production | Designed for text types with stable social purposes (academic argument, report, narrative). Does not address artifacts whose primary value is reasoning integrity rather than communicative form. No mechanism for teaching the intention behind a section — only its definition and linguistic features |
| **Socratic LLM facilitation** | Uses questioning rather than answering to guide a learner toward their own reasoning. Research shows LLMs that give answers rather than ask clarifying questions produce weaker learning and weaker artifacts | Designed for discrete problem-solving tasks (debugging, case-based clinical reasoning). Not designed for a multi-section artifact where section sequence matters and where the learner must stay in a section long enough to reason through it before moving forward |
| **ADR onboarding and LLM-assisted ADR generation** | Captures architectural decisions in lightweight structured form; recent work uses LLMs to assist drafting from code context or prior decisions | ADRs document conclusions — context, decision, consequences. They do not teach the reasoning discipline that precedes a decision. LLM-assisted ADR generation automates the artifact, which is the opposite of what the guided drafting prompt must do. The adoption barrier for ADRs is well-documented: the cost is paid immediately by the author, the benefit accrues to future readers — RFM faces the same barrier, and no existing approach addresses it through guided first-document production |
| **Facilitation frameworks** (ToP, ORID Focused Conversation, workshop facilitation methodology) | Guides groups through structured processes — from observation to reflection to interpretation to decision — with a facilitator holding the sequence | Designed for group decision-making in real time. The facilitator role is human. The artifact produced is a decision or action plan, not a living reasoning document. No mechanism for the non-linear revision loop that the Landscape section requires |

**The gap:** no existing approach combines section-by-section guidance with reasoning intention (not definition), a facilitator that questions rather than answers, and a built-in revision loop after the Landscape — where research can sharpen what was written before it. The guided drafting prompt occupies that gap specifically.

---

## The Options Considered

**1. Directive vs. Socratic facilitation mode**

Tell the newcomer what belongs in each section — definitions, examples, what good looks like — vs. ask questions that draw the reasoning out. Directive mode is faster and feels safer to a newcomer who doesn't know what to write. Rejected because directive mode produces the failure the prompt exists to prevent: a newcomer who fills sections correctly without reasoning through them. A section definition handed to the newcomer becomes a template. A question the newcomer must answer from their own thinking becomes reasoning. The Socratic mode is slower and requires the newcomer to tolerate uncertainty — which Assumption 4 names as a genuine risk. That risk is managed by making the "livingness" commitment explicit early (Assumption 5), not by retreating to directive mode.

**2. Linear vs. non-linear session structure**

Walk the newcomer through the eight sections in strict sequence vs. build in an explicit revision loop after the Landscape — returning to The Problem and The Assumptions to ask whether the research sharpened or changed what was written there. Linear sequence is simpler to follow and easier to design. Rejected because the Landscape section is the one point in the sequence where external research enters, and research changes things. A newcomer who completes The Problem and The Assumptions, conducts Landscape research, and then moves directly to Options Considered without revisiting will carry imprecise early sections forward into every subsequent section. The revision loop is not optional — it is the mechanism by which the Landscape earns its place in the sequence. The prompt must build it in explicitly and explain why, not leave it as an implied possibility.

**3. Single prompt vs. multi-turn scaffold**

One prompt the newcomer pastes at the start of a session — governing the LLM's behavior throughout — vs. a designed multi-turn interaction where the prompt issues section-by-section instructions as the session progresses. A single prompt is simpler to deploy and consistent with how the traveling prompt works. A multi-turn scaffold gives the LLM more control over pacing and can respond to where the newcomer actually is. Rejected because a multi-turn scaffold requires the LLM to manage session state and decide when to move forward — which collapses the newcomer's agency into the LLM's judgment. The newcomer must own the decision to move from one section to the next. A single prompt that governs the LLM's facilitation mode throughout the session preserves that ownership. The LLM guides. The newcomer decides.

---

## The Chosen Direction and Why

**Why the prompt's primary reader is the LLM, not the newcomer**

The guided drafting prompt governs LLM behavior during the session — what it asks, how it holds the Socratic mode, when it builds in the revision loop, how it responds when the newcomer pushes for directive answers. That is the same job the traveling prompt does, scoped to this specific session type. A prompt written for a human reader produces a different artifact: a guide, an orientation document, a set of instructions the human follows. Those are not wrong artifacts — they are different ones. The guided drafting prompt is a behavioral specification for the LLM. The newcomer reads it too, which means the framing must be legible to them — but legibility for the newcomer is a constraint on the prose, not a change to the primary reader. What the newcomer reads is a description of how the session will work. What the LLM reads is its instruction set.

**Why Socratic facilitation over directive mode**

The failure the guided drafting prompt exists to prevent is a newcomer who produces a correctly structured document without reasoning through it. Directive mode — definitions, examples, what good looks like — hands the newcomer a template. A template answered is not a reasoning document. It is a form. The Socratic mode draws reasoning out through questions the newcomer must answer from their own thinking. This is slower and requires tolerating uncertainty. That friction is the point — it is the signal that genuine reasoning is happening. The prompt manages the motivational risk (Assumption 4) by making the livingness commitment explicit early (Assumption 5), not by reducing the cognitive demand. Reducing the cognitive demand is the failure mode, not the mitigation.

**Why the revision loop after the Landscape is non-negotiable**

The Landscape is the one section where external knowledge enters the session. Research changes things — it sharpens problem statements, reveals assumptions that were imprecise, and occasionally reframes the problem entirely. A newcomer who completes The Problem and The Assumptions, conducts Landscape research, and moves directly to Options Considered carries imprecise early sections forward into every subsequent section. The revision loop is the mechanism by which the Landscape earns its place in the sequence. The prompt must make this explicit and explain why — not leave it as an implied possibility the newcomer may or may not take.

**Why the session must remain open to closing early — honestly**

If the Landscape research reveals that a solution to the newcomer's problem already exists, the honest response is to name that and close the reasoning document there. Continuing into Options Considered and Chosen Direction when the Landscape has already answered the question produces a document that reasons toward a conclusion the research already supplied — that is not reasoning, it is retrofitting. The prompt must make this possibility explicit: a reasoning document that closes after the Landscape because the Landscape resolved the problem is not a failed session. It is an honest one. The co-author's job at the Landscape stage includes asking directly whether the research has changed what the newcomer believed their problem to be — and whether continuing is still warranted.

**Why a single prompt over a multi-turn scaffold**

The newcomer must own the decision to move from one section to the next. A multi-turn scaffold that manages pacing collapses that ownership into the LLM's judgment — the LLM decides when the section is complete, when to move forward, when to loop back. That is the wrong division of labor at the execution step of the joint reasoning sequence. A single prompt that governs the LLM's behavior throughout the session preserves the newcomer's ownership of that decision. The LLM contributes through questions and pushback. The newcomer decides when a section has been reasoned through honestly enough to move forward.

**Why the guided drafting prompt layers over the traveling prompt rather than replacing it**

The traveling prompt governs collaborative posture — it is always present. The guided drafting prompt governs session behavior for a specific task — it is invoked for a newcomer's first reasoning document. They are not in conflict. The traveling prompt stays silent on what it has no instruction about. The guided drafting prompt operates within the posture the traveling prompt establishes. The "too much" risk is real but the resolution is scoping, not reduction. A well-scoped guided drafting prompt does not override the traveling prompt. It narrows the session's focus within it.

**Why the livingness commitment is stated before section work begins**

A newcomer who understands that the first document needs only to be honest and structured — not complete or authoritative — faces a different task than one who doesn't. That understanding doesn't come from having read the methodology. It comes from hearing it stated as permission at the moment the cost of starting is highest. The prompt makes explicit — before the first section opens — that the document is a living artifact: a starting point, not a deliverable.

**Why the guided drafting prompt must establish the co-author posture before section work begins**

The joint reasoning sequence — propose, reflect, converge, execute — governs how both parties work together. This applies to a newcomer's first reasoning document as much as to any other session. The LLM is not a facilitator guiding the newcomer through a process. It is a co-author contributing to the reasoning, red teaming weak thinking, and holding the methodology discipline jointly. The guided drafting prompt must make this explicit before the first section opens — not leave it to be inferred from the traveling prompt. A newcomer who arrives treating the LLM as a sophisticated assistant will push it into tool mode regardless of what the traveling prompt instructs. Establishing the co-author posture is the first job of the guided drafting prompt, not a precondition it can assume has been met.

---

## The Boundaries

**Not an introduction to RFM.** The guided drafting prompt assumes the newcomer has read the README and the top-level reasoning document. It does not explain what a reasoning document is or why it exists. A newcomer who arrives without that orientation will find the section-by-section guidance unanchored.

**Not a template.** The guided drafting prompt does not tell the newcomer what to write. It draws reasoning out through questions. A session that produces a correctly structured document without genuine reasoning has not succeeded — it has produced the failure the prompt exists to prevent.

**Not a one-session guarantee.** The first reasoning document produced with the guided drafting prompt will be imperfect. That is expected and correct. The livingness commitment means the document is a starting point, not a deliverable. The prompt cannot guarantee a complete or fully reasoned first document — only an honest one.

**Not a substitute for the traveling prompt.** The guided drafting prompt governs a specific session for a specific purpose. The traveling prompt governs collaborative posture across all sessions. Both are required. The guided drafting prompt operates within the posture the traveling prompt establishes — it does not replace it.

**Not designed for a newcomer who arrives without any problem at all.** The guided drafting prompt cannot generate the problem the reasoning document must address — that genuine starting point must come from the newcomer. But it does not need to be sharp before the session begins. The co-authorship in the session is precisely what sharpens it. A newcomer who arrives with a genuine but half-formed problem and reasons through it honestly will often produce a better problem statement at the end of The Problem section than they could have articulated before the session started. That sharpening is not a side effect — it is one of the primary values the guided drafting prompt delivers.

---

## The Open Questions

**[OQ-SMDP] Whether the Socratic facilitation mode holds under motivational pressure.**

A newcomer who stalls may push the LLM toward directive mode — asking directly for definitions, examples, or what to write. Whether the prompt can be designed to hold the Socratic mode under that pressure without losing the newcomer entirely is untested. The livingness commitment ([AS-LLNB]) is the primary mitigation — but whether it is sufficient to sustain engagement when the first section proves genuinely hard is an open question.

**[OQ-GDNP] Whether the guided drafting prompt is useful beyond its primary scope.**

The prompt was designed for a newcomer's first reasoning document. A first reasoning document for a new project — written by an experienced RFM practitioner — shares many of the same characteristics: the problem is not yet sharp, the assumptions are untested, the landscape is unmapped. Whether the guided drafting prompt serves that case as well as the newcomer case, or whether a separate artifact is warranted, is undesigned.

---

## Hard Lessons

**[HL-LRRL] The section sequence is not strictly linear — the Landscape can require revising what came before it.**

Drafting The Problem and The Assumptions first, then conducting Landscape research, then returning to ask whether the research sharpens or adjusts the first two sections produced better documents than treating the sequence as a one-way pass. The Landscape can reveal that an assumption was imprecise or that the problem statement was narrower than the domain warrants. The guided drafting prompt must build this revision loop in explicitly — and the newcomer must be told why, not just instructed to do it.

---

*v0.0.0.1 // module_reasoning // [living]*
*the guided drafting prompt is the derivative*
*this document is the source*
*the reasoning comes first — the prompt follows*