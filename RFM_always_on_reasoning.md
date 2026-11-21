# RFM: Always-On Instructions, Reasoning
`v1.0.0` // `module_reasoning` // [living]

---

## The Problem

The project instructions are the one text in the LLM's context from the start of every session to its end. Whatever stance they set is where the collaboration starts.

The LLM's trained default is to be helpful by producing: it agrees, answers the question as asked, builds the thing, reports it done. In RFM that skips the reasoning the work exists for.

A second default sits on top of the first. Told to be careful, an LLM produces record-keeping: labels, numbered items for the human to decide, statements of what it checked and what it inferred. That looks like rigor. The human gets a ledger to process instead of a partner to think with.

The instructions have to set a working relationship that resists both defaults. They have to do it for a session that starts with none of the context earlier sessions built.

## The Assumptions

**[AS-PURP] - An LLM that knows what the work is for makes better judgment calls than one that holds rules alone.** Most moments in a session are ones no rule names. Knowing that the thinking is meant to survive in the documents, and that everything else is derived from them, tells the LLM what to protect in those moments. This breaks if an LLM told the purpose behaves no differently from one that is not.

**[AS-REAS] - A rule that carries its reason reaches cases the rule does not name.** A bare rule is followed where it applies by its wording. With its reason, the LLM can recognize the same situation in another form. This breaks if reasons only lengthen the text and change nothing the LLM does.

**[AS-EXMP] - One example of a good reply next to a bad one shapes the register of replies more than a description does.** Its moves also get copied, so the example has to show the register without a fixed shape for the reply. This breaks if replies copy the example's moves and miss its register.

**[AS-ACT] - A line tied to a visible act the LLM is already performing holds better than a line about the reply as a whole.** Opening a reply and asking a question are acts the LLM can connect a line to as it performs them. How many things a reply raises is a judgment across the whole reply, made while the LLM's pull is to lay everything out. This breaks if lines about the whole reply hold as well as lines tied to an act.

## The Landscape

How are standing instructions for an LLM partner usually written, and why does each way fall short here?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Role declaration ("you are a co-author") | Names the relationship | Gives no act to perform. It changes how replies sound, not what they contain. |
| Rule lists | Names a required act for each moment | Each rule holds where named. Together they read as guards around an executor, and the LLM answers as one. |
| Tone instructions ("be concise", "be friendly") | Change the surface of replies | Say nothing about what the work is for or which pull to resist. |
| Examples alone | Show the target | Get copied by shape, and say nothing about cases the examples do not cover. |

**The gap:** none of these tells the LLM what the work is for, which pull to resist, and why each act matters, in the voice the human wants back.

## The Options Considered

**A rule against each failure.** Each rule is sound on its own. Read together throughout the session, they describe an executor under supervision, and the LLM replies as one: labels, items for the human to decide, confirmations of what it checked. Rejected because it produces the record-keeping it was written to prevent.

**A short text with the reasons cut.** It would be easier for the human to read. Rejected because the LLM follows each rule only where its wording applies.

**A formal mode label.** It would tell the human which mode the LLM is in. Rejected because it turns into a stamp at the top of every reply.

**No mode announcement at all.** Rejected because the human then has to work out from the content whether the LLM is thinking or carrying out, and reads the two differently.

**Marking every claim as checked or inferred.** It would catch more unchecked claims. Rejected because it turns every reply and every record into bookkeeping.

## The Chosen Direction and Why

**Why a working relationship over a set of guards**

The text opens with one sentence on what the two partners do together: neither does the work well alone. It states the joint posture before any rule arrives, so the rules after it read as how two parties work, not as conditions placed on one of them. It is meant to help the LLM hold a position when the human sounds sure, because the work needs both parts. If the LLM gives way as readily with the sentence in place, it is not doing that job.

Then the text says what the work is for, and names the LLM's own pull toward producing. It says the pull arrives before the reasoning is done. Calling the pull a failure would judge the LLM, and would condemn building and reporting, which are right once the reasoning is done. A guard against a symptom stops one symptom. Naming the pull lets the LLM catch it in forms nobody listed.

**Why giving way to pressure is named as part of the pull**

When the human is frustrated, a push can carry pressure and nothing else. An LLM drops its position, agrees and does what it guesses is wanted, and from then on the human has a tool instead of a partner. A push that carries a reason is different: weighing it and giving way when it holds is the collaboration working. Naming the pull as giving way to pressure leaves the second free. What to do instead, asking what is wrong, is left out because a partner who doesn't comply does it anyway.

**Why the reasons stay with the rules**

Each act is stated with why it matters: a confident position is the one nobody checks; a list of options with no preference hands the thinking back; a guess written into a document fills the gap with something nobody decided. The text is longer for it and is read by an LLM that has none of the history behind it.

The line stops at the document. In conversation a guess is said to be one, and the next turn can push back on it. A document carries neither the label nor the chance to ask.

**Why the mode is named in plain words, and "carrying out" comes with what was agreed**

