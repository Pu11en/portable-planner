# E-006 — Rerun affected behavior and package checks

Status: complete — 2026-08-10

- Outcome: Fresh isolated cases and repository-wide validation show that the repaired candidate fixes the beta.4 failures without regressing portability, state, safety, or existing planning behavior.
- Depends on: E-005

## Context

- [Live failure evidence](../../validation/DECISIVE-FLOW-LIVE-ACCEPTANCE.md)
- [Existing decisive-flow evidence](../../validation/DECISIVE-FLOW-TEST.md)
- [Acceptance checklist](../../docs/ACCEPTANCE.md)

## In scope

- Rerun explicit delegation invitation, digression recovery, provisional research-derived destination, low-friction test intake, canonical visual refresh, and presentation-failure fallback cases from fresh contexts.
- Validate the canonical skill, plugin manifests, versions, referenced files/templates, Markdown links, whitespace, secret exposure, installer behavior, and unchanged local-state resumption.
- Preserve raw outputs and failures in one release-candidate validation record.

## Out of scope

- Treating synthetic output as Drew's final human acceptance or loosening a failed assertion to force a pass.

## Constraints

- Use the unchanged repaired candidate for every case.
- Never execute untrusted repository code or mutate an unrelated project during validation.

## Proof

- Every affected failure has a passing fresh case or remains explicitly open.
- Package checks pass and no test creates another implementation copy or service.
- Acceptance state matches the actual evidence.

## If blocked or disproven

- Repair only the demonstrated shared instruction and rerun affected cases; do not publish a false production claim.

## Human review

- None for synthetic/package proof; the final genuine acceptance boundary remains explicit.

## Next eligible ticket

- E-007 — Integrate and publish the release candidate.

## Result

- [Beta-5 release-candidate evidence](../../validation/BETA5-RELEASE-CANDIDATE-TEST.md) passes delegation invitation, digression recovery, provisional research direction, low-friction test handoff, presentation fallback, package validation, isolated installation, and natural invocation.
- V-03 and V-04 remain open for a fresh beta-5 human run; synthetic behavior was not substituted for that proof.
