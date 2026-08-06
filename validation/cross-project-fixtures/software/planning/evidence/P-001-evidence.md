# P-001 — Decision-changing technical evidence

Accessed: 2026-08-05

## Tauri Windows runtime and installer

- Source: [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/)
- Finding: Tauri uses Microsoft Edge WebView2 on Windows, and WebView2 is already installed on Windows 10 version 1803 and later. This supports a Windows 11-first desktop shell without bundling a separate browser engine.
- Choice changed: Supports Tauri 2 as the desktop shell for option A.

- Source: [Tauri Windows installer](https://v2.tauri.app/distribute/windows-installer/)
- Finding: Tauri can produce `.msi` or NSIS setup packages; Windows 11 includes WebView2, while installer modes are available for missing runtimes.
- Choice changed: Makes a normal Windows installer and offline acceptance run feasible; exact installer target remains an execution detail to prove in E-006.

## Local full-text retrieval

- Source: [SQLite FTS5 extension](https://www.sqlite.org/fts5.html)
- Finding: FTS5 supplies BM25 ranking plus `highlight()` and `snippet()` helpers for returning relevant fragments around search terms.
- Choice changed: Supports deterministic local ranked passage search and highlighted evidence snippets without an embedding service or model.

- Source: [rusqlite feature manifest](https://docs.rs/crate/rusqlite/latest/source/Cargo.toml.orig)
- Finding: `rusqlite` exposes a `bundled` SQLite feature and a `bundled-full` combination, allowing the application to ship a known SQLite library rather than depend on a user's system SQLite.
- Choice changed: Supports the Rust/backend database route and requires E-001 to prove FTS5 availability in the packaged build before downstream work.

## Narrow local file access

- Source: [Tauri file-system plugin](https://v2.tauri.app/plugin/file-system/)
- Finding: Tauri documents native Rust file APIs, explicit filesystem scopes, app-local data directories, and directory watching. Potentially dangerous frontend filesystem commands are blocked unless enabled.
- Choice changed: Keep transcript traversal in narrow Rust commands, store the database in app-local data, and defer background watching because explicit refresh satisfies the MVP with less permission and lifecycle complexity.

## Research stop

These primary sources settle the architecture-changing questions. Additional framework comparisons or scale claims would not change the chosen Windows-first, local FTS route; performance remains an objective E-006 acceptance test rather than an assumed fact.
