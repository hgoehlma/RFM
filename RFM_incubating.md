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

## K. Verifying a claimed absence or precedent against git history, not just current file content

Checking git log, log -S for term additions or removals, log --all -p for full history including discarded commits, log -p on a specific commit, before asserting a document lacks something or that a pattern is established, caught two real findings this session that current-file grepping alone would have gotten wrong. A claimed stale cross-reference turned out to exist under a different word form ("dilutes" rather than "dilution") and wasn't stale at all. A genuine version-bump precedent contradicting a stated convention (a module branch bumped minor, not major) was found only by checking history, and it grounded the rename that followed. Current-state search tells you what exists now; it can't distinguish "never happened" from "happened and was worded differently," or show how a convention has actually been applied over time.

**Why not captured yet:** single session, three uses. No evidence yet that this is a deliberately reused technique across sessions rather than this session's own approach.

**Possible home when ready:** an extension to `[R-VERIFY]`'s failure-shape list in the handover rules file, or a new discriminator in `RFM_instruction_design_reasoning.md` if it generalizes beyond this one project's git-backed handover structure.

**Signal count: 1** *(this session, RFM-on-RFM work)*

---

## J. Citation as hedging: a reference to another document added to justify a claim that was already true without it

Recalled across multiple past drafting sessions, not pinned to one instance: a reasoning or operational document states a claim, then adds a pointer to a sibling document, most often the glossary, as if the citation is what makes the claim hold. The claim was already correct. The citation performs support rather than providing it.

Whether this is a distinct failure or already covered by the Language family's existing curation-failure type, "text that does not earn its place... repetition of reasoning stated elsewhere that adds no signal," in `RFM_operational.md`, is unresolved. A citation added purely as decoration may already be that bullet's territory, not a gap next to it.

**Why not captured yet:** no grounding incident. What exists is a recalled impression across unspecified past sessions, not a caught instance with the actual before-and-after in hand. The taxonomy's own families are added on demonstrated failure, not argument; the same bar should apply here before this becomes a Hard Lesson.

**Possible home when ready:** `RFM_skill_drafting_reasoning.md`, near `[HL-PCSKIP]`, as a Hard Lesson, if a real instance is caught and the overlap question above resolves toward distinct. Otherwise may fold into the existing curation-failure type with no new entry needed.

**Signal count: 1** *(recalled pattern, unspecified prior sessions, not yet caught in the act)*

---

## L. An approved removal carries content the approval never named

A session proposed removing an open question that had been answered, and the human approved. The open question's entry also held a survey of precedent, three cases of RFM specifying an artifact at different strengths, which was reasoning in its own right and was deleted along with the question it sat under. The approval was for removing the question. Nothing in it ruled whether the survey graduated to a destination or expired, which the ripple-check skill requires before a removal. The shape is that an approval names a target and the target has contents, and the contents travel with it silently because the removal is executed as one act.

**Why not captured yet:** one occurrence. Whether this is a distinct failure or an instance of the ripple-check skill simply not being followed is unresolved. It would be distinct if the approval itself is what makes the contents invisible, rather than the model skipping a step it knew about.

**Possible home when ready:** an extension to the ripple-check skill's step 3, or a Hard Lesson in `RFM_top_level_reasoning.md` if it recurs outside removals.

**Signal count: 1** *(this session, removal of an answered open question)*

---

## M. Red team aimed at the session's own conduct rather than its content

The human asked for a red team of the session's thinking at the point the drafting was finished. Three of the four findings were about the reasoning just written. The fourth was that the session had executed a removal without ruling graduation against expiry, which is a procedural violation by the model rather than a flaw in any document. That finding is the one that produced a fix in the same session. The candidate is that pointing a red team at how the session conducted itself, not only at what it produced, reaches failures no content review asks about.

**Why not captured yet:** one occurrence. The prior session's red team was checked before naming this a pattern; it was aimed at the plan's content, and the self-correction in it was about a finding rather than about conduct. So there is no second instance.

**Possible home when ready:** `RFM_sweep_reasoning.md`, if it turns out to be a distinct sweep target, or the traveling prompt if it belongs as an ambient posture at the end of drafting.

**Signal count: 1** *(this session, RFM-on-RFM work)*

---

## N. A reasoning document can teach a later session the error it contains, which the session then produces as its own reasoning

This session proposed that instructions be delivered coarsely by default and finely only where the partner cannot be relied on to notice. The human rejected the framing: it makes execution a tolerated concession and collaboration the real work, when both parties execute constantly. Reading afterwards found `RFM_top_level_reasoning.md` asserting that pressure mode is "not a degraded version of the methodology" and then defining it as what is invoked when the full discipline becomes "locally unacceptable". The document claims parity and encodes concession. The model produced the same error earlier in the session without having read that passage in this session.

