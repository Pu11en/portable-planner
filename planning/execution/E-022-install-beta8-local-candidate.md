# E-022 — Install beta 8 as a local field candidate

- Status: complete
- Depends on: confirmed I-10 failure, passing final-write-barrier candidate checks, and Drew's explicit local-install authorization

## Outcome

Codex discovers one enabled Portable Planner beta-8 development installation from this repository's local marketplace while the public marketplace remains configured for rollback.

## In scope

- Version the five active package and marketplace manifests as `0.1.0-beta.8`.
- Add the thin local Codex marketplace adapter for this existing canonical plugin.
- Apply one Codex development cachebuster, validate the package, register the local marketplace, install its plugin, and remove the duplicate public beta-7 installation.
- Verify the installed manifest, complete canonical skill bundle, and final-write-barrier rule against the repository source.
- Record the installed identifier and field-proof boundary in canonical planning state.

## Excluded

- Commit, push, pull request, tag, GitHub release, public marketplace update, Claude/ZCode installation, or production-proof claim.
- A second skill copy, changed planning protocol, new service, database, runtime, or MCP server.

## Proof

- Package, skill, manifest, link, final-write-barrier, I-01, and diff checks pass after the final source mutation.
- `codex plugin list --json` reports `portable-planner@portable-planner-local` installed and enabled at the expected beta-8 cachebuster version.
- The installed plugin source resolves to `/home/drewp/main-projects/portable-planner/plugins/portable-planner`.
- The public `portable-planner@portable-planner` installation is absent while its marketplace remains configured.
- Installed and source canonical skill trees match.

## Failure and recovery

If local marketplace registration or installation fails, leave the public beta-7 installation enabled or reinstall it before stopping. If verification fails, do not claim beta 8 installed and restore the public installation.

## Human review

Start a new Codex task after installation and use Portable Planner naturally. The first qualifying late-mutation session supplies the field judgment; no coached prompt is required.

## Result

- Local marketplace: `portable-planner-local` at `/home/drewp/main-projects/portable-planner`.
- Installed plugin: `portable-planner@portable-planner-local`.
- Installed version: `0.1.0-beta.8+codex.20260819234732`.
- Installed cache: `/mnt/c/Users/drewp/.codex/plugins/cache/portable-planner-local/portable-planner/0.1.0-beta.8+codex.20260819234732`.
- Codex reports exactly one installed and enabled Portable Planner, sourced from this repository.
- The public beta-7 plugin installation was removed after beta 8 passed installation; the public `portable-planner` Git marketplace remains configured for rollback.
- Recursive comparison confirms the installed plugin matches the repository plugin, all required skill files exist, and the installed skill contains the final-write barrier.
