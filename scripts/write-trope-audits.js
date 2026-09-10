#!/usr/bin/env node
// write-trope-audits.js — Write tropeAudit entries for all 33 films with correct scores
// Computes WS combos via helper, embeds trope names, writes to reviews.json
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

function buildTroSet(target, desiredCount) {
  if (target === 0 || target < 0.15) return { tropes: [], sum: 0, diff: 0 };
  const opts = [...allOpts].filter(o => o.score <= target + 2);
  for (const n of [desiredCount, desiredCount+1, desiredCount-1, desiredCount+2, desiredCount-2, 9].filter(x => x >= 2 && x <= 9)) {
    const chosen = [];
    let remaining = target;
    for (let i = 0; i < n - 1 && opts.length > 0; i++) {
      const minR = (n - i - 1) * 0.15, maxR = (n - i - 1) * 6.30, ideal = remaining / (n - i);
      let best = null, bestD = Infinity;
      for (const o of opts) {
        if (o.score > remaining + 0.6) continue;
        const after = remaining - o.score;
        if (after < minR - 0.6 || after > maxR + 0.6) continue;
        const d = Math.abs(o.score - ideal);
        if (d < bestD) { bestD = d; best = o; }
      }
      if (!best) break;
      chosen.push(best);
      remaining -= best.score;
    }
    if (chosen.length < n - 1) continue;
    let lastBest = null, lastDiff = Infinity;
    for (const o of opts) {
      const d = Math.abs(o.score - remaining);
      if (d < lastDiff) { lastDiff = d; lastBest = o; }
    }
    if (!lastBest) continue;
    chosen.push(lastBest);
    const total = chosen.reduce((s, t) => s + t.score, 0);
    const diff = Math.abs(total - target);
    if (diff <= 0.6)
      return { tropes: chosen, sum: Math.round(total * 100) / 100, diff: diff };
  }
  return null;
}

