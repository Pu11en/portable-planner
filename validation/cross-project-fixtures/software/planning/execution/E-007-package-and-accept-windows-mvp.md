# E-007 — Package and accept the Windows MVP

- Outcome: A reproducible Windows 11 installer passes clean-account offline installation, the approved evidence workflow, uninstall checks, and final human acceptance.
- Depends on: [E-006](E-006-prove-integrated-mvp.md)

## Context

- [Plan destination, success, and boundaries](../PLAN.md)
- [Complete MVP and acceptance proof](../decisions/P-001-define-mvp-and-build-route.md)
- [E-006 integrated proof contract](E-006-prove-integrated-mvp.md) and its completed report

## In scope

- Select the smallest Tauri-supported Windows installer target that meets the approved Windows 11 and offline-use boundary, then record the configuration.
- Produce a release build and installer from a clean versioned source state; record build identifiers and installer checksum.
- Install under a clean Windows 11 test account, launch from the normal desktop UI, and rerun the preserved E-006 acceptance runner with network disabled.
- Verify restart persistence, Forget library behavior, uninstall behavior, and that transcript sources remain unchanged throughout install/use/uninstall.
- Record clean-machine steps, actual results, screenshots/logs, installer size/checksum, known limitations, and final human accept/reject decision in the package acceptance report.

## Out of scope

- Shipping or publishing the installer, buying a code-signing certificate, bypassing Windows warnings, app-store submission, auto-update, other operating systems, new features, and rewriting the E-006 corpus/runner.

## Constraints

- The everyday and acceptance paths must not require a terminal or network connection.
- Do not waive failed installer launch, privacy, provenance, source-read-only, 500-file, refresh, Forget, or speed proof.
- A failure caused by an implementation defect returns to its source E-* ticket; a changed product/platform assumption returns to planning.

## Proof

- The package report includes a reproducible clean build, installer checksum, clean-account install/launch/uninstall evidence, and a fully passing offline rerun of the E-006 acceptance runner.
- At least three returned passages are manually compared with their source files and line ranges.
- Source snapshots are unchanged, Forget removes app-local evidence data, uninstall leaves transcripts intact, and human acceptance is explicitly recorded.

## If blocked or disproven

- Report the exact failed condition, reproduction, and owning prior ticket or planning assumption. Do not ship, call the MVP complete, or remove evidence to obtain a pass.

## Human review

- Required final acceptance: a human follows the normal Windows 11 UI path, compares at least three passages with source files, confirms privacy/Forget and no-terminal behavior, reviews the package record, and explicitly accepts or rejects the MVP.

## Next eligible ticket

- Plan complete after every proof and explicit human acceptance pass; otherwise return to the named failed execution ticket or to planning.
