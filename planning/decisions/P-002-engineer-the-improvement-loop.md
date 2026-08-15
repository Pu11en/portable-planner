# P-002 — Engineer the next improvement loop

- Status: complete — 2026-08-15
- Depends on: P-001

## Decision

Choose how Portable Planner should become more reliable and effective after beta 6 without cargo-culting expert workflows, increasing question burden, or bloating the skill with unmeasured instructions.

## Viable options

- A. Build a decision-kernel and repeatable evaluation loop — Recommended; more initial engineering, but it makes future improvements measurable and protects against regressions.
- B. Tighten the canonical instructions directly from the expert patterns — Faster, but another prose-only revision may improve one case while silently harming others.
- C. Wait for more uncoached beta-6 use and repair only observed failures — Lowest immediate cost, but it leaves frontier quality and run-to-run variance largely unmeasured.

## Recommendation

A — Keep the current user-facing experience, formalize the hidden decision and state-transition contract, first compare beta 5 with beta 6 on frozen shared scenarios, then make only evidence-backed changes. Use scripts for objective invariants and preserve human judgment for whether questions and plans are actually good. Cap the first experiment at 30 fresh automated scenario runs, stop early on any hard failure, and reserve one separate uncoached run for Drew.

## Confirmed decision

A — Build the decision-kernel and repeatable evaluation loop. Immutable beta-5 and beta-6 tags are paired controls before another change. If beta 6 regressed shared behavior, restore public beta 5 and make that regression the only candidate target. Otherwise beta 6 remains the reference. Any later candidate remains isolated and cannot merge, release, or replace the reference installation unless it has zero hard-gate failures, fixes its target consistently, avoids material regression, and passes Drew's uncoached test. Worse or inconclusive always keeps or restores the better proven reference.

## Delegation

None. Drew selected option A but has not yet approved the finished execution plan for build.

## Interaction state

- Recommended-key streak: 0
- Option-B shortcut: not ready

## Evidence

- [Current repository and Channel Brains evidence](../evidence/P-002-expert-engineering-evidence.md)
- [Earlier fixed-commit expert-skill pass](../../research/PORTABLE-PLANNER-EXPERT-SKILLS.md)
- [Beta-6 objective evidence](../../validation/BETA6-RELEASE-CANDIDATE-TEST.md)

## Effects

- Returns lifecycle state to `planning`; the beta-6 human test remains valid but no longer stands in for approving this new improvement program.
- If A is confirmed, execution planning will cover the normative decision kernel, trace corpus, objective validator, beta-5/beta-6 control comparison, one-change experiment, held-out regression run, and fresh human acceptance.
- The first experiment may use at most 30 automated fresh-task runs; it cannot spend the cap to tune repeatedly against the same visible cases.
- The first eighteen runs compare all six visible scenarios once on beta 5 and beta 6, then repeat the three highest-risk shared scenarios once on both versions. The remaining twelve are reserved for affected, regression, and held-out candidate proof.
- A beta-6 hard or material shared-behavior regression restores public beta 5 before candidate work. The candidate is developed and tested away from `main`; a worse or inconclusive result is never merged, and a failed temporary human-test installation restores the proven reference immediately.
- No database, service, MCP server, second skill, second canonical state tree, autonomous prompt optimizer, or production UI is justified by this research.

## Complete when

Drew's A decision, beta-5/beta-6 control comparison, success metrics, 30-run ceiling, rollback rule, architecture boundary, and human gate are explicit; E-010 through E-016 cover the complete experiment; and canonical state is ready for final approval without treating expert opinion as proof.
