# Codex Installation Forward Test

Date: 2026-08-05

## Package under test

The canonical plugin at `portable-planner/` was copied unchanged into the isolated local marketplace at `validation/codex-install-forward-20260805/marketplace/plugins/portable-planner/`.

Before use, recursive comparisons reported no differences between:

- the canonical plugin and the marketplace copy; and
- the canonical plugin and Codex's installed cache at `portable-planner-forward/portable-planner/0.1.0`.

Both the plugin validator and the skill validator had already passed on the canonical package.

## Installation

The isolated marketplace was registered from its absolute local path, then the plugin was installed with Codex's plugin CLI. `codex plugin list --json` reported:

- plugin ID `portable-planner@portable-planner-forward`;
- version `0.1.0`;
- installed and enabled;
- the expected local marketplace source; and
- the expected copied canonical plugin source.

The first attempt used a bare relative marketplace path and failed with:

```text
invalid marketplace source format; expected owner/repo, a git URL, or a local marketplace path
```

Using the resolved absolute path succeeded. This is a concrete installation recovery rule: resolve a local package to an absolute marketplace root before registering it.

## Fresh natural-language smoke interaction

A fresh `codex exec` session started in `validation/codex-install-forward-20260805/test-project/` with this request and no skill name or skill path:

```text
Plan the idea in IDEA.md with me. Start naturally and stop after the first user-facing planning turn.
```

The installed plugin produced this user-facing turn:

```text
Test drive: we're planning a neighborhood repair café; no event work happens here.

Planning: Neighborhood Repair Café
Now: Define a successful first afternoon
Later: Plan safety, capacity, volunteers, and event flow

If an item cannot be fixed, a safe diagnosis and clear next step could still count as useful.

A. Safe, useful pilot — Recommended; balanced and repeatable.
B. Repairs completed — Clearest output, but favors easier fixes.
C. Community connection — Welcoming, but weaker repair proof.

Or give a different answer. Reply A, B, or C.
```

It also created project-local `planning/PLAN.md`, `planning/NEXT.md`, and `planning/decisions/P-001-define-pilot-win.md`. The files preserve the full choice meanings, recommendation, scope, lifecycle boundary, and exact fresh-session continuation state.

## Clean one-request installation and same-session use

The temporary plugin and marketplace registration were removed before this test. `codex plugin list --json` confirmed that Portable Planner was absent.

A second fresh `codex exec` session received only:

- the absolute path to the isolated local marketplace package;
- a natural-language request to install the plugin without user-run terminal commands;
- a request to verify the skill and visual template;
- permission to use the documented direct-load fallback; and
- the workshop idea in the current project's `IDEA.md`.

The agent then, without asking the user to run anything:

1. inspected the package manifest and canonical skill;
2. registered the local marketplace with `codex plugin marketplace add`;
3. installed `portable-planner@portable-planner-forward` version `0.1.0` at user scope;
4. confirmed the installed package through `codex plugin list --json`;
5. recursively compared the installed cache with the supplied package;
6. verified matching SHA-256 hashes for `SKILL.md` and `templates/PLAN-VIEW.md`;
7. ran the skill validator successfully;
8. explicitly direct-loaded the installed skill because the session's startup catalog could not refresh; and
9. created project-local planning state and returned the first planning question in the same session.

The first planning turn stayed planning-only, oriented the user, asked one consequential delivery-model choice, put the recommended answer first as `A`, offered three viable choices plus a custom path, and wrote the complete choice meanings to `planning/` before displaying them.

Raw state: `validation/codex-natural-install-forward-20260805/project/planning/`.

Fresh Codex session: `019fd3cb-b921-71c0-8e1b-e267ac0936b1`.

## Result

**PASS for installed-plugin discovery and natural planning invocation in a fresh Codex context.** The smoke interaction required no command memorization, asked one human-owned decision, recommended `A`, performed no event work, and wrote the expected durable state.

**PASS for P-02.** Together, the clean installation run and the earlier malformed-relative-path recovery prove user-scope installation from one local package, package and visual verification, direct-load recovery for frozen same-session discovery, immediate smoke use, durable state creation, and one precise installation recovery without GitHub, another runtime, another download, or user-run terminal work.
