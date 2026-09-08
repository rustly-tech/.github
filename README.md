# rustly-tech/.github

Organisation-wide metadata, engineering standards, and reusable CI for
[Rustly](https://rustly.tech).

**This repository contains no application code.** Application code lives in the
per-domain repositories listed in the [organisation profile](profile/README.md).

## The organisation

| Repository | Purpose |
| --- | --- |
| [`web`](https://github.com/rustly-tech/web) | Static-first Astro web application for rustly.tech |
| [`core`](https://github.com/rustly-tech/core) | Trusted control-plane backend (Rust / Axum / PostgreSQL) |
| [`judge`](https://github.com/rustly-tech/judge) | Sandboxed Rust submission judging (Wasmtime) |
| [`content`](https://github.com/rustly-tech/content) | Versioned educational content and validation tooling |
| [`toolchain`](https://github.com/rustly-tech/toolchain) | Browser-side Rust compile/run abstraction and assets |
| [`fabric`](https://github.com/rustly-tech/fabric) | Content-addressed immutable data plane (BLAKE3 CAS) |
| [`git`](https://github.com/rustly-tech/git) | Git Smart HTTP ingress for the learning workspace |
| [`infra`](https://github.com/rustly-tech/infra) | Reproducible $0-capable deployment and observability |
| `.github` | This repository |

## Contents

| Path | Purpose |
| --- | --- |
| [`profile/README.md`](profile/README.md) | Public organisation profile - a landing page, kept short on purpose |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Org-wide contribution rules |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Contributor Covenant 2.1 |
| [`SECURITY.md`](SECURITY.md) | Vulnerability reporting, scope, CI security baseline |
| [`SUPPORT.md`](SUPPORT.md) | Where to take which kind of problem |
| [`NOTICE`](NOTICE) | Licensing for code, content, and third-party material |
| [`docs/PRODUCT.md`](docs/PRODUCT.md) | What Rustly is, the learning loop, and the product boundaries |
| [`docs/MATURITY.md`](docs/MATURITY.md) | How capability claims are labelled |
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
      msrv: "1.88.0"          # omit to skip the MSRV job
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

`audit-ignore` takes space-separated RUSTSEC ids. It exists because cargo-audit
reads `Cargo.lock`, which records every *optional* dependency whether or not it
is ever compiled - so an advisory can fire for code the build never touches.
cargo-deny's advisories check walks the real dependency graph and is the
authority; anything passed to `audit-ignore` must be justified where it is
passed.

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

The calling repository must declare `"packageManager": "pnpm@x.y.z"` in its
`package.json`. `pnpm/action-setup` reads it, and it pins the package manager
for contributors through corepack too.

## Why reusable workflows are referenced by `@main`

External actions are pinned to immutable commit SHAs, without exception. Our own
reusable workflows are referenced by branch on purpose: they *are* org CI policy,
and pinning them per-repository would mean a security fix to the CI baseline
could not be shipped without nine coordinated pull requests. They are reviewed as
source in this repository. `tools/check_action_pins.py` encodes exactly this
exemption and fails on anything else.

## License

Dual-licensed under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option.
