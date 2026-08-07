# E-002 — Update the canonical skill

- Outcome: The one canonical Portable Planner skill performs the approved decisive and brief planning behavior.
- Depends on: P-001, E-001

## Context

- [Confirmed behavior](../decisions/P-001-define-decisive-planning.md)
- Updated product contract from E-001

## In scope

- Update the canonical skill and only the necessary conversation, question, artifact, validation, and template guidance.
- Add scoped delegation, uncertainty routing, short-output, immediate-action, bounded-trial, evidence-preservation, failure-retest, proactive approval and live-test handoffs, and protected-gate rules.

## Out of scope

- A second skill, mode, database, MCP server, web app, cloud dependency, production prototype, or domain-specific framework.

## Constraints

- Keep harness manifests and installers thin; keep all durable state in project-local `planning/`.

## Proof

- Skill validation and plugin-manifest validation pass; all referenced files and templates exist; instruction conflicts are absent.

## If blocked or disproven

- Record the exact instruction-level failure before proposing architecture expansion.

## Human review

- Review only if implementation exposes a new protected tradeoff.

## Next eligible ticket

- E-003 — Prove varied planning behavior.
