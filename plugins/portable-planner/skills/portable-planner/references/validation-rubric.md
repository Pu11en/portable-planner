# Validation Rubric

## Complete a planning ticket only if all pass

- The confirmed decision is explicit and durable.
- Decision-changing evidence is linked.
- Contradictions and downstream effects are reconciled.
- Dependencies and status match the canonical map.
- The objective completion check is satisfied.
- No unresolved issue blocks the next ticket.
- `NEXT.md` names exactly one current unblocked ticket and its completion test.

If no planning ticket remains, replace the last check with the finish audit and make `NEXT.md` state that planning is ready for human review rather than inventing more planning work.

## Finish audit

Planning is finished only if all pass:

- Destination and success are unambiguous.
- Boundaries and exclusions are explicit.
- No major choice, contradiction, or factual blocker remains.
- Every explicit delegation has a recorded scope, and no protected decision was absorbed into it.
- Every decision-changing factual claim uses a primary source or direct provider; any unavoidable secondary fallback is explicitly provisional, independently corroborated, and has a direct recheck before irreversible commitment.
- The map, decision tickets, evidence, and execution tickets agree.
- Remaining work is execution rather than planning.
- Dependency-ordered execution tickets cover the complete route.
- Every execution ticket has one outcome, exact scope and exclusions, dependencies, objective proof, human review, and next eligibility.
- Every execution ticket fits one fresh agent session.
- `PLAN.md` remains a short linked overview.
- A fresh agent can understand what to do from local files alone.
- Plan lifecycle status is `awaiting approval`; it cannot become `approved for build` before the finished visual is explicitly approved.
- The completion turn visibly contains the graph or complete compact text route and one explicit approval question; a file link alone is a failure.

Run this audit adaptively rather than after a fixed number of questions. A requested draft or useful-draft offer does not imply that it passes. The automatic final review gate is ready only when the complete route can be defended without reopening a major human-owned decision; minor mechanics the agent can safely infer are not blockers.

If any check fails, keep planning open and resolve the demonstrated gap. Do not add new storage, services, roles, commands, or domain packs unless a concrete validation failure cannot be fixed within the existing skill, references, and templates.

After explicit approval, verify that `PLAN.md`, `PLAN-VIEW.md`, and `NEXT.md` all say `approved for build` and name the same first eligible execution ticket. Then immediately enter the harness's normal build workflow when safe; do not end on a handoff announcement or ask for permission again.

## Decisive-flow audit

Before claiming this behavior passes, use materially different software and non-software cases to verify:

- ordinary replies are a few short lines and avoid settled-context recap;
- explicit reversible delegation synthesizes decisions, while repeated agreement does not create authority;
- after three consecutive recommended reversible selections with at least two such decisions remaining, one explicit delegation-or-continue invitation appears without inferring authority;
- every choice uses literal `A.`, `B.`, `C.`, or `D.` prefixes, and a digression restores the recomputed current choice set at the bottom when a human decision remains;
- facts and settled choices are not re-asked;
- research-derived changes to destination, output, or the role of a value-bearing source remain provisional until human confirmation;
- dynamic uncertainty becomes one preserved ordinary/contrasting/failure trial;
- a failed case causes a targeted revision and affected rerun before architecture expands;
- the next safe action happens in the same turn rather than being merely announced;
- `yes` to the direct final approval question updates state and begins normal harness execution without another authorization step;
- irreversible commitments, uncovered personal tradeoffs, conflicts, implementation authorization, and final approval remain protected; and
- after agent-run checks, the smallest genuine user test is presented proactively from refreshed state, reuses known context, and asks at most one truly blocking input question; and
- a rich-presentation failure preserves the verified source, is reported separately from plan validity, and falls back to a supported readable view in the same turn.

Synthetic scenarios prove instruction behavior only. They never replace the person's live acceptance judgment.

After a targeted revision request, return to `planning`, reopen only the affected human decision, reconcile every downstream artifact, and refresh the view. After “keep planning,” return to `planning` and select the highest-value unresolved human decision. After confusion, pause the sequence and explain current state before asking anything else.

## Before a handoff

Simulate a context reset: ignore chat memory, follow `NEXT.md`, load the named files, and verify that the current outcome and completion test are unambiguous. Compare the current ticket's unresolved decision with `PLAN.md` current/next, `PLAN-VIEW.md` now/next, and `NEXT.md` work/session/completion lines. They must name the same frontier, and none may describe the decision just settled. Fix the artifacts if the simulation requires guessing.

## Before automatic task continuation

All must pass:

- `PLAN.md` records explicit plan-scoped authorization for automatic continuation.
- A concrete boundary from `session-chaining.md` exists; a small reliable plan remains in the current task.
- Canonical state and compact `NEXT.md` are saved before task creation.
- `NEXT.md` names exactly one action and only the files required for it.
- The successor prompt is only `Use $portable-planner. Follow /absolute/path/to/planning/NEXT.md.`
- Exactly one successor is requested, its returned identifier is recorded after success, and creation is not retried after success or an uncertain result.
- The successor can continue from local files unchanged and does not require GitHub, a worktree, a service, or chat history.
- If native creation is unsupported or fails, the same short prompt is shown as the single recovery action.
