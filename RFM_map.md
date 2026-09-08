# Reasoning-First Methodology: Document Map
`v0.6.0` // `top_level_artifact` // [living]

---

## What this document covers

Where every document in RFM sits and what version it currently carries. This is the navigational entry point for the document set. A reader arriving at RFM starts here to find which document to open. `README.md` is the entry point for a reader deciding whether RFM is worth reading at all, and carries no versions.

This document does not list itself. A file cannot record its own version twice without one copy going stale. The reasoning is recorded as a hard lesson in `RFM_top_level_reasoning.md`.

The rules for maintaining this file, including when a version bumps and what a bump requires, live in `RFM_operational.md`.

---

## Hierarchy

A document's sources are its position in this tree read upward: its own reasoning document, its module's documents, then the top level. A document states a source in its own text only where the edge leaves its branch.

```text
RFM
├─ RFM_map.md
├─ RFM_top_level_reasoning.md
├─ RFM_operational.md
├─ RFM_glossary.md
├─ RFM_incubating.md
├─ README.md
├─ examples/
│
├─ Curation module
│  └─ RFM_curation_reasoning.md
│
├─ Instruction design module
│  └─ RFM_instruction_design_reasoning.md
│
├─ Prompts module
│  ├─ RFM_prompts_reasoning.md
│  │
│  ├─ Traveling prompt module
│  │  ├─ RFM_traveling_prompt_reasoning.md
│  │  ├─ RFM_traveling_prompt_operational.md
│  │  └─ RFM_traveling_prompt.md
│  │
│  ├─ Sweep module
│  │  ├─ RFM_sweep_reasoning.md
│  │  ├─ RFM_sweep_operational.md
│  │  ├─ RFM_sweep_prompt_structural.md
│  │  ├─ RFM_sweep_prompt_language.md
│  │  └─ RFM_sweep_prompt_relational.md
│  │
│  ├─ Human prompt module
│  │  ├─ RFM_human_prompt_reasoning.md
│  │  └─ RFM_human_prompt.md
│  │
│  ├─ Guided drafting module
│  │  ├─ RFM_guided_drafting_prompt_reasoning.md
│  │  ├─ RFM_guided_drafting_prompt_operational.md
│  │  ├─ RFM_guided_drafting_prompt.md
│  │  └─ RFM_first_session_guidance.md
│  │
│  └─ Derivation module
│     ├─ RFM_derivation_prompt_reasoning.md
│     ├─ RFM_derivation_prompt_operational.md
│     ├─ RFM_derivation_prompt.md
│     └─ RFM_derivation_session_guidance.md
│
└─ Skill design module
   ├─ RFM_skill_design_reasoning.md
   ├─ RFM_skill_design_operational.md
   │
   ├─ rfm-unslop skill module
   │  ├─ RFM_skill_unslop_reasoning.md
   │  └─ RFM_skill_unslop_operational.md
   │
   ├─ rfm-ripple-check skill module
   │  ├─ RFM_skill_ripple_check_reasoning.md
   │  └─ RFM_skill_ripple_check_operational.md
   │
   └─ rfm-drafting skill module
      ├─ RFM_skill_drafting_reasoning.md
      └─ RFM_skill_drafting_operational.md
```

`RFM_map.md` appears in the tree because the tree states position and the map has one. It carries no row in the table below because that would be a second copy of its own version.

---

## Document Map

