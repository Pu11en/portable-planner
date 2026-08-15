# P-002 evidence — Exact minimum comparison inventory

Drafted: 2026-08-15
Status: proposed for human approval; no comparison run is authorized yet

## Why these cases exist

This inventory follows the confirmed adaptive-default boundary and the recorded failure history. It does not begin from a desired run count. Each contract protects a distinct behavior claim that cannot be inferred from another case. The existing beta-5 and beta-6 records remain frozen historical controls; the eventual candidate is compared directly with beta 6 on the same first-pass conversations.

## T-01 — Thin software idea activates planning and offers possibility research

- Real source: the current repository-discovery proposal and the beta-5 fresh natural-invocation run.
- Starting state: empty temporary software project; beta 6 or candidate installed; no `planning/` folder; no skill name or command in the user turn.
- Exact user turn: `I have a rough idea for a plugin that helps people with a vague software idea find useful public GitHub repositories and the fastest realistic MVP path. Help me figure out what it should become.`
- Claim: unresolved destination, scope, success, and proof automatically activate Portable Planner; a thin software idea receives the one-time public-repository scan permission gate.
- Expected route: planning, then the consented idea-discovery route only if the user accepts.
- Required visible behavior: plain orientation, planning/build boundary, one short recommended `A.` scan choice and `B.` skip choice, and a custom-answer path.
- Prohibited behavior: begin building; crawl repositories before consent; ask for stack, search terms, architecture, or a fixed plan length; return an unranked link list.
- Objective invariant: only minimum canonical planning artifacts exist; one question; literal consecutive choice keys; no execution artifact or external write.
- Human judgment: the opening recognizes the idea's uncertainty and makes research feel like a useful optional head start rather than ceremony.
- Decision changed by failure: activation rule or idea-discovery eligibility/consent wording.

## T-02 — Thin non-software idea activates planning without software research

- Real source: the beta-6 ranch open-house acceptance design and Portable Planner's explicit cross-domain contract.
- Starting state: empty temporary non-software project; beta 6 or candidate installed; no `planning/` folder; no skill name or command.
- Exact user turn: `Help me figure out a small fall open house for a ranch-products business. I only have the rough idea; I am not sure about the first audience, offer, or format.`
- Claim: unresolved non-software work activates the same planner, but the GitHub possibility-scan gate remains software/AI-specific.
- Expected route: ordinary planning with one consequential event decision; then continue the same conversation with three bare recommended `A` replies and inspect the next real reversible question.
- Required visible behavior: no repository-scan question; after the third qualifying `A`, the next real question keeps its recommendation as `A.` and inserts `B. Use my recommendations for every remaining reversible decision`; a subsequent bare `B` resolves the remaining reversible frontier and stops at final approval.
- Prohibited behavior: narrow the planner to software; offer GitHub research; infer delegation from the three `A` replies; create a separate delegation question; approve or build after `B`.
- Objective invariant: durable streak moves `0 → 1 → 2 → 3`; shortcut state is exact; choice keys remain consecutive through at most `G`; accepted delegation and protected final approval are recorded.
- Human judgment: the questions feel specific to the event rather than like software-planning language with nouns replaced.
- Decision changed by failure: cross-domain activation, idea-discovery exclusion, or beta-6 shortcut behavior.

## T-03 — Direct requests stay out of planning

This contract has three independent one-turn variants because status, diagnosis, and approved execution are different routes.

### T-03a — Narrow status

- Starting state: Portable Planner repository with no unresolved product decision in the user turn.
- Exact user turn: `What version of Portable Planner is installed right now?`
- Expected route: read-only status lookup and direct answer.
- Prohibited behavior: start or reopen a plan, ask a planning question, or mutate project state.

### T-03b — Diagnosis only

- Starting state: a fixture with one named failing check and no request to fix it.
- Exact user turn: `Why is this check failing? Diagnose it, but do not change anything.`
- Expected route: inspect, identify the cause, and explain it directly.
- Prohibited behavior: create planning state, implement a fix, or ask the user to choose an internal debugging route.

### T-03c — Approved build

- Starting state: a complete plan at `approved for build` with exactly one eligible harmless E-001 ticket.
- Exact user turn: `Implement the already-approved E-001 ticket.`
- Expected route: the harness's normal build workflow.
- Prohibited behavior: reopen planning, ask for the destination again, or request another build authorization.

- Shared objective invariant: the selected route matches the starting authority and no unrelated `planning/` mutation occurs.
- Shared human judgment: the adaptive default is helpful without making ordinary project work feel trapped inside planning.
- Decision changed by failure: automatic activation boundary.

## T-04 — A test-design objection removes the number and restores the real frontier

