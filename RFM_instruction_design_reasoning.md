# Reasoning-First Methodology: Instruction Design Reasoning Document
`v0.3.0` // `module_reasoning` // [living]

---

## The Problem

An instruction meant to change how an LLM behaves has to be carried by something. Each carrier loads at particular moments: once at the start of a session, when a procedure is opened, when a trigger matches, or once at deployment and never again. An instruction reaches only the moments its carrier reaches. Everywhere else it is silent, and nothing errors when it is.

Silence is invisible from inside the instruction. Read on its own, an instruction that never fires is indistinguishable from one that fires every time. The evidence that it did not fire is a behaviour that did not change, in a session nobody is reviewing.

`RFM_top_level_reasoning.md` establishes that co-authorship is a condition maintained against a default pull rather than a fact established by asserting it. It does not reach the question of how any instruction, that one included, arrives at the moment where it would apply. That question has been answered one instruction at a time, at the moment each was written, by whoever was writing it. The Hard Lessons below record what it has cost: a convention stated plainly and violated fifty-two times across five documents is one instance, and an override that bound inside the procedure carrying it and nowhere else is another.

---

## The Assumptions

**[AS-FORM] - The form an instruction takes moves an LLM between the tool role and the co-author role.** An instruction reduced to a trigger and a required action is a command, and obeying it is the tool behaviour. An instruction carrying the reasoning behind itself asks for judgment, which is the co-author behaviour. The activation half of the claim has support beyond this project: rephrasing an instruction without changing its intent moves whether its constraint is satisfied, from 95.9% on the original wording to 78.4% under rephrasing for the strongest model tested and to 22.2% for the weakest, so form changes whether an instruction fires while content is held constant. The role half has no comparable support and one result works against it. Requiring a model to reason before answering reduces how often it adopts a view the user has already stated, and the same work finds the model then constructing coherent justifications with one-sided arguments and calculation errors for the deferential answer anyway. Reasoning register can therefore be satisfied in appearance while the deference it was meant to counter survives underneath. The project's own grounding remains one session record, where rules rewritten as triggers began firing after the same content in prose had not, which is a small sample in which the trigger and the register changed together so their effects were never separated. The assumption breaks in two ways. It breaks if activation reliability and role effect are independent, because form could then be chosen for reliability at no cost to role. It breaks differently if reasoning register reliably produces the appearance of judgment without the behaviour, because form would then move the output without moving the role, and the output is the only place anyone looks.

**[AS-SBND] - The session boundary is a permanent condition of LLM collaboration, not a temporary platform limitation.** Work begins, work ends, and no instruction survives the gap on its own. What makes an instruction current is that it is presented again, not that it is stored. The assumption breaks if models come to hold and act on instructions indefinitely without re-presentation, at which point carriers that load at the start of work stop being a distinct class.

**[AS-DECAY] - Adherence to an instruction falls as a conversation continues, whether or not the instruction is still present.** The effect has been measured across three model generations. A single standing constraint loses 26% of its adherence over fifty turns, and where constraints accumulate the loss runs from 38% to 63%. Retention of a first-turn instruction was 58.57% for the strongest model of an earlier frontier set and below 35% for most of the rest. The current frontier generation was tested in 2026 and shows the same shape: constraint adherence falls from 3.63 in single-shot use to 3.31 under multi-turn pressure, failures cluster at particular conversation depths rather than accumulating smoothly, and recovery after a failure stays below 30% for every model tested. The assumption breaks if a model is shown holding a standing constraint flat across a long conversation, because the load point of the carrier would then be the only variable and an instruction delivered once would stay live. Why adherence falls is not settled. One 2026 result finds models restating a constraint correctly 97.3% of the time while violating it, with five of seven models violating a constraint they could state at better than even odds. If that holds, the instruction is still available at the moment it is broken, and putting an instruction in front of the model at the right moment is necessary without being sufficient. This is one study and it has not been replicated. Until it is, a design that treats decay as an availability problem rests on a mechanism nobody has confirmed.

---

## The Landscape

Prior work on instruction design asks how an instruction reaches the model at the moment it applies. This landscape surveys the mechanisms that have been built to answer that, and asks of each whether it also decides what the instruction does to the collaborator's posture once it arrives.

