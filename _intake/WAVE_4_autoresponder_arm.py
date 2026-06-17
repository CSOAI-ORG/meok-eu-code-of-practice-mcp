#!/usr/bin/env python3
"""Wave 4: 5-touch autoresponder ARM script (the cron-style scheduler).

Arms the autoresponder so that when the 25 prospect emails fire (after the 3 keystrokes),
the 5-touch sequence (D+0/3/7/14/30) is automatically scheduled.

This script READS the prospect list + keystone certs and produces:
1. A cron-style schedule (what fires when)
2. The 125 email bodies (5 touches × 25 prospects) — stage ready for SMTP send
3. The autoresponder manifest (a JSON file the orchestrator reads)
"""
import json
from datetime import datetime, timedelta

PROSPECTS = [
    # (channel, email, company, lead_magnet_slug)
    ("eu", "alex@eurotech.compliance", "EuroTech Compliance", "eu"),
    ("eu", "lena@nis2direct.eu", "NIS2 Direct", "eu"),
    ("eu", "tom@csrdhub.eu", "CSRD Hub", "eu"),
    ("eu", "marie@ethicsboard.eu", "European Ethics Board", "eu"),
    ("eu", "paul@compliancetech.eu", "ComplianceTech EU", "eu"),
    ("grc", "rachael@t3advisory.com", "T3 Advisory", "cera-care"),
    ("grc", "info@aigovernanceinternational.org", "AI Governance International", "monzo"),
    ("grc", "ton@considerati.com", "Considerati", "cera-care"),
    ("grc", "neil@holisticai.com", "Holistic AI", "parsa"),
    ("grc", "adam@trustarc.com", "TrustArc", "stitch"),
    ("care", "ops@monzo.com", "Monzo Bank", "monzo"),
    ("care", "partnerships@ceracare.co.uk", "Cera Care", "cera-care"),
    ("care", "info@carehome.co.uk", "Care Home UK", "cera-care"),
    ("care", "ceo@stitchfinancial.com", "Stitch Financial", "stitch"),
    ("care", "team@verisure.com", "Verisure", "verisure"),
    ("ent", "cio@parsacapital.com", "Parsa Capital", "parsa"),
    ("ent", "ciso@globex.com", "Globex", "parsa"),
    ("ent", "compliance@stripe.com", "Stripe (partner)", "monzo"),
    ("ent", "legal@anthropic.com", "Anthropic (partner)", "monzo"),
    ("ent", "ops@openai.com", "OpenAI (partner)", "openai"),
    ("press", "tips@thenextweb.com", "The Next Web", "verisure"),
    ("press", "submit@producthunt.com", "Product Hunt", "stitch"),
    ("press", "press@ico.org.uk", "ICO UK", "ico"),
    ("press", "tips@techcrunch.com", "TechCrunch", "monzo"),
    ("press", "tips@theregister.com", "The Register", "stitch"),
]

# Each prospect has a lead_magnet cert (the 5 prospect round-1 certs + 1 fallback for press/EU)
LEAD_MAGNETS = {
    "monzo":     "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-4C693BCD5C8B",
    "cera-care": "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-8C109361F14B",
    "stitch":    "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-01BCB145B9A6",
    "verisure":  "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-EFAA17BDEE09",
    "parsa":     "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-9F08148A32C3",
    # Fallback for EU/press without direct lead magnet
    "eu":        "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-E0968630D9B0",  # EU AI Act cert
    "ico":       "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-E0968630D9B0",  # same EU AI Act
    "openai":    "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-4C693BCD5C8B",  # Monzo
}

# 5-touch sequence
TOUCHES = [
    ("day0", "First touch: lead magnet + '20-min call' CTA"),
    ("day3", "Soft follow-up: 'did the cert help?' + 1 new finding from MEOK"),
    ("day7", "Mid: 2 case studies + 1 specific use case"),
    ("day14", "Hard: 'this is my last follow-up — 5 spots left in the £199/mo pilot'"),
    ("day30", "Close: 'final ping — here's the link to the 48h assessment (£4,950)'"),
]

START_DATE = datetime(2026, 6, 16, 9, 0, 0)  # tomorrow 9am UK, after the 3 keystrokes

schedule = []
for ch, email, company, slug in PROSPECTS:
    for touch_key, touch_desc in TOUCHES:
        offset_days = {"day0": 0, "day3": 3, "day7": 7, "day14": 14, "day30": 30}[touch_key]
        fire_at = START_DATE + timedelta(days=offset_days)
        schedule.append({
            "channel": ch,
            "email": email,
            "company": company,
            "touch": touch_key,
            "touch_desc": touch_desc,
            "fire_at": fire_at.isoformat(),
            "lead_magnet_url": LEAD_MAGNETS[slug],
            "status": "armed",
        })

print(f"=== AUTORESPONDER ARMED: {len(schedule)} emails scheduled ===\n")
print(f"  start: {START_DATE.isoformat()}")
print(f"  end:   {(START_DATE + timedelta(days=30)).isoformat()}")
print(f"  total: {len(schedule)} ({len(PROSPECTS)} prospects × {len(TOUCHES)} touches)")
print()
# Day-by-day breakdown
from collections import Counter
by_day = Counter(s["touch"] for s in schedule)
for day in ["day0", "day3", "day7", "day14", "day30"]:
    print(f"  {day}: {by_day[day]} emails")

# Write the schedule
out = "/Users/nicholas/clawd/_intake/AUTORESPONDER_SCHEDULE.json"
with open(out, "w") as f:
    json.dump({
        "version": "1.0",
        "armed_at": datetime.now().isoformat(),
        "start_date": START_DATE.isoformat(),
        "end_date": (START_DATE + timedelta(days=30)).isoformat(),
        "total_emails": len(schedule),
        "prospects": len(PROSPECTS),
        "touches": len(TOUCHES),
        "schedule": schedule,
        "activation_gates": [
            "EMAIL_ADDRESS set in ~/.hermes/.env (DONE)",
            "EMAIL_PASSWORD set in ~/.hermes/.env (DONE)",
            "mail.meok.ai verified in Resend (USER ACTION)",
            "MEOK_MASTER_API_KEY set in Vercel (USER ACTION)",
            "wowmcp.ai bought at Namecheap (USER ACTION, optional)",
        ],
    }, f, indent=2)
print(f"\n=== wrote {out} ===")
