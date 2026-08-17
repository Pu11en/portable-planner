# P-002 evidence — Portable Planner improvement inventory

Opened: 2026-08-15
Status: initial evidence-backed inventory; discover problems before selecting solutions

## Inventory rule

Portable Planner improvements are handled in two distinct phases:

1. Build and verify the problem inventory from Drew's current feedback, historical Codex/ZCode conversations, validation failures, and still-open human acceptance checks.
2. Take one confirmed issue at a time through evidence, alternative solution families, a bounded prototype or replay when needed, a selected correction, and affected regression proof.

Do not bundle an assumed solution into an issue statement. Do not treat an objective fixture pass as human acceptance, and do not redesign a behavior that has only a historical failure until the current version is checked.

## State labels

- **Confirmed current problem:** Drew's latest feedback or current live evidence establishes the problem now.
- **Settled target, unproven:** the desired behavior is defined, but the released experience has not passed the necessary real-use proof.
- **Historical failure, repair unconfirmed:** a correction exists, but the affected live experience has not proved it.
- **Regression guard:** objective evidence passes; preserve it unless real history shows a remaining failure.

## Improvement issues

### I-01 — A plan is hard to comprehend, and Mermaid does not solve it

- State: **Confirmed current problem.** This is the first issue to solve.
- Drew's current statement: visual plans are not correct; Mermaid does not add useful comprehension, and large plans or text-report plans are especially hard to understand.
- Existing evidence: [Visual comprehension failure](../../validation/VISUAL-COMPREHENSION-FAILURE.md) says the Hanoi view mixed route, live state, proof, scheduling, and supporting systems and exposed implementation structure instead of an immediately readable orientation. [Complex visual acceptance](../../validation/HANOI-HUMAN-ACCEPTANCE.md) records that later negative feedback superseded the earlier positive reaction.
- Problem boundary: this is not primarily a Mermaid syntax or styling problem. The generated view lacks a scalable information hierarchy, useful levels of detail, and an interaction model that lets the person understand the whole without reading the whole.
- Observable harm: Drew cannot quickly answer the destination, current position, next action, important human gates, and how to inspect one relevant part without interpreting a dense diagram or opening long reports.
- Solution work must compare: non-diagram outline/table views, progressive-disclosure cards, overview-plus-phase views, task-focused filters, and a genuinely interactive navigator on supported hosts. Mermaid may remain a portability fallback, but it cannot be assumed to be the comprehension experience.
- Completion evidence: on an actual large plan, Drew can orient himself, inspect one part, return to the overview, and state what happens next without reading the canonical reports first.

### I-02 — The planner can continue asking after words have stopped adding value

- State: **Settled target, unproven in ordinary live use.**
- Evidence: Drew said that once repeated recommended answers show alignment, more verbal questions can become useless and actual scenarios are more informative. The current contract defines delegation and bounded trials, but fresh human checks for speed, worthwhile questions, and walls of text remain open in [acceptance](../../docs/ACCEPTANCE.md).
- Problem boundary: distinguish a meaningful unresolved human choice from residual uncertainty that the agent should synthesize, research, or test.
- Observable harm: planning feels slow; the person repeats agreement; the agent produces more words instead of evidence.
- Completion evidence: real sessions contain only consequential questions, switch to a bounded example or trial when behavior/feel is the unknown, and reach a protected approval gate without hiding a major choice.

### I-03 — Planning must activate automatically without hijacking direct work

- State: **Settled target, unproven.**
- Evidence: Drew confirmed that unresolved destination, scope, success, proof, or meaningful tradeoffs should activate planning, while narrow status, explanation, diagnosis-only work, and sufficiently specified approved builds remain direct.
- Problem boundary: this is route discrimination, not a rule that every conversation becomes a plan.
- Observable harm: the planner either fails to help while the outcome is still being shaped or adds planning ceremony to work that is already clear.
- Completion evidence: real historical and fresh cases route unresolved work into the existing plan and keep direct tasks direct, with no duplicate plan or stale frontier.

### I-04 — Idea-stage repository research may be costly or produce links instead of understanding