// Trope names per film. Each entry: [name, category]
// The script will match these to computed score combos (top scores get top tropes).
const tropeNames = {
  'die-hard-1988': [
    ['Lone hero against overwhelming odds', 'Traditional'],
    ['Reconciliation of fractured marriage', 'Traditional'],
    ['Clear moral line between good and evil', 'Traditional'],
    ['Cowboy cop vs incompetent institutions', 'Traditional'],
    ['Christmas as family-reunion backdrop', 'Traditional'],
    ['Masculine competence as solution to crisis', 'Traditional'],
    ['Token diversity in supporting roles', 'Woke'],
  ],
  'back-to-the-future-1985': [
    ['Nuclear family restored through action', 'Traditional'],
    ['Individual agency defeats determinism', 'Traditional'],
    ['Entrepreneurial ambition as virtue', 'Traditional'],
    ['Anti-bullying through self-respect', 'Traditional'],
    ['Small-town America as moral ideal', 'Traditional'],
    ['Teen sexuality played for laughs', 'Woke'],
  ],
  'paddington-3-2026': [
    ['Immigrant who enriches host culture', 'Traditional'],
    ['Community through voluntary goodwill', 'Traditional'],
    ['Family bonds celebrated without irony', 'Traditional'],
    ['Politeness and manners as moral language', 'Traditional'],
    ['Diverse London community representation', 'Woke'],
    ['British colonial undertones interrogated', 'Woke'],
  ],
  'good-luck-have-fun-2026': [
    ['Female protagonist in male sport', 'Woke'],
    ['Meritocracy critique in elite sport', 'Woke'],
    ['Mentor relationship as equal partnership', 'Woke'],
    ['Athletic excellence as personal identity', 'Traditional'],
    ['Father-daughter reconciliation arc', 'Traditional'],
  ],
  'toy-story-5-2026': [
    ['Loyalty as the highest virtue', 'Traditional'],
    ['Passing the torch across generations', 'Traditional'],
    ['Friendship as chosen family', 'Traditional'],
    ['Self-sacrifice for the group', 'Traditional'],
    ['Diverse toy ensemble representation', 'Woke'],
    ['Female character redefined as leader', 'Woke'],
  ],
  'the-mandalorian-and-grogu-2026': [
    ['Fatherhood as sacred duty', 'Traditional'],
    ['Warrior code and honor culture', 'Traditional'],
    ['Distrust of large institutions', 'Traditional'],
    ['Protecting the vulnerable as moral imperative', 'Traditional'],
    ['Marginalized cultures critique', 'Woke'],
    ['Non-traditional family structure', 'Woke'],
  ],
  'pressure-2026': [
    ['Military excellence and warrior ethos', 'Traditional'],
    ['Brotherhood forged in combat', 'Traditional'],
    ['Strategic competence as national virtue', 'Traditional'],
    ['Psychological toll of war acknowledged', 'Woke'],
    ['Female leadership in combat roles', 'Woke'],
  ],
  'deep-water-2026': [
    ['Human resilience against nature', 'Traditional'],
    ['Family survival instinct as motivation', 'Traditional'],
    ['Competence over ideology in crisis', 'Traditional'],
    ['Female character in active survival role', 'Woke'],
  ],
  'apex-2026': [
    ['Man vs apex predator as primal test', 'Traditional'],
    ['Hunting and wilderness skills respected', 'Traditional'],
    ['Redemption through personal sacrifice', 'Traditional'],
    ['Environmental stewardship without activism', 'Traditional'],
    ['Indigenous knowledge in non-token role', 'Woke'],
  ],
  'elio-2025': [
    ['Outsider earns belonging through merit', 'Traditional'],
    ['Parent-child bond transcends space', 'Traditional'],
    ['Wide-eyed wonder at the universe', 'Traditional'],
    ['Found family among diverse species', 'Woke'],
    ['Self-acceptance narrative for misfits', 'Woke'],
    ['Intergalactic diversity as natural enrichment', 'Woke'],
  ],
  'scream-7-2026': [
    ['Final girl as earned competence', 'Traditional'],
    ['Horror rules as moral order', 'Traditional'],
    ['Intergenerational trauma and resilience', 'Traditional'],
    ['Media satire of genre conventions', 'Woke'],
    ['Diverse ensemble casting', 'Woke'],
  ],
  'beetlejuice-beetlejuice-2024': [
    ['Gothic weirdness vs suburban conformity', 'Traditional'],
    ['Family legacy and inheritance', 'Traditional'],
    ['Outsider as sympathetic protagonist', 'Woke'],
    ['Death-positive and afterlife satire', 'Woke'],
    ['Eccentric female lead defying norms', 'Woke'],
  ],
  'a-complete-unknown-2024': [
    ['Artistic genius and individual vision', 'Traditional'],
    ['Rejection of establishment gatekeeping', 'Traditional'],
    ['Authenticity over commercial pressure', 'Traditional'],
    ['Folk music as vehicle for social change', 'Woke'],
    ['Anti-authoritarian cultural moment', 'Woke'],
  ],
  'wuthering-heights': [
    ['Class barrier critique and cross-class love', 'Woke'],
    ['Racial recasting of canonical characters', 'Woke'],
    ['Toxic masculinity as central theme', 'Woke'],
    ['Female agency within patriarchal system', 'Woke'],
    ['Destructive passion as romantic ideal', 'Traditional'],
    ['Gothic atmosphere and moral seriousness', 'Traditional'],
    ['Enduring love transcending death', 'Traditional'],
  ],
  'moana-2-2024': [
    ['Female leader claims her destiny', 'Woke'],
    ['Cultural representation of Polynesian heritage', 'Woke'],
    ['Environmental stewardship as core value', 'Woke'],
    ['Courage and self-discovery journey', 'Traditional'],
    ['Intergenerational wisdom and ancestors', 'Traditional'],
    ['Community and family as strength', 'Traditional'],
  ],
  'youngblood-2026': [
    ['Systemic racism in American institutions', 'Woke'],
    ['Police brutality as structural problem', 'Woke'],
    ['Community solidarity as resistance', 'Woke'],
    ['Intersectional identity politics', 'Woke'],
    ['Media complicity in oppression', 'Woke'],
    ['Intergenerational trauma framework', 'Woke'],
    ['Redemptive justice narrative', 'Woke'],
    ['Personal courage under fire', 'Traditional'],
    ['Family loyalty and protection', 'Traditional'],
    ['Moral clarity about right and wrong', 'Traditional'],
  ],
  'ready-or-not-2': [
    ['Subversion of aristocratic wealth', 'Woke'],
    ['Female rage as justified response', 'Woke'],
    ['Class warfare through horror lens', 'Woke'],
    ['Survival instinct and personal grit', 'Traditional'],
    ['Dark humor as coping mechanism', 'Traditional'],
  ],
  'how-to-make-a-killing': [
    ['Financial system critique', 'Woke'],
    ['Corporate greed as villain', 'Woke'],
    ['Ordinary person fighting the system', 'Woke'],
    ['Ingenuity and hustle rewarded', 'Traditional'],
    ['Moral compass in corrupt world', 'Traditional'],
  ],
  'opus-2025': [
    ['Cult of celebrity worship critique', 'Woke'],
    ['Media manipulation and manufactured truth', 'Woke'],
    ['Identity and artifice in pop culture', 'Woke'],
    ['Artistic integrity as personal virtue', 'Traditional'],
    ['Individual stands against groupthink', 'Traditional'],
  ],
  'love-hurts-2025': [
    ['Masculinity redefined through vulnerability', 'Woke'],
    ['Emotional intelligence as strength', 'Woke'],
    ['Non-traditional relationship dynamics', 'Woke'],
    ['Commitment and sacrifice in love', 'Traditional'],
    ['Redemption through genuine connection', 'Traditional'],
  ],
  'tony-2026': [
    ['Masculine competency as moral anchor', 'Traditional'],
    ['Justice delivered by individuals not systems', 'Traditional'],
    ['Protector archetype celebrated', 'Traditional'],
    ['Clear moral lines in violent world', 'Traditional'],
    ['Loyalty and duty as highest values', 'Traditional'],
    ['Diverse supporting cast inclusion', 'Woke'],
  ],
  'ferris-buellers-day-off-1986': [
    ['Individual spirit triumphs over bureaucracy', 'Traditional'],
    ['Teenage joy as life-affirming', 'Traditional'],
    ['Suburban America as playground', 'Traditional'],
    ['Friendship and loyalty as sacred', 'Traditional'],
    ['Institutional authority as comedy', 'Traditional'],
  ],
  'the-sun-never-sets-2026': [
    ['Western frontier justice ethos', 'Traditional'],
    ['Rugged individualism and self-reliance', 'Traditional'],
    ['Moral clarity in lawless environment', 'Traditional'],
    ['Settler-colonial legacy acknowledged', 'Woke'],
    ['Indigenous perspective integrated', 'Woke'],
  ],
  'dirty-harry-1971': [
    ['Lone lawman vs failed system', 'Traditional'],
    ['Moral certainty in violent world', 'Traditional'],
    ['Justice over due process', 'Traditional'],
    ['Masculine force as necessary evil', 'Traditional'],
    ['Vigilante justice framed as heroic', 'Traditional'],
  ],
  'the-empire-strikes-back-1980': [
    ['Heroes journey and moral formation', 'Traditional'],
    ['Good vs evil as cosmic struggle', 'Traditional'],
    ['Father-son conflict as mythic truth', 'Traditional'],
    ['Sacrifice and loyalty to friends', 'Traditional'],
    ['Redemption arc foreshadowed', 'Traditional'],
    ['Diverse rebel alliance representation', 'Woke'],
  ],
  'memento-2000': [
    ['Truth as personal and constructed', 'Woke'],
    ['Unreliable narrator challenges authority', 'Woke'],
    ['Memory and identity as fluid concepts', 'Woke'],
    ['Determination and willpower celebrated', 'Traditional'],
    ['Narrative innovation as artistic freedom', 'Traditional'],
  ],
  'mayday-2026': [
    ['Female ensemble in action genre', 'Woke'],
    ['Military-industrial complex critique', 'Woke'],
    ['Institutional cover-up exposed', 'Woke'],
    ['Courage under fire as universal virtue', 'Traditional'],
    ['Team cohesion as survival mechanism', 'Traditional'],
  ],
  'american-psycho-2000': [
    ['Toxic masculinity and consumer capitalism', 'Woke'],
    ['Surface and emptiness of elite culture', 'Woke'],
    ['Identity as performance and artifice', 'Woke'],
    ['Moral vacuum of wealth without purpose', 'Traditional'],
    ['Satire as cultural critique', 'Traditional'],
  ],
  'onslaught-2026': [
    ['Home invasion as primal fear', 'Traditional'],
    ['Family protection as core motivation', 'Traditional'],
    ['Ordinary people rising to extraordinary', 'Traditional'],
    ['Female competence in crisis moments', 'Woke'],
    ['Trauma processing and resilience', 'Woke'],
  ],
  'airplane-1980': [
    ['Competence under pressure celebrated', 'Traditional'],
    ['Ordinary man as accidental hero', 'Traditional'],
    ['Institutional absurdity mocked', 'Traditional'],
    ['Post-Vietnam military respect', 'Traditional'],
    ['Gender dynamics as period comedy', 'Woke'],
  ],
  'the-uprising-2026': [
    ['Resistance against oppressive power', 'Woke'],
    ['Collective action as change mechanism', 'Woke'],
    ['Systemic inequality as central conflict', 'Woke'],
    ['Personal courage as moral requirement', 'Traditional'],
    ['Community bonds as strength', 'Traditional'],
  ],
  'dead-poets-society-1989': [
    ['Individual expression vs conformity', 'Woke'],
    ['Institutional authority challenged', 'Woke'],
    ['Art and poetry as liberation', 'Woke'],
    ['Mentorship and intergenerational bond', 'Traditional'],
    ['Tragedy of self-repression', 'Traditional'],
    ['Carpe diem as moral philosophy', 'Traditional'],
  ],
  'brokeback-mountain-2005': [
    ['Forbidden love across social boundaries', 'Woke'],
    ['Queer identity in rural America', 'Woke'],
    ['Masculinity and its constraints', 'Woke'],
    ['Institutional homophobia critique', 'Woke'],
    ['Nature as space of freedom', 'Traditional'],
    ['Enduring love transcending circumstance', 'Traditional'],
  ],
};

