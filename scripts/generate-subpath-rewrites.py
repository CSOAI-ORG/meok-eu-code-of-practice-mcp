#!/usr/bin/env python3
"""Generate Vercel rewrites for meok.ai subpath deploy directories that are not
already served by the main ui project. Reads health check report, probes default
deploy URLs, and appends rewrite rules to meok/ui/vercel.json.
"""
import json
import re
import urllib.request
from pathlib import Path

HEALTH = Path("/Users/nicholas/clawd/_findings/EMPIRE_HEALTH_CHECK_2026-06-15.md")
VERCEL_JSON = Path("/Users/nicholas/clawd/meok/ui/vercel.json")
TIMEOUT = 10


def probe(url: str) -> int:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "MEOK-HealthBot/1.0"}, method="GET")
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.getcode()
    except Exception as e:
        return getattr(e, "code", 0)


def main():
    report = HEALTH.read_text(encoding="utf-8")
    entries = []
    for line in report.splitlines():
        if not line.startswith("|") or "meok.ai/" not in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 10 or parts[9] != "F":
            continue
        dir_name = parts[1]
        canonical = parts[2]
        if not canonical.startswith("https://meok.ai"):
            continue
        path = canonical[len("https://meok.ai"):]
        slug = dir_name.replace("-deploy", "")
        # Try default deploy URL.
        deploy_url = f"https://{slug}-deploy.vercel.app"
        code = probe(deploy_url)
        if code != 200:
            print(f"SKIP {dir_name}: {deploy_url} returned {code}")
            continue
        entries.append((path, deploy_url))

    # Load vercel.json
    config = json.loads(VERCEL_JSON.read_text(encoding="utf-8"))
    existing_sources = {r.get("source") for r in config.get("rewrites", [])}
    new_rewrites = []
    for path, deploy in entries:
        src = path.rstrip("/")
        if src in existing_sources or src + "/:path*" in existing_sources:
            continue
        new_rewrites.append({"source": src, "destination": deploy.rstrip("/") + "/"})
        new_rewrites.append({"source": src + "/:path*", "destination": deploy.rstrip("/") + "/:path*"})

    config.setdefault("rewrites", []).extend(new_rewrites)
    VERCEL_JSON.write_text(json.dumps(config, indent=2), encoding="utf-8")
    print(f"Added {len(new_rewrites)} rewrite rules for {len(entries)} subpaths.")
    for path, deploy in entries:
        print(f"  {path} -> {deploy}")


if __name__ == "__main__":
    main()
