# OLM — Organic Learning Model · Spec v0.1
*Drafted 2026-06-07 by the MEOK ONE tab, per Nick's decision (INBOX). Until this spec is accepted, OLM is **"planned"**, not shipped (honesty rule). Canonical home for this doc once accepted: the `meok-ai` repo README.*

## One-line
**OLM is the learning layer that makes a MEOK character become *yours* — it learns from your real conversations, under the care membrane, and the weights stay on hardware you control.** ("The AI that learns you, becomes you, and stays yours forever.")

## What it is NOT (kills the hype)
- Not a new foundation model. OLM does **not** pretrain an LLM.
- Not cloud-harvested. Your data is **not** training a shared global model by default.
- Not magic consciousness. It's a concrete, inspectable loop: log → score → adapt → evaluate → roll back if worse.

## The cluster that already exists (this is why OLM is "planned", not "vapor")
| Piece | Repo | Role in OLM |
|---|---|---|
| Vision / product shell | `meok-ai` 🔒 | The promise + the user-facing "your AI" framing |
| Organic agent engine | `meok-agent-zero` 🔒 | Care-gated Agent Zero fork — the runtime that "grows & learns with you" |
| **Learning mechanism** | **`meok-neural-learning`** | Shared module: logs interactions, trains the small adapters. The actual ICRL loop. |
| Cognition substrate | `consciousness-engine-mcp`, `creativity-engine-mcp` | Reflection / dream / novelty signals that feed reward |
| Retrain harness | SOV3 neural retrain + `openmoe-bft` | Nightly retrain + BFT-gated "did it actually improve?" tournament |

OLM = **naming + wiring these five into one named product**, not building from scratch.

## How it learns (the loop, concretely)
1. **Log** — every MEOK ONE conversation turn is recorded with consent (SIGIL hash-chained, [[reference_sov3_state_layers]]), tagged by character + care signals.
2. **Score** — reward = care-membrane validity × engagement × novelty (consciousness/creativity engines supply the last two). Harmful/uncared turns get **negative** reward — the membrane is a hard gate, not a suggestion.
3. **Adapt** — train small per-user / per-character **adapters** (LoRA-scale), NOT the base model. Cheap, local, reversible. Mechanism lives in `meok-neural-learning`.
4. **Evaluate** — `openmoe-bft` self-improvement tournament + SOV3 retrain gate: a new adapter ships only if a Byzantine-quorum of judges says it beat the incumbent. (Precedent: relationship_evolution_nn was **rolled back** when it regressed — [[sov3_retrain_log]]. That rollback discipline IS the product's credibility.)
5. **Persist where the user controls it** — adapters stored locally / on the user's chosen node (Mac sovereign, their VM, or device). "Stays yours."

## Where it lives
- **Engine:** `meok-neural-learning` (mechanism) + `meok-agent-zero` (runtime) + SOV3 retrain (harness).
- **Surface:** MEOK ONE `/os` — a character that visibly "remembers" and evolves (ties into the existing Tamagotchi hatch→sovereign stages: bond = accumulated learning).
- **Boundary:** OLM never crosses the care membrane (Maternal Covenant). No learning from harm; no covert persona drift.

## What's missing before "shipped"
- [ ] One adapter trained end-to-end from real MEOK ONE logs (proof the loop closes).
- [ ] The care-membrane reward sign verified (harmful turns actually push reward down).
- [ ] A user-visible "your AI has learned X" surface + an export/delete control ("stays yours" must be literally true — GDPR + the promise).
- [ ] BFT gate wired to block bad adapters automatically (not manual).

## Honest status line (use this externally)
> "OLM is MEOK's on-your-hardware learning layer — built from our neural-learning module, care-gated Agent Zero runtime, and a Byzantine-gated retrain loop. Today it's wired and in trials; the end-to-end personal-adapter loop is the next milestone."
