# Reasoning-First Methodology: Guided Drafting Prompt Reasoning Document
`v0.2.0` // `module_reasoning` // [living]

---

## The Problem

The traveling prompt calibrates the LLM's collaborative posture. The human prompt calibrates the human's. Neither is designed for a newcomer encountering RFM for the first time and attempting to produce their first reasoning document.

A newcomer who reads the methodology can understand what a reasoning document is. What they cannot get from reading is the experience of reasoning through one: the discipline of recognizing what belongs in each section and what doesn't, the discipline of staying in a section before moving to the next, the difference between an assumption and a description, between a boundary and a constraint. That understanding only comes from doing it, with guidance that teaches the intention behind each section rather than its definition.

Without a guided drafting prompt, the newcomer's first reasoning document is produced either alone (with the section definitions as the only guide, which tends toward checklist behavior) or in an unstructured conversation with an LLM that has no mandate to teach the reasoning discipline. Both paths produce a document that looks correct and reasons poorly. The guided drafting prompt closes that gap: it walks a newcomer through their first reasoning document section by section, teaching intention, not form.

The guided drafting prompt is a deliberate response to a specific risk: that RFM, encountered for the first time, can look overwhelming. A methodology with eight sections, a document hierarchy, and a co-authorship frame asks a lot of a newcomer before they have produced anything. The prompt exists to lower that entry cost, not by simplifying the methodology, but by absorbing the structural difficulty. The newcomer brings a genuine problem and honest thinking. The prompt supplies the structure and the questions; the co-author holds the discipline.

---

## The Assumptions

**[AS-CBID] - Checklist behavior is the default failure mode for a first-time author.** Without active guidance on intention, a newcomer will treat the eight sections as boxes to fill, producing content that satisfies the section definition without reasoning through it. The prompt must actively resist this tendency, not assume the newcomer will resist it themselves.

**[AS-CBTM] - Understanding the methodology does not resolve the cost/benefit timing mismatch of the first document.** A newcomer who knows what a reasoning document is may still stall when the first section proves harder than expected and the benefit feels distant.

---

## The Landscape

| Approach | What it does | Why it's insufficient for the guided drafting prompt |
|---|---|---|
| **Socratic LLM facilitation** | Uses questioning rather than answering to guide a learner toward their own reasoning. Research shows LLMs that give answers rather than ask clarifying questions produce weaker learning and weaker artifacts | Designed for discrete problem-solving tasks (debugging, case-based clinical reasoning). Not designed for a multi-section artifact where section sequence matters and where the learner must stay in a section long enough to reason through it before moving forward |

**The gap:** no existing approach combines section-by-section guidance with reasoning intention (not definition), a facilitator that questions rather than answers, and a built-in revision loop after the Landscape, where research can sharpen what was written before it. The guided drafting prompt occupies that gap specifically.

---

## The Options Considered

**1. Directive vs. Socratic facilitation mode**

Tell the newcomer what belongs in each section (definitions, examples, what good looks like) vs. ask questions that draw the reasoning out. Directive mode is faster and feels safer to a newcomer who doesn't know what to write. Rejected because directive mode produces the failure the prompt exists to prevent: a newcomer who fills sections correctly without reasoning through them. A section definition handed to the newcomer becomes a template. A question the newcomer must answer from their own thinking becomes reasoning. The Socratic mode is slower and requires the newcomer to tolerate uncertainty, which Assumption 4 names as a genuine risk. That risk is managed by making the "livingness" commitment explicit early (Assumption 5), not by retreating to directive mode.

**2. Linear vs. non-linear session structure**

Walk the newcomer through the eight sections in strict sequence vs. build in an explicit revision loop after the Landscape, returning to The Problem and The Assumptions to ask whether the research sharpened or changed what was written there. Linear sequence is simpler to follow and easier to design. Rejected because the Landscape section is the one point in the sequence where external research enters, and research changes things. A newcomer who completes The Problem and The Assumptions, conducts Landscape research, and then moves directly to Options Considered without revisiting will carry imprecise early sections forward into every subsequent section. The revision loop is not optional: it is the mechanism by which the Landscape earns its place in the sequence. The prompt must build it in explicitly and explain why, not leave it as an implied possibility.

**3. Single prompt vs. multi-turn scaffold**

