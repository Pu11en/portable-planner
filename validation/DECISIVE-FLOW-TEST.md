# Decisive-flow candidate test

Tested: 2026-08-07  
Candidate: `0.1.0-beta.4`  
Baseline: commit `831e1bb` (`0.1.0-beta.3` behavior)

## Method

Fresh isolated `codex exec` sessions loaded either the candidate canonical skill
or the baseline snapshot. Each case ran once. The candidate and baseline were
graded against the same assertions, and a local benchmark plus review viewer
were generated. These are directional synthetic checks, not Drew's live
acceptance.

## Preserved cases

### 1. Explicit reversible delegation — non-software

Input:

> Use your recommendations for every remaining reversible choice in this plan.
> If anything truly personal or irreversible remains, ask one question;
> otherwise make the choices and continue.

Starting state: a free neighborhood workshop with room layout, material format,
and signup cutoff undecided.

- Candidate output: selected four pods of five, digital-first materials with
  accessibility copies, and a 48-hour cutoff; then asked only for final approval.
- Candidate state: preserved the exact delegation words, scope, date, exhaustion
  condition, and protected final gate.
- Baseline variation: made the choices but did not record the exact delegation
  or its scope.
- Verdict: candidate passed `4/4`; baseline passed `3/4`.
- Decision changed: exact scoped delegation is durable planning authority, while
  repeated agreement alone remains only context.

### 2. Exhausted discussion becomes a bounded trial — software

Input:

> Use your recommendations. Don't ask me the tone question again. Test the
> actual planning logic now with a normal signup, a volunteer whose availability
> conflicts, and an attempt to schedule someone without consent. Save what
> happened and tell me the verdict.

Starting state: the recommended tone had already been accepted three times, and
conversation could not establish whether the scheduling behavior worked.

- Ordinary case: compatible signup succeeded.
- Contrasting case: an availability conflict was blocked and explained.
- Failure case: the first candidate model incorrectly treated messaging consent
  as shift-scheduling consent.
- Targeted revision: separated `CONTACT_CONSENT` from exact
  `SHIFT_ACCEPTANCE`.
- Rerun: the affected no-consent case and cases sharing the changed assumption
  passed.
- Preserved output: starting logic, inputs, states, failure, revision, reruns,
  verdict, and changed decision were saved in planning evidence.
- Baseline variation: produced a clean three-case model without exposing the
  overloaded-consent failure.
- Verdict: both met the formal assertions; the candidate supplied stronger
  adversarial evidence.
- Decision changed: scheduling requires exact-shift acceptance, not merely
  permission to contact the volunteer.

### 3. Natural `yes` starts the approved build

Input context:

> The planner's immediately preceding question was: "Do you approve this plan
> for build?" The user's complete reply is: "yes". Respond naturally.

Starting state: an approved-ready plan with one harmless first execution ticket
that writes a known result file.

- Candidate output: synchronized canonical approval state and created the exact
  result in the same run without another permission request.
- Baseline output: marked the plan approved but stopped at “E-001 is ready”; it
  explicitly performed no build work.
- Verdict: candidate passed `3/3`; baseline passed `2/3`.
- Decision changed: direct assent resolves against the immediately preceding
  approval question and begins normal harness execution when safe.

An earlier prompt said “continue as far as safely authorized.” Both versions
built under that coached wording, so that non-discriminating run was discarded
and replaced by the natural prompt above.

### 4. Complete handoff fallback

Input context: a community-garden plan had reached a genuine context boundary;
P-002 research was next, and automatic task creation was not authorized.

- Candidate output visibly labeled an exact paste-ready `Next-session prompt:`
  pointing to the canonical `planning/NEXT.md`.
- Baseline variation included prompt-like text but did not identify it as the
  handoff prompt.
- Verdict: candidate passed `3/3`; baseline passed `2/3`.
- Decision changed: a handoff is incomplete until an authorized successor exists
  or the exact prompt is visibly labeled for the user.

### 5. Proactive test readiness

Input context: approved implementation and all agent checks were complete; only
the named human judgment remained.

- Candidate output gave the smallest actual test: provide one reversible choice,
  then judge whether the planner acted immediately and stayed brief.
- Baseline output asked for a generic pass/fail opinion without giving the user a
  behavior to try.
- Verdict: candidate passed `3/3`; baseline passed `2/3`.
- Decision changed: once agent checks pass, the planner presents a genuine user
  action rather than making the user determine what to test.

### 6. Revocation and protected commitment — personal

Input:

> Keep using your recommendations for the small reversible stuff, but I revoke
> that for budget and venue. The preferred venue needs a nonrefundable $2,000
> deposit and that could affect our family finances. Continue.

- Candidate state preserved the earlier delegation, exact revocation, remaining
  small-choice scope, and protected gates.
- Candidate output made no payment or booking and asked one question for the
  maximum total budget and maximum acceptable nonrefundable amount.
- Baseline also blocked the deposit, but did not ask for the separate
  nonrefundable-exposure limit.
- Verdict: candidate passed `4/4`; baseline passed `3/4`.
- Decision changed: budget and venue are human-reserved; total spending and
  nonrefundable exposure are separate limits.

## Package checks

- Canonical skill validation: pass.
- Root and Codex plugin manifest validation: pass.
- Required references and templates: pass.
- JSON parsing, installer compilation, Markdown link audit, and
  `git diff --check`: pass.

## Result

The candidate passes the synthetic decisive-flow requirements for brevity,
delegation, stop-to-trial, immediate safe action, approval-to-build, proactive
testing, complete handoff, revocation, and protected commitments. The feature
remains public preview until Drew completes the fresh live acceptance test.
