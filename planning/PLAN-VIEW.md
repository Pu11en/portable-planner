# Make Portable Planner decisive and brief

**Status:** approved for build

**Destination:** Short, decisive planning that stops grilling when discussion is exhausted, then proactively moves finished work into approval and live testing while preserving human control.

**Success:** Fresh varied sessions prove delegated choices proceed without extra questions, bounded trials replace unproductive discussion, and the planner clearly pushes completed work into approval and the right live test without crossing protected gates.

**Now:** E-001 through E-008 are complete. The exact beta-6 shortcut passes its affected behavior, state, natural-invocation, and package checks; E-009 is publishing it.

**Next:** Publish and install beta 6, then Drew runs the exact real-project acceptance test in a new task.

```mermaid
flowchart LR
    H["DONE · HUMAN approved plan"]
    E1["DONE · Lock behavior contract"]
    E2["DONE · Update canonical skill"]
    E3["DONE · Prove varied behavior"]
    E4["DONE · Live failures captured"]
    E5["DONE · Repair shared behavior"]
    E6["DONE · Rerun release checks"]
    E7["DONE · Integrate prerelease"]
    E8["DONE · Exact option-B shortcut"]
    E9(["NOW · Publish beta 6"])
    D["HUMAN · Real-project acceptance"]
    H --> E1 --> E2 --> E3 --> E4 --> E5 --> E6 --> E7 --> E8 --> E9 --> D

    classDef current stroke-width:3px,font-weight:700;
    classDef milestone stroke-width:2px;
    classDef proof stroke-width:3px,font-weight:700;

    class E9 current;
    class H,E1,E2,E3,E4,E5,E6,E7,E8,D milestone;
```

**Text route:** HUMAN approved plan → DONE beta-5 route → DONE exact bare-key option-`B` shortcut → NOW publish passing beta 6 → HUMAN run the real-project acceptance test.

## Step details

<details>
<summary>DONE · HUMAN approved plan</summary>

- Outcome: Building is explicitly authorized.
- Owner: Drew.
- Inputs: Finished plan, confirmed decision, and evidence.
- Proof: Drew explicitly approved on 2026-08-07.
- If blocked or changed: Reopen only the affected decision.

</details>

<details>
<summary>DONE · E-001 · Lock behavior contract</summary>

- Outcome: Product and acceptance documents define the new behavior consistently.
- Owner: Agent.
- Inputs: P-001 and recorded live failures.
- Proof: Authority documents agree without claiming proven effectiveness.
- If blocked or changed: Return conflicting product tradeoffs to planning.

</details>

<details>
<summary>DONE · E-002 · Update canonical skill</summary>

- Outcome: One skill implements brevity, explicit delegation, stopping, bounded trials, immediate action, proactive approval and test handoffs, and protected gates.
- Owner: Agent.
- Inputs: Locked behavior contract.
- Proof: References resolve and adapters remain thin.
- If blocked or changed: Record the instruction failure before adding architecture.

</details>

<details>
<summary>DONE · E-003 · Prove varied behavior</summary>

- Outcome: Normal, contrasting, and failure cases pass across software and non-software planning.
- Owner: Agent.
- Inputs: Updated canonical skill and fixtures.
- Proof: Preserved inputs, outputs, variations, failures, and changed decisions.
- If blocked or changed: Make a targeted revision and rerun affected cases.

</details>

<details>
<summary>DONE · E-004 · HUMAN live acceptance</summary>

- Outcome: A genuine fresh session preserved both passing behavior and concrete failures.
- Owner: Shared.
- Inputs: Passing package and an ordinary fresh request.
- Proof: Drew's direct judgments and the preserved beta.4 trace.
- If blocked or changed: Reopen only the affected shared behavior.

</details>

<details>
<summary>DONE · E-005 · Repair shared behavior</summary>

- Outcome: Fix delegation invitation, digression choices, provisional research direction, test intake, visual freshness, and fallback behavior in the one canonical skill.
- Owner: Agent.
- Inputs: Recorded beta.4 failures and Drew's confirmed corrections.
- Proof: Product and skill contracts agree without domain-specific instructions or new architecture.
- If blocked or changed: Return only a genuinely new product tradeoff to planning.

</details>

<details>
<summary>DONE · E-006 · Rerun release checks</summary>

- Outcome: Fresh affected cases and full package checks pass on the unchanged repaired candidate.
- Owner: Agent.
- Inputs: E-005 candidate and preserved failure assertions.
- Proof: Raw outputs, package validation, link/state audits, installer proof, and honest acceptance reconciliation.
- If blocked or changed: Repair only the failed shared instruction and rerun affected cases.

</details>

<details>
<summary>DONE · E-007 · Integrate prerelease</summary>

- Outcome: Reviewed changes reach remote `main`, a matching tag, and a GitHub prerelease.
- Owner: Agent; Drew supplies remaining post-install human acceptance.
- Inputs: Passing E-006 candidate.
- Proof: Remote hashes, merged PR, tag, release, clean worktree, and explicit remaining gates.
- If blocked or changed: Push the branch and record the exact release blocker without a false production claim.

</details>

<details>
<summary>DONE · E-008 · Exact option-B shortcut</summary>

- Outcome: Only bare recommended keys build the streak; the next real question inserts delegation as `B` while preserving its recommendation as `A`.
- Owner: Agent.
- Inputs: Drew's exact 2026-08-15 interaction rule and the beta-5 canonical skill.
- Proof: Product authority, skill guidance, durable state, templates, and acceptance agree without inferred delegation.
- If blocked or changed: Return only a genuinely ambiguous safety boundary to Drew.

</details>

<details open>
<summary>NOW · E-009 · Validate and publish beta 6</summary>

- Outcome: Positive, reset, resumption, protected-gate, package, and natural-invocation checks pass before beta 6 is published and installed.
- Owner: Agent.
- Inputs: Unchanged E-008 candidate.
- Proof: Preserved release-candidate evidence, remote main/tag/release agreement, public plugin installation, and exact human test instructions.
- If blocked or changed: Repair only the failed shared instruction and rerun affected cases.

</details>

<details>
<summary>HUMAN · Real-project acceptance</summary>

- Outcome: Drew confirms the shortcut appears at the right moment, delegates only through bare `B`, and stops at final approval.
- Owner: Drew.
- Inputs: Installed public beta 6 and the durable human test runbook.
- Proof: Actual fresh-task trace recorded against C-02, C-12, and C-13.
- If blocked or changed: Record the exact failure and reopen only its shared behavior.

</details>

## Plan-wide safety

- Never infer delegation from repeated agreement.
- Never delegate irreversible commitments, personal tradeoffs, conflicts, implementation, or final approval.
- Trials are planning evidence, not production work.
- Keep one canonical skill and one project-local planning state.
- Record live failures before architecture expands.
- Keep ordinary replies short; reveal details only when requested or required for safety.

Details: [plan](PLAN.md) · [confirmed decision](decisions/P-001-define-decisive-planning.md)
