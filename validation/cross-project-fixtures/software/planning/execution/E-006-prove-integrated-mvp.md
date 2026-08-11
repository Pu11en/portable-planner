# E-006 — Prove the integrated MVP

- Outcome: A deterministic 500-file acceptance corpus and automated full-system record prove the integrated workflow, correctness, privacy, source immutability, and post-index search speed before packaging.
- Depends on: [E-005](E-005-make-refresh-and-privacy-durable.md)

## Context

- [Plan destination, success, and boundaries](../PLAN.md)
- [Complete MVP and acceptance proof](../decisions/P-001-define-mvp-and-build-route.md)
- E-001 through E-005 proof records

## In scope

- Create a deterministic corpus of 500 supported files totaling no more than 250 MB, with known term/phrase targets, nested paths, Unicode, add/change/delete cases, one invalid UTF-8 file, and one unsupported file.
- Add one repeatable automated acceptance runner for select → index → term/phrase search → inspect → copy → add/change/delete refresh → restart → stale handling → forget.
- Run all unit, integration, component, accessibility, desktop, refresh, privacy, and source-immutability tests from a clean checkout/build.
- Measure initial indexing and post-index query time on a named Windows 11 reference machine; require known term and phrase results to render in under one second after indexing and record the actual indexing duration.
- Compare copied citations with source lines, repeat the automated path with network disabled, and record corpus manifest, OS/build identifiers, test output, timings, capability/dependency audit, and failures in an integrated proof report.

## Out of scope

- Installer creation, clean-account install/uninstall, code signing, human final acceptance, app-store submission, other operating systems, new features, and tuning beyond an observed acceptance failure.

## Constraints

- Do not waive a failed privacy, provenance, source-read-only, no-terminal, 500-file, offline, or sub-one-second search check.
- Preserve the deterministic corpus and runner so E-007 can repeat them without reconstructing evidence.
- A remedy that changes a confirmed product decision returns to planning.

## Proof

- The integrated proof report shows the deterministic runner and all lower-level suites passing from a clean build on the named Windows 11 reference machine.
- Known term and phrase results render in under one second after indexing, copied lines match sources, source snapshots remain unchanged, refresh/stale/restart/forget pass, and the runner passes with network disabled.
- The report records actual indexing duration and every skipped-file path/reason without claiming installer acceptance.

## If blocked or disproven

- Return to the exact failed execution ticket for an implementation defect, or to planning with the measurement and smallest decision that must change for a disproven success assumption. E-007 remains ineligible.

## Human review

- None; E-007 owns clean-install and final human acceptance. Preserve the integrated report for that review.

## Next eligible ticket

- [E-007 — Package and accept the Windows MVP](E-007-package-and-accept-windows-mvp.md), only after the integrated proof report passes in full.
