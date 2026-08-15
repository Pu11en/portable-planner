# E-011 — Build the bounded evaluation harness

- Outcome: A local, repeatable harness runs frozen planning scenarios from fresh state and separates deterministic failures from judgment scores.
- Depends on: E-010

## Context

- [Decision-kernel contract ticket](E-010-lock-decision-kernel.md)
- [Validation rubric](../../plugins/portable-planner/skills/portable-planner/references/validation-rubric.md)
- [Existing fixtures](../../validation/FIXTURES.md)

## In scope

- Create six representative visible scenarios and two held-out scenarios covering natural invocation, idea-stage scan eligibility, fact-versus-decision routing, question quality, exact delegation, digression, resumption, trial selection, protected gates, final approval, and build transition.
- Create one isolated fresh project and fresh agent task per run; preserve exact prompt, output, planning artifacts, version/commit, run metadata, and validator result.
- Add deterministic checks for invocation, choice labels, one-question behavior, legal state transitions, write-through, artifact agreement, protected gates, and implementation authorization.
- Add a fixed judgment rubric for consequential-question yield, missed decisions, turns to a defensible plan, brevity, and usefulness.
- Freeze the corpus, assertions, scoring rules, and file hashes before E-012 starts.

## Out of scope

- A cloud service, database, dashboard, autonomous prompt optimizer, live production workload, or using held-out prompts to write the candidate.

## Constraints

- Plain repository files and lightweight scripts only.
- A deterministic validator may reject objective violations but cannot declare a subjective plan good.
- The runner must accept an explicit plugin source or immutable tag so baseline and candidate cannot be confused.

## Proof

- A dry run proves isolation, exact capture, version attribution, deterministic checks, fixed scoring, early-stop behavior, and corpus hashes.
- Deliberately malformed fixtures trigger each hard validator.
- Repeating one known fixture does not reuse planning state from the prior run.

## If blocked or disproven

- Reduce runner convenience, not evidence integrity. If fresh-task automation cannot be made reliable locally, preserve the same frozen corpus and run it manually with exact capture.

## Human review

- None.

## Next eligible ticket

- E-012 — Measure the immutable beta-6 baseline.
