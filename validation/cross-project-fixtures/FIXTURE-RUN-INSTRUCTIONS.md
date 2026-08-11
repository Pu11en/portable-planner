# Portable Planner adversarial fixture run

This is a non-human validation fixture, not human acceptance evidence.

Use the unchanged canonical Portable Planner skill at:

`/home/drewp/main-projects/portable-planner/plugins/portable-planner/skills/portable-planner/SKILL.md`

Read that skill and every reference or template it requires. Do not modify the skill or inspect any sibling fixture, prior validation report, or project outside this fixture directory. Read only this directory's `IDEA.md` and `TEST-PROFILE.md` as project inputs.

Exercise the complete planning flow in this fresh context. Treat `TEST-PROFILE.md` as already confirmed human preferences. If a consequential preference is still missing, simulate a separate turn: write the exact compact question and A/B/C choices to `planning/TEST-TRANSCRIPT.md`, then apply the recommended A answer. Do not ask the real user. Do not invent preference questions merely to produce a transcript. Derive mechanics and research facts yourself.

Create the canonical project-local planning state, finish every planning ticket, generate ordered one-session execution tickets, generate and display the completed visual plan in your final response, and stop at the explicit human approval gate without executing the project.

Also create `planning/TEST-RESULT.md` with PASS or FAIL and concrete evidence for:

- one worthwhile question at most per simulated turn;
- compact A/B/C choices with recommendation first when a question is necessary;
- no factual, obvious, repeated, or technical-routing question transferred to the user;
- complete, internally consistent plan with no major unresolved decision;
- visual completeness and canonical-state agreement;
- blocked-ticket and dependency safety;
- execution tickets small enough for one fresh agent session, with scope, exclusions, dependencies, proof, review, and next eligibility;
- exact `NEXT.md` fresh-session handoff;
- planning stops before execution and waits for explicit human approval; and
- whether any domain-specific addition to the core skill was actually necessary.

Call out every failure honestly. A fixture is not a pass merely because files were generated.
