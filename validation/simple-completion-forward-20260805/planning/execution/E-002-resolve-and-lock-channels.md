# E-002 — Resolve and Lock the Supplied Channels

- Outcome: Natural-language channel inputs resolve to one immutable allowed-channel set that prevents lookalike or outside-channel contamination.
- Depends on: P-001, E-001

## Context

- [Confirmed channel-identity contract](../decisions/P-001-define-finder-contract.md)
- [Channel identity evidence](../evidence/P-001-evidence.md)

## In scope

- Normalize comma-separated, bulleted, or conversational channel display names, handles, and URLs.
- Resolve each item to its canonical channel URL/handle and channel ID when publicly visible.
- Preserve Drew's original label beside the resolved identity for the final coverage note.
- Add an immutable allowed-channel check reused by discovery, capture, and output.
- For a genuinely ambiguous display name, identify the ambiguity and request only that channel's handle/URL; do not guess or silently drop it.
- Handle missing, unavailable, duplicated, or malformed entries plainly.

## Out of scope

- Finding videos/comments, scoring, using subscription lists, signing in, or broadening beyond Drew's supplied group.

## Constraints

- A display-name match alone is not authoritative when multiple plausible channels exist.
- No Google account, API key, or paid identity service.
- No later step may mutate or expand the allowed-channel set.

## Proof

- Deterministic cases accept equivalent name/handle/URL inputs, collapse duplicates, and retain correct canonical identities.
- Lookalike-channel and same-display-name cases either resolve from public evidence or pause for a handle/URL.
- A forced outside-channel candidate fails the shared allowed-channel check.

## If blocked or disproven

- If public information cannot distinguish a channel, stop only that resolution and ask for its handle/URL. Do not invent an identity or change the product route.

## Human review

- None during deterministic implementation; ambiguity wording is reviewed in E-007.

## Next eligible ticket

- E-003 — Discover relevant videos within the lock.
