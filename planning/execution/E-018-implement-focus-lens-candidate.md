# E-018 — Implement the Journey plus focus lens candidate

- Status: draft — requires E-017 and human review of the I-01 route
- Depends on: E-017

## Outcome

Portable Planner generates the accepted compact route, one focal current step, one focus lens, and one quiet rail from canonical plan state while preserving a semantically equal text fallback.

## Context

- [Frozen I-01 contract](E-017-freeze-i01-fidelity-contract.md)
- [Accepted candidate evidence](../evidence/P-002-I-01-plan-comprehension.md)
- Canonical skill: `plugins/portable-planner/skills/portable-planner/`

## In scope

- Update the existing visual contract and `PLAN-VIEW.md` template to encode five-to-nine route milestones, exactly one focal current milestone, and the focus-lens fields: current outcome, next action, human role, proof, and recovery.
- Keep remaining issues and no more than six plan-wide rules subordinate to the route.
- Keep Mermaid and compact text routes semantically equivalent and visible in the active session.
- Add only the smallest static validator needed for assertions that existing checks cannot express.

## Out of scope

- An application UI, dashboard, browser renderer, file-backed inline HTML, PNG export, second skill/state tree, database, service, or unrelated conversation behavior.

## Constraints

- Canonical planning files remain the only source of truth; the view introduces no decisions.
- Literal labels and shapes preserve meaning without color.
- Essential comprehension never requires expansion or a file link.
- Prefer deleting conflicting or duplicate visual instructions over adding another parallel rule set.

## Proof

- Skill, visual contract, template, and any validator agree on the accepted grammar.
- Static skill, plugin, link, manifest, template-reference, and malformed-fixture checks pass.
- The diff contains no unrelated behavior or architecture.

## If blocked or disproven

- Return the exact unexpressible assertion to planning. Do not add a renderer or infrastructure automatically.

## Human review

- None until objective comparison passes.

## Next eligible ticket

- E-019 — Run the I-01 objective comparison and regression checks.
