# Reasoning-First Methodology: Sweep Prompts Reasoning Document
`v0.9.0` // `module_reasoning` // [living]

---

## The Problem

The sweep prompts are the corrective arm of the prompt system. Their existence and purpose are established in `RFM_prompts_reasoning.md`. What that document does not carry is the artifact-level design: how each sweep is structured, what it targets section by section, how it signals completion, and how the sweeps differ in cognitive mode while sharing the same output discipline. Without a reasoning document at this level, the sweep prompts have no source: they are derivatives with nowhere to point when their design is questioned or needs to change.

---

## The Assumptions

** [AS-SDCM] - Each sweep requires a distinct cognitive mode and must not run simultaneously with another.** The structural sweep requires architectural judgment: is this content at the right level, is this section straining, is this open question ready to graduate? The language sweep requires close reading: does this term carry its meaning without session context, has session residue accumulated? Each mode requires concentration the other's presence would dilute. Running more than one in a single pass produces shallow work in every direction.

** [AS-SSPS] - The structural sweep's precondition is section sequence, not content presence.** A coherent draft means the eight sections have been populated in order: Problem before Assumptions, Landscape before Options, Options before Chosen Direction. Content can be sparse. What cannot be missing is the sequence. A structural sweep invoked before the sequence is honored has no architecture to review against. It produces noise, not findings.

** [AS-OPNS] - Operational documents have no fixed structure to sweep against.** Reasoning documents share the eight-section spine across every domain because reasoning has a universal shape. Operational documents carry whatever a domain's execution requires: a business plan, a questionnaire analysis, a planting plan. No sweep that anchors to a fixed structure can be applied to them. This assumption breaks if RFM ever adopts a mandatory structure for operational documents, which would require revisiting the relational sweep's design from scratch.

---

## The Landscape

**The gap:** no existing approach applies mode-distinct corrective passes, organized by cognitive job rather than document type, to a living reasoning document hierarchy, with findings produced for human ruling rather than automated scoring. The sweep prompts occupy this gap specifically.

---

## The Options Considered

**3. Scoring output vs. findings-for-ruling output**

Produce a quality score vs. produce named findings with proposed resolutions for human ruling. Scoring is automated and scalable, the dominant pattern in LLM-as-judge practice. Rejected because the sweep targets reasoning document integrity, not output quality. A score compresses the finding into a number that cannot be acted on. Named findings with proposed resolutions keep the human as decision-maker and produce output that can be directly executed or rejected. Findings-for-ruling is the only output format consistent with the co-author ceiling.

---

## The Chosen Direction and Why

**Why the sweeps have different entry conditions**

The structural sweep requires section sequence to be honored because it reviews architecture, and architecture requires something to be built. The language sweep can run on partial content because wording failures are local. Entry conditions differ by design, not convention.

**Why the structural sweep owns hierarchy and the language sweep owns expression**

Hierarchy failures require holding the full document structure in view and reasoning across it. Expression failures require close reading of individual sentences. Assigning each to its own sweep ensures neither cognitive mode is diluted by the other's presence.

**Why the mode-contamination test applies to the question, not the finding's content**

When an LLM running the structural sweep evaluates whether a finding belongs, the test is the cognitive mode that generated the question, not what the finding happens to touch. A structural question can surface an expression symptom incidentally and remain correctly placed: the question arose from architectural judgment. A question framed in expression-review mode does not belong in the structural sweep regardless of whether it also identifies a positional problem. The behavioral instruction must specify the register test: is this question an act of architectural judgment, or of close reading? If close reading generated the question, it belongs in the language sweep, not here. Framing the test as "does this finding touch expression failures?" produces false positives: legitimate structural findings that name expression symptoms get suppressed.

**Why the relational sweep checks both directions across the reasoning-to-operational boundary**

