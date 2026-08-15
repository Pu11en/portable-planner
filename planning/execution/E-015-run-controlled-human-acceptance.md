# E-015 — Run the controlled human acceptance

Status: superseded draft — blocked by reopened P-002; the exact human test must follow the replacement evidence-derived route.

- Outcome: Drew experiences the objectively passing candidate in one fresh uncoached task, with automatic restoration to the winning beta-5/beta-6 reference after a failure.
- Depends on: E-014, or E-012 when no candidate was justified

## Context

- [Comparison verdict](E-014-compare-keep-or-reject-candidate.md)
- [Existing beta-6 human runbook](../../validation/BETA6-HUMAN-TEST.md)
- [Acceptance checklist](../../docs/ACCEPTANCE.md)

## In scope

- For a kept candidate, record the current proven reference installation, install the exact candidate bytes in controlled user scope, verify its version/source, and open one dedicated empty test project.
- Give Drew one natural uncoached test that exercises the targeted improvement plus the beta-6 delegation and protected-approval behavior where compatible.
- Preserve the visible turns and Drew's direct verdict on speed, question value, plan usefulness, and whether anything is worse.
- On any failure or “worse” judgment, immediately restore and verify the winning reference; mark the candidate rejected.
- If E-012 justified no candidate, run the unchanged winning reference human test instead and preserve that result.

## Out of scope

- Coaching the test agent mid-run, publishing before judgment, treating synthetic scores as acceptance, or leaving a failed candidate installed.

## Constraints

- Use a new task because open tasks retain their frozen skill catalog.
- One human run is not spent repeatedly tuning the candidate.
- Final approval and implementation authorization remain protected during the test.

## Proof

- Installed bytes and task-visible version are verified before the run.
- The exact trace and Drew's verdict are recorded.
- Failure proof includes successful reference restoration; pass proof identifies the unchanged candidate eligible for release.

## If blocked or disproven

- Restore the winning reference and record the blocker or first failure. Reopen only the shared behavior that caused it.

## Human review

- Required: Drew performs and judges the fresh task.

## Next eligible ticket

- E-016 — Publish the proven prerelease only after a pass.
