# Visual Contract

Create one **Journey plus focus lens** view from canonical plan state. Its first read must answer, with less reading than the underlying plan: where are we going, where are we now, what happens next, what does the person own, how do we know this step worked, and what happens if it does not. In Codex, prefer the approved interactive presentation. In a plain Markdown viewer or unknown custom harness, preserve the same plan through `PLAN-VIEW.md` and its Mermaid/text route.

## Choose the view

- Use one **journey route**: five to nine short outcome milestones in one dominant reading direction. Mark exactly one milestone `NOW`; use literal state labels such as `DONE`, `NEXT`, `HUMAN`, `BLOCKED`, and `PROOF` only where they change comprehension.
- Put one **focus lens** immediately beside or below the route. It contains exactly the current outcome, exact next action, human role or `none`, objective proof, and recovery behavior. Keep these fields visible without expansion.
- Put remaining issues and no more than six plan-wide guardrails in one quiet rail below the focus lens. They are subordinate context, not peer milestones or graph nodes.
- Put supporting systems, architecture, owners, inputs, and step-level work in expandable or linked detail below the first read. Do not mix those maps into the overview merely because the source plan contains them. Recovery for the current step stays in the visible focus lens.
- Add a branch or dependency edge only when omitting it would make the execution order false. If a plan still cannot be understood in nine overview milestones, show one overview plus a separate visual for the affected phase when the user opens it.

Do not ask the user to choose the view. Select the simplest view that preserves every important relationship.

For multi-row routes, every row reads left to right. Continue from the end of one row to the start of the next without reversing the direction of alternate rows.

## Decide when to show it

Create `planning/PLAN-VIEW.md` as soon as destination, success, current state, next action, and a coherent route are known, or immediately when the user asks to see the plan. Refresh it after a meaningful route or state change, including material execution progress. Immediately before any human test or display trigger, compare it with canonical state and regenerate it if completed/current status, blockers, or next action changed.

Use an adaptive hybrid gate; never count questions:

- **Requested draft:** “Show me the plan” or equivalent always displays the best current view. Keep lifecycle status `planning` unless the finish audit independently passes.
- **Useful draft offer:** while grilling, the agent may offer the view once when a coherent route would materially help the user judge direction. Do not repeatedly ask whether they want to see it.
- **Automatic final review:** display the view without first asking permission when the full route is defensible and the finish audit passes. Set lifecycle status to `awaiting approval` before display.
- **State refresh:** redisplay after a major route or dependency change when the previous view would mislead, and in the first reply after a fresh-session resume when a coherent route exists.

The full route is defensible when destination and observable success are clear; boundaries are explicit; major human-owned decisions are settled; the end-to-end order, important dependencies, human gates, risks, and recovery behavior are coherent; execution tickets can be derived without reopening major planning; and canonical artifacts agree. Do not delay review for minor implementation mechanics the agent can safely infer.

Treat a natural-language `continue` or `resume` request as the fresh-session trigger. Its first user-facing reply must contain the visible graph or complete compact text route when a coherent route exists; generating or linking `PLAN-VIEW.md` alone does not satisfy the trigger.

An automatic successor prompt that only points to `NEXT.md` is a machine handoff, not a natural-language `continue` or `resume` request. Do not force the full visual in every chained task. The requested-draft, useful-draft, material-change, and automatic-final-review triggers still apply.

Do not interrupt every ordinary question with the full view.

## Keep the first view compact

Show only three primary regions:

1. **Journey:** destination plus the complete ordered route as five to nine plain-language milestones, with exactly one `NOW`.
2. **Focus lens:** current outcome, exact next action, human role or `none`, objective proof, and recovery behavior.
3. **Quiet rail:** remaining issues and no more than six short plan-wide guardrails.

Lifecycle status and destination success remain visible metadata. A blocker is part of the current outcome or recovery behavior rather than a fourth competing region. Preserve every decision-changing fact from canonical state, including an unresolved recommendation, blocked scope, human gate, or losing reference when one exists; compress wording, never meaning.

The overview is a roadmap, not an architecture diagram. Never combine the product's operating loop, implementation architecture, support-system network, and build route in one graph. Pick the route that answers: “Where are we going, where are we now, and what happens next?” Keep the other views in linked detail.

