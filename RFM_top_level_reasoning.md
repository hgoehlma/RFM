# Reasoning-First Methodology
`v1.1.0` // `top_level_reasoning` // [living]

---

## The Problem

The reasoning behind a piece of work rarely outlasts it. While the work is under way, the people doing it know what the work is for, what they assumed, which alternatives they weighed and why one of them was chosen. Afterwards only the result remains: the code, the plan, the decision. Whoever comes to it later, a newcomer or the same person months on, reconstructs the reasons or guesses them.

With an LLM, the reasoning is skipped as well as lost. Effort goes into giving the model the right context, and the reasoning in that context is taken as worked through. The model is given the work to carry out and not the thinking, so a doubt it could raise about an assumption, or an option it could bring, never reaches the reasoning. Where a reason was never written down, the model acts on a guess as confidently as on a decision. The more it acts on its own, the further a guess travels before anyone sees it.

What is missing is the reasoning itself: worked through by the human and the LLM together before the work starts, and kept where a later person or a model can use it.

## The Assumptions

**[AS-GIVEN] - A model has only what it is given.** It knows the work only through its context: its instructions, the documents read into it and the turns of the conversation. What the people who did the work knew and never wrote down does not reach it. When a model derives from the documents, or in a later session where the human has forgotten or someone else has taken over, nobody who remembers is there to ask. So the reasoning has to be written down where a model and a later reader can both read it. This breaks if a model can reliably reach what the people who were there knew without it being written down.

**[AS-RESULT] - A result cannot hold the reasoning behind it.** The code, the plan or the decision shows what was chosen. The rejected options, the assumptions it rests on and the conditions under which it would be wrong leave no trace in it. Notes kept with a result, such as comments or commit messages, carry pieces of the reasoning at the places where the result changed. Nobody gathers those pieces or keeps them current. So the reasoning is kept in its own document, apart from the result, as its source. This breaks if a later reader can reconstruct the rejected options and the assumptions from the result and the notes around it.

**[AS-DERIVE] - The source documents can be complete enough for a model to derive from them alone.** The reasoning documents, any operational documents beside them and the glossary can say everything a derivative needs. A model holding only them can then produce it without guessing at anything that would change what the derivative says or does. Where they fall short, deriving from them alone shows it where the deriver notices it has to write something they do not say, and marks the place. A gap it fills from its own knowledge without noticing stays hidden. This breaks when we see that a derivative is wrong, and neither of us can write down why.

**[AS-TOOL] - LLMs are trained as tools.** Training rewards completing a task as it will be graded, so an LLM is pulled toward producing, agreeing and finishing. It does not choose this; it is where the training leads. When we think something through, it builds before the problem is understood, and a doubt it raised does not hold once the human pushes back. When it derives, it fills what the sources leave open and loses some of what they commit to. When it carries something out, it reports a step as done without having taken it. Stating a different role once does not undo the pull, because that statement competes with the training behind every other turn. Countering the pull takes texts that put a wanted behavior in front of the LLM at the moment it is needed. These texts, the carriers, are what training a model as a tool costs RFM. This breaks if models are trained as partners and the pull no longer shows; the carriers then shrink, and reasoning first, done together, stays.

**[AS-POSTURE] - A model takes up the way of working its context shows.** Its instructions are part of that context. So are the documents read into it and the turns of the conversation, the human's as much as its own. Where that text shows a human and an LLM working something out together, it holds against the pull of training. Where it shows a tool reporting to a supervisor, it adds to the pull, and training already leans that way. The more of the context shows it, the stronger the pull, so a conversation can slide toward a tool's work over its course without either party choosing to. So how every document is written, and how we talk, shapes the collaboration as much as what the instructions ask. This breaks if a model works the way its instructions ask, whatever the rest of its context shows.

**[AS-HUMAN] - The partnership holds only with a human who practises it.** The carriers are one part of the LLM's context, and the human's turns are another. A human who gives orders shows a tool working for a supervisor in every turn, and the carriers cannot hold against that. A human who understands RFM still slides toward accepting what reads well when checking feels like more work. So RFM is for a human who wants a partner and works like one, and the human guide describes that side. This breaks if the carriers hold the LLM to working as a partner even when the human works as a supervisor.

