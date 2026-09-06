# Reasoning-First Methodology: Sweep Prompts Operational Document
`v0.5.0` // `operational` // [living]

---

## What this module produces

This module produces sweep prompt artifacts, one per mode.

**The structural sweep prompt** (`RFM_sweep_prompt_structural.md`) activates a concentrated architectural review pass over a reasoning document. Findings for human ruling, not edits. Invoked deliberately, not ambient.

**The language sweep prompt** (`RFM_sweep_prompt_language.md`) activates a concentrated language review pass over a reasoning document. Findings for human ruling, not edits. Invoked deliberately, not ambient.

**The relational sweep prompt** (`RFM_sweep_prompt_relational.md`) activates a boundary check between a reasoning document and its operational derivative. Findings for human ruling, not edits. Invoked deliberately, not ambient.

No two sweep prompts are invoked simultaneously. Each requires a cognitive mode the other's presence would dilute.

---

## Source documents

Load this document's sources before deriving any sweep prompt. They are its branch of the hierarchy in `RFM_map.md`, read upward.

---

## Language catalog

The failure types the language sweep looks for are in `RFM_operational.md` under Failure Taxonomy. This catalog carries the per-section primary questions derived from them, and is the source specification for the language sweep prompt's "What you are looking for" section. Any change to a question begins here. Any change to a failure type begins in `RFM_operational.md`.

The language sweep assesses the language failure types only. The structural failure types belong to the structural sweep.

**Per-section primary questions**

*The Problem:* Does this section use any terms carrying project-specific meaning without a glossary pointer or inline definition? Is the problem statement legible to a domain-agnostic reader?

*The Assumptions:* Does each entry read as a testable belief to a first-time reader, or does the wording make it sound like a description or instruction? Has any session-born shorthand been captured without being spelled out?

*The Landscape:* Does each row use consistent language across entries? Has any cell absorbed insider shorthand a fresh reader cannot parse? Does the closing paragraph use domain-legible wording or process-internal shorthand?

*The Options Considered:* Is each option's rejection reasoning legible without the session context that produced it? Does any entry assume the reader knows what was tried before the option was named?

*The Chosen Direction and Why:* Does each entry separate observation from interpretation cleanly? Has any entry compressed reasoning into a conclusion without showing the path? Is any claim present that outruns its evidence without being flagged?

*The Boundaries:* Is each boundary stated in terms a first-time reader can apply, or does any entry require prior session context to understand what is being excluded?

*The Open Questions:* Is each question genuinely open as stated, or has session context resolved it invisibly, leaving wording that implies uncertainty that no longer exists? Does any entry use shorthand for a question that requires spelling out?

*The Hard Lessons:* Does each lesson carry the reasoning that earned it, or has it been compressed to a conclusion? Would a reader who was not in the session that produced the lesson understand both what happened and why it matters?

---

## Grey zone rule

When a failure is both positional and about wording, the positional dimension must be ruled on before the language dimension is assessed. The structural sweep flags it as a grey zone, names both failure types, and proposes a structural resolution. The language sweep does not assess that entry until the human has ruled.

---

## Structural catalog

The failure types the structural sweep looks for are in `RFM_operational.md` under Failure Taxonomy. This catalog carries the per-section primary questions derived from them, and is the source specification for the structural sweep prompt's "What you are looking for" and "Protocol" sections. Any change to a question begins here. Any change to a failure type begins in `RFM_operational.md`.

The structural sweep assesses the structural and lifespan failure types. The language failure types belong to the language sweep.

**Per-section primary questions**

*The Problem:* Has this section absorbed scope that belongs at a lower level, or has it drifted from the original statement without a flag?

*The Assumptions:* Does each entry state a testable belief, or has implementation detail leaked in? Are any assumptions now contradicted by the Chosen Direction?

*The Landscape:* Does each row distinguish its approach clearly from its neighbors? Does the closing paragraph name the gap without beginning to choose? Has early option selection absorbed work that belongs in Options Considered?

