# rustly-tech/.github

Organisation-wide metadata, engineering standards, and reusable CI for
[Rustly](https://rustly.tech).

**This repository contains no application code.** Application code lives in the
per-domain repositories listed in the [organisation profile](profile/README.md).

## Contents

| Path | Purpose |
| --- | --- |
| [`profile/README.md`](profile/README.md) | Public organisation profile |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Org-wide contribution rules |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Contributor Covenant 2.1 |
| [`SECURITY.md`](SECURITY.md) | Vulnerability reporting, scope, CI security baseline |
| [`SUPPORT.md`](SUPPORT.md) | Where to take which kind of problem |
| [`docs/ARCHITECTURE_INVARIANTS.md`](docs/ARCHITECTURE_INVARIANTS.md) | The ten non-negotiable invariants |
| [`docs/CI_CONVENTIONS.md`](docs/CI_CONVENTIONS.md) | Runner selection, caching, artifact, and matrix policy |
| [`docs/RELEASE.md`](docs/RELEASE.md) | SemVer and the explicitly versioned wire formats |
| [`docs/DEPENDENCY_POLICY.md`](docs/DEPENDENCY_POLICY.md) | License allowlist, audits, untrusted-PR rules |
| `.github/workflows/*.yml` | Reusable workflows consumed by other repositories |
| `tools/` | Metadata validators run by this repository's own CI |

## Reusable workflows

### `rust-ci.yml`

```yaml
jobs:
  ci:
    uses: rustly-tech/.github/.github/workflows/rust-ci.yml@main
    with:
      msrv: "1.85.0"          # omit to skip the MSRV job
      features: "--all-features"
      beta: true              # non-blocking early warning
      targets: ""             # extra rustup targets, space separated
      apt-packages: ""        # build dependencies to apt-get install
```

Jobs: `rustfmt` (ubuntu-slim), `clippy -D warnings`, `cargo nextest` + doctests on
stable and beta, optional MSRV `cargo check`, and `cargo doc` with
`RUSTDOCFLAGS=-D warnings`.

### `rust-security.yml`

```yaml
jobs:
  security:
    uses: rustly-tech/.github/.github/workflows/rust-security.yml@main
```

Jobs: `cargo-deny` (advisories, and bans/licenses/sources as separate matrix
legs) and `cargo-audit --deny warnings`.

### `web-ci.yml`

```yaml
jobs:
  ci:
    uses: rustly-tech/.github/.github/workflows/web-ci.yml@main
    with:
      node-version: "22"
```

Jobs: `pnpm install --frozen-lockfile`, typecheck, lint, test, build, plus a
`pnpm audit --audit-level high` leg.

## Why reusable workflows are referenced by `@main`

External actions are pinned to immutable commit SHAs, without exception. Our own
reusable workflows are referenced by branch on purpose: they *are* org CI policy,
and pinning them per-repository would mean a security fix to the CI baseline
could not be shipped without nine coordinated pull requests. They are reviewed as
source in this repository. `tools/check_action_pins.py` encodes exactly this
exemption and fails on anything else.

## License

Dual-licensed under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option.
