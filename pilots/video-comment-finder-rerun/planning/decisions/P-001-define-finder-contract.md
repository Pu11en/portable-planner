# P-001 — Define the Finder Contract

- Status: current
- Depends on: none

## Decision

Define the smallest dependable operating contract for the skill: how a run gets AI-related YouTube videos, what makes a comment question worthwhile, what evidence makes Drew qualified to answer it, and exactly what each linked option shows. These choices determine whether the result is useful without drifting into content creation.

## Viable options

- Source videos supplied for each run: Drew pastes one or more video links. Tightest and easiest to trust, but requires manual sourcing.
- Saved source list: the skill scans a maintained set of AI channels. More repeatable, but needs upkeep and may narrow discovery.
- Open discovery: the skill finds recent AI-related videos itself. Broadest reach, but adds relevance, freshness, and search-quality decisions.

## Recommendation

Use Drew's saved pool of AI channel names as the discovery boundary. This gives the skill room to find relevant videos without the noise of open-ended discovery; Drew accepts the upkeep and narrower reach of the pool.

## Confirmed decision

Confirmed source mode: Drew supplies and maintains a saved group of AI channel names that he believes will have good comments. On each run, the skill discovers relevant videos only within that provided channel pool, then searches those videos for worthwhile comment questions.

Confirmed hard boundary: the skill presents several linked questions Drew is qualified to answer and stops. Drew manually chooses and opens a comment, then records the answer; the skill does not answer, script, record, edit, publish, reply, or choose for him. The worth, qualification, and output rules are not yet confirmed.

## Evidence

- No external evidence needed; the open choices are product-direction preferences.

## Effects

- Channel-pool storage and maintenance belong in execution scope, along with discovery of relevant videos within that pool.
- Open-web video discovery and per-run video-link input are outside the initial skill contract.
- The worth and qualification rules will determine the acceptance tests for returned options.
- The output contract must preserve the hard stop before answer creation.

## Complete when

The source mode, worthwhile-question rule, qualification evidence, output fields, and hard-stop behavior are explicit; their tradeoffs and downstream effects agree with `PLAN.md`; and the finish audit can produce dependency-ordered, session-sized execution tickets without guessing.
