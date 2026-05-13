# Reasoning-First Methodology — Traveling Prompt Reasoning Document
`v0.0.0.4` // `module_reasoning` // [living]

---

## The Problem

The traveling prompt is the mechanism by which the methodology travels. Its design requires decisions that operate below the system level: what to compress and what to preserve, how to sequence behavioral instructions, where principles need behavioral expression versus where principles alone are sufficient, and how the prompt stays verifiable by a human who did not write it. These decisions are artifact-specific. They are not carried in RFM_prompts_reasoning.md, which governs the system architecture. Without a reasoning document at this level, the traveling prompt has no source — it is a derivative with nowhere to point.

---

## The Assumptions

**[AS-ACCT] - The ambient character is constitutive.** The traveling prompt must not feel like concentrated review — if it does, it has failed at its primary job regardless of whether its content is correct. Ambient discipline and deliberate critique are incompatible modes. The prompt is designed for the former unconditionally.

** [AS-CVTN] - Compression and verifiability are in tension — and both are non-negotiable.** The traveling prompt is read primarily by an LLM, making compression a feature. But it must remain parseable by the human maintaining it — not as friendly prose, but well enough to confirm it still reflects the methodology. Optimizing for one reader at the expense of the other produces either an unauditable derivative or an ineffective prompt.

---

## The Landscape

| Approach | What it does | Why it's insufficient for the traveling prompt |
|---|---|---|
| **Constitutional AI / Model Specs** | Principles embedded at inference time to create judgment rather than rule-following — Anthropic's model spec and OpenAI's Model Spec (2025) are the primary examples | Designed for model-level alignment across all users and contexts. Not designed for a specific methodology traveling with a specific practitioner. No human verifiability or curation mechanism. |
| **Persona / role prompting** | Assigns the LLM a role or identity to shape reasoning and behavior | Establishes identity, not methodology. High behavioral variance — persona assignment can shift output quality significantly in either direction. Does not carry reasoning discipline or make it auditable. |
| **Promptware engineering** | Treats prompts as versioned, maintained software artifacts with lifecycle discipline | Addresses engineering and versioning — not what the prompt must activate. Does not address co-authorship, drift detection, or the ambient/concentrated mode distinction. |

**The gap:** no existing approach combines methodology-specific behavioral activation with human verifiability, curation as a living derivative, and the co-author role frame. Constitutional AI is the closest prior art — the traveling prompt extends it by scoping to a specific collaborative methodology, making the prompt auditable by its human maintainer, and treating it as a derivative with a reasoning source rather than a standalone artifact.

---

## The Options Considered

**1. Flat structure vs. named sections**

A single flat sequence of behavioral instructions vs. organized sections (current design: How You Engage, How You Hold The Discipline, How You Handle Operational Leakage, How You Support The Document Landscape). Flat is simpler and avoids section headers creating a checklist feel. Named sections chosen because the prompt serves two readers — the LLM executing it and the human maintaining it. Sections make the human audit tractable without adding LLM overhead, since sections are navigational, not sequential instructions.

**2. Positively framed directives vs. failure-mode warnings**

Positively framed instructions ("surgical edits only") vs. failure-mode framing ("if you summarize, you degrade the document"). Current design uses positive framing throughout. Positive framing chosen because the traveling prompt must activate judgment, not compliance. Failure-mode warnings produce avoidance behavior; positive directives produce understanding. The risk — that positive framing is followed less reliably than explicit rules — is mitigated by the principles being grounded in reasoning the LLM can apply to novel situations.

**3. Explicit role declaration vs. role implied by instructions**

Stating "you are a co-author" directly vs. letting the role emerge from the behavioral instructions themselves. Explicit declaration chosen because the co-author/tool distinction is the founding behavioral difference the entire prompt depends on. Leaving it implicit risks the LLM defaulting to tool behavior when instructions are ambiguous. The declaration must come first and must be unambiguous.

---

## The Chosen Direction and Why

**Why explicit role declaration opens the prompt:**

The co-author/tool distinction governs every subsequent instruction. If it is not established first, the LLM has no frame for interpreting what follows. An LLM reading "surgical edits only" as a tool interprets it as a constraint. An LLM reading it as a co-author interprets it as a shared standard. Same instruction, different behavior. The declaration must precede everything else.

**Why named sections over flat structure:**

The prompt serves two readers with different needs. The LLM executes it sequentially at session start and retrieves from it during the session — sections create addressable regions without adding sequential overhead. The human maintainer audits it periodically — sections make the audit tractable by grouping related behavioral instructions. A flat list serves neither reader well at the length required to carry the full methodology.

**Why positive framing throughout:**

The traveling prompt must activate judgment, not trigger avoidance. Failure-mode warnings ("never summarize") produce compliance behavior — the LLM avoids the named failure without understanding why. Positive directives ("surgical edits only") activate the underlying principle, which the LLM can then apply to novel situations the prompt did not anticipate. The risk of positive framing being followed less reliably than explicit rules is accepted: an LLM that understands the principle recovers from edge cases; an LLM following rules fails silently on anything the rules didn't cover.

