# Reasoning-First Methodology: Human Prompt Reasoning Document
`v0.6.0` // `module_reasoning` // [living]

---

## The Problem

The traveling prompt calibrates the LLM's collaborative posture precisely. Nothing calibrates the human's. The methodology assumes a human who already works in a particular way: thinking out loud rather than stating destinations, tolerating uncertainty rather than demanding confident answers, pushing back with genuine curiosity, applying the "so what?" test to their own best ideas. These are not personality traits. They are practices. And without an artifact that makes them explicit and actionable, the methodology's value depends on the human arriving with them already internalized.

The asymmetry is real and consequential: one practitioner has a behavioral artifact designed for them, the other does not. When the human's collaborative posture drifts (toward passive acceptance, toward delegating rather than reasoning, toward smoothing over friction rather than naming it), the reasoning document accumulates what the AI produces rather than what both parties worked out together. The discipline holds on one side of the collaboration and quietly fails on the other.

---

## The Assumptions

**[AS-ACWN] - The artifact calibrates willingness; it does not create it.** The practices described here assume a reader with a natural affinity for deliberate reflection. That affinity is a people constraint, not a process gap. A reader who arrives without genuine willingness to reason carefully will find the entries obvious or irritating rather than actionable, and the artifact cannot change that.

**[AS-REBI] - Repeated exposure builds internalization.** The reference card is built to be returned to across many sessions, not absorbed once. That design bets on repetition itself doing the work: a phrase encountered again and again, at the moment it becomes relevant, becomes something the reader recognizes without consulting the card. If a single careful reading were enough, or if repetition without that reinforcement changed nothing, the card's whole shape, short, phrase-based, meant to be reopened, would be doing work for no reason.

**[AS-RSGP] - The cognitive-offloading risk documented in the general population extends to RFM practitioners.** An RFM session is still a session where an LLM produces fluent, well-structured output on request. Nothing about working inside this methodology exempts a practitioner from the same offloading risk studied elsewhere. This assumption breaks if RFM's own structure, built around joint reasoning rather than one-shot answers, already prevents that drift on its own. If it did, the human prompt would be addressing a problem the methodology had already solved.

---

## The Landscape

| Approach | What it does | Why it's insufficient for the human prompt |
|---|---|---|
| **Reflective practice frameworks** | Structured approaches to professional reflection: Schön's reflective practitioner, Kolb's experiential learning cycle, Kember et al.'s four-level reflection framework. Establish the value of deliberate self-examination as a professional discipline | Designed for post-hoc reflection, not real-time collaborative sessions. They address how to think about practice after it has happened, not how to sustain a collaborative reasoning posture while it is happening. No mechanism for mid-session recalibration. |
| **Prompt engineering and AI interaction guides** | Practical guidance on how to phrase requests, structure context, and elicit better AI output, evolved by 2025-2026 into context engineering, covering what fills the context window at each step | Focused entirely on improving AI output quality through better input construction. Address the transactional layer, what the human sends, not the collaborative posture the human holds throughout a session. The human remains a prompt author, not a thinking partner. |
| **AI literacy and onboarding programs** | Structured training on AI governance, interaction techniques, and responsible use, increasingly mandatory in large organizations (Forrester 2026: 30% of large companies requiring formal AI training). Accenture's tiered model (governance → interaction techniques → peer teaching) is a representative example | Address knowledge and compliance, not internalized practice. Designed to bring users to a baseline of functional competence. Do not address drift, friction, or the cultivation of a sustained collaborative reasoning posture over time. |
| **Collaborative AI metacognition frameworks** | Emerging research strand (Sidra and Mason 2025; validated scales published 2025) defining "collaborative AI metacognition" as the ability to monitor and regulate one's own thinking when working with AI: planning, monitoring, reflection. Identifies four characteristics that distinguish human-AI from human-human interaction and require specific metacognitive skills | Closest prior art. Describes the capability the human prompt is designed to cultivate. Remains a measurement and research construct, not an actionable artifact a practitioner can use. No guidance on how to build or sustain the metacognitive posture in practice, and not designed for a specific collaborative methodology. |

