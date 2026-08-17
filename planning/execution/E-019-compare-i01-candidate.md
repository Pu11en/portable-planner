# E-019 — Compare the I-01 candidate and protect beta 6

- Status: current — candidate implementation complete; objective checks pending
- Depends on: E-018

## Outcome

The unchanged candidate passes all six I-01 claims and preserves beta-6 behavior, or it is rejected with beta 6 remaining the proven reference.

## Context

- [Frozen fidelity contract](E-017-freeze-i01-fidelity-contract.md)
- [Candidate implementation](E-018-implement-focus-lens-candidate.md)
- Immutable reference: `v0.1.0-beta.6`

## In scope

- Run F-01 through F-06 once each from fresh fixture state and preserve exact output, canonical state, candidate commit, and assertion result.
- Run the existing beta-6 package, natural-invocation, bare-key/delegation, protected-gate, approval, and resumption regression checks against unchanged candidate bytes.
- Verify one material state advance regenerates current, next, focus lens, and text route together.
- Give exactly one verdict: `candidate eligible for human test` or `candidate rejected`.

## Out of scope

- Rewriting assertions after output, additional tuning rounds, publishing, or treating objective fidelity as human comprehension proof.

## Constraints

- Stop on canonical-state, authority, approval, stale-view, or attribution failure.
- One pass per distinct claim is the default; repeat only an observed variable case and record why.
- Worse or inconclusive results favor beta 6. A losing candidate never reaches `main` or the active public installation.

## Proof

- Six attributable claim results and the existing regression results link to preserved outputs.
- Mermaid/text parity, state freshness, and lifecycle/authority assertions pass.
- Candidate and reference bytes are unambiguous and beta 6 remains recoverable.

## If blocked or disproven

- Preserve the exact failure, reject or narrowly repair the candidate through planning, and keep or restore beta 6. Do not expand the run count to force a pass.

## Human review

- None for the objective verdict; an eligible candidate still requires E-020.

## Next eligible ticket

- E-020 — Run one fresh real-session acceptance, or stop with beta 6 if rejected.
