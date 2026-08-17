# Beta 7 release-candidate check

Date: 2026-08-17  
Candidate: `0.1.0-beta.7`  
Scope: package integrity and existing objective regression checks only

## Release decision

Drew explicitly authorized beta 7 without the coached E-020 conversation. Ordinary Codex and ZCode use replaces that artificial test, followed later by local session-history review. This is a change in the evidence route, not a human-acceptance pass; beta 7 remains a public-preview field candidate.

## Passing checks

- All five active marketplace and harness manifests resolve to `0.1.0-beta.7`.
- The canonical skill passes the Skill Creator validator.
- The bundled plugin passes the Plugin Creator validator.
- Every concrete Markdown link inside the canonical skill resolves; template placeholders are intentionally excluded.
- The six valid I-01 fidelity fixtures and six malformed controls pass.
- The Journey plus focus-lens canonical contract and template grammar pass.
- An isolated ZCode user-scope install exactly matches the source plugin tree.
- `git diff --check` passes.

## Deliberately not claimed

- No scripted or coached conversation was run for this release.
- E-020 is superseded, not passed.
- V-03 through V-05, idea-stage live proof, T-01, T-02, H-01 through H-05, and final production acceptance remain open.

## Field proof route

Codex and ZCode receive the same canonical plugin plus the same scoped global activation rule. Drew uses both normally. When he later requests review, raw histories remain local and only redacted, decision-relevant failure evidence may enter this public repository.
