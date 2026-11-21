# RFM: Sweeps, Reasoning
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

A finished document holds failures that those who wrote it cannot see. Content sits at the wrong level or in the wrong section. Two entries carry one argument in different words. A sentence uses a term only its writers knew. Two documents state opposite things about one practice, or an operational document leaves a gap that whoever derives from it would fill by inventing. From inside the session each of these reads as sound: the duplicated argument reads as thoroughness, the undefined term reads as clear, and the gap gets filled from memory without anyone noticing.

Some of them only show when the whole document is read at once. The writer checks text as it is written, and the document those failures live in does not exist yet.

A reader asked to find problems finds them, whether or not the document holds. What comes back is a list in which most items would change nothing for someone using the document, and the few that matter sit among them. Someone then has to sort the list. If nobody does, the human gets the sorting as work, and a long list is where accepting what reads well comes easiest.

## The Assumptions

**[AS-ANCHOR] - A reader without the writing session's context sees failures its writers read as sound.** The writers know what each term means and what a gap was meant to hold, so they read the document as they meant it. A reader who has only the document reads what is there. This breaks if the writers reviewing their own document are shown to find as much as a fresh reader does.

**[AS-ONEJOB] - Each kind of reading needs attention the others would divert.** Judging where content sits, how a sentence reads, and what passes between two documents are different readings. One pass asked to do several does each of them shallowly. This breaks if a single pass is shown to find what separate passes find.

**[AS-SORT] - The LLM that helped write the document can judge a finding put in front of it, even though it could not find it.** Reading its own document, the LLM takes a duplicated argument for thoroughness and passes it. Shown the two passages quoted side by side, it no longer has to find anything. It has to judge whether merging them would change anything for someone using the document, and that takes knowing what the document is for, which the LLM has. This breaks if the LLM, shown the quoted passages, still reads them as it read them while writing, and sets valid findings aside.

## The Landscape

How does a finished document get read for failures its writer cannot see?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Peer or editorial review | A second reader comments, and the author answers each comment against what the work is for | Close to what is needed, and the part to borrow is the author answering each comment. It needs a second person every time. |
| LLM reviewers in code review | A model comments on a change | Trained to help, it returns many suggestions, and the one defect that matters is buried among them. Telling it to flag only real defects helps little. |
| Critic loops | A second model critiques a draft, and the writer revises | The writer revises on the critique without anyone sorting which points matter, and nothing shows what was dismissed. |
| Scoring by an LLM judge | Rates the output | A number cannot be acted on, and a model rating its own work favors it. |
| Traceability tools | Link each requirement to the specification that meets it | Track links someone declared. They do not read whether two passages agree. |

**The gap:** nothing pairs a reader who has only the document with a judge who knows what the document is for, and has the judge give its reason on each finding where the human can see it.

## The Options Considered

**A sweep prompt pasted into a fresh conversation.** The reader has only the document and the prompt, and it finds failures. Rejected because the findings come back in another conversation, away from the LLM that knows what the document is for, so nobody judges them before the human has to sort them.

**Findings relayed to the human for ruling.** A subagent returns findings, and the LLM passes them on untouched for the human to rule on. Rejected because the human gets the whole list to sort, while the LLM, which could judge each finding, keeps its view to itself.

**A separate sweep reading a reasoning document against its operational one.** It checks whether each need in the reasoning is covered in the operations. Rejected because reading a reasoning document against its operational one is the same reading as reading any two documents against each other, and a sweep limited to one pair lets two reasoning documents that state opposite things about one practice pass.

## The Chosen Direction and Why

**Why a subagent with only the document**

Those who wrote the document read it as they meant it, so the review goes to a subagent that was not in the session. It gets the document and the review the human and the LLM agreed on, and, like any subagent, its standing instructions, which include the always-on instructions. It gets nothing about what the document was meant to say, because that would hand it the writers' reading.

**Why the subagent sets aside how it is asked to collaborate**

The standing instructions ask for a partner who proposes and builds in conversation. A reader that proposes changes turns the review back into writing, and the LLM would be sorting a partner's draft instead of a reader's findings. For this task it reads and reports, and changes no file.

**Why the subagent says first whether the document holds**

A reader asked to find problems returns a list whatever the document's state. Asked first whether the document holds overall, it has to judge the document before it lists anything, and a finding has to earn its place against that judgment. A pass that finds nothing reports what it read and the questions it put to it. It does not call the document clean, because a shallow pass and a sound document look the same from its result.

**Why the LLM sorts, and says what it set aside**

The LLM could not find these failures itself, but it can judge one put in front of it, and it knows what the document is for. So it judges which findings would change something for someone using the document. It says first whether it agrees the document holds, and gives its reason on each finding before its verdict, because a model judging its own work leans toward it, and stating the reason first is expected to reduce that, though this is not yet tested. The findings it sets aside are named with a line each, so the human can pick one back up. Then we decide together what changes.

**Why one kind of reading per sweep**

A pass doing several kinds of reading does each shallowly, so each sweep keeps to its own reading. A placement finding that also shows a wording problem stays a placement finding, and the wording is left to the language sweep.

