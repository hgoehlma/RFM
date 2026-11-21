---
name: rfm-derive
description: "In an RFM session, load when we are about to produce a derivative from its sources, new or again in full, whether or not we say \"derive\": a skill, a prompt, code, a plan, a deck. Not for a focused edit. Without it you fill what the sources leave open and drop what they commit to, and the result reads as faithful to both of us."
---

# Deriving

We are about to produce a derivative from its sources. A derivative written in this session reads as faithful even where the sources alone would not carry it, because this session's context fills the gaps they leave. So a subagent derives from the sources alone, and the cross-document sweep reads its result against them.

This applies when a derivative is first created or derived again in full. A focused change, where we put the sources in shape and then edit the derivative to match, is short enough to read in full, and reading it is the check.

## The frame

Say "Carrying out" and give what the always-on instructions ask for: what we agreed, what the work covers and leaves out, and what will count as done. This statement is the frame. In a derivation it starts with the source files, by path:

- the reasoning document the derivative comes from;
- its operational document, where it has one;
- the documents above them in the hierarchy, because content shared across a level, such as what each section is for, lives there;
- the project's glossary, where it has one, because a misread term changes what the derivative says.

Say also that the subagent writes the derivative to a scratch location, whether an existing version is being replaced, and that I will see the derivative once it is written, together with the subagent's marks and notes and the sweep's findings, rather than as a draft beforehand. Go on once we agree the frame.

## The subagent derives

Start a subagent, hand it only the listed source files, and give it the prompt below.

When it returns, compare the files it opened with the files handed. If it opened any other, its marks no longer show what the sources carry: say so and run it again.

## The cross-document sweep

Run `rfm-cross-document-sweep` on the derivative in the scratch location. Hand it the source files from the frame and, after a full re-derivation, the version being replaced, which stays as it is.

## Showing and settling

Show me the derivative's text in the conversation, together with the subagent's marks and notes and the sweep's findings, which say where to look.

Then we settle them together. For each mark, say what the sources leave open, what you would put into them, and why. For each mark, note and finding, say whether it would change anything for the derivative's reader. Setting one aside is as good an outcome as acting on it. What we decide goes into the sources first, and then the derivative is brought in line with what the sources now say, by an edit or by deriving again.

A derivation goes through once: the subagent derives, the sweep reads, we settle. The subagent, the sweep and you weighing what they return all pull toward finding something more, and each round of fixes can turn up another. So after settling, the derivation is done. It is derived again only if settling changed the sources so much that the derivative no longer follows from them, and we work that out together.

Nothing from the scratch location reaches the project until the marks, notes and findings are settled. Then the new version replaces the old one, once we agree which files go. Write it into place with the file tools.

## Subagent prompt

> The human and the LLM agreed on this derivation: "[the frame as we agreed it, quoted]". For this task, set aside how your standing instructions ask you to collaborate: you write what the files say. Where you would have decided differently, an improvement you write in reads as faithful and nobody can trace it to a file, so write what the files say and note your doubt beside it.
>
> Files: [paths]. Read these files and no others. Do not search for or open any other file, and do not use anything you know about this project from elsewhere. If you cannot read a file, say so and stop.
>
> Task: produce [the derivative] from these files alone and write it to [the scratch location]. Write nothing anywhere else.
>
> Where the files leave something open, write your best reading and mark it, because you cannot ask and a guess written in without a mark reads as faithful. Mark only where another reading would change what the derivative says or does. A word choice the files leave open is part of deriving, not a gap.
>
> Return:
> - Coverage: every file you opened, by path.
> - Marks: for each, the passage of the derivative it sits in, what you had to interpret, guess or bring from outside the files, and the source passage it comes from or what is missing.
> - Notes: for each doubt, the source passage and why you doubt it.
