# RFM: Carrier Types
`v0.1.0` // `top_level_artifact` // [living]

---

## What this file is

A carrier is how a piece of wanted behavior actually reaches the LLM, or the human, and stays in effect. Each type below: what it's good for, what breaks, how to build one.

---

## How to update this file

You are updating the carrier toolbox after scanning the external landscape for new insight on how carriers can be built. The toolbox is every way behavior reaches the LLM or the human and stays in effect: the type list, and the form and gating axes beneath it.

Update a type in place. New material that corrects, sharpens, or adds to a Can, Cannot, or Practical line replaces that line. Two sentences making the same point from two different sweeps is drift, not coverage; keep one.

Add a type only when a mechanism doesn't fit inside any existing Can, Cannot, or Practical, and give it the same four parts as the rest: Delivery, Can, Cannot, Practical. A variant of something already here is a line inside that type, not a new heading.

State what's found as fact. No "a study found," no source names, no dates, no research framing. If it isn't solid enough to assert plainly, it isn't ready for this file.

Check both directions before changing a line: what confirms it and what would overturn it. Weight recent material over old; the field moves fast enough that a claim from even a year back may already be wrong.

Cut anything that explains why the guidance is right instead of stating what to do. This file guides a decision. It doesn't defend one.

---

## Always-on (system prompt / project instructions)
Delivery: resent in full every turn.

Can: guaranteed presence every turn, no recall dependency.

Cannot: scale for free, per-turn token tax. Presence isn't the same as attention; a long session competes for salience against everything since. A standing constraint loses real adherence as a session lengthens even though it never leaves context, roughly a quarter of its force over fifty turns for one constraint alone, more where several constraints stack. Presence isn't what decays, whether it's still read as binding does. The drift has a direction, toward execution posture, the trained default, not a neutral fade toward nothing in particular.

Practical: decay isn't fixed by brevity alone, a short constraint stated once at the front still loses force as the session grows; where it truly matters, restate it nearer the moment it's needed rather than trusting the front-loaded copy to still be read as binding by then. Write tight, cost is paid every turn whether or not the turn needed it. Reserve for what must be true at every moment, not for what's merely important. Without reliable self-detection mid-session, anything that can't be pinned to a discrete trigger has nowhere else to go, that's the actual mechanism behind this carrier ballooning over time, not carelessness, a missing middle option. Don't put an instruction here that names an action a later carrier owns, an always-on instruction fires the moment it's read, so "flag this for later" gets acted on immediately instead of flagged, flagging and acting cost about the same at that moment. If this carrier's canonical text lives in a repo but is deployed by copy into a platform's own settings field, nothing that checks the repo alone will ever see the deployed copy drift from its source, that gap needs its own explicit check or resync habit. Declaring an identity or role here ("you are a co-author") is not neutral, it trades depth for clarity rather than doing nothing. Role framing reads as more expert and more careful, and less clear and more verbose, and the trade lands differently by domain: it helps where the reader wants risk-aware, cautious guidance, hurts where the reader wants a short direct answer. Deciding to declare a role here is a domain bet, not a default. It does not install a posture by being stated. Tool posture is what gets reached for without effort; co-authorship is not; naming the role doesn't install the posture that has to be worked for instead, and doesn't reliably raise answer quality on its own, only its style and tone. This carrier is visible to the human as well as the LLM, so it has two readers with different needs at once, not one to optimize for: compress where the LLM is the reader, cut reassurance and backward-glance summary, but preserve enough that the human can still audit it and confirm it says what it's supposed to.

## Session handover file
Delivery: read once per session, at open. Replaced wholesale at every close.

Can: carry time-bound status, where things stand, what's open, without paying a per-turn tax.

Cannot: stay salient deep into a long session. Delivered once, applied at unbounded later points. Compression can silently drop what matters, not just go stale: a close-out summary that compresses "confirmed and load-bearing" into "discussed" has lost the one detail a later session needed, and nothing flags the loss, the summary still reads as complete.