When the surface supports interaction, selecting any non-current route step may reveal its outcome, owner, inputs, proof, and failure behavior. In plain Markdown, provide optional step detail in compact collapsed or linked sections below the first read. Link deeper detail to canonical files instead of copying it into the view. Destination, route, current focus, next action, human role, proof, recovery, and guardrails may never require a click, expansion, or file link.

Show lifecycle status as `planning`, `awaiting approval`, or `approved for build`. The completed visual is the approval surface; it must not imply that building is authorized before explicit approval.

## Give the route deliberate visual design

- Use a small semantic style system carried by literal labels, node shapes, and emphasis: `NOW`, numbered milestones, `HUMAN` where a person must act, `DONE` or `PROOF`, and `BLOCKED` or `INVALID` when necessary.
- Let the host's Mermaid theme supply light/dark-safe colors. Never hardcode a light-only or dark-only palette, and never let color alone carry meaning.
- Make the one current milestone and final destination the strongest nodes. Keep peer milestones visually consistent. Never show two milestones as `NOW`.
- Do not place supporting-system cards or a web of dashed links in the overview. They belong in the selected milestone's detail unless a single dependency line is essential to make the route truthful.
- Use the same class for peer steps rather than decorating every node differently. Do not add custom color, icons, legends, or containers that do not improve comprehension.
- Put the class definitions in `PLAN-VIEW.md` itself so styling remains zero-dependency and portable. If a harness ignores Mermaid styling, the labels, shapes, links, and compact text route plus focus lens must still carry the full meaning.
- Keep the design polished but restrained: styling may improve hierarchy and scanability, never add plan content or become a second source of truth.

## Display without dependencies

First detect the actual host boundary. A built-in interactive visualization is preferred only when that surface can read and display the generated source. Windows Codex Desktop backed by WSL cannot read file-backed inline HTML through the cross-environment bridge: do not emit such a reference or repeatedly rename, rewrite, relocate, or regenerate a valid source to work around `Invalid visualization read request`. Use rendered Mermaid or native expandable Markdown for an in-task view. When real interaction is required, show verified HTML through a browser/Site; a true inline interactive view requires a supported normal ChatGPT chat with `@Visualize` selected.

Use this fallback order without asking the user to install anything:

1. In Codex or another capable host, use its available built-in visualization capability to create an in-session Journey plus focus lens view with the same three primary regions and semantics. Follow that host capability's required writable path and display reference, verify the view actually appears, and require no separate renderer, app, runtime, or user download. If no such capability is available, continue immediately to the portable fallback.
2. Otherwise render the Mermaid block directly in the session when supported.
3. Otherwise use the harness's native Markdown artifact, attachment, or preview surface for `PLAN-VIEW.md`.
4. Otherwise open or show the local Markdown file using an available built-in file preview.
5. If no graphical surface exists, paste the compact text route, focus lens, and quiet rail from the same file in the session.

Never claim the visual was shown until it is visible. If a richer display errors, preserve any verified source, report the presentation failure separately from plan validity, immediately fall back in the same turn, and record the harness limitation. Do not move or regenerate valid plan content merely to repair a preview bridge. A terminal-only or text-only custom harness cannot produce a graphical popup; the text route is the guaranteed universal fallback.

A local-file link, attachment name, or statement such as “review the plan” is only navigation; it never proves display. At every automatic display trigger, the user-facing turn itself must contain either the visible rich view or the complete compact text route, focus lens, and quiet rail. At planning completion, show that view and ask one explicit approval question in the same turn while status remains `awaiting approval`.

Do not export or substitute a PNG, screenshot, or other raster image for the normal in-session plan view. Drew explicitly rejected that presentation. A raster export is allowed only when the user separately asks to save or share an image.

## Preserve one source of truth

Treat `PLAN-VIEW.md` only as a generated view. When it conflicts with canonical planning files, canonical state wins and the view must be regenerated.

Any host-native interactive surface is also generated from the same canonical state. It may improve presentation and interaction, but it cannot introduce or own plan decisions.

The Mermaid route and compact text route must contain the same milestones, state labels, and dependency order. Before every display or resume trigger, compare destination, lifecycle, current, next, milestone states, human authority, proof, and recovery with canonical files and regenerate the entire view when any changed.
