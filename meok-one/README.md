# MEOK ONE

**The unified consumer AI.** A consumer hatches their own care-director — one AI character that fronts the entire MEOK / SOV3 substrate. The character is the **face + personality**; SOV3 (110 tools, council, care-LLM, memory) is the **mind**.

> Think Step-3.5-with-a-character: the whole OS, but you talk to *your* character, not a chatbot.

## The 4 layers (built + tested, staged)

```
  ┌─ FACE ───────────────────────────────────────────────┐
  │  Amica 3D VRM avatar / web / TUI  (the surface)        │  ← Stage 5 (wires to this)
  └───────────────────────────────────────────────────────┘
            │ reads character config from
  ┌─ REGISTRY ────────────────────────────────────────────┐
  │  meok_one/registry.py — THE canonical source           │  ✅ Stage 1 (16 tests)
  │  27 characters · 8 archetypes · 5 care-styles · 6 hatch │
  │  stages. Replaces 4 duplicate character_factory copies. │
  └───────────────────────────────────────────────────────┘
            │ persona feeds
  ┌─ BRAIN ───────────────────────────────────────────────┐
  │  meok_one/brain.py — character.say() → SOV3 nemotron    │  ✅ Stage 2 (6 tests, live-verified)
  │  persona becomes system_prompt → in-character reply     │
  └───────────────────────────────────────────────────────┘
            │ onboarding via
  ┌─ HATCH ───────────────────────────────────────────────┐
  │  meok_one/hatch.py — egg → choose archetype/care-style/ │  ✅ Stage 3 (5 tests)
  │  name → hatch → talk → XP grows it through 6 stages     │
  └───────────────────────────────────────────────────────┘
```

## Does it hatch? Yes.
6 emergence stages (already in the data): 🥚 egg(0) → 🐣 cracking(10) → ✨ hatching(25) → 🌱 growing(50) → 🌟 mature(100) → 👑 **full sovereign**(200). Every exchange grows the bond (XP); characters and stages unlock as you go.

## Customisable options (what the consumer picks at hatch)
- **archetype** (8): challenger · nurturer · explorer · strategist · creator · guardian · sage · seeker
- **care_style** (5): gentle · supporter · challenger · explorer · seeker
- **name** (theirs) + inherited **voice** (ElevenLabs-ready params) + **visual** (colour/emoji/gradient)

## Quick start
```python
from meok_one import Registry
from meok_one.brain import talk
from meok_one.hatch import HatchSession

talk("aria", "I've had a long week.")          # talk to a character live (needs SOV3 :3101)

s = HatchSession()
s.hatch("nurturer", "gentle", "Bramble")        # hatch a care-director
s.talk("Hi Bramble, help me feel calmer.")      # bond grows it through the stages
```
```
python3 -m meok_one.hatch     # full hatch-flow demo
python3 -m meok_one.brain aria "hello"
python3 tests/test_registry.py && python3 tests/test_brain.py && python3 tests/test_hatch.py
```

## Live proof (2026-05-30)
Same brain, same question *"I procrastinate and feel guilty"*:
- **Aria 🌸** (nurturer): *"it takes courage to even name what you're feeling… one small, gentle step kind to yourself"*
- **Marcus ⚡** (challenger): *"Guilt is wasted energy—convert it into action. Whose standard are you measuring against?"*

The persona genuinely shapes SOV3's reply. One OS, many faces.

## Deprecation note
This package replaces the 4 scattered `character_factory.py` copies (`meok/core/`, `meok/meok/core/`, `meok/meok/mcp/tools/`) + duplicate `characters.json`. **Point all surfaces at `meok_one.Registry`.** Old copies should be deleted once consumers migrate.

## Still ahead
- **Stage 5:** wire the Amica 3D VRM avatar (`meok-amica/`) face → this registry/brain.
- Sign each exchange with the attestation layer (proofof.ai) for the EU AI Act Art 12/14 audit trail.

© CSOAI LTD (trading as MEOK AI Labs) · MIT