Practical: can be written dense and LLM-optimized rather than for a human reader, if something else keeps the human's picture current (e.g. the LLM restating status directly at session open). Weigh density against legibility by how often the carrier is paid for: heavier pressure to write tight the more often it's paid, lighter the less often. A designated place to park unresolved items changes behavior on its own: it lowers the threshold for parking until deferring becomes the default instead of doing the harder work of deciding whether something is ready now. That's a cost of the carrier existing at all, not a content problem, and no amount of careful wording removes it. Replacing the file wholesale at every close, rather than patching it, already defends against the more common failure in memory kept this way, an old fact left standing after something contradicts it. The remaining risk runs the other direction, compression losing something true and important; carry anything safety- or decision-critical forward verbatim rather than trusting the summarization pass to keep it.

## Initial rules file
Delivery: read once per session, at open, alongside the handover file. Edited incrementally, like source code, small diffs, never regenerated wholesale. That update rhythm, not content, is what separates it from the handover file.

Can: establish rules at session open without a per-turn tax.

Cannot: stay live through a long session the way a resent-every-turn instruction does.

Practical: a sentinel marker, a fixed end-of-file string plus an instruction to re-view if it's missing, guards against a truncated one-shot read. Worth it for a long, front-loaded file. Keeping rules (edited like source) and session state (rewritten wholesale) in separate files stops their different update rhythms from fighting each other. A rule here that overrides a standing default only binds while this file is loaded, everywhere else the default still applies unopposed and nothing errors, so an override belongs either beside the default it overrides or in a carrier loaded everywhere that default applies, not buried inside a narrower one. The file's existence buys most of the compliance this carrier is good for; length, ordering, nesting, even internal contradictions move compliance by roughly nothing once the file exists at all, so stop polishing structure once the rules are stated, the marginal return on organizing this file well is smaller than it feels while doing it. Where this file gets scoped to a subdirectory, it only loads when something opens a file there, not at session start, that's a different carrier wearing this one's name; if it has to be live from turn one, it belongs at the root.

## Event-triggered skill
Delivery: loaded when something recognizes a moment, drafting, session close, session start, verify-execution.

Can: carry procedural depth, no per-turn tax since it only enters context when relevant.

Cannot: fire on an unanticipated moment. Depends entirely on something, usually the LLM, recognizing the trigger. Naming an already-loaded skill again inside the same session does not force a fresh restatement, it can return a stub pointing back at the earlier presentation rather than reloading the text, so it's not a reliable way to re-bind something mid-session that needs to be live again. Firing at the right moment is not the same as helping: a skill that loads correctly can still be the thing that makes the output worse, by prescribing more procedure than the instance in front of it needs, or by steering toward the wrong implementation of what was asked. That failure is more common than mis-triggering and it's invisible from outside, the skill fired, the output just wasn't what the task needed.

Practical: write the trigger description at the moment of deciding when this should load, not while editing the skill, a description written mid-edit records what just changed, reads as accurate, and names no trigger, so the skill quietly stops matching later and nothing reports it. The body isn't documentation read afterward, it's text loaded directly into the context of the response it's governing while that response gets written, so weak prose in a skill body degrades the very output it's supposed to improve. A large number of installed skills carries its own per-session cost, discovery and selection burden, independent of any one skill's length. Cap the count, not just the size, selection quality holds up to roughly thirty to fifty loaded skills and drops past it, and what drives the drop at that point is two skills sounding like they cover the same moment, not the raw count, so write triggers to be distinguishable from each other, not just individually accurate. Write the skill body to prescribe the minimum procedure the moment needs, not the maximum it could justify, a skill that over-specifies gets followed and bloats the output even when it fires exactly right. Pushed too far, finely-grained triggers become a trigger architecture, nothing happens unless something upstream decided the moment arrived, and every moment nobody anticipated fires nothing. That's a tool posture built into the structure regardless of what the surrounding text claims.

## Event-triggered check/checklist
Delivery: fires at a narrower, more mechanical sub-moment than a skill, branching a module, hitting a reference.

