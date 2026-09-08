# Rustly architectural invariants

These are non-negotiable. A pull request that violates one is closed regardless
of code quality. If an invariant is genuinely wrong, change *this document*
first, with a rationale, and get it reviewed on its own.

## A. Static-first

Ordinary Learn, cheatsheet, and Trial *reads* must not require a database or API
request. They are static assets served from a CDN or a local cache.

*Test:* the site must render `/learn/*`, `/cheatsheets/*`, and `/trials/*` with
the API host unreachable.

## B. Local-first

Drafts, quiz state, editor state, and most learning progress live in the browser
first (OPFS / IndexedDB) and sync as compact checkpoints.

## C. API-light

The authoritative backend never receives keystrokes, editor heartbeats, lesson
view pings, individual quiz clicks, or local Run invocations. Progress arrives as
batched checkpoints.

## D. Distributed immutable bytes

Large immutable objects live in the content-addressed data plane
(CAS / CDN / cache / P2P). They do not travel through the core API and they are
never stored in PostgreSQL. The API returns CAS metadata, CIDs, and source
locations.

## E. Small trusted authority

The trusted control plane owns, and is the only writer of:

- identity
- permissions
- Rank / Level / Global Rank
- Git refs
- hidden tests
- supporter entitlement
- moderation state
- accepted-verdict state

Everything else can be recomputed, re-fetched, or reconstructed.

## F. Browser work first where safe

The browser handles static search, quizzes, the editor, local state, cheap
diagnostics, WASM execution where practical, and visualisations. Server work is
the exception, not the default.

## G. Judge is separate

The control API must never spawn user code. Submission execution happens only in
the judge, behind a broker, in a sandbox. This is a process and a network
boundary, not a module boundary.

## H. Cache is disposable

Compiled artifacts are rebuildable. Cache corruption must cause a clean retry or
quarantine, never an incorrect user verdict. Infrastructure and cache failures
are reported as `JE`/`IE`, never as `CE`/`WA`.

## I. $0 mode must fail closed financially

Quota pressure degrades service; it never silently spends money. The
`ZeroCostGovernor` prefers local and P2P paths, disables optional background
work, queues advanced jobs, and degrades gracefully. Unexpected charges are a
severity-1 bug.

## J. No provider is logically irreplaceable

Providers are accelerators and anchors, not architecture. Domain logic depends on
`ObjectStore`, `MetadataStore`, `ArtifactSource`, `JobQueue`, and
`RealtimeTransport` - never on a vendor SDK.
