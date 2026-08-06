# E-001 — Establish the desktop foundation

- Outcome: A runnable Windows-targeted Tauri 2, React, and TypeScript app opens through a normal desktop window, creates an app-local SQLite database with the approved schema, and proves bundled FTS5 is available.
- Depends on: [P-001](../decisions/P-001-define-mvp-and-build-route.md) and explicit plan approval

## Context

- [MVP and build route](../decisions/P-001-define-mvp-and-build-route.md)
- [Technical evidence](../evidence/P-001-evidence.md)

## In scope

- Initialize the smallest maintainable Tauri 2 + React + TypeScript project and document supported Windows 11 development prerequisites.
- Add Rust modules for typed commands, app-local paths, database opening, and versioned migrations.
- Add `rusqlite` with a bundled SQLite configuration and create empty library metadata, documents, passages, and FTS5 structures needed by later tickets.
- Add a minimal main window and a backend health call that reports schema version and FTS5 readiness without exposing transcript filesystem access to frontend JavaScript.
- Add unit/integration tests for migrations, reopening the database, and an insert/query/delete FTS5 smoke cycle.

## Out of scope

- Folder selection, transcript parsing, production indexing, search UI, refresh behavior, acceptance corpus, installer packaging, macOS, and Linux.

## Constraints

- No network, telemetry, updater, remote asset, account, shell, or unrestricted filesystem dependency or permission.
- Store mutable data only in the OS app-local data directory; never in the install directory or a transcript folder.
- Keep schema changes versioned and transactional.

## Proof

- Automated tests create a fresh database, migrate it, reopen it, and pass an FTS5 insert/ranked-query/delete smoke test.
- The desktop development build opens on Windows 11 and the visible health state reports the expected schema and FTS5 readiness.
- Dependency and capability review finds no network or broad frontend filesystem access.

## If blocked or disproven

- Return to planning if a bundled SQLite build cannot supply FTS5 in the Windows package, Tauri cannot produce a normal Windows 11 window in the available build environment, or the implementation requires network/unrestricted filesystem capability. Do not start E-002 with an unproven database foundation.

## Human review

- None; retain the Windows launch screenshot/log and test output for E-006.

## Next eligible ticket

- [E-002 — Build the transcript index](E-002-build-transcript-index.md), only after every proof above passes.
