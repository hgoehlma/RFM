# Reasoning-First Methodology: Human Prompt Reasoning Document
`v0.3.1` // `module_reasoning` // [living]

---

## The Problem

The traveling prompt calibrates the LLM's collaborative posture precisely. Nothing calibrates the human's. The methodology assumes a human who already works in a particular way: thinking out loud rather than stating destinations, tolerating uncertainty rather than demanding confident answers, pushing back with genuine curiosity, applying the "so what?" test to their own best ideas. These are not personality traits. They are practices. And without an artifact that makes them explicit and actionable, the methodology's value depends on the human arriving with them already internalized.

The asymmetry is real and consequential: one practitioner has a behavioral artifact designed for them, the other does not. When the human's collaborative posture drifts (toward passive acceptance, toward delegating rather than reasoning, toward smoothing over friction rather than naming it), the reasoning document accumulates what the AI produces rather than what both parties worked out together. The discipline holds on one side of the collaboration and quietly fails on the other.

---

## The Assumptions

**[AS-ACWN] - The artifact calibrates willingness; it does not create it.** The practices described here assume a reader with a natural affinity for deliberate reflection. That affinity is a people constraint, not a process gap. A reader who arrives without genuine willingness to reason carefully will find the entries obvious or irritating rather than actionable, and the artifact cannot change that.

---

## The Landscape

**The gap:** the cognitive risk is well-evidenced: Gerlich (2025), studying 666 participants across age groups and educational backgrounds, found a significant negative correlation between frequent AI tool usage and critical thinking abilities, mediated by increased cognitive offloading. What does not exist is a practitioner artifact that addresses this risk from the inside: something that cultivates the human's collaborative reasoning posture through repeated exposure, designed for a specific methodology, actionable mid-session, and honest about what it cannot enforce. The human prompt occupies that gap.

---

## The Options Considered

*No options considered at this time.*

---

## The Chosen Direction and Why

**Why these entries and not others**

Output quality is a distinct failure mode category the traveling prompt cannot address: the LLM producing text that looks polished but is verbose, journaling, or repetitive. It requires a separate entry because the human's corrective move is different: not recalibrating the collaboration but reading the output critically before accepting it.

A dedicated entry on how the human delivers corrections addresses a failure mode that neither the drift entry nor the output entry names: the human defaults to verdict-shaped correction. A verdict ("this is wrong, remove it") provides resolution. The LLM closes a verdict by pattern-matching to avoid the marked behavior, not by reasoning to a position. The result is improved form without improved judgment. A correction that withholds resolution forces the LLM to generate a position. The LLM cannot close that loop without exercising judgment. The cost lands on the human side. Withholding resolution requires the human to hold back the answer even when they know it. That is a discipline only the human can apply.

[NO REASONING: "State the path, not the destination; bring open questions to the AI rather than conclusions to execute."]

[NO REASONING: "Notice your own disengagement and either stop the session or explicitly reset."]

[NO REASONING: "Pause before accepting a confident answer; ask what's still unsure."]

[NO REASONING: "Name where you think an idea belongs before asking the AI to develop it."]

[NO REASONING: "Ask the AI to steel-man an option before rejecting it, rather than asking it to help reject it."]

[NO REASONING: "Ask the AI to show its work when an answer arrives too cleanly, rather than accepting fluency as evidence of soundness."]

[NO REASONING: "Apply the so-what test to your own best idea before building on it."]

[NO REASONING: "Schedule deliberate return to a document without a trigger, not only when something breaks."]

[NO REASONING: "Keep a Chesterton's Fence log during pressure mode: deviations, deferrals, broken assumptions."]

---

## The Boundaries

**Not a methodology introduction.** The human prompt assumes the reader has encountered RFM through the README and the top-level reasoning document. It does not explain the methodology. A reader arriving without that orientation will find the references to reasoning documents, co-authorship, and the document landscape without context.

**Not a compliance document.** The human prompt cannot enforce the posture it describes. It makes the practices explicit and repeatable; what happens with them depends entirely on the reader. A reader who treats it as a requirement to satisfy has already misread it.

**Not a substitute for the traveling prompt.** The traveling prompt calibrates the LLM's collaborative posture. The human prompt calibrates the human's. They are complements, not alternatives. Collapsing one into the other would leave one collaborator uncalibrated.

**Not a one-time read.** A single reading produces familiarity, not internalization.

---

## The Open Questions

*No open questions at this time.*

---

## Hard Lessons

**[HL-SSDM] The LLM's behavioral posture is not fully established at session start; the human must notice and correct early.**

In the session that produced this reasoning document, methodology-specific terminology appeared in the first response before the collaborative posture had been established. The traveling prompt activates the LLM's methodology discipline, but activation is not instantaneous: the early exchanges can already reflect tool behavior rather than co-author posture. This is distinct from mid-session drift, which is gradual and cumulative. Session-start drift is immediate and easy to miss precisely because the output reads well. The human's job in the early exchanges is to read for posture, not just content, and to correct before the pattern compounds.

**[HL-VRDCT] A correction script that asks for a self-report can be satisfied without the state it asks about.**

"Notice when the AI drifts, and pull it back" offered two in-practice scripts as equivalent: a question, "are you drifting?", and a command, "stop being agreeable, push back." Both ask the AI to characterize its own state rather than produce anything checkable. A denial of drift is exactly as cheap to generate as a claim of having pushed back, so grammatical mood does not look like what made the command version worse. The actual failure is that neither script demands a deliverable, something specific enough that its absence, not a denial, is the evidence. "Correct with a question, not a verdict" in the same artifact already gives the working version: "I still don't see why this matters" cannot be answered with a claim about the AI's own state, it requires the AI to produce a justification. "Red team this," used elsewhere in the same artifact, is grammatically a command and has the same property: it asks for named weaknesses, not a report on posture, so a command asking for a deliverable does not fit the failure mode this entry needed to name. This distinction is drawn from two examples in one session, not tested against a wider set; it may not hold as cleanly elsewhere.

The same entry named drift in one direction only: presenting options instead of proposing, softening under pushback, waiting for permission. Its in-practice line told the human to push the AI to act more. Applied to the opposite direction, treating a narrow delegation as authorization for everything downstream of it and moving straight to unconfirmed execution, that corrective is not neutral. Pushing an AI that has already over-extended one authorization adds pressure in the wrong direction. An entry that names drift in a single direction cannot catch the other, and its corrective can actively worsen the direction it does not name.

The corrective this suggests: a light, default check that asks for a deliverable scoped to the immediate output, "what's weak here?", escalating, when the answer comes back thin, to the same question scoped across several exchanges rather than switching to a different phrase. The escalation widens what has to be accounted for. It does not introduce a second script standing as an equal alternative to the first, the same design error the two co-equal scripts at the start of this entry already made once.

---

*module_reasoning // [living]*
*the human prompt is the derivative*
*this document is the source*
*the reasoning followed the artifact, that was the exception, not the rule*