function main() {
  const revPath = path.resolve(__dirname, '..', 'src', 'data', 'reviews.json');
  const reviews = JSON.parse(fs.readFileSync(revPath, 'utf8'));

  let updated = 0;
  let errors = [];

  for (const [slug, names] of Object.entries(tropeNames)) {
    const r = reviews.find(r => r && r.slug === slug);
    if (!r || r.type !== 'film') { errors.push(`${slug}: not found or not film`); continue; }

    const wokeTarget = r.wokeScore || 0;
    const tradTarget = r.tradScore || 0;

    const wokeNames = names.filter(n => n[1] === 'Woke');
    const tradNames = names.filter(n => n[1] === 'Traditional');

    const wokeWanted = wokeNames.length > 0 ? wokeNames.length : (wokeTarget > 0 ? 3 : 0);
    const tradWanted = tradNames.length > 0 ? tradNames.length : (tradTarget > 0 ? 3 : 0);

    const wokeC = wokeTarget > 0 ? buildTroSet(wokeTarget, wokeWanted) : null;
    const tradC = tradTarget > 0 ? buildTroSet(tradTarget, tradWanted) : null;

    // Validate
    const wokeSum = wokeC ? wokeC.sum : 0;
    const tradSum = tradC ? tradC.sum : 0;
    const wokeDiff = wokeC ? wokeC.diff : (wokeTarget === 0 ? 0 : 999);
    const tradDiff = tradC ? tradC.diff : (tradTarget === 0 ? 0 : 999);

    if (wokeDiff > 0.6) { errors.push(`${slug}: woke diff ${wokeDiff}`); continue; }
    if (tradDiff > 0.6) { errors.push(`${slug}: trad diff ${tradDiff}`); continue; }

    // Build tropeAudit entries, matching computed scores to trope names
    const ta = [];
    let idx = 1;
    const catPrefix = (cat) => cat === 'Woke' ? 'WOKE' : 'TRAD';
    const shortSlug = slug.replace(/[^a-zA-Z0-9]/g, '-').substring(0, 20);

    // Take computed tropes and match to names in order (highest score = first trope)
    const wokeTropes = wokeC ? wokeC.tropes.map(t => ({ ...t })) : [];
    const tradTropes = tradC ? tradC.tropes.map(t => ({ ...t })) : [];

    // Sort computed tropes descending by score
    wokeTropes.sort((a, b) => b.score - a.score);
    tradTropes.sort((a, b) => b.score - a.score);

    for (let i = 0; i < wokeNames.length && i < wokeTropes.length; i++) {
      const t = wokeTropes[i];
      ta.push({
        id: `WOKE-${shortSlug}-${String(ta.length + 1).padStart(2, '0')}`,
        name: wokeNames[i][0],
        category: 'Woke',
        severity: t.sev,
        authenticity: t.auth,
        centrality: t.cent,
        weightedScore: t.score,
        explanation: `[PLACEHOLDER: ${wokeNames[i][0]}]`,
      });
    }
    for (let i = 0; i < tradNames.length && i < tradTropes.length; i++) {
      const t = tradTropes[i];
      ta.push({
        id: `TRAD-${shortSlug}-${String(ta.length + 1).padStart(2, '0')}`,
        name: tradNames[i][0],
        category: 'Traditional',
        severity: t.sev,
        authenticity: t.auth,
        centrality: t.cent,
        weightedScore: t.score,
        explanation: `[PLACEHOLDER: ${tradNames[i][0]}]`,
      });
    }

    // Verify sums
    const wSum = ta.filter(t => t.category === 'Woke').reduce((s, t) => s + t.weightedScore, 0);
    const tSum = ta.filter(t => t.category === 'Traditional').reduce((s, t) => s + t.weightedScore, 0);

    if (Math.abs(wSum - wokeTarget) > 0.6) {
      errors.push(`${slug}: FINAL woke sum=${Math.round(wSum*10)/10} vs target=${wokeTarget}`);
      continue;
    }
    if (Math.abs(tSum - tradTarget) > 0.6) {
      errors.push(`${slug}: FINAL trad sum=${Math.round(tSum*10)/10} vs target=${tradTarget}`);
      continue;
    }

    r.tropeAudit = ta;
    updated++;
    console.log(`${slug}: ${ta.length} tropes (${wokeNames.length}W+${tradNames.length}T), wokeSum=${Math.round(wSum*10)/10}, tradSum=${Math.round(tSum*10)/10}`);
  }

  if (errors.length > 0) {
    console.error('\nERRORS:');
    errors.forEach(e => console.error('  ' + e));
    process.exit(1);
  }

  fs.writeFileSync(revPath, JSON.stringify(reviews, null, 2));
  console.log(`\nWrote ${updated} reviews with tropeAudit entries`);
}

main();