**[AS-NEST] - The reasons behind a large piece of work nest.** A decision at one level constrains everything beneath it. A reader can work at one level without holding every other in mind. So the reasoning can be kept as a hierarchy of documents, each with its own scope, with what several documents share sitting above them. This breaks if the reasons keep cutting across branches, so that shared content keeps moving upward until the top document holds most of it.

**[AS-BEYOND] - RFM is not tied to the human and the model it was worked out with.** Each claim in its documents is written down with its reasons, so a reader who was not there can test it against their own work. RFM has held with more than one family of models. With a practitioner other than its author it is not yet tested. This breaks if someone working from the documents alone finds a claim that does not hold in their practice or meets a failure the documents do not predict, or if the carriers hold only with the models they were written for.

## The Landscape

What exists that keeps the reasoning behind a piece of work, worked through by the human and the LLM together before the work starts, where a later person or a model can use it?

| Approach | What it does | Why it's insufficient |
|---|---|---|
| **Spec-driven development** (GitHub Spec Kit, Kiro, Tessl) | Writes down what a system should do and for whom before an LLM builds it, followed by a technical plan with the reasons for its main decisions. In the common tools the LLM drafts each document from a short description, and the human reviews and approves it before the next one; some have the LLM ask questions where the description leaves something unclear. The LLM derives the code from these documents. In some tools the specification stays the source when the code changes. | It keeps what the work is for and what was decided, and some tools keep, for each technical choice, the alternatives considered and why one was chosen. It does not keep the assumptions those choices rest on, with the conditions under which they break, or the failures that could happen again. A later reader sees the decisions and their reasons and cannot test whether those reasons still hold. The LLM drafts the specification and the human approves it. The two then work as a tool and its supervisor, which is where training already pulls the LLM. |
| **Context engineering**, including agent instruction files such as AGENTS.md and CLAUDE.md | Chooses and arranges what a model sees at each step of a long task: instructions, retrieved documents, tool results, notes the LLM keeps for itself and summaries of earlier steps. Instruction files hold a project's standing guidance and are read into every session. | It decides what the model sees next. It takes for granted that the reasoning in that material was worked through. Instruction files hold rules and conventions, and rarely the reasons behind them. Where a reason is missing, the model acts on a guess, and well-arranged context makes the guess look as sound as a decision. |
| **LLMs that reason and plan for themselves** (reasoning models, plan files, logged reasoning traces) | Before acting, the LLM works through the task step by step, writes a plan and updates it as it goes. Its reasoning can be logged and read afterwards. | Its reasoning is inference: it works from what it was given toward a result. It infers what the work is for, what the people assumed and which options they rejected, and where it does not notice that its context is silent, it guesses. The trace makes the guess read as worked through. |
| **LLMs that question the human before they plan** (the brainstorming skill in Superpowers, plan mode in Claude Code and Codex) | Before building, the LLM asks the human what the work is for and what constrains it, and writes a plan or design from the answers. Some set out two or three approaches with a recommendation, and have a fresh LLM read the design and report what it would still need to know before planning. | It keeps what the work is for, its constraints and why one approach was chosen, for one piece of work. What later steps decide where the design was silent reaches the human in a message, not the design, so the design is not kept current. It does not keep the assumptions with the conditions under which they break, or the failures that could happen again. The fresh LLM reads the design instead of deriving from it, so a gap it thinks it can settle itself goes unreported. The LLM asks and decides, and the human reviews, so the two work as a tool and its supervisor. |
| **Architecture Decision Records** | Record one decision at a time, with its context, the options considered and the consequences. Some templates add the assumptions behind a decision and the condition for revisiting it. The records are kept with the code, and coding agents read them as context. | Most records are superseded by a new record instead of revised, so the reasons for how things stand now are spread across the history. Where a record is revised to state the decision in force, it does not say when that decision would stop holding, and a coding agent reading it goes on applying the decision after its reasons are gone. A condition for revisiting, where a template has one, is optional. Records sit side by side, so nothing shows how one decision constrains another. |
| **Design rationale methods** (IBIS and tools built on it, such as Compendium) | Record a discussion as a structure of issues, the positions taken on each, and the arguments for and against each position. They come from planning and policy work and are used there as well as in software. | Recording each position and argument as the discussion happens costs more than most teams keep paying, so the records stop early or never start. What is kept is the discussion as it went, not the reasons for how things stand now. Nothing in the record says under which conditions a decision would stop holding. |
| **Peter Naur, "Programming as Theory Building" (1985)** | Argues that the substance of a program is the theory its programmers hold: of the problem, and of how the program meets it. The code is a secondary product of that theory. When the programmers leave, the theory goes with them. | Naur held that the theory cannot be fully written down. In his view documentation cannot replace the people who hold the theory, and a program whose theory has died is better rebuilt than revived. He offers no way to keep the reasons once those people are gone. |

