# Public Preview Distribution Test

**Date:** 2026-08-06  
**Public repository:** `https://github.com/Pu11en/portable-planner`  
**Tested release:** `v0.1.0-beta.1`  
**Tested commit:** `405683a0efab0ecf1dc8885b9beea08919df39b0`

## Purpose

Verify that the experiment's one-link installation promise survives publication as a separate repository without adding MCP, a runtime, database, cloud account, web app, or second planning brain.

## Package contract

- GitHub reports the repository `PUBLIC` and the release as a prerelease.
- The repository contains one canonical skill at `plugins/portable-planner/skills/portable-planner/`.
- Codex, Claude Code, and ZCode manifests are thin wrappers around that same directory.
- Hermes installs that same GitHub directory directly.
- The canonical skill matched the tested experiment skill before the publication-only template-link correction.

## Static validation

- Official Codex plugin validator: PASS.
- Official Agent Skill validator: PASS.
- Claude Code plugin manifest validator: PASS.
- Claude Code marketplace validator: PASS.
- Every JSON manifest parsed successfully.
- The ZCode installer compiled successfully with Python 3.
- Secret scan found no real credential, token, private-key, or bearer-value exposure.

## Codex public install

Client: `codex-cli 0.147.0-alpha.1.2`

1. `codex plugin marketplace add Pu11en/portable-planner --json` cloned the public repository as marketplace `portable-planner`.
2. `codex plugin add portable-planner@portable-planner` installed `0.1.0-beta.1`.
3. `codex plugin list` reported `portable-planner@portable-planner` as `installed, enabled`.
4. The obsolete local `portable-planner@personal` installation was removed after the public copy passed, leaving the public copy as the one enabled Codex installation.

**Result:** PASS for public Codex marketplace installation and unambiguous enabled-package resolution.

## Claude Code public install

Client: Claude Code `2.1.177`

1. Claude Code cloned and validated `Pu11en/portable-planner` as marketplace `portable-planner`.
2. `claude plugin install portable-planner@portable-planner --scope user` succeeded.
3. `claude plugin list --json` reported version `0.1.0-beta.1`, scope `user`, and `enabled: true`.

**Result:** PASS for public Claude Code marketplace installation.

## Hermes direct install and demonstrated failure

Client: Hermes Agent `0.19.1`

The first direct GitHub install passed Hermes's fresh security scan but installed `SKILL.md` and references without the five Markdown templates. Hermes only copies support files explicitly linked from `SKILL.md`; the skill had named the template folder but not each file.

The canonical skill was corrected to link all five templates explicitly, committed as `e1a64b5`, and republished. A forced clean reinstall then reported:

- verdict `SAFE` and decision `ALLOWED`;
- fresh scanner provenance;
- `SKILL.md`;
- all five references; and
- `templates/NEXT.md`, `PLAN-VIEW.md`, `PLAN.md`, `execution-ticket.md`, and `planning-ticket.md`.

`hermes skills update portable-planner` then reported no update available at the current public content.

**Result:** PASS after demonstrated failure, canonical fix, republish, fresh security scan, and complete-bundle reinstall.

## ZCode isolated installer

The user-scoped installer ran against an isolated temporary plugin directory and configuration file. It copied the complete canonical plugin, wrote valid JSON, enabled plugins, registered exactly the resolved plugin path, and preserved the install outside any project state.

**Result:** PASS for installer logic. A live ZCode client was unavailable in this environment, so live discovery remains desirable but is not used as proof.

## Outcome

Public distribution strengthens P-01, P-02, and P-03. The public repository is installable in Codex, Claude Code, and Hermes from the one supplied URL, with ZCode packaging preflighted. This does not satisfy Drew's human experience gates or the incomplete ordinary and complex live pilots.