| Document | Type | Version | What it carries |
|---|---|---|---|
| `RFM_top_level_reasoning.md` | `top_level_reasoning` | v0.15.0 | The problem, assumptions, landscape, chosen direction, boundaries, open questions and hard lessons governing the methodology as a whole |
| `RFM_operational.md` | `top_level_operational` | v0.8.1 | File naming conventions, document map maintenance and the map check, the header convention, version discipline, and the failure taxonomy both sweep arms and the drafting pre-check retrieve from |
| `RFM_glossary.md` | `top_level_artifact` | v0.1.6 | Disambiguation of terms that carry different meanings across reader contexts |
| `RFM_curation_reasoning.md` | `module_reasoning` | v0.1.0 | The reasoning document governing curation: what keeps a document true after the session that wrote it, and why its failures are invisible from inside that session |
| `RFM_instruction_design_reasoning.md` | `module_reasoning` | v0.5.0 | The reasoning document governing how an instruction is shaped, where it is placed, and whether anything checks it |
| `RFM_prompts_reasoning.md` | `module_reasoning` | v0.3.0 | The reasoning document governing all system prompt decisions |
| `RFM_traveling_prompt_reasoning.md` | `module_reasoning` | v0.2.1 | The reasoning document governing traveling prompt design decisions |
| `RFM_traveling_prompt_operational.md` | `module_operational` | v0.2.0 | Derivation procedure and coverage check discipline for the traveling prompt |
| `RFM_traveling_prompt.md` | `module_artifact` | v0.3.6 | The system prompt that carries the methodology into every LLM conversation |
| `RFM_sweep_reasoning.md` | `module_reasoning` | v0.5.0 | The reasoning document governing sweep prompt design decisions |
| `RFM_sweep_operational.md` | `module_operational` | v0.6.0 | Language and structural catalogs, grey zone rule, source documents, coverage check, and version discipline for the sweep prompts |
| `RFM_sweep_prompt_structural.md` | `module_artifact` | v0.5.1 | The prompt artifact that activates the structural sweep: findings for ruling, not edits |
| `RFM_sweep_prompt_language.md` | `module_artifact` | v0.2.1 | The prompt artifact that activates the language sweep: findings for ruling, not edits |
| `RFM_sweep_prompt_relational.md` | `module_artifact` | v0.3.0 | The prompt artifact that activates the relational sweep: boundary check between a reasoning document and its operational derivative, findings for ruling, not edits |
| `RFM_human_prompt_reasoning.md` | `module_reasoning` | v0.1.2 | Reasoning document governing human prompt design decisions |
| `RFM_human_prompt.md` | `module_artifact` | v0.1.2 | The prompt artifact for the human collaborator: practices that keep the co-author role alive across sessions |
| `RFM_guided_drafting_prompt_reasoning.md` | `module_reasoning` | v0.1.1 | Reasoning document governing guided drafting prompt design decisions |
| `RFM_guided_drafting_prompt_operational.md` | `module_operational` | v0.1.1 | Deployment and artifact inventory for the guided drafting prompt module |
| `RFM_guided_drafting_prompt.md` | `module_artifact` | v0.1.1 | The prompt artifact that activates the guided drafting session: behavioral specification for the LLM, section intentions for the newcomer |
| `RFM_first_session_guidance.md` | `module_artifact` | v0.1.3 | Practical preparation for a newcomer's first guided drafting session: what to bring, what to expect, what to watch for |
| `RFM_derivation_prompt_reasoning.md` | `module_reasoning` | v0.5.0 | The reasoning document governing derivation prompt design decisions |
| `RFM_derivation_prompt_operational.md` | `module_operational` | v0.3.0 | Invocation procedure, confirmation gate, and versioning discipline for the derivation prompt |
| `RFM_derivation_prompt.md` | `module_artifact` | v0.2.1 | The system prompt that governs autonomous LLM execution from completed RFM reasoning documents |
| `RFM_derivation_session_guidance.md` | `module_artifact` | v0.1.2 | Practical preparation for a phase two derivation session: what to confirm, what to expect, the one step that must not be skipped |
| `RFM_skill_unslop_reasoning.md` | `skill_reasoning` | v0.3.2 | Reasoning document governing the rfm-unslop skill: why always-on, why one skill with register awareness, why the session is the entry point |
| `RFM_skill_unslop_operational.md` | `skill_operational` | v0.3.2 | Derivation procedure, traveling prompt declaration, and pattern list maintenance for the rfm-unslop skill |
| `RFM_skill_ripple_check_reasoning.md` | `skill_reasoning` | v0.1.4 | Reasoning document governing the rfm-ripple-check skill: why RFM-specific, why graduation is a trigger condition, why the general ripple-check skill is retired |
| `RFM_skill_ripple_check_operational.md` | `skill_operational` | v0.3.2 | Derivation procedure and retirement steps for the rfm-ripple-check skill |
| `RFM_skill_drafting_reasoning.md` | `skill_reasoning` | v0.4.2 | Reasoning document governing the rfm-drafting skill: why a skill rather than operational doc guidance, why glossary entries are in scope |
| `RFM_skill_drafting_operational.md` | `skill_operational` | v0.6.1 | Derivation procedure, pre-check specification, and skill body maintenance for the rfm-drafting skill |
| `RFM_skill_design_reasoning.md` | `module_reasoning` | v0.5.1 | The reasoning document governing skill design decisions across skills |
| `RFM_skill_design_operational.md` | `module_operational` | v0.1.3 | Shared derivation rules for all RFM skills: delivery, skill structure, frontmatter rules, and shared coverage check |
| `README.md` | `top_level_artifact` | unversioned | Public-facing orientation for a reader encountering RFM for the first time, carrying no version numbers by design |
| `RFM_incubating.md` | `top_level_artifact` | unversioned | Ideas captured at session close that are not yet ready to enter a document |
| `examples/` |  | unversioned | Reasoning documents from projects using RFM, kept as worked examples |
