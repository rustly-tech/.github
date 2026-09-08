# Release and versioning conventions

## SemVer

All published Rustly artifacts use Semantic Versioning. Pre-1.0 repositories may
break minor versions, but breakage must be documented in the changelog.

Tags are `v<MAJOR>.<MINOR>.<PATCH>`, per repository. Repositories release
independently; `web` and `content` in particular have their own cadence.

## Explicitly versioned formats

These carry their own version field, independent of the repository version.
Changing one without bumping it is a breaking-change incident.

| Format | Owner | Version field |
| --- | --- | --- |
| HTTP API | `core` | URL path `/api/v1`, plus `GET /api/version` |
| Trial package format | `content` | `format_version` |
| Content pack | `content` | `format_version` |
| Judge job format | `judge` | `protocol_version` |
| Judge result format | `judge` | `protocol_version` |
| CAS manifest | `fabric` | `manifest_version` |
| Worker protocol | `judge` | `protocol_version` |

## Release process

1. Update `CHANGELOG.md` (Keep a Changelog format).
2. Bump versions; commit as `chore(release): vX.Y.Z`.
3. Tag `vX.Y.Z` and push the tag.
4. The release workflow builds artifacts, generates an SBOM, and publishes a
   GitHub Release. Container images go to GHCR tagged with both the version and
   the commit SHA.
5. Consumers pin the version or the image digest. Never `latest` in production.

## Changelog

Every user-visible change gets a changelog entry. Entries state maturity
(`IMPLEMENTED` / `QUALIFIED` / `EXPERIMENTAL` / `PLANNED`) when introducing a
capability.
