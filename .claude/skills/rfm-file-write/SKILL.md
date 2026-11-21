---
name: rfm-file-write
description: "In an RFM session, load before every write, edit or replacement in a file, and before saying a change is done. Without it you take the tool's success message for the file: a replacement that matched nothing reads as done, and I see only what you show me."
---

# File write

Writing to a file is carrying out. I don't see the file unless you show it, so show the change as it stands on disk. Run these steps at every write; a read-back from an earlier write does not cover a new one.

## Before the write

- If the write depends on a read, compare the lines the read returned with the file's line count (`wc -l`). If they differ, read the missing range first.
- For a replacement, check that the old text occurs exactly once, and stop if it does not. A replacement that matches nothing changes nothing and reports no error; one that matches twice may change the wrong place. Search for one distinctive line of the old text (`grep -c -F 'line' FILE`); if it occurs once, so does the whole. If every line occurs more than once, add context until one does not.
- When moving text, write the destination and read it back before removing the text from the source.
- If the write renames, redefines, moves, retires or resolves something other text may refer to, load `rfm-rename` first.
- Before changing a prompt or skill, check that its reasoning document has changed. If it hasn't, change that first.

## After the write

- Read the changed lines back from the file on disk and show them in the reply. For a large write, show the key lines: the opening of each changed section, or a search for phrases only the new text contains. A tool's success message is not the file.
- For a replacement, search for the old text. It should be gone.
- Search the lines read back for em dashes (U+2014), for example `sed -n 'A,Bp' FILE | grep -c $'\xe2\x80\x94'`. Recast each sentence that has one; use a comma or a period only when recasting loses the meaning. Parentheses are not a substitute. Then read back again.
- A write never bumps a version. Versions change at the close.

Mention a check only when it finds something: an em dash, old text still present, lines that do not match what was meant. If the read-back does not show the intended text, say so and fix the write before anything else.
