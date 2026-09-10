#!/usr/bin/env node
// compute-trope-combos.js — For each film, compute the exact (sev,auth,cent) combos
// that sum to wokeScore/tradScore within ±0.6, then write them to reviews.json
// as placeholders. Builder fills in names + explanations afterward.

const fs = require('fs');
const path = require('path');

const AM = { High: 0.7, Moderate: 0.5, Low: 0.3 };
const CM = { High: 1.8, Moderate: 1.0, Low: 0.5 };
function ws(sev, auth, cent) { return Math.round(sev * AM[auth] * CM[cent] * 100) / 100; }

const allOpts = [];
for (const sev of [5,4,3,2,1])
  for (const auth of Object.keys(AM))
    for (const cent of Object.keys(CM))
      allOpts.push({ sev, auth, cent, score: ws(sev, auth, cent) });
allOpts.sort((a,b) => b.score - a.score);

// Cache of all 2-8 element combos that sum to a given target ±0.6
// Key: target*100, Value: array of combos (each combo is array of {sev,auth,cent,score})
const comboCache = {};

function findCombos(target, minN, maxN) {
  if (target === 0) return [[]]; // empty combo
  const key = `${Math.round(target*100)}_${minN}_${maxN}`;
  if (comboCache[key]) return comboCache[key];
  
  const targetX100 = Math.round(target * 100);
  const results = [];
  
  for (let n = minN; n <= maxN; n++) {
    // Build all combos of n items
    const indices = new Array(n).fill(0);
    
    function dfs(pos, start, sumX100) {
      if (pos === n) {
        if (Math.abs(sumX100 - targetX100) <= 60) {
          const combo = indices.map(i => allOpts[i]);
          results.push(combo);
        }
        return;
      }
      if (results.length > 0) return; // first match is fine
      for (let i = start; i < allOpts.length; i++) {
        const newSum = sumX100 + Math.round(allOpts[i].score * 100);
        // Prune: can we still reach target?
        const remaining = n - pos - 1;
        const maxAdd = remaining * Math.round(allOpts[0].score * 100);
        const minAdd = remaining * Math.round(allOpts[allOpts.length-1].score * 100);
        if (newSum + maxAdd < targetX100 - 60) continue;
        if (newSum + minAdd > targetX100 + 60) continue;
        indices[pos] = i;
        dfs(pos + 1, i, newSum);
      }
    }
    dfs(0, 0, 0);
  }
  
  comboCache[key] = results;
  return results;
}

const films = [
  'die-hard-1988','back-to-the-future-1985','paddington-3-2026',
  'good-luck-have-fun-2026','toy-story-5-2026','the-mandalorian-and-grogu-2026',
  'pressure-2026','deep-water-2026','apex-2026','elio-2025','scream-7-2026',
  'beetlejuice-beetlejuice-2024','a-complete-unknown-2024','wuthering-heights',
  'moana-2-2024','youngblood-2026','ready-or-not-2','how-to-make-a-killing',
  'opus-2025','love-hurts-2025','tony-2026','ferris-buellers-day-off-1986',
  'the-sun-never-sets-2026','dirty-harry-1971','the-empire-strikes-back-1980',
  'memento-2000','mayday-2026','american-psycho-2000','onslaught-2026',
  'airplane-1980','the-uprising-2026','dead-poets-society-1989','brokeback-mountain-2005',
];

