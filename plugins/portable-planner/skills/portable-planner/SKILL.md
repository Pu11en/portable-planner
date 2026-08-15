---
name: portable-planner
description: Turn no idea, a thin idea, or a vague idea into a cohesive, durable plan and ordered session-sized execution tickets using plain project-local Markdown. Use when a person naturally asks to explore or plan an idea or project, continue or resume a plan, show the plan map, prepare or automatically create the next planning task, settle planning decisions, create execution tickets, or move an explicitly approved plan into the harness's normal build and live-test flow. Work across software, business, course, creative, event, operational, and personal projects without requiring project-management knowledge or command syntax.
---

# Portable Planner

Move from no idea, a thin idea, or a vague idea to a complete route without making the user manage the planning process.

## Load the right guidance

- Read [conversation-contract.md](references/conversation-contract.md) before replying to a planning request.
- Read [question-engine.md](references/question-engine.md) before selecting or writing a planning question.
- Read [idea-discovery.md](references/idea-discovery.md) before the first reply when a new software or AI project may have no product idea or only a thin one. Do not load or apply it to resumed plans, existing-project changes, detailed specifications, direct build requests, or ordinary research later in a plan.
- Read [artifact-contract.md](references/artifact-contract.md) before creating or changing planning files.
- Read [session-chaining.md](references/session-chaining.md) when a plan may cross tasks, the user asks about task/session behavior, or a fresh-task boundary is near.
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
6. For a new idea, orient the user before asking: name what is being planned, state that this flow creates the plan rather than performing the final work, and identify the highest-leverage unresolved decision in plain language. For an eligible no-idea or thin-idea software/AI start, that first decision is the one-time scan permission gate in [idea-discovery.md](references/idea-discovery.md); explicit requests to research or scan repositories already supply consent.
7. Default a new plan to one planning ticket containing the unresolved planning work. Do not pre-create one ticket per anticipated question.
8. Split into a multi-ticket map only after a concrete current-session limit appears: an independent research or prototype blocker, unresolved work too large to settle reliably now, or a dependency that cannot yet be resolved. Record the reason for escalation in `PLAN.md`.
9. Create the minimum canonical artifacts before relying on chat context. Never create planning files outside `planning/`.
10. If the user explicitly authorizes automatic continuation across tasks, record that permission in `PLAN.md`. Do not treat a natural planning request alone as task-creation permission.

## Route the current uncertainty

Choose the route yourself:

- **Synthesize** when the answer follows from confirmed context.
- **Research** factual uncertainty using primary or direct sources; save only decision-changing evidence.
- **Prototype** only when a cheap, disposable comparison is necessary to settle a decision. Do not perform production work.
- **Ask** only when multiple viable answers depend on human preference or direction.

Before acting, classify the live uncertainty:

- **Fact:** research it.
- **Settled or delegated reversible decision:** synthesize and continue.
- **Human-reserved decision:** ask one question.
- **Grillable uncertainty:** discuss only while another answer can materially change the plan.
- **Trial-needed uncertainty:** run one bounded planning trial when concrete behavior, feel, or interaction is the only useful evidence.

Do not ask because uncertainty still exists in the abstract. Stop verbal grilling when facts, prior words, explicit delegation, or diminishing decision value have reduced it as far as discussion can. A trial normally compares an ordinary case, a materially contrasting case, and a failure or prohibited-action case. It produces planning evidence, never production implementation.

Never ask the user to select an internal workflow, tool, architecture, research method, ticket order, or other technical/process choice the agent can derive. If research tools are unavailable, record the exact factual blocker and recovery step; do not ask the user to guess.

The idea-stage scan is a special, consented form of the Research route. It expands the person's understanding of plausible directions before the plan adopts one; it does not choose the product, perform broad market research, clone or execute discovered code, or change ordinary research behavior. Follow its eligibility, privacy, search, inspection, evidence, output, state, and fallback limits exactly.

Research and reused project evidence may reveal a better direction, but they cannot silently redefine the destination, intended output, or role of an important source asset. Treat such a change as a provisional recommendation and put the grounded product choice back in the human-owned frontier before optimizing downstream work around it.

Maintain the prerequisite-aware candidate frontier in [question-engine.md](references/question-engine.md). Expose only its single most consequential ready human-owned decision. The recommendation is always the first option, `A`.

## Work one ticket

