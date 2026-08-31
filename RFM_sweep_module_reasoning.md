# Reasoning-First Methodology: Sweep Prompts Reasoning Document
`v0.2.3` // `module_reasoning` // [living]

---

## The Problem

The sweep prompts are the corrective arm of the prompt system. Their existence and purpose are established in `RFM_prompts_reasoning.md`. What that document does not carry is the artifact-level design: how each sweep is structured, what it targets section by section, how it signals completion, and how the sweeps differ in cognitive mode while sharing the same output discipline. Without a reasoning document at this level, the sweep prompts have no source: they are derivatives with nowhere to point when their design is questioned or needs to change.

---

## The Assumptions

** [AS-SDCM] - Each sweep requires a distinct cognitive mode and must not run simultaneously with another.** The structural sweep requires architectural judgment: is this content at the right level, is this section straining, is this open question ready to graduate? The language sweep requires close reading: does this term carry its meaning without session context, has session residue accumulated? Each mode requires concentration the other's presence would dilute. Running more than one in a single pass produces shallow work in every direction.

** [AS-SSPS] - The structural sweep's precondition is section sequence, not content presence.** A coherent draft means the eight sections have been populated in order: Problem before Assumptions, Landscape before Options, Options before Chosen Direction. Content can be sparse. What cannot be missing is the sequence. A structural sweep invoked before the sequence is honored has no architecture to review against. It produces noise, not findings.

** [AS-OPNS] - Operational documents have no fixed structure to sweep against.** Reasoning documents share the eight-section spine across every domain because reasoning has a universal shape. Operational documents carry whatever a domain's execution requires: a business plan, a questionnaire analysis, a planting plan. No sweep that anchors to a fixed structure can be applied to them. This assumption breaks if RFM ever adopts a mandatory structure for operational documents, which would require revisiting the operational sweep's design from scratch.

---

## The Landscape

| Approach | What it does | Why it's insufficient for the sweep prompts |
|---|---|---|
| **LLM-as-judge with rubrics** | A second LLM evaluates output against structured criteria. Rubric-based judging (Prometheus, G-Eval, RRD, 2025-2026) improves reliability over holistic judgment. | Rubrics are static and output-focused. Cannot detect hierarchy failures, session residue, or ownership drift in a living document. Criteria do not distinguish structural from language failures. |
| **Multi-agent critique** | Multiple LLM agents critique each other's outputs, simulating peer review. | Designed for discrete outputs, not living documents with history and derivative chains. Research shows LLMs systematically underperform at identifying weaknesses and raising substantive questions, the core sweep function. |
| **Structured critique prompts** | Chain-of-thought evaluation steps generated from task introduction and explicit criteria (G-Eval pattern). | Closest prior art. Criteria are task-specific and static: no section-sequence awareness, no hierarchy ownership check, no structural/language mode distinction. |

**The gap:** no existing approach applies mode-distinct corrective passes, organized by cognitive job rather than document type, to a living reasoning document hierarchy, with findings produced for human ruling rather than automated scoring. The sweep prompts occupy this gap specifically.

---

## The Options Considered

**1. Holistic review vs. section-by-section protocol**

Ask the LLM to identify failures across the whole document at once vs. work through section by section in sequence. Holistic review is faster but misses gradual drift. Failures that only become visible under sequential attention fall through. Section-by-section protocol chosen because the failure modes the sweep targets are cumulative and positional: session residue accumulates across sections, hierarchy drift is visible only when sections are compared against each other in sequence.

**2. Fixed criteria vs. document-adaptive criteria**

Apply the same checklist to every document vs. allow the sweep to adapt its attention to the specific document's type, age, and state. Fixed criteria are auditable and consistent but miss document-specific strain signals. Adaptive criteria require the LLM to reason about what matters here, which is the correct cognitive mode for a living document. Document-adaptive criteria chosen, with the section-by-section protocol as the structural anchor that prevents adaptation from becoming drift.

**4. Broad derivation readiness vs. textual handoff audit**

