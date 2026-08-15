# E-012 — Measure the immutable beta-6 baseline

- Outcome: Twelve unchanged fresh-task runs establish beta 6's behavior, failures, and normal variance before any candidate instruction changes.
- Depends on: E-011

## Context

- [Confirmed rollback contract](../decisions/P-002-engineer-the-improvement-loop.md)
- [Bounded harness](E-011-build-bounded-evaluation-harness.md)
- Public baseline tag: `v0.1.0-beta.6`

## In scope

- Run each of the six visible scenarios twice from isolated state against the immutable beta-6 tag.
- Preserve every output, including losing runs, and produce one baseline report with hard failures, rubric scores, word/turn counts, missed-decision review, and observed run-to-run range.
- Select at most one demonstrated failure class as the candidate target.

## Out of scope

- Editing skill instructions, changing frozen assertions after seeing output, discarding outliers, reading held-out prompts for candidate design, or spending more than twelve baseline runs.

## Constraints

- Verify the loaded plugin version and source hash inside every run.
- Stop and repair only the harness if version attribution or isolation is wrong; restart the baseline from run one afterward.
- If no meaningful improvable failure appears, do not manufacture a change.

## Proof

- Exactly twelve attributable runs and an append-only report exist.
- Every hard failure and directional score traces to preserved output and artifacts.
- The selected target is observed rather than inferred from expert opinion.

## If blocked or disproven

- If beta 6 exposes no safe evidence-backed target, skip E-013 and take unchanged beta 6 to E-015 human acceptance. If the harness is invalid, return to E-011 without touching product instructions.

## Human review

- None; the report informs the bounded candidate experiment but does not replace Drew's later judgment.

## Next eligible ticket

- E-013 — Implement one evidence-backed candidate change, or E-015 if no change is justified.
