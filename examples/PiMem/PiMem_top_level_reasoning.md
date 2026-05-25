# PiMem
`v0.1.0` // `top_level_document` // [living]

---

## Document Map

| Document | Type | Version | What it carries |
|---|---|---|---|
| `PiMem_top_level_reasoning.md` | Top-level reasoning | v0.1.0 | Pi agent memory — problem, assumptions, landscape, chosen direction, open questions, hard lessons |
| `PiMem_operational.md` | Operational | v0.1.0 | Memory categories, expiry criteria, write constraints for AGENTS.md |

---

## The Problem

Pi coding agents accumulate memory by default or start fresh — there is no middle path. The pi-memory-md extension persists whatever the agent decides to write across sessions; without it, every session begins without context. Both failure modes are visible in Pi's community: accumulated memory grows noisy, stale, and oversized until it actively degrades agent behavior; starting fresh forces the agent to rediscover context it has already earned.

The deeper failure is not technical. It is the absence of a governing discipline for what memory is *for*. Without a principled answer to that question, any memory mechanism defaults to accumulation. The agent writes what seems relevant in the moment, nothing expires, and the memory file becomes a liability rather than an asset.

An AGENTS.md that installs principled memory discipline addresses this gap: not by replacing pi-memory-md or any other extension, but by giving the agent explicit criteria for what to remember, why, and what never to accumulate.

---

## The Assumptions

The following are believed to be true. They cannot all be fully proven yet. If any of them is wrong, the approach needs to change.

**[AS-AMSS] - AGENTS.md is the right place to define memory behavior.** It is the only content Pi injects beyond its minimal system prompt, it loads at session start before any work begins, and it is human-maintained rather than agent-written. If memory rules belong anywhere, they belong here.

**[AS-ADNM] - Accumulation without explicit rules is the default failure mode.** Any memory mechanism without clear criteria for what to write, what to skip, and what to retire will grow without bound. The agent writes what seems relevant in the moment; nothing expires. The problem is not the extension — it is the absence of rules.

**[AS-MPHC] - Not all persistent information serves the same purpose.** Project constants (stack, conventions, key paths), earned lessons (what failed and why), and active context (current state, open decisions) are different kinds of information with different shelf lives. Mixing them without distinction produces noise.

**[AS-HOWN] - The human sets the rules; the agent follows them.** The agent cannot judge whether a memory entry is still true, still relevant, or has expired — that requires project-level judgment the agent does not hold. The AGENTS.md defines what the agent may write and what should trigger a human review.

**[AS-SNCF] - Small and current beats large and comprehensive.** A memory file the agent can read and apply in full is more valuable than a complete record it must filter. Usefulness degrades with size. The rules must enforce a ceiling, not just a floor.

---

## The Landscape

The question this landscape must answer is: what approaches exist for giving a Pi coding agent persistent memory that remains useful over time?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **No memory (default Pi)** | Each session starts fresh; nothing persists across sessions | The agent rediscovers the same context repeatedly. Any project with history becomes expensive and frustrating. |
| **pi-memory-md and equivalents** | Agent writes to markdown memory files across sessions; loaded automatically at session start | No rules govern what gets written or retired. Grows noisy and stale. Users report active degradation of agent behavior as files grow. |
| **Multi-tier markdown extensions** (pi-mem, pi-hermes-memory, tickernelz/pi-memory) | Separate memory into tiers — long-term facts, daily logs, scratchpad — with different injection and retention behavior | Tiers describe *where* information lives, not *what belongs there*. The agent still decides what to write into each tier without explicit criteria. Degradation is deferred, not prevented. |
| **Vector and semantic memory** (agentmemory, mem0, Memori) | Store memories as embeddings; retrieve by relevance; auto-evict by frequency or age | Adds significant infrastructure. Eviction by frequency or age is a proxy for usefulness — it does not distinguish a stale fact from an important but rarely invoked one. Human judgment plays no role in routine write and retire decisions. |
| **AGENTS.md as static context** | Human writes project conventions, stack, and preferences once; agent reads at session start | Covers stable facts well. No mechanism for the agent to capture what it learns during sessions. Static by design — cannot evolve without human edits. |
| **Compaction (/compact)** | Summarizes older messages in long sessions to stay within context limits | Within-session only. Summarization loses signal. Does not persist anything across sessions. |

