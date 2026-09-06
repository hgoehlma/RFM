# Reasoning-First Methodology: Operational Document
`v0.5.0` // `operational` // [living]

---

## File Naming Convention

Documents follow this naming pattern:

`[project]_[type]_[descriptor].md`

`project` is the tag for whichever project is applying the RFM approach. This project's tag is `RFM`, since the project's subject is the methodology itself. A different project applying the RFM approach uses its own tag there instead.

Where `type` is one of:
- `top_level_reasoning`
- `module_reasoning`
- `prompts_reasoning`
- `skill_reasoning`
- `skill_operational`
- `traveling_prompt`
- `sweep_prompt_language`
- `sweep_prompt_structural`
- `sweep_prompt_relational`
- `operational`
- `human_prompt`
- `glossary`
- `map`

Each sweep prompt is named for the cognitive mode it runs in, not for the document type it reads.

Project files drop the version suffix; the file in the project is always current. The version is visible in the document header.

Archive files carry the version suffix: `RFM_prompts_reasoning_v0.0.5.md`

Some artifacts are unique (produced once for a specific purpose with no repeating instances). These follow the same naming pattern but are not listed as reusable types:

- `RFM_first_session_guidance.md`: practical preparation document for a newcomer's first guided drafting session

Execution artifacts (the traveling prompt, sweep prompts, and human prompt) carry a version number in their header only. They do not carry a document type tag or `[living]` marker. These artifacts sit at the end of the derivative chain: they are regenerated from their source reasoning documents, not curated independently. The version number is sufficient to detect drift against the source. A patch-level fix to an execution artifact is legitimate only when the source reasoning document changed first.

---

## Document Map Maintenance

The document map is `RFM_map.md`. It must be updated in the same session as any document version bump. Version numbers in the map must be real, no wildcards.

The README carries orientation for public readers without version numbers. It is not a substitute for the document map.

**The map check.** Run it in any session that changes a document's version, adds a document, or removes one.

Compare every map row's version against the header of the file the row names. Compare the file set against the map in both directions: a document file with no row is a finding, and a row naming no file is a finding. The map does not list itself, so its own file is never a finding.

Read each version from the file itself. A version the session believes it set is not evidence.

Report the check as done only after showing its output.

---

## Content-Derived IDs for Assumptions, Hard Lessons and Open Questions

Assumptions, Hard Lessons, and Open Questions use content-derived IDs rather than positional numbers. Format: `[AS-XXXX]` for Assumptions, `[HL-XXXX]` for Hard Lessons, `[OQ-XXXX]` for Open Questions, where XXXX is a short abbreviation derived from the entry content.

Rules:
- ID is assigned once at capture and never re-derived
- Abbreviation must be recoverable on cold read without session context
- Cross-references use the ID, never the position number
- IDs are unique within their section type within a single document; they do not form a shared registry across documents

---

## Count-Dependent References

Reasoning documents must not contain statements whose correctness depends on a count remaining stable. Four specific forms are excluded:

- Version numbers in cross-document references: the document name is the stable identifier; the document map carries the version snapshot
- Numerical counts of entries (assumptions, options, hard lessons): adding or removing one entry silently invalidates the count
- Cross-document ID references: they imply a shared registry that does not exist and would signal the entry is in the wrong place
- IDs scoped beyond a single document: IDs are per-document only

---

## Version Number Discipline

Version numbers appear in the document header. The header is the single source of version truth. An unbumped header mid-session is expected, not drift. Drift is a header and document map that still disagree after the close-out bump step has run.

Version numbers follow the format vX.X.X (major.minor.patch). The patch digit increments for small edits and language fixes. The minor digit increments for meaningful content additions or structural changes. The major digit increments for fundamental methodology changes.

---

## Empty Section Placeholder Convention

When a section has no entries, use a placeholder rather than leaving it blank. This signals that the section was considered and is genuinely empty, not overlooked.

Standard placeholder: `*No [section name] at this time.*`

Examples: `*No open questions at this time.*` / `*No hard lessons at this time.*`

A blank section is ambiguous. A placeholder is an explicit statement.

---

## Formatting Conventions for Reasoning Documents

These conventions apply to all RFM reasoning documents. They are not methodology; they are the formatting that practice has shown best serves the reasoning each section requires. Newcomers are guided to follow them in their first session. RFM documents follow them as the current best formulation.

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

## Failure Taxonomy

This section is the single source for the failure classes RFM recognizes. Both arms retrieve from here: the sweep prompts through `RFM_sweep_module_operational.md`, and the drafting-moment check through the drafting skill. Neither restates the classes in its own words. Each derives its own questions from them.

**Structural failure types**

- Content at the wrong level of the hierarchy
- Content in the wrong section of a document
- A section straining toward a new module
- Reasoning duplicated across sections of one document
- Reasoning a child module owns still carried by the parent
- An entry ready to graduate or expire

**Language failure types**

- Session-born shorthand that requires the drafting session to be understood
- Insider terminology without a definition or a glossary pointer
- A claim that outruns its evidence without being flagged
- Reasoning compressed to a conclusion without showing the path
- Observation and interpretation conflated in one sentence
- Wording that implies uncertainty that no longer exists
- Curation failures: text that does not earn its place, language written for the session that produced it rather than for a future reader, repetition of reasoning stated elsewhere that adds no signal

