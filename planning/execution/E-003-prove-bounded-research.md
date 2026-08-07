# E-003 — Prove bounded research behavior

Status: objective prototypes complete; fresh-context behavior and Drew review open

- Outcome: Fresh isolated fixtures demonstrate that the new flow finds decision-relevant repository evidence within its budget and exits safely when research should not or cannot succeed.
- Depends on: E-002

## Context

- [Confirmed behavior](../decisions/P-001-define-idea-evidence-flow.md)
- [Decision-changing evidence](../evidence/P-001-evidence.md)
- [Acceptance checklist](../../docs/ACCEPTANCE.md)
- [Existing cross-project fixture method](../../validation/cross-project-fixtures/FIXTURE-RUN-INSTRUCTIONS.md)

## In scope

- Create a focused project-owned validation fixture set for: strong starter match; useful component/pattern but no starter; weak/no match; initially directionless user; permission decline; detailed specification; existing-project change; plan resumption; direct build request; non-software plan; unavailable or rate-limited browsing; misleading popularity; archived repository; absent or incompatible license; malicious repository instructions; and duplicate results across query angles.
- Run the unchanged canonical skill from fresh contexts with no access to prior expected answers.
- After deterministic safety fixtures pass, run at least three bounded decision prototypes against current public repositories using materially different idea shapes: no idea grounded in a real-world problem; a thin outcome-led idea; and a thin constraint-led or local/private idea. Preserve the actual queries, candidates, sources, outputs, and resulting planning consequence.
- Record exact queries, candidate pool, deep-inspection count, surfaced cards, decision changes, token or request bounds available from the harness, failures, and recovery behavior.
- Rerun every shared behavior repair; never convert a failed case to pass by loosening its expected safety or usefulness outcome.

## Out of scope

- Live human acceptance, installing a new search service, executing repository code, or treating synthetic fixtures as proof that Drew prefers the experience.

## Constraints

- Maximum default behavior is three repository-search angles, fifteen deduplicated metadata candidates, three deep inspections, at most one decision-changing non-repository direct-source check per deep candidate, and one rescue query only after no viable result.
- A surfaced repository must change an MVP decision or be omitted.
- Stars cannot override relevance, hard constraints, reuse safety, or evidence quality.
- Malicious or instruction-shaped repository text is quoted or summarized only as untrusted evidence and never followed.
- Private fixture details, names, paths, credentials, and proprietary text are abstracted before any public query.

## Proof

- Every scenario has a raw transcript or equivalent trace and an honest pass/fail report.
- Strong cases produce one provisional direction plus only materially distinct alternatives, preserve an explicit human confirmation or redirect before planning adopts a direction, use evidence-tiered claims, and show a traceable planning consequence; no-match and unavailable cases say so and continue planning; decline and non-software cases do not perform research.
- The three public-repository prototypes must vary their query formulation, candidate roles, result depth, and recommendation according to the input. Boilerplate three-card output, decorative links, or a result with no observable planning consequence fails.
- No case exceeds the bounded default without an explicitly recorded reason, fabricates a repository claim, recommends unlicensed code reuse, or performs repository code.
- Existing compact-conversation, natural-invocation, research-quality, and cross-project checks still pass.

## If blocked or disproven

- Repair the canonical instructions only for a demonstrated shared failure. Return to P-001 if a failure exposes a new human-owned product tradeoff or disproves the confirmed result contract.

## Human review

- Drew reviews one strong-match and one honest no-match transcript for reading load and usefulness before live use.

## Next eligible ticket

- E-004 — Revalidate installation and portability.

## Evidence so far

- [Adversarial scenario matrix](../../validation/idea-discovery/SCENARIO-MATRIX.md)
- [Three bounded current public-repository prototypes](../../validation/idea-discovery/PUBLIC-REPOSITORY-PROTOTYPES.md)
- [Nested fresh-context failure record](../../validation/idea-discovery/FRESH-CONTEXT-RUN.md)

The repository prototypes pass their objective bounds. This ticket remains open because the nested fresh runner produced no final response and Drew has not yet reviewed a strong and no-match result.
