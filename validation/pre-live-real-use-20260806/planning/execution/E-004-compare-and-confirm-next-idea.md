# E-004 — Compare and confirm the next idea

- Outcome: An agent presents a reasoned shortlist of at most three ideas and records exactly one as selected only after Drew confirms it.
- Depends on: P-001, E-001, E-003

## Context

- [Confirmed product contract](../decisions/P-001-define-shared-inbox-contract.md)
- Current Business Brain priorities: `../../../../../../NOW.md`

## In scope

- Add agent instructions for building a shortlist from current goals, likely value or evidence, and the smallest useful proof.
- Require the comparison to distinguish stored facts from agent inference and recommend one candidate plainly.
- Present one explicit confirmation gate before any status change.
- On confirmation, use the safe updater to record `selected`, rationale, and date for the intended ID; preserve every other entry.
- If another idea is already selected, show the conflict and require an explicit replace-or-cancel decision.

## Out of scope

- Automatic selection, project creation, `NOW.md` changes, task execution, deletion, arbitrary numerical scoring, or changing more than the confirmed inbox entry.

## Constraints

- No confirmation means no mutation.
- A recommendation is not a decision and must never be represented as one.

## Proof

- Tests demonstrate zero mutation before confirmation, one intended status change after confirmation, safe cancellation, and explicit handling of an existing selection.
- A fresh agent produces a three-or-fewer shortlist with traceable reasons and no invented evidence.

## If blocked or disproven

- Preserve all statuses. Return to P-001 only if current workspace priorities cannot support a meaningful comparison without a new human-owned rule.

## Human review

- Drew reviews the shortlist, confirms or rejects the recommendation, and verifies that no work starts automatically.

## Next eligible ticket

- E-005 — Prove the complete live flow.
