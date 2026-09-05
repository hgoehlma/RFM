# Reasoning-First Methodology: RFM Unslop Skill Reasoning Document
`v0.3.0` // `skill_unslop_reasoning` // `[living]`

---

## The Problem

Slop enters RFM documents through the co-authorship session itself. The traveling prompt instructs suppression of LLM behavioral patterns, but that instruction is ambient and competes with the cognitive load of doing the reasoning work simultaneously. The two-layer discipline (write from the reasoning, suppress LLM patterns) assumes both can be held in one pass. In practice, slop gets through. Catching it requires a separate sweep pass that costs time proportional to how much reasoning happened in the session. The longer the session, the larger the debt.

The debt compounds in a specific way: productive sessions generate more slop, which means more sweep work, which means the sessions that advance the reasoning most are also the sessions that create the most corrective work. Clean source documents reduce how much filler the LLM adds in derivatives, but they do not touch the entry point. Nothing currently catches slop at the session level before it hardens into documents.

---

## The Assumptions

The following are believed to be true. If any is wrong, the skill design needs to change.

**[AS-SESS] -** The boundary between session text and document text is not detectable in practice. Any output produced during a session (a draft, an answer to a phrasing question, incorporated thinking) can migrate into a document.

**[AS-AMB] -** An instruction that competes with active reasoning load will not reliably fire. The more demanding the session work, the more the suppression instruction loses to it. This holds regardless of how clearly the instruction is written.

**[AS-REG] -** The behavioral patterns that constitute slop are the same across document types. What differs is the threshold for what counts as a violation. A single skill with register-specific thresholds is simpler to maintain than separate skills per document type, and removes the classification judgment that per-register skills require.

**[AS-UP] -** Precise source documents reduce filler in derivatives. An LLM with dense, specific source material has less room to add explanation or pad structure. This does not address the session entry point; it reduces pressure downstream of it.

---

## The Landscape

*What approaches exist for preventing LLM behavioral patterns from entering co-authored reasoning documents?*

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Generic unslop skill | Removes AI vocabulary and adds human voice and rhythm | Wrong register for reasoning documents. "Add soul" and "vary rhythm" are actively harmful in precision-governed text. Triggers on writing tasks, not on RFM session membership. |
| Traveling prompt two-layer discipline | Ambient instruction to suppress LLM patterns on every prose derivative | Too abstract to activate reliably. Competes with reasoning load. Does not cover conversational session text that migrates into documents. |
| Post-session language sweep | Dedicated corrective pass for language failures after the fact | Catches what slipped through but patterns have already hardened into documents. Cost scales with session length. |
| Per-register separate skills | One skill per document type | Requires a judgment call at the trigger point about which skill applies. That judgment fails under delivery pressure. The patterns are the same across registers anyway. |
| Co-authorship behavioral guidelines | Instructions in the system prompt for LLM posture: challenge weak reasoning, avoid sycophancy, resist anchoring to early framings | Addresses upstream reasoning failures, not surface output patterns. A well-postured LLM can still produce throat-clearing, importance inflation, and epistemic flatness in the text it generates. Different failure class, different corrective. |

**The gap:** no mechanism fires at the moment of text production, for all output, in all RFM sessions, with pattern guidance concrete enough to catch surface slop before it hardens.

---

## The Options Considered

**1. Extend the traveling prompt with a concrete pattern list.**

The pattern list would sit where it fires most reliably: in the document loaded every session. Rejected because the traveling prompt already carries ambient discipline and identity instructions. Adding a detailed pattern list inflates it beyond its scope and creates a maintenance burden when patterns change. The traveling prompt names requirements; a dedicated artifact carries the detail.

**2. Add a second-pass instruction to the derivation procedure.**

A post-draft review step would catch slop before derivatives are accepted. Rejected because slop enters before derivation, in the session text that becomes source material. A derivation-time check does not reach the entry point.

---

## The Chosen Direction and Why

**Why always-on rather than invocable.**
An invocable skill puts the trigger decision in the human's hands at the moment of production. That is exactly the moment when delivery pressure is highest and cognitive load leaves least room for a meta-decision about tooling. The failure mode of an invocable skill is identical to the failure mode of an ambient instruction: both require the human to remember to act. Always-on moves the trigger out of the human's hands entirely. The session system prompt carries the declaration once; the skill fires on every response without further decision.

