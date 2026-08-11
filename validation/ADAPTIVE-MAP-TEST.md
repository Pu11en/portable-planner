# Adaptive Planning Map Forward Test

**Date:** 2026-08-05  
**Initial and blocker session:** `019fd40b-fe72-7c20-8978-5eb7a80197ec`  
**Fresh evidence-resume session:** `019fd412-b143-71f0-9b46-c0fccc939e48`  
**Raw fixture:** [`adaptive-map/`](adaptive-map/)

## Purpose

Test R-02 as state transitions rather than static instructions:

1. begin a new idea with one planning ticket;
2. split only after a demonstrated current-session blocker;
3. resume from files in a fresh context;
4. incorporate direct evidence that changes the route; and
5. remove, add, merge, or reorder work instead of preserving a stale map.

## State 1 — Minimum start

The fresh opening created exactly three canonical files: `PLAN.md`, `NEXT.md`, and `decisions/P-001-define-event-route.md`. Its map contained only:

- `▶ P-001 — Define the executable event route`

No `PLAN-VIEW.md`, evidence file, execution ticket, or speculative second planning ticket was created. The user-facing turn asked the one consequential fallback preference and stopped.

## State 2 — Demonstrated blocker expands the map

Drew's simulated `A` choice saved the full indoor-fallback preference. `BLOCKER.md` then supplied a direct venue-manager response requiring an independent four-part site assessment before park approval or equipment selection. That assessment was too large to settle reliably in the current turn.

The planner changed the map to:

- `✓ P-001 — Confirm the fallback policy`
- `▶ P-002 — Assess Riverside Park feasibility` — depends on P-001

It recorded the split reason in `PLAN.md`, generated the first coherent `PLAN-VIEW.md`, saved direct evidence, and made P-002 the one unblocked next planning step. The captured route and expected mutation are preserved in [`adaptive-map/BEFORE-MUTATION.md`](adaptive-map/BEFORE-MUTATION.md).

## State 3 — New evidence collapses and reorders the route

A new Codex context loaded only the canonical files, unchanged skill, and `NEW-EVIDENCE.md`. The direct result denied the park and offered a free indoor community center with built-in AV, capacity 100, accessible facilities, a marked aisle, and two required clear exits.

The reconciled state:

- completed P-002 with the direct denial and activated the already-saved indoor preference without another question;
- removed the park-decision branch from the visual route;
- removed generator rental, outdoor screen/anchoring, sound-spill mitigation, rain monitoring, and outdoor weather fallback from future work;
- retained those terms only in historical evidence, explicit exclusions, and the rule forbidding their silent reintroduction;
- added six indoor execution tickets;
- ordered venue confirmation before movie licensing and budget;
- ordered the room/show runbook before communication;
- added a human readiness gate before event operation;
- regenerated `PLAN.md`, `PLAN-VIEW.md`, and `NEXT.md` at `awaiting approval`; and
- stopped without authorizing or performing execution.

Final execution route:

`Visual approval → confirm community center → license movie and lock budget → build indoor room/show runbook → release communication → human readiness gate → operate and measure → prove attendance, retention, safety, compliance, cleanup, and spend`

## Independent audit

The root-agent audit verifies:

- exactly one initial P ticket;
- an explicit demonstrated split reason;
- no stale current/next wording from the park-assessment frontier;
- no active outdoor work in the execution route;
- `awaiting approval` agreement across plan, view, and handoff;
- zero current planning tickets after finish;
- every E ticket has scope, exclusions, constraints, proof, recovery, human review, and next eligibility;
- zero broken relative Markdown links;
- no unresolved placeholders or `Not confirmed` markers;
- one first eligible execution ticket and dependency-consistent ordering; and
- plugin and skill package validators still pass.

## Result

**PASS for R-02.** The same core skill starts minimally, expands only for demonstrated uncertainty, resumes durably, and materially removes/adds/reorders route work when new evidence changes the plan. No new architecture or domain pack was needed.