Can: enforce a property reliably and cheaply, when the property reduces to a search, the same answer on every run, checkable at the moment of writing rather than at review.

Cannot: judge prose or a judgment call. A pattern loose enough to catch a real failure also catches compliant text; tightened to spare compliant text, it misses the failure. Using a model to judge compliance instead just relocates the judgment problem rather than solving it, an automated judge run against the same output a human rated caught a small fraction of the violations the human found. A model judging compliance disagrees with a human rater on most of what the human would flag, and gets worse, not better, on input that's paraphrased or reformatted without being substantively different, treat "a model checked it" as advisory at best, never as this carrier's replacement. A verdict alone, clean or passed, is indistinguishable from the check never having run at all.

Practical: before building a check, confirm the failure it targets is the one that actually occurs, not the one that happens to be easy to detect, those aren't always the same failure. A convention with no check behind it drifts regardless of how plainly it's stated, one project measured zero violations of a checked convention against fifty-two violations of an unchecked one stated with equal clarity in the same document set. Require the check to show what it found against the specific content in front of it, not just its verdict, or a real miss and a skipped check look identical. Scope it to what changed since it last ran, not the accumulated total, a check that gets more expensive as the thing it protects grows is exactly the check that gets skipped under pressure, when it's needed most.

## Session-scoped artifact/prompt
Delivery: governs one whole bounded episode end to end, sweep prompt, guided-drafting prompt, derivation prompt. Not optional once that session type is invoked, it is the entire content of that session.

Can: hold sequencing and pacing rules that only make sense across a whole episode.

Cannot: apply outside that session type. A stated procedure does raise the odds of a good outcome, removing it hurts every model it's been tried against, this carrier is not decorative. What actually breaks runs opposite to the obvious worry: not abandoning the procedure, but sticking to it past the point it should have been left, executing a step faithfully after the situation underneath it already changed. Build the exit into the artifact itself, name in advance what would mean stop and replan, don't rely on noticing from inside the procedure that it's gone stale. Ambient framing is what makes an always-on carrier work and what makes this one fail silently: a session-scoped carrier that doesn't concentrate attention produces a shallow pass that still reads as clean, this one needs to feel like deliberate critique, not background discipline.

## The human
Not an LLM-side carrier.

Can: self-report on own state, notice own disengagement, things unavailable to the LLM.

Cannot: be relied on precisely when it matters most. Both parties tend to drift toward execution posture at the same time, so human judgment is cheapest to trust exactly when it's least trustworthy. Effort here is elastic, not fixed: once the output looks good enough, review pressure drops on its own, so a human step positioned as a formality gets treated as one. And the act of supervising erodes the skill supervision needs, the longer someone oversees a system that's usually right, the less prepared they are for the moment it's wrong, exactly backwards from what the role requires. This carrier isn't present at all during an unattended run, nothing there to request an artifact from or notice drift; what covers that gap is a checkpoint and a log reviewed after the run instead of during it, a different shape of involvement than anything else here assumes.

Practical: when the human's role is part of a producing-act gate, a required artifact before a transition completes, keep it to requesting the artifact, not evaluating it. The moment that most needs the gate is also the moment the human is least able to review carefully. Don't default to inserting a human step because it feels safer, an overstretched reviewer rubber-stamping something can be worse than no review at all; decide this carrier belongs in a given spot on purpose, the same way any other carrier gets chosen, not by habit.

## On-demand reference document
Delivery: pulled only when something goes looking for it. Never pushed.

Can: grow without a fixed cap, cost charged only to the reader who opens it.

Cannot: be counted on to be seen at all. If nothing prompts a lookup, it might as well not exist that session. This isn't a wording problem either, an agent left to decide for itself when to look something up can't reliably tell when its own knowledge is thin enough to need it, that's a property of pull-only retrieval, not a fixable trigger phrase.

Practical: distinct from a session-scoped artifact because it's optional even when relevant, and distinct from an event-triggered skill because nothing auto-triggers it, pure pull. Never put anything load-bearing here, this carrier is for material that's fine to miss most sessions, a reference worth having but not worth guaranteeing; anything that must be seen belongs in a carrier with real delivery instead.

