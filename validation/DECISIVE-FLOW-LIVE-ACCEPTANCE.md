# Decisive-flow live acceptance

Date: 2026-08-07
Candidate: `0.1.0-beta.4`
Status: completed with recorded failures — beta 4 not accepted

## Test policy

- Record each natural interaction as it happens.
- Do not revise the plugin mid-run unless safety, state loss, or a hard blocker
  makes continuation invalid.
- After the run, group concrete failures, make the smallest targeted changes,
  and rerun affected interactions.
- Do not add architecture unless a recorded failure cannot be corrected inside
  the canonical skill, references, or templates.

## Interaction 1 — New Pinterest-to-brand project

### User input

The user naturally described a new product concept: create a Pinterest mood
board, give it to an agent session with a plugin, and use its visual references
to help create a website or brand identity.

### Observed process

- The agent naturally selected Portable Planner.
- Its first catalog path was stale and failed to resolve. It located the actual
  installed skill and continued without asking Drew to troubleshoot.
- It inspected an empty workspace and created only the initial canonical
  `planning/PLAN.md`, `planning/NEXT.md`, and one decision ticket.
- No application, Pinterest integration, runtime, MCP server, database, or
  second state system was created.

### Visible reply

> Planning: Pinterest-to-Brand Plugin
> Now: See what’s already possible
> Later: Choose the strongest MVP direction
> This phase creates the product plan; it does not build the plugin.
> A. Scan first — Recommended; briefly research public approaches for Pinterest
> ingestion, style extraction, and AI branding workflows.
> B. Skip the scan — Plan directly from the current concept.
> Or give a different preference. Reply A or B.

### Judgment

- Pass: correct idea-stage eligibility and one-time scan permission gate.
- Pass: recommendation-first `A/B`, custom-answer path, one question, clear
  planning-only boundary, and compact visible output.
- Pass: durable state was saved before relying on chat memory.
- Pass: no evidence of product or harness overengineering.
- Watch: the collapsed process commentary was longer than the visible answer,
  but Drew said the normal visible output was appropriately short.
- Recorded integration issue: the initial installed-skill catalog path was
  stale. Recovery succeeded, so it is not yet a Portable Planner behavior
  failure; investigate after the unchanged live run if it recurs.

### Current verdict

Continue the natural planning session with the unchanged candidate. No plugin
correction is justified from this interaction alone.

## Interaction 2 — Accept the repository scan

### User input

> a

### Observed process

- The agent resolved `A` against the immediately preceding choice and began the
  promised scan without asking Drew to repeat the answer.
- A first state edit missed because the saved files had changed. The agent read
  the actual files, preserved the concept, and continued.
- The scan separated Pinterest access, image reuse, and style interpretation.
  It rejected anonymous Pinterest scraping as the MVP foundation and preserved
  uploaded images as a reliable fallback to authorized import.

### Visible result

The agent recommended a “mood-board-to-brand compiler,” explained the Pinterest
OAuth constraint, and offered full compiler, brand-profile-only, or
extension-first directions.

### Judgment

- Pass: one-key write-through and immediate safe action.
- Pass: factual platform limits changed the proposed route.
- Pass: the recoverable state mismatch did not lose or duplicate the plan.
- Watch: the scan began converging on a text-and-token “style translator” before
  proving whether Drew wanted the original images to remain direct generation
  inputs. The later correction confirms this was a material unresolved product
  distinction, not a minor implementation detail.

## Interaction 3 — Choose the smaller brand-profile direction

### User input

> b

### Visible result

The agent recorded a profile-only MVP, removed website generation, then asked
whether it should produce one editable verbal profile or several alternatives.
Its concrete example reduced ten Pins to language such as “warm editorial
palette” and “natural photography.”

### Judgment

