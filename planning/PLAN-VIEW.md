# Make Portable Planner diligent before it acts

**Status:** planning

**Destination:** Portable Planner recognizes when an outcome is still being shaped, helps Drew and the agent reach the same understanding, and makes even a large plan genuinely comprehensible before implementation or testing runs ahead.

**Success:** Improvement problems are listed before solutions; each problem is solved and proved separately; a large plan reveals destination, current position, next action, important gates, and relevant detail without forcing Drew through Mermaid or a report; and a worse version is never left installed.

**Now:** Test the selected Journey plus focus lens composition across four materially different plan states.

**Next:** Replace the superseded draft execution route with the approved implementation and comparison sequence.

```mermaid
flowchart LR
    E["DONE · Recover real session history"]
    I["DONE · List nine improvement issues"]
    F["FAILED · Image and plain-view detours"]
    C["DONE · Select Journey + focus lens"]
    M{"NOW · Test four dynamic scenarios"}
    H(["HUMAN · Judge comprehension and appeal"])
    B["Refine only a demonstrated failure"]
    X["Prototype on a real large plan"]
    R(["PROOF · Keep/restore winner"])
    E --> I --> F --> C --> M --> H --> B --> X --> R

    classDef current stroke-width:3px,font-weight:700;
    classDef milestone stroke-width:2px;
    classDef proof stroke-width:3px,font-weight:700;
    class M current;
    class E,I,F,C,B,X milestone;
    class H,R proof;
```

**Text route:** DONE recover real-session evidence → DONE list nine improvement issues → FAILED image and plain/expansion-dependent views → DONE select Journey plus focus lens → NOW test current, early, complex, and failure states → HUMAN judge comprehension and appeal → refine only a failing behavior → prototype on a real large plan → keep beta 6 or prove the candidate

## Confirmed boundary and current decision

Example boundaries:

- “What does 30 runs mean?” receives a direct explanation; it does not create a new planning route.
- “We need to improve Portable Planner, but I do not trust the proposed tests” automatically starts or resumes planning.
- “Implement the already approved E-010 ticket” uses the normal build workflow.

The confirmed boundary is unresolved project/product work: planning activates when destination, scope, success, proof, or a meaningful human tradeoff is still being negotiated. Narrow facts, status, explanation, diagnosis-only work, and sufficiently specified builds remain direct.

There is no current human-owned test-count or renderer decision. The [improvement inventory](evidence/P-002-improvement-issues.md) defines nine problems or regression constraints. [I-01 research](evidence/P-002-I-01-plan-comprehension.md) preserves the rejected variants, selected Journey plus focus lens composition, and four-case dynamic trial. Implementation waits for Drew's concrete reaction to those in-session cases.

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
