# RFM: Incubating Ideas
*Captured end of session // not yet ready for document capture*

---

## What this file is

This file is public because transparency about work-in-progress is consistent with RFM's own principles. If you are encountering RFM for the first time, start with the README and `RFM_top_level_reasoning.md`; this file shows the methodology's thinking-in-progress, not its conclusions.

These are ideas that surfaced during a refining session but are not sharp enough yet to capture in the methodology documents. They are candidates, not conclusions. Read this file into a future session when the topic feels relevant.

**On signal counts:** each entry carries a signal count: the number of independent observations from distinct contexts (different LLMs, different domains, different problem types) that have surfaced the same idea. Repetition within the same session or LLM does not increment the count. Multiple independent signals on the same candidate should trigger a document home conversation. Two independent contexts is sufficient to propose; three should trigger action regardless.

---

## A. The LLM as bridge between universal and domain-specific

The co-author relationship may be the mechanism by which universal RFM principles become domain-specific operational practice, not through templates or examples provided by the methodology, but through a targeted conversation grounded in the specific reasoning document just built. The output belongs to the project, not to RFM. This keeps the methodology universal while making it immediately actionable in any domain.

**Why not captured yet:** not yet tested or named precisely enough. The idea is a hunch, not an observation.

**Possible home when ready:** Open Question 3 (onboarding), or a new open question in `RFM_top_level_reasoning.md`.

**Signal count: 1** *(origin session, pre-dating the counter)*

---

## B. The reasoning document as what makes something safely routine

External feedback suggested RFM has low value for "routine" work. The response: the routine had to start somewhere. The reasoning document is what allows something to safely become routine, because the assumptions and boundaries are explicit enough that everyone knows what conditions the routine depends on. When those conditions change, the reasoning document is what tells you that, and why.

**Why not captured yet:** sharp as a conversational observation, not yet shaped into a methodology-level insight.

**Possible home when ready:** may connect to A; both are about the methodology's role in the transition between high-stakes original thinking and confident downstream execution. Could become a new open question, or strengthen Assumption 11 (the virtuous cycle).

**Signal count: 1** *(origin session, pre-dating the counter)*

---

## Note on relationship between A and B

They may belong together. Both describe the LLM and the reasoning document as the connective tissue between original high-stakes reasoning and confident downstream execution. If they converge, the combined insight may be strong enough to capture as a single open question or as an addition to Chosen Direction.

---

## D. Dreaming (Anthropic Managed Agents) as external validation of the curation problem

Anthropic's "dreaming" feature for Managed Agents (May 2026) is a scheduled process that reviews past agent sessions, extracts patterns, and curates memory between sessions, including automatic memory updates. The diagnosis behind it is identical to RFM's founding curation assumption: memory left to accumulate without periodic review degrades. The solution differs sharply (automated vs. deliberate) and that difference is where RFM's position must stay sharp. Automated curation is the failure mode RFM names, not a solution, because compression is always structural and requires human judgment. But the fact that Anthropic built infrastructure around this problem is meaningful external signal that AS-CDNO is pointing at something real and generalizable, not a preference of its authors.

**Why not captured yet:** single source, single context. The validation is real but the implications for RFM's own curation design (whether the deliberate/automated distinction needs to be more explicitly argued in the documents) require more signal before warranting a document change.

**Possible home when ready:** AS-CDNO in `RFM_top_level_reasoning.md`; the assumption would carry a stronger grounding sentence. Or the Landscape in the same document if the automated-vs-deliberate tension becomes sharp enough to warrant a named row.

**Signal count: 1** *(Anthropic Managed Agents blog, May 2026)*

---

## E. RFM translation to a new LLM environment fails predictably at the derivative chain

A quick-and-dirty RFM translation to a new agentic environment under time pressure produced a working result: the derivative chain held well enough to generate a working agent specification from two reasoning documents within four hours, in a non-software domain, with a non-technical operator. But two structural drifts entered undetected:

