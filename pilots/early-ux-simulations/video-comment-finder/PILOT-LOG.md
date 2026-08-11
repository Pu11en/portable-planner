# Trusted-Channel Video Comment Finder — Human Live Pilot Log

**Status:** waiting for Drew's first answer; T-01 is not passed.  
**Canonical state:** [`planning/`](planning/)  
**Corrected clean opening session:** `019fd421-a377-7330-9e1f-f0e6f179f512`

## Preserved failures

- [`failed-opening-20260805`](archive/failed-opening-20260805/FAILURE.md): numbered choices, invented `1/5` route, wrong artifact location, stale broad-channel idea, and no visual gate.
- [`F-011`](archive/failed-live-opening-F011-20260805/FAILURE.md): corrected live opening still used abstract comment-category labels without a literal example.

## F-011 fix and clean rerun

The generic `question-engine.md` now says category names, experience qualities, priorities, and similar labels are abstract; a literal project-specific input, output, or moment must appear before those choices, and option descriptions do not count as the example.

The plugin cachebuster advanced to `0.1.0+codex.20260805225242`. Official plugin and skill validators passed before the rerun.

The clean rerun created exactly one planning ticket under canonical `planning/`, no speculative plan view or execution tickets, no fixed progress count, and this user-facing turn:

<!-- OPENING-START -->
Planning: Trusted-Channel Video Comment Finder  
Now: Decide which worthwhile comments rise first  
Later: Turn the decisions into a visual, execution-ready plan

We’re deciding what to build and how to prove it—not building or running the finder.

Picture this comment: “My custom GPT keeps ignoring its instructions—what should I fix first?”

A. Practical blockers — Recommended; useful and evergreen.  
B. Misconceptions — Strong teaching angle, but needs context.  
C. Timely tool questions — Topical, but expires faster.

Or give a different answer. Reply A, B, or C.
<!-- OPENING-END -->

The opening passes the F-011 completion test. The human pilot remains open until Drew answers, the planner writes through each real decision, shows the finished visual, Drew approves or revises it, and the final experience is judged.

## Drew's length calibration

This opening measures 86 words. Drew explicitly confirmed that 86 is fine, anything under 100 is acceptable, and roughly 60 should remain a flexible standard rather than a strict limit. No F-012 failure remains.
