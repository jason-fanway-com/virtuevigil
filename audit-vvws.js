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

let issues = [];
let mismatches = [];
let reviewed = 0;

reviews.forEach((r, idx) => {
  if ((r.wokeScore === undefined || r.wokeScore === null) && r.type === 'film') {
    issues.push(`${r.slug}: missing wokeScore`);
    return;
  }
  if ((r.tradScore === undefined || r.tradScore === null) && r.type === 'film') {
    issues.push(`${r.slug}: missing tradScore`);
    return;
  }

  // Skip articles
  if (r.type !== 'film') return;

  reviewed++;
  const calculatedMargin = Math.round(r.tradScore - r.wokeScore);
  const expectedLabel = getMarginLabel(calculatedMargin);
  const expectedVerdict = getVerdictForMargin(calculatedMargin);

  // Parse current scoreMargin to extract the number
  let currentMargin = null;
  if (r.scoreMargin) {
    const match = r.scoreMargin.match(/([+-]?\d+)/);
    currentMargin = match ? parseInt(match[1]) : null;
  }

  // Check margin mismatch
  if (currentMargin !== calculatedMargin) {
    mismatches.push({
      slug: r.slug,
      type: 'scoreMargin',
      current: r.scoreMargin,
      expected: expectedLabel,
      trad: r.tradScore,
      woke: r.wokeScore,
      margin: calculatedMargin
    });
  }

  // Check verdict mismatch
  if (r.verdict !== expectedVerdict) {
    mismatches.push({
      slug: r.slug,
      type: 'verdict',
      current: r.verdict,
      expected: expectedVerdict,
      margin: calculatedMargin
    });
  }

  // Check woke trap logic
  if (r.wokeTrap && calculatedMargin >= 0) {
    mismatches.push({
      slug: r.slug,
      type: 'woke_trap_false_positive',
      current: true,
      expected: false,
      margin: calculatedMargin,
      note: 'woke_trap should be false (margin is non-negative)'
    });
  }
});

console.log(`\n=== VVWS SCORING AUDIT REPORT ===\n`);
console.log(`Total film reviews audited: ${reviewed}`);
console.log(`Scoring mismatches found: ${mismatches.length}`);

if (mismatches.length > 0) {
  console.log(`\nMISMATCHES (first 30):`);
  mismatches.slice(0, 30).forEach(m => {
    if (m.type === 'scoreMargin') {
      console.log(`  ${m.slug}: scoreMargin "${m.current}" → "${m.expected}"`);
    } else if (m.type === 'verdict') {
      console.log(`  ${m.slug}: verdict "${m.current}" → "${m.expected}" (margin=${m.margin})`);
    } else if (m.type === 'woke_trap_false_positive') {
      console.log(`  ${m.slug}: woke_trap=true but margin=${m.margin} (should be false)`);
    }
  });
  if (mismatches.length > 30) {
    console.log(`  ... (${mismatches.length - 30} more)\n`);
  }
}

if (issues.length > 0) {
  console.log(`\nDATA ISSUES:`);
  issues.forEach(i => console.log(`  - ${i}`));
}

console.log(`\n=== FIX SUMMARY ===`);
console.log(`Margin mismatches: ${mismatches.filter(m => m.type === 'scoreMargin').length}`);
console.log(`Verdict mismatches: ${mismatches.filter(m => m.type === 'verdict').length}`);
console.log(`Woke trap issues: ${mismatches.filter(m => m.type === 'woke_trap_false_positive').length}`);

// Write mismatches to file for processing
fs.writeFileSync('./AUDIT-MISMATCHES.json', JSON.stringify(mismatches, null, 2));
console.log(`\n✓ Detailed mismatches written to AUDIT-MISMATCHES.json`);
