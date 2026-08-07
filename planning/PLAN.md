# Plan: Add repo-assisted idea discovery

**Status:** approved for build

## Continuation

- Mode: manual
- Latest boundary: none
- Successor task: none

## Destination

Portable Planner offers a quick related-repository scan at the beginning of qualifying idea-stage software or AI-product planning, gathers only enough context to search effectively after permission, and uses evidenced existing possibilities to help the user confirm a stronger direction before ordinary planning—without making GitHub a requirement or slowing declined or unrelated plans.

## Success

- In fresh-session tests, the planner gives no-idea or thin-idea software planning an immediate, understandable research choice; detailed plans and existing work skip it. After consent it gathers only missing search-critical context, surfaces one provisional evidence-backed direction plus at most two materially different alternatives, explains reuse limits, and waits for human confirmation before ordinary planning adopts a direction.
- The flow has explicit search, inspection, output, privacy, and stopping bounds so irrelevant repositories, sensitive query content, and token use remain controlled.
- Declined scans, non-software ideas, unavailable research, and searches with no useful result continue through the current planning experience without delay or a false blocker.

## Boundaries

- In: an idea-stage permission gate; one real-world grounding clue when directionless; privacy-safe minimum search briefs; bounded repository-first discovery with narrow direct-source verification; evidence-tiered possibility assessment; extraction of reusable patterns or components; a provisional human-confirmed direction; graceful decline, no-result, and unavailable-research behavior; varied real-repository scenario trials; updates to the canonical skill, product contract, fixtures, and live acceptance checks.
- Out: a second skill or mode, mandatory GitHub account or API, cloning or executing untrusted repositories during planning, guaranteed legal clearance, bulk indexing, a database or MCP service, automatic code assembly, and repository research for every project type.

## Map

`1/1`

- ✓ [P-001 — Define the idea-evidence flow](decisions/P-001-define-idea-evidence-flow.md) — depends on: none

## Confirmed decisions

- [P-001](decisions/P-001-define-idea-evidence-flow.md): Only new no-idea or thin-idea software planning receives the optional scan; directionless research starts from one privacy-safe real-world anchor, returns one to three provisional evidence-tiered possibilities only when they improve the plan, and requires human confirmation before adopting a direction.

## Execution

- ✓ [E-001 — Lock the product contract](execution/E-001-lock-product-contract.md)
- ✓ [E-002 — Add the flow to the canonical skill](execution/E-002-add-canonical-skill-flow.md)
- ▶ [E-003 — Prove bounded research behavior](execution/E-003-prove-bounded-research.md)
- [E-004 — Revalidate installation and portability](execution/E-004-revalidate-portability.md)
- [E-005 — Run live idea-stage acceptance](execution/E-005-live-idea-stage-acceptance.md)

## Approval

- Visual review: approved
- Build handoff: approved by Drew on 2026-08-07

## Now

- Current: E-003 — Run the fresh Codex behavior check and Drew review; the static matrix and public-repository prototypes pass.
- Next: E-004 — Complete fresh Codex and non-Codex behavior after the current runner and Claude authentication limitations are cleared.
