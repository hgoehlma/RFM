# Reasoning-First Methodology: Sweep Prompts Reasoning Document
`v0.10.0` // `module_reasoning` // [living]

---

## The Problem

A finished document can hold failures that nobody sees while writing it: content sitting at the wrong level, a parent still carrying what its child now owns, wording that only makes sense to the session that produced it, claims that planned work will make false, and a reasoning document and its operational derivative that leave a gap the LLM would have to fill by inventing. Catching these takes a deliberate pass over the finished document, and a pass built without regard to what each kind of failure needs goes wrong in predictable ways. A pass asked to judge structure and wording at once tends to do shallow work on both. A pass that edits decides what the human should decide, and a pass that scores hands back a number nobody can act on. The failures then stay in the documents, or get fixed without the human having ruled on them.

---

## The Assumptions

**[AS-SWDJ] - Each sweep does one job, and no two sweeps run in the same pass.** The structural sweep judges architecture: is this content at the right level, is this section straining, is this open question ready to graduate? The language sweep reads sentences closely: does this term carry its meaning without session context, has session residue accumulated? Each job needs attention that the other's presence would divert, so a pass doing both does shallow work on both. This breaks if a single pass that covers both is shown to find what two separate passes find.

**[AS-SSPS] - The structural sweep's precondition is section sequence, not content presence.** A coherent draft means the eight sections have been populated in order: Problem before Assumptions, Landscape before Options, Options before Chosen Direction. Content can be sparse. What cannot be missing is the sequence. This breaks if a sweep of a document with a missing or out-of-order section is shown to produce findings as reliable as a sweep of a complete one.

**[AS-OPNS] - Operational documents have no fixed structure to sweep against.** Reasoning documents share the eight-section spine across every domain because reasoning has a universal shape. Operational documents carry whatever a domain's execution requires: a business plan, a questionnaire analysis, a planting plan. No sweep that anchors to a fixed structure can be applied to them. This breaks if RFM ever adopts a mandatory structure for operational documents, which would make a structure-based sweep of them possible.

---

## The Landscape

| Approach | What it does | Why it's insufficient for the sweep prompts |
|---|---|---|
| **LLM-as-judge with rubrics** | A second LLM evaluates output against structured criteria. Rubric-based judging (Prometheus, G-Eval, RRD, 2025-2026) improves reliability over holistic judgment. | Rubrics are static and output-focused. Cannot detect hierarchy failures, session residue, or ownership drift in a living document. Criteria do not distinguish structural from language failures. |
| **Multi-agent critique** | Multiple LLM agents critique each other's outputs, simulating peer review. | Designed for discrete outputs, not living documents with history and derivative chains. The critique it relies on is weak: a study of LLM-written reviews of scientific papers (arXiv 2509.19326) found five single LLMs consistently underperformed at identifying weaknesses and raising substantive questions, the core sweep function. The study did not test multi-agent setups, so the weakness carries over only as far as those setups rely on the same critique. |
| **Structured critique prompts** | Chain-of-thought evaluation steps generated from task introduction and explicit criteria (G-Eval pattern). | Closest prior art. Criteria are task-specific and static: no section-sequence awareness, no hierarchy ownership check, no structural/language mode distinction. |

**The gap:** no existing approach reviews a living hierarchy of reasoning documents for the failures a finished document accumulates, with a separate pass for each kind of failure, and hands its findings to a human to rule on instead of returning a score. The sweep prompts occupy this gap.

---

## The Options Considered

**Scoring output vs. findings-for-ruling output**

Produce a quality score vs. produce named findings with proposed resolutions for human ruling. Scoring is automated and scalable, the dominant pattern in LLM-as-judge practice. Rejected because the sweep targets reasoning document integrity, not output quality. A score compresses the finding into a number that cannot be acted on. Named findings with proposed resolutions keep the human as decision-maker and produce output that can be directly executed or rejected. Findings-for-ruling is the only output format consistent with the co-author ceiling.

---

## The Chosen Direction and Why

**Why the sweeps have different entry conditions**

**Why the sweeps produce findings for ruling, not edits**

A sweep that edits the document directly collapses the corrective pass into the authoring pass: it removes the human judgment step the correction exists to protect. Findings for ruling keep that step in place. This is a different argument from the one against scoring: scoring fails because a number cannot be acted on, while editing fails because it stops being a correction at all.

The structural sweep requires section sequence to be honored because it reviews architecture, and architecture requires something to be built. The language sweep can run on partial content because wording failures are local. Entry conditions differ by design, not convention.