**Lifespan failure types**

- A claim conditioned on something already planned, which that plan will make false
- A note or placeholder describing work that a scheduled step will perform

**Boundary between the families.** A failure is structural when it concerns where content sits. A failure is language when it concerns how content reads. A failure is lifespan when the content sits correctly and reads clearly today and planned work will make it false or redundant. A well-written sentence in the wrong section is structural. A correctly placed sentence carrying session residue is language. A correctly placed, clearly written sentence describing a condition already scheduled for removal is lifespan. A conditional whose trigger is uncertain is not a lifespan failure, because no plan holds that condition and the document is the only place it is recorded. When a failure meets more than one description, the artifact that invoked the taxonomy applies its own ordering rule; the sweep ordering is in `RFM_sweep_module_operational.md`.

---

## Graduation and Expiry Procedure

**Graduation**: an entry whose reasoning still has a recipient:
1. Identify the destination: the section and document where a practitioner needs to encounter this reasoning for it to do its work.
2. Draft the resolved reasoning in the destination document and confirm it is complete without the source entry. Complete the destination edit before returning to remove the source entry, one document at a time, in that order.
3. Remove the source entry from its original location.
4. Bump the version of both the destination document and the source document. Update the document map.

Both steps 2 and 3 are required in the same session. An entry resolved but not removed annotates rather than curates.

**Expiry**: an entry whose reasoning no longer has a recipient:
1. Confirm the reasoning would not change how any practitioner thinks or acts anywhere in the current system.
2. Confirm the version history holds the record.
3. Remove the entry.
4. Bump the version of the source document. Update the document map.

The distinction between graduation and expiry is a reasoning act, not a mechanical classification. When the case is genuinely ambiguous, flag it rather than resolve it unilaterally.

---

## Prose Derivative Writing

Text-facing RFM derivatives (public documentation, onboarding guides, worked examples, README files) require two layers of writing discipline applied together. Neither substitutes for the other.

**Layer 1: Write from the reasoning**

RFM prose follows from RFM's epistemic commitments. Apply these directly:

- State the argument first, then support it. Do not build to a conclusion.
- Name uncertainty explicitly. Do not smooth over it.
- When something could fail, say so. Do not lead with aspiration.
- Commit to one defensible position. Do not hedge across multiple alternatives to avoid commitment.

These are not style preferences. They are what RFM reasoning looks like in prose form. A derivative that does not reflect them is not consistent with its source.

**Layer 2: Protect legibility**

LLM-generated text carries recognizable behavioral patterns. Readers detect them (consciously or not) and they undermine the signal the derivative is meant to carry. Suppress the following regardless of how well Layer 1 is applied:

- Uniform paragraph length and sentence rhythm
- Importance inflation: phrases like "a pivotal moment," "it is worth noting," "this underscores"
- Throat-clearing openers: grand statements about the state of the world, restatement of the question just asked
- Structural false contrasts: "It's not X, it's Y" / "Not X, just Y"
- Em dashes: barred entirely. See Em Dash Check.
- Vocabulary tells: "delve," "underscore," "robust," "seamless," "transformative," "holistic," "leverage" (as verb), "comprehensive"
- Rhetorical ramps: announcing an instruction before giving it. "The required act is simple:", "The answer is straightforward:", "What this requires is:" all bury the instruction under an announcement of the instruction. State the action directly.

**Applying both layers**

Draft for Layer 1 first, get the reasoning character right. Then read for Layer 2, remove the patterns that would make the derivative read as machine-generated. A draft that passes Layer 1 but fails Layer 2 has the right content and will not be read. A draft that passes Layer 2 but fails Layer 1 is legible and says nothing worth reading.

## Em Dash Check

Em dashes are barred from every file in the project. Conversation is out of scope.

Anything destined for a file is written without em dashes from the first draft, a draft shown for approval included. A draft approved with em dashes in it becomes a rewrite of content already agreed.

Verify by grep, not by rereading. Write the candidate text to a scratch file outside the project and grep it for the character. The destination document is never the file grepped. Report the check as done only after the grep returns clean.

Replace an em dash with a comma, a period, or a recast sentence. Parentheses are not a substitute. They carry the same tell, and a sweep that used them as the default replacement is recorded as a hard lesson in `RFM_skill_unslop_reasoning.md`.

## Skill Count Working Band

A well-triggered skill is one whose description is written from the vocabulary a practitioner uses at the moment the skill is needed.

Tens of well-triggered skills sit inside the range where selection holds. Low hundreds sit past the point where degradation is reported. Use the band as the starting point when deciding whether a family of related behavior becomes one skill or several, not as a limit to fill up to.

The band is inferred from published tool-selection results and has not been measured on this project. Revise it when better evidence arrives. Why a band is the right form, and why it is likely conservative for this project, is in `RFM_skills_module_reasoning.md`.

---

---

*operational // [living]*
*carries what, the reasoning documents carry why*