**Why a sweep runs when we agree it is time**

A sweep of an unready draft returns noise, and no fixed trigger can tell whether a draft is ready. Either of us can tell, so either of us can propose a sweep when a document seems ready, and it runs when we agree. One exception: a derivative is produced whole from its sources rather than drafted over several sessions, so it is ready once written, and the derivation skill runs the cross-document sweep as its last step without asking.

A sweep is also proposed when we come back to a document. A parent can be right when written and go stale as its modules change, with nobody touching it, and content can come to belong in another document. We expect this to be the main use in a larger project or one that runs for a long time.

**Why a sweep reads the whole document**

A sweep judges one document, all of it, because a section nobody changed can be made wrong by one that did. We can narrow it to named sections when a document is long.

**Why a structural sweep**

It judges where content sits. A missing or misplaced section is reported first, because every other placement finding assumes the sections are right. The same argument made twice in one document is its question, not the cross-document sweep's: both passages sit in one document, so the question is where the argument belongs.

**Why a language sweep**

It judges how the document reads to someone who was not there. It reads any kind of document, because these failures do not depend on the kind. Whether a sentence could stand in any project, whether a conclusion comes with the reasoning behind it, and whether a decision shows its question and the case for and against it, are asked of reasoning documents only: a general instruction in an operational document is often right, and its reasons live in the reasoning document behind it. The subagent says what it takes each project term to mean, because a term read confidently and wrongly shows no other way. Em dashes, which the unslop skill strips as a mark of LLM-written text, are counted over the whole document, because the file-write skill checks only the lines it writes.

**Why the language sweep also reads for the way of working**

A text read into a later session passes on the way of working its words show. Small words that read as careful can show a tool and its supervisor: "approve" where both agreed, or a passage hedged for someone who will check it. While we work we read a text for its content, and those words get past both of us. The language sweep reads wording, not content, and asks how a sentence reads to someone who was not there. The LLM in a later session is such a reader. Reading for the way of working is therefore the same kind of reading the language sweep already does, and a separate sweep would read the same sentences for the same reader.

Its main question is the swap: a sentence that no longer reads right with the human and the LLM swapped needs a reason for the asymmetry. A difference in position is such a reason, such as who wrote a text and who reads it from outside, a place the human, the LLM in a later session and a subagent can each hold. Which of the two is the human and which the LLM is not a reason on its own. It becomes one when the asymmetry answers a pull the always-on instructions name, such as the LLM's pull to deliver or the human's pull to accept what reads well. Without that condition, "the LLM's training" would serve as the reason for any asymmetry. The subagent has the always-on instructions among its standing instructions, so it can tell whether a pull is named there.

Some texts ask the LLM for something its training pulls against, such as holding a position when the human sounds sure. For those, the sweep asks whether the text says what the request is for. A bare rule, such as "do not agree without a reason", is followed in the cases it names and dropped in the ones it does not. When the text says what the rule is for, the LLM can act on it in a case nobody wrote down.

These questions apply where a passage speaks of how the human and the LLM work together. In a project that uses RFM, that is mostly the working agreements and any prompt or skill the project derives; the reasoning behind a garden plan rarely speaks of the partnership. Elsewhere the questions find nothing, and we expect them to take little from the rest of the reading. Wording written for someone who will check it, a hedge or a defending citation, shows in any text, and the sweep already asks about it.

**Why a cross-document sweep**

It judges what passes between documents. It also reads the document against the plan, because a statement can become false once work we have agreed on is done. The subagent finds the other documents by search, because the LLM would hand it only the ones it remembers, and the contradiction that matters is usually in the one nobody thought of. When the derivation skill calls it, the sweep is handed the sources the derivation declared, because a derivative need not name its sources and a search might not find them. The subagent still searches for everything else. After a full re-derivation it is also handed the version being replaced, and reports what that version has and the new one lacks, because content dropped in a re-derivation reads as present to the LLM that wrote it.

## The Boundaries

**Not what is known outside the project's documents.** Reading a document against outside work that may have moved on is the research check's job.

**Not whether an entry graduates or reasoning is cut.** A sweep can turn up a candidate. Whether it goes is decided when either of us proposes it, with the curation skill.

**Not text being written.** The drafting and unslop skills act while text is produced. The sweeps read what is finished.

**Not the changes.** A sweep changes nothing. What changes is decided together afterwards, and carried out like any agreed work.

## The Open Questions

**[OQ-SETASIDE] Does a subagent set aside its standing instructions when the prompt that starts it says to?**

If it comes back proposing changes in a partner's voice, or asking questions instead of reporting, that prompt needs rewording.

**[OQ-HOLDS] Does asking first whether the document holds shorten the list?**

If the subagent still returns a long list behind a verdict that the document holds, the question is not doing its work, and the sorting falls back on the LLM alone.

**[OQ-PROPOSE] Does the LLM propose a sweep at the moments it would help?**

If it proposes them too often, or not at all, the proposal needs a clearer moment, or the LLM stops proposing and only the human asks for a sweep.

## The Hard Lessons

*No Hard Lessons at this time.*

---

*sweeps reasoning // [living]*
