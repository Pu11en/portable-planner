# Final-write barrier candidate test

Date: 2026-08-19
Candidate: `0.1.0-beta.8` public-preview release candidate
Source issue: I-10 — a late planning mutation can bypass the final proof boundary

## Evidence route

A bounded local session-history review confirmed one beta-7 planning path with this sanitized order:

`planning write -> relevant check -> material late planning write -> handoff`

No validation or canonical reconciliation followed the final mutation. A second Better Harness candidate was rejected because its raw trace did contain a custom final link check and canonical reread. See [the redacted review](../planning/evidence/P-002-beta7-final-state-review.md).

## Candidate correction

The canonical skill now treats the latest planning-file mutation as the final proof boundary for ticket completion, final review, handoff, and testing/build transitions. Reconciliation and the cheapest relevant check must occur after that mutation; another mutation invalidates them. No-write replies do not acquire a check requirement.

This is an instruction-only correction in the existing skill and validation rubric. It adds no runtime hook, state marker, service, database, role, project script, or domain-specific rule.

## Minimum replay

`validation/final-write-barrier/validate_trace.py` evaluated six event traces from `fixtures.json`:

- rejected the observed beta-7 late-write order for a software plan;
- rejected the same late-write order for an operational-event plan;
- accepted both domains after reconciliation and a check followed the last write;
- accepted a no-write informational reply without a check; and
- accepted an ordinary non-terminal write-through reply after canonical reconciliation without imposing a terminal check.

Result: `PASS 6 final-write-barrier fixtures`.

## Regression and package checks

- Skill Creator quick validation: pass.
- Codex plugin validation: pass.
- Codex, Claude Code, and ZCode manifest JSON parsing: pass.
- I-01 canonical Journey plus focus-lens grammar: pass.
- Six valid I-01 fidelity fixtures and six malformed controls: pass.
- New validator compilation: pass.
- `git diff --check`: pass.

## Evidence boundary

This proves the candidate contract, event-order invariant, package integrity, and selected cross-domain regression boundaries. It does not claim fresh human acceptance or that every host/model will obey the instruction. Codex locally installed `0.1.0-beta.8+codex.20260819234732` from this repository and verified that its cached bundle matches the source; it has not been published. The next qualifying ordinary-use trace should confirm that a late planning mutation is followed by final reconciliation/check without burdening no-write turns.
