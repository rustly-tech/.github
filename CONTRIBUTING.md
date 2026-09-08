# Contributing to Rustly

Thank you for helping build Rustly. This document is org-wide policy; individual
repositories may add repo-specific notes in their own `CONTRIBUTING.md`.

## Ground rules

1. **Truth in labelling.** Never describe a placeholder as production-ready. Use the
   maturity vocabulary (`IMPLEMENTED` / `QUALIFIED` / `EXPERIMENTAL` / `PLANNED`)
   in docs, README sections, and PR descriptions.
2. **Tests prove claims.** If a PR asserts a behaviour, a test must demonstrate it.
3. **Architectural invariants are non-negotiable.** See
   [ARCHITECTURE_INVARIANTS.md](docs/ARCHITECTURE_INVARIANTS.md). A PR that
   violates one will be closed regardless of code quality.
4. **Small trusted authority.** Do not move identity, permissions, ranking,
   hidden tests, or accepted-verdict state out of the trusted control plane.
5. **No paid infrastructure by default.** Every change must remain operable in
   the `$0` configuration or be explicitly gated behind the ZeroCostGovernor.

## Workflow

- Fork or branch from `main`. Branch naming: `type/short-description`
  (`feat/`, `fix/`, `docs/`, `chore/`, `refactor/`, `test/`, `ci/`).
- Commits use [Conventional Commits](https://www.conventionalcommits.org/):
  `feat(judge): add output-limit enforcement`.
- Open a PR early as a draft. CI must be green before review.
- One logical change per PR. Mechanical reformatting goes in its own PR.

## Rust repositories

Before pushing:

```sh
cargo fmt --all
cargo clippy --all-targets --all-features -- -D warnings
cargo test --workspace --all-features
```

- Edition 2021, MSRV declared per repository in `Cargo.toml` (`rust-version`).
- `thiserror` for library error types, `anyhow` only at binary/boundary layers.
- `unsafe` requires a `// SAFETY:` comment and a reviewer who understands it.
- Public items in `protocol`/`domain` crates need doc comments.
- Every wire format is explicitly versioned. No hidden breaking changes.

## Web repository

```sh
pnpm install --frozen-lockfile
pnpm typecheck && pnpm lint && pnpm test && pnpm build
```

- TypeScript `strict` is mandatory; `any` requires a comment justifying it.
- React islands only where interactivity is genuinely required.
- Accessibility is a blocking review criterion, not a follow-up.

## Content repository

Content is `CC BY 4.0`. Do not paste text from copyrighted books. Write original
explanations and cite sources. Every OSS example must record repository, commit
SHA, path, line range, upstream license, and attribution. Never pin an example to
a moving branch.

## Security

Never open a public issue for a vulnerability. See [SECURITY.md](SECURITY.md).

## Code of Conduct

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