The operational document was repositioned as independent infrastructure rather than a derivative of the reasoning document, granting the agent explicit autonomy to modify it without a reasoning document touch. This inverts the derivative chain at the point most likely to cause silent failures.

A fictional bash script entered the operational document, referencing files and commands that do not exist. It reads as executable infrastructure. It is not.

Both failures share a common shape: under time pressure, the operational layer is where the derivative discipline slips first. The reasoning structure holds. The connection between reasoning and operational breaks.

**Why not captured yet:** single deployment, single context. The pattern feels robust; a second independent signal would confirm it.

**Possible home when ready:** Hard Lessons in `RFM_top_level_reasoning.md` under execution practice, or a behavioral instruction in the traveling prompt about translation verification checkpoints.

**Signal count: 1** *(Antigravity IDE, organizational behavior analysis domain, real deployment under four-hour delivery pressure, May 2026)*

---

## F. The human's collaboration contract needs to be named at session start

When the human doesn't state the collaboration loop structure explicitly before work begins (what counts as a draft, what counts as a file write, what order is expected) the LLM fills the gap with its own assumptions. Those assumptions are often wrong, and the correction comes after drift has already occurred rather than before it.

This is distinct from engagement level (covered in the human prompt) and from thinking out loud (same). It's about the working agreement for the session: comparison intent, review loop, ordering. The LLM cannot reliably infer these from the work itself.

**Why not captured yet:** single deployment, single context (Codex). The failure is human-side and travels with the human, but one observation is insufficient. A second independent signal (same gap surfacing in a Claude collaboration) would confirm it.

**Possible home when ready:** human prompt, as a new entry between "be engaged or don't start" and "read the first few exchanges for posture." Or a new practice in "To Internalize Next."

**Signal count: 1** *(Codex deployment, May 2026, human-side failure identified by Codex LLM self-assessment)*

---

## G. Some behavioral instructions ask for a disposition, not knowledge, and dispositions do not survive a session boundary

A session produced two genuine fixes to derivation discipline: a sequential gate for sibling-artifact contamination, and a rule against cross-document ID references. Both were caught only because the human noticed the LLM's own draft violating a principle the LLM had itself stated minutes earlier, in the same session, with the relevant reasoning still active in context.

The distinction this surfaced: written content survives a session boundary cleanly. A Hard Lesson, once in a document, is genuinely available to the next session, regardless of which LLM reads it. A standing disposition to apply a check unprompted, before being asked, does not survive the same boundary. "I now know to check this" is true only for the remainder of the session that earned it. The next session does not inherit the habit, only the instruction to have the habit, and an instruction is not the thing it describes.

This may explain why the traveling prompt's existing acknowledgments that instruction reduces but does not guarantee behavior, already present for co-author drift, are not edge cases but close to the rule. Most of what a behavioral prompt asks for is disposition, not content, and disposition is exactly the category that does not transfer between sessions the way the document hierarchy assumes derivatives transfer.

A possible distinguishing test: does verifying that an instruction was followed depend on the LLM's own self-awareness in the moment, or can it be checked from outside, after the fact, by something that is not the LLM's own judgment? Instructions that fail this test may not be improvable through better phrasing. The fix may need to live outside the LLM entirely, as a mechanical gate, rather than inside a prompt asking the LLM to remember.

**Why not captured yet:** the distinction is sharp, but its implication, that a class of existing traveling prompt instructions may be permanently unreliable rather than temporarily under-specified, is large enough to need testing against the rest of the prompt system before it reshapes anything. One session, one set of examples.

**Possible home when ready:** a new Open Question in `RFM_prompts_reasoning.md`, adjacent to the existing fresh-LLM test and trigger-conditions questions, since both already probe the limits of what instruction alone can guarantee. Could also sharpen `RFM_prompts_reasoning.md`'s Hard Lesson on the two directions of co-author drift, if the generalization holds: not just co-author drift, but a named category of disposition-dependent instructions across the whole prompt system.

