# RFM — Incubating Ideas
*Captured end of session // not yet ready for document capture*

---

## What this file is

This file is public because transparency about work-in-progress is consistent with RFM's own principles. If you are encountering RFM for the first time, start with the README and `RFM_top_level_reasoning.md` — this file shows the methodology's thinking-in-progress, not its conclusions.

These are ideas that surfaced during a refining session but are not sharp enough yet to capture in the methodology documents. They are candidates, not conclusions. Read this file into a future session when the topic feels relevant.

**On signal counts:** each entry carries a signal count — the number of independent observations from distinct contexts (different LLMs, different domains, different problem types) that have surfaced the same idea. Repetition within the same session or LLM does not increment the count. Multiple independent signals on the same candidate should trigger a document home conversation. Two independent contexts is sufficient to propose; three should trigger action regardless.

---

## A. The LLM as bridge between universal and domain-specific

The co-author relationship may be the mechanism by which universal RFM principles become domain-specific operational practice — not through templates or examples provided by the methodology, but through a targeted conversation grounded in the specific reasoning document just built. The output belongs to the project, not to RFM. This keeps the methodology universal while making it immediately actionable in any domain.

**Why not captured yet:** not yet tested or named precisely enough. The idea is a hunch, not an observation.

**Possible home when ready:** Open Question 3 (onboarding), or a new open question in `RFM_top_level_reasoning.md`.

**Signal count: 1** *(origin session, pre-dating the counter)*

---

## B. The reasoning document as what makes something safely routine

External feedback suggested RFM has low value for "routine" work. The response: the routine had to start somewhere. The reasoning document is what allows something to safely become routine — because the assumptions and boundaries are explicit enough that everyone knows what conditions the routine depends on. When those conditions change, the reasoning document is what tells you that, and why.

**Why not captured yet:** sharp as a conversational observation, not yet shaped into a methodology-level insight.

**Possible home when ready:** may connect to A — both are about the methodology's role in the transition between high-stakes original thinking and confident downstream execution. Could become a new open question, or strengthen Assumption 11 (the virtuous cycle).

**Signal count: 1** *(origin session, pre-dating the counter)*

---

## Note on relationship between A and B

They may belong together. Both describe the LLM and the reasoning document as the connective tissue between original high-stakes reasoning and confident downstream execution. If they converge, the combined insight may be strong enough to capture as a single open question or as an addition to Chosen Direction.

---

## F. The human system prompt — a missing document type

The traveling prompt tells the LLM how to show up. Nothing tells the human. The collaborative posture is described in Open Question 3 of the top-level reasoning document — but buried there as an observation, not a behavioral guide. The practices are now accumulating enough to warrant their own artifact: reasoning before stating destinations, naming drift when you see it, pushing back rather than confirming, applying the "so what?" test to your own best ideas, testing whether a candidate belongs at this level before inviting a draft, actively pushing the LLM back into the co-author role when it drifts.

A human prompt would be a new document type — `RFM_human_prompt.md` — sitting alongside the traveling prompt as its pair. The prompts reasoning document would need a new section. Open Question 3's collaborative posture paragraph is the seed.

**Why not captured yet:** the document type is new and the content needs deliberate design, not session accumulation.

**Possible home when ready:** new Open Question in `RFM_top_level_reasoning.md`, or directly to design if the posture description in OQ3 is already sufficient seed material.

**Note:** Codex session (April 2026) produced evidence for the importance of human co-author correction behavior, but assessed this as support for that behavior generally rather than for a new document type specifically. Not counted as a clean signal.

**Signal count: 1** *(origin session, pre-dating the counter)*

---

## G. RFM value rises when language itself can distort the object

Cross-LLM feedback from a discovery science application surfaced a precise observation the documents don't yet contain: RFM is most valuable when the scientific object is still being shaped and the language used to describe it can itself distort it. The current framing in the top-level reasoning document is that RFM prevents reasoning from disappearing. This is more specific: RFM is most valuable when premature language hardens into unexamined reality — when the words used to describe the problem become the problem, invisibly. The discipline of keeping reasoning explicit and curated protects the object from the names we give it before it is fully known.

**Why not captured yet:** signal count at threshold but both observations from LLM-assisted domain-facing work. A third signal from a different context, or a cleaner test of the core claim, would justify proposing a document home.

**Possible home when ready:** Open Question 6 (evolutionary stage problem) — domain fit as a function of how settled the object is; or Open Question 2 (minimum viable document) — the domain-fit condition as a determinant of where RFM earns its overhead. Could also connect to A and B if those converge.

**Flag on "shallow work" framing:** the observation that RFM is too heavy for shallow work is not yet principled enough to capture. "Shallow" is undefined and risks becoming a self-serving exit condition. Hold until OQ2 produces a better frame for domain fit.

**Signal count: 2** *(cross-LLM, discovery science domain, pre-dating the counter; Codex / GPT-5.4, domain-facing delivery context, April 2026 — moderate match)*

---

## H. Once a module exists, top-level ownership must be actively reduced

When a section strains and a new module branches from it, the top-level document does not automatically contract. Without active reduction, both layers start talking about the same thing — the top level drifts toward restating what the module now owns. The discipline after branching is not just creating the new module; it is deliberately removing from the top level whatever the module now carries. This is a distinct failure mode from the branching signal itself and is not currently named in the documents.

**Why not captured yet:** at threshold. Ready for a document home conversation.