**Why the structural sweep owns hierarchy and the language sweep owns expression**

**Why duplicated reasoning is a primary structural target**

The same argument restated in different styles across Options Considered and Chosen Direction reads as thoroughness from inside the session that wrote it. Only a pass reading the whole document at once, with nothing else to attend to, can see that two entries carry one argument. This is why the structural sweep's protocol treats duplicated reasoning, not just duplicated content, as a primary target.

Hierarchy failures require holding the full document structure in view and reasoning across it. Expression failures require close reading of individual sentences. Assigning each to its own sweep ensures neither job is diluted by the other's presence.

**Why the contamination test applies to the question, not the finding's content**

When an LLM running the structural sweep evaluates whether a finding belongs, the test is the job that generated the question, not what the finding happens to touch. A structural question can surface an expression symptom incidentally and remain correctly placed: the question arose from architectural judgment. A question generated by close reading of expression does not belong in the structural sweep regardless of whether it also identifies a positional problem. The behavioral instruction must specify the register test: is this question an act of architectural judgment, or of close reading? If close reading generated the question, it belongs in the language sweep, not here. Framing the test as "does this finding touch expression failures?" produces false positives: legitimate structural findings that name expression symptoms get suppressed.

**Why the relational sweep checks both directions across the reasoning-to-operational boundary**

Reasoning documents announce needs without specifying them: a concrete value, threshold, interface, or procedure that derivation will require. Specifying them in the reasoning document pulls implementation detail where it does not belong. The operational document covers those needs. Checking only forward, whether the operational document covers every announced need, trusts that the reasoning document announced every need. An unannounced need is invisible to that pass and falls through, leaving the LLM to invent the specification during derivation rather than read it. Checking only in reverse, whether every specification in the operational document traces to an announced need, catches a different failure: a specification with no announced need means either the reasoning failed to announce it, now made visible, or a decision was made at the operational level that belongs in reasoning first. A specification that traces to a broader reasoning commitment, a chosen direction or design principle, is grounded. The reverse-direction finding is the absence of any grounding in the reasoning document, not the absence of a one-to-one announced need. A reasoning document that commits to a direction at a level of abstraction that produces multiple operational specifications has announced a need at the appropriate level. Requiring a separate announced need for each downstream specification would pull implementation specificity into the reasoning document. Both directions check the same boundary. Neither catches what the other misses. This also closes the boundary the methodology already guards from one side: wrong content present in the operational document is reasoning-leak; required content absent is a specification gap. Same boundary, two violations.

**Why the reasoning-to-operational check is relational, not inward-reading**

The structural sweep asks whether a document coheres with itself. The language sweep asks whether its expression is clean. Both read inward. The reasoning-to-operational check asks whether two documents together are sufficient to produce the derivative without the LLM inventing content. That question cannot be answered by reading either document alone. It requires holding both simultaneously and checking what passes between them. This is a different cognitive job, which is why it cannot be folded into either existing sweep without losing the check that only the relational pass performs.

**Why the corrective arm organizes by job, not document type**

Labeling the sweeps by document type creates a trap. A reasoning sweep and an operational sweep sounds tidy, but it puts the language job in an impossible position: language failures, session residue, opaque wording, compressed reasoning, appear in both document types equally. Tie the label to document type and the language catalog either splits across two artifacts or gets duplicated. Both outcomes mean two people maintaining the same list. Organizing by job avoids this. Architectural judgment goes in one sweep, relational checking in another, close reading for language quality in a third. A sweep named for a document type reintroduces the trap at the label even where the design underneath is organized by job. The language catalog stays one object with one source.

**Why the language catalog transfers across document types but the architecture jobs do not share one**

Language failures appear regardless of document type. Session residue accumulates in a reasoning document and an operational document for the same reason: the person writing had context the reader lacks. Opaque wording, compressed reasoning, claims that outrun their evidence: none of these care what kind of document they are in. One catalog catches them all. Architecture failures are specific to document type. The structural sweep checks whether the eight-section spine is intact and whether content sits at the right level, a question that only makes sense for reasoning documents. The relational check asks whether every need announced in the reasoning document is covered in the operational document, a question that only makes sense when both documents are present. No set of per-section questions spans both, because the questions themselves do not overlap.

**Why detecting content a parent document still carries after branching belongs in the structural sweep**

When a module branches from a parent document, the parent is expected to remove whatever the module now owns. In practice this does not happen automatically. Catching it requires holding both the parent and child in view simultaneously, which is architectural judgment. Wording failures are local to a single document. This failure is not.

