# Portable Planner

Tell your AI to install it. Then plan naturally.

> **Public preview:** Portable Planner is usable now, but Drew is still testing it on real plans. The planning flow and file format may change before v1.

Portable Planner turns a rough idea into a clear, durable plan by asking one worthwhile question at a time. It recommends the strongest answer first, keeps replies short, saves the plan inside the project, and shows a visual route when the plan is coherent enough to review.

## Install

Paste this into Codex, Claude Code, ZCode, Hermes, Zed, or another local coding agent:

```text
Get this on yourself: https://github.com/Pu11en/portable-planner
```

The agent should detect its own harness, install at user scope, verify the skill, and continue in the same session. The complete agent runbook is in [AGENT_INSTALL.md](AGENT_INSTALL.md).

No cloud account, database, web app, MCP server, API key, or project-management service is required.

## Use it

You do not need a command. Say what you want:

```text
I want to plan marketing for this course.
```

Other natural requests work too:

- `Plan this idea with me.`
- `Continue my plan.`
- `Show me the visual plan.`
- `Turn the approved plan into execution tickets.`

The planner creates plain project-local Markdown under `planning/`. A fresh agent session can resume from those files without the original chat. In Codex, a plan that genuinely outgrows the current task can create one compact successor task after the user authorizes automatic continuation for that plan; small plans stay in the current task.

## What the experience is designed to do

- Ask one recommendation-first A/B/C question at a time.
- Keep normal conversational output compact—usually under 100 words when a question is enough.
- Research or infer agent-owned decisions instead of grilling the user about implementation details.
- Show an ordered visual route automatically at the approval point.
- Produce dependency-ordered, session-sized execution tickets.
- Cross real Codex context boundaries with a short local-state pointer instead of making the next task rediscover the project.
- Stop at an approved plan; the host agent keeps its normal build workflow.

## Compatibility

Portable Planner has one canonical [Agent Skill](plugins/portable-planner/skills/portable-planner/SKILL.md). Harness packages are thin installation wrappers around that same directory.

| Harness | Install path | Preview status |
| --- | --- | --- |
| Codex | Native plugin marketplace | Public marketplace install passed |
| Claude Code | Native plugin marketplace | Public marketplace install passed |
| ZCode | User plugin directory | Isolated installer test passed; live client test pending |
| Hermes Agent | Direct GitHub skill install | Public install and security scan passed |
| Zed | Global Agent Skills directory | Standards-compatible; public install test pending |
| Other Agent Skills clients | Client's documented user skill directory | Best effort |

## Privacy and project state

The planner works on local files only. It writes planning state under the active project's `planning/` directory and does not require telemetry or a remote service. Installers must preserve unrelated plugins, settings, and project files.

## Preview feedback

Useful failure reports include: an obvious or repeated question, a wall of text, lost state after a fresh session, a confusing visual route, a weak handoff, or an execution ticket that is not build-ready.

## License

MIT
