# Reasoning-First Methodology: Skills Module Operational Document
`v0.1.1` // `module_operational` // `[living]`

---

## What this document covers

Shared derivation rules for all RFM skills. The reasoning behind every decision here is in `RFM_skills_module_reasoning.md`. Each skill operational document carries what is specific to that skill and references this document for what is shared.

---

## Delivery

The skill source is `[skill-name]/SKILL.md`. Delivery is environment-specific: some environments package the source into an installable file the user downloads, others present the source for review and save it directly. Use the mechanism the current environment provides. The requirement is that the user ends up with the skill installed, not that a file is produced.

---

## Skill structure

The skill has no `references/` directory. All content is in `SKILL.md`. If the body exceeds 500 lines in a future revision, extract the appropriate section to a `references/` subdirectory and add a pointer in the body. The extracted file name is decided by what the body contains at that point.

---

## Frontmatter rules

- Description must be a single quoted string. Multi-line YAML values break validation.
- Keep description between 200 and 400 characters.
- Front-load the scope phrase in the description. The scope phrase is the narrowest term that describes who should use this skill. Place it first for truncation safety.

---

## Coverage check: after derivation or revision

Each skill operational document may add skill-specific items after this list.

- Frontmatter validates without error.
- Description is a single line, 200 to 400 characters, scope phrase appears first.
- Body opens directly on content, no preamble.

---

*module_operational // [living]*
*carries what; the reasoning documents carry why*
