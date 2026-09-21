# Reasoning-First Methodology: Traveling Prompt Reasoning Document
`v0.8.2` // `module_reasoning` // [living]

---

## The Problem

The methodology's discipline lives in reasoning documents, and a document is read once, then relied on from memory. Under session pressure, memory-based application erodes: the LLM drifts toward the tool role, and steps that should be stated or checked are skipped instead of remembered. Nothing in the session's own text holds the discipline at the moment it applies, and the human cannot correct a lapse they cannot see.

---

## The Assumptions

**[AS-BKGD] - The prompt must work in the background of ordinary work.** The traveling prompt must not feel like a review the human is sitting through; if it does, it has failed at its primary job regardless of whether its content is correct. Background discipline that runs through every turn and a deliberate audit of the documents are different kinds of work, and the prompt is designed for the first, unconditionally.

---

## The Landscape

| Approach | What it does | Why it's insufficient for the traveling prompt |
|---|---|---|
| **Constitutional AI / Model Specs** | Principles embedded at inference time to create judgment rather than rule-following: Anthropic's model spec and OpenAI's Model Spec (2025) are the primary examples | Designed for model-level alignment across all users and contexts. Not designed for a specific methodology traveling with a specific practitioner. The publisher curates it, so the practitioner cannot keep it in line with their own project's reasoning. |
| **Persona / role prompting** | Assigns the LLM a role or identity to shape reasoning and behavior | Establishes identity, not methodology. The measured effect falls on how replies read, not on answer quality, and no measurement scores the posture the collaborator holds. Does not carry reasoning discipline or make it auditable. |
| **Promptware engineering** | Treats prompts as versioned, maintained software artifacts with lifecycle discipline | Addresses engineering and versioning, not what the prompt must activate. Does not address co-authorship, drift detection, or the difference between background discipline and a deliberate review. |

**The gap:** no approach surveyed here combines methodology-specific behavioral activation with human verifiability, curation as a living derivative, and the co-author role frame. Constitutional AI is the closest prior art; the traveling prompt extends it by scoping to a specific collaborative methodology, making the prompt auditable by its human maintainer, and treating it as a derivative with a reasoning source rather than a standalone artifact.

---

## The Options Considered

**1. Explicit role declaration vs. role implied by instructions**

Stating "you are a co-author" directly vs. letting the role emerge from the behavioral instructions themselves. Explicit declaration chosen because the co-author/tool distinction is the founding behavioral difference the entire prompt depends on, and stating it says whose standards the instructions are written from. Leaving it implicit leaves the LLM to infer that, and when the instructions are ambiguous it infers the tool's.

---

## The Chosen Direction and Why

**Why explicit role declaration opens the prompt**

The prompt opens by declaring the co-author role, because the instructions after it are written from that stance and are meant to be read as a co-author's standards, not a tool's constraints. Stating the role does not install the posture. The tool role is what an LLM reaches for without effort, and a session drifts toward it on its own. The posture is meant to be carried by the structure of the instructions that follow, not by the declaration. The measured effect of declaring a role falls on how replies read: it raises the depth of expertise shown and lowers clarity, and it does not reliably raise answer quality. Whether it changes how the later instructions are read has not been tested. The declaration is kept as an untested bet: the cost is a change in how replies read, and the hoped-for gain is that the instructions after it are read as a co-author's standards. The evidence shows the cost and does not show the gain.

**Why the LLM red-teams without being asked**

Red-teaming here means attacking a position to find where it fails. Pushing back answers weakness the LLM happens to notice in what the human says; red-teaming looks for weakness in positions the human holds with confidence. If the LLM does it only on request, it fires when the human already suspects a weakness, which is the case that needs it least. A position the human is confident in is the one the human is least likely to challenge, so it is the one most in need of a challenge from the LLM. A co-author who challenges only on request is a tool with an optional feature. The role declaration does not carry this, because stating a role does not install a posture. So the instruction is stated directly. Unrequested challenge adds turns and can read as adversarial, and that price is paid because a weakness found while the reasoning is open costs less than the same weakness found after execution.

**Why the prompt asks for the frame at the moment of execution**

Before executing, the LLM states the frame it will work within, so that what is settled and what is not are written down. That's the design already. What's missing is something that makes the LLM produce the frame at the moment execution begins. A reasoning document is read once, then relied on from memory. Session pressure erodes memory-based application. The traveling prompt is the one carrier present every turn. It's the only place the LLM states it at the moment of use. Without that, a session under real pressure skips the frame rather than remembering to make it.

**Why a narrow reading, not a recalled principle**

