# P-002 — Engineer the next improvement loop

- Status: current — reopened 2026-08-15 after the test-design and default-routing gap
- Depends on: P-001

## Decision

Choose how Portable Planner should become more reliable and effective after beta 6 without cargo-culting expert workflows, increasing question burden, or treating an arbitrary run count as a test design.

## Reopened gap

Drew rejected the 30-run route because the plan selected a quantity before the exact conversations, starting states, failure claims, expected behavior, and human judgments were shaped. He also clarified the larger product intent: during project work, when the agent and user are still discussing what the outcome should be rather than executing an already-understood route, Portable Planner should normally recognize that planning is happening without requiring a command.

The previous approval surface was therefore premature. No automated-run budget is currently approved. The local history audit then established that the desktop connector's Codex `thread_list_unavailable` result did not mean the history was absent: Codex rollout files and ZCode's structured local session databases contain a substantial real-use corpus. The next route must mine and redact those real traces before authored prompts or a comparison count are considered.

## Confirmed external-inspiration boundary

Drew confirmed that Portable Planner remains its own cross-domain plugin. Open-source skills and repositories may be inspected for mechanisms, engineering discipline, failure evidence, or small reusable components, then adapted to Portable Planner's existing protocol. They may not replace its conversation model, canonical state, voice, portability boundary, or support for software, business, courses, creative work, events, operations, and personal projects.

Repository popularity is discovery evidence, not effectiveness proof. A borrowed mechanism must solve a named Portable Planner failure, fit the existing skill/reference architecture, preserve generality, and pass materially different domain cases. If implementation code is reused rather than the idea being independently adapted, its license, provenance, maintenance surface, and exact included scope must be reviewed first. Installing or vendoring another planning framework is not the default route.

## Viable options

- A. Build a decision-kernel and repeatable evaluation loop — Recommended; more initial engineering, but it makes future improvements measurable and protects against regressions.
- B. Tighten the canonical instructions directly from the expert patterns — Faster, but another prose-only revision may improve one case while silently harming others.
- C. Wait for more uncoached beta-6 use and repair only observed failures — Lowest immediate cost, but it leaves frontier quality and run-to-run variance largely unmeasured.

## Confirmed automatic planning boundary

Drew selected option A with a bare `a`: Portable Planner becomes the adaptive default for unresolved project/product work. It automatically starts or resumes planning when destination, scope, success, proof, or a meaningful human tradeoff is still being negotiated. Sufficiently specified builds, narrow facts and status, explanation, and diagnosis-only requests remain in their normal workflows. An active-plan digression still reconciles and saves the planning frontier without treating the side question itself as a new plan.

## Current evidence action — historical corpus first

The agent now owns the next action: create a private, read-only index of real Codex and ZCode conversations, identify the smallest materially different planning and correction moments, and surface redacted case summaries. Drew does not need to choose a synthetic conversation count or test matrix before that evidence exists.

## Recommendation

Preserve the selected evidence-led improvement direction, but use the historical corpus as the test-design source. Mine real saved failures and relevant task traces, convert each material behavior claim into a redacted test contract, then choose only the decision-point replays needed to discriminate beta 6 and a later candidate. Use scripts for objective invariants and preserve human judgment for whether the planner understood the person and asked worthwhile questions.

## Confirmed decision

A remains confirmed as the improvement method: build a small decision-kernel and repeatable evaluation loop, compare immutable beta 5 and beta 6 before another behavior change, and restore the better proven reference after any regression. The former 30-run allocation and its derived execution route are withdrawn. Test count, prompts, starting states, and scoring remain unconfirmed until the evidence-derived test contracts and automatic planning boundary are settled.

External inspiration is also confirmed as bounded input: preserve Portable Planner's own cross-domain protocol and adapt only evidence-backed mechanisms that survive cross-domain tests.

The automatic activation boundary is confirmed as the adaptive default described above. The authored six-contract/eight-unit matrix is withdrawn. The replacement source and privacy boundary are recorded in the [historical Codex and ZCode corpus inventory](../evidence/P-002-test-inventory.md).

## Delegation

None. Corpus indexing and redacted case discovery are agent-owned research actions. Drew has not delegated product decisions or approved a candidate implementation or comparison run.

## Interaction state

- Recommended-key streak: 0
- Option-B shortcut: not ready

## Evidence

- [Current repository and Channel Brains evidence](../evidence/P-002-expert-engineering-evidence.md)
- [Historical Codex and ZCode corpus inventory](../evidence/P-002-test-inventory.md)
- [Earlier fixed-commit expert-skill pass](../../research/PORTABLE-PLANNER-EXPERT-SKILLS.md)
- [Beta-6 objective evidence](../../validation/BETA6-RELEASE-CANDIDATE-TEST.md)
- [Real beta-4 planning and test-handoff failures](../../validation/DECISIVE-FLOW-LIVE-ACCEPTANCE.md)

## Effects

- Returns lifecycle state to `planning`; E-010 through E-016 are draft-only and ineligible until the replacement test design passes review.
- The replacement route must inventory real failures before writing synthetic cases. Raw conversations remain private and untracked; only aggregates, redacted contracts, and minimum sanitized excerpts may enter this public repository.
- Historical traces supply real wording, behavior, and user corrections. Candidate changes are tested with the minimum decision-point replay needed for a counterfactual comparison, not blanket full-conversation generation.
- No run count may be selected before duplicate claims are collapsed and the minimum discriminating case set is visible. Repetition is justified only for observed model variance or a high-risk behavior that a single pass cannot distinguish.
- The adaptive automatic planning boundary is settled and must control every natural-invocation and direct-route test.
- Any imported or adapted mechanism must be tested across materially different software and non-software plans; a software-only success cannot justify narrowing the general planner.
- A beta-6 hard or material shared-behavior regression restores public beta 5 before candidate work. The candidate is developed and tested away from `main`; a worse or inconclusive result is never merged, and a failed temporary human-test installation restores the proven reference immediately.
- No database, service, MCP server, second skill, second canonical state tree, autonomous prompt optimizer, or production UI is justified by this research.

## Complete when

The real-session corpus is privately indexed and deduplicated; Drew sees a redacted set of materially different historical planning moments; any remaining comparison count follows from those cases rather than precedes them; rollback, privacy, architecture, and human gates are explicit; and revised execution tickets do not treat expert opinion or authored prompts as proof.
