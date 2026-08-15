# Portable Planning Plugin — MVP Plan

**Status:** Confirmed MVP destination. Experimental implementation exists; live validation and human acceptance remain incomplete.

## Destination

Create an extremely easy planning plugin that lets a person begin with no product idea, a thin idea, or one vague idea and finish with:

1. one cohesive plan reaching the intended final result;
2. every important decision settled or explicitly researched;
3. ordered execution tickets that another agent can perform; and
4. an exact starter for the next fresh session at every handoff.

The plugin is for any project type or size. It assumes no technical or project-management knowledge and keeps reading load very low.

## MVP user

A person who has either a rough idea or one real-world problem, audience, workflow, frustration, asset, or area of access, but does not yet know which software direction is feasible or how to turn it into a complete plan across fresh AI-agent sessions.

They should need only:

- access to a capable AI harness;
- one sentence describing the idea or real-world starting point; and
- a local folder where the planning files can live.

No GitHub account, issue tracker, database, web app, or terminal knowledge is required.

## Core experience

### Start

The user says something natural such as:

```text
Plan this idea: ...
```

The plugin restates the destination briefly, identifies the first meaningful uncertainty, and begins.

For a new software or AI project with no idea or only a thin idea, the first meaningful uncertainty is whether to run a short possibility scan. The plugin asks permission once, recommends the scan, and offers an immediate ordinary-planning route. With consent, it grounds a directionless start in one real-world anchor, forms a privacy-safe one-sentence brief, and performs the bounded repository-first flow in the [product contract](PRODUCT-CONTRACT.md#idea-stage-possibility-scan). The result is one provisional recommendation plus at most two materially different alternatives; the person confirms, combines, or redirects it before canonical planning adopts a direction.

### Decide whether a map is needed

- If the entire route can be settled reliably in one session, the plugin completes a normal plan in that session.
- If meaningful uncertainty or scope remains, it creates an adaptive planning map.
- A simple project can have one planning ticket. A large project can have many.

### Planning map

Canonical map state is a plain ordered list, not a graph:

```text
PLAN: Start a food truck                         3/8

✓ Destination
✓ Customer
▶ Offer — working here now
○ Costs
○ Launch plan
! Permits — blocked until local rules are researched
```

During ordinary conversation, the user sees only compact progress and the current step:

```text
3/8  ▶ Offer
Next: Costs

What should customers buy first?
```

The full map is always available on request. The agent may offer a useful draft once when it would help judge direction, and opens the finished review automatically when the plan is defensible.

### Visual plan

When destination, success, current state, next action, and a coherent route are known, the plugin generates a route-first visual from canonical project-local state. It shows destination/current/next first and compresses the complete plan into one dominant route of five to nine plain-language outcome milestones. Architecture and supporting systems stay in selected-step detail instead of competing with the route. Selecting a milestone reveals its outcome, owner, inputs, proof, and failure or change behavior.

The visual uses an adaptive hybrid gate rather than a fixed question count. It is always available on request; the agent may offer it once as a useful draft; and it opens automatically for final review only when destination, observable success, boundaries, major human decisions, end-to-end order, important dependencies and gates, risks and recovery, execution tickets, and canonical artifacts form a defensible whole. It also refreshes after a major route change when the prior view would mislead and appears in the first reply after a fresh resume when a coherent route exists.

Codex prefers the approved interactive presentation: destination/current/next summary cards, a clickable ordered route, one selected-step detail surface, compact support connections, and a short safety line. A raster screenshot is never substituted unless the user explicitly asks to export one. Other harnesses use Mermaid, Markdown, or the compact text route according to their capabilities. The experience requires no separate renderer or download and never becomes a second source of truth.

At final review the lifecycle is `awaiting approval`. Approval authorizes handoff to the harness's first execution ticket. A targeted change returns only the affected human decision to planning; “keep planning” resumes the highest-value unresolved decision; confusion pauses questions and explains the current state.

### Work one planning ticket

The plugin automatically selects the next unblocked ticket. It never asks the user to choose internal workflow or technical routing.

Each ticket may require:

- a human preference decision;
- narrow factual research;
- a cheap decision-only prototype when words are insufficient; or
- direct synthesis when the answer is already known.

Research uses primary/direct sources, saves links and evidence, and stops when more sources are unlikely to change the decision. A prototype exists only to settle a planning choice; it is not production work.

### End a planning ticket

A ticket is complete only when:

- its decisions are explicit and saved;
- evidence is linked when facts affected the decision;
- contradictions and downstream effects are reconciled;
- no unresolved issue blocks the next ticket; and
- the plugin has generated the exact next-session starter.

The map may add, remove, split, merge, or reorder tickets as understanding improves.

### Finish planning

Planning stops when:

- the destination is unambiguous;
- all planning tickets are resolved;
- no major choice remains unspecified;
- the plan is internally consistent;
- remaining work is execution; and
- execution tickets cover the complete route to the intended result.

The user reviews the short final overview before execution begins. A direct `yes` to the approval question authorizes the harness to begin the first eligible execution ticket immediately when safe; the agent does not stop merely to ask whether it should build.

## Conversation contract

The plugin must:

1. Ask at most one question per turn.
2. Ask only about meaningful preferences or direction choices with multiple viable answers.
3. Derive obvious process and technical choices itself.
4. Research external facts instead of asking the user to guess.
5. Offer two or three short, genuinely viable choices when choices help; add more only when each is meaningfully distinct and never exceed seven.
6. Label choices consecutively from `A` through at most `G`, and always place the concise recommendation first as `A` with its main tradeoff.
7. Always accept a custom answer.
8. Show a small concrete example before asking about an abstract concept.
9. Remember and apply previous answers instead of asking disguised repeats.
10. Challenge unnecessary scope and contradictions directly but briefly.
11. Default to a few short lines, aim around 40 words, and keep ordinary planning replies under 80 words; requested evidence or a required approval view may genuinely need more.
12. Never describe users by intelligence labels; optimize for low reading load and no assumed expertise.

The plugin must not offer an option that clearly contradicts an already confirmed preference merely to manufacture a choice.

If the user explicitly delegates a defined group of reversible decisions to the plugin's recommendations, the plugin records the exact scope and applies the recommended routes without continuing to ask inside it. Repeated agreement alone is not delegation. Only a complete trimmed one-letter reply matching the recommended option increments the durable streak; added words or punctuation and every other reply reset it. After three qualifying replies, the next real reversible question keeps its recommendation as `A`, inserts the remaining-recommendations shortcut as `B`, and shifts other routes to `C` through at most `G`. Bare `B` grants delegation, applies the current recommendation, completes remaining reversible decisions, and stops at the first protected gate. The plugin still pauses for irreversible commitments, material personal tradeoffs the delegation did not clearly cover, conflicts, implementation authorization, and final-plan approval.

After a side question, challenge, or context-rich paragraph, the planner answers or reconciles first, recomputes the frontier, and restores the complete lettered choice at the bottom whenever a worthwhile human decision remains.

The plugin stops asking when facts, prior words, or delegation already settle the issue, or when another verbal answer is unlikely to change the plan. Experiential uncertainty becomes one bounded decision trial, normally using an ordinary case, a materially contrasting case, and a failure or prohibited-action case. Inputs, outputs, variations, failures, verdict, and the changed decision remain durable planning evidence; prototype work never becomes production implementation.

Research or reused-project evidence cannot silently redefine the destination, audience, deliverable, success proof, or value-bearing source material. Such a change remains provisional until the person confirms it or a bounded planning trial settles it.

When the next safe planning action is clear, the agent performs it in the same turn rather than ending with an intention statement. An immediate `yes` to a direct approval question counts as explicit authorization and transitions into the normal harness build without a second permission question. After agent checks pass, the smallest genuine user test is presented proactively.

If an unrelated idea appears during planning, the plugin preserves the current plan and resolves whether to switch or separate it instead of silently combining destinations. If a tool, file, display, research step, or handoff fails, it names the failure, preserves trustworthy state, gives one recovery action, and continues through a supported fallback when possible.

After agent-run build checks, the plugin refreshes canonical status, the visual view, and the handoff before presenting a live test. It reuses known context, gives the smallest concrete action, applies safe defaults, and asks no more than one genuinely blocking human question.

At a demonstrated session boundary, the plugin saves state first, then either creates one successor when the person authorized automatic continuation or shows a clearly labeled exact next-session prompt. Merely naming the next ticket or saying another session is needed is not a completed handoff.

## Durable output contract

Canonical state lives in plain local files inside the user's project folder:

```text
planning/
├── PLAN.md
├── PLAN-VIEW.md
├── NEXT.md
├── decisions/
│   └── P-001-short-title.md
├── evidence/
│   └── P-001-evidence.md
└── execution/
    └── E-001-short-title.md
```

### `PLAN.md`

A short home page containing only:

- destination;
- success definition;
- boundaries;
- compact map with status and dependencies;
- confirmed decisions summarized in one line each;
- links to detailed decision and execution tickets; and
- current/next action.

It is never a long duplicate of every linked artifact.

### Planning ticket

Each `P-*` file contains:

- stable ID and title;
- status and dependencies;
- the decision being resolved and why it matters;
- viable options and tradeoffs when applicable;
- recommendation;
- the human's confirmed decision;
- evidence links when used;
- effects on the rest of the map; and
- an objective completion check.

### `NEXT.md`

Contains a paste-ready starter for a fresh session with:

- the plan location;
- the one ticket to work;
- essential context only;
- instructions to load canonical files rather than trust chat memory;
- what the session must decide or produce; and
- the ticket's completion test.

Losing `NEXT.md` must not lose the plan; another agent can regenerate it from `PLAN.md` and the linked ticket.

### Execution ticket

Each `E-*` file is sized for one fresh agent session and contains:

- one outcome;
- necessary context and linked decisions;
- dependencies;
- exact in-scope work and exclusions;
- proof required for completion;
- human review required, if any; and
- the next eligible ticket after completion.

Oversized execution tickets are split before planning is declared complete.

## MVP boundary

### Included

- an optional, consented idea-stage possibility scan for new software or AI projects with no idea or a thin idea;
- bounded public-repository discovery, evidence-tier claims, licensing and untrusted-content safeguards, and a no-account ordinary-planning fallback;
- idea intake and destination clarification;
- conditional one-session or multi-session planning;
- adaptive planning map;
- decision, research, and decision-prototype routing;
- local durable artifacts;
- exact fresh-session handoffs;
- final cohesive plan and ordered execution tickets;
- a generated route-first visual plan with a compact text route;
- review for omissions, contradictions, dependencies, and completion criteria;
- simple and complex project testing; and
- portable installation/invocation guidance.

### Excluded from the first MVP

- performing final execution work;
- a web dashboard or separate visual application;
- MCP server;
- database or cloud account;
- required GitHub usage;
- issue-tracker integration;
- collaboration, permissions, or multi-user sync;
- automatic scheduling or notifications;
- domain-specific planning packs;
- multiple personas or agent-role selection; and
- slash-command-only operation.

These can be added only after live use exposes a clear need.

## Portability model

The MVP uses one canonical Agent Skill package as the planning brain:

```text
portable-planner/
├── SKILL.md
├── references/
│   ├── conversation-contract.md
│   ├── artifact-contract.md
│   ├── visual-contract.md
│   └── validation-rubric.md
└── templates/
    ├── PLAN.md
    ├── PLAN-VIEW.md
    ├── NEXT.md
    ├── planning-ticket.md
    └── execution-ticket.md
```

Harness-specific adapters should only locate and invoke the same core skill. Planning state stays in the user's project, not inside a harness, so Codex, Hermes, Claude Code, or a custom harness can resume it.

The first implementation deliberately avoids MCP and a persistent runtime because the MVP needs instructions, local files, and templates—not a network service or privileged tool. Add deterministic scripts only if live testing proves agents cannot keep the artifact contract reliable without them.

## Installation and invocation

### Installation promise

The user gives an agent one natural-language instruction plus either a local package, download archive, or optional public repository URL. The installer:

1. detects the current harness;
2. places the skill in the correct user-level location;
3. verifies the skill can be discovered;
4. runs a tiny smoke planning interaction; and
5. reports success or one precise recovery step.

GitHub configuration or an account is never required. A public repository may be one optional distribution source later.

### Invocation promise

No command memorization is required. Natural language must work:

```text
Plan this idea: ...
Continue my plan.
Show my full plan map.
Prepare the next session.
```

Harness-specific commands may exist as conveniences, not as the core experience.

## Validation standard

### Conversation checks

- one question maximum per turn;
- no obvious or already-answered question;
- no technical choice transferred to a non-technical user;
- two or three real options only when multiple good routes exist, with a fourth only when genuinely distinct;
- stable consecutive `A` through at most `G` labels, with the recommendation always first as `A`;
- concrete example before abstract UX choices;
- ordinary replies default to a few short lines, aim around 40 words, remain under 80 words, and preserve useful context;
- settled or delegated choices are synthesized without ceremonial questions;
- experiential uncertainty switches to a preserved three-case decision trial instead of more verbal grilling;
- direct approval starts the normal harness build without another permission request; and
- validated work proactively tells the user the smallest genuine test;
- the user always knows current progress and what happens next.

### State and handoff checks

- every confirmed decision is durable before context is cleared;
- a fresh agent can resume from local files alone;
- `NEXT.md` names exactly one planning ticket;
- dependencies prevent blocked tickets from being selected;
- changed decisions reconcile affected tickets;
- the short overview never becomes a duplicate long document;
- every execution ticket fits one fresh session; and
- planning cannot finish with unresolved major choices or missing completion tests.

### Project-type checks

The same core skill must be exercised against at least:

1. Drew's first ordinary real plan after installation;
2. one naturally complex real plan;
3. one software product;
4. one content or creative project;
5. one event or operational process; and
6. one personal project.

The first ordinary plan and one naturally complex plan must be run as full real-use sessions with Drew from fresh context and without test coaching. The others may begin as structured adversarial walkthroughs, then become real-use tests if they expose gaps.

### Portability checks

- the same canonical skill works in Codex;
- the same canonical skill works in at least one non-Codex harness;
- switching harnesses preserves the project plan without conversion;
- installation requires no GitHub account or technical setup from the user; and
- failures produce a plain recovery instruction.

### Human acceptance

The MVP passes only when Drew confirms that:

- planning feels substantially faster than the current experience;
- questions are worth answering;
- replies do not feel like walls of text;
- the map and handoffs remove session-boundary confusion;
- the first ordinary and naturally complex plans are plans he would actually use; and
- the final execution tickets are clear enough to start without major planning questions.

## First real-use proof

The retired YouTube-comment finder is not the first live test. Drew starts any real plan he genuinely wants in a fresh Codex task using ordinary language and no test coaching.

That first use tests whether the plugin can turn an unprepared idea into a cohesive plan without obvious questions, walls of text, lost state, visual failure, or a bad handoff. Every demonstrated failure is recorded and fixed before the proof passes. A later naturally complex real plan must also exercise dependencies, gates, revision, recovery, and execution tickets.

## Implementation handoff

The remaining effort does **not** fit one reliable session. It needs a Wayfinder-style multi-session implementation and validation map because the skill must be built, dogfooded, corrected, portability-tested, and retested across different project types.

Recommended implementation stages:

1. Turn this MVP plan into a strict acceptance rubric and fixture set.
2. Build the smallest Agent Skill package and templates—no MCP or runtime.
3. Install the local plugin and let Drew start any ordinary real plan in a fresh task without coaching.
4. Record friction, revise the skill, and rerun the failed interaction from clean context.
5. Run one naturally complex real plan and revise again.
6. Test remaining project types for shallow or missing planning logic.
7. Verify install, resume, and handoff in Codex and one other harness.
8. Review the final plugin against this destination and perform Drew's human acceptance.

No new architecture or feature should be added unless a failed test demonstrates why it is necessary.

## Confirmed decisions from grilling

1. The plugin handles any kind or size of plan, not only buildable MVPs.
2. It can plan all the way to a large final result, including an entire business.
3. It maintains continuity across fresh sessions.
4. It uses an adaptive master map and one planning ticket per session when multiple sessions are needed.
5. It generates the exact next-session starter.
6. A ticket ends only when decisions are saved and nothing unresolved blocks the next ticket.
7. The plugin plans; the chosen harness performs final execution separately.
8. Questions are short, plain, one at a time, and assume no technical knowledge.
9. Choices default to two or three real options, add more only when necessary, never exceed `G`, keep the recommendation as `A`, and preserve a custom-answer path.
10. Finished plans include ordered execution tickets with dependencies and objective completion tests.
11. Each execution ticket fits one fresh agent session.
12. The plugin asks only genuine human-preference questions and derives or researches everything else.
13. Ordinary planning shows compact progress plus the current step; the full map is on request.
14. The finished plan is a short overview linked to detail, never one long document.
15. Abstract choices are shown concretely before the user is asked to decide.
16. The generated visual is a route-first view of canonical state, uses left-to-right rows, reveals detail on selection, and requires no separate download.
17. The finished visual plan is an explicit approval gate before artifacts are handed to the harness's normal build workflow.
18. The visual is always available, may be offered once as a useful draft, and opens final review automatically only at defensible readiness; there is no fixed question count.
19. Approval, targeted revision, continued planning, and confusion each return the plan to a defined lifecycle path.
20. Scoped “use your recommendations” delegation advances without repeated questions while preserving human control over uncovered irreversible or personal decisions.
21. Scope drift and operational failures preserve trustworthy state, remain honest, and have one clear recovery path.
22. Repeated agreement never implies delegation; explicit scoped delegation lasts until exhausted, revoked, contradicted, or blocked by a protected gate.
23. When discussion cannot further reduce meaningful uncertainty, one bounded normal/contrasting/failure trial supplies planning evidence instead of more questions.
24. The next safe action happens in the same turn; a direct `yes` to the final approval question begins normal-harness execution without a second authorization pause.
25. After agent-run validation passes, the planner or harness proactively presents the smallest genuine user test and asks for live acceptance.
26. A real session boundary produces either one successfully created authorized successor or one visible, labeled, paste-ready prompt—never a vague handoff announcement.

## Research input

[`PORTABLE-PLANNING-SYSTEMS.md`](../research/PORTABLE-PLANNING-SYSTEMS.md) compares Wayfinder, Spec Kit, OpenSpec, BMAD, Superpowers, Beads, Agent Skills, and Channel Brains using primary sources. It supports the recommended mechanics but is evidence, not a product decision.

[`PORTABLE-PLANNER-EXPERT-SKILLS.md`](../research/PORTABLE-PLANNER-EXPERT-SKILLS.md) adds a fixed-commit, line-linked inspection of the complete Matt Pocock and David Ondrej skill repositories Drew supplied. It validates the prerequisite-aware question engine, human-decisions-versus-agent-facts boundary, explicit plan/build separation, immediate Markdown write-through, fresh-context tickets, and thin harness adapters. It also identifies Drew's one-question lettered-choice surface and visual plan as intentional product improvements rather than copied expert behavior.