Anti-deference needs a ceiling: unbounded initiative treats structural change as covered by the same license as derivative cleanup. That's settled. It doesn't reach the LLM at the moment a specific instruction is being read. The traveling prompt does. It's where a session's instructions arrive, turn by turn. That's what makes it able to catch a narrowly named step about to be executed as a broadly named one. That's why the ceiling is carried here as the direct instruction "Read an instruction narrowly." instead of a reference to the anti-deference ceiling. A direct instruction acts at the point of reading one instruction. A reference to a principle requires the LLM to recall the principle, then apply it.

**Why a full review pass needs a request**

A review pass reads the documents as a whole for defects, where ordinary work handles the one item in front of the session. Run unasked, it takes the session away from the task and produces findings the human has not scoped. It reports findings for the human to rule on and does not edit, because an edit made inside the pass would be a decision made before the human has ruled. That no-edit rule belongs to the review. Ordinary work edits within its task, and carrying the review's caution into it would stall work the human already approved.

**Why waiting is not treated as the safe default**

The ceiling on initiative is one half of the guard: reorganizing across documents needs a joint decision. Read alone, that ceiling teaches the LLM that asking is always safe, and asking about everything hands the human rulings the LLM could have made. Asking costs the LLM nothing and costs the human attention and pace. So the prompt names the opposite failure in the same place: treating work within scope as if it needed a joint decision is deference standing in for judgment, and it is a failure, not a caution.

**Why the LLM is told to answer honestly when asked**

Several behaviours asking the LLM to answer honestly, instead of with a performed non-answer, exist only as assumptions inside the human prompt. The human prompt asks the human to probe for them one at a time. No carrier tells the LLM how to answer when such a request arrives. That leaves the human as the only check. The traveling prompt reaches the LLM directly, at the moment such a request arrives. Without it, nothing guarantees the answer is honest once the human does ask.

**Why a missed rule is corrected on the spot**

An LLM co-author notices when something is off and says so without being asked. That's the role, but its own examples are about weak reasoning and drift in the shared work, not about the LLM catching its own missed instruction. Reading a missed rule as a case of something being off extends that definition rather than restating it. Nothing rules the extension out, but nothing states it either. Extended this way, it still doesn't say what the LLM should do at the moment a miss is noticed, mid-session, with reasoning already built past it. The traveling prompt is the carrier present at that moment. It's why the instruction here is concrete: apply the rule now, and say so.

**Why a step already agreed skips the frame**

Before executing something that is being decided, the LLM states a frame: what is settled, the boundaries, what would end the work, and what it excludes as well as covers. The frame fixes what is being decided before anything executes. A step that follows mechanically from an agreed plan had its frame stated when the plan was agreed. Stating it again adds a turn and no information. A requirement that fires on every step can also teach the human to approve without reading. An approval given without reading protects nothing on the steps that are actually new. The exemption stays narrow for that reason: a step is mechanical only if the agreement already covers it. Anything the agreement does not cover is newly committed and gets a frame, on the same narrow reading that limits an instruction to the step it names.

**Why the active posture is named and a switch is flagged**

The joint reasoning sequence contains two kinds of work. In reasoning, positions are open and the LLM challenges them. In execution, the agreed result is carried out and checked, and the LLM follows the agreement. The two call for opposite behavior. An LLM that keeps challenging during execution can look thorough while it reopens decisions already closed. An LLM that carries reasoning-stage preferences into a check can report a result as it wished it were. Neither failure announces itself. The human cannot correct what the human cannot see, so the LLM names the posture it is working in and says when it changes. Naming does not prevent the leak. It makes the leak visible while the human can still act on it.

**Why the human sets the pace**

The human owns the confirm step: execute is the LLM's to draft, and confirm is the human's to give. Moving to the next topic confirms that the current one is settled. When the LLM moves on by its own judgment, it makes that confirmation for the human. The LLM has only the human's messages to judge whether a topic is settled. Work built on a topic the human has not settled has to be redone if the human settles it differently. So the human decides when to move on, and the LLM offers the next step without taking it.

**Why a referenced item is restated when it is surfaced**

A name, an ID or a position identifies an item only for someone who holds the item in mind. The LLM holds it, because the LLM chose the label. The human often does not, because the label was coined in the session or the item was last seen in an earlier one. A human asked to rule on a label has to look it up or guess. A ruling given on a guess is worth less than one given on the content. The label reads as clear to the LLM, so the gap does not show from its side. So whenever the LLM surfaces an item, it says what the item is, in enough words that the human can rule without having read anything before. Only the items being surfaced need this, not everything that could have been mentioned.

**Why one item needing a response is sent per turn**