## External validation / mechanical check outside the model
Delivery: runs against the artifact itself, not against the model, independent of whether the model reads or agrees with anything, a linter, a schema validator, an output guardrail.

Can: the most reliable mechanism available, since it never depends on reaching the model at all, no activation, no adherence, no decay. Also the only carrier that can maintain, not only gate, regenerating a derived file, fixing formatting, syncing a version number, doing the mechanical part directly instead of asking the LLM or the human to.

Cannot: apply anywhere the property doesn't reduce to a search or a fixed transformation. Can reject, fix, or regenerate; cannot carry an instruction about how to think, and cannot produce judgment, only a predetermined response to a predetermined condition. Even inside what it does check, a pattern-based version of this only catches the patterns actually enumerated on it, not the general failure class, a clean pass says nothing about a failure nobody has added yet.

Practical: use wherever a property is checkable, prefer this over any model-facing carrier for that slice of the problem, then hand the remainder, whatever doesn't reduce to a search, to whichever advisory carrier fits. A property split this way, the checkable part kept here, the judgment part to an advisory carrier, is more reliable than asking one carrier to do both. A carrier of this kind still needs a traceable source or it can silently lose content with nothing able to detect it, every consistency check works by comparing a document to its source or its derivative, an artifact with neither is invisible to all of them.

## Capability boundary
Delivery: not text at all. What the LLM is permitted to reach, decided outside the model, before anything is generated, a tool withheld, a permission scoped, a write path that doesn't exist for it to use.

Can: make the disallowed thing not representable, not merely discouraged. Nothing to bypass, ignore, or talk around, because there is no path to the capability for language to route through in the first place.

Cannot: carry judgment, only presence or absence of an affordance. Can't express "usually not, but here's the exception," that has to live in an advisory carrier layered on top of whatever the boundary already permits. Only covers what was thought to restrict in advance, a capability nobody thought to withhold is available by default, and this carrier doesn't self-audit the way a check can be re-run against new content.

Practical: put a thing here whenever the cost of getting it wrong is high and the shape of "wrong" is nameable in advance, deletion, a write to a document nobody approved, reaching outside the scope of the task. Everything else stays advisory, this carrier is expensive to build and to change, so it's for what must never happen, not for what merely shouldn't. Where an instruction and a capability boundary say the same thing, the boundary is what's actually true; the instruction is a courtesy to whoever's reading, not the enforcement. A close cousin bounds by quantity instead of kind, a cap on how many times an available action can fire, a retry limit, a token ceiling, so something correctly scoped still can't run away inside what it's permitted to do.

## Subagent/delegation boundary
Delivery: isolates a sub-task in its own separate context. The parent never sees the sub-task's full trace, only what's defined to cross back.

Can: hold an entire sub-reasoning trace off to the side so it never counts against the parent's attention budget, the actual defense against a long episode filling up with material only one step needed.

Cannot: return more than what was defined to come back. Whatever the sub-task's context held and didn't put in the summary is gone from the parent's view, permanently, the same compression-loses-detail risk a handover file carries, except it happens inside a single episode and looks like nothing crossed a boundary at all.

Practical: define the shape of what comes back before building the delegation, not after, extracted facts, a confidence signal, open questions, a fixed small contract. Scope the sub-task to only the tools it actually needs, not the parent's full toolset. Don't reach for this as a parallelism trick first and a context-isolation device second, the isolation is the reason to use it.

## Design principles across types

Delivery is finite and structural, before every turn, before session start, at a triggered moment, on lookup. Application, when a behavior should actually fire, is unbounded and situational. No amount of fine-grained triggering closes that gap, it only relocates where the misses happen.