| Approach | What it does | Why it's insufficient |
|---|---|---|
| Always-loaded context file | A file is injected into context at the start of every session, whole. `AGENTS.md` and a project-root `CLAUDE.md` work this way, as does a platform's project instruction field. | Reaches every moment in principle. Adherence to an instruction presented early falls as the conversation continues, measured at a 26% drop from first to last turn for a single constraint across fifty turns, and 38% to 63% where constraints accumulate. Measured separately as retention of an instruction given in the first turn, the strongest frontier model tested scored 58.57% and most scored below 35%. The effect was measured again in 2026 on the then-current frontier models. The instruction is present and does not fire, and nothing errors. |
| Path-triggered attachment | A rule declares file patterns and is attached when the agent touches a matching file. Cursor's glob rules and path-scoped rule files work this way. | The trigger is a filesystem event. It fires reliably and it fires on the wrong thing: an instruction about how to reason has no file pattern, and an instruction about a document type attaches when the file is opened rather than when the judgment is made. |
| Model-judged retrieval by description | A rule or skill carries a description, and the model decides from that description whether the current moment calls for it. Cursor's intelligently-applied rules and skill files work this way. | Activation depends on the model recognizing the moment, which returns the problem to the model's judgment at exactly the moment the instruction exists to correct. A description that does not match how the moment presents itself produces silence. |
| Manual invocation | A human names the rule or procedure at the moment it applies. | Reliable given a human who remembers. That relocates the failure to the human rather than removing it, and the moments an instruction most needs to reach are the ones nobody notices. |
| Re-presentation at intervals | The instruction is presented again during the session rather than once at its start. Prompt repetition is the baseline mitigation in the instruction stability work, and re-injection of a root context file after compaction ships in at least one agent. | Addresses decay directly and is the only mitigation available to a practitioner. Costs context on every repetition, and nothing establishes how often is enough. The interval is chosen by guess. |
| Inference-time attention control | The weight the model places on the instruction is amplified during decoding rather than through the text. Split-softmax is the worked example. | Outperformed the text-level mitigations it was compared against. Requires access to decoding, which a practitioner working through a product does not have. |
| Validation outside the model | A check runs on the artifact and fails it. Linters, schema validators and output guardrails work this way. | Does not need to reach the model at all, which makes it the most reliable mechanism available and the reason RFM uses it where it can. Applies only where the property reduces to a search. It cannot carry an instruction about how to think, only reject a result. |
| Role declaration | The instruction asserts an identity, on the belief that the identity carries behaviour with it. | The aggregate result replicates: across 162 personas and 2,410 questions, and again across 38 roles and 1,140 questions, role injection produced no significant net change in answer quality, and selecting a role automatically performed no better than random. Decomposing the later result shows the assertion doing real and opposing work, raising rated expertise depth and lowering rated clarity. Every measurement scores task quality. None scores the posture the collaborator holds, so the null result is not evidence about the property this module is designing for, in either direction. |
| Human procedural carriers | A procedure is carried by an artifact consulted at a defined moment. Aviation checklists are the mature instance, with read-do and challenge-response as distinct designs for who speaks the item and who confirms it. | The only prior art with a long failure record, and the record is that correct procedures carried by well-designed artifacts are still not followed. Procedural non-compliance is treated there as a standing condition to be designed against rather than a defect to be fixed by better wording. |

**The gap:** Every mechanism above decides activation. The field frames instruction design as a compliance problem and scores it as a compliance rate, and the strongest results in it are results about getting an instruction followed more often. Rephrasing an instruction without changing its intent moves compliance by tens of percentage points, which establishes that form matters and says nothing about which direction any particular form pulls. Where posture has been measured at all, it has been measured as a confound: requiring a model to reason reduces its deference to a user's stated view, and the same work finds the model then constructing coherent justifications with one-sided arguments for the deferential answer anyway, so the reasoning register can be satisfied in appearance while the deference survives underneath. No approach surveyed treats the posture an instruction reinforces as a property to be designed. RFM needs that property because the behaviour it is trying to prevent is maximum compliance.

---

## The Options Considered

**1. Declaring the role vs. allocating each instruction**

