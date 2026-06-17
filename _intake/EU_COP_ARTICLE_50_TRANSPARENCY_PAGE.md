# 🐉 meok.ai/eu-code-of-practice — Article 50 Transparency sub-page
**Status:** Scaffolded (iCloud-staged, awaiting Vercel WAF cooldown)
**Strategy:** EU Code of Practice first-mover. The 2 Aug 2026 transparency cliff is 48 days from today.
**Keystone certs as inline content:** 10 framework certs ready as live verify links.

---

## The page structure (Next.js + NAVY + GOLD + BG, follows article-50-kit pattern)

```tsx
// meok-ai/ui/src/app/eu-code-of-practice/article-50-transparency/page.tsx
import type { Metadata } from "next";
import Link from "next/link";
import { Article50Countdown } from "@/components/Article50Countdown";

export const metadata: Metadata = {
  title: "EU AI Act Article 50 Transparency — 2 Aug 2026 Cliff · MEOK AI Labs",
  description:
    "The EU AI Act Article 50 transparency obligations apply from 2 August 2026. " +
    "MEOK provides the signed, verifiable stack: 10 keystone certs (EU AI Act, DORA, " +
    "NIS2, CRA, GDPR, ISO 42001, ISO 27001, SOC 2, PCI DSS, NIST AI RMF) all " +
    "Ed25519-signed and offline-verifiable. 48 days to compliance.",
  alternates: { canonical: "https://meok.ai/eu-code-of-practice/article-50-transparency" },
  // OpenGraph + keywords + JSON-LD similar to /article-50-kit
};

const NAVY = "#1a1a2e";
const GOLD = "#c9a84c";
const BG = "#f5f0e8";

const FRAMEWORK_CERTS = [
  { name: "EU AI Act",     cert: "MEOK-MEOKEU-E0968630D9B0", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKEU-E0968630D9B0" },
  { name: "DORA",         cert: "MEOK-MEOKDO-65460BD7AC31", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKDO-65460BD7AC31" },
  { name: "NIS2",         cert: "MEOK-MEOKNI-106F56B7DB17", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKNI-106F56B7DB17" },
  { name: "CRA",          cert: "MEOK-MEOKCR-C969CE1F3265", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKCR-C969CE1F3265" },
  { name: "GDPR",         cert: "MEOK-MEOKGD-9662BABD9BAD", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKGD-9662BABD9BAD" },
  { name: "ISO 42001",    cert: "MEOK-MEOKIS-FDBE80D6A920", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKIS-FDBE80D6A920" },
  { name: "ISO 27001",    cert: "MEOK-MEOKIS-388663741EEB", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKIS-388663741EEB" },
  { name: "SOC 2",        cert: "MEOK-MEOKSO-90A6C4571CA8", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKSO-90A6C4571CA8" },
  { name: "PCI DSS",      cert: "MEOK-MEOKPC-FFE975D640AD", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKPC-FFE975D640AD" },
  { name: "NIST AI RMF",  cert: "MEOK-MEOKNI-9BA49CA344FD", url: "https://meok-attestation-api.vercel.app/verify/MEOK-MEOKNI-9BA49CA344FD" },
];

const STRIPE_LINK = "https://buy.stripe.com/4gM3cx0xScMOdMFfL28k91u"; // £999 Article 50 Kit
const KEYSTONE_SIGNUP = "https://meok-attestation-api.vercel.app/signup";

export default function Article50TransparencyPage() {
  return (
    <main style={{ background: BG, color: NAVY, fontFamily: "ui-sans-serif, system-ui, sans-serif", padding: "2rem 1rem" }}>
      <section style={{ maxWidth: 880, margin: "0 auto" }}>
        <h1 style={{ fontSize: "2.5rem", color: NAVY, lineHeight: 1.2 }}>
          EU AI Act Article 50 — Transparency Cliff in 48 Days
        </h1>
        <p style={{ fontSize: "1.125rem", color: NAVY, margin: "1rem 0 2rem" }}>
          The transparency obligations of <strong>Article 50</strong> apply from{" "}
          <strong>2 August 2026</strong>. The Digital Omnibus did NOT defer Article 50
          for new generative systems. Providers of generative AI must mark outputs
          as machine-readable; deployers must disclose AI generation to people
          exposed to it. The June 2026 EU Code of Practice on AI content marking
          finalises this month and mandates a two-layer approach (C2PA + invisible
          watermark + optional fingerprinting + logging).
        </p>

        <div style={{ margin: "2rem 0" }}>
          <Article50Countdown targetDate="2026-08-02T00:00:00Z" />
        </div>

        <h2 style={{ color: GOLD, marginTop: "3rem" }}>The 10 keystone certs (live now)</h2>
        <p>
          Each of the 10 frameworks below has a real keystone cert issued by{" "}
          <code>meok-attestation-api.vercel.app</code> (Ed25519-signed, public verify
          URL, offline-verifiable). Click any cert to see the live attestation.
        </p>
        <ul style={{ listStyle: "none", padding: 0 }}>
          {FRAMEWORK_CERTS.map((f) => (
            <li key={f.cert} style={{ margin: "0.5rem 0", padding: "0.75rem", background: "white", borderRadius: 8, border: "1px solid #e5e0d8" }}>
              <strong>{f.name}</strong>{" "}
              <code style={{ background: "#f0f0f0", padding: "0.1rem 0.3rem", borderRadius: 3, fontSize: "0.85rem" }}>{f.cert}</code>
              {" — "}
              <a href={f.url} style={{ color: GOLD }} target="_blank" rel="noreferrer">
                verify offline
              </a>
            </li>
          ))}
        </ul>

        <h2 style={{ color: GOLD, marginTop: "3rem" }}>The Article 50 Kit (£999, ships in 7 days)</h2>
        <p>
          C2PA + invisible watermark + fingerprinting + signed Article 50 conformity
          attestation. Ships in 7 days. The 2-layer minimum the Code of Practice
          mandates.
        </p>
        <a href={STRIPE_LINK} style={{ display: "inline-block", padding: "1rem 2rem", background: GOLD, color: NAVY, borderRadius: 8, fontWeight: 600, textDecoration: "none" }}>
          Get the Article 50 Kit — £999 one-time
        </a>

        <h2 style={{ color: GOLD, marginTop: "3rem" }}>Or get a free keystone cert (3/day, no login)</h2>
        <p>
          The first 3 keystone certs per email are free. The auditor can verify
          the cert offline via the Ed25519 signature — no contacting MEOK, no
          trusting the platform.
        </p>
        <a href={KEYSTONE_SIGNUP} style={{ display: "inline-block", padding: "0.75rem 1.5rem", background: "white", color: NAVY, borderRadius: 8, fontWeight: 600, textDecoration: "none", border: `2px solid ${GOLD}` }}>
          Get your free keystone cert →
        </a>

        <h2 style={{ color: GOLD, marginTop: "3rem" }}>FAQ</h2>
        <details style={{ margin: "1rem 0" }}>
          <summary><strong>When does EU AI Act Article 50 apply?</strong></summary>
          <p>
            Article 50 transparency obligations apply from <strong>2 August 2026</strong>.
            Providers of generative AI systems must mark AI-generated outputs as
            machine-readable; deployers must disclose AI generation to people
            exposed to it.
          </p>
        </details>
        <details style={{ margin: "1rem 0" }}>
          <summary><strong>What is the EU Code of Practice on AI?</strong></summary>
          <p>
            The Code of Practice is a voluntary but practically-mandatory standard
            that the Commission will finalise in autumn 2026. The June 2026
            second draft mandates a two-layer marking approach: C2PA + invisible
            watermarking (with optional fingerprinting + logging).
          </p>
        </details>
        <details style={{ margin: "1rem 0" }}>
          <summary><strong>What is a keystone cert?</strong></summary>
          <p>
            A keystone cert is an Ed25519-signed attestation issued by the MEOK
            keystone. The signature is verifiable offline by anyone with the
            keystone's public key — no contacting MEOK, no trusting the platform.
            Every cert has a public verify URL like{" "}
            <code>https://meok-attestation-api.vercel.app/verify/&lt;cert_id&gt;</code>.
          </p>
        </details>

        <p style={{ marginTop: "3rem", color: "#666" }}>
          <Link href="/article-50-kit" style={{ color: GOLD }}>← back to the full Article 50 kit</Link>
        </p>
      </section>
    </main>
  );
}
```

---

## The 5 deploy steps (when Vercel WAF clears)

1. **cp** the file from iCloud staging to `meok-ai/ui/src/app/eu-code-of-practice/article-50-transparency/page.tsx`
2. **Add** to `meok-ai/ui/src/app/eu-code-of-practice/page.tsx` a 1-line cross-link to the new sub-page
3. **Add** to `meok-ai/ui/src/app/article-50-kit/page.tsx` a 1-line cross-link
4. **Test** locally: `cd meok-ai/ui && npx next dev -p 3456 && curl -sI http://localhost:3456/eu-code-of-practice/article-50-transparency`
5. **Deploy** via Vercel (once WAF cooldown clears) + run pre-re-alias check

---

## The 5-question pre-flight (before deploy)

1. Does the page render at 200?
2. Do all 10 keystone cert links return 200?
3. Does the Article50Countdown component show 48 days remaining?
4. Is the canonical URL set in the metadata?
5. Is the Stripe link live and pointing to the right product?

---

JEEVES, signing off. 🫡
