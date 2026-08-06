# E-006 — Render the Five-Result Handoff

- Outcome: The skill returns a concise, source-verifiable list Drew can manually open and use to record one short vertical answer.
- Depends on: P-001, E-005

## Context

- [Confirmed output and human-handoff contract](../decisions/P-001-define-finder-contract.md)
- E-005's ordered qualified candidates and confidence labels

## In scope

- Render up to five ranked results with: channel; video title and direct link; exact comment; direct highlighted-comment link when available or an explicit unavailable note; why the question is worth answering; and a brief confidence note.
- Add one compact coverage line naming resolved allowed channels and material access limitations such as disabled comments.
- State a transparent shortfall when fewer than five survive the gates or the permitted source budget/access route ends.
- End with the manual next step: Drew opens one result and records his answer himself.
- Keep the report scannable and avoid drafting an answer unless Drew separately asks after this workflow ends.

## Out of scope

- Replying, posting, liking, subscribing, downloading, recording, scripting Drew's answer, publishing, scheduling, analytics, or saving commenters to a database.

## Constraints

- Exact comments remain verbatim and visibly separate from the skill's reasoning.
- Never imply an unavailable comment link exists.
- Never claim five qualifying results if fewer survived.
- No action-oriented control may suggest the skill will engage on YouTube or record content.

## Proof

- Schema validation confirms all required fields for each result and the coverage line.
- Five-result, fewer-than-five, unavailable-comment-link, and access-blocked snapshots are readable and factually explicit.
- A prohibited-action string scan and manual review find no instruction or claim that the skill replies, posts, downloads, records, or publishes.

## If blocked or disproven

- If the report becomes too long, tighten explanatory prose without removing required source fields. If a source field is unavailable, expose the limitation rather than changing the contract.

## Human review

- Drew reviews whether one representative report is fast to scan and gives him enough confidence to open one result.

## Next eligible ticket

- E-007 — Prove behavior with deterministic fixtures.
