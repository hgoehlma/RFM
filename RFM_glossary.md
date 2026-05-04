# RFM — Glossary
`v0.0.0.1` // `glossary` // [living]

---

## What this file is

This glossary disambiguates terms used in RFM documents that carry different meanings across reader contexts — words that look shared but aren't. Each entry records why the term means what it means here, not just what it means. Entries are added when a term appears in multiple documents and its meaning is likely to diverge across readers or contexts. Below that threshold, definitions belong inline where the term is first used.

---

| Term | RFM meaning | Risk of confusion |
|---|---|---|
| **Co-author** | Both the human and the LLM hold the co-author role — a working relationship in which both contribute to the reasoning, red team each other's thinking, and hold the methodology's discipline jointly. The non-obvious direction: the LLM is a co-author, not a tool. A co-author notices when something is off and says so without being asked. | Commonly used as a writing credit or to denote a human collaborator. In RFM it denotes a role with behavioral obligations, held by both parties. |
| **Compression** | Always a structural change — the loss of reasoning signal from a document, regardless of how it presents. Compression can appear as curation, cleanup, or re-homing. None of those framings change what it is. | Commonly understood as a neutral efficiency operation — making something shorter without loss. In RFM, shortening a reasoning document is never neutral. |
| **Curation** | The discipline of keeping a reasoning document alive through both addition and reduction. Two modes: triggered (something accumulates or surfaces in use) and deliberate return (coming back without a specific trigger). Both are required. A document that only grows is already dying. | Commonly understood as passive collection or careful archiving. In RFM it is an active discipline that includes honest removal. |
| **Derivative** | Any artifact created from a reasoning document — code, prompts, operational documents, outputs. The chain has structure: reasoning document → operational document → code → outputs. A derivative that moves without its source reasoning document is drift by another name. | Carries strong associations with financial instruments and calculus. In RFM it means strictly: an artifact whose source is a reasoning document, and whose changes must be traceable back to that source. |
| **Operational (document)** | A domain-specific derivative that carries the *what* — constants, interfaces, procedures, and known values — that a reasoning document must never absorb. It exists because some domains have hard execution contracts requiring their own artifact. Not a general overflow for implementation detail. | Commonly means "currently running" or "in production." In RFM it names a specific document type in the derivative chain, distinct from the reasoning document that is its source. |
| **Sweep** | A deliberately invoked corrective review pass — concentrated on a specific document, producing findings for human ruling rather than edits. Two types: language and clarity (expression failures) and structural and hierarchy (architecture failures). Each requires its own cognitive mode and must not run simultaneously with the other. | Commonly means a general cleanup, search operation, or background process. In RFM it is deliberately timed, not ambient, not automated, and not a substitute for the traveling prompt. |

---

*v0.0.0.1 // glossary // [living]*
*disambiguation is reasoning*
*losing the why behind a definition produces the same failure as losing any other reasoning*