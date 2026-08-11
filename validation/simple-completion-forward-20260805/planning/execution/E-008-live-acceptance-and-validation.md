# E-008 — Run Live Read-Only Acceptance and Package Validation

- Outcome: A clean-context install and one representative public run prove the skill's portability, source fidelity, safety, and usefulness without an account or paid service.
- Depends on: P-001, E-007

## Context

- [Finished plan and approval status](../PLAN.md)
- [Confirmed contract](../decisions/P-001-define-finder-contract.md)
- [Platform evidence](../evidence/P-001-evidence.md)
- E-007 deterministic test summary

## In scope

- Install/load the unchanged skill package in a clean supported agent context using the normal Agent Skill path.
- Invoke it with ordinary language and a representative group of public AI YouTube channels supplied for acceptance.
- Verify the resolved allowed-channel set before evaluating output provenance.
- Run through compliant public access without signing in, using an API key, paying for a service, downloading media/transcripts, or performing any YouTube write action.
- Spot-check every returned channel/video/title/comment and each available highlighted-comment link against its public page.
- Confirm access failures or disabled comments are reported honestly.
- Have Drew review usefulness and manually open one result; recording remains outside the skill and this ticket.
- Rerun the package validator and archive only concise pass/fail evidence, not harvested comment datasets.

## Out of scope

- Replying/posting/liking/subscribing, recording or publishing content, retaining commenter profiles, exhaustive crawling, API-account setup, paid providers, dashboards, schedules, and product expansion.

## Constraints

- Live acceptance cannot pass if the harness lacks a compliant public-comment reading path; report that exact blocker and stop.
- One successful page is insufficient if any returned quote or attribution is wrong.
- Drew's visual/usefulness review is required, but no implementation work may extend beyond the approved contract.

## Proof

- Skill/package validation passes in the clean context.
- The natural-language run completes without account, key, payment, media download, or write action.
- All returned source fields spot-check correctly; wrong-channel count is zero; available comment links open the cited thread.
- If five results are returned, all five pass the rejection and Drew-fit gates; if fewer, the documented limitation is accurate and no padding occurred.
- Drew confirms at least one result is specific, credible, and worth opening for a manual short-video response.

## If blocked or disproven

- Record the exact platform, permission, capability, provenance, or quality failure. Fix only within the owning approved ticket and rerun; return to planning if compliant public access or the no-account requirement proves infeasible.

## Human review

- Required: Drew checks the final report, opens one source, and confirms whether it is worth recording. He does not approve any posting or recording automation.

## Next eligible ticket

- Plan complete.
