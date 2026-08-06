# Portable Planner contributor guide

This repository is a public-preview experiment. Do not describe the planning
experience as proven until the live acceptance checklist passes.

The one canonical skill is:

```text
plugins/portable-planner/skills/portable-planner/
```

Project ownership also lives here:

- `docs/` owns the goal, product contract, MVP plan, and acceptance checklist.
- `project-map/` owns the remaining-work map and its issues.
- `validation/` and `pilots/` contain evidence, fixtures, and real-use records.

Harness manifests and installer code must remain thin adapters. Do not create a
second skill copy, database, MCP server, web app, cloud dependency, domain pack,
or build-mode framework without a recorded failed validation that requires it.

Before publishing a change:

1. Validate the canonical skill and Codex plugin manifest.
2. Confirm every referenced file and template exists.
3. Test natural-language invocation from a fresh session.
4. Preserve project-local `planning/` state unchanged across resumption.
5. Record live failures before expanding architecture.

Keep Portable Planner product state in this repository. The AI-course workspace may
link to this project, but it must not hold a second implementation or validation
tree.