**The gap:** every existing approach either gives the agent too much freedom (write anything, retire nothing) or relies on technical proxies — tiers, embeddings, frequency scores — that substitute for the harder question: what *should* an agent remember, and why? GitHub Copilot's engineering team has documented this directly: memory quality is primarily a freshness and invalidation problem, and stale memories are often more dangerous than no memory at all. What is missing is a set of explicit, human-defined rules inside AGENTS.md that tell the agent what categories of information are worth remembering, what has a limited shelf life, and what should never be written down. The mechanism already exists. The rules do not.

---

## The Options Considered

**1. Human-maintained AGENTS.md only — no memory extension**

Static context: the human writes project constants, conventions, and hard-won lessons directly into AGENTS.md and maintains it manually. The agent reads but never writes. No extension required.

Rejected because it breaks the feedback loop the problem requires. The agent earns context during sessions — what failed, what the codebase resists, what assumptions proved wrong — and that learning disappears when the session ends. Manual maintenance puts the entire capture burden on the human, at the moment the human is least positioned to capture well: after the session, from memory, without the agent's perspective. The problem is not that AGENTS.md is the wrong artifact. It is that human-only maintenance cannot keep pace with what sessions reveal.

**2. Rules in AGENTS.md paired with a memory extension — agent writes within defined criteria**

The agent writes to a persistent memory file across sessions, but only under explicit rules defined in AGENTS.md: what categories of information are worth persisting, what has a limited shelf life, and what should never be written. The human sets the rules; the agent operates within them.

This is the direction under active consideration. Kept open here pending honest comparison with the remaining options.

**3. Rules in AGENTS.md paired with a tiered memory extension**

Tiered extensions — long-term facts, daily logs, scratchpad — provide structural separation; AGENTS.md rules govern what belongs in each tier. The structure does more of the work; the agent decides less about placement.

Rejected because the tiers describe *where* information lives, not *what makes it worth keeping*. Extensions that encode their own write policies — memory categories, failure capture, correction tracking — introduce a competing discipline layer rather than extending the one defined in AGENTS.md. The result is two sets of rules governing the same decisions. A single well-governed memory file under clear AGENTS.md rules is simpler and more honest than tiers that either duplicate that discipline or leave the categorization problem unsolved.

**4. Vector or semantic memory — retrieval replaces curation**

Embeddings replace explicit rules: the agent stores freely, retrieval surfaces what is relevant, eviction operates by frequency or recency. Human judgment plays no role in routine write and retire decisions.

Rejected for two reasons. First, it introduces infrastructure that exceeds the problem's scope — the gap is a rules gap, not a search gap. Second, and more fundamentally: frequency and recency are proxies for usefulness, not measures of it. A stale assumption about the codebase may be invoked rarely but still actively mislead. An important constraint may not appear in recent sessions but must not expire. Automated eviction cannot distinguish between these cases. Human judgment at the rules level — not at the injection level — is what the problem requires.

---

## The Chosen Direction and Why

**Why AGENTS.md is the right place to define memory rules**

AGENTS.md is the one artifact Pi loads before any session work begins — before the agent has read the codebase, before any extension has run. Rules placed there are read at the moment they matter most: before the agent decides anything. It is also human-maintained by design. Unlike a memory file the agent can write to, AGENTS.md cannot be modified by the agent mid-session. That separation — human sets the rules, agent operates within them — is what keeps the discipline stable across sessions rather than drifting with whatever the agent decided to write last time.

**Why a single governed memory file over tiers**

A single memory file with explicit write categories is auditable in a way tiered files are not. The human can open it, read the full state, and retire entries that have expired. Tiers distribute that content across multiple files and multiple write policies — the human loses the single view that makes honest maintenance possible. The discipline the problem requires is not structural separation of content. It is clear criteria for what belongs and what must go. One file, governed by explicit categories, keeps that discipline visible and actionable.

**Why human-defined categories over agent-decided writes**

The agent cannot judge whether something it learned last session is still true. Staleness is invisible from inside the session that produced the stale belief — the agent has no access to what changed in the codebase while it wasn't running, what decisions the human reversed, what assumptions proved wrong over time. Only the human holds that judgment. Categories defined in AGENTS.md make the write decision explicit: the agent writes what the rules permit, flags what seems worth human review, and never decides unilaterally that something is durable. That boundary — agent captures, human governs — is what prevents the memory file from becoming a liability.