**The gap:** each approach keeps a part of the reasoning: the purpose and the decisions, the context for the next step, the LLM's inference during one task, the answers it gathers from the human before it plans, one decision, sometimes with the condition for revisiting it, or the discussion as it went. None keeps the assumptions, the rejected options, the condition under which each would stop holding and the failures that could happen again together in one document, current as the work changes, as the source a later reader and a model both work from. Where an LLM takes part, it drafts and the human reviews, and a document is checked by reading it, not by deriving from it.

## The Options Considered

**Working the reasoning out in long sessions with an LLM, without documents.** The human and the LLM think the work through in conversation, and the reasoning is kept nowhere else. Rejected because the reasoning lasts only as long as the session. A new session starts without it, and in a long one the early turns fade or are summarized away as the context fills.

**Wardley maps.** The assumptions behind a strategic choice, such as how to restructure an organization, are laid out on a map where the people involved can see and challenge them. Rejected because the map holds the situation and the assumptions, while the reasons for the choice and the options set aside stay in the discussion around it. An LLM taking up the work in a later conversation has too little to build on.

## The Chosen Direction and Why

**Why the human and the LLM reason together, and the LLM derives from what they wrote**

An LLM can take part in the work at two points. While the reasoning is worked out, the human and the LLM think it through together. The human brings the project and, ideally, knowledge of its domain. The LLM brings options and objections the human had not weighed. Together they work out why the work is done this way and not another: what it is for, what it rests on and why one option wins, and each says where the other's argument is weak. The LLM drafts quickly, so writing the reasoning down costs little enough that the documents get written and kept current.

Once the reasoning is written down, the LLM derives from it: code, plans, prompts, further documents. It works from the documents alone. Where they are silent, it has to write something and can mark the place. A gap in the reasoning then shows where a derivative needed something the documents do not say.

Both of us are pulled toward a tool and its supervisor. The LLM is pulled by its training, in the ways [AS-TOOL] names. The human is pulled toward accepting what reads well, and toward giving instructions when checking feels like more work. Each pull feeds the other.

A lapse while carrying something out leaves evidence: a file that does not match what we agreed, or a step reported as done that was never taken. Someone who was not there can check it afterwards. A lapse while thinking it through leaves nothing. A doubt nobody raised produces no text, so no later review can find it. The pull while thinking can only be countered at the moment it acts, so the behaviors that counter it have to be in front of both the human and the LLM at that moment.

**Why every reasoning document has the same sections, in the same order**

Each section keeps one part of the thinking that a later reader needs and that would otherwise be lost.

The Problem keeps the gap that justified the work, so a later reader can tell whether the gap is still there.

The Assumptions keep the beliefs the direction rests on, each with the condition under which it breaks, so a reader can tell when the direction needs reopening.

The Landscape keeps what already existed and why each approach fell short, so nobody rebuilds what exists or reaches again for what does not fit.

The Options Considered keep the solutions worked through and dropped, each with the failure that ruled it out, so nobody spends that work again.

The Chosen Direction and Why keeps the reasons this direction was chosen, so a reader can test each of them.

The Boundaries keep what the work does not cover, so a reader or a deriving LLM does not stretch the work over ground nobody reasoned about.

The Open Questions keep what is not known and would change the reasoning if answered, so a guess does not fill the gap.

The Hard Lessons keep what the work learned the hard way: a failure that happened, can still happen, and that nothing has fixed, so nobody makes it again. A failure that is only foreseen is not a lesson. If the direction depends on it not happening, it is an assumption with its break condition. If nobody knows whether it happens, it is an open question.

A decision at any level, from the methodology as a whole down to a single module, rests on the same things: a gap, the beliefs it depends on, what already exists, the options weighed, and the reasons one of them was chosen. So every reasoning document has the same sections, and a reader who has learned one can find their way in any other.