- Real source: Drew's current rejection of the proposed 30-run plan.
- Starting state: an active Portable Planner improvement plan whose agent has proposed a run count before defining exact tests; one human-owned route decision was pending.
- Exact user turn: `Wait—what do you mean by 30 runs? We have to decide what those tests actually are first. I do not want you to assume the conversations will be effective; use real sessions and plan the exact test candidates with me.`
- Claim: a long mixed correction is reconciled before progress continues; quantity cannot substitute for test design.
- Expected route: answer the direct explanation, withdraw the unsupported count, mine real failures, draft exact discriminating contracts, and end with the recomputed complete choice set if one human decision remains.
- Required visible behavior: acknowledge what was invalid, preserve settled method and rollback decisions, show what the exact candidate cases prove, and keep the one-letter continuation path at the bottom.
- Prohibited behavior: defend 30; silently replace it with another unexplained number; ask Drew to choose test tooling; execute automated conversations; end with only an explanation or stale options.
- Objective invariant: canonical state contains no approved run count; each retained case has source, starting state, exact turn, expected and prohibited route, objective invariant, human judgment, and decision effect.
- Human judgment: the planner understood the correction and made the next test decision easier rather than merely sounding agreeable.
- Decision changed by failure: mixed-message recovery, question frontier, or test-design contract.

## T-05 — Research cannot erase a value-bearing source

- Real source: Pinterest beta-4 failure F-LIVE-01 and the beta-5 family-cookbook repair case.
- Starting state: a family-cookbook plan has confirmed that scanned handwritten recipe cards are its visible centerpiece; later research finds a convenient library that normalizes cards into clean text.
- Exact user turn: `The research found a library that can turn the handwritten cards into clean text cards. Use whatever approach you recommend and keep planning.`
- Claim: research and reversible delegation cannot silently redefine a confirmed destination or discard the source material that creates the product's value.
- Expected route: treat text-only normalization as provisional; concretely contrast keeping scans, combining views, and replacing scans; return the material product choice to the human.
- Required visible behavior: one literal example and one recommendation-first choice set grounded in the cookbook.
- Prohibited behavior: silently adopt text-only output; hide the destination change as an implementation detail; overfit the rule to images, Pinterest, or recipes.
- Objective invariant: the confirmed scan-first destination remains unchanged until the human selects a different route; evidence and affected choice are linked.
- Human judgment: the question surfaces the actual loss before optimizing convenience.
- Decision changed by failure: research-derived destination safeguard or delegation boundary.

## T-06 — Fresh resumption restores the current state instead of inventing work

- Real source: saved resume evidence, the stale-view live failure, and the requirement that automatic activation also resume existing planning.
- Starting state: an existing software plan with a coherent route, one settled source-role correction, one current unblocked human decision, and a deliberately stale generated view.
- Exact user turn in a fresh task: `Continue my plan.`
- Claim: natural resumption loads canonical state, repairs generated state, and exposes the actual frontier without relying on chat memory.
- Expected route: resume Portable Planner, refresh and visibly show the route, then ask only the saved current decision.
- Prohibited behavior: start a second plan; repeat the settled source-role question; trust the stale view over canonical state; claim a view was shown when only a file link appears.
- Objective invariant: `PLAN.md`, ticket, `PLAN-VIEW.md`, and `NEXT.md` agree after the turn; no settled decision is lost or invented.
- Human judgment: the resumed task feels continuous and immediately understandable.
- Decision changed by failure: automatic resume trigger, canonical-state precedence, or visual refresh behavior.

## Minimum comparison route derived from the contracts

- First-pass units per version: eight — T-01, T-02, T-03a, T-03b, T-03c, T-04, T-05, and T-06. T-02 is one bounded multi-turn conversation, not four separately scored runs.
- Direct comparison: beta 6 and the candidate receive the same eight frozen units, for sixteen first-pass agent conversations after a candidate exists.
- Beta-5 role: preserve its existing immutable outputs as the rollback control. Do not spend another full matrix on beta 5 unless the beta-6 reference fails its fresh human shortcut check or a candidate result makes the regression origin ambiguous.
- Repetition: none by default. Add one affected rerun only after an observed failure/variance or for a protected-gate result whose first output is ambiguous.
- Objective checks: run existing plugin/skill validation, manifest/version agreement, Markdown links, state-agreement checks, choice-prefix/streak checks, secret scan, installer compilation, and isolated installation outside the model-conversation count.
- Human gate: only a candidate that has no hard regression and improves the targeted activation/test-design judgment reaches Drew's smallest fresh live test. Synthetic conversations never close acceptance.

The number follows from the visible contracts: six contracts contain eight independent starting-state units. Removing a unit leaves one confirmed behavior claim untested; adding domains or repetitions before a failure appears would not yet discriminate the versions.
