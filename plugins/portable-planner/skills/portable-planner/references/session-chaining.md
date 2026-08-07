# Session Chaining

Use task chaining only to protect planning quality across a real context boundary. It is an adaptive continuation mechanism, not a required step in every plan.

## Authorization

A successor task changes the user's task list. Create one only when the user has explicitly authorized automatic task continuation for this plan. Record that plan-scoped permission in `PLAN.md` as `Continuation: automatic — authorized`. A natural planning request by itself does not grant task-creation permission. If permission is absent when a real boundary appears, give one clearly labeled paste-ready next-session prompt. Do not end with only a ticket name, path, or vague statement that another session is next.

Automatic task-creation permission covers planning successors only. A direct `yes` to the finished plan's explicit build-approval question does authorize implementation through the current harness's normal build workflow. Begin in the current task when safe. Creating a separate build task still requires the host's normal task-creation authority; if that authority is absent, keep the approved `NEXT.md` handoff exact without asking for build permission again.

## Stay or chain

Stay in the current task when the current planning ticket can still be completed and verified reliably. Small or clear plans should finish in one task.

Chain only when at least one concrete boundary exists:

- the remaining planning unit will not fit reliably in the current context;
- an independent research or decision-prototype ticket needs a clean context;
- the current task has accumulated enough unrelated context that a fresh task materially reduces drift; or
- a human review must be deferred and the current task can no longer preserve a clear review surface.

Do not chain merely because a question was answered, a file was written, or multiple tickets exist. Do not create one task per question.

## Save before creating

Before requesting a successor:

1. write every confirmed decision through to its ticket and linked evidence;
2. reconcile `PLAN.md`, dependencies, current/next, and `PLAN-VIEW.md`;
3. write compact `NEXT.md` naming exactly one action and only the files needed for it;
4. run the fresh-context handoff check from the validation rubric; and
5. record that a boundary was reached and why in `PLAN.md`.

The successor prompt is only:

```text
Use $portable-planner. Follow /absolute/path/to/planning/NEXT.md.
```

The new task must load `NEXT.md`, `PLAN.md`, the named current ticket, and only linked evidence needed now. It must not rediscover the project, reread unrelated files, or trust prior chat.

## Codex adapter

When Codex exposes native task creation and plan-scoped authorization is recorded:

1. create one successor in the same saved project using the direct/local project environment so it sees the same project-local planning state;
2. use the exact compact prompt above and a short title based on the current planning outcome;
3. after creation succeeds, record the returned task identifier in `PLAN.md`; and
4. do not create or retry another successor unless Codex explicitly reports that creation failed.

After creation succeeds, tell the person briefly that the next task was started and identify it. Do not also give a paste-ready prompt unless creation failed.

The automatic pointer is a machine handoff, not a natural-language `continue` request. Its first reply should use the compact plan/now/later shape. Do not force the full visual unless another visual trigger applies. A human-owned ticket may wait in the successor for the user's answer; an agent-owned research ticket may continue without interruption.

Do not create a planning worktree. Sequential planning tasks must share the same local canonical files. A later build task may use the harness's normal repository and worktree behavior after approval.

## Unsupported or failed creation

If the host has no task-creation capability, creation is not authorized, or creation fails, preserve state and show this one clearly labeled paste-ready recovery action:

```text
Next-session prompt:
Use $portable-planner. Follow /absolute/path/to/planning/NEXT.md.
```

Never claim a successor exists until the host returns success. Never hide an uncertain result by retrying and risking duplicates. A handoff is incomplete until either the successor task exists or the exact labeled prompt is visible to the person.
