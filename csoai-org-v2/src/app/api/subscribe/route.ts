import { NextRequest, NextResponse } from "next/server";

// Simple in-memory store for demo (resets on cold start, but captures leads)
const leads: Array<{ email: string; source: string; timestamp: string }> = [];

export async function POST(request: NextRequest) {
  try {
    const { email, source } = await request.json();
    
    if (!email || !email.includes("@")) {
      return NextResponse.json(
        { success: false, error: "Valid email required" },
        { status: 400 }
      );
    }

    const lead = { email, source: source || "website", timestamp: new Date().toISOString() };
    leads.push(lead);
    
    // Log for monitoring (visible in Vercel logs)
    console.log("[LEAD CAPTURED]", JSON.stringify(lead));
    
    // Try Postgres if DATABASE_URL is available
    if (process.env.DATABASE_URL) {
      try {
        const { Pool } = await import("pg");
        const pool = new Pool({ connectionString: process.env.DATABASE_URL });
        const client = await pool.connect();
        try {
          await client.query(
            "INSERT INTO subscribers (email, source, created_at) VALUES ($1, $2, NOW()) ON CONFLICT DO NOTHING",
            [email, source || "website"]
          );
        } finally {
          client.release();
        }
      } catch (dbErr) {
        console.error("DB write failed (non-critical):", dbErr);
        // Non-critical: lead is still in memory + logs
      }
    }

    return NextResponse.json({
      success: true,
      message: "Subscribed successfully",
      lead: { email, source: source || "website" }
    });
  } catch (error) {
    console.error("Subscribe error:", error);
    return NextResponse.json(
      { success: false, error: "Server error" },
      { status: 500 }
    );
  }
}

// GET endpoint to retrieve captured leads (protected, for admin use)
export async function GET(request: NextRequest) {
  const auth = request.headers.get("authorization");
  const adminToken = process.env.ADMIN_TOKEN;
  if (!adminToken) {
    console.error("ADMIN_TOKEN not configured");
    return NextResponse.json({ error: "Admin not configured" }, { status: 500 });
  }
  if (auth !== `Bearer ${adminToken}`) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }
  return NextResponse.json({ leads, count: leads.length });
}
