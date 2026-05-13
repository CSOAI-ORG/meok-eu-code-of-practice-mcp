# MEOK/CSOAI — Pricing Single Source of Truth

**Last Updated:** 2026-05-09
**Authority:** This document overrides all other pricing docs. If any other file conflicts, THIS is correct.
**Source:** `clawd/meok-labs-engine/monetization_engine.py` + live Stripe price IDs

---

## MCP Subscription Packs

| Tier | Monthly | Annual (save ~17%) | Stripe Product ID | Monthly Price ID | Annual Price ID |
|------|---------|---------------------|-------------------|------------------|-----------------|
| **Core** | £49/mo | £470/yr | `meok-core` | `price_1TUKOtQvIueK5XpbLsnE5vJ5` | `price_1TUKPtQvIueK5XpbLsnE5vJ5` |
| **Governance** | £149/mo | £1,430/yr | `meok-governance` | `price_1TUKOuQvIueK5XpbU2uVM87H` | `price_1TUKPuQvIueK5XpbU2uVM87H` |
| **Security** | £199/mo | £1,910/yr | `meok-security` | `price_1TUKOvQvIueK5XpbaANgKzER` | `price_1TUKPvQvIueK5XpbaANgKzER` |
| **Industry** | £299/mo | £2,870/yr | `meok-industry` | `price_1TUKOwQvIueK5XpbM8AtgSxg` | `price_1TUKPwQvIueK5XpbM8AtgSxg` |
| **Defence** | £499/mo | £4,790/yr | `meok-defence` | `price_1TUKOvQvIueK5Xpbx2PspAy6` | `price_1TUKPvQvIueK5Xpbx2PspAy6` |
| **COBOL Bridge Pro** | £199/mo | £1,910/yr | `cobol-bridge-pro` | `price_1TUKOwQvIueK5XpbVLs5ZbCU` | `price_1TUKPwQvIueK5XpbVLs5ZbCU` |

### Target Markets

| Tier | Who It's For |
|------|-------------|
| Core | Developers, startups, indie hackers |
| Governance | Enterprises, regulated industries, compliance teams |
| Security | Security teams, MSSPs, government |
| Industry | Infrastructure operators, utilities, regulators |
| Defence | Defence contractors, government agencies |
| COBOL Bridge Pro | Banks, insurance, government with COBOL systems |

---

## One-Time Products (Live Payment Links)

| Product | Price | Payment Link |
|---------|-------|-------------|
| EU AI Act Compliance Toolkit | £199 | https://buy.stripe.com/6oUfZja8s002cIB56o8k831 |
| Asimov V8 Robot CAD Pack | £29 | https://buy.stripe.com/6oU6oJ94o4gi9wpfL28k832 |
| 48-Hour Compliance Assessment | £5,000 | https://buy.stripe.com/4gM7sN2G0bIKeQJfL28k833 |
| MEOK Compliance Pack (monthly) | £49/mo | https://buy.stripe.com/7sY7sN2G01466kdaqI8k834 |
| Enterprise All Access (monthly) | £499/mo | https://buy.stripe.com/28EcN7fsM002fUN1Uc8k835 |

---

## Pricing History

| Date | Change | Notes |
|------|--------|-------|
| 2026-04-26 | Initial Stripe setup | 58 products created |
| 2026-04-26 | Pricing pivot | Added Indie tier (£499/yr), split NIS2 |
| 2026-05-05 | Temporary price change | Changed to £79/£99/£149/£199 — REVERTED |
| 2026-05-07 | Restored original prices | Back to £49/£149/£199/£499/£299/£199 |

---

## Rules

1. **NEVER change prices without updating this file FIRST**
2. **All Stripe price IDs must match this document**
3. **If Stripe dashboard differs from this file, Stripe is wrong — fix it**
4. **All other pricing docs are deprecated and should be deleted:**
   - `revenue/STRIPE_PRICING_PIVOT_2026-04-26.md` (historical only)
   - `revenue/STRIPE_NEW_LINKS_2026-04-26.md` (superseded)
   - `fix-stripe-pricing.py` (delete after verification)
   - `fix-stripe-pricing-NOW.sh` (delete after verification)
   - `meok-labs-engine/stripe-pricing-fixes.json` (delete after verification)
   - `meok-labs-engine/fix-stripe-pricing.js` (delete after verification)

---

## Stripe Mode Status

- **Current Mode:** ⚠️ TEST MODE (Live mode not activated)
- **Action Required:** Switch Stripe to LIVE mode in dashboard
- **Impact:** £25K/month revenue blocked until LIVE mode active
- **Live Key Location:** `~/.secrets/stripe_live.env` (exports `STRIPE_LIVE_KEY`)
