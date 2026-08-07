# Prove the idea-stage possibility scan

Type: implementation and validation
Status: approved, not yet proven
Blocked by:

## Question

Can Portable Planner help a person with no product idea or a thin software/AI idea understand plausible, evidence-backed directions and the fastest credible MVP route without adding ceremonial intake, unsafe repository use, excessive research, or a competing product/build system?

## Confirmed behavior

- Gate only new no-idea or thin-idea software/AI planning; skip detailed specifications, existing-project changes, resumed plans, and direct build requests.
- Ask once whether to scan or skip. With consent, derive a privacy-safe one-sentence brief from a real-world anchor and ask only search-critical gaps one at a time.
- Search no more than three repository angles, shortlist no more than fifteen candidates, and deeply inspect no more than three without cloning, installing, or executing code.
- Return one provisional recommendation and at most two materially different alternatives. Use evidence-tier claims, conservative license language, and explicit human confirmation before plan adoption.
- Fail honestly into ordinary planning without requiring an account, API client, MCP server, database, cloud dependency, or new runtime.

The current normative behavior is in the canonical [idea-discovery reference](../../plugins/portable-planner/skills/portable-planner/references/idea-discovery.md), supported by the [scenario matrix](../../validation/idea-discovery/SCENARIO-MATRIX.md) and repository-prototype evidence.

## Work route

1. Re-run the varied repository scenario matrix against the current canonical skill.
2. Revalidate package and cross-harness behavior without adding architecture.
3. Run Drew's uncoached fresh-session idea-stage use and record any correction loop.

## Acceptance

This issue resolves only when [I-01 through I-05](../../docs/ACCEPTANCE.md#idea-stage-possibility-scan) pass with linked evidence. Authored examples, implementation simulations, and the planning decision itself do not count as Drew's live proof.
