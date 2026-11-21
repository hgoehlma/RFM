# RFM: Curation Skill, Reasoning
`v1.0.0` // `module_reasoning` // [living]

---

## The Problem

A reasoning document says why things are the way they are now. Over time its entries stop doing that: a question is answered, a failure is fixed by a change, the reason an option lost no longer holds, a module takes over part of the reasoning. An entry that no longer does its section's job still reads as reasoning, and a later reader takes it as current. A document that keeps such entries grows into a record of how it got here, which is what it was meant to replace.

What goes is decided by whoever holds the content, and they judge badly in both directions. They keep entries that no longer do their job. When they do shorten, they hold the context they are removing, so they cannot see when two things that only look alike have been merged into one and the distinction between them lost.

Moving reasoning into a module has the same blindness. The parent keeps stating what the module now owns, and what was derived from the moved reasoning stays attached to the old place. Each document reads as correct on its own.

## The Assumptions

**[AS-KEEP] - Whoever looks for a reason to remove an entry finds a reason to keep it.** Whatever was once argued for still carries its argument, and an entry with a real failure behind it always has one. A review that asks entry by entry whether something should go therefore keeps nearly everything. This breaks if reviews that ask that question do remove what no longer does its job.

**[AS-GAP] - A wrong removal leaves a gap that someone notices.** The default leans toward removal because of this. One passage can carry part of another's meaning without referring to it, such as an example that shows what a principle covers. When the first is cut, the second still reads complete. Nothing refers to the cut passage, so the rename skill finds nothing either. This breaks if a passage turns up that lost part of its meaning to a cut nobody questioned.

## The Landscape

What do people reach for when a living document's entries stop being true and nobody removes them?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Decision records that are superseded, never changed | Keeps every decision and marks an old one as superseded, linked to its replacement | The document becomes the record of how it got here. A reader has to find what holds now among what used to hold. |
| Expiry rules | Removes or flags content once it reaches a certain age or is of a kind meant to be short-lived | Age and kind don't show whether an entry still does its job. An old hard lesson can be live and a recent note dead. |
| Review dates and owners | Gives each page an owner and a date by which it must be reviewed, and flags pages past it | It makes the review happen. The reviewer still decides what stays, and keeps what was once argued for. |
| Automatic consolidation | An LLM merges similar entries into summaries on a schedule | It merges by how alike entries look, which is where distinctions get lost, and nobody reads the result against what it replaced. The loss grows with each round. |

**The gap:** none of these asks of each entry whether it still does its section's job, and none allows for the fact that whoever judges is the one holding the content.

## The Options Considered

**Brakes on every cut.** Every cut is treated as a structural change: named as one, with evidence that its situation cannot recur and a statement of what it loses. Rejected because each entry can still be argued for, so nearly every entry is kept and documents only grow.

**A sweep afterwards for what a branch left behind.** A sweep reading the parent and the module can see the parent restating what the module owns. Rejected because it cannot see something derived from the moved reasoning that stayed attached to the old place, since each file passes on its own. That has to be asked at the move.

## The Chosen Direction and Why

**Why an entry stays only while it does its section's job**

Earlier versions of a document are kept outside it, in the project's version history. The document holds only what is true now, and each entry is there because its section gives it a job for a reader now. When it stops doing that job, it leaves the section.

The job differs by section, and so does how fast an entry stops doing it.

The test applies to what an entry contains, not to its heading. An entry can hold reasoning beyond what its title names, and an entry removed for its title takes that reasoning with it. An entry that repeats what another already says does no job of its own.

**Why the default leans toward removal**

Whoever decides holds the content, and everything once argued for still reads as worth keeping. Asking of each entry whether there is a reason to remove it therefore keeps nearly everything. The question is turned around: an entry stays when its job for a reader now can be named, and goes when it cannot. A wrong removal usually costs little. Someone notices the gap, and the reasoning is written again from what is true now or recovered from the history.

**Why a resolution goes where it now does its job, with its reason**

