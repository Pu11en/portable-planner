# Portable Planner

Tell your AI to install it. Then plan naturally.

> **Public preview:** Portable Planner is usable now, but Drew is still testing it on real plans. The planning flow and file format may change before v1.

Portable Planner turns no idea, a rough idea, or a defined project into a clear, durable plan by asking one worthwhile question at a time. At the beginning of a rough software or AI idea, the local `beta.3` candidate can optionally scan current public repositories to show plausible directions and a fast MVP path before ordinary planning. This new scan remains unproven until the linked acceptance checks pass.

## Project source of truth

This repository now contains the complete Portable Planner project, not only its installable package:

- [Product goal](docs/GOAL.md)
- [Confirmed product contract](docs/PRODUCT-CONTRACT.md)
- [MVP plan](docs/MVP-PLAN.md)
- [Acceptance checklist](docs/ACCEPTANCE.md)
- [Remaining-work map](project-map/map.md)
- [Validation evidence](validation/)
- [Live pilot evidence](pilots/)

The one canonical installable skill remains under `plugins/portable-planner/skills/portable-planner/`. Validation fixtures and historical evidence are not alternate skill sources.

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

- `I want to make some kind of software, but I do not have an idea yet.`
- `Explore what is possible for this rough app idea.`
- `Plan this idea with me.`
- `Continue my plan.`
- `Show me the visual plan.`
- `Turn the approved plan into execution tickets.`

The planner creates plain project-local Markdown under `planning/`. A fresh agent session can resume from those files without the original chat. In Codex, a plan that genuinely outgrows the current task can create one compact successor task after the user authorizes automatic continuation for that plan; small plans stay in the current task.

## What the experience is designed to do

- Ask one recommendation-first A/B/C question at a time.
- Keep normal conversational output compact—usually under 100 words when a question is enough.
- Research or infer agent-owned decisions instead of grilling the user about implementation details.
- With permission at the start of a thin software/AI idea, run a privacy-safe, bounded public-repository scan and keep its recommendation provisional until the user confirms the direction.
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

Planning state stays in local files under the active project's `planning/` directory and requires no telemetry or remote storage service. The optional idea-stage scan sends only a sanitized search brief to the host's existing public research surface after permission; it must remove or generalize private names, credentials, paths, proprietary text, and sensitive details. It never clones or executes discovered repositories. Installers must preserve unrelated plugins, settings, and project files.

## Preview feedback

Useful failure reports include: an obvious or repeated question, a wall of text, lost state after a fresh session, a confusing visual route, a weak handoff, or an execution ticket that is not build-ready.

## License

MIT
