# RFM: File-Write Skill, Reasoning
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

A write to a file can fail without anyone noticing. A replacement that matches nothing changes nothing and raises no error. A replacement whose old text occurs twice can change the wrong place, because some edit tools change the first match and raise no error. A write built on a read that returned only part of a file damages the part it never saw. Text cut from one file before it reaches the other is gone. A write tool can report success while the file holds something else, as when a tool that copies a prepared file reuses an earlier copy with the same name.

While the LLM carries out agreed work, the human does not watch the files. The reply is their view of what changed, and a reply written from memory of the intended change says nothing about the file.

Em dashes are part of the same moment. They are the clearest typographic sign of LLM-written prose, and instruction does not hold them: a model told to remove one often removes it and inserts another in the same sentence.

## The Assumptions

**[AS-SILENT] - Only the file shows whether a write landed.** Tool messages report that a call ran, not what the file now holds. This breaks if write tools reliably report every failure.

**[AS-SHOWN] - During carrying out, the human sees a file change only if it is shown to them.** This breaks if the human routinely opens the files after each change.

**[AS-DASH] - A search holds em dashes where instruction does not.** A character either appears or it does not, so a search can find every one. This breaks if models stop producing them unprompted.

## The Landscape

How does someone making a change to a file usually know it landed?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| The tool's success message | Reports that the call ran | Says nothing about what the file holds. |
| Version control | Shows every change since the version last saved | Comes after the work, and not every folder is under version control. |
| A hook after each write | Runs a check outside the model | Can check a file, but cannot have the writer show the human what the file now holds. |

**The gap:** none of these has the writer read the file at the moment of the write and show the human what it now holds.

## The Options Considered

**Printing the output of every check:** the raw read-back, a count of zero em dashes, a search showing the old text is gone, the header quoted unchanged. It would make a skipped check visible. Rejected because it fills the reply with proof that steps ran and found nothing, and the human reads the record of checking instead of the change.

**The steps as a line in the always-on text.** It would be in context at every write. Rejected because it would be paid for on every turn, including turns with no write.

**A hook after each write.** It would run outside the model. Rejected because a hook can check the file, but it cannot have the writer read the file and show the human what it now holds.

## The Chosen Direction and Why

**Why the skill shows the result and not the process**

Writing to a file is carrying out. We agreed on the work, and a partner who made a change shows it. So the reply shows the changed lines as they now stand on disk. Producing them takes reading the file, which is what catches a write that did not land. For a large write, the reply shows the key lines: the opening of each changed section, or a search for phrases only the new text contains.

A check that finds nothing stays out of the reply. A check that finds something is mentioned with what it found: an em dash, old text still present, lines that do not match what was meant.

**Why the checks before the write**

Each guards a failure that leaves no trace. A write that depends on a read compares the lines read with the file's line count, because a partial read looks like the whole file. A replacement checks that its old text occurs exactly once, because a replacement that matches nothing reports nothing, and one that matches twice may change the wrong place. One line of the old text that occurs once in the file is enough, because the whole text can then occur at most once; a search for that line only reads the file, so the write hook lets it through. A move writes the destination and reads it back before cutting the source, because a cut made first is lost if the write fails. A write that renames, redefines, moves, retires or resolves something other text refers to loads the rename skill first, because the references break silently.

**Why changing the reasoning first sits with the checks before the write**

A prompt or skill changes only after its reasoning document has changed, and that matters only at the moment of a write. This skill loads before that write. A miss is not severe and a later comparison can find it, so a skill that sometimes fails to load is enough to carry it.

**Why the em dash search sits here**

The skill loads at every write and reads the changed lines back, so the search runs on every file written, skill files included. It runs on the lines read back, so existing em dashes elsewhere in a file do not show up at every write. A count over the whole file before and after would miss the swap, one removed and another inserted. A hit is fixed by recasting the sentence. A comma or period is used only when recasting loses the meaning, and parentheses are not a substitute. The skill names the character by its Unicode number, so its own file does not contain one.

**Why a write never bumps a version**

A version line in front of the writer reads like an instruction to bump it. Versions change at the close, where the whole session's changes are known.

## The Boundaries

**Not drafts.** Text shown for discussion is not a write, and the drafting skill governs it.

**Not version bumps.** Those belong to the close.

**Not the reference search after a rename.** The rename skill does that.

## The Open Questions

**[OQ-KEYLINES] Does choosing key lines keep a large write honest?**

The writer picks which lines to show from its own work. Whether that choice shows the human what they need, or only what looks right, has to be seen in use.

**[OQ-LOAD] Does the skill load at every write?**

A missed load leaves a reply with no lines from the file. That shows only to a human who expects them.

## The Hard Lessons

*No Hard Lessons at this time.*

---

*file-write skill reasoning // [living]*
