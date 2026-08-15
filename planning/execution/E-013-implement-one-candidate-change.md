# E-013 — Implement one evidence-backed candidate change

- Outcome: One isolated candidate makes the smallest plausible correction to the single failure class selected from the beta-6 baseline.
- Depends on: E-012

## Context

- [Baseline report ticket](E-012-measure-beta6-baseline.md)
- [Decision-kernel contract](E-010-lock-decision-kernel.md)
- [Confirmed improvement method](../decisions/P-002-engineer-the-improvement-loop.md)

## In scope

- Create a candidate branch from the reviewed planning baseline.
- Change only the normative instruction, validator, template, or precedence rule causally linked to the selected failure.
- Prefer deleting duplication or clarifying precedence over adding more instruction text.
- Run static, package, link, and deliberately malformed-fixture checks before behavioral comparison.

## Out of scope

- Multiple behavior experiments, reading held-out prompts, tuning to individual transcript wording, merging, releasing, or replacing the public beta-6 installation.

## Constraints

- One demonstrated failure class permits one targeted revision.
- The candidate must remain attributable to one diff and one pre-registered assertion.
- Beta-6 tag and public installation remain recoverable and unchanged.

## Proof

- The diff is minimal, validators pass, and the change-to-failure causal claim is written before candidate behavioral runs begin.
- No unrelated product rule or architecture enters the candidate.

## If blocked or disproven

- If the failure cannot be fixed within the existing skill, references, templates, and lightweight validator, return to planning with the exact evidence. Do not expand architecture automatically.

## Human review

- None until objective non-regression passes.

## Next eligible ticket

- E-014 — Compare, keep, or reject the candidate.
