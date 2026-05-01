# Reasoning-First Methodology — Operational Document
`v0.0.0.1` // `operational` // [living]

---

## File Naming Convention

RFM documents follow this naming pattern:

`RFM_[type]_[descriptor].md`

Where `type` is one of:
- `top_level_reasoning`
- `module_reasoning`
- `prompts_reasoning`
- `traveling_prompt`
- `sweep_prompt_language`
- `sweep_prompt_structural`
- `operational`
- `human_prompt` (anticipated)

Project files drop the version suffix — the file in the project is always current. The version is visible in the document header.

Archive files carry the version suffix: `RFM_prompts_reasoning_v0.0.0.5.md`

---

## Document Map Maintenance

The document map lives at the top of `RFM_top_level_reasoning.md`. It must be updated in the same session as any document version bump. Version numbers in the map must be real — no wildcards.

The README carries orientation for public readers without version numbers. It is not a substitute for the document map.

---

## Version Number Discipline

Version numbers appear in two places in every reasoning document: the header and the footer. Both must be bumped together in the same edit. A document where header and footer versions disagree is already drifting.

---

*v0.0.0.1 // operational // [living]*
*carries what — the reasoning documents carry why*