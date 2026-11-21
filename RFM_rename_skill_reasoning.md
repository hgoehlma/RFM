# RFM: Rename Skill, Reasoning
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

A change to what something is called, what it means, or whether it still holds is made in one document, but the set refers to it in many. Nothing in the document being changed shows where else it is referred to. The change does not reach those places, and the set ends up saying two different things.

Redefinition and resolution are the harder cases. The word stays, so nothing looks wrong.

Whoever makes the change has their attention on the document in front of them, and does not look elsewhere unless something prompts it at that moment.

## The Assumptions

**[AS-ATTENTION] - Whoever makes a change does not look beyond the document in front of them unless something prompts it at that moment.** This breaks if writers reliably search the set on their own when they rename, redefine or resolve something.

**[AS-WORDS] - References across documents are made mostly in ordinary words.** A few things have exact handles: a document its file name, an entry its named ID inside its own document. A change to one of those can be found exactly. Everything else is found by searching for words, and a search finds only the words it is given. This breaks if documents come to refer to each other mainly through handles that can be traced.

## The Landscape

What helps carry a change in a name, a meaning or a status through a set of prose documents?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Find and replace | Changes every exact match of a word | It misses variant compounds and changed meanings. |
| Renaming in code editors | Renames a symbol and every use of it | It works because code has symbols a tool can trace. References in prose are ordinary words. |
| Backlinks in wikis and note tools | Lists every page that links to a page | It sees explicit links, not a word used in a sentence. |
| Terminology management: a termbase, a style checker with a word list, an LLM audit against preferred terms | Flags outdated or variant terms | It catches the old word, not a word still used in its old meaning. Someone has to keep the list. |
| Single-sourcing | Keeps a definition in one place and includes it by reference | It removes repeated definitions. Most references are sentences that use a term to say something else, and these cannot be included. |

**The gap:** every approach handles the exact word or the explicit link, and single-sourcing avoids repeating a definition. None catches a passage that still uses a word in a meaning it no longer has, or still treats something as open that has been resolved. That takes reading the passage.

## The Options Considered

**Showing the search in the reply:** the search patterns, the raw output and, after the fixes, a count of the remaining hits. It would force the search to happen. Rejected because it turns the reply into an audit: the human reads the record of searching instead of what changed, and the skill is written for someone who has to be convinced the work was done.

**A separate agent running the search.** Rejected because the agent does not know what changed, and what to search for comes from the change.

**This skill also covering an edit that changes what one document says about another.** Rejected because nothing is renamed in such an edit, so there is no word to search for. Not restating a fact kept elsewhere belongs to drafting, and checking documents against each other to the cross-document sweep. Two skills described for the same moment would also compete for the load.

**A pointer to this skill in the always-on text.** Rejected because the always-on text holds only what is acted on wherever it is read, and most turns change no name, meaning or status.

## The Chosen Direction and Why

**Why the search comes before the change**

The search shows how far the change reaches. Run before the change, it gives the scope of the work: which documents the change reaches and what each one needs. The LLM states that scope once, in plain sentences, by document and by what changes there, before carrying the change out. At that point we can still leave something out. Afterwards, the fixes show in the documents. The scope cannot be stated without the search, and that is what brings the search about. A scope given as patterns, raw output or counts has turned back into the audit.

**Why the search list goes beyond the old name**

A search finds only the words it is given. The list holds four kinds of words. The first is the old name. The second is its exact handle, where it has one. The third is its head word alone, because a search on the full term misses variant compounds. The fourth is the other words the set uses for the same subject, because a passage that carries the idea in other words still says the old thing. The first three are mechanical. The neighbouring words depend on how much of the set the LLM has read in the session, and nothing shows when that list is thin. So the scope names them, and the human can add the one that was missed.

**Why each hit is read, and some are thought through together**

A redefined or resolved thing keeps its word, so a search line cannot show whether a passage still means what it did. Each hit is read in its passage. What decides the next step is whether the passage only uses the word or depends on what it meant. A passage that only uses it gets the new word or the new status. That is carrying out, and the LLM makes these fixes without asking about each one. A passage whose argument rested on the old meaning or the old status needs new reasoning. A resolved question can weaken an assumption. A redefined term can leave a reason that no longer holds. Such a passage is brought to the human with what the LLM would do with it, and we think it through together. An entry the change leaves with nothing live is the clearest case, and whether it goes, shrinks or moves is a curation decision. The scope sorts the hits into these two groups.

**Why there are two ways in**

The trigger is weak. The change has to be recognized as a rename, a redefinition or a resolution, and a missed load leaves no trace. The skill's description names the moment in those words. The file-write skill is in front of the LLM at every write, and it loads this skill before a write that renames, redefines, moves, retires or resolves something. That reaches the change at the write that makes it, even when the description did not prompt the load.

## The Boundaries

**Not the decision to rename.** Whether a change is right, and what a new word means, is reasoning done before the skill loads.

**Not a new term's first definition.** Checking that a new word agrees with how the set already uses it happens while drafting.

**Not what happens to an entry a change leaves empty.** The skill brings it up with what the LLM would do, and we decide with the curation skill.

**Not stale references left by earlier changes.** Those are a question about the whole set, for the sweeps.

**Not logs or the handover note.** A log records what happened, and nothing is derived from it. The handover note is rewritten from the documents at every close. The skill searches the documents things are derived from, and what is derived from them.

## The Open Questions

**[OQ-SCOPE] Does stating the scope make the search happen without the audit?**

Showing the search forces it to happen. A scope statement only invites it. If changes keep reaching only the document in front of the LLM, the skill needs a stronger push that is still not a report.

**[OQ-LOAD] Are the two ways in enough to load the skill when a change is made?**

A missed load is silent. If renames keep going through without the skill, it needs another way in.

## The Hard Lessons

*No Hard Lessons at this time.*

---

*rename skill reasoning // [living]*
