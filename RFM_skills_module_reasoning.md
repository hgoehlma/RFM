# Reasoning-First Methodology: Skills Module Reasoning Document
`v0.2.0` // `module_reasoning` // `[living]`

---

## The Problem

RFM uses skills to carry behavior that fires at a specific moment in a session. A skill differs from always-on instruction in that nobody invokes it: it matches its own trigger description or it does not run, and nothing reports the sessions where it did not. Each skill reasoning document carries the design of its own skill. What none of them carries is the design that decides whether a skill fires at all: what makes a behavior a skill rather than always-on instruction, how a trigger description is written so the skill matches when it should, and how a skill reaches the environment that runs it.

---

## The Assumptions

**[AS-AMBC] - A skill's ambient cost is its description, not its body.** Every installed skill puts its name and description into the session at open, whether or not it fires. Only the body is held back until the skill is judged relevant. Instruction-following degrades measurably as the number of instructions present rises, and instructions appearing earlier are followed more reliably than later ones, so the descriptions of skills that never fire still cost the skills that do. Moving a behavior into a skill reduces its ambient cost rather than removing it. What is not measured is where the balance sits: how many installed skills it takes before their descriptions alone reproduce the load that moving the bodies out was meant to relieve. This breaks if descriptions stop being preloaded, or if instruction-following stops degrading with density.

**[AS-MATCH] - Description design raises the probability that a skill fires. It does not make it certain.** Whether a skill runs is decided by a model judging its description against what the session appears to be doing. Descriptions written for that judgment rather than for a human reader measurably improve selection, and the improvement grows as the number of candidates grows. Selection accuracy itself falls as that set grows, and the cases that fail are those where the right unit is not the obvious match. Neither the model's judgment nor the session's appearance is under the author's control, so some sessions that need a skill will not load it, and nothing in the session marks the omission. Wording and installed count are both levers, and where the count should sit is the same unmeasured quantity `[AS-AMBC]` leaves open. This breaks if skills begin firing reliably from their descriptions alone.

**[AS-DELIV] - No skill delivery mechanism is stable enough to name in reasoning.** A skill has to reach the environment that runs it, and every environment does that differently: a file layout, a package, an installer, a proposal a user approves. These mechanisms change faster than the reasoning that governs skill design. A reasoning document that names one goes stale the next time an environment changes, and every skill document written against it has to be revised for a reason that has nothing to do with the skill. What holds across environments is that the installed skill is the artifact and the mechanism that put it there is local detail. This breaks if a portable skill format is adopted widely enough that naming it costs nothing.

---

## The Landscape

What decides that a behavior should be packaged as a separately triggered unit of instruction for an LLM, and how is that trigger designed so the unit fires at the right moment?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **Always-on system prompt** | Carries every behavior in context for every session. No trigger design needed because nothing is ever absent. | Instruction-following degrades measurably with instruction density, and earlier instructions are followed more reliably than later ones. Offers no way to scope behavior to a moment. |
| **Retrieval-augmented context** | Holds material outside the context and pulls in what is semantically close to the current query. | Retrieves reference content by similarity to a query, not conduct by relevance to a moment in a session. Nothing decides which material should be a unit in the first place. |
| **Tool and function descriptions** | The model selects a tool by matching its description against the task. Closest prior art on trigger design: rewriting descriptions for the model rather than for a human reader measurably improves selection, and author-written descriptions fail by leaving constraints implicit. | Optimizes which unit is picked from a fixed catalogue. Says nothing about what should have become a unit. A tool is invoked, returns a result, and the model continues; a skill changes how the model works for the rest of the session. |
| **Agent skill libraries** | Stores learned behaviors as reusable units indexed by the embedding of a description and retrieves the top matches for a new task. The closest existing case of description-as-trigger for behavior rather than for a call. | Units are code the agent wrote for itself from task success, so nothing decides what deserves to be a unit. Retrieval returns a fixed number of matches per task, which neither composes nor abstains. |
| **Prompt routing and chaining** | A router classifies the input and dispatches to a specialized prompt. Closest existing treatment of trigger matching as a design problem. | Routing is exclusive: one branch is chosen per input. Skills compose, and several may apply at once. The router is designed per application, so nothing transfers to the design of an individual unit. |
| **Software modularity** | Decides what becomes a unit by cohesion and coupling, which is the same allocation question. | Dispatch is deterministic and the caller is explicit. Here the caller is a model's judgment about what the session is doing, and a unit that does not fire leaves no trace. |
| **Checklists and clinical protocols** | Packages behavior for a named moment with an explicit trigger, the human precedent for moment-scoped instruction. | The trigger fires when a person observes an external event. Nothing in the design covers a case where the actor decides for itself whether the moment has arrived. |

**The gap:** no existing approach decides which behaviors become separately triggered units of instruction for an LLM, under conditions where dispatch is the model judging a description rather than a caller selecting a branch or a retriever returning top matches, where units compose rather than route, and where a unit that fails to fire is silent.

---

## The Options Considered

**1. All behavior carried as always-on instruction vs. behavior split between always-on instruction and skills**

Carry every behavior in the traveling prompt so that it is present in every session, or split it so that what must hold throughout stays there and what fires at one moment becomes a skill. The always-on option is simpler: one artifact, read once, nothing to match, no possibility of a behavior failing to load. It was rejected because instruction-following degrades as density rises, and an always-on artifact has no way to mark that an instruction applies at one moment only. An instruction added to cover a moment-specific behavior spends attention in every session where that moment never arrives, and the instructions that pay for it are the ones further down. The split is not free. A skill that fails to fire leaves no trace, where an instruction that was present at least had its chance to be followed.

**2. One skill per behavior vs. one skill covering a family of related behavior**

