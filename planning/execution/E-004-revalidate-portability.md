# E-004 — Revalidate installation and portability

Status: static package preflight complete; fresh Codex and non-Codex behavior open

- Outcome: The modified canonical package installs and invokes naturally across supported harnesses while preserving the same optional research behavior and unchanged project-local planning state.
- Depends on: E-003

## Context

- [Confirmed behavior](../decisions/P-001-define-idea-evidence-flow.md)
- [Canonical package](../../plugins/portable-planner/skills/portable-planner/SKILL.md)
- [Current installation evidence](../../validation/PUBLIC-PREVIEW-DISTRIBUTION-TEST.md)
- [Current portability evidence](../../validation/PORTABLE-VIEW-TEST.md)

## In scope

- Validate the canonical skill and Codex, Claude, and ZCode plugin manifests using the repository's existing validation paths.
- Confirm every new reference is included by installers that copy only explicitly linked support files.
- Test fresh natural-language idea-stage invocation in Codex and at least one non-Codex harness using the same canonical skill and project-local plan state.
- Verify decline, successful public research, unavailable research, and cross-harness resume behavior without requiring a GitHub account or token.

## Out of scope

- New harness-specific research logic, a separate skill copy, private-repository access, account setup, or modification of historical validation fixtures as if they were new evidence.

## Constraints

- Harness adapters remain thin and cannot own behavior.
- A harness lacking research capability must expose the exact limitation and continue planning rather than fail installation or invent results.
- Planning state remains unchanged across resumption and no worktree is introduced for planning.

## Proof

- All manifests parse and validate; package/install checks confirm the new reference exists; all referenced files and templates resolve.
- Fresh Codex and non-Codex transcripts show the same gate, bounds, result fields, and fallback semantics within each host's available tools.
- Cross-harness resumption reads unchanged `planning/` files and does not repeat a settled permission decision.

## If blocked or disproven

- Record the exact harness limitation. Change an adapter only for installation or discovery; return shared behavior failures to E-002 or P-001 as appropriate.

## Human review

- None; objective portability evidence is reviewed in E-005's final audit.

## Next eligible ticket

- E-005 — Run live idea-stage acceptance.

## Evidence so far

- [Package and portability preflight](../../validation/idea-discovery/PACKAGE-PORTABILITY-PREFLIGHT.md)

Canonical validation, manifests, links, and an isolated ZCode install pass. Fresh Codex emitted no final response, Claude Code authentication is expired, Hermes cannot inspect the unpublished local directory, and the installed Codex `beta.2` correctly remains unchanged. No cross-harness behavioral pass is claimed yet.
