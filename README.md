# Reasoning-First Methodology (RFM)

Every complex system has the same failure: the thinking disappears. What remains is code, output, or structure — but the reasoning that shaped it, the alternatives that were rejected, the assumptions that were made — that is gone. Humans who come later must reconstruct it. And anyone — human or AI — working within it without that context is guessing.

RFM places the reasoning document at the center. Not the code. Not the output. The reasoning — explicit, hierarchical, curated — designed to survive beyond the people and sessions that produced it — so that returning to it six months later, or bringing in a new collaborator, doesn't mean starting from scratch.

Every change to a system begins with a change to the reasoning document at the appropriate level. The document is the source. Everything else follows from them.

If you've ever joined a project and had no idea why anything was built the way it was — or watched a decision get made again from scratch because no one recorded why it was made the first time — this is for that. The problem is not unique to software. But software is where it hurts most visibly.

---

## The Core Idea

A reasoning document is a structured, living artifact with eight sections: The Problem, The Assumptions, The Landscape, The Options Considered, The Chosen Direction and Why, The Boundaries, The Open Questions, and Hard Lessons.

The same eight sections apply at every level of the hierarchy — from top-level methodology to individual module — with different scope but identical discipline. Think of a country map and a street map: different resolution, same navigational rules, and they connect. This property — the same structure governing at every level — is what mathematicians call fractal. The term is precise: a fractal is not just a pattern that repeats, it is a pattern whose rules apply at every level. That is exactly what the reasoning document hierarchy is.

The AI is a co-author in this practice, not a tool that executes within it — which means it is expected to challenge weak thinking, notice when something is off, and hold the discipline alongside the human, not wait to be asked. The methodology applies to itself: these documents were built in true collaboration between human and AI using RFM principles, with the reasoning coming before the structure. That was the right order.

One honest caveat: AI systems are trained to be agreeable, and that tendency does not disappear because you instruct them otherwise. RFM designs for this directly — the reasoning document holds the position even when the AI would soften it, and the human's active role in the collaboration is a designed practice, not a constant struggle.

---

## Two Modes

The methodology operates in two modes. Reasoning mode is the default: the reasoning document precedes execution, every change begins at the appropriate level of the hierarchy. Execution mode is the correct response to delivery pressure — a deadline, a time-boxed commitment — when reasoning documents are sufficiently established. The discipline shifts from reasoning before every action to executing within established reasoning, using those documents as the fixed reference point. What execution mode requires is minimal capture: deviations, deferrals, and broken assumptions noted as they happen, enough to make the return to reasoning mode honest rather than reconstructed after the fact. The return is not optional.

---

## Where To Start

If you are encountering RFM for the first time:

1. [`RFM_top_level_reasoning.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_top_level_reasoning.md) — the methodology itself. Start here.
2. [`RFM_first_session_guidance.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_first_session_guidance.md) — practical preparation for producing your first reasoning document.

That is enough to begin. The rest of the document landscape is for collaborators maintaining and extending the methodology — you will find your way into it naturally once you have produced your first reasoning document.

## System Documents

For collaborators working within the methodology:

| Document | What it carries |
|---|---|
| [`RFM_top_level_reasoning.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_top_level_reasoning.md) | The methodology itself — problem, assumptions, landscape, chosen direction, hard lessons |
| [`RFM_human_prompt.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_human_prompt.md) | Practices that keep the human's collaborative posture alive across sessions |
| [`RFM_traveling_prompt.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_traveling_prompt.md) | The system prompt that carries the methodology into every LLM conversation |
| [`RFM_guided_drafting_prompt.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_guided_drafting_prompt.md) | The prompt that activates a guided first-document session |
| [`RFM_sweep_prompt_structural.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_sweep_prompt_structural.md) | Structural review — findings for ruling, not edits |
| [`RFM_sweep_prompt_language.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_sweep_prompt_language.md) | Language review — findings for ruling, not edits |
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

The way people work with AI is changing fast — and the dominant focus is on assembling everything a model needs to act well: the right documents, the right context, the right instructions. That is the right instinct. But it answers the wrong question first. It asks: what does the AI need? RFM asks first: was the reasoning behind that actually worked through — thoroughly, from multiple angles, before anything was built?

A model working from well-assembled context but poorly-reasoned documents doesn't fail cautiously. It executes confidently on assumptions that were never examined, alternatives that were never named, and decisions whose reasoning disappeared the moment they were made.

The agentic shift makes this more urgent, not less. As AI systems act autonomously across longer chains — planning, executing, adjusting without human oversight at each step — the reasoning document becomes the only reliable mechanism for keeping human intent legible to the systems executing it. A capable agent acting on vague intent fails at scale, and the failure is hard to trace. Explicit reasoning before autonomous execution is not overhead. It is the only thing that makes the execution accountable.

---

## License

[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

© 2026 Hinrich W.H. Göhlmann

*Developed in collaboration with Claude Sonnet 4.6 (Anthropic), acting as co-author throughout.*
