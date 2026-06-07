"""
MEOK ONE — THE KING: SOV3 the sovereign, talking to the 28 hive queens.

Topology (Nick's model, grounded):

    👤 you / user / agent
            │
        🤴 KING = SOV3 the sovereign  (one mouth you talk to)
            │   "which hive(s) should answer this?"  ← thin, stateless routing
     ┌──────┼──────┬───────── … ×28
     ▼      ▼      ▼
   👑meok  👑grab  👑koi   queens = hive_queen.queen(domain)  (MoE + BFT)
     └──────┴──────┴── all deposit honey ──▶ 🍯 HONEYCOMB = SOV3 memory

The king IS the sovereign (SOV3 identity), but its ROUTING is kept thin and stateless
so a SOV3 memory/VM wobble can't stop it picking a queen. Two modes:

    route(message)              -> pick the most relevant hive(s) (a fast classifier)
    king(message, fan_out=...)  -> route, call the queen(s), (fan_out) convene + synthesize

Inference runs on the GCP VM (the fast box); SOV3 (king/honeycomb) runs on the Mac :3101.
"""
from __future__ import annotations

import json
from pathlib import Path

from .router import ask
from .hive_queen import queen, load_hive, _HIVE_ROOT

# Use the SAME resident model the queens use for routing + synthesis, so a king call
# never forces an Ollama model swap on the RAM-constrained VM (one model stays loaded).
_CLASSIFIER_MODEL = "llama3.2:3b"


def hives() -> list[dict]:
    """All hives the king governs, with their domain scope (from each stack.yml)."""
    out = []
    if not _HIVE_ROOT.is_dir():
        return out
    for d in sorted(_HIVE_ROOT.glob("*-hive")):
        slug = d.name[:-5]  # strip "-hive"
        cfg = load_hive(slug)
        out.append({"slug": slug, "scope": cfg.get("scope") or slug,
                    "tools": cfg.get("tools", [])})
    return out


def route(message: str, k: int = 1, model: str = _CLASSIFIER_MODEL, tier: str = "pro") -> list[str]:
    """Pick the k most relevant hive slugs for a message. Fast LLM classifier with a
    keyword fallback so routing never hard-fails (thin + resilient — the king must
    always be able to pick a queen even if the classifier model is down)."""
    hv = hives()
    if not hv:
        return []
    # Compact catalog: slug + first ~8 words of scope. The full scopes were ~560 input
    # tokens → ~60s CPU prompt-eval. Trimming to ~150 tokens cuts routing to ~10-15s.
    def _short(s):
        return " ".join((s or "").replace("\n", " ").split()[:8])
    catalog = "\n".join(f"{h['slug']}: {_short(h['scope'])}" for h in hv)
    prompt = (f"Route this message to the ONE best MEOK hive. Reply with ONLY the slug.\n\n"
              f"{catalog}\n\nMESSAGE: {message}\nSLUG:" if k == 1 else
              f"Choose the {k} most relevant hive slugs (comma-separated, slugs only).\n\n"
              f"{catalog}\n\nMESSAGE: {message}\nSLUGS:")
    r = ask(prompt, model=model, tier=tier, max_tokens=24)
    slugs = [s.strip().lower() for s in (r.get("reply") or "").replace("\n", ",").split(",")]
    valid = {h["slug"] for h in hv}
    picked = [s for s in slugs if s in valid][:k]
    if picked:
        return picked
    # keyword fallback: score by word overlap with slug+scope
    words = set(message.lower().split())
    scored = sorted(hv, key=lambda h: -len((set((h["slug"] + " " + h["scope"]).lower().split())) & words))
    return [scored[0]["slug"]] if scored else []


def king(message: str, fan_out: bool = False, k: int = 3, brain: str = "council",
         do_gossip: bool = True, quorum: int = 3) -> dict:
    """The sovereign answers by convening the right queen(s).

    fan_out=False : route to the single best hive, return its queen's answer.
    fan_out=True  : convene the top-k queens, then the sovereign synthesizes ONE answer.
    do_gossip     : each queen records its lesson UP to the SOV3 honeycomb.
    """
    targets = route(message, k=k if fan_out else 1)
    if not targets:
        return {"king": "SOV3 sovereign", "routed_to": [], "reply":
                "[king couldn't route — no hives found]", "queens": []}

    answers = []
    for slug in targets:
        a = queen(slug, message, brain=brain, do_gossip=do_gossip, quorum=quorum)
        answers.append({"hive": slug, "reply": a.get("reply"), "engine": a.get("engine"),
                        "safe": a.get("safe"), "governance": a.get("governance")})

    if not fan_out:
        a = answers[0]
        return {"king": "SOV3 sovereign", "routed_to": targets, "mode": "route",
                "reply": a["reply"], "queens": answers}

    # fan-out: the sovereign synthesizes the queens' answers into one.
    brief = "\n\n".join(f"[{x['hive']} queen]: {x['reply']}" for x in answers)
    synth = ask(f"You are SOV3, the sovereign over MEOK's hives. {len(answers)} hive "
                f"queens answered the user. Synthesize ONE clear, safe answer for the "
                f"user, noting which hive each insight came from.\n\nUSER: {message}\n\n"
                f"QUEEN ANSWERS:\n{brief}\n\nSOVEREIGN SYNTHESIS:",
                model=_CLASSIFIER_MODEL, tier="pro", max_tokens=400)
    return {"king": "SOV3 sovereign", "routed_to": targets, "mode": "fan_out",
            "reply": synth.get("reply") or brief, "queens": answers}


if __name__ == "__main__":
    import sys
    msg = sys.argv[1] if len(sys.argv) > 1 else "I need to tip soil at a construction site — what permits?"
    fan = "--fan" in sys.argv
    print(f"=== 🤴 KING (fan_out={fan}) ===\nuser: {msg}\n")
    res = king(msg, fan_out=fan)
    print("routed_to:", res["routed_to"], "| mode:", res.get("mode"))
    print("\nreply:\n", (res["reply"] or "")[:600])
    print("\n--- queens consulted ---")
    for q in res["queens"]:
        print(f"  👑 {q['hive']}: {q['engine']} | safe={q['safe']}")
