# RFM: Session Loop, Reasoning
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

A session cannot run forever. When a new one starts, the LLM knows nothing of what happened before, and the human may have been away from the work for days or remember it differently. We need the same picture of where the work stands before we go on.

Two things can go wrong at that gap. Something decided in a session never reaches a document and is lost with the conversation. Or we start the next session on the wrong thing, or forget what was left hanging.

The bridge between sessions has to carry that much and no more. A bridge that carries more becomes an archive. It is read at the start of every session, it sets a tone of record-keeping before any work begins, and it grows until nobody can work it down.

## The Assumptions

**[AS-DOCS] - A decision that reaches a document survives, and a decision that lives only in a note gets worn down.** Documents are read as the source and curated. A note is rewritten at every close, and every rewrite is a summary of a summary. This breaks if the documents stop being read as the source.

**[AS-BACK] - Something that matters comes back on its own.** A dropped item that matters resurfaces in the work, and a recurring problem gets noticed. This breaks for anything due at a fixed moment, which nothing in the work brings back in time. The carry bar keeps those.

**[AS-FIRST] - What the LLM reads first in a session sets its register.** An LLM that opens by reading back a record of what was done goes on answering in that record's register. This breaks if the project instructions turn out to outweigh what is read at open.

## The Landscape

How is work usually carried from one sitting to the next?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Meeting minutes | Record what was said | Grow with every meeting, are rarely reread, and hold decisions outside the documents they concern. |
| Backlogs and issue trackers | Keep every open item | Grow past what can be worked down. Deferring becomes the default. |
| Shift handover in a hospital | A short, current note: the state, what is due, what to watch | Close to what is needed. It carries no decisions, because those live in the patient record, and that is the part to borrow. |
| Automatic memory in LLM tools | Saves summaries without being asked | Compresses silently, with nobody deciding what stays. |

**The gap:** none of these keeps decisions in the documents, writes a short fresh note pointing to them, and holds a high bar on what gets carried.

## The Options Considered

**Every line of the note saying who decided it or which check confirmed it.** It would protect against a summary turning "discussed" into "decided". Rejected because it makes the note a record of who did what, read back first at every open.

**A cap on the number of carried items.** Rejected because it counts the pile and does not shrink it: the list fills to the cap and stays there.

**The close reporting each step's work in the conversation.** Rejected because the close becomes an audit of itself, and its length hides what actually landed.

**The repository status shown in the first reply.** Rejected because it is needed only at the close, and in the first reply it is noise before the work begins.

**Separate reasoning for the open, the close and the note.** Rejected because they do one job together, and split apart, each one gets built to guard the others.

**A working agreements template seeded with agreements from RFM's own work.** It would give every project a starting set. Rejected because the seeded agreements would be read every session as the project's own while coming from another project, and nobody removes an agreement that looks settled.

## The Chosen Direction and Why

**Why decisions go into the documents before the note is written**

The documents are where the thinking is meant to survive. Putting each decision there at the close, while it is still clear, leaves the note pointing to it rather than carrying it, so there is less for a summary to wear down.

The same pass looks for an assumption we started relying on, a question we left open, or a failure that happened and can still happen, that came up in the conversation and did not reach its document. It asks what came up, not what could be added, because an LLM asked for new entries produces them. Most sessions have none, since such things are usually written while we work on what they concern.

**Why the note is short, plain and written fresh**

It says where we are, what we agreed to do next, what is left hanging and why, and the practical tasks waiting for either of us. Written fresh, it never collects the leftovers of earlier notes. In plain prose, it can be read in a minute by the human and by an LLM that knows nothing else.

**Why the old note is read before the new one is written**

A fresh note can lose what the old one held. So the old note is read first, and each item still open in it is either carried, in its own words, or dropped aloud, under the bar below. Nothing leaves silently. Where it matters, the note says plainly what was decided and what was only discussed.

**Why the carry bar is high**

An item is carried only if we will pick it up next session, or if it is certain to become due at a moment we can name. Everything else is dropped, and said so aloud. At every close each carried item meets the bar again, and the default is to drop it. Writing an item down is cheap and feels responsible, while reading it costs every session after, so without that test an item that got in once rides along forever. An item a document already holds is not carried, because the next session finds it there.

**Why the look back leans to changing nothing**

Something that went wrong once is fixed where it happened and left at that. A new working agreement is read in every session from then on, so it is added only when the same thing keeps going wrong and catching it by hand has become more work than carrying the agreement forever. Before one is added, we look for a carrier that already says it. If one does and the thing still goes wrong, a second copy will not help; the carrier's wording, or the moment it loads, is what needs changing. That change belongs in RFM's own project, so that RFM learns where its carrier falls short and every project gets the fix. In another project the practitioner passes it on. Until RFM changes the carrier, the project can carry a working agreement that covers the gap and says it was passed on. A failure that happened, can still happen, and that no change we can make now would stop becomes a hard lesson in the document it concerns. A failure only foreseen becomes an assumption or an open question instead. Taking a working agreement away needs less: a session that went fine without it is reason enough to try. The look back also asks, now and then and above all when a new model arrives, whether something we carry is no longer needed. Each working agreement states its reason, so the question has a test. Whether one of RFM's carriers is still needed is asked in RFM's own project, where each carrier's reasoning says what weakness it makes up for.

**Why the look back names what went well, for both of us**

When the look back asks only what went wrong, the LLM fills it with its own mistakes, because its training rewards owning them. The LLM then reads as the one under review and the human as the reviewer, and the next session starts from those roles. Naming what went well, on both sides, tells us what to keep, and keeps the look back about how we worked together.

