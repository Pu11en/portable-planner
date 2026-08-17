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
    M6["DONE · 6 · Compare and protect"]
    M7(["NOW · HUMAN · 7 · Judge fresh task"])
    M1 --> M2 --> M3 --> M4 --> M5 --> M6 --> M7

    classDef current stroke-width:3px,font-weight:700;
    classDef milestone stroke-width:2px;
    classDef proof stroke-width:3px,font-weight:700;
    class M7 current;
    class M1,M2,M3,M4,M5,M6 milestone;
```

**Text route:** DONE · 1 · Recover evidence → DONE · 2 · Inventory nine issues → DONE · 3 · Select focus-lens route → DONE · 4 · Freeze six claims → DONE · 5 · Implement candidate → DONE · 6 · Compare and protect → NOW · HUMAN · 7 · Judge fresh task

## Focus lens

- **Current outcome:** E-020 determines whether the objectively passing candidate actually gives Drew a shorter, equally complete, and more pleasing first read.
- **Next action:** Open one new Codex task in this repository and paste the exact natural continuation prompt from `NEXT.md`.
- **Human role:** Judge the uncoached visible first read as `better`, `same`, or `worse` than beta 6.
- **Proof:** The fresh task preserves destination, journey, current outcome, next action, human role, proof, and recovery without requiring a report, expansion, or file link.
- **Recovery:** On `same`, `worse`, or a hard failure, restore the verified beta-6 cache immediately and reopen only I-01.

## Quiet rail

- **Remaining:** Drew's E-020 verdict · then I-02 through I-09 one issue at a time only if I-01 wins
- **Guardrails:** Raw histories stay local · no arbitrary run count · no second state tree · no renderer or app · no publication from objective proof alone · beta 6 wins ties

## Optional detail

<details>
<summary>E-020 acceptance boundary</summary>

- Outcome: one better/same/worse verdict from the exact installed candidate
- Owner: Drew
- Inputs: this real plan, a fresh task, and the natural continuation prompt
- Proof: preserved visible first read plus Drew's direct judgment
- If blocked or changed: restore beta 6 and preserve the first concrete failure

</details>

Details: [plan](PLAN.md) · [current ticket](execution/E-020-run-i01-human-acceptance.md) · [objective evidence](../validation/I01-CANDIDATE-TEST.md)
