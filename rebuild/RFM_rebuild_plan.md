*Interim working file for the carrier rebuild. Not part of the methodology. This folder is removed once its content has moved into tracked reasoning and operational documents.*

# RFM: Carrier Rebuild Plan

State: the plan as it stood before the first corpus scan. Items are marked **Decided** or **Proposed** (not yet agreed). Open items are listed at the end.

---

## The question being decided

How do we rebuild the set of carriers that support RFM without reproducing the existing set by drift?

Case for rebuilding from first principles: past rebuild attempts got anchored in the existing documents and reproduced what exists instead of rebuilding.

Case against: the existing carriers encode hard-won lessons, and a rebuild from scratch risks losing them. The comparison step (step 4) exists to answer this.

---

## Reading rule

**Decided.** Inputs for steps 1 to 3: `README.md`, `RFM_top_level_reasoning.md`, `RFM_operational.md`, `RFM_carrier_types.md`, and the human's statements. No other document in the corpus is read before step 4.

**Decided.** The traveling prompt (the project instructions) stays as it is during the rebuild. It is not exempt: step 4 compares it against the inventory like every other carrier.

**Decided.** The `rfm-unslop` skill stays in use for all rebuild writing. When the unslop carrier itself is rebuilt, drafts produced under it are not evidence that it works. It is judged against the failures it counters.

---

## Steps

**0. Setup.** **Decided.** A tracked `rebuild/` folder holds all interim work. Removing it is the last step, and it happens only after everything worth keeping has moved into tracked reasoning and operational documents in step 5. Deleting the folder earlier is how the rebuild's reasoning would disappear.

**1. Approach.** **Proposed.** The LLM writes a one-page statement of RFM in its own words from the permitted inputs. The human corrects it. Done when the human recognizes it and nothing load-bearing is missing.

**2. Failures, then behaviors.** **Decided:** failures are inventoried before behaviors. **Proposed:** one step with an internal order, not two phases. First the failures, then one counter-behavior per failure, in the same table.

Failure sources (**Proposed**):
- Top-down: for each thing RFM requires (the two phases, the crossings between postures, curation, pressure mode, derivation without the human, the release trial), ask how it fails. This source is needed because a list built from memory favors failures that left evidence. Co-author failures leave none.
- Memory and recorded hard lessons.
- Document failures: reuse the Failure Taxonomy in `RFM_operational.md`. It is a list of failures, not a carrier. Collaboration and process failures have no single inventory yet, and most of the new work is there.

Per behavior, record: who is forced to perform it (only where forced, see step 3), when it is needed (phase, mode, moment), and the routing properties the carrier types file uses: can a miss be checked afterwards from outside; is the cost of a miss severe and nameable in advance; does it reduce to a search; can the moment be triggered, or does it arrive unannounced.

Exit (**Proposed**): stop when new failures stop producing new behaviors. The aim is to make the gaps visible, not to be complete.

**3. Mapping.** **Proposed.** Route each behavior along the carrier types file's three axes: carrier type, form, gating. Output: an allocation table, plus behaviors with no good carrier, kept as named gaps.

**Decided:** the question is who *should* perform each behavior (LLM, human, mechanical), not who does today. **Proposed:** step 2 records the actor only where it is forced (intent and confirmation can only come from the human; a check that reduces to a search can be mechanical). Step 3 decides the rest, because the human and mechanical checks are carrier types, and assigning them earlier would make the carrier choice before the mapping.

**4. Comparison.** **Proposed.** The first point where the existing carriers are read, as a harvest source, not a template. What do they carry that the inventory missed (back to step 2)? What sits in the wrong carrier? What is duplicated?

**5. Distribution.** **Proposed.** Place the why in reasoning documents and the what in operational documents. The carrier choice for a behavior is itself reasoned, so mapping produces reasoning content, and it gets placed here. Reorganizing how information is laid out across documents is a joint decision.

**6. Priority and build order.** **Proposed** criteria: how much a carrier helps build the others; the severity of the failures it covers; what the first external trial needs (carriers must work for a model reading only the handed set).

---

## Corpus scan

**Decided.** Once the plan is settled, a subagent scans the corpus to test whether the plan fits it. Only plan-level findings come back. The subagent's reading stays in its own context.

---

## Open items

1. Scope: which carrier instances are in the rebuild.
2. Rebuild sessions: what each session may read, and whether the startup and closeout procedures apply.
3. Exit conditions for each phase.
4. Changeover: the old carriers stay live during the rebuild. When and how does a new carrier replace an old one, all at once or one at a time?
5. The project rule that a prompt or skill changes only after the reasoning document behind it has changed, and how that fits the build order.
