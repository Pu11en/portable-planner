# Fresh-Resume Visual and Handoff Test

Date: 2026-08-05

## Setup

Portable Planner was installed as a real Codex plugin. A fresh Codex context received only a natural-language continuation request, the one-letter answer `A`, and the existing project-local workshop planning state.

## Demonstrated failures

The installed plugin correctly discovered the skill, resolved `A` to the complete capped-coaching decision, reconciled `PLAN.md` and the current planning ticket, generated `PLAN-VIEW.md`, and asked one new recommendation-first question. Three failures prevent this run from counting as clean evidence:

1. **F-005 — Fresh-resume visual not displayed.** The agent generated `PLAN-VIEW.md` but returned only the next A/B/C question. The user-facing turn contained neither the Mermaid graph nor the complete compact text route even though a fresh resume is an automatic display trigger.
2. **F-006 — Stale handoff completion test.** `NEXT.md` advanced its session outcome to the accepted-task-scope decision but its `Complete when` line still described the already-settled delivery-model decision.
3. **F-007 — Validation contamination.** The test agent browsed a sibling validation report. It did not obtain the answer from that report, but an evaluation that can inspect prior conclusions is not independent enough to count.

Raw failed state remains under `validation/codex-natural-install-forward-20260805/project/planning/`.

Fresh Codex session: `019fd3d0-a6de-7601-8424-9d575ff4c5e1`.

## Required fix

- Treat every natural-language `continue` or `resume` invocation as a mandatory first-reply visual display trigger when a coherent route exists.
- Before replying after any decision write-through, compare the current decision, `PLAN.md` current/next, `NEXT.md` work/session/completion lines, and `PLAN-VIEW.md` now/next. All must describe the same unresolved frontier; no line may still describe the just-settled choice.
- Rerun with instructions that prohibit reading anything outside the installed plugin and the isolated project state.

## Independent rerun

The canonical plugin was revised, cache-busted to `0.1.0+codex.20260805213005`, copied unchanged into the isolated marketplace, and reinstalled. A new ephemeral Codex context was instructed to use only the installed plugin plus the current project's `IDEA.md` and `planning/` directory and to avoid parent directories, sibling fixtures, reports, and prior conclusions.

The rerun:

- resolved the pending `A` to the full supported-menu-plus-screened-customs decision;
- saved the decision and downstream safety effects before continuing;
- advanced the same current ticket to the next consequential menu decision;
- refreshed `PLAN.md`, `PLAN-VIEW.md`, and `NEXT.md` consistently;
- replaced the stale `NEXT.md` completion test with the current menu completion test;
- included the complete updated text route in the first user-facing continuation reply;
- asked exactly one recommendation-first A/B/C question; and
- inspected no project file outside `IDEA.md` and `planning/`.

The installed-skill catalog initially supplied an incomplete cache path after the cache-buster update. The agent located the installed skill under the declared plugin root and continued without transferring the problem to the user. This is a Codex cache-path recovery observation, not a planning-state failure.

Clean Codex session: `019fd3d5-b947-7652-aab4-9b65945feebb`.

## Current result

**PASS after fix and independent rerun.** F-005, F-006, and F-007 are closed: the continuation reply visibly carried the complete route, the handoff frontier and completion test agreed across files, and the clean agent did not inspect prior validation evidence.
