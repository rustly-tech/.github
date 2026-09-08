# What Rustly is

Rustly is a Rust-first learning, practice, judging, and community platform.

It is **not** a Rust Book mirror, a LeetCode clone with Rust enabled, a Codewars
clone, a generic online IDE, a social network, or an AI wrapper. Knowing what it
is not is load-bearing: most feature requests that would damage it arrive
disguised as one of those.

## The learning loop

Everything in the product serves one loop:

```
concept
  -> mental model
  -> small runnable example
  -> predict result/error
  -> micro quiz
  -> Hard Check
  -> Run
  -> explain compiler/runtime result
  -> real OSS Rust example
  -> mutate/break/fix
  -> Trial
  -> compare accepted solutions
  -> cheatsheet
```

A feature that does not sit somewhere on that line needs a strong argument.

## What makes it different

1. **Rust-only and Rust-native.** No polyglot compromises in the pedagogy.
2. **Real compiler feedback is part of teaching.** Raw `rustc` diagnostics are
   never hidden or rewritten. Explaining a diagnostic is allowed; replacing it is
   not.
3. **Hard Check before execution.** You commit to a prediction before you run.
4. **Context-aware pedagogical linting**, not just Clippy passthrough.
5. **Mental-model visualisations** for ownership, borrows, and lifetimes.
6. **Compact contextual cheatsheets** pinned to what you are reading right now.
7. **Curated real-world OSS Rust examples**, pinned to immutable commit SHAs -
   never to a moving branch.
8. **Post-solve solution comparison.** Revealing solutions is allowed; it costs
   first-solve ranking credit and nothing else.
9. **A high-quality sandboxed judge**, with compilation and execution treated as
   separate security domains.
10. **Git-native, local-first workflow.**
11. **Distributed content-addressed storage and compute.**
12. **Operable in a hard $0 configuration**, failing closed financially.

## Product boundaries

Some things are deliberately absent, and adding them is a product decision rather
than a feature increment:

- No country, regional, or state rankings.
- No public performance-history graphs or contribution heatmaps.
- No collectible course badges, and no stacked milestone badges - one Trial
  milestone badge is displayed and it upgrades in place.
- No gold/silver/diamond style tiers.
- No clan currency, clan levels, skill trees, territory, or purchasable capacity.
- No social-feed spam: Recent shows meaningful platform events, not user activity.
- Supporter status is cosmetic. It never affects ranking, judging priority, or
  access to learning material.
- No AI features before the deterministic learning loop works.

## Related documents

- [Architectural invariants](ARCHITECTURE_INVARIANTS.md) - the ten technical rules
- [Maturity vocabulary](MATURITY.md) - how capability claims are labelled