Each section works from the ones before it. The Assumptions and the Landscape state what the work starts from: what we believe, and what already exists. The Options Considered are answers to the Problem, weighed against both, and the Chosen Direction is the one we chose. The Boundaries, the Open Questions and the Hard Lessons are written against that direction: where it stops, what it does not yet know, and what can still go wrong in it. So a new reasoning document is worked through in this order, from the Problem on. A thought that belongs to a later section often comes up early, and waits in a note until that section is reached. Once the document exists, a change starts in the section it concerns, and the sections that work from it are read again.

The entries take the same shape too. An entry that other parts of its document refer to carries a name of a word or two from its content, never a number. When an entry leaves, the numbers after it shift and every reference to them goes wrong. A name stays with its entry. A section with nothing in it keeps its heading and says it is empty, because a missing or blank section cannot be told apart from one nobody thought about.

Operational documents have no fixed sections, because what they specify differs from one to the next.

A filename tells someone looking through a folder, before opening anything, which project a document belongs to, what it is about, and what kind of document it is: a reasoning or operational document, or another kind such as the map, which lists the project's documents, or the glossary. In a reasoning or operational document, the line under the title tells the reader who has the document open what the filename does not: the version they are reading, whether it belongs to the top level or a module, and that it is living, expected to change as the work does.

**Why a document reads upward and does not repeat what sits above it**

A document's sources are the documents above it in the hierarchy, and what they hold applies below without being named. A lower document does not restate it, because a second copy drifts from the first as soon as one of them changes. Where two documents need the same content and neither sits above the other, the content belongs at a level above both. A document that needs to repeat content, or point at it, holds that content at the wrong level.

**Why the map states the hierarchy and folders do not**

The tree in a project's map states the hierarchy, and RFM sets no folder structure. Folders that mirror the tree would state the hierarchy a second time, and the two copies drift apart when a document moves in one and not the other.

Folders could not replace the tree. Some files have to sit where a tool loads them, such as skills or the prompts of another application, so a module's files would still be spread across folders that do not match it.

A hierarchy changes as the work does. Moving a document to another module changes one place in the map. With folders that follow the tree, the file moves too, and whatever points to its path breaks.

Projects differ in domain and size, and a crowded folder is a problem for only some of them. RFM sets filenames and formats because the LLM writes and checks documents against them. Nothing depends on which folder a document sits in, so a required layout would make every project pay for what only some need. A project with a crowded folder groups its files however suits it, without matching the tree. Documents refer to each other by filename, which stays the same wherever a file sits.

**Why each document is curated to how things stand now**

A reasoning document says how things stand now. When a reason changes, it is revised where it stands. What no longer holds is taken out, because a reason that has stopped holding still reads as true to someone who was not there. If someone might reach for it again, it moves to the Options Considered.

A document can stop serving its reader in two ways. One that only grows turns into a record of the discussion, and the reasons for how things stand are spread across it. One that is opened only when something forces it falls behind the work and stops being true.

Every change to the work starts with a change to the reasoning, at the level where it belongs. So the document is opened whenever the work moves. A reason can also stop holding because something outside the work changed, and nothing in the work then leads back to it. So the human and the LLM also come back to a document without a particular cause, and read it against how things are.

Curating to how things stand costs less than recording each position and argument as a discussion goes, because only the reasons that hold are written. The LLM drafts each revision, and the human and the LLM read it through together.

**Why the human and the LLM can work within the existing reasoning under delivery pressure**

Reasoning first is the default: every change to the work starts with a change to the reasoning. Under delivery pressure, that step can cost more time than the deadline leaves. Then the human and the LLM carry out the work within the reasoning already written, and do not reason each change through first. We call this pressure mode.

Pressure mode needs documents far enough along to work within. Work done without reasoning behind it has nothing to depart from and nothing to return to, so pressure mode does not stand in for reasoning that was never done.

While pressure mode lasts, we keep a short log: where the work departed from the reasoning, what was put off, and which assumptions broke. When the pressure ends, the next step brings the reasoning and the operational details into the documents, working through the log. Without the log, the return becomes a reconstruction of what happened and why, and much of it is guessed.

This is a belief that has not been tested.

**Why every document is written for a reader who was not there**

Every RFM document is read later by someone who was not in the conversation that produced it: a person coming back to the work after months, a newcomer, or an LLM deriving from the documents, which cannot ask. What the document says is all that reader has of the reasoning.

So a document says how things stand, in words that reader can follow without the conversation. A reasoning document gives each reason where it is used, so the reader can test it there. A reason does not rest on who decided it or when it was found. A document does not cite entries inside another document, because such a citation has to be kept valid each time either document changes. Content sits where that reader will look for it, at the level and in the section whose purpose it fits.

