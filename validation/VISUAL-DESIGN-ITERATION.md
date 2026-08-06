# Visual Design Iteration

**Date:** 2026-08-05  
**Status:** Rejected by human review; replaced by a simpler milestone-route experiment.

## Trigger

After accepting the Hanoi visual's information architecture, Drew asked whether the presentation could feel more intentionally designed and polished.

## Change

- Preserved the accepted route, facts, left-to-right row order, support connections, and Markdown fallback.
- Added a portable Mermaid base theme using ordinary system fonts.
- Added quiet numbered stage panels.
- Made the goal, current action, and proof visually strongest.
- Used rounded cards for human gates, the current action, and proof; automatic work remains a simpler rectangular card.
- Added one consistent semantic palette for goal, current, human, automatic, proof, support, and invalid states.
- Kept literal semantic labels so the plan remains understandable if a harness strips all styling.
- Added no renderer, runtime, package, app, or download.

## Render-discovered failure and correction

The first real Mermaid render exposed a layout failure that source inspection did not: support systems floated above and beside the production route, dense dashed lines competed with the route, and the schedule stage was stranded at the lower left. That was not polished enough to present as finished.

The corrected graph keeps the three route rows dominant, places Schedule after the acceptance proof in the final left-to-right row, and gathers support systems in one quiet panel below. Each support card names the exact step or stages it powers, preserving the important connections without a web of crossing lines. One invisible layout edge keeps that panel below the route; it adds no visible or semantic plan content.

## Verification

- Official plugin validator: pass.
- Official skill validator: pass.
- Mermaid CLI `11.12.0` rendered the complete graph successfully to a `1893 × 919` PNG.
- Plugin cachebuster refreshed to `0.1.0+codex.20260805230902`.
- Human visual-design result: fail. Drew rejected the raster image and reported that the route layout was confusing.
