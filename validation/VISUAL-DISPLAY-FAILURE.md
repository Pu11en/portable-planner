# Visual Display Failure

Date: 2026-08-05

## Observed failure

The first interactive Hanoi HTML view rendered during local inspection but the Codex in-session visualization surface returned `An error occurred inside the visualization`. The response therefore failed its actual delivery test even though the local file looked correct.

## Exact diagnosis

After the minimal fragment failed, Codex exposed the underlying error:

```text
Error: ENOENT: no such file or directory, lstat '\\wsl.localhost\Ubuntu\home\drewp\.codex\visualizations\2026\08\05\019fd2af-654e-78b0-81dd-b451b66ce60a\visual-host-test.html'
```

The directive resolved relative to the WSL Codex home at `/home/drewp/.codex/visualizations/...`, but the files had been written under the Windows-mounted path `/mnt/c/Users/drewp/.codex/visualizations/...`. Local Chromium succeeded because it opened the Windows-mounted file directly; the Codex host failed before parsing any HTML because its resolved WSL file did not exist.

This is the exact immediate cause. The graph HTML and JavaScript were never loaded by the in-session host, so they cannot be blamed for this failure.

Primary-source research in `wiki/research/PORTABLE-PLAN-VISUALS.md` establishes the architectural cause: Agent Skills standardize instructions and bundled resources, not popups, artifact panes, inline HTML, or rendering. The `::codex-inline-vis` channel is a Codex-surface contract, not a portable Agent Skills feature.

The original graph still has several independent contract issues worth correcting before reuse: SVG links acted as controls instead of native buttons, the narrow layout introduced horizontal scrolling, and the interaction was denser than the installed Visualize guidance recommends. Those are product-quality issues, not the cause of this `ENOENT` failure.

## Fix

Write the fragment to the exact thread directory under the active WSL Codex home before emitting the filename-only directive. Do not infer the runtime visualization root from a similarly named Windows-mounted directory.

The repaired minimal fragment now exists at the exact path from the error. Its real in-session render remains the completion check.

## Pass condition

The exact failing layer is isolated in the real Codex session; the corrected Hanoi graph is visible there; and the chosen cross-harness presentation architecture passes on Codex plus one non-Codex harness without changing canonical plan state.

## Fresh-context completion failure

After the recommendation-first revision, a fresh Codex CLI context completed the fully specified YouTube question-finder plan under `validation/simple-completion-forward-20260805/`. It correctly generated canonical state, official-source evidence, `PLAN-VIEW.md`, and eight execution tickets, then stopped at `awaiting approval` without building.

Its entire user-facing completion turn was:

```text
Plan complete. The finish audit passed; eight session-sized execution tickets are ready.

Review PLAN-VIEW.md. Status remains awaiting approval. Nothing was approved or implemented.
```

This is failure **F-004**. The route was not visible in the session and no explicit approval question was asked. Linking the file is navigation, not display.

The contract now requires every automatic display turn to contain the actual rich graph, rendered Mermaid, or complete compact text route. The completion turn must also ask one explicit approval question while status remains `awaiting approval`. A fresh-context resume of the same unchanged plan must prove the repair.

## Fresh-context completion rerun

A new Codex CLI context received only the revised canonical skill, the unchanged completed planning folder, and the natural request `Continue my plan.` It loaded canonical state, rendered the complete eight-step Mermaid route directly in its user-facing reply, summarized the six plan-wide protections, and asked one explicit approval question with `A` as the recommendation. It did not alter `awaiting approval` or perform implementation.

**F-004 result: PASS.** The raw unchanged plan remains under `validation/simple-completion-forward-20260805/`. This proves the Markdown/Mermaid in-session path and fresh-session approval-gate recovery; it does not yet prove the richer Codex Desktop interactive surface or non-Codex display.
