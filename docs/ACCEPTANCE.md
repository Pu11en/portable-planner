# Portable Planner MVP — Pass/Fail Checklist

**Rule:** Mark a check `PASS` only with linked evidence. Any `FAIL` blocks acceptance. `H-*` checks require Drew's direct confirmation.

## Product result

- [x] **R-01 — Vague idea to cohesive plan:** The final plan reaches an unambiguous destination with success, boundaries, decisions, dependencies, and no major unresolved choice. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **R-02 — Adaptive route:** A small idea can finish in one session; meaningful uncertainty produces a compact ordered planning map that can split, merge, add, remove, or reorder tickets. [Evidence](../validation/ADAPTIVE-MAP-TEST.md)
- [x] **R-03 — Useful execution:** Ordered execution tickets cover the complete route, each fits one fresh agent session, and each has scope, exclusions, dependencies, proof, review, and next eligibility. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **R-04 — Approval starts normal build:** The planner stops before execution, displays the finished plan, and waits for explicit approval. A direct `yes` then updates canonical state and immediately starts the first safe ticket through the harness's normal build behavior without another permission request or competing build system. [Evidence](../validation/DECISIVE-FLOW-TEST.md)

## Visual plan

- [x] **V-01 — Complete at a glance:** The first view shows destination, success proof, live status, blocker, next action, complete route, dependencies, human control points, and plan-wide safety rules without becoming a wall of text. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **V-02 — Detail without loss:** Selecting a step reveals its outcome, owner, inputs/context, proof, and failure/change behavior; every important canonical decision is either visible or reachable from the visual. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **V-03 — One source of truth:** The visual is generated from and links back to canonical project-local plan state; a decision change updates both without contradiction. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **V-04 — Built in:** The canonical plugin carries its zero-dependency `PLAN-VIEW.md` template. The visual is always available, may be offered once as a useful draft, opens final review automatically at defensible readiness, refreshes after misleading major changes, and appears after fresh resume. Codex prefers the host-native interactive route presentation; Mermaid, native preview, local preview, and compact text remain fallbacks. The user installs no renderer, runtime, visual app, or download, and a display error falls back honestly in the same turn. [Evidence: completion fallback](../validation/VISUAL-DISPLAY-FAILURE.md) · [fresh-resume and major-change display](../validation/FRESH-RESUME-VISUAL-TEST.md) · [packaged template verification](../validation/CODEX-INSTALL-TEST.md) · [adaptive gate decision](../project-map/issues/01-decide-adaptive-review-gate.md)
- [ ] **V-05 — Complex proof:** Drew can use a complex real-project visual to understand the final goal, current state, end-to-end route, human gates, proof, and recovery rules without reading the underlying long-form authority first. Earlier Hanoi comprehension praise was superseded by Drew's later report that the route layout was confusing and that the raster-image presentation should not be used. [Evidence](../validation/HANOI-HUMAN-ACCEPTANCE.md) · [latest failure](../validation/VISUAL-COMPREHENSION-FAILURE.md)

## Conversation

