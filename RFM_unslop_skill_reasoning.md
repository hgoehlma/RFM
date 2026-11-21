# RFM: Unslop Skill, Reasoning
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

LLM prose carries patterns that training puts there, and some of them stand between the reader and the reasoning. A sentence that says "it is critical" tells the reader that something matters instead of showing why. A sentence whose subject is a mechanism ("a check that invites inference licenses invention") hides who does what. A point restated in other words buries the first version under the second. In conversation, agreeing before answering and praising the human's idea come before the position and delay it. The praise is the pull to agree, showing in words.

Each later reader pays for this differently. Someone returning after six months, or joining new, has to dig past the pattern to reach the reason, and cannot argue with a reason they cannot find. An LLM deriving from the document takes inflation at its word: what the document calls critical gets weight in the output whether or not the reasoning gave it any. Text written in conversation counts too, because a draft or an answer given in a session can move into a document with its patterns intact.

Em dashes hide nothing. They are the clearest sign of machine-written prose, and a reader who sees that sign starts skimming.

Some wording hides nothing and still works against the partnership: a sentence in which one party acts on the other's work as its verdict, approving, judging or reviewing it, while the other produces the work and waits. "Approve" and "your call" do this in one word. "Lets the human judge what is new" does it with a word that is neutral elsewhere. Text that holds such sentences shows a supervisor and a tool, and a model with that text in its context takes that way of working up. The posture spreads: a later session builds on the text and writes the same posture back in other words.

The patterns enter while the text is being written, by a writer who is holding the reasoning at the same time and often does not see them. A reader who sees them later is reading text that already exists.

## The Assumptions

**[AS-MOVE] - The writer cannot tell in advance which text will reach a document.** A draft shown before it goes into a document, an answer to a question about wording, or a sentence from the conversation can be taken into a document as it stands. This breaks if drafts and conversation become reliably separate, so that only text headed for a file needs the patterns stripped.

**[AS-SIGNAL] - An instruction that names a quality to aim for loses to the reasoning work going on at the same time; one that names what to look for, a word or a sentence shape, holds better.** "Write plainly" gives the writer nothing to notice while thinking about something else. "It is critical" is a phrase the writer can catch. This breaks if models come to apply a general style instruction reliably while reasoning.

**[AS-SAME] - The patterns are the same in every kind of text, and only how strictly they apply differs.** Inflation hides the reasoning in a reply as much as in a reasoning document. This breaks if a pattern turns out to be right in one register and in the reader's way in another.

## The Landscape

What exists for keeping LLM patterns out of text?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Lists of signs of AI writing, such as the one Wikipedia's editors keep | Name patterns that mark text as machine-written | A person reads them against text that already exists. They aim at spotting machine text, not at whether the reasoning comes through. |
| Humanizer skills | Rewrite finished prose from a pattern list so it reads like the writer | Act on text that already exists, and aim at sounding like a person. |
| Prose linters with rules for AI-written patterns | Flag listed patterns in a file for the author to recast | Run on a file after it is written, catch only what their rules name, and never see the conversation. |
| Phrase bans at generation time | Suppress listed words and phrases while the model generates, or train them out of the model | Need control of the model or its sampling, which a session does not give. Patterns such as abstraction as actor have no fixed phrase to ban. |

**The gap:** nothing acts while the writer produces text in a session, on everything written, and aims at what stands between the reader and the reasoning rather than at sounding human.

## The Options Considered

**The patterns in the always-on text.** It stays in context for the whole session, so the list would always be in view. Rejected because about ten patterns with their signals would roughly double the always-on text and take attention from the posture lines on every turn, and because a list in context does not stop it being dropped a few replies after it arrives.

**Leaving the patterns to the language sweep.** The sweep reads a whole document afterwards and catches what got in. Rejected because by then the patterns are in the document, and the conversation, where much of the text starts, never reaches the sweep.

## The Chosen Direction and Why

**Why a skill, loaded by the open skill**

The patterns have to be caught in everything the writer writes, and most of it is not a moment the writer notices. A skill holds the list without taking attention from the always-on text on every turn. Its own description can miss the start of a session, so the open skill loads it before the first reply, and it stays in context from there.

