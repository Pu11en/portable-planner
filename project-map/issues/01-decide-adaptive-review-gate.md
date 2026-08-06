# Decide the adaptive review gate

Type: grilling
Status: resolved
Blocked by:

## Question

What evidence should let Portable Planner decide—without a rigid question count—that a plan is coherent enough to open the interactive review automatically, and exactly how should approval, targeted revision, or continued grilling return the plan to the correct state?

## Comments

- This is the current frontier. Resolve it with concrete simple and complex examples, then write the decision into the plugin's question, visual, artifact, and finish contracts before the next ticket begins.
- 2026-08-06: Claimed for a live Drew + Codex grilling session. Drew clarified that the visual is a built-in capability the agent may show or offer, not a rigid mandatory event tied to a fixed question count.

## Answer

Portable Planner uses an adaptive hybrid review gate:

- The visual is always available through natural language such as “show me the plan.” That displays the best current draft without claiming planning is complete.
- During grilling, the agent may offer the draft once it has enough coherent structure to be useful. It does not repeatedly ask whether the user wants to see it.
- The agent automatically opens the final review only after it can defend the complete route: destination and observable success are clear; boundaries are explicit; major human-owned decisions are settled; the route, dependencies, owners, gates, risks, and recovery behavior are coherent; execution tickets can be derived without reopening major planning; and canonical artifacts agree.
- There is no question-count threshold, and minor implementation mechanics do not block review when the agent can safely infer them.
- Automatic final review runs the finish audit, creates or refreshes execution tickets, changes lifecycle status to `awaiting approval`, and displays the interactive plan without first asking whether the user wants to see it.
- Approval changes status to `approved for build` and points the harness to the first execution ticket. A targeted change returns the plan to `planning`, reopens only the affected human decision, reconciles downstream state, and refreshes the view. “Keep planning” returns to `planning` and asks the highest-value unresolved human decision one at a time. Confusion pauses questions and explains the state.
- Codex prefers the approved interactive route presentation: destination/current/next cards, a clickable ordered route, one selected-step detail surface, compact support connections, and a short safety line. `PLAN-VIEW.md` remains the portable generated Markdown/Mermaid/text fallback and canonical project files remain authoritative. A PNG is never the normal plan view.

This decision was confirmed by Drew on 2026-08-06.
