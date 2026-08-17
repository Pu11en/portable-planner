# E-017 — Freeze the I-01 fidelity contract

- Status: draft — requires human review of the I-01 route
- Depends on: P-002

## Outcome

Six sanitized, deterministic fixtures and assertions make the accepted Journey plus focus lens behavior testable without copying private conversations or depending on a sibling project.

## Context

- [I-01 evidence and accepted candidate](../evidence/P-002-I-01-plan-comprehension.md)
- [Current visual contract](../../plugins/portable-planner/skills/portable-planner/references/visual-contract.md)
- [Existing fixtures](../../validation/FIXTURES.md)

## In scope

- Create the minimum repository-local fixtures for F-01 through F-06: canonical fidelity, state freshness, blocked recovery, human authority, readable density, and rich/text parity.
- Preserve the decision-changing structure of the real GOMER trial in a patient-free sanitized fixture; do not copy GOMER files, credentials, patient data, or unrelated product detail.
- Record exact expected visible semantics and prohibited behavior for every case.
- Add malformed variants that prove each deterministic assertion can fail.

## Out of scope

- Candidate instruction changes, model-run quantities, a general planning benchmark, a database, or a copy of the Codex/ZCode transcript corpus.

## Constraints

- Every fixture maps to one unique failure claim; no duplicate cases are added for cosmetic coverage.
- Raw historical sessions and sibling-project state remain read-only and untracked.
- Repetition is added only after observed variance or a protected high-risk failure.

## Proof

- F-01 through F-06 each have one fixture, expected semantics, prohibited behavior, and a deliberately failing variant.
- Fixture content is patient-free, project-local, and sufficient without chat history or GOMER access.
- The contract names no arbitrary run count.

## If blocked or disproven

- Reduce fixture detail while preserving the failure claim. Do not introduce another corpus store or service.

## Human review

- None; the accepted I-01 structure and current evidence define the contract.

## Next eligible ticket

- E-018 — Implement the Journey plus focus lens candidate.
