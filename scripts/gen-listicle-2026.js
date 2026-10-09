const fs = require('fs');

const reviews = require('../src/data/reviews.json');
const y2026 = reviews.filter(r => r.year === 2026).map(r => {
  const ts = r.tradScore || 0;
  const ws = r.wokeScore || 0;
  const margin = +(ts - ws).toFixed(2);
  return { ...r, margin };
}).sort((a,b) => a.margin - b.margin);

// Generate HTML entries for each film
let entries = '';
y2026.forEach((r, i) => {
  const num = i + 1;
  
  // Verdict badge label
  let verdictLabel = '';
  let verdictClass = '';
  if (r.margin <= -15) { verdictLabel = 'woke'; verdictClass = 'woke'; }
  else if (r.margin <= -5) { verdictLabel = 'woke-lean'; verdictClass = 'woke-lean'; }
  else if (r.margin < 5) { verdictLabel = 'balanced'; verdictClass = 'balanced'; }
  else if (r.margin < 15) { verdictLabel = 'traditional-lean'; verdictClass = 'traditional-lean'; }
  else { verdictLabel = 'traditional'; verdictClass = 'traditional'; }
  
  const slug = r.slug;
  
  // Clean up titles that have 'Is X Woke? | VirtueVigil Review' etc
  let displayTitle = r.title;
  if (displayTitle.startsWith('Is ') && displayTitle.includes(' Woke? | VirtueVigil')) {
    displayTitle = displayTitle.replace('Is ', '').replace(' Woke? | VirtueVigil Review', '').replace(' Woke? | VirtueVigil', '');
  }
  if (displayTitle.includes(' Movie Review: Is It Woke? | VirtueVigil')) {
    displayTitle = displayTitle.replace(' Movie Review: Is It Woke? | VirtueVigil', '');
  }
  
  const genre = (r.genre || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const platform = (r.platform || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  
  const tradScore = r.tradScore;
  const wokeScore = r.wokeScore;
  
  entries += `  <hr>

  <h3>#${num}: <a href="/reviews/${slug}/">${displayTitle}</a></h3>
  <div class="listicle-scores">
    <span class="verdict-badge ${verdictClass}">${verdictLabel}</span>
    <span class="mini-score trad">TRAD: ${tradScore}</span>
    <span class="mini-score woke">WOKE: ${wokeScore}</span>
    <span class="mini-score" style="color:var(--accent-amber);">MARGIN: ${r.margin >= 0 ? '+' : ''}${r.margin.toFixed(2)}</span>
  </div>
  <p class="listicle-meta"><strong>Genre:</strong> ${genre}${platform ? ' &bull; <strong>Platform:</strong> ' + platform : ''}</p>
  <p><a href="/reviews/${slug}/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of ${displayTitle}</a></p>
`;
});

// Count statistics
const wokeCount = y2026.filter(r => r.margin < -5).length;
const balancedCount = y2026.filter(r => r.margin >= -5 && r.margin <= 5).length;
const tradCount = y2026.filter(r => r.margin > 5).length;

// Build the full HTML
const html = `<!--
  Social Share Metadata
  Title: Every 2026 Movie Ranked by Woke Score -- VirtueVigil
  Description: We ranked all ${y2026.length} films and shows from 2026 in our database from most woke to most traditional. ${wokeCount} lean woke, ${balancedCount} are balanced, ${tradCount} lean traditional. See the full VVWS ranking.
-->

<article class="listicle-article">
  <div class="listicle-intro">
    <p>2026 is the year Hollywood doubled down -- and audiences finally walked away for good. After the 2025 box office made it painfully clear that traditional films earn the money (Ne Zha 2 at $2.1B, SpongeBob at $1.2B, Mission: Impossible at $1.1B), the industry's response in 2026 has been revealing: keep producing progressive content, but with bigger budgets and louder prestige campaigns. The result is a year of stunning traditional successes standing shoulder to shoulder with some of the most aggressive ideological filmmaking VirtueVigil has ever measured.</p>

    <p>The VirtueVigil Woke Score (VVWS) measures progressive ideological content: identity politics, institutional distrust, progressive sexual framing, and systemic oppression narratives. The Traditional Score measures traditional values: courage, family, faith, sacrifice, moral clarity, and individual agency. The margin between them is what matters. A negative margin means the film pushes progressive ideology. A positive margin means it affirms traditional values.</p>

    <p>Of the ${y2026.length} scored 2026 films and TV seasons in our database, ${wokeCount} lean woke, ${balancedCount} are roughly balanced, and ${tradCount} lean traditional. On raw numbers, 2026 appears more traditional than 2025. But the distribution of cultural attention tells a different story: the most aggressively woke projects are commanding massive marketing budgets and streaming platform pushes, while the most traditional films -- many of them faith-based or military -- are being released with little fanfare and finding their audiences anyway.</p>

    <p>The top of the woke list features Teenage Sex and Death at Camp Miasma, Six The Musical Live!, and The Bride!, three very different projects united by progressive framing. At the traditional end, Exit 8, The Death of Robin Hood, and Beast anchor a year where faith, family, and moral clarity continue to prove their cultural durability. What follows is the definitive ranking -- every 2026 film and show in the VirtueVigil database, ranked from most woke to most traditional. Every entry links to the full review with content warnings for parents and complete category breakdowns.</p>
  </div>

  <hr>

  <h2>Full Rankings: Most Woke to Most Traditional</h2>${entries}
  <hr>

  <h2>What 2026 Is Telling Us</h2>

  <p>The 2026 data confirms a pattern that is now undeniable: traditional films outperform at the box office, but the culture industry does not learn from the market. Faith-based films like A Great Awakening, Daniel and the Fiery Furnace, and Young Washington continue to be produced on modest budgets and find grateful audiences. Military thrillers like Brothers Under Fire, Lucky Strike, and The Brink of War deliver clean, morally grounded action. Family films like PAW Patrol: The Dino Movie, Toy Story 5, and The Super Mario Galaxy Movie prove that parents are hungry for content that does not lecture their children.</p>

  <p>Meanwhile, the prestige pipeline keeps churning: Scarpetta, The Pitt: Season 2, Disclosure Day, and The Bride! represent the kind of high-budget progressive storytelling that dominates awards conversations and critical discourse regardless of audience reception. The gap between what critics celebrate and what audiences actually want has never been wider.</p>

  <p>The most important metric is not the count -- it is the trend. 2026's woke films are not softer than 2025's. They are more aggressive, more polished, and more embedded in major franchises. The traditional films are not retreating either. They are growing in number and in confidence. The culture war is not cooling off. It is escalating. Every film on this list links to its full VirtueVigil review with complete category breakdowns, parental guidance warnings, and detailed scoring. The work continues.</p>

  <hr>

  <p class="listicle-footer"><em>Last updated: October 9, 2026. Scores reflect the VVWS methodology as of this date. Reviews are added weekly. Film counts may increase as new releases are scored.</em></p>
</article>`;

const outPath = '/Users/joestrazza/virtuevigil/lists/every-2026-movie-ranked-by-woke-score/content.html';
fs.mkdirSync('/Users/joestrazza/virtuevigil/lists/every-2026-movie-ranked-by-woke-score', { recursive: true });
fs.writeFileSync(outPath, html, 'utf8');
console.log(`Written: ${outPath}`);
console.log(`Entries: ${y2026.length}`);
console.log(`Woke: ${wokeCount}, Balanced: ${balancedCount}, Traditional: ${tradCount}`);
console.log(`Byte size: ${html.length}`);