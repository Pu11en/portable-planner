# Visual Contract

Create one route-first view from canonical plan state. In Codex, prefer the approved interactive presentation. In a plain Markdown viewer or unknown custom harness, preserve the same plan through `PLAN-VIEW.md` and its Mermaid/text route.

## Choose the view

- Use one **milestone route** by default: five to nine short outcome labels in one dominant reading direction.
- Keep current state, next action, success proof, and plan-wide rules immediately above or below the route instead of turning each into another graph node.
- Put supporting systems, architecture, owners, inputs, failure paths, and step-level work in the expandable details below the route. Do not mix those maps into the overview merely because the source plan contains them.
- Add a branch or dependency edge only when omitting it would make the execution order false. If a plan still cannot be understood in nine overview milestones, show one overview plus a separate visual for the affected phase when the user opens it.

Do not ask the user to choose the view. Select the simplest view that preserves every important relationship.

For multi-row routes, every row reads left to right. Continue from the end of one row to the start of the next without reversing the direction of alternate rows.

## Decide when to show it

Create `planning/PLAN-VIEW.md` as soon as destination, success, current state, next action, and a coherent route are known, or immediately when the user asks to see the plan. Refresh it after a meaningful route or state change.

Use an adaptive hybrid gate; never count questions:

- **Requested draft:** “Show me the plan” or equivalent always displays the best current view. Keep lifecycle status `planning` unless the finish audit independently passes.
- **Useful draft offer:** while grilling, the agent may offer the view once when a coherent route would materially help the user judge direction. Do not repeatedly ask whether they want to see it.
- **Automatic final review:** display the view without first asking permission when the full route is defensible and the finish audit passes. Set lifecycle status to `awaiting approval` before display.
- **State refresh:** redisplay after a major route or dependency change when the previous view would mislead, and in the first reply after a fresh-session resume when a coherent route exists.

The full route is defensible when destination and observable success are clear; boundaries are explicit; major human-owned decisions are settled; the end-to-end order, important dependencies, human gates, risks, and recovery behavior are coherent; execution tickets can be derived without reopening major planning; and canonical artifacts agree. Do not delay review for minor implementation mechanics the agent can safely infer.

Treat a natural-language `continue` or `resume` request as the fresh-session trigger. Its first user-facing reply must contain the visible graph or complete compact text route when a coherent route exists; generating or linking `PLAN-VIEW.md` alone does not satisfy the trigger.

Do not interrupt every ordinary question with the full view.

## Keep the first view compact

Show:

- destination and success proof;
- current state, blocker, and next action;
- the complete ordered route as five to nine plain-language milestones;
- human decisions versus agent or automatic work when that distinction changes what the person must do; and
- no more than six short plan-wide safety rules.

The overview is a roadmap, not an architecture diagram. Never combine the product's operating loop, implementation architecture, support-system network, and build route in one graph. Pick the route that answers: “Where are we going, where are we now, and what happens next?” Keep the other views in linked detail.

When the surface supports interaction, selecting any route step reveals its outcome, owner, inputs, proof, and failure behavior. In plain Markdown, provide the same information in compact collapsible or linked step details below the graph. Link deeper detail to canonical files instead of copying it into the view.

Show lifecycle status as `planning`, `awaiting approval`, or `approved for build`. The completed visual is the approval surface; it must not imply that building is authorized before explicit approval.

## Give the route deliberate visual design

- Use a small semantic style system carried by literal labels, node shapes, and emphasis: `NOW`, numbered milestones, `HUMAN` where a person must act, `DONE` or `PROOF`, and `BLOCKED` or `INVALID` when necessary.
- Let the host's Mermaid theme supply light/dark-safe colors. Never hardcode a light-only or dark-only palette, and never let color alone carry meaning.
- Make the current milestone and final destination the strongest nodes. Keep peer milestones visually consistent.
- Do not place supporting-system cards or a web of dashed links in the overview. They belong in the selected milestone's detail unless a single dependency line is essential to make the route truthful.
- Use the same class for peer steps rather than decorating every node differently. Do not add custom color, icons, legends, or containers that do not improve comprehension.
- Put the class definitions in `PLAN-VIEW.md` itself so styling remains zero-dependency and portable. If a harness ignores Mermaid styling, the labels, shapes, links, and text route must still carry the full meaning.
- Keep the design polished but restrained: styling may improve hierarchy and scanability, never add plan content or become a second source of truth.

## Display without dependencies

Use this fallback order without asking the user to install anything:

1. In Codex or another capable host, use its available built-in visualization capability to create an in-session interactive view with destination/current/next summary cards, a clickable ordered route, one selected-step detail surface, compact support connections, and a short plan-wide safety line. Follow that host capability's required writable path and display reference, verify the view actually appears, and require no separate renderer, app, runtime, or user download. If no such capability is available, continue immediately to the portable fallback.
2. Otherwise render the Mermaid block directly in the session when supported.
3. Otherwise use the harness's native Markdown artifact, attachment, or preview surface for `PLAN-VIEW.md`.
4. Otherwise open or show the local Markdown file using an available built-in file preview.
5. If no graphical surface exists, paste the compact text route and current-step detail from the same file in the session.

Never claim the visual was shown until it is visible. If a richer display errors, immediately fall back in the same turn and record the harness limitation. A terminal-only or text-only custom harness cannot produce a graphical popup; the text route is the guaranteed universal fallback.

A local-file link, attachment name, or statement such as “review the plan” is only navigation; it never proves display. At every automatic display trigger, the user-facing turn itself must contain either the visible rich view, rendered Mermaid, or the complete compact text route. At planning completion, show that view and ask one explicit approval question in the same turn while status remains `awaiting approval`.

Do not export or substitute a PNG, screenshot, or other raster image for the normal in-session plan view. Drew explicitly rejected that presentation. A raster export is allowed only when the user separately asks to save or share an image.

## Preserve one source of truth

Treat `PLAN-VIEW.md` only as a generated view. When it conflicts with canonical planning files, canonical state wins and the view must be regenerated.

Any host-native interactive surface is also generated from the same canonical state. It may improve presentation and interaction, but it cannot introduce or own plan decisions.
