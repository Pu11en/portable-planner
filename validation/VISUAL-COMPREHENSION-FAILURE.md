# Visual Comprehension Failure

**Date:** 2026-08-05  
**Result:** Failed human review; V-05 reopened.

## Drew's feedback

Drew said the exported-image version should not be used and that the plan's layout was confusing. He asked for a new attempt using a different project that already contains one of his real plans.

## Concrete failures

1. A locally rendered PNG proved syntax and clipping, but it was the wrong user-facing presentation. The normal Codex experience should keep the plan inline.
2. The Hanoi overview mixed route milestones, current/invalid state, proof, scheduling, and supporting systems. Even after line cleanup, it still required too much interpretation.
3. The graph exposed implementation structure rather than giving one instantly readable answer to “where are we going, where are we now, and what happens next?”

## Correction under test

- Use one dominant milestone route with five to nine short outcome labels.
- Keep current state, next action, proof, and rules as compact text around the route.
- Move architecture, support systems, owners, inputs, and failure behavior into selected-step detail.
- Use inline Mermaid in Codex; never substitute a raster image unless the user explicitly asks for an exported image.
- Rerun on White Brain using its actual `PLAN.md`, `AGENTS.md`, and `README.md`, not a reconstructed project summary.
