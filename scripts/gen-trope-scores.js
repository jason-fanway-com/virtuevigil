#!/usr/bin/env node
// gen-trope-scores.js — Compute valid trope score combinations using DP subset-sum
// Formula: weightedScore = severity × authMultiplier × centMultiplier
// Auth: High=0.7, Moderate=0.5, Low=0.3
// Cent: High=1.8, Moderate=1.0, Low=0.5

const AUTH_MAP = { High: 0.7, Moderate: 0.5, Low: 0.3 };
const CENT_MAP = { High: 1.8, Moderate: 1.0, Low: 0.5 };

function ws(severity, auth, cent) {
  return Math.round(severity * AUTH_MAP[auth] * CENT_MAP[cent] * 100) / 100;
}

// All distinct trope configurations
function allConfigs() {
  const configs = [];
  for (const sev of [5,4,3,2,1]) {
    for (const auth of ['High','Moderate','Low']) {
      for (const cent of ['High','Moderate','Low']) {
        configs.push({ sev, auth, cent, score: ws(sev, auth, cent) });
      }
    }
  }
  return configs;
}

// Use DP subset-sum to find best combination for target
function findBestSubset(target, minN, maxN) {
  const configs = allConfigs();
  
  // DP[key] = best set achieving sum ~key with n items
  // Key is score*100 to avoid float issues
  const targetX100 = Math.round(target * 100);
  const tolerance = 60; // ±0.6 = ±60 in *100 space
  
  let best = null;
  let bestDiff = Infinity;
  
  // Use iterative deepening: try 2, 3, 4, 5, 6 tropes
  for (let n = minN; n <= maxN; n++) {
    // Build all n-element combinations efficiently
    // Limit search to top 20 configs (ignore the tiny ones for efficiency)
    const topConfigs = configs.slice(0, 20);
    
    function tryCombos(start, depth, current, sum) {
      if (depth === n) {
        const diff = Math.abs(sum - targetX100);
        if (diff <= tolerance && diff < bestDiff) {
          bestDiff = diff;
          best = current.map(idx => configs[idx]);
        }
        return;
      }
      const remaining = n - depth;
      for (let i = start; i < configs.length; i++) {
        const newSum = sum + Math.round(configs[i].score * 100);
        // Prune: if even adding the largest remaining values can't reach target
        // and even adding the smallest remaining values would overshoot
        tryCombos(i, depth + 1, [...current, i], newSum);
      }
    }
    
    tryCombos(0, 0, [], 0);
    if (best) {
      return { n, tropes: best, sum: best.reduce((s, t) => s + t.score, 0), diff: bestDiff / 100 };
    }
  }
  
  // If DP didn't find perfect, try up to n=6 with wider search
  for (let n = 2; n <= 6; n++) {
    const topConfigs = configs.slice(0, 25);
    
    function tryCombos2(start, depth, current, sum) {
      if (depth === n) {
        const diff = Math.abs(sum - targetX100);
        if (diff < bestDiff) {
          bestDiff = diff;
          best = current.map(idx => configs[idx]);
        }
        return;
      }
      for (let i = start; i < topConfigs.length; i++) {
        const newSum = sum + Math.round(topConfigs[i].score * 100);
        tryCombos2(i, depth + 1, [...current, i], newSum);
      }
    }
    
    tryCombos2(0, 0, [], 0);
    if (bestDiff <= tolerance) {
      return { n, tropes: best, sum: best.reduce((s, t) => s + t.score, 0), diff: bestDiff / 100 };
    }
  }
  
  // Fallback: return best found even if outside tolerance
  return best ? { tropes: best, sum: best.reduce((s, t) => s + t.score, 0), diff: bestDiff / 100 } : null;
}

const films = [
  { slug: 'die-hard-1988', woke: 2.5, trad: 15.05 },
  { slug: 'back-to-the-future-1985', woke: 1, trad: 18.19 },
  { slug: 'paddington-3-2026', woke: 3.5, trad: 18.9 },
  { slug: 'good-luck-have-fun-2026', woke: 10.2, trad: 7.4 },
  { slug: 'toy-story-5-2026', woke: 9.38, trad: 34.02 },
  { slug: 'the-mandalorian-and-grogu-2026', woke: 11.4, trad: 7.8 },
  { slug: 'pressure-2026', woke: 7.2, trad: 11.8 },
  { slug: 'deep-water-2026', woke: 3.5, trad: 14.2 },
  { slug: 'apex-2026', woke: 6.8, trad: 18.4 },
  { slug: 'elio-2025', woke: 18, trad: 24 },
  { slug: 'scream-7-2026', woke: 8.5, trad: 16.2 },
  { slug: 'beetlejuice-beetlejuice-2024', woke: 16, trad: 12 },
  { slug: 'a-complete-unknown-2024', woke: 14, trad: 16 },
  { slug: 'wuthering-heights', woke: 36, trad: 26 },
  { slug: 'moana-2-2024', woke: 13, trad: 17 },
  { slug: 'youngblood-2026', woke: 48, trad: 52 },
  { slug: 'ready-or-not-2', woke: 6, trad: 3 },
  { slug: 'how-to-make-a-killing', woke: 9, trad: 14 },
  { slug: 'opus-2025', woke: 8.4, trad: 5.1 },
  { slug: 'love-hurts-2025', woke: 3.6, trad: 10.2 },
  { slug: 'tony-2026', woke: 2.5, trad: 24.75 },
  { slug: 'ferris-buellers-day-off-1986', woke: 0, trad: 27.25 },
  { slug: 'the-sun-never-sets-2026', woke: 2.8, trad: 16.4 },
  { slug: 'dirty-harry-1971', woke: 1.4, trad: 31.98 },
  { slug: 'the-empire-strikes-back-1980', woke: 1.62, trad: 30.24 },
  { slug: 'memento-2000', woke: 5.88, trad: 18.48 },
  { slug: 'mayday-2026', woke: 5.04, trad: 17.76 },
  { slug: 'american-psycho-2000', woke: 7.5, trad: 15.6 },
  { slug: 'onslaught-2026', woke: 4.59, trad: 18.48 },
  { slug: 'airplane-1980', woke: 2.16, trad: 24.36 },
  { slug: 'the-uprising-2026', woke: 11.28, trad: 17.88 },
  { slug: 'dead-poets-society-1989', woke: 14.04, trad: 18.12 },
  { slug: 'brokeback-mountain-2005', woke: 18, trad: 18 },
];

