# E-003 — Discover Relevant Videos Within the Lock

- Outcome: The skill creates a bounded, balanced, recent-first pool of topic-relevant videos verified to belong to Drew's allowed channels.
- Depends on: P-001, E-002

## Context

- [Confirmed discovery and qualification contract](../decisions/P-001-define-finder-contract.md)
- E-001's Drew qualification reference
- E-002's canonical allowed-channel representation

## In scope

- Define a portable discovery sequence using only compliant public browsing/search capabilities available to the harness.
- Start with recent uploads and rotate across allowed channels before spending more review budget on one channel.
- Use the qualification profile to judge topical relevance from public titles/descriptions and page metadata without downloading or transcribing video.
- Allow older high-fit videos only after the recent pass and within the documented bounded inspection budget.
- Capture canonical channel identity, video title, direct watch URL, publication recency, and the reason each video is relevant.
- Recheck every candidate against the immutable allowed-channel set before comment review.

## Out of scope

- Comments, full video viewing, transcript/audio/video download, exhaustive channel crawling, unrelated search results, scoring final questions, and background monitoring.

## Constraints

- Recent and balanced discovery is the default; relevance and channel provenance outrank popularity.
- The implementation must document a finite inspection budget and stop condition suitable for one user-initiated run.
- Any harness/tool access must comply with the source platform; no scraping, evasion, or unofficial API emulation.

## Proof

- Mixed-channel fixtures yield only allowed-channel videos and rotate across the supplied set before deeper sampling.
- Recent relevant videos precede older ones; an older candidate enters only under the exceptional-fit rule.
- Unrelated, wrong-channel, unavailable, and duplicate videos are excluded with a recorded reason.

## If blocked or disproven

- If no compliant public discovery route exists in the harness, return the capability blocker and do not build a bypass. If the finite budget cannot reasonably finish in one run, tighten the documented budget without weakening the channel lock.

## Human review

- None until E-008's representative live run.

## Next eligible ticket

- E-004 — Capture comment candidates and provenance.
