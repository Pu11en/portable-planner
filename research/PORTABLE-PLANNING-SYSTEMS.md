# Portable Planning Systems Research

**Status:** Research input, not a product decision  
**Question:** Which existing systems offer useful patterns for a low-reading-load, multi-session planner that can take any vague idea to a cohesive end-to-end plan and ordered execution tickets?

## Bottom line

No reviewed system combines the whole target experience. The closest evidence comes from several complementary systems:

- **Wayfinder** supplies the adaptive decision map, one-ticket sessions, and separate research/prototype/human-decision work.
- **Spec Kit** supplies a shallow durable roadmap of bounded, dependency-ordered slices and exact persisted workflow resumption.
- **OpenSpec** supplies a local artifact dependency graph whose state can be derived from files and kept coherent as decisions change.
- **BMAD** supplies an explicit “what should I do next?” guide and fresh-chat workflow discipline.
- **Superpowers** supplies concise one-question-at-a-time discovery and an approval gate between design and implementation planning.
- **Agent Skills plus the Channel Brains installer** show a plausible portable packaging and beginner-facing installation pattern.

This is an inference from the sources below, not a recommendation to copy any one architecture.

## Comparisons

| System | Relevant evidence | Useful idea to evaluate | Pitfall to avoid |
|---|---|---|---|
| Wayfinder | It names the destination first, treats the map as an index, exposes the open unblocked frontier, resolves at most one decision ticket per session, and distinguishes human-in-the-loop grilling/prototype tickets from agent-run research. It can fall back to local Markdown. [Official Wayfinder documentation](https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md) | Let later discoveries add or reshape tickets without pretending the whole route is knowable upfront. Keep each decision authoritative in one place and show only the next usable frontier. | Its language (`fog`, `frontier`, HITL/AFK), issue-tracker framing, explicit `/wayfinder` invocation, branching, and surrounding skill suite are too technical to expose directly to a first-time planner. Wayfinder also stops at decisions; another step must create the final spec and execution tickets. |
| GitHub Spec Kit | Its “Spec of Specs” records an ordinary Markdown roadmap with stable IDs, intent, scope boundaries, dependencies, status, and links; entries are handled one at a time and can be recursively split. Workflow runs persist `state.json`, inputs, and a log, then resume at the exact paused or failed step. [Spec of Specs](https://github.github.com/spec-kit/concepts/spec-of-specs.html) · [Workflow state and resume](https://github.github.com/spec-kit/reference/workflows.html) | A shallow master map can remain readable while detailed work lives in linked artifacts. Stable identifiers and explicit dependencies preserve traceability across sessions. A stored resume point is more reliable than chat memory. | Roadmap reconciliation is manual, and recursive maps can become document bureaucracy. The default process is software-focused, with CLI initialization and harness-specific command forms. Spec Kit itself warns that large-feature decomposition adds overhead and should be conditional. |
| OpenSpec | Schemas define artifacts and their dependencies; status is derived as done, ready, or blocked; `/opsx:continue` creates one ready artifact, while `/opsx:update` revises existing planning artifacts coherently. The CLI exposes status, missing dependencies, instructions, and dependency content as JSON. [OPSX workflow](https://openspec.dev/docs/opsx) · [CLI reference](https://openspec.dev/docs/reference/cli) | The planner could derive “what is next?” from local canonical artifacts instead of asking the user to remember a session. An update operation could deliberately reconcile affected artifacts when a decision changes. | Its default proposal/spec/design/tasks vocabulary is still software-change oriented. Installation requires Node and terminal setup. Its own docs explain that invocation differs across tools—for example Claude, Hermes, and Codex use different forms—which creates a portability UX problem even when the underlying intent is identical. [How commands work](https://openspec.dev/docs/how-commands-work) |
| BMAD Method | BMAD progressively builds context through optional analysis, planning, solutioning, and implementation workflows. `bmad-help` inspects progress and recommends what comes next; its workflows create explicit artifacts, and official guidance uses fresh chats for separate workflows. [Workflow map](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/reference/workflow-map.md) · [Getting started](https://docs.bmad-method.org/tutorials/getting-started/) | A single plain-language “continue my plan” entry point could inspect durable state, select the next planning unit, and explain it without requiring the user to know session boundaries or command names. | The full method is role-heavy, artifact-heavy, and strongly oriented toward software delivery. Asking a beginner to select agents, tracks, or workflows transfers system-routing work to the user. It guides the next workflow but does not inherently generate a paste-ready next-session starter. |
| Superpowers | Brainstorming asks one question at a time, prefers multiple choice, offers 2–3 approaches with trade-offs and a recommendation, cuts scope aggressively, writes a durable spec, self-checks it, and requires user review before implementation planning. [Brainstorming skill](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) · [Writing plans skill](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) | Reserve questions for real preference decisions; present genuine alternatives together instead of asking the user to approve obvious mechanics one by one. Separate the agreed destination from the execution plan and require a review gate between them. | Its standard design review can still produce long sections, and its plan format assumes coding, exact file paths, tests, Git, and commits. Mandatory gates for every task can become ceremony when the route is already clear. |
| Beads | Beads is a persistent dependency-aware graph with auto-detected ready work and local agent setup. Its own positioning is long-horizon agent memory rather than a planning conversation. [Official Beads repository](https://github.com/gastownhall/beads) | Dependency-aware ready-state calculation and durable memory are useful reference behaviors if plain files alone prove insufficient. | It introduces a CLI and database-backed issue system before the planning UX requires one. Its concepts (`beads`, claims, Dolt sync) would increase learning load, and it targets coding agents rather than non-technical planning. It is a possible storage reference, not a proven core experience. |

## Process ideas supported by more than one source

These are candidate behaviors to test, not locked requirements:

1. **Start small, escalate only when necessary.** Wayfinder skips a map when the opening discussion exposes no meaningful fog. Spec Kit says its multi-map decomposition has high overhead and should be used only when lighter approaches fail. A planner therefore needs a deliberate one-session-versus-multi-session decision, not one heavyweight path for every idea. [Wayfinder](https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md) · [Spec Kit](https://github.github.com/spec-kit/concepts/spec-of-specs.html)
2. **Separate destination, decisions, and execution.** Wayfinder tickets settle decisions; Superpowers writes an approved design before an implementation plan; BMAD distinguishes planning artifacts from solutioning and build artifacts. This prevents an execution checklist from silently standing in for a coherent plan. [Wayfinder](https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md) · [Superpowers](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) · [BMAD](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/reference/workflow-map.md)
3. **Make the map shallow and the state durable.** Wayfinder keeps detail in tickets rather than duplicating it in the map. Spec Kit uses a shallow roadmap with stable IDs and links. OpenSpec derives readiness from artifacts and dependencies. Together these patterns reduce both context load and drift. [Wayfinder](https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md) · [Spec Kit](https://github.github.com/spec-kit/concepts/spec-of-specs.html) · [OpenSpec](https://openspec.dev/docs/reference/cli)
4. **Resume from state, then show the human one next action.** Spec Kit proves exact local workflow resumption; OpenSpec can report ready and blocked artifacts; BMAD adds a user-facing help layer. A generated next-session starter is valuable, but durable state should still be sufficient if that starter is lost. [Spec Kit workflows](https://github.github.com/spec-kit/reference/workflows.html) · [OpenSpec status](https://openspec.dev/docs/reference/cli) · [BMAD help](https://docs.bmad-method.org/reference/core-tools/)
5. **Keep factual uncertainty out of preference questioning.** Wayfinder models research as its own blocker and reserves grilling/prototypes for live human judgment. BMAD similarly separates decision research from product discovery. This supports fewer, higher-value questions. [Wayfinder](https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md) · [BMAD workflow map](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/reference/workflow-map.md)

## Portability and installation evidence

The open [Agent Skills specification](https://github.com/agentskills/agentskills) defines a portable folder centered on `SKILL.md`, with optional scripts, references, and assets loaded progressively. That is evidence that the conversational planning method can be packaged independently of a particular agent. It does **not** guarantee identical behavior across harnesses or provide durable project state by itself.

OpenSpec demonstrates a two-layer model: one common engine/state model plus generated tool-specific skills or commands. Its official invocation table includes Claude Code, Hermes, shared `.agents`, and Codex, while also exposing the downside: the same action is typed differently in different tools. [OpenSpec command model](https://openspec.dev/docs/how-commands-work)

Channel Brains demonstrates a different beginner-facing installation contract: the user gives one natural instruction plus a repository URL, and the installing agent detects its client, installs the appropriate adapter, verifies it, and handles same-session fallback. That behavior is documented in the [Channel Brains repository](https://github.com/Pu11en/channel-brains). Its MCP server is justified by executable search/indexing capabilities; that does not establish that this planning product needs MCP.

## Important non-conclusions

The research does not yet decide:

- whether canonical state should be a few Markdown files, Markdown plus a small machine-readable state file, or a local database;
- whether the user sees a “map,” a short progress view, or both;
- whether research and prototype work are visible ticket types or internal routing;
- whether installation needs only Agent Skills packaging or an additional local runtime;
- how much detail belongs in the final cohesive plan versus linked ticket artifacts;
- whether one universal process works across businesses, events, content, personal projects, and software, or whether lightweight project-type overlays are necessary.

Those choices require either user-experience decisions or cross-project validation; the comparable systems do not settle them.

## Practical research conclusion

The clearest opportunity is not to invent another full planning methodology. It is to combine and simplify proven mechanics: Wayfinder’s adaptive decision frontier, Spec Kit/OpenSpec’s durable local dependency state, BMAD’s next-step guidance, and Superpowers’ one-question discovery—then remove software jargon, role selection, tracker setup, Git requirements, and command memorization from the student-facing experience.

## Fixed-commit expert-skills follow-up

After Drew supplied the complete [`mattpocock/skills`](https://github.com/mattpocock/skills) and [`davidondrej/skills`](https://github.com/davidondrej/skills) repositories, a second primary-source pass inspected both at fixed commits instead of relying only on their public overview documentation. The detailed evidence and line-linked implications are in [`PORTABLE-PLANNER-EXPERT-SKILLS.md`](PORTABLE-PLANNER-EXPERT-SKILLS.md).

That pass strengthens—not replaces—the conclusion above: use Matt's prerequisite-aware decision frontier, facts-versus-decisions split, explicit plan/build handoff, local linked state, and one-session vertical-slice tickets; combine it with David's single-next-decision rhythm and immediate durable write-through. Drew's `A/B/C(/D)` interface, recommendation always first as `A`, route-first visual, and ordinary-reply length calibration remain deliberate product adaptations rather than claims about either expert's exact interface.
