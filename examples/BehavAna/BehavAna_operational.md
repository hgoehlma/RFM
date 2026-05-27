# Project — Operational Document
`v0.1.1` // `operational` // [living]

---

## File Naming Convention

All system artifacts created within this workspace must strictly match this exact pattern:

`Project_[type]_[descriptor].md`

Where `type` must be one of:
- `top_level_reasoning`
- `module_reasoning`
- `operational`
- `glossary`

### Execution Rules
1. **Current Workspace Files:** Active project files dropped into the repository directories omit version suffixes. The current version string must be visible exclusively within the document header metadata block.
2. **Archived Files:** Historical snapshots preserved for lineage tracking must carry an explicit version suffix appended to the filename string (e.g., `Project_top_level_reasoning_v0.0.5.md`).

---

## Document Map Maintenance

The authoritative document mapping register lives at the top of `Project_top_level_reasoning.md`. 

### Synchronization Policy
- Any edit that advances a document's version identifier requires a mandatory, simultaneous update to the Document Map within the same commit or session exchange. 
- Version numbers tracked within the map must be absolute, literal values. The deployment of wildcard tokens or imprecise placeholders is strictly prohibited.

---

## Technical Environment and Tooling Agreements

Define the strict environment runtime baselines, dependency engines, and configuration tools required to turn the architecture into physical output. This block details how tools are applied without referencing why they were chosen.

### 1. Human Data Pre-Processing Protocols
Prior to session ingestion, raw survey matrix data must be mathematically consolidated within an external spreadsheet to defend the GUI agent context window from computational overflow.

- **Metric Consolidation:** Calculate the mathematical average, minimum boundary, and maximum boundary of current behavior metrics alongside desired behavior metrics, categorized strictly by individual actor role cohort.
- **Root Cause Indexing:** Count and weight prioritized participant root causes, assigning primary numeric values based on ranking criteria (e.g., first choice = Weight 1.0, second choice = Weight 0.5).
- **Deliverable Target:** Generate a text-fenced 'Cohort Quantitative Baseline Summary Block' containing clean descriptive parameters for each R&D role to act as the primary structural constraint.

### 2. File Ingestion Targets and Session Execution
- **Workspace Scope:** Analysis execution maps directly into isolated, single-cohort chat sessions to enforce strict representative balancing.
- **Ingestion Limit:** A maximum of 1 role cohort's aggregated transcript notes and its corresponding pre-processed spreadsheet summary block may sit in active context at any time.

### 3. Prompt Execution Harness (The Iceberg Engine)
To run the analysis pipeline without system drift, execution prompts inside the workspace environment must enforce a rigid multi-pass trajectory:

#### Execution Prompt 1: Phase 1 — Quantitative Baseline Lockdown
    SYSTEM CONFIGURATION RULE: You are an objective, zero-temperature data-linkage engine. 
    You are entering Phase 1 of the analysis.
    Incorporate the following pre-calculated cohort metrics as absolute mathematical constraints:
    [INSERT COHORT QUANTITATIVE BASELINE SUMMARY BLOCK HERE]

    Your only task in this turn is to confirm receipt of these metrics and outline the specific numerical variations (averages, min/max spreads, prioritized root causes) you will actively audit within the transcripts. Do not read or extract textual themes yet.

#### Execution Prompt 2: Phase 2 — Pass 1 (Overt Behavior Extraction)
    SYSTEM CONFIGURATION RULE: Analyze the attached transcript files for [INSERT SPECIFIC ROLE COHORT HERE] strictly through the lens of the Phase 1 quantitative boundaries.

    Execute Pass 1 of the Iceberg Method: Identify and extract explicit actions, observable habits, and stated desired behaviors that match or directly explain the numeric slider deviations. 

    CRITICAL CONSTRAINT: Every identified behavioral trend MUST be immediately followed by a direct, verbatim quote, participant identifier, and clear source citation. Do not summarize or use generic corporate syntax.

#### Execution Prompt 3: Phase 2 — Pass 2 (Vertical Psychological Mapping)
    SYSTEM CONFIGURATION RULE: Maintain focus on the verbatim behaviors extracted in the previous turn. 

    Execute Pass 2 of the Iceberg Method: Systematically trace each identified behavior downward to its underlying emotional markers and hidden personal blockers. 

    CRITICAL CONSTRAINT: You are forbidden from introducing unanchored or generalized emotional categories. Every discovered blocker must map directly back to a Pass 1 behavior and be strictly verified by a direct, verbatim textual quote.

---

## Production Deployment and Release Workflows

State the unyielding step-by-step commands required to package, compile, and distribute the derivative output assets.

### 1. Verification Sequence
Before declaring an output target ready for production graduation, the local engine must successfully process these steps in sequence:
1. Verify that every final behavior, blocker, and emotional pattern contains a minimum of two unique, verbatim direct-quote citations from distinct participant identifiers.
2. Execute structural sweep audits to verify tracking ID integrity across modified documents.
3. Confirm that output summaries follow the required stakeholder structure (H1: background, problem; H2: Methode; H3: results sliders; H4: root causes and blockers; H5: desired behaviour; H6: advice for desired behaviour workstream).

### 2. Output Generation Command
To compile the independent role profiles into the master multi-cohort delivery report, execute the following syntax block:

```bash
# Execute local verification suite and merge balanced cohort deliverables
bash scripts/validate_citations.sh --cohort=all && markdown-to-pdf Project_operational_final_report.md --target=production