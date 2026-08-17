# Next

Plan: `/home/drewp/main-projects/portable-planner/planning/`
State: `planning`
Work: **AGENT — Run E-019 objective and beta-6 regression checks**
Read: `PLAN.md`, `execution/E-019-compare-i01-candidate.md`, `validation/i01-plan-comprehension/README.md`, the canonical visual contract/template, and the existing beta-6 release-candidate evidence.
Context: Drew approved E-017 through E-020 with bare `A`; no delegation exists. E-017's six valid fixtures and six malformed controls pass. E-018 changes only the existing visual contract, template, and smallest static validator. Candidate bytes must remain unchanged during E-019.
Outcome: Preserve attributable I-01 and beta-6 regression results and give exactly one verdict: `candidate eligible for human test` or `candidate rejected`.
Done when: all six I-01 claims and affected beta-6 package/behavior checks pass against one candidate commit, or the first hard failure rejects the candidate while beta 6 remains recoverable.

Do not publish, merge to `main`, install over beta 6, begin E-020, or start I-02 before the E-019 verdict.