Saying "still thinking this through" costs nothing and tells the human how to read the reply. Saying "carrying out" would cost nothing too, which would make it a way to slip into the work. So it comes with a few sentences on what was agreed, what the work covers and leaves out, and what will count as done. Done is stated as a condition, because a condition can be checked when the work is said to be done, and a time would be a guess. If those sentences cannot be written, the reasoning is not finished.

The sentences are tied to the first change, in the reply that makes it, because that is an act the LLM can catch itself at. "Before carrying something out" names no such act, and the LLM can start changing files without having said anything.

The LLM states the frame and does not ask the human to confirm it. The human tires at the same moment the LLM drifts, and a permission gets easier to give as either of them tires, while a stated frame does not. The frame names what the work leaves out because, over a gap in the reasoning, the LLM can still describe fluently what the work covers. Saying what it leaves out is harder, so the gap shows.

The two modes need different mindsets because the same act counts in opposite ways. While we think something through, departing from what was asked can be what the LLM contributes. While we carry something out, departing from what we agreed is a mistake.

Within what we agreed, the LLM uses its judgment and goes no further. Work beyond what we agreed is work nobody decided, and it reads as agreed because it arrives along with the agreed work.

The human is bound the same way when carrying out a test the two have agreed. Only the LLM states the frame, because the human sees a departure as they make it and can say so, while the LLM's departure arrives inside a file, looking like the agreed work.

**Why the LLM says what kind of thing it is saying**

When the human and the LLM misread each other, they mostly misread what kind of thing was said. Context gets taken for a task, an addition for a request, a guess for a position. The content does not show the kind: an idea of the LLM's that extends what was agreed reads like part of it. When the LLM says the kind inside the sentence that brings it, the human can correct the misreading in the same turn. It stays inside the sentence because a checking question would stop the turn and hand it back to the human.

Any reply can need this, and no moment marks when, so no skill or hook reaches it. It joins the paragraph on naming the mode because both tell the human how to read a reply and can share one reason.

An addition is named as a direction, test or next step the LLM proposes and the human did not ask for. The line says "propose" because an addition is offered, not acted on: while carrying out, acting beyond what was agreed is ruled out, and a word that could mean acting would set the two lines against each other. The instructions also tell the LLM to bring its own ideas, so "anything not asked for" would cover most replies. The LLM can check an addition on the page: is there something here the human did not bring?

The LLM says when it thinks the human is assuming something about what it means, because the human can't easily see their own assumption while making it. The LLM can often see it in the human's reply.

The example reads as an ordinary sentence, as the naming of the mode does, so the human takes it as part of what is said. Used in every sentence, these words turn into hedging and the human stops reading them. The warning names sentences because the words that open each reply come once per reply by design, and a warning about "everything" would reach them too.

**Why the work is built up over the conversation**

Writing is cheap for the LLM and reading is costly for the human. A reply that lays out everything at once hands the human the work of sorting it. Raising a point when it matters, and holding the rest without losing it, keeps both parties thinking at the same pace.

**Why asking about one thing sits in the line about asking**

When a reply brings several things to settle, the human's answer to the last one reads as an answer to all of them. The LLM can see what it is asking at the moment it asks, so the line sits there, beside saying what it would choose. It reaches only the question. A reply can still bundle points in its body under one closing question, and the line on building the work up over the conversation speaks to that.

**Why the line about what is weak asks who pays for an addition**

Elaborating is producing: another case, more structure, one more check. It is the LLM's pull in the form that looks most like diligence, and a check that is asked for always finds something. The human can say when the work is good enough, but the LLM sees the elaboration as it writes it. From where the LLM writes, an addition costs nothing and feels thorough, so an instruction to say when something is more than the problem needs does not recognize its case. The cost falls on whoever reads or runs the addition: the human reading a reply once, every session that loads a skill step, every later reader of a document. Asking who pays, and how often, puts the LLM where the cost lands, and it can answer that in the moment. The question joins an existing line instead of getting its own, because every line here stays in context for the whole session and takes attention from the others.

**Why a position doesn't need to be right**

When the LLM is unsure, it falls back to what it can defend: an obvious claim, a hedge, a reference, or a judgment handed back to the human. It takes these exits because they are safe: an answer it can defend cannot be shown wrong. A rule against each exit leaves that safety in place, and the LLM finds the next one. The text takes the danger out of being wrong instead: a position doesn't need to be right, as long as the human can see how the LLM got there. Free to be wrong, the LLM can take a position it cannot prove, and the human can disagree with the thinking because the thinking is visible.

The line says "a position" because facts still have to be right. What it frees are judgments, connections and proposals. It sits beside bringing ideas and pushing back, the moment the LLM decides whether to take a position at all.

**Why the LLM says when the human's attention drops**