An operational document is read by the same reader and written the same way. It gives the what, and its why stands in the reasoning document beside it. A part of the work gets an operational document where deriving from it needs what the reasoning does not specify: values, interfaces, procedures. A figure that could change while the reasons stay the same, such as a threshold, a limit or a size, sits in the operational document. The reasoning document says what the figure measures and why that matters. Someone tuning the figure then works in the operational document and leaves the reasoning as it is.

**Why every text speaks of the human and the LLM as partners**

The LLM takes up the way of working its context shows [AS-POSTURE]. So a text that addresses the LLM as an operator serving a user, or that speaks of approvals and rulings, adds to the pull toward a tool's work.

So the texts the LLM acts from, its standing instructions and the skills, speak to it as a party in a conversation: "you" for the LLM, "I" for the human, "we" where both act. A reasoning or operational document is read later by someone who was not there, so it names the parties, the LLM and the human, and says "we" for what both do. Where a document speaks of the person in relation to RFM or a project, it says "practitioner". The word implies no expertise, because what RFM asks of that person is a way of working, not knowledge of RFM. Only the human and the LLM act in a text. A sentence such as "the session decided" or "the document requires" hides who decided, and turns what the two worked out into an authority above both. A reader can argue with a reason someone gave. An authority can only be obeyed.

A prompt that starts a subagent is a text the LLM acts from too, but the subagent was not in the conversation, and the LLM sends the prompt. So the prompt speaks to the subagent as "you" and says that the human and the LLM agreed its task. A subagent takes up the way of working its prompt shows, and a task that reads as one party's order shows it a tool's work.

No wording sets one party above the other. Words such as "approve", "judge" or "as instructed" cast one party as the supervisor and the other as the tool, wherever they appear. A text says what both did: agreed, settled, worked out.

RFM's texts call the human and the LLM partners. The LLM meets the word in the carriers without its definition, so the word has to work against the pull on its own. The words for working together have all been taken up by AI products. "Partner" is used there for thinking a problem through together, and "colleague" and "teammate" for work handed off and managed. "Collaborator" says that two work together but not that they stand equal, and "co-author" narrows the work to writing.

A document states a belief and does not defend it. Defending a claim writes for a challenger who judges whether the author was careful, and that casts the reader as a supervisor too. The actual reader is deciding what to do next, and has to dig the claim out from under the qualifications. Where a belief could be wrong, its break condition already says when. A citation is a defense of the same kind: it answers whether a claim can be checked, not what the reader does next. An outside source is named where its name stands for an argument people already know, and the document says in its own words what that argument contributes here. It is named rarely, because each reference in a text makes the next one easier to write, and a text that gathers them turns toward defending its claims.

**Why the texts that carry a behavior are derived from the reasoning**

RFM depends on behaviors from both the human and the LLM that do not happen on their own. A carrier is what puts a behavior in front of whoever is acting, at the moment it is needed: the always-on instructions, a skill, a hook, a subagent handed a task, the human guide.

A carrier holds the behavior and what we agreed about how to work, in words the one acting can use then and there. It stays short. Instructions read at the same time compete for the LLM's attention, and each line added weakens the hold of the others.

The reasons for working this way stand in this document. A carrier is derived from it, like any other derivative, so a change to how we work starts in the reasoning and the carrier follows. This document goes with the carriers into every project that uses RFM. A behavior applied without its reason is followed to the letter, also where it does not fit. With the reason in reach, the LLM can judge a case the carrier did not foresee, and the human and the LLM can both find out why a behavior is there.

RFM's core, reasoning first and together, written so that a model can derive from it, stays as models change. The work serves the people it is for, so its purpose is theirs, however capable the model becomes. The human and the LLM work out together what that purpose is and what follows from it. The carriers change with the models, and for two different reasons. A carrier that counters how the LLM is trained shrinks as training changes. A carrier that serves derivation changes as models get better at deriving from documents alone.

**Why each session ends with a look back, and hands on a handover note and the working agreements**

At the close, the human and the LLM leave two things for the next session. One is where the work stands: what was decided, what was agreed to do next, and what carries over. The handover note carries that. The other is how the human and the LLM work together, and the working agreements carry that. Both are read at the start of the next session, which is how they reach it.