**Signal count: 1** *(this session, RFM-on-RFM derivation work)*

---

## H. A reliability-classification check, distinct from both existing sweeps

Following directly from G: if some behavioral instructions ask for something that cannot reliably hold across sessions, the methodology may need a way to identify which instructions are in that category before relying on them.

The shape that emerged in conversation: sort every behavioral instruction in a prompt artifact into one of three classes. Mechanizable now: already deterministic and checkable by a script, no LLM judgment required, for example a rule against a specific character. Checkable after the fact: not deterministic, but verifiable by a separate pass, human or LLM, reading the finished artifact rather than relying on the producing LLM to have caught it mid-task. Genuinely judgment-dependent: no external check exists yet, the instruction asks for something closer to an instinct than a rule, and the honest position is to name it as a structurally fragile point requiring ongoing human attention, not to keep refining the wording in the hope that better phrasing closes the gap.

This is not a fit for either existing sweep. The structural sweep asks whether content sits at the right level of the hierarchy. The language sweep asks whether content is expressed clearly. This check asks neither question; it asks whether a given instruction, however clearly expressed and however correctly placed, is the kind of thing an LLM can actually be relied on to do unprompted. It is closer in cognitive mode to the structural sweep's architectural judgment than to the language sweep's close reading, but it operates on instructions rather than on reasoning content, which neither sweep currently does.

**Why not captured yet:** the idea exists at the level of a sound kernel, not a designed artifact. Whether it becomes a third sweep, an extension to the structural sweep's scope, or a one-time audit rather than a repeatable artifact, is undecided. It also appears to be a low-frequency need: it surfaced because RFM's own prompt artifacts are unusually dense with instructions about LLM self-monitoring, a concentration unlikely to repeat in most domain projects built with RFM, where reasoning documents describe a domain rather than an LLM's own behavior. Worth holding as named and real, not worth treating as urgent.

**Possible home when ready:** `RFM_prompts_reasoning.md`, as a fourth landscape entry or a new option in the Options Considered, evaluated against the existing two-sweep design the same way any new corrective artifact would be. Should be read alongside G; if G's Open Question resolves toward "yes, a distinct unreliable-instruction category exists," H is the corrective mechanism that question would point toward. If G resolves the other way, H may not be needed at all.

**Signal count: 1** *(this session, RFM-on-RFM derivation work)*

---

## I. Splitting a claim's evidentiary support by sub-claim, not by claim

When an assumption or claim bundles two sub-claims with different evidentiary strength, writing one confidence level across both produces epistemic flatness even when the words are hedged correctly for the claim as a whole. `[AS-FORM]` in `RFM_instruction_design_reasoning.md` splits its own claim (instruction form moves role) into an activation half, grounded in outside research, and a role half, grounded only in the project's own session record, and states each separately rather than writing one blended sentence. This reads as a general drafting technique rather than an incident specific to that entry: name the sub-claim, then its evidence, repeated for each sub-claim, instead of one summary confidence statement for the whole.

**Why not captured yet:** single instance, drafted once inside one assumption. Not yet tested as a deliberate technique applied on purpose to a different entry.

**Possible home when ready:** `RFM_skill_drafting_operational.md`'s language-compliance guidance, or a new discriminator alongside the existing epistemic-flatness failure type in `RFM_operational.md`'s Failure Taxonomy.

**Signal count: 1** *(this session, `[AS-FORM]` in `RFM_instruction_design_reasoning.md`)*

---

## Note on relationship between G and H

G names a problem: some instructions ask for something that does not survive a session boundary. H names a possible response: a way to identify which instructions are in that category before depending on them. G should be evaluated first. H is only worth designing if G holds up under a second independent signal.

---

*Not versioned. This is a working note, not a methodology artifact.*
*Discard once the ideas have found their home or been consciously dismissed.*
