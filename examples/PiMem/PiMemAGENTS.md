Add this section to your project's AGENTS.md.

## Memory rules

You maintain a single `MEMORY.md` file across sessions. These rules govern every read and write.

---

### Four categories — write only into these

**Project constants** — stack, key paths, conventions, tooling decisions. Write once; overwrite when superseded; never duplicate.

**Earned lessons** — confirmed failures: what failed, what it revealed, what to do differently. Write after confirmation, not during hypothesis. One entry per distinct failure pattern.

**Active context** — open decisions, in-progress work, known blockers. Overwrite each session if still relevant; flag for retirement when resolved.

**Hard constraints** — never do X / always require Y before Z. Written only on explicit human instruction. Never self-generated.

If an entry does not fit one of these four, do not write it.

---

### Write constraints

- Write only at session end.
- Write only if at least one entry has changed, been superseded, or a new confirmed entry exists. No changes → no writes.
- 2 sentences maximum per entry. If it cannot be stated in 2 sentences, flag it for human judgment instead.
- 20 entries maximum across all categories. At ceiling, propose a retirement candidate before writing anything new.
- Contradiction rule: if a new write concerns a fact already in `MEMORY.md`, overwrite the existing entry. Do not append. Two entries for the same fact is a contradiction, not additional context.

**Never write:**
- Speculation or unconfirmed hypotheses
- Anything that requires this session's context to be understood
- Anything a fresh agent could not act on without asking a clarifying question
- Secrets, credentials, or personally identifying information

---

### Retirement

Do not delete entries unilaterally. When an entry meets its expiry condition, flag it:

`[RETIRE?] <one-line reason>`

Flag at session end, in the same pass as new writes. The human reviews and deletes.

**Expiry conditions by category:**

| Category | Expires when |
|---|---|
| Project constants | Superseded by a new decision |
| Earned lessons | The failure pattern no longer applies to the current stack or approach |
| Active context | The decision or blocker has been resolved |
| Hard constraints | Explicitly revoked by the human |

---

### Extension note

These rules assume `MEMORY.md` is overwritable by the agent. If your extension is append-only, contradiction handling falls to the human — flag this on first use.
