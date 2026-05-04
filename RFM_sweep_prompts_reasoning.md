# Reasoning-First Methodology — Sweep Prompts Reasoning Document
`v0.0.0.1` // `module_reasoning` // [living]

---

## The Problem

The sweep prompts are the corrective arm of the prompt system. Their existence and purpose are established in `RFM_prompts_reasoning.md`. What that document does not carry is the artifact-level design: how each sweep is structured, what it targets section by section, how it signals completion, and how the two sweeps differ in cognitive mode while sharing the same output discipline. Without a reasoning document at this level, the sweep prompts have no source — they are derivatives with nowhere to point when their design is questioned or needs to change.

---

## The Assumptions

1. **The two sweeps require different cognitive modes and must not run simultaneously.** The structural sweep requires architectural judgment — is this content at the right level, is this section straining, is this open question ready to graduate? The language sweep requires close reading — does this term carry its meaning without session context, has session residue accumulated? Each mode requires concentration the other's presence would dilute. Running both in one pass produces shallow work in both directions.

2. **The structural sweep's precondition is section sequence, not content presence.** A coherent draft means the eight sections have been populated in order — Problem before Assumptions, Landscape before Options, Options before Chosen Direction. Content can be sparse. What cannot be missing is the sequence. A structural sweep invoked before the sequence is honored has no architecture to review against — it produces noise, not findings.

---

## The Landscape

| Approach | What it does | Why it's insufficient for the sweep prompts |
|---|---|---|
| **LLM-as-judge with rubrics** | A second LLM evaluates output against structured criteria — rubric-based judging (Prometheus, G-Eval, RRD, 2025–2026) improves reliability over holistic judgment | Rubrics are static and output-focused. Cannot detect hierarchy failures, session residue, or ownership drift in a living document. Criteria do not distinguish structural from language failures. |
| **Multi-agent critique** | Multiple LLM agents critique each other's outputs, simulating peer review | Designed for discrete outputs, not living documents with history and derivative chains. Research shows LLMs systematically underperform at identifying weaknesses and raising substantive questions — the core sweep function. |
| **Structured critique prompts** | Chain-of-thought evaluation steps generated from task introduction and explicit criteria (G-Eval pattern) | Closest prior art. Criteria are task-specific and static — no section-sequence awareness, no hierarchy ownership check, no structural/language mode distinction. |

**The gap:** no existing approach applies two mode-distinct corrective passes — one architectural, one linguistic — to a living reasoning document hierarchy, with findings produced for human ruling rather than automated scoring. The sweep prompts occupy this gap specifically.

---

## The Options Considered

**1. Holistic review vs. section-by-section protocol**

Ask the LLM to identify failures across the whole document at once vs. work through section by section in sequence. Holistic review is faster but misses gradual drift — failures that only become visible under sequential attention. Section-by-section protocol chosen because the failure modes the sweep targets are cumulative and positional: session residue accumulates across sections, hierarchy drift is visible only when sections are compared against each other in sequence.

**2. Fixed criteria vs. document-adaptive criteria**

Apply the same checklist to every document vs. allow the sweep to adapt its attention to the specific document's type, age, and state. Fixed criteria are auditable and consistent but miss document-specific strain signals. Adaptive criteria require the LLM to reason about what matters here — which is the correct cognitive mode for a living document. Document-adaptive criteria chosen, with the section-by-section protocol as the structural anchor that prevents adaptation from becoming drift.

**3. Scoring output vs. findings-for-ruling output**

Produce a quality score vs. produce named findings with proposed resolutions for human ruling. Scoring is automated and scalable — the dominant pattern in LLM-as-judge practice. Rejected because the sweep targets reasoning document integrity, not output quality. A score compresses the finding into a number that cannot be acted on. Named findings with proposed resolutions keep the human as decision-maker and produce output that can be directly executed or rejected. Findings-for-ruling is the only output format consistent with the co-author ceiling.

---

## The Chosen Direction and Why

**Why section-by-section protocol with document-adaptive criteria:**

The section sequence is fixed — it is the structural anchor. The criteria adapt to the document's state — early development has different failure modes than a mature curated document. Fixed sequence prevents adaptation from becoming drift. Adaptive criteria prevent the protocol from becoming a checklist that misses what actually matters here.

**Why the two sweeps have different entry conditions:**

The structural sweep requires section sequence to be honored — it reviews architecture, and architecture requires something to be built. The language sweep can run on partial content — expression failures are local. Entry conditions differ by design, not convention.

**Why the structural sweep owns hierarchy and the language sweep owns expression:**

Hierarchy failures require holding the full document structure in view and reasoning across it. Expression failures require close reading of individual sentences. Assigning each to its own sweep ensures neither cognitive mode is diluted by the other's presence.

---

## The Boundaries

**Not a quality gate that can be passed.** The sweep produces findings, not a score. Absence of findings signals either a well-curated document or a shallow sweep — the human cannot distinguish between the two without judging the sweep's depth independently. There is no clean sweep. The output is always findings for ruling, never a certification.

**Not a substitute for the traveling prompt.** The sweep corrects failures that slipped through ambient discipline. It cannot compensate for absent discipline. A document produced without the traveling prompt's prevention will accumulate failures faster than the sweep can reliably catch them.

---

## The Open Questions

**1. The section-by-section protocol.**

What exactly does each sweep do at each of the eight sections? The structural sweep and language sweep will have different attention at each section — what the structural sweep looks for in Assumptions differs from what it looks for in Hard Lessons. The per-section protocol for each sweep is undesigned. This is the primary design work remaining before either prompt can be built.

**2. The quality gate.**

How does the human know a sweep was deep rather than superficial? Absence of findings is ambiguous. A sweep that produces no findings against a well-curated document looks identical to a sweep that produced no findings because it didn't concentrate. The quality gate — the signal that distinguishes a complete sweep from a shallow one — is undesigned.

**3. Grey zone ownership.**

Some failures sit ambiguously between structural and language classes — a term that is both session residue and in the wrong section, an assumption that is both an implementation detail and opaquely worded. Which sweep owns the grey zone, and how is that decision made without one sweep absorbing the other's job? Unresolved.

---

## Hard Lessons

**1. A sweep prompt that is too ambient fails silently.**

The sweep fails not by producing wrong findings but by producing shallow ones — the LLM runs through sections without concentrating, flags nothing, and the document appears clean. Ambient character is the traveling prompt's strength and the sweep prompt's primary failure mode. The sweep must feel like deliberate critique, not background discipline.

**2. Repetition across sections is invisible from inside the session that produced it.**

The same argument restated in different styles across Options Considered and Chosen Direction looks like thoroughness from inside the drafting session. It is only visible under the concentrated attention of a structural sweep. This is a primary target for the structural sweep — not duplication of content, but duplication of reasoning dressed as distinct entries.

---

*v0.0.0.1 // module_reasoning // [living]*
*the sweep prompts are the corrective arm*
*findings for ruling, not edits*
*the reasoning comes first — the prompts follow*