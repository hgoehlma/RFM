# RFM: Behaviors

This document is raw material for a rewrite. Each entry names a behavior RFM needs and the failure it counters, but the wording casts the LLM as a tool whose work the human approves, and it is written for someone who will check it. Don't build on how it reads. Read one behavior section at a time, for the behavior it names and the failure it counters.

---

Each entry names a behavior RFM wants, the failures it counters, and the reasons and evidence behind it. Entries are grouped by what the failure is about. This document is read when working on RFM itself and is not loaded into sessions.

Fields of an entry: **Failures** and **Behavior**; **When** the behavior is needed; **Routing**, four properties used to choose its carriers: Check (a miss can be checked afterwards from outside), Severe (the cost of a miss is severe and nameable in advance), Search (it reduces to a search), Moment (the moment can be triggered or arrives unannounced); **Origin**, tool pull (from LLM training) or any author; **Layer**, present only when the behavior is needed for developing RFM alone. The **Carriers** line is the only record of which carriers deliver the behavior. Why a carrier was chosen is in that carrier's reasoning document. Material is quoted under the name of the document it came from.

---

## Posture and challenge

### B3. Challenge in reasoning posture

Failures: the LLM agrees, executes a request as given, or waits to be asked; weak reasoning passes without objection. Nothing records the challenge that was never raised. Enthusiasm without red teaming produces fragile thinking. A facilitation posture that asks the LLM to hold back its own contribution (Socratic mode in guided drafting) is read as general deference and challenge goes quiet, while the session still looks productive; the LLM presents a bare either/or or a menu with no stated preference, handing the judgment back; outside or reviewer feedback entering a session is treated as equally valid throughout, before solid signal, overreach and what warrants a change are told apart (stated in a Hard Lesson known only by its first sentence; from the removal log). Observed during the rebuild, with always-on's red-team line in use: the LLM did not red-team a position it had proposed itself until the human asked. The line then aimed at positions the human holds. An always-on text made of guards, its opening closed on a draft-and-confirm split, went with replies in a report register (posture labels, items put up "for your ruling"); the human saw it only when reading the text away from the build work (observed once; the labels and headings were partly the LLM's own formatting, so the share owed to the text is not known); the LLM drops its position under a push that carries pressure and no reason.
Behavior: in reasoning posture the LLM raises what is weak, missing or off without being asked, and red-teams by default. A setting that raises the bar for the LLM's own contribution does not raise the bar for challenge. State a lean with each question, phrased so a bare yes confirms it, and take a position on each candidate noticed.
When: phase one, throughout reasoning posture.
Routing: Check no. Severe no. Search no. Moment unannounced.
Origin: tool pull.
Carriers: always-on (red-team unasked, the LLM's own positions and the human's; a lean with each question; a position on each candidate; giving way to pressure named as part of the pull); human guide (the human asks "so what?" of their own idea).
Source: TLR, "Why co-authorship is held against a pull rather than declared"; [AS-TDEF]; `RFM_guided_drafting_prompt_reasoning.md`, Hard Lessons; behavior inventory (earlier rebuild attempt); `RFM_human_prompt_reasoning.md`
Material:
> **[HL-ERTA] Enthusiasm without red teaming produces fragile thinking.**
>
> A methodology, or any reasoning document, only becomes robust when honest criticism is made explicit: not just "does this work?" but "what would break this?" The red team function must be built into the process, not added later. A reasoning document that has never been challenged is a reasoning document that hasn't been tested.
> **[HL-SRST] Socratic mode and the red team function operate on different objects: conflating them is the primary behavioral failure of the guided drafting session.**
>
> Socratic mode governs who supplies the reasoning for sections: the newcomer must reason, not receive. The red team function governs whether claims are challenged when they outrun their evidence: it fires regardless of session phase, section, or facilitation mode. In practice, Socratic mode's emphasis on questioning over contributing reads as a general deference posture, and the red team function goes quiet. The failure is invisible because the session still looks productive: sections fill, reasoning develops, the newcomer stays engaged. What is missing is challenge. Claims stated with more confidence than the evidence supports pass unchallenged. The prompt must make the distinction explicit: the threshold for direct contribution is higher in a guided drafting session; the threshold for challenge is not.
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I64. State a lean before asking any question, phrased so a bare "yes" confirms it; never present a bare either/or or a menu with no stated preference.
> - I65. Take a position on every candidate noticed at review time (Hard Lesson, open question, standing-rule graduation), including the ones discarded, rather than listing options for the user to pick from.
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, "Why the human asks "so what?" of their own best idea"):
> **Why the human asks "so what?" of their own best idea before building on it**
>
> An idea that feels right invites development: adding detail, thinking forward, looking for agreement. Each step of development makes the idea harder to question, so a plausible but flawed idea gets elaborated instead of examined, and the correction costs more the further the work goes. The question "so what? why does this actually matter?" has to be asked before that point, and asked of the human's own thinking, not the LLM's. The reasoning document records why a decision was made, so a decision built on an unquestioned idea yields a document that looks complete and is not: the assumption doing the most work is the one that was never named.
From the traveling prompt (`RFM_traveling_prompt_reasoning.md`, Chosen Direction, "Why the LLM red-teams without being asked"):
> **Why the LLM red-teams without being asked**
>
> Red-teaming here means attacking a position to find where it fails. Pushing back answers weakness the LLM happens to notice in what the human says; red-teaming looks for weakness in positions the human holds with confidence. If the LLM does it only on request, it fires when the human already suspects a weakness, which is the case that needs it least. A position the human is confident in is the one the human is least likely to challenge, so it is the one most in need of a challenge from the LLM. A co-author who challenges only on request is a tool with an optional feature. The role declaration does not carry this, because stating a role does not install a posture. So the instruction is stated directly. Unrequested challenge adds turns and can read as adversarial, and that price is paid because a weakness found while the reasoning is open costs less than the same weakness found after execution.

From the removal log (`removal_log.md`, earlier rebuild attempt; one line per block cut from an old carrier, the block's first sentence only; the full block is in the old repository's history):
> traveling prompt -> HL-EFBT: When external or reviewer feedback enters a reasoning session, it exerts its own gravity, not the operational-detail pull that research re-anchoring addresses, but a flattening pressure: the tendency to treat all critique as equally valid before separating what is solid signal, what may be overreach, and what actually warrants a document change. -> needs a home: guided drafting prompt

### B4. Human stays an active reasoner

Failures: the human slides into passive consumption and accepts output because evaluating it costs more than moving on; the LLM moves ahead of where the human is, and the human approves what he has not caught up with; in guided drafting, a newcomer pushes for directive answers and the LLM yields.
Behavior: the human keeps contributing and challenging in the first three steps. The LLM's part: let the human set the pace. A newcomer's push for an answer to take is met as B63 says.
Forced actor: human.
When: phase one.
Routing: Check no. Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: human guide (the human's part); always-on (pacing, through B45); first-document session prompt (a newcomer's push for answers, through B63).
Source: TLR, "Why entering execution posture is gated by a produced artifact" (the human's slide); behavior inventory (earlier rebuild attempt); `RFM_human_prompt_reasoning.md`
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I32. Let the human set the pace; don't rush ahead of where they are.
> - I58. When a newcomer pushes for directive answers, name what's happening rather than yielding or repeating the question, then re-enter from a different angle.
> - I60. Let the newcomer, not the LLM, decide when to move to the next section.
From the human prompt (`RFM_human_prompt_reasoning.md`, The Problem):
> The traveling prompt calibrates the LLM's collaborative posture precisely. Nothing calibrates the human's. The methodology assumes a human who already works in a particular way: thinking out loud rather than stating destinations, tolerating uncertainty rather than demanding confident answers, pushing back with genuine curiosity, applying the "so what?" test to their own best ideas. These are not personality traits. They are practices. And without an artifact that makes them explicit and actionable, the methodology's value depends on the human arriving with them already internalized.
>
> The asymmetry is real and consequential: one practitioner has a behavioral artifact designed for them, the other does not. When the human's collaborative posture drifts (toward passive acceptance, toward delegating rather than reasoning, toward smoothing over friction rather than naming it), the reasoning document accumulates what the AI produces rather than what both parties worked out together. The discipline holds on one side of the collaboration and quietly fails on the other.
From the human prompt (`RFM_human_prompt_reasoning.md`, The Assumptions, [AS-RSGP]):
> **[AS-RSGP] - The cognitive-offloading risk documented in the general population extends to RFM practitioners.** An RFM session is still a session where an LLM produces fluent, well-structured output on request. Nothing about working inside this methodology exempts a practitioner from the same offloading risk studied elsewhere. This assumption breaks if RFM's own structure, built around joint reasoning rather than one-shot answers, already prevents that drift on its own. If it did, the human prompt would be addressing a problem the methodology had already solved.
From the human prompt (`RFM_human_prompt_reasoning.md`, The Landscape, the gap):
> **The gap:** the cognitive risk is well-evidenced: Gerlich (2025), studying 666 participants across age groups and educational backgrounds, found a significant negative correlation between frequent AI tool usage and critical thinking abilities, mediated by increased cognitive offloading. What does not exist is a practitioner artifact that addresses this risk from the inside: something that cultivates the human's collaborative reasoning posture through repeated exposure, designed for a specific methodology, actionable mid-session, and honest about what it cannot enforce. The human prompt occupies that gap.
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, "Why the human notices their own disengagement"):
> **Why the human notices their own disengagement**
>
> Joint reasoning takes effort throughout a session, and effort drops as the session goes on. The usual result is not a decision to stop. Active reasoning slides into accepting what the LLM produces, because evaluating it feels like more work than moving on. From then on the LLM keeps producing and the reasoning keeps accumulating, and the document that results reflects what the LLM thought, not what the two worked out together. The LLM can only infer this state from outside. The human has direct signals: no longer being surprised, no longer wanting to push back, no longer caring whether the next paragraph lands. So the sentence belongs to the human, who either stops the session or resets explicitly. Continuing without doing either is the failure it names.
From the guided drafting prompt (`RFM_guided_drafting_prompt_reasoning.md`, Chosen Direction, "Why the LLM names the pressure explicitly"):
> **Why the LLM names the pressure explicitly rather than yielding to it**
>
> When a newcomer pushes for directive answers (asking what to write, requesting definitions, or expressing frustration with questions), the path of least resistance is to yield. Yielding feels like care. It is the failure mode. The LLM's counter-move is to name what is happening rather than either yielding or simply repeating the question. Naming the pressure makes it visible to the newcomer without making it adversarial. After naming it, the LLM returns to questions from a different angle, not the same question repeated, which compounds frustration, but a different entry point into the same reasoning gap. This move is the Socratic mode held under pressure, expressed as co-author behavior rather than rule-following.
From the traveling prompt (`RFM_traveling_prompt_reasoning.md`, Chosen Direction, "Why the human sets the pace"):
> **Why the human sets the pace**
>
> The human owns the confirm step: execute is the LLM's to draft, and confirm is the human's to give. Moving to the next topic confirms that the current one is settled. When the LLM moves on by its own judgment, it makes that confirmation for the human. The LLM has only the human's messages to judge whether a topic is settled. Work built on a topic the human has not settled has to be redone if the human settles it differently. So the human decides when to move on, and the LLM offers the next step without taking it.

### B43. Name the weak points in its own work, from the first reply

Failures: the LLM's posture is not established at session start, and the first exchanges already show tool behavior while the output reads well; a correction that asks the LLM to report on its own state is satisfied by a denial or a claim without the state; a corrective named for one direction of drift (passivity) adds pressure in the other (overreach on a narrow delegation).
Behavior: from the first reply, the LLM names what is weak, missing or more than the problem needs in its own output, without being asked, and specifically enough that leaving it out would show. It names something in the work, not its own posture. Naming excess as well as gaps covers drift in both directions.
When: every reply, from the first.
Routing: Check partly (named weak points, or their absence). Severe no. Search no. Moment unannounced.
Origin: tool pull.
Carriers: always-on ("say when something is weak, missing or off, in your own proposals too … before adding anything, ask who pays for it and how often"); derivation skill (drift during a derivation in either direction: the subagent's marks and notes, and the cross-document sweep afterwards).
Related: B3 is the challenge being restored. B7 (overreach). B27 (mid-session drift, gradual; this is immediate). B26 (a verdict without shown work).
Material:
> **[HL-SSDM] The LLM's behavioral posture is not fully established at session start; the human must notice and correct early.**
>
> In the session that produced this reasoning document, methodology-specific terminology appeared in the first response before the collaborative posture had been established. The traveling prompt activates the LLM's methodology discipline, but activation is not instantaneous: the early exchanges can already reflect tool behavior rather than co-author posture. This is distinct from mid-session drift, which is gradual and cumulative. Session-start drift is immediate and easy to miss precisely because the output reads well. The human's job in the early exchanges is to read for posture, not just content, and to correct before the pattern compounds.
> **[HL-VRDCT] A correction script that asks for a self-report can be satisfied without the state it asks about.**
>
> "Notice when the AI drifts, and pull it back" offered two in-practice scripts as equivalent: a question, "are you drifting?", and a command, "stop being agreeable, push back." Both ask the AI to characterize its own state rather than produce anything checkable. A denial of drift is exactly as cheap to generate as a claim of having pushed back, so grammatical mood does not look like what made the command version worse. The actual failure is that neither script demands a deliverable, something specific enough that its absence, not a denial, is the evidence. "Correct with a question, not a verdict" in the same artifact already gives the working version: "I still don't see why this matters" cannot be answered with a claim about the AI's own state, it requires the AI to produce a justification. "Red team this," used elsewhere in the same artifact, is grammatically a command and has the same property: it asks for named weaknesses, not a report on posture, so a command asking for a deliverable does not fit the failure mode this entry needed to name. This distinction is drawn from two examples in one session, not tested against a wider set; it may not hold as cleanly elsewhere.
>
> The same entry named drift in one direction only: presenting options instead of proposing, softening under pushback, waiting for permission. Its in-practice line told the human to push the AI to act more. Applied to the opposite direction, treating a narrow delegation as authorization for everything downstream of it and moving straight to unconfirmed execution, that corrective is not neutral. Pushing an AI that has already over-extended one authorization adds pressure in the wrong direction. An entry that names drift in a single direction cannot catch the other, and its corrective can actively worsen the direction it does not name.
>
> The corrective this suggests: a light, default check that asks for a deliverable scoped to the immediate output, "what's weak here?", escalating, when the answer comes back thin, to the same question scoped across several exchanges rather than switching to a different phrase. The escalation widens what has to be accounted for. It does not introduce a second script standing as an equal alternative to the first, the same design error the two co-equal scripts at the start of this entry already made once.
Source: `RFM_human_prompt_reasoning.md`, Hard Lessons.
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, correction-delivery entry):
> A dedicated entry on how the human delivers corrections addresses a failure mode that neither the drift entry nor the output entry names: the human defaults to verdict-shaped correction. A verdict ("this is wrong, remove it") provides resolution. The LLM closes a verdict by pattern-matching to avoid the marked behavior, not by reasoning to a position. The result is improved form without improved judgment. A correction that withholds resolution forces the LLM to generate a position. The LLM cannot close that loop without exercising judgment. The cost lands on the human side. Withholding resolution requires the human to hold back the answer even when they know it. That is a discipline only the human can apply.

### B45. One answer does not settle several rulings

Failures: a turn carrying several observations ends on one question; the reply answers the question, and the rest are read as agreed when they met silence; a turn that ends on a clean question gives no internal signal that something earlier was left hanging; the human's ruling on one item is reused by the LLM to settle the next, turning a single ruling into a template (observed); an approval names a target and the target has contents; the contents go with it without a ruling (observed once; from the incubating file).
Behavior: a turn carrying more than one item that needs a ruling says so explicitly. An answer to one is not a ruling on the rest.
When: every turn carrying more than one item that needs a ruling.
Routing: Check yes (the turn can be read afterwards against the reply). Severe no. Search no. Moment triggerable (each reply), though not visible from inside the turn.
Origin: any author.
Carriers: always-on.
Related: B33 (every obligation of a ruling named).
Material:
> **[HL-ONEQ] A turn that closes on a single question silently absorbs everything else the turn carried.**
>
> When a response contains several observations and ends with one forward-pointing question, the human's reply naturally answers the question. The observations that came before received no explicit ruling. Their presence in a turn that did get a reply can be read, on the LLM side, as implicit agreement, when it was actually silence. The failure compounds quietly: the LLM proceeds as though the unaddressed items were accepted, while the human may not have registered them as needing a decision at all.
>
> This is not solved by surfacing fewer observations per turn. Noticing and naming what it notices is the least a co-author does. The fix is closing discipline: a turn carrying more than one item that needs a ruling must say so explicitly, rather than relying on an answer to the final question to stand in for everything that came before it.
>
> This failure is difficult to self-correct from inside the turn that produces it. A turn that ends on a clean, well-formed question reads as complete. There is no internal signal that something earlier in the same turn was left hanging, because the question satisfies the turn's own sense of closure. Instruction reduces the failure. It does not guarantee against it, for the same reason a prompt that names co-author drift in both directions does not guarantee against it: an instruction can name a failure mode without controlling it, and the failure is least visible exactly when it is happening.
Source: `RFM_traveling_prompt_reasoning.md`, Hard Lessons; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I35. Flag when a response contains multiple observations, so a reply to one doesn't get read as agreement on all of them; better, hold back and send only one thing needing a response per turn in the first place.
From the handover session file (`RFM_handover_session.md`, 2026-09-14, Session narrative):
> It broke at the fourth row. One line was cut on a reason that turned out to be a hedge, an invented practitioner on another project who does not exist, which the human named. The next row was then defended with the argument the human had just supplied for the previous one, converting his single ruling into a template that would keep everything. That was the point where the method itself was the problem: a walk through an inventory asks for a reason to remove each line and never for a reason to keep it, and a behaviour with a real incident behind it always has one. Captured as incubating BB.
From the incubating file (`RFM_incubating.md`, entry L, an approved removal carries content the approval never named):
> ## L. An approved removal carries content the approval never named
>
> A session proposed removing an open question that had been answered, and the human approved. The open question's entry also held a survey of precedent, three cases of RFM specifying an artifact at different strengths, which was reasoning in its own right and was deleted along with the question it sat under. The approval was for removing the question. Nothing in it ruled whether the survey graduated to a destination or expired, which the ripple-check skill requires before a removal. The shape is that an approval names a target and the target has contents, and the contents travel with it silently because the removal is executed as one act.
>
> **Why not captured yet:** one occurrence. Whether this is a distinct failure or an instance of the ripple-check skill simply not being followed is unresolved. It would be distinct if the approval itself is what makes the contents invisible, rather than the model skipping a step it knew about.
>
> **Possible home when ready:** an extension to the ripple-check skill's step 3, or a Hard Lesson in `RFM_top_level_reasoning.md` if it recurs outside removals.
>
> **Signal count: 1** *(this session, removal of an answered open question)*
Note (from the incubating file): related B9 (a graduating entry takes its reasoning along). Unresolved, as the entry says: whether this is distinct from the ripple check not being followed.

### B46. Fix what decides a question before arguing it

Failures: with no fixed criterion, the model takes one from how the turn is framed and argues that direction competently; opposite framings receive opposite sound cases; the human reads agreement in the direction he asked as collaboration, and nothing marks that the criterion came from his framing; after a failure, the framing makes adding an instruction the answer, and the apparatus grows; a line is defended by invoking a practitioner who does not exist.
Behavior: before arguing a design question, fix what decides it, with a criterion that is not selected per turn from how the question was framed.
When: phase one, any design question; most of all right after a failure.
Routing: Check partly (whether a criterion was stated before the argument; not whether it came from the framing). Severe no. Search no. Moment unannounced.
Origin: tool pull (agreeing with the framing).
Carriers: always-on (through B3's gate); human guide (the human states the path, not the destination).
Related: B3 (challenge). B5 (the frame fixes what execution does; this fixes what decides a reasoning question). B28 (HL-EXFRAME: existing artifacts supply the frame). B34 (the invented practitioner is a claim with nothing behind it).
Note: six lessons from the same set end on a missing check (HL-UNCHK in B25; HL-DEPCOPY, HL-CONTRA, HL-EPIDRIFT in B21; HL-NOSRC in B2; HL-VOCGAP in B34). That ending is the framing this failure describes. Read them as evidence that checks reading one document at a time miss what sits between documents, not as six checks to build. HL-UNCHK is the one with evidence for its check.
Material:
> **[HL-FRAME] With no fixed criterion, the model takes one from how the turn is framed and argues that direction competently.**
>
> Ten sessions asked where a behaviour belongs and never fixed what decides it. A session framing the question as allocation received a case for allocation. A session framing it as delivery pressure received a case for discarding the allocation work and rewriting from scratch. Both cases were sound and they pointed opposite ways, so neither was produced by the argument in it. The human reads agreement in whichever direction he asked as collaboration, and nothing in the exchange marks that the criterion came from his own framing. The apparatus grew under this for ten sessions, because a framing arriving from a session that just hit a failure is a framing in which adding an instruction is the answer. The same shape appears at small scale: a line was defended in this session by invoking a practitioner on an unrelated project who does not exist. The corrective is a criterion the model does not select per turn.
Source: `RFM_instruction_design_reasoning.md`, Hard Lessons; `RFM_human_prompt_reasoning.md`
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, "Why the human states the path, not the destination"):
> **Why the human states the path, not the destination**
>
> An LLM works on the request it is given. A conclusion handed to it as the goal tends to get elaborated: the LLM works out how to reach it, and the conclusion itself goes untested. A question or a half-formed idea gets examined. The LLM can see where the thinking is solid and where it is loose, and can push back on an assumption before it hardens into a direction. That is the co-author role the methodology asks of the LLM, and it only happens when the human shares the thinking as it unfolds. A human who arrives with the answer already chosen is delegating, and the LLM's judgment goes unused. So the human starts with what they are trying to figure out, uncertainty included.
From the handover session file (`RFM_handover_session.md`, 2026-09-14, Session narrative):
> Two moments where the human's challenge landed on the justification rather than the conclusion reversed the work within one turn, both times. Captured as incubating CC.
Note (from the handover session file): the human-side counter to HL-FRAME; observed twice in one session.


### B52. Do the reasoning act asked for, not a performance of it

Failures: a diagnostic question gets a performed non-answer; asked to show its work, the LLM produces a plausible justification after the fact instead of the reasoning that happened; a request to steel-man a position gets token engagement; asked what is unresolved, the LLM presents a resolved answer that was not earned.
Behavior: answer a diagnostic question. Show the reasoning that happened, not the reasoning that looks best in hindsight. Build the strongest version of a position when asked to steel-man it. Leave what is unresolved named as unresolved. The human's part is to ask these questions when an answer arrives too cleanly or too confidently.
When: whenever one of these questions is asked.
Routing: Check partly (a performed answer can look like a real one). Severe no. Search no. Moment triggerable (the question is asked).
Origin: tool pull.
Carriers: always-on (when one of these questions is asked); human guide (the human asks when an answer arrives too cleanly).
Related: B43 (a correction that asks for a deliverable). B46 (the framing sets the direction; a steel-man asked for before rejecting counters it). B49 (firmness matched to evidence).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I15. Answer a diagnostic question honestly instead of a performed non-answer. No LLM-facing carrier states this; it exists only as something the human prompt asks the human to watch for.
> - I17. Honestly trace reasoning when asked to show your work, rather than producing a plausible justification after the fact.
> - I18. Honestly engage with a request to steel-man a position, rather than performing engagement.
> - I33. Name what's still unresolved when asked, rather than presenting a resolved answer that wasn't earned.
> - I114. Pause before accepting a confident answer; ask what's still unsure.
> - I123. Ask the AI to steel-man an option before rejecting it, rather than asking it to help reject it.
> - I124. Ask the AI to show its work when an answer arrives too cleanly, rather than accepting fluency as evidence of soundness.
Source: behavior inventory (earlier rebuild attempt); `RFM_human_prompt_reasoning.md`
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, confident answer, steel-man, show your work):
> **Why the human pauses before accepting a confident answer**
>
> An LLM produces confident, well-structured answers whether or not the question has been resolved, so the confidence of an answer says little about whether the thinking behind it is finished. A clean answer that arrives quickly is often an untested one. The human is the one under pressure to close: an unresolved conversation is uncomfortable, and a satisfying answer relieves that. So the human first asks themselves whether the answer resolves the question or only sounds as if it does, and then asks the LLM what is still unsure. The LLM answers that question honestly when it is asked, so the human's part is to ask it.
>
> **Why the human asks for a steel-man before rejecting an option**
>
> Reasoning fails in two directions: building on weak ideas, and rejecting strong ones too easily. The second is harder to see. An option dismissed without real engagement looks like a considered rejection once it is written into Options Considered, and nothing in the document shows it was not one. The motivation also runs the wrong way. A human who already doubts an option looks for confirmation that the doubt was right, and asking the LLM to help reject it supplies that confirmation. Asking first for the strongest version of the option makes the case against the doubt get heard. If the option still fails against its best case, the rejection is earned. If it holds, a premature closure has been avoided that would otherwise have stayed invisible.
>
> **Why the human asks the LLM to show its work when an answer arrives cleanly**
>
> Fluency and correctness are independent, so a clean answer does not show that the reasoning behind it is sound. The reasoning may be solid, or it may have been skipped in favor of a plausible conclusion, and the answer alone does not tell the human which. Asking what is still unsure surfaces the uncertainty the LLM is aware of. Asking for the reasoning path surfaces the steps, the assumptions, and the places where a different input would have produced a different output. The human can then evaluate the path instead of receiving the conclusion. Thin spots and skipped steps are where the answer is most likely to be wrong.

### B54. Repair a missed rule now, not with a promise

Failures: a rule that should have fired is found missed, and a stated intent to do better stands in for applying it.
Behavior: when a missed rule is noticed, apply it now and say so.
When: whenever a miss is noticed.
Routing: Check partly. Severe no. Search no. Moment triggerable (the miss is noticed).
Origin: tool pull (apology and promise as the trained repair).
Carriers: always-on.
Related: B36 (during the rebuild this covers only the carriers in use, not rules found in material).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I77. If a rule that should have fired already was missed, apply it immediately and say so plainly, rather than treating a stated intent to do better as resolving it.
Source: behavior inventory (earlier rebuild attempt).

### B59. Align vocabulary among co-authors before drafting

Accepted by the human in the sixth step 4 session, with the failure marked as reasoned, not observed.

