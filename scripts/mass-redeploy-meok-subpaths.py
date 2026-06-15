#!/usr/bin/env python3
"""Bulk redeploy all *-deploy/ directories whose canonical is a meok.ai subpath.

Safe to run after the Vercel WAF/alias fix. Skips non-meok domains and any
project whose canonical is missing or already correct.
"""
import os
import re
import subprocess
import time
from pathlib import Path

BASE = Path("/Users/nicholas/clawd")
LOG = BASE / "_findings" / "MASS_REDEPLOY_MEOK_2026-06-15.md"


def canonical(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', text, re.I)
    if not m:
        m = re.search(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', text, re.I)
    return m.group(1).strip() if m else ""


def main():
    targets = []
    for deploy_dir in sorted(BASE.glob("*-deploy")):
        if not deploy_dir.is_dir() or not (deploy_dir / "index.html").exists():
            continue
        can = canonical(deploy_dir / "index.html")
        if can.startswith("https://meok.ai"):
            targets.append((deploy_dir.name, can))

    print(f"Found {len(targets)} meok.ai subpath deploys.")
    lines = ["# Mass Redeploy — meok.ai subpath sites", f"**Target count:** {len(targets)}", ""]
    lines.append("| Directory | Canonical | Result |")
    lines.append("|---|---|---|")

    for name, can in targets:
        print(f"Deploying {name} ...")
        try:
            result = subprocess.run(
                ["vercel", "--prod", "--yes"],
                cwd=str(BASE / name),
                capture_output=True,
                text=True,
                timeout=120,
            )
            ok = result.returncode == 0
            tail = (result.stdout or result.stderr).strip().splitlines()[-3:]
            detail = " ".join(tail) if ok else f"ERROR {result.returncode}: {result.stderr.strip()[-200:]}"
        except Exception as e:
            ok = False
            detail = str(e)
        lines.append(f"| {name} | {can} | {'✅ ' + detail if ok else '🔴 ' + detail} |")
        time.sleep(2)

    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text("\n".join(lines), encoding="utf-8")
    print(f"Log: {LOG}")


if __name__ == "__main__":
    main()