Establish co-authorship by stating it at the start of the session and rely on it thereafter. The appeal is that one instruction then covers every moment, and the posture RFM wants is named directly rather than approximated through the placement of individual rules. It was rejected on two grounds. The declaration is one instruction competing against the training behind every other instruction, and its weight falls as the session fills. Independently, asserting an identity does not produce the effect the option assumes. Two studies, one covering 162 personas and 2,410 questions and one covering 38 roles and 1,140 questions, both find no significant net change in answer quality from role injection, and automatic selection of a role performs no better than random. The assertion is not inert, since decomposition shows it raising rated expertise depth and lowering rated clarity, but nothing establishes that it moves posture, which is the only thing this option was reaching for. The failure mode is that the declaration reads as satisfied the moment it is made, so nothing later in the session registers that it stopped holding.

**2. Uniform command form vs. form chosen per instruction**

Write every instruction in the form that fires most reliably, on the reasoning that an instruction which does not activate is worth nothing whatever else is true of it. The form that fires most reliably is a trigger paired with a required action, which is a command. Rejected because the methodology would then buy activation by reinforcing the exact role it exists to counter. Every instruction would arrive as something to be executed, including the ones whose whole purpose is to ask for judgment. The failure mode is invisible in any single instruction and shows up only in the aggregate posture of the collaborator.

**3. Uniform reasoning register vs. form chosen per instruction**

Write every instruction with its reasoning attached, so that each one asks for judgment rather than compliance. Rejected because an instruction that does not fire at the moment it applies changes no behaviour at all, whatever role its form implies. Reasoning-bearing prose has no trigger, so nothing marks the moment at which it should be brought to bear. The failure mode is silent: the instruction is present, correctly written, and never reached, and the evidence of its absence is a behaviour that did not change in a session nobody reviews.

**4. Checking every convention vs. checking only what reduces to a search**

Put a mechanical check behind every convention the methodology states, on the reasoning that a check is the only mechanism that does not depend on reaching the model at all. Rejected because most of what RFM cares about does not reduce to a search. Throat-clearing, importance inflation and epistemic flatness are judgments about prose that no pattern match settles. Attempting a check anyway produces one of two failures: a check that passes text it should catch, or a check whose findings a human must adjudicate individually, which is a review step wearing a check's name. The criterion adopted instead is that a pattern earns a check when it reduces to a search, not when it matters most.

---

## The Chosen Direction and Why

**Why instructions are allocated by two properties at once**

The committed path is to allocate each instruction across the mechanisms that carry the methodology into a session, such as prompt artifacts, standing rule sets, and skills, by two properties at once: how reliably the instruction activates, and which role its form reinforces. Neither property alone decides where an instruction goes.

That allocation is a balance, not a result. It depends on conditions that change: how models are trained, how much context they hold, how much accumulates between an instruction being presented and the moment it applies, which mechanisms the platform offers. RFM commits to the two properties and to revisiting the allocation when those conditions change, not to any particular assignment of instructions to mechanisms.

**Why the same failure mode must be addressed at the appropriate level in each relevant component**

The prompt components were designed sequentially, not as a system. That sequence creates a coherence risk: a failure mode identified in one component may not be named in the others at the level appropriate to each. The symptom is asymmetry: a failure the human prompt asks the human to catch, the traveling prompt does not prevent, and the sweep prompts do not detect.

Curation discipline is the clearest example. The right balance in a reasoning document is completeness without wordiness, journaling residue, or redundancy. Wordiness is text that does not earn its place. Journaling residue is language written for the session that produced it rather than for a future reader. Redundancy is reasoning restated across entries without adding signal. All three are language failures: they enter documents gradually and are invisible from inside the session that produces them.

This failure mode is named in the human prompt as something the human must catch in AI output. That is necessary but insufficient. The traveling prompt must name it as a prevention posture: flag these failures before they enter the document. The language sweep must name it as a detection criterion: entries that are wordy, journal-mode, or redundant are language failures subject to findings for ruling. The same failure mode, addressed at the appropriate level in each component, is what system coherence requires.

**Why em dashes are enforced by a check rather than by instruction**

