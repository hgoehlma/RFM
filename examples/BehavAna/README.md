# BehavAna — RFM Field Example

## What this is

A real deployment of RFM under time pressure, in a translated environment.
The problem: analyze interview transcripts from approximately 50 R&D participants
across four roles to identify key behavioral changes for project efficiency.
The constraint: four hours, an off-the-shelf Copilot agent, no custom code.

The day before, RFM had been translated into Antigravity IDE (Google's
agent-first IDE, supporting Gemini, Claude, and other models). On the day,
the reasoning document and operational document were produced through that
translation. Antigravity IDE then derived the Copilot agent instruction
directly from those two documents. The agent ran on four transcripts and
produced output that stakeholders found credible.

The derivative chain held under real conditions: reasoning document →
operational document → agent instruction → analysis output.

## What worked

The sequencing discipline traveled. The core RFM commitments — reasoning before
execution, explicit assumptions, structured section sequence — survived
translation into a new environment and produced a working agent specification
without custom code.

The "loud voice trap" protection — prioritizing unique participant count over
quote volume — was reasoned into the documents and enforced structurally in the
agent. It worked in practice.

## What slipped

The translation was quick. Two structural drifts entered and were not caught
until after the deployment:

**The derivative chain was broken at the operational layer.** The AGENTS.md
file states that operational files "are not derivatives of reasoning" and grants
the agent autonomy to modify them independently. In RFM, operational documents
are derivatives — they carry what the reasoning document has decided. This
inversion gives the agent explicit permission to modify execution parameters
without a reasoning document touch, which is exactly the failure RFM is
designed to prevent.

**The operational document contains a fictional bash script.** The production
deployment section includes a script block referencing files and commands that
do not exist. It reads as executable infrastructure. It is not. A derivative
that points nowhere is drift.

## What this example proves

A quick-and-dirty RFM translation produced a working result. The core structure
is robust enough to survive imperfect implementation under time pressure.

It also shows where translation fails first: the derivative chain and the
operational document's relationship to reasoning are the points most likely to
slip when time is short. A practitioner using this example as a starting point
should treat those two drift points as the first things to verify in any new
translation.
