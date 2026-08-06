# Artifact Contract

Canonical state lives in the user's project:

```text
planning/
├── PLAN.md
├── PLAN-VIEW.md
├── NEXT.md
├── decisions/
│   └── P-001-short-title.md
├── evidence/
│   └── P-001-evidence.md
└── execution/
    └── E-001-short-title.md
```

Create only directories that are needed, but always use these paths and stable IDs. Use relative links so the folder remains portable.

`PLAN.md`, planning tickets, evidence, and execution tickets are canonical. `PLAN-VIEW.md` and any host-native interactive presentation are generated views of that state and must never contain a decision that is absent from canonical files.

`PLAN.md` has one lifecycle status: `planning`, `awaiting approval`, or `approved for build`. It also records continuation mode as `manual` or `automatic — authorized`, the reason for the latest task boundary, and the last successfully created successor task when one exists. Only the user's explicit approval of the finished visual plan may create `approved for build`. The plugin never performs the execution work.

## `PLAN-VIEW.md`

Generate it from canonical state using `templates/PLAN-VIEW.md` and [visual-contract.md](visual-contract.md). Keep a short text route beside the Mermaid source so the plan remains understandable when a harness cannot render diagrams. Regenerate the view after any change to destination, success, route, status, ownership, dependencies, blocker, next action, or plan-wide safety.

Displaying a requested or useful draft does not change lifecycle status from `planning`. Change to `awaiting approval` only after the finish audit passes and the finished review is ready to display automatically.

## `PLAN.md`

Keep it short. Include only lifecycle status, destination, objective success, boundaries, compact ordered map with status and dependencies, one-line confirmed decisions linked to their tickets, linked execution tickets, approval, and current/next action.

Use these status marks consistently:

- `✓` complete
- `▶` current and unblocked
- `○` pending
- `!` blocked, with the blocker named

Exactly one planning ticket may be current. Dependencies determine readiness; list order breaks ties.

Start a new plan with one planning ticket. Add or split tickets only when a demonstrated research, prototype, size, or dependency limit prevents reliable completion in the current session. Do not create placeholder tickets for decisions that may never be needed.

## Planning tickets

Use `P-NNN-short-title.md`. Record the decision and why it matters, status, dependencies, viable options and tradeoffs when applicable, recommendation, confirmed decision, evidence links, effects on the map, and an objective completion check.

A confirmed decision has one authoritative planning ticket. Summaries elsewhere link back to it.

## Evidence

Create `evidence/P-NNN-evidence.md` only when external facts affect a decision. Use primary sources or direct providers for every decision-changing claim. Record source, access date, relevant finding, and which choice it changes. If no primary/direct source can answer the narrow fact, label secondary evidence provisional, corroborate it independently, and put a direct recheck before any irreversible commitment in the relevant execution ticket. An uncorroborated secondary claim cannot settle a decision or pass the finish audit. Stop when additional sources are unlikely to change the decision.

## `NEXT.md`

During planning, name exactly one current unblocked planning ticket. Include the resolved absolute path to the `planning/` folder, lifecycle state, the minimum files to load, the required session outcome, and the ticket completion test. Do not rely on chat history or the original working directory. Keep it compact: it is an index into canonical state, not a second plan or a conversation transcript.

When status is `awaiting approval`, name the visual review as the one next action. When status is `approved for build`, name exactly one first eligible execution ticket and tell the harness to use its normal build workflow. Never authorize build while major planning work remains.

Regenerate a missing or stale `NEXT.md` from `PLAN.md` and the current ticket. The plan must remain complete without `NEXT.md`.

When an authorized successor is created, record its returned identifier and boundary reason in `PLAN.md`. Do not retry after success. If creation is unavailable or fails, leave `NEXT.md` valid and expose its exact short pointer as the recovery action.

## Execution tickets

Use `E-NNN-short-title.md`. Give one session-sized observable outcome, linked decisions and context, dependencies, exact in-scope work, explicit exclusions, constraints that must remain true, objective proof, failure or return-to-planning conditions, required human review, and the next eligible ticket.

Split a ticket when a fresh agent could not complete and verify it in one session. Execution tickets may depend on earlier execution tickets but must not hide unresolved planning decisions.

## Update order

After a confirmed decision:

1. update its planning ticket;
2. update linked evidence if used;
3. reconcile affected tickets and dependencies;
4. update the short summary and map in `PLAN.md`;
5. regenerate `PLAN-VIEW.md`;
6. regenerate `NEXT.md`;
7. compare the current ticket's unresolved decision with `PLAN.md` current/next, `PLAN-VIEW.md` now/next, and the work/session/completion lines in `NEXT.md`; update any line that still describes the decision just settled.