**The gap:** the cognitive risk is well-evidenced: Gerlich (2025), studying 666 participants across age groups and educational backgrounds, found a significant negative correlation between frequent AI tool usage and critical thinking abilities, mediated by increased cognitive offloading. What does not exist is a practitioner artifact that addresses this risk from the inside: something that cultivates the human's collaborative reasoning posture through repeated exposure, designed for a specific methodology, actionable mid-session, and honest about what it cannot enforce. The human prompt occupies that gap.

---

## The Options Considered

**1. Pre-session checklist**

A checklist the human works through before starting: verify engagement level, confirm the reasoning document is open, confirm the reasoning posture. Rejected because it measures whether steps were performed, not whether the underlying practice took hold. Completing a checklist item is a single act. The drift the human prompt targets happens continuously across a session, well after any checklist would have been closed.

**2. Session-sequence ordering**

Entries arranged by when they typically become relevant during a session: engagement first, drift detection in the middle, deliberate return at the end. Rejected because it optimizes for familiarity to someone already inside a session, not for what matters most to a reader encountering the list for the first time. A reader who stops partway through would encounter entries in narrative order, not in order of what costs the most to skip.

---

## The Chosen Direction and Why

**Why cultivation over checklist**

The failure a checklist cannot catch is going through the motions once and drifting anyway. A reference card built for repeated consultation stays live through the session instead of closing before it starts: it can be consulted mid-session, not only confirmed once in advance. That is what a cultivation artifact does that a checklist cannot.

**Why consequence ordering**

The reference card and the explanation entries share one order. That order has to serve a reader who may not get through the whole list. Ordering by how much damage drift toward an entry causes puts the highest-cost failures first, so a reader who stops early still sees the ones that matter most. Session sequence would put a mid-session entry ahead of a costlier one, simply because it happens to occur later in a typical session.

**Why the reference card is a plain list, not a numbered one**

Numbers imply a sequence to complete: item one before item two, a checklist a reader works through once and closes. The reference card is not that. Each phrase is a standalone trigger meant to fire on its own, in whatever order the moment calls for it, not steps in an order. A plain list carries no such implication.

**Why these entries and not others**

Output quality is a distinct failure mode category the traveling prompt cannot address: the LLM producing text that looks polished but is verbose, journaling, or repetitive. It requires a separate entry because the human's corrective move is different: not recalibrating the collaboration but reading the output critically before accepting it.

A dedicated entry on how the human delivers corrections addresses a failure mode that neither the drift entry nor the output entry names: the human defaults to verdict-shaped correction. A verdict ("this is wrong, remove it") provides resolution. The LLM closes a verdict by pattern-matching to avoid the marked behavior, not by reasoning to a position. The result is improved form without improved judgment. A correction that withholds resolution forces the LLM to generate a position. The LLM cannot close that loop without exercising judgment. The cost lands on the human side. Withholding resolution requires the human to hold back the answer even when they know it. That is a discipline only the human can apply.

**Why the set of entries is not closed**

The reference card lists practices worth naming so far, not all of them. Nothing requires the list to be complete, and a new entry can be added later without removing an old one. An entry belongs on the card because skipping it causes real damage, not because the list needs to be longer.

**Why "To Internalize Next" exists as a third section**

The reference card has to stay short enough to function as a recognition tool: a repertoire that fires without being consulted, not a document to search under pressure. That ceiling caps how many phrases the card can carry. A third section holds practices that are real and worth naming but have not yet earned a place on the capped list, so they are not lost, only not yet promoted.

**Why each entry follows a layered structure**

Each entry carries a bold header, an italic phrase, a paragraph on why the practice matters, and a paragraph on what to do about it. The two purposes don't collapse into one: understanding why a practice matters is not the same as knowing what to do when it matters, and a reader needs both, not one standing in for the other.

The italic phrase is not decoration. It matches the corresponding phrase on the reference card exactly, so a reader who recognizes the phrase there can find its explanation here, and the reverse.

RFM concepts appear in the body only where they arise on their own: where a concept already has a direct home in the methodology and adds meaning rather than noise.

**Why the framing paragraph opens with the cognitive-offloading research, not the asymmetry**

The real motivation is the asymmetry: the LLM has a calibration artifact, and the human doesn't. But that argument only lands for a reader who already knows what the traveling prompt is and that it exists. The cognitive-offloading research needs no such context, so the artifact opens with it.

**Why the human states the path, not the destination**