*The Options Considered:* Is each option genuinely distinct, or is one a restatement of another dressed differently? Does each entry show evidence of having been actively considered, rather than invented to round out the section? Does the rejection name a specific failure mode, or only a preference? Does any entry restate the Chosen Direction's committed path instead of a discarded alternative? Is any option missing that was pursued as a competing way to resolve the Problem and dropped without record? A supporting commitment inside the Chosen Direction is not evidence of one.

*The Chosen Direction and Why:* Does each entry carry only why, or has how leaked in? Is any entry restating an option rather than justifying a direction? Does any entry restate content that a child module now owns, a sign the parent failed to contract after branching?

*The Boundaries:* Has any boundary drifted into a constraint on decision-making (which belongs in Assumptions)? Is anything described as "not this" that is actually just undesigned?

*The Open Questions:* Is any question ready to graduate, partially or fully resolved by the Chosen Direction or by an assumption? Is any question actually a deferred decision rather than a genuine unknown? Does the question have a plausible condition under which it could be resolved, or is it open-ended with no path to an answer? Would resolving it materially change the reasoning or the system, or is it decorative?

*The Hard Lessons:* Has any lesson been metabolized into an assumption or Chosen Direction and should now graduate? Is any lesson a restatement of another in different language?

**Cross-section question**

*Lifespan:* Does any entry state a condition that work already planned will satisfy? Ask it in every section alongside that section's primary question. Lifespan failures are not specific to a section, so no per-section wording is derived for them.

---

## Relational sweep specification

This specification is the source for the relational sweep prompt's entry conditions, finding criteria, and output format. Any change to any of these begins here.

**Entry conditions**

The following must be met before the boundary check begins.

*Both documents present.* The sweep requires the reasoning document and its operational derivative simultaneously. If either is absent, stop and flag it.

**Finding criteria**

*Forward direction.* An announced need is a finding only when its absence would leave an LLM deriving the current artifact without a necessary behavioral decision, constraint, or interface specification. Do not report the absence of a restatement of reasoning, an acknowledgement of future uncertainty, or a textual counterpart that adds no derivation guidance.

*Reverse direction.* A specification is grounded when it traces to any commitment in the reasoning document, including a chosen direction or design principle. The absence of a one-to-one announced need is not a finding when broader grounding exists. A finding requires the absence of any grounding at any level.

*Pre-filter gate.* Before surfacing a finding in either direction, confirm that the proposed addition or change would alter current derivation behavior. If it would not, do not report it.

**Output format**

Each finding uses two location fields, one per document. Either field may be blank when the finding is one-sided.

*Reasoning document:* [section name, entry or claim if specific; blank if the finding originates in the operational document]
*Operational document:* [section name, entry if specific; blank if the finding originates in the reasoning document]
*Finding:* [the boundary failure, named precisely: announced need with no coverage, or specification with no grounding in the reasoning document]
*Proposed resolution:* [one sentence]

When a section has no findings: **[Section name]: no boundary findings.**

---

## Sweep session invocation

Load the sweep prompt as the system prompt for a fresh conversation. Provide the document under sweep in the first human turn. Do not include other documents unless the sweep type requires them. The structural sweep and language sweep read a single document; the relational sweep requires both the reasoning document and its operational derivative.

Do not invoke a sweep inside a co-authorship session. The traveling prompt and a sweep prompt require incompatible postures. A sweep run inside a co-authorship session is not a sweep. It is the traveling prompt applied to one document, which is what the traveling prompt already does. The separation is the point.

Run one sweep per session. Running two simultaneously dilutes the cognitive mode each requires.

---

## Coverage check: after derivation

Compare against the previous version of the sweep prompt. The derivation is accepted if it is structurally better or equivalent and loses no load-bearing behavioral instructions. If the previous version carried something the derivation missed, assess whether it was present in the source reasoning documents. If yes: the derivation missed it, add it. If no: the previous version carried reasoning its source did not hold; that is a source document gap requiring a reasoning document addition before the next derivation cycle.

Do not loop the derivation. One pass, one coverage check, one reconciliation.

---

## Version discipline

The version number is assigned by the human at acceptance. A clean re-derivation increments the minor digit. A patch-level fix increments the patch digit. The header of each sweep prompt file is the single source of version truth for that artifact.

---

*operational // [living]*
*carries what; the reasoning documents carry why*
