# P-002 / I-01 evidence — Comprehending large plans

Researched: 2026-08-15
Status: static-image comparison rejected; recovered positive control resets the target to a real plan shown directly inside the session

## Decision question

What presentation model lets Drew understand a large Portable Planner plan without reading the canonical reports or interpreting a dense Mermaid graph, while preserving exact state, dependencies, and portability?

## Observed problem

- Drew's latest feedback is that the visual plans are not correct, Mermaid does not provide comprehension value, and plans become especially hard to understand when they read like reports.
- The [recorded visual failure](../../validation/VISUAL-COMPREHENSION-FAILURE.md) found that the Hanoi view mixed route, current/invalid state, proof, scheduling, and support systems. It exposed implementation structure instead of answering where the user is, where the plan is going, and what happens next.
- The GOMER plan is a useful real stress case: its canonical `PLAN.md` is 144 lines and its current `PLAN-VIEW.md` is 242 lines. The view contains a short Mermaid route followed by many expanded reports, so it demonstrates that a compact graph plus a long detail dump is still a large reading task.
- The first comparison attempt converted three information-architecture directions into standalone PNG screens. Drew rejected the entire comparison because it did not put the usable plan experience inside the active conversation. Asking him to select among those images therefore measured the wrong thing.

## Recovered positive control

The local Codex history contains the earlier experience Drew said he loved:

- Task: `Build and Iterate the Planning Plug…`
- Task ID: `019fd2af-654e-78b0-81dd-b451b66ce60a`
- Positive reaction recorded: 2026-08-05 22:56 UTC
- Surface: one ordinary assistant reply inside the Codex session, not a separate application screen.

That reply presented the actual Hanoi plan state in a rendered route and immediately followed it with the current position, invalidated prior state, exact next action, complete text fallback, recovery rule, and separate posting-confirmation gate. It also showed the real human checkpoints and supporting systems. Drew's positive reaction followed that combined in-session presentation.

The recovered evidence changes the design question. The target is not “which diagram or dashboard looks best?” It is “how should the agent present the real canonical plan directly in the conversation so Drew can orient, inspect, correct, and act without opening a report?” Mermaid happened to render the earlier route, but renderer choice alone neither caused nor proves comprehension.

## Corrected in-session contract

The next candidate must:

1. Appear directly in the active planning conversation.
2. Use the current project's canonical state rather than invented mock text.
3. Make destination, success, current position, and exact next action visible before detail.
4. Show the meaningful route, human gates, proof, supporting systems, and recovery behavior.
5. Keep a complete native text path in the same reply.
6. Let Drew react to the concrete plan itself before choosing a renderer or product UI.
7. Treat a PNG, link-only handoff, generic pretend screen, or long report as a failed substitute.

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

The recovered positive control is stronger evidence than the generated screens. Use its in-session, real-state presentation as the baseline: short orientation first, real route second, current/next/proof/recovery in the same reply, and detail only where it helps the present decision. The focus-first, collapsible, and task-specific-view patterns remain research inputs, not choices Drew must make before seeing a faithful candidate. This is not authorization to implement a UI.

## Host feasibility

- Canonical truth remains the existing project-local Markdown plan and tickets.
- A portable structured outline can be generated without another state store.
- Windows Codex Desktop backed by WSL cannot use file-backed inline HTML through the current bridge. The supported in-session trial therefore uses ordinary rendered conversation content—native Markdown and, when useful, rendered Mermaid—rather than hiding the candidate in a local HTML file.
- The comparison must evaluate comprehension separately from whether a host can render a file. A presentation bridge failure is not a plan-model verdict, and a locally rendered mock is not human acceptance.

## Superseded bounded comparison

Use the actual read-only GOMER `planning/PLAN.md` and `planning/PLAN-VIEW.md` as the source. Do not reconstruct or mutate the GOMER plan.

The first attempt created exactly three visual directions:

1. Focus-first navigator.
2. Coordinated overview/current/dependency workspace.
3. Collapsible phase-card outline.

Retain the current Mermaid/report presentation as the negative control, not a fourth candidate direction.

This comparison is withdrawn. It turned the directions into standalone screens and asked Drew to choose before he could experience a real plan inside the session. No direction was selected.

## Failed evidence — F-I01-01 static-image detour

The authoritative option order is the order the three generated images appeared in the task:

1. [Focus-first navigator](../../validation/i01-plan-comprehension/focus-first-navigator.png)
2. [Coordinated multi-view workspace](../../validation/i01-plan-comprehension/coordinated-multiview-workspace.png)
3. [Collapsible phase outline](../../validation/i01-plan-comprehension/collapsible-phase-outline.png)

All three stable PNG files remain preserved as failed evidence. They are not active candidates, approved product UI, or state-fidelity proof. Besides introducing altered plan content, they removed the experience from the conversation and forced a premature screen-selection decision.

## Current bounded trial

Show the current Portable Planner improvement plan directly in the active session using the recovered positive-control structure. Explain what is settled, what is not settled, the current position, exact next action, route, proof, and recovery rule. Do not ask Drew to choose a rendering family in the same reply. His natural reaction to that concrete presentation will identify which parts provide orientation and which still fail; only then should a narrower alternative be planned.
