#!/usr/bin/env node
/**
 * canonicalize-margins.js
 * Converts all raw-number and non-canonical-string scoreMargin values
 * to the canonical format: +X TRAD / -X WOKE / 0 NEUTRAL
 */

const fs = require('fs');
const path = require('path');

const reviewsPath = path.join(__dirname, '..', 'src', 'data', 'reviews.json');
const data = JSON.parse(fs.readFileSync(reviewsPath, 'utf8'));

const canonicalRe = /^[+-]?\d+ (TRAD|WOKE|NEUTRAL)$/;
let changed = 0;
const log = [];

data.forEach((review) => {
  const sm = review.scoreMargin;
  const margin = Math.round(review.tradScore - review.wokeScore);

  let needsChange = false;

  if (typeof sm === 'number') {
    needsChange = true;
  } else if (typeof sm === 'string' && !canonicalRe.test(sm)) {
    needsChange = true;
  }

  if (!needsChange) return;

  let canonical;
  if (margin > 0) {
    canonical = `+${margin} TRAD`;
  } else if (margin < 0) {
    canonical = `${margin} WOKE`;
  } else {
    canonical = '0 NEUTRAL';
  }

  log.push(`${review.slug.padEnd(50)} "${sm}" → "${canonical}"`);
  review.scoreMargin = canonical;
  changed++;
});

console.log(`Changed ${changed} reviews:\n`);
log.forEach(l => console.log('  ' + l));

fs.writeFileSync(reviewsPath, JSON.stringify(data, null, 2));
console.log(`\n✓ Written ${data.length} reviews to ${reviewsPath}`);