- State: **Settled target, unproven.**
- Evidence: the idea-stage scan contract exists, but all `I-*` acceptance checks remain open. Drew's intended result is understanding what is possible, proven directions worth considering, and the fastest credible MVP path—not a popularity-ranked repository list.
- Problem boundary: relevance, decision usefulness, cost, consent, privacy, license handling, and honest no-match behavior.
- Observable harm: token/search cost rises while the user receives implementation trivia or links that do not change the product direction.
- Completion evidence: real thin ideas produce a bounded provisional recommendation and at most two materially different alternatives that change the user's understanding or MVP route; irrelevant and unsafe results are discarded.

### I-05 — Generated views and resumptions can disagree with the real plan state

- State: **Historical failure, repair unconfirmed in affected live use.**
- Evidence: `V-03` and `V-04` remain open after a stale beta-4 post-build view and earlier display failures. Objective fresh-resume checks pass, but the repaired candidate still needs affected human evidence.
- Problem boundary: canonical state remains authoritative; every displayed summary, current action, handoff, and resumed task must agree with it.
- Observable harm: the user sees completed work as current, repeats settled choices, or cannot tell which step is actually next.
- Completion evidence: a material change and a fresh resume both show the same current state and next action without relying on chat memory.

### I-06 — Recommendation convergence and delegation must save effort without stealing authority

- State: **Regression guard; live experience still open.**
- Evidence: beta 6 objectively passes the exact three-bare-recommended-key streak, option-`B` shortcut, reset, resumption, choice ceiling, and protected-gate matrix.
- Problem boundary: the shortcut offers delegation; it never infers it. Extra words do not count as a bare-key streak, and final approval remains human-owned.
- Observable harm if regressed: either needless preference questions continue after explicit delegation or the planner makes irreversible/personal decisions without authority.
- Completion evidence: preserve the beta-6 objective checks and verify the shortcut feels useful in a natural session. Do not redesign it merely because it belongs in the inventory.

### I-07 — The finished plan and build/test handoff may be technically complete but not usable

- State: **Settled target, human acceptance open.**
- Evidence: objective execution-ticket, approval-transition, and proactive-test checks pass, while human checks for usable plans and executable handoffs remain open.
- Problem boundary: a handoff must make the next real action obvious and executable without reopening major planning or making Drew design the test.
- Observable harm: the planner declares completion, points at files, or leaves the person to infer how to begin or judge the result.
- Completion evidence: Drew can start from the first ticket and later run the smallest real acceptance action without major clarification.

### I-08 — One protocol must remain effective across different kinds of work

- State: **Regression guard with natural-use risk.**
- Evidence: software, creative, event, operational, and personal fixtures pass, but ordinary and naturally complex human-use proofs remain open.
- Problem boundary: improve general decision behavior rather than adding domain packs or narrowing the planner to software workflows.
- Observable harm: questions become generic noun-swaps, repository mechanics leak into non-software planning, or an outside framework replaces Portable Planner's voice and state model.
- Completion evidence: materially different real plans retain worthwhile, project-specific questions and coherent outputs without separate domain implementations.

### I-09 — The improvement process itself can manufacture confidence

- State: **Confirmed current process problem.**
- Evidence: the former 30-run plan chose quantity before test meaning; the next authored six-contract matrix still ignored the available Codex/ZCode history. The [historical corpus inventory](P-002-test-inventory.md) corrects the source route.
- Problem boundary: use real conversations to discover and define failures, then replay only the minimum historical decision points needed to compare a candidate.
- Observable harm: time and tokens are spent on plausible-looking synthetic conversations that do not represent Drew's real usage, while regressions can still be missed.
- Completion evidence: every implemented correction links to a real issue and real trace, objective invariant, minimum counterfactual proof where necessary, and fresh human judgment.

## Initial order

1. I-01 — plan comprehension and scalable presentation, because Drew confirmed it now and every later review depends on understanding the plan.
2. I-02 and I-03 — conversation efficiency and correct activation, because they control whether the planner reaches a useful plan without friction.
3. I-04 — idea-stage research usefulness, because it is a new unproven entry flow.
4. I-05 through I-08 — verify repaired or objectively passing behaviors against real sessions and preserve them as regression constraints.
5. I-09 applies throughout as the method for every issue rather than a separate product feature.

This order is provisional only where later real-session evidence reveals a more damaging current failure. The next action is solution discovery for I-01, beginning with comprehension requirements and alternative information architectures rather than selecting a renderer.
