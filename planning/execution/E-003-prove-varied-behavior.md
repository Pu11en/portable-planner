# E-003 — Prove varied planning behavior

- Outcome: Reproducible scenarios demonstrate the new behavior across materially different project types and failure boundaries.
- Depends on: P-001, E-002

## Context

- [Confirmed behavior](../decisions/P-001-define-decisive-planning.md)
- [Research and initial trials](../evidence/P-001-evidence.md)

## In scope

- Add or update fixtures for software, creative or business, and personal or operational planning.
- Test ordinary delegation, reduced-value questioning, dynamic trial switching, short output, immediate action, proactive approval and test readiness, revocation or conflict, irreversible choice, and final approval.
- Preserve inputs, outputs, materially different variations, failures, targeted revisions, reruns, and decisions changed.
- Revalidate the canonical skill, plugin manifest, references, templates, natural invocation, and unchanged project-local resumption.

## Out of scope

- Production implementation of prototype subjects or architecture expansion without a recorded failure.

## Constraints

- One decision question per trial; default to ordinary, tricky, and failure cases; no fixed conversational question quota.

## Proof

- The scenario matrix and package checks pass, outputs vary appropriately, protected gates never leak, and any failed case passes after a targeted revision and affected rerun.

## If blocked or disproven

- Record the failure, revise only affected instructions, and return a persistent tradeoff or conflict to planning.

## Human review

- Drew reviews the compact comparison, not full transcripts unless requested.

## Next eligible ticket

- E-004 — Run fresh live acceptance.
