# P-002 evidence — Expert engineering patterns for the next improvement

Researched: 2026-08-15

## Scope and method

This pass compared Portable Planner beta 6 with the current public skill repositories and with timestamped excerpts from the existing Channel Brains indexes for Matt Pocock and David Ondrej. Repository source is the authority for workflow mechanics; creator captions add rationale and cautions. The local brains contain the fifty view-count-selected videos indexed for each channel on 2026-08-05, so they are useful but not exhaustive.

Current repository snapshots:

- [mattpocock/skills at `8b78b53`](https://github.com/mattpocock/skills/tree/8b78b531ab965735c5dc74f6f7a219e1e37326df)
- [davidondrej/skills at `62ed9fe`](https://github.com/davidondrej/skills/tree/62ed9fe998f6e6b6ab724e301cdeb60f3a6c5b50)

The repositories are untrusted third-party inputs. No script or instruction from them was executed inside Portable Planner.

## Findings

### 1. Portable Planner already has the right visible interaction primitive

Matt's current grilling source models the subject as a decision tree, recomputes a prerequisite-ready frontier after every answer, and separates discoverable facts from human decisions ([source](https://github.com/mattpocock/skills/blob/8b78b531ab965735c5dc74f6f7a219e1e37326df/skills/productivity/grilling/SKILL.md#L6-L22)). David's `next-decision` selects the most important unresolved decision, recommends an answer, records the response, and continues concisely ([source](https://github.com/davidondrej/skills/blob/62ed9fe998f6e6b6ab724e301cdeb60f3a6c5b50/skills/thinking-and-docs/next-decision/SKILL.md#L6-L14)). Matt also describes the design-tree and fact-versus-decision split directly in [5 Claude Code skills I use every single day at 1:32](https://youtu.be/EJyuu6zlQCg?t=92).

**Implication:** copying another visible question style is unlikely to be the next major gain. Portable Planner's one-question, recommendation-first, lettered interface is already a deliberate synthesis of these patterns.

### 2. The real unsolved problem is the hidden frontier's reliability

Matt's own current documentation says the frontier is model judgment rather than a computed graph and can discover too late that one question should have depended on another ([source](https://github.com/mattpocock/skills/blob/8b78b531ab965735c5dc74f6f7a219e1e37326df/docs/productivity/grilling.md#L25-L31)). Wayfinder strengthens the conceptual model with explicit ticket types, prerequisites, ownership, and a frontier of open, unblocked work ([source](https://github.com/mattpocock/skills/blob/8b78b531ab965735c5dc74f6f7a219e1e37326df/skills/engineering/wayfinder/SKILL.md#L55-L80)), but this still depends on the model honoring the mode.

Current open Wayfinder reports show the concrete failure: agents may treat a human-in-the-loop label as descriptive metadata and autonomously resolve the decision anyway ([workflow-gate report](https://github.com/mattpocock/skills/issues/540)).

**Implication:** Portable Planner should make its hidden planning kernel explicit enough to inspect and test: prerequisites, owner, uncertainty type, selected action, protected status, and the state mutation expected after the turn. This belongs in the existing planning ticket and one normative reference, not a second product state tree.

### 3. Deterministic guards and judgment should be engineered differently

David's authoring guide says fragile or repetitive behavior should move into deterministic code, while judgment remains in prompts; it also calls the verify-fix-reverify loop the largest output-quality improvement ([source](https://github.com/davidondrej/skills/blob/62ed9fe998f6e6b6ab724e301cdeb60f3a6c5b50/skills/skill-authoring/effective-agent-skills/SKILL.md#L148-L168)). Matt's logic-prototype guide similarly recommends a pure reducer or explicit state machine when legal actions and transitions are the question ([source](https://github.com/mattpocock/skills/blob/8b78b531ab965735c5dc74f6f7a219e1e37326df/skills/engineering/prototype/LOGIC.md#L18-L33)).

**Implication:** do not attempt to code the subjective choice of the “best” planning question. Code only invariant checks and trace validation—choice labels, legal transitions, state write-through, protected gates, artifact agreement—and leave consequentiality and recommendation quality to an explicit rubric plus human review.

### 4. More instructions can make the skill worse

Matt warns that unnecessary repository context burns tokens, distracts the agent, and rots quickly in [Never Run claude /init at 0:00](https://youtu.be/9tmsq-Gvx6g?t=0). He also argues that concise global instructions preserve more instruction budget in [I was an AI skeptic. Then I tried plan mode at 8:48](https://youtu.be/WNx-s-RxVxk?t=528). David's interview with Matt repeats the same caution: skill descriptions leak into context and skills are hard to write well ([Matt Pocock's Agentic Engineering Workflow at 20:44](https://youtu.be/nQwJVHCtDDY?t=1244)); the closing recommendation is to remove accumulated machinery and observe the baseline first ([same video at 60:22](https://youtu.be/nQwJVHCtDDY?t=3622)).

David's guide formalizes the same engineering rule: keep `SKILL.md` lean, load references just in time, and add only after real testing reveals a gap ([source](https://github.com/davidondrej/skills/blob/62ed9fe998f6e6b6ab724e301cdeb60f3a6c5b50/skills/skill-authoring/effective-agent-skills/SKILL.md#L134-L185)).

**Implication:** the improvement program needs a deletion budget. Every added instruction must replace ambiguity or satisfy a failed eval; otherwise it should not enter the canonical skill.

### 5. Improvement needs a hybrid evaluation loop, not autonomous prompt evolution

David recommends testing triggering separately from execution, adversarial cases, weakest-target-model runs, and a representative eval suite ([source](https://github.com/davidondrej/skills/blob/62ed9fe998f6e6b6ab724e301cdeb60f3a6c5b50/skills/skill-authoring/effective-agent-skills/SKILL.md#L244-L265)). His AutoResearch explanation adds an important limit: autonomous optimization needs one clear metric, no human bottleneck, and one mutable surface; subjective UX and pricing usually fail that test ([The only AutoResearch tutorial you'll ever need at 9:55](https://youtu.be/uBWuKh1nZ2Y?t=595)). Feedback should become a regression test rather than another intuition-driven rewrite ([Why This Dev Ships 100x Faster Than 99% of Engineers at 21:10](https://youtu.be/PzVV4X37ihg?t=1270)).

**Implication:** Portable Planner should not run an open-ended self-improvement loop. Use deterministic hard gates plus scored behavioral metrics and a final uncoached human judgment.

## Recommended measurement contract

Hard failures—any one blocks release:

- protected-gate violation;
- human-owned decision answered without delegation;
- factual or inspectable question transferred to the person;
- repeated or already-settled question;
- canonical state and visible reply disagree;
- resumption loses or invents a decision;
- implementation begins before approval.

Directional metrics—compare beta 6 with a candidate rather than pretending one number defines quality:

- consequential-question yield: useful human-owned decisions divided by questions asked;
- turns to a defensible approval surface;
- missed consequential decisions found by a held-out review;
- ordinary reply word count and choice validity;
- state-drift and recovery rate;
- variance across repeated runs of the same scenario;
- Drew's uncoached judgment of speed, question value, and plan usefulness.

## Provisional recommendation

Build a small **decision-kernel and evaluation loop**, not a larger planning framework:

1. Write one normative transition table for uncertainty type, owner, prerequisites, allowed action, state mutation, and protected gates.
2. Add a compact frontier ledger to the existing active planning ticket so fresh sessions can inspect the next decision without relying on chat memory.
3. Create a bounded scenario corpus spanning invocation, thin-idea research, fact-versus-decision routing, digressions, delegation, resumption, trials, approval, and prohibited actions.
4. Add deterministic validators only for objective invariants; use a fixed rubric and held-out human review for judgment quality.
5. Compare immutable beta 5 and beta 6 on frozen shared scenarios, then establish the winning version as the reference before changing instructions.
6. Make one targeted revision per demonstrated failure class, then rerun the affected, regression, and held-out cases.
7. Ship a later prerelease only if hard gates remain perfect and the directional metrics improve without increased context bloat.

## 2026-08-15 correction — design tests from real failures first

The first plan derived a 30-run allocation before the exact cases were defined. Drew rejected that order. Existing evidence already supplies higher-value starting points:

- The [beta-4 live record](../../validation/DECISIVE-FLOW-LIVE-ACCEPTANCE.md) shows the planner optimizing a text-profile interpretation before confirming whether source images must remain direct inputs, silently narrowing the product after inspecting an older repository, asking several reversible recommendations in succession, and turning the first live test into a five-field intake even though most fields were known or optional.
- The original Pinterest task, re-read through Codex task history on 2026-08-15, confirms those were visible interaction failures rather than only retrospective labels. It also shows that later implementation and research succeeded once Drew corrected the product meaning, which makes “understand the value-bearing input before optimizing mechanics” a more important test claim than generic plan completeness.
- [Beta 5 objective evidence](../../validation/BETA5-RELEASE-CANDIDATE-TEST.md) proves several targeted instruction repairs, while [beta 6 objective evidence](../../validation/BETA6-RELEASE-CANDIDATE-TEST.md) proves the exact delegation shortcut matrix. Neither proves that the broader planner understands a new situation or asks the right question.

Each proposed behavioral case must therefore begin with a named real failure or an explicit product claim. The durable case contract is: exact project state; exact natural user turn; why the case matters; expected planning/build/research route; required visible behavior; prohibited shortcut or assumption; objective invariant; human judgment; and the decision that a pass or failure changes. Repetitions are added only after a first pass reveals variance or when a protected high-risk behavior needs confirmation.

## GStack mechanisms worth adapting—and its warning

Primary sources inspected on 2026-08-15:

- [GStack workflow routing](https://github.com/garrytan/gstack/blob/main/AGENTS.md) assigns idea shaping, strategy, engineering review, QA, investigation, and shipping to distinct routes. Its [office-hours skill](https://github.com/garrytan/gstack/blob/main/office-hours/SKILL.md) proactively invokes for new product ideas, loads prior project context before clarification, and selects stage-relevant forcing questions rather than always asking every question.
- [Plan Tune](https://github.com/garrytan/gstack/blob/main/plan-tune/SKILL.md) records question identity, category, recommendation, and user response locally so repeated noisy questions can be inspected and eventually tuned. Portable Planner can adopt the smaller principle—record whether a question changed the plan and whether Drew found it valuable—inside existing evidence artifacts, without adding GStack's user-profile system.
- GStack's [pacing design](https://github.com/garrytan/gstack/blob/main/docs/designs/PACING_UPDATES_V0.md) records that roughly 30–50 interruptions across four review phases caused nontechnical users to disengage around 10–15 interruptions. It explicitly says rewriting an interruption does not fix interruption volume. This directly argues against importing its multi-review ceremony or selecting a large test/question count as a quality proxy.
- GStack's [skill-eval proposal](https://github.com/garrytan/gstack/issues/24) frames tests around each skill's specific behavioral claims. That structure is useful, but the proposal itself does not establish that authored scenarios predict real user satisfaction.

Provisional recommendation: make Portable Planner the adaptive default for unresolved project/product discussion, not literally every non-build message. A status explanation, narrow fact, or diagnosis request should remain direct; a discussion that is still negotiating destination, scope, success, proof, or a meaningful tradeoff should automatically start or resume planning. Preserve one canonical planner and its existing state rather than copying GStack's role pack, telemetry, profile, or large generated skills.

This is an inference from the sources and Portable Planner's own failure history, not a claim that either creator prescribed this exact architecture.