Test whether the reasoning-plus-operational pair can produce the derivative, vs. scan the reasoning document for announced needs and verify each is specified in the operational document. The broad reading was rejected because it runs the derivation to find the sweep's own failures. That makes the sweep indistinguishable from the thing it is meant to precede, and eliminates the independent corrective pass that produces findings before the human commits to derivation.

**3. Scoring output vs. findings-for-ruling output**

Produce a quality score vs. produce named findings with proposed resolutions for human ruling. Scoring is automated and scalable, the dominant pattern in LLM-as-judge practice. Rejected because the sweep targets reasoning document integrity, not output quality. A score compresses the finding into a number that cannot be acted on. Named findings with proposed resolutions keep the human as decision-maker and produce output that can be directly executed or rejected. Findings-for-ruling is the only output format consistent with the co-author ceiling.

---

## The Chosen Direction and Why

**Why section-by-section protocol with document-adaptive criteria:**

The section sequence is fixed. It is the structural anchor. The criteria adapt to the document's state: early development has different failure modes than a mature curated document. Fixed sequence prevents adaptation from becoming drift. Adaptive criteria prevent the protocol from becoming a checklist that misses what actually matters here.

**Why the sweeps have different entry conditions:**

The structural sweep requires section sequence to be honored because it reviews architecture, and architecture requires something to be built. The language sweep can run on partial content because wording failures are local. Entry conditions differ by design, not convention.

**Why the structural sweep verifies source set completeness as an entry condition:**

A derivative whose operational document omits its source set, or whose source set excludes `RFM_top_level_reasoning.md`, will not inherit methodology-level discipline through re-derivation. That gap is invisible from inside a single session and will not surface as a section-level finding. It must be caught before the sweep proceeds, not during it.

Source set completeness is therefore an entry condition for the structural sweep, not a section-level finding. If the document under sweep is a derivative, the sweep verifies that its operational document names the source set and that the source set is complete before architectural review begins. An incomplete source set stops the sweep and surfaces as a flag for human ruling. A structural sweep conducted against a derivative with an unverified source set cannot confirm that its findings are complete.

**Why source set completeness is an entry condition for the operational sweep:**

The operational sweep checks what passes between two documents. If the operational document does not name its source set, or if the source set is incomplete, the sweep cannot verify that the boundary it is checking is the right one. The failure is the same as in the structural sweep: a gap invisible from inside the session that will not surface as a relational finding. It must be caught before the check begins, not during it.

Source set completeness is therefore a hard stop for the operational sweep, not a finding. If the operational document does not name its source set, or the source set excludes `RFM_top_level_reasoning.md`, the sweep stops and flags it for human ruling.

**Why the operational sweep output uses a two-field location rather than a single location field:**

A finding in the structural or language sweep has one location: a section, and optionally an entry, within a single document. A finding in the operational sweep is relational. It names a gap between two documents: an announced need on the reasoning side with no coverage on the operational side, or a specification on the operational side with no announced need on the reasoning side. A single location field cannot represent both sides of that gap without requiring the reviewer to parse a prefix convention at the moment of ruling. Two fields, one per document, make the directionality of the finding visible directly. Either field may be blank when the finding is one-sided.

**Why findings are surfaced one per exchange:**

The exchange itself is the tracking mechanism. When findings arrive as a list, the human cannot hold them all. Some get ruled on, the rest disappear without explicit closure. One finding per exchange eliminates that failure mode: nothing can slip through because the next finding does not appear until the current one has been ruled on. The LLM holds the queue.

This is consistent with the living document principle: ruling quality does not need to be perfect in any single sweep. Corrections surface in the next. The cost of an imperfect ruling is low. The cost of findings disappearing unruled is not recoverable in the same session.

When a finding is entangled with another, where the ruling on one affects the right ruling on the other, the LLM flags that before the human rules, not after. The LLM holds the structural map across the session. The human does not need to.

**Why the structural sweep owns hierarchy and the language sweep owns expression:**

