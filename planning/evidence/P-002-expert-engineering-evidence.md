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

This is an inference from the sources and Portable Planner's own failure history, not a claim that either creator prescribed this exact architecture.
