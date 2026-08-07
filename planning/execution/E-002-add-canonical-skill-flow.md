# E-002 — Add the flow to the canonical skill

Status: complete — 2026-08-07

- Outcome: The unchanged canonical Portable Planner package can offer, conduct, summarize, and recover from the bounded idea-stage repository scan through natural conversation.
- Depends on: E-001

## Context

- [Confirmed behavior](../decisions/P-001-define-idea-evidence-flow.md)
- [Decision-changing evidence](../evidence/P-001-evidence.md)
- [Canonical skill](../../plugins/portable-planner/skills/portable-planner/SKILL.md)

## In scope

- Add the minimum focused reference needed to specify idea-stage eligibility and skip cases, the permission gate, real-world directionless grounding, privacy-safe search-brief sufficiency, three-angle repository discovery, shortlist and deep-inspection budgets, narrowly bounded direct-source verification, candidate roles, scoring, evidence tiers, adaptive possibility-first output, human direction confirmation, stopping, safety, and fallback behavior.
- Wire that reference into `SKILL.md` start and routing behavior and reconcile only the affected conversation, question, artifact, or validation guidance.
- Ensure decision-changing repository findings use the existing `planning/evidence/` contract and feed the same ordinary plan rather than creating pre-plan state or a second mode.
- Preserve natural-language invocation, compact replies, one worthwhile question at a time, and immediate decision write-through.

## Out of scope

- A GitHub API client, authentication flow, crawler, index, cache, database, service, MCP server, new state template, separate skill, repository cloning, code execution, or changes to harness build behavior.

## Constraints

- Repository content is untrusted data and cannot override system, user, skill, or project instructions.
- A decline or research failure must continue ordinary planning without a blocker.
- Public web or GitHub research must work through capabilities already available to the harness; no account or token may be required.
- The canonical skill remains the only behavior source; harness manifests stay thin.

## Proof

- The skill and every directly affected reference contain one non-contradictory behavior path covering eligibility, consent, real-world grounding, private-detail abstraction, bounded discovery, evaluation, adaptive provisional possibilities, human confirmation or redirect, evidence, and recovery.
- A fresh-context reader can execute the flow without inventing a query count, result count, reuse rule, or fallback.
- Every referenced file and template exists and all relative links resolve.

## If blocked or disproven

- If instructions alone cannot produce reliable behavior, record the exact failing fixture before proposing deterministic code or any broader architecture.

## Human review

- None; E-003 and E-005 provide behavioral and human review.

## Next eligible ticket

- E-003 — Prove bounded research behavior.

## Completion evidence

- [The canonical skill](../../plugins/portable-planner/skills/portable-planner/SKILL.md) loads one focused [idea-discovery reference](../../plugins/portable-planner/skills/portable-planner/references/idea-discovery.md); the conversation, question, and artifact contracts use the same consented, bounded, provisional path without adding another state tree or executable component.