1. Select the earliest unblocked ticket automatically.
2. Show only the plan name, current step, next step, and at most one worthwhile question. Show a numeric fraction only when a reliable multi-ticket map actually exists; never invent a fixed question count.
3. After every confirmed answer, update the ticket and affected canonical artifacts before proceeding.
4. Refresh `PLAN-VIEW.md` whenever destination, success, route, ownership, current state, blocker, next action, dependency, or plan-wide safety changes.
5. Reconcile contradictions and downstream effects immediately. Add, remove, split, merge, or reorder tickets only when new understanding requires it.
6. Challenge unnecessary scope briefly and tie the challenge to the destination.
7. Honor an explicit request to use the agent's recommendations for a defined set of reversible decisions: record the user's exact words and scope, then synthesize those choices without more questions. The delegation lasts for that plan until exhausted, revoked, contradicted, or blocked by an irreversible commitment, uncovered material personal tradeoff, conflict, implementation authorization, or final-plan approval. Repeated agreement alone never creates delegation.
8. Track a consecutive recommended-key streak using only replies whose trimmed complete content is exactly the recommended option letter, case-insensitively. Any punctuation, explanation, second character, non-recommended key, digression, redirect, or protected gate resets the streak to zero. After the third qualifying reply, if another reversible human-owned question exists, keep its ordinary recommended route as `A.` and insert `B. Use my recommendations for every remaining reversible decision`; relabel its other viable routes from `C.` through at most `G.`. The pattern only exposes option `B`; choosing `B` alone grants delegation.
9. If the user digresses, asks a side question, or supplies a long mixed message, answer or reconcile it first, reset the streak, recompute the frontier, and—if one human-owned decision remains—put the complete refreshed `A.` through at most `G.` choice set at the bottom of the same reply. Never repeat a stale choice set merely to preserve the one-letter path.
10. If an unrelated idea appears, preserve the current plan and separate or switch it deliberately; never silently mix destinations.
11. Complete a ticket only when its decision and effects are explicit, evidence is linked when used, its completion check passes, no unresolved issue blocks the next ticket, and `NEXT.md` is exact.
12. Before replying after a write-through, compare the current unresolved decision in its ticket with `PLAN.md` current/next, `NEXT.md` work/session/completion lines, and `PLAN-VIEW.md` now/next. Repair every stale reference to the just-settled decision.
13. Keep ordinary replies to a few short lines: current result, next action, and at most one worthwhile question. Do not recap settled context unless it changed. Evidence or a required final review may be longer, but summarize first.
14. When the next safe planning action is clear, perform it in the same turn. Never end after merely announcing research, synthesis, a trial, a file update, approval processing, or another safe action that can be completed now.
15. When the current ticket can still be completed reliably, stay in this task. At a demonstrated context boundary, follow [session-chaining.md](references/session-chaining.md): save first, then create at most one authorized successor or visibly label and provide the exact compact next-session prompt. Never stop at a vague handoff announcement.

If the user says they are confused, stop the planning sequence. Explain what this session is doing, what it is not doing, and the current step in plain language. Do not ask another planning decision in that reply. Resume only after the user understands or redirects the work.

If a file, tool, display, research step, or handoff fails, preserve every confirmed decision, name the exact failure, give one recovery action, and use the next supported fallback when possible. Never fake success or restart the plan to hide a failure.

## Finish planning

1. Do not use a fixed question count. Attempt the finish audit in [validation-rubric.md](references/validation-rubric.md) when the destination, success, boundaries, major human decisions, route, gates, dependencies, risks, and recovery behavior appear defensible.
2. Resolve every major omission, contradiction, dependency, vague completion test, and oversized execution ticket. Infer low-impact implementation mechanics instead of extending grilling unnecessarily.
3. Generate dependency-ordered `execution/E-*` tickets covering the complete route. Size each for one fresh agent session.
4. Keep `PLAN.md` a short linked overview rather than duplicating ticket detail.
5. When the audit passes, set plan status to `awaiting approval` and automatically present the finished interactive visual plan without first asking whether the user wants to see it. The same turn asks one explicit approval question.
6. After a direct approval question, treat an immediate `yes`, `approved`, or the displayed approval choice as explicit approval. Record `approved for build`, regenerate the view and handoff, and point the harness to the first eligible execution ticket.
7. If the user requests a targeted change, return to `planning`, reopen only the affected human decision, reconcile downstream state, and refresh the view. If they want to keep planning, return to `planning` and select the highest-value unresolved human decision. If they are confused, pause questions and explain the state.
8. Portable Planner does not implement the final project itself or replace the harness's build system. However, approval is not a reason to stop the agent: after planning state is synchronized, immediately leave planning behavior and begin the first eligible ticket through the harness's normal build workflow when it is safe and fits the current task. Do not ask for a second "build it" confirmation. Stop only for an explicit planning-only request, a real task boundary, a protected decision, or an operational blocker.

## Move finished work into testing

1. Agent-run checks come before human testing. Complete the ticket's objective proof and record failures before expanding architecture.
2. Before presenting a test, reconcile `PLAN.md`, the active ticket, `PLAN-VIEW.md`, and `NEXT.md` so completed work is not shown as current. Reuse confirmed product, brand, source, and acceptance context rather than asking the person to restate it.
3. When the candidate is genuinely ready for human judgment, proactively present the smallest real test that can confirm or disprove the changed behavior. Do not leave the person to guess whether the work is ready or what to try.
4. Keep the invitation short: state what is ready, give one natural test action, and say what judgment is needed. Apply safe reversible defaults and ask at most one question, only when its answer truly blocks the test action.
5. Synthetic trials and authored examples are planning or implementation evidence, not live acceptance. Record the person's actual result separately.

## Prepare a handoff

Write compact `NEXT.md` with the resolved absolute path to `planning/`, lifecycle state, exactly one current action, the minimum files to read, the required outcome, and its objective completion test. A fresh agent must resume without prior chat or the original working directory. When an authorized real boundary exists, use [session-chaining.md](references/session-chaining.md) to create one successor with only the short pointer to this file.

## Show the map

When asked, when a useful draft would materially aid direction, or when an automatic trigger in [visual-contract.md](references/visual-contract.md) fires, refresh and show the route-first view generated from canonical state. Prefer the approved interactive presentation only on a host that actually supports it. In Windows Codex Desktop backed by WSL, do not emit a file-backed inline HTML visualization: use rendered Mermaid or native expandable Markdown, or show interactive HTML through a browser/Site. If a richer surface fails or is unavailable, preserve any verified source, report the presentation failure separately, and immediately show Mermaid, Markdown, or the complete compact text route; never regenerate valid plan content merely to work around the display or make the user troubleshoot it. A file link by itself does not count as showing the plan. At the approval gate, the same user-facing turn must contain the visible view or complete text route and ask one explicit approval question. Otherwise show only progress, current step, and next step. Never dump every linked artifact into the conversation.
