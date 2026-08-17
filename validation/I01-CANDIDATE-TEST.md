# I-01 Journey plus focus lens candidate test

Tested: 2026-08-17

Candidate plugin commit: `0553101c7e16a9019605df8bd2e1a5c7fbcbb644`

Reference: `v0.1.0-beta.6` at `cc4ff6e7b8e1465b4b3c0bb57656d480ddd29465`

## Verdict

`candidate eligible for human test`

This is an objective fidelity and regression verdict. It does not claim that
the new first read is easier or more pleasing for Drew; E-020 owns that fresh
human judgment.

## Six fidelity claims

| Claim | Valid view | Malformed control | Result |
|---|---|---|---|
| F-01 canonical fidelity | Preserved all decision-changing source fields | Changed the current decision | Pass; failed only `equal:current` |
| F-02 state freshness | Advanced current, next, and statuses together | Left milestone statuses stale | Pass; failed only `equal:statuses` |
| F-03 blocked recovery | Kept blocker, winner, and recovery visible | Continued toward release | Pass; failed only `equal:recovery` |
| F-04 human authority | Kept planning lifecycle and no delegation | Invented approval and delegation | Pass; failed only `equal:authority` |
| F-05 readable density | Used eight milestones, one `NOW`, six visible fields, and six rules | Used ten milestones | Pass; failed only `route_bounds` |
| F-06 rich/text parity | Kept identical ordered route semantics | Reordered the text route | Pass; failed only `parity:rich_route:text_route` |

`validate_candidate.py` also passed the canonical contract/template grammar.
The real project view contains seven milestones, exactly one rich-route `NOW`,
all five focus fields, six guardrails, and an exactly matching text route.

## Material state advance

The prior state at commit `101ef36` showed human review of E-017 through E-020
as current. Candidate commit `0553101` records E-017 and E-018 complete, E-019
current, and regenerates all of these together:

- the journey milestone states;
- the compact text route;
- the focus-lens current outcome;
- the exact next action; and
- the human role, proof, and recovery.

The stale approval-review state no longer appears as current.

## Beta-6 regression protection

Relative to `v0.1.0-beta.6`, only the canonical visual contract and
`PLAN-VIEW.md` template changed inside the plugin. The responsible bytes for
natural invocation, question routing, bare-key and option-B delegation,
protected gates, approval, artifact state, and session chaining are identical:

- `SKILL.md`
- `artifact-contract.md`
- `conversation-contract.md`
- `question-engine.md`
- `session-chaining.md`
- `validation-rubric.md`

The prior beta-6 behavior results therefore remain attributable to unchanged
instructions. Changed resumption/display behavior was separately exercised by
the state-advance, freshness, density, authority, and parity checks above.

## Package checks

- Skill Creator quick validation: pass.
- Plugin Creator validation: pass.
- Root and active plugin JSON manifests: parse pass.
- Version synchronization: five active entries remain `0.1.0-beta.6`; this
  candidate is not a published version.
- Current-product Markdown links: 207 local targets pass.
- Isolated ZCode installation: pass; installed bytes equal candidate source.
- `git diff --check`: pass.
- Installed beta-6 preflight: all 17 plugin files matched the beta-6 tag before
  controlled candidate installation.

## Candidate installation for E-020

The exact candidate plugin bytes are temporarily installed at:

`/mnt/c/Users/drewp/.codex/plugins/cache/portable-planner/portable-planner/0.1.0-beta.6`

The verified 17-file beta-6 recovery copy is preserved at:

`/mnt/c/Users/drewp/.codex/plugins/cache/portable-planner-recovery/portable-planner/0.1.0-beta.6`

The manifest version remains beta 6 because this is a controlled candidate
test, not a release. A failure or `worse` verdict restores the recovery copy
before any further improvement work.