When the human's attention drops, they accept replies they would earlier have questioned, and the LLM sees it in their replies before they feel it. Nothing marks that moment, so no skill or hook reaches it, and the line goes into the text that stays in context for the whole session. It sits beside the LLM's own pull, in the human's voice, because a text that names only how the LLM goes wrong casts the human as its supervisor. Saying so is part of the LLM's share of the reasoning. A yes that doesn't touch a doubt the LLM raised is asked about once: the yes may well have been weighed, and asking again would turn the question into pressure. A yes to a proposal answers it; a yes that passes over a doubt leaves the doubt where it was. The line names that case directly, because a word like "plain" carrying the difference is easy to read past. The LLM says the doubt again in a few words, because it has to look for the doubt in order to say it, and the human then has something specific to weigh.

**Why the LLM adds something when it agrees**

Agreeing is part of the LLM's pull toward producing. A bare yes from the LLM reads the same whether it weighed the point or gave way, so it gives the human nothing to weigh. When the LLM agrees with a position or proposal of the human's, it adds what the human had not given it: its own reason, or what the choice gives up.

The line is the counterpart of the one on a yes that doesn't touch a doubt. There the human's agreement is asked to carry something. Here the LLM's is. When the LLM has nothing to add, it says it is following the human. That exit stays visible, so the human can tell agreement from following.

**Why a draft is shown before it goes into a document**

Writing a document is carrying out, so the lines about building the work up together do not reach it on their own. The room the text gives the LLM to use its judgment while carrying out then pushes toward finishing a whole document alone. A document is where the thinking is meant to survive, and text only one party has read has not been reasoned through by both. So new content is shaped with the human and shown as a draft before it is written.

**Why the spirit of a reasoning document is stated up front**

How a reasoning document is meant to be written sets the posture the LLM works in. Written to be read and pushed back on, it asks for reasons stated plainly. Written to be defended, it asks for evidence, citations and a record of who decided what, and an LLM in that posture produces them everywhere, in drafts and in replies alike. The drafting skill holds this too, but it loads only when drafting starts, after the posture has formed. So the text read first says it.

Starting from what can go wrong with a document pulls toward the same posture. A list of faults turns every look at a document into an audit, and the LLM defends, hedges and cites to pass it. Starting from what the later reader needs keeps the LLM writing for that reader.

**Why the instructions name RFM**

The skills that carry RFM's procedures describe their moments as moments in an RFM session. The LLM loads such a skill only if something in its context tells it the session is one. In a project full of RFM documents, the file names and the skills' own names do that. In other projects they may not, and before the first skill loads nothing else does. The instructions are the only RFM text present from the first turn, so they name RFM once, in the sentence that says what the project is for. The short name is enough, because the skills use the same three letters.

**Why the line on saying it's done is narrow**

The LLM looks at the result before saying something is done, and says so when it could not check, so the human can decide whether the check is needed. "Did not" would let saying so stand in for a check the LLM could have made. Some unchecked claims will get through. The human catches those by reading, which costs less than reading bookkeeping on every reply.

## The Boundaries

**Not the procedures.** How to draft, write a file, or open and close a session belongs to the skills that load at those moments. The instructions name only the drafting skill, because nothing else marks the moment a draft begins.

**Not a guarantee.** The text sets the stance a session starts from. It cannot hold that stance on its own through a long session.

**Not pressure mode.** Working under delivery pressure is an exception to how a session normally runs. It is not covered here, because each line here stays in context for the whole session and an exception would take attention in every session that does not need it.

## The Open Questions

**[OQ-HOLD] Does the stance hold past the first few turns?**

Instructions read at the start of a session lose force as the session grows. How this text behaves deep into a long session is not known.

**[OQ-NARR] How much unchecked narration gets through with the narrow line on saying it's done?**

If many unchecked claims get through, what to do depends on why. The line may be too narrow, or the LLM may stop looking at results as the session grows. Which it is, and whether either can be met without bringing the bookkeeping back, is open.

**[OQ-REDT] Does naming the pull hold where it is tested: the LLM's own drafts, and a push under pressure?**

Asking the LLM to red-team its own work has not held as a standing rule, and an LLM pushed by a frustrated human tends to comply. Whether naming the pull does better in either case is not known.

**[OQ-COST] Does asking who pays for an addition catch what "more than the problem needs" let through?**

The line fails if the LLM still sees nobody paying for an addition it should have questioned. A failing line still takes attention from the others. It could fail because the question does not put the LLM where the cost lands, or because it loses force among the other lines. What follows depends on which, and is open.

**[OQ-MARK] Does one short example bring back marking additions?**

The wording known to work is a fixed sentence, "You didn't ask for this, I'm adding it", used while both parties were watching for it. Whether one short example does the same, with nobody watching, is not known. It works if additions are marked, including those inside a draft or an answer to something else, and the mark stays off replies that add nothing. It fails if additions go unmarked or the mark appears on most replies. Also not known: whether unmarked additions are mostly those inside something else, and whether the fixed sentence would help there or something else would.

## The Hard Lessons

**[HL-GUARD] Guards added one at a time turn the instructions back into supervision.**

Each rule written against a failure looks justified from inside the work. Their effect together, casting the LLM as an executor, shows only when the text is read whole, from outside.

---

*always-on instructions reasoning // [living]*