**Why overwrite rather than flag when a contradiction is detected**

The agent cannot resolve a contradiction by judgment — determining which of two conflicting entries is still true requires project-level knowledge the agent does not hold. But flagging the contradiction at write time collapses into the same problem: the agent must decide whether a conflict exists and then wait for human resolution before completing the write. Overwrite sidesteps both failures. The rule is deterministic: a new write about a fact already recorded replaces the existing entry. The human governs this through the write categories and criteria defined in AGENTS.md — not through per-contradiction rulings at session end.

**Why specific ceilings rather than principle-only constraints**

The principle that memory must stay small and current does not itself constrain an agent. A ceiling that exists only as a principle requires judgment the agent cannot exercise. Specific numbers make the constraint deterministic and actionable. The values are provisional starting points subject to revision as practice reveals whether they are too tight or too loose — that revision belongs in the operational document, not here.

**Why the pairing of AGENTS.md rules with a memory extension — not AGENTS.md alone**

A well-maintained AGENTS.md without a memory extension puts the entire capture burden on the human. The agent earns context during sessions — failure modes discovered, codebase patterns that resist certain approaches, decisions made and their reasoning — and all of it disappears when the session ends. The human is expected to reconstruct and manually record what the agent observed, after the fact, from memory. That discipline does not hold. The memory extension closes the feedback loop: the agent captures what it learned, within the rules the human defined, so that the next session starts with earned context rather than a blank slate.

---

## The Boundaries

**Not a specification of the memory rules themselves.** This document reasons about where rules should live and why. The actual categories, expiry criteria, and write constraints belong in an operational document — the intermediate artifact between this reasoning and the AGENTS.md content it will eventually govern.

**Not a guide to installing or configuring a memory extension.** Which extension to use, how to install it, and how to configure injection behavior are implementation decisions that follow from this reasoning. They do not belong here.

**Not applicable to memory management for non-Pi agents.** The reasoning is grounded in Pi's AGENTS.md load order, extension model, and session behavior. Other coding agents may share some characteristics but are not covered by this document.

**Not a substitute for human curation of the memory file.** This document establishes why human-defined rules govern what the agent writes. It does not describe how often the human should review the memory file, what a retirement session looks like, or how to recognize when the file has drifted. That discipline is outside this document's scope.

**Not a license to make AGENTS.md verbose.** Memory rules belong in AGENTS.md because they govern agent behavior across every session — but they must remain lean enough to honor Pi's minimal-signal philosophy. A memory rules section that grows over-specified becomes the noise it was designed to prevent.

---

## The Open Questions

**[OQ-MFSG] Memory file size and session performance.**

At what point does a governed memory file grow large enough to degrade the agent's session performance through context injection overhead? The entry ceiling defined in the operational document is designed to prevent this, but the degradation threshold is unknown and the ceiling value is provisional. This may only become visible through sustained use.

**[OQ-MASQ] Memory behavior in multi-agent and subagent sessions.**

Pi supports subagents for parallel work. Whether memory rules designed for a single-agent session hold when subagents are running — whether they read the same memory file, write to it independently, or ignore it — is unresolved. The rules as designed do not address this case.

**[OQ-RCUP] Whether lean rules discipline holds under development pressure.**

The reasoning asserts that memory rules in AGENTS.md can remain lean and high-signal through curation. Whether that discipline holds in practice — on an active project, across many sessions, with accumulating edge cases — has not been tested. The failure mode is gradual rule accumulation that mirrors the memory file bloat the rules were designed to prevent.

**[OQ-PELC] Whether a 2-sentence per-entry length ceiling holds for earned lessons.**

Earned lessons may require more context than 2 sentences to be actionable by a fresh agent — the ceiling was set as a starting guess, not a tested constraint. Whether it is too tight for lessons that involve non-obvious failure patterns, or whether tightness is itself the discipline that keeps entries useful, requires practice to resolve.

---

## Hard Lessons

**[HL-CHME] Contradiction handling is not provided by simple markdown extensions — it must be an explicit write rule.**

Simple markdown memory extensions do not detect when a new write conflicts with an existing entry. Without an explicit overwrite rule, two entries for the same fact coexist permanently and silently. The write rules in the operational document must cover this gap directly; it cannot be delegated to extension infrastructure in the simple markdown target case.

---

*top_level_document // [living]*
*the reasoning arrived before the structure did*
*that was the right order*