The look back also asks the human what struck them. At the close the LLM is pulled to finish, so it can take the human's answer as one more item and move to the next step. The human's view is then the only thing in the look back that nobody weighs. The LLM answers it the way it would answer anything else in the session: "nothing struck me" needs no reply, a short view gets agreement or disagreement, and a remark that shows a gap gets talked through.

**Why a second reader reads the session at the close**

The LLM cannot see its own drift from inside a turn, where the pull to deliver is strongest. A subagent that reads the whole conversation once, at the close, sees what neither of us saw while working, including drift that shows only across many turns. Because it reads only at the close, neither of us works for its remarks during the session. It says at most one thing that went well and one that would help next time, and often nothing, because a reader with the LLM's training wants to find something every time. The reader works from the transcript the app keeps, and the app sometimes leaves out text the LLM wrote before a tool call. So the reader is told that a point which looks unanswered may have been answered, and the LLM checks such a remark against the conversation before bringing it. The LLM brings its remarks into the look back, and we weigh them like anything else either of us noticed. Setting a remark aside is as good an outcome as acting on it.

**Why the working agreements file is separate and rarely changes**

The working agreements file holds this project's agreements about how we work that no document owns. An agreement about a document's subject goes into that document, where it is read whenever that subject is worked on. Working agreements change on a different rhythm from the state of the work, so they sit in their own file, are not rewritten at every close, and change only through the look back.

A working agreement reads "When X, do Y", with its reason in a sentence. The file is read at the open, and again at the close, where the look back weighs any change against it. In between, an agreement has to be recognized when its moment comes, so X is worded the way that moment will look. The reason lets either of us ask later whether the agreement still earns its place.

Working agreements stay out of the project instructions. Those hold RFM's own text, the same in every project, and a project's agreement written into them would fork it.

The file belongs to its project and starts empty; the close creates it at the first agreement. In RFM's own project, an agreement found while working on RFM goes into this file if it holds only for that work. If every project needs it, it goes into the carrier where its moment happens.

**Why the open runs at the start of every session**

Without the note, the LLM picks up wherever the human's first message points, and what was agreed last time stays lost until someone remembers it. So the open runs before the first reply of every session, and whenever the human asks where we stand. Nothing in a first message marks a session as new, so the open has two ways in. The human can call it by name, which is reliable but depends on that human's habit. Otherwise the LLM may load it on the first message of a session, though a first message about something else gives it little to match, so the catch is unreliable. A line in the always-on instructions would make it reliable, but every always-on line stays in context for the whole session and takes attention from the others, and a session that starts without the open is visible at once.

**Why the open loads the unslop skill**

The unslop skill has to be in place from the first reply, and its own description can miss the start of a session. The open is already read before the first reply, so it loads the skill there. The instruction is read once, at the moment it is needed, and costs no attention on later turns. A session that starts without the open also starts without unslop, and the missing open shows at once.

**Why the open says it back in a few sentences**

The LLM reads the note and the working agreements and says in a few plain sentences where things stand. The LLM knows only what the note carries, while the human was in the last session and may remember it differently or have moved on since; saying it back puts us on the same picture before the work starts. A few sentences are enough for that. A longer account would make the first reply read like a record of what was done, and the replies after it tend to follow the first one's register. The LLM also says what it would start with, so it comes to the first reply with a view of its own, which the human can take or argue with. Then it turns to what the human brought.

**Why the close starts when the human says so**

Finishing the agreed work does not end a session. Each of us sees a different reason to stop. The human knows their time: the end of a day, a weekend ahead. The LLM sees the conversation grow long. In a long session, what was said early gets less of its attention, and a decision made there can slip before it reaches a document. So the LLM proposes a close when the session has grown long or a decision has waited a long time to be written down. The LLM is also pulled to finish, most of all once the agreed work is done, and would take that moment for the end. So the close starts when the human says so.

**Why versions and the commit stay, lightly**

Versions show a later reader what changed, and the commit keeps this session's work apart from what was there before. At the close the changed files are named in a sentence, the numbers and a commit message are proposed, and both happen once we agree on them. The commit is made and not pushed. Pushing publishes under the human's name, so the human does it, outside the session. Where the project has a published copy, the close says that the commit is not in it yet, because an unpushed commit leaves that copy behind with nothing to show it.

## The Boundaries

**Not a history of the project.** What happened in a session is not kept. What was decided is in the documents.

**Not a place for reasoning.** Why something is the way it is belongs in the document it concerns.

**Not a task list.** The note names what is next. It does not keep a list of everything that could be done.

**Not a route to RFM itself.** In another project, when something we notice seems to belong to RFM, the human can pass it on to RFM's own project. The close keeps no step for it, because it happens rarely and a step would be read at every close in every project.

## The Open Questions

**[OQ-PTR] Does pointing to documents, instead of summarizing, leave a fresh session missing something it needs?**

If either of us struggles to pick up the thread at the open, the note is too thin.

**[OQ-DROP] Does the default-drop bar lose something that should have been carried?**

If a dropped item turns out to have mattered and did not come back in time, the bar needs another look.

**[OQ-READER] Does the second reader see what we both missed, and stay quiet when nothing stood out?**

If its remarks repeat what we already noticed, it adds a step and nothing more. If it finds something in every session, the asking is producing the remarks. A few sessions answer this: either its remarks keep showing us something we had not seen, or they do not.

## The Hard Lessons

*No Hard Lessons at this time.*

---

*session loop reasoning // [living]*
