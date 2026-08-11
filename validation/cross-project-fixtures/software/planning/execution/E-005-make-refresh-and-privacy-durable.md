# E-005 — Make refresh and privacy behavior durable

- Outcome: The desktop library reconciles added, changed, deleted, skipped, and stale source files safely, and the user can remove all app-local library data without touching transcripts.
- Depends on: [E-004](E-004-deliver-complete-desktop-flow.md)

## Context

- [Approved refresh, trust, and privacy contracts](../decisions/P-001-define-mvp-and-build-route.md)

## In scope

- Implement **Refresh library** to fingerprint the current folder, add new files, atomically replace changed-file passages, remove deleted-file rows, and report indexed/changed/removed/skipped counts.
- Preserve and continue serving the last valid index when a refresh transaction fails, while showing that refresh did not complete.
- Before showing stored evidence as current, compare current file metadata/fingerprint as needed; label changed, missing, or unreadable source results stale and require refresh.
- Implement **Forget library** with confirmation; delete database/index and remembered folder state from app-local storage, then return to first-run state without deleting or changing source files.
- Add restart/recovery and tests for add/change/delete, rename as delete+add, invalid file, folder unavailable, transaction failure, stale result, forgotten library, and source immutability.
- Audit packaged capabilities and dependencies for network, telemetry, updater, remote assets, shell, and broad frontend filesystem access.

## Out of scope

- Automatic background watching, multiple libraries, recovery of forgotten indexes, source deletion/editing, cloud backup, auto-update, and packaging polish.

## Constraints

- Never show a changed or missing source passage as current evidence without a stale warning.
- Refresh is atomic at the library level; a failed refresh cannot destroy the last valid index.
- Forget deletes only app-owned data and must require a clear human confirmation.

## Proof

- Automated add/change/delete/rename fixtures reconcile exact document, passage, and FTS rows and produce correct UI counts.
- Forced refresh failure leaves the prior index queryable and visibly marks refresh failure.
- Stale and missing-source tests prevent a current-evidence presentation until refresh.
- Forget removes the database and saved path after restart while source snapshots remain byte-for-byte and timestamp identical.
- Capability/dependency audit reports no network, telemetry, updater, remote asset, shell, or unrestricted frontend filesystem route.

## If blocked or disproven

- Return to planning if atomic refresh, trustworthy staleness behavior, local-only storage, or source immutability cannot be upheld. E-006 cannot package a privacy or provenance exception.

## Human review

- A human verifies the warning and confirmation language is unmistakable and that **Forget library** names only the local index, not source transcripts.

## Next eligible ticket

- [E-006 — Prove the integrated MVP](E-006-prove-integrated-mvp.md), after durability proof and wording review pass.