Give each behavior its own skill so that every description is narrow and matches precisely, or group related behavior into a single skill that adapts to the situation it is applied in. Narrow skills match more precisely one at a time. Splitting by default was rejected because every installed skill spends its description at session open whether or not it fires, and selection accuracy falls as the candidate set grows: splitting buys precision on one description and charges it to every other skill's chance of firing. Grouping is not free either. A grouped skill loads its whole body when only part of it applies, and its description has to cover a family without becoming vague enough to match everything.

---

## The Chosen Direction and Why

**Why behavior is allocated by when it applies, not by what it is about**

The split between the traveling prompt and a skill is decided by one question: must this hold through the whole session, or does it apply at an identifiable moment. Allocating by subject would group everything about drafting in one place and everything about closing a session in another. That reads tidier and produces ambient instruction that is present when it cannot act, and skills asked to hold a posture that has no moment to fire at. Timing is the property that decides cost. Behavior that must hold throughout has to be present throughout and its cost cannot be avoided. Behavior needed at one moment can be held back, which makes its only real question whether the moment can be described well enough for the skill to fire.

**Why a skill covers a family of behavior rather than a single behavior**

Every installed skill charges its description against the same session-open budget, and match reliability falls as the number of candidates rises, so the count of skills is a cost paid by every skill including the ones that fire. A family grouped under one skill spends one description where the split version spends several. Splitting a family also inserts a judgment before the trigger. One skill covering a moment fires on that moment. Several skills covering the same moment fire only after something has decided which of them applies. That decision falls on whoever is present when the moment arrives: the model, when the split runs along a property of the model's own output, or the practitioner, when the split runs along which artifact to reach for. In both cases the judgment is made under the load the skill exists to relieve, and it is made before any skill body has loaded, so nothing the skill carries is available to inform it. This cost is independent of the description budget. A split whose descriptions were free would still fail at the point where someone has to classify first.

The grouping holds only while the family shares a moment. When one member fires at a different moment from the rest, a single description has to name two moments and matches well for neither, which is worse than the split it was meant to save.

**Why a trigger description is written from the vocabulary of the moment, not from the skill's contents**

A description is matched against what the session appears to be doing, which reaches the model as the words the practitioner has been using. A description written from the skill's contents describes the skill accurately and shares little surface with the session that needs it. The lever available to the author is overlap with the language of the moment, not accuracy about the skill. An RFM project has an advantage here that a general skill author does not: the glossary fixes the vocabulary a practitioner uses, so the words that will be present when a skill is needed are known rather than guessed.

---

## The Boundaries

**Not the design of any individual skill.** Each skill has its own reasoning document, which owns why that skill exists, what it covers, and what it must not do. This module owns only what holds across skills. A commitment that would change if one skill changed belongs in that skill's document.

**Not the allocation of content within the traveling prompt.** This module owns one side of the boundary: whether a behavior belongs in a skill. What the traveling prompt should carry and how it should be organized is reasoned about in the prompts documents. A finding here that would change the traveling prompt's internal design belongs there.

**Not a general theory of skill design for LLMs.** The direction taken here depends on a project having a curated vocabulary that a trigger description can be built from. A project without one has to reason about trigger design differently. These claims hold for a project applying RFM, not for skill authoring at large.

---

## The Open Questions

**[OQ-SILENT] Can a skill's failure to fire be observed?**

A skill that does not match leaves no record. The session proceeds, the behavior is absent, and nothing distinguishes that from a session where the skill was never needed. Without a way to see a non-fire, every question about trigger quality and skill count is answered by impression. Resolution paths exist and none has been tested.

**[OQ-COUNT] How many skills can a project install before their descriptions cost more than the skills save?**

Every installed skill spends its description at session open, and selection accuracy falls as the candidate set grows. Both effects are established. Where they cross for a given project is not, and the answer would change how aggressively behavior is grouped into families. It is the same unmeasured quantity named in `[AS-AMBC]` and `[AS-MATCH]`, and it cannot be settled while `[OQ-SILENT]` is open.

**[OQ-FORCE] Which skills need a mechanism outside themselves to guarantee they fire?**

A skill whose absence is silent and costly is not made reliable by a better description alone. Something always-on can name the moment and force the load, which reintroduces the ambient cost that moving the behavior into a skill was meant to avoid. Whether that trade is worth making, and what property of a skill decides it, is unresolved.

**[OQ-POSTR] Does the register that makes a skill act also push the model toward executing rather than co-authoring?**

A skill body is written as procedure: named steps, imperatives, checks. That register is what makes it take effect once loaded. It is also the register of an instruction handed to a tool, and RFM depends on the model holding a posture that questions and pushes back. Whether loading procedural text at a moment shifts that posture, and whether a skill can be written to act without paying that cost, is unknown.

---

## Hard Lessons

**[HL-DESCH] A skill description written while editing the skill records what changed instead of when to load it.**

A description has to be supplied at the moment a skill is saved, which is the moment its author is holding what just changed rather than what the skill is for. The result is truthful, well formed, and names no trigger, so it passes any check that reads the description on its own terms. The skill then stops matching and nothing reports it. The failure is invisible from the author's side, because the skill looks finished and its description is accurate.

**[HL-BODYC] A skill body is not documentation. It is text loaded into the context of the response it governs.**

Language failures in a reasoning document cost a future reader some clarity. The same failures in a skill body sit inside the context of the response being written while that response is being written, so the skill's own prose is an input to the work it is meant to improve. Skill bodies were treated as documents that describe behavior, and were held to the standard that applies to documents someone reads later.

---

*module_reasoning // [living]*
*skills carry behavior that fires at a moment. the rules file carries what must hold throughout*
*the reasoning comes first. the skills follow*
