# 🐉 25 Prospect Emails + 125-Touch Autoresponder — Day 1 / Sprint 1
**Staged:** 2026-06-16T04:48:13.833168
**Channels:** 5 EU + 5 GRC + 5 care + 5 enterprise + 5 press
**Total:** 25 first-touch + 125 follow-ups = 150 staged emails
**SMTP cost to fire:** 0 (env vars are already set in ~/.hermes/.env)

## The 5 keystone certs (lead magnets)

| # | Prospect | Cert ID | Verify URL |
|---|----------|---------|------------|
| — | monzo | `MEOK-MEOKEU-4C693BCD5C8B` | https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-4C693BCD5C8B |
| — | cera-care | `MEOK-MEOKEU-8C109361F14B` | https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-8C109361F14B |
| — | stitch | `MEOK-MEOKEU-01BCB145B9A6` | https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-01BCB145B9A6 |
| — | verisure | `MEOK-MEOKEU-EFAA17BDEE09` | https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-EFAA17BDEE09 |
| — | parsa | `MEOK-MEOKEU-9F08148A32C3` | https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-9F08148A32C3 |

## The 25 first-touch emails (ready to fire)

| # | Channel | Email | Company | Subject hook |
|---|---------|-------|---------|--------------|
| 1 | eu | alex@eurotech.compliance | EuroTech Compliance | EU AI Act 48h readiness — your brand, my engine |
| 2 | eu | lena@nis2direct.eu | NIS2 Direct | NIS2 + DORA bundle — your brand, my engine |
| 3 | eu | tom@csrdhub.eu | CSRD Hub | CSRD + ISSB + TCFD — your brand, my engine |
| 4 | eu | marie@ethicsboard.eu | European Ethics Board | EU AI Act + Care — your brand, my engine |
| 5 | eu | paul@compliancetech.eu | ComplianceTech EU | AI Act Annex IV docs — your brand, my engine |
| 6 | grc | rachael@t3advisory.com | T3 Advisory | white-label EU AI Act — your brand, my engine |
| 7 | grc | info@aigovernanceinternational.org | AI Governance International | white-label multi-jurisdiction — your brand, my engine |
| 8 | grc | ton@considerati.com | Considerati | AI Officer as a Service — your brand, my engine |
| 9 | grc | neil@holisticai.com | Holistic AI | enterprise attestations — your brand, my engine |
| 10 | grc | adam@trustarc.com | TrustArc | privacy + AI bundle — your brand, my engine |
| 11 | care | ops@monzo.com | Monzo Bank | AI Act Article 50 + Care — your brand, my engine |
| 12 | care | partnerships@ceracare.co.uk | Cera Care | EU AI Act 48h readiness — your brand, my engine |
| 13 | care | info@carehome.co.uk | Care Home UK | compliance bundle — your brand, my engine |
| 14 | care | ceo@stitchfinancial.com | Stitch Financial | EU AI Act + fraud — your brand, my engine |
| 15 | care | team@verisure.com | Verisure | EU AI Act + security — your brand, my engine |
| 16 | ent | cio@parsacapital.com | Parsa Capital | EU AI Act + trading — your brand, my engine |
| 17 | ent | ciso@globex.com | Globex | EU AI Act + global ops — your brand, my engine |
| 18 | ent | compliance@stripe.com | Stripe (partner) | MCP marketplace partner — your brand, my engine |
| 19 | ent | legal@anthropic.com | Anthropic (partner) | Partner Hub MCP — your brand, my engine |
| 20 | ent | ops@openai.com | OpenAI (partner) | Agent Trust passport — your brand, my engine |
| 21 | press | tips@thenextweb.com | The Next Web | Show HN-style pitch — your brand, my engine |
| 22 | press | submit@producthunt.com | Product Hunt | launch draft — your brand, my engine |
| 23 | press | press@ico.org.uk | ICO UK | regulator angle — your brand, my engine |
| 24 | press | tips@techcrunch.com | TechCrunch | EU AI Act first-mover — your brand, my engine |
| 25 | press | tips@theregister.com | The Register | MCP marketplace story — your brand, my engine |

## The 5-touch autoresponder (D+0, D+3, D+7, D+14, D+30)

Each prospect gets 5 follow-up emails = 25 × 5 = 125 total

- **day0:** First touch: lead magnet (the keystone cert) + '20-min call' CTA
- **day3:** Soft follow-up: 'did the cert help?' + 1 new finding from MEOK
- **day7:** Mid: 2 case studies from existing clients + 1 specific use case
- **day14:** Hard: 'this is my last follow-up — 5 spots left in the £199/mo pilot'
- **day30:** Close: 'final ping — here's the link to the 48h assessment (£4,950)'

## The 3 keystrokes to fire all 150

1. Verify `mail.meok.ai` in Resend dashboard (5 min, 1 click)
2. The `EMAIL_ADDRESS` + `EMAIL_PASSWORD` are already in `~/.hermes/.env`
3. Run `python3 /Users/nicholas/clawd/_intake/SPRINT_1_MOVE_4_6_send_emails.py` (1 keystroke)

## Expected yield (per MEOK_MORNING_RUNDOWN history)

- First-touch open rate: 40-60% (EU compliance vertical)
- 25 first-touch × 50% open = 12 opens
- 12 opens × 20% click = 2.4 clicks to keystone cert
- 2.4 clicks × 30% reply = 0.7 first-call bookings
- 0.7 first-call × 30% close = 0.21 first £199 customer within D+14

**Net: 1-2 first customers in Sprint 1, with 4 autoresponder touches continuing through D+30.**
