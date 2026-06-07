# Billing Consolidation — one ladder, one backend (Decision #4)

> CSOAI lane. The "one funnel not 50 Stripe links" fix. Live account: **MEOK AI LTD**
> (`acct_1TLlEKQvIueK5Xpb`, GBP, balance £0). Authored 2026-06-07.

## Live state (audited via Stripe MCP — note: MCP can't paginate, dashboard needed for full link list)

**10 active products, all now with `default_price` set ✅ (this session):**

| Product | Price | Type |
|---------|-------|------|
| MEOK ONE Pro `prod_UdBfCGtXhbi69B` | **£9/mo** `price_1TdvHh…` | recurring ⭐ only subscription |
| NIS2 BSI Self-Serve | £99 | one-time |
| NIS2 BSI Done-For-You | £499 | one-time |
| EU AI Act Art50 Watermarking Kit | £999 | one-time |
| DORA Belgium Rapid Response | £999 | one-time |
| Compliance Audit-Prep Bundle | £4,950 | one-time |
| Smoke Test | £1 | one-time |
| PAYG £10 / £50 / £200 top-ups | £10/£50/£200 | one-time |

## Done this session (safe, reversible, no charge)
- **Set `default_price` on all 10 products.** Previously every product had `default_price: null`, forcing every Buy button / checkout to hardcode a throwaway price or link — the sprawl's root cause. Now a product resolves to its price; `meok-stripe-acp-checkout-mcp` and all skins (openmoe.ai, meok.ai) can reference the stable product id.

## Gated on Nick (real money — won't guess on a live account)
1. **Canonical consumer ladder.** Live = MEOK ONE Pro **£9/mo** only. Memory said Free/Pro **£19**/Team **£99**. These disagree. No Team product and no recurring "Compliance Pro £79" exist live. → Need the canonical ladder confirmed before creating/renaming recurring prices.
2. **Link retirement.** `has_more:true` on payment_links but the MCP can't paginate (`starting_after` is ignored) — the full sprawl can't be safely enumerated or deactivated from here. Dashboard pass, gated on (1).

## The target (once ladder confirmed)
ONE auth + ONE recurring ladder; openmoe.ai + meok.ai are skins that tag `funnel` source only; one-time compliance services stay as productised default-price items the ACP MCP serves; PAYG unchanged. Kill per-product throwaway links — reference products.
