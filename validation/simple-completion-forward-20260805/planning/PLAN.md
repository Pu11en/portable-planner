# Plan: Drew's YouTube Question Finder Skill

**Status:** awaiting approval

## Destination

A portable, natural-language agent skill that takes a group of AI YouTube channel names, searches only those channels, reviews public comments, and gives Drew the five strongest distinct questions he can credibly answer in short vertical videos, with source links and concise selection reasoning.

## Success

- From a representative channel-name input, the verified skill produces five qualifying, non-duplicative results in the required format; every quote and channel/video attribution matches its public source, every available highlighted-comment link opens the cited thread, and no run replies, posts, downloads video, records content, requires a paid service, or silently includes a channel outside the supplied set.

## Boundaries

- In: natural-language invocation; supplied-channel resolution; relevant-video discovery; recent-first public-comment review; conservative Drew-fit filtering; spam, praise, duplicate, troll, and credential filtering; ranking; five-result report; direct video and comment links; reasons and confidence notes; graceful shortfall and access-blocked behavior; project-local portable skill files and verification.
- Out: replying or posting on YouTube; liking, subscribing, or other engagement; signing into an account as a core requirement; paid data providers; video/audio/transcript download; content recording; publishing; broad discovery outside the supplied channels; comment-author profiling; databases, dashboards, schedulers, and background monitoring.

## Map

`1/1`

- ✓ [P-001 — Define the finder contract and route](decisions/P-001-define-finder-contract.md) — depends on: none

## Confirmed decisions

- [P-001](decisions/P-001-define-finder-contract.md): Use a read-only, public-access-first, bounded research workflow with strict channel provenance, a conservative project-local Drew qualification profile, hard rejection gates, recency-aware ranking, exact source capture, and no fabricated fifth result.

## Execution

- [E-001 — Create the portable skill foundation](execution/E-001-create-skill-foundation.md) — depends on: P-001
- [E-002 — Resolve and lock the supplied channels](execution/E-002-resolve-and-lock-channels.md) — depends on: E-001
- [E-003 — Discover relevant videos within the lock](execution/E-003-discover-relevant-videos.md) — depends on: E-002
- [E-004 — Capture comment candidates and provenance](execution/E-004-capture-comment-candidates.md) — depends on: E-003
- [E-005 — Filter, deduplicate, and rank questions](execution/E-005-rank-qualified-questions.md) — depends on: E-004
- [E-006 — Render the five-result handoff](execution/E-006-render-result-handoff.md) — depends on: E-005
- [E-007 — Prove behavior with deterministic fixtures](execution/E-007-prove-with-fixtures.md) — depends on: E-006
- [E-008 — Run live read-only acceptance and package validation](execution/E-008-live-acceptance-and-validation.md) — depends on: E-007

## Approval

- Visual review: awaiting approval
- Build handoff: not authorized

## Now

- Current: Human review of the finished visual plan.
- Next: Drew approves the visual plan or requests a change; no build begins before explicit approval.