Hierarchy failures require holding the full document structure in view and reasoning across it. Expression failures require close reading of individual sentences. Assigning each to its own sweep ensures neither cognitive mode is diluted by the other's presence.

**Why the structural sweep owns positional grey zones:**

Some failures are both positional and about wording. The primary failure type determines ownership. Positional failures go to the structural sweep regardless of whether wording failures are also present. Wording failures go to the language sweep. When both are present in equal weight, the structural sweep flags it as a grey zone, names both failure types, and the language sweep does not run on that entry until the human has ruled.

**Why the mode-contamination test applies to the question, not the finding's content:**

When an LLM running the structural sweep evaluates whether a finding belongs, the test is the cognitive mode that generated the question, not what the finding happens to touch. A structural question can surface an expression symptom incidentally and remain correctly placed: the question arose from architectural judgment. A question framed in expression-review mode does not belong in the structural sweep regardless of whether it also identifies a positional problem. The behavioral instruction must specify the register test: is this question an act of architectural judgment, or of close reading? If close reading generated the question, it belongs in the language sweep, not here. Framing the test as "does this finding touch expression failures?" produces false positives: legitimate structural findings that name expression symptoms get suppressed.

**Why the operational sweep checks both directions across the reasoning-to-operational boundary:**

Reasoning documents announce needs without specifying them: a concrete value, threshold, interface, or procedure that derivation will require. Specifying them in the reasoning document pulls implementation detail where it does not belong. The operational document covers those needs. Checking only forward, whether the operational document covers every announced need, trusts that the reasoning document announced every need. An unannounced need is invisible to that pass and falls through, leaving the LLM to invent the specification during derivation rather than read it. Checking only in reverse, whether every specification in the operational document traces to an announced need, catches a different failure: a specification with no announced need means either the reasoning failed to announce it, now made visible, or a decision was made at the operational level that belongs in reasoning first. A specification that traces to a broader reasoning commitment, a chosen direction or design principle, is grounded. The reverse-direction finding is the absence of any grounding in the reasoning document, not the absence of a one-to-one announced need. A reasoning document that commits to a direction at a level of abstraction that produces multiple operational specifications has announced a need at the appropriate level. Requiring a separate announced need for each downstream specification would pull implementation specificity into the reasoning document. Both directions check the same boundary. Neither catches what the other misses. This also closes the boundary the methodology already guards from one side: wrong content present in the operational document is reasoning-leak; required content absent is a specification gap. Same boundary, two violations.

**Why the reasoning-to-operational check is relational, not inward-reading:**

The structural sweep asks whether a document coheres with itself. The language sweep asks whether its expression is clean. Both read inward. The reasoning-to-operational check asks whether two documents together are sufficient to produce the derivative without the LLM inventing content. That question cannot be answered by reading either document alone. It requires holding both simultaneously and checking what passes between them. This is a different cognitive job, which is why it cannot be folded into either existing sweep without losing the check that only the relational pass performs.

**Why the reasoning-to-operational check is textual and bounded, not a trial derivation:**

Scanning for announced needs and verifying each is covered in the operational document keeps the check independent of the derivation it precedes. Running a trial derivation to find gaps would work in principle, but it collapses the corrective pass into the thing it is meant to come before. The practitioner loses the independent findings-for-ruling step. The textual check is also auditable: each gap it surfaces names a specific announced need with no corresponding specification, which the human can rule on directly. A trial derivation surfaces gaps only as derivation failures, which are harder to locate and harder to rule on before the full derivation is committed.

**Why the corrective arm organizes by cognitive mode, not document type:**

Labeling the sweeps by document type creates a trap. A reasoning sweep and an operational sweep sounds tidy, but it puts the language job in an impossible position: language failures, session residue, opaque wording, compressed reasoning, appear in both document types equally. Tie the label to document type and the language catalog either splits across two artifacts or gets duplicated. Both outcomes mean two people maintaining the same list. Mode-based organization avoids this. Architectural judgment goes in one sweep, relational checking in another, close reading for language quality in a third. The language catalog stays one object with one source.

