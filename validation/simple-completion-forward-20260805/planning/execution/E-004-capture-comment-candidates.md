# E-004 — Capture Comment Candidates and Provenance

- Outcome: The skill captures exact potential questions and enough public source metadata to verify each one and open its comment thread when YouTube exposes a direct link.
- Depends on: P-001, E-003

## Context

- [Confirmed comment and access contract](../decisions/P-001-define-finder-contract.md)
- [Official comment-link and sorting evidence](../evidence/P-001-evidence.md)
- E-003's verified video candidate representation

## In scope

- Review public comments `Newest first` on verified videos and use `Top comments` or relevant replies only as a secondary exceptional-question pass.
- Detect question-shaped comments, including clearly answerable requests written without a question mark.
- Preserve exact visible text, displayed comment age/date, canonical channel, video title, video URL, and any timestamp-generated highlighted-comment URL.
- Record explicit states for comments disabled, page unavailable, sign-in gated, direct link unavailable, or access/capability blocked.
- Keep the review bounded and user-initiated; capture only fields required for evaluation and provenance.

## Out of scope

- Comment-author profiling, contact details, sentiment dossiers, replies/posts/likes, media or transcript download, bulk harvesting, question ranking, or final report rendering.

## Constraints

- Never paraphrase the stored exact-comment field.
- Never create a synthetic direct-comment URL; use the interface-provided highlighted URL or mark it unavailable.
- Do not bypass sign-in, disabled comments, rate limits, access controls, or platform restrictions.

## Proof

- Fixture comments round-trip character-for-character through capture.
- Provided highlighted-comment URLs retain their comment/thread identifier and the correct video URL.
- Disabled, blocked, and unavailable-link fixtures produce explicit states rather than missing data or fabricated links.
- No disallowed commenter-profile fields are retained.

## If blocked or disproven

- If the harness cannot read public comments through a permitted route, return the exact blocker and shortfall; do not substitute invented comments or an unofficial scraping path.

## Human review

- None until source links are spot-checked in E-008.

## Next eligible ticket

- E-005 — Filter, deduplicate, and rank questions.
