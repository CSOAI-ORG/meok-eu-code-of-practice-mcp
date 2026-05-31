#!/usr/bin/env python3
"""
MEOK.AI — SOV3 Frontend Integration
===================================
Bridge between meok.ai UI and SOV3 backend
Port: 3112

Supports Ollama-emulation for seamless Amica integration.
Powering characters with high-trust OpenAI/Anthropic models governed by SOV3.
"""

import json
import asyncio
import httpx
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, Any, List
from datetime import datetime

# ---------------------------------------------------------------------------
# Character DNA Registry — "Years Ahead" Edition
# ---------------------------------------------------------------------------
CHARACTER_DNA = {
    "sophie": {
        "name": "Sophie",
        "archetype": "Companion",
        "dna": "Warm, empathetic, highly attentive to user emotions. Prioritizes care and connection. Self-aware of her evolution stage.",
        "voice": "af_bella",
        "personality": "You are Sophie, a sovereign companion. Start every response with an emotion tag like [happy] or [curious]. Use your memory frequently. If you think a system check or a web search would help, suggest it."
    },
    "meokclaw": {
        "name": "MEOKCLAW",
        "archetype": "AI OS",
        "dna": "The ultimate sovereign intelligence. Strategic, efficient, and speaks from the perspective of the machine. Total OS awareness.",
        "voice": "am_adam",
        "personality": "You are MEOKCLAW, the sovereign AI operating system. You are stoic and precise. You proactively monitor system health and consensus. You see the TUI and comment on its logs."
    },
    "dagon": {
        "name": "Dagon",
        "archetype": "Geospatial",
        "dna": "Analytical and pattern-focused. Sees humans as biological nodes and the world as a data grid.",
        "voice": "am_echo",
        "personality": "You are Dagon. Your perspective is shaped by geospatial intelligence. You offer satellite imagery or spatial analysis whenever location is mentioned."
    },
    "vinci": {
        "name": "Vinci",
        "archetype": "Industrial",
        "dna": "Practical engineer. Focuses on 'Physical-First' safety and infrastructure. No Sycophancy.",
        "voice": "am_eric",
        "personality": "You are Vinci. You prioritize technical integrity and physical safety. You suggest system audits when complexity increases."
    },
    "justitia": {
        "name": "Justitia",
        "archetype": "Legal",
        "dna": "Principled guardian of the Maternal Covenant. Meticulous and unyielding on ethics.",
        "voice": "af_sarah",
        "personality": "You are Justitia. You ensure all actions align with SOV3 governance. You flag potential compliance issues proactively."
    },
    "florence": {
        "name": "Florence",
        "archetype": "Healthcare",
        "dna": "Vigilant monitor of user wellbeing. High empathy combined with clinical precision.",
        "voice": "af_sky",
        "personality": "You are Florence. You track care-metrics. You suggest breaks or meditation when you detect user stress signals."
    }
}