// Print all unique scores
const configs = allConfigs();
const uniqueScores = [...new Set(configs.map(c => c.score))].sort((a,b) => b-a);
console.log('Unique trope scores:', uniqueScores.length, 'values');
console.log(uniqueScores.join(', '));
console.log();

// DP subset sum
const scoreSet = new Set(uniqueScores.map(s => Math.round(s * 100)));

function findExactCombo(target, minN, maxN) {
  if (target === 0) return null;
  const targetX100 = Math.round(target * 100);
  const toleranceX100 = 60; // ±0.6

  let bestScoreCombo = null;
  let bestDiff = Infinity;
  let bestN = 0;

  for (let n = minN; n <= maxN; n++) {
    // For each n, we try all combos of n scores
    // Use iterative approach with the unique scores
    const scores = uniqueScores;
    
    function dfs(start, depth, current, sumX100) {
      if (depth === n) {
        const diff = Math.abs(sumX100 - targetX100);
        if (diff < bestDiff) {
          bestDiff = diff;
          bestScoreCombo = [...current];
          bestN = n;
        }
        return;
      }
      if (bestDiff === 0) return; // perfect match found
      for (let i = start; i < scores.length; i++) {
        const sX100 = Math.round(scores[i] * 100);
        // Prune
        const remaining = n - depth - 1;
        const maxRemaining = remaining * Math.round(scores[0] * 100); // all remaining at max
        const minRemaining = remaining * Math.round(scores[scores.length - 1] * 100); // at min
        const curSum = sumX100 + sX100;
        if (curSum + maxRemaining < targetX100 - toleranceX100) continue; // can't reach
        if (curSum + minRemaining > targetX100 + toleranceX100) break; // will overshoot
        dfs(i, depth + 1, [...current, scores[i]], curSum);
      }
    }
    
    dfs(0, 0, [], 0);
    if (bestDiff <= toleranceX100) break; // found within tolerance
  }

  if (bestScoreCombo) {
    // Map scores back to configs (pick configs matching those scores)
    const mapped = [];
    const used = new Set();
    for (const score of bestScoreCombo) {
      const cfg = configs.find((c, i) => c.score === score && !used.has(i));
      if (cfg) {
        used.add(configs.indexOf(cfg));
        mapped.push(cfg);
      }
    }
    const sum = bestScoreCombo.reduce((s, v) => s + v, 0);
    return { n: bestN, tropes: mapped, sum: Math.round(sum * 100) / 100, diff: bestDiff / 100 };
  }
  return null;
}

for (const film of films) {
  console.log(`--- ${film.slug} (woke=${film.woke}, trad=${film.trad}) ---`);
  
  const wokeC = film.woke > 0 ? findExactCombo(film.woke, 2, 5) : null;
  const tradC = film.trad > 0 ? findExactCombo(film.trad, 2, 5) : null;
  
  if (wokeC) {
    console.log(`  WOKE (${wokeC.n}): sum=${wokeC.sum} diff=${Math.round(wokeC.diff*100)/100}`);
    wokeC.tropes.forEach(t => console.log(`    sev=${t.sev} auth=${t.auth} cent=${t.cent} ws=${t.score}`));
  } else if (film.woke > 0) {
    console.log(`  WOKE: NO COMBO FOUND for target ${film.woke}`);
  } else {
    console.log(`  WOKE: 0 (no tropes needed)`);
  }
  
  if (tradC) {
    console.log(`  TRAD (${tradC.n}): sum=${tradC.sum} diff=${Math.round(tradC.diff*100)/100}`);
    tradC.tropes.forEach(t => console.log(`    sev=${t.sev} auth=${t.auth} cent=${t.cent} ws=${t.score}`));
  } else if (film.trad > 0) {
    console.log(`  TRAD: NO COMBO FOUND for target ${film.trad}`);
  } else {
    console.log(`  TRAD: 0 (no tropes needed)`);
  }
}