**Why the traveling prompt carries the declaration.**
The traveling prompt is always loaded. It is the only artifact that guarantees a session-level instruction reaches every exchange. A document the LLM may or may not have loaded cannot carry a session-wide trigger reliably.

**Why conversational responses are in scope.**
The boundary between session conversation and document candidate is not detectable in advance. Any session output can migrate into a document. Excluding conversational responses creates a gap at the most likely entry point.

**Why one skill with register awareness rather than per-register skills.**
The surface patterns are the same across document types. What differs is the threshold for what counts as a violation. One skill with register-specific thresholds is simpler to maintain and removes the judgment call that per-register skills require.

**Why the skill targets surface patterns, not epistemic posture.**
Epistemic failures (sycophancy, anchoring to early framings, uniform confidence across claims of different strength) are upstream of text production. They corrupt what gets reasoned before a word is written. Surface pattern suppression does not reach them, and trying to combine both in one skill would dilute the trigger clarity that makes the always-on design work. Epistemic posture is addressed in the traveling prompt's co-author role instructions.

---

## The Boundaries

**Not a substitute for the language sweep.** The language sweep catches failures of reasoning legibility: session-born vocabulary, undefined terms, claims that outrun their evidence. This skill catches surface behavioral patterns in the text itself. Different failure classes, different corrective passes.

**Not a substitute for the structural sweep.** Content at the wrong level, graduation candidates, module strain are not in scope here.

**Not a corrective for epistemic posture failures.** Sycophancy, anchoring to early framings, and uniform confidence across claims of different strength are upstream of text production. This skill does not reach them. They are addressed in the traveling prompt's co-author role instructions.

**Not a voice or style skill.** Adding soul, varying rhythm, using first person: wrong register for reasoning documents. The generic unslop skill covers those. This skill strips patterns; it does not add character.

**Not applicable to non-RFM projects.** The trigger is the session system prompt's RFM declaration. Without that declaration the skill does not fire.

**Not self-activating.** The skill does not fire through its description alone. Reliable activation requires explicit invocation. In RFM projects, that invocation depends on session-startup reading the handover rules file at session open; a rule stating this skill must be invoked is not sufficient by itself. See HL-SELFENF.

---

## The Open Questions

**[OQ-EPFL] Can epistemic flatness be specified concretely enough to be actionable in the skill?**

Epistemic flatness is the failure where every claim lands with the same assertive tone regardless of how established it is. In reasoning documents this is specific: assumptions are believed but not proven, open questions are genuinely unresolved, chosen directions are committed. Writing all of these with identical confidence misrepresents the document's epistemic state. The corrective is not hedging words on every sentence. It is matching sentence confidence to section epistemic status. Whether this can be specified as a concrete, actionable pattern or requires a different mechanism is not yet determined. Needs empirical observation across sessions before any specification attempt.

---

## Hard Lessons

**[HL-RLNA] Reading a constraint and holding it under production load are different.**

An LLM confirms a skill is loaded, then violates it in the next response. The skill fires more reliably on deliberate drafting tasks than on conversational output. Compliance narrated at load time is not compliance at production time. The check must happen at the moment of output, not at the moment of loading.

**[HL-RSGV] A corrective pass applied without reading the governing skill produces output that looks compliant and is not.**

During an em-dash sweep, the default replacement was parentheses. The rfm-unslop skill explicitly flags parentheses as trading one AI tell for another. The error was not caught until the skill was consulted mid-session. The surface check passed. The deeper check failed. Any corrective pass on style, structure, or language must begin by reading the artifact that governs the failure class being corrected.

**[HL-SELFENF] A rule that names its own invocation mechanism is not proof the mechanism runs.**

This skill's Boundaries entry credited "the rules file and the handover carry-forward mechanism" with reliable activation. Nothing executed at session open actually read the rules file. The rule existed in writing. The skill still didn't fire, twice in the same session. The fix was not a stronger rule. It was adding an explicit step to session-startup that reads the rules file before producing any output. A rule that says to read something is not self-enforcing; only an executed step is.

**[HL-PLCL] A pattern list catches the patterns on it, not bad writing in general.**

Two drafts of a reasoning entry passed every check in this skill and were rejected on register. The failure was elevated diction with an abstraction as the sentence's subject: "a check that invites inference from silence licenses invention." No pattern named it, so both drafts came back clean, and human reading caught what the skill could not. The error was treating a clean pass as evidence the prose was sound. The list reports only on what it enumerates. When a new failure shows up in practice, add it as a pattern; until then, a clean pass says nothing about that failure.