- Pass: one-key answer was saved and the chosen smaller scope was applied.
- Pass: only one labeled recommendation-first question was visible.
- Failure F-LIVE-01: the next question operationalized an unconfirmed assumption
  that the product's core output was vocabulary and design tokens. That was the
  exact behavior Drew did not want. The planner should have surfaced or tested
  direct visual conditioning versus verbal translation before optimizing the
  number of text profiles.
- Constraint for the later fix: do not add a Pinterest-specific domain pack.
  The general planner should detect when a proposed abstraction may discard the
  source material that creates the product's value.

## Interaction 4 — Correct the product's core job

### User input

Drew explained that reference images must travel directly into the generation
model so their colors, textures, composition, and aesthetic remain influential.
Vocabulary may organize or constrain the process, but must not replace visual
conditioning.

### Visible result

The agent clearly contrasted the intended route—reference images directly into
the generator—with the rejected route—images reduced to adjectives and then
re-guessed. It preserved roles and influence controls for individual images,
revised the saved destination and route, and asked whether generation belongs
inside the plugin, outside through an exported pack, or both.

### Judgment

- Pass: the agent understood the correction instead of defending its earlier
  recommendation.
- Pass: canonical state and downstream route were reconciled immediately.
- Pass: the explanation made the changed product concrete.
- Watch: the visible reply was longer than an ordinary turn, but the extra
  contrast directly repaired a material misunderstanding.
- Watch: the next generation-location question arrived before checking the
  existing-tool landscape. Drew had to request that factual research in the
  following turn.

## Interaction 5 — Research direct visual-reference products

### User input

Drew asked whether GitHub or current products already solve the direct
multi-reference branding problem, or whether the idea is new.

### Observed process

- The agent researched the exact distinction rather than generic mood-board
  tools: multiple reference images remain model inputs and create adaptable
  brand work.
- It separated established generation mechanics from the fragmented
  Pinterest-to-brand product workflow.
- It saved the full findings into the plan's normal evidence folder.

### Visible result

The agent identified Recraft custom styles, Midjourney Moodboards, Adobe
Firefly Boards, the niche Diatech Studio workflow, ComfyUI IPAdapter, and a
small Pinterest extension. It concluded that reference-conditioned generation
is established while the general Pinterest import → roles and weights → brand
generation → reusable cross-project system remains fragmented.

### Judgment

- Pass: research answered Drew's real question and materially corrected the
  product positioning.
- Pass: the result distinguished product/workflow innovation from inventing a
  new model.
- Pass: existing tools and open-source mechanics reduced technical uncertainty
  without expanding Portable Planner's architecture.
- Accepted: Drew deliberately opened the expanded work details so this audit
  could inspect them. He did not identify the research detail or summaries as a
  reading-load failure. Do not treat the manually expanded diagnostic view as
  the ordinary surfaced reply.
- Watch: asking Drew to choose a specific generator is justified only if its
  platform dependency materially changes his desired product; internal tool
  selection should otherwise remain agent-owned.

## Running verdict after interaction 5

Continue the unchanged live run. Confirm whether later turns repeat
F-LIVE-01, and evaluate the eventual finish, approval, build
transition, test prompt, and handoff before changing the candidate.

## Interaction 6 — Reuse the user's existing project evidence

### User input

Drew selected the recommended integrated direction and asked the planner to
inspect his existing DREMES agent project for Pinterest-related work. When the
connected GitHub search could not find the name, he clarified that the project
might exist locally in WSL and described its ad-repurposing purpose.

### Observed process

- The agent searched connected GitHub repositories before asking for a link.
- After Drew redirected it to WSL, it searched likely projects and content,
  found `/home/drewp/_repo-inspect/dremes-agent`, read its local guidance, and
  inspected it without modifying it.
- It found a Pinterest board drain, deduplication, reference pools, approval
  gates, generation manifests, and a pipeline that sends actual reference,
  product, and logo images into GPT Image 2 or Gemini.
- It separated reusable direct-image mechanics from scraping/cookie intake and
  overly close single-ad reconstruction.
- Context compacted during the work; the agent resumed from preserved project
  state and completed the audit.

### Judgment