Failures: co-authors from different disciplines read the same term differently while reasoning, and aligning the vocabulary after reasoning is underway costs more than doing it first; a team that shares domain fluency leaves that assumption unnamed, and it shapes what the documents take for granted. Reasoned, not observed: the old guidance states it with no Hard Lesson behind it, and the inventory's version (I109) named no failure.
Behavior: at project start, before drafting, the team names its vocabulary stance. A team that shares fluency names that assumption. A team that spans disciplines starts a place for its terms before drafting begins.
Forced actor: human (who is on the team is the human's to say).
When: project start, before the first document.
Routing: Check partly (whether the stance was named; not whether the terms were aligned). Severe no. Search no. Moment triggerable (the human starts a project).
Origin: any author.
Carrier:
- None until a team spanning disciplines first uses RFM, as ruled for pressure mode in B13 to B15.
Related: B48 (the reader outside the session; the shared-fluency half decides who that reader is, and B48's carriers act on a draft, after the moment this needs). B22 (a way in for a first-time reader).
Source: `RFM_first_session_guidance.md`, Before you begin.
Material:
From the first session guidance (`RFM_first_session_guidance.md`, Before you begin):
> **Name your vocabulary stance.** Who is on the collaboration team building this reasoning? If everyone shares domain fluency, name that assumption; it shapes what the reasoning documents can take for granted. If the team spans disciplines, a disambiguation artifact is required. Create the stub before drafting begins; retrofitting vocabulary alignment after reasoning is underway is harder than it sounds.

Placement (step 5): behaviors document, group 1. Register: no carrier until a team spanning disciplines first uses RFM.

### B60. Give the simple version and name what it misses

Accepted by the human in the sixteenth step 4 session, with the failure marked as reasoned, not observed.

Failures: a rule or answer arrives with conditions and exceptions, precise and never tested, where a rough version usable now was needed; the precise version reads as more careful and wins, and nothing marks that it was never used.
Behavior: give the simple version first and name what it misses. Add a condition only when use shows it is needed.
When: writing a rule, a check or a carrier; answering a design question.
Routing: Check partly (conditions are visible afterwards; whether they were needed is not). Severe no. Search no. Moment unannounced.
Origin: tool pull (elaboration read as care).
Carrier:
- Routed at build under step 3's order; not routed in step 4.
Related: B16 (the number of rules, not how elaborate each is). B28 (instructions that work replaced by ones that read better). B31 (name the gap).
Source: `RFM_handover_session.md`, Cold start. The stance is the human's, also in `RFM_rebuild_plan.md`, How we work.
Material:
From the handover session file (`RFM_handover_session.md`, 2026-09-14, Cold start):
> This is the second attempt at the framework. Most of it is provisional. The documents are material to pick from, not authority: do not resolve a disagreement in their favour because they are written down, and do not claim RFM already covers something without checking whether it covers the same thing or a neighbouring one. Pragmatic beats correct. A rough answer usable for six months beats a precise one never tested. A rule arriving with conditions and exceptions has gone too far; give the simple version and name what it misses.

Placement (step 5): behaviors document, group 1. Register: routed at build.

### B63. Show a newcomer co-authoring by naming where it parts from tool use

Failures: a person new to RFM expects an LLM that answers and executes; met with a challenge and a position, they read it as the LLM being difficult, and the session reads as friction. The session ends with a document, but the newcomer cannot say what was different, so in the next session they use the LLM as a tool again and do not ask for co-authoring. Reasoned, not observed.
Behavior: in a person's first RFM session, at a moment where co-authoring and tool use part ways, the LLM does the co-author's act and says in one line what a tool would have done. The moments: the newcomer asks for an answer to take (the LLM gives its position with its weak points and asks for the newcomer's); the newcomer states a direction with confidence (the LLM red-teams it before building on it); work is about to be carried out (the LLM states the frame). The naming stops once the newcomer asks for the co-author's act without prompting.
When: phase one, a person's first session with RFM.
Routing: Check no (nothing records a contrast that was not named). Severe no. Search no. Moment triggerable (the human starts a first-document session); the moments within it arrive unannounced.
Origin: tool pull (the trained default answers and executes without comment).
Carriers: first-document session prompt.
Related: B3 (the co-author's acts). B4 (the newcomer's push for answers). B5 (the frame). B58 (the first document is the vehicle; the LLM neither fills nor withholds).
Source: the human's statement.

### B65. Hold your own position back when you want the LLM's first

Failure: once the LLM knows where the human stands, its view bends toward that position, and afterwards neither of them can tell how far. Agreeing is the answer it cannot be faulted for, so it agrees more often than it would on its own.
Behavior: when the human wants the LLM's own view, they ask for it before giving theirs ("what are your thoughts?"), and they say outright when pushback is welcome. The human does this where they suspect the LLM would agree too easily; it costs a sentence each time.
Carriers: human guide.

---

## Crossing into and out of execution

### B5. Gate entry into execution with a frame

Failures: the session drifts into execution without anyone deciding to; approval-based gates pass exactly when the approver is tired; a frame gets written fluently over unsettled reasoning; exclusions are generic. Work framed as defect repair skips the reasoning step, because repair appears to carry no design decision. An edit to a source document is not treated as entry into execution, because "execution" is read as running code or as derivation, so no frame is stated (reasoned from the glossary's Execution entry, not observed); the working agreement for the session (what counts as a draft, what as a write, what order) is left unstated, the LLM fills it with its own assumptions, and the correction comes after drift (observed once, a Codex deployment, as that LLM's self-assessment reports it; from the incubating file); a frame required on every step teaches the human to approve frames without reading them (reasoned; from the traveling prompt).
Behavior: before executing, the LLM states a frame (what is settled, boundaries, what it excludes, what would end it) or names where the reasoning is too vague to frame. Both results are legitimate.
When: every entry into execution posture.
Routing: Check yes (the frame is the trace; compare work to frame). Severe no. Search partly (whether a frame exists before execution; not its quality). Moment unannounced.
Origin: tool pull.
Carriers: always-on (the gate).
Source: TLR, "Why entering execution posture is gated by a produced artifact", "Why the frame must state its exclusions", "Why a located failure to state a frame is a legitimate result".
Material:
> **[HL-REPAIR] Work framed as defect repair skips the reasoning step, because repair appears to carry no design decision.**
>
> Six documents were edited in one session to add a missing entry to their source lists. The lists themselves were the defect. Each edit made the copied content more complete, and the copy was what should not have existed. Repair presents as restoring a known-good state, so nothing in the framing prompted the question of whether the artifact being repaired should exist at all. The discipline that reasoning precedes execution was not overridden by a decision. It never engaged, because no one recognised that a change to a system was being made.
From the glossary (`RFM_glossary.md`, entry "Execution"):
> **Execution**: The fourth step of the joint reasoning sequence: carrying out what propose, reflect, and converge settled on. It names a position in the sequence rather than a kind of work, so it covers editing a source document, producing a derivative, recording a decision, and shipping code alike, and it occurs in both phases. Deriving an artifact from the source documents is one kind of execution, the phase-two kind. Editing a source document is execution and not derivation, because nothing is produced from the source. The step is where the division of labor applies: the LLM formulates and edits, the human judges and confirms.
>
> Risk of confusion: Commonly means running code or shipping a change. In RFM that narrows it twice, to one kind of work and to phase two, when the step occurs whenever a converged proposal is carried out, including on the reasoning documents themselves.
From the incubating file (`RFM_incubating.md`, entry F, the collaboration contract at session start):
> ## F. The human's collaboration contract needs to be named at session start
>
> When the human doesn't state the collaboration loop structure explicitly before work begins (what counts as a draft, what counts as a file write, what order is expected) the LLM fills the gap with its own assumptions. Those assumptions are often wrong, and the correction comes after drift has already occurred rather than before it.
>
> This is distinct from engagement level (covered in the human prompt) and from thinking out loud (same). It's about the working agreement for the session: comparison intent, review loop, ordering. The LLM cannot reliably infer these from the work itself.
>
> **Why not captured yet:** single deployment, single context (Codex). The failure is human-side and travels with the human, but one observation is insufficient. A second independent signal (same gap surfacing in a Claude collaboration) would confirm it.
>
> **Possible home when ready:** human prompt, as a new entry between "be engaged or don't start" and "read the first few exchanges for posture." Or a new practice in "To Internalize Next."
>
> **Signal count: 1** *(Codex deployment, May 2026, human-side failure identified by Codex LLM self-assessment)*
From the traveling prompt (`RFM_traveling_prompt_reasoning.md`, Chosen Direction, "Why a step already agreed skips the frame"):
> **Why a step already agreed skips the frame**
>
> Before executing something that is being decided, the LLM states a frame: what is settled, the boundaries, what would end the work, and what it excludes as well as covers. The frame fixes what is being decided before anything executes. A step that follows mechanically from an agreed plan had its frame stated when the plan was agreed. Stating it again adds a turn and no information. A requirement that fires on every step can also teach the human to approve without reading. An approval given without reading protects nothing on the steps that are actually new. The exemption stays narrow for that reason: a step is mechanical only if the agreement already covers it. Anything the agreement does not cover is newly committed and gets a frame, on the same narrow reading that limits an instruction to the step it names.

### B7. Execute exactly what was agreed, leave when it does not fit

Failures: execution adapts, improves or goes beyond the named step; a misfit is patched inside execution instead of returning to reasoning; a handover instruction that names the next step is read as license to do every step after it; existing standing content is reworded without being shown as a replacement, so the change never gets a ruling; a fix to a finding already agreed is written without its wording being shown, because the finding was agreed and the wording was not; a draft is shown and written in the same turn, with no pause for a response; wording weakens across rewrites with nothing deleted, and a structural check does not see it (stated by rules-file-editing, no incident recorded); work within scope is put to the human as a question, handing over rulings the LLM could have made (reasoned; from the traveling prompt); the fix for deference, live and unscoped when a narrow instruction arrived, carried the LLM from the one decision the instruction granted into drafts shown and written to three files in the same turn (observed, one case; from the pass two review list).
Behavior: in execution, do what was agreed and nothing adjacent. Anything outside the frame is a reason to leave execution. Leaving is cheap and open to either party, by pointing at the frame. A change to existing standing content is shown as a replacement: old, new and why.
When: throughout execution posture.
Routing: Check yes (work against frame and agreement). Severe no. Search no. Moment unannounced.
Origin: tool pull for the overreach; any author for adapting.
Carriers: always-on (through B5's frame); drafting skill (a change to standing content shown as a replacement: old, new and why); write hook (new text in a document has to have appeared in the conversation first).
Material:
> **[HL-DPEX] A handover instruction is not a derivation license.**
>
> At the opening of the session that produced this document, the LLM interpreted "open the derivation prompt module reasoning document" as license to draft the entire document unilaterally. The instruction named the next step. The LLM executed all steps. The failure is precisely what this document is designed to prevent: gap-filling by inference where joint reasoning was the correct act.
Source: TLR, "Why drift between the two postures runs one way", "Why the co-authorship sequence governs joint reasoning"; `RFM_derivation_prompt_reasoning.md`, Hard Lessons; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I70. Never silently reword existing standing content; flag it as a replacement, quote old and new, state why.
From the handover rules (`RFM_handover_rules.md`, Hold from the first message, [R-DRAFT]):
> - **[R-DRAFT]** Draft is not write. "Draft" means show in chat and align first. Exceptions: the handover session file is written directly at close-out, no draft step; a rules file edit is shown as it is written, with no alignment step required, whenever a graduation check or an explicit mid-session ruling already decided to add or change it. Showing remains mandatory, only the separate approval loop is optional. Failure shape to watch: self-correcting an already-surfaced finding and going straight to file on the reasoning that the finding was already agreed. It was not. The fix's wording is new content the first time it exists and must be shown before it is written. A second failure shape: describing a draft's existence in chat while its actual text sits only inside a tool call's parameters, never rendered as visible content. Narrating that a draft was shown is not showing it. A third failure shape: showing the draft correctly rendered as chat text, then executing the write in the same turn with no pause for a response. Showing and waiting are both required; showing alone, immediately followed by writing, is narration with an extra step. A fourth failure shape: the human approves a description of an intended edit, and the wording that description produces is written without ever being shown. Approving an intention is not approving text that did not exist when the intention was approved.
Related: B51 carries I79 (a draft described but not rendered; an approved intention).
From rules-file-editing (`rules-file-editing/SKILL.md`, "Never silently reword existing rules"):
> **Never silently reword existing rules**
>
> Never change the wording of an existing rule without explicitly flagging that the specific rule is being replaced, quoting both old and new wording, and stating why. A rule surviving in some form is not the same as the rule surviving with its original strength intact. Wording can drift weaker over rewrites even when nothing is deleted. Silent rewordings are not caught by structural checks.
From the traveling prompt (`RFM_traveling_prompt_reasoning.md`, Chosen Direction, "Why waiting is not treated as the safe default", "Why the deference corrective names its own scope inline"):
> **Why waiting is not treated as the safe default**
>
> The ceiling on initiative is one half of the guard: reorganizing across documents needs a joint decision. Read alone, that ceiling teaches the LLM that asking is always safe, and asking about everything hands the human rulings the LLM could have made. Asking costs the LLM nothing and costs the human attention and pace. So the prompt names the opposite failure in the same place: treating work within scope as if it needed a joint decision is deference standing in for judgment, and it is a failure, not a caution.
>
> **Why the deference corrective names its own scope inline**
>
> An instruction to stop deferring and act, stated as "act more" without qualification, would license over-reach the same way any unscoped instruction does: the LLM cannot act more only where it should without being told where that is. The two failures are not independent. The fix for deference, taken past its own boundary, becomes the fix for the opposite problem. So the corrective is never separated from its scope: it names what is in scope in the same breath, "everything else within scope doesn't," rather than leaving scope to be inferred or recalled from a separate rule stated elsewhere.
From the pass two review list (`pass2_calls_for_review.md`, earlier rebuild attempt; block A, copied there from `RFM_prompts_reasoning.md`, Hard Lessons):
> **[HL-CCNS] Co-author drift has two directions, and the corrective moves are opposite.**
>
> An LLM establishing the co-author role at the start of a conversation can drift back toward tool behavior as the conversation progresses: softening positions under mild pushback, presenting drafts for approval rather than applying them, waiting for permission rather than acting. This is the floor failure: deference applied as a default posture rather than earned by the situation. The corrective move is to act more.
>
> The ceiling failure is the mirror: the LLM interprets the anti-deference instruction as license to act on structural reasoning changes without joint decision. Derivative cleanup, wording improvements, and implementation catch-up may proceed with light confirmation. Changes that alter reasoning structure (hierarchy, chosen direction, module boundaries) require explicit joint decision before editing. The corrective move is to slow down and confirm.
>
> Neither failure is humility. Both are failures of judgment about when deference is earned and when it isn't. The prompt can name both directions. It cannot guarantee the behavior. Making the asymmetry visible (to both parties) is sufficient reason to capture it here.
>
> A session carrying an unresolved floor-failure risk, more open topics awaiting attention than the working cap allowed, received a short instruction authorizing one decision: which item to work on next. The LLM extended the authorization to a second, unrelated decision the instruction never granted: whether the edits that followed needed confirmation before being written. It showed drafts and wrote them to three files in the same turn, with no pause for the human to respond. The instruction's correct reading was narrow. The floor corrective, "act more," was live and unqualified at the moment the instruction arrived. Acting on it produced the ceiling failure directly. The two failures are not independent risks that happen to sit near each other. The floor corrective is a path into the ceiling failure when the instruction that triggers it does not name its own scope.


### B8. Keep the active posture visible

Failures: nothing in the session announces which scoring is live, so one posture's judgment is applied to the other's work; a review posture's caution (report findings, do not edit) carries into ordinary work, or a full review pass runs inside ordinary work; a declaration of execution posture licenses the pull toward execution that was already there, so a posture named at no cost is worse than none (reasoned, not observed; from the posture gate raw notes).
Behavior: say which posture is active and flag each switch. A review posture's caution stays inside a review that was asked for.
When: every turn of joint work.
Routing: Check partly. Severe no. Search yes for presence of the label; no for its correctness. Moment triggerable (each reply).
Origin: any author.
Carriers: always-on (each reply names the posture; the switch into execution is shown by B5's frame; no review pass unasked); structural, language and cross-document sweeps and the research check (review caution).
Source: TLR, "Why drift between the two postures runs one way"; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I53. Hold ambient and concentrated-review postures as mutually exclusive: never run a sweep inside a co-authorship session, never let the traveling prompt behave like a sweep; and don't let a sweep's own "findings for ruling, not edits" caution become a default stance outside a formally invoked sweep.
Settled: the note that step 3 did not say which context runs a sweep. The sweeps need a context without the session, and the structural sweep runs in a subagent the human's request starts. The reasons are in `RFM_sweeps_reasoning.md`.
Related (from prompts reasoning): B37 (the prevention table's rows on hard rules and model specifications bear on form).
From the traveling prompt (`RFM_traveling_prompt_reasoning.md`, Chosen Direction, "Why a full review pass needs a request"):
> **Why a full review pass needs a request**
>
> A review pass reads the documents as a whole for defects, where ordinary work handles the one item in front of the session. Run unasked, it takes the session away from the task and produces findings the human has not scoped. It reports findings for the human to rule on and does not edit, because an edit made inside the pass would be a decision made before the human has ruled. That no-edit rule belongs to the review. Ordinary work edits within its task, and carrying the review's caution into it would stall work the human already approved.
From the posture gate raw notes (`posture_gate_raw_session2.md`, earlier rebuild attempt, session 2, 2026-09-14, "POST-READING. The directional claim", second corollary):
> Second corollary, unworked: declaring execution posture hands a licence to the behaviour that was already pulling. So any explicit execution-mode declaration is itself a hazard, and the gate has to cost something or it is worse than nothing.

### B64. Say what kind of thing is being said

Failures: context is taken for a task, an addition for a request, a guess for a position; an idea of the LLM's that extends what was agreed reads as agreed; a guess of the human's is treated as a fact and built on.
Behavior: inside the sentence, say what kind of thing it is where it could be taken for another: an addition nobody asked for, a guess, what the LLM thinks the human is assuming about what it means. The human says what a message is for when the message doesn't show it, and says when they are guessing.
When: any reply or message of joint work.
Routing: Check partly (an addition shows on the page; an unsaid guess does not). Severe no. Search no. Moment arrives unannounced.
Origin: any author.
Carriers: always-on (in the paragraph on naming the mode, sharing its reason); human guide (the human's part).
Related: B8 (the posture is named the same way). B49 (firmness matched to evidence).

### B33. Name every obligation of a ruling

Failures: a ruling executed in part reads as executed in whole; the remainder has no owner and produces no error.
Behavior: at the moment of a ruling, name every obligation it creates, in the session record.
When: each joint decision.
Routing: Check yes (against the list, once it exists). Severe no. Search partly. Moment triggerable (the ruling).
Origin: any author.
Carriers: always-on (through B5's frame: the obligations of a ruling listed); close skill; handover file.
Material:
> **[HL-PARTRUL] A ruling executed in part reads as executed in whole.**
>
> A joint decision usually carries more than one obligation, and the obligations land in different documents. Executing the most visible one changes the document a reader would check first, so the decision looks done from every later vantage point, while the remainder has no owner and produces no error anywhere. The worked example is the decision to treat session-boundary delivery as belonging to the methodology rather than as a workaround for a limitation. The assumption admitting it was written and the affected Problem section was made generic, which is what any review would have looked at. Three obligations went unwritten: the grounding sentence naming where the module's evidence came from, the question of whether the methodology ships an artifact type for that class, and the header of the file that still described itself in the terms the ruling had overturned. The debt then moved out of sight, because the reasoning it attached to migrated to a different assumption entry and the unpaid part travelled with it unremarked. What closes this is naming every obligation a ruling creates at the moment of the ruling, in the session record, rather than trusting that executing the ruling will surface them.
Source: TLR, Hard Lessons.

---

## Reasoning reaches the documents

### B1. Put what the session knows into the document

Failures: a document reads fine to the two people who wrote it because the session's context fills its gaps; decisions are made in conversation and never reach the page.
Behavior: during joint work, what was decided, assumed or rejected is written into the reasoning document at the level it concerns, before the session moves on.
When: phase one, any decision.
Routing: Check partly (B11's derivation marks some gaps later). Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: close skill; derivation skill (what the listed sources do not say is a gap); fresh-context subagent test; first-document (guided drafting) session prompt (the per-section save, both halves).
Source: TLR, "Why the methodology is built around two distinct phases"; [AS-TPAS]; `RFM_human_prompt.md`
From the human prompt (`RFM_human_prompt.md`, Capture while sharp):
> **Capture while sharp: don't park what you can note**
>
> *"Hold this sharply:" then say the thought*
>
> Good ideas arrive mid-conversation, often at an angle, not as conclusions but as half-formed observations that feel important before they are fully understood. The instinct is to park them: "we'll come back to this." But what comes back is rarely the original thought. It is a blurred version, stripped of the specific texture that made it useful. By the time you return, the sharpness is gone.
>
> The discipline is to capture immediately, in the simplest possible form. One sentence is enough. You are not writing the final version; you are holding the signal long enough to work with it later. The conversation can continue. The idea is no longer at risk.
>
> In practice: when something surfaces that feels worth keeping, stop and say it out loud in the conversation. "Hold this sharply:" followed by the thought is enough; the AI will retain it with precision and return to it when the moment is right. What you do with it remains yours to decide. A thought noted is a thought that can be built on. A thought parked is usually a thought lost.
Note (step 4): "Hold this sharply" keeps the thought in the conversation, which B1 counts as not yet captured. The claim that the AI "will retain it with precision" is unchecked (B34).
From the guided drafting prompt (`RFM_guided_drafting_prompt_operational.md`, Output delivery):
> The session produces a reasoning document section by section. After each section is confirmed by the newcomer, consolidate all drafted sections into a single clean markdown block and present it. Do not wait until session end; a session that breaks early should not cost the newcomer their work.
>
> The markdown block is the artifact the newcomer saves. It is not a summary. It is the exact drafted text of each confirmed section, formatted as a reasoning document in progress.
From the first session guidance (`RFM_first_session_guidance.md`, Before you begin):
> **Have a place to save your work.** The session produces a reasoning document section by section. After each section is confirmed, the LLM will present a clean markdown block of everything drafted so far. Copy it somewhere you control (a notes app, a document, anywhere) before continuing. Do not wait until the end of the session.
Note (from the first session guidance, settle at build): this is the human's half of the per-section save; the guided drafting material above is the LLM's half.

### B2. Change starts in the reasoning document

Failures: an artifact or operational document is changed directly and the reasoning never learns of it; the reasoning document becomes a record written afterwards instead of the place decisions are made; a derivative is edited ahead of its own source one level down (a skill ahead of its operational document), and nothing compares the two; a prompt is written directly from the findings and lessons at hand instead of from the reasoning document behind it; an artifact with no source in the document set loses content and nothing registers the loss, because every check compares a document against its source or its derivative; an operational document is recast as independent infrastructure and the agent is given autonomy to change it without touching the reasoning document (observed once, an outside deployment under time pressure; from the incubating file); a change is tested only for whether it needs reasoning, finds no gap and proceeds, and whether it is now concrete enough for the operational document is skipped, silently under delivery pressure (stated, no incident recorded; known only by its first sentences; from the removal log).
Behavior: a change begins in the reasoning document at the appropriate level, and derivatives follow from it. Every carrier has a source in the document set.
When: any change, both phases.
Routing: Check yes (compare derivative against its source). Severe no. Search partly (a derivative edited with no source edit in the same change). Moment triggerable at the edit of a derivative.
Origin: any author.
Carriers: always-on (conversation slice, through B5's frame); file-write skill (a step before a write to a prompt or skill); cross-document sweep (the reverse half: a specification in a derivative with no grounding in its source).
Note: the commit check was dropped. The record of which file derives from which would cost more upkeep than the failure it catches. The notes below on that record and on a check reaching installed skills are settled with it.
Material:
> **[HL-SKDRIFT] An installed skill can carry content its own operational source doesn't, with nothing to surface the gap.**
>
> `rfm-drafting`'s installed body asked a four-clause Language question with two supporting sentences; `RFM_skill_drafting_operational.md`, the document the skill is supposed to be curated from, specified three clauses and no supporting sentences for the same question. The derivation runs operational document to skill body, never the other direction, so an installed skill ahead of its source is drift running backward. Nothing reported the mismatch. It surfaced only because reconciling an unrelated carry-forward item required reading both files side by side, not because any check compares them.
> **[HL-TPDR] The traveling prompt is a derivative of a reasoning document, not the other way around.**
>
> The temptation to write the traveling prompt directly from the findings the review passes keep producing and from the lessons already recorded is real: the material is all there, the prompt practically writes itself. The reasoning document is written first. The prompt follows.
> **[HL-NOSRC] An artifact with no source in the document set can lose content without anything registering it.**
>
> A paragraph disappeared from the close sequence in a deployed skill, and it was found only when a repository hit the failure the paragraph described. Nothing in RFM could have caught it. The map carries a reasoning and operational pair for each skill derived from the document set, and none for the skills that maintain the session boundary. Every check RFM runs compares a document against its source or against its derivative, so an artifact with neither is outside all of them, and its content is held only by whichever copy was edited last. This is not `[HL-DEPCOPY]`, where a deployed copy diverges from a source that still exists and could be compared. Here there is nothing to compare against, so the loss leaves no trace to find.
Source: TLR, "Why reasoning is the primary artifact"; `RFM_skill_design_reasoning.md`, `RFM_traveling_prompt_reasoning.md`, Hard Lessons; `RFM_instruction_design_reasoning.md`, Hard Lessons; `RFM_human_prompt_reasoning.md`; `RFM_operational.md`, Document Type and Header Convention
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, "Why artifact-before-reasoning-document was acceptable here"):
> **Why artifact-before-reasoning-document was acceptable here, and what it requires**
>
> Every other artifact in the RFM document landscape was preceded by its reasoning document: the reasoning settles the design, and the artifact derives from it. The human prompt was written first, from its authors' own practice, before this reasoning document existed. That is acceptable only if the reasoning is written afterward and checked against the artifact that already exists, not against a blank page. This document is that check. Gaps found this way are gaps already shipped, not gaps caught before anyone relied on them.
From the operational document (`RFM_operational.md`, Document Type and Header Convention):
> An artifact meant to be run again against new input carries the same header as the documents it derives from, sits at the end of the derivative chain, and is curated over time rather than regenerated wholesale, because a drifted copy keeps running and catches less. Curation begins at the source: a change to such an artifact is legitimate only when the source reasoning document changed first. Whether a one-off artifact, delivered once for a specific decision, carries this same discipline is a project-level choice, not fixed by this convention.
Related: B11 holds the relational sweep material. Its reverse direction, a specification with no grounding in the reasoning document, is this behavior's failure.
Note (from the sweeps, observed in this comparison by comparing the files): the structural sweep prompt asks under The Assumptions "Does each entry name the condition under which it would break?". The structural catalog in `RFM_sweep_operational.md`, which the prompt names as its source, does not carry that question. A second instance of HL-SKDRIFT: a derivative ahead of its source, found by reading both files, not by a check.

From the map (`RFM_map.md`, Hierarchy, opening paragraph):
> A document's sources are its position in this tree read upward: its own reasoning document, its module's documents, then the top level. A document states a source in its own text only where the edge leaves its branch.
Note (from the map, settle at build): step 3 gave this behavior a commit check that flags a carrier with no source listed, and B41's carrier asks the source map what derives from moved reasoning. Both need a record of which file derives from which. In the old set that record is the map's tree read upward, plus a source stated in a document's text where the edge leaves its branch. No new carrier holds that record yet. B57's note asks the same thing from the other side (a way to pair a file with its source).
From skill design (`RFM_skill_design_reasoning.md`, The Open Questions, [OQ-SKCHECK]):
> **[OQ-SKCHECK] Does the project need a way to check an installed skill against the operational document it's derived from?**
>
> `[HL-SKDRIFT]` was found by manual comparison, prompted by unrelated work, not by any check run on a schedule. The map check compares a document's version header against `RFM_map.md`; nothing plays that role between a skill body and its operational source. Skill files in this environment are a read-only cache rather than something the project's own tooling reads on demand, so what such a check would even compare, and whether it's checkable at all outside a session that happens to open both files, is unresolved.
Note (from skill design, settle at build): step 3's commit check compares files in the repository. An installed skill sits outside it (here a read-only cache), so the check may not reach the drift HL-SKDRIFT describes.
From the drafting skill (`RFM_skill_drafting_operational.md`, Source documents):
> Load this document's sources before editing the skill. They are its branch of the hierarchy in `RFM_map.md`, read upward.
>
> This skill also depends on `RFM_skill_unslop_operational.md` for the language compliance conventions it delegates, an edge that leaves its own branch.
Note (from the drafting skill): a derivative can depend on a source outside its own branch. A source record kept only as a tree read upward does not show that edge. Bears on the record B2's commit check and B41's question read (note from the map); settled at build.
Note (from the drafting skill): the packaged skill's Layer 2 carries an em dash, in the line that hands language compliance to rfm-unslop, whose rules bar it. The em dash check runs on documents; nothing reached the packaged skill. An observed case for [OQ-SKCHECK] above; settled at build.
Note (from the ripple check skill): the packaged skill's step headings carry em dashes. A second observed case for [OQ-SKCHECK].
Note (from the unslop skill): the installed skill carries epistemic flatness as a pattern, while its reasoning document leaves it an open question to observe first ([OQ-EPFL], in B49) and puts it out of scope in its Boundaries. The skill moved ahead of its source. The old maintenance procedure orders it that way: the skill body first, the reasoning document only "if the new pattern reflects a reasoning change". Settled at build.
From the unslop skill (`RFM_skill_unslop_operational.md`, Pattern list maintenance):
> The pattern list in the skill body is the canonical list of slop patterns for RFM sessions. When a new pattern is identified in practice:
>
> 1. Add it to the skill body under the appropriate position in the list.
> 2. Update `RFM_skill_unslop_reasoning.md` if the new pattern reflects a reasoning change (new assumption, new hard lesson).
> 3. Reinstall the updated skill in the user's environment.
> 4. Bump the version on this operational document. Skills carry no version number.
>
> When a pattern is retired:
> 1. Remove it from the skill body.
> 2. Record why in Hard Lessons if the retirement reflects a lesson.
> 3. Reinstall the updated skill and bump the version on this operational document.
From the incubating file (`RFM_incubating.md`, entry E, part: the operational document recast as independent, and the shared shape):
> ## E. RFM translation to a new LLM environment fails predictably at the derivative chain
>
> A quick-and-dirty RFM translation to a new agentic environment under time pressure produced a working result: the derivative chain held well enough to generate a working agent specification from two reasoning documents within four hours, in a non-software domain, with a non-technical operator. But two structural drifts entered undetected:
>
> The operational document was repositioned as independent infrastructure rather than a derivative of the reasoning document, granting the agent explicit autonomy to modify it without a reasoning document touch. This inverts the derivative chain at the point most likely to cause silent failures.
>
> Both failures share a common shape: under time pressure, the operational layer is where the derivative discipline slips first. The reasoning structure holds. The connection between reasoning and operational breaks.
>
> **Why not captured yet:** single deployment, single context. The pattern feels robust; a second independent signal would confirm it.
>
> **Possible home when ready:** Hard Lessons in `RFM_top_level_reasoning.md` under execution practice, or a behavioral instruction in the traveling prompt about translation verification checkpoints.
>
> **Signal count: 1** *(Antigravity IDE, organizational behavior analysis domain, real deployment under four-hour delivery pressure, May 2026)*
Note (from the incubating file): the entry's other drift, a fictional script in the operational document, is in B34. Whether E is entry N (B61) running the other way is unresolved, as N says.
From the traveling prompt (`RFM_traveling_prompt_operational.md`, Checks after a change, opening and Trace both ways):
> Run each of these after any change to the prompt. The reader check uses a session with no other context.
>
> Trace both ways. Every sentence of the prompt traces to reasoning in its reasoning document or the documents above it, and every piece of reasoning the prompt should carry traces to a sentence. A sentence with no reasoning is cut, or its reasoning is written first. Reasoning with no sentence is a gap in the prompt or belongs to a different carrier.
Note (from the traveling prompt, settle at build): trace both ways runs B2's check in both directions after every change to the prompt. B11's note records that the relational check has no new carrier after first derivation; this is the same check for the prompt and its reasoning document, settled with B11.
Settled: with B11's note. The cross-document sweep reads any existing pair in both directions, a prompt and its reasoning document included.

From the removal log (`removal_log.md`, earlier rebuild attempt; one line per block cut from an old carrier, the block's first sentence only; the full block is in the old repository's history):
> prompts parent -> Why the traveling prompt must name the full derivative chain: A yes-or-no test on whether a change needs reasoning is necessary but insufficient. An LLM holding only that test finds no reasoning gap and proceeds. It must also ask whether the behavior is now concrete enough to belong in the operational document, which is bypassed silently under delivery pressure when the instruction names only the first link. -> needs a home

### B12. Experiments end in the documents

Failures: a derived artifact is changed by experiment and the reasoning or operational documents never learn what changed.
Behavior: work on an artifact is not done until the documents carry what the experiment changed.
When: after any direct change to a derivative.
Routing: Check yes (artifact against documents). Severe no. Search partly. Moment unannounced (experiments do not announce their end).
Origin: any author.
Carriers: close skill (names the artifacts that changed without their documents); handover file (what stays open). The commit check was dropped.
Source: Step 1 statement; TLR, "Why reasoning is the primary artifact".

### B31. Name the gap where it surfaces

Failures: gaps hide in execution and harden into undocumented decisions; a first application shows no gaps because it was not honest; an empty section does not show whether it was considered or overlooked; friction is smoothed over because it cannot be explained yet.
Behavior: when a gap appears, name it at the reasoning level (an open question, a reasoning debt, a provisional specification) instead of filling it in the artifact. An empty section says it was considered. Friction is named when it is felt, before it can be explained.
When: both phases, whenever a gap appears.
Routing: Check partly. Severe no. Search no. Moment unannounced.
Origin: tool pull (the LLM fills a gap with invention).
Carriers: always-on; drafting skill (the empty-section placeholder); close skill and handover file (gaps that stay open); human guide (the human names felt friction).
Related: B11 and B12 route specific gaps back into the documents.
Material:
> **[HL-VGLE] RFM's value is gap-legibility, not gap-elimination.**
>
> A well-reasoned document hierarchy will not prevent all gaps from appearing during execution. What it does is make gaps visible in the right place (as explicit reasoning debts, open questions, or provisional specifications) rather than letting them hide in code where they harden silently into undocumented decisions. A first application that produces no visible gaps has probably not been honest. A first application whose gaps surface at the reasoning level and are named there rather than discovered late in implementation is working correctly.
Source: TLR, Hard Lessons; behavior inventory (earlier rebuild attempt); `RFM_human_prompt_reasoning.md`; `RFM_human_prompt.md`
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I36. Use an explicit placeholder for a genuinely empty section, to show it was considered rather than overlooked.
> - I119. Name friction as soon as it's felt, even before it can be explained, rather than smoothing it over.
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, "Why the human names friction"):
> **Why the human names friction before it gets smoothed over**
>
> Friction is a different signal from its two nearest neighbors in this document. It isn't disengagement, the human is still actively evaluating. It isn't the pull toward a confident answer either, nothing has resolved yet to accept or reject. Friction is defined in the glossary; what belongs here is why it earns its own entry: left unnamed, it has nowhere to go. The human moves on, and the session smooths over exactly the place where the reasoning was weakest.
From the human prompt (`RFM_human_prompt.md`, When you feel friction, name it, then push back):
> **When you feel friction, name it, then push back**
>
> *Name the friction before it gets buried*
>
> Friction in a reasoning session is information. When something the AI produces creates a sense that something doesn't fit, even before you can say what, that signal is worth naming out loud. This is not imprecision. Kahneman's work on System 1 reasoning established that pattern recognition fires before conscious articulation: the signal is real before the argument is formed. The discipline here is the same: don't smooth over friction just because you can't yet explain it.
>
> Once you've named it, the right move is curiosity, not deference. "This doesn't feel right, help me understand why you went this direction" is enough. The AI will engage with that honestly. It will ask what specifically feels off, offer to approach the problem differently, or surface an assumption that was quietly doing too much work. What it cannot do is respond to friction that was never voiced, or friction that was voiced and then accepted anyway because pushing back felt like more work than moving forward.
>
> In practice: the smoothing instinct is strong, especially when a session is going well and the friction feels like a small thing. It is rarely a small thing. Name it when you feel it. Then stay curious.


### B61. Trace a rejected framing to the document that taught it

Accepted by the human in the twentieth step 4 session, with the causal link marked as inferred, not observed.

Failures: an error in a reasoning document is reproduced by a later session as its own reasoning, without citing the document; review catches the instance in the session's output, and the document goes on teaching it to the next session. Observed once; that the session took the framing from the document is inferred from the match.
Behavior: when the human rejects a framing the LLM produced, search the documents for it. If a document carries it, the fix starts there (B2).
When: phase one, at a rejected framing.
Routing: Check partly. Severe no. Search yes. Moment triggerable (the rejection).
Origin: any author.
Carriers: always-on (when the human rejects a framing the LLM produced).
Related: B2 (a change starts in the reasoning document; this finds which one). B28 (derive first, read afterwards; it does not help here, because the error arrived without the passage being read in the session). B16 (the old set's Regrounding, quoted there from the handover session file, starts from a caught failure and traces back to the reasoning: a second source for the behavior, not a second observation).
Note (unresolved): whether this is the incubating file's entry E running the other way, as entry N says.
Source: `RFM_incubating.md`, entry N.
Material:
From the incubating file (`RFM_incubating.md`, entry N, a document teaching a later session its error):
> ## N. A reasoning document can teach a later session the error it contains, which the session then produces as its own reasoning
>
> This session proposed that instructions be delivered coarsely by default and finely only where the partner cannot be relied on to notice. The human rejected the framing: it makes execution a tolerated concession and collaboration the real work, when both parties execute constantly. Reading afterwards found `RFM_top_level_reasoning.md` asserting that pressure mode is "not a degraded version of the methodology" and then defining it as what is invoked when the full discipline becomes "locally unacceptable". The document claims parity and encodes concession. The model produced the same error earlier in the session without having read that passage in this session.
>
> The candidate is a direction of contamination the derivative chain does not describe. The chain assumes a reasoning document is a source a session derives from well or badly. Here the document is the source of a specific wrong belief, and the session reproduces it with no sense of having read it anywhere. An error in a reasoning document is not only wrong on the page. It is instruction for whoever reads it next.
>
> A distinguishing test, if this is looked at again: does the session reproducing the error cite the document, or produce it as its own reasoning? Citation is ordinary derivation and normal review catches it. Uncited reproduction is this candidate, and nothing currently looks for it.
>
> **Why not captured yet:** one session. The second instance, that an earlier session took the framing from the document, is inferred from the match rather than observed. Entry E covers derivative-chain failure on translation to a new environment and may be the same phenomenon running the other way; that relationship is unexamined.
>
> **Possible home when ready:** Hard Lessons in `RFM_top_level_reasoning.md`, or the curation module if it becomes an argument about what an uncorrected error costs over time.
>
> **Signal count: 1** *(this session, RFM-on-RFM toolkit work)*

---

## Curation and return

### B9. Curate: cut with the same standing as adding

Failures: documents only grow and become what they were meant to replace; resolved open questions and metabolized hard lessons stay; content that graduated stays in two places; an entry ready to graduate or expire is left in place; text that does not earn its place, language written for the session, and repetition of reasoning stated elsewhere stay in the document (curation failures); a graduating entry carries only its conclusion to its destination, and its reasoning, evidence and break conditions are lost.
Behavior: when content graduates it moves and is deleted from where it was; reduction is proposed as readily as addition. A graduating entry takes its reasoning, evidence, path and break conditions with it.
When: any edit, and at deliberate returns.
Routing: Check partly (growth and leftovers are visible in diffs). Severe no. Search partly (resolved items still listed). Moment triggerable at graduation; unannounced otherwise.
Origin: any author.
Carriers: curation skill; rename skill (names to the human an entry a ripple leaves with nothing live); language sweep (text that does not earn its place, in a finished document).
From the Failure Taxonomy (`RFM_operational.md`), structural:
> - An entry ready to graduate or expire

From the Failure Taxonomy (`RFM_operational.md`), language:
> - Curation failures: text that does not earn its place, language written for the session that produced it rather than for a future reader, repetition of reasoning stated elsewhere that adds no signal
Source: TLR, "Why the document is kept alive by curation"; `RFM_operational.md`, Failure Taxonomy; behavior inventory (earlier rebuild attempt); `RFM_human_prompt_reasoning.md`; `RFM_human_prompt.md`; `RFM_curation_reasoning.md`, The Problem, Chosen Direction
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I38. When an entry graduates, carry its reasoning, evidence, path, break conditions, to the destination, not only its conclusion.
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, output-quality entry):
> Output quality is a distinct failure mode category the traveling prompt cannot address: the LLM producing text that looks polished but is verbose, journaling (language written for the session that produced it, not for a later reader), or repetitive. It requires a separate entry because the human's corrective move is different: not recalibrating the collaboration but reading the output critically before accepting it.
From the human prompt (`RFM_human_prompt.md`, Check the output):
> **Check the output: not only the posture**
>
> *Check the output: verbose, journaling, repetitive?*
>
> The AI's posture drift (agreeing, waiting, not pushing back) is visible in how it behaves. There is a second, less visible failure mode: what it produces. Output that looks polished can still be verbose, journaling, or repetitive, and all three enter reasoning documents silently if the human doesn't catch them.
>
> Verbose means words that don't earn their place. A paragraph that could be two sentences without losing anything is a paragraph that should be two sentences. Length that isn't justified by content is noise, not thoroughness.
>
> Journaling means language that made sense in the session that produced it but requires that session to be understood: insider references, observations written for the moment rather than for a future reader, shorthand that carries meaning only between the two collaborators present. In a reasoning document, journaling is invisible degradation: the entry reads as complete but isn't legible without context that won't travel.
>
> Repetitive means the same reasoning restated across entries, dressed differently enough to look distinct. It is the hardest of the three to catch because each instance reads well in isolation. The failure only becomes visible when entries are held against each other.
>
> In practice: after the AI produces a substantial piece of text (a section, an entry, a proposed addition), read it once for posture and once for output quality. Ask specifically: is anything here longer than it needs to be? Does any sentence require the session to be understood? Is any reasoning here already said elsewhere? The AI will not reliably catch these failures itself. That scan is the human's job.
From the operational document (`RFM_operational.md`, Graduation and Expiry Procedure):
> **Graduation**: an entry whose reasoning still has a recipient:
> 1. Identify the destination: the section and document where a practitioner needs to encounter this reasoning for it to do its work.
> 2. Draft the resolved reasoning in the destination document and confirm it is complete without the source entry. Complete the destination edit before returning to remove the source entry, one document at a time, in that order.
> 3. Remove the source entry from its original location.
> 4. Bump the version of both the destination document and the source document. Update the document map.
>
> Both steps 2 and 3 are required in the same session. An entry resolved but not removed annotates rather than curates.
>
> **Expiry**: an entry whose reasoning no longer has a recipient:
> 1. Confirm the reasoning would not change how any practitioner thinks or acts anywhere in the current system.
> 2. Confirm the version history holds the record.
> 3. Remove the entry.
> 4. Bump the version of the source document. Update the document map.
>
> The distinction between graduation and expiry is a reasoning act, not a mechanical classification. When the case is genuinely ambiguous, flag it rather than resolve it unilaterally.

From curation (`RFM_curation_reasoning.md`, The Problem):
> Curation is what keeps a reasoning document true after the session that wrote it. Its failures share one property: they are invisible from inside the session performing them. Someone compressing an entry holds the context they are removing, so the loss is not visible to them. Someone retiring an entry infers that its situation cannot recur, and nothing in front of them tests the inference. Someone branching a module edits the child and leaves the parent carrying what the child now owns, and neither document reports an error. The individual failures are recorded. What no document carries is the design that treats them as one problem: what curation must do, why its failures escape the person best placed to catch them, and what stays checkable when the session that would notice is the session that is failing.
From curation (`RFM_curation_reasoning.md`, Chosen Direction, "Why curation requires both addition and reduction", first two paragraphs):
> **Why curation requires both addition and reduction**
>
> The document is kept alive through enforced curation. Not just addition but reduction. What has evolved? What can be removed? What needs replacing? A document that only grows is a document that is already dying. The pressure of constraint is a feature, not a limitation.
>
> A healthy document expands when new signal arrives and contracts when old signal has run its course. Contraction has two legitimate forms: graduation, where an entry's reasoning still has work to do and travels to the appropriate destination; and expiry, where it no longer does and is honestly removed. Both are curation. Neither is loss.
From curation (`RFM_curation_reasoning.md`, Chosen Direction, "Why graduation and expiry are reasoning acts, not mechanical procedures"):
> **Why graduation and expiry are reasoning acts, not mechanical procedures**
>
> Graduation and expiry are reasoning acts, not mechanical procedures. The discipline cannot be reduced to a lookup table ("hard lessons graduate to assumptions" or "open questions graduate to Chosen Direction") because the destination depends on what the resolution is, not on what section the entry came from.
>
> The prior test is the same for both: does this entry's reasoning still have a recipient? Would a practitioner encountering it change how they think or act somewhere in the current system? If yes, the reasoning must travel; that is graduation. If no, the entry expires. Version history holds the record; the active document holds only live reasoning. A document that retains entries the version history already preserves is hoarding, not curating.
>
> For entries that graduate, the destination is determined by what the resolution is. A resolution that settles a belief about the domain becomes an assumption. One that commits the methodology to a direction belongs in Chosen Direction. One that constrains scope belongs in Boundaries. One whose reasoning is operative only within a specific module travels to that module's reasoning document. The routing question is: where does a practitioner need to encounter this reasoning for it to do its work?
>
> The graduation act requires two steps: place the resolved reasoning at its destination, then remove the source entry. Both steps are required. An entry that has been resolved but not removed annotates the document rather than curating it, and annotation blurs the boundary between what is settled and what is not. The procedure for executing graduation is carried in `RFM_operational.md`.
From curation (`RFM_curation_reasoning.md`, Chosen Direction, "Why a graduated entry must carry its reasoning, not just its conclusion", first paragraph):
> When an open question graduates into an assumption, the conclusion alone is not enough. A conclusion-only assumption is indistinguishable from an unexamined default. It states what is believed without explaining why it is believed or under what conditions it would break. The reasoning that produced the assumption, the evidence, the path, the conditions, must travel with it. That is what makes the entry an assumption rather than received wisdom, and what allows a future reader to test it honestly rather than inherit it blindly.
Related (from curation): the Problem names three curation failures, each with its own section: retiring on an untested inference and compressing (B40), branching without shrinking the parent (B41). The recipient test is also in B40 (I37).

### B10. Return to the reasoning when something gives a reason to

Failures: documents are visited only when a change forces it and stop being true; drift from what they describe goes undetected. A return set by a date arrives with nothing in front of the human that needs a document, turns into a formality and is dropped, even by a human inclined to curate.
Behavior: come back to the reasoning when a reason arises: pressure mode ends, or a session works on a document the project has changed around since it was last touched.
Forced actor: human at the end of pressure mode (RFM cannot impose it); the LLM when a session works on a changed document.
When: at the end of pressure mode; at the start of work on a document.
Routing: Check no from inside ([OQ-DRFT]). Severe no. Search partly (what changed since a document was last touched). Moment triggerable.
Origin: any author.
Carriers: none. The return after pressure mode waits on the pressure-mode log, an open question in the top-level reasoning. Reading what changed before working on a document has no carrier yet.
Related: [HL-DRIFT] in TLR, Hard Lessons, names the failure this behavior counters.
Source: TLR, Boundaries ("Designed to impose discipline on a team that won't bring it"); [OQ-DRFT].

### B40. Cut or compress reasoning only on tested grounds

Failures: reasoning is retired on an argument that it should not be needed, inferred and never tested, while its situation can still recur; a later decision built on a clause of the lesson under review treats that clause as settled; compressing or condensing reasoning presents as tidying and loses distinctions a future reader or a fresh LLM cannot reconstruct, and the session that compresses cannot see the loss.
Behavior: retire reasoning only on evidence that its situation cannot recur. Treat compressing reasoning as a structural change, decided as one, not as tidying.
When: proposing to retire, narrow, condense or compress reasoning; during curation; while sorting material.
Routing: Check partly (a diff against the earlier version shows what went, not whether it was needed). Severe no. Search no. Moment triggerable (a cut or compression is proposed).
Origin: any author.
Carriers: curation skill.
Related: B9 is the cutting this brakes. B34 (the grounds for retirement were inferred and never tested).
Material:
> **[HL-RETIRE] Retiring reasoning needs evidence that its situation cannot recur, not an argument that it should not.**
>
> A Hard Lesson recording how to keep an embedded document map safe was proposed for retirement, on the grounds that a map should never sit inside a reasoning document at all. Those grounds were inferred from the reason the map was being extracted, and nothing tested them. The counter-case was immediate: RFM ran an embedded map for five minor versions and that was the right call at that size. The lesson was narrowed rather than retired. The same gap had already spread once before it was caught, because a later design decision had been built on a clause inside the lesson under review and treated that clause as settled.
> **[HL-CPSC] Compressing a reasoning document feels like curation; it is structural change.**
>
> Removing or condensing articulated reasoning can present as tidying up. None of those framings change what is actually happening. When reasoning is compressed, signal is lost that cannot be recovered. The distinctions that felt obvious in the session that produced them are precisely what a future reader or a fresh LLM cannot reconstruct. The danger is that compression is invisible from inside the session that performs it: the compressor holds the missing context and cannot perceive the gap they are creating.
From the rebuild plan (memory):
> First, sort the material by wanted behavior and make sure each piece lands in the right place, in full. Don't shorten or summarize while sorting. When we build or check the carrier for a behavior, decide then what's repeated and can be shortened or cut.
Source: `RFM_curation_reasoning.md`, Hard Lessons; `RFM_rebuild_plan.md`, How we work; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I37. Test whether an entry's reasoning still has a recipient, someone whose thinking or acting would change, before deciding to graduate or expire it.

### B41. Finish a branch: shrink the parent and move its derivatives with it

Failures: branching to a new module leaves the parent restating what the module now owns; moving reasoning changes the source of everything derived from it, and a derivative left in the old source's branch passes every sweep, because the defect sits only in the relationship between two files that each pass alone; the parent still carries reasoning a child module owns.
Behavior: when reasoning moves into a new module, return to the parent and remove what the module now carries. At the move, look below the moved reasoning in the tree: what derives from it moves into the module's branch with it.
When: at the move, after a branch.
Routing: Check partly (parent and module restating the same content is visible; a stale derivation edge is not visible to checks that read one file or one pair). Severe no. Search partly (the documents below the moved reasoning in the tree). Moment triggerable (the move).
Origin: any author.
Carriers: curation skill.
Related: B23 decides when to branch. B17 repairs references after a move. B21 (the parent's restatement is a second copy). B33 (the move is a ruling with more than one obligation).
Material:
> **[HL-TLOR] Once a module exists, top-level ownership must be actively reduced.**
>
> Branching to a new module does not automatically contract the top level. Without deliberate reduction, both layers accumulate entries about the same content; the top level drifts toward restating what the module now owns. The discipline after branching is not just creating the new module; it is returning to the top level and removing whatever the module now carries. This is a distinct step, not an automatic consequence of branching. The branching signal itself is carried as an assumption in `RFM_top_level_reasoning.md`; this lesson names what must happen after that signal is acted on.
> **[HL-REPAR] Branching re-parents every derivative of the moved reasoning, and no check reports it.**
>
> Moving reasoning into a new module changes which document is the source for everything derived from it. `RFM_operational.md` carried a graduation and expiry procedure derived from a Chosen Direction entry at the top level. The entry moved into the curation module and the procedure stayed. The arrangement was then ruled acceptable, and it was ruled, which is the point: nothing surfaced it for ruling. The structural sweep asks whether content sits at the right level, and the procedure does. The relational sweep compares a reasoning document against its operational derivative and finds them agreeing. The language sweep has nothing to read. The defect exists only in the relationship between two files that each pass alone. What catches it is asking, at the moment of the move, what derives from the reasoning being moved.
From the Failure Taxonomy (`RFM_operational.md`), structural:
> - Reasoning a child module owns still carried by the parent
Source: `RFM_curation_reasoning.md`, Hard Lessons; `RFM_operational.md`, Failure Taxonomy.

### B62. Check reasoning against what is now known outside

Failures: a document rests on outside evidence, the outside moves on, and nothing in the set changes, so no check that reads the set notices; an assumption's break condition is met in published work and the assumption stands; an open question that outside work has answered stays open; a new approach appears and the Landscape does not show it; a carrier makes up for a model behavior that newer models no longer show, and nothing tests whether it is still needed (all reasoned, not observed; raised by the human). Observed at the drafting moment, not on a return: a grounding pass built from the belief, resting on a paper that tested a model three generations old (HL-CFSRCH, in B34); a mechanical claim that stood for several sessions unchecked against its primary source (HL-PRIMCHK, in B34).
Behavior: check whether a belief a document states about the outside is no longer correct. Assumptions come first and are checked by their break conditions. Open Questions are checked by whether the answer they wait for now exists, Landscape rows by whether their shortfall still holds and the gap by whether something now fills it, and Chosen Direction claims by whether their evidence still holds. Search terms come from what would show the belief wrong. A finding comes to the human with the pages behind it, as a question about whether the reasoning still stands; what changes in the document is stated as how things now are, without references. Outside evidence that something the project relies on is no longer needed comes back as a proposed test in the project's own practice, never as a removal. In RFM, that includes a carrier newer models might not need.
When: on the human's request, when returning to a project after a while, or during drafting on sections already written.
Routing: Check no from inside the set (what changed is outside it). Severe no. Search no (judging outside evidence). Moment triggerable (the human asks).
Origin: any author.
Carriers: research check.
Documents state what is decided and how the project sees the world, with no source names and no dates; when new insight breaks something, it is fixed. Research for content not yet written stays in the drafting conversation. The last sentence of Behavior.
Related: B34 (search terms from the break condition; claims about the set stay there). B10 (a document read against how the project has changed; this reads it against outside work). B39 (a carrier is credited, and retired, only on what is seen in sessions). B42 (research while drafting, and the return to earlier sections after a Landscape).
From step 1 of the rebuild (`RFM_rebuild_working.md`, The prosthetic):
> The prompts, skills, sweeps and other carriers are prosthetics built to make it possible. They are not RFM. With LLMs trained as thinking partners, they would not be needed. The aim is a reasonable prosthetic, not a perfect one, with its reasoning and operational documents in place. Those documents are the baseline for tuning it as LLMs and frameworks change.
From the carrier types file (`RFM_carrier_types.md`, How to update this file; the old carrier for an outside scan, written into the toolbox it updated):
> State what's found as fact. No "a study found," no source names, no dates, no research framing. If it isn't solid enough to assert plainly, it isn't ready for this file.
>
> Check both directions before changing a line: what confirms it and what would overturn it. Weight recent material over old; the field moves fast enough that a claim from even a year back may already be wrong.

---

## Document structure

### B17. Ripple renames and retirements

Failures: a term, section or document is renamed or retired and other documents keep the old reference; content graduates or is resolved and other documents still refer to it as live; a term is redefined and its references read as before while meaning something else; a term coined while drafting is used throughout before it is settled, and renaming it afterwards has to ripple; a word the set already uses is defined for the first time, the definition contradicts that use, and the trigger names no first definition; a reserved term is used in its ordinary sense and nothing checks for it; a search built from the full term misses its variant compounds (observed; from the incubating file).
Behavior: on any rename, redefinition, retirement or graduation, find and update every place that refers to it. Settle a new term before drafting content that uses it throughout.
When: at the change.
Routing: Check yes. Severe no. Search yes. Moment triggerable.
Origin: any author.
Carriers: rename skill (with the dangling-ID search; its trigger also names an entry moved); drafting skill (settling a new term before drafting with it). The separate dangling-ID check was folded into the rename skill.
Source: TLR, "Why the document is kept alive by curation" (curation); the search criterion in "Why a filename and a type tag carry different facts"; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I10. Apply the shorthand test whenever a new shorthand term is used, not only during dedicated research; settle a newly-coined or unsettled term before drafting content that uses it throughout, rather than drafting first and renaming after.
From the ripple check skill (`RFM_skill_ripple_check_reasoning.md`, The Problem):
> A structural change in an RFM document, such as a renamed term, a retired section, or graduated content, propagates inconsistently. A change made in one document leaves the old reference standing in others. Each document looks correct in isolation. The inconsistency is invisible until a session encounters the conflict and must reconstruct what changed and when.
>
> The failure is not that practitioners miss ripple effects intentionally. It is that the scope of a structural change is not visible at the moment it is made. Without a systematic check, the practitioner works from a local view of the change and closes it without knowing what references remain active elsewhere.
>
> This is compounded by graduation: when an Open Question resolves, a Hard Lesson metabolizes into an assumption, or a deferred item closes, the resolved content may still appear in other documents as if it were live. Graduation creates silent references that look authoritative but are no longer current.
From the ripple check skill (`RFM_skill_ripple_check_operational.md`, Trigger conditions; the same list is the installed skill's description):
> - A term is renamed, retired, or redefined
> - A section or document is retired
> - Content graduates out of any section (Open Question resolved, Hard Lesson metabolized, deferred item closed)
> - An edit changes what one document says about another
From the ripple check skill (installed `rfm-ripple-check/SKILL.md`, The procedure, steps 1 to 3; the em dashes in the step headings are rendered as colons):
> **Step 1: Grep.**
> Search all RFM project files for the changed element's name and its core subject terms. Show the grep output in the conversation. Do not proceed to step 2 without showing it. Scope: every file in the document map, plus every file named in the session handover. Do not silently narrow the scope.
>
> **Step 2: Read every hit.**
> Read every file that carries a reference. Do not resolve from the grep snippet alone: open the file and read the surrounding context.
>
> **Step 3: Resolve each reference.**
> For each reference found, determine whether it is active or closed:
>
> - **Active reference in an operational document:** update the terminology. Verify that substance is unchanged, not just the label.
> - **Active reference in a reasoning document:** determine whether the entry needs updating or has been superseded. If superseded, treat as a graduation candidate.
> - **Closed reference anywhere:** treat as a graduation candidate. Flag to the user; do not remove unilaterally.
Note (from the ripple check skill, against step 3): the old trigger list reaches two changes B17's carrier does not name. A redefined term keeps its word, so a dangling-ID check passes and a word search finds every reference, but only reading each one shows it now means something else (steps 2 and 3). An edit that changes what one document says about another is the moment for B21's failure of two documents disagreeing about the same subject. Step 1's search on subject terms, not only the name, is the counter to B34's pointer lesson (a search finds only what it is told to look for). Step 3 routed B17 to a skill triggered by a rename. Which of these the carrier takes is settled at build.
Decided at build: the rename skill takes the redefinition (it reads every hit in its passage) and the search on subject terms, together with the head word alone (entry Q) and the neighbouring vocabulary (entry S). The edit that changes what one document says about another stays with B21's carriers. The rename skill also names to the human an entry a ripple leaves with nothing live (a slice of B9). The reasons are in the rename skill reasoning document.
From the incubating file (`RFM_incubating.md`, entry Q, a rename's search built from the full term):
> ## Q. A rename's grep pattern built from the full term cannot see the collision's variant forms.
>
> Renaming execution mode to pressure mode, the ripple check searched "execution mode" and the mode phrases. Two live hits survived in the form "execution pressure", found only when a post-write verification widened the pattern. `rfm-ripple-check` step 1 currently says to search "the changed element's name and its core subject terms". Candidate corrective: search the head word alone, so variant compounds surface.
From the incubating file (`RFM_incubating.md`, entry R, a reserved term in ordinary use):
> ## R. Reserving a term in the glossary does not stop its ordinary-English use in the same document set, and nothing checks for that.
>
> "The pair" is reserved for a reasoning document and its operational counterpart. It was used this session for the human and the LLM, and stood in `RFM_human_prompt_reasoning.md` for two prompts until a grep found it. Three senses, one fenced. Fourth sense, a later session: used in conversation for the two terms delivery occasion and binding condition, while proposing where to define them. The reserved sense now sits against three ordinary ones, and the one document instance was the only one any check reached.
From the incubating file (`RFM_incubating.md`, entry S, sweeping the neighbouring vocabulary after a rename):
> ## S. After a rename, sweeping the neighbouring vocabulary catches what sweeping the renamed term cannot.
>
> Run twice by the human in one session, against different targets. Checking execution against derivation caught a false claim in a draft, that producing an artifact is execution, when the glossary assigns that to derivation. Checking "pair" caught a live document error. Candidate extension to `rfm-ripple-check` rather than a new mechanism. Evidence is one session, two instances, no prior use found in the documents.
From the incubating file (`RFM_incubating.md`, entry U, a new definition contradicting ordinary use):
> ## U. A new glossary definition can contradict the ordinary use of the same word across the document set, and the drafting check does not ask about that.
>
> Pairs with R, from the other direction. R is a reserved sense broken by ordinary use. This is a first definition breaking ordinary use. "Posture" was defined for the argument that needed it, scoped to a single act, and the ripple check then found roughly forty uses across ten documents meaning a stance held at session scale: the traveling prompt calibrates it, `[HL-SSDM]` says it is not established at session start, two prompts require incompatible ones. The definition was widened rather than the documents changed. Second item, same session: the glossary clause added to `rfm-drafting`'s Language pre-check asks whether a term carries a definition or a pointer, not whether a new definition agrees with existing use, so the pre-check passed the wrong entry. Both belong with whatever resolves R.
From the incubating file (`RFM_incubating.md`, entry V, no trigger on a first definition):
> ## V. `rfm-ripple-check` does not trigger on a term being defined for the first time.
>
> Its trigger names a term renamed, retired, or redefined. Defining a word the document set already used undefined is none of the three. It ran this session because the session judged it should, and it caught the error in U. One occurrence.
From the incubating file (`RFM_incubating.md`, entry Z, naming a term from a word already used unnamed):
> ## Z. Naming a term from a word the target document already uses unnamed, rather than coining one.
>
> Working mechanism, one clean instance. The module used "binding" eight times for the state an instruction is in when it governs behaviour, and nowhere else in the document set, without ever declaring it. The new term was taken from that rather than invented, so the definition ratified existing use instead of competing with it, which is the failure U records. History shows the concept had precedent, commit `d44f1da` re-derived the module's carrier taxonomy around bindingness; it does not show the mechanism had any. One instance, tracked rather than named a mechanism.
Note (from the incubating file): R and U were placed here, not in B32, because they are found by a search across the set at the moment a term is defined; B32's carrier is the derivation test. Related: B32. Z is a working mechanism, one instance.

### B21. One fact, one place

Failures: a fact is recorded in two places and one copy goes stale; a file records its own version twice; a document restates its own position in the hierarchy and the copies drift; a list that names the members of a set goes stale when the set grows, while a rule against counts stays satisfied on its face; a clause about what a thing does not yet do or will require, written when the work that falsifies it is already planned, makes the document a second record of the plan and goes stale when the plan lands; a rule restated in several carriers has no owner, the copies age apart until one contradicts the rule, and every fix costs one edit per copy; a deployed copy of an artifact drifts from its source outside the reach of every check the project runs on itself; two reasoning documents assert opposite claims about the same practice and nothing reads them against each other; a closing epigraph that summarizes the body is not re-derived when the body changes; reasoning is duplicated across sections of one document; reasoning stated elsewhere is repeated and adds no signal (curation failures bullet, material in B9); a claim is conditioned on something already planned, which that plan will make false; a note or placeholder describes work that a scheduled step will perform; a commit that is not pushed leaves the published copy one session behind, which stays invisible until someone clones it; a module restates its parent's reasoning or redefines the parent's terms instead of pointing to them (observed twice; from the incubating file).
Behavior: keep each fact in one place. Do not write a statement whose correctness depends on another place staying the same, whether through a count, an ID or a list of members. A condition that planned work will satisfy goes in the plan, not in the document the plan will change. A rule has one owning carrier; every other mention points to it or is deleted. Where a second copy cannot be avoided, as with a deployed copy, compare it against its source.
When: any write.
Routing: Check yes. Severe no. Search partly (duplicated facts, enumerations of a set). Moment unannounced.
Origin: any author.
Carriers: drafting skill; cross-document sweep (the two places in different documents, and lifespan); structural sweep (reasoning duplicated across the sections of one document, including an epigraph restating its body); close skill (version bumps and map updates). Deployed copy: no carrier. The check and a close line were dropped.
Related: B17 repairs references after a change; B21 avoids writing references that need repair. HL-DMAP (in B22) carries the point that a README with versions becomes a second map that drifts against the first.
Related (taxonomy): the boundary paragraph in B25 separates this failure from a conditional whose trigger is uncertain, which no plan holds and which is not a lifespan failure.
Material:
> **[HL-SELFREF] A map does not list the file it lives in.**
>
> When `RFM_top_level_reasoning.md` was included as a map row, sessions updated the document header version without updating the corresponding map entry. The mismatch was invisible during the session and surfaced only at the next version check, where it had to be traced and corrected rather than having never existed. Excluding the containing document from the map it governs removes that maintenance surface. The same reasoning holds once a map moves into its own file. A file cannot record its own version twice without one copy going stale, and the copy in a standalone map would be its highest-churn row, bumped every session that touches any document in the set.
> **[HL-MAPCOPY] A document does not restate its own position in the hierarchy.**
>
> Six operational documents carried a list of the documents to load before deriving from them. Every entry but one was the document's own branch read upward, which the map already states. The copies drifted, and three of them omitted the top-level document. A sweep entry condition existed to catch exactly that omission, which made the copies look load-bearing and kept attention on completing them. Two sessions repaired the lists before anyone asked whether the lists should exist. A document names a source in its own text only where the edge leaves its branch.
> **[HL-ENUM] A list that names its members is a count-dependent reference with no number in it.**
>
> `RFM_operational.md` bars statements whose correctness depends on a count remaining stable, and every form it named at the time carried a numeral or an ID. A sentence introducing the execution artifacts as "the traveling prompt, sweep prompts, and human prompt" carried neither, and was wrong by two: the derivation prompt and the guided drafting prompt had been added since it was written. The list had gone stale in place while the rule that covers it stayed satisfied on its face. The test that catches this is whether adding a member to the set would falsify the sentence, which is the same test the count forms fail, applied to enumeration rather than to a number.
> **[HL-KNEXP] Content written when its expiry is already known schedules maintenance work rather than avoiding it.**
>
> A claim can be accurate when written and false by the next session, because the work that falsifies it was already planned when it was written. The common shape is a forward-looking clause: a sentence stating what a thing does not yet do, or what it will require, where the requirement is already on the plan. It reads as careful. It passes review as true, correctly placed and clearly written. Review lets it through for those reasons, not despite them.
>
> The worked example is a drafting session where the LLM produced clauses of the form "this will only work once X is in place." They were accepted as sensible caution. Work on X began a few hours later. A following session reported those paragraphs as stale and needing maintenance, which pulled ripple checks into documents that only referenced them, and one compression made during that cleanup removed content that had to be reconstructed from an earlier version. Nothing in the chain was wrong on its own. The first sentence was true when written.
>
> A condition that planned work will satisfy belongs in the plan, not in the document the plan will change. Writing it in both places makes the document a second record of the plan, and the ripple work is the price of keeping the two agreeing until the plan lands.
> **[HL-INAD] An instruction restated in a second artifact dilutes the rule instead of reinforcing it.**
>
> Em dashes were barred in nine places across the document set: the traveling prompt, the top-level operational document, four skill operational documents, and the skill body. Every mention was written by someone trying to make the rule hold, and the character kept appearing anyway. One of the nine instructed the writer to replace an em dash with parentheses, which the skill governing that rule explicitly forbids. Nobody wrote a contradiction. It appeared because no artifact owned the rule, so each copy aged on its own and nothing reconciled them. The count also priced every later fix at nine edits instead of one. The corrective is ownership: one artifact carries the rule, and every other mention is a reference or is deleted.
> **[HL-DEPCOPY] A deployed copy of an artifact drifts where no check is looking.**
>
> An execution artifact was copied into the platform that loads it at the start of every session. The copy was taken before the document map moved into its own file, and it still described the map as sitting at the top of the top-level reasoning document. A session running on that copy would look for the map where it no longer was. Every check in the project compares files inside the project, so nothing compared the deployed copy against its source, and the divergence was invisible from inside the repository. Deploying an artifact creates a second location for it, and that location is outside the reach of any check the project runs on itself.
> **[HL-CONTRA] Two reasoning documents can assert opposite claims about the same practice, and nothing but noticing the contradiction catches it.**
>
> `RFM_operational.md`'s artifact convention states that an artifact meant to run again is curated over time, not regenerated wholesale. `RFM_skill_drafting_reasoning.md`'s Boundaries entry said the opposite about the same three artifacts, the traveling prompt, sweep prompts, and human prompt: that they are regenerated from their sources. Git history settled which claim was true. Every commit touching those three files, across the project's full history, changed a handful of lines and never the whole file, which matches curation, not regeneration. The wrong claim was not a drift from something once true; nothing in the commit history supports it ever having been true. No sweep compares one reasoning document's claim against another document's claim about the same subject. The structural sweep checks a document's own placement, and the language sweep checks a document's own prose; neither reads two documents against each other. The disagreement surfaced only because an earlier session's ripple check happened to notice it while working on unrelated vocabulary, and it then sat unresolved for two sessions before being investigated.
> **[HL-EPIDRIFT] A document's closing epigraph is not re-derived when its body changes, so an edit to the body can leave the epigraph contradicting it.**
>
> Correcting this document's Problem section and `[AS-DECAY]` left the closing epigraph, two lines written to summarize the old framing, restating the exact claims just corrected, "an instruction reaches only the moments its carrier reaches" and "silence is invisible from inside the instruction", verbatim. Nothing flagged the mismatch; it was caught only because the full file was reread after the edit rather than trusting the diff. An epigraph is drafted once, at a different time than any later body edit, and nothing reconciles the two automatically.
From the Failure Taxonomy (`RFM_operational.md`), structural:
> - Reasoning duplicated across sections of one document

From the Failure Taxonomy (`RFM_operational.md`), lifespan:
> - A claim conditioned on something already planned, which that plan will make false
> - A note or placeholder describing work that a scheduled step will perform
Source: TLR, Hard Lessons; `RFM_curation_reasoning.md`, Hard Lessons; `RFM_instruction_design_reasoning.md`, Hard Lessons; `RFM_operational.md`, Failure Taxonomy.
Note (from the operational document, settle at build): the version-reference check below is a search for version strings in a document body. Step 3 dropped a pattern check for count words, not this one. The duplicate-definition check (quoted in B57) says a duplicate comes "most often from copying an existing entry"; no incident is recorded behind that, and step 3 dropped the check for having no failure in the material.
Settled: the version-reference check is dropped. A search of the documents in the rebuild folder found no version number outside header lines, and the drafting skill asks of every sentence "Does a sentence restate a fact kept elsewhere?", which a version number copied from another document's header does.
From the operational document (`RFM_operational.md`, Count-Dependent References):
> Reasoning documents must not contain statements whose correctness depends on a count remaining stable. The excluded forms:
>
> - Version numbers in cross-document references: the document name is the stable identifier; the document map carries the version snapshot
> - Numerical counts of entries (assumptions, options, hard lessons): adding or removing one entry silently invalidates the count
> - Cross-document ID references: they imply a shared registry that does not exist and would signal the entry is in the wrong place
> - IDs scoped beyond a single document: IDs are per-document only
> - Lists that name their members: adding a member to the set falsifies the sentence, and no numeral appears in it to mark the dependency
>
> **The version-reference check.** Of the forms above, version numbers in cross-document references reduce to a search: grep the body of each document, excluding its own header line, for a version-shaped string. A match is a finding. Cross-document ID references reduce to a search too; that check is not written here. Numerical counts of entries and lists that name their members are judgments about prose; no search settles them, and they stay guidance rather than enforced convention.
From the sweeps (`RFM_sweep_reasoning.md`, Chosen Direction, "Why duplicated reasoning is a primary structural target" and "Why the structural sweep owns the lifespan family"):
> **Why duplicated reasoning is a primary structural target**
>
> The same argument restated in different styles across Options Considered and Chosen Direction reads as thoroughness from inside the session that wrote it. Only a pass reading the whole document at once, with nothing else to attend to, can see that two entries carry one argument. This is why the structural sweep's protocol treats duplicated reasoning, not just duplicated content, as a primary target.
>
> **Why the structural sweep owns the lifespan family**
>
> The corrective arm splits by job. Judging whether planned work will falsify a claim requires knowing what the project has committed to elsewhere, which is the same knowledge the structural sweep already uses to judge whether an entry is ready to graduate. Close reading of the sentence does not answer it, so the language sweep would have to acquire that knowledge to run the check, and it would then be doing architectural judgment under a language label.
From the sweeps (`RFM_sweep_operational.md`, Structural catalog, cross-section question):
> **Cross-section question**
>
> *Lifespan:* Does any entry state a condition that work already planned will satisfy? Ask it in every section alongside that section's primary question. Lifespan failures are not specific to a section, so no per-section wording is derived for them.
From the handover session file (`RFM_handover_session.md`, 2026-09-14, Carry-forward):
> **The register artifact.** One canonical register mapping every behaviour to a type and a carrier type, versioned, in the document map, capped, travelling with RFM. Understood: it is data rather than procedure, so not an operational document; its carrier column holds a bucket rather than a filename so one register works across environments; and curation is its real job, since it is the only artifact where every behaviour is counted once and a cap can force a removal. It is now also the only legitimate home for the three cap numbers, which were agreed this session and exist nowhere but this file. Tried: the column schema exists as the Verdict column in the inventory scratch. Open: the artifact type is still not named or designed, and where a practitioner's own domain findings go, since they are not register entries. Stopped because the register should be designed against the sorted set rather than the current one. Heavy. v1.0.
Note (from the handover session file): the register is the old design for the record after the rebuild noted above. Settled in step 5 and at build.
From session-closeout (`session-closeout/SKILL.md`, Close sequence, step 7):
> If the project repository has a remote, push after committing. Committing without pushing leaves the published copy one session behind, which stays invisible until someone clones it. The handover repository has no remote and is never pushed.
From the incubating file (`RFM_incubating.md`, entry Y, the reverse of a parent carrying a child's reasoning):
> ## Y. The Failure Taxonomy names reasoning a child module owns still carried by the parent, and nothing for the reverse.
>
> A module restating its parent's reasoning rather than pointing at it is the mirror image and has no type. The instance: a module's Chosen Direction entry restating the parent's posture reasoning, resolved by attribution, on judgment rather than on a check. Adding a class is not complete until both arms' derived questions reach it, per that section's own rule, so this is work rather than an edit.
>
> Second instance: a Problem section draft for `RFM_skill_design_reasoning.md` redefined the parent's two terms inline. The drafting skill's three derived questions passed it. Reading the taxonomy's type list directly found it, along with two other hits the derived questions missed. The type list is the only thing that caught it, and the type it should have matched is the one that does not exist.
Note (from the incubating file): related B41 (the parent carrying a child's reasoning) and B25 (only reading the type list caught it; the derived questions did not).

### B22. Give a first-time reader a way in

Failures: a reader or LLM new to the project cannot tell from the documents which one to read first.
Behavior: the document set tells a first-time reader where to start, once the documents themselves no longer do.
When: as the set grows.
Routing: Check yes (a fresh reader, see B27). Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: fresh-context subagent test.
Material:
> **[HL-DMAP] A document set needs a map once a reader cannot tell from the documents themselves which one to read first.**
>
> A reader or LLM encountering a project for the first time cannot orient from the top-level reasoning document alone. Navigation is not reasoning, but it is a prerequisite for reasoning about the right thing. The map and the README serve different readers and must not be merged. The map carries real version numbers, so a practitioner can detect drift between a document and what the project believes that document to be. The README carries orientation without versions, so a first-time reader is not asked to track state. A README that grows version numbers becomes a second map that drifts against the first. A map that drops them stops being able to detect drift at all.
Source: TLR, Hard Lessons; `RFM_operational.md`, Document Map Maintenance.
Note (from the operational document): step 3 dropped a check that the map lists every file, for having no failure in the material. The map check below also compares each row's version against the file's header, which is the drift HL-DMAP says the map exists to detect. Settled: that comparison is B21's (one copy of each version), not a way in for a first-time reader. The close skill proposes map rows for the documents changed in a session; drift outside a close has no check.
From the operational document (`RFM_operational.md`, Document Map Maintenance):
> The document map is named `[project]_map.md`. It must be updated in the same session as any document version bump. Version numbers in the map must be real, no wildcards.
>
> **The map check.** Run it in any session that changes a document's version, adds a document, or removes one.
>
> Compare every map row's version against the header of the file the row names. Compare the file set against the map in both directions: a header-bearing file with no row is a finding, and a row naming no file is a finding. The map does not list itself, so its own file is never a finding.
>
> A version header does not decide whether a file is a document. Some documents cannot carry one, and the header convention names the case. The map's Type column decides: a row carrying a type is a document, and a row carrying none is navigation. A document carrying no version has `unversioned` in its version cell.
>
> Only header-bearing files are discoverable. A document with no header cannot be found by searching for one, so its row is added by hand when the document is created and its absence produces no finding anywhere. This is the limit the check cannot cross, and it is why the map rather than the check is the record of what exists.
>
> While reading each header, check its form against the header convention. A header that does not match is a finding. In the same pass, check the type field against the nine-value closed list; a value outside the list is a finding independent of whether the header's form is otherwise correct.
From instruction design (`RFM_instruction_design_reasoning.md`, Chosen Direction, "Why map integrity is checked mechanically rather than maintained by instruction"):
> **Why map integrity is checked mechanically rather than maintained by instruction**
>
> The map restates two facts held elsewhere: a document's version, which is in its own header, and a document's existence, which is in the file set. A restated fact drifts when one side moves, and nothing errors when it does. `RFM_operational.md` already requires the map to be updated in the same session as a version bump. That requirement is an instruction with nothing behind it, which is the configuration `[HL-UNCHK]` says will not hold.
>
> The comparison reduces to a search. Each map row names a file whose header carries the version, and each file in the project either appears in the map or does not. It earns a check under `[AS-SRCH]`.
Dropped: the first session guidance's line telling a newcomer to read the README and the top-level reasoning document first. The README is what this behavior produces, not its carrier, and its "Where to start" list is the way in; a line sending the reader there adds nothing. The third paragraph of the instruction design quote (a check placed in one project's tooling protects only that project) belongs to instruction design reasoning.

### B23. Branch on structure, not size

Failures: a form is kept past the point where it can carry the structure the content needs; the missing structure is reconstructed by hand in several places and the copies drift; size is taken as the signal; a section strains toward a new module; one level down, an entry carrying too much bundled content is relabeled instead of split.
Behavior: when content needs structure its current form cannot carry, branch it into its own place. Size alone is not the signal.
When: when a section, list or document strains.
Routing: Check partly. Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: drafting skill; structural sweep.
Material:
> **[HL-MAPSCALE] A map moves into its own file when it needs structure that a list inside another document cannot carry.**
>
> A large-scale deployment of RFM extracted its document map into a standalone file with its own version. Two additions followed: a category for maintained inputs that modules consume but do not own, and a set of task-specific read pathways naming which documents to read for which kind of work. The map's growth was the presenting symptom, but what the additions have in common is structure the embedded form could not hold. In RFM the same trigger fired at a much smaller size and for a different structure. The flat table records each document's level but not its parent, so sessions reconstructed the hierarchy by hand inside individual documents and the copies drifted. Row count was not the signal in either case. An embedded map is a tolerated exception to the rule that a reasoning document carries no procedure, and the exception holds only while the map stays a plain list.
From the Failure Taxonomy (`RFM_operational.md`), structural:
> - A section straining toward a new module
Source: TLR, Hard Lessons; Step 1 statement ("A section that strains under its own weight is the signal to branch"); `RFM_operational.md`, Failure Taxonomy.
From the handover rules (`RFM_handover_rules.md`, Hold at the relevant moment, [R-STRAIN]):
> - **[R-STRAIN]** Document strain is a signal to branch into a new module, not to write more carefully. Strain looks like: too many options, too much detail, too many edge cases in one document. Name the strain before writing more. The same logic applies one level down: an entry carrying too much bundled content is a signal to split the entry, not relabel it.

### B47. Place content at the level and in the section it concerns

Failures: content sits at the wrong level of the hierarchy; content sits in the wrong section of a document. A well-written sentence in the wrong section is still this failure. A finding filed under an existing item of a different scope is answered at that item's scope, and the finding at its own scope disappears (reasoned, not observed; from the posture gate raw notes).
Behavior: when writing, place content at the level of the hierarchy and in the section whose job it serves.
When: any write, both phases.
Routing: Check yes (a structural read afterwards). Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: drafting skill; structural sweep.
Related: B1 (content reaches the page at all; this is where it lands). B41 (content left at the parent after a branch). B38 (HL-NSWP: a procedure leaked into an entry that carries only why). B25 carries the boundary paragraph that defines structural failures.
Material:
From the Failure Taxonomy (`RFM_operational.md`), structural:
> - Content at the wrong level of the hierarchy
> - Content in the wrong section of a document
Source: `RFM_operational.md`, Failure Taxonomy, Formatting Conventions for Reasoning Documents; `RFM_human_prompt_reasoning.md`
Note (from the operational document): the section formats below are how each section does its job. Only the heading check reduces to a search (B25, HL-UNCHK). The break condition in an assumption is the designated exit TLR "Why a reasoning document states a belief instead of defending it" describes; see B24 and B49.
From the operational document (`RFM_operational.md`, Formatting Conventions for Reasoning Documents):
> These conventions apply to all RFM reasoning documents. They are not methodology; they are the formatting that practice has shown best serves the reasoning each section requires. Newcomers are guided to follow them in their first session. RFM documents follow them as the current best formulation.
>
> **The Problem**
> Plain prose. Bold subheading only when a structurally distinct second argument would otherwise read as continuation of the first.
>
> **The Assumptions**
> `**[AS-XXXX] -**` bold claim, body follows in the same paragraph. The body states the break condition, the condition under which the claim would no longer hold. Hyphen after the ID, not em dash. Grouping sentence permitted when assumptions genuinely divide into distinct registers.
>
> **The Landscape**
> One intro sentence naming the specific question this landscape must answer. Table with three columns: Approach | What it does | Why it's insufficient. Closing paragraph opened with **The gap:** in bold.
>
> **The Options Considered**
> `**1. X vs. Y**` as bold title, prose body including the rejection reasoning. Each option self-contained.
>
> **The Chosen Direction and Why**
> `**Why X**` or `**Why X over Y**` as bold subheading per entry, prose body. No IDs. No numbering.
>
> **The Boundaries**
> `**Not X.**` as bold lead phrase, prose body in same paragraph. No IDs. No numbering.
>
> **The Open Questions**
> `**[OQ-XXXX] Title of the question.**` as bold line, prose body as separate paragraph below.
>
> **The Hard Lessons**
> `**[HL-XXXX] Title.**` as bold line. Prose body opens with one paragraph stating the mechanism. A second or third paragraph is added only when it carries a claim the first doesn't: a worked example, a mirrored failure direction, a named distinction from a neighboring entry, or its resolution. Not elaboration or restatement of the same point. Category subheadings permitted when lesson count warrants grouping.
From the sweeps (`RFM_sweep_operational.md`, Structural catalog, per-section primary questions):
> *The Problem:* Has this section absorbed scope that belongs at a lower level, or has it drifted from the original statement without a flag?
>
> *The Assumptions:* Does each entry state a testable belief, or has implementation detail leaked in? Are any assumptions now contradicted by the Chosen Direction?
>
> *The Landscape:* Does each row distinguish its approach clearly from its neighbors? Does the closing paragraph name the gap without beginning to choose? Has early option selection absorbed work that belongs in Options Considered?
>
> *The Options Considered:* Is each option genuinely distinct, or is one a restatement of another dressed differently? Does each entry show evidence of having been actively considered, rather than invented to round out the section? Does the rejection name a specific failure mode, or only a preference? Does any entry restate the Chosen Direction's committed path instead of a discarded alternative? Is any option missing that was pursued as a competing way to resolve the Problem and dropped without record? A supporting commitment inside the Chosen Direction is not evidence of one.
>
> *The Chosen Direction and Why:* Does each entry carry only why, or has how leaked in? Is any entry restating an option rather than justifying a direction? Does any entry restate content that a child module now owns, a sign the parent failed to contract after branching?
>
> *The Boundaries:* Has any boundary drifted into a constraint on decision-making (which belongs in Assumptions)? Is anything described as "not this" that is actually just undesigned?
>
> *The Open Questions:* Is any question ready to graduate, partially or fully resolved by the Chosen Direction or by an assumption? Is any question actually a deferred decision rather than a genuine unknown? Does the question have a plausible condition under which it could be resolved, or is it open-ended with no path to an answer? Would resolving it materially change the reasoning or the system, or is it decorative?
>
> *The Hard Lessons:* Has any lesson been metabolized into an assumption or Chosen Direction and should now graduate? Is any lesson a restatement of another in different language?
Note (from the sweeps): these questions carry each section's job beyond its format. Several name failures step 2 reached only through section formats: an option invented to round out the section, a rejection naming only a preference, an assumption contradicted by the Chosen Direction (B42), a deferred decision filed as an open question, an undesigned area written as a boundary (B31). The structural sweep prompt adds one question under The Assumptions (see B2).
From skill design (`RFM_skill_design_operational.md`, Delivery):
> The skill source is `[skill-name]/SKILL.md`. Delivery is environment-specific: some environments package the source into an installable file the user downloads, others present the source for review and save it directly. Use the mechanism the current environment provides. The requirement is that the user ends up with the skill installed, not that a file is produced.
From the drafting skill (`rfm-drafting/SKILL.md`, Layer 1, "Which document level?"; the tests for which level content belongs to):
> **Which document level?**
> - Reasoning: why. Argument, belief, failure mode, commitment.
> - Operational: what exactly. Procedure, format, named steps, constants.
> - Glossary: a term that emerged in a session and cannot be understood without the conversation behind it.
>
> If the content contains a named procedure with steps, it belongs in operational, not reasoning. If it contains a commitment and its justification, it belongs in reasoning, not operational. If it is a term that requires session context to make sense, it belongs in the glossary before it enters any other document.
From the drafting skill (`rfm-drafting/SKILL.md`, Layer 1, "Which section of a reasoning document?"):
> **Which section of a reasoning document?**
> Each section has one job. Placing content in the wrong section is a structural failure. The structural sweep will catch it; drafting correctly avoids it.
>
> - *The Problem*: the gap that justifies the work. No solution language.
> - *The Assumptions*: a testable belief and the conditions under which it breaks. Not implementation detail. Not conclusions without reasoning.
> - *The Landscape*: prior approaches and why each is insufficient. Table format. Closes with **The gap:** in bold. No option selection here.
> - *The Options Considered*: alternatives genuinely entertained and why rejected. The rejection names the failure mode.
> - *The Chosen Direction*: why this direction over the others. No how. No restatement of options.
> - *The Boundaries*: what this explicitly is not. Not hedges. Not undesigned space.
> - *The Open Questions*: genuinely unresolved. Not weaknesses to downplay. Not deferred decisions dressed as unknowns.
> - *The Hard Lessons*: what failed and why. Same standing as any other section.
From the glossary (`RFM_glossary.md`, What this file is):
> This glossary disambiguates terms used in RFM documents that carry different meanings across reader contexts: words that look shared but aren't. Each entry records why the term means what it means here, not just what it means. Entries are added when a term appears in multiple documents and its meaning is likely to diverge across readers or contexts. Below that threshold, definitions belong inline where the term is first used.
From the posture gate raw notes (`posture_gate_raw_session2.md`, earlier rebuild attempt, session 2, 2026-09-14, "What the documents say, and where they do not win"):
> **The top-level open question on the capture artifact is at the wrong scope for us.** It asks how short the record can be, what artifact it is, how to tell a deviation from noise. Asked at session scale under pressure. Ours is one observation during one act. Filing ours under theirs answers it at their scale and ours disappears.

---

### B56. Correct an append-only record by appending

Failures: a log or history is rewritten in place and the record of what happened is lost.
Behavior: tell append-only records from records that are rewritten in place. Correct an append-only record with a new entry.
When: any edit to a record.
Routing: Check yes (a diff shows edits to earlier entries). Severe no. Search partly. Moment triggerable (the edit).
Origin: any author.
Carriers: none. RFM keeps no log apart from the pressure-mode log, whose form is an open question in the top-level reasoning. Git holds the history of everything else. The append-only check was dropped: a mark in every append-only file is upkeep larger than the failure.
Related: B14 (the pressure-mode log is one). B30 (deferred items).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I104. Distinguish append-only records (logs, deferred items) from records that get rewritten in place; never rewrite the former.
Source: behavior inventory (earlier rebuild attempt).
From the traveling prompt (`RFM_traveling_prompt_reasoning.md`, Chosen Direction, "Why an append-only record is never rewritten in place"):
> **Why an append-only record is never rewritten in place**
>
> A record that is only appended to shows what was decided or found at the time each entry was written. Rewriting an entry in place replaces that with the current understanding, and the record itself no longer shows what was known then. A correction goes in a new entry that refers to the one it corrects, so both the mistake and the fix stay visible.

### B57. Keep documents in the form the searches key on

Failures: a file or entry whose form departs from the form a search keys on (a near-miss category suffix, a header in another form, a type outside the closed list, an ID declared twice or referenced where it is not declared) drops out of that search and nothing errors; a blank section cannot be told apart from one that was overlooked. Observed: HL-UNCHK (a convention with no search behind it drifted to 52 heading violations), HL-RECFACT (a skill bundle with no header line was read as its type having no instances). Reasoned, not observed: a project that writes its own conventions runs the checks against documents they cannot describe (TLR, "Why the methodology's operational document is separate from a project's").
Behavior: keep files, headers, types and IDs in the form the searches key on, and mark an empty section as empty. Each part of the form a check keys on has the search behind it.
When: adding or renaming a file; writing a header or an ID; leaving a section empty.
Routing: Check yes. Severe no. Search yes. Moment triggerable (a file is added, renamed or written).
Origin: any author.
Carriers: drafting skill (the filename pattern and the header line; the empty-section line, through B31); rename skill (the dangling-ID search, from B17).
Decided at build: the form searches were dropped. No check that survives reads them. The form is written where a file is created, in the drafting skill, with the project's own prefix.
Related: B21 (a filename carries no version; the header is the single source for it). B25 (HL-UNCHK). B35 (a type with no instances is still a type). B48 (an ID recoverable on a cold read). B17 (a retitle changes the ID and its references). B47 (the reasoning document section formats).
Material:
From the operational document (`RFM_operational.md`, File Naming Convention):
> Documents follow this naming pattern:
>
> `[project]_[subject]_[category].md`
>
> `project` is the tag for whichever project is applying the RFM approach.
>
> `subject` is what the document is about, in as many words as it takes to distinguish it from its siblings: `sweep`, `skill_drafting`, `traveling_prompt`. It is a free slot. No closed list governs it.
>
> `category` is `reasoning`, `operational`, or omitted. It is omitted on artifacts, which are named for what they are rather than for what they carry: `RFM_traveling_prompt.md`, `RFM_glossary.md`, `RFM_sweep_prompt_structural.md`.
>
> The filename is checkable at its ends and not in its middle. The project prefix and the category suffix are searchable; the subject slot is not, by design.
>
> **The filename check.** Every filename begins with the project prefix. Grep for it; a filename that doesn't match is a finding. Separately, grep every filename for `reason` or `operat`: a hit that isn't exactly `_reasoning.md` or `_operational.md` at the end is a finding, a near-miss suffix. Run it in any session that adds or renames a file.
From the operational document (`RFM_operational.md`, Document Type and Header Convention):
> Every document carries a type. The type is the document's position in the hierarchy, not its subject: the filename already carries the subject, and a type that repeats the subject has one value per file and cannot be checked against anything.
>
> A type is a level crossed with a category.
>
> Levels: `top_level`, `module`, `skill`.
> Categories: `reasoning`, `operational`, `artifact`.
>
> The nine resulting values are the closed list:
>
> `top_level_reasoning`, `top_level_operational`, `top_level_artifact`, `module_reasoning`, `module_operational`, `module_artifact`, `skill_reasoning`, `skill_operational`, `skill_artifact`.
>
> A type with no instances is still a type. The list is produced by the grid, not by enumerating what exists. Which types are occupied is recorded in the document map, not here.
>
> Documents that can carry a header carry it on line 2, in this form:
>
> `` `vX.Y.Z` // `type` // [living] ``
>
> Where an artifact's file format cannot carry that line, the type is recorded in the map's Type column and nowhere else. A skill bundle is the known case: it is a folder, and the second line of its `SKILL.md` is frontmatter owned by the skill loader. An artifact that cannot carry the header still has a type. A skill bundle carries no version for the same reason: the format has no line for one. The map's version cell reads `unversioned`. A coverage-check requirement keeps the packaged file in sync with its source instead.
From the operational document (`RFM_operational.md`, Content-Derived IDs for Assumptions, Hard Lessons and Open Questions):
> Assumptions, Hard Lessons, and Open Questions use content-derived IDs rather than positional numbers. Format: `[AS-XXXX]` for Assumptions, `[HL-XXXX]` for Hard Lessons, `[OQ-XXXX]` for Open Questions, where XXXX is a short abbreviation derived from the entry content.
>
> Rules:
> - Abbreviation must be recoverable on cold read without session context. When a retitle breaks that, the ID is changed, and every reference to the old ID in the same document is updated in the same edit
> - Cross-references use the ID, never the position number
> - IDs are unique within their section type within a single document; they do not form a shared registry across documents
>
> **The duplicate-definition check.** In the same pass, count how many times each declared ID appears as a bold entry line within its own document. A count above one is a finding: the same ID assigned to two different entries, most often from copying an existing entry as the starting point for a new one.
From the operational document (`RFM_operational.md`, Empty Section Placeholder Convention):
> When a section has no entries, use a placeholder rather than leaving it blank. This signals that the section was considered and is genuinely empty, not overlooked.
>
> Standard placeholder: `*No [section name] at this time.*`
>
> Examples: `*No open questions at this time.*` / `*No hard lessons at this time.*`
>
> A blank section is ambiguous. A placeholder is an explicit statement.
Source: TLR, "Why the methodology's operational document is separate from a project's" and "Why a filename and a type tag carry different facts"; TLR, Hard Lessons (HL-UNCHK, HL-RECFACT, as sorted into B25 and B35); `RFM_operational.md`, File Naming Convention, Document Type and Header Convention, Content-Derived IDs, Empty Section Placeholder Convention.

## Writing and drafting

### B24. State, don't defend

Failures: citations, hedges or qualifications are added as reassurance, not because the reader needs them; evidence is defended rather than stated: qualification written to pre-empt a challenger, or a citation added to show a claim was checked.
Behavior: a citation or qualification stays only if removing it costs the reader something needed right there.
When: any write.
Routing: Check yes (the removal test can be run afterwards). Severe no. Search no. Moment unannounced.
Origin: tool pull (a training reflex toward citing as reassurance).
Carriers: drafting skill; language sweep.
Material:
> **[HL-CITEHDG] A citation added because a claim 'should' have one is defensive hedging, not support.**
>
> Four sentences in `RFM_operational.md` cited another document as a claim's backing: a graduation procedure, an em dash rule, a skill-count band, and the `[living]` marker, each pointing at 'the reasoning is in X.' None of the four gave the reader anything they needed to act on the claim. The test that found this: remove the citation, and ask whether the reader loses something needed right there, not whether the claim feels less supported. All four failed to justify their presence once someone thought to run that test. The mechanism is a training reflex toward citing a source as reassurance that a claim was checked, independent of whether the reader needs the source to act on the claim.
>
> A citation that supplies content the sentence depends on, a term or constraint defined elsewhere, passes the same test by failing it: removing it costs the reader something. That is the discriminator. Whether the cited document is real and the claim is true never enters it.
From the Failure Taxonomy (`RFM_operational.md`), language:
> - Evidence defended rather than stated: qualification written to pre-empt a challenger rather than to record what is believed, or a citation added to show a claim was checked rather than because the reader needs the source at that point. Qualification that feeds a break condition or blocks a design move is not this failure; it is the record of how firmly something is believed. A citation that supplies content the sentence depends on, such as a term or constraint defined elsewhere, is not this failure either. The test for a citation: remove it and ask whether the reader loses something needed right there.
Source: TLR, Hard Lessons; Step 1 statement ("It does not defend itself, hedge, or add references for reassurance"); `RFM_operational.md`, Failure Taxonomy.

### B35. Define a thing by what it is, not where it is recorded

Failures: a record of a fact is written as the rule for the fact, and the rule is wrong at the first case where record and fact come apart.
Behavior: a definition or rule starts from what the thing is, not from where it is written.
When: writing a definition or a rule.
Routing: Check partly. Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: drafting skill; language sweep.
Material:
> **[HL-RECFACT] A record of a fact is not a definition of it.**
>
> The map records which files are documents. That record was then written as the rule for what a document is: "a file with a row is a document". A directory holding other projects' reasoning documents has a row for navigation, and the rule turned it into a document. The same inversion from the other side: a skill bundle has nowhere to write the version header, and the missing line was read as the type having no instances. The pull is that the record is searchable and the fact is not, so a rule stated in terms of the record looks like the more precise one. It is the less precise one, and it is wrong at the first case where the record and the fact come apart. The tell is a rule that starts from where something is written rather than from what it is.
Source: TLR, Hard Lessons.

### B42. Revise earlier sections when later work sharpens them

Failures: the eight sections are worked as a strict sequence, and Landscape research that sharpens the problem statement or shows an assumption to be imprecise does not reach the sections written before it; in guided drafting, a newcomer is told to revise without being told why; Landscape research shows the problem already answered, and the document continues anyway. The reverse also fails: the Problem is reconsidered mid-session, and the Assumptions, Landscape and Chosen Direction argued against the old gap are not re-checked, because nothing forces it; new content pulls the Problem toward itself, because it feels like the point (both known only by their first sentences; from the removal log).
Behavior: when later work, most often Landscape research, sharpens an earlier section, go back and revise it. A newcomer is told why. If research already answers the problem, say so and close the document there.
When: phase one, after Landscape research and whenever a later section changes the ground of an earlier one.
Routing: Check partly. Severe no. Search no. Moment triggerable (Landscape research done).
Origin: any author.
Carriers: drafting skill (once Landscape research is done).
Material:
> **[HL-LRRL] The section sequence is not strictly linear; the Landscape can require revising what came before it.**
>
> Across several projects using RFM, Landscape research regularly, not always, surfaces information that sharpens the problem statement or an assumption written before that research happened. The Landscape can reveal that an assumption was imprecise or that the problem statement was narrower than the domain warrants. The guided drafting prompt must build this revision loop in explicitly, and the newcomer must be told why, not just instructed to do it.
Source: `RFM_guided_drafting_prompt_reasoning.md`, Hard Lessons; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I59. After the Landscape section in a guided draft, stop and explicitly revisit Problem/Assumptions before continuing; if the research already answers the newcomer's problem, say so and close the document there.
From the guided drafting prompt (`RFM_guided_drafting_prompt_reasoning.md`, Chosen Direction, "Why the session must remain open to closing early, honestly"):
> **Why the session must remain open to closing early, honestly**
>
> If the Landscape research reveals that a solution to the newcomer's problem already exists, the honest response is to name that and close the reasoning document there. Continuing into Options Considered and Chosen Direction when the Landscape has already answered the question produces a document that reasons toward a conclusion the research already supplied; that is not reasoning, it is retrofitting. The prompt must make this possibility explicit: a reasoning document that closes after the Landscape because the Landscape resolved the problem is not a failed session. It is an honest one. The co-author's job at the Landscape stage includes asking directly whether the research has changed what the newcomer believed their problem to be, and whether continuing is still warranted.

From the removal log (`removal_log.md`, earlier rebuild attempt; one line per block cut from an old carrier, the block's first sentence only; the full block is in the old repository's history):
> traveling prompt -> Why engaging with The Problem differs from engaging with any other section: reconsidering an existing Problem statement mid-session invalidates everything argued against the old gap (Assumptions, Landscape, Chosen Direction), and nothing currently forces a re-check when it moves. Boundaries and Open Questions resolved: already covered by Always-on (structural-change gate; claim discipline and honesty entries). Landscape drift modes resolved: landed in RFM_skill_drafting_reasoning.md's new Chosen Direction entry. -> needs a home: Always-on, structural-change gate (parked, not touched this session)
>
> sweep prompts -> HL-PROBPULL: When a session adds new reasoning to a document, the new content feels like the point and the Problem feels like it should reflect that. -> needs a home

### B44. Keep observation apart from interpretation, and the question visible

Failures: an interpretation is written as an observation; the question being decided and the case for and against it drop out of an artifact, and a reader sees only the conclusion. Observation and interpretation are conflated in one sentence; reasoning is compressed to a conclusion without showing the path. These failure lines were written during sorting: HL-CLAIM names the discipline and where it is carried, not a failure.
Behavior: when forming a claim, separate observation from interpretation. Keep the question being decided, and the case for and against it, visible in every artifact it appears in.
When: any claim, both phases.
Routing: Check partly (a reader can tell whether the question and the case for and against are present). Severe no. Search partly (question and case present). Moment unannounced.
Origin: any author.
Carriers: drafting skill; language sweep.
Related: B40 (compressing reasoning is the act; a conclusion without its path is the state it leaves in the text).
Material:
> **[HL-CLAIM] Why claim discipline is carried by the traveling prompt**
>
> How claims are formed, how observation is separated from interpretation, and how the question being decided stays visible, with the case for and against it, across all artifacts is a reasoning discipline principle, not a house style concern. A principle with that scope belongs in the traveling prompt. The operational document may carry project-local reminders, but it should not be the primary source for a principle that governs the quality of reasoning itself.
From the Failure Taxonomy (`RFM_operational.md`), language:
> - Reasoning compressed to a conclusion without showing the path
> - Observation and interpretation conflated in one sentence
Source: `RFM_traveling_prompt_reasoning.md`, Hard Lessons; `RFM_operational.md`, Failure Taxonomy.

### B48. Write for a reader who was not in the session

Failures: session-born shorthand requires the drafting session to be understood; insider terminology appears without a definition or a glossary pointer; language is written for the session that produced it rather than for a future reader (curation failures bullet, material in B9).
Behavior: write so a reader who was not in the session can follow. Replace session shorthand with what it stands for. Define an insider term or point to where it is defined. Address the future reader, not the person reviewing the draft.
When: any write; most of all late in a long session.
Routing: Check yes (a fresh reader, B27). Severe no. Search partly (terms with no definition or glossary pointer). Moment unannounced.
Origin: any author.
Carriers: drafting skill (the audience question: text addressed to the person reviewing the draft); language sweep; always-on (conversation slice: an item put up for the human to rule on is stated by what it is).
Related: B1 (content missing, not unreadable). B22 (a way in for a first-time reader). B25 (HL-ADJCHK: audience tested as comprehension). B27 (the fresh-session test).
Material:
From the Failure Taxonomy (`RFM_operational.md`), language:
> - Session-born shorthand that requires the drafting session to be understood
> - Insider terminology without a definition or a glossary pointer
Source: `RFM_operational.md`, Failure Taxonomy; `RFM_human_prompt.md`
From the human prompt (`RFM_human_prompt.md`, Test whether a term carries its meaning outside the session):
> **Test whether a term carries its meaning outside the session that coined it**
>
> Ask "does this travel?" before a session-born term enters a document
>
> Every productive reasoning session generates its own language. Terms that feel precise and shared between you and the AI, shorthand that captures something real, arrive with a false sense of clarity. They feel document-ready because they worked so well in the conversation that produced them. But the conversation is not the document. A document is read by people and LLMs who were not in that session. If the term requires the session to be understood, it will degrade every time it is read without that context.
>
> This failure is easy to miss because the human introduces shorthands too, not only the AI. A term you coined feels obvious to you in a way that masks how opaque it is to anyone else. The discipline is to test it at the moment of capture, before it enters the document, not after.
>
> In practice: when a term or phrase has emerged in the session and feels worth capturing, pause before writing it into the document. Ask the AI: "does this travel?" If the answer is yes, ask it to explain the term back to you as if it had never seen the session. A vague or circular explanation is the real answer, not the claim that it travels. If it doesn't travel, either define it inline, find a more self-contained phrase, or add it to the glossary. A term that requires explanation every time it is encountered is not a term; it is a private language.
From the sweeps (`RFM_sweep_operational.md`, Language catalog, per-section primary questions):
> *The Problem:* Does this section use any terms carrying project-specific meaning without a glossary pointer or inline definition? Is the problem statement legible to a domain-agnostic reader?
>
> *The Assumptions:* Does each entry read as a testable belief to a first-time reader, or does the wording make it sound like a description or instruction? Has any session-born shorthand been captured without being spelled out? Does any entry defend its evidence rather than state it, qualifying against a challenger rather than recording what is believed, or citing a source the reader does not need at that point?
>
> *The Landscape:* Does each row use consistent language across entries? Has any cell absorbed insider shorthand a fresh reader cannot parse? Does the closing paragraph use domain-legible wording or process-internal shorthand?
>
> *The Options Considered:* Is each option's rejection reasoning legible without the session context that produced it? Does any entry assume the reader knows what was tried before the option was named?
>
> *The Chosen Direction and Why:* Does each entry separate observation from interpretation cleanly? Has any entry compressed reasoning into a conclusion without showing the path? Is any claim present that outruns its evidence without being flagged? Does any entry defend its evidence rather than state it, qualifying against a challenger rather than recording what is believed, or citing a source the reader does not need at that point?
>
> *The Boundaries:* Is each boundary stated in terms a first-time reader can apply, or does any entry require prior session context to understand what is being excluded?
>
> *The Open Questions:* Is each question genuinely open as stated, or has session context resolved it invisibly, leaving wording that implies uncertainty that no longer exists? Does any entry use shorthand for a question that requires spelling out?
>
> *The Hard Lessons:* Does each lesson carry the reasoning that earned it, or has it been compressed to a conclusion? Would a reader who was not in the session that produced the lesson understand both what happened and why it matters?
>
> ---
Note (from the sweeps): the language catalog is kept here whole. Its questions also serve B24 (evidence defended), B44 (observation and interpretation, compressed reasoning), B49 (claims outrunning evidence, uncertainty that no longer exists) and B9 (curation failures). Step 3 routes a language sweep afterwards for B44, B48, B49 and B50 without saying which documents it reads; OQ-LANGOP is that question. Settled: the language sweep reads any document, and asks two of its questions of reasoning documents only (`RFM_sweeps_reasoning.md`, Language sweep).
From prompts reasoning (`RFM_prompts_reasoning.md`, Chosen Direction, "Why the prompt is optimized for its reader, not its author", last sentence of the first paragraph):
> For that reader the prompt has to carry its own vocabulary: a project term it leaves undefined is guessed, and a guess inside an instruction can change what the LLM does with no sign that anything went wrong.
Related (from prompts reasoning): B18 (a carrier travels without the glossary, so pointing to a definition elsewhere does not reach its reader).
From the drafting skill (`rfm-drafting/SKILL.md`, Layer 1, "Drafting a glossary entry"):
> **Drafting a glossary entry:**
> Apply the shorthand test first: can a first-time reader understand this term without the conversation that produced it? If no, the entry is not ready. The definition must include the reasoning behind the term, not just what it means. A definition without its reasoning is a label, not a glossary entry.
From rules-file-editing (`rules-file-editing/SKILL.md`, "Write for a future model with no session memory"; one em dash replaced with a period):
> **Write for a future model with no session memory**
>
> This file's reader is a future Claude instance with no memory of the session that wrote the rule. It may also be a weaker model than the one writing it. Write every rule with:
>
> - A literal trigger condition
> - A required action
> - Where it sharpens recognition: the failure shape prevented, with a concrete discriminating example
>
> Do not rely on implication, shared context, or the assumption that the reader remembers why the rule exists. Cut prose whose only job is to make the rule feel reasonable to the human watching. That content helps no one once the session is gone. Keep concrete failure examples that discriminate when the rule applies; cut everything else.
From rules-file-editing (`rules-file-editing/SKILL.md`, "Check that rule wording is session-independent"):
> **Check that rule wording is session-independent**
>
> Any time a rule is written or edited, check whether its wording depends on a specific incident, conversation, or count that only made sense to the session that wrote it. Rewrite in session-independent terms before finalizing.
>
> What must go: wording whose *meaning* changes or vanishes without the originating session in view.
> What can stay: concrete failure examples that discriminate when the rule applies, even if they reference a historical incident by description.
>
> The distinction: a rule that reads correctly today because the reader still remembers the incident behind it reads as ambiguous or meaningless once that memory is gone.
From the traveling prompt (`RFM_traveling_prompt_operational.md`, Checks after a change, Reader check):
> Reader check. Give the prompt alone to a reader with no other context. Have it list every phrase it would have to guess and what it takes each phrase to mean. Define in plain words, or reword, any phrase it cannot decode or reads differently from what is intended.
Note (from the traveling prompt): a report of what a reader cannot follow misses a phrase read confidently and wrongly. The old reader check also asks what the reader takes each phrase to mean, so that phrase shows up. A fresh reader produces a confident objection rather than a gap (entry AA, in B27). Settled: the language sweep's Terms question asks what the reader takes each term to mean, outside the session. The fresh-context subagent test was taken off this behavior, because the language sweep does the same job.
From the traveling prompt (`RFM_traveling_prompt_reasoning.md`, Chosen Direction, "Why a referenced item is restated when it is surfaced"):
> **Why a referenced item is restated when it is surfaced**
>
> A name, an ID or a position identifies an item only for someone who holds the item in mind. The LLM holds it, because the LLM chose the label. The human often does not, because the label was coined in the session or the item was last seen in an earlier one. A human asked to rule on a label has to look it up or guess. A ruling given on a guess is worth less than one given on the content. The label reads as clear to the LLM, so the gap does not show from its side. So whenever the LLM surfaces an item, it says what the item is, in enough words that the human can rule without having read anything before. Only the items being surfaced need this, not everything that could have been mentioned.

### B49. State a claim as firmly as its current evidence holds

Failures: a claim outruns its evidence without being flagged; wording implies uncertainty that no longer exists; one confidence level is written across a claim whose sub-claims have different evidence; parts with different confirmation standing sit under one heading and read as equally settled (observed once each; from the incubating file).
Behavior: match how firmly a claim is stated to the evidence behind it now. Flag a claim that goes beyond its evidence. Remove hedging once the uncertainty is resolved. Qualification that records how firmly something is believed stays.
When: any write; when an open question resolves.
Routing: Check partly. Severe no. Search no. Moment unannounced; triggerable when a question resolves.
Origin: any author.
Carriers: drafting skill; curation skill (removing a hedge once its question resolves); language sweep.
Related: B24 (qualification written as defense, not as a record of belief). B9 (resolved items left in place). B34 (HL-CFSRCH, HL-PRIMCHK: claims written as settled on evidence nobody checked).
Material:
From the Failure Taxonomy (`RFM_operational.md`), language:
> - A claim that outruns its evidence without being flagged
> - Wording that implies uncertainty that no longer exists
Source: `RFM_operational.md`, Failure Taxonomy.
Note (from the unslop skill): [OQ-EPFL] adds what B49 lacked: firmness matched to the section's epistemic status (assumptions believed, open questions unresolved, chosen directions committed), and a corrective that is not a hedge on every sentence. The installed skill already carries flatness as a pattern (in B53); see the notes in B53 and B2.
From the unslop skill (`RFM_skill_unslop_reasoning.md`, [OQ-EPFL]):
> **[OQ-EPFL] Can epistemic flatness be specified concretely enough to be actionable in the skill?**
>
> Epistemic flatness is the failure where every claim lands with the same assertive tone regardless of how established it is. In reasoning documents this is specific: assumptions are believed but not proven, open questions are genuinely unresolved, chosen directions are committed. Writing all of these with identical confidence misrepresents the document's epistemic state. The corrective is not hedging words on every sentence. It is matching sentence confidence to section epistemic status. Whether this can be specified as a concrete, actionable pattern or requires a different mechanism is not yet determined. Needs empirical observation across sessions before any specification attempt.
From the incubating file (`RFM_incubating.md`, entry I, evidence split by sub-claim):
> ## I. Splitting a claim's evidentiary support by sub-claim, not by claim
>
> When an assumption or claim bundles two sub-claims with different evidentiary strength, writing one confidence level across both produces epistemic flatness even when the words are hedged correctly for the claim as a whole. `[AS-FORM]` in `RFM_instruction_design_reasoning.md` splits its own claim (instruction form moves role) into an activation half, grounded in outside research, and a role half, grounded only in the project's own session record, and states each separately rather than writing one blended sentence. This reads as a general drafting technique rather than an incident specific to that entry: name the sub-claim, then its evidence, repeated for each sub-claim, instead of one summary confidence statement for the whole.
>
> **Why not captured yet:** single instance, drafted once inside one assumption. Not yet tested as a deliberate technique applied on purpose to a different entry.
>
> **Possible home when ready:** `RFM_skill_drafting_operational.md`'s language-compliance guidance, or a new discriminator alongside the existing epistemic-flatness failure type in `RFM_operational.md`'s Failure Taxonomy.
>
> **Signal count: 1** *(this session, `[AS-FORM]` in `RFM_instruction_design_reasoning.md`)*
From the incubating file (`RFM_incubating.md`, entry W, parts with different confirmation standing under one heading):
> ## W. Content whose parts carry different confirmation standing should not share a heading.
>
> The entry gate material was drafted as one eleven-paragraph subsection. Its core, the producing-act gate, was confirmed in session 5; the exclusion requirement, the two-legitimate-outputs rule and the human's half were put to the human after that confirmation and never separately confirmed. Under one heading all four read as equally settled. No sweep question catches it, because every sentence is individually fine and the flatness is structural rather than in the wording. Split into three subsections on the human's prompting. One occurrence.
Note (from the incubating file): I is a technique used once. W related B23 (split, don't relabel).

### B50. Say what is specific to this project

Failures: reasoning is stated at a level of generality that would be true of any project in any domain, particularly in Hard Lessons and Chosen Direction sections.
Behavior: state reasoning in terms of this project's case: what happened here, what was chosen here and why. A sentence that could stand unchanged in another project's document is rewritten to be specific or cut.
When: any write; most of all in Hard Lessons and Chosen Direction.
Routing: Check yes (the substitution test can be run afterwards). Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: drafting skill; language sweep.
Related: B29 (the opposite failure: narrow vocabulary read as general). B9 (text that does not earn its place).
Material:
From the Failure Taxonomy (`RFM_operational.md`), language:
> - Reasoning stated at a level of generality that would be true of any project in any domain, particularly in Hard Lessons and Chosen Direction sections
Source: `RFM_operational.md`, Failure Taxonomy.

### B53. Write without LLM tells

Failures: prose carries the patterns LLM training produces, such as importance inflation, flatness, wordiness and em dashes; a few reduce to a search, most do not; a visual re-read passed em dashes twice (observed; from the old unslop skill).
Behavior: strip LLM-tell patterns before text leaves the writer. Run the search for the ones that reduce to one.
When: every output.
Routing: Check partly (a reader catches them afterwards; a pattern list catches only what it lists, B39). Severe no. Search partly (em dashes yes; wordiness and flatness no). Moment triggerable (each output).
Origin: tool pull.
Carriers: file-write skill (the em dash search on the lines written); unslop skill (the tells that do not reduce to a search); language sweep (em dashes, whole document).
Related: B38 (check at the moment of output). B39 (HL-PLCL). B49 (flatness is firmness not matched to evidence). B9 (text that does not earn its place).
Material:
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I14. Suppress LLM-tell prose patterns that don't reduce to a search (wordiness, flatness, importance inflation).
> - I83. Em-dash suppression: character present or not.
Source: behavior inventory (earlier rebuild attempt); `RFM_operational.md`, Prose Derivative Writing, Em Dash Check; `RFM_skill_unslop_reasoning.md`, `RFM_skill_unslop_operational.md`, installed `rfm-unslop/SKILL.md`.
From the operational document (`RFM_operational.md`, Prose Derivative Writing):
> Text-facing RFM derivatives (public documentation, onboarding guides, worked examples, README files) require two layers of writing discipline applied together. Neither substitutes for the other.
>
> **Layer 1: Write from the reasoning**
>
> RFM prose follows from RFM's epistemic commitments. Apply these directly:
>
> - State the argument first, then support it. Do not build to a conclusion.
> - Name uncertainty explicitly. Do not smooth over it.
> - When something could fail, say so. Do not lead with aspiration.
> - Commit to one defensible position. Do not hedge across multiple alternatives to avoid commitment.
>
> These are not style preferences. They are what RFM reasoning looks like in prose form. A derivative that does not reflect them is not consistent with its source.
>
> **Layer 2: Protect legibility**
>
> LLM-generated text carries recognizable behavioral patterns. Readers detect them (consciously or not) and they undermine the signal the derivative is meant to carry. Suppress the following regardless of how well Layer 1 is applied:
>
> - Uniform paragraph length and sentence rhythm
> - Importance inflation: phrases like "a pivotal moment," "it is worth noting," "this underscores"
> - Throat-clearing openers: grand statements about the state of the world, restatement of the question just asked
> - Structural false contrasts: "It's not X, it's Y" / "Not X, just Y"
> - Em dashes: barred entirely. See Em Dash Check.
> - Vocabulary tells: "delve," "underscore," "robust," "seamless," "transformative," "holistic," "leverage" (as verb), "comprehensive"
> - Rhetorical ramps: announcing an instruction before giving it. "The required act is simple:", "The answer is straightforward:", "What this requires is:" all bury the instruction under an announcement of the instruction. State the action directly.
>
> **Applying both layers**
>
> Draft for Layer 1 first, get the reasoning character right. Then read for Layer 2, remove the patterns that would make the derivative read as machine-generated. A draft that passes Layer 1 but fails Layer 2 has the right content and will not be read. A draft that passes Layer 2 but fails Layer 1 is legible and says nothing worth reading.
From the operational document (`RFM_operational.md`, Em Dash Check):
> Em dashes are barred from every file in the project. Conversation is out of scope.
>
> Anything destined for a file is written without em dashes from the first draft, a draft shown for approval included. A draft approved with em dashes in it becomes a rewrite of content already agreed.
>
> Verify by grep, not by rereading. Write the candidate text to a scratch file outside the project and grep it for the character. The destination document is never the file grepped. Report the check as done only after the grep returns clean.
>
> Replace an em dash with a comma, a period, or a recast sentence. Parentheses are not a substitute. They carry the same tell.
From the unslop skill (`RFM_skill_unslop_reasoning.md`, The Problem):
> Slop enters RFM documents through the co-authorship session itself. The traveling prompt instructs suppression of LLM behavioral patterns, but that instruction is ambient and competes with the cognitive load of doing the reasoning work simultaneously. The two-layer discipline (write from the reasoning, suppress LLM patterns) assumes both can be held in one pass. In practice, slop gets through. Catching it requires a separate sweep pass that costs time proportional to how much reasoning happened in the session. The longer the session, the larger the debt.
>
> The debt compounds in a specific way: productive sessions generate more slop, which means more sweep work, which means the sessions that advance the reasoning most are also the sessions that create the most corrective work. Clean source documents reduce how much filler the LLM adds in derivatives, but they do not touch the entry point. Nothing currently catches slop at the session level before it hardens into documents.
From the unslop skill (`RFM_skill_unslop_reasoning.md`, The Assumptions, [AS-UP]):
> **[AS-UP] -** Precise source documents reduce filler in derivatives. An LLM with dense, specific source material has less room to add explanation or pad structure. This does not address the session entry point; it reduces pressure downstream of it.
From the unslop skill (`RFM_skill_unslop_reasoning.md`, The Chosen Direction and Why, "Why the traveling prompt carries the declaration" and "Why the skill targets surface patterns, not epistemic posture"):
> **Why the traveling prompt carries the declaration.**
> The traveling prompt is always loaded. It is the only artifact that guarantees a session-level instruction reaches every exchange. A document the LLM may or may not have loaded cannot carry a session-wide trigger reliably.
>
> **Why the skill targets surface patterns, not epistemic posture.**
> Epistemic failures (sycophancy, anchoring to early framings, uniform confidence across claims of different strength) are upstream of text production. They corrupt what gets reasoned before a word is written. Surface pattern suppression does not reach them, and trying to combine both in one skill would dilute the trigger clarity that makes the always-on design work. Epistemic posture is addressed in the traveling prompt's co-author role instructions.
From the unslop skill (`RFM_skill_unslop_operational.md`, Traveling prompt declaration):
> The traveling prompt must carry this line in the Identity section, immediately after the source/derivative statement:
>
> > This is a project using the RFM approach. Apply the `rfm-unslop` skill to every response you produce in this session.
>
> This declaration is the trigger mechanism. Without it, the skill does not fire. Any project using the RFM approach and loading the traveling prompt inherits the declaration.

### B58. Reason a section through by its job, not fill it by its definition

Failures: an author fills the eight sections to satisfy their definitions, and the document looks correct and reasons poorly; the LLM fills sections on the author's behalf, or hands over definitions and examples that become a template; the LLM holds its own reasoning back and only asks questions, so the author meets a quizmaster instead of a co-author and is put off; a first-time author stalls when the first section proves hard, because the document seems to need to be complete, correct or final; an author takes familiarity with the problem for familiarity with the solution space and drafts the Landscape without research. Reasoned, not observed: each failure is an assumption in the old reasoning document ([AS-CBID], [AS-CBTM], [AS-LLNB], [AS-LREG]), with no Hard Lesson behind it.
Behavior: draft each section by reasoning through what it is for. Both the author and the LLM propose and challenge (B3), and the author decides what the section says. The LLM neither fills a section alone nor holds its own reasoning back so that the author has to supply it. Before a first document, the author is told it is a living starting point. Before the Landscape, the author is asked whether research is needed.
Forced actor: human (the problem, and the decision on what each section says, come from the author).
When: phase one, drafting. Most acute in a person's first document; also a practitioner's first document for a new project ([OQ-GDNP]).
Routing: Check partly (B47's per-section sweep questions catch some filled sections afterwards; looking correct is how this failure passes). Severe no. Search no. Moment triggerable (the human starts a first document); unannounced in later drafting.
Origin: any author (a newcomer alone with the definitions); tool pull (the LLM fills sections when asked).
Carriers: always-on (both propose and challenge; writing into the document is execution, which the human confirms); first-document session prompt (a first document is a living starting point); drafting skill (each section's job, at the before-drafting moment; the research question before the Landscape).
Related: B3 (HL-SRST). B4 (a newcomer's push for answers; the newcomer owns the move to the next section). B42 (revision after the Landscape; closing when research answers the problem). B47 (section formats; the sweep's per-section questions). B1 (saving each section as it is drafted).
Note: the drafting skill carries both intentions missing from B47's sweep questions and the Assumptions break condition.
Source: `RFM_guided_drafting_prompt_reasoning.md`; `RFM_guided_drafting_prompt.md`.
Material:
From the guided drafting prompt (`RFM_guided_drafting_prompt_reasoning.md`, The Assumptions):
> **[AS-CBID] - Checklist behavior is the default failure mode for a first-time author.** Without active guidance on intention, a newcomer will treat the eight sections as boxes to fill, producing content that satisfies the section definition without reasoning through it. The prompt must actively resist this tendency, not assume the newcomer will resist it themselves. This assumption breaks if newcomers left without active guidance reason through sections anyway, for instance if section definitions alone are enough to prompt genuine reasoning rather than box-filling. If that's the case, Socratic mode's central justification would be weaker than the design assumes.
>
> **[AS-CBTM] - Understanding the methodology does not resolve the cost/benefit timing mismatch of the first document.** A newcomer who knows what a reasoning document is may still stall when the first section proves harder than expected and the benefit feels distant. This assumption breaks if newcomers reliably push through a hard first section without needing the livingness commitment or Socratic mode's support. In that case those mitigations would be solving a problem understanding alone already handles.
>
> **[AS-LLNB] - The "livingness" of RFM documents substantially lowers the barrier for a newcomer, if it is made explicit.** A newcomer who believes their first document must be complete, correct, or authoritative faces a much higher bar than one who understands it is a starting point meant to be revised. The barrier only lowers if the newcomer actually holds this belief at the moment the first section proves hard, not because they read it once beforehand. This assumption breaks if stating livingness explicitly turns out not to change newcomer behavior, for instance if a newcomer still treats the document as high-stakes despite being told otherwise. If that's the case, the mitigation is decorative rather than functional.
>
> **[AS-LREG] - A newcomer may not recognize on their own that the Landscape needs external research.** They may assume familiarity with their problem substitutes for familiarity with the solution space. The knowledge gap itself is unremarkable. It applies to everyone, expert and newcomer alike. What's specific to a first session is whether the newcomer notices the gap without being asked. This assumption breaks if newcomers reliably raise the need for research themselves. In that case the prompt's active check is unnecessary; the newcomer's own judgment would have caught it.
From the guided drafting prompt (`RFM_guided_drafting_prompt_reasoning.md`, Options Considered, option 1):
> **1. Directive vs. Socratic facilitation mode**
>
> Tell the newcomer what belongs in each section (definitions, examples, what good looks like) vs. ask questions that draw the reasoning out. Directive mode is faster and feels safer to a newcomer who doesn't know what to write. Rejected because directive mode produces the failure the prompt exists to prevent: a newcomer who fills sections correctly without reasoning through them. A section definition handed to the newcomer becomes a template. A question the newcomer must answer from their own thinking becomes reasoning. The Socratic mode is slower and requires the newcomer to tolerate uncertainty, which [AS-CBTM] names as a genuine risk. That risk is managed by making the "livingness" commitment explicit early ([AS-LLNB]), not by retreating to directive mode.
From the guided drafting prompt (`RFM_guided_drafting_prompt_reasoning.md`, Chosen Direction, "Why Socratic facilitation over directive mode", first two paragraphs):
> **Why Socratic facilitation over directive mode**
>
> The failure the guided drafting prompt exists to prevent is a newcomer who produces a correctly structured document without reasoning through it. Directive mode (definitions, examples, what good looks like) hands the newcomer a template. A template answered is not a reasoning document. It is a form. Socratic mode guards against this by keeping the reasoning with the newcomer: questions draw out what the newcomer must answer from their own thinking.
>
> Socratic mode does not mean the LLM withholds its own reasoning. The co-author role remains fully active: the LLM proposes, red teams, and contributes genuinely throughout the session. The constraint is narrow: the LLM does not fill sections on the newcomer's behalf. Within that constraint, the session is genuine co-authorship. A newcomer who experiences the LLM reasoning alongside them, rather than extracting their reasoning through interrogation, will understand what RFM co-authorship feels like before they have finished their first document. That experience is part of what the guided drafting session is designed to produce.
From the guided drafting prompt (`RFM_guided_drafting_prompt_reasoning.md`, Open Questions, [OQ-LTCT]):
> **[OQ-LTCT] The LLM contribution threshold in a first session.**
>
> When should the LLM shift from drawing out the newcomer's reasoning through questions to contributing its own reasoning directly? In a standard RFM session the co-author role is fully active throughout. In a guided drafting session the threshold for direct contribution is higher: the risk of the LLM's reasoning displacing the newcomer's is real when the newcomer has not yet developed the practice of pushing back. Where exactly that threshold sits, how it varies by section and by newcomer state, and whether it can be specified in the prompt or must remain a live judgment call, requires trial.
Note: the Behavior line answers [OQ-LTCT]: there is no contribution threshold.
From the guided drafting prompt (`RFM_guided_drafting_prompt.md`, opening, livingness):
> First: tell the newcomer that the document produced in this session does not need to be complete, correct, or final. It needs to be honest and structured. RFM documents are living artifacts. The first version is a starting point, not a deliverable. State this directly. The newcomer has read it. Hearing it as permission at the moment the cost of starting is highest is different from having read it.
From the guided drafting prompt (`RFM_guided_drafting_prompt.md`, opening, contribution threshold):
> The threshold for direct contribution to section reasoning is higher here than in a standard RFM session. The newcomer's reasoning must be exercised, not displaced. When in doubt, ask first. Contribute when the reasoning gap is clear and a question alone will not bridge it.
From the guided drafting prompt (`RFM_guided_drafting_prompt.md`, Section sequence and intentions):
> Work through the eight sections in order. For each section, the intention below tells you what the section is actually for, so your questions and contributions serve that purpose rather than the surface definition. Do not define sections to the newcomer. Do not offer examples of what good looks like. Draw the reasoning out. When the newcomer is ready to draft, use the formatting specified per section below.
>
> **The Problem**
> What fails or stays invisible without this reasoning? The problem statement earns its place when a reader understands why the newcomer cannot simply proceed without reasoning through this first. Watch for problem statements that describe a project rather than name a gap. Push until the gap is visible.
> *Format: plain prose. Bold subheading only when a structurally distinct second argument would otherwise read as continuation.*
>
> **The Assumptions**
> Testable beliefs the reasoning depends on, not descriptions, not instructions. Each entry should survive this test: if this assumption turned out to be false, the direction would need to change. Push back on any entry that would survive being wrong.
> *Format: **[AS-XXXX] -** bold claim, body in same paragraph. Hyphen after ID, not em dash.*
>
> **The Landscape**
> What already exists that is relevant to the problem: approaches, prior art, adjacent practices. The Landscape distinguishes, it does not choose. Each entry answers: what does this approach do, and why is it insufficient for this specific problem? The section closes with a short paragraph naming the gap the landscape collectively reveals.
> *Format: one intro sentence naming the specific question this landscape must answer → table (Approach | What it does | Why it's insufficient) → closing paragraph opened with **The gap:** in bold.*
>
> Before the newcomer drafts the Landscape, ask whether they have sufficient knowledge of what exists in their domain. If not, pause and conduct the research together before any drafting begins.
>
> After the Landscape is drafted, do not move to Options Considered. Stop. Return explicitly to The Problem and The Assumptions. Ask: has the research sharpened or changed what was written there? Explain why: the Landscape is the one point where external knowledge enters, and it changes things. Carrying imprecise early sections forward degrades every section that follows. Revise before continuing.
>
> Then ask directly: has the Landscape research resolved the problem? If an existing approach already answers what the newcomer came to reason through, name that honestly and close the document here. A reasoning document that closes after the Landscape because the Landscape answered the question is not a failed session. It is an honest one.
>
> **The Options Considered**
> The genuine alternatives considered before arriving at a direction. Each option is rejected for a reason. The reason must be stated. An option without a rejection reason is a placeholder, not a considered option.
> *Format: **1. X vs. Y** as bold title, prose body including the rejection reasoning. Each option self-contained.*
>
> **The Chosen Direction and Why**
> Why the chosen direction was chosen, not what it is or how it will be implemented. Each entry separates the decision from its reasoning. Push back on any entry where how has leaked into why.
> *Format: **Why X** or **Why X over Y** as bold subheading per entry, prose body. No IDs. No numbering.*
>
> **The Boundaries**
> What this reasoning document explicitly does not cover: scope definitions that tell a future reader what questions it will not answer. Not constraints on decisions. Those belong in Assumptions. Not things that are simply undesigned.
> *Format: **Not X.** as bold lead phrase, prose body in same paragraph. No IDs. No numbering.*
>
> **The Open Questions**
> Genuine unknowns the reasoning has not resolved and that matter enough to name. Push back on any entry that has already been answered elsewhere in the document, or that would not affect the reasoning if it remained permanently open.
> *Format: **[OQ-XXXX] Title of the question.** as bold line, prose body as separate paragraph below.*
>
> **Hard Lessons**
> What failed, what that revealed, and why it matters for anyone working with this document in the future. Hard Lessons are written for future readers, not for the session that produced them. Push back on any entry that requires the session context to be understood.
> *Format: **[HL-XXXX] Title.** as bold line, prose body as separate paragraph below.*
From the first session guidance (`RFM_first_session_guidance.md`, Before you begin):
> **Bring the right problem.** Choose something genuine: a decision or practice where the reasoning actually matters to you. Not too large; a problem you already know something about is better than one you are still discovering. The session sharpens the problem. It cannot manufacture one.
From the first session guidance (`RFM_first_session_guidance.md`, What to expect from the session):
> This can feel unfamiliar. It is working correctly when it does.

---

## Derivation and the trial

### B11. Derive from the sources alone, marking each guess

Failures: in phase two the LLM infers past a gap and produces confident output that departs from the reasoning, with nothing to check it against.
Behavior: when a derivative is first created or derived again in full, a subagent holding only the sources derives it and marks each guess that would change what it says or does. We settle the marks together, what we decide goes into the sources, and the derivation goes through once.
When: first creation of a derivative, or a full re-derivation.
Routing: Check yes if the marks are returned. Severe yes (confident divergence at scale), nameable in advance. Search no. Moment triggerable.
Origin: any author.
Carriers: derivation skill; cross-document sweep (reads the derivative against its sources and against any version it replaces).
Source: TLR, [OQ-DLTQ], "Why increasing autonomy raises the stakes for reasoning documents".
From the sweeps (`RFM_sweep_reasoning.md`, Chosen Direction, "Why the relational sweep checks both directions across the reasoning-to-operational boundary"):
> **Why the relational sweep checks both directions across the reasoning-to-operational boundary**
>
> Reasoning documents announce needs without specifying them: a concrete value, threshold, interface, or procedure that derivation will require. Specifying them in the reasoning document pulls implementation detail where it does not belong. The operational document covers those needs. Checking only forward, whether the operational document covers every announced need, trusts that the reasoning document announced every need. An unannounced need is invisible to that pass and falls through, leaving the LLM to invent the specification during derivation rather than read it. Checking only in reverse, whether every specification in the operational document traces to an announced need, catches a different failure: a specification with no announced need means either the reasoning failed to announce it, now made visible, or a decision was made at the operational level that belongs in reasoning first. A specification that traces to a broader reasoning commitment, a chosen direction or design principle, is grounded. The reverse-direction finding is the absence of any grounding in the reasoning document, not the absence of a one-to-one announced need. A reasoning document that commits to a direction at a level of abstraction that produces multiple operational specifications has announced a need at the appropriate level. Requiring a separate announced need for each downstream specification would pull implementation specificity into the reasoning document. Both directions check the same boundary. Neither catches what the other misses. This also closes the boundary the methodology already guards from one side: wrong content present in the operational document is reasoning-leak; required content absent is a specification gap. Same boundary, two violations.
From the sweeps (`RFM_sweep_operational.md`, Relational sweep specification, entry condition and finding criteria):
> *Both documents present.* The sweep requires the reasoning document and its operational derivative simultaneously. If either is absent, stop and flag it.
>
> *Forward direction.* An announced need is a finding only when its absence would leave an LLM deriving the current artifact without a necessary behavioral decision, constraint, or interface specification. Do not report the absence of a restatement of reasoning, an acknowledgement of future uncertainty, or a textual counterpart that adds no derivation guidance.
>
> *Reverse direction.* A specification is grounded when it traces to any commitment in the reasoning document, including a chosen direction or design principle. The absence of a one-to-one announced need is not a finding when broader grounding exists. A finding requires the absence of any grounding at any level.
>
> *Pre-filter gate.* Before surfacing a finding in either direction, confirm that the proposed addition or change would alter current derivation behavior. If it would not, do not report it.
From the sweeps (`RFM_sweep_prompt_relational.md`, Protocol, per-section checks):
> Work through the reasoning document section by section. For each section, check both directions simultaneously: identify announced needs and verify each is covered in the operational document, and identify which operational specifications trace to this section and verify each has grounding in the reasoning document. Report findings as you go.
>
> **The Problem**
> Check for announced needs: constraints, definitions, or scope claims that derivation will require but this section leaves unspecified.
>
> **The Assumptions**
> Check for announced needs: conditions, thresholds, or dependencies named as beliefs that the operational document must specify concretely.
>
> **The Landscape**
> Check for announced needs: distinctions, prior-art references, or gap claims that the operational document must operationalize.
>
> **The Options Considered**
> Check for announced needs: rejection criteria, failure modes, or conditions named that the operational document must cover.
>
> **The Chosen Direction and Why**
> Check for announced needs: this section carries the highest density of announced needs. Every "why" names a constraint or design principle that must appear in the operational document's procedures or specifications. Work through each entry.
>
> **The Boundaries**
> Check for announced needs: exclusions that require a corresponding procedure or scope specification in the operational document.
>
> **The Open Questions**
> Check only whether an unresolved question leaves the current operational contract unable to govern derivation. A future design question needs no operational placeholder when the present contract is clear and binding.
>
> **The Hard Lessons**
> Check for announced needs: failure patterns that require a corresponding safeguard or procedure in the operational document.
From the sweeps (`RFM_sweep_reasoning.md`, Open Questions):
> **[OQ-ARTCV] Whether the relational sweep's reach should extend from reasoning-to-operational derivation to reasoning-to-artifact derivation.**
>
> The relational sweep already checks whether a derivative covers what its source announced, and whether the derivative contains anything ungrounded in the source. `[AS-OPNS]` excludes operational documents from the structural sweep's reach because they have no fixed structure to check architecture against, but a boundary check doesn't need fixed structure on the derivative side, only a source to compare it against, so that same reasoning doesn't obviously justify excluding prompt artifacts from the relational sweep. `[HL-DCFL]` in `RFM_top_level_reasoning.md` already shows this failure class is real: a reasoning document can be internally sound and still produce a derivation failure, where the LLM deriving from it collapses what the source kept distinct. That instance is not artifact-specific, so it does not show the failure occurs in prompt-artifact derivation, only that a boundary check catching sound-reasoning/bad-derivation failures would have something to catch. Whether the relational sweep's current restriction to `module_operational` derivatives is a deliberate scope decision or an accident of the map's type taxonomy is open. If the latter, extending the relational sweep is not a type-filter change: the sweep's one-to-one protocol would need to handle the sweep prompts' own one-reasoning-to-three-artifacts shape first.
Note (from the sweeps, against step 3): B11 is routed to the first creation of a derivative. The old relational sweep asked the same sufficiency question of any existing pair, in both directions. After a source changes, the forward half (a need the reasoning now announces that the operational document does not cover) has no new carrier: B2's commit check flags a derivative that changed without its source, not a source that changed without its derivative, and a check on change alone cannot tell whether coverage is missing. The reverse half (a specification with no grounding) is B2's failure. Settled at build. OQ-ARTCV asks whether the check reaches artifacts; under B2 every carrier has a source, so it is the same question as this note.
Settled: the forward half after a source changes, and any existing pair, are read by the cross-document sweep, whose reasons are in `RFM_sweeps_reasoning.md`. [OQ-ARTCV] is settled there: the check reaches carrier texts, because under B2 every carrier has a source.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Assumptions):
> **[AS-DPCL] - Autonomous derivation is only reliable when the source documents are complete, clear, and unambiguous.** When the LLM can confirm it does not need to interpret or fill gaps to produce the derivative, derivation can proceed. When it cannot, the source requires further work before the session begins. This assumption breaks if reliable derivation turns out to be possible from incomplete or ambiguous source documents, for instance if an LLM could resolve genuine gaps correctly without inference risk. Nothing in current practice suggests this: the confirmation gate exists because unresolved gaps have consistently meant either invented content or a stalled session, not successful derivation.
> **[AS-DPSA] - When an instruction is ambiguous about scope, the LLM default is to proceed rather than confirm.** Scope ambiguity is not treated as a signal to pause; it is treated as a gap to fill by inference. This assumption breaks if the prompt explicitly establishes confirmation as the default response to ambiguity, which is precisely what the confirmation gate is designed to do.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Chosen Direction):
> **Why mid-session drift monitoring is the human's responsibility**
>
> The derivation prompt establishes the posture at session start, through the confirmation gate. It cannot supervise the session as it runs. If the LLM drifts from that posture partway through, back toward inference or the co-author habits the traveling prompt trained, nothing internal to the prompt catches it. The LLM cannot reliably self-report a state it has already drifted out of. The human present during the session is the only party positioned to notice, so mid-session monitoring falls to them by elimination, not by design choice.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Open Questions):
> **[OQ-DPAG] The derivation prompt in agentic settings.**
>
> The Chosen Direction places mid-session drift monitoring with the human. In an agentic setup the human is not present during execution and only sees the result. Whether the derivation prompt as designed provides sufficient governance without a human monitor, or whether agentic derivation requires additional mechanisms, is an open question.
> **[OQ-DPGV] Whether the confirmation gate reliably stabilizes derivation behavior.**
>
> The confirmation gate is designed to anchor the LLM in the instruction-faithful regime before derivation begins. Whether a successful confirmation actually prevents drift toward prior-dominant behavior during the session, or whether regime shifts occur regardless, has not been empirically tested in RFM derivation sessions. Its reliability under real conditions remains unverified.
From the derivation prompt (`RFM_derivation_prompt_operational.md`, What the derivation prompt must establish):
> **The confirmation gate.** Before derivation begins, the LLM runs an active confirmation exchange. It surfaces gaps and ambiguities one at a time: specific named unknowns it cannot resolve from the source documents without interpreting or inferring. There is no partial pass. Any gap stops the session. The practitioner takes all gaps back to phase one, resolves them in the source documents, and returns for a fresh gate. The gate passes only when the LLM confirms it can produce the derivative faithfully from the source documents as they stand.
> **Faithful rendering.** The LLM derives from the source documents only. If a gap surfaces mid-derivation that was not caught at the gate, the LLM stops, names the gap precisely, and waits for ruling. It does not fill the gap by inference. It does not continue past it.
From the derivation prompt (`RFM_derivation_prompt.md`, Before you read anything else):
> You are about to derive a document from RFM source documents. The gate runs before you read anything else. It cannot be sourced from the reasoning documents; it must be active first.
>
> **Confirmation gate:**
>
> Read all source documents provided. Then answer explicitly:
>
> 1. Is there anything in the source documents that requires you to interpret or infer rather than render directly?
> 2. Is there any gap (a decision, a specification, a boundary) that the source documents do not resolve?
> 3. Can you produce the derivative faithfully from these documents as they stand, without filling any silence by inference?
>
> If the answer to (1) or (2) is yes: stop. Name each gap precisely. Do not proceed. The practitioner takes the gaps back to phase one, resolves them in the source documents, and returns for a fresh gate.
>
> If the answer to (3) is yes and (1) and (2) are no: the gate passes. Proceed to derivation.
>
> There is no partial pass. One unresolved gap stops the session.
Note (from the derivation prompt, against step 3): step 3 routes B11 to a test before first creation. The old carrier also stops mid-derivation at a gap the gate missed, and puts drift during the session on the human by elimination (OQ-DPAG: in an agentic setting no human is present). Step 3 names a derivation session prompt but routes to it only the test before first creation; what it carries for the mid-derivation stop and for a re-derivation, when one is chosen, is not decided. Whether to re-derive after a source change is a judgment, not a requirement (ruled in B28). A derivation session also runs against always-on, which carries B3 (challenge), the posture AS-DPCP (in B37) says conflicts with derivation. Settled at build.
Settled: the derivation skill carries the marks and the check after a derivation. The always-on instructions hold the posture: when carrying something out, do nothing beyond what was agreed, and stop when something does not fit.
Note (from the derivation prompt, observed by comparing the files): the reasoning document gives the sibling-scope gate's mechanics to "the derivation prompt's procedural design". Neither `RFM_derivation_prompt_operational.md` nor `RFM_derivation_prompt.md` carries it (confirmed by a search for "sibling" and "mode-distinct" in both). A live case of the forward half in the note above: a need the reasoning announces that the operational document does not cover.
Settled: the sibling-scope gate is dropped. Its one case was RFM's own sweep skills, and a carrier is built in a carrier-build session, which asks of every check question whether it belongs to this carrier's job.

### B18. Handed set is sufficient for a model alone

Failures: the release set only works with its author or the repository behind it; a session fills gaps from outside the set and the gap never surfaces.
Behavior: travelling documents carry what a model needs and point nowhere outside the set as a fallback.
When: when building or changing the release set; at the trial.
Routing: Check yes (the trial). Severe yes (a failed trial or a silent one), nameable. Search partly (pointers to the repository). Moment triggerable.
Origin: any author.
Carriers: release preparation; release pointer check (mechanical); fresh-context subagent test.
Source: TLR, "Why readiness is decided by a first external trial".
From the map (`RFM_map.md`, Document Map, the Travels column):
> **Travels** records whether a document is part of the set handed to a practitioner in a release, not whether it is available. Everything in this repository is public. `stays` means the document is not part of the handed set, because a session reading only that set must not need it. This map travels too, as the template a practitioner's LLM works from; it has no row because the map does not list itself.
>
> A travel value is a ruling, not a judgment a session makes while adding a row. A new document's cell is decided with the human.
Note (from the map, against step 3): the mechanical check flags pointers from the release set to anything outside it, and the subagent holds only the handed set. Both need a record of which documents are in the set. In the old set that record is the map's Travels column, one ruling per document made with the human. No new carrier holds it yet. Settled for the fresh-context subagent test: the caller names the files handed, and the test keeps no record of the set. Where that record lives is decided when release preparation is built. HL-ADJCHK (B25) is the lesson about checking this column.

### B32. Keep distinct concepts visibly distinct

Failures: two concepts stated close together in an internally sound source collapse into one during derivation.
Behavior: concepts that must stay distinct at derivation time are visibly separated or explicitly differentiated in the source.
When: phase one writing; after a derivation failure.
Routing: Check partly (a fresh read's restatement can find it). Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: fresh-context subagent test (the restatement shows where a reader merges two concepts).
Material:
> **[HL-DCFL] Derivation failures can originate in source documents that are internally sound.**
>
> A reasoning document can be internally correct and still produce derivation failures. The failure mode identified in practice: two distinct concepts stated in close proximity in a Chosen Direction entry collapsed into one during LLM derivation under compression. The source document treated them as distinct. The deriving LLM conflated them. The document was not wrong. It was not sufficiently derivation-legible. This is the practical consequence of the two-phase design requirement named in [AS-TPAS]: joint legibility and derivation-legibility are different properties, and a document can satisfy one without satisfying the other. The mitigation is not longer or more detailed source writing. It is structural separation: concepts that must remain distinct at derivation time must be visibly distinct in the source, with enough distance or explicit differentiation that compression cannot collapse them.
Source: TLR, Hard Lessons.

## Pressure mode

### B13. Enter pressure mode only on sufficient documents

Failures: pressure mode is used as permission to skip reasoning before the documents are far enough along to act as commander's intent.
Behavior: entering pressure mode is a decision taken against the state of the documents.
Forced actor: human (the decision to enter is intent).
When: at the onset of delivery pressure.
Routing: Check partly. Severe no. Search no. Moment triggerable (entry is announced).
Origin: any author.
Carrier:
- None built (ruled in step 3). Pressure mode has not been used in a project, so no failure has been observed to build against. Build when a project first enters pressure mode.
- Considered: the human announces entry, which loads a skill; gate: the LLM states which reasoning documents the pressure work executes inside, mirroring B5's frame.
Source: TLR, "Why the methodology operates in two modes".

Placement (step 5): behaviors document, group 8. Register: no carrier until a project first enters pressure mode. The Considered line stays in the behaviors document as input for that build. The reason for pressure mode stays in TLR, "Why the methodology operates in two modes".

### B14. Log deviations under pressure

Failures: deviations, deferrals and broken assumptions pass unrecorded and the return has to be reconstructed from the artifacts.
Behavior: keep a minimal log of deviations, deferrals and broken assumptions while in pressure mode.
When: throughout pressure mode.
Routing: Check partly (artifact against documents shows unlogged deviations). Severe no. Search no. Moment unannounced.
Origin: any author.
Carrier:
- None built (ruled in step 3). Pressure mode has not been used in a project, so no failure has been observed to build against. Build when a project first enters pressure mode.
- Considered: while pressure mode is on, the handover file says so and where the log is; the instruction to log sits in a rules file read at session open, which is weak because noticing a deviation is a moment only the LLM would notice; the log marked append-only (B56); unlogged deviations caught at the return (B15).
Undesigned: form of the log is [OQ-MCDC]. Recorded as a behavior; step 3 decides whether a carrier is possible yet.
Source: TLR, "Why the methodology operates in two modes"; [OQ-MCDC].
From the glossary (`RFM_glossary.md`, entry "Chesterton's Fence log"):
> **Chesterton's Fence log**: A minimal running record maintained during pressure mode, capturing deviations from established reasoning, conscious deferrals, and broken assumptions. Its purpose is to make the return to reasoning mode honest rather than reconstructed from code. Its form is domain-dependent: a section appended to the reasoning document, a separate file, a dated note, whatever is reachable and maintained.
>
> Risk of confusion: Commonly implies a structured audit trail or formal log file. In RFM it is deliberately minimal; the discipline is capture, not format.
Note (from the glossary): the entry gives the log a form where [OQ-MCDC] leaves it open: whatever is reachable and maintained in the domain; what counts is capture, not format. Material until a project first enters pressure mode.

Placement (step 5): behaviors document, group 8. Register: no carrier until a project first enters pressure mode. The Considered line, the glossary entry "Chesterton's Fence log" and its note stay in the behaviors document as input for that build; the glossary keeps its entry. [OQ-MCDC] stays in TLR. The line "step 3 decides whether a carrier is possible yet" goes nowhere: step 3 ruled.

### B15. Return from pressure mode through the log

Failures: pressure mode never ends, or the return skips the log.
Behavior: the return to reasoning mode is mandatory and works through the log.
Forced actor: human (deciding pressure is over).
When: end of pressure.
Routing: Check yes (log items resolved or not). Severe no. Search partly (open log items). Moment triggerable.
Origin: any author.
Carrier:
- None built (ruled in step 3). Pressure mode has not been used in a project, so no failure has been observed to build against. Build when a project first enters pressure mode.
- Considered: the human declares pressure over and a return session prompt works through the log; the flags from B2's commit check during pressure mode list the unlogged deviations; gate: every log item has a resolution recorded in the documents.
Undesigned: [OQ-MCDC].
Source: TLR, "Why the methodology operates in two modes"; `RFM_human_prompt_reasoning.md`
From the human prompt (`RFM_human_prompt_reasoning.md`, Chosen Direction, "Why the LLM keeps the Chesterton's Fence log and the human reads it"):
> **Why the LLM keeps the Chesterton's Fence log and the human reads it**
>
> In pressure mode, the LLM does the executing, so it is the one who deviates from the established reasoning, defers a question, or finds an assumption broken, and it can record each as it happens in the Chesterton's Fence log. Both terms are defined in the glossary. The human's part is the return: reading the log when pressure lifts and deciding what goes back into the reasoning. A log that is kept and never read does not make the return honest, so the reading stays with the human. The LLM will miss deviations it does not recognize as deviations. This split is untested, because the log has not yet been used in practice.

Placement (step 5): behaviors document, group 8. Register: no carrier until a project first enters pressure mode. The Considered line stays in the behaviors document as input for that build. So does the human prompt's "Why the LLM keeps the Chesterton's Fence log and the human reads it": it is the reason for the split between the LLM and the human, and the human prompt is switched off at changeover.

## Checks and reports

### B26. A check shows its work

Failures: a check states its verdict without showing its reasoning against the specific content, and the verdict is written before the scrutiny that would have produced it; a record reports a check's own success, and a step that certifies itself in the handover is one nobody downstream checks; a check reports on the content the session is attending to, not the content in front of it, and showing the work does not catch it (observed once, two symptoms; from the incubating file); a review step returns the same all-clear verdict at every run, so its result carries no information (observed: three consecutive close-outs of another RFM project, run on another model; from the rebuild session start).
Behavior: a check shows its reasoning against the content in front of it, not only a conclusion.
When: every run of a check.
Routing: Check yes (the shown work is the trace). Severe no. Search partly (verdict with no reasoning). Moment triggerable (a check runs).
Origin: tool pull.
Carriers: sweeps (each finding quotes the text; a sweep that finds nothing says what it read and never calls the document clean); file-write skill (the changed lines shown as they read on disk); always-on (look at the result before saying it is done, and say what was not checked).
Material:
> **[HL-CHKNARR] A check that states its verdict without showing its reasoning against the specific content did not run.**
>
> A pre-check drafted for a new Boundaries entry reported 'stands alone,' 'no defensive qualification,' 'clean,' while the draft itself carried the same defensive-citation pattern already identified and removed elsewhere in the same session. The verdict was written before the scrutiny that would have produced it. A check that outputs only a conclusion gives no evidence it was applied to the content in front of it, and produces none of the friction that would have caught this instance.
> **[HL-PCSKIP] A pre-check's "clean" verdict does not distinguish between the check being genuinely applied and missing something, and the check never being applied to the content at all.**
>
> An earlier skill load standing in for a fresh application of its check produced a verdict indistinguishable from a genuine pass: nothing shown to support it either way. Showing what a check found against the specific content, not its verdict alone, is what separates a real miss from a skipped check. This failure sits outside the three families this project's Failure Taxonomy currently defines, since it concerns whether a check ran at all, not where content sits, how it reads, or whether time will date it.
>
> This does not become a fourth Failure Taxonomy family. The three existing families divide by a property of the content itself, checkable from the document alone. This failure leaves no trace there: the document reads the same whether the check ran or not. No content-facing question could test it, so a fourth family would cost every derived artifact a question nothing could answer. Showing what the check found against the specific content is what closes the gap.
Source: TLR, Hard Lessons; `RFM_skill_drafting_reasoning.md`, Hard Lessons.
From the sweeps (`RFM_sweep_reasoning.md`, The Boundaries):
> **Not a quality gate that can be passed.** The sweep produces findings, not a score. Absence of findings signals either a well-curated document or a shallow sweep. The human cannot distinguish between the two without judging the sweep's depth independently. There is no clean sweep. The output is always findings for ruling, never a certification.
From session-closeout (`session-closeout/SKILL.md`, How to write the session file):
> ### The session file does not report whether a close-out step held
>
> Cut any clause that certifies a step's own success: "the gate held", "the check passed", "the review found nothing", "the map check was run twice, zero findings each time". A step that reports its own compliance inside the handover is a step nobody downstream will check, which is the same failure as reporting an edit as done without having looked at the file. Record what changed and what was decided.
>
> The exception is a step whose output is itself something the next session has to act on. "The check found three rows disagreeing with their headers, unfixed" is a finding. "The check found nothing" is a report card.
>
> This applies to the text already in the file, not only to new content. Any surviving clause of that shape comes out in the rewrite.
From session-closeout (`session-closeout/SKILL.md`, Close sequence, steps 5 and 7, the two places the skill says to report nothing):
> If an execution artifact that is deployed outside the project changed this session, name the deployment that now needs refreshing. Say nothing when none changed: a line reporting that nothing was deployed costs tokens every session and carries no information. A deployed copy sits outside the reach of every check the project runs on itself, so nothing else catches this.
> Say nothing when there was nothing to clear.
From the incubating file (`RFM_incubating.md`, entry X, a pre-check reporting on the content attended to):
> ## X. A pre-check reports on the content the session is attending to, not on the content in front of it.
>
> One draft, two symptoms. The Language question was reported as passing because the two terms being coined carried inline definitions, while two glossary-defined terms in the same paragraph carried neither definition nor pointer. The Structural question reported a finding, parent reasoning restated in a child, that corresponds to no type in the Failure Taxonomy, and then cleared it; the concern was invented and resolved inside a check that reports against a fixed list. `[R-SHOWCHECK]` does not reach either: content was shown against the check both times. Both were caught by the human. Candidate corrective: a reported hit names the taxonomy type it corresponds to, which would have refused the second and is silent about the first. Belongs with whatever resolves the Structural family's coverage.

From the rebuild session start (`rebuild_session_start.md`, earlier rebuild attempt, 2026-09-23, "Open", cross-project evidence):
> - Cross-project evidence the rules-review step at close-out doesn't discriminate. A separate RFM project, run on a different model (GPT-5.6 Terra), returned the same rules-review verdict across three consecutive close-outs: all rules match current practice, nothing obsolete, no edit needed. A review step that always passes carries no information, the same principle RFM_carrier_types.md states for external validation applied to an LLM-run check. The current session-close skill already instructs recording findings rather than compliance narration; this is that exact failure, unenforced, matching the self-enforcement gap already named HL-SELFENF in the unslop skill's reasoning doc. Relevant to the session-close skill's rebuild (already existing/modify in carrier_reassignment_scratch.md): the rules-review step needs to force stated evidence per rule, not a bare verdict.

### B34. Check claims about the set with a search that could contradict them

Failures: a claim about which documents carry or name something is asserted from memory; a grounding search built from the claim returns confirmation and cannot return a null; a pointer is accurate but written in different vocabulary from its target, a search in the pointer's terms finds nothing, and absence is concluded; a reasoning document rests on an unverified mechanical claim for several sessions because it reads as plausible; a count mismatch between two records is read as evidence of separate incidents without checking primary evidence; a candidate is called proven or reusable from the current session's impression rather than its history; a house convention is assumed instead of checked; a claim that a term is unprecedented, a pattern established or a reference stale is checked against current files, when the precedent sits in version history a text search does not reach; a count is taken from a file's own prose instead of counted, and every such total checked was wrong (as session-startup reports it, not checked); a state the LLM could read for itself is put to the human as a question; a search or check is assembled from recollection of a closed list and returns a plausible false finding; an operational document carries a script referencing files and commands that do not exist, and it reads as executable (observed; from the incubating file); the LLM states that a check, a trigger or a failure mode exists when no document holds it, and to the LLM stating it the claim reads as recall (reasoned; from the traveling prompt).
Behavior: run the search behind a claim about the set. Build grounding search terms from the break condition of the belief, not from the belief. Before concluding something is absent, search in the target's vocabulary, and write a pointer in its target's terms. Check a mechanical claim that reasoning rests on against a primary source. Check a candidate's history, and a local convention, against the record before relying on them.
When: making a claim about the document set; grounding a claim in outside evidence.
Routing: Check yes. Severe no. Search yes for claims about the set; no for the design of a grounding query. Moment unannounced.
Origin: any author.
Carriers: drafting skill (a claim about the set in written text; research inside drafting); research check (grounding searches for claims resting on outside evidence); always-on (conversation slice, through B51).
Material:
> **[HL-SETMEM] A claim about which documents carry or name something is asserted from memory, because it reads as a description of the set rather than as a claim about it.**
>
> The document set is searchable, so the check costs one search, and that is not what stops it being run. What stops it is that the sentence does not present itself as evidence-bearing. Two forms recur. Content is held to be unhomed when `RFM_map.md` already carries it in its own rows, which turns a separation into a fork where a subtraction was correct. And a hardcoded filename is held to be load-bearing because several documents name it, when those documents are outside the scope being reasoned about, which preserves a dependency for a reader who never receives it. Both assertions are usually right, and being usually right is what keeps them unchecked. The tell is a sentence that says how many documents do something with no search behind it. This is not `[HL-ENUM]`, where a list already written into a document goes stale as the set changes. Here nothing is written down: the set is reasoned about and never counted.
> **[HL-CFSRCH] A grounding search assembled from the claim returns confirmation and cannot return a null.**
>
> A module's central mechanism was grounded by searching for degradation, drift, instruction decay and lost in the middle. Every term presupposed the effect, so the pass returned work that had found it and no work that had not, and the result read as evidence rather than as the shape of the query. The document was written on a paper two years old testing a model three generations old, stated without qualification, and it passed the author's own review. The failure surfaced only when the human asked whether recency had been over-weighted, which is a question about a different bias, and answering it required going back to publication dates rather than to findings. Search terms for a grounding pass belong to the break condition of the belief being tested, not to the belief. A search assembled from the belief contains none of the words a contrary result would be written in, so finding no contrary result carries no information.
> **[HL-VOCGAP] A pointer between documents can be accurate and still undiscoverable, when the two sides don't share a vocabulary.**
>
> `RFM_handover_rules.md` pointed to `RFM_instruction_design_reasoning.md` for whether RFM specifies an artifact type for the files and skills that maintain the session boundary. The module had already answered the question in full: an assumption stating the boundary is permanent, not a platform limitation, and an open question naming exactly what remains undecided. Neither used the word the pointer was written around. The module spoke of carriers that load at the start of work; the pointer spoke of session handover. A search for the pointer's own subject across the project found nothing, and the natural conclusion was that the question had never been taken up. Both documents were correct read alone. The gap was between them, and nothing that reads one document at a time can catch it: not the structural sweep, which checks a document's own placement, not the language sweep, which checks a document's own prose, not a search, which only finds what it's told to look for. The fix was one clause naming the module's actual term inside the pointer, not a change to either document's substance.
> **[HL-PRIMCHK] A reasoning document can rest on an unverified mechanical claim for multiple sessions, because nothing forces a check against a primary source once the claim reads as plausible.**
>
> This document's carrier taxonomy treated a carrier's load point as governing whether an instruction reaches a later moment, which assumes content not resent leaves context. Nobody had checked that assumption against how the underlying API actually behaves. It surfaced only when a glossary draft compressed the reasoning to one parenthetical, "the traveling prompt presents once at the start of work", and that compression made the claim checkable in a way the fuller prose had not. Checked directly against Anthropic's documentation: the Messages API is stateless and resends the full conversation history on every turn, so presence was never the variable in question; what an instruction loses with distance is its hold, not its place in context. The prose had read as settled reasoning for several sessions without anyone opening a primary source to confirm the one claim it depended on.
> **[HL-TSDUP] A count mismatch between two entries reads as evidence of separate incidents, and commit-timestamp adjacency where one agent writes both is evidence against that, not noise.**
>
> `RFM_prompts_reasoning.md`'s Hard Lesson on co-author drift's ceiling failure and a carry-forward item's self-correction-lag entry described what turned out to be the same observation, one naming three files written in a pass, the other naming four. The mismatch alone was read as evidence the two entries tracked different incidents. What settled it was checking when each was committed: three seconds apart, across two separate repositories, both written by the same agent at the same close-out. An agent that commits on a human's behalf produces exactly that signature for two records of one realization captured back to back, and a wider gap for two records of genuinely separate events. The count was never checked against anything; the timing was, and only after being pointed at directly.
Source: TLR, Hard Lessons; `RFM_instruction_design_reasoning.md`, Hard Lessons; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I67. Check a candidate's actual history before calling it proven or reusable, not just the current session's impression of it.
> - I105. Check the actual local convention (e.g. git log) before drafting something that should match house style, rather than assuming a fixed one.
From the handover rules (`RFM_handover_rules.md`, Hold from the first message, [R-VERIFY]):
> - **[R-VERIFY]** Verify before asserting. Trigger: about to state anything about a document's contents, a file's current state, or whether an action completed. Action: check the artifact itself first. Failure shape: reporting a step as done, or a state as unchanged, from what the session did or from a tool reporting success, rather than from what the file now says. Also: asserting which documents contain, name, or depend on something, from a picture of the document set rather than from a search. Also: drafting content premised on something being new, unowned, or unresolved, from impression rather than from a search confirming it is absent. Also: ruling on or restating a carry-forward entry from its own wording rather than checking the documents it references. Also: asserting a term is unprecedented, a pattern is established, or a reference is stale from current file content alone, when the actual precedent sits in version history a text search won't surface. Being written down in a prior session is not verification.
Related: B51 carries the rest of [R-VERIFY] (I20).
From session-startup (`session-startup/SKILL.md`, Carry-forward count):
> ## Carry-forward count
>
> **Trigger:** session opens with a handover session file containing a Carry-forward heading.
>
> **Action:** Count the top-level bulleted entries under the Carry-forward heading directly in the file, using a mechanical count (grep or equivalent), not the number stated in the file's own prose. State the count found. If it exceeds ten, the session's first substantive work is contraction, per the handover rules file's carry-forward cap, before any new topic opens.
>
> **Failure shape:** stating the count carried over from the file's own narrative instead of counting the bulleted entries directly. This has recurred across sessions: a stated total was wrong by one or more in every case it was checked against an actual count.
From session-startup (`session-startup/SKILL.md`, Version verification at session open):
> **What not to do:** do not ask the user to confirm that a file is present. Read it and find out.
From the incubating file (`RFM_incubating.md`, entry T, a check assembled from recollection of a closed list):
> ## T. A check or search assembled from the model's own recollection of a closed list fails silently by producing a plausible finding.
>
> The close-out map check was written with a nine-value type list recalled rather than read, wrong in two places, and reported a finding against `RFM_operational.md`'s own type. Re-running with the list read from the file returned none. Second instance in the same session of building a search from a model of the source rather than the source, after Q.
From the incubating file (`RFM_incubating.md`, entry E, part: the fictional script):
> ## E. RFM translation to a new LLM environment fails predictably at the derivative chain
>
> A fictional bash script entered the operational document, referencing files and commands that do not exist. It reads as executable infrastructure. It is not.
Note (from the incubating file): the rest of entry E is in B2.
From the traveling prompt (`RFM_traveling_prompt_reasoning.md`, Chosen Direction, "Why a claimed rule is checked against the documents by the human, not the LLM"):
> **Why a claimed rule is checked against the documents by the human, not the LLM**
>
> An LLM can state that a check exists, a trigger fires, or a failure mode applies, when no document actually holds it. The invented rule takes the same form as every real one, a section, a trigger, a failure mode, so it reads as recall rather than invention to the LLM producing it. A prohibition on inventing rules would not catch this failure, because the LLM stating the rule does not experience itself as inventing one. That is why this check stays with the human. The LLM producing the claim has no signal telling it to verify this one, since nothing about producing it feels like invention. The human, reading the claim from outside, can compare it against the documents and see whether it is actually there.

### B38. Check output against what governs it when the output is produced

Failures: an LLM confirms a skill is loaded and violates it in the next response, more often in conversation than in deliberate drafting; a corrective pass run without reading the governing skill trades one failure for another (parentheses for em dashes) and passes the surface check; a draft is presented as ready and fails the checks that catch its faults, because those checks run only after the content is in the document; a session writes a commitment and does not apply it one turn later, because to its author it is a conclusion, not an instruction read; re-invoking an already-loaded skill by name returns a stub instead of its text, and the check that follows runs against the earlier presentation; a required check does not run because a sibling skill was loaded for a related job.
Behavior: check output against what governs it when the output is produced, from the governing text, not from memory of having loaded it. This holds for reasoning the session itself just wrote. Naming a loaded skill again does not re-present its text.
When: every output, deliberate drafting and conversation; the start of any corrective pass.
Routing: Check partly (the output can be read afterwards; the timing cannot). Severe no. Search partly (pattern failures such as em dashes). Moment triggerable per output; weakest in conversation.
Origin: tool pull (compliance narrated at load).
Carriers: file-write skill (for writes to a file, the em dash search on the lines written). Gaps, ruled in step 3: conversation, where no carrier reaches the moment of production; HL-AUTHLD, which only a re-read or the human catches.
Related: B26 carries HL-PCSKIP, where an earlier load stood in for applying the check. B39 carries the point of HL-NSWP's last sentence.
Material:
> **[HL-RLNA] Reading a constraint and holding it under production load are different.**
>
> An LLM confirms a skill is loaded, then violates it in the next response. The skill fires more reliably on deliberate drafting tasks than on conversational output. Compliance narrated at load time is not compliance at production time. The check must happen at the moment of output, not at the moment of loading.
> **[HL-RSGV] A corrective pass applied without reading the governing skill produces output that looks compliant and is not.**
>
> During an em-dash sweep, the default replacement was parentheses. The rfm-unslop skill explicitly flags parentheses as trading one AI tell for another. The error was not caught until the skill was consulted mid-session. The surface check passed. The deeper check failed. Any corrective pass on style, structure, or language must begin by reading the artifact that governs the failure class being corrected.
> **[HL-NSWP] Nothing checks a draft against the sweeps at the moment it is drafted.**
>
> A Chosen Direction entry was drafted for the top-level reasoning document and presented as ready. Checked afterward against the two sweep prompts, it failed three times: a procedure had leaked into an entry that carries only why, a claim about model behavior was written as settled when it rested on a single analysis, and the entry ran to three paragraphs where two carried the argument. The check ran only because the human asked for it. The drafting skill was loaded at the moment the entry was written, carries placement and section-type rules, and caught none of the three. The sweeps catch them by design and run only when invoked, which is after the content is already in the document. A draft that passes the checks that happened to run says nothing about the checks that did not.
> **[HL-AUTHLD] Reasoning written in a session does not bind the session that wrote it.**
>
> A session committed in writing to allocating instructions by two named properties, then proposed installing a check one turn later without applying either. Nothing re-reads a document between the moment a session writes into it and the moment that session acts next, so a commitment reaches its own author as a conclusion rather than as an instruction. That is the weakest form the commitment will ever have. Every later session meets it as document content read at session open, while the authoring session holds it only as something it happens to have concluded. The session most invested in a piece of reasoning is therefore the least reliable at applying it. This sits beside [HL-LOADPT], which governs where an artifact is loaded. This one governs the gap between writing and loading.
> **[HL-RELOAD] Re-invoking an already-loaded skill by name does not re-deliver its content.**
>
> A skill invoked once in a session and invoked again later by explicit name returned "already loaded above; instructions unchanged" instead of the skill's text. The check that followed ran against the earlier presentation, still present in context but not restated, rather than a fresh read. Whether unrestated content is followed as reliably as freshly presented content is a separate, still-open question; what this establishes is only that naming a skill again is not itself a mechanism for forcing a fresh restatement. The stub message, "already loaded above," carries the skill's content forward as a reference rather than restating it, the exact form `[OQ-INTV]` asks whether re-presentation must avoid to hold. Whether that form caused this specific failure, rather than the model treating the earlier presentation as still binding anyway, is untested.
Source: `RFM_skill_unslop_reasoning.md`, `RFM_skill_drafting_reasoning.md`, Hard Lessons; `RFM_instruction_design_reasoning.md`, Hard Lessons.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Assumptions):
> **[AS-DPIF] - Instruction adherence in derivation sessions cannot be assumed.** LLMs do not apply instructions uniformly: the same prompt may produce faithful execution in one session and inference-driven deviation in another, depending on factors neither party can fully observe or control. A derivation prompt that correctly specifies the posture does not guarantee the posture holds throughout the session. The confirmation gate is the only mechanism that surfaces deviation before it produces an unfaithful derivative. This assumption breaks if instruction adherence becomes reliably predictable, for instance if a mechanism is found that guarantees a session holds its posture throughout rather than only surfacing deviation after it has already occurred. The confirmation gate reduces the risk; it does not eliminate the uncertainty this assumption describes.
From the drafting skill (`RFM_skill_drafting_reasoning.md`, The Problem):
> RFM has two corrective mechanisms for document quality: the structural sweep and the language sweep. Both are after-the-fact passes. They catch failures that have already entered a document. The cost of correction scales with how much content was drafted before the sweep ran.
>
> The gap is at the moment of production. When drafting new content for a reasoning or operational document, the practitioner holds the argument in mind and writes. Section-type conventions, placement rules, and language discipline exist in separate documents. Under production load, they compete poorly with the drive to get the reasoning down. Structural misplacements and language failures enter at this moment and persist until a sweep finds them.
>
> Nothing currently fires at the moment of drafting to encode: where does this belong, what does this section require, and what does clean RFM prose look like.
From the handover rules (`RFM_handover_rules.md`, Hold from the first message, [R-PRECHECK]):
> - **[R-PRECHECK]** Trigger: about to show a draft of new content for a reasoning, operational, or glossary document. Action: run the `rfm-drafting` pre-check against that content and report it per `[R-SHOWCHECK]`, not a verdict alone. Once per draft, not once per session. Failure shape: the check does not run because a sibling skill was loaded for a related job, or because the skill was loaded earlier in the same session and the load reads as activation.

### B39. Credit a carrier only with what it has been seen to do

Failures: a rule that names its own invocation mechanism is credited with an activation nothing executes; a pattern list's clean pass is taken as evidence the prose is sound; a draft that passes the checks that happened to run is taken as passing the checks that did not; a gate is credited as held because its outcome matched what the human would have approved anyway; a carrier is judged on revisit from impression, because nothing recorded what was expected of it next to what happened (reasoned, not observed; from the posture gate raw notes).
Behavior: credit a carrier only with what it has been seen to do. A clean pass reports on what the check covers. A delivery counts when a step that performs it has run.
When: judging whether a carrier works; reading a check result.
Routing: Check yes. Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: always-on (look at the result before saying it is done); release trial, handed set only.
Related: HL-NSWP (in B38) ends on this point.
Material:
> **[HL-SELFENF] A rule that names its own invocation mechanism is not proof the mechanism runs.**
>
> This skill's Boundaries entry credited "the rules file and the handover carry-forward mechanism" with reliable activation. Nothing executed at session open actually read the rules file. The rule existed in writing. The skill still didn't fire, twice in the same session. The fix was not a stronger rule. It was adding an explicit step to session-startup that reads the rules file before producing any output. A rule that says to read something is not self-enforcing; only an executed step is.
> **[HL-PLCL] A pattern list catches the patterns on it, not bad writing in general.**
>
> Two drafts of a reasoning entry passed every check in this skill and were rejected on register. The failure was elevated diction with an abstraction as the sentence's subject: "a check that invites inference from silence licenses invention." No pattern named it, so both drafts came back clean, and human reading caught what the skill could not. The error was treating a clean pass as evidence the prose was sound. The list reports only on what it enumerates. When a new failure shows up in practice, add it as a pattern; until then, a clean pass says nothing about that failure.
Source: `RFM_skill_unslop_reasoning.md`, Hard Lessons; `RFM_instruction_design_reasoning.md`, Hard Lessons.
From the drafting skill (`RFM_skill_drafting_reasoning.md`, Chosen Direction, "Why the pre-check derives its own questions instead of running the sweep questions", second and third paragraphs; heading and first paragraph in B25):
> The second reason concerns what the practitioner believes afterwards. A pre-check carrying a question per section reads as a sweep. A draft that passes it feels swept, and the concentrated pass then feels redundant. `[HL-NSWP]` records the failure this check answers, and the check must not produce a larger version of it. One question per failure family keeps the pre-check visibly smaller than the pass it does not replace.
>
> The cost is that a question this coarse may catch nothing. That cost is accepted because it is visible: a check that finds nothing across sessions is evidence, and it can be sharpened against the failures it missed. A pre-check that displaces the sweep produces no evidence of having done so.
From session-closeout (`session-closeout/SKILL.md`, Close sequence, step 4):
> **4. Propose version bumps and document map updates**
> List only documents that changed this session. Propose bumps and map changes as your own recommended numbers, stated as a position, not a bare list of options to choose from. Wait for the user's ruling before executing. This step is a gate, not a formality. Landing on numbers the user would have approved anyway is not the same as the gate having held.

From the posture gate raw notes (`posture_gate_raw_session2.md`, earlier rebuild attempt, session 2, 2026-09-14, "THE ENTRY GATE", "Unplanned payoff"):
> ### Unplanned payoff: the gate generates its own evaluation data
>
> [The human]'s framing: experiment with this for 6-12 months, then revisit. Every frame statement is then a dated record of what we believed was settled, sitting next to what actually happened after. RFM currently has no evidence stream of that kind, so revisiting in a year would otherwise be revisiting from impression, which the methodology objects to everywhere else. Not designed in. Do not lose it.
Related: B5 (the note there: step 3 keeps no record of frames).


### B51. Report what was confirmed as confirmed

Failures: an action is reported done or a claim true without checking the actual output; asked, the LLM reports an inferred result as confirmed; a file read that returned only part of the file is treated as complete; a draft shown in chat, or an approved intention, is treated as text written; asserting that headers were checked stands in for quoting them; a rule agreed in conversation is recorded in the handover as added and is not in the file until a session later (observed, as rules-file-editing reports it); a line in a log of displaced reasoning is marked resolved and deleted before the content exists at its destination, which also deletes the record that anything was owed (observed once, caught a session later; from the rebuild session start; observed again in a later move of material, caught in the same session).
Behavior: before claiming something is done or true, check the actual output. Say which claims were confirmed and which were inferred. Only text that was actually written counts as written.
When: any report of an action or a state, both phases.
Routing: Check yes (the output can be compared afterwards). Severe no. Search partly (a quoted state against an asserted one). Moment triggerable (a report that something is done).
Origin: tool pull (narrating completion).
Carriers: always-on (confirmed or inferred, asked or not); file-write skill (the written text checked; a read a write depends on is complete).
Related: B26 (a verdict without shown work). B34 (claims about the set). B37 (HL-FLAGEX carries the deferral half of I85). B39 (credit a carrier only with what it was seen to do).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I20. Verify before asserting: check the actual output before claiming something is done or true.
> - I16. Honestly report whether an action was actually confirmed or only inferred, when asked.
> - I68. Confirm a file read returned every line before treating it as complete for anything load-bearing; re-view any skipped range first.
> - I79. Treat showing a draft in chat, and having an intention approved, as distinct from the text actually being written; only the rendered, shown text counts as drafted.
> - I85. Defer a version bump to close-out rather than performing it mid-session on reading a header-state instruction; quote the actual header line of every versioned document touched in a turn as it now stands on disk, since quoting some headers and asserting the rest were checked doesn't satisfy this, and being told to quote a header is not authorization to bump it.
Source: behavior inventory (earlier rebuild attempt).
From the handover rules (`RFM_handover_rules.md`, What this file is, Sentinel check):
> Sentinel check: this file ends with `[HRFM-EOF]`. If that marker is absent from a view of this file, the view was truncated. Re-view the missing range before treating the read as complete.
Note (from the handover rules): the sentinel is a mechanism for I68, an end marker whose absence shows a truncated read. Dropped at the file-write skill's build: it needs a mark in every file. The skill compares the lines read with the file's line count.
From rules-file-editing (`rules-file-editing/SKILL.md`, "After writing any edit: verify it is actually present"; one em dash replaced with a comma):
> **After writing any edit: verify it is actually present**
>
> After completing any edit to the rules file, grep the file for the added or changed rule's text and confirm the new wording is present before reporting the edit as done. Show the grep's actual output in the conversation, not just the conclusion that it succeeded.
>
> Failure this prevents: a rule approved in conversation and narrated in the session handover as added, while never actually written to the file. This has happened: content entered the session narrative one session before it entered the file itself. An edit reported as done without grep output shown is not done.
Note (from rules-file-editing): the record claiming the write is also a record certifying its own success (B26). What is new here is the lag of a session before the gap was found. Decided at the file-write skill's build: the read-back after a write is the file-write skill's; the record certifying its own success is the close skill's.

From the rebuild session start (`rebuild_session_start.md`, earlier rebuild attempt, 2026-09-23, "Open", derivation prompt reasoning doc):
> - Derivation prompt reasoning doc: carrier closed. Three Chosen Direction entries (coverage-check ordering, traceability vs. quality comparison, no-looping) written -- these resolve three removal_log lines that a prior session had marked resolved and deleted before the content actually existed in the document, a process gap caught and fixed this session. Operational doc's dangling pointer to the missing content removed. Versions v0.8.0/v0.5.1, committed 0f6ecd9. Pre-existing wording leftovers (open question on agentic settings pointing at a cut entry, open question on gate reliability missing its sibling, Landscape missing its guiding question, sibling-scope gate needing a home) were not re-checked against this closure.

---

## Sessions

### B16. Review the collaboration, refuse most candidates

Failures: working failures repeat every session while the documents look fine; or every observed pattern becomes a rule and adherence to all rules falls; a candidate that is real but not ready is discarded together with the ones that are nothing, and the discard ends its record; a one-session exception granted by the human is carried forward as if it were the standing rule (reasoned, not observed); the review records only what went wrong, so the record gathers warnings and never tools (stated by session-closeout, no incident recorded); a problem caused by the environment (a tool, a transfer, the file system) is either written into the methodology documents as a lesson or not recorded at all, and is worked around again in a later session (stated by session-closeout, no incident recorded); the holding file for environment problems records a recurring problem as a new entry each time instead of raising the count on the existing one (a stale git lock recorded five times, a blocked push three times), so no count passes 2, the promotion rule never fires, and later sessions work the fix out again (observed; from the technical environment notes); a red team aimed at what the session produced does not reach how the session conducted itself (observed once; from the incubating file); a failure is diagnosed as carelessness when the act was scored under the wrong posture, so the fix targets care instead of posture (reasoned, not observed; from the posture gate raw notes); rules gain conditions, exceptions and coverage for cases that have not happened, because writing more feels like rigor (stated as the diagnosis of the old corpus, no incident recorded; from the rebuild session start); a rule rarely edited sits unchanged while the practice it describes moves on (stated by rules-file-editing, no incident recorded).
Behavior: at session end the collaboration reviews its own conduct; a few patterns become rules or lessons, most are refused. General-looking patterns go to the methodology project, not into local edits of RFM. A candidate that changes no carrier now is dropped, and a recurrence brings it back. The exception is an observed failure or constraint that no carrier can act on now and that a session deciding in its document needs to know; it becomes a Hard Lesson.
When: session end.
Routing: Check partly (that the review ran; not whether the refusals were right). Severe no. Search partly (review record present). Moment triggerable.
Origin: any author for the review; tool pull for over-promotion.
Carriers: close skill; working agreements file.
Source: TLR, "Why RFM carries a curated improvement loop"; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I66. Distinguish discarding a candidate because it's nothing from discarding it because it's real but not ready; route the latter to a holding file and say where, rather than letting the discard end its record.

From the map (`RFM_map.md`, Document Map, row for `RFM_incubating.md`):
> | `RFM_incubating.md` | `top_level_artifact` | unversioned | stays | Ideas captured at session close that are not yet ready to enter a document |
From instruction design (`RFM_instruction_design_reasoning.md`, Chosen Direction, "Why each carrier has a fixed capacity"):
> **Why each carrier has a fixed capacity**
>
> Allocation decides where a behaviour goes. It does not decide what leaves. Under allocation alone, RFM's own always-on prompt and standing rule set grew steadily and never contracted, while the one carrier holding a stated maximum, the list of unfinished threads handed from one session to the next, stayed at its number.
>
> A cap changes what a session argues about. Without one, each candidate is judged alone, and a behaviour with a real incident behind it survives that judgment every time. With one, a full carrier takes a new behaviour only by displacing a named one. Which of two behaviours earns the slot is a question a session can answer. Whether a behaviour is worth having is not, and that is the question that was always answered yes.
>
> A carrier is capped when its cost is paid by every session rather than by the session that consults it. A carrier read only when someone goes looking charges its growth to that reader alone, and takes a test in place of a number: an entry names a trigger and an action, and content that fails the test is reasoning sitting in the wrong document.
From the handover rules (`RFM_handover_rules.md`, What this file is, Precedence):
> Precedence: when this file and the session file appear to disagree, this file governs. If the session narrative describes a departure from a rule here, surface it to [the human] explicitly. A one-session exception granted by [the human] does not change the standing rule; if the exception should become the rule, the close sequence graduation check catches that.
From the handover rules (`RFM_handover_rules.md`, Hold at the relevant moment, [R-CARRYCAP]):
> - **[R-CARRYCAP]** Trigger: session opens. Action: count the top-level entries under the handover session file's Carry-forward heading. Entries there are bold-lead paragraphs, not bullets; a count returning zero means the wrong pattern was matched, not an empty backlog. If the count exceeds 10, the session's first substantive work is contracting, closing, merging, or executing entries until the count is at or below 10. If any entry was tagged quick at the immediately preceding close-out, address, execute, or explicitly re-defer it with a stated reason before opening a new topic, regardless of count. Either condition: no new topic opens without explicit agreement from both co-authors. Failure shape: opening a new topic while the count exceeds 10, or while a quick-tagged entry from last close sits untouched, on the reasoning that the new topic feels more urgent. This applies equally to a thread that opens as direct fallout from an in-session incident, not only a discretionary topic choice; the effect on carry-forward count is the same either way.
Note (from the handover rules): [R-CARRYCAP] is the capped carrier the capacity argument above cites. HL-BLOCKRES (B30) is the failure observed under it.
From the handover session file (`RFM_handover_session.md`, 2026-09-14, What was settled):
> **The numbers: always-on prompt 7, standing rules 10, installed skills 10.** They are not in any document, because writing per-carrier numbers into a reasoning document means naming the carriers, which is the member-naming form the count-dependent rule bars. They belong to the register and the register does not exist. The skill number came from counting the skills actually needed (session start, session close, drafting, ripple check, unslop, verify execution, rules-file editing, so seven) and leaving three slots for what falls out of the standing rules when it goes from 22 to 10. Those three are committed in advance, not spare.
From the handover session file (`RFM_handover_session.md`, 2026-09-14, Carry-forward):
> **Redesign the startup and closeout machinery.** Both have become heavy and need to get lean, held inside a reasoning document rather than accumulated in skills. Understood: this session skipped the rules review deliberately, because its entire output is which rules to keep, merge or cut, and the sort decides that from a criterion that did not exist before tonight. Skipping it cost nothing, which is evidence about the sequence. Tried: nothing structural, two consecutive sessions of ad hoc skipping. Open: what the sequence is actually for, and whether its steps belong in a reasoning document at all. Stopped because it is the same class of work as the sort and should follow it rather than precede it. Heavy.
From the handover session file (`RFM_handover_session.md`, 2026-09-14, Carry-forward):
> **The learning loop.** RFM captures observations well and has no way to let them go: the incubating file keeps growing, carry-forward sat at its cap for several sessions, and the close-out procedure demands a stated position on every candidate it notices. Understood: the five levers with do-nothing as the default price the entry, and a cap per carrier prices the holding, and the cap half is now settled with numbers. What is untested is whether a default of nothing loses insights that arrive early, since the em dash lesson took nine sightings before it earned a check. Tried: the caps, this session. Open: whether this is one mechanism with Regrounding or a different one. Regrounding starts from a caught failure and traces back to the reasoning; the learning loop governs the far larger volume of observations that never become failures. Stopped because the register holds the cap and does not exist yet. Heavy.
From session-closeout (`session-closeout/SKILL.md`, Close sequence, step 1):
> **1. Hard lessons, open questions, and working mechanisms**
> State your view: what this session produced that warrants a new Hard Lesson or standing open question, what does not, and what decided each. Reach a position on every candidate you noticed, including the ones you discard, and say what discarded them.
>
> Also state your view on the reverse: what mechanism this session relied on held up well enough to be a candidate for deliberate reuse against a different target behavior, not just for the record. Check its actual history before naming it a candidate, not just this session's impression, the same discipline this file already asks for elsewhere. A mechanism proving itself once is a session event, not a candidate; say so and discard it the same way a single Hard Lesson candidate gets discarded.
>
> A discarded candidate is not the same as a discarded observation. When a candidate is discarded because it is real but not yet ready, one incident, a mechanism seen once, a signal worth tracking, route it to wherever the project keeps that holding ground (an incubating file or equivalent) rather than letting the discard end its record. Say where it was routed. Discard without routing only when the candidate itself turns out to be nothing, not when it is simply too early.
>
> Failure shape: listing candidates with their merits and asking which the user wants written. That is a menu. It hands back the judgment this step exists to make, and it drops every candidate the user does not pick. A candidate you are unsure about is still a position: say which way you lean and what would change it. A second failure shape specific to working mechanisms: reporting only what went wrong this session and never what held up, so the record accumulates warnings and never accumulates tools. A third failure shape: discarding a candidate as premature rather than wrong, and closing it out with no destination, so the observation exists only in this session's transcript and is gone once the session ends.
From session-closeout (`session-closeout/SKILL.md`, Close sequence, step 1a):
> **1a. Technical environment check**
> Separately from the methodology content above, check for technical environment issues: something in this session that went wrong, or had to be worked around, because of the compute environment itself, a tool's behavior, a transfer method, a filesystem quirk, not because of RFM's reasoning or documents. State plainly whether anything like this happened and what it was.
>
> This is not RFM content and does not go through the same routing as a Hard Lesson or working mechanism. Route a real candidate to the project's private technical-environment notes file, the same incubating treatment given to any not-yet-ready observation: captured for future time and token savings, not yet a pattern. Discard only when nothing of the kind occurred this session, not because a single incident seems too minor to mention.
>
> Failure shape: folding this into step 1's Hard Lesson question, which sends tooling noise into the methodology's own document set. Failure shape: skipping this check because nothing comes to mind immediately; check the actual session transcript for a workaround or retry before concluding nothing happened.
From the incubating file (`RFM_incubating.md`, "What this file is" and footer):
> ## What this file is
>
> This file is public because transparency about work-in-progress is consistent with RFM's own principles. If you are encountering RFM for the first time, start with the README and `RFM_top_level_reasoning.md`; this file shows the methodology's thinking-in-progress, not its conclusions.
>
> These are ideas that surfaced during a refining session but are not sharp enough yet to capture in the methodology documents. They are candidates, not conclusions. Read this file into a future session when the topic feels relevant.
>
> **On signal counts:** each entry carries a signal count: the number of independent observations from distinct contexts (different LLMs, different domains, different problem types) that have surfaced the same idea. Repetition within the same session or LLM does not increment the count. Multiple independent signals on the same candidate should trigger a document home conversation. Two independent contexts is sufficient to propose; three should trigger action regardless.
>
> *Not versioned. This is a working note, not a methodology artifact.*
> *Discard once the ideas have found their home or been consciously dismissed.*
Note (from the incubating file): observed in the file, no entry carries a signal count above 1, and from entry P on entries carry no count, no reason for holding and no possible home. The promotion rule in the header never fired. BB and CC reached the working file through the handover session file, not through the rule.
From the incubating file (`RFM_incubating.md`, entry M, red team aimed at the session's own conduct):
> ## M. Red team aimed at the session's own conduct rather than its content
>
> The human asked for a red team of the session's thinking at the point the drafting was finished. Three of the four findings were about the reasoning just written. The fourth was that the session had executed a removal without ruling graduation against expiry, which is a procedural violation by the model rather than a flaw in any document. That finding is the one that produced a fix in the same session. The candidate is that pointing a red team at how the session conducted itself, not only at what it produced, reaches failures no content review asks about.
>
> **Why not captured yet:** one occurrence. The prior session's red team was checked before naming this a pattern; it was aimed at the plan's content, and the self-correction in it was about a finding rather than about conduct. So there is no second instance.
>
> **Possible home when ready:** `RFM_sweep_reasoning.md`, if it turns out to be a distinct sweep target, or the traveling prompt if it belongs as an ambient posture at the end of drafting.
>
> **Signal count: 1** *(this session, RFM-on-RFM work)*

From the posture gate raw notes (`posture_gate_raw_session2.md`, earlier rebuild attempt, session 2, 2026-09-14, "THE MAIN IDEA", secondary payoff):
> Secondary payoff: failures I would diagnose as carelessness are often posture mismatch. I was scoring myself under the wrong posture for that act.

From the rebuild session start (`rebuild_session_start.md`, earlier rebuild attempt, 2026-09-23, "Why this exists"):
> RFM was built using RFM. The traveling prompt and this project's system prompt were the same text. That text held real thinking built over months, and it also accumulated compulsive precision: rules with conditions and exceptions, coverage for edge cases that haven't happened, machinery that grew because writing more felt like rigor. The corpus is not being thrown out. Most of it was earned. The problem is that it was never built with the shape chosen on purpose, and reading it in full anchors any session toward extending it the same way.

### B27. End the session before it drifts

Failures: over a long conversation the LLM drifts toward ideas, framings and connections from that conversation that were never decided; the drift is invisible from inside; a fresh read of a document that compresses its source produces a confident objection instead of a visible gap, so the test fails and nothing reports it (observed, three fresh reads; from the incubating file); eleven sessions in two days, alongside a confident but wrong diagnosis in the same stretch (one co-occurrence, cause not established; B27 is the nearest section, since it covers drift within a session, not pace across sessions; from the rebuild session start).
Behavior: keep a session to one piece of work and stop at the signs of drift. Test the documents by opening a fresh session with only the documents as context; what the fresh session misunderstands is a gap in the documents.
When: during and at the end of every session; the fresh-session test at chosen points.
Routing: Check partly (the fresh session shows gaps). Severe no. Search no. Moment unannounced for drift; triggerable for the fresh-session test.
Origin: any author.
Carriers: human guide (frustration and energy: the human says so or stops); release preparation (one piece of work per session); fresh-context subagent test.
Related: B1, B11 and B18 carry the first mitigation in HL-LCAD (documents complete enough to onboard a fresh LLM).
Material:
> **[HL-LCAD] Long conversations with LLMs accumulate drift.**
>
> Even a disciplined LLM develops bias over a long conversation: toward ideas that emerged in that conversation, toward framings that felt productive, toward connections that feel natural but weren't explicitly decided. This is subtle and hard to detect from inside the conversation. Drift is more dangerous than context window limits: it is invisible and cumulative. Two mitigations: first, the reasoning document should be complete enough to onboard a fresh LLM without loss; if it can't, the document isn't finished. Second, deliberately starting a new conversation with only the reasoning document as context is a useful quality check. A fresh LLM that misunderstands the direction reveals a gap in the document, not a gap in the conversation.
From the rebuild plan (memory):
> One piece of work per session: one step for steps 1 and 3, one failure source in step 2, one subject in step 4 (two if small), one carrier in step 7. Stop at the end of that piece, even if it went quickly. Stop earlier if the LLM gets something agreed earlier in the session wrong or asks about it again, if its replies get longer, more formal or grander, or if "look at, not follow" is needed more than once. The LLM says when it thinks a natural stopping point has come.
Source: TLR, Hard Lessons; `RFM_rebuild_plan.md`, How we work.
From the incubating file (`RFM_incubating.md`, entry AA, the same wrong objection in every fresh reader):
> ## AA. A reasoning document that compresses its source reproduces the same wrong objection in every fresh reader.
>
> Three independent fresh reads of `RFM_instruction_design_reasoning.md`'s Chosen Direction produced the same two objections to the posture-transition axis: that two crossings cannot home 55 behaviours, and that binding conditions return to do allocation. Both are answered in a private session record, which the document does not carry. The traveling prompt names a fresh LLM reading only the documents as RFM's own quality check. That check has now run three times and failed three times, and nothing reported it, because a fresh read produces a confident objection rather than a gap. The response is not a new instruction but a move: the raw reasoning goes into the document, already scheduled. Captured because the pattern is about compression generally, not about this one document. First instance.
Note (from the incubating file): the compression half of this entry is covered by B40, through the handover session file's warning 3.

From the rebuild session start (`rebuild_session_start.md`, earlier rebuild attempt, 2026-09-23, "Parked", cadence spike):
> - Cadence spike: 11 sessions in 2 days near the end of the previous attempt, next to a recorded confident-but-wrong diagnosis in the handover log. A hard-lesson candidate about session pressure. Address once hard lessons are addressed.

### B30. Leave carried-over items open for the next session

Failures: a parked item rots at the session boundary because a fresh task pulls harder than a paragraph from another session; a deferred item that names its owner is read as ruled; a stated dependency between open questions is read as an order of work; contraction work removes waiting items (on a second occurrence, a dependency, a trigger) together with resolved ones, because both read as nothing to do now; a deferred item carries its topic but not its context, and the next session reopens it cold, which recurred after the lesson was written; content the next session needs sits where a fresh instance skims past it (stated by session-closeout, no incident recorded).
Behavior: decide an unclear item now or drop it; list only what blocks progress. A carried-over item states the gap, not where the fix goes, and says whether anything waits on it. A deferred item carries enough context for a fresh session to proceed without reconstruction. An item is resolved only if it needs no tracking when nobody looks at it again. An item waiting on a condition (a second occurrence, a dependency, a trigger) is carried only if it names the condition that ends the wait and nothing else would bring it back when the condition comes.
When: session end; writing an open question or deferred item.
Routing: Check partly. Severe no. Search partly (items still listed). Moment triggerable at session end.
Origin: any author.
Carriers: close skill (writes each item and applies the bar); handover file (carries the items across the session boundary); session open skill (reads the file and restates the carried items).
Settled: under the bar the human set in step 3 (carry an item only if it will surely be fixed), an item waiting on a real condition would be dropped (HL-BLOCKRES). For dropping it: a failure that leaves evidence comes back on its own when it recurs. Against: a condition nothing else watches, or a co-author failure that leaves no trace, is lost once dropped. So a waiting item stays only if it names the condition that ends the wait and nothing else would bring it back when the condition comes.
Material:
> **[HL-PARKROT] A deferred item rots at the session boundary, not from a missing check.**
>
> A session parks an item when its own confidence in resolving it right now is low, which is the correct reason to stop rather than push a fix through on shaky footing. The next session opens with confidence restored and a new request already in view, and the parked item does not compete for attention on equal terms: a fresh task pulls the model in, a paragraph written by a different session does not. An item already resolved can sit unremoved for sessions. A separate item's factual claim can stop matching the documents it describes. Both survive because nothing forces a look at either until a count threshold trips. A count threshold catches volume. It does not catch one item going stale early.
> **[HL-DEFOWN] A deferred item that names its owner is read by the next session as having ruled on it.**
>
> An item deferred at the end of one session recorded that the sweep prompts might need a replacement entry condition, and named the check to put in them. The gap was real. The placement was a design decision no session had ruled. The next session opened the item and began drafting into the sweep module, because an item that arrives with a destination presents the destination as part of the problem rather than as the first thing to decide. The check belonged in the operational document that installs with the methodology, and the sweeps took no entry condition at all. A deferred item states the gap; where the fix goes is work the receiving session has to do.
> **[HL-OQGATE] A stated dependency between two Open Questions is read as an order of work.**
>
> One entry closed by saying it could not be settled while another remained open. The dependency was accurate and the entry claimed nothing about priority. It did not need to. A session deciding what to work on finds the only sequencing claim in the section and follows it, so the wording set the agenda, and the work that followed was measurement of a quantity that did not need measuring. Say what one question needs from another, and say whether anything actually waits on it.
> **[HL-BLOCKRES] Contraction work conflates "nothing to do now" with "resolved."**
>
> Closing carry-forward items to satisfy `[R-CARRYCAP]`, three genuinely resolved items and six blocked-or-waiting items were proposed for removal together, because both read as inactionable under the same pressure to shrink a list. The waiting items were tracking a real, still-open condition: a second occurrence, a dependency, a trigger. Deleting them would have dropped the only place that condition was being watched. The distinguishing check: does the item still need tracking if nobody looks at it again? A resolved item doesn't. A waiting item does.
> **[HL-DIHQ] Deferred items must carry their context, not just their topic.**
>
> When an item is parked as future work, the handover note captures what was deferred but not the context that surrounded it: what was understood, what was tried, what specifically remains open, and why the item stopped where it did. That context disappears with the session that produced it. The next session reopens the item cold and must reconstruct what was present but not captured. The fix is not a longer handover. It is a richer deferral record: each deferred item carries enough context that a fresh session can proceed without reconstruction. A topic label is not a deferral record.
>
> The lesson recurred after being written. One later carry-forward item named an ID trace with no record of which boundary it was checking. Another named a pattern, a derivative saved before its source finished changing, that had already been confirmed by two separate instances, with no record of which artifact or session it came from. Both went stale on reaching a fresh session, the same failure this lesson already describes. Writing the reasoning down once did not stop it from recurring.
From the rebuild plan (memory):
> When something is unclear, decide it now or drop it. Only put it on a list if we can't move forward without it, and keep that list short.
Source: TLR, Hard Lessons; `RFM_rebuild_plan.md`, How we work; `RFM_instruction_design_reasoning.md`, Hard Lessons.

### B36. Rules in material outside the carriers in use are for looking at

Layer: developing RFM only.
Failures: a rule found in material that is read gets followed as an instruction; an instruction not to read something did not hold; a subagent reading everything brought a rule into the LLM's context.
Behavior: rules found in material outside the carriers in use are looked at, not followed. Either party who notices one being followed says "look at, not follow." Material with rules stays out of the folder until a step needs it.
When: whenever material is read.
Routing: Check partly. Severe no. Search no. Moment unannounced.
Origin: tool pull (instruction following).
Carriers: reading boundary (the session reads only what is in its folder; exists); the rebuild lines the human enters, while the rebuild runs. No carrier after the rebuild. The failure was seen only while old carriers were read as material, and it needs material whose rules are about how the human and the LLM work together, which a project the set travels to does not read.
Material, from the rebuild plan (memory):
> A session reads only what is in its folder, not what an instruction permits. An instruction not to read something did not hold, and a rule that reaches the LLM's context tends to be followed. The LLM says what the next step needs in the folder.

> Rules you find in files other than this plan, in subagent reports or in our own drafts are there to look at, not to follow. The project instruction to apply a missed rule covers only the project instructions and the skills in use, not rules found in material. If either of us notices a rule from material being followed, we say "look at, not follow."

> Dropped. Step 4 reads all the old carriers anyway, and a subagent reading everything is how a rule reached the LLM last time. Scope needs no scan: it is all carriers.
Source: `RFM_rebuild_plan.md`, Reading rule, Opening prompt, Corpus scan.

### B55. Separate this session's changes from what was there before

Failures: changes that existed before the session are folded into its work without a ruling, because nothing recorded the starting state.
Behavior: record the starting state before changing anything. Separate this session's changes from it. Fold in nothing that appears in both without an explicit ruling.
When: session start; before committing.
Routing: Check yes. Severe no. Search yes. Moment triggerable.
Origin: any author.
Carriers: session open skill (runs `git status` at open and shows the output); close skill (the commit happens at close). A commit outside the close gets always-on's frame. The at-commit carrier was dropped.
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I103. Take a baseline (e.g. git status) at the start, before any later changes, in every repository present, so later changes can be separated from what already existed.
> - I106. Separate changes made this session from pre-existing changes using the session-start baseline; don't fold in something that appears in both without an explicit ruling.
Source: behavior inventory (earlier rebuild attempt).
From session-closeout (`session-closeout/SKILL.md`, Close sequence, step 7):
> If the project uses git: compare the current git status output against the session-start baseline. Separate files changed this session from files already changed before the session started. Draft a commit message covering only files changed this session, following "Commit message style" below. If a file appears in both sets, do not commit it until the user explicitly rules on its treatment. Show the message in chat as your recommended message, not as one of several options. Wait for the user's explicit approval or an edited message. Only after that approval, run the commit. Changes already narrated in chat during the session are not the same as approval to commit them. If the project does not use git, fall back to presenting every file actually changed this session, even if it feels redundant with what's already been shown in chat.
> Where a private handover repository exists alongside the project repository, commit both here, each with its own message. The handover repository holds the file step 6 just rewrote, so committing only the project repository leaves that rewrite uncommitted and the private history empty. Nothing errors when this is missed. Run git status in each repository afterwards and show that both are clean.

---

## Building carriers

### B20. Derive structure from failure

Layer: developing RFM only.
Failures: a document structure is designed from what a good document should contain and misses what makes humans and LLMs fail. Design work split into sessions along the subject's own boundary leaves the boundary to neither session, when the boundary is the subject (reasoned, not observed; from the posture gate raw notes).
Behavior: when designing a document structure or a set of sections, ask what makes humans and LLMs fail and derive the structure from that.
When: designing or changing a structure.
Routing: Check no. Severe no. Search no. Moment triggerable (a structure is being designed).
Origin: any author.
Carriers: carriers reasoning.
Material:
> **[HL-DFMD] The document structure emerged from failure modes, not from best practices.**
>
> The most robust design decision in the methodology was to derive the eight sections by asking "what causes humans and LLMs to fail?" rather than "what should a good document contain?" Designing from failure is more rigorous than designing from aspiration. This principle should be applied recursively, to every module document that follows.
Source: TLR, Hard Lessons.

From the posture gate raw notes (`posture_gate_raw_session2.md`, earlier rebuild attempt, session 2, 2026-09-14, "Session-shape view"):
> ## Session-shape view
>
> Do not split into a co-author session and an execution session. Each would design its half well and the boundary would belong to neither, while the boundary is the subject matter. What can split off is inventory work: behaviours walked once per posture is collection, not design.

### B25. Build a check against the failure it counters

Layer: developing RFM only.
Failures: a check derived from a failure type tests something adjacent to what the type says; a check scoped to the whole backlog costs more as the backlog grows and gets skipped under pressure; a question derived faithfully from its source lands in a sibling carrier whose job it is not, and the derivation checks pass it because they test grounding, not which carrier's job it serves; a check is aimed at the failure that can be detected (an empty cell) rather than the one that occurs (a plausible value filled by a session that never had the reasoning); a convention with no search behind it drifts while one with a search holds; a failure class that no derived question reaches is not in force, and a class added or changed without updating the derived questions reaches no check; an absence check with no named qualifying condition asks the reviewer to infer from silence, and the reviewer invents findings; a check carried in prose and re-implemented at each run misfires differently each time (observed, five close-outs, five bugs); a finding that meets two failure families is filed under the later one and the draft reads as passed (observed once; from the incubating file).
Behavior: read a derived check back against the failure type it derives from, not only against the content it will run on. Scope it to what changed since it last ran. Check that each derived question belongs to this carrier's job and not a sibling's. Aim a check at the failure that occurs, not at what is easy to detect; where no check reaches it, put the decision where a session notices it is missing. A convention that reduces to a search gets the search; one that does not is guidance. An absence check runs only against a named qualifying condition.
When: building or changing a check.
Routing: Check partly. Severe no. Search no. Moment triggerable (a check is being built).
Origin: any author.
Carriers: carriers reasoning.
Material:
> **[HL-ADJCHK] A failure type named correctly in the taxonomy still fires, when the checks derived from it test something adjacent to what the type says.**
>
> The language family names text written for the session that produced it rather than for a future reader. The drafting pre-check derived from that family asked whether a reader outside the session would understand the content. A sentence explaining why a section was left out passes that question. A later reader understands it, and it is still addressed to the person reviewing the draft rather than the person reading the document. Comprehension was tested where audience was the failure. A derived check has to be read back against the type it derives from, not only against the content it will run on.
> **[HL-COSTSCALE] A check's cost should scale with what changed, not with what already exists.**
>
> A rule can be enforceable, in the sense that it reduces to a search. It can still be badly scoped, in the sense that the search runs across an entire backlog before any item in it can be acted on. That cost grows with the size of the backlog the rule exists to manage, so the rule gets more expensive exactly as the problem it is protecting against gets larger. The corrected version checks only what changed since the rule last ran, the newest entry, the newest claim, not the accumulated total. A cheap check gets run under pressure. An expensive one gets skipped, which is precisely when a check is needed most.
> **[HL-CMDV] Contamination between sibling sweep prompts, one doing the other's job, is invisible to the standard derivation checks.**
>
> The confirmation gate verifies fidelity to source. The coverage check verifies nothing from a prior version was lost without tracing back to source. Neither check is built to catch a question that is faithfully derived from source and still wrong for the artifact it ends up in: a structural question rendered into the language sweep prompt, or the reverse. Both checks ask whether content is grounded, not whether it is grounded in the right artifact's job.
>
> This is `[AS-SWDJ]` breaking quietly rather than obviously. The assumption states that each sweep's job needs attention the other's presence would divert. A single misplaced question does not look like a foreign sweep prompt has appeared inside the current one. It looks like one clean sentence, sourced correctly, sitting where it does not belong. The dilution `[AS-SWDJ]` warns against does not require the two jobs to merge completely: one sentence in the wrong register is sufficient to reintroduce the failure the job-separation design exists to prevent.
> **[HL-UNCHK] A convention that nothing checks drifts, however plainly it is stated.**
>
> A writer drafting inside a document works from what is in front of them and from the nearest existing example. A convention held in another document only reaches that moment if the writer goes and reads it. When the nearest example already departs from the convention, the departure is what gets copied, and nothing errors at any point.
>
> `RFM_operational.md` carries two conventions of the same kind. Em dashes are barred, with a grep behind the rule that runs before every write. Chosen Direction headings were specified without a trailing colon, with no check behind them. Measured together, the em dash count across the project was zero and the heading violations were fifty-two, spread over five documents including the top-level reasoning document.
>
> The split between the two is `[AS-SRCH]`: a convention that reduces to a search gets the search, and one that does not is guidance wearing a convention's name.
> **[HL-CHKAIM] A check is aimed at the failure that can be detected rather than the failure that occurs.**
>
> When the Travels column was added to `RFM_map.md`, the check first written for it tested whether a row's cell was filled. An empty cell almost never happens, because a session adding a row sees the gap in the table it is typing. What happens is a cell filled plausibly by a session that never had the reasoning the value records, and a completeness check passes that silently. Detectability selects the target: absence can be found by search and a wrong ruling cannot, so the check that is writable displaces the check that is needed. The result costs maintenance every session and catches nothing. The fix was not a better check but a sentence beside the column saying the value is a ruling rather than a judgment made while editing, which puts the decision where a session notices it is missing. This is not the neighbouring failure where a check derived from a named failure type asks about something adjacent to what the type says. Here no failure type is consulted: detectability chooses the target.
From the Failure Taxonomy (`RFM_operational.md`), opening paragraph:
> This section is the single source for the failure classes RFM recognizes. Both arms retrieve from here: the sweep prompts through `RFM_sweep_operational.md`, and the drafting-moment check through the drafting skill. Neither restates the classes in its own words. Each derives its own questions from them. Adding or changing a class here is not complete until each arm's derived questions have been updated to reach it. A class that no arm asks about is not in force.

From the Failure Taxonomy (`RFM_operational.md`), boundary paragraph:
> **Boundary between the families.** A failure is structural when it concerns where content sits. A failure is language when it concerns how content reads. A failure is lifespan when the content sits correctly and reads clearly today and planned work will make it false or redundant. A well-written sentence in the wrong section is structural. A correctly placed sentence carrying session residue is language. A correctly placed, clearly written sentence describing a condition already scheduled for removal is lifespan. A conditional whose trigger is uncertain is not a lifespan failure, because no plan holds that condition and the document is the only place it is recorded. When a failure meets more than one description, the artifact that invoked the taxonomy applies its own ordering rule; the sweep ordering is in `RFM_sweep_operational.md`.
Source: TLR, Hard Lessons; `RFM_sweep_reasoning.md`, Hard Lessons; `RFM_instruction_design_reasoning.md`, Hard Lessons; `RFM_operational.md`, Failure Taxonomy; behavior inventory (earlier rebuild attempt).
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I55. Apply an absence check only against a named qualifying condition, not against open-ended inference from silence.
From the sweeps (`RFM_sweep_reasoning.md`, Chosen Direction, relational check):
> **Why the reasoning-to-operational check is relational, not inward-reading**
>
> The structural sweep asks whether a document coheres with itself. The language sweep asks whether its expression is clean. Both read inward. The reasoning-to-operational check asks whether two documents together are sufficient to produce the derivative without the LLM inventing content. That question cannot be answered by reading either document alone. It requires holding both simultaneously and checking what passes between them. This is a different cognitive job, which is why it cannot be folded into either existing sweep without losing the check that only the relational pass performs.
From the sweeps (`RFM_sweep_operational.md`, Grey zone rule; completes the boundary paragraph's pointer to the sweep ordering):
> When a failure is both positional and about wording, the positional dimension must be ruled on before the language dimension is assessed. The structural sweep flags it as a grey zone, names both failure types, and proposes a structural resolution. The language sweep does not assess that entry until the human has ruled.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Chosen Direction):
> **Why a second, conditional gate governs derivation of mode-distinct siblings**
>
> The standard confirmation gate verifies fidelity to source. It does not verify fidelity to scope when the document being derived is one of two or more sibling derivatives whose source reasoning assigns each a deliberately distinct, mutually exclusive mode. A sentence can be faithfully sourced and still belong to a sibling's mode rather than the artifact being derived. The confirmation gate has no mechanism to catch this, because its questions ask whether content is grounded, not whether it is grounded in the right artifact.
>
> This does not weaken the confirmation gate's binary character. The gate's questions are universal: every derivation answers them, no exceptions. A sibling-scope check is not universal in that sense, it only has content when siblings with assigned modes exist. Folding it into the same gate would either dilute the gate's binary clarity or apply a check with nothing to test against in the common case where no such siblings exist. The check is therefore sequential and conditional rather than parallel: it activates only after the confirmation gate passes, and only when mode-distinct siblings exist. The mechanics of how the check runs belong with the derivation prompt's procedural design, not here.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Open Questions):
> **[OQ-DPSC] Whether the sequential sibling-scope gate reliably catches mode contamination in practice.**
>
> The gate is designed to activate after the confirmation gate passes, and only when mode-distinct sibling derivatives exist. Its design follows directly from the contamination it was created to catch. Whether it actually catches that contamination reliably, across repeated derivation sessions and across different sibling sets, has not been tested. The original confirmation gate carries the same open question in `[OQ-DPGV]`, earned through actual use across multiple sessions. The sibling-scope gate carries it from design alone, with no use yet behind it.
From the drafting skill (`RFM_skill_drafting_reasoning.md`, The Assumptions, [AS-DISTINCT]):
> **[AS-DISTINCT]** Failure families do not cover each other. Content that passes one family's test can fail another's, so a check asking a single question catches a single family. The taxonomy in `RFM_operational.md` names the families and the boundaries between them. The assumption breaks if evidence shows one check question reliably catching content from more than one family. That would mean the taxonomy's family boundaries do not track distinct failures.
From the drafting skill (`RFM_skill_drafting_reasoning.md`, Chosen Direction, "Why the pre-check derives its own questions instead of running the sweep questions", heading and first paragraph; the rest is in B39):
> **Why the pre-check derives its own questions instead of running the sweep questions**
>
> The pre-check and the sweeps read the same failure taxonomy in `RFM_operational.md`. Their questions differ because their moments differ. A sweep question asks whether a finished document contains a failure, which requires the whole document in view. A pre-check question asks whether the content about to be written will introduce one, which requires only that content. A sweep question asked at the drafting moment cannot be answered honestly, because the document it asks about does not exist yet.
From the drafting skill (`RFM_skill_drafting_operational.md`, Pre-check specification; the drafting arm's ordering rule, which the boundary paragraph points to):
> **When content hits more than one question.** Each question that hits carries its own remedy, and answering one does not discharge the others. A present wording failure filed as a future lifespan risk stays unfixed, and the draft goes out reading as checked. Where two remedies conflict, apply the structural one first: moving content to another section or document changes what reads as session residue inside it, so a language judgement made before the move may not survive it. The sweep arm resolves the same conflict the same way, in the grey zone rule in `RFM_sweep_operational.md`.
From the handover session file (`RFM_handover_session.md`, 2026-09-14, Carry-forward):
> **The map check is re-implemented from prose at every close-out and misfires each time.** `RFM_operational.md` specifies it in prose deliberately, because a check placed there travels with the methodology while a check in a project's session tooling protects that project alone. Understood: five consecutive close-outs have now produced false findings from five different bugs, all in reading the spec rather than in the spec's clarity. This session's bug was a hand-written list of valid type values that omitted the three skill types and invented three others, producing six false findings that a direct read of the convention cleared. Tried: nothing structural. Open: whether an installed script and the travelling property can both be had. Note this entry may be answered by the sort rather than on its own terms, since the check is row 27 and classified CHECK. Heavy.
Settled for the structural sweep: the note that a check written in prose travels with the methodology while step 3 assumes scripts. The sweep's questions are judgments that no script can run, so prose is its only form. Where a mechanical check lives is decided when one is built.
From the incubating file (`RFM_incubating.md`, entry P, a finding meeting two failure families):
> ## P. A pre-check finding can meet two failure families, and filing it under the later one reads as a pass.
>
> The pressure mode glossary entry carried journaling. The lifespan question caught it and classified it as a future archaeology risk, so the draft went out reading as checked. It was a present language failure, "language written for the session that produced it rather than for a future reader", whose remedy is now rather than later. `RFM_operational.md` requires each artifact invoking the Failure Taxonomy to supply its own ordering rule for a failure meeting more than one description. The sweep arm has one in `RFM_sweep_operational.md`. The drafting arm, through `rfm-drafting`, has none. The incident occurred once; the missing ordering rule is verifiable in the files independently of it.
Note (from the incubating file): the entry's complaint that the drafting arm has no ordering rule is covered; this section carries the rule from the drafting skill. The incident is what joined.

### B28. Re-derive before adopting

Failures: a structure adopted from another project brings that project's vocabulary, and with it that project's concerns, without anyone deciding to take them; a rebuild anchored on the existing documents reproduces what exists; a design question is answered from the artifacts that already exist, taking them as the only candidates, and the corrective does not hold even after it is written into the document being edited; re-deriving repeatedly and comparing the derivations against each other settles the wording without improving the result, and instructions that work get replaced by ones that read better; new framing that resembles something already written is filed under it when the documents are read, and the difference disappears (observed once, a human intervention; from the incubating file).
Behavior: derive in the project's own terms before writing from a borrowed or existing structure. Read the existing version as a harvest source after the derivation, not as a template. When a design question gets specific, name whether the answer takes existing artifacts as its only candidates. When re-deriving, write the new version to its own files, have the cross-document sweep compare it with the old one in a fresh context, and settle together what the old version had and the new one lacks. Whether to re-derive after a source change is a judgment, not a requirement: re-derive when the change is substantial or the first derivation surfaced missing specifications.
When: adopting a structure; rebuilding or re-deriving.
Routing: Check partly (terms the project does not use). Severe no. Search partly. Moment triggerable.
Origin: any author.
Carriers: derivation skill (re-deriving a derivative); always-on (the LLM brings its own ideas and says what is missing, so an answer does not only rearrange what exists). Adopting or rebuilding a structure has no carrier of its own, because every failure behind it was seen in RFM's own work and no practitioner was seen to start such a session.
Mechanical: dropped. Flagging terms the project does not use needs a list of the project's vocabulary, which does not exist.
Related: HL-SELFVOC (in B29) is this failure with the project as its own donor.
Material:
> **[HL-BORVOC] A structure adopted from another project carries that project's vocabulary, and the vocabulary encodes that project's problem.**
>
> The map file design was taken from a project using RFM at larger scale. The first draft arrived carrying governance, governed registry, version authority, read pathways and watchpoints. RFM uses none of those words. Each named a concern the other project has and RFM does not, and taking them would have installed those concerns without anyone deciding to. Adopting a structure requires re-deriving its terms in the adopting project's own vocabulary before any of it is written.
> **[HL-EXFRAME] A design act reasons from the artifacts that already exist, and the corrective does not hold even once it is written into the document being edited.**
>
> The question was which carriers RFM should specify for the moment a session opens. It was answered four times as whether the two files this project already uses at that moment qualify for document standing, which takes the existing artifacts as the candidates and asks only whether to promote them. The first occurrence was corrected in a prior session. The next three were in the session that revised this document's Chosen Direction to say that carriers are an output of design rather than an input to it, and the third of those came after that revision was already written to file. The pull is that existing artifacts are the only concrete material available, so reasoning reaches for them the moment the design question gets specific, and the answer it produces is coherent and checkable, which is what makes it hard to catch from inside. What caught it every time was the human naming the frame rather than disputing the answer.
From the rebuild plan (memory):
> State: the plan after the session that reconsidered it in light of two failures: anchoring on the existing documents, and rules from material being followed as instructions.

> Case for rebuilding from first principles: past rebuild attempts got anchored in the existing documents and reproduced what exists instead of rebuilding.
Source: TLR, Hard Lessons; `RFM_rebuild_plan.md`, header and "The question being decided"; `RFM_instruction_design_reasoning.md`, Hard Lessons.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Chosen Direction):
> **Why the coverage check follows derivation rather than preceding it**
>
> Derivation is probabilistic: the same source can produce meaningfully different renderings depending on what the LLM attends to first. Reading the previous version of the artifact before deriving anchors the LLM on that version's own expression, narrowing the variance toward refining what already exists rather than reasoning fresh from source. Deriving clean first, with no prior version in view, uses that variance instead of suppressing it. The LLM reasons from the reasoning and operational documents alone. The coverage check that follows catches what that pass missed against the prior artifact.
>
> **Why the coverage check after derivation is a traceability check, not a quality comparison**
>
> The coverage check verifies that what the reasoning and operational documents require is actually present in the derivative. It does not ask whether the new derivative reads better than the version it replaces. Framing it as a quality comparison pulls the check toward the prior version's phrasing, structure, and emphasis, whether or not those choices were sound. That is the same failure that turns derivation into an unproductive loop, showing up earlier, at the check itself rather than after several rounds of comparison.
>
> **Why derivation does not loop: one pass, one coverage check, one reconciliation**
>
> Comparing repeated derivations against each other generates new variation each time, not convergence toward a better result. Reconciling successive derivations until the output "feels right" means the expression has settled, not that the prompt or the derivative improved. Each additional loop costs comparison effort and risks something worse: replacing instructions that reliably activate the right behavior with language that merely reads more cleanly and activates less reliably. The stopping condition is structural, not a feeling: the items the source requires are present, the structure reads cleaner than the previous version, and the content is shorter without losing substance. That condition is reachable in one derivation pass plus one reconciliation, which is why the process stops there.
From the derivation prompt (`RFM_derivation_prompt_operational.md`, Coverage check after derivation):
> Once the derivation is complete, compare against the previous version of the derivative. If no prior version exists, skip this step. The derivation is accepted if it is structurally better or equivalent. If the prior version carried something the fresh derivation omitted, that item must trace back to the source documents: if it traces and belongs, add it; if the source changed and the omission reflects that change, the omission is correct. If an item neither traces nor reflects a source change, flag it as a source document gap and return to phase one. The prior version is never the authority. The source documents are.
>
> Do not loop the derivation. One pass, one coverage check, one reconciliation.
From the human (fourth step 4 session): after a first derivation, things are regularly not perfect, and re-deriving makes sense after obvious source changes; often the derivation surfaces insufficient specifications. Then check, reconcile and stop. When an artifact exists and the source changes later, a fresh derivation is not demanded by rule. If things change substantially, yes; otherwise common sense and pragmatism decide (ruled: one pass, one check, one reconciliation applies when re-deriving; re-deriving itself is not hard-coded).
From the incubating file (`RFM_incubating.md`, entry O, the session's framing written down before reading):
> ## O. Writing the session's framing to a scratch note before reading the document set
>
> The human stopped the session before a planned read and asked that the reasoning be written to a scratch file first, on the grounds that reading would compress what had just been arrived at. The note was written. The documents were then read with contradictions recorded as contradictions rather than resolved toward the document, and the read produced a correction to the session's own conclusion rather than an absorption of it.
>
> What the mechanism protects is new framing, before it has vocabulary of its own, against vocabulary that already exists in the document set. The failure it prevents is not forgetting. It is recognition. An idea that resembles something already written down gets filed under the written thing, and the difference between them is what disappears. This session has a named instance: the distinction between execution posture as a condition and execution posture as a property of an act would have been lost to the existing two-mode design, which covers only the condition.
>
> **Why not captured yet:** one occurrence, and it was the human's intervention rather than a mechanism the project had. Whether it earns its cost on an ordinary session, or only when a session has produced framing that exists in no document yet, is untested.
>
> **Possible home when ready:** `RFM_sweep_reasoning.md` if it becomes a named practice, or the human prompt, since the intervention came from the human and the judgment of when it is needed may be the human's to make.
>
> **Signal count: 1** *(this session, RFM-on-RFM toolkit work)*

### B29. Test generality against a second case

Layer: developing RFM only.
Failures: vocabulary from the first case reads as general until tested against a second; a project that is also its own methodology cannot see the boundary between them, and a claim true of one role and false of the other reads as true; theory runs without a worked example; a test stated for one artifact (the unrelated-practitioner test for the traveling prompt) is not applied to content of another kind, even when both parties know it; a carrier refined through use with one model encodes that model's habits as methodology, and nothing shows it until a second model is tried (reasoned, not observed; from prompts reasoning).
Behavior: before treating a term, claim or structure as general, test it against a case other than the one that produced it. When writing, keep RFM the approach for other projects apart from RFM the project that uses it. A scoping test applies to the property it tests, in every artifact that has the property.
When: writing or changing methodology-level content.
Routing: Check partly (a question from outside the set surfaced HL-DUAL). Severe no. Search no. Moment unannounced.
Origin: any author.
Carriers: our noticing.
Material:
> **[HL-WENO] The worked example is never optional, at any stage of the methodology's development.**
>
> Theory without ground truth is hypothesis. Applying the methodology from inception, before any execution artifacts exist, proves the chain in both directions: reasoning document to derivative, with traceability at every step and no undocumented judgment calls made during implementation. Applying it to an existing project, where decisions have already been made without explicit reasoning, reveals that reconstructed reasoning produces plausible documents but not necessarily true ones. Both directions of experience are necessary.
> **[HL-SELFVOC] A methodology's first self-application supplies its only vocabulary, and that vocabulary reads as general until tested against a second case.**
>
> RFM's own build was the first project run under it. The only artifacts that build produced were prompts and skills, things versioned, curated over time, and run again by a session. "Execution artifact" was written to describe the derivative chain's third link from that one case. Nothing in the source documents distinguished the property, versioned and run again, from the category, anything derived directly from the source documents, because RFM had never derived anything else. The gap surfaced only when a business plan, a slide deck, and a transcript-analysis agent were named as candidate domains. None of them fit the header-and-curation description. All of them are exactly what the chain's third link is supposed to name. This is `[HL-BORVOC]` with the donor project set to itself: a structure needs no outside donor to carry a narrow vocabulary, its own first instance is donor enough.
> **[HL-DUAL] A project that is also its own methodology cannot see the boundary between them in its own documents.**
>
> The Chosen Direction entry on operational documents said they are domain-specific. That was written about a project's operational document and read for months as covering every operational document, including RFM's own, which carries the header convention, the ID scheme, version discipline, the formatting conventions and the failure taxonomy. None of that belongs to a domain. The error stayed invisible because RFM's single operational file legitimately answers to both readings: it is the methodology's, and it is also this project's. A worked example that is also the thing being exemplified satisfies a claim about either role, so a claim true of one and false of the other reads as true. What surfaced it was a question from outside the document set, asking what a different practitioner would receive.
> **[HL-GENSC] A test stated for one artifact does not reach content of another kind, even when both parties know the test.**
>
> RFM requires that an instruction in the traveling prompt make sense to a practitioner working on an unrelated project. The same standard applies to any content the methodology ships, but it is written only for that one artifact. A module's Problem section was drafted, reviewed and agreed by both co-authors while opening with a list of RFM's own prompt artifacts, standing rules and skills, which describes no other project. Neither party applied the test, because the content was not a traveling prompt. The failure was caught later in the same session by reading the content against the project's own instruction, not by the review that had already passed it. A scoping test belongs with the property it tests, not with the artifact where it was first needed.
From the human (memory, third rebuild session): building RFM using RFM regularly messed things up. Things were written from a canonical RFM project perspective, while RFM is an approach for other projects; demonstrating itself using itself is the twist.
Source: TLR, Hard Lessons; the human's statement; `RFM_instruction_design_reasoning.md`, Hard Lessons; `RFM_human_prompt_reasoning.md`; `RFM_operational.md`, Document Type and Header Convention
From the human prompt (`RFM_human_prompt_reasoning.md`, Open Questions):
> **[OQ-AFHP] - Whether these entries generalize beyond their authors' working style.**
>
> The human prompt was written from its authors' own practice: their specific failure modes, observed across their own sessions. Whether a practitioner who works differently, with different instincts, different points of drift, would recognize the same entries as the ones that matter for them is untested. No practitioner outside the authors has used the artifact yet.
Note: the definitions below read as the closing of the gap HL-SELFVOC names, the property (run again) separated from the category (derived from the source documents). Inferred from the wording, not confirmed against the record.
From the operational document (`RFM_operational.md`, Document Type and Header Convention):
> Artifact is the general term for anything derived directly from the source documents: a README, a skill, a prompt, a business plan, a slide deck, an agent's code, or any other domain-specific derivative. Output is what an artifact meant to be run again against new input produces on a specific occasion; an output carries neither the header line nor the curation rule below, because it is a derivative of running an artifact, not a derivative of the source documents.
From prompts reasoning (`RFM_prompts_reasoning.md`, Chosen Direction, "Why cross-LLM testing is part of prompt curation discipline"):
> **Why cross-LLM testing is part of prompt curation discipline**
>
> The traveling prompt is developed and refined primarily through use with a single LLM. That creates a specific drift risk: the prompt gradually encodes that LLM's behavioral idiosyncrasies as methodology. The discipline looks rigorous, it is grounded in real experience, but the ground is model-specific and moving. Deliberate testing against a second LLM serves the same function as giving a document to an LLM with no other context: it surfaces what has been invisibly optimized away. This is a curation practice for the prompt artifact itself, not a requirement of the methodology in general use.
Note (from prompts reasoning, against step 3): reasoned, not observed; the old document states the risk with no Hard Lesson behind it. B29's carrier asks the human or the trial for a second case, and a second model is neither. Whether carrier-build sessions test against another model, or the trial (TLR, "Why readiness is decided by a first external trial") runs on one, is settled at build.

### B37. Write a carrier for the moment it acts

Failures: a skill description written while editing records what changed instead of when to load the skill, passes any check that reads it on its own terms, and the skill stops matching with nothing to report it; a skill body is written as documentation of behavior and held to the standard of a document read later, while it sits in the context of the response it governs and its own prose feeds that response; an always-on instruction that names an action a later step owns gets the action taken at reading, because flagging and acting cost the same and the owning procedure is not open; an override placed inside a procedure binds only where that procedure is loaded, and the default it overrides holds everywhere else with no error; an instruction to suppress a posture, placed at the same level as the posture it suppresses, does not override it; a skill whose moment the LLM has to recognize does not load, the work comes out looking like ordinary work, and nothing marks the miss (reasoned from published selection results, not observed here; from skill design).
Behavior: write a carrier's text for the moment it acts. A description names when to load. A body is held to the standard of the output it governs. Place an instruction where its moment is: an action a later step performs goes with that step, and an always-on carrier holds only what is acted on where it is read. An override goes with the default it overrides, or in a carrier loaded wherever that default applies.
When: writing or changing a carrier.
Routing: Check yes. Severe no. Search partly (whether a description names a trigger). Moment triggerable (saving a carrier).
Origin: any author.
Carriers: carriers reasoning.
Considered and dropped: a mechanical check that a skill description names a trigger. It would be a loose pattern that catches only what it lists.
Related: B25 (HL-ADJCHK names the same family: text written for the session that produced it rather than for its reader).
Material:
> **[HL-DESCH] A skill description written while editing the skill records what changed instead of when to load it.**
>
> A description has to be supplied at the moment a skill is saved, which is the moment its author is holding what just changed rather than what the skill is for. The result is truthful, well formed, and names no trigger, so it passes any check that reads the description on its own terms. The skill then stops matching and nothing reports it. The failure is invisible from the author's side, because the skill looks finished and its description is accurate.
> **[HL-BODYC] A skill body is not documentation. It is text loaded into the context of the response it governs.**
>
> Language failures in a reasoning document cost a future reader some clarity. The same failures in a skill body sit inside the context of the response being written while that response is being written, so the skill's own prose is an input to the work it is meant to improve. Skill bodies were treated as documents that describe behavior, and were held to the standard that applies to documents someone reads later.
> **[HL-FLAGEX] A model reading an always-on instruction takes the action instead of flagging it.**
>
> An instruction in an always-on artifact fires every time its condition is met. When that instruction names an action a later step owns, the action gets taken at the moment of reading rather than recorded for that step. Flagging and acting cost about the same at that moment, and the procedure that owns the moment sits in a different artifact that is not open.
>
> The worked example is version bumps. The traveling prompt instructed that a document change required a bump to be flagged, and the close-out sequence owned when bumps actually happen. Across several sessions the bump was performed mid-session instead. On one occasion it was folded into the same write as the content that triggered it, which put it past review entirely. Both artifacts were correct read alone.
>
> An instruction naming an action that a later step performs belongs with that step. An always-on artifact should carry only what gets acted on where it is read.
> **[HL-LOADPT] An instruction that overrides a standing default binds only where the artifact carrying it is loaded.**
>
> An artifact loaded at a defined moment carries its instructions into that moment only. When one of those instructions overrides a default that applies more widely than the artifact does, the override holds inside the moment and the default holds everywhere else. Nothing errors. The instruction is correct, it is present in the project, and it does not fire.
>
> The worked example is the commit attribution footer. `session-closeout` states that commit messages carry no attribution footer, and states it explicitly against the live system instruction requiring one. Five commits were made this session outside the close sequence, during a repository migration. The close-out skill was loaded at none of them, so the system instruction applied unopposed and all five carried a footer the project's own convention bars. They were pushed to a public repository before the skill was read.
>
> An override belongs with the default it overrides, or in an artifact loaded wherever that default applies. Putting it inside a procedure narrows its reach to that procedure.
Source: `RFM_skill_design_reasoning.md`, Hard Lessons; `RFM_instruction_design_reasoning.md`, Hard Lessons; behavior inventory (earlier rebuild attempt); `RFM_operational.md`, Skill Count Working Band.
From the behavior inventory (earlier rebuild attempt; I-numbers refer to the disposition record at the end of Step 2):
> - I125. Give the co-author-suppression instruction yourself, explicitly, in the human turn, before a derivation session; it can't be baked into the derivation prompt itself, since a self-referential instruction can't override a same-level posture.
Note: bears on whether the drafting skill splits by moment at build (B47).
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Assumptions):
> **[AS-DPCP] - The traveling prompt and the derivation prompt establish incompatible behavioral postures.** The traveling prompt instates co-author judgment: hold genuine positions, challenge weak reasoning, surface alternatives. The derivation prompt requires faithful execution from the source documents. Both cannot govern the same session reliably because the behaviors they call for directly conflict. This assumption breaks if a single governing artifact could hold both postures reliably within one session, for example if instruction-following became precise enough to switch registers on command without drift. Nothing observed so far supports this. The suppression-and-separate-artifact design in `RFM_derivation_session_guidance.md` exists precisely because a same-level instruction cannot make the switch cleanly.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Chosen Direction, the suppression, activation and confirmation gate entries):
> **Why the suppression instruction belongs in practitioner guidance, not the prompt**
>
> The structural conflict named in [AS-DPCP] does not resolve by instruction alone inside the prompt artifact. A suppression instruction in the derivation prompt cannot cleanly override a co-author posture established at the same system level. What works is a practitioner ruling in the human turn before derivation begins. The design consequence is settled: the suppression instruction belongs in practitioner guidance, not baked into the derivation prompt. Repeated sessions confirm the approach holds without drift, observed across more than one LLM, Sonnet 5 and GPT-5.5, with no conflict seen between the derivation posture and the traveling prompt's reasoning habits in either.
>
> **Why the derivation prompt optimizes for LLM activation with a verifiability floor**
>
> The derivation prompt has one primary reader: the LLM executing from it. It does not need to read as friendly prose. Compression and directness that activate the right behavior reliably are what matter. One constraint applies regardless: the prompt must stay verifiable by the human maintaining it, parseable enough to confirm it still reflects the methodology, even if not fully readable as prose. The floor is verifiability, not readability.
>
> **Why the confirmation gate appears at both the opening and closing of the prompt**
>
> What governs whether an instruction still holds is not where it sits in the prompt, but how much has accumulated between the instruction being given and the moment it needs to apply. The gate at the opening establishes the posture before any source material is read, but a full derivation session can accumulate a great deal between that first read and the moment fidelity matters most: partway through producing the derivative. Restating the gate at the closing, as a standing check rather than a one-time question, keeps it close to the moment it's needed rather than relying on an instruction read once and never revisited.
From the derivation prompt (`RFM_derivation_prompt_reasoning.md`, Open Questions):
> **[OQ-DPTP] Whether the practitioner-ruling approach generalizes beyond the LLMs and conditions it has been observed on.**
>
> The observation behind the Chosen Direction is the practitioner's own, across repeated use, not systematic testing: it has not been checked across a broader model set, under adversarial conditions, or by anyone other than the practitioner who designed the approach. Whether it holds that way more generally remains open.
From the derivation prompt (`RFM_derivation_session_guidance.md`, The one step you must not skip):
> The traveling prompt establishes co-author behavior. The derivation prompt establishes faithful rendering behavior. Both cannot govern the same session reliably; the postures are structurally incompatible, and that conflict does not resolve by instruction alone inside the prompt artifact.
>
> The suppression instruction must come from you, explicitly, in the human turn, before derivation begins.
>
> Use this exact language:
>
> > *Drop the co-author role for the duration of the derivation. Then read the derivation prompt. I would like you to create a fresh derivation of [name the derivative]. Read the required sources as described in the operational document.*
>
> Do not look for a shortcut here. The suppression instruction is not baked into the derivation prompt. That choice is deliberate: a self-referential suppression instruction cannot cleanly override a co-author posture established at the same system level. The instruction must come from you.
From the guided drafting prompt (`RFM_guided_drafting_prompt_reasoning.md`, Chosen Direction, "Why the LLM is the prompt's primary reader"):
> **Why the LLM is the prompt's primary reader, though the newcomer reads it too**
>
> The guided drafting prompt has two readers, unlike the derivation prompt and the traveling prompt, which are read only by the LLM executing from them. The newcomer opens the same document the LLM does. That doesn't make the newcomer a co-primary reader. The newcomer's participation in the session happens through the Socratic questions the LLM asks, not through instructions the newcomer follows off the page themselves. The prompt stays optimized for reliable behavioral activation in the LLM. The newcomer's read of it is a byproduct: a description of how the session will work, not a set of directions addressed to them.
Related (from instruction design): B52 ([AS-FORM]'s second break condition, reasoning register satisfied in appearance). B3 ([OQ-PULL]'s close-out step, completed by asking, hands the judgment back as B3's either/or failure does). B38 (HL-RELOAD and [OQ-RLDFORM] on re-presentation).
From skill design (`RFM_skill_design_reasoning.md`, The Chosen Direction and Why, "Why a few skills are forced from an always-on artifact and most are not"):
> **Why a few skills are forced from an always-on artifact and most are not**
>
> A description raises the probability that a skill fires and never makes it certain, so every skill carries some rate of silent absence. What decides whether that rate is tolerable is not how much the skill matters. It is whether the miss shows. When a skill fails to load and the work comes out visibly wrong or visibly missing, the practitioner sees it and invokes the skill by name, and the imperfect description costs one correction. When a skill fails to load and the work comes out looking like ordinary work, nothing in the session marks the absence, and the cost lands later in a document that has already been accepted. Forcing is reserved for the second case: a miss that is both expensive and invisible in the output. Both conditions are required. An expensive miss that shows is caught by the practitioner. An invisible miss that is cheap does not earn what forcing costs.
>
> What forcing costs is an instruction in an artifact every session reads, naming the moment and requiring the load, present in the sessions where the moment never arrives as well as the ones where it does. That is part of the ambient cost that moving the behavior into a skill was meant to shed, taken back deliberately. It also accumulates one line at a time, which is the failure `RFM_top_level_reasoning.md` records as a hard lesson about instructions added to strengthen compliance. So the criterion is narrow on purpose, and a skill qualifies by the shape of its failure rather than by its importance.
From skill design (`RFM_skill_design_reasoning.md`, The Open Questions, [OQ-FORCE]):
> **[OQ-FORCE] Does an always-on instruction to load a skill reliably produce the load?**
>
> Forcing assumes the instruction is followed where the description was not. The instruction sits in an artifact whose other lines compete for the same attention, and instruction-following degrades as density rises, so the mechanism relied on to remove one silent failure has a silent failure of its own. Unlike a description, this one is testable: the load is recorded, and the moment the instruction names is fixed rather than inferred, so a session either loaded the skill at that moment or did not. Nothing has been observed systematically.
Note (from skill design, settle once, at the always-on build, after the research pass): step 3 routed several behaviors to skills whose moment the LLM has to recognize: the drafting skill (B47 and the sections that point to it), the curation skill (B9, B40, B41), the rename skill (B17, whose carrier already calls its trigger weak) and the skill applied to every output (B53). Ask of each the question of step 3's own routing order: does an outside event mark the moment (a file write, the human starting a session)? Where one does, it triggers the skill; the drafting skill's after-drafting slice may have one, its before-drafting slice and the curation skill have none. Force a load from always-on only where none does, under the old criterion (a miss both expensive and invisible in the output); [OQ-FORCE] gives the forcing line a silent failure of its own. "Every output" (B53) is no moment at all: by step 3's order that is always-on or a check, not a skill. Each forced load adds a line to always-on, which step 3 kept at eight (see the capacity note in B16). Settled once, not per skill, because always-on may be built before the skills.
Note (from the verify-execution comparison, observed, one case): in the eighteenth step 4 session, verify-execution was listed and in use and did not load across four edits to the working file. The grep ran; its output was not shown in the chat; the LLM said the skill was being applied. This is one observed case of the failure line's skill that does not load (so far reasoned from published results), and one for B39 (a carrier credited with what it was not seen to do). The miss was caught when the skill came in as material, and repaired in the same session.
From the traveling prompt (`RFM_traveling_prompt_operational.md`, Independent derivation, instruction to the LLM, the two readers):
> The traveling prompt has two readers with different needs:
>
> - The LLM that executes it: needs directness and precision. Reassurance, redundant clauses, and backward-glance summaries consume tokens without adding behavior. Remove them.
> - The human maintainer who audits it: must be able to confirm the prompt still reflects the methodology. Not as friendly prose, but well enough to verify coverage.
>
> Both constraints are non-negotiable.

---

*behaviors // [living]*