A hard lesson is resolved by a change. The failure then becomes the reason for that change in the Chosen Direction, and the lesson leaves. Where a change can fix a failure right away, no lesson is written: we make the change, and the failure is its reason.

An answered open question goes where its answer now does a job. That depends on what the answer is, not on which section the question came from. An answer that settles a belief becomes an assumption, with the condition under which it breaks. One that commits to a direction goes to the Chosen Direction, one that limits the scope to the Boundaries, and one that holds only inside a module to that module's document.

The reason travels with the resolution. A conclusion on its own reads as a default nobody examined, and a later reader cannot disagree with it. The entry leaves its old place in the same change, because left there it still reads as open. Passages that hedged on the question while it was open are then stated as firmly as the answer holds.

**Why the brakes sit only on conflation and on a live hard lesson**

Shortening is good when what it drops is no longer needed. It goes wrong when two things that look alike are merged into one: a distinction a reader still needs disappears, and the shorter text reads as complete, so nobody looks for what is missing. Old and new text side by side do not show this. Whenever a cut merges entries or sentences, the one proposing it therefore names what was distinct about the things merged and says whether that distinction still matters, and we agree on it before the cut is made.

A hard lesson removed while its failure can still happen is the other loss that does not announce itself. Nobody searches the history for a lesson they do not know existed, and the mistake comes back. Removing a hard lesson therefore names the change that fixed its failure, or why the failure can no longer happen. Where neither can be named, the lesson stays.

Everywhere else a cut goes ahead on the job test alone.

**Why a branch takes what derives from it**

When reasoning moves into its own module, the parent goes on saying what the module now owns unless someone removes it. The parent's copy does no job the module's does not, so it leaves in the same change that creates the module.

What was derived from the moved reasoning now has a new source. A document's sources are the branch of the hierarchy above it, so a derivative left where it was derives from reasoning that is no longer there, while each file still reads as correct on its own. The question is therefore asked at the move: what derives from this reasoning? Whatever does moves into the module's branch with it.

**Why curation is its own skill, loaded at the proposal**

Whether something goes, and where, is decided in conversation before anything is written, and a removal may write nothing at all. A skill that loads when writing starts arrives after the decision. Curation is therefore its own skill, and it loads when either of us proposes to cut, shorten, retire, graduate or branch. The proposal marks the moment, so nothing else has to force the load.

## The Boundaries

**Not finding what is ready to go.** Candidates come up while drafting, in a sweep or the research check, or when a rename leaves an entry with nothing live. This skill acts once a cut, a graduation or a branch is proposed, from wherever the proposal came.

**Not the references a change leaves.** Other documents that still name a removed or moved entry are found and fixed by the rename skill.

**Not how new content is written.** Where a resolution lands is decided here. How the text reads there, and any pointer the parent keeps after a branch, follow drafting.

**Not logs or the handover note.** A log records what happened and is corrected by adding to it. The handover note is written fresh at every close. Curation works on the documents things are derived from.

## The Open Questions

**[OQ-NAMING] Does asking for an entry's job lead us to cut, or do we name a job for everything?**

Turning the question around assumes that naming a live job is harder than finding a reason to keep. Whoever holds the content may find a job for every entry as easily. If documents keep growing under the job test, the push toward removal needs something other than a question answered by whoever holds the content.

**[OQ-UNNAMED] Does a shortening made while revising reach the skill?**

The skill loads at a proposal. A merge made in the middle of revising a passage is not proposed as a cut, so nothing loads the skill, and the old and new text that drafting shows do not show a lost distinction. If conflations keep arriving this way, the brake needs a way in at the revision itself.

**[OQ-CROSSBRANCH] What catches a derivative outside the branch of the reasoning it depends on?**

At a branch, the skill looks below the moved reasoning. A derivative in another branch that depends on it is not there, and stays attached to reasoning that has moved. Whether it is rare enough to leave to a sweep, or needs its own step at the move, is not known.

## The Hard Lessons

*No Hard Lessons at this time.*

---

*curation skill reasoning // [living]*
