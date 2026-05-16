# Reasoning-First Methodology — Operational Document
`v0.0.0.6` // `operational` // [living]

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

Some artifacts are unique — produced once for a specific purpose with no repeating instances. These follow the same naming pattern but are not listed as reusable types:

- `RFM_first_session_guidance.md` — practical preparation document for a newcomer's first guided drafting session

---

## Document Map Maintenance

The document map lives at the top of `RFM_top_level_reasoning.md`. It must be updated in the same session as any document version bump. Version numbers in the map must be real — no wildcards.

The README carries orientation for public readers without version numbers. It is not a substitute for the document map.

---

## Content-Derived IDs for Assumptions, Hard Lessons and Open Questions

Assumptions, Hard Lessons, and Open Questions use content-derived IDs rather than positional numbers. Format: `[AS-XXXX]` for Assumptions, `[HL-XXXX]` for Hard Lessons, `[OQ-XXXX]` for Open Questions, where XXXX is a short abbreviation derived from the entry content.

Rules:
- ID is assigned once at capture and never re-derived
- Abbreviation must be recoverable on cold read without session context
- Cross-references use the ID, never the position number
- IDs are unique within their section type across all documents

---

## Version Number Discipline

Version numbers appear in two places in every reasoning document: the header and the footer. Both must be bumped together in the same edit. A document where header and footer versions disagree is already drifting.

---

## Empty Section Placeholder Convention

When a section has no entries, use a placeholder rather than leaving it blank. This signals that the section was considered and is genuinely empty — not overlooked.

Standard placeholder: `*No [section name] at this time.*`

Examples: `*No open questions at this time.*` / `*No hard lessons at this time.*`

A blank section is ambiguous. A placeholder is an explicit statement.

---

## Formatting Conventions for Reasoning Documents

These conventions apply to all RFM reasoning documents. They are not methodology — they are the formatting that practice has shown best serves the reasoning each section requires. Newcomers are guided to follow them in their first session. RFM documents follow them as the current best formulation.

**The Problem**
Plain prose. Bold subheading only when a structurally distinct second argument would otherwise read as continuation of the first.

**The Assumptions**
`**[AS-XXXX] -**` bold claim, body follows in the same paragraph. Hyphen after the ID, not em dash. Grouping sentence permitted when assumptions genuinely divide into distinct registers.

**The Landscape**
One intro sentence naming the specific question this landscape must answer. Table with three columns: Approach | What it does | Why it's insufficient. Closing paragraph opened with **The gap:** in bold.

**The Options Considered**
`**1. X vs. Y**` as bold title, prose body including the rejection reasoning. Each option self-contained.

**The Chosen Direction and Why**
`**Why X**` or `**Why X over Y**` as bold subheading per entry, prose body. No IDs. No numbering.

**The Boundaries**
`**Not X.**` as bold lead phrase, prose body in same paragraph. No IDs. No numbering.

**The Open Questions**
`**[OQ-XXXX] Title of the question.**` as bold line, prose body as separate paragraph below.

**The Hard Lessons**
`**[HL-XXXX] Title.**` as bold line, prose body as separate paragraph below. Category subheadings permitted when lesson count warrants grouping.

---

*operational // [living]*
*carries what — the reasoning documents carry why*