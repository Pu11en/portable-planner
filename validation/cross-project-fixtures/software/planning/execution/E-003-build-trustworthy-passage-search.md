# E-003 — Build trustworthy passage search

- Outcome: A tested Rust query boundary returns ranked, source-verifiable passages and context for safe term and quoted-phrase searches, including honest empty and invalid-query states.
- Depends on: [E-002](E-002-build-transcript-index.md)

## Context

- [MVP search and trust contracts](../decisions/P-001-define-mvp-and-build-route.md)
- [SQLite FTS5 evidence](../evidence/P-001-evidence.md)

## In scope

- Define typed request/response models for search, result cards, provenance, nearby context, and query errors.
- Convert plain unquoted words and quoted phrases into parameterized, escaped FTS5 queries; reject unmatched quotes and empty-effective queries without exposing raw database syntax.
- Rank with BM25 and deterministic tie-breaking; return highlighted snippets, exact stored passage text, relative path, 1-based line range, document fingerprint, and nearby indexed passages.
- Add a copy payload containing the exact passage plus `relative/path:lines start-end`.
- Add deterministic tests for terms, phrases, punctuation, Unicode, injection-like input, ranking ties, empty results, nearby context, result limits, and byte-for-byte/source-line provenance.

## Out of scope

- Desktop layout and interaction, folder picker, refresh reconciliation, current-file fingerprint checks, background watching, semantic search, summaries, and packaging.

## Constraints

- Never synthesize, paraphrase, or alter evidence text in the exact-passage field or copy payload.
- Never execute unchecked user text as raw FTS syntax or SQL.
- A result without relative path and valid line range is an error, not displayable evidence.

## Proof

- Search contract tests pass for known term and exact-phrase queries and assert deterministic ordering.
- Adversarial query strings cannot change SQL/FTS structure and return a typed result or typed validation error.
- Every returned exact passage and line range matches the indexed fixture source, and the copy payload round-trips exactly.

## If blocked or disproven

- Return to planning if FTS5 cannot meet the safe-query or exact-provenance contract, or if acceptable search requires an external service/model. Do not mask missing provenance or start E-004.

## Human review

- None; retain representative query outputs for final evidence review.

## Next eligible ticket

- [E-004 — Deliver the complete desktop flow](E-004-deliver-complete-desktop-flow.md), only after the search contract passes.
