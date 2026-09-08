# CI conventions

## What GitHub Actions is for

Actions runs **CI/CD for Rustly's own software**: builds, tests, lints, fuzzing,
cross-platform and toolchain-compatibility checks, content validation, example
compilation, reference-solution validation, release builds, container builds,
SBOM generation, security scanning, and publication.

## What GitHub Actions is never for

- executing Rustly **user** submissions
- the production judge
- generic serverless compute or a CDN
- arbitrary user-requested compute
- workloads unrelated to the repository they run in
- multiplying cache or minute quotas through fake repositories

Repository boundaries in this org are architectural. We do not create empty
repositories to obtain more CI capacity.

## Runner selection

| Runner | Use for |
| --- | --- |
| `ubuntu-slim` | 1-vCPU lightweight jobs: formatting, YAML/JSON validation, link checks, metadata audits |
| `ubuntu-latest` | Rust compilation, tests, web builds - anything CPU-bound |
| `ubuntu-24.04-arm` | Real ARM qualification only |
| `macos-*` / `windows-*` | Only where the software genuinely supports that OS |

`ubuntu-slim` carries a minimal toolset. If a job needs preinstalled tooling,
use `ubuntu-latest`.

## Required in every workflow

```yaml
permissions:
  contents: read          # widen per job, never at workflow scope by default

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}
```

Never cancel in-progress runs on `main` - release and deploy jobs must complete.

All third-party actions are pinned to an immutable commit SHA with a trailing
`# vN` comment. `actions/*` are pinned too.

## Caching

Actions cache is an **acceleration layer only**. A cold cache must produce
identical results. Never treat it as durable storage.

Cache keys must include:

- Rust: OS, arch, rustc/toolchain version, `Cargo.lock`, and the feature/profile
  set when it differs between jobs. `Swatinem/rust-cache` derives these.
- Web: lockfile hash, Node version, package-manager version.

Never share a writable `target/` directory between jobs with different trust
levels. Per-repository caches hold only that repository's real build inputs and
outputs.

## Artifacts

- Workflow artifacts: 1-7 day retention unless a specific investigation needs more.
- Durable published software: **GitHub Releases** and **GHCR**, never long-lived
  Actions artifact storage.

## Toolchain matrix

- `stable` is the qualification target and is always blocking.
- `beta` runs as an early-warning signal and is `continue-on-error`.
- `nightly` only where it provides real value (for example, fuzzing).
- MSRV jobs run only where an MSRV is deliberately declared in `Cargo.toml`.

## Cross-repository consumption

Never consume an arbitrary `main` artifact in production. Cross-repo releases use
explicit versions and manifests with immutable commit or digest references.