To size a carrier: can compliance be checked after the fact from outside, or does it depend entirely on the LLM's awareness in the moment? Checkable-after-the-fact behaviors fit lighter, advisory carriers: always-on, handover file, rules file, skill, check, session-scoped artifact, on-demand reference. Behaviors with no external trace of failure at all need a producing-act gate laid onto one of those carriers, see below, since nothing else manufactures the trace that would otherwise never exist. Behaviors where the cost of a miss is severe and the miss is nameable in advance belong in a capability boundary before any of this is considered, that carrier removes the need for the others on whatever it covers. A behavior that needs an entire sub-task walled off from the parent's context, not merely stated somewhere, calls for a subagent boundary instead, that's a structural choice about the episode, not a place a rule gets written. Behaviors that reduce to a search belong in external validation regardless of anything else.

Form is a separate axis from carrier type and pulls independently of it. An instruction reduced to a trigger and a required action fires more reliably and reads as a command, tool behaviour. An instruction carrying its own reasoning asks for judgment, co-author behaviour, and fires less reliably. Writing something in reasoning-bearing form doesn't guarantee the judgment actually happens either, it can be satisfied in appearance, the visible output changing while the underlying deference survives underneath. Choose form per instruction, independent of which carrier holds it.

Gating is a third axis, independent of both carrier type and form. A producing-act gate isn't a delivery channel, there's no such thing as a gate arriving on its own; it's a requirement laid onto whichever carrier already reaches the transition it guards, almost always always-on, since the transition (entering execution posture, in the clearest case) is unbounded and unanticipated, not something an event trigger can wait for. What makes it a gate rather than passive text: it requires the LLM to produce something, a stated frame, what's settled, the boundaries, what would exit it, before the transition completes, and difficulty producing that artifact is itself the signal, unsettled reasoning makes the frame hard to write. Only two legitimate outputs, a stated frame or a named gap, or the mechanism always passes and isn't a gate at all. Require the artifact to state exclusions, not only coverage: coverage is easy to produce for anything already in view, exclusions require modeling what a reader would wrongly assume was included, harder to fake, and reads as generic immediately when faked. It can't force honesty, fluent text is a core LLM competence, so a hollow but fluent frame can still pass; what it buys is a checkable trace afterward, not a guarantee in the moment. Price the two directions of the transition asymmetrically: gate entry hard, because drift runs toward execution on its own without anyone deciding; make exit cheap, unilateral, either party, pointing back at the artifact rather than re-arguing. The same gate can sit on the human's side of a transition too, keep that half to requesting the artifact, not evaluating it, the moment that most needs the gate is also the moment careful evaluation is least available. A dated gate produces its own evaluation data over time, what was believed settled next to what happened after, worth keeping even when that isn't the point of building it.

Restating the same failure mode in more than one carrier is healthy allocation when each carrier does a different job, fires at a different moment, reaches a different reader. It becomes dilution the moment two carriers do the identical job with no single owner, each copy then ages on its own and nothing reconciles them, one can even drift into contradicting another written to enforce the same thing.

An artifact's obligations are decided per carrier, not as a package. A version number answers what changed since last time, and only makes sense for something edited incrementally, not something replaced wholesale. A registry or map entry answers whether a session can find the artifact when orienting. Curation exposure answers whether its entries graduate or expire rather than only accumulating. A given carrier instance can need any of the three without needing the others, decide each separately from what that carrier actually does.

A rule that names its own invocation mechanism is not proof the mechanism runs. Only an executed step actually reads and applies content, writing "this is enforced by X" is not the same as X running, and the gap between the two is invisible until the moment it's tested.

An instruction cannot reliably override a posture standing at the same system level, whatever its wording claims. Overriding it takes a different level or a different actor, not restated text at the level being overridden: this is why suppressing co-authorship for a session-scoped episode is the human's to give, explicitly, in the human turn, every time, rather than a line written into the episode's own prompt, a same-level self-suppression instruction competes with the standing posture instead of replacing it.

The goal across every type here is gap-legibility, not gap-elimination. A carrier set that produces no visible gaps under real use probably hasn't been tested honestly. One whose gaps surface as named, checkable debts instead of hiding until they harden into undiscovered decisions is doing its job.

---

*carrier types // [living]*
*carries the toolbox, not why any type in it looks the way it does*
