#!/usr/bin/env python3
"""Verify that relative Markdown links in this repository resolve to real files.

External (http/https/mailto) links are not fetched here: network link-checking is
flaky and would make CI a coin flip. We check only what we own.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    problems: list[str] = []
    checked = 0
    for md in sorted(root.rglob("*.md")):
        if ".git/" in str(md):
            continue
        for lineno, line in enumerate(md.read_text().splitlines(), 1):
            for target in LINK.findall(line):
                target = target.split()[0].strip("<>")
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                checked += 1
                path = (md.parent / target.split("#", 1)[0]).resolve()
                if not path.exists():
                    problems.append(f"{md.relative_to(root)}:{lineno}: broken link -> {target}")
    if problems:
        print("Broken relative links:", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1
    print(f"OK: {checked} relative link(s) resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
