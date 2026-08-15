# E-009 — Validate and publish beta 6

- Status: current
- Depends on: E-008

## Outcome

The unchanged beta-6 candidate passes the exact shortcut matrix and package checks, reaches remote `main` with a matching tag and prerelease, and is installed from the public marketplace.

## Context

- [E-008](E-008-implement-exact-delegation-shortcut.md)
- [Acceptance checklist](../../docs/ACCEPTANCE.md)
- [Human test runbook](../../validation/BETA6-HUMAN-TEST.md)

## In scope

- Test three bare recommended keys, added-text reset, non-recommended reset, resumption, option-`B` insertion, bare-`B` delegation, protected-gate stopping, `G` ceiling, natural invocation, package validation, links, versions, isolated install, and secrets.
- Commit, push, merge, tag, prerelease, and install beta 6 only after objective checks pass.

## Out of scope

- Treating synthetic proof as Drew's human acceptance or calling the public preview production-proven.

## Constraints

- Use one unchanged candidate for all affected tests.
- Preserve beta-5 historical evidence unchanged.

## Proof

- Release-candidate evidence links every assertion to an observed result.
- Local main, remote main, tag, release, and installed public plugin agree.

## If blocked or disproven

- Repair only the demonstrated instruction failure and rerun the affected matrix before publishing.

## Human review

- Drew performs the exact fresh-task run after publication.

## Next eligible ticket

- Human beta-6 acceptance; otherwise reopen only the failed behavior.
