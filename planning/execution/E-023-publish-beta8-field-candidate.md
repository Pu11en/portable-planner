# E-023 — Publish beta 8 for ordinary field use

- Status: complete
- Depends on: E-022 and explicit publication authorization

## Outcome

The validated beta-8 candidate is merged to public `main`, tagged and released as a GitHub prerelease, and installed from the public Portable Planner marketplace as Drew's sole enabled Portable Planner.

## In scope

- Normalize the Codex development cachebuster back to release version `0.1.0-beta.8` and keep all five package/marketplace manifests aligned.
- Create a `codex/` release branch, stage only the beta-8 candidate and its evidence, commit, push, create one ready PR, verify checks, and merge it.
- Create annotated tag `v0.1.0-beta.8` on the merge commit and publish a GitHub prerelease.
- Refresh the configured public marketplace, install `portable-planner@portable-planner`, verify its version and canonical bundle, then remove the local development plugin and marketplace registration.
- Record the actual PR, merge, tag, release, and installed state.

## Excluded

- Production-proof claims, deletion or movement of beta-7 history/tag/release, unrelated changes, or publication of private raw session history.
- Claude Code, ZCode, Hermes, or Zed installation changes in this session.

## Proof

- Final skill, plugin, version, link, final-write-barrier, I-01, secret-pattern, and diff checks pass before commit.
- The release PR merges to `main`; the annotated beta-8 tag resolves to that merge commit; the GitHub release is marked prerelease.
- Public marketplace refresh and install report exactly one enabled Portable Planner at `0.1.0-beta.8` from the public Git marketplace.
- The installed public plugin tree matches the tagged canonical plugin tree.
- Beta 7 remains tagged and available for rollback.

## Failure and recovery

If PR, merge, tag, release, refresh, or installation fails, stop at the last verified state and do not claim beta 8 current. Keep or restore the verified local beta-8 installation until the public install passes. Never retry an uncertain release mutation blindly.

## Human review

Use beta 8 normally in fresh Codex tasks. After enough natural use to expose a qualifying late-mutation path, request the same bounded local-history audit and judge both correctness and added burden.

## Result

- [PR #4](https://github.com/Pu11en/portable-planner/pull/4) merged to `main` as `6d2f37c46386b82cfdcd5e28bb7802b47cfeb19e`.
- Annotated tag `v0.1.0-beta.8` resolves to that merge commit.
- [Portable Planner 0.1.0-beta.8](https://github.com/Pu11en/portable-planner/releases/tag/v0.1.0-beta.8) is a published GitHub prerelease.
- The public Codex marketplace refreshed without errors and installed `portable-planner@portable-planner` at `0.1.0-beta.8`.
- The public snapshot and installed cache match the merged canonical plugin, and the installed skill contains the final-write barrier.
- Codex reports exactly one enabled Portable Planner from the public Git marketplace. The temporary local development marketplace was removed.
- `v0.1.0-beta.7` remains available and unchanged for rollback.