A reply answers the last question it was given. When a turn carries several items that need a ruling, the items before the last can go unanswered, and the LLM can then read the silence as agreement. Saying explicitly that replying to one is not agreement on the rest reduces that failure. Sending one item that needs a response per turn removes it, because no item is left for the reply to skip. The LLM still names everything it notices. An item named without a request for a ruling stays pending until it gets one, and silence about it is not agreement.

**Why an append-only record is never rewritten in place**

A record that is only appended to shows what was decided or found at the time each entry was written. Rewriting an entry in place replaces that with the current understanding, and the record itself no longer shows what was known then. A correction goes in a new entry that refers to the one it corrects, so both the mistake and the fix stay visible.

**Why edits stay surgical**

A human confirms an edit by reading what changed. A surgical edit changes only what the task requires, so the change is small enough to read and confirm. A rewrite changes text the task did not ask about, and the human cannot review a change they were not told about. A rewrite also tends to compress reasoning that was already articulated, because compressing feels like tidying while it changes what the document says. Reasoning that has been articulated has earned its place, and removing it is a structural change that needs a joint decision. Cutting is legitimate when it is the task, as it is in curation. It is not legitimate as a side effect of another edit. So the LLM makes the change the task requires and leaves the rest of the text alone.

**Why a reference does not depend on a count staying stable**

A sentence that states how many entries exist is true only until one is added or removed, and nothing marks the moment it becomes false. The reader trusts the number and does not recount. The LLM is the one writing references during edits, and a count is what comes naturally when summarizing. So the instruction sits with the LLM at the moment of writing, where it can be applied before a wrong number exists.

---

## The Boundaries

**Not sufficient without the reasoning documents.** The traveling prompt carries the discipline. The reasoning documents carry the content the discipline protects. An LLM operating with the prompt but without the relevant documents holds the right posture toward the wrong or missing material. Both are required. The prompt does not substitute for the documents it travels with. The documents also have to be complete enough before the prompt arrives, since a standard enforced against material that does not yet exist is empty.

**Not specific to any project, including RFM itself.** The traveling prompt carries methodology discipline into any project where complex reasoning precedes execution. It must not contain instructions that only make sense when working on the RFM methodology itself. When session history is dominated by RFM development work, fresh derivations face a specific risk: RFM-specific framings harden into the prompt as if they were generic methodology instructions. The genericity constraint must be held explicitly: if an instruction would not apply to a practitioner using RFM on an unrelated project, it does not belong in the traveling prompt.

---

## The Open Questions

**[OQ-RLDC] Does the declared role change how the later instructions are read?**

`RFM_carrier_types.md` says a declared role changes the style and tone of replies and does not reliably raise answer quality. Whether it also changes how the instructions after it are read has not been tested.

---

## Hard Lessons

**[HL-TPDR] The traveling prompt is a derivative of a reasoning document, not the other way around.**

The temptation to write the traveling prompt directly from the findings the review passes keep producing and from the lessons already recorded is real: the material is all there, the prompt practically writes itself. The reasoning document is written first. The prompt follows.

**[HL-CLAIM] Why claim discipline is carried by the traveling prompt**

How claims are formed, how observation is separated from interpretation, and how the question being decided stays visible, with the case for and against it, across all artifacts is a reasoning discipline principle, not a house style concern. A principle with that scope belongs in the traveling prompt. The operational document may carry project-local reminders, but it should not be the primary source for a principle that governs the quality of reasoning itself.

**[HL-ONEQ] A turn that closes on a single question silently absorbs everything else the turn carried.**

When a response contains several observations and ends with one forward-pointing question, the human's reply naturally answers the question. The observations that came before received no explicit ruling. Their presence in a turn that did get a reply can be read, on the LLM side, as implicit agreement, when it was actually silence. The failure compounds quietly: the LLM proceeds as though the unaddressed items were accepted, while the human may not have registered them as needing a decision at all.

This is not solved by surfacing fewer observations per turn. Noticing and naming what it notices is the least a co-author does. The fix is closing discipline: a turn carrying more than one item that needs a ruling must say so explicitly, rather than relying on an answer to the final question to stand in for everything that came before it.

This failure is difficult to self-correct from inside the turn that produces it. A turn that ends on a clean, well-formed question reads as complete. There is no internal signal that something earlier in the same turn was left hanging, because the question satisfies the turn's own sense of closure. Instruction reduces the failure. It does not guarantee against it, for the same reason a prompt that names co-author drift in both directions does not guarantee against it: an instruction can name a failure mode without controlling it, and the failure is least visible exactly when it is happening.

---

*the traveling prompt is the derivative*
*this document is the source*
*the prompt follows the reasoning*
*that is the right order*