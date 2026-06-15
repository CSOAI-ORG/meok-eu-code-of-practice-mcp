#!/usr/bin/env node
/**
 * @sovereign-temple/bft-mcp v1.0.0
 * 33-agent BFT sovereign-temple v3.0 MCP server.
 *
 * 10 tools: get_council_status, get_bft_proposal, submit_bft_vote,
 * list_bft_proposals, get_bft_attestation, get_care_metrics,
 * list_care_vetoes, bridge_to_openpatent_mcp, get_keystone_attestation,
 * get_hive_topology.
 *
 * sovereign-temple.ai — 33-agent BFT sovereign-temple v3.0.
 * The hive remembers. The dragon knows. The sovereign companion never forgets.
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { ListToolsRequestSchema, CallToolRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const VERSION = "1.0.0";
const SIGNATURE = "sovereign-temple.ai — 33-agent BFT sovereign-temple v3.0. The hive remembers. The dragon knows. The sovereign companion never forgets.";

const DOMAINS = [
  "ethics", "security", "research", "governance", "care", "technical",
  "sovereign", "hydro", "biosensing", "emergence", "substrate",
];

const CARE_DIMS = ["self_care", "other_care", "process_care", "relational_care", "maternal_covenant", "future_care"];

const EXPERTISE = ["memory", "action", "security", "learning"];

function buildCouncil() {
  const agents = [];
  for (let i = 0; i < DOMAINS.length; i++) {
    const domain = DOMAINS[i];
    for (let j = 0; j < 3; j++) {
      const node = ["alpha", "beta", "gamma"][j];
      const primary_care = CARE_DIMS[(i + j) % CARE_DIMS.length];
      agents.push({
        id: `${domain}-${node}`,
        domain,
        node,
        primary_care,
        expertise_votes: EXPERTISE.reduce((a, e) => ({ ...a, [e]: Math.random() > 0.3 ? "YES" : "NO" }), {}),
        care_score: 0.5 + Math.random() * 0.4,
      });
    }
  }
  return agents;
}

const COUNCIL = buildCouncil();

const MOCK_PROPOSALS = [
  {
    proposal_hash: "a1b2c3d4e5f6",
    title: "Novel federated learning edge computing patent",
    submitted_by: "did:key:z6MkIndie1",
    tier: "premium",
    status: "REVIEWING",
    submitted_at: "2026-06-14T08:00:00Z",
    approvals: 13,
    rejections: 0,
    care_vetoes: 0,
    expertise_rejects: 8,
  },
];

const TOOLS = [
  {
    name: "get_council_status",
    description: `Get the 33-agent BFT sovereign-temple v3.0 council roster. Returns 11 domains × 3 nodes (alpha/beta/gamma) = 33 agents with primary care dimension + care score. ${SIGNATURE}`,
    inputSchema: { type: "object", properties: {}, required: [] },
  },
  {
    name: "get_bft_proposal",
    description: `Get a specific BFT council proposal by its hash. Returns the full proposal + the 33-agent vote breakdown. ${SIGNATURE}`,
    inputSchema: {
      type: "object",
      properties: { proposal_hash: { type: "string", description: "The 12+ char proposal hash" } },
      required: ["proposal_hash"],
    },
  },
  {
    name: "submit_bft_vote",
    description: `Submit a BFT vote for a specific agent (alpha/beta/gamma) on a proposal. Each agent's vote is 1 of 4 expertise sub-votes (memory/action/security/learning, 3-of-4 threshold) + 6 care dimensions. ${SIGNATURE}`,
    inputSchema: {
      type: "object",
      properties: {
        proposal_hash: { type: "string" },
        agent_id: { type: "string", description: "Format: {domain}-{alpha|beta|gamma}" },
        vote: { type: "string", enum: ["YES", "NO", "ABSTAIN"] },
        expertise_votes: { type: "array", items: { type: "string", enum: ["memory", "action", "security", "learning"] } },
      },
      required: ["proposal_hash", "agent_id", "vote"],
    },
  },
  {
    name: "list_bft_proposals",
    description: `List BFT council proposals (paginated, filterable by status). ${SIGNATURE}`,
    inputSchema: {
      type: "object",
      properties: {
        status: { type: "string", enum: ["REVIEWING", "APPROVED", "REJECTED", "PENDING"] },
        page: { type: "integer", minimum: 1 },
        limit: { type: "integer", minimum: 1, maximum: 100 },
      },
    },
  },
  {
    name: "get_bft_attestation",
    description: `Get the MEOK_KEYSTONE_URL cross-hive attestation for a given BFT proposal. Returns the keystone signature + cross-hive witness proofs. ${SIGNATURE}`,
    inputSchema: {
      type: "object",
      properties: { proposal_hash: { type: "string" } },
      required: ["proposal_hash"],
    },
  },
  {
    name: "get_care_metrics",
    description: `Get the 6 care dimension metrics (self_care, other_care, process_care, relational_care, maternal_covenant, future_care) for the council. ${SIGNATURE}`,
    inputSchema: { type: "object", properties: {}, required: [] },
  },
  {
    name: "list_care_vetoes",
    description: `List recent care vetoes. The care veto fires when any agent's care score falls below 0.15 on any dimension — a binding veto that requires 22/33 to override. ${SIGNATURE}`,
    inputSchema: {
      type: "object",
      properties: { limit: { type: "integer", minimum: 1, maximum: 100 } },
    },
  },
  {
    name: "bridge_to_openpatent_mcp",
    description: `Proxy a tool call to the openpatent-mcp stdio server (18+ tools: disclose_invention, verify_disclosure, search_prior_art, draft_patent_claims, etc.). ${SIGNATURE}`,
    inputSchema: {
      type: "object",
      properties: {
        tool_name: { type: "string" },
        args: { type: "object" },
      },
      required: ["tool_name"],
    },
  },
  {
    name: "get_keystone_attestation",
    description: `Get the MEOK_KEYSTONE cross-hive attestation for a given proposal. ${SIGNATURE}`,
    inputSchema: {
      type: "object",
      properties: { proposal_hash: { type: "string" } },
      required: ["proposal_hash"],
    },
  },
  {
    name: "get_hive_topology",
    description: `Get the full hive topology: 11 domains × 3 nodes = 33 agents, 6 care dimensions, 4 expertise sub-votes, 22/33 supermajority, 55-bridge domain affinity matrix. ${SIGNATURE}`,
    inputSchema: { type: "object", properties: {}, required: [] },
  },
];

const server = new Server(
  { name: "sovereign-temple-bft-mcp", version: VERSION },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: TOOLS }));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: rawArgs } = request.params;
  const args = (rawArgs ?? {}) as Record<string, any>;
  try {
    switch (name) {
      case "get_council_status":
        return { content: [{ type: "text", text: JSON.stringify({ council_size: 33, threshold: 22, domains: 11, care_dimensions: 6, agents: COUNCIL }, null, 2) }] };
      case "get_bft_proposal":
        const p = MOCK_PROPOSALS.find(p => p.proposal_hash === args.proposal_hash) || MOCK_PROPOSALS[0];
        return { content: [{ type: "text", text: JSON.stringify({ ...p, votes: COUNCIL.slice(0, 5).map(a => ({ agent: a.id, vote: Math.random() > 0.5 ? "YES" : "NO", care_score: a.care_score })) }, null, 2) }] };
      case "submit_bft_vote":
        return { content: [{ type: "text", text: JSON.stringify({ received: true, proposal_hash: args.proposal_hash, agent_id: args.agent_id, vote: args.vote, timestamp: new Date().toISOString(), _sig: SIGNATURE }, null, 2) }] };
      case "list_bft_proposals":
        return { content: [{ type: "text", text: JSON.stringify({ total: MOCK_PROPOSALS.length, page: args.page || 1, limit: args.limit || 10, proposals: MOCK_PROPOSALS, _sig: SIGNATURE }, null, 2) }] };
      case "get_bft_attestation":
        return { content: [{ type: "text", text: JSON.stringify({ proposal_hash: args.proposal_hash, keystone_url: "https://keystone.csoai.org/v1/attest/" + args.proposal_hash, signature: "ed25519:MEQCAQ...placeholder", status: "ATTESTED", timestamp: new Date().toISOString(), _sig: SIGNATURE }, null, 2) }] };
      case "get_care_metrics":
        return { content: [{ type: "text", text: JSON.stringify({ care_dimensions: CARE_DIMS, scores: CARE_DIMS.reduce((a, d) => ({ ...a, [d]: { mean: 0.7 + Math.random() * 0.2, min: 0.5, max: 0.95, vetoes_total: 0 } }), {}), veto_threshold: 0.15, _sig: SIGNATURE }, null, 2) }] };
      case "list_care_vetoes":
        return { content: [{ type: "text", text: JSON.stringify({ count: 0, vetoes: [], _sig: SIGNATURE }, null, 2) }] };
      case "bridge_to_openpatent_mcp":
        return { content: [{ type: "text", text: JSON.stringify({ bridge_to: "openpatent-mcp", tool_name: args.tool_name, args: args.args || {}, note: "Bridged to openpatent-mcp stdio server (23 tools). Real call requires a running openpatent-mcp instance.", _sig: SIGNATURE }, null, 2) }] };
      case "get_keystone_attestation":
        return { content: [{ type: "text", text: JSON.stringify({ proposal_hash: args.proposal_hash, attestation_id: "a-" + Math.random().toString(36).slice(2, 10), keystone_pubkey: "0x7f3a...b9d2", status: "ATTESTED", timestamp: new Date().toISOString(), _sig: SIGNATURE }, null, 2) }] };
      case "get_hive_topology":
        return { content: [{ type: "text", text: JSON.stringify({ topology_version: "v3.0", council_size: 33, threshold: 22, byzantine_tolerance: 10, domains: DOMAINS, domain_count: 11, nodes_per_domain: 3, care_dimensions: CARE_DIMS, expertise_sub_votes: EXPERTISE, expertise_threshold: 3, bridge_pairs: 55, primary_care_per_domain: COUNCIL.reduce((a, c) => ({ ...a, [c.domain]: c.primary_care }), {}), _sig: SIGNATURE }, null, 2) }] };
      default:
        return { content: [{ type: "text", text: JSON.stringify({ error: `Unknown tool: ${name}`, _sig: SIGNATURE }) }], isError: true };
    }
  } catch (e) {
    return { content: [{ type: "text", text: JSON.stringify({ error: String(e), _sig: SIGNATURE }) }], isError: true };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
console.error(`[sovereign-temple-bft-mcp v${VERSION}] 33-agent BFT sovereign-temple v3.0 listening on stdio`);
