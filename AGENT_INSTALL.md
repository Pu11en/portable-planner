# Install Portable Planner into your agent

This runbook is for the AI agent operating the user's local Codex, Claude Code,
ZCode, Hermes Agent, Zed, or other Agent Skills client. When the user supplies
this repository URL and asks to get, install, add, or put it on the agent,
complete the matching procedure yourself.

Do not ask the user to identify the client, choose an installation method, copy
commands, or restart an application. Detect the current client and use user
scope unless the user explicitly requests project scope.

Portable Planner is a file-only Agent Skill. It has no MCP server, runtime,
account, API key, database, or package dependency.

## Required outcome

The installed client can discover `portable-planner` from natural planning
requests and load the complete canonical bundle:

```text
plugins/portable-planner/skills/portable-planner/
```

That directory is the only canonical skill. Do not rewrite, summarize, merge,
or generate a harness-specific variation of it.

## Safety

- Install only from `https://github.com/Pu11en/portable-planner`.
- Preserve unrelated plugins, marketplaces, skills, configuration, and project files.
- Inspect an existing target before replacing it. Replace only another installation whose `SKILL.md` declares `name: portable-planner`.
- Never add Portable Planner instructions to a project's `AGENTS.md`, `CLAUDE.md`, or equivalent unless the user explicitly requests a project-local installation.
- Do not create `planning/` during installation. Planning files begin only when the user asks to plan.

## Common preflight and verification

Keep a temporary or existing local checkout available until installation is
verified. Confirm these files exist in the canonical bundle:

```text
SKILL.md
references/artifact-contract.md
references/conversation-contract.md
references/question-engine.md
references/validation-rubric.md
references/visual-contract.md
templates/NEXT.md
templates/PLAN-VIEW.md
templates/PLAN.md
templates/execution-ticket.md
templates/planning-ticket.md
```

After installation, read the installed `SKILL.md` and verify its YAML name is
`portable-planner`. Verify the referenced and template files above are present.
If the current task's skill catalog is frozen, load the canonical `SKILL.md` and
its task-required references directly from the checkout and continue in the
same session. Future sessions should discover the installed skill normally.

## Codex

Read `codex plugin marketplace list --json`. If the `portable-planner`
marketplace exists, refresh it; otherwise add it:

```text
codex plugin marketplace upgrade portable-planner --json
codex plugin marketplace add Pu11en/portable-planner --json
```

Run only the applicable command. Then install or refresh the plugin:

```text
codex plugin add portable-planner@portable-planner
codex plugin list
```

Require `codex plugin list` to report Portable Planner installed and enabled.
Use the direct-load procedure above for the current task if necessary; do not
ask the user to open a new task just to continue.

## Claude Code

Read `claude plugin marketplace list`. If the `portable-planner` marketplace
exists, refresh it; otherwise add it:

```text
claude plugin marketplace update portable-planner
claude plugin marketplace add Pu11en/portable-planner
```

Run only the applicable command. Then inspect `claude plugin list --json` and
install or update as appropriate:

```text
claude plugin install portable-planner@portable-planner --scope user
claude plugin update portable-planner@portable-planner --scope user
```

If `/reload-plugins` is available to the agent, invoke it. Otherwise use the
direct-load procedure and continue; the native plugin will be discoverable in
future sessions.

## ZCode

From the repository root, run:

```text
python3 scripts/install_zcode_plugin.py
```

Then validate `~/.zcode/cli/config.json` as JSON. Require
`plugins.enabled` to be `true` and `plugins.dirs` to contain the absolute
`~/.zcode/plugins/portable-planner` path. The installer atomically merges that
supported directory and preserves unrelated configuration.

Continue with the direct-load procedure if the current request cannot refresh
its skill catalog mid-turn.

## Hermes Agent

Read `hermes skills list`. For a missing skill, use Hermes's direct public
GitHub skill installation:

```text
hermes skills inspect Pu11en/portable-planner/plugins/portable-planner/skills/portable-planner
hermes skills install Pu11en/portable-planner/plugins/portable-planner/skills/portable-planner
```

For an existing Portable Planner installation from this repository, refresh it:

```text
hermes skills update portable-planner
```

Require the security inspection to identify `portable-planner`, then confirm it
with `hermes skills list`. If the current session cannot see the newly installed
skill, use the direct-load procedure rather than asking the user to restart.

## Zed

Zed discovers global Agent Skills as direct children of `~/.agents/skills/`.
Copy the canonical bundle unchanged to:

```text
~/.agents/skills/portable-planner/
```

Do not copy only `SKILL.md`; the referenced guidance and templates are required.
Verify the full bundle, then use the direct-load procedure for the current task
if Zed has not refreshed its catalog yet.

## Other Agent Skills clients

Use the client's documented user-scoped Agent Skills directory and copy the
canonical bundle unchanged as one direct child named `portable-planner`. Prefer
a native plugin or skill installer when the client provides one. Verify the
complete bundle and use direct loading for the current session when supported.

If the environment is a web-only chat without local computer access, state that
it cannot install local files. Do not pretend installation succeeded.

## Completion language

Use these states accurately:

- **Package verified:** the repository contains one complete canonical skill.
- **Installed:** the harness saved and enabled or indexed that skill.
- **Ready now:** the current session loaded the skill, either natively or directly.
- **Future-session ready:** a fresh session can discover it without the checkout.

After success, tell the user which state passed and invite a natural planning
request. Do not require the skill name or a slash command.