**Why the structural sweep owns the lifespan family**

The corrective arm splits by job. Judging whether planned work will falsify a claim requires knowing what the project has committed to elsewhere, which is the same knowledge the structural sweep already uses to judge whether an entry is ready to graduate. Close reading of the sentence does not answer it, so the language sweep would have to acquire that knowledge to run the check, and it would then be doing architectural judgment under a language label.

---

## The Boundaries

**Not a quality gate that can be passed.** The sweep produces findings, not a score. Absence of findings signals either a well-curated document or a shallow sweep. The human cannot distinguish between the two without judging the sweep's depth independently. There is no clean sweep. The output is always findings for ruling, never a certification.

**Not a substitute for the traveling prompt.** The sweep corrects failures that slipped through the traveling prompt's prevention. It cannot compensate for absent discipline. A document produced without the traveling prompt will accumulate failures faster than the sweep can reliably catch them.

**Not a validator of the reasoning itself.** The sweeps find structural, language and lifespan failures. They do not assess whether the reasoning is correct, whether the chosen direction is the right one, or whether the assumptions will hold. That judgment belongs to the human. A document that passes every sweep may still contain wrong thinking.

---

## The Open Questions

**[OQ-ARTCV] Whether the relational sweep's reach should extend from reasoning-to-operational derivation to reasoning-to-artifact derivation.**

The relational sweep already checks whether a derivative covers what its source announced, and whether the derivative contains anything ungrounded in the source. `[AS-OPNS]` excludes operational documents from the structural sweep's reach because they have no fixed structure to check architecture against, but a boundary check doesn't need fixed structure on the derivative side, only a source to compare it against, so that same reasoning doesn't obviously justify excluding prompt artifacts from the relational sweep. `[HL-DCFL]` in `RFM_top_level_reasoning.md` already shows this failure class is real: a reasoning document can be internally sound and still produce a derivation failure, where the LLM deriving from it collapses what the source kept distinct. That instance is not artifact-specific, so it does not show the failure occurs in prompt-artifact derivation, only that a boundary check catching sound-reasoning/bad-derivation failures would have something to catch. Whether the relational sweep's current restriction to `module_operational` derivatives is a deliberate scope decision or an accident of the map's type taxonomy is open. If the latter, extending the relational sweep is not a type-filter change: the sweep's one-to-one protocol would need to handle the sweep prompts' own one-reasoning-to-three-artifacts shape first.

**[OQ-LANGOP] Whether the language sweep should run on operational documents, and what it would ask there.**

The entry titled "Why the language catalog transfers across document types but the architecture jobs do not share one" says language failures appear in reasoning and operational documents for the same reason, and that one catalog catches them all. The language sweep prompt and its catalog in `RFM_sweep_operational.md` are both scoped to a reasoning document. The catalog's per-section questions are keyed to the eight reasoning sections. An operational document has no such sections (`[AS-OPNS]`), so no current artifact says how the language sweep would run on one. No current sweep checks an operational document for language failures.

The chosen-direction entry supports two readings. Under the first, it claims only that the failure types apply to any document, and the current scope is correct. Under the second, it claims the sweep should cover operational documents, and the artifacts do not yet deliver that. The record does not say which was meant.

If the second reading holds, the open design question is what the sweep asks of a document with no section spine: the language failure types alone, or a question set keyed to whatever structure that document's type carries.

---

## Hard Lessons

**[HL-CMDV] Contamination between sibling sweep prompts, one doing the other's job, is invisible to the standard derivation checks.**

The confirmation gate verifies fidelity to source. The coverage check verifies nothing from a prior version was lost without tracing back to source. Neither check is built to catch a question that is faithfully derived from source and still wrong for the artifact it ends up in: a structural question rendered into the language sweep prompt, or the reverse. Both checks ask whether content is grounded, not whether it is grounded in the right artifact's job.

This is `[AS-SWDJ]` breaking quietly rather than obviously. The assumption states that each sweep's job needs attention the other's presence would divert. A single misplaced question does not look like a foreign sweep prompt has appeared inside the current one. It looks like one clean sentence, sourced correctly, sitting where it does not belong. The dilution `[AS-SWDJ]` warns against does not require the two jobs to merge completely: one sentence in the wrong register is sufficient to reintroduce the failure the job-separation design exists to prevent.

---

*module_reasoning // [living]*
*the sweep prompts are the corrective arm*
*findings for ruling, not edits*
*the reasoning comes first. the prompts follow*
