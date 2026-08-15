# Plan: Make Portable Planner measurably better

**Status:** awaiting approval

## Continuation

- Mode: manual
- Latest boundary: none
- Successor task: none

## Destination

Portable Planner reliably chooses the right next planning action with less user effort, preserves human authority and durable state, and proves each improvement repeatably before it ships.

## Success

- A frozen beta-5/beta-6 comparison first proves the exact beta-6 change did not degrade shared behavior or restores beta 5 if it did; a later candidate must then keep every protected and state-safety gate perfect, improve its targeted failure without material regression, and earn Drew's uncoached judgment that planning is faster and more useful without increased context bloat.

## Boundaries

- In: the existing canonical skill and planning state, a normative decision-kernel contract, a bounded trace corpus, objective invariant validation, repeated behavioral comparison, and fresh human acceptance.
- Out: copying another creator's interface, a second skill or state tree, a database or service, an autonomous prompt optimizer, production UI, a fixed question quota, or changes justified only by expert opinion.

## Map

`2/2`

- ✓ [P-001 — Define decisive planning behavior](decisions/P-001-define-decisive-planning.md) — depends on: none
- ✓ [P-002 — Engineer the next improvement loop](decisions/P-002-engineer-the-improvement-loop.md) — depends on: P-001

## Confirmed decisions

- [P-001](decisions/P-001-define-decisive-planning.md): Explicit scoped delegation covers remaining reversible decisions; settled or experiential uncertainty is not re-asked; bounded trials replace exhausted discussion; replies stay short, take the next safe action, and proactively move finished work to approval and live testing; protected gates remain explicit.
- [P-002](decisions/P-002-engineer-the-improvement-loop.md): Compare immutable beta 5 and beta 6 before another change, formalize the hidden decision kernel, cap the first experiment at 30 automated runs, restore beta 5 if beta 6 regressed, and reject or restore any later candidate that is worse or inconclusive.

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
- ○ [E-010 — Lock the decision-kernel contract](execution/E-010-lock-decision-kernel.md)
- ○ [E-011 — Build the bounded evaluation harness](execution/E-011-build-bounded-evaluation-harness.md)
- ○ [E-012 — Compare beta 5 and beta 6](execution/E-012-measure-beta6-baseline.md)
- ○ [E-013 — Implement one evidence-backed candidate change](execution/E-013-implement-one-candidate-change.md)
- ○ [E-014 — Compare, keep, or reject the candidate](execution/E-014-compare-keep-or-reject-candidate.md)
- ○ [E-015 — Run the controlled human acceptance](execution/E-015-run-controlled-human-acceptance.md)
- ○ [E-016 — Publish the proven prerelease](execution/E-016-publish-proven-prerelease.md)

## Approval

- Prior beta-6 route: approved and released
- Current improvement revision: awaiting Drew's visual approval

## Now

- Current: HUMAN — Review the complete evidence-led improvement and rollback route.
- Next: After explicit approval, begin E-010 through the harness's normal build workflow.