Reasoning documents announce needs without specifying them: a concrete value, threshold, interface, or procedure that derivation will require. Specifying them in the reasoning document pulls implementation detail where it does not belong. The operational document covers those needs. Checking only forward, whether the operational document covers every announced need, trusts that the reasoning document announced every need. An unannounced need is invisible to that pass and falls through, leaving the LLM to invent the specification during derivation rather than read it. Checking only in reverse, whether every specification in the operational document traces to an announced need, catches a different failure: a specification with no announced need means either the reasoning failed to announce it, now made visible, or a decision was made at the operational level that belongs in reasoning first. A specification that traces to a broader reasoning commitment, a chosen direction or design principle, is grounded. The reverse-direction finding is the absence of any grounding in the reasoning document, not the absence of a one-to-one announced need. A reasoning document that commits to a direction at a level of abstraction that produces multiple operational specifications has announced a need at the appropriate level. Requiring a separate announced need for each downstream specification would pull implementation specificity into the reasoning document. Both directions check the same boundary. Neither catches what the other misses. This also closes the boundary the methodology already guards from one side: wrong content present in the operational document is reasoning-leak; required content absent is a specification gap. Same boundary, two violations.

**Why the reasoning-to-operational check is relational, not inward-reading**

The structural sweep asks whether a document coheres with itself. The language sweep asks whether its expression is clean. Both read inward. The reasoning-to-operational check asks whether two documents together are sufficient to produce the derivative without the LLM inventing content. That question cannot be answered by reading either document alone. It requires holding both simultaneously and checking what passes between them. This is a different cognitive job, which is why it cannot be folded into either existing sweep without losing the check that only the relational pass performs.

**Why the corrective arm organizes by cognitive mode, not document type**

Labeling the sweeps by document type creates a trap. A reasoning sweep and an operational sweep sounds tidy, but it puts the language job in an impossible position: language failures, session residue, opaque wording, compressed reasoning, appear in both document types equally. Tie the label to document type and the language catalog either splits across two artifacts or gets duplicated. Both outcomes mean two people maintaining the same list. Mode-based organization avoids this. Architectural judgment goes in one sweep, relational checking in another, close reading for language quality in a third. A sweep named for a document type reintroduces the trap at the label even where the design underneath is mode-based. The language catalog stays one object with one source.

**Why the language catalog transfers across document types but the architecture jobs do not share one**

Language failures appear regardless of document type. Session residue accumulates in a reasoning document and an operational document for the same reason: the person writing had context the reader lacks. Opaque wording, compressed reasoning, claims that outrun their evidence: none of these care what kind of document they are in. One catalog catches them all. Architecture failures are specific to document type. The structural sweep checks whether the eight-section spine is intact and whether content sits at the right level, a question that only makes sense for reasoning documents. The relational check asks whether every need announced in the reasoning document is covered in the operational document, a question that only makes sense when both documents are present. No set of per-section questions spans both, because the questions themselves do not overlap.

**Why detecting content a parent document still carries after branching belongs in the structural sweep**

When a module branches from a parent document, the parent is expected to remove whatever the module now owns. In practice this does not happen automatically. Catching it requires holding both the parent and child in view simultaneously, which is architectural judgment. Wording failures are local to a single document. This failure is not.

**Why the structural sweep owns the lifespan family**

The corrective arm splits by cognitive mode. Judging whether planned work will falsify a claim requires knowing what the project has committed to elsewhere, which is the same knowledge the structural sweep already uses to judge whether an entry is ready to graduate. Close reading of the sentence does not answer it, so the language sweep would have to acquire that knowledge to run the check, and it would then be doing architectural judgment under a language label.

---

## The Boundaries

**Not a quality gate that can be passed.** The sweep produces findings, not a score. Absence of findings signals either a well-curated document or a shallow sweep. The human cannot distinguish between the two without judging the sweep's depth independently. There is no clean sweep. The output is always findings for ruling, never a certification.

**Not a substitute for the traveling prompt.** The sweep corrects failures that slipped through ambient discipline. It cannot compensate for absent discipline. A document produced without the traveling prompt will accumulate failures faster than the sweep can reliably catch them.

