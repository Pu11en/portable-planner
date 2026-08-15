# Next

Plan: `/home/drewp/main-projects/portable-planner/planning/`
State: `planning`
Work: **HUMAN — Settle Portable Planner's automatic activation boundary**
Read: `PLAN.md`, `PLAN-VIEW.md`, `decisions/P-002-engineer-the-improvement-loop.md`, and `evidence/P-002-expert-engineering-evidence.md` only.
Context: Drew withdrew the prior 30-run approval surface because test quantity preceded test design. The evidence-led method and rollback rule remain selected, but the agent must derive exact test contracts from real failures and task history before choosing a run count. Current evidence supports an adaptive default for unresolved project/product work, not literal activation for every non-build message.
Outcome: Drew selects or revises the automatic activation boundary in P-002.
Done when: The boundary distinguishes unresolved planning from direct builds, narrow facts/status, explanation, and diagnosis-only work clearly enough to define natural-invocation test cases without guessing.

Do not begin E-010 or any automated beta comparison until P-002 is complete and a replacement exact test route receives explicit approval.
