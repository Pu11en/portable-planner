# Wayfinder map: Finish Portable Planner

## Destination

A decision-complete, Drew-approved product behavior spec for Portable Planner from a vague idea through one-question planning, automatic interactive plan review, revision or approval, durable execution tickets, and normal-harness build handoff. Reaching the destination means implementation and the two required real-use proofs can finish without inventing more product behavior.

## Notes

- This map decides the remaining product behavior; it does not replace the active MVP acceptance checklist or perform final-plan execution.
- Use the confirmed planning-only boundary, plain project-local state, one consequential human question per turn, recommendation-first `A/B/C(/D)` choices, and no rigid question count.
- The approved Codex presentation is the earlier interactive Hanoi style: destination/current/next summary, clickable ordered route, one selected-step detail surface, compact supporting-system connections, and short plan-wide safety rules.
- Automatically display that review surface when the agent can defend a coherent end-to-end plan. Keep Mermaid/Markdown/text as portability fallbacks rather than the preferred Codex experience.
- Keep all implementation isolated in this repository; do not add MCP, a database, web app, cloud account, GitHub requirement, domain pack, or competing build workflow.
- Human evidence must come from Drew's ordinary plans in fresh tasks. An implementation simulation or canned example cannot stand in for him.

## Decisions so far

- [Planning-only product boundary](../docs/PRODUCT-CONTRACT.md) — Portable Planner plans and hands approved tickets to the harness; it does not replace normal build behavior.
- [Question and state contract](../plugins/portable-planner/skills/portable-planner/SKILL.md) — one highest-value human decision at a time, facts researched or derived, immediate local write-through, and exact fresh-session resumption.
- [Interactive visual direction](../validation/HANOI-HUMAN-ACCEPTANCE.md) — Drew identified the earlier interactive Hanoi display as the presentation to keep; exported images and a plain Mermaid-only Codex experience are rejected.
- [Portability baseline](../validation/PORTABLE-VIEW-TEST.md) — canonical state and planning logic remain unchanged across Codex and Hermes; each host shows its richest supported view with a complete text fallback.
- [Objective MVP evidence](../docs/ACCEPTANCE.md) — conversation, state, ticket, install, cross-project, and Codex/Hermes checks are already evidenced; human live experience remains the final authority.
- [Adaptive review gate](issues/01-decide-adaptive-review-gate.md) — the visual is always available, may be offered once as a useful draft, and opens automatically only when the complete route is defensible; approval, targeted revision, continued planning, and confusion each return to an explicit lifecycle path without a question-count threshold.
- [Idea-stage possibility scan](issues/05-prove-idea-stage-possibility-scan.md) — a new no-idea or thin-idea software/AI start may opt into bounded repository-first discovery, but the result remains provisional and unproven until objective scenario checks and Drew's fresh-session use pass.

## Not yet specified

- Exact implementation corrections exposed by the first real plan and the first naturally complex real plan.
- Exact corrections exposed by the idea-stage scenario matrix and Drew's first natural fresh-session scan.
- Whether naturally complex use exposes a genuinely new planning behavior after the first real-use flow is clean.
- The final wording Drew uses to judge speed, worthwhile questions, boundary clarity, usable plans, and executable handoff after both real-use proofs.

## Out of scope

- A new build mode, implementation agent, or replacement for each harness's normal build behavior.
- MCP, database-backed state, hosted web app, cloud account, GitHub dependency, domain pack, or mandatory renderer.
- A repository-cloning pipeline, required GitHub account, automatic dependency installation, or claim that repository popularity proves a product idea.
- A graphical popup guarantee in terminal-only or text-only harnesses.
- Publishing the plugin repository before the verified local experiment and Drew's final acceptance pass.
