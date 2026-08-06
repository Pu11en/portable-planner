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
- The map, decision tickets, evidence, and execution tickets agree.
- Remaining work is execution rather than planning.
- Dependency-ordered execution tickets cover the complete route.
- Every execution ticket has one outcome, exact scope and exclusions, dependencies, objective proof, human review, and next eligibility.
- Every execution ticket fits one fresh agent session.
- `PLAN.md` remains a short linked overview.
- A fresh agent can understand what to do from local files alone.
- Plan lifecycle status is `awaiting approval`; it cannot become `approved for build` before the finished visual is explicitly approved.
- The completion turn visibly contains the graph or complete compact text route and one explicit approval question; a file link alone is a failure.

If any check fails, keep planning open and resolve the demonstrated gap. Do not add new storage, services, roles, commands, or domain packs unless a concrete validation failure cannot be fixed within the existing skill, references, and templates.

After explicit approval, verify that `PLAN.md`, `PLAN-VIEW.md`, and `NEXT.md` all say `approved for build`, name the same first eligible execution ticket, and leave implementation to the harness's normal build workflow.

## Before a handoff

Simulate a context reset: ignore chat memory, follow `NEXT.md`, load the named files, and verify that the current outcome and completion test are unambiguous. Compare the current ticket's unresolved decision with `PLAN.md` current/next, `PLAN-VIEW.md` now/next, and `NEXT.md` work/session/completion lines. They must name the same frontier, and none may describe the decision just settled. Fix the artifacts if the simulation requires guessing.
