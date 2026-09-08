# Dependency and security policy

## Adding a dependency

Ask, in order:

1. Can the standard library do it in under ~50 lines we would enjoy maintaining?
2. Is it already in the dependency graph?
3. Is it maintained, and does it have a license we can ship?

Prefer widely-used, audited crates over novel ones, especially anywhere near the
sandbox, cryptography, or parsing untrusted input.

## Licenses

Allowed for code dependencies: `MIT`, `Apache-2.0`, `Apache-2.0 WITH LLVM-exception`,
`BSD-2-Clause`, `BSD-3-Clause`, `ISC`, `Unicode-3.0`, `Zlib`, `CC0-1.0`, `MPL-2.0`.

Not allowed without explicit maintainer sign-off: `GPL-*`, `AGPL-*`, `LGPL-*`,
`SSPL-*`, `BUSL-*`, and any license without an SPDX identifier.

`cargo-deny` enforces this. Do not add an exception without a comment explaining
why in `deny.toml`.

## Automated checks

| Check | Where | Cadence |
| --- | --- | --- |
| `cargo-deny` (advisories, bans, licenses, sources) | every Rust repo | PR + weekly |
| `cargo-audit` | every Rust repo | PR + weekly |
| `pnpm audit --audit-level high` | `web` | PR + weekly |
| CodeQL | repos with supported languages | PR + weekly |
| Dependabot | all repos | weekly |
| SBOM generation | release workflows | every release |
| Secret scanning + push protection | all repos | continuous |

## Untrusted pull requests

Repositories are public, so PRs are untrusted code.

- `pull_request` workflows get read-only tokens and **no secrets**.
- Anything needing a secret runs on `push`/`workflow_dispatch` after review, or
  in a `pull_request_target` workflow that never checks out PR code.
- Untrusted PR code never runs on a self-hosted or privileged runner.
- Fork PRs do not get write access to caches used by trusted jobs.

## Vulnerability response

A `RUSTSEC` advisory or a high-severity `pnpm audit` finding blocks CI. Fix by
upgrading, replacing, or - only with a written justification and an expiry date -
adding a time-limited ignore in `deny.toml` with a tracking issue.
