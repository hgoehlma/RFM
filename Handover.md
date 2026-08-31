# RFM — Session Handover
2026-08-31. Written by Claude for Claude. Read alongside `RFM_handover_rules.md`.

---

## Version check

| Document | Version | Status this session |
|---|---|---|
| `RFM_skill_rfm_ripple_check_reasoning.md` | v0.1.1 | Journaling removed from Chosen Direction (R-RIPPLECHECK retirement explanation). |
| `RFM_skill_rfm_drafting_reasoning.md` | v0.1.1 | Journaling removed from Chosen Direction (R-LENSMODE retirement explanation). R-LENSMODE removed from Landscape placeholder. |
| `RFM_top_level_reasoning.md` | v0.2.10 | Document map updated: five version bumps; R-LENSMODE phrase removed from rfm-drafting-reasoning row. |

Do not include `RFM_top_level_reasoning.md` in the version check table except as a changed document. The document map inside it is the correct record for all document versions.

---

## Where the project stands

Both new skills (rfm-ripple-check and rfm-drafting) are now installed. Retirement procedures are complete. The rules file carries R-UNSLOP, added this session, as the latest attempt to solve OQ-CONV.

OQ-CONV is not closed. The directive-template description rewrite for rfm-unslop was packaged and installed this session. It failed. R-UNSLOP in the rules file is the current untested attempt. Test result will be known at the next session open.

Three documents updated in a separate fix session (outside this session's narrative): `RFM_sweep_module_reasoning.md` (v0.2.3), `RFM_sweep_module_operational.md` (v0.1.5), `RFM_sweep_prompt_operational.md` (v0.1.2). Document map updated accordingly.

---

## Session narrative

Session opened with startup check. All five version-checked documents matched.

**OQ-CONV: rfm-unslop self-activation failure.** First priority this session. Three approaches evaluated. Option 1 (session-startup skill) rejected: session-startup is not RFM-specific, coupling it to rfm-unslop would misconstrain non-RFM sessions. Option 2 (traveling prompt) noted as possible but unverified. Option 3 (OQ-CONV as a document entry) removed from carry-forward; it was premature to park rather than act.

External research run. Key finding: directive descriptions (ALWAYS invoke + negative constraint) outperform passive descriptions in controlled testing, but the study never tested a topic-less always-on skill with no keyword trigger. That is the exact shape of rfm-unslop's problem. The description rewrite was still the highest-evidence available fix, so it was executed.

rfm-unslop description rewritten to directive template: "ALWAYS invoke this skill before producing any response: drafts, rewrites, conversational replies, procedural output, startup summaries. Do not send any text without running this filter first." Em-dash introduced in the first draft, caught and corrected. Skill packaged and installed.

Result: failed. The directive rewrite did not produce reliable activation on the startup response.

R-UNSLOP added to the ACTIVATE FIRST section of `RFM_handover_rules.md`. Trigger: session opens in an RFM project. Action: read rfm-unslop before producing the first response. Failure shape named explicitly: startup summary or procedural reply bypasses the skill because the model classifies it as non-drafting output. This is now the active untested approach.

**rfm-ripple-check and rfm-drafting installation.** Both confirmed installed by Hinrich. Retirement procedures run. R-RIPPLECHECK and R-LENSMODE both confirmed absent from the rules file (retired last session). Ripple check run across all project documents: no stale operational references found.

**Journaling removal.** Ripple check review surfaced journaling in two Chosen Direction sections. Both removed after ruling: "Why R-LENSMODE is retired alongside this skill" from rfm-drafting-reasoning, "Why R-RIPPLECHECK in the rules file is retired alongside the general skill" from rfm-ripple-check-reasoning. R-LENSMODE also removed from the Landscape placeholder in rfm-drafting-reasoning (retired rule, not a prior approach to survey). Document map row for rfm-drafting-reasoning updated to remove the phrase "why R-LENSMODE is retired."

---

## Carry-forward

**OQ-CONV: rfm-unslop self-activation failure.** R-UNSLOP is now in the rules file. Test result will be visible at next session open. If R-UNSLOP also fails, OQ-CONV should resolve toward a structural limit: no instruction-based mechanism can reliably fire on a topic-less always-on skill. That would close the question rather than generate another patch attempt.

**Complete rfm-ripple-check and rfm-drafting reasoning/operational skeletons.** Landscape and Options Considered deferred. Dedicated sessions needed for both.

**R-FILEACC strain.** Longest and most procedural rule in the file. Mild strain, not urgent. Worth examining in a future rules review.

**Chosen Direction note: self-referential map rows excluded.** The reasoning belongs in the Chosen Direction or Boundaries of whatever document governs the map. Not yet placed.

**Fresh-LLM test.** Not rerun since the document landscape grew. Run when the document set stabilises further.

---

## Cold-start orientation

OQ-CONV is the first test of this session: did the startup summary arrive clean, without the rfm-unslop filter having been bypassed? If yes, R-UNSLOP worked. If no, OQ-CONV should close toward a structural limit rather than another patch.

Both new skills are installed and their retirement procedures are complete. The four skill reasoning/operational documents are skeletons: Landscape and Options Considered are empty in all four. Do not treat them as complete reasoning documents.

The rules file is at 20 rules. R-UNSLOP is the newest addition.
