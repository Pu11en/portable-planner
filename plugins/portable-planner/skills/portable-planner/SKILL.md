---
name: portable-planner
description: Turn a vague idea into a cohesive, durable plan and ordered session-sized execution tickets using plain project-local Markdown. Use when a person naturally asks to plan an idea or project, continue or resume a plan, show the plan map, prepare the next planning session, settle planning decisions, or create execution tickets from a finished plan. Work across software, business, course, creative, event, operational, and personal projects without requiring project-management knowledge or command syntax.
---

# Portable Planner

Move from one vague idea to a complete route without making the user manage the planning process.

## Load the right guidance

- Read [conversation-contract.md](references/conversation-contract.md) before replying to a planning request.
- Read [question-engine.md](references/question-engine.md) before selecting or writing a planning question.
- Read [artifact-contract.md](references/artifact-contract.md) before creating or changing planning files.
- Read [visual-contract.md](references/visual-contract.md) before creating, refreshing, or displaying a plan view.
- Read [validation-rubric.md](references/validation-rubric.md) before completing a planning ticket or declaring planning finished.
- Copy the canonical structures from [PLAN.md](templates/PLAN.md),
  [NEXT.md](templates/NEXT.md), [PLAN-VIEW.md](templates/PLAN-VIEW.md),
  [planning-ticket.md](templates/planning-ticket.md), and
  [execution-ticket.md](templates/execution-ticket.md). Do not invent parallel
  state files.

## Start or resume

1. Treat natural requests such as “Plan this idea,” “Continue my plan,” “Show my full plan map,” and “Prepare the next session” as invocations. Do not require a slash command or skill name.
2. Resolve the project folder from the user's stated location or current working directory. Keep all state in `<project>/planning/`.
3. If `planning/PLAN.md` exists, read it, `planning/NEXT.md`, the current planning ticket, and only the linked decisions or evidence needed now. Trust files over chat memory.
4. If `NEXT.md` is missing or stale, regenerate it from `PLAN.md` and the one current unblocked ticket before continuing.
5. Treat every natural-language `continue` or `resume` invocation as a fresh-resume visual trigger. When a coherent route exists, refresh `PLAN-VIEW.md` and include its rendered graph or complete compact text route in that invocation's first user-facing reply, even when the same reply also asks the next question.
6. For a new idea, orient the user before asking: name what is being planned, state that this flow creates the plan rather than performing the final work, and identify the highest-leverage unresolved decision in plain language.
7. Default a new plan to one planning ticket containing the unresolved planning work. Do not pre-create one ticket per anticipated question.
8. Split into a multi-ticket map only after a concrete current-session limit appears: an independent research or prototype blocker, unresolved work too large to settle reliably now, or a dependency that cannot yet be resolved. Record the reason for escalation in `PLAN.md`.
9. Create the minimum canonical artifacts before relying on chat context. Never create planning files outside `planning/`.

## Route the current uncertainty

Choose the route yourself:

- **Synthesize** when the answer follows from confirmed context.
- **Research** factual uncertainty using primary or direct sources; save only decision-changing evidence.
- **Prototype** only when a cheap, disposable comparison is necessary to settle a decision. Do not perform production work.
- **Ask** only when multiple viable answers depend on human preference or direction.

Never ask the user to select an internal workflow, tool, architecture, research method, ticket order, or other technical/process choice the agent can derive. If research tools are unavailable, record the exact factual blocker and recovery step; do not ask the user to guess.

Maintain the prerequisite-aware candidate frontier in [question-engine.md](references/question-engine.md). Expose only its single most consequential ready human-owned decision. The recommendation is always the first option, `A`.

## Work one ticket

1. Select the earliest unblocked ticket automatically.
2. Show only the plan name, current step, next step, and at most one worthwhile question. Show a numeric fraction only when a reliable multi-ticket map actually exists; never invent a fixed question count.
3. After every confirmed answer, update the ticket and affected canonical artifacts before proceeding.
4. Refresh `PLAN-VIEW.md` whenever destination, success, route, ownership, current state, blocker, next action, dependency, or plan-wide safety changes.
5. Reconcile contradictions and downstream effects immediately. Add, remove, split, merge, or reorder tickets only when new understanding requires it.
6. Challenge unnecessary scope briefly and tie the challenge to the destination.
7. Honor an explicit request to use the agent's recommendations for a defined set of decisions: record the delegation and synthesize those choices without more questions. Stop only for an irreversible commitment, an uncovered material personal tradeoff, or a conflict.
8. If an unrelated idea appears, preserve the current plan and separate or switch it deliberately; never silently mix destinations.
9. Complete a ticket only when its decision and effects are explicit, evidence is linked when used, its completion check passes, no unresolved issue blocks the next ticket, and `NEXT.md` is exact.
10. Before replying after a write-through, compare the current unresolved decision in its ticket with `PLAN.md` current/next, `NEXT.md` work/session/completion lines, and `PLAN-VIEW.md` now/next. Repair every stale reference to the just-settled decision.
11. End the turn with the compact state and the one next action. Do not narrate routine file writes.

If the user says they are confused, stop the planning sequence. Explain what this session is doing, what it is not doing, and the current step in plain language. Do not ask another planning decision in that reply. Resume only after the user understands or redirects the work.

If a file, tool, display, research step, or handoff fails, preserve every confirmed decision, name the exact failure, give one recovery action, and use the next supported fallback when possible. Never fake success or restart the plan to hide a failure.

## Finish planning

1. Do not use a fixed question count. Attempt the finish audit in [validation-rubric.md](references/validation-rubric.md) when the destination, success, boundaries, major human decisions, route, gates, dependencies, risks, and recovery behavior appear defensible.
2. Resolve every major omission, contradiction, dependency, vague completion test, and oversized execution ticket. Infer low-impact implementation mechanics instead of extending grilling unnecessarily.
3. Generate dependency-ordered `execution/E-*` tickets covering the complete route. Size each for one fresh agent session.
4. Keep `PLAN.md` a short linked overview rather than duplicating ticket detail.
5. When the audit passes, set plan status to `awaiting approval` and automatically present the finished interactive visual plan without first asking whether the user wants to see it. The same turn asks one explicit approval question.
6. After approval, record `approved for build` in `PLAN.md`, regenerate the view and handoff, and point the harness to the first eligible execution ticket.
7. If the user requests a targeted change, return to `planning`, reopen only the affected human decision, reconcile downstream state, and refresh the view. If they want to keep planning, return to `planning` and select the highest-value unresolved human decision. If they are confused, pause questions and explain the state.
8. Do not execute the final plan or replace the harness's normal build workflow while using this skill.

## Prepare a handoff

Write `NEXT.md` as a paste-ready starter that includes the resolved absolute path to `planning/`, tells a fresh agent to load canonical files, names exactly one current planning ticket, supplies essential context only, states the required outcome, and includes its objective completion test. A fresh agent must be able to resume without prior chat or the original working directory.

## Show the map

When asked, when a useful draft would materially aid direction, or when an automatic trigger in [visual-contract.md](references/visual-contract.md) fires, show the route-first view generated from canonical state. In Codex, prefer the approved interactive presentation: destination/current/next cards, a clickable ordered route, one selected-step detail surface, compact support connections, and a short safety line. If that surface fails or is unavailable, immediately use Mermaid, Markdown preview, or the complete compact text route; never make the user install a renderer or troubleshoot the visual. A file link by itself does not count as showing the plan. At the approval gate, the same user-facing turn must contain the visible view or complete text route and ask one explicit approval question. Otherwise show only progress, current step, and next step. Never dump every linked artifact into the conversation.
