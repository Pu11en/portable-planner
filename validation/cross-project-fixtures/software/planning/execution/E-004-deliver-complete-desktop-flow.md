# E-004 — Deliver the complete desktop flow

- Outcome: A nontechnical user can complete folder selection, indexing, search, result inspection, surrounding-context review, and citation copying through one coherent desktop UI with no terminal.
- Depends on: [E-003](E-003-build-trustworthy-passage-search.md)

## Context

- [Approved everyday workflow and visible states](../decisions/P-001-define-mvp-and-build-route.md)

## In scope

- Implement the first-run folder-selection screen with a native directory picker and clear `.txt`/`.md`, privacy, and 500-file expectations.
- Implement indexing progress and completion summaries with indexed and skipped counts plus accessible per-file reasons.
- Implement a focused search screen with plain-language query help, loading, empty, invalid-query, and error states.
- Implement keyboard-accessible ranked result cards showing highlighted snippet, relative path, and line range; selection opens exact passage plus nearby context.
- Implement **Copy passage + source** with visible success/failure feedback.
- Preserve selected library and current UI state across ordinary window refresh/restart using app-local metadata.
- Add component tests and an automated desktop happy-path test using a small fixture folder.

## Out of scope

- Incremental refresh reconciliation, stale-source warning, Forget library, background watching, visual redesign beyond a usable MVP, installer packaging, macOS, and Linux.

## Constraints

- Everyday use has no terminal, raw path entry requirement, SQL/FTS syntax, or technical error dump.
- Filename and line range remain visible wherever evidence text is shown.
- Meet keyboard focus visibility, semantic labels, status announcements, and reasonable contrast in all core states.
- UI code cannot read arbitrary transcript files directly; it calls the narrow Rust boundaries.

## Proof

- Automated desktop test selects a fixture folder, indexes it, searches a known phrase, opens the expected passage/context, copies the exact source payload, and completes without a terminal.
- Component/accessibility checks cover initial, loading, indexed, skipped, result, empty, invalid, and failure states.
- Manual keyboard pass reaches and operates every core control in a logical order with visible focus.

## If blocked or disproven

- Fix ordinary UI or accessibility defects within this ticket. Return to planning only if the agreed workflow cannot be delivered without a new product decision or broader filesystem permission. E-005 is blocked until all core states work.

## Human review

- A human reviews the automated-run capture and performs the keyboard path on Windows 11; material workflow or legibility rejection returns this ticket for correction before E-005.

## Next eligible ticket

- [E-005 — Make refresh and privacy behavior durable](E-005-make-refresh-and-privacy-durable.md), after automated proof and required human review pass.
