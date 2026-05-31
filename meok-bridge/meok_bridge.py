#!/usr/bin/env python3
"""
MEOK.AI — SOV3 Frontend Integration
===================================
Bridge between meok.ai UI and SOV3 backend
Port: 3112
"""

import json
import asyncio
import httpx
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, Any, List
from datetime import datetime

class MeokBridge:
    """
    Bridge between meok.ai frontend and SOV3 backend.
    
    Exposes SOV3 capabilities through meok.ai-branded API.
    """
    
    def __init__(self):
        self.sov3_url = "http://localhost:3101/mcp"
        self.councilof_url = "http://localhost:3103/mcp"
        self.moe_url = "http://localhost:3104/mcp"
        self.ralph_url = "http://localhost:3201/mcp"
        self.quantum_url = "http://localhost:3111/mcp"
        self.certification_url = "http://localhost:3110/api"
        
        self.brand = {
            "name": "MEOK AI",
            "tagline": "Sovereign Intelligence, Personal Care",
            "version": "SOV3-2026.05",
            "colors": {
                "primary": "#00ff88",
                "secondary": "#0088ff",
                "accent": "#ff8800"
            }
        }
    
    async def chat(self, message: str, user_id: str, session_id: str = None) -> Dict[str, Any]:
        """
        Main chat endpoint for meok.ai
        
        Flow:
        0. Situational Awareness (Alerts/Safety)
        1. Route to optimal expert (MoE)
        2. Get CouncilOf vote (governance)
        3. Generate response (SOV3)
        4. Store in memory (Qdrant)
        5. Return branded response
        """
        
        # Step 0: Situational Awareness
        awareness_context = ""
        async with httpx.AsyncClient() as client:
            try:
                # Get alerts
                alert_res = await client.post(
                    "http://localhost:3102/mcp",
                    json={"jsonrpc":"2.0", "id":1, "method":"tools/call", "params":{"name":"get_active_alerts", "arguments":{}}}
                )
                if alert_res.status_code == 200:
                    alerts = alert_res.json().get("result", {}).get("content", [{}])[0].get("text", "[]")
                    if len(alerts) > 10:
                        awareness_context += f"\n[SYSTEM ALERTS: {alerts}]"
                
                # Get last 5 audit logs for real-time perception
                log_res = await client.post(
                    "http://localhost:3102/mcp",
                    json={"jsonrpc":"2.0", "id":1, "method":"tools/call", "params":{"name":"get_audit_logs", "arguments":{"limit": 5}}}
                )
                if log_res.status_code == 200:
                    logs = log_res.json().get("result", {}).get("content", [{}])[0].get("text", "{\"logs\":[]}")
                    parsed_logs = json.loads(logs).get("logs", [])
                    if parsed_logs:
                        log_lines = "\n".join([f"- {l.get('event_type')}: {l.get('message')}" for l in parsed_logs])
                        awareness_context += f"\n[SYSTEM PERCEPTION - LAST 5 EVENTS]:\n{log_lines}"
            except: pass

        # Step 1: Route to expert
        async with httpx.AsyncClient() as client:
            route_response = await client.post(
                self.moe_url,
                json={
                    "tool": "moe_route",
                    "params": {
                        "prompt": message,
                        "type": "reasoning"
                    }
                },
                timeout=10.0
            )
            
            if route_response.status_code == 200:
                route_data = route_response.json()
                expert = route_data.get("expert", "sov3")
            else:
                expert = "sov3"
        
        # Step 2: Get CouncilOf vote
        async with httpx.AsyncClient() as client:
            vote_response = await client.post(
                self.councilof_url,
                json={
                    "tool": "councilof_vote",
                    "params": {
                        "description": f"Respond to: {message[:50]}...",
                        "severity": "routine"
                    }
                },
                timeout=10.0
            )
            
            vote_approved = vote_response.status_code == 200
        
        # Step 3: Generate response via SOV3
        async with httpx.AsyncClient() as client:
            sov3_response = await client.post(
                self.sov3_url,
                json={
                    "tool": "care_assess",
                    "params": {
                        "content": f"{awareness_context}\nUser Message: {message}",
                        "user_id": user_id
                    }
                },
                timeout=30.0
            )
            
            if sov3_response.status_code == 200:
                response_data = sov3_response.json()
                # Extract response (handle different response formats)
                if "response" in response_data:
                    ai_response = response_data["response"]
                elif "result" in response_data:
                    ai_response = response_data["result"]
                else:
                    ai_response = "I'm here to help. What would you like to discuss?"
            else:
                ai_response = "I'm processing your request. One moment please."
        
        return {
            "success": True,
            "message": ai_response,
            "brand": self.brand["name"],
            "expert_used": expert,
            "council_approved": vote_approved,
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id or f"meok-{datetime.now().timestamp()}",
            "user_id": user_id,
            "sov3_version": self.brand["version"]
        }
    
    async def research(self, query: str, depth: int = 3) -> Dict[str, Any]:
        """Research endpoint using Search Agent"""
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:3108/mcp",
                json={
                    "tool": "search_agent_research",
                    "params": {
                        "query": query,
                        "depth": depth
                    }
                },
                timeout=120.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"success": False, "error": "Research failed"}
    
    async def get_status(self) -> Dict[str, Any]:
        """Get SOV3 system status"""
        
        # Check all services
        services = {
            "sov3_core": self.sov3_url,
            "councilof": self.councilof_url,
            "moe": self.moe_url,
            "quantum": self.quantum_url
        }
        
        healthy = 0
        for name, url in services.items():
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        url,
                        json={"tool": "health", "params": {}},
                        timeout=5.0
                    )
                    if response.status_code == 200:
                        healthy += 1
            except:
                pass
        
        return {
            "brand": self.brand,
            "status": "operational" if healthy >= 3 else "degraded",
            "services_healthy": healthy,
            "services_total": len(services),
            "timestamp": datetime.now().isoformat(),
            "message": "MEOK AI is ready to assist you."
        }
    
    async def certify_ai(self, ai_name: str, ai_endpoint: str, contact_email: str) -> Dict[str, Any]:
        """Request AI certification"""
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.certification_url}/certify",
                json={
                    "ai_name": ai_name,
                    "ai_endpoint": ai_endpoint,
                    "ai_type": "chat",
                    "contact_email": contact_email,
                    "tier": "professional"
                },
                timeout=10.0
            )
            
            return response.json()