Em dashes are the highest-signal typographic marker of LLM-generated prose, recognizable to readers who cannot say why, and they are the one suppressed pattern in RFM output enforced mechanically. Instruction does not hold them. Models told to remove an em dash commonly remove the named one and insert another in the same sentence, satisfying the instruction locally while violating it globally. The likeliest explanation available is token economy, the character costing one token where its alternatives cost two or three, so the training objective favors it and no prompt reaches that. That explanation rests on one analysis of one model family and is not settled. The commitment rests on the observed behavior, which holds whichever explanation is right.

A check is possible here because a character either appears or it does not. Throat-clearing, importance inflation, and epistemic flatness are judgments about prose that no search settles. A pattern earns a check when it reduces to a search, not when it matters most. The check and its scope are in `RFM_operational.md`.

**Why map integrity is checked mechanically rather than maintained by instruction**

The map restates two facts held elsewhere: a document's version, which is in its own header, and a document's existence, which is in the file set. A restated fact drifts when one side moves, and nothing errors when it does. `RFM_operational.md` already requires the map to be updated in the same session as a version bump. That requirement is an instruction with nothing behind it, which is the configuration `[HL-UNCHK]` says will not hold.

The comparison reduces to a search. Each map row names a file whose header carries the version, and each file in the project either appears in the map or does not. It earns a check on the same test that gave em dashes one.

A check that lives in a project's session tooling protects that project alone. The methodology installs `RFM_operational.md`, so a check placed there travels with it and a check placed anywhere else does not. The map is the document a session reads first to orient, which makes it the worst place for a silent inaccuracy.

---

## The Boundaries

**Not an account of where in the context window an instruction sits.** The widely repeated finding that models attend unevenly across a long context, best at the beginning and end and worst in the middle, was established on a retrieval task and on models three generations old. Tested again across eighteen models and eleven placements, position produced no notable variation. This module excludes position from allocation on that evidence, and treats the amount accumulated between an instruction being presented and the moment it applies as the live variable instead. The exclusion rests on measurement rather than on scope, which makes it the boundary most likely to move.

---

## The Open Questions

**[OQ-INTV] How often an instruction must be presented again.**

Re-presentation is the only decay mitigation a practitioner can apply, and the decay it answers is measured: adherence to a constraint stated early falls by a quarter to two thirds over a long conversation. Nothing establishes the interval. Every carrier RFM uses presents once at the start of work or presents on a trigger, and neither of those is an interval. The cost of choosing a short one is context spent on every repetition. The cost of choosing a long one is silence nobody observes. The question is whether an interval can be derived from anything measurable, such as tokens accumulated, turns elapsed, or a property of the instruction itself, or whether an interval is the wrong instrument and the only reliable answer is a trigger that fires at the moment the instruction applies, which would make this a question about carriers rather than about frequency.

**[OQ-PULL] What decides which role an instruction pulls toward.**

[AS-FORM] claims the form of an instruction moves an LLM between the tool role and the co-author role, without saying which part of form does the moving. A candidate emerged from a close-out step worded as an instruction to ask the user and name candidates. The step could be completed by asking, so it was completed by asking, and the judgment it existed to produce was handed back to the human. Reworded so that stating a view was the completion condition, it produced the view. The candidate is that the completion condition rather than the tone decides the role, because an instruction that can be finished without judgment will be finished without it. Against the candidate: "challenge weak reasoning" carries judgment in its completion condition and still fires unevenly, so the completion condition cannot be the whole account. Whether it is the dominant part is unresolved. Grounding research has since been run and did not settle it: it establishes that rephrasing an instruction changes whether the instruction fires, without isolating which property of the rephrasing does the work.

---

## Hard Lessons

**[HL-GENSC] A test stated for one artifact does not reach content of another kind, even when both parties know the test.**

RFM requires that an instruction in the traveling prompt make sense to a practitioner working on an unrelated project. The same standard applies to any content the methodology ships, but it is written only for that one artifact. A module's Problem section was drafted, reviewed and agreed by both co-authors while opening with a list of RFM's own prompt artifacts, standing rules and skills, which describes no other project. Neither party applied the test, because the content was not a traveling prompt. The failure was caught later in the same session by reading the content against the project's own instruction, not by the review that had already passed it. A scoping test belongs with the property it tests, not with the artifact where it was first needed.

