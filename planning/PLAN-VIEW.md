# Make Portable Planner measurably better

**Status:** awaiting approval

**Destination:** Portable Planner chooses the right next planning action with less user effort, proves beta 6 did not make shared behavior worse than beta 5, and accepts a later revision only when it beats the better proven reference without weakening safety, authority, or durable state.

**Success:** Beta 5 and beta 6 receive a fair shared-behavior comparison; the better version becomes the reference. A later candidate fixes one demonstrated failure, keeps every hard gate perfect, avoids material non-target regression, passes Drew's uncoached test, and restores the winning reference automatically after any failure.

**Now:** Option A and the complete bounded execution route are ready for Drew's approval.

**Next:** After explicit approval, begin E-010 and preserve both `v0.1.0-beta.5` and `v0.1.0-beta.6` as immutable controls.

```mermaid
flowchart LR
    CTRL["SAFE · Immutable beta 5 + beta 6"]
    A(["NOW · HUMAN approve route"])
    K["E-010 · Decision kernel"]
    H["E-011 · Frozen eval harness"]
    M{"E-012 · 18-run control"}
    REF["Winning reference"]
    C["E-013 · One candidate change"]
    V{"E-014 · Better?"}
    T["E-015 · HUMAN fresh test"]
    R(["E-016 · Proven release"])
    KEEP["REJECT · Keep/restore reference"]
    CTRL --> A --> K --> H --> M
    M -->|beta 6 preserved| REF
    M -->|beta 6 regressed; restore beta 5| REF
    REF --> C --> V
    V -->|yes| T -->|pass| R
    V -->|worse or unclear| KEEP
    T -->|fail or worse| KEEP

    classDef current stroke-width:3px,font-weight:700;
    classDef milestone stroke-width:2px;
    classDef proof stroke-width:3px,font-weight:700;
    classDef blocked stroke-width:3px;

    class A current;
    class CTRL,K,H,M,REF,C,T milestone;
    class V,R proof;
    class KEEP blocked;
```

**Text route:** SAFE immutable beta 5 + beta 6 → NOW HUMAN approve → define the decision kernel → freeze the evaluation harness → compare shared behavior in eighteen control runs → if beta 6 regressed, restore beta 5; otherwise keep beta 6 → use the winning version as the reference → make at most one targeted candidate change → compare with twelve candidate runs → if worse or unclear, reject and keep/restore the reference → if objectively better, HUMAN fresh test → on failure restore the reference; on pass publish the proven prerelease

## Step details

<details open>
<summary>NOW · HUMAN approve the route</summary>

- Outcome: The bounded experiment and rollback policy receive explicit build authorization.
- Owner: Drew.
- Inputs: [confirmed decision](decisions/P-002-engineer-the-improvement-loop.md), [expert evidence](evidence/P-002-expert-engineering-evidence.md), and E-010 through E-016.
- Proof: Direct approval changes lifecycle state to `approved for build` and makes E-010 eligible.
- If blocked or changed: Reopen only P-002; both released tags remain untouched and the current public installation remains unchanged.

</details>

<details>
<summary>E-010 · Define the decision kernel</summary>

- Outcome: One normative contract covers prerequisites, ownership, legal actions, state mutation, and protected gates.
- Owner: Agent.
- Inputs: P-002, expert evidence, current canonical references.
- Proof: Every current behavior class maps to one non-conflicting transition and deterministic invariant set.
- If blocked or changed: Return an unresolved ownership or safety tradeoff to planning; add no infrastructure.

</details>

<details>
<summary>E-011 · Freeze the evaluation harness</summary>

- Outcome: Six visible and two held-out scenarios run from fresh isolated state with exact trace capture.
- Owner: Agent.
- Inputs: Decision kernel and existing fixtures.
- Proof: Corpus hashes, objective validators, judgment rubric, version attribution, isolation, and early stop all pass before baseline work.
- If blocked or changed: Use exact manual runs rather than weakening evidence integrity.

</details>

<details>
<summary>E-012 · Compare beta 5 and beta 6</summary>

- Outcome: Eighteen unchanged fresh-task runs establish whether beta 6 preserved beta 5's shared behavior and name the better proven reference.
- Owner: Agent.
- Inputs: Immutable `v0.1.0-beta.5`, immutable `v0.1.0-beta.6`, and the frozen harness.
- Proof: All six visible scenarios run once on each version; the three highest-risk shared scenarios repeat once on each. Beta-6-only behavior is scored separately so beta 5 is not penalized for lacking the new shortcut.
- If blocked or changed: A hard or material shared-behavior regression restores beta 5 from its immutable release before candidate work. If no meaningful failure appears, make no candidate and take the winning reference to human acceptance.

</details>

<details>
<summary>E-013 · Make one candidate change</summary>

- Outcome: One isolated branch receives the smallest causal correction to the selected failure.
- Owner: Agent.
- Inputs: Control report, winning reference, and pre-registered assertion.
- Proof: Minimal diff, static/package proof, and a written causal claim exist before candidate runs.
- If blocked or changed: Return to planning rather than add a second skill, state tree, service, or broad rewrite.

</details>

<details>
<summary>E-014 · Compare, keep, or reject</summary>

- Outcome: Twelve candidate runs produce exactly one objective verdict.
- Owner: Agent.
- Inputs: Affected cases, unrelated regression cases, held-out cases, and baseline run ranges.
- Proof: Zero hard failures, consistent target fix, no new held-out missed decision, and no material non-target regression are required to keep the candidate.
- If blocked or changed: Worse or inconclusive means reject; do not merge or spend more runs to force a pass.

</details>

<details>
<summary>E-015 · HUMAN fresh acceptance</summary>

- Outcome: Drew judges the objectively passing candidate in one new uncoached task.
- Owner: Drew; agent controls installation and rollback.
- Inputs: Kept candidate, verified temporary installation, and dedicated empty test project.
- Proof: Exact visible trace plus Drew's speed, question-value, usefulness, and “nothing worse” verdict.
- If blocked or changed: Immediately reinstall and verify the winning beta-5/beta-6 reference; reject the candidate.

</details>

<details>
<summary>E-016 · Publish only the proven candidate</summary>

- Outcome: A human-passed candidate alone reaches `main`, tag, prerelease, marketplace, and public installation.
- Owner: Agent.
- Inputs: Objective comparison and human acceptance.
- Proof: Source, remote main, tag, release, marketplace, installed bytes, validators, and evidence agree.
- If blocked or changed: Restore the winning reference and report the release blocker without changing quality claims.

</details>

## Plan-wide safety

- `v0.1.0-beta.5` and `v0.1.0-beta.6` are immutable and permanently recoverable.
- Establish the winning beta-5/beta-6 reference before changing the skill.
- One demonstrated failure class permits one candidate change.
- Thirty automated fresh-task runs is the first-cycle ceiling: eighteen control runs plus twelve candidate runs.
- Worse or inconclusive means reject; safety failures stop immediately.
- A temporary human-test failure restores the winning reference before handoff.

Details: [plan](PLAN.md) · [confirmed decision](decisions/P-002-engineer-the-improvement-loop.md)
