# E-016 — Publish the proven prerelease

Status: superseded draft — blocked by reopened P-002; no candidate may publish from the withdrawn route.

- Outcome: Only a candidate that passed objective comparison and Drew's fresh acceptance reaches `main`, a matching prerelease, and the public installed plugin.
- Depends on: E-015

## Context

- [Objective comparison](E-014-compare-keep-or-reject-candidate.md)
- [Human acceptance](E-015-run-controlled-human-acceptance.md)
- [Public distribution proof](../../validation/PUBLIC-PREVIEW-DISTRIBUTION-TEST.md)

## In scope

- Review the complete diff and evidence, validate the canonical skill and manifests, commit intentionally, push, merge the candidate PR, bump the prerelease version, tag the exact final `main`, and publish an honest prerelease.
- Replace any temporary candidate installation with the public marketplace copy and compare source, marketplace, tag, and installed bytes.
- Update planning, acceptance, project map, and release evidence without claiming broader unpassed checks.

## Out of scope

- Publishing a rejected, inconclusive, or human-failed candidate; moving the beta-6 tag; declaring production proof; or bundling unrelated product changes.

## Constraints

- Release bytes must be the unchanged human-tested candidate plus release-record/version metadata only.
- Beta 5 and beta 6 remain permanently recoverable by tag and release.
- Every previously open acceptance gate stays visibly open unless this exact run satisfied it.

## Proof

- Local `main`, remote `main`, tag, GitHub prerelease, public marketplace, and installed plugin agree.
- The worktree is clean; validators, links, manifests, isolated install, and secret audit pass.
- Release notes name the targeted improvement, comparison result, human evidence, and remaining limits.

## If blocked or disproven

- Leave the proven candidate branch and evidence intact, restore the winning reference if necessary, and report the exact release blocker without changing quality claims.

## Human review

- Already supplied by E-015; no second acceptance run is required for metadata-only publication.

## Next eligible ticket

- Plan complete.
