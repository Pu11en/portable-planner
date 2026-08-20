# Plan: Make Portable Planner measurably better

**Status:** planning

## Continuation

- Mode: manual
- Latest boundary: none
- Successor task: none

## Destination

Portable Planner reliably chooses the right next planning action with less user effort, preserves human authority and durable state, and proves each improvement repeatably before it ships.

## Success

- The planner automatically recognizes unresolved project/product planning at the agreed boundary, presents even large plans in a form Drew can genuinely comprehend, and improves through a visible problem inventory followed by one evidence-backed solution at a time. Any candidate comparison uses the smallest real decision-point replays with exact state, expected decision, prohibited behavior, and human judgment.

## Boundaries

- In: the existing canonical skill and planning state, a complete improvement-issue inventory, scalable plan-comprehension alternatives, selective adaptation of evidence-backed mechanisms, a normative decision-kernel contract, read-only private indexing of historical Codex/ZCode sessions, a bounded redacted trace corpus across materially different domains, objective invariant validation, minimum counterfactual replay, and uncoached field-use review.
- Out: replacing or vendoring another planning framework, copying another creator's protocol or interface, narrowing to software, a second skill or state tree, a database or service, an autonomous prompt optimizer, production UI, a fixed question quota, or changes justified only by popularity or expert opinion.

## Map

`2/2`

- ✓ [P-001 — Define decisive planning behavior](decisions/P-001-define-decisive-planning.md) — depends on: none
- ▶ [P-002 — Engineer the next improvement loop](decisions/P-002-engineer-the-improvement-loop.md) — depends on: P-001

## Confirmed decisions

- [P-001](decisions/P-001-define-decisive-planning.md): Explicit scoped delegation covers remaining reversible decisions; settled or experiential uncertainty is not re-asked; bounded trials replace exhausted discussion; replies stay short, take the next safe action, and proactively move finished work to approval and live testing; protected gates remain explicit.
- [P-002](decisions/P-002-engineer-the-improvement-loop.md): Use Portable Planner as the adaptive default for unresolved project/product work, keep direct status/diagnosis/approved-build routes direct, preserve one original cross-domain protocol, adapt outside mechanisms only for named failures with cross-domain proof, and derive the minimum comparison set from real failures before revising the build route.

## Execution

- ✓ [E-001 — Lock the behavior contract](execution/E-001-lock-behavior-contract.md)
- ✓ [E-002 — Update the canonical skill](execution/E-002-update-canonical-skill.md)
- ✓ [E-003 — Prove varied planning behavior](execution/E-003-prove-varied-behavior.md)
- ✓ [E-004 — Run fresh live acceptance](execution/E-004-run-live-acceptance.md) — completed with recorded failures
- ✓ [E-005 — Repair the live interaction failures](execution/E-005-repair-live-failures.md)
- ✓ [E-006 — Rerun affected behavior and package checks](execution/E-006-rerun-release-candidate.md)
- ✓ [E-007 — Integrate and publish the release candidate](execution/E-007-publish-release-candidate.md)
- ✓ [E-008 — Implement the exact option-B delegation shortcut](execution/E-008-implement-exact-delegation-shortcut.md)
- ✓ [E-009 — Validate and publish beta 6](execution/E-009-validate-publish-beta6.md)
- ! [E-010 through E-016 — Draft improvement route](execution/E-010-lock-decision-kernel.md) — blocked by reopened P-002; former test counts are invalid
- ✓ [E-017 — Freeze the I-01 fidelity contract](execution/E-017-freeze-i01-fidelity-contract.md)
- ✓ [E-018 — Implement the Journey plus focus lens candidate](execution/E-018-implement-focus-lens-candidate.md)
- ✓ [E-019 — Compare the I-01 candidate and protect beta 6](execution/E-019-compare-i01-candidate.md)
- ~ [E-020 — Run the I-01 fresh-session acceptance](execution/E-020-run-i01-human-acceptance.md) — superseded by Drew's field-use decision; not passed
- ✓ [E-021 — Publish beta 7 for ordinary field use](execution/E-021-publish-beta7-field-candidate.md) — depends on E-019
- ✓ [E-022 — Install beta 8 as a local field candidate](execution/E-022-install-beta8-local-candidate.md) — depends on confirmed I-10 evidence and candidate checks
- ▶ [E-023 — Publish beta 8 for ordinary field use](execution/E-023-publish-beta8-field-candidate.md) — depends on E-022 and explicit publication authorization

## Approval

- Prior beta-6 route: approved and released
- Current improvement revision: beta 7 publication and uncoached Codex/ZCode field use explicitly authorized; production proof remains open
- Current session: Drew selected the recommended prove-and-improve route on 2026-08-19. This authorizes one evidence-backed Portable Planner change and its validation if beta-7 attribution and a reproducible failure are established; unsupported changes remain prohibited.
- Beta-8 disposition: Drew's immediate `yes` authorized the recommended local beta-8 version and Codex installation for ordinary field proof. It does not authorize commit, push, publication, tag, GitHub release, or other-harness installation.
- Beta-8 publication: Drew then explicitly asked to push beta 8 as the new version used instead of beta 7. This authorizes the scoped commit, push, release PR/merge, `v0.1.0-beta.8` prerelease, public marketplace refresh, and public Codex installation. Production-proof claims and other-harness installs remain unauthorized.

## Now

- Current: PUBLISH — Promote the validated beta-8 candidate through a reviewed public release and replace the local development install with the public beta-8 plugin.
- Next: HUMAN PROOF — Use public beta 8 normally, then request the bounded audit after enough sessions to expose a useful pattern.
