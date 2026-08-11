# Fresh-Session Resume Tests

## Existing handoff

- Setup: A fresh agent received only the canonical skill path and the simple pilot's `planning/` location.
- Result: PASS. It loaded the pending P-001 state and reconstructed the same source-mode preference without prior chat or state conversion.

## Missing `NEXT.md` — initial run

- Setup: Copied `PLAN.md` and P-001 into an isolated planning folder, deliberately omitted `NEXT.md`, and asked a fresh agent to continue using only that folder.
- Result: PARTIAL. The agent regenerated the correct current ticket, essential context, required outcome, and completion test.
- Failure **F-002:** The regenerated `NEXT.md` wrote `Plan location: planning/` instead of the resolved absolute location. A paste-ready handoff could therefore resume from the wrong folder when the fresh session starts elsewhere.
- Fix: Require the resolved absolute `planning/` path and independence from the original working directory in both the core handoff instruction and artifact contract.

## Missing `NEXT.md` — clean rerun

- Result: PASS. The fresh agent regenerated the same pending P-001 state and wrote the resolved absolute planning path, exact session outcome, and completion test without prior chat or the original working directory.
- Conversation failure **F-003:** Its user-facing choice included three viable options and a recommendation but omitted an explicit custom-answer path.
- Fix: Require every displayed choice set to visibly end with a custom-answer path, not merely accept one internally.

## Conversation-contract resume rerun

- Result: PASS. A new fresh agent resumed from the repaired canonical state, presented three viable choices and a recommendation, and visibly ended with “Or give a different answer.”