An LLM works on the request it is given. A conclusion handed to it as the goal tends to get elaborated: the LLM works out how to reach it, and the conclusion itself goes untested. A question or a half-formed idea gets examined. The LLM can see where the thinking is solid and where it is loose, and can push back on an assumption before it hardens into a direction. That is the co-author role the methodology asks of the LLM, and it only happens when the human shares the thinking as it unfolds. A human who arrives with the answer already chosen is delegating, and the LLM's judgment goes unused. So the human starts with what they are trying to figure out, uncertainty included.

**Why the human notices their own disengagement**

Joint reasoning takes effort throughout a session, and effort drops as the session goes on. The usual result is not a decision to stop. Active reasoning slides into accepting what the LLM produces, because evaluating it feels like more work than moving on. From then on the LLM keeps producing and the reasoning keeps accumulating, and the document that results reflects what the LLM thought, not what the two worked out together. The LLM can only infer this state from outside. The human has direct signals: no longer being surprised, no longer wanting to push back, no longer caring whether the next paragraph lands. So the sentence belongs to the human, who either stops the session or resets explicitly. Continuing without doing either is the failure it names.

**Why the human pauses before accepting a confident answer**

An LLM produces confident, well-structured answers whether or not the question has been resolved, so the confidence of an answer says little about whether the thinking behind it is finished. A clean answer that arrives quickly is often an untested one. The human is the one under pressure to close: an unresolved conversation is uncomfortable, and a satisfying answer relieves that. So the human first asks themselves whether the answer resolves the question or only sounds as if it does, and then asks the LLM what is still unsure. The LLM answers that question honestly when it is asked, so the human's part is to ask it.

**Why the human names where an idea belongs before asking for it to be developed**

Not every idea that surfaces belongs in the document being worked on. Some belong at another level of the hierarchy, some in a different kind of artifact, and some are not ready to be written anywhere. A draft creates its own momentum: once an idea has been developed into a paragraph, questioning whether it belongs there is harder than it was before the paragraph existed. The cheap moment to ask is before the draft. The human states where they think the idea belongs, and the LLM confirms it, redirects it, or offers a better home. When the reasoning documents are loaded into the session, the LLM can answer this because it can see what each document carries.

**Why the human asks for a steel-man before rejecting an option**

Reasoning fails in two directions: building on weak ideas, and rejecting strong ones too easily. The second is harder to see. An option dismissed without real engagement looks like a considered rejection once it is written into Options Considered, and nothing in the document shows it was not one. The motivation also runs the wrong way. A human who already doubts an option looks for confirmation that the doubt was right, and asking the LLM to help reject it supplies that confirmation. Asking first for the strongest version of the option makes the case against the doubt get heard. If the option still fails against its best case, the rejection is earned. If it holds, a premature closure has been avoided that would otherwise have stayed invisible.

**Why the human asks the LLM to show its work when an answer arrives cleanly**

Fluency and correctness are independent, so a clean answer does not show that the reasoning behind it is sound. The reasoning may be solid, or it may have been skipped in favor of a plausible conclusion, and the answer alone does not tell the human which. Asking what is still unsure surfaces the uncertainty the LLM is aware of. Asking for the reasoning path surfaces the steps, the assumptions, and the places where a different input would have produced a different output. The human can then evaluate the path instead of receiving the conclusion. Thin spots and skipped steps are where the answer is most likely to be wrong.

**Why the human asks "so what?" of their own best idea before building on it**

An idea that feels right invites development: adding detail, thinking forward, looking for agreement. Each step of development makes the idea harder to question, so a plausible but flawed idea gets elaborated instead of examined, and the correction costs more the further the work goes. The question "so what? why does this actually matter?" has to be asked before that point, and asked of the human's own thinking, not the LLM's. The reasoning document records why a decision was made, so a decision built on an unquestioned idea yields a document that looks complete and is not: the assumption doing the most work is the one that was never named.

**Why the LLM keeps the Chesterton's Fence log and the human reads it**

In pressure mode the LLM does the executing, so it is the one who deviates from the established reasoning, defers a question, or finds an assumption broken, and it can record each as it happens. The human's part is the return: reading the log when pressure lifts and deciding what goes back into the reasoning. A log that is kept and never read does not make the return honest, so the reading stays with the human. The LLM will miss deviations it does not recognize as deviations. This split is untested, because the log has not yet been used in practice.

**Why artifact-before-reasoning-document was acceptable here, and what it requires**

