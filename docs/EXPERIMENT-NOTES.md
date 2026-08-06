# Portable Planner Experiment

**Status:** Unproven MVP experiment. Do not treat this as a permanent product or course component until the acceptance checklist passes and Drew approves both real-use flows.

## Purpose

Test whether one portable Agent Skill can turn a vague idea into a cohesive plan, durable fresh-session handoffs, and session-sized execution tickets with less friction than Drew's current planning experience.

## Boundaries

- Canonical planning logic lives in `../plugins/portable-planner/skills/portable-planner/`.
- Test evidence lives in `../validation/` and `../pilots/`.
- Forward-test state lives under `../validation/`; old pilot fixtures remain historical evidence only.
- Human evidence comes from Drew naturally using the installed plugin for any real plan in a fresh task without test coaching. Later, one naturally complex real plan must also exercise dependencies, gates, revision, recovery, and execution tickets. Canned examples and implementation forward tests do not count as Drew's acceptance.
- The MVP uses project-local Markdown, including a generated Mermaid plan view with a compact text fallback. It has no MCP server, database, web app, cloud account, GitHub dependency, renderer dependency, or domain pack.
- This repository is the project source. Harness installation copies the same canonical skill; it must not fork the planning logic.

## Acceptance source

[`PRODUCT-CONTRACT.md`](./PRODUCT-CONTRACT.md) is the concise source for the product behavior Drew has confirmed so far, including the planning-only boundary and the accepted visual direction.

[`ACCEPTANCE.md`](./ACCEPTANCE.md) translates the destination and validation standard in [`MVP-PLAN.md`](./MVP-PLAN.md) into pass/fail checks.

[`../validation/EFFECTIVENESS.md`](../validation/EFFECTIVENESS.md) defines how the planning experience is measured during pilots.

[`GOAL.md`](./GOAL.md) records Drew's revised requirement for one-link same-session installation and a built-in visual plan. It supersedes the earlier visual-graph exclusion while the experiment is active.
