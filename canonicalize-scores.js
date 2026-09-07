// canonicalize-scores.js -- fix ALL review scoreMargin and verdict fields
// Idempotent: running twice produces no changes on second run
const fs = require('fs');
const reviews = require('./src/data/reviews.json');

// LOCKED verdict table (VVWS deterministic)
function getVerdict(margin) {
  if (margin >= 20) return 'TRADITIONAL';
  if (margin >= 15) return 'TRADITIONAL LEAN';
  if (margin >= 5) return 'BALANCED TRADITIONAL';
  if (margin >= -4) return 'BALANCED';
  if (margin >= -14) return 'BALANCED WOKE';
  if (margin >= -19) return 'WOKE LEAN';
  return 'WOKE';
}

function getMarginLabel(margin) {
  if (margin > 0) return `+${margin} TRAD`;
  if (margin < 0) return `${margin} WOKE`;
  return '0 BALANCED';
}

let changed = 0;
let fieldsFixed = 0;

reviews.forEach((r) => {
  if (r.type !== 'film') return;
  if (r.wokeScore === undefined || r.wokeScore === null) return;
  if (r.tradScore === undefined || r.tradScore === null) return;

  const margin = Math.round(r.tradScore - r.wokeScore);
  const expectedLabel = getMarginLabel(margin);
  const expectedVerdict = getVerdict(margin);

  // Fix scoreMargin
  if (r.scoreMargin !== expectedLabel) {
    r.scoreMargin = expectedLabel;
    fieldsFixed++;
  }

  // Fix verdict
  if (r.verdict !== expectedVerdict) {
    r.verdict = expectedVerdict;
    fieldsFixed++;
  }

  // Fix woke trap: if margin >= 0, wokeTrap must be false
  if (r.wokeTrap === true && margin >= 0) {
    r.wokeTrap = false;
    fieldsFixed++;
  }

  changed++;
});

console.log(`Reviews canonicalized: ${changed} of ${reviews.filter(r=>r.type==='film').length} film reviews`);
console.log(`Fields fixed: ${fieldsFixed}`);

// Write back
fs.writeFileSync('./src/data/reviews.json', JSON.stringify(reviews, null, 2));
console.log(`\n${fieldsFixed > 0 ? 'Wrote canonicalized reviews.json' : 'No changes needed (idempotent)'}`);