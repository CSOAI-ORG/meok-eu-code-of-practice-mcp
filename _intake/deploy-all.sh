#!/usr/bin/env bash
# Deploy script — generated 2026-06-16T17:06:37.618395
# Run this after Vercel WAF cooldown clears (expected ~48h from 13 Jun 14:00 BST)
# Usage: bash deploy-all.sh

DEST_BASE="/Users/nicholas/clawd/meok-ai/ui/src/app"
ICLOUD_BASE="/Users/nicholas/Library/Mobile Documents/com~apple~CloudDocs/clawdbot-shared/mcp-staging"

echo '=== DEPLOYING 29+ PAGES ==='
total=0
mkdir -p $DEST_BASE/eu-code-of-practice
cp $ICLOUD_BASE/eu-code-of-practice/page.tsx $DEST_BASE/eu-code-of-practice/page.tsx
echo '  ✓ eu-code-of-practice/page.tsx → eu-code-of-practice/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/eu-code-of-practice/article-50-marking
cp $ICLOUD_BASE/eu-code-of-practice-subpages/article-50-marking/page.tsx $DEST_BASE/eu-code-of-practice/article-50-marking/page.tsx
echo '  ✓ eu-code-of-practice-subpages/article-50-marking/page.tsx → eu-code-of-practice/article-50-marking/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/eu-code-of-practice/code-of-practice-2nd-draft
cp $ICLOUD_BASE/eu-code-of-practice-subpages/code-of-practice-2nd-draft/page.tsx $DEST_BASE/eu-code-of-practice/code-of-practice-2nd-draft/page.tsx
echo '  ✓ eu-code-of-practice-subpages/code-of-practice-2nd-draft/page.tsx → eu-code-of-practice/code-of-practice-2nd-draft/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/eu-code-of-practice/article-50-deepfake
cp $ICLOUD_BASE/eu-code-of-practice-subpages/article-50-deepfake/page.tsx $DEST_BASE/eu-code-of-practice/article-50-deepfake/page.tsx
echo '  ✓ eu-code-of-practice-subpages/article-50-deepfake/page.tsx → eu-code-of-practice/article-50-deepfake/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for-fintech
cp $ICLOUD_BASE/verticals-and-comparisons/vertical-fintech/page.tsx $DEST_BASE/for-fintech/page.tsx
echo '  ✓ verticals-and-comparisons/vertical-fintech/page.tsx → for-fintech/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for-care-homes
cp $ICLOUD_BASE/verticals-and-comparisons/vertical-care-homes/page.tsx $DEST_BASE/for-care-homes/page.tsx
echo '  ✓ verticals-and-comparisons/vertical-care-homes/page.tsx → for-care-homes/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for-edtech
cp $ICLOUD_BASE/verticals-and-comparisons/vertical-edtech/page.tsx $DEST_BASE/for-edtech/page.tsx
echo '  ✓ verticals-and-comparisons/vertical-edtech/page.tsx → for-edtech/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for-saas
cp $ICLOUD_BASE/verticals-and-comparisons/vertical-saas/page.tsx $DEST_BASE/for-saas/page.tsx
echo '  ✓ verticals-and-comparisons/vertical-saas/page.tsx → for-saas/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for-healthcare
cp $ICLOUD_BASE/verticals-and-comparisons/vertical-healthcare/page.tsx $DEST_BASE/for-healthcare/page.tsx
echo '  ✓ verticals-and-comparisons/vertical-healthcare/page.tsx → for-healthcare/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/vs/vanta
cp $ICLOUD_BASE/comparisons/vs-vanta/page.tsx $DEST_BASE/vs/vanta/page.tsx
echo '  ✓ comparisons/vs-vanta/page.tsx → vs/vanta/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/vs/drata
cp $ICLOUD_BASE/comparisons/vs-drata/page.tsx $DEST_BASE/vs/drata/page.tsx
echo '  ✓ comparisons/vs-drata/page.tsx → vs/drata/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/vs/arthur-ai
cp $ICLOUD_BASE/comparisons/vs-arthur-ai/page.tsx $DEST_BASE/vs/arthur-ai/page.tsx
echo '  ✓ comparisons/vs-arthur-ai/page.tsx → vs/arthur-ai/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/vs/credo-ai
cp $ICLOUD_BASE/comparisons/vs-credo-ai/page.tsx $DEST_BASE/vs/credo-ai/page.tsx
echo '  ✓ comparisons/vs-credo-ai/page.tsx → vs/credo-ai/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/vs/holistic-ai
cp $ICLOUD_BASE/comparisons/vs-holistic-ai/page.tsx $DEST_BASE/vs/holistic-ai/page.tsx
echo '  ✓ comparisons/vs-holistic-ai/page.tsx → vs/holistic-ai/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/vs/nevermined
cp $ICLOUD_BASE/comparisons/vs-nevermined/page.tsx $DEST_BASE/vs/nevermined/page.tsx
echo '  ✓ comparisons/vs-nevermined/page.tsx → vs/nevermined/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/vs/regen-network
cp $ICLOUD_BASE/comparisons/vs-regen-network/page.tsx $DEST_BASE/vs/regen-network/page.tsx
echo '  ✓ comparisons/vs-regen-network/page.tsx → vs/regen-network/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/empire
cp $ICLOUD_BASE/4-surface-empire/empire/page.tsx $DEST_BASE/empire/page.tsx
echo '  ✓ 4-surface-empire/empire/page.tsx → empire/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/csoai-org
cp $ICLOUD_BASE/4-surface-empire/csoai-org/page.tsx $DEST_BASE/csoai-org/page.tsx
echo '  ✓ 4-surface-empire/csoai-org/page.tsx → csoai-org/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/openmoe-ai
cp $ICLOUD_BASE/4-surface-empire/openmoe-ai/page.tsx $DEST_BASE/openmoe-ai/page.tsx
echo '  ✓ 4-surface-empire/openmoe-ai/page.tsx → openmoe-ai/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/openpatent-ai
cp $ICLOUD_BASE/4-surface-empire/openpatent-ai/page.tsx $DEST_BASE/openpatent-ai/page.tsx
echo '  ✓ 4-surface-empire/openpatent-ai/page.tsx → openpatent-ai/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/by-numbers
cp $ICLOUD_BASE/4-surface-empire/by-numbers/page.tsx $DEST_BASE/by-numbers/page.tsx
echo '  ✓ 4-surface-empire/by-numbers/page.tsx → by-numbers/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/manifesto
cp $ICLOUD_BASE/4-surface-empire/manifesto/page.tsx $DEST_BASE/manifesto/page.tsx
echo '  ✓ 4-surface-empire/manifesto/page.tsx → manifesto/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/nav
cp $ICLOUD_BASE/4-surface-empire/nav/page.tsx $DEST_BASE/nav/page.tsx
echo '  ✓ 4-surface-empire/nav/page.tsx → nav/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/press
cp $ICLOUD_BASE/4-surface-empire/press/page.tsx $DEST_BASE/press/page.tsx
echo '  ✓ 4-surface-empire/press/page.tsx → press/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for/monzo
cp $ICLOUD_BASE/lead-magnets/for-monzo/page.tsx $DEST_BASE/for/monzo/page.tsx
echo '  ✓ lead-magnets/for-monzo/page.tsx → for/monzo/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for/cera-care
cp $ICLOUD_BASE/lead-magnets/for-cera-care/page.tsx $DEST_BASE/for/cera-care/page.tsx
echo '  ✓ lead-magnets/for-cera-care/page.tsx → for/cera-care/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for/stitch
cp $ICLOUD_BASE/lead-magnets/for-stitch/page.tsx $DEST_BASE/for/stitch/page.tsx
echo '  ✓ lead-magnets/for-stitch/page.tsx → for/stitch/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for/verisure
cp $ICLOUD_BASE/lead-magnets/for-verisure/page.tsx $DEST_BASE/for/verisure/page.tsx
echo '  ✓ lead-magnets/for-verisure/page.tsx → for/verisure/page.tsx'
total=$((total + 1))
mkdir -p $DEST_BASE/for/parsa
cp $ICLOUD_BASE/lead-magnets/for-parsa/page.tsx $DEST_BASE/for/parsa/page.tsx
echo '  ✓ lead-magnets/for-parsa/page.tsx → for/parsa/page.tsx'
total=$((total + 1))

echo '=== ALL DONE ==='
echo 'Deployed $total pages'