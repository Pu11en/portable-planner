# Next

Plan: `/home/drewp/main-projects/portable-planner/planning/`
State: `awaiting approval`
Work: **HUMAN — Review the evidence-led improvement plan**
Read: `PLAN.md`, `PLAN-VIEW.md`, `decisions/P-002-engineer-the-improvement-loop.md`, and `execution/E-010-lock-decision-kernel.md` through `execution/E-016-publish-proven-prerelease.md` only.
Context: Drew selected option A. The finished route first compares immutable beta 5 and beta 6, restores beta 5 if beta 6 regressed shared behavior, caps automated evidence at 30 fresh runs, changes one demonstrated failure class at a time, rejects a worse or inconclusive candidate before merge, and restores the winning reference after any temporary-install human failure.
Outcome: Drew either explicitly approves this finished route for build or names one targeted revision.
Done when: Direct approval changes lifecycle state to `approved for build` and makes E-010 eligible, or a requested revision reopens only P-002.

Do not begin E-010 before explicit approval. After approval, preserve `v0.1.0-beta.5` and `v0.1.0-beta.6` as immutable controls and use the harness's normal build workflow.
