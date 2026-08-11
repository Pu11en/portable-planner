# Continue This Plan

Plan location: `{{project path}}/planning/`

Load `PLAN.md` first. Follow its lifecycle status:

- `planning`: load `decisions/{{current ticket file}}` and only its linked evidence or decisions.
- `awaiting approval`: show `PLAN-VIEW.md` and obtain explicit approval; do not build.
- `approved for build`: load `execution/{{first eligible ticket file}}` and use the harness's normal build workflow; Portable Planner does not perform the work.

Treat those files as canonical; do not rely on previous chat.

Work only on **{{one P-NNN planning ticket, visual approval, or E-NNN build ticket}}**.

Essential context: {{minimum context needed to avoid rereading unrelated artifacts}}

This session must: {{one decision, approval, planning output, or build-ticket outcome}}

Complete when: {{objective ticket completion check}}