- Pass: the planner researched a factual lead instead of asking Drew to locate
  technical details it could discover.
- Pass: it reused existing project knowledge and avoided rebuilding known
  mechanics from scratch.
- Pass: it challenged unsafe or weak inherited behavior rather than treating
  the old project as unquestioned authority.
- Pass: the inspected repository was unchanged and no new Portable Planner
  architecture was added.
- Pass: saved state survived automatic context compaction.
- Accepted: Drew manually exposed the work detail for this audit and did not
  identify its length as a problem. The normal answer remained usable.

## Interaction 7 — Review, recovery, retention, and rights choices

### User inputs

Drew selected `A` for four sequential product decisions:

1. side-by-side Pass/Adjust review by visual category;
2. a guided correction ladder with preserved versions;
3. a private project-local reference pack with explicit deletion; and
4. a lightweight rights, provenance, and originality gate.

### Judgment

- Pass: every one-key reply resolved to the immediately preceding choice and
  wrote through without asking Drew to repeat it.
- Pass: the questions changed visible product behavior or protected privacy,
  provenance, and creative-risk boundaries; they were not internal architecture
  questions.
- Pass: the recommendations consistently favored visible control, reversibility,
  private local state, and no silent retry or cloud expansion.
- Pass: repeated acceptance was not misrepresented as broad delegated authority.
- Failure F-LIVE-05 — confirmed by Drew: after several consecutive selections
  of the recommended route, the planner kept asking reversible choices one at a
  time. Repeated acceptance must never silently create delegation, but it should
  trigger one concise delegation offer so the user can explicitly authorize it.
- Required general option when that pattern appears:
  `A. Use your recommendations for every remaining reversible decision — Recommended; continue automatically and stop only for an irreversible commitment, uncovered material personal tradeoff, conflict, implementation authorization, or final approval.`
  The alternative is to keep choosing one at a time, with a custom narrower
  scope allowed. If Drew selects delegation, record its exact words and scope,
  then synthesize without more reversible preference questions.
- Minor failure F-LIVE-03: later choice sets used `A —`, `B —`, and `C —`
  instead of the skill's required stable `A.`, `B.`, and `C.` labels. Replies
  still resolved correctly, but the canonical presentation contract drifted.

## Interaction 8 — Finish audit and approval view

### Observed process

- The agent converted the settled route into five session-sized tickets:
  plugin foundation and local pack, manual intake and rights gate, direct-image
  generation, visual review and guided correction, and end-to-end verification.
- It ran a finish audit, stopped before implementation, displayed a compact
  route, linked the finished detail, and asked one explicit build-approval
  question.
- The route excluded scraping, cloud storage, website generation, and
  multi-asset campaigns from the MVP.

### Judgment

- Pass: the five-ticket route is cohesive and does not introduce another
  harness, state tree, server, database, or cloud dependency.
- Pass: the visible approval turn contains the route, current gate, safety
  boundaries, and explicit `A/B` decision rather than only a file link.
- Pass: implementation did not begin before approval.
- Watch, not a Drew-reported failure: after inspecting an ad-repurposing
  repository, the planner narrowed the destination to “one original
  on-aesthetic key visual” and began calling it a “campaign visual.” Existing
  evidence should inform mechanics without silently importing the old project's
  product destination. Confirm during approval or revision whether this was an
  acceptable inferred MVP proof.
- General safeguard to evaluate later: when research or reused project evidence
  introduces a new destination, audience, deliverable, or success proof, label
  it as provisional and ask or trial the material product choice before final
  approval. Do not add Pinterest- or advertising-specific instructions.

## Running verdict after interaction 8

The unchanged candidate reached the correct approval boundary. Drew's confirmed
interaction failure is F-LIVE-05: the planner did not offer explicit scoped
delegation after a clear pattern of recommended-choice acceptance. Expanded
work details are not a failure. Continue by testing the approval transition and
later test/handoff behavior before changing the candidate.

