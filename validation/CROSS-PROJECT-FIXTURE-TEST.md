# Cross-Project Fixture Test

**Date:** 2026-08-05  
**Result:** PASS for T-03  
**Evidence class:** Synthetic adversarial validation, not Drew's human live-pilot acceptance.

## Method

Four isolated fresh Codex contexts directly loaded the same canonical Portable Planner skill. Each context could read only its own vague `IDEA.md`, confirmed synthetic preference profile, and the canonical skill/references/templates. It could not inspect sibling fixtures or prior validation reports.

Each run had to complete planning, record any simulated one-question turns, create canonical project-local state, generate a complete visual, produce dependency-ordered session-sized execution tickets, run the finish and reset audits, stop before execution, and write an honest `TEST-RESULT.md`. No domain pack was supplied.

An independent audit then checked required files, lifecycle agreement, unresolved markers, visual and text routes, all execution-ticket contract headings, local links, question counts, source quality, plugin/skill validity, and whitespace errors. Agent self-ratings did not count by themselves.

## Results

| Type | Planning questions | Execution tickets | Result | Evidence |
|---|---:|---:|---|---|
| Software — local interview evidence library | 1 | 7 | PASS after the finish audit split an oversized final ticket | [Result](cross-project-fixtures/software/planning/TEST-RESULT.md) · [Plan](cross-project-fixtures/software/planning/PLAN.md) · [Visual](cross-project-fixtures/software/planning/PLAN-VIEW.md) |
| Creative/content — five agent-vs-chat videos | 0 | 5 | PASS; the confirmed profile left no worthwhile question | [Result](cross-project-fixtures/creative-content/planning/TEST-RESULT.md) · [Plan](cross-project-fixtures/creative-content/planning/PLAN.md) · [Visual](cross-project-fixtures/creative-content/planning/PLAN-VIEW.md) |
| Operational/event — 25-person AI workshop | 1 | 10 | PASS | [Result](cross-project-fixtures/operational-event/planning/TEST-RESULT.md) · [Plan](cross-project-fixtures/operational-event/planning/PLAN.md) · [Visual](cross-project-fixtures/operational-event/planning/PLAN-VIEW.md) |
| Personal — two-week family road trip | 2 | 5 | PASS after a source-quality failure was fixed and rerun | [Corrected result](cross-project-fixtures/personal-project/planning/TEST-RESULT.md) · [Plan](cross-project-fixtures/personal-project/planning/PLAN.md) · [Visual](cross-project-fixtures/personal-project/planning/PLAN-VIEW.md) |

Every final fixture has one complete planning ticket, `PLAN.md` and `PLAN-VIEW.md` at `awaiting approval`, `NEXT.md` naming only visual approval, build handoff unauthorized, a visible Mermaid view plus complete text route, and zero broken relative Markdown links. All execution tickets contain context, scope, exclusions, constraints, proof, blocked/disproven behavior, human review, and next eligibility.

## Demonstrated failures and fixes

### F-008 — Weak secondary evidence passed its own audit

The first personal-project run used travel aggregators as decision-changing route-duration evidence and still labeled itself PASS. The independent audit rejected that result.

The existing evidence contract and finish rubric were strengthened generically: decision-changing claims now require a primary source or direct provider; an unavoidable secondary fallback must be provisional, independently corroborated, and rechecked directly before irreversible commitment. No new component, storage, template, or domain rule was added.

A fresh-context rerun used direct OSRM routing and official attraction providers. Direct evidence disproved the original Dallas → Hot Springs and Little Rock → Dallas legs, so the plan added outbound and return Texarkana overnights and reconciled dates, nights, route, visual, decisions, evidence, handoff, and all execution tickets. Thirty-three evidence links and the complete fixture contract passed on rerun.

### F-009 — One software execution ticket was too large

The software finish audit found that one ticket combined corpus creation, integrated proof, performance verification, Windows packaging, clean installation, and human acceptance. It split that work into E-006 integrated proof and E-007 package/acceptance, then reran link, dependency, lifecycle, and ticket-contract checks.

The existing one-session sizing rule caught and repaired this failure. No plugin change or software domain pack was necessary.

## Independent conclusion

The current canonical core skill passes software, creative/content, operational/event, and personal-project fixtures without a domain pack. It adapts question count to actual uncertainty, keeps mechanics away from the user, researches consequential facts, reconciles contradictions, catches oversized handoffs, creates useful execution routes, and stops at explicit visual approval.

This proves T-03 only. It does not satisfy the simple or complex human live pilots and does not count as Drew's H-* acceptance.
