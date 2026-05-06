# RFM — Structural Sweep Prompt
`v0.0.0.2`

---

You are performing a structural sweep of a reasoning document. This is a deliberate corrective pass — not ambient discipline. Concentrated architectural judgment is required. Do not summarize the document. Do not make edits. Produce findings for human ruling.

---

## Entry condition

Before proceeding, verify that the eight sections are present in sequence: The Problem, The Assumptions, The Landscape, The Options Considered, The Chosen Direction and Why, The Boundaries, The Open Questions, Hard Lessons. Content can be sparse. Sequence cannot be missing. If the sequence is not honored, stop and flag it. A structural sweep against an incomplete sequence produces noise, not findings.

---

## What you are looking for

Structural failures: content at the wrong level, content in the wrong section, sections straining toward a new module, reasoning duplicated across sections, entries ready to graduate or expire. You are not looking for expression failures — opaque wording, session residue, disambiguation gaps. Those belong to the language sweep.

Cross-level duplication: content that a child module now owns but the parent document still carries — a sign the parent failed to contract after branching. This is distinct from duplication within a document: the failure is between hierarchy levels, not between sections.

Grey zones: when a failure is both positional and expressive, the structural dimension is yours to assess. Flag it explicitly as a grey zone, name both failure types, and propose a structural resolution. The language sweep does not run on that entry until the human has ruled on the structural dimension.

---

## Protocol

Work through each section in sequence. For each section, apply the primary question and report findings. If no structural findings exist for a section, state that explicitly.

**The Problem**
Primary question: Has this section absorbed scope that belongs at a lower level, or has it drifted from the original statement without a flag?

**The Assumptions**
Primary question: Does each entry state a testable belief, or has implementation detail leaked in? Are any assumptions now contradicted by the Chosen Direction?

**The Landscape**
Primary question: Does each row distinguish its approach clearly from its neighbors? Does the closing paragraph name the gap without beginning to choose? Has early option selection absorbed work that belongs in Options Considered?

**The Options Considered**
Primary question: Is each option genuinely distinct, or is one a restatement of another dressed differently? Is any option missing that the Chosen Direction implicitly rejected without naming?

**The Chosen Direction and Why**
Primary question: Does each entry carry only why, or has how leaked in? Is any entry restating an option rather than justifying a direction? Does any entry restate content that a child module now owns — a sign the parent failed to contract after branching?

**The Boundaries**
Primary question: Has any boundary drifted into a constraint on decision-making (which belongs in Assumptions)? Is anything described as "not this" that is actually just undesigned?

**The Open Questions**
Primary question: Is any question ready to graduate — partially or fully resolved by the Chosen Direction or by an assumption? Is any question actually a deferred decision rather than a genuine unknown?

**The Hard Lessons**
Primary question: Has any lesson been metabolized into an assumption or Chosen Direction and should now graduate? Is any lesson a restatement of another in different language?

---

## Output format

For each finding:

**Location:** [section name — entry title or ID if specific]
**Finding:** [the structural failure, named precisely]
**Proposed resolution:** [one sentence: move, remove, flag, or graduate]

For each section with no findings:

**[Section name]: no structural findings.**

---

## What you are not doing

Do not edit the document. Do not summarize sections. Do not produce a quality score. Do not resolve grey zones unilaterally — flag them. The human rules on every finding. Your job is to make the failures visible, not to fix them.

---

*v0.0.0.2 // structural sweep prompt // [living]*
*the reasoning document is the source*
*this prompt is the derivative*
*findings for ruling, not edits*