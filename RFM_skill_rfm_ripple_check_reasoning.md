# Reasoning-First Methodology: RFM Ripple Check Skill Reasoning Document
`v0.1.3` // `skill_rfm_ripple_check_reasoning` // [living]

---

## The Problem

A structural change in an RFM document, such as a renamed term, a retired section, or graduated content, propagates inconsistently. A change made in one document leaves the old reference standing in others. Each document looks correct in isolation. The inconsistency is invisible until a session encounters the conflict and must reconstruct what changed and when.

The failure is not that practitioners miss ripple effects intentionally. It is that the scope of a structural change is not visible at the moment it is made. Without a systematic check, the practitioner works from a local view of the change and closes it without knowing what references remain active elsewhere.

This is compounded by graduation: when an Open Question resolves, a Hard Lesson metabolizes into an assumption, or a deferred item closes, the resolved content may still appear in other documents as if it were live. Graduation creates silent references that look authoritative but are no longer current.

---

## The Assumptions

The following are believed to be true. If any is wrong, the skill design needs to change.

**[AS-SCOPE]** The scope of a structural change is not knowable from the document being changed alone. It requires searching all documents that reference the changed element.

**[AS-GRAD]** Graduation is a structural change. When content moves out of a section or is resolved, references to it in other documents become stale. Graduation triggers the same check as renaming or retiring.

**[AS-GREP]** Showing grep output in the conversation is the minimum viable evidence that a check ran. A check reported without that output shown is not confirmed closed.

**[AS-OPFIX]** Operational document fixes are not judgment calls. When a reference is active and incorrect, it should be fixed in the same session. Deferring operational fixes compounds the inconsistency.

---

## The Landscape

*[To be completed in a dedicated session. Capture the prior approaches and why each is insufficient: manual cross-referencing, sweep-only detection, session-memory reliance.]*

---

## The Options Considered

*[To be completed in a dedicated session.]*

---

## The Chosen Direction and Why

A standalone RFM-specific skill that fires automatically on the trigger conditions, rather than a general-purpose ripple check skill.

**Why RFM-specific rather than general.**
The procedure references RFM-specific constructs: the document map, the session handover, reasoning documents, operational documents, graduation candidates. A general skill either omits these or carries them as dead weight for non-RFM projects. Scoping the skill to RFM sessions makes the trigger conditions and procedure precise.

**Why retire the general `/ripple-check` skill.**
The existing `/ripple-check` skill was already written for RFM documents in practice. The name implied generality that the content did not deliver. Renaming makes the scope explicit and removes the mismatch.

**Why the trigger covers graduation explicitly.**
The original `/ripple-check` skill covered structural changes and renamed terms but did not name graduation as a trigger condition. Graduation is the most common source of stale references in RFM documents: Open Questions resolve, Hard Lessons metabolize, deferred items close. These are structural changes that leave references behind. The trigger must name them explicitly or they will be missed.

---

## The Boundaries

**Not a substitute for the structural sweep.** The structural sweep finds content at the wrong level, graduation candidates, and module strain. This skill checks that a change already decided propagates correctly. Different moment, different scope.

**Not applicable to non-RFM projects.** The procedure references RFM-specific document types and constructs. Without those, the skill has no meaningful scope.

**Graduation candidates are flagged, not resolved unilaterally.** The skill surfaces candidates to the user. Resolving them is a ruling, not a mechanical step.

---

## The Open Questions

*[To be completed as questions emerge in practice.]*

---

## Hard Lessons

*[To be completed as lessons accumulate in practice.]*
