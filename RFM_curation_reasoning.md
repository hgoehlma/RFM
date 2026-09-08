# Reasoning-First Methodology: Curation Reasoning Document
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

Curation is what keeps a reasoning document true after the session that wrote it. Its failures share one property: they are invisible from inside the session performing them. Someone compressing an entry holds the context they are removing, so the loss is not visible to them. Someone retiring an entry infers that its situation cannot recur, and nothing in front of them tests the inference. Someone branching a module edits the child and leaves the parent carrying what the child now owns, and neither document reports an error. The individual failures are recorded. What no document carries is the design that treats them as one problem: what curation must do, why its failures escape the person best placed to catch them, and what stays checkable when the session that would notice is the session that is failing.

---

## The Assumptions

**[AS-CDNO] - Curation must be deliberate, not optional.** A reasoning document that is only visited when something forces it gradually stops being true. Deliberate return, coming back without a specific trigger, is as necessary as triggered curation. A time-triggered cadence risks becoming performative rather than genuine. Both modes must be practiced as discipline, not suggestion.

---

## The Landscape

*No landscape at this time.*

---

## The Options Considered

*No options considered at this time.*

---

## The Chosen Direction and Why

**Why curation requires both addition and reduction**

The document is kept alive through enforced curation. Not just addition but reduction. What has evolved? What can be removed? What needs replacing? A document that only grows is a document that is already dying. The pressure of constraint is a feature, not a limitation.

A healthy document expands when new signal arrives and contracts when old signal has run its course. Contraction has two legitimate forms: graduation, where an entry's reasoning still has work to do and travels to the appropriate destination; and expiry, where it no longer does and is honestly removed. Both are curation. Neither is loss.

Hard lessons earn a dedicated section, not an appendix, not an afterthought.

**Why graduation and expiry are reasoning acts, not mechanical procedures**

Graduation and expiry are reasoning acts, not mechanical procedures. The discipline cannot be reduced to a lookup table ("hard lessons graduate to assumptions" or "open questions graduate to Chosen Direction") because the destination depends on what the resolution is, not on what section the entry came from.

The prior test is the same for both: does this entry's reasoning still have a recipient? Would a practitioner encountering it change how they think or act somewhere in the current system? If yes, the reasoning must travel; that is graduation. If no, the entry expires. Version history holds the record; the active document holds only live reasoning. A document that retains entries the version history already preserves is hoarding, not curating.

For entries that graduate, the destination is determined by what the resolution is. A resolution that settles a belief about the domain becomes an assumption. One that commits the methodology to a direction belongs in Chosen Direction. One that constrains scope belongs in Boundaries. One whose reasoning is operative only within a specific module travels to that module's reasoning document. The routing question is: where does a practitioner need to encounter this reasoning for it to do its work?

The graduation act requires two steps: place the resolved reasoning at its destination, then remove the source entry. Both steps are required. An entry that has been resolved but not removed annotates the document rather than curating it, and annotation blurs the boundary between what is settled and what is not. The procedure for executing graduation is carried in `RFM_operational.md`.

**Why a graduated entry must carry its reasoning, not just its conclusion**

When an open question graduates into an assumption, the conclusion alone is not enough. A conclusion-only assumption is indistinguishable from an unexamined default. It states what is believed without explaining why it is believed or under what conditions it would break. The reasoning that produced the assumption, the evidence, the path, the conditions, must travel with it. That is what makes the entry an assumption rather than received wisdom, and what allows a future reader to test it honestly rather than inherit it blindly.

Every change to a derivative (code, prompt, operational document) begins with a change to its source reasoning document. Derivatives don't merely stay connected to the reasoning; they are created from it. That is the right order, and maintaining it is what curation means in practice.

---

## The Boundaries

*No boundaries at this time.*

---

## The Open Questions

*No open questions at this time.*

---

## Hard Lessons

**[HL-RETIRE] Retiring reasoning needs evidence that its situation cannot recur, not an argument that it should not.**

A Hard Lesson recording how to keep an embedded document map safe was proposed for retirement, on the grounds that a map should never sit inside a reasoning document at all. Those grounds were inferred from the reason the map was being extracted, and nothing tested them. The counter-case was immediate: RFM ran an embedded map for five minor versions and that was the right call at that size. The lesson was narrowed rather than retired. The same gap had already spread once before it was caught, because a later design decision had been built on a clause inside the lesson under review and treated that clause as settled.

**[HL-TLOR] Once a module exists, top-level ownership must be actively reduced.**

Branching to a new module does not automatically contract the top level. Without deliberate reduction, both layers accumulate entries about the same content; the top level drifts toward restating what the module now owns. The discipline after branching is not just creating the new module; it is returning to the top level and removing whatever the module now carries. This is a distinct step, not an automatic consequence of branching. The branching signal itself is carried as an assumption in `RFM_top_level_reasoning.md`; this lesson names what must happen after that signal is acted on.

**[HL-CPSC] Compressing a reasoning document feels like curation; it is structural change.**

Removing or condensing articulated reasoning can present as tidying up. None of those framings change what is actually happening. When reasoning is compressed, signal is lost that cannot be recovered. The distinctions that felt obvious in the session that produced them are precisely what a future reader or a fresh LLM cannot reconstruct. The danger is that compression is invisible from inside the session that performs it: the compressor holds the missing context and cannot perceive the gap they are creating.

**[HL-REPAR] Branching re-parents every derivative of the moved reasoning, and no check reports it.**

Moving reasoning into a new module changes which document is the source for everything derived from it. `RFM_operational.md` carried a graduation and expiry procedure derived from a Chosen Direction entry at the top level. The entry moved into the curation module and the procedure stayed. The arrangement was then ruled acceptable, and it was ruled, which is the point: nothing surfaced it for ruling. The structural sweep asks whether content sits at the right level, and the procedure does. The relational sweep compares a reasoning document against its operational derivative and finds them agreeing. The language sweep has nothing to read. The defect exists only in the relationship between two files that each pass alone. What catches it is asking, at the moment of the move, what derives from the reasoning being moved.

**[HL-KNEXP] Content written when its expiry is already known schedules maintenance work rather than avoiding it.**

A claim can be accurate when written and false by the next session, because the work that falsifies it was already planned when it was written. The common shape is a forward-looking clause: a sentence stating what a thing does not yet do, or what it will require, where the requirement is already on the plan. It reads as careful. It passes review as true, correctly placed and clearly written. Review lets it through for those reasons, not despite them.

The worked example is a drafting session where the LLM produced clauses of the form "this will only work once X is in place." They were accepted as sensible caution. Work on X began a few hours later. A following session reported those paragraphs as stale and needing maintenance, which pulled ripple checks into documents that only referenced them, and one compression made during that cleanup removed content that had to be reconstructed from an earlier version. Nothing in the chain was wrong on its own. The first sentence was true when written.

A condition that planned work will satisfy belongs in the plan, not in the document the plan will change. Writing it in both places makes the document a second record of the plan, and the ripple work is the price of keeping the two agreeing until the plan lands.

---

*module_reasoning // [living]*
*curation fails where nobody is looking, which is inside the session*
