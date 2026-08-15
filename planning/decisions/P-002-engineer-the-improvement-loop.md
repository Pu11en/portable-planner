# P-002 — Engineer the next improvement loop

- Status: current — reopened 2026-08-15 after the test-design and default-routing gap
- Depends on: P-001

## Decision

Choose how Portable Planner should become more reliable and effective after beta 6 without cargo-culting expert workflows, increasing question burden, or treating an arbitrary run count as a test design.

## Reopened gap

Drew rejected the 30-run route because the plan selected a quantity before the exact conversations, starting states, failure claims, expected behavior, and human judgments were shaped. He also clarified the larger product intent: during project work, when the agent and user are still discussing what the outcome should be rather than executing an already-understood route, Portable Planner should normally recognize that planning is happening without requiring a command.

The previous approval surface was therefore premature. No automated-run budget is currently approved. The next route must first derive a small test inventory from real Codex/ZCode sessions and saved live failures, state what each case can prove, and ask only the human-owned questions that materially change that inventory.

## Viable options

- A. Build a decision-kernel and repeatable evaluation loop — Recommended; more initial engineering, but it makes future improvements measurable and protects against regressions.
- B. Tighten the canonical instructions directly from the expert patterns — Faster, but another prose-only revision may improve one case while silently harming others.
- C. Wait for more uncoached beta-6 use and repair only observed failures — Lowest immediate cost, but it leaves frontier quality and run-to-run variance largely unmeasured.

## Current unresolved decision — automatic planning boundary

- A. Default Portable Planner for unresolved project/product work — Recommended; automatically start or resume planning when destination, scope, success, or proof is still being negotiated, while leaving direct builds, narrow facts/status, and diagnosis-only requests in their normal workflows.
- B. Use Portable Planner for every project conversation that is not already building — Maximum planning coverage, but status questions, explanations, and narrow research would create unnecessary planning state.
- C. Keep explicit or phrase-matched invocation — Least intrusive, but repeats the current failure where planning behavior depends on the user knowing when to request it.

## Recommendation

A — Preserve the selected evidence-led improvement direction, but replace the preselected 30-run ceiling with evidence-first test design. Mine real saved failures and relevant task traces, convert each material behavior claim into a test contract, then choose the minimum ordinary, contrasting, and prohibited-action cases needed to discriminate beta 5, beta 6, and any later candidate. Use scripts for objective invariants and preserve human judgment for whether the planner understood the person and asked worthwhile questions.

## Confirmed decision

A remains confirmed as the improvement method: build a small decision-kernel and repeatable evaluation loop, compare immutable beta 5 and beta 6 before another behavior change, and restore the better proven reference after any regression. The former 30-run allocation and its derived execution route are withdrawn. Test count, prompts, starting states, and scoring remain unconfirmed until the evidence-derived test contracts and automatic planning boundary are settled.

## Delegation

None. Drew selected the evidence-led method but has not approved a replacement execution plan or delegated the current product boundary.

## Interaction state

- Recommended-key streak: 0
- Option-B shortcut: not ready

## Evidence

- [Current repository and Channel Brains evidence](../evidence/P-002-expert-engineering-evidence.md)
- [Earlier fixed-commit expert-skill pass](../../research/PORTABLE-PLANNER-EXPERT-SKILLS.md)
- [Beta-6 objective evidence](../../validation/BETA6-RELEASE-CANDIDATE-TEST.md)
- [Real beta-4 planning and test-handoff failures](../../validation/DECISIVE-FLOW-LIVE-ACCEPTANCE.md)

## Effects

- Returns lifecycle state to `planning`; E-010 through E-016 are draft-only and ineligible until the replacement test design passes review.
- The replacement route must inventory real failures before writing synthetic cases. Every retained case needs an exact starting state, exact natural user message, behavior claim, expected routing/decision, prohibited behavior, preserved output, and human-quality judgment.
- No run count may be selected before duplicate claims are collapsed and the minimum discriminating case set is visible. Repetition is justified only for observed model variance or a high-risk behavior that a single pass cannot distinguish.
- The automatic planning boundary must be settled before testing natural invocation; otherwise a test cannot tell a missed trigger from an intentionally excluded request.
- A beta-6 hard or material shared-behavior regression restores public beta 5 before candidate work. The candidate is developed and tested away from `main`; a worse or inconclusive result is never merged, and a failed temporary human-test installation restores the proven reference immediately.
- No database, service, MCP server, second skill, second canonical state tree, autonomous prompt optimizer, or production UI is justified by this research.

## Complete when

Drew settles the automatic planning boundary; the real-failure inventory and minimum test contracts are visible and individually justified; run count follows from those contracts rather than precedes them; rollback, architecture, and human gates are explicit; and revised execution tickets cover the complete route without treating expert opinion or authored prompts as proof.
