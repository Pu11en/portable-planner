# Pre-live real-use audit

**Date:** 2026-08-06  
**Package:** `0.1.0+codex.20260806154800`  
**Result:** Ready for Drew's first ordinary real plan. This is technical readiness, not human acceptance.

## Installed-package proof

- Official plugin validator: pass.
- Official skill validator: pass.
- Canonical package and personal-marketplace source: recursive match before installation.
- `codex plugin add portable-planner@personal`: pass.
- `codex plugin list --json`: installed and enabled from `/home/drewp/plugins/portable-planner`.
- Fresh task natural invocation without the skill name: pass.

## Fresh-context behavior

The fresh task received only `Plan the idea in IDEA.md with me`.

- Discovered and loaded the installed skill automatically.
- Oriented the user and preserved the planning-only boundary.
- Asked exactly one consequential human question.
- Used `A/B/C`, recommendation first, and a custom-answer path.
- Created only project-local `planning/PLAN.md`, `NEXT.md`, and one current decision ticket.
- Kept unrelated dirty workspace changes untouched.

## Delegated-completion behavior

The next instruction was `Use your recommended answers for the rest of this plan`.

- Asked no further preference questions inside the delegation.
- Researched only route-changing factual feasibility from direct documentation.
- Produced one completed route, canonical `PLAN-VIEW.md`, and five dependency-ordered session-sized execution tickets.
- Set all review artifacts to `awaiting approval` and kept build authorization off.
- Displayed Mermaid plus a complete text route in the CLI, where the richer desktop visualization surface was unavailable.
- Asked for explicit approval and performed no build work.

## Failure and recovery coverage

| Risk | Result |
|---|---|
| Natural invocation misses the plugin | Passed in a fresh task |
| One-character choices lose meaning | Previously forward-tested; full meaning persists in canonical state |
| User delegates remaining recommendations | Passed in current installed package |
| Workspace path contains an apostrophe | A read command failed; the task named the failure, corrected quoting, preserved state, and continued |
| Visual surface is unavailable | CLI showed Mermaid and the complete text route instead of claiming an interactive popup |
| Confusion during planning | Existing fresh-context recovery test passes; questions pause until orientation returns |
| Unrelated idea appears mid-plan | Contract now preserves current state and requires a deliberate switch-or-separate decision |
| Targeted revision after review | Existing approval-transition test passes and current lifecycle contract reopens only affected planning |
| Fresh-session state loss | Existing Codex and Hermes resume evidence passes from unchanged project-local files |
| Premature implementation | Current completion run stopped at `awaiting approval` with build authorization off |
| Incomplete handoff | Current run generated five ordered tickets with scope, exclusions, proof, recovery, human review, and next eligibility |

## Human checks still open

- Whether the ordinary conversation actually feels faster and clearer to Drew.
- Whether the preferred interactive desktop presentation appears and is understandable during a real plan.
- Whether a naturally complex real plan remains comprehensive without becoming a wall of text.
- Whether Drew would actually use the final plan and execution tickets.

Those checks can only be answered by real use; additional canned examples cannot close them.
