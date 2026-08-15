# E-012 — Compare beta 5 and beta 6

Status: superseded draft — blocked by reopened P-002. Every scenario and numerical allocation below is withdrawn and non-authoritative.

- Outcome: Eighteen unchanged fresh-task runs determine whether beta 6 preserved beta 5's shared behavior and establish the better proven version as the reference before any candidate change.
- Depends on: E-011

## Context

- [Confirmed rollback contract](../decisions/P-002-engineer-the-improvement-loop.md)
- [Bounded harness](E-011-build-bounded-evaluation-harness.md)
- Immutable control tags: `v0.1.0-beta.5` and `v0.1.0-beta.6`

## In scope

- Run each of the six visible scenarios once against beta 5 and once against beta 6, then repeat the three highest-risk shared scenarios once on both versions: eighteen control runs total.
- Score intended beta-6-only behavior separately so beta 5 is not falsely penalized for lacking the new shortcut. Compare invocation, ordinary question quality, shared delegation safety, digression, resumption, state, protected gates, approval, and build authorization directly.
- Preserve every output, including losing runs, and produce one control report with hard failures, rubric scores, word/turn counts, missed-decision review, and observed high-risk run range.
- If beta 6 has a hard or material shared-behavior regression, restore and verify the public beta-5 installation before candidate work and select that regression as the sole target. Otherwise keep beta 6 as the reference and select at most one other demonstrated failure class.

## Out of scope

- Editing skill instructions, changing frozen assertions after seeing output, discarding outliers, reading held-out prompts for candidate design, or spending more than eighteen control runs.

## Constraints

- Verify the loaded plugin version and source hash inside every run.
- Stop and repair only the harness if version attribution or isolation is wrong; restart the control comparison from run one afterward.
- If no meaningful improvable failure appears, do not manufacture a change.

## Proof

- Exactly eighteen attributable runs and an append-only paired report exist.
- Every hard failure and directional score traces to preserved output and artifacts.
- The report names the winning reference version, records any installation restoration, and selects an observed target rather than one inferred from expert opinion.

## If blocked or disproven

- If neither version exposes a safe evidence-backed target, skip E-013 and take the winning unchanged reference to E-015 human acceptance. If the harness is invalid, return to E-011 without touching product instructions.

## Human review

- None; the report informs the bounded candidate experiment but does not replace Drew's later judgment.

## Next eligible ticket

- E-013 — Implement one evidence-backed candidate change, or E-015 if no change is justified.