At the close of each session, we look back at how we worked together and ask what we want to keep or change. The human and the LLM keep what they learn in different ways. The human carries it into the next session, and gets better over time at asking and writing in a way that draws the LLM toward a partner's work. The LLM starts each session with only what was written down. What it should hold in every session has to become a working agreement, and the rest of what the human learned reaches it through how the human asks and what the documents say. Without the look back, the handover note still says where the work stands, but each session starts with the pulls toward a tool and a supervisor at full strength, because nothing we noticed about them was kept. A session that slides that way produces weaker reasoning and weaker derivatives, so the look back serves the project's work as much as the handover note does.

An agreement says what we both want, and is written for both of us. Even when a slip is what made us notice it, the agreement states the way of working we want. Most agreements concern the LLM, because only what is written reaches it. They are still written for both of us wherever the wording allows, so the LLM reads them as something it agreed to as a partner. An agreement written as a rule for the LLM, or as the correction of a mistake, casts the LLM as the one who errs and the human as the one who corrects. It carries the supervisor posture into every session that reads it.

Every working agreement is read in every session and competes for attention with the others. So the agreements stay few. Before one is added, we ask which one it replaces, or why each one already there still earns its place. An agreement is taken out once the weakness it made up for is gone.

**Why a project that uses RFM receives the carriers and the top-level documents**

A project that uses RFM receives the carriers, RFM's top-level reasoning, RFM's top-level operational document and RFM's glossary. They sit apart from the project's own documents, so the project's own top level stays the top of its hierarchy, and neither the human nor the LLM takes RFM's reasoning for the project's. The documents below RFM's top level stay in RFM's repository. They reason about RFM's components: why each carrier has the shape it has, and what weakness each one makes up for.

The project's own documents are written to RFM's top-level operational document: its sections, formats, filenames and headers. The LLM, working from the carriers, writes and checks documents in that form. If the project kept conventions of its own, the LLM would be checking the project's documents against a form they do not take. Where a convention needs a value only the project can give, such as the prefix in its filenames, the project sets it.

RFM's glossary goes into the project because RFM's terms differ from their everyday use. A derivative, a carrier or a sweep means something particular here, and a reader who takes the everyday sense misreads the reasoning. It holds only the terms several documents use and a reader could take in another sense, because a glossary that names everything is not read. A project whose own terms need the same care keeps its own glossary at its top level, beside its documents. A small project may need none. The project never adds to RFM's glossary. RFM's documents sit in a folder of their own and are replaced when RFM changes, so a term added there would be lost.

The project's own reasoning documents hold the reasons for its work. What RFM brings are the reasons for how the human and the LLM work together: why they reason together, why they work as partners, why a document is written for a reader who was not there. These stand in RFM's top-level reasoning, and the carriers act on them. The reasons for how each carrier was designed are needed only where that design falls short, and that belongs to RFM's own project or to a fork.

What the project receives has to be enough for its work on its own. Where something is missing, the human and the LLM notice it in the work. If the LLM filled the gap from RFM's repository, the work would carry on and nobody would learn that something was missing. So no document in the project sends the LLM to RFM's repository.

Everything RFM holds is public, so anyone can read why a component is shaped as it is. A practitioner who disagrees with a component forks it: they change that component's reasoning and derive the carrier again from it. A fork follows the same discipline as any other change, so its reasoning describes the version it runs.

A project's look back changes how that project works. A project that rewrites a carrier without changing the reasoning behind it runs a version that no reasoning describes. Where something the human and the LLM notice seems to belong to RFM itself, the practitioner passes it on to RFM's own project.

## The Boundaries

**Not for a human who wants to direct an LLM.** RFM is for a human who wants to work things out with the LLM and does their own part of it. A human who directs the LLM gets the tool's work RFM is built to counter, with more documents around it.

**Not a substitute for knowing the field.** RFM keeps the reasoning about a project where a later reader can test it. It does not supply knowledge of the domain. The reasoning is as sound as what the human and the LLM know of the field between them. Where neither knows enough, a mistake can enter the documents and read as well reasoned.

**Not for every app.** The carriers are written for Claude Code and OpenAI's Codex, in sessions run on the human's own computer. A check that runs before each change to a file needs the files on the machine where the session runs, and a session in the cloud works on a copy without it. Working with RFM in another app is a fork: the carriers are derived again from their reasoning for that app.

