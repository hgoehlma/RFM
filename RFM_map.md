# RFM: Map

Where each RFM document sits in the hierarchy, what it is, and whether it goes into a practitioner's project. A document's version is in its header. `README.md` is the entry point for someone deciding whether RFM is worth reading.

## Hierarchy

A document's sources are its position in this tree, read upward.

```text
RFM
├─ RFM_map.md
├─ RFM_top_level_reasoning.md
├─ RFM_top_level_operational.md
├─ RFM_glossary.md
├─ RFM_human_guide.md
├─ README.md
├─ RFM_setup_guide.md
├─ examples/
│
└─ Carriers module
   ├─ RFM_carriers_reasoning.md
   ├─ RFM_carriers_operational.md
   ├─ RFM_behaviors.md
   ├─ RFM_carrier_types.md
   ├─ rfm_write_hook.py
   ├─ settings.json
   ├─ hooks.json
   │
   ├─ Always-on module
   │  ├─ RFM_always_on_reasoning.md
   │  ├─ AGENTS.md
   │  └─ CLAUDE.md
   │
   ├─ Session loop module
   │  ├─ RFM_session_loop_reasoning.md
   │  ├─ rfm-open
   │  └─ rfm-close
   │
   ├─ Sweeps module
   │  ├─ RFM_sweeps_reasoning.md
   │  ├─ RFM_sweeps_operational.md
   │  ├─ rfm-structural-sweep
   │  ├─ rfm-language-sweep
   │  └─ rfm-cross-document-sweep
   │
   ├─ Research check module
   │  ├─ RFM_research_check_reasoning.md
   │  ├─ RFM_research_check_operational.md
   │  └─ rfm-research-check
   │
   ├─ Drafting skill module
   │  ├─ RFM_drafting_skill_reasoning.md
   │  ├─ RFM_drafting_skill_operational.md
   │  └─ rfm-drafting
   │
   ├─ Unslop skill module
   │  ├─ RFM_unslop_skill_reasoning.md
   │  ├─ RFM_unslop_skill_operational.md
   │  └─ rfm-unslop
   │
   ├─ Curation skill module
   │  ├─ RFM_curation_skill_reasoning.md
   │  └─ rfm-curation
   │
   ├─ Derivation skill module
   │  ├─ RFM_derivation_skill_reasoning.md
   │  └─ rfm-derive
   │
   ├─ File-write skill module
   │  ├─ RFM_file_write_skill_reasoning.md
   │  └─ rfm-file-write
   │
   ├─ Fresh-read skill module
   │  ├─ RFM_fresh_read_skill_reasoning.md
   │  └─ rfm-fresh-read
   │
   └─ Rename skill module
      ├─ RFM_rename_skill_reasoning.md
      └─ rfm-rename
```

## What goes into a project

These go into a practitioner's project. Everything else in the tree stays in RFM's public repository.

| File | What it is |
|---|---|
| `AGENTS.md` | The always-on instructions, sent in every session. Codex reads this file directly. |
| `CLAUDE.md` | Holds only `@AGENTS.md`, so Claude Code loads the same text. |
| The `rfm-` skills | The skills the LLM or the human loads at their moments. One real copy in `.claude/skills/`, linked from `.agents/skills/`. |
| `rfm_write_hook.py` | In `.rfm/hooks/`, where Claude Code and Codex both run it. Stops text going into a document before it has been shown. Derived from the carriers operational document; change it there first. |
| `settings.json` | In `.claude/`. Registers the hook and turns the app's memory off. Changes are made here. |
| `hooks.json` | In `.codex/`. Registers the hook for Codex. It finds the script by searching upward, so it works when Codex is opened on a subfolder. After a change, Codex skips the hook until it is approved again. |
| `RFM_human_guide.md` | The human's side of the practice. |
| `RFM_glossary.md` | Terms a reader could take the wrong way. |
| `RFM_top_level_reasoning.md` | Why RFM is the way it is. |
| `RFM_top_level_operational.md` | How documents are written: sections, formats, filenames and headers. |

## What stays in the repository

| File | What it is |
|---|---|
| `README.md` | First contact for someone new to RFM. |
| `RFM_setup_guide.md` | How a newcomer's first session is set up and where each file sits. Changes are made here. |
| `RFM_behaviors.md` | The inventory of behaviors RFM wants, the failures they counter and what carries each. Changes are made here. |
| `RFM_carrier_types.md` | The toolbox of ways to bring a behavior about, gone back to when a model or an app changes. Changes are made here. |
| Reasoning and operational documents below the top level | Why each carrier is the way it is, and how it runs. |
| `examples/` | Projects that used RFM, written in an earlier form of it. |