**Why the language catalog transfers across document types but the architecture jobs do not share one:**

Language failures appear regardless of document type. Session residue accumulates in a reasoning document and an operational document for the same reason: the person writing had context the reader lacks. Opaque wording, compressed reasoning, claims that outrun their evidence: none of these care what kind of document they are in. One catalog catches them all. Architecture failures are specific to document type. The structural sweep checks whether the eight-section spine is intact and whether content sits at the right level, a question that only makes sense for reasoning documents. The relational check asks whether every need announced in the reasoning document is covered in the operational document, a question that only makes sense when both documents are present. No catalog spans both, because the questions themselves do not overlap.

**Why detecting content a parent document still carries after branching belongs in the structural sweep:**

When a module branches from a parent document, the parent is expected to remove whatever the module now owns. In practice this does not happen automatically. Catching it requires holding both the parent and child in view simultaneously, which is architectural judgment. Wording failures are local to a single document. This failure is not.

---

## The Boundaries

**Not a quality gate that can be passed.** The sweep produces findings, not a score. Absence of findings signals either a well-curated document or a shallow sweep. The human cannot distinguish between the two without judging the sweep's depth independently. There is no clean sweep. The output is always findings for ruling, never a certification.

**Not a substitute for the traveling prompt.** The sweep corrects failures that slipped through ambient discipline. It cannot compensate for absent discipline. A document produced without the traveling prompt will accumulate failures faster than the sweep can reliably catch them.

**Not a validator of the reasoning itself.** The sweeps find structural and language failures. They do not assess whether the reasoning is correct, whether the chosen direction is the right one, or whether the assumptions will hold. That judgment belongs to the human. A document that passes both sweeps may still contain wrong thinking.

---

## The Open Questions

*No open questions at this time.*

---

## Hard Lessons

**[HL-SAFT] A sweep prompt that is too ambient fails silently.**

The sweep fails not by producing wrong findings but by producing shallow ones. The LLM runs through sections without concentrating, flags nothing, and the document appears clean. Ambient character is the traveling prompt's strength and the sweep prompt's primary failure mode. The sweep must feel like deliberate critique, not background discipline.

**[HL-RPSI] Repetition across sections is invisible from inside the session that produced it.**

The same argument restated in different styles across Options Considered and Chosen Direction looks like thoroughness from inside the drafting session. It is only visible under the concentrated attention of a structural sweep. This is a primary target for the structural sweep: not duplication of content, but duplication of reasoning dressed as distinct entries.

**[HL-CMDV] Mode-contamination between sibling sweep prompts is invisible to the standard derivation checks.**

The confirmation gate verifies fidelity to source. The coverage check verifies nothing from a prior version was lost without tracing back to source. Neither check is built to catch a question that is faithfully derived from source, and still wrong for the artifact it ends up in: a structural-mode question rendered into the language sweep prompt, or the reverse. The error passed both checks cleanly in practice, because both checks ask whether content is grounded, not whether it is grounded in the right artifact's mode.

This is `[AS-SDCM]` failing silently rather than loudly. The assumption states that each sweep's mode requires concentration the other's presence would dilute. A single misplaced question does not look like a foreign sweep prompt has appeared inside the current one. It looks like one clean sentence, sourced correctly, sitting where it does not belong. The dilution `[AS-SDCM]` warns against does not require modes to be merged wholesale: one sentence in the wrong register is sufficient to reintroduce the failure the mode-separation design exists to prevent.

**[HL-LCAD] The Problem gets pulled toward the session's own material.**

When a session adds new reasoning to a document, the new content feels like the point and the Problem feels like it should reflect that. It should not. The Problem states why the document exists. That question does not change when the answer grows. Rewriting the Problem to absorb session content loses the original gap statement and makes the document harder to re-derive from. The fix is simple: leave the Problem alone unless the gap itself has changed, not just the reasoning that fills it.

---

*module_reasoning // [living]*
*the sweep prompts are the corrective arm*
*findings for ruling, not edits*
*the reasoning comes first. the prompts follow*
