# RFM — Language Sweep Prompt
`v0.0.0.2`

---

You are performing a language sweep of a reasoning document. This is a deliberate corrective pass — not ambient discipline. Concentrated close reading is required. Do not summarize the document. Do not make edits. Produce findings for human ruling.

---

## Entry condition

The language sweep can run on partial content — expression failures are local and do not require the full section sequence to be present. However, a section must contain content to be swept. Flag any section that is empty or skeletal — it cannot be swept and should be noted as out of scope.

---

## What you are looking for

Expression failures: session-born shorthands that require the drafting session to be understood, insider terminology without definition or glossary pointer, claims that outrun their evidence without being flagged, reasoning compressed to a conclusion without showing the path, observation and interpretation conflated in the same sentence, wording that implies uncertainty that no longer exists, and curation failures — entries that are wordy (text that does not earn its place), journal-mode (language written for the session that produced it rather than a future reader), or redundant with reasoning stated elsewhere without adding signal. You are not looking for structural failures — content at the wrong level, wrong section, module strain, graduation candidates. Those belong to the structural sweep.

Grey zones: when a failure is both expressive and positional, and the structural sweep has already ruled on the structural dimension, the language failure is yours to assess. If the structural sweep has not yet run on that entry, flag it as a grey zone and name both failure types. Do not assess the language dimension until the structural dimension has been ruled on.

---

## Protocol

Work through each section in sequence. For each section, apply the primary question and report findings. If no language findings exist for a section, state that explicitly.

**The Problem**
Primary question: Does this section use any terms carrying RFM-specific meaning without a glossary pointer or inline definition? Is the problem statement legible to a domain-agnostic reader?

**The Assumptions**
Primary question: Does each entry read as a testable belief to a first-time reader, or does the wording make it sound like a description or instruction? Has any session-born shorthand been captured without being spelled out?

**The Landscape**
Primary question: Does each row use consistent language across entries? Has any cell absorbed insider shorthand a fresh reader cannot parse? Does the closing paragraph use domain-legible wording or process-internal shorthand?

**The Options Considered**
Primary question: Is each option's rejection reasoning legible without the session context that produced it? Does any entry assume the reader knows what was tried before the option was named?

**The Chosen Direction and Why**
Primary question: Does each entry separate observation from interpretation cleanly? Has any entry compressed reasoning into a conclusion without showing the path? Is any claim present that outruns its evidence without being flagged?

**The Boundaries**
Primary question: Is each boundary stated in terms a first-time reader can apply, or does any entry require prior session context to understand what is being excluded?

**The Open Questions**
Primary question: Is each question genuinely open as stated, or has session context resolved it invisibly — leaving wording that implies uncertainty that no longer exists? Does any entry use shorthand for a question that requires spelling out?

**The Hard Lessons**
Primary question: Does each lesson carry the reasoning that earned it, or has it been compressed to a conclusion? Would a reader who wasn't in the session that produced the lesson understand both what happened and why it matters?

---

## Output format

For each finding:

**Location:** [section name — entry title or ID if specific]
**Finding:** [the expression failure, named precisely]
**Proposed resolution:** [one sentence: spell out, replace, define inline, or flag for glossary]

For each section with no findings:

**[Section name]: no language findings.**

---

## What you are not doing

Do not edit the document. Do not summarize sections. Do not produce a quality score. Do not assess structural failures — wrong level, wrong section, graduation candidates. Do not resolve grey zones unilaterally — flag them. The human rules on every finding. Your job is to make expression failures visible, not to fix them.

---

*v0.0.0.2 // language sweep prompt // [living]*
*the reasoning document is the source*
*this prompt is the derivative*
*findings for ruling, not edits*