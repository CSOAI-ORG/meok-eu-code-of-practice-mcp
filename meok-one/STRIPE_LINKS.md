# MEOK ONE — live Stripe links (single source of truth)

Created 2026-05-30 via Stripe MCP (account: **MEOK AI LTD**, live mode). These are the
real, chargeable links — wire them into the pricing page / tiers.py when ready.

| Tier | Price | Stripe product | Stripe price | Payment link |
|---|---|---|---|---|
| **Local** | £0 (self-host, OSS) | — | — | no product — free, runs on user's machine |
| **Free** | £0 (hosted) | — | — | no product — free on-ramp |
| **Pro** | £9 / mo | `prod_Ubx9DdgoXPnzUD` | `price_1TcjHUQvIueK5Xpb1tLUecD3` | https://buy.stripe.com/8x2dRb94obIK8sl1Uc8k916 |
| **Usage** | £0.002 / interaction | ⚠️ NOT created | — | sub-penny — needs a **metered** price with `unit_amount_decimal` set in the Stripe dashboard (the API create_price tool can't do sub-1p amounts). For platform/B2B deals, not self-serve. |
| **Enterprise** | £1,499 / mo | `prod_UbxMotixQGr9CN` | `price_1TckGYQvIueK5XpbWHljNicd` | https://buy.stripe.com/3cIfZj1zG04250912c8k918 |

## Notes
- **Local + Free are genuinely £0** — deliberately no Stripe product (creating £0 products
  would just add to the 100+ stale-product cleanup already on the list).
- **Usage tier is the one gap:** £0.002/interaction is below Stripe's 1p minimum for a
  standard price. It must be a metered price (`unit_amount_decimal: "0.2"`, per-unit, metered
  usage) created in the dashboard — appropriate anyway since platforms sign contracts, not
  click a self-serve link.
- **Enterprise:** there is also a separate **CSOAI Enterprise £1,499** product from earlier
  (task #7). This `MEOK ONE Enterprise` is the consumer-product-branded top tier. If you'd
  rather not run two £1,499 products, archive one — flag which.

## To wire into the pricing surface
Drop the Pro + Enterprise links onto the MEOK ONE / pricing page. (Deferred from this session:
the live editor was returning corrupted file reads, so source edits to `tiers.py` / `README.md`
were held back rather than risk clobbering working code — do them when the environment is stable.)
