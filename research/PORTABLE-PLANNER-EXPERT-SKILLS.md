# Portable Planner: Expert Skills Evidence

Research date: 2026-08-05

Primary repositories inspected at fixed commits:

- [mattpocock/skills at `8b36d4f`](https://github.com/mattpocock/skills/tree/8b36d4fb2635b3c21998dcd8144439c9e5ba7302) (`v1.2.2`)
- [davidondrej/skills at `04bd15a`](https://github.com/davidondrej/skills/tree/04bd15abae135f5744e3dc825a4ab9c75d61fbfc)

This report treats the repositories as primary evidence for their authors' workflows. Product rules below that combine or change those workflows are explicitly marked as implications, not attributed to either author.

## Bottom line

The strongest reusable design is not a giant planning framework. It is a small stateful loop:

1. Maintain an internal tree of unresolved decisions and their prerequisites.
2. Ask the single most consequential decision that is ready now.
3. Give a few viable choices and state the agent's recommendation.
4. Research discoverable facts instead of asking the user.
5. Save each answer immediately into plain project-local state.
6. Stay in planning until the route, proof, scope, and next execution slice are clear.
7. Build from small, verifiable tickets in fresh contexts; feed newly discovered product decisions back into planning.

David Ondrej's `next-decision` is the closest direct precedent for Drew's desired interaction: it says to handle open decisions **one at a time**, select the most important unresolved one, provide four choices, state a preference, stop, save the answer, and repeat ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/thinking-and-docs/next-decision/SKILL.md#L1-L14)). Matt Pocock supplies the stronger reasoning engine beneath that surface: model decisions as a prerequisite-aware design tree, ask only the ready frontier, distinguish facts the agent can discover from decisions the user must make, and wait for shared understanding before acting ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/productivity/grilling/SKILL.md#L6-L22)).

Matt's default asks the whole independent frontier in a round, not one question per turn ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/docs/productivity/grilling.md#L43-L55)). Therefore, **one question at a time and lettered A/B/C/D replies are deliberate Drew-specific product rules**, not faithful copies of Matt's current interface.

## Evidence-backed product implications

### 1. The question engine

Evidence:

- David's `next-decision` chooses the most important unresolved decision, offers four choices, gives a preference, then stops and waits ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/thinking-and-docs/next-decision/SKILL.md#L6-L14)).
- David's `before-building` says to surface only one to three truly consequential hidden choices, keep options brief, recommend an answer, and skip minor questions ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/thinking-and-docs/before-building/SKILL.md#L7-L12)).
- Matt models the interview as a design tree. A question is ready only when its prerequisites are settled; every question carries a recommendation ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/productivity/grilling/SKILL.md#L6-L18)).
- David's adaptive assessment anchors questions in the real project, varies territory, and asks about systems, failure modes, strategy, and economics rather than syntax trivia ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/thinking-and-docs/level-up/SKILL.md#L18-L32)).

Product implication:

The plugin should maintain many candidate questions internally but expose exactly one. Select it with this pass/fail filter:

- **Consequential:** a different answer materially changes destination, scope, route, proof, ownership, or risk.
- **Ready:** it does not depend on another unsettled decision.
- **Human-owned:** the answer requires Drew's preference or authority, not information the agent can inspect or research.
- **Grounded:** it uses the project's real language and current state.
- **Answerable:** A/B/C, with D only when a fourth genuinely strong choice exists; choices are distinct, viable, and written in plain language.
- **Opinionated:** mark the recommended choice and explain the deciding trade-off in one short sentence.
- **Durable:** after a one-letter answer, save the full question, selected meaning, rationale, and plan impact before asking anything else.

The letter convention comes from Drew's tested preference. Neither repository supplies a dependable A/B/C/D contract.

### 2. PLAN and BUILD are separate states

Evidence:

- Matt's `wayfinder` is explicitly "Plan, don't do": decision tickets clarify the route, and the urge to execute signals a handoff boundary ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/wayfinder/SKILL.md#L7-L13)).
- Matt's main flow is interview -> optional prototype -> spec -> execution tickets -> implement. Multi-session work uses a fresh context for each self-contained ticket ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/ask-matt/SKILL.md#L13-L30)).
- A large decision map must collapse into a spec before implementation; jumping directly from map to build loses linked decision detail ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/ask-matt/SKILL.md#L44-L46)).
- Matt's `implement` skill accepts a spec or tickets, runs repeated tests, performs a final review, and commits only afterward ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/implement/SKILL.md#L1-L15)).

Product implication:

- **PLAN mode** is the plugin: it asks and records decisions, performs research or prototypes needed to answer them, and produces the visual plan plus execution tickets. It does not silently start delivery.
- **BUILD mode** means the current harness's normal implementation behavior consuming an approved ticket. Portable Planner does not replace, prescribe, or expand that build system.
- If implementation exposes a new consequential human decision or invalidates the plan, the harness can invoke Portable Planner again to revise the canonical state before implementation continues.
- The approved plan/build handoff must be explicit in the durable artifact, so a fresh agent never guesses whether implementation is authorized.

### 3. Research is dynamic support, not a questionnaire burden

Evidence:

- Matt says environmental facts are the agent's job. A research dependency can run in a subagent while unrelated ready decisions continue ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/productivity/grilling/SKILL.md#L18-L20)).
- Matt's research skill requires primary sources and a cited Markdown artifact written by a background agent ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/research/SKILL.md#L1-L12)).
- Matt's large-plan flow launches independent research tickets in parallel and stores context pointers back on the plan map ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/wayfinder/SKILL.md#L103-L126)).
- David's research-prompt workflow requires one decision-focused mission, complete context, three to six coverage questions, primary sources, contradiction handling, a gap pass, and one Markdown output ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/research-and-web/research-prompt/SKILL.md#L8-L38)).

Product implication:

When a planning decision needs facts, create a bounded research question tied to that decision, save a cited report locally, and feed only its decision-relevant findings back into the plan. Do not hard-code one research provider, fixed sources, or domain pack into the planning skill. Delegation is opportunistic: use it only when the harness supports it and the task is independent; the canonical workflow must still work in a single agent.

### 4. Durable state should be small, local, and non-duplicative

Evidence:

- David's `brain-to-docs` reads existing state before every round and updates Markdown after every answer, separating vision from decisions ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/thinking-and-docs/brain-to-docs/SKILL.md#L8-L32)).
- Matt's wayfinder map is a low-resolution canonical index. Detailed decisions live once, in their ticket; the map links and summarizes instead of duplicating them ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/wayfinder/SKILL.md#L19-L25)).
- Matt's domain-modeling workflow captures resolved terms immediately but reserves ADRs for choices that are hard to reverse, surprising without context, and based on a real trade-off ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/domain-modeling/SKILL.md#L40-L73)).
- David's handoff rules say to record state rather than commands, reference existing artifacts rather than duplicate them, and preserve why, failed approaches, relevant files, and open work ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/agent-orchestration/handoff/SKILL.md#L9-L29)).

Product implication:

Use a plain project-local planning directory with one source of truth for each kind of state:

- a low-resolution plan: destination, current mode, current state, scope, route, proof, and links;
- a next-action pointer: the one question or ticket that resumes immediately;
- a decision record updated after each answer;
- one file per execution ticket;
- optional cited research or prototype artifacts linked from the relevant decision.

The visual graph is a **view derived from that state**, not a competing plan document. A fresh session must be able to read the plan and next-action pointer, restate the current state briefly, and continue without repeating settled questions.

### 5. Execution tickets must carry behavior, proof, and dependency edges

Evidence:

- Matt's tickets are narrow but complete end-to-end tracer bullets, independently demonstrable or verifiable, sized for one fresh context, with explicit blockers ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/to-tickets/SKILL.md#L25-L40)).
- The user reviews granularity, blockers, and split/merge decisions before publication ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/to-tickets/SKILL.md#L42-L56)).
- The local ticket format includes user-visible behavior, blockers, ready status, and acceptance criteria in one Markdown file per ticket ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/skills/engineering/to-tickets/SKILL.md#L58-L105)).

Product implication:

Every build ticket should answer: what observable outcome becomes real, what must already be true, what evidence proves completion, which constraints must remain true, and what failure returns the work to planning. Avoid layer-only tasks and brittle implementation instructions unless the plan deliberately fixed them. Tickets are the contract with the harness's normal build workflow and the fresh-session handoff.

### 6. Portability belongs in the core format; presentation and invocation need adapters

Evidence:

- Matt describes the skills as small, adaptable, composable, and model-independent ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/README.md#L15-L19)). His Claude Code path is a native plugin, while Codex and other agents can receive ordinary editable skill files through `skills.sh` ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/README.md#L25-L70)).
- Matt's repository pairs Claude-specific frontmatter with `agents/openai.yaml` for Codex rather than assuming one invocation control works everywhere ([source](https://github.com/mattpocock/skills/blob/8b36d4fb2635b3c21998dcd8144439c9e5ba7302/.agents/invocation.md#L1-L10)).
- David's authoring guide uses the canonical `SKILL.md` plus optional `scripts/`, `references/`, and `assets/`, but warns that invocation controls are client-specific and must be tested per runtime ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/skill-authoring/effective-agent-skills/SKILL.md#L12-L24), [source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/skill-authoring/effective-agent-skills/SKILL.md#L90-L107)).
- David recommends repo-level persistent artifacts, explicit interfaces between skills, validation loops, and testing with the weakest target model ([source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/skill-authoring/effective-agent-skills/SKILL.md#L163-L200), [source](https://github.com/davidondrej/skills/blob/04bd15abae135f5744e3dc825a4ab9c75d61fbfc/skills/skill-authoring/effective-agent-skills/SKILL.md#L244-L265)).

Product implication:

Keep the MVP as one canonical Agent Skill with directly linked references and Markdown templates, plus the ordinary project-local artifacts above. Natural-language triggering must live in the skill description and be tested, but harness-specific metadata or rich visualization calls are thin adapters. Do not make the plan format depend on Codex inline HTML. Codex can render the richer view; another harness can render Mermaid, HTML, or plain Markdown from the same saved state without changing the plan.

The first version should not reproduce machine-specific symlink layouts or require GitHub, an issue tracker, MCP, or a research API. Those are distribution or capability options, not requirements of the planning logic.

## Patterns to adopt, adapt, and defer

### Adopt now

- Prerequisite-aware decision tree and fact-versus-decision split.
- Single most consequential ready decision per turn.
- Concise choices plus explicit recommendation.
- Immediate write-through after every answer.
- Explicit planning/build boundary and approved handoff.
- Canonical low-resolution plan with links to detailed single-source artifacts.
- End-to-end execution tickets sized for one fresh context.
- Verify -> fix -> re-verify before claiming completion.
- Primary-source research saved locally when facts genuinely block a decision.

### Adapt for Drew

- Matt's multi-question frontier becomes one visible question while the full frontier remains internal.
- Choices become A/B/C, with D only when useful, and the user may answer with one letter.
- The recommendation is placed first or unmistakably labeled.
- The plan view is short and visual; detail appears on demand from the same canonical state.
- Planning covers software, business, creative, operational, and personal projects, so tickets describe observable outcomes rather than assuming code layers.

### Defer until a failed pilot proves the need

- Multiple collaborating planning skills instead of one canonical skill.
- A database or issue tracker as canonical state.
- Mandatory subagents, a fixed research provider, or a domain pack.
- Harness-specific rich UI beyond thin presentation adapters.
- A heavy wayfinder map for plans that fit comfortably in one session.

## Acceptance tests implied by the evidence

1. A fresh session reads the local state and asks the correct next question without repeating a settled one.
2. Every user-facing planning turn contains only one consequential A/B/C(/D) decision and a clear recommendation.
3. The agent answers discoverable factual questions itself or researches them; it does not offload them to Drew.
4. Portable Planner never starts implementation without explicit human approval and handoff.
5. The harness's normal build workflow can complete a ticket from its artifact alone and returns to planning only for a new consequential decision or genuine blocker.
6. Every ticket has an observable outcome, blockers, acceptance proof, constraints, and a failure path.
7. The visual view and Markdown artifacts agree because the visual is generated from the canonical state.
8. Natural-language invocation and unchanged project-state resumption pass in Codex and at least one non-Codex harness.
9. Simple and complex pilots expose failures as concrete observations, followed by fix and rerun, before any architecture is added.

## Research conclusion

The repositories strongly support Drew's core instinct: planning quality comes from better decision selection, recommendations, durable state, and explicit handoffs—not from asking more questions or generating a longer plan. The best MVP is a small, opinionated interview-and-state skill whose hidden reasoning can be sophisticated while every visible turn stays short.
