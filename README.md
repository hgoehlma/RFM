# Reasoning-First Methodology (RFM)

Every complex system has the same failure: the thinking disappears. What remains is code, output, or structure — but the reasoning that shaped it, the alternatives that were rejected, the assumptions that were made — that is gone. Humans who come later must reconstruct it. LLMs working within it hallucinate because the context they needed was never recorded.

RFM places the reasoning document at the center. Not the code. Not the output. The reasoning — explicit, hierarchical, curated, and designed simultaneously for human understanding and LLM execution.

Every change to a system begins with a change to the reasoning document at the appropriate level. Code is the derivative. The document is the source.

If you've ever inherited a codebase and had no idea why anything was built the way it was — or watched an LLM confidently reconstruct intent it never had — this is for that. The problem is not unique to software. But software is where it hurts most visibly.

---

## The Core Idea

A reasoning document is a structured, living artifact with eight sections: The Problem, The Assumptions, The Landscape, The Options Considered, The Chosen Direction and Why, The Boundaries, The Open Questions, and Hard Lessons.

The same eight sections apply at every level of the hierarchy — from top-level methodology to individual module — with different scope but identical discipline. Think of a country map and a street map: different resolution, same navigational rules, and they connect. Zoom in and the practice is identical. This property — the same structure governing at every level — is what makes the hierarchy navigable rather than just large.

The methodology applies to itself. These documents were built using RFM principles, in active collaboration between human and LLM as co-authors. The reasoning came before the structure. That was the right order.

---

## Document Map

| Document | Type | What it carries |
|---|---|---|
| [RFM_top_level_reasoning.md](RFM_top_level_reasoning.md) | Top-level reasoning | The methodology itself — the problem, the assumptions, the landscape, the chosen direction, the hard lessons earned |
| [RFM_prompts_reasoning.md](RFM_prompts_reasoning.md) | Prompts reasoning | The reasoning document governing all system prompt decisions — why the prompt is designed the way it is |
| [RFM_traveling_prompt.md](RFM_traveling_prompt.md) | Traveling system prompt | The system prompt that carries the methodology into every LLM conversation — the discipline made ambient |

*Start with `RFM_top_level_reasoning.md`. It is the map, the anchor, and the most complete entry point into the methodology.*

---

## State

This methodology is in active development. All documents are living artifacts, versioned and curated.

The abbreviation RFM is not accidental. Those who recognize the older acronym will understand immediately what this methodology thinks you should do before touching anything.

---

## License

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

© 2026 Hinrich W.H. Göhlmann

*Developed in collaboration with Claude Sonnet 4.6 (Anthropic), acting as co-author throughout.*

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
