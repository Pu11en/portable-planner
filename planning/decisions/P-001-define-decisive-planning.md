# P-001 — Define decisive planning behavior

- Status: complete
- Depends on: none

## Decision

Define when Portable Planner should synthesize, ask, or switch to a bounded trial so it stays brief without taking decisions that belong to the user.

## Viable options

- A. Explicit scoped delegation plus an uncertainty router: synthesize reversible choices, ask only protected human decisions, and trial experiential uncertainty. Best balance of speed and control.
- B. Keep asking until every decision is individually confirmed. Maximizes ceremony and repeats the failure Drew reported.
- C. Let the agent infer broad authority from repeated agreement. Faster, but unsafe and likely to mistake fatigue for consent.

## Recommendation

A — It matches Drew's explicit delegation, Matt Pocock's discussion-to-prototype boundary, and the need to preserve final human control.

## Confirmed decision

- Record the user's exact delegation and scope. It persists for that plan until exhausted, revoked, contradicted, or blocked by a protected gate.
- Explicitly delegated reversible choices are synthesized with a compact choice and reason; repeated agreement alone never creates delegation.
- Only a complete trimmed bare recommended key increments the durable streak; any extra content or other reply resets it. After three consecutive matches, the next real reversible question keeps its recommendation as `A`, inserts delegation as `B`, and shifts remaining routes consecutively through at most `G`. Bare `B` applies the current recommendation and resolves remaining reversible decisions; the streak itself never grants authority.
- Do not ask when facts, prior words, or delegation already settle the issue, or when another verbal answer is unlikely to change the plan.
- Dynamic or experiential uncertainty switches to a bounded planning trial: one decision question, normally three materially different cases—ordinary, tricky, and failure or prohibited action.
- Preserve each trial's input or starting state, variation, observed output, surprise or failure, verdict, and decision changed. Show Drew only the compact comparison unless he asks for detail.
- A failed case receives one targeted planning revision and affected cases are rerun. Persistent failure or a new human tradeoff returns to Drew.
- Ordinary replies contain only the current result, next action, and at most one worthwhile question. When the next safe planning action is clear, perform it in the same turn instead of ending with an intention statement.
- After a side question, challenge, or context-rich paragraph, answer or reconcile first, recompute the frontier, and end with the complete refreshed lettered choice whenever a worthwhile human decision remains.
- Treat research or reused-project evidence that changes destination, audience, deliverable, success proof, or value-bearing source material as provisional until Drew confirms it or a bounded trial settles it.
- When the finish audit passes, proactively say planning is complete, show the compact route, and ask for explicit build approval. After the approved build passes agent-run checks, proactively present the smallest genuine user test and request live acceptance; do not leave Drew to guess whether or how to test.
- A live-test handoff reuses canonical context, gives the concrete action, applies safe defaults, and asks at most one genuinely missing protected blocker. It never becomes a bundled intake form.
- Before presenting a plan or human test, reconcile canonical status and regenerate the visual and handoff. A presentation failure is separate from plan validity and falls back without rewriting trustworthy state.
- At a real context boundary, create one successor only when authorized; otherwise show a clearly labeled exact next-session prompt. Never treat a ticket name or vague future-action statement as a completed handoff.
- Stop for irreversible commitments, uncovered material personal tradeoffs, conflicts, implementation authorization, and explicit final-plan approval.
- Apply the behavior across software, business, creative, operational, event, and personal planning without creating another mode or skill.

## Evidence

- [Research and scenario evidence](../evidence/P-001-evidence.md)
- [Beta.4 live failure evidence](../../validation/DECISIVE-FLOW-LIVE-ACCEPTANCE.md)

## Effects

- Product, acceptance, conversation, question, artifact, and validation guidance must agree.
- Cross-project scenarios and fresh live acceptance must demonstrate effectiveness before the public-preview behavior is described as proven.
- No new service, database, state tree, or production-prototype framework is justified.

## Complete when

Delegation, stopping, trial, brevity, immediate-action, proactive approval/testing, protected-gate, evidence, failure, and cross-project rules are explicit and every downstream execution ticket preserves them.
