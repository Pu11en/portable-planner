# Engineer an evidence-led improvement loop

Type: planning and validation
Status: planned; awaiting approval
Blocked by:

## Question

How should Portable Planner improve after beta 6 so the hidden planning logic becomes more reliable without adding question burden, context bloat, or unjustified infrastructure?

## Current evidence

- The current Matt Pocock and David Ondrej repositories still support a decision tree, prerequisite-ready frontier, fact-versus-decision ownership, immediate durable state, concise recommendations, and verify-fix-reverify loops.
- Channel Brains adds the authors' rationale: strict processes compensate for agent memory limits, excessive instructions waste context, and autonomous optimization is unsuitable when “better” remains subjective.
- The strongest unresolved engineering gap is not the visible A/B/C interaction. It is whether the model selects the correct frontier, honors ownership and protected modes, mutates state correctly, and does so consistently across repeated runs.

The full primary-source record and inference boundary are in [P-002 evidence](../../planning/evidence/P-002-expert-engineering-evidence.md).

## Provisional route

1. Define one normative decision-kernel transition contract inside the existing skill/reference architecture.
2. Add a compact frontier ledger to the existing planning ticket rather than creating another state tree.
3. Build a bounded scenario corpus and deterministic invariant validator.
4. Measure repeated unchanged beta-6 runs before editing instructions.
5. Make one minimal revision for one demonstrated failure class.
6. Rerun affected, regression, and held-out cases.
7. Require Drew's uncoached real-task judgment before release.

The recommended first-cycle ceiling is 24 automated fresh-task scenario runs with early stop on a hard failure, plus one separate uncoached human run. The cap may not be used for repeated tuning against the same visible cases.

## Acceptance

Option A is confirmed in [P-002](../../planning/decisions/P-002-engineer-the-improvement-loop.md); hard failure gates, directional metrics, the 24-run ceiling, candidate isolation, beta-6 restoration, and the human gate are explicit; [E-010 through E-016](../../planning/PLAN.md) cover the complete experiment. This issue resolves only when the candidate proves better and ships, or the losing candidate is preserved and beta 6 remains the verified product.
