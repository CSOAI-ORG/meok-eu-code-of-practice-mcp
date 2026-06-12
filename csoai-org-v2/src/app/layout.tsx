import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import CouncilNav from "@/components/CouncilNav";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "CSOAI — The Council for the Safety of AI",
  description:
    "The independent authority that certifies AI is safe — and lets anyone verify it. Watchdog Certification, MCP governance fabric, and the CSOAI Council substrate.",
  keywords: [
    "CSOAI",
    "AI safety",
    "AI governance",
    "EU AI Act",
    "Watchdog Certification",
    "MCP",
    "BFT Council",
    "A2A",
    "x402",
  ],
  openGraph: {
    title: "CSOAI — The Council for the Safety of AI",
    description:
      "Watchdog Certification, MCP governance fabric, and the CSOAI Council substrate.",
    url: "https://csoai.org",
    siteName: "CSOAI",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "CSOAI — The Council for the Safety of AI",
    description: "Watchdog Certification + MCP governance fabric.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased bg-slate-950 text-white`}>
        <CouncilNav />
        {children}
      </body>
    </html>
  );
}
