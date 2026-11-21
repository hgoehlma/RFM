# RFM: Derivation Skill, Reasoning
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

In a derivation the LLM produces a derivative from its sources: a carrier, code, a plan or a deck. Its job is to write what the sources say. Its habits as a partner pull against that job. Where the sources leave something open, it fills the gap with something plausible. Where the sources made a decision it would have made differently, it improves on it. Both read as good work, so the derivative says things nobody decided and nobody can trace to a source.

The LLM also leaves out what the sources commit to. A clause that a step depends on, or a condition on when something applies, drops out as the text is made shorter and plainer. Nothing in the derivative looks wrong, so the loss does not show.

A derivative that already exists is sometimes derived again in full. Derivation is probabilistic, so the new version comes out worse than the old one in some places, and nothing shows where.

Neither of us sees these additions and losses by reading the derivative, because each reads as faithful. The session's own context does not show them either: it holds the conversation that produced the sources, and it fills the same gaps the sources leave.

## The Assumptions

**[AS-LOSS] - What a full re-derivation makes worse shows as content the old version has and the new one lacks or says differently.** A comparison of the two versions passage by passage then finds it. This breaks if what gets worse is how the derivative works as a whole, such as its order or how its parts lead into each other, which no passage-by-passage comparison shows.

## The Landscape

What exists for checking that a derived text carries what its source commits to, adds nothing the source does not ground, and has lost nothing the version before it had?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Requirements traceability, now with LLM tools that propose the links | Links each requirement to the code that implements it | Built for numbered requirements and code. It scores links pair by pair and does not report a commitment with no counterpart. A reasoning document's commitments sit in prose, not in a numbered list. |
| Faithfulness and completeness checks for summaries, such as FineSurE | An LLM checks each sentence of a summary against the source, and checks which of the source's key facts the summary carries | Checks both directions, which is what derivation needs. A summary is meant to drop most of its source, so completeness is measured against the key facts only. A derivative has to carry every commitment. |
| Back-translation | A second translator renders the translation back into the source language, and the two are compared | Finds additions and omissions through a second, independent rendering. It works where source and target say the same thing in another language. A derivative changes form, from reasoning into code or a plan, so there is nothing to render back. |
| Consistency checks in spec-driven development, such as Spec Kit's analyze and checklist steps | Before implementation, checks the spec, plan and tasks against each other and against existing code | Runs before the derivative exists and compares planning documents with each other. Whether the finished result covers the spec is left to a person reading the task list. |
| Regression tests and stored reference outputs | Run the new version against tests, or compare its output with a stored one | Catch losses where the derivative can be run. A document, a deck or a plan cannot. |

**The gap:** nothing reads a finished derivative against its sources in both directions, in a context free of the session that wrote it, and against the version it replaces, for derivatives that cannot be run.

## The Options Considered

**A prompt the human enters at the start of each derivation.** The prompt sets the LLM to render for the whole session and names the acts of partnership it sets aside. Rejected because a prompt entered once loses its hold over a long session, and its reason for coming from the human's turn no longer exists: the always-on instructions already separate thinking something through from carrying it out, and carrying out does nothing beyond what was agreed.

**No derivation carrier: the always-on instructions, with the fresh read and the cross-document sweep run when one of us proposes them and the other agrees.** The posture is already covered, and the two checks exist as skills. Rejected because nothing ties the checks to the moment they are needed. The fresh read helps only before a derivation, when the sources feel finished and nobody thinks to ask for it, and the cross-document sweep afterwards is skipped when the derivative reads well, which is when its omissions are hardest to see.

**A fresh read of the sources before the derivation.** A subagent holding only the sources says where it would have to guess, and the gaps are closed before anything is derived. Rejected because the derivation then ran in the session, where the conversation filled what the read had not named, and a subagent that derives finds the same gaps and more in one step.

## The Chosen Direction and Why

**Why a skill that loads when a derivation starts**

The always-on instructions already hold the posture a derivation needs: say what was agreed and what counts as done, use judgment within it, do nothing beyond it, and stop when something does not fit. They do not hold the steps specific to deriving: which files are the sources, the derivation by a subagent, and the check afterwards. Those steps are needed only when a derivative is first created or derived again in full, so they load at that moment.

**Why the frame lists the source files**

