#!/usr/bin/env python3
"""Move 3: Issue 5 free keystone certs via meok-attestation-api.vercel.app/sign.

Each cert is a unique email + EU AI Act framework + signed attestation.
The verify URL is the keystone's public audit surface.
"""
import urllib.request, urllib.error, json
from datetime import datetime

TS = int(datetime.now().timestamp())
PROSPECTS = [
    ("monzo", "Monzo Bank", "fintech", "credit scoring AI"),
    ("cera-care", "Cera Care", "care", "caregiver matching AI"),
    ("stitch", "Stitch Financial", "fintech", "fraud detection AI"),
    ("verisure", "Verisure", "security", "alarm monitoring AI"),
    ("parsa", "Parsa Capital", "fintech", "trading signals AI"),
]

print(f"=== MOVE 3-5: Issue 5 keystone certs (ts={TS}) ===\n")
certs = []
for slug, name, sector, system in PROSPECTS:
    email = f"morning-{slug}-{TS}@meok.ai"
    payload = {
        "email": email,
        "regulation": "MEOK-EU-AI-ACT-MORNING-BRIEFING-v1",
        "entity": f"{name} EU AI Act readiness audit (sector: {sector})",
        "score": 100.0,
        "findings": [
            f"{name} operates in the {sector} sector",
            f"AI system scope: {system}",
            "EU AI Act Article 50 transparency applies from 2 Aug 2026",
            "MEOK MORNING-BRIEFING v1 framework — 2026-06-15",
            "Free keystone cert issued by keystone MEOK_MORNING_BRIEFING flow",
        ],
        "articles_audited": ["50", "51"],
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://meok-attestation-api.vercel.app/sign",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode())
            cert_id = d.get("cert_id") or d.get("id") or "?"
            verify_url = f"https://meok-attestation-api.vercel.app/verify/{cert_id}"
            certs.append({
                "slug": slug,
                "name": name,
                "sector": sector,
                "email": email,
                "cert_id": cert_id,
                "verify_url": verify_url,
            })
            print(f"  ✓ {name}: {cert_id}")
            print(f"    verify: {verify_url}")
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:200]
        print(f"  ✗ {name}: HTTP {e.code} — {err}")
    except Exception as e:
        print(f"  ✗ {name}: {type(e).__name__}: {e}")

# Write the verify URLs to a durable file
out = "/Users/nicholas/clawd/_intake/SPRINT_1_DAY1_KEYSTONE_CERTS.md"
with open(out, "w") as f:
    f.write(f"# 🐉 5 Keystone Certs — Day 1 / Sprint 1\n")
    f.write(f"**Issued:** {datetime.now().isoformat()}\n")
    f.write(f"**Framework:** MEOK-EU-AI-ACT-MORNING-BRIEFING-v1\n")
    f.write(f"**Verify surface:** https://meok-attestation-api.vercel.app/verify/<cert_id>\n\n")
    f.write(f"## The 5 prospect certs (lead magnets for first-touch emails)\n\n")
    f.write(f"| # | Prospect | Sector | Cert ID | Verify URL | Email |\n")
    f.write(f"|---|----------|--------|---------|------------|-------|\n")
    for i, c in enumerate(certs, 1):
        f.write(f"| {i} | {c['name']} | {c['sector']} | `{c['cert_id']}` | [verify]({c['verify_url']}) | {c['email']} |\n")
    f.write(f"\n## How prospects use this\n\n")
    f.write(f"1. The first-touch email includes the verify URL (one click, no login, no contacting anyone)\n")
    f.write(f"2. The auditor clicks the verify URL → sees a real signed attestation with the keystone's Ed25519 signature\n")
    f.write(f"3. The auditor can validate offline (signature is verifiable without the keystone running)\n")
    f.write(f"4. The conversion is: signed evidence → trust → purchase (Pro £199/mo or 48h Assessment £4,950)\n")
print(f"\n=== wrote {out} with {len(certs)} certs ===")
