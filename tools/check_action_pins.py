#!/usr/bin/env python3
"""Fail if any GitHub Action reference in this org is not pinned to a 40-hex SHA.

Rustly policy (docs/DEPENDENCY_POLICY.md): every `uses:` reference to an external
action must be immutable. Local actions (`./...`) and reusable workflows owned by
this organisation are exempt; reusable workflows are reviewed as source, and
pinning them to a SHA would make org-wide CI policy updates unshippable.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

USES = re.compile(r"^\s*(?:-\s+)?uses:\s*(\S+)")
SHA = re.compile(r"^[0-9a-f]{40}$")
ORG_REUSABLE = "rustly-tech/.github/"


def check(path: Path) -> list[str]:
    problems: list[str] = []
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        m = USES.match(line)
        if not m:
            continue
        ref = m.group(1).strip("'\"")
        if ref.startswith("./") or ref.startswith("docker://"):
            continue
        if ref.startswith(ORG_REUSABLE):
            continue
        if "@" not in ref:
            problems.append(f"{path}:{lineno}: `{ref}` has no version reference")
            continue
        _, _, version = ref.partition("@")
        if not SHA.match(version):
            problems.append(
                f"{path}:{lineno}: `{ref}` is not pinned to a 40-character commit SHA"
            )
    return problems


def main() -> int:
    roots = [Path(p) for p in (sys.argv[1:] or ["."])]
    files: list[Path] = []
    for root in roots:
        files.extend(sorted(root.rglob("*.yml")))
        files.extend(sorted(root.rglob("*.yaml")))
    files = [f for f in files if "workflows" in f.parts or "actions" in f.parts]

    problems: list[str] = []
    for f in files:
        problems.extend(check(f))

    if problems:
        print("Unpinned GitHub Action references:", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1
    print(f"OK: {len(files)} workflow file(s) checked, all external actions SHA-pinned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
