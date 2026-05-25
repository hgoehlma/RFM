# PiMem — Pi Memory Discipline

A worked example of the Reasoning-First Methodology applied to a non-software problem: giving a Pi coding agent deliberate memory discipline.

## The problem

Pi memory extensions accumulate by default. Without explicit rules governing what to write, what expires, and what must never be stored, any memory file grows noisy and stale — often becoming a liability faster than it becomes an asset. This is not a tooling problem. It is the absence of a governing discipline for what memory is *for*.

## The chain

Three files, in derivation order:

| File | What it carries |
|---|---|
| `PiMem_top_level_reasoning.md` | The reasoning document — problem, assumptions, landscape, options considered, chosen direction, open questions, hard lessons |
| `PiMem_operational.md` | Memory categories, expiry criteria, write constraints — derived from the reasoning document |
| `PiMemAGENTS.md` | The AGENTS.md content, ready to drop in — derived from the operational document |

Read the reasoning document first. The AGENTS.md rules only make sense — and can only be honestly adapted — if you understand why those specific rules and not others.

## How to use

Add the contents as a section in your existing `AGENTS.md`. Adapt the categories and ceilings to your situation. If you change a rule, change the reasoning document first.

To derive a version optimized for your agent: give your preferred LLM the reasoning and operational documents and ask it to produce an AGENTS.md that activates the discipline with minimal text.

## What remains open

The biggest unresolved question — named honestly as [OQ-RCUP] in the reasoning document — is whether the rules discipline itself holds under development pressure, or whether the AGENTS.md gradually accumulates the same bloat it was designed to prevent. Not yet tested at scale.

## Context

Built using the Reasoning-First Methodology: https://github.com/hgoehlma/RFM
