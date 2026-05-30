"""
MEOK ONE — the unified consumer AI: hatch your care-director, talk to one
character that fronts the whole MEOK/SOV3 substrate.

This package is THE canonical character layer. Every surface (SaaS, TUI, voice,
Amica 3D avatar, inner-LLMs) reads characters from here.
"""
from .registry import Registry, default

__version__ = "0.1.0"
__all__ = ["Registry", "default"]
