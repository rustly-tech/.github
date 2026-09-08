## What this changes

<!-- One paragraph. What is different after this PR? -->

## Why

<!-- Link the issue. Closes #NNN -->

## Maturity of what is added

<!--
Delete the ones that do not apply. Be honest; mislabelling is a review blocker.
Definitions: https://github.com/rustly-tech/.github/blob/main/docs/MATURITY.md
-->

- [ ] **IMPLEMENTED** - code exists, built by CI, covered by tests
- [ ] **QUALIFIED** - validated against an adversarial/reproducible corpus
- [ ] **EXPERIMENTAL** - runs, but design or safety envelope is unsettled
- [ ] **PLANNED** - interface or design only

## Tests that prove it

<!-- Name the tests. "Manually verified" is not an answer for behavioural claims. -->

## Architectural invariants

- [ ] Static-first: ordinary lesson/cheatsheet/Trial reads still need no DB/API call
- [ ] Local-first: drafts/quiz/editor state still live locally first
- [ ] API-light: no keystrokes, heartbeats, view pings, or local Runs sent to core
- [ ] Large immutable bytes stay in CAS/CDN, not in the API or Postgres
- [ ] Trusted authority unchanged (identity, permissions, rank, refs, hidden tests, verdicts)
- [ ] No user code is executed inside an API process
- [ ] Cache remains disposable; corruption causes retry/quarantine, not a wrong verdict
- [ ] No new default-on paid infrastructure

## Security

- [ ] No secret is exposed to fork PR workflows
- [ ] New third-party actions are pinned to a commit SHA
- [ ] Hidden tests / private source are not distributed to untrusted peers
- [ ] Threat model doc updated if trust boundaries moved

## Compatibility

- [ ] No wire format changed, or the format version was bumped and documented