**Not a validator of the reasoning itself.** The sweeps find structural, language and lifespan failures. They do not assess whether the reasoning is correct, whether the chosen direction is the right one, or whether the assumptions will hold. That judgment belongs to the human. A document that passes every sweep may still contain wrong thinking.

---

## The Open Questions

**[OQ-ARTCV] Whether the relational sweep's reach should extend from reasoning-to-operational derivation to reasoning-to-artifact derivation.**

The relational sweep already checks whether a derivative covers what its source announced, and whether the derivative contains anything ungrounded in the source. `[AS-OPNS]` excludes operational documents from the structural sweep's reach because they have no fixed structure to check architecture against, but a boundary check doesn't need fixed structure on the derivative side, only a source to compare it against, so that same reasoning doesn't obviously justify excluding prompt artifacts from the relational sweep. A correction-script failure already recorded as a Hard Lesson in `RFM_human_prompt_reasoning.md` is exactly the shape of defect a boundary check would catch: the reasoning behind it was sound, and the specific wording chosen during derivation was not, a derivation-boundary failure rather than a reasoning failure. Whether the relational sweep's current restriction to `module_operational` derivatives is a deliberate scope decision or an accident of the map's type taxonomy is open. If the latter, extending the relational sweep is not a type-filter change: the sweep's one-to-one protocol would need to handle the sweep prompts' own one-reasoning-to-three-artifacts shape first.

**[OQ-LANGOP] Whether the language sweep should run on operational documents, and what it would ask there.**

The entry titled "Why the language catalog transfers across document types but the architecture jobs do not share one" says language failures appear in reasoning and operational documents for the same reason, and that one catalog catches them all. The language sweep prompt and its catalog in `RFM_sweep_operational.md` are both scoped to a reasoning document. The catalog's per-section questions are keyed to the eight reasoning sections. An operational document has no such sections (`[AS-OPNS]`), so no current artifact says how the language sweep would run on one. No current sweep checks an operational document for language failures.

The chosen-direction entry supports two readings. Under the first, it claims only that the failure types apply to any document, and the current scope is correct. Under the second, it claims the sweep should cover operational documents, and the artifacts do not yet deliver that. The record does not say which was meant.

If the second reading holds, the open design question is what the sweep asks of a document with no section spine: the language failure types alone, or a question set keyed to whatever structure that document's type carries.

---

## Hard Lessons

**[HL-RPSI] Repetition across sections is invisible from inside the session that produced it.**

The same argument restated in different styles across Options Considered and Chosen Direction looks like thoroughness from inside the drafting session. It is only visible under the concentrated attention of a structural sweep. This is a primary target for the structural sweep: not duplication of content, but duplication of reasoning dressed as distinct entries.

**[HL-CMDV] Mode-contamination between sibling sweep prompts is invisible to the standard derivation checks.**

The confirmation gate verifies fidelity to source. The coverage check verifies nothing from a prior version was lost without tracing back to source. Neither check is built to catch a question that is faithfully derived from source, and still wrong for the artifact it ends up in: a structural-mode question rendered into the language sweep prompt, or the reverse. The error passed both checks cleanly in practice, because both checks ask whether content is grounded, not whether it is grounded in the right artifact's mode.

This is `[AS-SDCM]` failing silently rather than loudly. The assumption states that each sweep's mode requires concentration the other's presence would dilute. A single misplaced question does not look like a foreign sweep prompt has appeared inside the current one. It looks like one clean sentence, sourced correctly, sitting where it does not belong. The dilution `[AS-SDCM]` warns against does not require modes to be merged wholesale: one sentence in the wrong register is sufficient to reintroduce the failure the mode-separation design exists to prevent.

---

*module_reasoning // [living]*
*the sweep prompts are the corrective arm*
*findings for ruling, not edits*
*the reasoning comes first. the prompts follow*
