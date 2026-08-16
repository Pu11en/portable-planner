# Make Portable Planner diligent before it acts

**Status:** planning

**Destination:** Portable Planner recognizes when an outcome is still being shaped, helps Drew and the agent reach the same understanding, and makes even a large plan genuinely comprehensible before implementation or testing runs ahead.

**Success:** Improvement problems are listed before solutions; each problem is solved and proved separately; a large plan reveals destination, current position, next action, important gates, and relevant detail without forcing Drew through Mermaid or a report; and a worse version is never left installed.

**Now:** Judge one polished Journey plus focus lens prototype using this plan's real state.

**Next:** Lock the structure or make one targeted revision, then test the faithful candidate on an actual large plan.

```mermaid
flowchart TB
    G(["DESTINATION · A measurably better Portable Planner"])

    subgraph R1["UNDERSTAND"]
        direction LR
        E["01 · Evidence<br/>DONE"] --> I["02 · Nine issues<br/>DONE"] --> C{{"03 · Plan clarity<br/>NOW"}} --> P["04 · Faithful prototype"]
    end

    subgraph R2["PROVE"]
        direction LR
        B["05 · Compare with beta 6"] --> H(["06 · HUMAN<br/>Real-plan judgment"]) --> W(["07 · Keep the winner"])
    end

    L["FOCUS · I-01 PLAN COMPREHENSION<br/><br/>NEXT · Lock or revise this first-read structure<br/>HUMAN · Judge clarity and visual appeal<br/>PROOF · Goal, now, next, gate and recovery are obvious<br/>RECOVERY · Beta 6 remains untouched"]

    Q["ISSUE RAIL · NEXT I-02–04 · VERIFY I-05 & I-07 · PROTECT I-06 & I-08 · METHOD I-09"]

    G --> E
    C --> L
    P --> B
    L --- Q

    classDef done stroke-width:1.5px;
    classDef current stroke-width:4px,font-weight:700;
    classDef protected stroke-width:3px,font-weight:700;
    classDef quiet stroke-width:1px,stroke-dasharray:4 3;
    class E,I done;
    class C,L current;
    class H,W protected;
    class Q quiet;
```

**Text route:** DONE recover real-session evidence → DONE inventory nine issues → NOW lock or revise the polished I-01 prototype → build one faithful candidate → compare with beta 6 → HUMAN judge it on a real large plan → keep the winner

## Confirmed boundary and current decision

Example boundaries:

- “What does 30 runs mean?” receives a direct explanation; it does not create a new planning route.
- “We need to improve Portable Planner, but I do not trust the proposed tests” automatically starts or resumes planning.
- “Implement the already approved E-010 ticket” uses the normal build workflow.

The confirmed boundary is unresolved project/product work: planning activates when destination, scope, success, proof, or a meaningful human tradeoff is still being negotiated. Narrow facts, status, explanation, diagnosis-only work, and sufficiently specified builds remain direct.

There is no current human-owned test-count or renderer decision. The [improvement inventory](evidence/P-002-improvement-issues.md) defines nine problems or regression constraints. [I-01 research](evidence/P-002-I-01-plan-comprehension.md) preserves the rejected variants, selected Journey plus focus lens composition, four-case directional pass, and polished faithful prototype contract. Implementation waits for Drew's judgment of this first-read structure.

## Plan-wide safety

- The former 30-run allocation is withdrawn.
- Real session evidence and explicit behavior claims come before authored prompts.
- Raw Codex/ZCode transcripts remain local, private, read-only, and untracked.
- Historical cases replace full synthetic conversations; only selected decision points are replayed when a candidate needs counterfactual proof.
- Mermaid rendering is not accepted as proof of comprehension; the solution must work on an actual large plan.
- Solve one confirmed issue at a time and preserve objectively passing behaviors as regression guards.
- Each test has an exact starting state, expected route, prohibited behavior, and human judgment.
- Repetition requires observed variance or protected high risk.
- Expert skills and outside mechanisms supply selective evidence, not product authority; Portable Planner's protocol and cross-domain scope remain its own.
- Beta 5 and beta 6 remain immutable and recoverable.

Details: [plan](PLAN.md) · [current decision](decisions/P-002-engineer-the-improvement-loop.md) · [improvement inventory](evidence/P-002-improvement-issues.md) · [I-01 comprehension research](evidence/P-002-I-01-plan-comprehension.md) · [historical corpus](evidence/P-002-test-inventory.md)
