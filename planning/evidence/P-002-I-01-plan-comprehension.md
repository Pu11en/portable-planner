# P-002 / I-01 evidence — Comprehending large plans

Researched: 2026-08-15
Status: three visual directions generated from the same GOMER brief; awaiting Drew's selection or refinement

## Decision question

What presentation model lets Drew understand a large Portable Planner plan without reading the canonical reports or interpreting a dense Mermaid graph, while preserving exact state, dependencies, and portability?

## Observed problem

- Drew's latest feedback is that the visual plans are not correct, Mermaid does not provide comprehension value, and plans become especially hard to understand when they read like reports.
- The [recorded visual failure](../../validation/VISUAL-COMPREHENSION-FAILURE.md) found that the Hanoi view mixed route, current/invalid state, proof, scheduling, and support systems. It exposed implementation structure instead of answering where the user is, where the plan is going, and what happens next.
- The GOMER plan is a useful real stress case: its canonical `PLAN.md` is 144 lines and its current `PLAN-VIEW.md` is 242 lines. The view contains a short Mermaid route followed by many expanded reports, so it demonstrates that a compact graph plus a long detail dump is still a large reading task.

## Comprehension jobs

A useful plan surface must let Drew do these jobs without first opening the long source files:

1. State the intended result and how success will be recognized.
2. Identify the current phase, immediate next action, and the next meaningful milestone.
3. See which steps are done, current, blocked, or human-owned.
4. Open one relevant phase and understand its outcome, inputs, proof, and failure behavior.
5. See a dependency only when it changes what can happen next.
6. Return from detail to the whole-plan orientation without losing position.
7. Switch to a different useful view without creating a second source of truth.

## Direct pattern evidence

- Ben Shneiderman's original information-visualization taxonomy frames the interaction as “overview first, zoom and filter, then details-on-demand.” The University of Maryland hosts the [original paper and abstract](https://drum.lib.umd.edu/items/155a868e-fb83-4115-9899-9187ea8c0498).
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects) keeps one project collection but supports table, board, and roadmap layouts plus filtering, sorting, and grouping. This is evidence that one plan may need task-specific views rather than one universal diagram.
- [Linear's project overview](https://linear.app/docs/project-overview) separates a brief summary, properties, resources, descriptions, and milestones; its [milestone model](https://linear.app/docs/project-milestones) exposes current progress and permits filtering into one milestone.
- W3C's accessible [accordion pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/) and [disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) support hiding detail behind meaningful headings while preserving keyboard access and explicit expanded/collapsed state.
- Microsoft's [Tree View guidance](https://learn.microsoft.com/en-us/windows/apps/design/controls/tree-view) recommends a tree when nested relationships are the task, but says a regular list is more appropriate for ordinary drill-in. This cautions against making hierarchy or graph structure the default experience.

## Solution families

### S-01 — Focus-first plan navigator — provisional recommendation

- Persistent orientation: destination, proof of success, current phase, next action, and blocker.
- A short ordered list of phases replaces the dependency graph as the main navigation.
- One selected phase opens beside or below the list with outcome, decisions, inputs, proof, and recovery behavior.
- Dependency, owner, and history controls appear only when relevant to the selected phase.
- Strongest fit: understanding and acting on one large plan without losing the whole.
- Main tradeoff: requires a genuinely interactive surface for the best experience; the portable fallback becomes a structured outline rather than an equivalent interaction.

### S-02 — Coordinated multi-view workspace

- One canonical plan can be viewed as Overview, Current, Route, Dependencies, and optionally Timeline.
- Each view answers a different question; filters and selection persist across them.
- Strongest fit: plans where scheduling, dependencies, and status are all important at different moments.
- Main tradeoff: tabs and view choices can become another layer of product complexity. The default view and route must remain obvious.

### S-03 — Collapsible phase cards or hierarchical outline

- Each phase always shows a short title, state, and one-line outcome; expanding it reveals detail.
- Works in browser UI and has a close accessible Markdown/HTML fallback.
- Strongest fit: zero-dependency portability and linear reading.
- Main tradeoff: cross-phase dependencies and alternate routes are weaker unless a separate filtered dependency view exists.

### S-04 — Spatial graph with semantic zoom

- The graph begins with phases; zooming or selection reveals nested decisions, work, and dependencies.
- Strongest fit: cases where relationship discovery is itself the user's job.
- Main tradeoff: navigation, layout instability, edge crossings, and spatial memory add interpretation cost. It should be an optional dependency view, not the default plan surface, unless comparison evidence overturns this concern.

## Provisional synthesis

The strongest direction is not one of these families in isolation. Use S-01 as the default comprehension experience, use S-03 as its portable fallback, and borrow S-02 only for optional task-specific views. Keep a graph, if any, as an optional dependency inspection mode. This is provisional until distinct visual prototypes are compared; it is not authorization to implement a UI.

## Host feasibility

- Canonical truth remains the existing project-local Markdown plan and tickets.
- A portable structured outline can be generated without another state store.
- Windows Codex Desktop backed by WSL cannot use file-backed inline HTML through the current bridge. A real interactive prototype must be shown through a browser/Site or another supported host; Mermaid remains a static fallback only.
- The comparison must evaluate comprehension separately from whether a host can render a file. A presentation bridge failure is not a plan-model verdict, and a locally rendered mock is not human acceptance.

## Bounded comparison

Use the actual read-only GOMER `planning/PLAN.md` and `planning/PLAN-VIEW.md` as the source. Do not reconstruct or mutate the GOMER plan.

Create exactly three visual directions:

1. Focus-first navigator.
2. Coordinated overview/current/dependency workspace.
3. Collapsible phase-card outline.

Retain the current Mermaid/report presentation as the negative control, not a fourth candidate direction.

For each direction, show the same GOMER state and ask Drew to perform the same tasks: identify the destination, current decision, next milestone, one human gate, one failure rule, and return to the overview after inspecting a phase. Preserve the output and Drew's concrete confusion or success. The direction that makes these tasks easiest without hiding important state becomes the I-01 candidate; no implementation begins before that judgment.

## Generated directions

The authoritative option order is the order the three generated images appeared in the task:

1. [Focus-first navigator](../../validation/i01-plan-comprehension/focus-first-navigator.png)
2. [Coordinated multi-view workspace](../../validation/i01-plan-comprehension/coordinated-multiview-workspace.png)
3. [Collapsible phase outline](../../validation/i01-plan-comprehension/collapsible-phase-outline.png)

All three stable PNG files were copied into the repository and verified as 1487 × 1058 RGB images. They are visual structure concepts, not approved product UI or state-fidelity proof. Image generation introduced some extra or altered phase wording, dates, and implementation details despite the shared source brief; those discrepancies are failures to correct in a selected prototype, not plan decisions. Drew should judge the information hierarchy and interaction direction rather than accept the mock text as canonical GOMER state.
