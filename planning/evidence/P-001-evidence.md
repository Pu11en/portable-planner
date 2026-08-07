# P-001 evidence — Decisive planning behavior

Accessed: 2026-08-07

## Primary research

- Matt Pocock's current grilling guidance treats questions that cannot be settled through discussion as prototype candidates rather than prompts to rephrase indefinitely: <https://github.com/mattpocock/skills/blob/84fdeffd12f2ee307994d1eb6feb48173b6e0502/docs/productivity/grill-me.md#L21-L45>.
- His prototype guidance limits a prototype to one explicit question and warns that whole-feature prototypes drift into production: <https://github.com/mattpocock/skills/blob/84fdeffd12f2ee307994d1eb6feb48173b6e0502/docs/engineering/prototype.md#L1-L50>.
- Logic trials start from known state and cover an ordinary path, a tricky edge, and an illegal attempt, then evolve from surprises: <https://github.com/mattpocock/skills/blob/84fdeffd12f2ee307994d1eb6feb48173b6e0502/skills/engineering/prototype/LOGIC.md#L35-L58>.
- UI comparisons default to three materially different variants, cap at five, and retain the alternatives and verdict: <https://github.com/mattpocock/skills/blob/84fdeffd12f2ee307994d1eb6feb48173b6e0502/skills/engineering/prototype/UI.md#L34-L105>.
- His published video demonstrates explicitly asking an agent to choose its recommended answers, but his current GitHub skill does not define a delegation contract: <https://youtu.be/3MP8D-mdheA?t=484>.
- Microsoft human-AI interaction guidance supports remembering prior interactions, exposing efficient correction, and scoping behavior when uncertain: <https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/>.

## Bounded scenario trials

### Ordinary — explicit reversible delegation

- Input: Drew said to use the agent's recommendations for questions the research could answer.
- Variation: Reversible planning-method and presentation choices.
- Observed output: The research was completed, but the response exposed too much detail.
- Failure: The decision route worked; brevity did not.
- Verdict: Record the delegation, synthesize the choices, and expose only the short result.
- Decision changed: Added the compact-output requirement.

### Tricky — discussion has stopped improving the plan

- Input: The behavior was verbally settled, and Drew told the planner to continue.
- Variation: The next safe action was a three-case planning trial.
- Observed output: The assistant announced that it would run the trials but stopped without doing so.
- Failure: Intent narration replaced safe action and caused confusion.
- Verdict: Perform the next safe planning action in the same turn; bounded trials replace exhausted discussion.
- Decision changed: Added the immediate-action rule.

### Failure boundary — ambiguous continuation near approval

- Input: Short assent such as "yes, continue" or "are we done."
- Variation: Reversible planning continuation versus final build authorization.
- Observed output: The wording is sufficient to continue planning but does not name approval of the finished plan.
- Failure prevented: Do not infer final approval or implementation authority.
- Verdict: Continue safe planning work, but ask one explicit final approval question before build.
- Decision changed: Preserved the protected final-plan gate.

### Completion handoff — user should not manage test readiness

- Input: Drew said that when the planner feels finished, it should push him toward testing rather than wait for him to work out the next step.
- Variation: Planning completion versus post-build validation completion.
- Observed output: The planner asked for final approval, but did not yet state the later live-test behavior as an explicit product rule.
- Failure prevented: Finished work no longer stalls in an ambiguous "what now?" state.
- Verdict: Automatically surface the approval gate when planning is complete and the smallest genuine user test when the build is ready.
- Decision changed: Added proactive approval and live-test handoffs while preserving explicit human authorization.

## Limits

- Three cases are a practical first batch, not a scientific proof threshold.
- These trials are planning evidence, not production implementation or live acceptance.
- The delegation contract and general non-code trial form are Portable Planner adaptations, not claims that Matt Pocock already specified them.
