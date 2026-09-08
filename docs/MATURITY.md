# Maturity vocabulary

Every capability claim in every Rustly repository carries one of four words. We
use them literally, and mislabelling is a review blocker.

| Tag | Meaning |
| --- | --- |
| **IMPLEMENTED** | Code exists, is built by CI, and is covered by tests. |
| **QUALIFIED** | Independently validated against an adversarial or reproducible test corpus, and safe to depend on for the stated purpose. |
| **EXPERIMENTAL** | Runs, but the design or safety envelope is not settled. Do not depend on it. |
| **PLANNED** | Design or interface only. No working implementation. |

**No placeholder implementation is ever described as production-ready.**

## Where the words go

- README status tables, so a reader knows what they are getting.
- Doc comments on the type or module the claim is about.
- The PR template checklist, so the author states it and a reviewer checks it.

## The distinction that matters most

`IMPLEMENTED` and `QUALIFIED` are not the same thing, and the gap between them is
where security bugs live.

The Wasmtime execution backend in `judge` is `IMPLEMENTED` *and* every bound it
enforces has an adversarial test that tries to break it. The native execution
backend is `EXPERIMENTAL`: it compiles, it is behind a feature flag, and it
refuses to execute anything, because "it looked right" is not qualification.
Compiling untrusted Rust is likewise not yet qualified, and
[the judge threat model](https://github.com/rustly-tech/judge/blob/main/docs/THREAT_MODEL.md)
says so in as many words.

If you cannot point at the test corpus, it is not `QUALIFIED`.
