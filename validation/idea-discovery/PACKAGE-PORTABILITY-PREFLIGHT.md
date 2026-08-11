# Idea-stage discovery — package and portability preflight

Date: 2026-08-07
Candidate package version: `0.1.0-beta.3`
Result: STATIC PACKAGE PASS; FRESH HARNESS INVOCATION OPEN

## Passing checks

- The official bundled skill quick validator passed the canonical folder.
- Claude Code's plugin validator passed `plugins/portable-planner/.claude-plugin/plugin.json`.
- Claude Code's marketplace validator passed `.claude-plugin/marketplace.json`.
- Root, Codex, Claude, Agents, and ZCode JSON manifests all parsed successfully.
- The canonical `SKILL.md` directly links the new `references/idea-discovery.md`, so installers that copy only explicitly linked support files can discover it.
- Every local Markdown link in the modified and newly added files resolved.
- `git diff --check` reported no whitespace errors.
- The ZCode installer source compiled in memory without writing bytecode.
- An isolated ZCode install copied the canonical plugin byte-for-byte, included `references/idea-discovery.md`, wrote valid configuration, enabled plugins, and registered exactly one resolved plugin directory.
- The Agent Skill UI metadata now matches the new trigger: the short description covers rough-idea exploration and the default prompt explicitly invokes `$portable-planner`.
- The Codex manifest remains within its supported maximum of three default prompts.
- No second skill, database, MCP server, search client, account flow, runtime, cloud service, repository clone, or build mode was added.

## Installed-copy boundary

The enabled Codex plugin is the published `portable-planner@portable-planner` version `0.1.0-beta.2` from `https://github.com/Pu11en/portable-planner.git`. It correctly remains unchanged and does not contain this unaccepted local feature. The modified canonical package is now versioned `0.1.0-beta.3` so a later local or published install cannot falsely appear identical to the existing cache.

No installed cache, marketplace source, or user configuration was overwritten during this preflight.

## Fresh-harness attempts

### Codex

The nested ephemeral Codex runner did not emit a final assistant response after loading the modified canonical skill. Details are in [FRESH-CONTEXT-RUN.md](FRESH-CONTEXT-RUN.md). This is not a natural-invocation pass.

### Claude Code

An isolated Claude Code invocation used `--plugin-dir` to load the canonical local plugin directly, disabled session persistence, and used plan-only permissions. Claude Code stopped before inference with:

```text
Failed to authenticate. API Error: 401 OAuth access token has expired. Re-authenticate to continue.
```

The failure is authentication outside the plugin, not a skill result. It is recorded rather than worked around with a new account or token.

### Hermes

The installed Hermes client accepts registry identifiers or direct HTTP(S) `SKILL.md` URLs, not a local skill directory for inspect/install. The public URL still points to accepted `beta.2`; publishing the unaccepted local candidate merely to run this check would violate the live-proof boundary. No Hermes pass is claimed for `beta.3`.

## Recovery and acceptance consequence

Use the canonical local package directly in a genuine fresh Codex task, then rerun at least one non-Codex invocation after its existing authentication is restored or after `beta.3` is legitimately published. Do not edit harness adapters to conceal these host limitations.

E-004 and `I-01` through `I-05` remain open. Static packaging is ready for the live trial; cross-harness behavioral equivalence is not yet proven.