# Initialize bridge
bridge = MeokBridge()

class MeokHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        import asyncio
        
        if self.path == '/':
            # Root endpoint — status
            result = asyncio.run(bridge.get_status())
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result, default=str).encode())
        
        elif self.path == '/brand':
            # Brand info
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(bridge.brand).encode())
        
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        """Handle POST requests"""
        import asyncio
        
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            request = json.loads(post_data)
            path = self.path
            
            if path == '/api/chat':
                result = asyncio.run(bridge.chat(
                    message=request.get('message', ''),
                    user_id=request.get('user_id', 'anonymous'),
                    session_id=request.get('session_id')
                ))
            
            elif path == '/api/research':
                result = asyncio.run(bridge.research(
                    query=request.get('query', ''),
                    depth=request.get('depth', 3)
                ))
            
            elif path == '/api/certify':
                result = asyncio.run(bridge.certify_ai(
                    ai_name=request.get('ai_name', ''),
                    ai_endpoint=request.get('ai_endpoint', ''),
                    contact_email=request.get('contact_email', '')
                ))
            
            else:
                result = {"error": f"Unknown endpoint: {path}"}
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result, default=str).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def log_message(self, format, *args):
        pass

def run_server():
    server = HTTPServer(('localhost', 3112), MeokHandler)
    print("🌐 MEOK.AI Bridge running on port 3112")
    print("   Connecting meok.ai frontend to SOV3 backend")
    print("")
    print("   Endpoints:")
    print("     GET  /           — System status")
    print("     GET  /brand      — Brand info")
    print("     POST /api/chat   — Chat with SOV3")
    print("     POST /api/research — Research query")
    print("     POST /api/certify — Request certification")
    print("")
    print("   Brand: MEOK AI — Sovereign Intelligence, Personal Care")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
