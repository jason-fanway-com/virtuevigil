#!/usr/bin/env node
/**
 * VVWS Scoring Fix Script — Mercedes QA Audit
 * Fixes: verdict, scoreMargin, wokeTrap boolean normalization
 * Also fixes: markdown in summary.overall fields
 * Run: node scripts/vvws-fix.js
 */

const fs = require('fs');
const path = require('path');

const reviewsPath = path.join(__dirname, '../src/data/reviews.json');
const reviews = JSON.parse(fs.readFileSync(reviewsPath, 'utf8'));

let fixCount = 0;
const log = [];

function calcVerdict(margin) {
  if (margin >= 20) return 'STRONGLY TRADITIONAL';
  if (margin >= 10) return 'TRADITIONAL';
  if (margin >= 3)  return 'TRADITIONAL LEAN';
  if (margin >= -2) return 'MIXED';
  if (margin >= -9) return 'WOKE LEAN';
  if (margin >= -19) return 'WOKE';
  return 'STRONGLY WOKE';
}

function calcMarginStr(margin) {
  const abs = Math.round(Math.abs(margin));
  if (margin > 0) return '+' + abs + ' TRAD';
  if (margin < 0) return '-' + abs + ' WOKE';
  return '0 NEUTRAL';
}

function stripMarkdown(text) {
  if (typeof text !== 'string') return text;
  // Remove leading heading lines like "# Title" or "## Heading"
  text = text.replace(/^#+\s+[^\n]+\n+/gm, '');
  // Remove bold/italic markdown
  text = text.replace(/\*\*([^*]+)\*\*/g, '$1');
  text = text.replace(/\*([^*]+)\*/g, '$1');
  text = text.replace(/_([^_]+)_/g, '$1');
  // Remove any remaining lines that are just bold labels like "**WOKE 31 | TRADITIONAL 14 | ...**"
  text = text.replace(/\*\*[^*\n]+\*\*/g, '');
  // Clean up multiple blank lines
  text = text.replace(/\n{3,}/g, '\n\n').trim();
  return text;
}

const fixed = reviews.map(r => {
  const changes = [];
  const margin = r.tradScore - r.wokeScore;
  const roundedMargin = Math.round(margin);

  // Fix verdict
  const expectedVerdict = calcVerdict(roundedMargin);
  if (r.verdict !== expectedVerdict) {
    changes.push(`verdict: '${r.verdict}' -> '${expectedVerdict}'`);
    r.verdict = expectedVerdict;
  }

  // Fix scoreMargin
  const expectedMarginStr = calcMarginStr(roundedMargin);
  if (r.scoreMargin !== expectedMarginStr) {
    changes.push(`scoreMargin: '${r.scoreMargin}' -> '${expectedMarginStr}'`);
    r.scoreMargin = expectedMarginStr;
  }

  // Fix wokeTrap — normalize to boolean
  // Per audit task: is_trap=true ONLY if margin is negative
  const expectedTrap = roundedMargin < 0;

  if (typeof r.wokeTrap === 'object' && r.wokeTrap !== null) {
    // Old object format — flatten to boolean
    changes.push(`wokeTrap: [object] -> ${expectedTrap}`);
    r.wokeTrap = expectedTrap;
  } else if (r.wokeTrap !== expectedTrap) {
    changes.push(`wokeTrap: ${r.wokeTrap} -> ${expectedTrap}`);
    r.wokeTrap = expectedTrap;
  }

  // Also fix woke_trap_assessment.is_trap if it exists
  if (r.woke_trap_assessment && r.woke_trap_assessment.is_trap !== expectedTrap) {
    r.woke_trap_assessment.is_trap = expectedTrap;
    if (!changes.some(c => c.includes('wokeTrap'))) {
      changes.push(`woke_trap_assessment.is_trap -> ${expectedTrap}`);
    }
  }

  // Fix markdown in summary fields
  if (r.summary) {
    ['overall', 'takeaway', 'context'].forEach(field => {
      if (typeof r.summary[field] === 'string') {
        const stripped = stripMarkdown(r.summary[field]);
        if (stripped !== r.summary[field]) {
          changes.push(`summary.${field}: markdown stripped`);
          r.summary[field] = stripped;
        }
      }
    });
  }

  if (changes.length > 0) {
    fixCount++;
    log.push({ slug: r.slug, margin: roundedMargin, changes });
  }

  return r;
});

// Write fixed reviews
fs.writeFileSync(reviewsPath, JSON.stringify(fixed, null, 2));

console.log(`\n✅ VVWS Fix Complete`);
console.log(`Fixed ${fixCount} reviews out of ${reviews.length} total\n`);
log.forEach(entry => {
  console.log(`📌 ${entry.slug} (margin: ${entry.margin > 0 ? '+' : ''}${entry.margin})`);
  entry.changes.forEach(c => console.log(`   - ${c}`));
});

// Write fix report
const reportPath = path.join(__dirname, '../vvws-fix-report.json');
fs.writeFileSync(reportPath, JSON.stringify({ timestamp: new Date().toISOString(), fixCount, fixes: log }, null, 2));
console.log(`\nReport saved to vvws-fix-report.json`);
