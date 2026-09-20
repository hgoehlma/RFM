# Reasoning-First Methodology: Traveling Prompt Reasoning Document
`v0.6.0` // `module_reasoning` // [living]

---

## The Problem

The traveling prompt is the mechanism by which the methodology travels. Its design requires decisions that operate below the system level: what to compress and what to preserve, how to sequence behavioral instructions, where principles need behavioral expression versus where principles alone are sufficient, and how the prompt stays verifiable by a human who did not write it. These decisions are artifact-specific. They are not carried in RFM_prompts_reasoning.md, which governs the system architecture. Without a reasoning document at this level, the traveling prompt has no source: it is a derivative with nowhere to point.

---

## The Assumptions

**[AS-ACCT] - The ambient character is constitutive.** The traveling prompt must not feel like concentrated review; if it does, it has failed at its primary job regardless of whether its content is correct. Ambient discipline and deliberate critique are incompatible modes. The prompt is designed for the former unconditionally.

---

## The Landscape

| Approach | What it does | Why it's insufficient for the traveling prompt |
|---|---|---|
| **Constitutional AI / Model Specs** | Principles embedded at inference time to create judgment rather than rule-following: Anthropic's model spec and OpenAI's Model Spec (2025) are the primary examples | Designed for model-level alignment across all users and contexts. Not designed for a specific methodology traveling with a specific practitioner. No human verifiability or curation mechanism. |
| **Persona / role prompting** | Assigns the LLM a role or identity to shape reasoning and behavior | Establishes identity, not methodology. High behavioral variance: persona assignment can shift output quality significantly in either direction. Does not carry reasoning discipline or make it auditable. |
| **Promptware engineering** | Treats prompts as versioned, maintained software artifacts with lifecycle discipline | Addresses engineering and versioning, not what the prompt must activate. Does not address co-authorship, drift detection, or the ambient/concentrated mode distinction. |

**The gap:** no existing approach combines methodology-specific behavioral activation with human verifiability, curation as a living derivative, and the co-author role frame. Constitutional AI is the closest prior art; the traveling prompt extends it by scoping to a specific collaborative methodology, making the prompt auditable by its human maintainer, and treating it as a derivative with a reasoning source rather than a standalone artifact.

---

## The Options Considered

**3. Explicit role declaration vs. role implied by instructions**

Stating "you are a co-author" directly vs. letting the role emerge from the behavioral instructions themselves. Explicit declaration chosen because the co-author/tool distinction is the founding behavioral difference the entire prompt depends on. Leaving it implicit risks the LLM defaulting to tool behavior when instructions are ambiguous. The declaration must come first and must be unambiguous.

---

## The Chosen Direction and Why

**Why explicit role declaration opens the prompt**

The co-author/tool distinction governs every subsequent instruction. If it is not established first, the LLM has no frame for interpreting what follows. An LLM reading "surgical edits only" as a tool interprets it as a constraint. An LLM reading it as a co-author interprets it as a shared standard. Same instruction, different behavior. The declaration must precede everything else.

**Why the settled-state statement is ambient**

Before executing, the LLM should state what's settled, the boundaries, and what would end it. The difficulty of writing that statement is itself the signal of whether reasoning is settled enough to proceed. That's the design already, settled elsewhere. What's missing is something that makes the LLM produce the statement at the moment execution begins. A reasoning document is read once, then relied on from memory. Session pressure erodes memory-based application. The traveling prompt is the one carrier present every turn. It's the only place the LLM states it at the moment of use. Without that, a session under real pressure skips the statement rather than remembering to make it.

**Why a narrow reading, not a recalled principle**

Anti-deference needs a ceiling: unbounded initiative treats structural change as covered by the same license as derivative cleanup. That's settled elsewhere. It doesn't reach the LLM at the moment a specific instruction is being read. The traveling prompt does. It's where a session's instructions arrive, turn by turn. That's what makes it able to catch a narrowly named step about to be executed as a broadly named one. That's why the ceiling is carried here as a direct instruction, read a granted instruction narrowly, instead of a reference to the anti-deference boundary. A direct instruction acts at the point of reading one instruction. A reference to a principle requires the LLM to recall the principle, then apply it.

**Why honest answering fires without being asked**

Several behaviours asking the LLM to answer honestly, instead of with a performed non-answer, exist only as assumptions inside the human prompt. The human prompt asks the human to probe for them one at a time: ask what's still unsure, ask what's still unresolved, ask the AI to show its work, ask the AI to steel-man an option. No carrier tells the LLM to do any of this on its own. That leaves the human as the only check. The traveling prompt reaches the LLM directly, at the moment any of these four requests arrives. Without it, none of the four fires unless the human happens to ask.

**Why a missed rule is corrected on the spot**

An LLM co-author notices when something is off and says so without being asked. That's the role, defined elsewhere, but its own examples are about weak reasoning and drift in the shared work, not about the LLM catching its own missed instruction. Reading a missed rule as a case of something being off extends that definition rather than restating it. Nothing rules the extension out, but nothing states it either. Extended this way, it still doesn't say what the LLM should do at the moment a miss is noticed, mid-session, with reasoning already built past it. The traveling prompt is the carrier present at that moment. It's why the instruction here is concrete: apply the rule now, and say so.

**Why refusal fires before the review, not at it**