**Possible home when ready:** Hard Lessons under Document discipline, or a behavioral instruction in the traveling prompt. Connects to HL8 (document strain is diagnostic) but is a subsequent step that HL8 doesn't cover.

**Signal count: 2** *(origin session, pre-dating the counter; Codex / GPT-5.4, module ownership and top-level contraction, April 2026 — strong match)*

---

## I. The two sweep types have different jobs and should not be conflated

Practice has revealed at least two distinct sweep modes: a language/clarity sweep (removing shorthand, journaling, internal dialect, session residue) and a structural/hierarchy sweep (checking ownership levels, graduating open questions, detecting module strain). These are different cognitive modes with different failure modes if conflated. A sweep that attempts both simultaneously risks doing neither with sufficient concentration. OQ9 names the sweep prompt as undesigned — this sharpens what it needs to design for.

**Why not captured yet:** at threshold. Ready for a document home conversation — most naturally in the sweep prompt design (OQ9), but the principle may also warrant a behavioral note in the traveling prompt.

**Possible home when ready:** directly into the sweep prompt design (OQ9), as a founding constraint — two prompts or two explicit modes, not one undifferentiated sweep.

**Signal count: 2** *(origin session, pre-dating the counter; Codex / GPT-5.4, language vs. hierarchy cleanup separation, April 2026 — strong match)*

---

## J. Reviewer subagents are most useful after a coherent draft exists

Premature review — invoking a reviewer subagent before a coherent draft exists — produces noise, not signal. The reviewer has nothing stable to review against and either invents problems or reinforces incompleteness. The useful moment is after a draft is coherent, when the reviewer can distinguish between what is structurally wrong and what is still being formed. This is specific enough to be behavioral guidance for the sweep prompt design and possibly for the traveling prompt.

**Why not captured yet:** at threshold, but both signals came from LLM-assisted drafting contexts. The principle feels robust; the placement question (sweep prompt vs. traveling prompt) remains unresolved pending the sweep prompt design.

**Possible home when ready:** sweep prompt design (OQ9) as a timing constraint; or traveling prompt as a behavioral instruction about when to invoke review.

**Signal count: 2** *(origin session, pre-dating the counter; Codex / GPT-5.4, subagent review timing, April 2026 — moderate match)*

---

## K. External feedback requires explicit triage before it affects documents

When external or reviewer feedback enters a reasoning session, it exerts gravity of its own kind — not the operational-detail gravity that "re-anchor after research" addresses, but a flattening pressure: the tendency to treat all critique as equally valid before separating what is solid signal, what may be overreach, and what actually warrants a document change. Without explicit triage, the LLM (and the human) can end up polishing in the direction of the most recent feedback rather than the most correct one. The triage is: (1) solid signal — confirmed by evidence or reasoning, (2) possible overreach — plausible but not yet grounded in the local context, (3) what actually changes our documents — the subset that survives both prior tests. Applying this split early in a feedback session, rather than late, is the discipline.

**Why not captured yet:** at threshold. Ready for a document home conversation.

**Possible home when ready:** traveling prompt as a behavioral instruction, parallel in structure to "re-anchor after research" but scoped to feedback rather than research material. Could also inform the sweep prompt design (OQ9) if reviewer subagents are in scope there.

**Signal count: 2** *(Codex / GPT-5.4, domain-facing delivery context, April 2026; Codex / GPT-5.4, subagent and Copilot feedback triage, April 2026 — strong match)*

---

## L. The prompt system has no mechanism for grounding against evolving prompt engineering practice

The reasoning documents govern why the prompts are designed the way they are. But prompt engineering practice evolves — LLM behavior changes across model generations, optimal activation patterns shift, new evidence emerges. Nothing in the current methodology triggers a periodic check: do the derived prompts still reflect the state of the art given what the reasoning documents prescribe? The concept: a grounding sweep — not a structural or language sweep, but a research-first pass asking whether the prompt artifacts are still optimally designed given current practice. May be lightweight (an operational note) or substantial (a new sweep type). Not yet sharp enough to place.

**Signal count: 1** *(this session)*

---

## M. Dreaming (Anthropic Managed Agents) as external validation of the curation problem

Anthropic's "dreaming" feature for Managed Agents (May 2026) is a scheduled process that reviews past agent sessions, extracts patterns, and curates memory between sessions — including automatic memory updates. The diagnosis behind it is identical to RFM's founding curation assumption: memory left to accumulate without periodic review degrades. The solution differs sharply — automated vs. deliberate — and that difference is where RFM's position must stay sharp. Automated curation is the failure mode RFM names, not a solution, because compression is always structural and requires human judgment. But the fact that Anthropic built infrastructure around this problem is meaningful external signal that AS-CDNO is pointing at something real and generalizable, not a preference of its authors.

**Why not captured yet:** single source, single context. The validation is real but the implications for RFM's own curation design — whether the deliberate/automated distinction needs to be more explicitly argued in the documents — require more signal before warranting a document change.

**Possible home when ready:** AS-CDNO in `RFM_top_level_reasoning.md` — the assumption would carry a stronger grounding sentence. Or the Landscape in the same document if the automated-vs-deliberate tension becomes sharp enough to warrant a named row.

**Signal count: 1** *(Anthropic Managed Agents blog, May 2026)*

---

*Not versioned — this is a working note, not a methodology artifact.*
*Discard once the ideas have found their home or been consciously dismissed.*
