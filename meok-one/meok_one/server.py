"""
MEOK ONE — Web server: the OS comes to life.

A thin, stdlib-only HTTP server (no Flask/FastAPI — zero deps) that exposes the
whole MEOK ONE package as JSON so a browser UX can hatch a character and talk to it.

    python3 -m meok_one.server          # serves on http://localhost:4173
    python3 -m meok_one.server 8080     # custom port

Endpoints (all JSON unless noted):
    GET  /                       -> the web UX (index.html)
    GET  /api/health             -> {ok, characters, version}
    GET  /api/archetypes         -> {archetypes[], care_styles{}, stages{}}  (the hatch picker)
    GET  /api/characters         -> the 27 seed characters (cards)
    GET  /api/brains?tier=pro    -> left/right/both availability (the brain toggle)
    POST /api/hatch  {archetype, care_style, name}        -> hatched care-director
    POST /api/think  {character, message, brain, tier}    -> live reply (Sovereign-safe)
    POST /api/voice  {character, message, brain, tier}    -> reply + TTS voice spec

Honest: /api/think calls the real local LLM (qwen3 via Ollama) — replies take a few
seconds and are never fabricated. If a backend is down the JSON says so.
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import os

from . import default, ladder, __version__
from .brains import brains, think
from .hatch import HatchSession
from .voice import voice_reply

_HERE = os.path.dirname(os.path.abspath(__file__))
_INDEX = os.path.join(_HERE, "web", "index.html")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _html(self, path):
        try:
            with open(path, "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except FileNotFoundError:
            self._json(404, {"error": "index.html not found"})

    def _body(self):
        try:
            n = int(self.headers.get("Content-Length", 0) or 0)
            return json.loads(self.rfile.read(n).decode() or "{}") if n else {}
        except (ValueError, json.JSONDecodeError):
            return {}

    def do_OPTIONS(self):
        self._json(204, {})

    def do_GET(self):
        path = urlparse(self.path).path
        qs = parse_qs(urlparse(self.path).query)
        reg = default()
        if path in ("/", "/index.html"):
            return self._html(_INDEX)
        if path in ("/avatar", "/avatar.html", "/3d"):
            return self._html(os.path.join(_HERE, "web", "avatar.html"))
        if path.endswith((".vrm", ".vrma")):
            # serve any VRM model / VRMA animation under web/ (path-traversal safe)
            base = os.path.join(_HERE, "web")
            fp = os.path.normpath(os.path.join(base, path.lstrip("/")))
            if fp.startswith(base) and os.path.isfile(fp):
                with open(fp, "rb") as f:
                    body = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            else:
                self._json(404, {"error": "not found", "path": path})
            return
        if path == "/avatar.vrm":
            try:
                with open(os.path.join(_HERE, "web", "avatar.vrm"), "rb") as f:
                    body = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except FileNotFoundError:
                self._json(404, {"error": "avatar.vrm not found"})
            return
        if path == "/api/health":
            return self._json(200, {"ok": True, "characters": reg.total, "version": __version__})
        if path == "/api/archetypes":
            return self._json(200, {
                "archetypes": [{"id": a["id"], "label": a["label"], "description": a["description"],
                                "emoji": a["emoji"], "color": a["color"]} for a in reg.archetypes()],
                "care_styles": reg.care_styles(),
                "stages": reg.emergence_stages(),
            })
        if path == "/api/characters":
            return self._json(200, {"characters": reg.list_characters()})
        if path == "/api/brains":
            return self._json(200, brains(qs.get("tier", ["pro"])[0]))
        if path == "/api/tiers":
            return self._json(200, {"ladder": ladder()})
        return self._json(404, {"error": "not found", "path": path})

    def do_POST(self):
        path = urlparse(self.path).path
        b = self._body()
        try:
            if path == "/api/hatch":
                s = HatchSession()
                return self._json(200, s.hatch(b.get("archetype", "nurturer"),
                                               b.get("care_style", "gentle"),
                                               b.get("name") or None))
            if path == "/api/think":
                out = think(b.get("character", "aria"), b.get("message", ""),
                            brain=b.get("brain", "left"), tier=b.get("tier", "pro"),
                            user_id=b.get("user_id", "web"))
                return self._json(200, out)
            if path == "/api/voice":
                return self._json(200, voice_reply(b.get("character", "aria"), b.get("message", "")))
        except KeyError as e:
            return self._json(400, {"error": f"unknown id {e}"})
        except Exception as e:
            return self._json(500, {"error": f"{type(e).__name__}: {e}"})
        return self._json(404, {"error": "not found", "path": path})


def main(port: int = 4173):
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"=== MEOK ONE is live: http://localhost:{port} ===")
    print(f"    {default().total} characters · v{__version__} · open the URL to hatch + talk")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nMEOK ONE server stopped.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4173)
