# Make Portable Planner diligent before it acts

**Status:** planning

**Destination:** Portable Planner recognizes when an outcome is still being shaped, helps Drew and the agent reach the same understanding, and makes even a large plan genuinely comprehensible before implementation or testing runs ahead.

**Success:** Each improvement starts from a named real failure, preserves already-good behavior, and passes objective checks plus Drew's fresh-session judgment before it can replace beta 6.

## Journey

```mermaid
flowchart LR
    M1["DONE · 1 · Recover evidence"]
    M2["DONE · 2 · Inventory nine issues"]
    M3["DONE · 3 · Select focus-lens route"]
    M4["DONE · 4 · Freeze six claims"]
    M5["DONE · 5 · Implement candidate"]
    M6(["NOW · 6 · Compare and protect"])
    M7(["HUMAN · 7 · Judge fresh task"])
    M1 --> M2 --> M3 --> M4 --> M5 --> M6 --> M7

    classDef current stroke-width:3px,font-weight:700;
    classDef milestone stroke-width:2px;
    classDef proof stroke-width:3px,font-weight:700;
    class M6 current;
    class M1,M2,M3,M4,M5 milestone;
    class M7 proof;
```

**Text route:** DONE · 1 · Recover evidence → DONE · 2 · Inventory nine issues → DONE · 3 · Select focus-lens route → DONE · 4 · Freeze six claims → DONE · 5 · Implement candidate → NOW · 6 · Compare and protect → HUMAN · 7 · Judge fresh task

## Focus lens

- **Current outcome:** E-019 determines whether the unchanged candidate preserves all six I-01 claims and beta-6 behavior.
- **Next action:** Run the package, fidelity, state-refresh, and affected beta-6 regression checks against one candidate commit.
- **Human role:** None during objective comparison; Drew owns the fresh-session comprehension judgment only if the candidate is eligible.
- **Proof:** Six attributable claim results and all affected regressions pass with candidate/reference bytes recorded.
- **Recovery:** Reject the candidate on a hard failure; leave beta 6 installed and recoverable, and do not begin I-02.

## Quiet rail

- **Remaining:** E-020 fresh acceptance · then I-02 through I-09 one issue at a time
- **Guardrails:** Raw histories stay local · no arbitrary run count · no second state tree · no renderer or app · no publication from objective proof alone · beta 6 wins ties

## Optional detail

<details>
<summary>E-019 comparison boundary</summary>

- Outcome: one eligible-or-rejected verdict from fixed candidate bytes
- Owner: agent
- Inputs: frozen F-01 through F-06 fixtures, canonical skill, beta-6 evidence
- Proof: preserved validation report linked to the candidate commit
- If blocked or changed: reject or return the exact unexpressible assertion to planning

</details>

Details: [plan](PLAN.md) · [current ticket](execution/E-019-compare-i01-candidate.md) · [I-01 evidence](evidence/P-002-I-01-plan-comprehension.md)
