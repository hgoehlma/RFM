# Reasoning-First Methodology — Operational Document
`v0.1.2` // `operational` // [living]

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
- `human_prompt`
- `glossary`

Project files drop the version suffix — the file in the project is always current. The version is visible in the document header.

Archive files carry the version suffix: `RFM_prompts_reasoning_v0.0.5.md`

Some artifacts are unique — produced once for a specific purpose with no repeating instances. These follow the same naming pattern but are not listed as reusable types:

- `RFM_first_session_guidance.md` — practical preparation document for a newcomer's first guided drafting session

Execution artifacts — the traveling prompt, sweep prompts, and human prompt — carry a version number in their header only. They do not carry a document type tag or `[living]` marker. These artifacts sit at the end of the derivative chain: they are regenerated from their source reasoning documents, not curated independently. The version number is sufficient to detect drift against the source.

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

Version numbers appear in the document header. The header is the single source of version truth. A document where the header version has not been bumped after an edit is already drifting.

Version numbers follow the format vX.X.X — major.minor.patch. The patch digit increments for small edits and language fixes. The minor digit increments for meaningful content additions or structural changes. The major digit increments for fundamental methodology changes.

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

## Graduation and Expiry Procedure

**Graduation** — an entry whose reasoning still has a recipient:
1. Identify the destination: the section and document where a practitioner needs to encounter this reasoning for it to do its work.
2. Draft the resolved reasoning in the destination document and confirm it is complete without the source entry. Complete the destination edit before returning to remove the source entry — one document at a time, in that order.
3. Remove the source entry from its original location.
4. Bump the version of both the destination document and the source document. Update the document map.

Both steps 2 and 3 are required in the same session. An entry resolved but not removed annotates rather than curates.

**Expiry** — an entry whose reasoning no longer has a recipient:
1. Confirm the reasoning would not change how any practitioner thinks or acts anywhere in the current system.
2. Confirm the version history holds the record.
3. Remove the entry.
4. Bump the version of the source document. Update the document map.

The distinction between graduation and expiry is a reasoning act, not a mechanical classification. When the case is genuinely ambiguous, flag it rather than resolve it unilaterally.

---

*operational // [living]*
*carries what — the reasoning documents carry why*