# Session-Boundary Validation Failure

## Intended split

- The separate simulation task test-drives the planner on the YouTube-comment finder and owns canonical live-pilot state under `wiki/projects/planning-plugin-pilots/video-comment-finder/`.
- This goal-driven task builds and revises the portable planner from pilot evidence. It does not ask Drew the sample project's planning questions.

## Observed failure

The simulation opened directly with `1/5 ▶ Worthwhile question` and planning choices. Drew replied that he did not understand. The next reply presented another version of the same planning choice instead of explaining the task. Only after Drew explicitly asked about the other session did it explain the test-drive versus plugin-build split.

This implementation task then duplicated the simulation and asked Drew sample-project questions here, reinforcing the confusion.

## Required fixes

1. Orient before the first question: plan name, planning-only result, and—when applicable—test-drive status.
2. Keep live-pilot conversation and state in the simulation task only.
3. Treat “I’m confused” as a hard pause: explain the session and current step; ask no planning question in that reply.
4. Avoid internal terms and numeric progress until they add truthful information.

## Rerun proof required

A fresh simulation must make the session boundary understandable in its opening. An adversarial “I’m confused—what are we doing?” turn must receive a plain orientation reply with no planning question. Drew must then confirm the flow is clear enough to continue.
