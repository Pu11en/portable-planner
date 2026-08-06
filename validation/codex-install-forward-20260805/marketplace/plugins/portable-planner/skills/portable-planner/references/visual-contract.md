# Visual Contract

Create one route-first view that is useful in a rich chat, a plain Markdown viewer, or an unknown custom harness.

## Choose the view

- Use **route only** for a genuinely simple plan with no supporting systems or cross-links.
- Use **route plus connections** by default. Make the ordered route dominant and connect only the supporting systems or dependencies that change comprehension.
- Use a **full network** only when parallel branches or cross-dependencies cannot be understood from the route-first view.

Do not ask the user to choose the view. Select the simplest view that preserves every important relationship.

For multi-row routes, every row reads left to right. Continue from the end of one row to the start of the next without reversing the direction of alternate rows.

## Create and refresh

Create `planning/PLAN-VIEW.md` as soon as destination, success, current state, next action, and a coherent route are known, or immediately when the user asks to see the plan. Refresh it after a meaningful route or state change.

Automatically display it:

1. the first time the plan becomes coherent enough to view;
2. after a major route or dependency change;
3. after a fresh-session resume; and
4. at planning completion before human acceptance.

Treat a natural-language `continue` or `resume` request as the fresh-session trigger. Its first user-facing reply must contain the visible graph or complete compact text route when a coherent route exists; generating or linking `PLAN-VIEW.md` alone does not satisfy the trigger.

Do not interrupt every ordinary question with the full view.

## Keep the first view compact

Show:

- destination and success proof;
- current state, blocker, and next action;
- the complete ordered route;
- human decisions versus agent or automatic work;
- important supporting-system or dependency connections; and
- no more than six short plan-wide safety rules.

When the surface supports interaction, selecting any route step reveals its outcome, owner, inputs, proof, and failure behavior. In plain Markdown, provide the same information in compact collapsible or linked step details below the graph. Link deeper detail to canonical files instead of copying it into the view.

Show lifecycle status as `planning`, `awaiting approval`, or `approved for build`. The completed visual is the approval surface; it must not imply that building is authorized before explicit approval.

## Display without dependencies

Use this fallback order without asking the user to install anything:

1. Use a built-in rich artifact or visualization surface when it can produce the accepted route-first hierarchy and selectable step detail from `PLAN-VIEW.md` without another user install. Verify that it actually appears before claiming success.
2. Otherwise render the Mermaid block directly in the session when supported.
3. Otherwise use the harness's native Markdown artifact, attachment, or preview surface for `PLAN-VIEW.md`.
4. Otherwise open or show the local Markdown file using an available built-in file preview.
5. If no graphical surface exists, paste the compact text route and current-step detail from the same file in the session.

Never claim the visual was shown until it is visible. If a richer display errors, immediately fall back in the same turn and record the harness limitation. A terminal-only or text-only custom harness cannot produce a graphical popup; the text route is the guaranteed universal fallback.

A local-file link, attachment name, or statement such as “review the plan” is only navigation; it never proves display. At every automatic display trigger, the user-facing turn itself must contain either the visible rich graph, rendered Mermaid, or the complete compact text route. At planning completion, show that view and ask one explicit approval question in the same turn while status remains `awaiting approval`.

## Preserve one source of truth

Treat `PLAN-VIEW.md` only as a generated view. When it conflicts with canonical planning files, canonical state wins and the view must be regenerated.
