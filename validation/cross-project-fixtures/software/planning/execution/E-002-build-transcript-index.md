# E-002 — Build the transcript index

- Outcome: A tested Rust indexing service converts one approved local folder of supported transcripts into passage, provenance, fingerprint, and FTS rows without modifying source files.
- Depends on: [E-001](E-001-establish-desktop-foundation.md)

## Context

- [MVP input, passage, trust, and privacy contracts](../decisions/P-001-define-mvp-and-build-route.md)

## In scope

- Implement a narrow Rust folder-selection result boundary and recursive scan of regular `.txt` and `.md` files, capped at 500 supported files.
- Canonicalize the selected root; ignore symlinks and anything outside it; generate stable relative paths.
- Decode UTF-8 with optional BOM, normalize newlines for parsing, track 1-based source lines, split nonblank blocks, and split oversized blocks at line boundaries near the approved 1,500-character ceiling.
- Compute document fingerprints and persist source metadata, exact passage text, relative path, line ranges, and FTS rows in one transaction.
- Produce structured progress, indexed counts, and per-file skip reasons for invalid UTF-8, unreadable files, unsupported types, and the 500-file cap.
- Add fixtures and automated tests for CRLF/LF, BOM, blank blocks, long blocks, Unicode, nested paths, invalid text, symlinks, cap behavior, line ranges, rollback, and source-folder immutability.

## Out of scope

- Search ranking/API, result UI, incremental refresh, source staleness checks, background watching, copying citations, and packaging.

## Constraints

- Source folders are read-only inputs. Tests must snapshot file paths, bytes, and modification times before and after indexing.
- One bad file cannot invalidate successfully parsed files; a database or transaction failure must keep the previous valid index.
- Never store absolute source paths in FTS content or user-visible result text.

## Proof

- Automated fixtures assert exact passage text and start/end line ranges for every parsing edge case.
- A deterministic 500-file fixture indexes within the cap, produces correct counts, and leaves every source byte and modification time unchanged.
- Forced transaction failure leaves the prior valid database state intact and exposes a structured error.

## If blocked or disproven

- Stop and return to planning if source line provenance cannot remain stable under the agreed normalization, if the safe 500-file boundary cannot be enforced, or if any required indexing step writes to the transcript folder. E-003 remains ineligible.

## Human review

- None; parser fixtures and source immutability checks are the review evidence.

## Next eligible ticket

- [E-003 — Build trustworthy passage search](E-003-build-trustworthy-passage-search.md), only after indexing proof passes.
