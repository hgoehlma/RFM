# Reasoning-First Methodology: RFM Drafting Skill Operational Document
`v0.4.0` // `skill_rfm_drafting_operational` // `[living]`

---

## What this document covers

Derivation procedure for the `rfm-drafting` skill. The reasoning behind every decision here is in `RFM_skill_rfm_drafting_reasoning.md`. Rules shared by all RFM skills are in `RFM_skills_module_operational.md`. This document carries what is specific to `rfm-drafting`.

---

## The artifact

The `rfm-drafting` skill, installed and active in the user's environment.

The skill source is `rfm-drafting/SKILL.md`. Delivery is environment-specific: some environments package the source into an installable file the user downloads, others present the source for review and save it directly. Use the mechanism the current environment provides. The requirement is that the user ends up with the skill installed, not that a file is produced.

---

## Source documents: load before editing the skill

1. `RFM_skill_rfm_drafting_reasoning.md`: the reasoning governing all design decisions
2. `RFM_operational.md`: formatting conventions and document structure rules
3. `RFM_skill_unslop_operational.md`: language compliance conventions delegated to rfm-unslop

---

## Skill structure

The skill has no `references/` directory. All content is in `SKILL.md`. If the body exceeds 500 lines in a future revision, extract the section-type guidance to `references/sections.md` and add a pointer in the body.

YAML frontmatter rules:
- Description must be a single quoted string. Multi-line YAML values break validation.
- Keep description between 200-400 characters.
- Front-load "RFM sessions only" in the description for truncation safety.

---

## Pre-check specification

The pre-check is Layer 4 of the skill body. It runs after Layers 1 to 3 and before the draft is shown to the human. It is scoped to the content in hand, never to the document the content will enter.

**The questions.** One per failure family in the Failure Taxonomy in `RFM_operational.md`. Any change to a question begins here.

*Structural:* Does every part of this content belong at this level, in this section, and to this document rather than another?

*Language:* Would a reader who was not in this session understand this content and see the reasoning behind each claim it makes?

*Lifespan:* Will work already planned make any part of this content false or redundant?

**On a hit.** Revise before presenting. When the hit cannot be resolved without a ruling, present the draft with the concern named rather than silently resolving it.

**What the pre-check does not do.** It does not report a draft as swept. It reads one question per failure family against one piece of content; a sweep reads a document. A draft that passes the pre-check carries no evidence about anything the pre-check did not ask.

---

## Skill body maintenance

When a new drafting failure class is identified in practice:

1. Determine which layer it belongs to: placement (Layer 1), writing rules (Layer 2), derivative chain (Layer 3), or the pre-check (Layer 4).
2. Add it to the skill body under the appropriate layer.
3. Update `RFM_skill_rfm_drafting_reasoning.md` if the addition reflects a new assumption or hard lesson. If the addition is a new failure class rather than new guidance, it belongs in the Failure Taxonomy in `RFM_operational.md` first.
4. Reinstall the updated skill in the user's environment.
5. Bump the version on this operational document. Skills carry no version number.

---

## Coverage check: after derivation

Apply the shared coverage check in `RFM_skills_module_operational.md` first. In addition, verify the skill:
- Description front-loads "RFM sessions only"
- Body opens directly on Layer 1
- rfm-unslop is referenced in Layer 2, not duplicated
- Layer 4 states that the pre-check is not a sweep

---

*skill_rfm_drafting_operational // [living]*
*carries what; the reasoning documents carry why*
