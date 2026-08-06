# E-001 — Protect and structure the inbox

- Outcome: A tested local inbox core can add and update managed idea entries without damaging legacy or unrelated `INBOX.md` content.
- Depends on: P-001

## Context

- [Confirmed product contract](../decisions/P-001-define-shared-inbox-contract.md)
- Existing Business Brain inbox: `../../../../../../INBOX.md`

## In scope

- Inspect the real inbox format read-only, then build against a fixture copy first.
- Define a managed capture section and stable `I-YYYYMMDD-NNN` IDs compatible with the existing Markdown template.
- Store original text, optional source link, capture time, source message ID, status, title, and later selection rationale/date.
- Implement read, append, and single-entry status update operations with validation, locking or equivalent concurrency protection, atomic replacement, and explicit failure results.
- Support legacy entries as read-only search results without bulk migration.

## Out of scope

- Telegram, AI ranking, rewriting legacy ideas, auto-commits, `NOW.md` edits, deletion, and user-facing build work.

## Constraints

- Preserve unrelated content exactly and never overwrite on a parse, identity, lock, or write uncertainty.
- Do not create a second canonical idea store.

## Proof

- Automated tests cover empty, legacy, managed, duplicate-message, concurrent-update, invalid, and forced-write-failure cases.
- A before/after fixture diff changes only the intended managed entry; forced failure leaves the file byte-for-byte unchanged.
- A reviewed dry run against the real inbox reports the intended edit before one controlled test entry is allowed.

## If blocked or disproven

- Stop before changing the real inbox if its structure cannot support isolated managed entries; record the exact conflict and return to P-001 for a storage revision.

## Human review

- Drew reviews the proposed real-inbox diff before the first controlled entry is written.

## Next eligible ticket

- E-002 — Capture privately from the phone.
