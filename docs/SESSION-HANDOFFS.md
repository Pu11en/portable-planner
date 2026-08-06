# Portable Planning Plugin — Session Handoffs

These are the two working sessions requested after MVP planning.

## Session 1 — Live UX simulation

**Purpose:** experience the proposed planner on a small real idea before plugin implementation determines the UX.

```text
Run a live simulation of the proposed Portable Planning Plugin.

Read the canonical MVP plan at:
/home/drewp/main-projects/portable-planner/docs/MVP-PLAN.md

Do not build, install, or modify plugin code. Act exactly like the planned plugin so Drew can judge the experience.

Loose idea to plan:
Create a skill that finds worthwhile questions in comments on AI-related YouTube videos, shows Drew several linked options he is qualified to answer, and stops there. Drew manually opens a chosen comment and records a short 9:16 talking-head answer for YouTube Shorts or TikTok.

Follow the conversation contract exactly:
- show compact progress and the current planning step;
- ask at most one high-value preference question per turn;
- never ask about an obvious, already answered, factual, or technical choice;
- when a real choice exists, give 2–3 short viable options, recommend one, and allow a custom answer;
- show a concrete example before asking about anything abstract;
- keep ordinary replies under roughly 60 words;
- research factual unknowns yourself from primary/direct sources;
- update durable local planning artifacts after each confirmed decision;
- generate an exact next-session starter whenever a planning ticket ends.

Store only this pilot's planning artifacts under:
/home/drewp/main-projects/portable-planner/pilots/early-ux-simulations/video-comment-finder/

At the end, create PILOT-REVIEW.md there. Compare the experience against the canonical validation rubric, record Drew's feedback, and identify only failures demonstrated by the pilot. Do not propose extra architecture without a failed test requiring it.

Start naturally with the compact progress display and the first genuinely important preference decision.
```

## Session 2 — Goal-driven MVP implementation and iteration

**Purpose:** build the smallest plugin, test it against real plans, revise it from evidence, and stop only at human acceptance.

```text
Create and pursue this explicit goal:

Deliver a portable planning plugin MVP that Drew prefers over the current planning experience, proven by simple and complex live pilots, durable fresh-session resumption, useful execution tickets, and portability across Codex plus at least one non-Codex harness.

Read these canonical inputs first:
- /home/drewp/main-projects/portable-planner/docs/MVP-PLAN.md
- /home/drewp/main-projects/portable-planner/research/PORTABLE-PLANNING-SYSTEMS.md
- /home/drewp/main-projects/portable-planner/pilots/early-ux-simulations/video-comment-finder/ if it exists

Use the product destination and acceptance standard in the MVP plan as the goal criteria. Before implementation, translate them into a concise pass/fail checklist. Then build and iterate.

Implementation constraints:
- start with one canonical Agent Skill, references, and Markdown templates;
- use plain project-local planning artifacts;
- no MCP, database, web app, cloud account, GitHub requirement, or domain pack in the first version;
- natural-language invocation must work;
- preserve unrelated workspace changes;
- keep implementation isolated and documented as an experiment until live testing proves it;
- do not add architecture unless a failed validation test demonstrates the need;
- use local save points and focused commits only for verified work owned by this effort.

Required iteration loop:
1. Build the smallest usable version.
2. Run the simple YouTube-comment finder pilot from a fresh context.
3. Record every obvious question, repeated question, wall of text, state loss, bad handoff, or incomplete output as a concrete failure.
4. Fix demonstrated failures and rerun.
5. Run one complex business or course-planning pilot.
6. Test software, creative/content, operational/event, and personal-project fixtures.
7. Verify installation and unchanged project-state portability in Codex and one non-Codex harness.
8. Review against the original destination, then ask Drew for human acceptance.

Do not mark the goal complete until every objective criterion passes and Drew confirms that the simple and complex live experiences are planning flows he would actually use.
```