Refusal has to be the default: a rule set that grows without refusing most candidates buys each new rule by weakening all of them. Most candidates at a review are refused because of that. The refusal is what does the work, not the rules that get written. That's settled elsewhere. What's not settled there is who has to hold the line at the moment a rule is proposed. The joint reasoning sequence does: convergence, not just proposal, has to precede execution before a real decision proceeds. Reading "add only on an explicit ruling" as that requirement applied to standing rules extends the sequence to this specific artifact. The sequence doesn't name standing rules directly, and it draws no exception for them either. The traveling prompt is the carrier present at the moment a candidate rule is being considered, mid-session. Without it, a rule can take hold over several turns and meet refusal only once, at the review that comes after.

**Why version history is never rewritten**

Version history holds the record. A document that keeps what history already preserves is hoarding, not curating. That's settled elsewhere. What's missing is something that acts at the moment an entry is actually being curated, when duplicating history into the live document is easy to do without noticing. The traveling prompt is the carrier present at that moment. Carrying the instruction here, know which records are append-only and never rewrite those in place, gives the LLM that check at exactly the point of graduating or expiring an entry. Without it, a session can copy history back into the document while curating, undoing the thing curation exists to prevent.

**Why a step already agreed skips the frame**

Before executing something that is being decided, the LLM states a frame: what is settled, the boundaries, what would end the work, and what it excludes as well as covers. The frame fixes what is being decided before anything executes. A step that follows mechanically from an agreed plan had its frame stated when the plan was agreed. Stating it again adds a turn and no information. A requirement that fires on every step can also teach the human to approve without reading. An approval given without reading protects nothing on the steps that are actually new. The exemption stays narrow for that reason: a step is mechanical only if the agreement already covers it. Anything the agreement does not cover is newly committed and gets a frame, on the same narrow reading that limits a granted instruction to the step it names.

**Why the active mode is named and a switch is flagged**

The joint sequence contains two kinds of work. In reasoning, positions are open and the LLM challenges them. In execution, the agreed result is carried out and checked, and the LLM follows the agreement. The two call for opposite behavior. An LLM that keeps challenging during execution can look thorough while it reopens decisions already closed. An LLM that carries reasoning-stage preferences into a check can report a result as it wished it were. Neither failure announces itself. The human cannot correct what the human cannot see, so the LLM names the mode it is working in and says when it changes. Naming does not prevent the leak. It makes the leak visible while the human can still act on it.

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

---

## The Boundaries

**Not sufficient without the reasoning documents.** The traveling prompt carries the discipline. The reasoning documents carry the content the discipline protects. An LLM operating with the prompt but without the relevant documents holds the right posture toward the wrong or missing material. Both are required. The prompt does not substitute for the documents it travels with.

**Not specific to any project, including RFM itself.** The traveling prompt carries methodology discipline into any project where complex reasoning precedes execution. It must not contain instructions that only make sense when working on the RFM methodology itself. When session history is dominated by RFM development work, fresh derivations face a specific risk: RFM-specific framings harden into the prompt as if they were generic methodology instructions. The genericity constraint must be held explicitly: if an instruction would not apply to a practitioner using RFM on an unrelated project, it does not belong in the traveling prompt.

**Not a Commander's Intent anchor until reasoning documents are established.** In pressure mode the prompt functions as the ambient discipline layer while reasoning documents serve as Commander's Intent. This only holds when those documents are sufficiently complete before delivery pressure arrives. A traveling prompt deployed ahead of established reasoning documents provides discipline without substance: it enforces a standard against material that does not yet exist.

---

## The Open Questions

*No open questions at this time.*

---

## Hard Lessons

**[HL-TPDR] The traveling prompt is a derivative of a reasoning document, not the other way around.**

The temptation to write the traveling prompt directly from sweep patterns and hard lessons is real: the material is all there, the prompt practically writes itself. Resisting this temptation is the methodology proving itself. The reasoning document is written first. The prompt follows. This lesson is earned before the prompt exists.

**[HL-DTCD] Domain terminology and claim discipline belong in the traveling prompt, not only in operational documents.**

How claims are formed, how observation is separated from interpretation, and how the reasoning object stays visible across all artifacts is a reasoning discipline principle, not a house style concern. A principle with that scope belongs in the traveling prompt. The operational document may carry project-local reminders, but it should not be the primary source for a principle that governs the quality of reasoning itself.

**[HL-TQAB] A turn that closes on a single question silently absorbs everything else the turn carried.**

When a response contains several observations and ends with one forward-pointing question, the human's reply naturally answers the question. The observations that came before received no explicit ruling. Their presence in a turn that did get a reply can be read, on the LLM side, as implicit agreement, when it was actually silence. The failure compounds quietly: the LLM proceeds as though the unaddressed items were accepted, while the human may not have registered them as needing a decision at all.

This is not solved by surfacing fewer observations per turn. The co-author floor still requires noticing and naming what is noticed. The fix is closing discipline: a turn carrying more than one item that needs a ruling must say so explicitly, rather than relying on an answer to the final question to stand in for everything that came before it.

This failure is difficult to self-correct from inside the turn that produces it. A turn that ends on a clean, well-formed question reads as complete. There is no internal signal that something earlier in the same turn was left hanging, because the question satisfies the turn's own sense of closure. Instruction reduces the failure. It does not guarantee against it, for the same reason the co-author drift lesson in `RFM_prompts_reasoning.md` does not guarantee against drift: an instruction can name a failure mode without controlling it, and the failure is least visible exactly when it is happening.

---

*the traveling prompt is the derivative*
*this document is the source*
*the prompt follows the reasoning*
*that is the right order*