# Reasoning-First Methodology: RFM Unslop Skill Operational Document
`v0.3.1` // `skill_unslop_operational` // [living]

---

## What this document covers

Derivation procedure for the `rfm-unslop` skill and the traveling prompt declaration that activates it. The reasoning behind every decision here is in `RFM_skill_unslop_reasoning.md`. Rules shared by all RFM skills are in `RFM_skills_module_operational.md`. This document carries what is specific to `rfm-unslop`.

---

## The artifact

The `rfm-unslop` skill, installed and active in the user's environment.

The skill source is `rfm-unslop/SKILL.md`. Delivery is environment-specific: some environments package the source into an installable file the user downloads, others present the source for review and save it directly. Use the mechanism the current environment provides. The requirement is that the user ends up with the skill installed, not that a file is produced.

---

## Traveling prompt declaration

The traveling prompt must carry this line in the Identity section, immediately after the source/derivative statement:

> This is a project using the RFM approach. Apply the `rfm-unslop` skill to every response you produce in this session.

This declaration is the trigger mechanism. Without it, the skill does not fire. Any project using the RFM approach and loading the traveling prompt inherits the declaration.

---

## Source documents

Load this document's sources before editing the skill. They are its branch of the hierarchy in `RFM_map.md`, read upward.

---

## Skill structure

The skill has no `references/` directory. All content is in `SKILL.md`. If the body exceeds 500 lines in a future revision, extract the pattern list to `references/patterns.md` and add a pointer in the body.

YAML frontmatter rules:
- Description must be a single quoted string. Multi-line YAML values break validation.
- Keep description between 200-400 characters.
- Front-load "RFM approach" in the description for truncation safety.

---

## Pattern list maintenance

The pattern list in the skill body is the canonical list of slop patterns for RFM sessions. When a new pattern is identified in practice:

1. Add it to the skill body under the appropriate position in the list.
2. Update `RFM_skill_unslop_reasoning.md` if the new pattern reflects a reasoning change (new assumption, new hard lesson).
3. Reinstall the updated skill in the user's environment.
4. Bump the version on this operational document. Skills carry no version number.

When a pattern is retired:
1. Remove it from the skill body.
2. Record why in Hard Lessons if the retirement reflects a lesson.
3. Reinstall the updated skill and bump the version on this operational document.

---

## Register rules maintenance

The register-specific rules at the bottom of the skill body are a separate section from the pattern list. They govern threshold and remediation, not pattern detection. Edit them independently of the pattern list when register behavior changes.

---

## Coverage check: after derivation

Apply the shared coverage check in `RFM_skills_module_operational.md` first. In addition, verify the skill:
- Description front-loads "RFM approach"
- Body opens directly on the pattern list
- Register rules section present at the end

Verify the traveling prompt:
- Declaration line present in Identity section
- Version bumped

---

*skill_unslop_operational // [living]*
*carries what; the reasoning documents carry why*
