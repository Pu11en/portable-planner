# E-008 — Implement the exact option-B delegation shortcut

- Status: complete — 2026-08-15
- Depends on: E-007

## Outcome

Portable Planner counts only consecutive bare recommended keys and, after the third, inserts an explicit remaining-recommendations shortcut as option `B` in the next real reversible question.

## Context

- [Confirmed behavior](../decisions/P-001-define-decisive-planning.md)
- [Product contract](../../docs/PRODUCT-CONTRACT.md)
- Drew's exact interaction clarification on 2026-08-15

## In scope

- Define the complete-reply match, reset rules, durable streak state, option-`B` insertion, `A` through `G` ceiling, delegation effects, and protected gates.
- Reconcile the one canonical skill, necessary references, planning-ticket template, product authority, acceptance, project map, and release version.

## Out of scope

- Inferring delegation from a pattern, adding a separate delegation-only question, delegating protected decisions, a second skill or state tree, or new infrastructure.

## Constraints

- The ordinary current-question recommendation remains `A`.
- Only bare `B` to the inserted shortcut grants delegation.
- Any extra content resets the streak.

## Proof

- A fresh reader can apply the rule deterministically without guessing what counts, when to offer, how to relabel, or where to stop.
- Product, skill, template, and acceptance language agree.

## If blocked or disproven

- Return only an unresolved safety or ownership tradeoff to Drew; do not weaken the exact matching rule.

## Human review

- Not required for implementation; E-009 supplies objective proof and the final live runbook.

## Next eligible ticket

- E-009 — Validate and publish beta 6.

## Result

- Product authority, the one canonical skill, durable interaction state, template, acceptance, and test runbook now agree on the exact rule.
- One forward-test ambiguity at a protected gate was corrected to the deterministic `0 / not ready` transition and reran successfully.
