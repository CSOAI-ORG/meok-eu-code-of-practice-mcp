"use client";

import { useState } from "react";

export default function Article50Kit() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleCheckout = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("/api/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ product_id: "article_50_kit" }),
      });
      const data = await res.json();
      if (!res.ok) {
        if (res.status === 503) {
          setError("Payments are being set up. Email hello@meok.ai to purchase.");
        } else {
          setError(data?.message || "Checkout failed");
        }
        return;
      }
      if (data?.url) {
        window.location.href = data.url;
      }
    } catch (e: any) {
      setError(e?.message || "Network error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white selection:bg-red-500/30">
      <div className="max-w-4xl mx-auto px-4 py-20">
        <div className="border-2 border-red-500 rounded-3xl p-10 bg-red-500/5 mb-20 text-center">
          <span className="inline-block mb-4 px-3 py-1 rounded-full bg-red-500 text-white text-[10px] font-black tracking-widest uppercase">
            Emergency Response
          </span>
          <h1 className="text-5xl font-black mb-4 text-red-500 tracking-tighter">
            ARTICLE 50 KIT
          </h1>
          <p className="text-xl font-bold uppercase tracking-widest text-slate-400">
            Deadline: August 2, 2026 — 52 Days Left
          </p>
        </div>

        <section className="mb-20">
          <h2 className="text-3xl font-bold mb-6">The €35,000,000 Risk</h2>
          <p className="text-slate-400 text-lg leading-relaxed">
            Under the EU AI Act, general-purpose AI systems failing to meet Article 50
            transparency obligations face fines up to 7% of global turnover or €35M.
            Compliance is not optional—it is a production gate.
          </p>
        </section>

        <div className="grid md:grid-cols-2 gap-6 mb-20">
          {[
            { title: "Transparency Docs", desc: "Ready-to-file technical documentation for Article 50(1)." },
            { title: "Risk Classification", desc: "Automated Annex III risk assessment templates." },
            { title: "Human Oversight", desc: "Codified protocols for the 33-agent BFT Council." },
            { title: "Post-Market Plan", desc: "Monitoring system for continuous runtime compliance." },
          ].map((f) => (
            <div key={f.title} className="p-8 rounded-2xl bg-white/5 border border-white/10">
              <h3 className="text-xl font-bold mb-4 text-emerald-400">{f.title}</h3>
              <p className="text-sm text-slate-400 leading-relaxed">{f.desc}</p>
            </div>
          ))}
        </div>

        {error && (
          <div className="mb-6 p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-300 text-sm">
            {error}
          </div>
        )}

        <div className="text-center p-12 rounded-3xl bg-white/5 border border-white/10">
          <div className="text-6xl font-black mb-2">£999</div>
          <p className="text-slate-500 mb-8 font-medium">
            One-time purchase. Instant digital delivery. Guaranteed compliant.
          </p>
          <button
            onClick={handleCheckout}
            disabled={loading}
            className="px-12 py-5 rounded-2xl bg-red-600 hover:bg-red-700 disabled:opacity-50 disabled:cursor-not-allowed text-white font-black text-xl transition shadow-2xl shadow-red-600/20 uppercase tracking-widest"
          >
            {loading ? "Redirecting to Stripe…" : "Secure Compliance Now"}
          </button>
        </div>
      </div>
    </div>
  );
}
