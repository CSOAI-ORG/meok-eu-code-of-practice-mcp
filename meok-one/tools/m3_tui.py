#!/usr/bin/env python3
"""
MEOK — MiniMax M3 TUI.  A clean terminal chat with MiniMax M3 (the dual-agent
auditor: Claude builds / M3 audits / Nick sovereign).

M3 runs FREE on this Mac via Ollama's cloud proxy (model `minimax-m3:cloud`) — no
OpenRouter key. This talks straight to local Ollama with streaming, so you see M3
think in real time.

    python3 tools/m3_tui.py                 # interactive chat
    echo "hi" | python3 tools/m3_tui.py     # one-shot (pipe)

Commands inside the chat:
    /audit <text>   ask M3 to adversarially audit a claim/plan/diff (auditor role)
    /reset          clear the conversation
    /quit           exit
"""
import json
import sys
import urllib.request

OLLAMA = "http://localhost:11434/api/chat"
MODEL = "minimax-m3:cloud"

# ANSI
C = dict(reset="\033[0m", dim="\033[2m", cyan="\033[36m", mag="\033[35m",
         yel="\033[33m", grn="\033[32m", red="\033[31m", bold="\033[1m",
         indigo="\033[38;5;99m", gray="\033[38;5;245m")

BANNER = f"""{C['indigo']}{C['bold']}
  ███╗   ███╗██████╗     ┌─ MiniMax M3 ─┐
  ████╗ ████║╚═══██╗     │  auditor /   │
  ██╔████╔██║ █████╔╝    │  reasoner    │
  ██║╚██╔╝██║ ╚═══██╗    └──────────────┘
  ██║ ╚═╝ ██║██████╔╝   {C['gray']}MEOK dual-agent · free via Ollama{C['indigo']}
  ╚═╝     ╚═╝╚═════╝{C['reset']}
  {C['gray']}/audit <text>  ·  /reset  ·  /quit{C['reset']}
"""

AUDIT_SYS = ("You are MiniMax M3, the AUDITOR in a dual-agent protocol (Claude builds, "
             "you audit, Nick is sovereign). Be adversarial and concrete: find the flaw, "
             "the unverified claim, the risk. If it's sound, say so plainly and briefly. "
             "No flattery.")
CHAT_SYS = ("You are MiniMax M3 running locally for Nick (MEOK AI Labs). Be direct, "
            "technical, and honest. No filler.")


def stream(messages):
    """Stream a chat completion from local Ollama, printing tokens as they arrive.
    Returns the full assistant text."""
    body = json.dumps({"model": MODEL, "messages": messages, "stream": True}).encode()
    req = urllib.request.Request(OLLAMA, data=body,
                                 headers={"Content-Type": "application/json"})
    full = []
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            for line in r:
                line = line.strip()
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                except json.JSONDecodeError:
                    continue
                tok = chunk.get("message", {}).get("content", "")
                if tok:
                    full.append(tok)
                    sys.stdout.write(C["grn"] + tok + C["reset"])
                    sys.stdout.flush()
                if chunk.get("done"):
                    break
    except Exception as e:  # noqa: BLE001
        print(f"\n{C['red']}[M3 unreachable: {type(e).__name__}. Is Ollama up on :11434?]{C['reset']}")
        return ""
    print()
    return "".join(full)


def main():
    # piped one-shot
    if not sys.stdin.isatty():
        q = sys.stdin.read().strip()
        if q:
            stream([{"role": "system", "content": CHAT_SYS}, {"role": "user", "content": q}])
        return

    print(BANNER)
    history = [{"role": "system", "content": CHAT_SYS}]
    while True:
        try:
            msg = input(f"{C['cyan']}{C['bold']}you ›{C['reset']} ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{C['gray']}bye.{C['reset']}")
            return
        if not msg:
            continue
        if msg in ("/quit", "/q", "/exit"):
            print(f"{C['gray']}bye.{C['reset']}")
            return
        if msg == "/reset":
            history = [{"role": "system", "content": CHAT_SYS}]
            print(f"{C['gray']}(conversation cleared){C['reset']}")
            continue
        if msg.startswith("/audit"):
            target = msg[len("/audit"):].strip() or input(f"{C['yel']}audit what? ›{C['reset']} ").strip()
            print(f"{C['mag']}{C['bold']}M3 audit ›{C['reset']}")
            stream([{"role": "system", "content": AUDIT_SYS}, {"role": "user", "content": target}])
            continue
        history.append({"role": "user", "content": msg})
        print(f"{C['mag']}{C['bold']}M3 ›{C['reset']}")
        reply = stream(history)
        if reply:
            history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
