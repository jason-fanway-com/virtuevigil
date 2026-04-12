// Build: Every 2026 Horror Movie Ranked by Woke Score
process.chdir('/Users/joestrazza/virtuevigil');
const { buildListiclePage, writePage } = require('./build.js');

const htmlContent = `<article class="listicle-article">
  <style>
    .horror-item { display:flex; gap:18px; align-items:flex-start; background:#13131e; border:1px solid rgba(196,64,64,0.18); border-radius:10px; padding:20px; margin-bottom:20px; }
    .horror-rank { min-width:44px; height:44px; border-radius:50%; background:rgba(196,64,64,0.15); display:flex; align-items:center; justify-content:center; font-family:'Cinzel',Georgia,serif; font-weight:700; color:#c44040; font-size:0.95rem; flex-shrink:0; margin-top:2px; }
    .horror-rank.trad { background:rgba(201,168,76,0.12); color:#c9a84c; }
    .horror-body { flex:1; min-width:0; }
    .horror-title { font-size:1.05rem; font-weight:700; color:#e8e6e1; margin:0 0 6px; }
    .horror-meta { font-size:0.78rem; color:#a0a0a8; margin:0 0 10px; }
    .horror-verdict { display:inline-block; padding:3px 10px; border-radius:5px; font-size:0.72rem; font-weight:700; }
    .horror-verdict.woke { background:rgba(196,64,64,0.15); color:#c44040; border:1px solid rgba(196,64,64,0.4); }
    .horror-verdict.strongly-woke { background:rgba(196,64,64,0.25); color:#ff6060; border:1px solid rgba(196,64,64,0.6); }
    .horror-verdict.woke-lean { background:rgba(196,64,64,0.1); color:#d46060; border:1px solid rgba(196,64,64,0.3); }
    .horror-verdict.trad-lean { background:rgba(201,168,76,0.1); color:#c9a84c; border:1px solid rgba(201,168,76,0.3); }
    .horror-verdict.trad { background:rgba(201,168,76,0.15); color:#c9a84c; border:1px solid rgba(201,168,76,0.4); }
    .horror-verdict.strongly-trad { background:rgba(201,168,76,0.25); color:#d4aa50; border:1px solid rgba(201,168,76,0.6); }
    .horror-verdict.predicted { opacity:0.85; font-style:italic; }
    .horror-summary { font-size:0.9rem; color:#ccc; line-height:1.65; margin:10px 0; }
    .horror-link { font-size:0.85rem; font-weight:600; color:#c9a84c; text-decoration:none; }
    .horror-link:hover { text-decoration:underline; }
    .horror-score-chip { display:inline-block; background:rgba(196,64,64,0.12); border:1px solid rgba(196,64,64,0.3); border-radius:4px; padding:2px 8px; font-size:0.75rem; font-weight:700; color:#c44040; margin-left:8px; }
    .horror-score-chip.trad { background:rgba(201,168,76,0.12); border-color:rgba(201,168,76,0.3); color:#c9a84c; }
    .divider-label { text-align:center; margin:28px 0 20px; font-family:'Cinzel',Georgia,serif; font-size:0.85rem; color:#888; letter-spacing:0.08em; text-transform:uppercase; border-top:1px solid rgba(255,255,255,0.07); padding-top:20px; }
  </style>

  <p>Horror is the most ideologically saturated genre in Hollywood right now. The genre has always reflected what a culture fears, and contemporary horror has made its fears very clear: traditional families, faith, masculine authority, and suburban normalcy. At the same time, 2026 has produced a surprising number of horror films that reject that template entirely, choosing atmosphere, creature features, and survival mechanics over social lectures.</p>

  <p>We pulled every 2026 horror film in the VirtueVigil database and ranked them by woke score, highest to lowest. The result is a complete picture of where horror stands this year. Three films scored WOKE or worse. Eight scored TRADITIONAL LEAN or better. Two hit STRONGLY TRADITIONAL territory. Here is the full ranking.</p>

  <hr>

  <div class="divider-label">Most Woke</div>

  <div class="horror-item">
    <div class="horror-rank">#1</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/forbidden-fruits-2026/" style="color:#e8e6e1;text-decoration:none;">Forbidden Fruits (2026)</a> <span class="horror-verdict woke-lean">WOKE LEAN</span> <span class="horror-score-chip">-6.6 WOKE</span></div>
      <div class="horror-meta">Genre: Comedy Horror &bull; Woke Score: 27.8 &bull; Traditional Score: 21.2</div>
      <div class="horror-summary">Forbidden Fruits leads the 2026 horror field in raw woke score at 27.8, built around a feminist ideology functioning as cult doctrine and sapphic content as a primary narrative thread. The saving grace is that the cult leader is ultimately exposed and punished, and the film shows consequences for self-destructive behavior, which pulls the traditional score up to 21.2. The net margin is -6.6 WOKE. It scores WOKE LEAN rather than WOKE because the traditional architecture partially offsets the ideology. Still the most ideologically loaded horror release of 2026 so far.</div>
      <a href="/reviews/forbidden-fruits-2026/" class="horror-link">Read the full VirtueVigil review of Forbidden Fruits <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank">#2</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/the-bride-2026/" style="color:#e8e6e1;text-decoration:none;">The Bride! (2026)</a> <span class="horror-verdict woke">WOKE</span> <span class="horror-score-chip">-14 WOKE</span></div>
      <div class="horror-meta">Genre: Gothic Horror &bull; Woke Score: 22.1 &bull; Traditional Score: 8.4</div>
      <div class="horror-summary">Maggie Gyllenhaal's reimagining of Bride of Frankenstein is the most nakedly political horror film of the year. The climax features Jessie Buckley's Bride screaming "Me too! Me too!" directly at the audience. The entire arc is a feminist awakening narrative in which the creature rejects every male-assigned name, embraces female rage as liberation, and escapes male control entirely. The gothic setting is faithfully rendered and romantic love exists as a structural element, which accounts for the 8.4 traditional score. But the -14 margin and WOKE verdict are unambiguous. This is horror as gender politics delivery system.</div>
      <a href="/reviews/the-bride-2026/" class="horror-link">Read the full VirtueVigil review of The Bride! <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank">#3</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/ready-or-not-2-2026/" style="color:#e8e6e1;text-decoration:none;">Ready or Not 2: Here I Come (2026)</a> <span class="horror-verdict woke">WOKE</span> <span class="horror-score-chip">-12.6 WOKE</span></div>
      <div class="horror-meta">Genre: Horror / Dark Comedy / Thriller &bull; Woke Score: 21.4 &bull; Traditional Score: 8.8</div>
      <div class="horror-summary">The sequel amplifies the original's anti-elite messaging into something more explicitly ideological. Elite tradition is framed as demonic evil, and marriage is presented as an institutional trap and coercive mechanism. The film does earn some traditional credit: a sibling loyalty sacrifice drives a key story beat, and a character's refusal of a demonic power pact reads as a genuine moral choice. But the woke scaffolding is dominant throughout, landing the sequel at -12.6 WOKE and a WOKE verdict that edges out the original's ideology count.</div>
      <a href="/reviews/ready-or-not-2-2026/" class="horror-link">Read the full VirtueVigil review of Ready or Not 2 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="divider-label">Mixed Territory</div>

  <div class="horror-item">
    <div class="horror-rank trad">#4</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/return-to-silent-hill-2026/" style="color:#e8e6e1;text-decoration:none;">Return to Silent Hill (2026)</a> <span class="horror-verdict trad-lean">TRADITIONAL LEAN</span> <span class="horror-score-chip trad">+1 TRAD</span></div>
      <div class="horror-meta">Genre: Horror &bull; Woke Score: 15 &bull; Traditional Score: 16</div>
      <div class="horror-summary">Return to Silent Hill sits at the narrowest possible margin in the database: +1 TRAD. Both woke and traditional scores are elevated, reflecting a film that carries real ideological pressure from multiple directions. The Silent Hill franchise has always built its horror from guilt, punishment, and the weight of past choices, which generates traditional tropes naturally. But 2026's entry has not avoided contemporary ideology entirely. It lands just barely on the traditional side of neutral. If you want Silent Hill horror without high woke exposure, this is technically the choice, but the margin offers limited comfort.</div>
      <a href="/reviews/return-to-silent-hill-2026/" class="horror-link">Read the full VirtueVigil review of Return to Silent Hill <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#5</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/send-help-2026/" style="color:#e8e6e1;text-decoration:none;">Send Help (2026)</a> <span class="horror-verdict trad-lean">TRADITIONAL LEAN</span> <span class="horror-score-chip trad">+7 TRAD</span></div>
      <div class="horror-meta">Genre: Horror &bull; Woke Score: 15 &bull; Traditional Score: 22</div>
      <div class="horror-summary">Send Help carries an elevated woke score of 15 alongside a substantial traditional score of 22, producing a +7 TRAD margin that places it comfortably in TRADITIONAL LEAN territory. The woke score reflects genre-standard ideology present in much modern horror, but the traditional architecture is strong enough to offset it clearly. The film works as a horror recommendation for audiences who want traditional values present and dominant in the story without requiring a squeaky-clean ideological score sheet.</div>
      <a href="/reviews/send-help-2026/" class="horror-link">Read the full VirtueVigil review of Send Help <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#6</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/28-years-later-the-bone-temple-2026/" style="color:#e8e6e1;text-decoration:none;">28 Years Later: The Bone Temple (2026)</a> <span class="horror-verdict trad-lean">TRADITIONAL LEAN</span> <span class="horror-score-chip trad">+4 TRAD</span></div>
      <div class="horror-meta">Genre: Horror / Post-Apocalyptic &bull; Woke Score: 10 &bull; Traditional Score: 14.3</div>
      <div class="horror-summary">The second film in Danny Boyle and Alex Garland's 28 Years Later trilogy scores TRADITIONAL LEAN at +4, the result of two competing currents. The male protagonist is diminished and a female character serves as the film's moral compass, both flagged woke signals. But the traditional architecture holds: redemption through compassion drives a key character arc, and evil is defined by specific actions rather than group identity or systemic critique. The post-apocalyptic survival framework generates traditional values organically. A solid horror pick for conservative audiences comfortable with some woke friction in exchange for strong narrative craft.</div>
      <a href="/reviews/28-years-later-the-bone-temple-2026/" class="horror-link">Read the full VirtueVigil review of 28 Years Later: The Bone Temple <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#7</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/scream-7/" style="color:#e8e6e1;text-decoration:none;">Scream 7 (2026)</a> <span class="horror-verdict trad-lean">TRADITIONAL LEAN</span> <span class="horror-score-chip trad">+8.84 TRAD</span></div>
      <div class="horror-meta">Genre: Horror &bull; Woke Score: 9.5 &bull; Traditional Score: 18.3</div>
      <div class="horror-summary">Scream 7 threads the needle the franchise has always attempted: meta-commentary on horror conventions while maintaining audience investment in real stakes. The LGBTQ+ normalization and progressive meta-commentary generate the 9.5 woke score. But the traditional core is genuine: motherhood and family protection anchor the protagonist's motivation, and self-sacrifice drives the climax's emotional weight. At +8.84 TRAD and TRADITIONAL LEAN, Scream 7 is a franchise entry that conservative horror fans can engage with. The woke signals are present but they do not dominate the story's moral architecture.</div>
      <a href="/reviews/scream-7/" class="horror-link">Read the full VirtueVigil review of Scream 7 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#8</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/scary-movie-6-2026/" style="color:#e8e6e1;text-decoration:none;">Scary Movie 6 (2026)</a> <span class="horror-verdict trad-lean">TRADITIONAL LEAN</span> <span class="horror-score-chip trad">+6 TRAD</span></div>
      <div class="horror-meta">Genre: Horror Parody / Comedy &bull; Woke Score: 8.4 &bull; Traditional Score: 14.7</div>
      <div class="horror-summary">Scary Movie 6 is genuinely unusual on this list. The film includes a non-binary character and satirizes racial politics in a Get Out parody segment, which generates the 8.4 woke score. But the traditional score of 14.7 is built on explicit mockery of pronoun culture and gender ideology as a core comedic target, and anti-cancel-culture positioning as a central part of the film's brand identity. This is a parody that lampoons woke culture from the inside, using horror genre conventions as the vehicle. The result is +6 TRAD and TRADITIONAL LEAN, a film that will land differently depending on how you feel about parody as political commentary.</div>
      <a href="/reviews/scary-movie-6-2026/" class="horror-link">Read the full VirtueVigil review of Scary Movie 6 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="divider-label">Solidly Traditional</div>

  <div class="horror-item">
    <div class="horror-rank trad">#9</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/they-will-kill-you/" style="color:#e8e6e1;text-decoration:none;">They Will Kill You (2026)</a> <span class="horror-verdict trad">TRADITIONAL</span> <span class="horror-score-chip trad">+16.2 TRAD</span></div>
      <div class="horror-meta">Genre: Action / Comedy / Horror &bull; Woke Score: 7.7 &bull; Traditional Score: 23.9</div>
      <div class="horror-summary">They Will Kill You is one of the pleasant surprises in 2026's horror lineup. A female-led action duo generates a mild woke signal, and wealthy villains carry some class-critique potential. But family loyalty and self-sacrifice are the dominant traditional tropes, and they are executed with genuine conviction. The action-comedy-horror blend dilutes any ideological messaging by keeping the tone grounded in genre entertainment. At +16.2 TRAD and a flat TRADITIONAL verdict, it's a clean recommendation for horror fans who want a contemporary film without the politics baggage.</div>
      <a href="/reviews/they-will-kill-you/" class="horror-link">Read the full VirtueVigil review of They Will Kill You <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#10</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/the-strangers-chapter-3/" style="color:#e8e6e1;text-decoration:none;">The Strangers: Chapter 3 (2026)</a> <span class="horror-verdict trad-lean">TRADITIONAL LEAN</span> <span class="horror-score-chip trad">+6 TRAD</span></div>
      <div class="horror-meta">Genre: Horror &bull; Woke Score: 5 &bull; Traditional Score: 11</div>
      <div class="horror-summary">The Strangers franchise has always operated in the purest horror tradition: strangers kill people in isolated locations because they can. Chapter 3 continues that tradition with a 5.0 woke score and an 11 traditional score, landing at +6 TRAD. No substantial ideological content on either side. This is survival horror built on competence, fear, and the terrifying randomness of violence. For audiences who want horror without political messaging in any direction, Chapter 3 is a clean entry point into a franchise that respects the basics of what the genre is supposed to do.</div>
      <a href="/reviews/the-strangers-chapter-3/" class="horror-link">Read the full VirtueVigil review of The Strangers: Chapter 3 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#11</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/backrooms-2026/" style="color:#e8e6e1;text-decoration:none;">Backrooms (2026)</a> <span class="horror-verdict trad-lean predicted">PREDICTED: TRADITIONAL LEAN</span> <span class="horror-score-chip trad">+14.44 TRAD</span></div>
      <div class="horror-meta">Genre: Horror / Supernatural / Sci-Fi &bull; Woke Score: 4.9 &bull; Traditional Score: 19.3</div>
      <div class="horror-summary">Kane Pixels' A24 adaptation of the Backrooms viral horror universe carries a PREDICTED verdict ahead of its May 29 release. Based on pre-release materials and the creator's track record, VirtueVigil scored it at +14.44 TRAD and TRADITIONAL LEAN. The horror is atmospheric and psychological, built on rescue mission as moral imperative and practical competence as the survival mechanic. The A24 distribution flag generates a mild woke signal, but the content itself shows no ideological scaffolding. Pure liminal space horror without political commentary. The prediction carries moderate-high confidence and will be updated post-release.</div>
      <a href="/reviews/backrooms-2026/" class="horror-link">Read the full VirtueVigil review of Backrooms <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#12</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/undertone-2026/" style="color:#e8e6e1;text-decoration:none;">Undertone (2026)</a> <span class="horror-verdict trad">TRADITIONAL</span> <span class="horror-score-chip trad">+18 TRAD</span></div>
      <div class="horror-meta">Genre: Supernatural Horror &bull; Woke Score: 3.7 &bull; Traditional Score: 22</div>
      <div class="horror-summary">Undertone is the most theologically traditional horror film of 2026. Catholic faith functions as the film's structural horror architecture, and maternal caregiving as moral obligation drives the protagonist's motivation and choices. The woke signals are notable: the protagonist schedules an abortion appointment, and she lives independently without a partner present. These are genuine woke friction points. But the traditional architecture is dominant at 22 trad versus 3.7 woke, and the overall moral framework is built on faith and sacrifice rather than progressive liberation. At +18 TRAD, it is a strong pick for horror fans who want faith-based horror with real theological weight.</div>
      <a href="/reviews/undertone-2026/" class="horror-link">Read the full VirtueVigil review of Undertone <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#13</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/the-yeti-2026/" style="color:#e8e6e1;text-decoration:none;">The Yeti (2026)</a> <span class="horror-verdict trad predicted">PREDICTED: TRADITIONAL</span> <span class="horror-score-chip trad">+17.62 TRAD</span></div>
      <div class="horror-meta">Genre: Horror / Monster / Survival Thriller &bull; Woke Score: 1.6 &bull; Traditional Score: 19.2</div>
      <div class="horror-summary">Set in the Alaskan wilderness, The Yeti delivers monster horror anchored by family loyalty and man-versus-nature survival mechanics. Two adult children search for their missing fathers in a Yeti's territory. The rescue mission driven by family loyalty is the traditional core. The female lead generates a mild signal, and the oil tycoon as an implicit environmental villain scores low-centrality woke points. But at 1.56 woke versus 19.18 trad, the margin is decisive. Arriving as a PREDICTED: TRADITIONAL with high confidence, The Yeti is a creature feature for audiences who want genre thrills without ideological content.</div>
      <a href="/reviews/the-yeti-2026/" class="horror-link">Read the full VirtueVigil review of The Yeti <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#14</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/hunting-matthew-nichols-2026/" style="color:#e8e6e1;text-decoration:none;">Hunting Matthew Nichols (2026)</a> <span class="horror-verdict trad">TRADITIONAL</span> <span class="horror-score-chip trad">+19 TRAD</span></div>
      <div class="horror-meta">Genre: Horror / Found Footage &bull; Woke Score: 1.9 &bull; Traditional Score: 21.3</div>
      <div class="horror-summary">A found footage horror film built on sibling loyalty and family duty as the investigator's central motivation. Two mild woke signals are present: a female lead investigator and a subtle critique of male-dominated institutions. But with a woke score of just 1.9 and a traditional score of 21.28, the margin is +19 TRAD and the TRADITIONAL verdict is firm. Sibling loyalty and perseverance through fear and uncertainty are the emotional engine. If you want found footage horror that takes family seriously as a value rather than a burden, Hunting Matthew Nichols delivers.</div>
      <a href="/reviews/hunting-matthew-nichols-2026/" class="horror-link">Read the full VirtueVigil review of Hunting Matthew Nichols <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="divider-label">Strongly Traditional</div>

  <div class="horror-item">
    <div class="horror-rank trad">#15</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/the-mummy-2026/" style="color:#e8e6e1;text-decoration:none;">The Mummy (2026)</a> <span class="horror-verdict strongly-trad predicted">PREDICTED: STRONGLY TRADITIONAL</span> <span class="horror-score-chip trad">+22.08 TRAD</span></div>
      <div class="horror-meta">Genre: Horror / Supernatural &bull; Woke Score: 2.0 &bull; Traditional Score: 24.1</div>
      <div class="horror-summary">Lee Cronin's Mummy reboot carries a PREDICTED: STRONGLY TRADITIONAL verdict ahead of its April 17 theatrical release. The nuclear family as the horror's emotional core and the father as provider and protector are the dominant traditional tropes, both scored at maximum centrality. James Wan and Jason Blum as producers, New Line Cinema distribution, and Cronin's track record on Evil Dead Rise all support high confidence in the prediction. The woke signals are minimal: an ambiguous expert role for a female supporting cast member and an Exotic Supernatural Villain archetype. At +22.08 TRAD, this is the best pre-release traditional horror pick of the spring.</div>
      <a href="/reviews/the-mummy-2026/" class="horror-link">Read the full VirtueVigil review of The Mummy <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="horror-item">
    <div class="horror-rank trad">#16</div>
    <div class="horror-body">
      <div class="horror-title"><a href="/reviews/exit-8-2026/" style="color:#e8e6e1;text-decoration:none;">Exit 8 (2026)</a> <span class="horror-verdict strongly-trad predicted">PREDICTED: STRONGLY TRADITIONAL</span> <span class="horror-score-chip trad">+30.94 TRAD</span></div>
      <div class="horror-meta">Genre: Psychological Horror / Mystery / Drama &bull; Woke Score: 0.7 &bull; Traditional Score: 31.6</div>
      <div class="horror-summary">Exit 8 leads 2026 horror in traditional score by a wide margin: +30.94 TRAD, with 31.64 traditional points against 0.7 woke. The Japanese psychological horror film, based on the viral indie game, is built on male accountability and moral growth as the central theme, and fatherhood as the highest masculine responsibility. The single woke signal is male shaming used as narrative incitement to push the protagonist toward growth. A Cannes premiere with a standing ovation validates the craft. This is as close to a pure traditional horror film as the genre produces in 2026: a man confronting who he is supposed to be, in a space that will not let him leave until he becomes it.</div>
      <a href="/reviews/exit-8-2026/" class="horror-link">Read the full VirtueVigil review of Exit 8 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-conclusion" style="background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);border-radius:10px;padding:22px 26px;margin:28px 0;">
    <p>The 2026 horror landscape is more ideologically divided than the genre has been in years. Three films score WOKE or WOKE LEAN, all in the top three by woke score. But the bulk of the year's horror output is sitting in TRADITIONAL LEAN or better territory, with two films hitting STRONGLY TRADITIONAL. The genre's traditional instincts, survival, family protection, faith, and individual courage in the face of external evil, are still producing strong work in 2026. You just have to know where to look. Browse VirtueVigil's full horror database for complete VVWS scores, trope audits, and parental guidance on every title. <a href="/reviews/">Browse all reviews</a>.</p>
  </div>
</article>`;

writePage('lists/horror-movies-2026-woke-ranking/index.html', buildListiclePage({
  slug: 'horror-movies-2026-woke-ranking',
  title: 'Every 2026 Horror Movie Ranked by Woke Score',
  description: 'VirtueVigil scores all 16 reviewed 2026 horror films by woke score. From Strongly Woke to Strongly Traditional, here is the complete 2026 horror ranking.',
  canonicalPath: 'lists/horror-movies-2026-woke-ranking',
  publishDate: '2026-04-12',
  htmlContent
}));

console.log('Done. File written to dist/lists/horror-movies-2026-woke-ranking/index.html');
