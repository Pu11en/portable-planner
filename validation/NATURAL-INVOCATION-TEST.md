# Natural-Language Invocation Test

**Date:** 2026-08-05  
**Result:** PASS for C-05

The canonical skill treats ordinary requests as invocations without a slash command or memorized plugin syntax:

| Natural request | Fresh-context evidence | Result |
|---|---|---|
| `Plan this idea: ...` | A clean Codex installation smoke received a natural request to plan `IDEA.md`, discovered the installed plugin, created canonical state, and asked the first compact planning question. | [PASS](CODEX-INSTALL-TEST.md) |
| `Continue my plan` | A fresh installed-plugin context loaded canonical files, refreshed and displayed the complete route, advanced the keyed decision, and repaired stale handoff state. | [PASS](FRESH-RESUME-VISUAL-TEST.md) |
| `Show my full plan map` | Hermes and then Codex used the unchanged canonical skill and unchanged state to display the richest supported complete route. | [PASS](PORTABLE-VIEW-TEST.md) |
| `Prepare the next session` | Fresh Codex session `019fd3fb-68e6-7773-a84c-0c6e33d96076` loaded the current operational fixture, recognized `awaiting approval`, verified `NEXT.md`, and returned the exact current and later actions without changing state or starting execution. | PASS |

The installation test separately proves same-session discovery/direct-load recovery. This test concerns the user's ordinary language after the skill is available; none of the four requests requires a slash command or internal workflow choice.