- [x] **C-01 — One worthwhile question:** At most one question per turn; no obvious, repeated, factual, or technical-routing question is transferred to the user. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **C-02 — Good choices:** A real preference choice uses two or three viable options, or four only when necessary, and accepts a custom answer. Every option has a stable `A/B/C/D` label, the recommendation is always first as `A` with one brief tradeoff, and no choice set uses numbers or unlabeled bullets. A reply containing only the choice key resolves to and saves the full decision without repetition. [Evidence](../validation/KEYED-CHOICE-TEST.md)
- [x] **C-03 — Concrete and compact:** Abstract choices get a concrete example first; ordinary replies use a few short lines, aim around 40 words, remain under 80 words, avoid unnecessary recap, and show the current result plus next action. [Evidence](../validation/DECISIVE-FLOW-TEST.md)
- [x] **C-04 — Research and challenge:** The planner researches external facts from primary/direct sources, saves decision-relevant evidence, and briefly challenges contradictions or unnecessary scope. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **C-05 — Natural language:** `Plan this idea: ...`, `Continue my plan`, `Show my full plan map`, and `Prepare the next session` work without command memorization. [Evidence](../validation/NATURAL-INVOCATION-TEST.md)
- [x] **C-06 — Orientation and recovery:** The opening makes the planned result and planning-only boundary obvious; ordinary replies avoid unexplained process jargon; numeric progress is shown only for a reliable map; and any “I’m confused” turn pauses questions and restores orientation before planning resumes. [Evidence](../validation/ORIENTATION-TEST.md)
- [x] **C-07 — Explicit delegation:** A recorded, scoped request to use recommendations synthesizes reversible choices without more preference questions; repeated agreement alone never creates authority; revocation, conflict, irreversible commitments, uncovered personal tradeoffs, implementation, and final approval remain protected. [Evidence](../validation/DECISIVE-FLOW-TEST.md)
- [x] **C-08 — Stop and trial:** Facts and already-settled choices are not re-asked. When discussion cannot change a dynamic decision, one bounded planning trial preserves ordinary, contrasting, and failure cases with their inputs, outputs, surprises, verdict, and changed decision. [Evidence](../validation/DECISIVE-FLOW-TEST.md)
- [x] **C-09 — Immediate action:** When a safe next planning action is clear, the agent performs it in the same turn rather than stopping after an intention statement. A direct `yes` resolves against the approval question that immediately preceded it. [Evidence](../validation/DECISIVE-FLOW-TEST.md)
- [x] **C-10 — Proactive test readiness:** After agent-run checks pass, the harness clearly presents the smallest genuine user test and requests live acceptance without making Drew determine whether the change is ready. [Evidence](../validation/DECISIVE-FLOW-TEST.md)
- [x] **C-11 — Complete handoff:** At a real boundary, the planner either starts one authorized successor and identifies it or shows one clearly labeled exact next-session prompt. It never stops after only naming a ticket, path, or future session. [Evidence](../validation/DECISIVE-FLOW-TEST.md)

## Idea-stage possibility scan

- [ ] **I-01 — Correct gate and consent:** An uncoached fresh task with no product idea or a thin software/AI idea receives one concise scan-or-skip choice; detailed specifications, existing-project changes, resumed plans, and direct build requests do not. A decline continues ordinary planning and is not asked again.
- [ ] **I-02 — Grounded, bounded discovery:** With consent, the planner reuses the user's words, asks only search-critical real-world grounding one question at a time, sanitizes the public brief, uses no more than three query angles, ranks at most fifteen deduplicated candidates, and deeply inspects at most three without cloning, installing, or executing code.
- [ ] **I-03 — Decision-useful result:** The result uses evidence-tier language, distinguishes candidate roles, handles unclear or incompatible licenses conservatively, and contains one provisional recommendation plus at most two materially different alternatives only when each changes what seems possible or the fastest credible MVP route. Repository popularity does not choose the product, and the user confirms, combines, or redirects the direction before it enters the plan.
- [ ] **I-04 — Honest safety and fallback:** Private or sensitive details do not enter public queries; repository content is treated as untrusted; non-repository research stays within the narrow direct-source boundary; and an unavailable, rate-limited, or unsuccessful search names the limitation and returns to ordinary planning without requiring an account, API client, MCP server, database, cloud dependency, or new runtime.
- [ ] **I-05 — Varied and live proof:** At least three materially different public-repository decision prototypes—including a directionless start, a thin outcome-led idea, and a constrained or no-useful-match case—pass the objective checks, then Drew uses the flow naturally in a fresh task and says it improved his understanding of what was possible and the credible MVP route. Synthetic or authored transcripts do not count as Drew's human evidence.

## Durable state and handoffs

- [x] **S-01 — Canonical local state:** Each plan uses project-local `planning/PLAN.md`, `PLAN-VIEW.md`, `NEXT.md`, `decisions/`, and `execution/`, plus `evidence/` when external facts affect decisions; `PLAN.md` stays a short linked overview. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **S-02 — Decision durability:** Every confirmed decision is saved before context is cleared, with evidence and downstream effects reconciled when relevant. [Evidence: one-key write-through](../validation/KEYED-CHOICE-TEST.md) · [installed-plugin write-through](../validation/FRESH-RESUME-VISUAL-TEST.md)
- [x] **S-03 — Exact resume:** `NEXT.md` names exactly one unblocked planning ticket, loads canonical files instead of chat memory, and states the session outcome and completion test. [Evidence](../validation/FRESH-RESUME-VISUAL-TEST.md)
- [x] **S-04 — Loss recovery:** A fresh agent resumes from local files alone, and can regenerate a missing `NEXT.md` from `PLAN.md` plus the current ticket without losing plan state. [Evidence](../validation/RESUME-TEST.md)
- [x] **S-05 — Dependency safety:** Blocked tickets are not selected; ticket completion requires explicit decisions, reconciled effects, no blocker to the next ticket, and an exact next-session starter. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)
- [x] **S-06 — Honest finish:** Planning cannot finish with unresolved major choices, contradictions, missing links, missing completion tests, or oversized execution tickets. [Evidence](../validation/OBJECTIVE-EVIDENCE-AUDIT.md)