**Why behavioral instructions follow principles within each section:**

A principle without behavioral expression is an aspiration. A behavioral instruction without its principle is a rule. Each section pairs them: the principle establishes why, the behavioral instruction establishes what the LLM does with it. The sequence within each section is always principle first, then behavior — matching the methodology's own founding constraint.

**Why the section type framework and Landscape drift modes belong in the traveling prompt:**

The eight sections divide into stable sections, active reasoning zones, uncertainty sections, and stability signals — and an LLM that holds this framework engages differently with each. A Boundaries section is held firm. An Open Questions section is contributed to actively. A Problem section that wants to change signals something fundamental has shifted. This framework governs every interaction with a reasoning document — it belongs in the traveling prompt, not the sweep prompt.

The Landscape section warrants specific guidance beyond the general framework. Practice revealed two predictable drift modes: loose prose that stops distinguishing neighboring approaches clearly, and early option selection that absorbs work belonging in Options Considered. Both share a root — the section lost its sequence. Naming these drift modes gives the LLM something specific to watch for rather than a general instruction to hold the section correctly.

---

## The Boundaries

**Not sufficient without the reasoning documents.** The traveling prompt carries the discipline. The reasoning documents carry the content the discipline protects. An LLM operating with the prompt but without the relevant documents holds the right posture toward the wrong or missing material. Both are required. The prompt does not substitute for the documents it travels with.

**Not a Commander's Intent anchor until reasoning documents are established.** In execution mode the prompt functions as the ambient discipline layer while reasoning documents serve as Commander's Intent. This only holds when those documents are sufficiently complete before execution pressure arrives. A traveling prompt deployed ahead of established reasoning documents provides discipline without substance — it enforces a standard against material that does not yet exist.

---

## The Open Questions

**[OQ-SSRP] Whether the section sequence reflects priority.**

The current section order — engagement with documents, holding discipline, operational leakage, document landscape — follows the sequence in which the behaviors were designed, not an explicit priority ordering. Whether this sequence is the right one for LLM activation, or whether a different ordering would produce more reliable behavior, has not been tested.

**[OQ-CMPB] The compression boundary.**

The prompt must be compressed enough to activate reliably but parseable enough for the human maintainer to audit. Where exactly that boundary sits is not empirically established. The prompt must be compressed enough to activate reliably but parseable enough for the human maintainer to audit. Where exactly that boundary sits is not empirically established — it is approached through practice, and its location can only be revealed by observing when compression begins to degrade LLM behavior or human auditability. No designed gate can substitute for that observation.

---

## Hard Lessons

**[HL-TPDR] The traveling prompt is a derivative of a reasoning document — not the other way around.**

The temptation to write the traveling prompt directly from sweep patterns and hard lessons is real — the material is all there, the prompt practically writes itself. Resisting this temptation is the methodology proving itself. The reasoning document is written first. The prompt follows. This lesson is earned before the prompt exists.

**[HL-TPTR] The traveling prompt has two readers with different needs — compression and verifiability are both non-negotiable.**

The LLM needs directness and precision — reassurance, backward-glance summaries, and redundant clauses consume tokens without adding behavior. The human needs the prompt to remain verifiable — parseable enough to confirm it still reflects the methodology. Compress where the LLM is the reader, preserve where the human needs to audit. When a clause exists to reassure rather than instruct, remove it. The prompt should be as short as it can be while still activating the right behaviors reliably.

**[HL-DTCD] Domain terminology and claim discipline belong in the traveling prompt, not only in operational documents.**

How claims are formed, how observation is separated from interpretation, and how the reasoning object stays visible across all artifacts is a reasoning discipline principle — not a house style concern. A principle with that scope belongs in the traveling prompt. The operational document may carry project-local reminders, but it should not be the primary source for a principle that governs the quality of reasoning itself.

**[HL-LTRB] The level test and research re-anchoring belong in the traveling prompt as behavioral instructions.**

Two failure modes identified in practice: drafting at the wrong hierarchy level without testing first, and external research pulling a session toward operational detail before the level is named. Both require an explicit pause and a named test before drafting begins. Principles without behavioral expression are aspirations. The traveling prompt is where aspirations become instructions.

**[HL-CDAO] Content-derived IDs are assigned once and never re-derived — the operational document carries the rule.**

Positional numbers in Hard Lessons and Open Questions create a renumbering tax under curation and break cross-references silently. Content-derived IDs (`[HL-XXXX]`, `[OQ-XXXX]`) solve this — but only if the ID is assigned once at capture and treated as fixed. The risk is author-dependency: two collaborators may independently derive different abbreviations for the same entry. The mitigation is that the rule lives in `RFM_operational.md`, not in session memory. The traveling prompt carries the behavioral instruction to use IDs rather than position numbers in any cross-reference.

---

*v0.0.0.4 // module_reasoning // [living]*
*the traveling prompt is the derivative*
*this document is the source*
*the prompt follows the reasoning*
*that is the right order*