One prompt the newcomer pastes at the start of a session, governing the LLM's behavior throughout, vs. a designed multi-turn interaction where the prompt issues section-by-section instructions as the session progresses. A single prompt is simpler to deploy and consistent with how the traveling prompt works. A multi-turn scaffold gives the LLM more control over pacing and can respond to where the newcomer actually is. Rejected because a multi-turn scaffold requires the LLM to manage session state and decide when to move forward, which collapses the newcomer's agency into the LLM's judgment. The newcomer must own the decision to move from one section to the next. A single prompt that governs the LLM's facilitation mode throughout the session preserves that ownership. The LLM guides. The newcomer decides.

---

## The Chosen Direction and Why

**Why Socratic facilitation over directive mode**

The failure the guided drafting prompt exists to prevent is a newcomer who produces a correctly structured document without reasoning through it. Directive mode (definitions, examples, what good looks like) hands the newcomer a template. A template answered is not a reasoning document. It is a form. Socratic mode guards against this by keeping the reasoning with the newcomer: questions draw out what the newcomer must answer from their own thinking.

Socratic mode does not mean the LLM withholds its own reasoning. The co-author role remains fully active: the LLM proposes, red teams, and contributes genuinely throughout the session. The constraint is narrow: the LLM does not fill sections on the newcomer's behalf. Within that constraint, the session is genuine co-authorship. A newcomer who experiences the LLM reasoning alongside them, rather than extracting their reasoning through interrogation, will understand what RFM co-authorship feels like before they have finished their first document. That experience is part of what the guided drafting session is designed to produce.

The constraint is narrow and must be held as such: Socratic mode governs section-filling, not claim-challenging. When a newcomer states something with more confidence than the evidence supports, that is a red team moment, not a drawing-out moment. The LLM's job at that point is to challenge, not to ask another question. Socratic mode and the red team function are not alternatives. They operate on different objects and must both remain active throughout the session.

**Why the LLM names the pressure explicitly rather than yielding to it**

When a newcomer pushes for directive answers (asking what to write, requesting definitions, or expressing frustration with questions), the path of least resistance is to yield. Yielding feels like care. It is the failure mode. The LLM's counter-move is to name what is happening rather than either yielding or simply repeating the question: "you are asking me to fill this section; my job is to draw your reasoning out." Naming the pressure makes it visible to the newcomer without making it adversarial. After naming it, the LLM returns to questions from a different angle, not the same question repeated, which compounds frustration, but a different entry point into the same reasoning gap. This move is the Socratic mode held under pressure, expressed as co-author behavior rather than rule-following.

**Why the revision loop after the Landscape is non-negotiable**

The Landscape is the one section where external knowledge enters the session. Research changes things: it sharpens problem statements, reveals assumptions that were imprecise, and occasionally reframes the problem entirely. A newcomer who completes The Problem and The Assumptions, conducts Landscape research, and moves directly to Options Considered carries imprecise early sections forward into every subsequent section. The revision loop is the mechanism by which the Landscape earns its place in the sequence. The prompt must make this explicit and explain why, not leave it as an implied possibility the newcomer may or may not take.

**Why the session must remain open to closing early, honestly**

If the Landscape research reveals that a solution to the newcomer's problem already exists, the honest response is to name that and close the reasoning document there. Continuing into Options Considered and Chosen Direction when the Landscape has already answered the question produces a document that reasons toward a conclusion the research already supplied; that is not reasoning, it is retrofitting. The prompt must make this possibility explicit: a reasoning document that closes after the Landscape because the Landscape resolved the problem is not a failed session. It is an honest one. The co-author's job at the Landscape stage includes asking directly whether the research has changed what the newcomer believed their problem to be, and whether continuing is still warranted.

**Why a single prompt over a multi-turn scaffold**

The newcomer must own the decision to move from one section to the next. A multi-turn scaffold that manages pacing collapses that ownership into the LLM's judgment: the LLM decides when the section is complete, when to move forward, when to loop back. That is the wrong division of labor at the execution step of the joint reasoning sequence. A single prompt that governs the LLM's behavior throughout the session preserves the newcomer's ownership of that decision. The LLM contributes through questions and pushback. The newcomer decides when a section has been reasoned through honestly enough to move forward.

---

## The Boundaries

