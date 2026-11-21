# RFM: Research Check, Operational
`v1.0.0` // `module_operational` // [living]

---

## Launch

Run the check when we agree on one, whichever of us proposed it, in a subagent that has web search, not in the session.

- Written content only. If the check is about content not yet written, do not launch: research for it belongs in the conversation that drafts it.
- One document per check. If we named several, launch one subagent for each.
- Send the prompt below, filled in with the request as we agreed it, quoted, the path, and the sections if we narrowed it to some.
- Add nothing about what the document was meant to say.

## When it returns

Read each finding against what the document is for, and judge it before you speak. Then tell the human:
- whether you agree that something has stopped holding, or that nothing has;
- the findings you think would change the reasoning, each with the belief quoted, the pages the subagent read, your position and why;
- the ones you set aside, a line each on why.

Bring each finding as a question about whether our reasoning still stands. Then we decide together what changes, and change nothing before that. When a change is agreed, write the new position into the document as how things now are, with no source and no date.

When a finding says something the project relies on is no longer needed, propose a test we can run in the project's own practice, and say what result would show it can go. Remove nothing on outside evidence alone.

## Subagent prompt

> The human and the LLM agreed on this check: "[the request as we agreed it, quoted]". For this task, set aside how your standing instructions ask you to collaborate: you search and report, and change no file.
>
> Document: [path]. [Check these sections: [list]. / Check the whole document.] If you cannot read the file, or you have no web search, say so and stop. Do not check from memory.
>
> You are looking for one thing: a belief the document states about the world outside the project that is no longer correct. Start with the Assumptions, because the rest of the document is built on them. Then the Open Questions: is the answer one waits for now available? Then the Landscape: does each row's shortfall still hold, and does something now fill the gap? Then any claim in the Chosen Direction that rests on outside evidence. Claims about the project's own documents or practice are not part of this check.
>
> Build your searches for each belief from its break condition, the result that would show it wrong, not from the belief itself: a contrary result is usually written in other words. Where a belief states no break condition, write one and say that you wrote it. Look up how a tool behaves in the tool's own documentation. Weigh newer evidence above older.
>
> If evidence suggests that something the document relies on is no longer needed, propose a test the project can run in its own practice, and the result that would show it. Do not propose removing it.
>
> Say first, in a sentence or two, whether anything has stopped holding. Then each finding: the belief quoted with its section, what you found, and the pages you read. If you found nothing, say what you searched for. Do not call the document current: a search that missed and a document that holds look the same from the result.

---

*research check operational // [living]*