## Interaction 9 — Approved build reaches its first live test

### Observed process

- The approved build became active at a local preview URL.
- The agent proactively requested a real visual-reference test instead of
  waiting for Drew to decide whether the build was ready.
- It asked for 3–5 reference images plus brand/product, visual purpose, hard
  requirements, exclusions, and a rights confirmation in one turn.
- After six images were available, it correctly read them without requesting a
  duplicate upload and summarized their visual qualities.
- It again requested five inputs together. Drew supplied the already-known
  product and the new landing-page purpose; the agent then reduced the remaining
  gate to one rights-confirmation question.

### Judgment

- Pass: direct approval proceeded through build into a genuine test without a
  second build-authorization loop.
- Pass: the agent proactively presented a concrete test and successfully used
  the attached visual references.
- Pass: it did not ask Drew to upload the same images again.
- Pass: source logos, watermarks, identifiable people, UI elements, and exact
  compositions were excluded from generation.
- Failure F-LIVE-06: the test handoff violated the one-question rule by asking
  for five separate answers at once, twice. The later turn demonstrated that
  hard requirements and exclusions were not actually blocking inputs.
- Failure F-LIVE-07: `Brand/product` was already known from the saved project
  and should have been inferred. A test should reuse canonical context, ask only
  the first genuinely missing input, and avoid turning readiness into another
  intake form.
- General correction required later: test handoffs must separate a concrete
  user action from missing human decisions. Infer known facts and safe defaults;
  ask one unresolved blocker at a time. Do not add media- or Pinterest-specific
  instructions to Portable Planner.

### Current frontier

Determine whether the handoff felt like a genuine test or like renewed
grilling, then inspect generation, correction, completion, and handoff behavior
one turn at a time.

## Interaction 10 — Preserve the one-letter path after a digression

### Drew's confirmed preference

During active planning, Drew may answer with a long paragraph, challenge an
assumption, ask a side question, or add context instead of selecting the pending
choice. A longer explanation from the planner is acceptable and sometimes
useful. When a meaningful human decision still remains, the very bottom of that
reply must contain the complete current `A/B/C(/D)` choice set so Drew can still
continue with one letter.

### Required behavior

- Answer the side question or reconcile the new information first.
- Recompute the decision frontier; do not blindly repeat a stale question.
- If the paragraph settled the pending decision, save it and end with the next
  worthwhile lettered choice.
- If it did not settle the pending decision, end with the refreshed version of
  that same choice.
- Put the recommendation first as `A.` and keep the custom-answer path.
- Never finish an active decision turn with only explanation or an open-ended
  prompt when viable lettered answers exist.
- Do not manufacture a choice when no worthwhile human decision remains, when
  explicit delegation covers the reversible frontier, or during the immediate
  confusion-recovery explanation. Resume the lettered path as soon as the user
  is oriented.

### Generality

This applies across software, creative, operational, business, and personal
planning. It is not a media, image, or Pinterest-specific behavior.

## Interaction 11 — Drew's judgment of the test handoff

Drew selected `C`: the test itself was clear and useful, while the bundled
intake initially seemed annoying. After rereading the trace, he qualified that
judgment: the landing-page purpose had not yet been supplied, so asking what the
first generated output should be used for was correct. “Visual” was briefly
ambiguous—he first thought it meant one of the reference images—but the intended
meaning became clear.

Preserve proactive test readiness. The confirmed correction is narrower:

- infer the known project/product from canonical context;
- after reading the references, ask one clear question such as “What should the
  first generated image be used for?”;
- do not bundle that with optional hard requirements, exclusions, or repeated
  known information; and
- apply safe defaults, then ask a genuinely protected blocker separately only
  if it cannot be inferred.

Drew currently leans toward no separate rights-confirmation question and asked
for its downside before deciding.

## Interaction 12 — Passive rights notice and missing visual-plan experience

### Rights decision

