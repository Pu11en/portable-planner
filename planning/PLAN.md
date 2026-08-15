# Plan: Make Portable Planner measurably better

**Status:** planning

## Continuation

- Mode: manual
- Latest boundary: none
- Successor task: none

## Destination

Portable Planner reliably chooses the right next planning action with less user effort, preserves human authority and durable state, and proves each improvement repeatably before it ships.

## Success

- The planner automatically recognizes unresolved project/product planning at the agreed boundary, and every behavior test is derived from a real failure or explicit product claim before a run count is chosen. Beta 5, beta 6, and any candidate are compared only on cases with exact starting state, expected decision, prohibited behavior, and human judgment.

## Boundaries

- In: the existing canonical skill and planning state, selective adaptation of evidence-backed mechanisms, a normative decision-kernel contract, a bounded trace corpus across materially different domains, objective invariant validation, repeated behavioral comparison, and fresh human acceptance.
- Out: replacing or vendoring another planning framework, copying another creator's protocol or interface, narrowing to software, a second skill or state tree, a database or service, an autonomous prompt optimizer, production UI, a fixed question quota, or changes justified only by popularity or expert opinion.

## Map

`2/2`

- ✓ [P-001 — Define decisive planning behavior](decisions/P-001-define-decisive-planning.md) — depends on: none
- ▶ [P-002 — Engineer the next improvement loop](decisions/P-002-engineer-the-improvement-loop.md) — depends on: P-001

## Confirmed decisions

- [P-001](decisions/P-001-define-decisive-planning.md): Explicit scoped delegation covers remaining reversible decisions; settled or experiential uncertainty is not re-asked; bounded trials replace exhausted discussion; replies stay short, take the next safe action, and proactively move finished work to approval and live testing; protected gates remain explicit.
- [P-002](decisions/P-002-engineer-the-improvement-loop.md): Keep the evidence-led method and rollback protection, withdraw the preselected 30-run allocation, preserve one original cross-domain protocol, adapt outside mechanisms only for named failures with cross-domain proof, settle the automatic planning boundary, and derive the minimum test set from real failures before revising the build route.

## Execution

- ✓ [E-001 — Lock the behavior contract](execution/E-001-lock-behavior-contract.md)
- ✓ [E-002 — Update the canonical skill](execution/E-002-update-canonical-skill.md)
- ✓ [E-003 — Prove varied planning behavior](execution/E-003-prove-varied-behavior.md)
- ✓ [E-004 — Run fresh live acceptance](execution/E-004-run-live-acceptance.md) — completed with recorded failures
- ✓ [E-005 — Repair the live interaction failures](execution/E-005-repair-live-failures.md)
- ✓ [E-006 — Rerun affected behavior and package checks](execution/E-006-rerun-release-candidate.md)
- ✓ [E-007 — Integrate and publish the release candidate](execution/E-007-publish-release-candidate.md)
- ✓ [E-008 — Implement the exact option-B delegation shortcut](execution/E-008-implement-exact-delegation-shortcut.md)
- ✓ [E-009 — Validate and publish beta 6](execution/E-009-validate-publish-beta6.md)
- ! [E-010 through E-016 — Draft improvement route](execution/E-010-lock-decision-kernel.md) — blocked by reopened P-002; former test counts are invalid

## Approval

- Prior beta-6 route: approved and released
- Current improvement revision: planning reopened; prior approval surface withdrawn

## Now

- Current: HUMAN — Settle when Portable Planner should activate automatically.
- Next: Mine the real-failure inventory and shape the minimum test contracts before choosing any run count.
