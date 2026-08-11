# Portable Planner — Revised Product Goal

## Goal

Deliver one portable planning plugin that a person can give to an AI agent as a single link, install through one natural-language request, and use in that same session to turn no idea, a thin idea, or a vague idea into:

1. a complete, durable plan;
2. short, decisive planning turns instead of walls of text, repeated questions, or intention-only pauses;
3. an automatically generated visual plan that makes a detailed project easy to comprehend;
4. exact fresh-session continuation; and
5. ordered execution tickets another agent can perform.

Drew must prefer the complete experience over his current planning workflow.

The plugin ends at an approved plan and build-ready handoff. The selected harness performs implementation through its normal build behavior; Portable Planner does not replace or redesign that behavior.

## Installation promise

The person gives their agent the plugin link or local package and says, in ordinary language, to install it. The agent:

1. detects the harness;
2. installs the unchanged canonical skill in the correct user-level location;
3. verifies the package and visual template;
4. loads the skill directly as a same-session fallback when the harness freezes skill discovery until restart;
5. runs a tiny planning smoke test; and
6. reports success or one precise recovery action.

The person installs no runtime, renderer, MCP server, database, web app, package manager, or separate visual tool. GitHub is one distribution option, not a required account or project workflow.

## Planning experience

- Start from one sentence, or from one real-world problem, audience, workflow, frustration, asset, or area of access when the person has no product idea yet.
- For a new software or AI idea that is still absent or thin, ask once whether the person wants a short possibility scan before ordinary planning. A decline immediately returns to ordinary planning and is not asked again.
- With permission, form a privacy-safe one-sentence search brief, inspect a small set of current public repositories without cloning or running them, and show only one provisional recommendation plus at most two materially different alternatives.
- Describe repository evidence precisely—what exists, is documented, appears usable or maintained, has documented adoption, and permits reuse—without calling an idea "proven." The person, not repository popularity, confirms the direction before it enters the plan.
- Orient the user before the first question.
- Ask at most one question per turn and only when multiple good answers depend on human preference.
- Record explicit delegation of reversible decisions and use the agent's recommendations within that scope without more preference questions.
- Stop verbal grilling when facts, prior answers, or delegation already settle the issue; use a bounded planning trial when behavior must be judged from concrete cases.
- Label every offered answer `A/B/C`, adding `D` only when a genuinely distinct fourth choice is needed, so a one-character reply works.
- Derive mechanics and research facts without transferring them to the user.
- Keep ordinary replies to a few short lines, normally around 40 words and under 80 unless requested evidence or a required approval view needs more.
- Perform the next safe planning action in the same turn instead of stopping after saying what will happen next.
- Preserve confirmed decisions before continuing.
- Finish a simple route in one session; expand only when demonstrated uncertainty requires it.
- After three consecutive recommended reversible choices, offer one explicit delegation shortcut when more reversible choices remain; never infer that authority from repeated agreement.
- After a digression, preserve the one-letter path by ending with the refreshed complete choice set whenever a worthwhile human decision remains.
- Keep research-derived changes to the product provisional until the person confirms them, and make live-test handoffs reuse known context rather than reopening intake.
- At a real session boundary, start the one authorized successor or give a clearly labeled exact prompt the person can paste; never leave them with only a vague next-step announcement.
- When a direct approval question receives `yes`, treat it as explicit authorization: update state and immediately enter the harness's normal build workflow when safe. After agent checks pass, proactively present the smallest genuine user test.

The idea-stage scan is a public-preview behavior until its scenario checks and Drew's natural fresh-session use pass the acceptance checklist. It adds no required GitHub account, API client, MCP server, database, cloud service, or build mode.

## Visual experience

When the plan is coherent enough to show, automatically create or refresh one visual plan from the canonical local state.

The first view must show:

- final destination and proof of success;
- current status, blocker, and next action;
- the complete ordered route and dependencies;
- human decisions versus agent/automatic work; and
- the few rules that protect the whole plan.

Use a route-first graph as the default hierarchy. Keep the destination, current state, and next action prominent; show the ordered route as the main spine; and make supporting-system connections available in the same visual without allowing them to overwhelm the route.

Selecting a route step reveals its outcome, owner, inputs, proof, and failure or change behavior. Detail stays available without forcing it into the overview. The visual is a view of the durable plan, never a second competing source of truth.

The plugin carries its own zero-dependency visual template. Every harness generates the same project-local `planning/PLAN-VIEW.md` with a Mermaid graph plus a compact text route. The visual is always available on request, may be offered once as a useful draft, and opens automatically for final review only when the complete route passes the finish audit. It refreshes after a misleading planning or execution-state change, before human testing, and after a fresh resume when a coherent route exists. A genuinely supported rich host may use the approved interactive presentation; Windows Codex Desktop tasks running through WSL use rendered Mermaid or native expandable Markdown rather than unsupported file-backed inline HTML. Browser/Site and normal ChatGPT `@Visualize` remain interactive routes when available. No separate visual download is required.

A text-only custom harness cannot create a graphical popup, but it must still show the complete compact route in the same session. The agent must never claim a visual was displayed when the display surface errored.

## Effectiveness gates

The plugin passes only when:

- installation and natural-language use work in the same session;
- Drew understands the session, current step, and next step without explanation;
- every question is worth answering;
- explicit delegated choices advance without ceremony, and exhausted discussion becomes concrete evidence rather than more questions;
- direct approval begins the normal build without a second permission request, and validated work clearly tells Drew what to test;
- simple and complex plans are complete without feeling slow;
- a complex project such as Hanoi Picks is easy to understand visually without losing important detail;
- the visual and detailed local artifacts stay synchronized after changes;
- a fresh session and a second harness resume unchanged project state;
- execution tickets are immediately actionable; and
- Drew says he would actually use the first ordinary real-plan experience and a naturally complex planning experience.

## Confirmed visual direction

Use the earlier interactive Hanoi-style presentation: destination/current/next summary cards, a clickable ordered route, one selected-step detail surface, compact supporting-system connections, and a short safety line. Continue refining labels and density from real use without reopening the hierarchy unless comprehension testing fails.
