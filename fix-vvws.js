const fs = require('fs');
const reviews = require('./src/data/reviews.json');

function getVerdictForMargin(margin) {
  if (margin >= 20) return 'STRONGLY TRADITIONAL';
  if (margin >= 10) return 'TRADITIONAL';
  if (margin >= 3) return 'TRADITIONAL LEAN';
  if (margin >= -2 && margin <= 2) return 'MIXED';
  if (margin >= -9) return 'WOKE LEAN';
  if (margin >= -19) return 'WOKE';
  return 'STRONGLY WOKE';
}

function getMarginLabel(margin) {
  if (margin > 0) return `+${margin} TRAD`;
  if (margin < 0) return `${margin} WOKE`;
  return '0 NEUTRAL';
}

let fixes = [];

reviews.forEach((r, idx) => {
  if (r.type !== 'film') return;
  if (r.wokeScore === undefined || r.tradScore === undefined) return;

  const calculatedMargin = Math.round(r.tradScore - r.wokeScore);
  const expectedLabel = getMarginLabel(calculatedMargin);
  const expectedVerdict = getVerdictForMargin(calculatedMargin);

  // Parse current scoreMargin to extract the number
  let currentMargin = null;
  if (r.scoreMargin) {
    const match = r.scoreMargin.match(/([+-]?\d+)/);
    currentMargin = match ? parseInt(match[1]) : null;
  }

  let fixed = false;

  // Fix scoreMargin
  if (currentMargin !== calculatedMargin) {
    r.scoreMargin = expectedLabel;
    fixes.push(`${r.slug}: scoreMargin → ${expectedLabel}`);
    fixed = true;
  }

  // Fix verdict
  if (r.verdict !== expectedVerdict) {
    r.verdict = expectedVerdict;
    fixes.push(`${r.slug}: verdict → ${expectedVerdict}`);
    fixed = true;
  }

  // Fix woke trap (false positives only)
  if (r.wokeTrap && calculatedMargin >= 0) {
    r.wokeTrap = false;
    fixes.push(`${r.slug}: woke_trap → false (margin=${calculatedMargin})`);
    fixed = true;
  }
});

// Write fixed reviews back
fs.writeFileSync('./src/data/reviews.json', JSON.stringify(reviews, null, 2));

console.log(`\n=== VVWS FIXES APPLIED ===\n`);
console.log(`Total fixes: ${fixes.length}\n`);
fixes.slice(0, 20).forEach(f => console.log(`✓ ${f}`));
if (fixes.length > 20) {
  console.log(`... and ${fixes.length - 20} more`);
}

console.log(`\n✓ reviews.json updated with ${fixes.length} fixes`);
