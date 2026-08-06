# E-005 — Filter, Deduplicate, and Rank Questions

- Outcome: A deterministic evaluation pipeline keeps only distinct, specific, useful questions Drew can credibly answer, then orders them with a recent-comment preference and an older-exception path.
- Depends on: P-001, E-004

## Context

- [Confirmed qualification, rejection, and selection contract](../decisions/P-001-define-finder-contract.md)
- E-001's substantiated Drew qualification reference
- E-004's exact sourced candidate records

## In scope

- Apply hard rejection gates before any score: spam/promotion, vague praise, no answerable question, trolling/abuse, engagement bait, irrelevant requests, credential-required advice, insufficient context, and questions too broad for a useful short response.
- Normalize and cluster semantic duplicates across channels/videos; retain the best sourced, most specific version.
- Score survivors on specificity, substantiated Drew-fit, practical audience value, distinctness, and useful 30–90-second answerability.
- Apply recency as a preference/tie-breaker and define a documented threshold for an older candidate to beat recent alternatives.
- Assign high/medium/low confidence from provenance clarity, interpretation ambiguity, and Drew-fit—not from invented certainty.
- Continue or stop according to the bounded source budget; never lower gates to reach five.

## Out of scope

- Browsing, source capture, changing Drew's qualification profile without evidence, drafting Drew's answer, or rendering the final report.

## Constraints

- A candidate must pass the qualification and specificity gates regardless of likes or apparent popularity.
- A credential-sensitive question is rejected unless the local profile explicitly substantiates that credential.
- Duplicate topics cannot occupy multiple top-five slots merely because wording differs.

## Proof

- A labeled evaluation set rejects every required bad class and explains the triggered gate.
- Duplicate clusters retain one winner deterministically.
- A recent-versus-older fixture prefers recent near-ties but selects an older exceptional question when its substantive score clears the documented threshold.
- Ranking is repeatable for identical inputs and returns no more than five survivors.

## If blocked or disproven

- If real examples expose a missing rejection class or unstable tie, fix the reference and fixtures. Return to P-001 only if the confirmed product goal requires a new human preference.

## Human review

- Drew reviews false-positive/false-negative qualification examples in E-008; he is not asked to tune internal weights.

## Next eligible ticket

- E-006 — Render the five-result handoff.
