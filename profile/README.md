# Rustly

**Rust-first learning, practice, judging, and community platform.** → [rustly.tech](https://rustly.tech)

Rustly is not a Rust Book mirror, not a LeetCode clone with Rust enabled, not a
generic online IDE, and not an AI wrapper. It is a platform built around one
opinionated loop:

```
concept -> mental model -> small runnable example -> predict result/error -> micro quiz
   -> Hard Check -> Run -> explain compiler/runtime result -> real OSS Rust example
   -> mutate/break/fix -> Trial -> compare accepted solutions -> cheatsheet
```

## What makes it different

1. **Rust-only and Rust-native.** No polyglot compromises in the pedagogy.
2. **Real compiler feedback is part of teaching.** Raw `rustc` diagnostics are never hidden.
3. **Hard Check before execution.** You commit to a prediction before you run.
4. **Context-aware pedagogical linting**, not just Clippy passthrough.
5. **Mental-model visualizations** for ownership, borrows, and lifetimes.
6. **Compact contextual cheatsheets** pinned to what you are reading right now.
7. **Curated real-world OSS Rust examples**, pinned to immutable commit SHAs.
8. **Post-solve solution comparison.**
9. **High-quality sandboxed judge** - separate compile and runtime security domains.
10. **Git-native / local-first workflow.**
11. **Distributed content-addressed storage and compute.**
12. **Operable in a hard $0 infrastructure mode**, failing closed financially.

## Repositories

| Repository | Purpose |
| --- | --- |
| [`web`](https://github.com/rustly-tech/web) | Static-first Astro web application for rustly.tech |
| [`core`](https://github.com/rustly-tech/core) | Trusted control-plane backend (Rust / Axum / Postgres) |
| [`judge`](https://github.com/rustly-tech/judge) | Sandboxed Rust submission judging (Wasmtime) |
| [`content`](https://github.com/rustly-tech/content) | Versioned educational content + validation tooling |
| [`toolchain`](https://github.com/rustly-tech/toolchain) | Browser-side Rust compile/run abstraction and assets |
| [`fabric`](https://github.com/rustly-tech/fabric) | Content-addressed immutable data plane (BLAKE3 CAS) |
| [`git`](https://github.com/rustly-tech/git) | Git Smart HTTP ingress for the learning workspace |
| [`infra`](https://github.com/rustly-tech/infra) | Reproducible $0-capable deployment + observability |
| [`.github`](https://github.com/rustly-tech/.github) | Org metadata, reusable CI, engineering standards |

## Maturity vocabulary

Every claim in every Rustly repository is tagged with one of four words. We use
them literally.

| Tag | Meaning |
| --- | --- |
| **IMPLEMENTED** | Code exists, is built by CI, and is covered by tests. |
| **QUALIFIED** | Independently validated against an adversarial or reproducible test corpus, and safe to depend on for the stated purpose. |
| **EXPERIMENTAL** | Runs, but the design or safety envelope is not settled. Do not depend on it. |
| **PLANNED** | Design or interface only. No working implementation. |

**No placeholder implementation is ever described as production-ready.**

## Licensing

- Code: `MIT OR Apache-2.0`
- Educational content: `CC BY 4.0`
- Third-party snippets: upstream attribution and license retained and recorded.

## Contributing

Start with [CONTRIBUTING.md](https://github.com/rustly-tech/.github/blob/main/CONTRIBUTING.md)
and [the architecture overview](https://github.com/rustly-tech/infra/blob/main/docs/ARCHITECTURE.md).
