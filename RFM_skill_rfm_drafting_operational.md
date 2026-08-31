# Reasoning-First Methodology: RFM Drafting Skill Operational Document
`v0.1.0` // `skill_rfm_drafting_operational` // `[living]`

---

## What this document covers

Derivation procedure for the `rfm-drafting` skill. The reasoning behind every decision here is in `RFM_skill_rfm_drafting_reasoning.md`.

---

## The artifact

`rfm-drafting.skill`: a packaged skill file installed to the user's skill directory for the current environment.

The skill source is `rfm-drafting/SKILL.md`. Package it using the skill-creator packaging tool available in the current environment.

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

## Retirement of R-LENSMODE

R-LENSMODE in `RFM_handover_rules.md` is retired when `rfm-drafting` is installed. Steps:

1. Install `rfm-drafting.skill`.
2. Remove R-LENSMODE from `RFM_handover_rules.md`.
3. Bump version on `RFM_handover_rules.md`.
4. Run `rfm-ripple-check` to confirm no remaining references to R-LENSMODE across RFM documents.

---

## Skill body maintenance

When a new drafting failure class is identified in practice:

1. Determine which layer it belongs to: placement (Layer 1), writing rules (Layer 2), or derivative chain (Layer 3).
2. Add it to the skill body under the appropriate layer.
3. Update `RFM_skill_rfm_drafting_reasoning.md` if the addition reflects a new assumption or hard lesson.
4. Repackage the skill.
5. Bump versions on both the skill source and this operational document.

---

## Coverage check: after derivation

Verify the packaged skill:
- Validates without error via the environment's skill packaging tool
- Description is a single line, target 200-400 characters, "RFM sessions only" appears first
- Body opens directly on Layer 1, no preamble
- No em dashes in the skill body
- rfm-unslop is referenced in Layer 2, not duplicated

---

*skill_rfm_drafting_operational // [living]*
*carries what; the reasoning documents carry why*