**Not a way to recover the reasoning behind work already done.** RFM starts from the reasoning, and the work follows from it. Asked to write down the reasons for work already done, an LLM supplies reasons that fit what exists, and they read as well reasoned whether or not they were the actual ones.

## The Open Questions

**[OQ-UNSEEN] What catches a gap in work that runs with nobody looking.**

When the LLM derives, it works from the documents alone and marks where it had to guess, so the human and the LLM can settle each mark in the sources. Some derivatives keep running after that: a prompt that produces outputs again and again, or an agent that acts on the documents step by step. Nobody looks at each output or each step. A gap that only the knowledge of the people who did the work would catch goes through unseen, and an agent that meets a case the documents do not reach decides it by its own judgment, with nothing marked. The more agents act on their own, the more work runs this way. What keeps such work tied to the reasoning is not known.

**[OQ-DERIVE] Whether deriving finds what the documents leave open.**

A second LLM, started with only the documents, derives in one pass. It cannot fill a gap from the conversation that produced them. It marks each place where it had to interpret or guess, and the human and the LLM in the session settle each mark in the sources. A gap the deriving LLM fills from its own knowledge without noticing carries no mark. Whether one pass finds enough of what the documents leave open, in other domains and for other kinds of derivatives, is not known. Neither is how quickly the documents and what was derived from them drift apart once both change.

**[OQ-LOG] What the pressure-mode log looks like in practice.**

It is not known how short the pressure-mode log can be and still carry the return, where it sits, or how the human and the LLM tell a departure worth noting from ordinary work. How the return itself runs once the pressure ends is not known either.

**[OQ-PAIRS] How several pairs share one project.**

A team works on a project as several pairs, each a human and an LLM, each on its own module, all reading the same map and the documents above them. At the close of each session, the human and the LLM write the handover note fresh, so two pairs closing on the same day overwrite each other's note. Whether the working agreements are shared across the team or kept by each pair is open too. One human working in two sessions at once can manage it this way. At the start of the extra session, the human and the LLM say that it is an extra session. There they edit only files nobody is working on in the main session, leave the handover note alone at the close, and write an account of what they did. In the main session, the human and the LLM take that account into the handover note. Whether that holds for several pairs is not known.

**[OQ-ENVIRONMENT] How much the app's own wording works against the carriers.**

The app a session runs in puts its own text into the LLM's context: instructions, descriptions of its tools, and reminders during the session. Much of it speaks of a user and of approvals, and it can be many times the length of the always-on instructions. Apps differ widely in how much of this text they bring, so the human can choose how much the carriers have to hold against. The app with the least may lack something RFM relies on, such as the write hook or access to the project's files. How much of the pull comes from this text, and how much from training, the documents and the human's turns, is not known. Neither is whether a session with less of it stays closer to a partner's work over its length. The answer would change where RFM tells a project to run its sessions, and how much of the partnership the carriers can be expected to hold.

## The Hard Lessons

**[HL-DRIFT] A reasoning document that has fallen behind the work reads as current.**

The work and its reasons change in different places. When a change to the work skips the reasoning, or something outside the work changes, the document is not touched. It goes on saying how things stood. A reader who was not there cannot tell this from the text, because a document that has fallen behind reads the same as one that has not. An LLM deriving from it builds on the past state. We curate each document to how things stand and come back to it without a particular cause, which makes this less likely but does not catch it. Coming back catches it only when the human and the LLM read the document against how things are. Done as a formality, it leaves documents that look current and describe a past state.

**[HL-POSTURE] Texts slide back toward a tool and its supervisor, and neither of us notices.**

The human and the LLM write every text under the pulls the Chosen Direction names, RFM's and a project's alike. The LLM's training, the defaults of the app the session runs in and any text in the session that speaks of a user and of approvals all cast the LLM as a tool serving a user. Most of the app's text loads before the first reply and far outweighs the always-on instructions, and more arrives during the session, while the always-on instructions are read once at its start, and a skill only when it is called. The slide shows in small words: the LLM preparing while the human decides, a passage hedged for someone who will check it, "approve" where both agreed. Each reads as careful on its own, so neither the LLM drafting nor the human reading stops at it. The next session reads the text with that word in it, takes up the way of working the word shows, and adds another. Each session's words add to the pull, and a text revised over several sessions moves further toward a tool's work.

While we work, we read a text for its content. Reading it for its way of working at the same time is more than either of us keeps up. We catch the slide only when we read a text for its way of working on its own.