The candidate is a direction of contamination the derivative chain does not describe. The chain assumes a reasoning document is a source a session derives from well or badly. Here the document is the source of a specific wrong belief, and the session reproduces it with no sense of having read it anywhere. An error in a reasoning document is not only wrong on the page. It is instruction for whoever reads it next.

A distinguishing test, if this is looked at again: does the session reproducing the error cite the document, or produce it as its own reasoning? Citation is ordinary derivation and normal review catches it. Uncited reproduction is this candidate, and nothing currently looks for it.

**Why not captured yet:** one session. The second instance, that an earlier session took the framing from the document, is inferred from the match rather than observed. Entry E covers derivative-chain failure on translation to a new environment and may be the same phenomenon running the other way; that relationship is unexamined.

**Possible home when ready:** Hard Lessons in `RFM_top_level_reasoning.md`, or the curation module if it becomes an argument about what an uncorrected error costs over time.

**Signal count: 1** *(this session, RFM-on-RFM toolkit work)*

---

## O. Writing the session's framing to a scratch note before reading the document set

The human stopped the session before a planned read and asked that the reasoning be written to a scratch file first, on the grounds that reading would compress what had just been arrived at. The note was written. The documents were then read with contradictions recorded as contradictions rather than resolved toward the document, and the read produced a correction to the session's own conclusion rather than an absorption of it.

What the mechanism protects is new framing, before it has vocabulary of its own, against vocabulary that already exists in the document set. The failure it prevents is not forgetting. It is recognition. An idea that resembles something already written down gets filed under the written thing, and the difference between them is what disappears. This session has a named instance: the distinction between execution posture as a condition and execution posture as a property of an act would have been lost to the existing two-mode design, which covers only the condition.

**Why not captured yet:** one occurrence, and it was the human's intervention rather than a mechanism the project had. Whether it earns its cost on an ordinary session, or only when a session has produced framing that exists in no document yet, is untested.

**Possible home when ready:** `RFM_sweep_reasoning.md` if it becomes a named practice, or the human prompt, since the intervention came from the human and the judgment of when it is needed may be the human's to make.

**Signal count: 1** *(this session, RFM-on-RFM toolkit work)*

---

*Not versioned. This is a working note, not a methodology artifact.*
*Discard once the ideas have found their home or been consciously dismissed.*


## P. A pre-check finding can meet two failure families, and filing it under the later one reads as a pass.

The pressure mode glossary entry carried journaling. The lifespan question caught it and classified it as a future archaeology risk, so the draft went out reading as checked. It was a present language failure, "language written for the session that produced it rather than for a future reader", whose remedy is now rather than later. `RFM_operational.md` requires each artifact invoking the Failure Taxonomy to supply its own ordering rule for a failure meeting more than one description. The sweep arm has one in `RFM_sweep_operational.md`. The drafting arm, through `rfm-drafting`, has none. The incident occurred once; the missing ordering rule is verifiable in the files independently of it.

## Q. A rename's grep pattern built from the full term cannot see the collision's variant forms.

Renaming execution mode to pressure mode, the ripple check searched "execution mode" and the mode phrases. Two live hits survived in the form "execution pressure", found only when a post-write verification widened the pattern. `rfm-ripple-check` step 1 currently says to search "the changed element's name and its core subject terms". Candidate corrective: search the head word alone, so variant compounds surface.

## R. Reserving a term in the glossary does not stop its ordinary-English use in the same document set, and nothing checks for that.

"The pair" is reserved for a reasoning document and its operational counterpart. It was used this session for the human and the LLM, and stood in `RFM_human_prompt_reasoning.md` for two prompts until a grep found it. Three senses, one fenced.

## S. After a rename, sweeping the neighbouring vocabulary catches what sweeping the renamed term cannot.

Run twice by the human in one session, against different targets. Checking execution against derivation caught a false claim in a draft, that producing an artifact is execution, when the glossary assigns that to derivation. Checking "pair" caught a live document error. Candidate extension to `rfm-ripple-check` rather than a new mechanism. Evidence is one session, two instances, no prior use found in the documents.

## T. A check or search assembled from the model's own recollection of a closed list fails silently by producing a plausible finding.

The close-out map check was written with a nine-value type list recalled rather than read, wrong in two places, and reported a finding against `RFM_operational.md`'s own type. Re-running with the list read from the file returned none. Second instance in the same session of building a search from a model of the source rather than the source, after Q.
