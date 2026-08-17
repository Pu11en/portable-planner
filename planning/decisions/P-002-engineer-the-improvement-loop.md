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

The improvement loop now begins with a problem inventory rather than candidate solutions or test counts. Drew confirmed the first current issue: large plans and report-like text are hard to comprehend, while rendering structure alone does not make it meaningfully easier to understand. Nine initial issues are now visible. The three standalone I-01 image directions were rejected because they moved the experience outside the session and asked for a premature screen choice. Local history recovered the actual earlier positive control: a real project plan shown directly in one Codex reply with destination, current state, route, gates, next action, proof, and recovery. The current action is to replay that presentation contract using this plan's real state before choosing any implementation.

Drew then established the compression invariant: Portable Planner should reduce required reading without reducing comprehension of the same technical plan. I-01 will compare three in-session presentations of identical canonical state: a route-first visual spine, a compact status board, and a progressive-disclosure hybrid. The hybrid is provisional recommendation because it can keep the default view shortest while retaining detail in the same session; the comparison, not the description, determines whether that is true.

The first compressed examples exposed two further requirements: the core plan must not require expansion to become visible, and the presentation must be aesthetically pleasing enough to invite scanning. The active comparison therefore replaces the three isolated formats with four fully visible hybrids: mission control, journey plus focus lens, three-lane roadmap, and compass map. Journey plus focus lens is the provisional recommendation because it preserves the whole route while giving the current technical step visual priority.

Drew selected the recommended Journey plus focus lens composition with bare `A` on 2026-08-16. The selection advances I-01 to a dynamic scenario trial, not production implementation. The same composition is now tested against the real Portable Planner improvement state, an early thin software idea, the complex GOMER production plan, and a losing-candidate recovery state.

After seeing all four cases, Drew selected the recommended `Keep this structure and refine its polish` route with another bare `A`. The scenario set therefore passes directionally: stop producing new composition families and refine one faithful current-plan prototype. The prototype uses no more than seven route milestones, one dominant current step, one short focus lens, and one quiet issue rail.

Drew then selected bare `A. Lock this structure` on 2026-08-17, completing a three-response recommended-key streak. The locked grammar is now applied read-only to GOMER's actual 144-line canonical plan and 242-line current view. The next real reversible decision is whether that faithful large-plan output becomes the I-01 candidate or receives one targeted focus/route revision; its displayed choice set includes the option-`B` delegation shortcut without granting delegation automatically.

Drew accepted the GOMER-tested output as the I-01 candidate with bare `A`. Because `B` was the offered delegation shortcut, choosing `A` consumed the shortcut, reset the streak, and granted no delegation. Six unique failure claims now define the minimum objective proof; there is no arbitrary run count. The smallest candidate remains inside the existing visual contract, template, and objective validation surface.

The complete I-01 route is E-017 through E-020: freeze six sanitized claim-derived fixtures, implement only the accepted view contract/template/checks, run objective fidelity and beta-6 regression protection, then perform one fresh real-session acceptance with verified beta-6 restoration on failure. Drew approved this route with bare `A` on 2026-08-17. Passing I-01 creates a working improvement-branch candidate and returns to I-02; it does not publish a release by itself.

## Recommendation

Preserve the selected evidence-led improvement direction and separate problem discovery from solution selection. Use the [improvement inventory](../evidence/P-002-improvement-issues.md) to keep current failures, unproven targets, repaired historical failures, and regression guards distinct. For each confirmed issue, use historical traces as the test-design source and run only the minimum prototype or decision-point replay needed to choose a correction.

## Confirmed decision

A remains confirmed as the improvement method: build a small decision-kernel and repeatable evaluation loop, compare immutable beta 5 and beta 6 before another behavior change, and restore the better proven reference after any regression. The former 30-run allocation and its derived execution route are withdrawn. Test count, prompts, starting states, and scoring remain unconfirmed until the evidence-derived test contracts and automatic planning boundary are settled.

External inspiration is also confirmed as bounded input: preserve Portable Planner's own cross-domain protocol and adapt only evidence-backed mechanisms that survive cross-domain tests.

The automatic activation boundary is confirmed as the adaptive default described above. The authored six-contract/eight-unit matrix is withdrawn. The replacement source and privacy boundary are recorded in the [historical Codex and ZCode corpus inventory](../evidence/P-002-test-inventory.md). The first evidence-backed [improvement inventory](../evidence/P-002-improvement-issues.md) contains nine issues; I-01 plan comprehension is the first confirmed problem to take through solution discovery.

