#!/usr/bin/env node
// Generate: "Every Crime Movie & Series Ranked by Woke Score"
const fs = require('fs');
const data = require('../src/data/reviews.json');

const films = Object.entries(data)
  .filter(([k,r]) => r.genre && r.genre.includes('Crime') && r.wokeScore != null && r.tradScore != null && r.summary && r.summary.overall)
  .map(([key, r]) => ({
    slug: r.slug || key, title: r.title, year: r.year,
    wokeScore: r.wokeScore, tradScore: r.tradScore,
    margin: parseFloat(((r.tradScore||0) - (r.wokeScore||0)).toFixed(2)),
    verdict: r.verdict,
    director: r.director || '',
    stars: r.stars || '',
    genre: r.genre || '',
    platform: r.platform || '',
    distributor: r.distributor || '',
    summary: r.summary.overall
  }))
  .sort((a,b) => a.margin - b.margin);

// Verdict groups (most-woke to most-traditional)
const verdictSections = [
  { label: 'STRONGLY WOKE', films: [] },
  { label: 'WOKE', films: [] },
  { label: 'WOKE LEAN', films: [] },
  { label: 'MIXED', films: [] },
  { label: 'TRADITIONAL LEAN', films: [] },
  { label: 'TRADITIONAL', films: [] },
  { label: 'STRONGLY TRADITIONAL', films: [] },
];

films.forEach(f => {
  const section = verdictSections.find(s => s.label === f.verdict);
  if (section) section.films.push(f);
});

// Remove empty sections
const active = verdictSections.filter(s => s.films.length > 0);

function verdictClass(v) {
  const map = {
    'STRONGLY WOKE': 'strongly-woke',
    'WOKE': 'woke',
    'WOKE LEAN': 'woke-lean',
    'MIXED': 'mixed',
    'TRADITIONAL LEAN': 'traditional-lean',
    'TRADITIONAL': 'traditional',
    'STRONGLY TRADITIONAL': 'strongly-traditional',
  };
  return map[v] || 'mixed';
}

function formatMargin(m) {
  const abs = Math.abs(m).toFixed(1);
  if (m < 0) return `+${abs} WOKE`;
  if (m > 0) return `+${abs} TRADITIONAL`;
  return 'EVEN';
}

function extractDescription(summary, length) {
  // Get first meaningful paragraph
  const paras = summary.split('\n').filter(p => p.trim().length > 30);
  let desc = '';
  for (const p of paras) {
    if (desc.length + p.length > length) break;
    if (desc) desc += ' ';
    desc += p.trim();
  }
  if (desc.length > length) desc = desc.substring(0, length).replace(/\s\S*$/, '') + '...';
  return desc || summary.substring(0, length) + '...';
}

let html = `<!--
SOCIAL SHARE METADATA
Title: Every Crime Movie & Series Ranked by Woke Score: 76 Films Tested
Description: From Emilia Perez to The Silence of the Lambs, we scored every crime film and series in our database. See which crime stories Hollywood politicized and which ones told the truth. Rankings from most woke to most traditional. Parents, know what you're watching.
Image: https://virtuevigil.com/images/social-default.jpg
URL: https://virtuevigil.com/lists/every-crime-movie-ranked-woke-score/
-->

<article class="listicle-article">
  <div class="listicle-intro">
    <p>Crime films are the conscience of cinema. More than any other genre, they ask the question Hollywood prefers to avoid: what is justice, and who gets to define it? A detective chasing a killer, a mafia family at dinner, a heist crew planning the score — every crime story is a moral argument in disguise. The question isn't whether the film has a worldview. The question is which one.</p>

    <p>VirtueVigil has scored 76 crime films and series using the same dual-metric methodology we apply to every review. Progressive ideology gets tracked on one axis. Traditional values get tracked on the other. The margin between them tells you whether the film tells its story straight or bends the genre to serve a political narrative.</p>

    <p>What we found: crime cinema bends traditional overall. Twenty-two films carry the STRONGLY TRADITIONAL verdict, anchored by The Silence of the Lambs, The Godfather Part II, and 12 Angry Men. But the woke outliers are significant — Emilia Pérez made history as the most ideologically aggressive crime film in our database, and films like Chinatown and The Wolf of Wall Street hide progressive critiques of American institutions inside genre entertainment. Rankings run from most woke (top) to most traditional (bottom). Every entry links to its full VirtueVigil review with trope-by-trope breakdown, parental guidance, and scoring detail.</p>
  </div>
`;

let entryNum = 0;

for (const section of active) {
  html += `\n  <hr>\n  <h2>${section.label}</h2>\n`;
  
  if (section.label === 'STRONGLY WOKE' && section.films.length === 1) {
    html += `  <p class="section-note">Only one crime film in our database scored STRONGLY WOKE — but it made history doing it.</p>\n`;
  }
  if (section.label === 'STRONGLY TRADITIONAL') {
    html += `  <p class="section-note">Twenty-two crime films and series scored STRONGLY TRADITIONAL — the largest single verdict group in this ranking. The Godfather, The Dark Knight, John Wick, Reacher, 12 Angry Men: these are films that understand evil is real, justice is worth fighting for, and institutions work best when they protect the innocent rather than explain away the guilty.</p>\n`;
  }

  for (const f of section.films) {
    entryNum++;
    const linkSlug = f.slug;
    const desc = extractDescription(f.summary, 700);
    const marginDir = f.margin < 0 ? 'WOKE' : f.margin > 0 ? 'TRADITIONAL' : 'EVEN';

    // Build meta line
    let metaParts = [];
    if (f.genre) metaParts.push(`<strong>Genre:</strong> ${f.genre}`);
    if (f.year) metaParts.push(`<strong>Year:</strong> ${f.year}`);
    if (f.platform && f.platform !== 'Theatrical') metaParts.push(`<strong>Platform:</strong> ${f.platform}`);
    if (f.director) metaParts.push(`<strong>Director:</strong> ${f.director}`);
    const meta = metaParts.join(' &bull; ');

    html += `\n  <hr>\n`;
    html += `  <h3><a href="/reviews/${linkSlug}/">${f.title} (${f.year})</a></h3>\n`;
    html += `  <div class="listicle-scores">\n`;
    html += `    <span class="verdict-badge ${verdictClass(f.verdict)}">${f.verdict}</span>\n`;
    html += `    <span class="mini-score woke">WOKE: ${f.wokeScore.toFixed(1)}</span>\n`;
    html += `    <span class="mini-score trad">TRAD: ${f.tradScore.toFixed(1)}</span>\n`;
    html += `    <span class="mini-score" style="color:var(--accent-amber);">MARGIN: ${formatMargin(f.margin)}</span>\n`;
    html += `  </div>\n`;
    html += `  <p class="listicle-meta">${meta}</p>\n`;
    html += `  <p>${desc}</p>\n`;
    html += `  <p><a href="/reviews/${linkSlug}/" class="listicle-review-link">Read the full VirtueVigil review of ${f.title}</a></p>\n`;
  }
}

html += `
</article>`;

const outDir = '/Users/joestrazza/virtuevigil/lists/every-crime-movie-ranked-woke-score';
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(outDir + '/content.html', html);

console.log(`Written ${entryNum} entries to ${outDir}/content.html`);
console.log(`Verdict breakdown:`, active.map(s => `${s.label}: ${s.films.length}`).join(', '));