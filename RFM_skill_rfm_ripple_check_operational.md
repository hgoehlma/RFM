# Reasoning-First Methodology: RFM Ripple Check Skill Operational Document
`v0.3.1` // `skill_rfm_ripple_check_operational` // [living]

---

## What this document covers

Derivation procedure for the `rfm-ripple-check` skill. The reasoning behind every decision here is in `RFM_skill_rfm_ripple_check_reasoning.md`. Rules shared by all RFM skills are in `RFM_skills_module_operational.md`. This document carries what is specific to `rfm-ripple-check`.

---

## The artifact

The `rfm-ripple-check` skill, installed and active in the user's environment.

The skill source is `rfm-ripple-check/SKILL.md`. Delivery is environment-specific: some environments package the source into an installable file the user downloads, others present the source for review and save it directly. Use the mechanism the current environment provides. The requirement is that the user ends up with the skill installed, not that a file is produced.

---

## Trigger conditions

The skill description is the trigger mechanism. The conditions as of v0.1.0:

- A term is renamed, retired, or redefined
- A section or document is retired
- Content graduates out of any section (Open Question resolved, Hard Lesson metabolized, deferred item closed)
- An edit changes what one document says about another

When adding or changing trigger conditions, update the skill description first. The description is the canonical list.

---

## Source documents

Load this document's sources before editing the skill. They are its branch of the hierarchy in `RFM_map.md`, read upward.

---

## Skill structure

The skill has no `references/` directory. All content is in `SKILL.md`. If the body exceeds 500 lines in a future revision, extract the procedure to `references/procedure.md` and add a pointer in the body.

YAML frontmatter rules:
- Description must be a single quoted string. Multi-line YAML values break validation.
- Keep description between 200-400 characters.
- Front-load "RFM sessions only" in the description for truncation safety.

---

## Retirement of `/ripple-check`

The general `/ripple-check` skill is retired when `rfm-ripple-check` is installed. Steps:

1. Install `rfm-ripple-check`.
2. Remove `/ripple-check` from the user skill directory.
3. Remove R-RIPPLECHECK from `RFM_handover_rules.md`.
4. Bump versions on `RFM_handover_rules.md` and this document.
5. Run `rfm-ripple-check` to confirm no remaining references to the old skill name across RFM documents.

---

## Coverage check: after derivation

Apply the shared coverage check in `RFM_skills_module_operational.md` first. In addition, verify the skill:
- Description front-loads "RFM sessions only"
- Body opens directly on the procedure
- Behavioral constraints section present at the end

---

*skill_rfm_ripple_check_operational // [living]*
*carries what; the reasoning documents carry why*
