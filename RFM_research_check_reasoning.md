# RFM: Research Check, Reasoning
`v0.1.0` // `module_reasoning` // [living]

---

## The Problem

A reasoning document rests partly on what lies outside the project: how a tool behaves, what research has found, which approaches exist, what models do. Each such belief states what would break it. The outside moves and the document does not. A break condition is met in published work and the assumption stands. An open question answered elsewhere stays open. A new approach never reaches the Landscape. In RFM's own set, a carrier built to make up for a model behavior keeps running after newer models stop showing it.

Nothing that reads the set can notice, because what changed is not in it.

## The Assumptions

**[AS-PACE] - The outside moves slowly enough that a check started now and then catches a change before it costs anything.** A break condition met in published work matters once someone acts on the belief, and most beliefs are acted on again only when the work returns to them. This breaks if a derivation or a decision is found to rest on a belief whose break condition had already been met, at a cost an earlier check would have avoided.

**[AS-PUBLISHED] - What would break a claim about the outside usually gets published where a search can find it.** A tool's behavior is in its own documentation, a finding in the work that reports it, an approach where its makers describe it. How something behaves under the project's own conditions is the exception: how a model behaves across a long collaborative session is reported late or not at all, and the project's own work shows it first. This breaks if claims the check found nothing against keep turning out wrong in the project's practice, often enough that the search stops being worth running.

**[AS-WEIGH] - The LLM can weigh evidence against a belief the document holds once the evidence is in front of it.** The LLM reads the document's beliefs as how things are, which is why it would not go looking. Shown a tool's own documentation or a study that meets a break condition, it no longer has to find anything. It has to judge whether the break condition is met and what would change if it is, and that takes knowing what the document is for. This breaks if the LLM sets aside findings that the human, reading the evidence, picks back up.

## The Landscape

How does a document's reasoning stay current with what is known outside it?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Living reviews in medicine | Search for new evidence on a fixed schedule, with what would change the conclusion decided in advance | Built around one question, with a standing team and steady funding. Neither the time passed nor the number of new papers shows when an update is due; someone who knows the question has to judge. |
| Assumption-based planning | Names the assumptions a plan rests on and the early signs that one is failing | Says what to watch, not how to watch it. A sign catches only the way of failing someone imagined. |
| Decision records | Keep the reasoning behind a decision, sometimes with a condition for revisiting it | Nothing watches the condition. A decision is revisited when someone happens to come back to it. |
| Freshness tools for documentation | Expire a page's verified status, rank pages by their last change, or check documentation against the code | Compare a document with time or with the team's own material, never with the outside world. A page changed last week can be wrong. |
| LLM fact-checkers | Pick out checkable facts such as versions and figures, look them up in the tool's own documentation, and mark each accurate, outdated or unverifiable | Skip the reasoning, where a belief and what would break it live. Return an audit, with a source written into each fix. |
| Technology radar | A panel reviews outside techniques at each edition and fades entries whose assessment has not changed | Built for a field, not for one project's reasoning, and needs a panel. |

**The gap:** the pieces exist apart: naming what would break a belief, looking again from time to time, checking against sources. Nothing reads a reasoning document's beliefs by what would break them and brings what it finds back to the people who hold the reasoning, to think it through again.

## The Options Considered

*No Options Considered at this time.*

## The Chosen Direction and Why

**Why the check runs when we agree it is time**

The check runs when either of us proposes one and the other agrees: on returning to a project after a while, or when a belief starts to feel shaky. The outside moves slowly enough that this catches a change before it costs anything. A schedule would run the check whether or not anyone was about to act on the reasoning.

**Why the check asks only whether something no longer holds**

A search for anything bearing on the problem always finds something, and each find has to be weighed. The check looks for one thing: a belief the document states that is no longer correct. Assumptions come first, because the Chosen Direction is built on them. An open question counts when the answer it waits for now exists. A Landscape row counts when the shortfall it names no longer holds, and the gap counts when something now fills it.

**Why a subagent searches**

The LLM reads the document's beliefs as how things are, and a page that could be read either way reads to it as support. A subagent gets the document and the request we agreed on, and searches from each break condition with no stake in the belief. The searches and the pages they return stay in the subagent, so the LLM keeps room for the conversation the findings are for.

**Why searches start from the break condition**

A belief and the work that breaks it are often written in different words. A belief that a skill loads at the moment its description names is broken by work on how models choose among many tools, which never uses the word "skill". A search built from the belief, for it or against it, never reaches that work. The break condition names what a contrary result looks like, so the search is built from it. Where a belief states none, the subagent writes one and says so, so we know the condition is its own and not ours. How a tool behaves is looked up in the tool's own documentation, because accounts of a tool fall behind the tool.

**Why the subagent says first whether anything has stopped holding**

A subagent asked to search returns what it found, whatever it found. Asked first whether anything the document rests on has stopped holding, it has to judge before it lists, and each finding has to earn its place against that judgment. Where it found nothing, it says what it searched for. It does not call the document current, because a search that missed and a document that holds look the same from its result.

**Why the LLM brings each finding as a question, and the evidence stays in the conversation**

The LLM weighs each finding, because it knows what the document is for and the subagent does not. It gives its reason first and its view after, and names the findings it set aside with a line each. A finding comes with the pages the subagent read, so the human can read them too. They stay in the conversation. What changes in the document is decided together and written as how things now are, with no source and no date, like any other position the document holds. A finding asks whether our reasoning still stands, and the LLM brings it that way.

**Why a removal goes through a test in our own practice**

Outside evidence can suggest that something the project relies on is no longer needed, for instance a carrier newer models might not need. A tool's documentation or a study describes other conditions than the project's own, and the project's own work shows its conditions first. So the LLM brings such a finding back with a test it proposes for the project's practice: what to try, and what result would show the thing can go. Nothing is removed on outside evidence alone.

## The Boundaries

**Not claims about the project's own documents or practice.** Whether a document holds as written is the question of the structural, language and cross-document sweeps. Whether it matches how the project is actually worked is for us to notice while working on it.

**Not content not yet written.** Research for a section still being drafted belongs to the drafting skill, in the conversation that writes the section.

**Not the changes.** The check changes nothing. What changes is decided together afterwards and carried out like any agreed work.

## The Open Questions

**[OQ-UNIMAGINED] Does searching from the break condition miss the ways a belief fails that nobody imagined?**

A break condition names the failure its writer could picture. The outside can break the belief another way, and a search built from the written condition will not find it. If that happens often, the check needs a way to look beyond what was written.

**[OQ-PROPOSE] Does the LLM propose a check at the moments it would help?**

If it proposes them too often, or not at all, the proposal needs a clearer moment, or it goes.

## The Hard Lessons

*No Hard Lessons at this time.*

---

*research check reasoning // [living]*
