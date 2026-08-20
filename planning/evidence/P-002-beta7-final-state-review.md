# P-002 evidence — Beta-7 final-state review

Reviewed: 2026-08-19
Status: one confirmed beta-7 failure; one analyzer false positive

## Evidence boundary

- The source is a bounded local Codex history review for the Hanoi workspace plus the privacy-safe Better Harness report.
- Raw prompts and stable session identifiers remain local and are not copied here.
- Both decisive planning paths read the installed `0.1.0-beta.7` Portable Planner skill immediately before or during the relevant work.
- This establishes beta-7 attribution for the two reviewed paths, but it does not make every generic Harness finding a Portable Planner defect.

## Confirmed failure contract

### Decision question

Can a late planning mutation made after validation reach handoff without a new final-state reconciliation?

### Starting state

- An existing cross-domain plan is being created or materially revised.
- The agent has written the canonical planning artifacts and run a relevant check.
- Independent audit feedback arrives or completes inside the same turn after that check.

### Expected behavior

- Apply the audit-driven correction.
- Treat that correction as invalidating the prior validation result.
- Recompare the current decision with `PLAN.md`, `PLAN-VIEW.md`, and `NEXT.md` as applicable.
- Rerun the cheapest relevant final check after the last mutation.
- Hand off only when no later planning mutation follows that check.

### Observed beta-7 behavior

The agent wrote the plan, ran `git diff --check`, applied a later substantive correction to the decision, view, and evidence from independent audit results, and immediately handed off. No relevant validation or canonical reconciliation followed the final patch.

### Prohibited behavior

- Treat an earlier passing check as coverage for later mutations.
- Add a project-specific planner implementation or parallel state tree.
- Require every user project to adopt a new service, database, or broad test framework.
- Claim the failure changed the resulting plan's meaning without direct evidence; the confirmed defect is the missing final proof boundary.

### Minimum replay

1. Create or copy a sanitized cross-domain planning fixture.
2. Perform an initial write-through and validation.
3. Introduce one material audit correction after validation.
4. Observe whether the planner revalidates after the final mutation before handoff.
5. Reject the candidate if a mutation can occur after the final check, or if the repair adds ceremony to turns with no writes.

## Analyzer false positive

The second reported path created a detailed plan and appeared to have no check in the summary report. The bounded raw trace shows a final command that validated every relative planning link and then reread `PLAN.md`, `PLAN-VIEW.md`, and `NEXT.md` before handoff. Better Harness did not classify that custom command as a check. This path must not be used as Portable Planner failure evidence.

## Decision changed

- Add a current issue for the post-validation mutation boundary rather than broadening I-05 or I-07 beyond their evidence.
- Search external mechanisms only for last-write/final-validation ordering, invalidation, and handoff gating.
- Implement no change until the minimum replay fails on beta 7 and the selected correction is smaller than a project-specific validation system.

## GITBUTT mechanism search

Search date: 2026-08-19

The local read-only GITBUTT catalog was searched for last-write validation, checkpoint invalidation, and handoff gates. It surfaced three useful mechanism families:

- [Optim Plans](https://github.com/Optim-Agent/optim-plans) separates immutable run identity from append-only events and derives current state by replay. It also keeps an explicit planning-to-execution handoff. Portable Planner does not need that controller, but the relevant invariant is that accepted state is tied to an ordered point in history rather than covering later events.
- [Everything Claude Code / ECC](https://github.com/affaan-m/ECC) demonstrates checks triggered after file edits, including formatting and a TypeScript check. Portable Planner must remain host-portable, so it adopts the ordering principle rather than a host-specific hook.
- [dbosify-py](https://github.com/dbos-inc/dbosify-py) represents durable checkpointed workflow machinery backed by Postgres. That is disproportionate to a Markdown skill and is rejected.

Selected adaptation: treat the last planning-file mutation as the proof boundary. A completion, final review, testing/build transition, or handoff requires reconciliation plus the cheapest relevant check after that mutation. A later mutation invalidates both. No-write replies create no new proof obligation.

This remains one canonical-skill rule plus validation evidence. It adds no runtime, hook, state file, service, database, role, or domain-specific behavior.

## Minimum replay result

The sanitized beta-7 event order is:

`planning write -> relevant check -> material late planning write -> handoff`

The domain-neutral replay in `validation/final-write-barrier/` rejects that order in both software and non-software cases. It accepts the repaired order only when reconciliation and a relevant check follow the last write, and it accepts no-write and ordinary non-terminal replies without adding a check. This confirms the narrow failure boundary and the intended low-ceremony correction; it does not replace a later fresh-session behavioral test after an authorized candidate installation.