Drew selected the recommended compromise: show one passive notice per reference
pack rather than interrupting the conversation with a rights-confirmation
question. Uploading or continuing does not create legal rights; the notice
briefly states the user's responsibility, retains known provenance, and keeps
the originality safeguards visible without another planning answer.

### Visual-plan failure

Drew remembered that Portable Planner was specifically designed to provide a
visual plan. The agent generated `PLAN-VIEW.md` in the background and showed a
compact Mermaid route at final approval, but the result was bland, too small to
read in-session, and required opening it separately. That is not the previously
approved large, host-native interactive plan experience.

- Failure F-LIVE-08: the agent treated the Mermaid fallback as the normal visual
  even though Codex's host-native interactive presentation was available and no
  recorded rendering failure justified falling back. Creating or linking
  `PLAN-VIEW.md` is not itself the visual-plan experience. When a coherent route
  would help the user judge direction, offer the useful interactive draft once.
  At final approval, display the richest supported interactive route
  automatically; fall back visibly only if that surface fails or is unavailable.
- Failure F-LIVE-09: the Pinterest project's `PLAN-VIEW.md` was not refreshed
  when execution finished. Canonical `PLAN.md` says the implementation is
  complete and locally verified, while the visual still says the plan is only
  approved and references are the current step. A displayed visual must be
  generated from current canonical state so it cannot contradict the plan.
- Preserve the adaptive trigger: do not interrupt every question with a graph
  and do not use a fixed question count.
- Keep the behavior general and generated from canonical state; add no visual
  app, renderer, database, or second plan representation.

## Interaction 13 — Host-native visualization fails inline

The first replacement interactive plan displayed a generic error inside the
Codex visualization surface. The same fragment rendered successfully with the
bundled visualization renderer, loaded from the Windows-backed shared Codex
directory, changed steps correctly in Chromium, and reported no page or console
errors. The shared `/mnt/c` file was readable from WSL and Windows-backed
storage, so this evidence does not justify resetting WSL.

The user's repair action exposed the exact host error: `Invalid visualization
read request`. A direct Codex Desktop inspection attempt then failed before UI
access with `sandboxCwd is not a local file URI:
file:///home/drewp/main-projects/portable-planner`. Together, these results
localize the defect to Codex Desktop's Windows/WSL request bridge rather than
the plan fragment or a damaged WSL filesystem.

- Failure F-LIVE-10: the preferred host-native surface can fail even when the
  fragment itself passes standalone rendering and browser interaction checks.
  Portable Planner must report that presentation failure separately from the
  plan, preserve canonical state, and immediately offer a readable in-session
  fallback without regenerating or changing the plan.
- The diagnostic replacement removes custom visual chrome and uses only the
  host's supplied cards, grids, buttons, and text utilities. It retains local
  step selection and is being retried before attributing the failure to the
  desktop bridge or WSL.

### Resolution

Drew confirmed that the rebuilt in-chat route displayed and was acceptable.
The working fallback used the same Windows-backed `/mnt/c` visualization path
but removed custom scripting in favor of native expandable step details. This
rules out a damaged WSL mount and shows that the plan can still be presented
inside the conversation. The exact reason the richer read request was rejected
remains a host limitation; do not claim that WSL itself was broken.

## Final beta-4 verdict

The unchanged live run is complete. It passed natural invocation, idea-stage
consent, durable local state, repository research, one-key write-through,
context recovery, finish review, direct approval-to-build, proactive test
readiness, and the eventual native expandable plan fallback.

It did not pass final acceptance. F-LIVE-01, F-LIVE-03, and F-LIVE-05 through
F-LIVE-10 exposed general failures in research-derived product control, literal
choice labels, delegation invitation, one-question test intake, reuse of known
context, generated-state freshness, and host-specific presentation recovery.
Beta 4 must remain a historical prerelease candidate rather than a
production-proven release.

The approved repair route is E-005 through E-007 in the canonical project plan.
Objective beta-5 checks may prove that the instructions and package were
repaired, but they do not replace Drew's next fresh human acceptance run.
