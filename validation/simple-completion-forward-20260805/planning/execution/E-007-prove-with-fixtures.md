# E-007 — Prove Behavior With Deterministic Fixtures

- Outcome: A network-independent acceptance suite proves the complete contract, including adversarial and failure behavior, in a fresh context.
- Depends on: P-001, E-006

## Context

- [Complete confirmed contract](../decisions/P-001-define-finder-contract.md)
- E-001 through E-006 implementation and their objective proofs

## In scope

- Create small synthetic/local fixtures rather than copying real commenter identities or bulk public data.
- Cover: natural-language invocation; name/handle/URL resolution; ambiguous and lookalike channels; immutable channel lock; balanced recent discovery; older exceptional video/question; exact quote preservation; available/unavailable direct comment links; disabled/sign-in-gated comments; every rejection class; semantic duplicates; Drew-fit and credential traps; confidence labels; five-result success; fewer-than-five shortfall; and complete access failure.
- Run the skill from a fresh agent context that knows only the package and fixture prompt.
- Validate deterministic outputs/snapshots and package structure.
- Record failures against the execution ticket that owns the behavior and rerun after fixes.

## Out of scope

- Live YouTube proof, real commenter datasets, user accounts, API keys, media download, publishing, and human usefulness approval.

## Constraints

- Fixtures must contain no secrets or unnecessary personal data.
- Tests must not depend on network ordering, changing YouTube pages, or proprietary paid tools.
- Passing snapshots cannot substitute for E-008's live provenance check.

## Proof

- Every named acceptance case has an expected outcome and passes in a clean context.
- The suite detects deliberate wrong-channel, fabricated-link, padded-result, and prohibited-action regressions.
- The package validator and all deterministic checks exit successfully with reproducible commands documented locally.

## If blocked or disproven

- Fix failures in the owning E-001–E-006 scope and rerun. Return to planning only when two confirmed requirements are demonstrably incompatible.

## Human review

- None; provide a concise test summary for E-008.

## Next eligible ticket

- E-008 — Run live read-only acceptance and package validation.
