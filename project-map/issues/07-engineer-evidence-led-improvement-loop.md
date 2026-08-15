# Engineer an evidence-led improvement loop

Type: planning and validation
Status: planning; P-002 reopened after premature test-count selection
Blocked by:

## Question

How should Portable Planner improve after beta 6 so the hidden planning logic becomes more reliable without adding question burden, context bloat, or unjustified infrastructure?

## Current evidence

- The current Matt Pocock and David Ondrej repositories still support a decision tree, prerequisite-ready frontier, fact-versus-decision ownership, immediate durable state, concise recommendations, and verify-fix-reverify loops.
- Channel Brains adds the authors' rationale: strict processes compensate for agent memory limits, excessive instructions waste context, and autonomous optimization is unsuitable when “better” remains subjective.
- The strongest unresolved engineering gap is not the visible A/B/C interaction. It is whether the model selects the correct frontier, honors ownership and protected modes, mutates state correctly, and does so consistently across repeated runs.
- Portable Planner remains one original cross-domain protocol. Outside repositories may supply adapted mechanisms only when a named failure, architecture fit, and materially different software/non-software cases justify them.

The full primary-source record and inference boundary are in [P-002 evidence](../../planning/evidence/P-002-expert-engineering-evidence.md).

## Provisional route

1. Settle the automatic planning boundary so natural-invocation tests have a truthful expected route.
2. Inventory material failures from saved live records and relevant Codex/ZCode task traces before authoring synthetic prompts.
3. Give every retained case an exact starting state, natural user message, behavior claim, expected route, prohibited assumption, objective invariant, and human judgment.
4. Collapse duplicate claims, then choose the minimum ordinary, contrasting, and prohibited-action set; add repetition only for observed variance or protected high risk.
5. Define one normative decision-kernel transition contract and lightweight objective validator inside the existing skill/reference architecture.
6. Compare immutable beta 5 and beta 6, restore the better reference, and make at most one candidate correction for one demonstrated failure.
7. Require Drew's uncoached real-task judgment before release.

No automated-run count is approved. Quantity follows from the visible test contracts and their discrimination needs; it may not precede or substitute for test design.

## Acceptance

The evidence-led method is confirmed in [P-002](../../planning/decisions/P-002-engineer-the-improvement-loop.md), while the activation boundary, exact test contracts, and resulting run count remain open. E-010 through E-016 are superseded drafts and cannot execute until those decisions produce a replacement route. This issue resolves only when the approved cases prove which released version is the reference and any candidate proves better without weakening it—or the losing candidate is preserved and the better reference remains installed.
