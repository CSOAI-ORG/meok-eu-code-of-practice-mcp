"""
MEOK ONE — the unified consumer AI: hatch your care-director, talk to one
character that fronts the whole MEOK/SOV3 substrate.

This package is THE canonical character layer. Every surface (SaaS, TUI, voice,
Amica 3D avatar, inner-LLMs) reads characters from here.

Public API:
    Registry, default          — the 27-character canonical registry (registry.py)
    Character, talk            — a character as a live talking endpoint (brain.py)
    HatchSession, hatch_session — the hatch onboarding flow (hatch.py)
    connect, remember          — the neutral rail platforms plug into (connect.py)
    MemoryBridge, bridge       — cross-platform per-user memory (memory.py)
    TIERS, get_tier, quote, ladder, entitlements — the pricing ladder (tiers.py)
"""
from .registry import Registry, default
from .brain import Character, talk
from .hatch import HatchSession, hatch_session
from .connect import connect, remember, integration_spec
from .memory import MemoryBridge, bridge
from .tiers import TIERS, get_tier, quote, ladder, entitlements, can_hatch

__version__ = "0.1.0"
__all__ = [
    "Registry", "default",
    "Character", "talk",
    "HatchSession", "hatch_session",
    "connect", "remember", "integration_spec",
    "MemoryBridge", "bridge",
    "TIERS", "get_tier", "quote", "ladder", "entitlements", "can_hatch",
]
