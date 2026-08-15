# E-010 — Lock the decision-kernel contract

Status: superseded draft — blocked by reopened P-002; do not execute until the automatic planning boundary and evidence-derived test contracts produce a replacement route.

- Outcome: One normative reference and one compact ticket ledger make Portable Planner's next-action logic inspectable without replacing model judgment.
- Depends on: P-002

## Context

- [Confirmed improvement method](../decisions/P-002-engineer-the-improvement-loop.md)
- [Expert engineering evidence](../evidence/P-002-expert-engineering-evidence.md)
- [Current question engine](../../plugins/portable-planner/skills/portable-planner/references/question-engine.md)

## In scope

- Define the precedence and legal transitions among fact research, reversible human choice, explicit delegation, protected decision, conflict, trial-needed uncertainty, approval, and normal build handoff.
- Define one compact frontier-ledger shape inside the existing planning ticket: decision, prerequisites, owner, uncertainty type, readiness, selected route, and expected state mutation.
- Reconcile existing canonical references and the planning-ticket template so one location is normative and other files point to it rather than restating divergent logic.
- Pre-register the hard gates and directional comparison rules used by E-011 through E-014.

## Out of scope

- Coding the subjective choice of the best product question, changing the visible A/B/C interaction, adding another skill or state tree, or editing behavior before the beta-5/beta-6 control comparison exists.

## Constraints

- Judgment remains in the model; only legal transitions and objective invariants become deterministic.
- Human-owned and protected decisions cannot be synthesized without explicit authority.
- The canonical skill remains lean and references stay one level deep.

## Proof

- Every current behavior class maps to exactly one allowed next action and state mutation.
- Ordinary, conflicting, delegated, digression, resume, trial, approval, and prohibited traces expose no contradictory precedence.
- Skill, references, template, product authority, and pre-registered evaluation contract agree.

## If blocked or disproven

- Return only a genuinely unresolved ownership or safety tradeoff to planning. Do not add infrastructure to resolve prose ambiguity.

## Human review

- None; P-002 already confirms the architecture boundary.

## Next eligible ticket

- E-011 — Build the bounded evaluation harness.
