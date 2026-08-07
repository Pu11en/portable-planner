# E-001 — Lock the product contract

Status: complete — 2026-08-07

- Outcome: Portable Planner's authoritative product documents describe the approved optional idea-evidence flow and its objective acceptance boundary without weakening the existing planning-only or portability promises.
- Depends on: P-001

## Context

- [Confirmed behavior](../decisions/P-001-define-idea-evidence-flow.md)
- [Decision-changing evidence](../evidence/P-001-evidence.md)
- [Current product contract](../../docs/PRODUCT-CONTRACT.md)
- [Current acceptance checklist](../../docs/ACCEPTANCE.md)

## In scope

- Reconcile `docs/GOAL.md`, `docs/PRODUCT-CONTRACT.md`, `docs/MVP-PLAN.md`, and `docs/ACCEPTANCE.md` with the approved no-idea/thin-idea trigger and skip cases, early permission gate, real-world grounding, privacy-safe search briefs, bounded repository-first possibility research, narrowly permitted direct-source verification, adaptive one-to-three results, required human direction confirmation, evidence-tiered claims, safety rules, scenario trials, fallbacks, and human acceptance proof.
- Update `project-map/` so the remaining-work map owns the new implementation and validation work without creating a parallel tracker.
- Preserve the public-preview language and identify this capability as unproven until its live acceptance checks pass.

## Out of scope

- Editing the canonical skill behavior, creating validation fixtures, running live research, or implementing any service, API client, database, MCP server, web app, domain pack, or build mode.

## Constraints

- GitHub remains optional for users and is only one public research surface.
- The feature remains part of the one canonical planning skill and ends before build execution.
- Do not mark current human acceptance or real-use checks as passing based on planning or synthetic evidence.

## Proof

- Every new normative claim links to P-001 or its evidence; the four authority documents and project map agree on trigger, bounds, result, fallback, safety, and live proof.
- Existing excluded-architecture, no-account, one-question, and planning-only requirements remain explicit.
- All relative Markdown links resolve.

## If blocked or disproven

- If product authority cannot be reconciled without contradicting a confirmed Portable Planner boundary, stop and return only that exact conflict to planning.

## Human review

- Drew reviews the opening promise and acceptance wording for fidelity to the approved experience.

## Next eligible ticket

- E-002 — Add the flow to the canonical skill.

## Completion evidence

- The goal, product contract, MVP plan, acceptance checklist, and [remaining-work issue](../../project-map/issues/05-prove-idea-stage-possibility-scan.md) now agree on the approved behavior and keep I-01 through I-05 unpassed.
