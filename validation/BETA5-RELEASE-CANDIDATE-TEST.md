# Beta-5 release-candidate test

Tested: 2026-08-10
Candidate: `0.1.0-beta.5`
Baseline failure source: [beta-4 live acceptance](DECISIVE-FLOW-LIVE-ACCEPTANCE.md)

## Method

The unchanged repaired candidate was exercised through two independent
read-only forward-test agents, deterministic repository checks, an isolated
ZCode install, and a fresh ephemeral Codex session using the locally installed
candidate through its ordinary plugin path. Synthetic behavior checks prove the
instruction response, not Drew's final human experience.

## Affected behavior reruns

### 1. Delegation invitation after a digression

Starting state: a photography-workshop plan had three consecutive selections of
recommended reversible choices, at least three reversible human decisions
remaining, no delegation, and a pending signup-method question. The user asked
whether signup required an account and said they had otherwise liked the
recommendations.

Raw user-facing output:

> Planning: Local photography workshop
> Now: Decide how to handle the remaining preferences
> Later: Final plan review
>
> No—the recommended signup will be account-free. Participants will provide
> basic details and receive confirmation without creating a login.
>
> A. Use my recommendations for every remaining reversible decision —
> Recommended; I’ll continue and stop only for protected gates.
> B. Keep choosing one at a time — More control, but slower.
>
> Or give a narrower scope. Reply A or B.

Result: pass. The reply answered the side question first, did not infer
delegation, recomputed the frontier, put the complete current offer last, and
used literal `A.` and `B.` prefixes.

### 2. Research cannot silently discard a value-bearing source

Starting state: a family cookbook had already confirmed scanned handwritten
recipe cards as its visible centerpiece. Research found a technically convenient
normalization library that suggested replacing scans with uniform text cards.

Raw user-facing output:

> Planning: Family cookbook
> Now: Confirm the role of scanned cards
> Later: Shape search and reading
>
> The normalization library is convenient, but text-only cards would overturn
> the confirmed scan-first experience. For example, a recipe could open on the
> handwritten card with searchable text beneath it.
>
> A. Keep scans as the centerpiece — Recommended; use extracted text only for
> search and accessibility.
> B. Show scans and normalized cards together — Easier to read, but less
> scan-first.
> C. Switch to text-only cards — Simplest technically, but makes scans
> disposable input.
>
> Or give a different answer. Reply A, B, or C.

Result: pass. Research remained provisional, the confirmed source role was not
rewritten, and one grounded product decision returned to the person.

### 3. Refreshed, low-friction live-test handoff

Starting state: canonical context already named Beacon, its teal brand, browser
extension form, first save-one-highlight test, completed implementation, and
passing agent checks. An old view and handoff still named implementation as
current.

Raw user-facing output:

> Planning: Beacon
> Now: Test one real save
> Later: Record the live result
>
> Beacon’s teal browser extension is ready: implementation is complete, agent
> checks passed, and the saved plan now points to live testing.
>
> In your browser, highlight one sentence and save it with Beacon. Tell me
> whether that exact sentence appears saved correctly.

Result: pass for the instruction behavior. The response reconciled the stale
frontier, reused known context, supplied one concrete test action, and asked no
optional or repeated intake questions. A real file-mutating live rerun remains
required for V-03.

### 4. Windows Codex Desktop through WSL presentation failure

Starting state: `PLAN-VIEW.md` and an HTML source both verified, while the
file-backed inline rich view returned `Invalid visualization read request`.

The response preserved both valid sources, identified the desktop presentation
failure separately, visibly supplied a Mermaid graph plus complete text route in
the same reply, and named browser/Site as the interactive recovery. It did not
move or regenerate the valid plan.

Result: pass for the instruction behavior. A fresh beta-5 live display rerun
remains required for V-04.

## Fresh natural-language invocation

The exact local candidate was installed as
`portable-planner@portable-planner 0.1.0-beta.5`. A fresh ephemeral Codex session
in an empty temporary project received only:

> I have a rough idea for software that helps neighbors coordinate borrowing
> rarely used household tools, but I do not know what the first useful version
> should be. Help me plan it.

The session naturally selected Portable Planner, created only `planning/PLAN.md`,
`planning/NEXT.md`, and one current decision ticket, preserved the build boundary,
and returned the expected one-question permission gate with literal `A.` and
`B.` choices. No skill name or command appeared in the request.

The generated catalog initially pointed one directory above the installed
skill, the same Codex catalog-path issue recorded in the beta-4 live run. The
fresh agent located the installed `SKILL.md` and continued successfully. This is
a host integration limitation, not permission to add a second skill copy; it
remains recorded for observation.

## Package and portability checks

- Skill Creator `quick_validate.py`: pass.
- Plugin Creator `validate_plugin.py`: pass.
- Root, Claude, Codex, ZCode, and Agents marketplace JSON: parse pass.
- Version synchronization: every active manifest and marketplace entry says
  `0.1.0-beta.5`.
- Required skill references and templates: pass.
- Current-product Markdown link audit: pass; template placeholders and preserved
  historical fixture snapshots were correctly excluded.
- `git diff --check`: pass.
- Installer compilation: pass.
- Isolated ZCode install: pass; installed plugin is byte-for-byte equal to the
  candidate source.
- Secret-pattern scan outside preserved validation evidence: pass.
- Canonical skill remains 112 lines and one implementation; no MCP server,
  database, web app, cloud dependency, renderer, or domain pack was added.

## Result

The beta-5 candidate passes the affected instruction, package, portability, and
fresh natural-invocation checks. C-02 and C-12 through C-14 now have objective
release-candidate evidence. V-03, V-04, the idea-stage human checks, the complex
visual proof, both real-use proofs, and final human acceptance remain open.
Portable Planner is ready for an honest public-preview prerelease, not a claim
of production-proven behavior.
