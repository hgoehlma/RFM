# Reasoning-First Methodology: RFM Drafting Skill Reasoning Document
`v0.4.1` // `skill_rfm_drafting_reasoning` // [living]

---

## The Problem

RFM has two corrective mechanisms for document quality: the structural sweep and the language sweep. Both are after-the-fact passes. They catch failures that have already entered a document. The cost of correction scales with how much content was drafted before the sweep ran.

The gap is at the moment of production. When drafting new content for a reasoning or operational document, the practitioner holds the argument in mind and writes. Section-type conventions, placement rules, and language discipline exist in separate documents. Under production load, they compete poorly with the drive to get the reasoning down. Structural misplacements and language failures enter at this moment and persist until a sweep finds them.

Nothing currently fires at the moment of drafting to encode: where does this belong, what does this section require, and what does clean RFM prose look like.

---

## The Assumptions

**[AS-PRODLOAD]** Production load is the highest-risk moment for structural misplacement. The practitioner holds the reasoning and writes simultaneously. Checking placement requires stepping out of that mode. Without a forcing function, the check does not happen.

**[AS-DISTINCT]** Failure families do not cover each other. Content that passes one family's test can fail another's, so a check asking a single question catches a single family. The taxonomy in `RFM_operational.md` names the families and the boundaries between them.

**[AS-UNSLOP]** `rfm-unslop` already handles language compliance for all RFM session output. The drafting skill does not replicate that coverage. It references it and covers what it does not.

**[AS-HOME]** As RFM drafting practice accumulates insight, that insight needs a canonical home. The drafting skill is that home. It is explicitly extensible.

**[AS-SCOPE]** The skill covers reasoning documents, operational documents, and glossary entries. Execution artifacts sit at the end of the derivative chain and are regenerated, not drafted independently. They are out of scope.

---

## The Landscape

*[To be completed in a dedicated session. Prior approaches to consider: ambient instructions in the traveling prompt, section-type guidance in the operational doc, structural sweep as the only structural corrective.]*

---

## The Options Considered

*[To be completed in a dedicated session.]*

---

## The Chosen Direction and Why

**Why a skill rather than extended operational doc guidance.**
The operational doc carries formatting conventions. Drafting guidance is behavioral: it needs to fire at the moment of production, not be consulted after the fact. A skill fires; a document section does not.

**Why one skill covers the concerns that arise at the drafting moment**
These concerns arise at the same moment, when a practitioner is about to write content into a document. The module's rule groups a family that shares one moment, and its reasoning is in `RFM_skills_module_reasoning.md`. The rule applies cleanly here because no member of the family has a moment of its own to fire at.

**Why language compliance is delegated to rfm-unslop rather than duplicated.**
`rfm-unslop` is already always-on for all RFM session output. Duplicating its coverage in this skill creates two sources of truth for language rules. Delegation keeps language rules in one place and makes this skill's scope structurally distinct.

**Why glossary entries are in scope.**
Glossary entries are drafted at the same moment as other document content. The failure mode is specific: a term enters a document before it has been tested for standalone readability. The shorthand test and the reasoning requirement are the correct corrective at the drafting moment, not after the fact.

---

**Why the pre-check derives its own questions instead of running the sweep questions**

The pre-check and the sweeps read the same failure taxonomy in `RFM_operational.md`. Their questions differ because their moments differ. A sweep question asks whether a finished document contains a failure, which requires the whole document in view. A pre-check question asks whether the content about to be written will introduce one, which requires only that content. A sweep question asked at the drafting moment cannot be answered honestly, because the document it asks about does not exist yet.

The second reason concerns what the practitioner believes afterwards. A pre-check carrying a question per section reads as a sweep. A draft that passes it feels swept, and the concentrated pass then feels redundant. `[HL-NSWP]` records the failure this check answers, and the check must not produce a larger version of it. One question per failure family keeps the pre-check visibly smaller than the pass it does not replace.

The cost is that a question this coarse may catch nothing. That cost is accepted because it is visible: a check that finds nothing across sessions is evidence, and it can be sharpened against the failures it missed. A pre-check that displaces the sweep produces no evidence of having done so.

---

## The Boundaries

**Not a substitute for the structural sweep.** The structural sweep is a concentrated corrective pass requiring architectural judgment across a whole document. The drafting skill governs a single piece of content at the moment of production.

**Not a substitute for the language sweep.** `rfm-unslop` is the production-time language corrective. The language sweep catches what gets through.

**Not applicable to execution artifacts.** Traveling prompt, sweep prompts, and human prompt are regenerated from their sources. Drafting guidance does not apply to regeneration.

**Not applicable to non-RFM projects.** The section-type conventions and document structure rules are RFM-specific. The skill description front-loads this scope restriction.

---

## The Open Questions

**[OQ-TRIGGER] Does the skill trigger reliably on drafting tasks without being explicitly invoked?**
The description is written to fire on "drafting new content for any reasoning document, operational document, or glossary entry." Whether this is specific enough to activate without being asked, across different drafting contexts, is not yet known. Needs observation across sessions.

**[OQ-GROWTH] What additional drafting guidance belongs here that is not yet known?**
Practice will surface failure classes not yet anticipated. This question tracks what accumulates and signals when the skill body needs updating.

---

## Hard Lessons

**[HL-NSWP] Nothing checks a draft against the sweeps at the moment it is drafted.**

A Chosen Direction entry was drafted for the top-level reasoning document and presented as ready. Checked afterward against the two sweep prompts, it failed three times: a procedure had leaked into an entry that carries only why, a claim about model behavior was written as settled when it rested on a single analysis, and the entry ran to three paragraphs where two carried the argument. The check ran only because the human asked for it. The drafting skill was loaded at the moment the entry was written, carries placement and section-type rules, and caught none of the three. The sweeps catch them by design and run only when invoked, which is after the content is already in the document. A draft that passes the checks that happened to run says nothing about the checks that did not.