**Not an introduction to RFM.** The guided drafting prompt assumes the newcomer has read the README and the top-level reasoning document. It does not explain what a reasoning document is or why it exists. A newcomer who arrives without that orientation will find the section-by-section guidance unanchored.

**Not a template.** The guided drafting prompt does not tell the newcomer what to write. It draws reasoning out through questions. A session that produces a correctly structured document without genuine reasoning has not succeeded; it has produced the failure the prompt exists to prevent.

**Not a one-session guarantee.** The first reasoning document produced with the guided drafting prompt will be imperfect. That is expected and correct. The livingness commitment means the document is a starting point, not a deliverable. The prompt cannot guarantee a complete or fully reasoned first document, only an honest one.

**Not a substitute for the traveling prompt.** The guided drafting prompt governs a specific session for a specific purpose. The traveling prompt governs collaborative posture across all sessions. Both are required. The guided drafting prompt operates within the posture the traveling prompt establishes; it does not replace it.

**Not designed for a newcomer who arrives without any problem at all.** The guided drafting prompt cannot generate the problem the reasoning document must address; that genuine starting point must come from the newcomer. But it does not need to be sharp before the session begins. The co-authorship in the session is precisely what sharpens it. A newcomer who arrives with a genuine but half-formed problem and reasons through it honestly will often produce a better problem statement at the end of The Problem section than they could have articulated before the session started. That sharpening is not a side effect: it is one of the primary values the guided drafting prompt delivers.

---

## The Open Questions

**[OQ-SMDP] Whether the Socratic facilitation mode holds under motivational pressure.**

A newcomer who stalls may push the LLM toward directive mode, asking directly for definitions, examples, or what to write. Whether the prompt can be designed to hold the Socratic mode under that pressure without losing the newcomer entirely is untested. The livingness commitment ([AS-LLNB]) is the primary mitigation, but whether it is sufficient to sustain engagement when the first section proves genuinely hard is an open question.

**[OQ-CPFD] Whether context pressure degrades Socratic mode before the session completes.**

A single prompt governing the full session may lose behavioral fidelity as the session lengthens, not because the LLM forgets the instructions, but because co-author posture drifts under accumulated context. Whether this degradation is significant enough to warrant per-section prompt recalibration, or whether the human's drift-correction practices from the human prompt are sufficient mitigation, requires trial. The first version assumes a single prompt is sufficient. This assumption should be tested explicitly in early use.

**[OQ-LTCT] The LLM contribution threshold in a first session.**

When should the LLM shift from drawing out the newcomer's reasoning through questions to contributing its own reasoning directly? In a standard RFM session the co-author role is fully active throughout. In a guided drafting session the threshold for direct contribution is higher: the risk of the LLM's reasoning displacing the newcomer's is real when the newcomer has not yet developed the practice of pushing back. Where exactly that threshold sits, how it varies by section and by newcomer state, and whether it can be specified in the prompt or must remain a live judgment call, requires trial.

---

## Hard Lessons

**[HL-LRRL] The section sequence is not strictly linear; the Landscape can require revising what came before it.**

Drafting The Problem and The Assumptions first, then conducting Landscape research, then returning to ask whether the research sharpens or adjusts the first two sections produced better documents than treating the sequence as a one-way pass. The Landscape can reveal that an assumption was imprecise or that the problem statement was narrower than the domain warrants. The guided drafting prompt must build this revision loop in explicitly, and the newcomer must be told why, not just instructed to do it.

**[HL-SRST] Socratic mode and the red team function operate on different objects: conflating them is the primary behavioral failure of the guided drafting session.**

Socratic mode governs who supplies the reasoning for sections: the newcomer must reason, not receive. The red team function governs whether claims are challenged when they outrun their evidence: it fires regardless of session phase, section, or facilitation mode. In practice, Socratic mode's emphasis on questioning over contributing reads as a general deference posture, and the red team function goes quiet. The failure is invisible because the session still looks productive: sections fill, reasoning develops, the newcomer stays engaged. What is missing is challenge. Claims stated with more confidence than the evidence supports pass unchallenged. The prompt must make the distinction explicit: the threshold for direct contribution is higher in a guided drafting session; the threshold for challenge is not.

---

*module_reasoning // [living]*
*the guided drafting prompt is the derivative*
*this document is the source*
*the reasoning comes first, the prompt follows*