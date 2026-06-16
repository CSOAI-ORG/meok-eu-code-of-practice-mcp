import type { Metadata } from "next";

interface CoPReadyBadgeProps {
  size?: "sm" | "md" | "lg";
  showText?: boolean;
}

export function CoPReadyBadge({ size = "md", showText = true }: CoPReadyBadgeProps) {
  const sizes = { sm: 24, md: 36, lg: 48 };
  const px = sizes[size];
  return (
    <div style={{ display: "inline-flex", alignItems: "center", gap: "0.5rem" }}>
      <svg width={px} height={px} viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="24" cy="24" r="22" fill="#1a1a2e" stroke="#c9a84c" strokeWidth="2" />
        <path d="M16 24l6 6 10-12" stroke="#c9a84c" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
        <text x="24" y="38" textAnchor="middle" fill="#c9a84c" fontSize="6" fontFamily="monospace">CoP</text>
      </svg>
      {showText && (
        <span style={{ fontSize: size === "sm" ? "0.75rem" : size === "md" ? "0.875rem" : "1rem", color: "#c9a84c", fontWeight: 600 }}>
          EU Code of Practice Ready
        </span>
      )}
    </div>
  );
}