Every other artifact in the RFM document landscape was preceded by its reasoning document: the reasoning settles the design, and the artifact derives from it. The human prompt was written first, from its authors' own practice, before this reasoning document existed. That is acceptable only if the reasoning is written afterward and checked against the artifact that already exists, not against a blank page. This document is that check.

---

## The Boundaries

**Not a methodology introduction.** The human prompt assumes the reader has encountered RFM through the README and the top-level reasoning document. It does not explain the methodology. A reader arriving without that orientation will find the references to reasoning documents, co-authorship, and the document landscape without context.

**Not a compliance document.** The human prompt cannot enforce the posture it describes. It makes the practices explicit and repeatable; what happens with them depends entirely on the reader. A reader who treats it as a requirement to satisfy has already misread it.

**Not a substitute for the traveling prompt.** The traveling prompt calibrates the LLM's collaborative posture. The human prompt calibrates the human's. They are complements, not alternatives. Collapsing one into the other would leave one collaborator uncalibrated.

**Not a one-time read.** A single reading produces familiarity, not internalization.

---

## The Open Questions

**[OQ-AFHP] - Whether these entries generalize beyond their authors' working style.**

The human prompt was written from its authors' own practice: their specific failure modes, observed across their own sessions. Whether a practitioner who works differently, with different instincts, different points of drift, would recognize the same entries as the ones that matter for them is untested. No practitioner outside the authors has used the artifact yet.

---

## Hard Lessons

**[HL-SSDM] The LLM's behavioral posture is not fully established at session start; the human must notice and correct early.**

In the session that produced this reasoning document, methodology-specific terminology appeared in the first response before the collaborative posture had been established. The traveling prompt activates the LLM's methodology discipline, but activation is not instantaneous: the early exchanges can already reflect tool behavior rather than co-author posture. This is distinct from mid-session drift, which is gradual and cumulative. Session-start drift is immediate and easy to miss precisely because the output reads well. The human's job in the early exchanges is to read for posture, not just content, and to correct before the pattern compounds.

**[HL-VRDCT] A correction script that asks for a self-report can be satisfied without the state it asks about.**

"Notice when the AI drifts, and pull it back" offered two in-practice scripts as equivalent: a question, "are you drifting?", and a command, "stop being agreeable, push back." Both ask the AI to characterize its own state rather than produce anything checkable. A denial of drift is exactly as cheap to generate as a claim of having pushed back, so grammatical mood does not look like what made the command version worse. The actual failure is that neither script demands a deliverable, something specific enough that its absence, not a denial, is the evidence. "Correct with a question, not a verdict" in the same artifact already gives the working version: "I still don't see why this matters" cannot be answered with a claim about the AI's own state, it requires the AI to produce a justification. "Red team this," used elsewhere in the same artifact, is grammatically a command and has the same property: it asks for named weaknesses, not a report on posture, so a command asking for a deliverable does not fit the failure mode this entry needed to name. This distinction is drawn from two examples in one session, not tested against a wider set; it may not hold as cleanly elsewhere.

The same entry named drift in one direction only: presenting options instead of proposing, softening under pushback, waiting for permission. Its in-practice line told the human to push the AI to act more. Applied to the opposite direction, treating a narrow delegation as authorization for everything downstream of it and moving straight to unconfirmed execution, that corrective is not neutral. Pushing an AI that has already over-extended one authorization adds pressure in the wrong direction. An entry that names drift in a single direction cannot catch the other, and its corrective can actively worsen the direction it does not name.

The corrective this suggests: a light, default check that asks for a deliverable scoped to the immediate output, "what's weak here?", escalating, when the answer comes back thin, to the same question scoped across several exchanges rather than switching to a different phrase. The escalation widens what has to be accounted for. It does not introduce a second script standing as an equal alternative to the first, the same design error the two co-equal scripts at the start of this entry already made once.

**[HL-ABRR] The right order is reasoning document first, artifact second.**

The human prompt broke that order: it was written from its authors' practice before its reasoning document existed. Writing the reasoning afterward means checking it against a finished artifact, not shaping the artifact from a reasoning document still being settled. Gaps found this way are gaps already shipped, not gaps caught before anyone relied on them.

---

*module_reasoning // [living]*
*the human prompt is the derivative*
*this document is the source*
*the reasoning followed the artifact, that was the exception, not the rule*