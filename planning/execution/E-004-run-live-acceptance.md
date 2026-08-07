# E-004 — Run fresh live acceptance

- Outcome: A genuine fresh Portable Planner session is judged concise, decisive, responsive, safely human-controlled, and explicit about the smallest useful test when it is ready.
- Depends on: P-001, E-003

## Context

- [Confirmed behavior](../decisions/P-001-define-decisive-planning.md)
- Passing E-003 evidence

## In scope

- Install or invoke the unchanged candidate through the normal harness path.
- Use an ordinary planning request without test coaching.
- Have the planner proactively present the smallest genuine test after agent-run checks, then record the live trace, Drew's judgment, any failure, and the exact affected behavior.

## Out of scope

- Treating synthetic trials as human proof or expanding architecture before recording a live failure.

## Constraints

- Preserve the candidate's canonical skill and project-local state unchanged across resumption.

## Proof

- Drew confirms the live session stayed short, stopped low-value grilling, acted when safe, used delegation correctly, proactively moved him into a clear test, and preserved protected gates.

## If blocked or disproven

- Keep the feature in public preview, record the failure, and reopen only the affected decision or instruction.

## Human review

- Required: Drew's explicit live acceptance judgment.

## Next eligible ticket

- Plan complete.
