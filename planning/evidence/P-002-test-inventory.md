# P-002 evidence — Historical Codex and ZCode corpus

Inventoried: 2026-08-15
Status: confirmed as the first validation source; no comparison run count is approved

## Finding

The earlier Codex task-list failure was a connector failure, not a history or data failure. The desktop connector reported `thread_list_unavailable` for the local host, but Codex's local session files, archive, index, and state database are present. ZCode also has a large local conversation store and an official legacy-session recovery path.

The former six-contract, eight-unit authored inventory is withdrawn. It remains useful as a list of behavior claims, but its exact prompts and full-conversation run count are not accepted evidence. Existing real conversations now come first.

## Official access model

### Codex

- The official [Codex App Server documentation](https://developers.openai.com/codex/app-server) defines `thread/list` for paged stored-thread discovery and `thread/read` with `includeTurns: true` for reading a stored thread without resuming it.
- The same documentation states that archived thread logs are persisted as JSONL under `$CODEX_HOME/archived_sessions`.
- In this desktop environment, `CODEX_HOME` is `/mnt/c/Users/drewp/.codex`. The useful read-only sources are `sessions/`, `archived_sessions/`, `session_index.jsonl`, and `state_5.sqlite`.
- Because the current local-host connector cannot list threads, direct read-only indexing of the rollout JSONL files is the reliable fallback. The SQLite thread table is useful metadata but is not complete enough to be the sole source for recent desktop tasks.

### ZCode

- [ZCode task management](https://zcode.z.ai/en/docs/task-management) documents task timeline, search, and archived-task access.
- [ZCode usage statistics](https://zcode.z.ai/en/docs/usage-stats) explicitly says the app reads local ZCode session records on the current device.
- [ZCode installation and migration](https://zcode.z.ai/en/docs/install) documents conversation migration, while [ZCode plugins](https://zcode.z.ai/en/docs/plugin) lists the official `restore-legacy-sessions` plugin.
- The bundled restore plugin confirms the concrete local stores: `~/.zcode/v2/tasks-index.sqlite`, `~/.zcode/cli/db/db.sqlite`, and the agent transcript JSONL files. Its local documentation is at `/home/drewp/.zcode/server/agents/glm/packages/restore-legacy-sessions-plugin/README.md`.

## Local inventory

These are aggregate read-only counts, not copied transcripts.

### Codex

- The initial snapshot contained 442 active and archived rollout JSONL records. This total is expected to grow while Codex is used.
- 184 records were user-source task logs; the remainder were predominantly subagent logs plus a small number of voice, MCP, and editor-originated records. Test mining must not count subagent logs as independent user conversations.
- Recorded dates span 2026-07-05 through 2026-08-15.
- The corpus includes real work in GOMER, Drew's AI course, Hanoi Picks, Cinco H Ranch, Portable Planner, the Pinterest plugin, and other software and non-software workspaces.

### ZCode

- 310 session rows and 17,541 message rows in the WSL CLI database.
- 83 interactive sessions containing 1,434 real user text turns.
- 207 agent transcript JSONL files under the WSL store.
- An additional small Windows-side store contains 5 session directories and 12 transcript files.
- Real candidate tasks include product-research planning, project audits, job-search planning, workflow automation, handoff rules, and project-gap reviews across software and non-software work.
- A metadata-and-keyword signal pass over the 83 interactive sessions found 50 with planning signals, 49 with correction signals, 20 with recommendation/letter-choice signals, and 30 with continuation/resumption signals. These are discovery leads, not behavior labels; the surrounding turns still require review.

## Safe corpus contract

1. Access the stores read-only. Do not resume, edit, archive, restore, or delete any source task merely to evaluate Portable Planner.
2. Normalize only the visible user and assistant text plus minimum metadata needed to reconstruct order, workspace, task identity, and time.
3. Exclude system/developer instructions, hidden reasoning, tool payloads, subagent traffic, automated task runs, and binary attachments by default.
4. Deduplicate Codex rollout and compaction fragments by stable session and event identity. Do not treat every JSONL file as a separate conversation.
5. For ZCode, join `session`, `message`, and `part`; retain `task_type=interactive`, user/assistant roles, and visible text parts.
6. Keep raw transcripts local and untracked. Do not commit private conversations, credentials, personal details, or full proprietary task history to this public repository.
7. Commit only aggregate inventory, redacted case contracts, and the smallest sanitized excerpts needed to explain a behavior claim.

## Historical-first evaluation route

1. Mine real moments where Drew was planning, corrected the agent, repeatedly accepted recommendations, delegated reversible choices, rejected premature testing, resumed a plan, or asked for direct status/diagnosis/build work.
2. Label observed behavior without inventing an ideal answer: starting state, exact visible turn, route taken, user reaction or correction, durable-state effect, and the claim the moment can test.
3. Collapse duplicates and select the smallest set of materially different real traces. Domain variety is evidence only when it changes the failure risk.
4. Use historical traces as frozen baseline evidence. They reveal actual user language and actual failures without new conversation-generation cost.
5. When testing a changed candidate, replay only the selected decision point with the minimum preceding visible state needed to preserve meaning. Compare beta 6 and the candidate on that same frozen input; do not generate a whole replacement conversation unless the behavior genuinely depends on later turns.
6. Use deterministic checks for routing, option labels, streak state, canonical artifact agreement, protected gates, and prohibited mutations.
7. Finish with the smallest fresh uncoached human task because only live use can prove that the changed planner feels more effective in context.

## Evidence limit

Historical conversations prove what the earlier agent did and how Drew reacted. They do not, by themselves, prove that a future instruction change would respond better. A bounded counterfactual replay or fresh live use is still required for that claim. This limit is why the corpus removes most authored conversation work but does not remove all candidate execution.

## Next evidence action

Build a private, read-only candidate index from the two stores and surface a redacted set of real planning moments grouped by behavior claim. Only after seeing those real cases should Drew be asked whether any important behavior is missing or whether a candidate comparison is warranted.