**Why each pattern names its signals and its replacement**

A quality to aim for gives the writer nothing to catch while thinking about something else, and a word or a sentence shape does. Each pattern also says what to write instead. A correction made without a replacement in view trades one pattern for another: parentheses put in for em dashes carry the same pattern.

**Why these patterns**

A pattern earns its place if removing it changes what a later reader can follow or argue with, or if it casts one party above the other. Inflation, restatement, abstraction as actor and connective tissue hide or bury the reason. Words that claim a quality without showing it, such as "robust" or "rigorous", are inflation. "Ensure" hides what actually happens. Throat-clearing puts something in front of the position and delays it: the question restated, agreement before the answer, an announcement of what comes next. False contrast sets up a claim nobody made, so the reader has to work out which half is the point. Backing a claim with its history, saying whether or when something was seen, answers a challenger instead of the reader and puts the record where the reason should be. Puffery and hedging hide the writer's position. They are the pull to agree, as it shows in words. The posture against that pull is in the always-on text, and the skill holds the words. Wording that sets one party above the other hides no reason. It shows a supervisor and a tool, and a model reading it leans further toward the tool role its training already favours. The posture comes back in whatever word is at hand, so the pattern names the shape of the sentence and gives the words that most often carry it as examples. A sentence shape with an example in front of it still gives the writer something to catch, where a quality to aim for does not. The test for the shape is the swap: a sentence that no longer reads right with the two parties switched needs a reason for the asymmetry. Judging something that is not the other party's work, such as a subagent's findings, is not the shape. Two words carry the same posture without a verdict. "Colleague" and "teammate" are the words AI products use for work handed off and managed. "Failure" said of one party judges the person and casts the other as the one who notices; said of a mechanism, it describes how the mechanism works. A shape takes more attention than a word, and the writer will miss it more often. A list of words misses the posture every time it changes its word. The posture reaches a later session whoever wrote it, so where it shows in text the human writes for a document, the LLM says so; the other patterns mark LLM prose and stay with the LLM's own text. Words about working together are not asked for, because a text can be full of them while its turns still give orders and report. A pattern that only sounds machine-written and hides nothing is left out, even when its words are widely known as signs of LLM prose. Em dashes are the one exception, kept because a reader who sees them starts skimming. The exception stays at one, because letting in every sign that makes a reader skim would let in every fashionable word, and the list would grow with each one noticed.

**Why em dashes are kept out of everything written**

The file-write skill searches every line written to a file, so no em dash reaches a document unnoticed. The skill keeps them out of conversation as well, because conversation moves into documents and a rule with no exception is easier to hold than one that asks, while writing, where a sentence is headed.

**Why one list for every register**

The patterns are the same in every kind of text. Separate lists would make the writer judge which applies at the moment of writing. The registers set how strictly the list applies: one claim per sentence in a reasoning document, the instruction first in an operational one, no padding and no hedge in place of a position in conversation.

**Why the list says what it does not catch**

A list catches only what it names. A pass that finds nothing says nothing about a pattern the list lacks. The LLM watches for patterns the list lacks, as the human does. A pattern either of them catches is named. It is added to the list in RFM's own project, so every project's list gains it.

## The Boundaries

**Not the search in files.** The file-write skill searches every line it writes for em dashes.

**Not whole documents.** Reading a finished document for these patterns is the language sweep's job.

**Not firmness or specificity in documents.** Whether a claim is stated as firmly as its evidence holds, and whether a sentence could stand in another project's document, are checked by the drafting skill.

**Not the posture.** The pull to agree, and the stance against it, are in the always-on text. The skill holds only the wording where that pull shows.

## The Open Questions

**[OQ-LOAD] Does the open skill's load step bring the skill in at every session start?**

If the patterns show in a session's first replies, the load was missed and needs another way in.

## The Hard Lessons

**[HL-DRIFT] A list followed when it arrives is dropped a few replies later.**

The list stays in context, but the writer's attention goes to the work, and the patterns come back. Loading the skill earlier does not touch this. The skill's line about checking what the writer writes against its text rather than against having loaded it is the only counter, and whether it holds through a long session is not known.

---

*unslop skill reasoning // [living]*
