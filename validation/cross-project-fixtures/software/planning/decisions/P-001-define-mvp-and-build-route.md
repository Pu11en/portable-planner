# P-001 — Define the MVP and build route

- Status: complete
- Depends on: none

## Decision

Settle the release boundary, user workflow, trust contract, local architecture, acceptance proof, and dependency-safe implementation route for the interview evidence library. These choices determine whether the MVP can deliver fast, verifiable source passages without leaking transcripts or placing technical work on the user.

## Viable options

- A. Windows 11 first — Recommended; proves one polished desktop installer and everyday path now, while deferring other operating systems.
- B. macOS first — Equally viable for a Mac-first audience, but leaves Windows untested.
- C. Windows 11 and macOS together — Broader initial reach, but adds a second packaging and acceptance route before the core evidence workflow is proven.

## Recommendation

A — Release and acceptance-test Windows 11 first. This is the smallest complete desktop boundary and does not prevent later platform work.

## Confirmed decision

The simulated user selected A, Windows 11 first. The complete resolved MVP is:

- **Everyday workflow:** Open app → choose one transcript folder through a native folder picker → index supported files with visible progress → enter plain words or a quoted phrase → review ranked passage cards → open surrounding context → copy the passage with `relative/path:lines start-end` → press **Refresh library** after source changes.
- **Trust contract:** Every result is derived from stored source text and always shows the relative filename and 1-based source line range. The app never fabricates a passage. If the current source fingerprint differs from the indexed fingerprint, the app labels the result stale and requires refresh before presenting it as current evidence.
- **Input contract:** Recursively read `.txt` and `.md` regular files from the selected folder, up to 500 files. Decode UTF-8 with optional BOM. Ignore symlinks and unsupported types. Skip unreadable or invalid files without aborting the library, and show each skipped path and reason. Never write to the source folder.
- **Passage contract:** Normalize CRLF/LF for parsing while preserving line-number correspondence. Form passages from nonblank-line-delimited blocks; split an oversized block at line boundaries so no indexed passage exceeds roughly 1,500 characters. Store original passage text, relative path, start/end lines, file size, modified time, and a content fingerprint.
- **Search contract:** Use a bundled SQLite FTS5 index with `unicode61` tokenization and BM25 ranking. Treat ordinary unquoted words as safe term search and quoted text as phrase search; never pass unchecked raw FTS syntax. Return highlighted snippets, exact stored passage text, path, line range, and nearby passages. Show actionable empty, invalid-query, skipped-file, and indexing states.
- **Refresh contract:** The MVP uses an explicit **Refresh library** control rather than a background watcher. Refresh adds new files, replaces changed passages atomically, removes deleted-file rows, keeps the previous valid index if refresh fails, and reports indexed/skipped/removed counts.
- **Privacy contract:** Transcript contents, paths, fingerprints, and search index remain in the app's local data directory. The app has no accounts, telemetry, remote fonts/assets, HTTP client, updater, cloud service, model, or other network-dependent feature. **Forget library** deletes the local index and remembered path but never touches source transcripts.
- **Implementation route:** Tauri 2 desktop shell; React and TypeScript for the window UI; Rust commands own folder traversal, parsing, indexing, querying, provenance checks, and deletion; `rusqlite` with a bundled SQLite build owns the app-local database and FTS5 table. Tauri permissions expose only the native dialog and the narrow commands needed by the UI; transcript reads stay in the Rust backend.
- **Acceptance proof:** On a Windows 11 reference machine with a deterministic 500-file/250-MB-or-smaller corpus, the UI indexes all supported files without source writes; known term and phrase queries return the expected passage and provenance in under one second after indexing; add/change/delete refresh cases reconcile correctly; skipped and stale cases are visible; a copied citation matches the source lines; the app functions with network access disabled; restart retains the selected library; Forget library removes app-local evidence data; and an installable package launches through the normal desktop UI.

## Evidence

- [Decision-changing technical evidence](../evidence/P-001-evidence.md)

## Effects

- One platform is sufficient for MVP packaging and human acceptance; macOS and Linux cannot be pulled into an execution ticket without returning to planning.
- The core search route is deterministic local full-text retrieval, not AI summarization or semantic search.
- Exact provenance, source-read-only behavior, stale detection, and local-only operation are plan-wide constraints on every execution ticket.
- Execution is split into seven ordered, one-session tickets. Integrated corpus/performance proof is separate from Windows packaging and human acceptance. A blocked ticket makes all downstream tickets ineligible; a disproven trust, privacy, platform, or performance assumption returns the work to planning.
- No further major human preference, factual blocker, or planning dependency remains.

## Complete when

Complete when the platform, workflow, inputs, search and provenance behavior, privacy boundary, refresh lifecycle, architecture, objective acceptance proof, exclusions, and ordered session-sized execution tickets are explicit and agree with `PLAN.md`, `PLAN-VIEW.md`, and `NEXT.md`.
