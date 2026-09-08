# Security Policy

## Reporting a vulnerability

**Do not open a public issue.**

Report privately via GitHub Security Advisories on the affected repository
(`Security` -> `Report a vulnerability`), or by email to **security@rustly.tech**.

Please include:

- affected repository and commit SHA or release version
- reproduction steps or a proof-of-concept
- observed vs. expected behaviour
- your assessment of impact

We aim to acknowledge within 72 hours and to provide a remediation plan within
14 days. We will credit reporters in the advisory unless you ask us not to.

## Scope and severity

Rustly executes untrusted user-supplied Rust code. The following are treated as
**critical** by default:

| Class | Why |
| --- | --- |
| Sandbox escape in `judge` | Arbitrary code execution on judge infrastructure |
| Hidden-test disclosure | Destroys judging integrity for every user |
| Resource-limit bypass (CPU / memory / wall / output) | Denial of service and cost exposure |
| Verdict forgery or replay against `server` | Corrupts ranking and progress authority |
| CAS integrity bypass in `storage` | Poisoned content served as verified |
| Git ref or permission bypass in `workspaces` | Cross-tenant workspace access |
| Secret exposure through CI, especially fork PR workflows | Full org compromise |

## Judge threat model

The judge treats **compilation itself as untrusted code execution**, because
Cargo may invoke `build.rs` and procedural macros. The compile sandbox and the
runtime sandbox are separate security domains with separate policies. See
[`judge/docs/THREAT_MODEL.md`](https://github.com/rustly-tech/judge/blob/main/docs/THREAT_MODEL.md).

We do **not** currently claim the native execution backend is a security
boundary. It is `EXPERIMENTAL` and qualification-gated. Only the Wasmtime
backend is used for untrusted submissions.

## CI security baseline

Every Rustly repository must satisfy:

- minimal `GITHUB_TOKEN` permissions (`contents: read` by default)
- third-party actions pinned to immutable commit SHAs
- no production secret is ever exposed to a `pull_request` workflow from a fork
- untrusted PR code never runs on a privileged or self-hosted runner
- `cargo-deny` and `cargo-audit` on Rust repositories
- dependency audit on the web repository
- CodeQL where the language is supported
- Dependabot enabled
- SBOM generated for every published release artifact

## Supported versions

Rustly is pre-1.0. Only `main` and the most recent release of each repository
receive security fixes.
