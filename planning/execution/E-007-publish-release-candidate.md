# E-007 — Integrate and publish the release candidate

- Outcome: Every reviewed project change is committed, merged to `main`, tagged, and published as the next honest public-preview release candidate with its remaining human acceptance gates stated.
- Depends on: E-006

## Context

- [Acceptance checklist](../../docs/ACCEPTANCE.md)
- [Contributor guide](../../AGENTS.md)
- E-006 release-candidate validation record

## In scope

- Synchronize one strict-semver candidate version across manifests and marketplace entries.
- Commit all reviewed in-scope files, push the branch, create and merge a GitHub pull request into `main`, tag the merged commit, and publish release notes that distinguish passing objective checks from open human acceptance.
- Confirm remote `main`, tag, release, and clean local state.

## Out of scope

- Calling the planning experience proven or generally available while required live checks remain open.

## Constraints

- Do not overwrite unrelated user work or rewrite published history.
- The public release remains a prerelease unless the complete acceptance checklist passes.

## Proof

- Remote `main` contains the complete reviewed work.
- The tag and GitHub prerelease resolve to that merged commit.
- The release notes link the objective evidence and name all remaining genuine human gates.

## If blocked or disproven

- Push the reviewed branch, record the exact integration or release blocker, and do not misstate main or release status.

## Human review

- Drew performs the remaining fresh live acceptance from a new task after installation.

## Next eligible ticket

- Plan complete after the remaining human acceptance is recorded; otherwise reopen only the failed behavior.