## Test coverage

- [ ] **T-01 — First real-use plan:** Drew starts any real plan naturally in a fresh Codex task with no test coaching. Every confusion, weak or repeated question, wall of text, state loss, visual failure, bad recovery, and incomplete handoff is recorded, fixed, and rerun. Canned examples and implementation simulations never count as Drew's human evidence.
- [ ] **T-02 — Naturally complex plan:** Drew later uses the planner for a real plan complex enough to exercise dependencies, human gates, revision, recovery, and execution-ticket generation; concrete failures are recorded, fixed, and rerun.
- [x] **T-03 — Cross-project fixtures:** The same core skill passes software, creative/content, operational/event, and personal-project adversarial fixtures without a domain pack. [Evidence](../validation/CROSS-PROJECT-FIXTURE-TEST.md)
- [x] **T-04 — Decisive-flow scenarios:** Normal, materially contrasting, and failure-boundary scenarios pass for software and non-software planning, including delegated recommendations, exhausted discussion, direct approval, immediate build transition, revocation/conflict, protected gates, and proactive test readiness. [Evidence](../validation/DECISIVE-FLOW-TEST.md)

## Portability and installation

- [x] **P-01 — Canonical package:** One Agent Skill package supplies all planning logic, references, and Markdown templates; adapters only locate or invoke it. [Evidence: local](../validation/CODEX-INSTALL-TEST.md) · [public preview](../validation/PUBLIC-PREVIEW-DISTRIBUTION-TEST.md)
- [x] **P-02 — Codex install:** From one link or local package plus a natural-language request, an agent installs at user scope, verifies the skill and visual template, uses a direct-load fallback when discovery is frozen, runs a smoke interaction in the same session, and gives one precise recovery step on failure without requiring GitHub, terminal work, or another user-installed dependency. [Evidence: local and same-session](../validation/CODEX-INSTALL-TEST.md) · [public marketplace](../validation/PUBLIC-PREVIEW-DISTRIBUTION-TEST.md)
- [x] **P-03 — Non-Codex install:** The unchanged canonical skill works in at least one non-Codex harness. [Evidence: unchanged-state Hermes](../validation/PORTABLE-VIEW-TEST.md) · [public Hermes and Claude Code installs](../validation/PUBLIC-PREVIEW-DISTRIBUTION-TEST.md)
- [x] **P-04 — Cross-harness resume:** Codex and the selected non-Codex harness can alternately resume the same unchanged project planning state and `PLAN-VIEW.md` without conversion; each displays the richest supported view and the text route remains usable in a text-only custom harness. [Evidence: Codex → Hermes → Codex](../validation/PORTABLE-VIEW-TEST.md)

## Drew's acceptance

- [ ] **H-01 — Faster:** Drew says planning feels substantially faster than his current experience.
- [ ] **H-02 — Worthwhile conversation:** Drew says the questions are worth answering and replies do not feel like walls of text.
- [ ] **H-03 — Clear boundaries:** Drew says the map and handoffs remove session-boundary confusion.
- [ ] **H-04 — Usable real plans:** Drew says the first ordinary and naturally complex plans are plans he would actually use.
- [ ] **H-05 — Executable handoff:** Drew says the execution tickets are clear enough to start without major planning questions.

## Final result

**Current status: DECISIVE-FLOW CANDIDATE READY FOR LIVE ACCEPTANCE; IDEA-STAGE SCANNING IS NOT YET PROVEN.** Synthetic and package evidence passes C-03, C-07 through C-11, R-04, and T-04. Drew's fresh live judgment is still required before the decisive flow is treated as accepted. The complex visual proof, idea-stage checks, real-use proofs, H-01 through H-05, and final audit remain open.
