# E-003 — Find ideas from any agent session

- Outcome: A fresh workspace agent can retrieve exact ideas from the canonical inbox by ID, words, link, status, or date without changing the file.
- Depends on: P-001, E-001, E-002

## Context

- [Confirmed product contract](../decisions/P-001-define-shared-inbox-contract.md)
- Existing Business Brain inbox: `../../../../../../INBOX.md`

## In scope

- Add a read-only agent-facing search/list operation over managed and legacy inbox entries.
- Return stable IDs, titles, matching original excerpts, links, status, and dates with clear match reasons.
- Add concise local instructions so a fresh agent discovers the operation and knows that search is read-only.
- Handle no-result, ambiguous, legacy, malformed-but-unrelated, and special-character queries safely.

## Out of scope

- Semantic databases, embeddings, hosted search, ranking which idea is best, status changes, or altering legacy entries.

## Constraints

- `INBOX.md` is canonical; any index or cache must be disposable and rebuildable.
- Search must not modify file timestamps or content.

## Proof

- A fixture with at least 20 varied ideas passes known-result, no-result, ambiguous, legacy, URL, ID, status, date, and special-character tests.
- A fresh agent following only repository files retrieves the exact phone-captured original and can explain why it matched.

## If blocked or disproven

- Repair parsing or discard the derived index; never “fix” search by rewriting original captures.

## Human review

- Drew tries one remembered phrase and confirms the intended idea is easy to recognize.

## Next eligible ticket

- E-004 — Compare and confirm the next idea.