## Delegation

None. Corpus indexing and redacted case discovery are agent-owned research actions. Drew approved only the bounded E-017 through E-020 implementation and comparison route; he did not delegate product decisions, final acceptance, or publication.

## Interaction state

- Recommended-key streak: 0
- Option-B shortcut: consumed; no delegation granted

## Evidence

- [Current repository and Channel Brains evidence](../evidence/P-002-expert-engineering-evidence.md)
- [Historical Codex and ZCode corpus inventory](../evidence/P-002-test-inventory.md)
- [Portable Planner improvement inventory](../evidence/P-002-improvement-issues.md)
- [I-01 large-plan comprehension alternatives](../evidence/P-002-I-01-plan-comprehension.md)
- [Earlier fixed-commit expert-skill pass](../../research/PORTABLE-PLANNER-EXPERT-SKILLS.md)
- [Beta-6 objective evidence](../../validation/BETA6-RELEASE-CANDIDATE-TEST.md)
- [Real beta-4 planning and test-handoff failures](../../validation/DECISIVE-FLOW-LIVE-ACCEPTANCE.md)

## Effects

- Returns lifecycle state to `planning`; E-010 through E-016 are draft-only and ineligible until the replacement test design passes review.
- The replacement route must inventory real failures before writing synthetic cases. Raw conversations remain private and untracked; only aggregates, redacted contracts, and minimum sanitized excerpts may enter this public repository.
- Historical traces supply real wording, behavior, and user corrections. Candidate changes are tested with the minimum decision-point replay needed for a counterfactual comparison, not blanket full-conversation generation.
- Problems are inventoried before solutions. Every issue is labeled as a confirmed current problem, an unproven target, a historical repair awaiting confirmation, or a regression guard so a passing behavior is not needlessly redesigned.
- Mermaid is not accepted as the visual-comprehension solution merely because it renders. I-01 must compare alternative information architectures and supported interaction models on an actual large plan.
- I-01's current baseline is the recovered in-session presentation, not a selected dashboard or renderer. Focus-first navigation, structured disclosure, and optional task-specific views remain research inputs until the real in-session candidate exposes a narrower need.
- Three stable I-01 concept images remain as failed evidence. None was selected; their generated text drift and out-of-session presentation must not be mistaken for canonical state or human acceptance.
- The in-session candidate must use real canonical state and show orientation, route, current/next, human gates, proof, and recovery together. A PNG, link-only handoff, generic UI screen, or Mermaid rendering by itself cannot satisfy I-01.
- Journey plus focus lens is now the accepted I-01 candidate structure. Six claim-derived objective cases and Drew's later real-use judgment—not a fixed run count—decide whether it ships.
- Compression may change hierarchy and initial visibility, but it may not delete or alter technical meaning. Every I-01 variant uses identical canonical plan state and is rejected if Drew must open the planning reports to recover essential context.
- Requiring expansion for destination, current, next, route, gate, proof, or recovery is an I-01 failure. Aesthetics and hierarchy are judged as usability because a technically complete view that is visually unpleasant or hard to scan does not meet the product goal.
- No run count may be selected before duplicate claims are collapsed and the minimum discriminating case set is visible. Repetition is justified only for observed model variance or a high-risk behavior that a single pass cannot distinguish.
- The adaptive automatic planning boundary is settled and must control every natural-invocation and direct-route test.
- Any imported or adapted mechanism must be tested across materially different software and non-software plans; a software-only success cannot justify narrowing the general planner.
- A beta-6 hard or material shared-behavior regression restores public beta 5 before candidate work. The candidate is developed and tested away from `main`; a worse or inconclusive result is never merged, and a failed temporary human-test installation restores the proven reference immediately.
- No database, service, MCP server, second skill, second canonical state tree, autonomous prompt optimizer, or production UI is justified by this research.

## Complete when

The evidence-backed improvement inventory is complete enough for Drew to add or correct missing issues; every confirmed issue has a separate solution-discovery and proof route; the real-session corpus supplies redacted cases; any comparison count follows from those cases; and revised execution tickets do not treat Mermaid rendering, expert opinion, objective fixtures, or authored prompts as human proof.
