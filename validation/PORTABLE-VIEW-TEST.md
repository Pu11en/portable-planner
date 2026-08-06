# Portable Plan View Test

Date: 2026-08-05

## Codex fresh-context generation

A fresh planning agent loaded the unchanged canonical skill and planned a one-day neighborhood cleanup from a detailed natural-language request. It:

- created canonical plan state and four execution tickets;
- generated `planning/PLAN-VIEW.md` from that state;
- returned the Mermaid route directly in the user-facing session;
- included the same artifact's compact text route;
- kept safety boundaries and city handoff connections visible; and
- linked the visual and detailed plan without requiring a renderer or another download.

Raw evidence: `validation/portable-view-forward-20260805/planning/`.

**Result:** PASS for fresh Codex-side generation and fallback content. Drew's actual in-session visibility confirmation is still required.

## Claude Code unchanged-state attempt

Claude Code `2.1.177` was asked to load the canonical skill by path and resume the unchanged generated planning folder read-only. The harness failed before loading any plugin or project file:

```text
Failed to authenticate. API Error: 401 OAuth access token has expired. Re-authenticate to continue.
```

**Result:** BLOCKED by harness authentication, not passed. Exact recovery is `claude auth login`, after which the same read-only prompt must be rerun. No cross-harness portability claim may be made from this attempt.

## Hermes unchanged-skill and unchanged-state pass

Hermes Agent `0.19.1` was available with a working OpenAI Codex provider. From the workshop validation project, a one-shot Hermes context received only:

- the absolute path to the unchanged canonical `SKILL.md`;
- the unchanged project-local `planning/` directory;
- the natural request `Show my full plan map`; and
- a read-only boundary prohibiting file changes, decision answers, sibling fixtures, and prior test reports.

Hermes loaded the skill directly without a Hermes-specific copy or domain pack. Its text-native view showed:

- lifecycle status, destination, and success proof;
- current and next action;
- the complete ordered route with completed, current, and pending states;
- the dependency connection from starter menu through staffing, registration, flow, and safety; and
- all six plan-wide safety rules.

Hermes did not claim a graphical popup. It used the canonical compact text route, the richest surface supported by this one-shot text harness.

The SHA-256 hashes of `PLAN.md`, `PLAN-VIEW.md`, `NEXT.md`, and the current decision were recorded before and after Hermes; all four were byte-identical.

## Codex → Hermes → Codex alternation

After the Hermes read, a fresh read-only Codex CLI context loaded the same canonical skill path and the same untouched `planning/` directory. It rendered the full Mermaid graph, text route, step details, and safety rules from that state without conversion or modification.

A third hash check matched the same four pre-Hermes hashes:

```text
feb870b1...  planning/NEXT.md
5014f70c...  planning/PLAN-VIEW.md
3610c781...  planning/PLAN.md
43a9b389...  planning/decisions/P-001-define-workshop.md
```

Hermes output used shorter labels than Codex, but its destination, current frontier, complete route, dependencies, and safety rules agreed with canonical state. Presentation adapted to the harness; planning state did not.

**Result: PASS for unchanged canonical skill use in Hermes and PASS for Codex → Hermes → Codex unchanged-state resumption.** Claude Code remains desirable as the main second rich harness, but its expired OAuth token no longer blocks the MVP's explicit at-least-one-non-Codex acceptance gate.