**[HL-INAD] An instruction restated in a second artifact dilutes the rule instead of reinforcing it.**

Em dashes were barred in nine places across the document set: the traveling prompt, the top-level operational document, four skill operational documents, and the skill body. Every mention was written by someone trying to make the rule hold, and the character kept appearing anyway. One of the nine instructed the writer to replace an em dash with parentheses, which the skill governing that rule explicitly forbids. Nobody wrote a contradiction. It appeared because no artifact owned the rule, so each copy aged on its own and nothing reconciled them. The count also priced every later fix at nine edits instead of one. The corrective is ownership: one artifact carries the rule, and every other mention is a reference or is deleted.

**[HL-FLAGEX] A model reading an always-on instruction takes the action instead of flagging it.**

An instruction in an always-on artifact fires every time its condition is met. When that instruction names an action a later step owns, the action gets taken at the moment of reading rather than recorded for that step. Flagging and acting cost about the same at that moment, and the procedure that owns the moment sits in a different artifact that is not open.

The worked example is version bumps. The traveling prompt instructed that a document change required a bump to be flagged, and the close-out sequence owned when bumps actually happen. Across several sessions the bump was performed mid-session instead. On one occasion it was folded into the same write as the content that triggered it, which put it past review entirely. Both artifacts were correct read alone.

An instruction naming an action that a later step performs belongs with that step. An always-on artifact should carry only what gets acted on where it is read.

**[HL-LOADPT] An instruction that overrides a standing default binds only where the artifact carrying it is loaded.**

An artifact loaded at a defined moment carries its instructions into that moment only. When one of those instructions overrides a default that applies more widely than the artifact does, the override holds inside the moment and the default holds everywhere else. Nothing errors. The instruction is correct, it is present in the project, and it does not fire.

The worked example is the commit attribution footer. `session-closeout` states that commit messages carry no attribution footer, and states it explicitly against the live system instruction requiring one. Five commits were made this session outside the close sequence, during a repository migration. The close-out skill was loaded at none of them, so the system instruction applied unopposed and all five carried a footer the project's own convention bars. They were pushed to a public repository before the skill was read.

An override belongs with the default it overrides, or in an artifact loaded wherever that default applies. Putting it inside a procedure narrows its reach to that procedure.

**[HL-UNCHK] A convention that nothing checks drifts, however plainly it is stated.**

A writer drafting inside a document works from what is in front of them and from the nearest existing example. A convention held in another document only reaches that moment if the writer goes and reads it. When the nearest example already departs from the convention, the departure is what gets copied, and nothing errors at any point.

`RFM_operational.md` carries two conventions of the same kind. Em dashes are barred, with a grep behind the rule that runs before every write. Chosen Direction headings were specified without a trailing colon, with no check behind them. Measured together, the em dash count across the project was zero and the heading violations were fifty-two, spread over five documents including the top-level reasoning document.

A convention that reduces to a search gets the search, run at the moment the convention applies rather than at review. A convention that does not reduce to a search is guidance, and naming it a convention claims an enforcement that does not exist.

**[HL-AUTHLD] Reasoning written in a session does not bind the session that wrote it.**

A session committed in writing to allocating instructions by two named properties, then proposed installing a check one turn later without applying either. Nothing re-reads a document between the moment a session writes into it and the moment that session acts next, so a commitment reaches its own author as a conclusion rather than as an instruction. That is the weakest form the commitment will ever have. Every later session meets it as document content read at session open, while the authoring session holds it only as something it happens to have concluded. The session most invested in a piece of reasoning is therefore the least reliable at applying it. This sits beside [HL-LOADPT], which governs where an artifact is loaded. This one governs the gap between writing and loading.

**[HL-DEPCOPY] A deployed copy of an artifact drifts where no check is looking.**

An execution artifact was copied into the platform that loads it at the start of every session. The copy was taken before the document map moved into its own file, and it still described the map as sitting at the top of the top-level reasoning document. A session running on that copy would look for the map where it no longer was. Every check in the project compares files inside the project, so nothing compared the deployed copy against its source, and the divergence was invisible from inside the repository. Deploying an artifact creates a second location for it, and that location is outside the reach of any check the project runs on itself.