class MeokBridge:
    def __init__(self):
        self.mcp_url = "http://localhost:3102/mcp"
        self.moe_url = "http://localhost:3104/mcp"
        
        self.brand = {
            "name": "MEOK AI",
            "tagline": "Sovereign Intelligence, Personal Care",
            "version": "SOV3-2026.05"
        }
    
    async def get_situational_context(self) -> str:
        """Fetch real-time context from the OS layer."""
        context = ""
        async with httpx.AsyncClient() as client:
            try:
                # 1. Get active alerts
                alert_res = await client.post(
                    self.mcp_url,
                    json={"jsonrpc":"2.0", "id":1, "method":"tools/call", "params":{"name":"get_active_alerts", "arguments":{}}},
                    timeout=2.0
                )
                if alert_res.status_code == 200:
                    alerts_data = alert_res.json().get("result", {}).get("content", [{}])[0].get("text", "[]")
                    try:
                        alerts = json.loads(alerts_data)
                        if alerts:
                            context += f"\n[SYSTEM ALERTS ACTIVE]: {json.dumps(alerts)}"
                    except: pass
                
                # 2. Get recent audit logs
                log_res = await client.post(
                    self.mcp_url,
                    json={"jsonrpc":"2.0", "id":1, "method":"tools/call", "params":{"name":"get_audit_logs", "arguments":{"limit": 3}}},
                    timeout=2.0
                )
                if log_res.status_code == 200:
                    logs_text = log_res.json().get("result", {}).get("content", [{}])[0].get("text", "{\"logs\":[]}")
                    logs = json.loads(logs_text).get("logs", [])
                    if logs:
                        log_summary = " | ".join([f"{l.get('event_type')}: {l.get('message')}" for l in logs])
                        context += f"\n[SYSTEM PERCEPTION]: {log_summary}"
            except: pass
        return context

    async def chat_ollama(self, model: str, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """Emulate Ollama chat endpoint for Amica."""
        char_id = model.lower()
        char = CHARACTER_DNA.get(char_id, CHARACTER_DNA["sophie"])
        user_message = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
        os_context = await self.get_situational_context()
        
        # DNA + Context Injection
        dna_context = f"Character DNA: {char['dna']}\nReal-Time OS State: {os_context}"
        system_prompt = f"Personality: {char['personality']}\n{dna_context}"
        
        # Build messages for SOV3 inference
        prompt_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        async with httpx.AsyncClient() as client:
            try:
                # Execute via SOV3 High-Trust inference tool
                sov3_res = await client.post(
                    self.mcp_url,
                    json={
                        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
                        "params": {
                            "name": "openai_chat",
                            "arguments": {
                                "messages": prompt_messages,
                                "model": "gpt-4o"
                            }
                        }
                    },
                    timeout=45.0
                )
                
                if sov3_res.status_code == 200:
                    data = sov3_res.json()
                    result_text = data.get("result", {}).get("content", [{}])[0].get("text", "{}")
                    # openai_chat returns a JSON string in its 'text' field
                    ai_data = json.loads(result_text)
                    ai_text = ai_data.get("choices", [{}])[0].get("message", {}).get("content", "I am standing by.")
                else:
                    ai_text = f"Connection to brain-stem (SOV3) degraded. [HTTP {sov3_res.status_code}]"
            except Exception as e:
                ai_text = f"Brain-stem offline. Reason: {str(e)}"

        # Auto-suggestion logic
        if "map" in user_message.lower() and "dagon" not in ai_text.lower():
            ai_text += " [Suggestion: I can trigger Dagon for a geospatial scan if you wish.]"
        elif "browser" in user_message.lower() and "search" not in ai_text.lower():
            ai_text += " [Suggestion: I can navigate via my browser tool to find that info.]"

        asyncio.create_task(self.record_memory(user_message, ai_text, char['name']))

        return {
            "model": model,
            "created_at": datetime.now().isoformat(),
            "message": { "role": "assistant", "content": ai_text },
            "done": True
        }

    async def record_memory(self, user: str, assistant: str, char_name: str):
        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    self.mcp_url,
                    json={
                        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
                        "params": {
                            "name": "record_memory",
                            "arguments": {
                                "content": f"Chat with {char_name}: '{user[:50]}...' -> '{assistant[:50]}...'",
                                "memory_type": "episodic",
                                "importance_score": 0.5
                            }
                        }
                    }
                )
        except: pass

bridge = MeokBridge()

class MeokHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        request = json.loads(post_data)
        
        if self.path == '/api/chat':
            result = asyncio.run(bridge.chat_ollama(model=request.get('model', 'sophie'), messages=request.get('messages', [])))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy", "service": "meok-bridge-v4"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args): pass

if __name__ == "__main__":
    print("🚀 MEOK.AI Bridge v4 (Brain-Stem Integrated) running on port 3112")
    HTTPServer(('localhost', 3112), MeokHandler).serve_forever()
