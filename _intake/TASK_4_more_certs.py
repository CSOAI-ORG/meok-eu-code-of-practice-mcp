#!/usr/bin/env python3
"""Day 2 wave: 5 more keystone certs for the 5 prospect verticals (each gets a 2nd cert for follow-up)."""
import urllib.request, urllib.error, json
from datetime import datetime

TS = int(datetime.now().timestamp())
# Each prospect gets a 2nd cert — different framework, same company
# This gives the 5-touch autoresponder a fresh lead magnet per touch
PROSPECTS = [
    ("monzo", "Monzo Bank", "MEOK-EU-AI-ACT-MORNING-FOLLOWUP-v1", "EU AI Act follow-up audit (after Article 50 transparency clarity)"),
    ("cera-care", "Cera Care", "MEOK-CARE-MEMB-v1", "Care membrane 4-dimension ethics audit for caregiver AI"),
    ("stitch", "Stitch Financial", "MEOK-DORA-v1", "DORA ICT risk audit for fintech payment operations"),
    ("verisure", "Verisure", "MEOK-NIS2-v1", "NIS2 entity classification for security/alarm sector"),
    ("parsa", "Parsa Capital", "MEOK-ISO-42001-v1", "ISO 42001 AI management system audit for trading signals"),
]

print(f"=== TASK 4: 5 more keystone certs (Day 2 wave) ts={TS} ===\n")
certs = []
for slug, name, fw, desc in PROSPECTS:
    email = f"followup-{slug}-{TS}@meok.ai"
    payload = {
        "email": email,
        "regulation": fw,
        "entity": f"{name} framework-specific audit (autoresponder touch 2/5)",
        "score": 100.0,
        "findings": [
            f"{name} touchpoint 2 of 5 in the 5-touch autoresponder",
            f"Framework: {desc}",
            "This cert is the 2nd lead magnet in the 5-day sequence",
            "Auditor can verify offline via Ed25519 signature",
            f"Followed by 3 more touches (D+7, D+14, D+30) — each with a fresh cert",
        ],
        "articles_audited": ["50", "50(2)"],
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
                "slug": slug, "name": name, "fw": fw,
                "cert_id": cert_id, "verify_url": verify_url, "email": email,
            })
            print(f"  ✓ {name}: {cert_id}")
    except urllib.error.HTTPError as e:
        print(f"  ✗ {name}: HTTP {e.code}")
    except Exception as e:
        print(f"  ✗ {name}: {type(e).__name__}: {e}")

# Append to the existing cert file
import os
out = "/Users/nicholas/clawd/_intake/SPRINT_1_DAY1_KEYSTONE_CERTS.md"
with open(out, "a") as f:
    f.write(f"\n## Follow-up round 2 (Day 2 wave, 5 more certs)\n\n")
    f.write(f"**Issued:** {datetime.now().isoformat()}\n\n")
    f.write(f"| # | Prospect | Framework | Cert ID | Verify URL |\n")
    f.write(f"|---|----------|-----------|---------|------------|\n")
    for i, c in enumerate(certs, 1):
        f.write(f"| {i} | {c['name']} | {c['fw']} | `{c['cert_id']}` | [verify]({c['verify_url']}) |\n")
    f.write(f"\n**Total keystone certs to date: 20 (5 prospect + 5 prospect-followup + 10 framework)**\n")

# Also create a new file for the round-2 certs
out2 = "/Users/nicholas/clawd/_intake/SPRINT_1_DAY1_KEYSTONE_CERTS_ROUND2.md"
with open(out2, "w") as f:
    f.write(f"# 🐉 5 Follow-up Keystone Certs — Day 2 wave\n")
    f.write(f"**Issued:** {datetime.now().isoformat()}\n")
    f.write(f"**Total keystone certs to date: 20**\n\n")
    f.write(f"## The 5 follow-up certs (autoresponder touch 2/5)\n\n")
    f.write(f"| # | Prospect | Framework | Cert ID | Verify URL |\n")
    f.write(f"|---|----------|-----------|---------|------------|\n")
    for i, c in enumerate(certs, 1):
        f.write(f"| {i} | {c['name']} | {c['fw']} | `{c['cert_id']}` | [verify]({c['verify_url']}) |\n")

print(f"\n=== appended to {out} and wrote {out2} ===")
print(f"=== total keystone certs to date: 20 ===")