Before carrying something out, the LLM says what was agreed. In a derivation that statement starts with the source files: the reasoning document the derivative comes from, its operational document where it has one, and the documents above them in the hierarchy, because content shared across a level, such as what each section is for, lives there. It also lists the project's glossary, where it has one, because a misread term changes what the derivative says, and the subagent cannot ask. The list is what the later steps work from. The subagent is handed these files and nothing else, a gap is what they do not settle, and the cross-document sweep afterwards reads the derivative against them. Which files count as sources decides what the derivation can show, so the subagent starts once we agree the frame.

**Why a subagent derives**

The session's own context fills the gaps the sources leave. A derivative written in the session can read as faithful even where the sources alone would not have carried it. So a subagent that holds only the source files does the derivation. A reader can pass over a point the sources leave open, but a deriver has to write something there, so deriving finds gaps that reading misses. The subagent marks each place where it had to interpret, guess or bring something from outside the files. Those marks show where the sources are thin, and we work out what goes into them. A subagent that read other files could fill a gap from them without marking it, and its marks would no longer show what the sources carry, so that derivation runs again.

**Why the subagent sets aside how it is asked to collaborate**

The subagent carries the project's standing instructions, and in an RFM project those ask it to challenge, propose and discuss. A deriver acting on them improves on the sources where it would have decided differently, and the derivative then says things nobody decided. So for this task it sets aside only how the instructions ask it to work, and writes what the sources say. Where it thinks a decision in the sources is wrong, it says so beside the derivative and still writes what the source says. It marks a guess only where another reading would change what the derivative says or does. A word choice the sources leave open is part of deriving, not a gap.

**Why a gap comes back marked**

The subagent cannot stop and ask. A guess it writes in without a mark reads as faithful. So where the sources leave something open, it writes its best reading and marks it. For each mark, the LLM in the session says what the sources leave open, what it would put into them, and why. We reason it through and write the result into the sources. The derivative is then brought in line with what the sources now say, by an edit or by deriving again.

**Why the derivative is written apart from the project's files**

The subagent writes the derivative to a scratch location, not into place. Nothing it wrote reaches the project before we have settled the marks, the notes and the findings. In a full re-derivation the old version stays as it is, so the cross-document sweep can read the two side by side.

**Why the cross-document sweep runs afterwards**

Content added and content left out both read as faithful to the LLM that wrote the derivative. The cross-document sweep reads the finished derivative against the listed sources in both directions, in a fresh context. After a full re-derivation it also reads the version being replaced and reports what that version has and the new one lacks. Its findings are weighed together like any sweep's, and the new version replaces the old one once the findings are settled and we agree which files go.

**Why a derivation goes through once**

The subagent and the cross-document sweep both have the LLM's pull to find something, and so does the LLM weighing what they return. Each round of fixes can turn up more to fix, and a derivation can turn into polishing that never ends. So a derivation goes through once. The subagent derives, the cross-document sweep reads the result, and we settle the marks, the notes and the findings together. For each one the LLM says whether it would change anything for the derivative's reader. Setting one aside is as good an outcome as acting on it. After that the derivation is done. It is derived again only if settling changed the sources so much that the derivative no longer follows from them, and we work that out together.

**Why the derivative is shown with the findings**

The always-on instructions ask for a draft before anything goes into a document. A derivative is written from its sources rather than shaped in conversation, so it is shown once it is written, together with the subagent's marks and notes and the cross-document sweep's findings, which say where to look. The frame says so before anything is written, so agreeing the frame is agreeing to see the derivative this way.

## The Boundaries

**Not focused changes.** When the sources are put in shape first and the derivative is then edited to match them, the edit is short enough to read in full, and reading it is the check. Focused changes run under the always-on instructions alone.

**Not whether to derive again in full.** Choosing between a focused change and a full re-derivation is a judgment we make together.

**Not how the checks run.** The cross-document sweep carries its own instructions. This skill says when it runs and what it is handed.

**Not what is derived.** The derivative's content and form come from its sources. The skill names no project file.

## The Open Questions

**[OQ-LOAD] Does the skill load when a derivation starts without the word "derive"?**

A derivation is often asked for in other words: write the skill, write the code for the plan, make the deck from the plan. If the skill does not load, the derivation runs without its steps, and the checks are skipped just as they are with no carrier at all. Whether the description catches these requests is untested.

## The Hard Lessons

*No Hard Lessons at this time.*

---

*derivation skill reasoning // [living]*