function main() {
  const revPath = path.resolve(__dirname, '..', 'src', 'data', 'reviews.json');
  const reviews = JSON.parse(fs.readFileSync(revPath, 'utf8'));
  let errors = [];

  for (const slug of films) {
    const r = reviews.find(r => r && r.slug === slug && r.type === 'film');
    if (!r) { errors.push(`${slug}: not found`); continue; }

    const wokeTarget = r.wokeScore || 0;
    const tradTarget = r.tradScore || 0;

    // Find combos with 3-6 tropes per category (enough for meaningful detail)
    // For scores > 25, allow up to 7; for > 40, allow up to 9
    const wokeMin = wokeTarget > 40 ? 7 : wokeTarget > 25 ? 5 : wokeTarget > 10 ? 3 : wokeTarget > 0 ? 2 : 0;
    const wokeMax = wokeTarget > 40 ? 9 : wokeTarget > 25 ? 7 : wokeTarget > 10 ? 5 : wokeTarget > 0 ? 4 : 0;
    const tradMin = tradTarget > 40 ? 7 : tradTarget > 25 ? 5 : tradTarget > 10 ? 3 : tradTarget > 0 ? 2 : 0;
    const tradMax = tradTarget > 40 ? 9 : tradTarget > 25 ? 7 : tradTarget > 10 ? 5 : tradTarget > 0 ? 4 : 0;

    let wokeCombos = wokeTarget > 0 ? findCombos(wokeTarget, wokeMin, wokeMax) : [[]];
    let tradCombos = tradTarget > 0 ? findCombos(tradTarget, tradMin, tradMax) : [[]];

    // Pick best combo: prefer one where combo count is in the middle of range
    function pickBest(combos, minN, maxN) {
      if (!combos || combos.length === 0 || (combos.length === 1 && combos[0].length === 0)) return [];
      // Sort by: closest to midpoint of desired range, then closest sum match
      const mid = (minN + maxN) / 2;
      return combos.sort((a, b) => {
        const aDist = Math.abs(a.length - mid);
        const bDist = Math.abs(b.length - mid);
        if (aDist !== bDist) return aDist - bDist;
        // Secondary: smaller sum diff
        const aSum = a.reduce((s, t) => s + t.score, 0);
        const bSum = b.reduce((s, t) => s + t.score, 0);
        return Math.abs(aSum) - Math.abs(bSum);
      })[0] || [];
    }

    const wokeCombo = pickBest(wokeCombos, wokeMin, wokeMax);
    const tradCombo = pickBest(tradCombos, tradMin, tradMax);

    const wSum = wokeCombo.reduce((s, t) => s + (t.score || 0), 0);
    const tSum = tradCombo.reduce((s, t) => s + (t.score || 0), 0);

    if (wokeTarget > 0 && (wokeCombo.length === 0 || Math.abs(wSum - wokeTarget) > 0.6)) {
      errors.push(`${slug}: woke fail — target=${wokeTarget}, n=${wokeMin}-${wokeMax}, got ${wokeCombo.length} combos, sum=${Math.round(wSum*10)/10}`);
      continue;
    }
    if (tradTarget > 0 && (tradCombo.length === 0 || Math.abs(tSum - tradTarget) > 0.6)) {
      errors.push(`${slug}: trad fail — target=${tradTarget}, n=${tradMin}-${tradMax}, got ${tradCombo.length} combos, sum=${Math.round(tSum*10)/10}`);
      continue;
    }

    // Build tropeAudit with placeholder names
    const shortSlug = slug.replace(/[^a-zA-Z0-9]/g, '-').substring(0, 20);
    const ta = [];
    let num = 1;

    for (const t of wokeCombo) {
      ta.push({
        id: `WOKE-${shortSlug}-${String(num).padStart(2, '0')}`,
        name: `PLACEHOLDER-WOKE-${num}`,
        category: 'Woke',
        severity: t.sev,
        authenticity: t.auth,
        centrality: t.cent,
        weightedScore: t.score,
        explanation: `[PLACEHOLDER — fill with 2-4 sentence explanation for this film's woke trope]`,
      });
      num++;
    }
    for (const t of tradCombo) {
      ta.push({
        id: `TRAD-${shortSlug}-${String(num).padStart(2, '0')}`,
        name: `PLACEHOLDER-TRAD-${num}`,
        category: 'Traditional',
        severity: t.sev,
        authenticity: t.auth,
        centrality: t.cent,
        weightedScore: t.score,
        explanation: `[PLACEHOLDER — fill with 2-4 sentence explanation for this film's traditional trope]`,
      });
      num++;
    }

    r.tropeAudit = ta;
    
    console.log(`${slug}: ${wokeCombo.length}W+${tradCombo.length}T tropeAudit | wokeSum=${Math.round(wSum*10)/10}/${wokeTarget} tradSum=${Math.round(tSum*10)/10}/${tradTarget}`);
  }

  if (errors.length > 0) {
    console.error('\nERRORS:');
    errors.forEach(e => console.error('  ' + e));
    // Don't exit, write partial results
  }

  fs.writeFileSync(revPath, JSON.stringify(reviews, null, 2));
  console.log(`\nWritten to reviews.json`);
  if (errors.length > 0) process.exit(1);
}

main();