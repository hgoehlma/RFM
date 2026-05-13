# Reasoning-First Methodology (RFM)

Every complex system has the same failure: the thinking disappears. What remains is code, output, or structure — but the reasoning that shaped it, the alternatives that were rejected, the assumptions that were made — that is gone. Humans who come later must reconstruct it. LLMs working within it hallucinate because the context they needed was never recorded.

RFM places the reasoning document at the center. Not the code. Not the output. The reasoning — explicit, hierarchical, curated, and designed simultaneously for human understanding and LLM execution.

Every change to a system begins with a change to the reasoning document at the appropriate level. Code is the derivative. The document is the source.

If you've ever inherited a codebase and had no idea why anything was built the way it was — or watched an LLM confidently reconstruct intent it never had — this is for that. The problem is not unique to software. But software is where it hurts most visibly.

---

## The Core Idea

A reasoning document is a structured, living artifact with eight sections: The Problem, The Assumptions, The Landscape, The Options Considered, The Chosen Direction and Why, The Boundaries, The Open Questions, and Hard Lessons.

The same eight sections apply at every level of the hierarchy — from top-level methodology to individual module — with different scope but identical discipline. Think of a country map and a street map: different resolution, same navigational rules, and they connect. This property — the same structure governing at every level — is what mathematicians call fractal. The term is precise: a fractal is not just a pattern that repeats, it is a pattern whose rules apply at every level. That is exactly what the reasoning document hierarchy is.

The LLM is a co-author in this practice, not a tool that executes within it — which means it is expected to red team, flag drift, and hold the discipline alongside the human, not wait to be asked. The methodology applies to itself: these documents were built in true collaboration between human and LLM using RFM principles, with the reasoning coming before the structure. That was the right order.

---

## Two Modes

The methodology operates in two modes. Reasoning mode is the default: the reasoning document precedes execution, every change begins at the appropriate level of the hierarchy. Execution mode is the correct response to delivery pressure — a deadline, a sprint, a time-boxed commitment — when reasoning documents are sufficiently established. The discipline shifts from reasoning before every action to executing within established reasoning, using those documents as Commander's Intent. What execution mode requires is minimal capture: deviations, deferrals, and broken assumptions logged as they happen, enough to make the return to reasoning mode honest rather than reconstructed from code. The return is not optional.

---

## Where To Start

If you are encountering RFM for the first time:

1. [`RFM_top_level_reasoning.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_top_level_reasoning.md) — the methodology itself. Start here.
2. [`RFM_first_session_guidance.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_first_session_guidance.md) — practical preparation for your first guided drafting session.

That is enough to begin. The rest of the document landscape is for collaborators maintaining and extending the methodology — you will find your way into it naturally once you have produced your first reasoning document.

## System Documents

For collaborators working within the methodology:

| Document | What it carries |
|---|---|
| [`RFM_top_level_reasoning.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_top_level_reasoning.md) | The methodology itself — problem, assumptions, landscape, chosen direction, hard lessons |
| [`RFM_human_prompt.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_human_prompt.md) | Practices that keep the human's collaborative posture alive across sessions |
| [`RFM_traveling_prompt.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_traveling_prompt.md) | The system prompt that carries the methodology into every LLM conversation |
| [`RFM_guided_drafting_prompt.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_guided_drafting_prompt.md) | The prompt that activates a guided first-document session |
| [`RFM_sweep_prompt_structural.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_sweep_prompt_structural.md) | Structural sweep — findings for ruling, not edits |
| [`RFM_sweep_prompt_language.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_sweep_prompt_language.md) | Language sweep — findings for ruling, not edits |
| [`RFM_glossary.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_glossary.md) | Disambiguation of terms that carry RFM-specific meanings |
| [`RFM_operational.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_operational.md) | File naming, version discipline, ID conventions |

Reasoning documents for each artifact are in the repository — named `RFM_[artifact]_reasoning.md`. They carry the why behind every design decision.

---

## State

This methodology is in active development. All documents are living artifacts, versioned and curated.

The abbreviation RFM is not accidental. Those who recognize the older acronym will understand immediately what this methodology thinks you should do before touching anything.

RFM is a vehicle, not a prescription. The reasoning comes first — everything else is yours to design for your domain, your team, and your discipline.

---

## Why It Matters Now

Context engineering has become the defining AI skill of 2025–2026 — the discipline of assembling everything a model needs to act: documents, memory, tools, state. It is the right frame. But it answers the wrong question first. It asks: what information does the model need? RFM asks first: what reasoning produced that information, and does it still hold?

A model working from well-assembled context but poorly-reasoned documents doesn't fail cautiously. It executes confidently on assumptions that were never examined, alternatives that were never named, and decisions whose reasoning disappeared the moment they were made. Context engineering without reasoning capture is infrastructure without content.

The agentic shift makes this more urgent, not less. As AI systems act autonomously across longer chains — planning, executing, adjusting without human oversight at each step — the reasoning document becomes the only reliable mechanism for keeping human intent legible to the systems executing it. A capable agent acting on vague intent fails at scale, and the failure is hard to trace. The reasoning document is the deterministic anchor. Explicit reasoning before autonomous execution is not overhead. It is the only thing that makes the execution accountable.

---

## License

[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

© 2026 Hinrich W.H. Göhlmann

*Developed in collaboration with Claude Sonnet 4.6 (Anthropic), acting as co-author throughout.*
