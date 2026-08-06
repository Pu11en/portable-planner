# Portable Planner — Confirmed Product Contract

**Status:** Confirmed direction for the experiment. Change this only when Drew makes a new product decision or a live validation failure proves that a rule must change.

## Product boundary

Portable Planner is a planning plugin, not a replacement build system. It takes a vague idea to an approved, durable plan and session-sized execution tickets. Once planning is approved, the current harness builds from those artifacts using its normal implementation behavior. The planner may be invoked again to review a result, repair the plan, or prepare the next planning handoff, but it does not redefine how Codex, Claude Code, or another harness executes work.

## Conversation

- Work on one planning decision at a time.
- Keep ordinary replies short and make the current step obvious.
- Ask only decisions that require human judgment about the desired inputs, outputs, experience, boundaries, priorities, or proof of success.
- Discover facts from the project and research external uncertainty instead of asking the person to guess.
- Infer internal workflow, architecture, tools, and implementation mechanics unless they materially change the person's result.
- When choices help, use stable `A/B/C` labels; add `D` only for a genuinely distinct fourth route.
- Every listed route must be viable. Always put the agent's recommended route first as `A` and state its main tradeoff.
- Accept a custom answer and preserve every confirmed answer before continuing.
- When the user explicitly delegates a defined set of choices to the agent's recommendations, record that delegation and stop asking within its scope. Still pause for irreversible commitments, uncovered material personal tradeoffs, or conflicts.
- Ask no question merely because a template contains a field.

## Planning logic

- Begin from natural language; no command name is required.
- Start with the smallest reliable planning path and expand only when uncertainty, dependencies, research, or project size demonstrates the need.
- Use research or a cheap decision prototype when evidence is needed; do not turn planning into production work.
- Maintain one cohesive route to the complete intended result, not a diagram of the planner's own internal phases.
- Store the canonical plan, decisions, evidence, continuation state, and execution tickets as plain project-local files.
- Produce tickets that a fresh harness session can execute and objectively verify without reopening major planning decisions.
- Preserve the current plan when an unrelated idea appears; deliberately switch or separate it rather than silently mixing destinations.
- Use no fixed question count. Attempt final review when the complete route is defensible: destination, observable success, boundaries, major human decisions, order, dependencies, gates, risks, recovery, tickets, and canonical artifacts are coherent.
- Show the finished visual plan automatically as an explicit approval gate. Do not hand anything to the harness's normal build workflow until the person clearly approves it.

## Visual plan

- Keep the visual available at any time through natural language. The agent may offer a useful draft once during grilling, and it automatically opens final review when the finish audit passes. A draft does not imply completion.
- Redisplay after a major change when the prior view would mislead and in the first reply after a fresh resume when a coherent route exists.
- Use one dominant route-first hierarchy: destination/current/next first, then five to nine plain-language outcome milestones and plan-wide rules.
- Keep the overview in one reading direction. Add a branch only when a linear route would make the actual plan false.
- Present the route with deliberate semantic design: an emphasized `NOW`, consistent numbered milestones, an emphasized `DONE` or `PROOF`, and a literal `BLOCKED` state when needed. Use the host's theme rather than a fixed light/dark palette.
- Keep architecture, support systems, owners, inputs, proof detail, and failure behavior in the selected milestone's details rather than mixing multiple diagrams into the overview.
- Keep the overview easy to scan while allowing a selected step to reveal outcome, owner, inputs, proof, and failure/change behavior.
- Generate the view from canonical project state; it is never a second source of truth.
- In Codex, prefer the approved interactive presentation: destination/current/next summary cards, a clickable ordered route, one selected-step detail surface, compact support connections, and a short safety line. Do not replace it with a PNG or screenshot. Retain Mermaid/Markdown/text fallbacks for other harnesses and require no renderer or separate user download.
- Never claim the visual displayed when the surface failed.

## Review outcomes

- Explicit approval changes lifecycle status to `approved for build` and points to the first eligible execution ticket.
- A targeted change returns to `planning`, reopens only the affected human decision, reconciles downstream state, and refreshes the visual.
- “Keep planning” returns to `planning` and continues with one highest-value human decision at a time.
- Confusion pauses questions and triggers a plain-language explanation of the current state.

## Failure behavior

- State the exact file, tool, display, research, or handoff failure honestly.
- Preserve confirmed decisions and the last trustworthy state.
- Give one precise recovery action and continue through the next supported fallback when possible.
- Never fake success, discard the plan, or force a restart to conceal a failure.

## Portability

- One canonical Agent Skill contains the planning behavior, references, and Markdown templates.
- Harness adapters may only install, discover, or invoke that same skill.
- Natural-language installation from a local package, archive, or public repository link must work in the same session when the harness permits it.
- Codex is the first rich-display target. The unchanged planning brain and project state must also work in at least one non-Codex harness before MVP acceptance.

## Evidence policy

The interaction logic combines expert-supported mechanics rather than copying one system wholesale: decision-tree interviewing, facts-versus-decisions separation, explicit plan/build handoff, adaptive decision maps, primary-source research, durable local artifacts, and session-sized execution tickets. Drew's one-question rhythm, low reading load, stable lettered answers, and route-first visual are intentional product requirements even when an expert source uses a different interaction pattern.

## Acceptance boundary

This remains an experiment until the objective checklist passes and Drew confirms that both the simple and complex live planning flows are experiences he would actually use.
