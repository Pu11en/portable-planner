# Plan: Local Interview Evidence Library

**Status:** awaiting approval

## Destination

An installable Windows 11 desktop app that turns one selected folder of plain-text or Markdown interview transcripts into a private, searchable library of source-verifiable passages.

## Success

- On a Windows 11 acceptance machine, a nontechnical user can select a folder of up to 500 supported transcripts, index it, find a known passage in under one second after indexing, inspect the matching source text with filename and line range, refresh changed files, and complete the whole path without a terminal or network connection.

## Boundaries

- In: Windows 11; one local folder; `.txt` and `.md` UTF-8 files; up to 500 files; read-only source access; local full-text index; ranked passage results; file-and-line provenance; surrounding context; copy passage with source reference; explicit refresh; visible skipped-file and stale-source states; local installer.
- Out: macOS/Linux releases; cloud sync; telemetry; accounts; generated reports or summaries; embeddings or model downloads; transcription; OCR; PDF/DOCX/audio input; transcript editing; multi-library management; collaboration; automatic background folder watching.

## Map

`1/1`

- ✓ [P-001 — Define the MVP and build route](decisions/P-001-define-mvp-and-build-route.md) — depends on: none

## Confirmed decisions

- [P-001](decisions/P-001-define-mvp-and-build-route.md): Ship a Windows 11-first, local-only Tauri app using Rust and bundled SQLite FTS5, with passage-level search, exact provenance, explicit refresh, and a seven-session dependency-ordered build route.

## Execution

- [E-001 — Establish the desktop foundation](execution/E-001-establish-desktop-foundation.md) — depends on: P-001 and explicit plan approval
- [E-002 — Build the transcript index](execution/E-002-build-transcript-index.md) — depends on: E-001
- [E-003 — Build trustworthy passage search](execution/E-003-build-trustworthy-passage-search.md) — depends on: E-002
- [E-004 — Deliver the complete desktop flow](execution/E-004-deliver-complete-desktop-flow.md) — depends on: E-003
- [E-005 — Make refresh and privacy behavior durable](execution/E-005-make-refresh-and-privacy-durable.md) — depends on: E-004
- [E-006 — Prove the integrated MVP](execution/E-006-prove-integrated-mvp.md) — depends on: E-005
- [E-007 — Package and accept the Windows MVP](execution/E-007-package-and-accept-windows-mvp.md) — depends on: E-006

## Approval

- Visual review: awaiting approval
- Build handoff: not authorized

## Now

- Current: Human review of the finished visual plan
- Next: Approve the plan explicitly or request a change; no execution ticket is eligible before approval.
