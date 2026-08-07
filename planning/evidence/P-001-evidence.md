# P-001 — Idea-evidence research

Accessed: 2026-08-07

## Direct capability evidence

- Source: [GitHub — Searching for repositories](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)
  - Relevant finding: repository search can target names, descriptions, topics, and README contents, and can filter or compare language, stars, forks, recent pushes, topics, license, templates, mirrors, and archived state.
  - Decision changed: use a small fan-out of deliberately different repository-level queries, then apply metadata checks; do not rely on one literal phrase or use code search as the default discovery surface.
- Source: [GitHub — REST API endpoints for repositories](https://docs.github.com/en/rest/repos/repos#get-a-repository)
  - Relevant finding: public repository metadata is available without authentication and includes description, topics, language, stars, forks, size, archived/disabled state, timestamps, default branch, and detected license information.
  - Decision changed: shortlist candidates using cheap metadata before spending context on README or source inspection; no GitHub account is required for the public fallback.
- Source: [GitHub — Get a repository README](https://docs.github.com/en/rest/repos/contents#get-a-repository-readme)
  - Relevant finding: the preferred README for a public repository can be retrieved without authentication.
  - Decision changed: deep inspection defaults to a few READMEs and metadata records rather than cloning repositories or reading whole trees.
- Source: [GitHub — Rate limits for the REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
  - Relevant finding: unauthenticated public requests have a lower primary allowance than authenticated requests, and search endpoints have additional restrictive limits.
  - Decision changed: keep the portable default to three searches, three deep inspections, and at most one rescue query; never require authentication merely to raise the budget.
- Source: [GitHub — Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
  - Relevant finding: public visibility alone does not grant permission to reproduce, distribute, or create derivatives; without a license, default copyright applies. GitHub's detected-license information is a starting point, not a legal guarantee.
  - Decision changed: a missing, unclear, or incompatible license prevents a code-reuse recommendation, though the repository may still be labeled as read-only capability evidence or an architectural reference.

## Disposable query comparison

Input fixture: [local interview evidence library](../../validation/cross-project-fixtures/software/IDEA.md) — “Build a small local app that turns a folder of interview transcripts into a searchable evidence library.”

Four unauthenticated GitHub repository searches were compared against the same idea:

1. A broad literal query across name, description, topics, and README returned many high-popularity but irrelevant agent-skill and interview-coaching results.
2. A narrow quoted outcome query returned only one weak recruiting result.
3. A mechanism query around semantic transcript search found relevant transcript and media-search implementations.
4. An adjacent-solution query around local document search with citations found directly relevant local-file search systems.

Direct README inspection then distinguished three different candidate roles:

- [OpenDocuments](https://github.com/joungminsung/OpenDocuments) — a broad, production-oriented self-hosted document-search platform; useful as a capability and architecture reference, but much larger than the fixture MVP.
- [agentic-file-search](https://github.com/PromtEngineer/agentic-file-search) — a focused staged scan/deep-dive/backtrack pattern; useful as a mechanism reference, with external model and parsing dependencies that materially affect fit.
- [Generative-Search-Engine-For-Local-Files](https://github.com/imanoop7/Generative-Search-Engine-For-Local-Files) — a smaller local-file search baseline; closer to a starter, but still requires checking maintenance, dependency, desktop-UX, scale, and exact-license fit before reuse.

## Decision-changing conclusion

One query and popularity ordering are not reliable enough. The default should combine three complementary query angles, deduplicate and rank a small metadata pool, then deeply inspect no more than three differently useful candidates. The result should classify each candidate's role and state exactly how it changes the MVP route. Additional searches are unlikely to change this planning decision; real fixture and live-use failures should tune the query and scoring rules during execution.
