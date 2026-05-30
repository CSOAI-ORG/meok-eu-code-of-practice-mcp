# MEOK ONE

**The unified consumer AI.** A consumer hatches their own care-director — one AI character that fronts the entire MEOK / SOV3 substrate. The character is the **face + personality**; SOV3 (live tools, council, care-LLM, memory) is the **mind**. Big AI companies, games, and enterprises plug in via one neutral rail.

> Think Step-3.5-with-a-character: the whole OS, but you talk to *your* character, not a chatbot.

## The 6 modules (all built + tested — 54/54 passing)

```
  ┌─ FACE ────────────────────────────────────────────────┐
  │  Amica 3D VRM avatar / web / TUI  (the surface)         │  ◻ next — wires to the rail below
  └────────────────────────────────────────────────────────┘
            │ everything below is shipped code
  ┌─ REGISTRY ─────────────────────────────────────────────┐
  │  registry.py — THE canonical character source           │  ✅ 16 tests
  │  27 characters · 8 archetypes · 5 care-styles · 6 hatch  │
  └────────────────────────────────────────────────────────┘
  ┌─ BRAIN ────────────────────────────────────────────────┐
  │  brain.py — character.say() → SOV3 LLM (system_prompt)   │  ✅ 6 tests
  │  persona → in-character reply; honest offline fallback   │
  └────────────────────────────────────────────────────────┘
  ┌─ HATCH ────────────────────────────────────────────────┐
  │  hatch.py — egg → choose archetype/care-style/name →     │  ✅ 5 tests
  │  hatch → talk → XP grows it through 6 emergence stages    │
  └────────────────────────────────────────────────────────┘
  ┌─ CONNECT (the rail others plug into) ──────────────────┐
  │  connect.py — returns INGREDIENTS not replies:           │  ✅ 13 tests (w/ memory)
  │  {system_prompt, memory_context, safety_policy, billing}.│
  │  Platform runs its OWN model. Tier-gated. Game age-gates;│
  │  enterprise audit. Model-agnostic → MEOK runs no LLM.    │
  └────────────────────────────────────────────────────────┘
  ┌─ MEMORY (the moat) ────────────────────────────────────┐
  │  memory.py — per-user CROSS-PLATFORM memory over SOV3.   │  ✅ tested
  │  GDPR export (Art 20) + honest forget (Art 17).          │
  └────────────────────────────────────────────────────────┘
  ┌─ TIERS (the business model) ───────────────────────────┐
  │  tiers.py — the "everyone eats" ladder.                  │  ✅ 14 tests
  └────────────────────────────────────────────────────────┘
```

## Does it hatch? Yes.
6 emergence stages (in the data): 🥚 egg(0) → 🐣 cracking(10) → ✨ hatching(25) → 🌱 growing(50) → 🌟 mature(100) → 👑 **full sovereign**(200). Every exchange grows the bond (XP); characters and stages unlock as you go.

## Customisable options (what the consumer picks at hatch)
- **archetype** (8): challenger · nurturer · explorer · strategist · creator · guardian · sage · seeker
- **care_style** (5): gentle · supporter · challenger · explorer · seeker
- **name** (theirs) + inherited **voice** (ElevenLabs-ready params) + **visual** (colour/emoji/gradient)

## The "everyone eats" ladder (tiers.py)
| Tier | Price | Who | Buy |
|---|---|---|---|
| **Local** | £0, self-host, OSS | privacy-first / devs / wary | `pip install` (free) |
| **Free** | £0 hosted | consumer on-ramp | sign up (free) |
| **Pro** | £9/mo | engaged consumers | [buy.stripe.com/8x2dRb…](https://buy.stripe.com/8x2dRb94obIK8sl1Uc8k916) |
| **Usage** | £0.002 / interaction | AI cos + games embedding at scale | contract (metered) |
| **Enterprise** | £1,499/mo + RegGeoInt | regulated / government | [buy.stripe.com/3cI3cx…](https://buy.stripe.com/7sY5kF3K4cMObEx2Yg8k917) |

> Live Stripe links (MEOK AI LTD) — full IDs in [`STRIPE_LINKS.md`](STRIPE_LINKS.md). Local + Free are genuinely £0 (no product). Usage is sub-penny → metered price set in the Stripe dashboard, not self-serve.

Big AI companies eat on the paid tiers (Usage/Enterprise); the wary self-host Local for free — which still grows the network. **Ownership = GDPR + attestation fused** (you own your data; MEOK cryptographically proves it honoured export/delete) — not NFTs.

## Quick start
```python
from meok_one import Registry, talk, HatchSession, connect, quote

talk("aria", "I've had a long week.")             # talk to a character live (needs SOV3 :3101)

s = HatchSession()
s.hatch("nurturer", "gentle", "Bramble")           # hatch a care-director
s.talk("Hi Bramble, help me feel calmer.")         # bond grows it through the stages

connect("aria", user_id="u1", message="hi", tier="pro")   # the rail a platform calls
quote("usage", 500_000)                            # what 500k interactions/mo costs
```
```
python3 -m meok_one.hatch          # full hatch-flow demo
python3 -m meok_one.connect        # how a platform plugs in
python3 -m meok_one.tiers          # the pricing ladder
# tests:
for t in registry brain hatch connect_memory tiers; do python3 tests/test_$t.py; done
```

## Status (honest)
- **Architecture: built + tested.** All 6 modules, 54/54 tests pass. The persona→system_prompt→SOV3 path is wired correctly and degrades honestly when SOV3 is unreachable (returns a marked offline stub — never fabricates a reply).
- **Live character replies: blocked on SOV3's LLM endpoint.** `nemotron_chat` currently returns a 404 from the upstream NVIDIA API, so live replies hit the offline fallback. The bridge is correct; the model behind it needs configuring (or pointing `brain.py` at a working SOV3 LLM tool such as `hermes_ask`).
- **Attestation (Pro/Usage/Enterprise promise): coded, not yet demonstrable** — `proofof.ai/api/verify` serves a static page and 404s on the API. Needs the attestation API deployed before the "signed receipt" claim is live.

## Deprecation note
This package replaces the scattered `character_factory.py` copies (`meok/core/`, `meok/meok/core/`, `meok/meok/mcp/tools/`) + duplicate `characters.json`. **Point all surfaces at `meok_one.Registry`.** Delete the old copies once consumers migrate.

## Still ahead
- Wire the Amica 3D VRM avatar (`meok-amica/`) face → this registry/brain/connect rail.
- Sign each exchange with the attestation layer (proofof.ai) for the EU AI Act Art 12/14 audit trail (once the verify API is live).
- Wire the 5 tiers to real Stripe products to make them chargeable.

---
© CSOAI LTD (trading as MEOK AI Labs) · MIT
