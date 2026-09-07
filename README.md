<p align="center">
  <img src="./assets/RFM.png" width="80">
</p>

# Reasoning-First Methodology (RFM)

Every complex project fails the same way: the thinking disappears.

What survives is documents, notes, code, software, etc. But the alternatives that someone rejected at some point, the assumptions that people worked from, the reason a decision was taken one way and not the other are rarely visible. People who join a project later need to reconstruct it or hope that someone with the right knowledge is still around. Anyone working on the content of the project / system without that information is often guessing.

RFM puts the reasoning document at the center and treats it as the source. Any digital output (e.g., code / slide decks / business plans) is derived from it. The reasoning document is explicit and actively curated, arranged in a hierarchy, and written in such a way that people can come back to it after six months or can hand the project to someone new who will not have to start over.

Therefore every change begins with a change to the reasoning document at the appropriate level.

In other words: we start with the why. The why as intent. Reasoning why something is done. Operational documents hold the what and the how. They cover specifications and the variables that are needed to fulfil the why.

If you have ever joined a project and had no idea why anything was built the way it was or if you ever watched a team reconstruct a decision from scratch because nobody wrote down why they made it to begin with, this may be for you. Peter Naur diagnosed the problem in 1985. He did not offer a structural solution. This is ours.

---

## The core idea

A reasoning document has eight sections: The Problem, The Assumptions, The Landscape, The Options Considered, The Chosen Direction and Why, The Boundaries, The Open Questions, Hard Lessons.

The same eight sections apply at every level, from the methodology as a whole down to a single module. While the scope and the content change over time, the discipline does not. You can compare it with a country map and a street map. They differ in resolution but they follow the same navigational rules and they still connect to each other.

Mathematicians call such a structure fractal. A fractal's defining property is that its rules hold at every magnification. This is exactly the idea for the sections of a reasoning document.

### The role of a Large Language Model

The LLM works as a co-author. It challenges weak thinking, says when something is off, and holds the discipline without being asked each time. RFM was built exactly this way. Human and AI working together and reasoning first before deciding on the structure and the approach.

And this raises an obvious objection: LLMs are trained to agree. When you instruct an LLM to push back you cannot undo how the LLM was trained. RFM attempts to handle this structurally: the reasoning document holds a position the AI would otherwise weaken and the human's side of the collaboration is specified as a practice defined in a "human prompt".

---

## The two phases

Phase one: human and LLM build the reasoning documents together. They jointly work through the problem, the assumptions, the landscape, the options, and so on. Each brings strengths the other lacks.

Phase two: the finished documents become the source from which the LLM derives the digital output(s). Code, operational documents, business strategy, whatever a particular domain needs. This output is generated without the human.

Therefore the output of phase two depends on how well the documents of phase one were reasoned and specified.

---

## Two modes

The reasoning mode is the default setting. The document drafting, refining, and curation precedes execution. Every change starts with the corresponding document at the appropriate level of the hierarchy.

You switch into execution mode under delivery pressure. However, this requires that the reasoning and operational documents are established far enough. Then the human and the LLM can execute within existing reasoning. However, you keep a minimal log: deviations from the thinking, deferrals, but also assumptions that broke. That log keeps the return to reasoning mode honest and is intended to avoid reconstruction afterwards.

You do return to reasoning mode. Eventually. And then the log is what you will have to work through.

---

## Where to start

Two documents.

1. [`RFM_top_level_reasoning.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_top_level_reasoning.md), the methodology's own reasoning. Start here.
2. [`RFM_first_session_guidance.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_first_session_guidance.md), practical steps for producing your first reasoning document.

The rest of the repository serves people maintaining and extending RFM. However, if you want to go deeper, do read the glossary. As mentioned before, operational documents hold the what, the procedures, the specifications. Review prompts have been designed to sweep completed documents for structural, language and lifespan failures, but also for operational problems. Documents in RFM are living, so you change them often. The review prompts are what keep them in shape as they change. A set of skills has been developed that the LLM loads at the moments they apply. They also have their own reasoning documents. Furthermore, there is a shared failure taxonomy that both the sweeps and the skills draw on to check and detect problems.

In other words, every component of the approach has a reasoning document (and often an operational document) beside it. Files are named `RFM_[subject]_[category].md`, so the reasoning behind the sweep prompts sits in `RFM_sweep_reasoning.md` and the procedures derived from it in `RFM_sweep_operational.md`.

The full list, with current versions, is also in the document map, [`RFM_map.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_map.md). It is maintained only there.

---

## State

The approach is in active development. Every document is living, versioned and continuously curated.

The acronym for the methodology was chosen deliberately. Anyone who recognises the older expansion already knows what this methodology thinks you should do before touching anything.

RFM is a vehicle, not a prescription. The reasoning comes first. What you build on top of it is yours.

---

## Where this bites

Most of the current effort around working with AI goes into assembling what an LLM needs: the right documents, the right context, the right instructions. Sounds right, but it is the wrong first question. It asks what the AI needs before anyone has asked whether the reasoning underneath it was worked through at all.

If you give an LLM a well-assembled context and badly-reasoned documents, it will execute with confidence on assumptions that nobody examined and alternatives nobody named.

What's worse is that agentic systems make it even more challenging. As LLMs plan and act across long chains with no human checking each step, the reasoning document is intended to provide a mechanism that keeps the human intent visible to the system that executes it. Note that the industry calls those chains reasoning. But that is reasoning as inference, not reasoning as intent, and it is the second kind that disappears. In other words, a highly capable agent acting on vague intent fails confidently at scale. That failure is hard to trace back to its cause. Reasoning made explicit before autonomous execution is what makes the execution accountable.

---

## License

[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

© 2026 Hinrich W.H. Göhlmann

*Developed in collaboration with Claude (Anthropic), acting as co-author throughout.*
