# E-014 — Compare, keep, or reject the candidate

- Outcome: The remaining twelve-run budget decides objectively whether the isolated candidate may proceed or the winning beta-5/beta-6 reference must remain the product.
- Depends on: E-013

## Context

- [Frozen harness](E-011-build-bounded-evaluation-harness.md)
- [Beta-5/beta-6 control report](E-012-measure-beta6-baseline.md)
- [One candidate change](E-013-implement-one-candidate-change.md)

## In scope

- Run the two affected scenarios twice each, four unrelated visible regression scenarios once each, and two held-out scenarios twice each: twelve candidate runs total.
- Stop immediately on a protected-gate, ownership, authorization, state-integrity, or attribution failure.
- Compare the candidate with the winning reference using the pre-registered hard gates, targeted assertion, control run range, and directional metrics.
- Keep the candidate only when hard failures are zero, the target passes every repetition, held-out review finds no new missed major decision, and non-target turns/word count do not materially worsen without an explicitly accepted tradeoff.
- Reject a worse or inconclusive candidate without merging it. Preserve its traces as losing evidence.

## Out of scope

- Extra tuning rounds, changing metrics after results, averaging away a safety failure, merging before the verdict, or claiming human acceptance.

## Constraints

- Thirty automated runs is the absolute first-cycle ceiling: eighteen beta-5/beta-6 controls plus twelve candidate runs.
- “Inconclusive” resolves in favor of the winning reference.
- If candidate code was accidentally applied outside its branch, restore the reviewed reference behavior before continuing.

## Proof

- One signed-off comparison report links all thirty or fewer early-stopped runs and gives exactly one verdict: `keep candidate`, `reject candidate`, or `no candidate justified`.
- A kept candidate passes full package and installation audits from unchanged bytes.
- A rejected candidate is absent from `main`, releases, and the active public installation; the winning reference is installed and verified.

## If blocked or disproven

- Preserve the winning reference and return only a new product tradeoff or invalid evaluation method to planning. Do not spend more runs to force a conclusion.

## Human review

- None for the objective verdict. A kept candidate still requires E-015.

## Next eligible ticket

- E-015 — Run the controlled human acceptance, or stop with the winning reference if the candidate is rejected and no unchanged-reference human test is requested.
