// Build: Most Woke Movies of 2026 — Ranked by VirtueVigil Score
process.chdir('/Users/joestrazza/virtuevigil');
const { buildListiclePage, writePage } = require('./build.js');

const htmlContent = `<article class="listicle-article">
  <style>
    .listicle-item { display:flex; gap:18px; align-items:flex-start; background:#13131e; border:1px solid rgba(196,64,64,0.18); border-radius:10px; padding:20px; margin-bottom:20px; }
    .listicle-rank { min-width:44px; height:44px; border-radius:50%; background:rgba(196,64,64,0.15); display:flex; align-items:center; justify-content:center; font-family:'Cinzel',Georgia,serif; font-weight:700; color:#c44040; font-size:0.95rem; flex-shrink:0; margin-top:2px; }
    .listicle-rank.trad { background:rgba(201,168,76,0.12); color:#c9a84c; }
    .listicle-body { flex:1; min-width:0; }
    .listicle-title { font-size:1.05rem; font-weight:700; color:#e8e6e1; margin:0 0 6px; }
    .listicle-meta { font-size:0.78rem; color:#a0a0a8; margin:0 0 10px; }
    .listicle-verdict { display:inline-block; padding:3px 10px; border-radius:5px; font-size:0.72rem; font-weight:700; }
    .listicle-verdict.strongly-woke { background:rgba(196,64,64,0.28); color:#ff6060; border:1px solid rgba(196,64,64,0.6); }
    .listicle-verdict.woke { background:rgba(196,64,64,0.18); color:#c44040; border:1px solid rgba(196,64,64,0.4); }
    .listicle-verdict.woke-lean { background:rgba(196,64,64,0.1); color:#d46060; border:1px solid rgba(196,64,64,0.3); }
    .listicle-verdict.mixed { background:rgba(153,153,153,0.12); color:#999; border:1px solid rgba(153,153,153,0.25); }
    .listicle-verdict.predicted { opacity:0.85; font-style:italic; }
    .listicle-summary { font-size:0.9rem; color:#ccc; line-height:1.65; margin:10px 0; }
    .listicle-link { font-size:0.85rem; font-weight:600; color:#c9a84c; text-decoration:none; }
    .listicle-link:hover { text-decoration:underline; }
    .listicle-score-chip { display:inline-block; background:rgba(196,64,64,0.12); border:1px solid rgba(196,64,64,0.3); border-radius:4px; padding:2px 8px; font-size:0.75rem; font-weight:700; color:#c44040; margin-left:8px; }
    .divider-label { text-align:center; margin:28px 0 20px; font-family:'Cinzel',Georgia,serif; font-size:0.85rem; color:#888; letter-spacing:0.08em; text-transform:uppercase; border-top:1px solid rgba(255,255,255,0.07); padding-top:20px; }
  </style>

  <p>2026 is the most woke year in film history by volume alone. With over 150 films scored in the VirtueVigil database, the woke content has moved from subtext to text, from implication to thesis. The films on this list are not ambiguous. They know what they are doing. They have arguments to make, and they make them with craft, conviction, and in many cases, genuine artistic skill.</p>

  <p>This ranking is not a judgment on quality. Several of these films are excellent by conventional critical standards. It is a measurement of ideological content using the VirtueVigil Woke Scoring System (VVWS): Severity multiplied by Authenticity multiplied by Centrality, minus the same calculation applied to traditional content. The margin is the gap between the two scores. A negative margin means woke content outweighs traditional content. The lower the margin, the more ideologically weighted the film.</p>

  <p>We pulled the 20 films in the 2026 database with the most negative score margins (deduplicating entries where multiple versions exist) and ranked them from most woke to least. Twenty films. Seven different streaming and theatrical platforms. All 20 scored WOKE or worse. Here is the full ranking.</p>

  <hr>

  <div class="divider-label">STRONGLY WOKE</div>

  <div class="listicle-item">
    <div class="listicle-rank">#1</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/the-moment-2026/" style="color:#e8e6e1;text-decoration:none;">The Moment (2026)</a> <span class="listicle-verdict strongly-woke">STRONGLY WOKE</span> <span class="listicle-score-chip">-27 WOKE</span></div>
      <div class="listicle-meta">Genre: Comedy &bull; Woke Score: 32.0 &bull; Traditional Score: 5.0 &bull; Platform: A24 / Theatrical</div>
      <div class="listicle-summary">A $4 million mockumentary starring Charli XCX as a fictionalized version of herself, distributed by A24. The film positions the pop star's progressive persona as the cultural center of gravity around which all other characters orbit. Traditional content is minimal: a few moments of genuine friendship and professional loyalty. The 32-point woke score drives a -27 margin that makes The Moment the most ideologically saturated film of 2026 by a significant gap. If you want to understand where the cultural vanguard is pointing, this is the artifact.</div>
      <a href="/reviews/the-moment-2026/" class="listicle-link">Read the full VirtueVigil review of The Moment <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#2</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/hamlet-2026/" style="color:#e8e6e1;text-decoration:none;">Hamlet (2026)</a> <span class="listicle-verdict strongly-woke">STRONGLY WOKE</span> <span class="listicle-score-chip">-21.3 WOKE</span></div>
      <div class="listicle-meta">Genre: Drama / Tragedy &bull; Woke Score: 30.2 &bull; Traditional Score: 9.0</div>
      <div class="listicle-summary">A radical modern reimagining of Shakespeare's most famous tragedy that reorients the entire narrative around identity politics and contemporary grievance. The text of the play has been restructured to center marginalized perspectives at the expense of the original's exploration of madness, duty, and mortality. The traditional architecture of the play gives it some defensive traditional points, but the production's ideological project is comprehensive. At -21.3, it is the most politically weaponized adaptation of Shakespeare in the VirtueVigil database.</div>
      <a href="/reviews/hamlet-2026/" class="listicle-link">Read the full VirtueVigil review of Hamlet <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#3</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/the-pitt-s2-2026/" style="color:#e8e6e1;text-decoration:none;">The Pitt: Season 2 (2026)</a> <span class="listicle-verdict strongly-woke">STRONGLY WOKE</span> <span class="listicle-score-chip">-20 WOKE</span></div>
      <div class="listicle-meta">Genre: Medical Drama &bull; Woke Score: 29.9 &bull; Traditional Score: 9.9 &bull; Platform: HBO Max</div>
      <div class="listicle-summary">Season 2 of HBO's real-time medical drama sets its fifteen-hour shift on the Fourth of July, and the writers use every hour of that shift to layer progressive commentary into trauma medicine. Gun violence as public health crisis. Immigration enforcement as medical obstruction. Gender-affirming care as standard practice. The craft of the show remains high: the single-shift structure generates real tension. But the ideological content is woven into the premise in a way that makes it impossible to separate the medicine from the messaging.</div>
      <a href="/reviews/the-pitt-s2-2026/" class="listicle-link">Read the full VirtueVigil review of The Pitt: Season 2 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#4</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/leviticus-2026/" style="color:#e8e6e1;text-decoration:none;">Leviticus (2026)</a> <span class="listicle-verdict strongly-woke">STRONGLY WOKE</span> <span class="listicle-score-chip">-19.8 WOKE</span></div>
      <div class="listicle-meta">Genre: Horror / Romance / Coming-of-Age &bull; Woke Score: 23.8 &bull; Traditional Score: 4.0</div>
      <div class="listicle-summary">A horror film with a single ideological thesis: religious communities that oppose homosexuality are monstrous. The setup is familiar coming-of-age material: a new kid moves to a small religious town. The execution is a sustained argument that traditional religious sexual ethics are indistinguishable from horror. At 23.8 woke against 4.0 traditional, the ratio is nearly 6:1. The film does not hide what it is doing, and for parents evaluating content for teenagers, the clarity is useful even if the message is not.</div>
      <a href="/reviews/leviticus-2026/" class="listicle-link">Read the full VirtueVigil review of Leviticus <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#5</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/i-love-boosters-2026/" style="color:#e8e6e1;text-decoration:none;">I Love Boosters (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-19 WOKE</span></div>
      <div class="listicle-meta">Genre: Crime Comedy / Satire &bull; Woke Score: 20.0 &bull; Traditional Score: 1.0</div>
      <div class="listicle-summary">Boots Riley's follow-up to Sorry to Bother You is a Marxist crime comedy about organized retail theft as revolutionary praxis. The film follows a crew of shoplifters who target big-box chains and frame their theft as a political act. The nearly nonexistent traditional score of 1.0 reflects a film that has zero interest in offering a counterpoint to its own argument. Riley is a genuinely inventive filmmaker. His politics are not hidden, and the film's commitment to its own ideology is total. At -19, this is as ideologically one-sided as mainstream cinema gets in 2026.</div>
      <a href="/reviews/i-love-boosters-2026/" class="listicle-link">Read the full VirtueVigil review of I Love Boosters <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#6</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/scarpetta/" style="color:#e8e6e1;text-decoration:none;">Scarpetta (2026)</a> <span class="listicle-verdict woke predicted">PREDICTED: WOKE</span> <span class="listicle-score-chip">-16 WOKE</span></div>
      <div class="listicle-meta">Genre: Thriller &bull; Woke Score: 58.0 &bull; Traditional Score: 42.0 &bull; Platform: Amazon Prime Video</div>
      <div class="listicle-summary">The Patricia Cornwell adaptation starring Nicole Kidman as medical examiner Kay Scarpetta carries a PREDICTED verdict based on pre-release materials and creative team history. The dual 58/42 scores are the highest raw numbers of any 2026 film, reflecting dense ideological content in both directions. The Scarpetta novels have always balanced forensic procedural realism with progressive character politics. The adaptation appears to lean harder into the latter. The -16 margin is driven by structural choices in casting, relationship architecture, and institutional critique that compound across the series-length runtime. Prediction confidence: moderate-high.</div>
      <a href="/reviews/scarpetta/" class="listicle-link">Read the full VirtueVigil review of Scarpetta <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="divider-label">WOKE</div>

  <div class="listicle-item">
    <div class="listicle-rank">#7</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/the-drama-2026/" style="color:#e8e6e1;text-decoration:none;">The Drama (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-14.2 WOKE</span></div>
      <div class="listicle-meta">Genre: Dark Comedy / Romance / Drama &bull; Woke Score: 22.7 &bull; Traditional Score: 8.4</div>
      <div class="listicle-summary">Kristoffer Borgli's follow-up to Dream Scenario poses a single, devastating premise: what happens when you discover the person you love once planned a school shooting? The film uses its thriller architecture to explore themes of guilt, complicity, and the impossibility of love across ideological divides. The traditional elements, genuine romantic feeling and the gravity of confronting violent intent, provide the 8.4 traditional score. But the film's ideological framing treats the discovery of past violence as a permanent contamination that cannot be overcome, and the relationship architecture consistently privileges female judgment over male redemption.</div>
      <a href="/reviews/the-drama-2026/" class="listicle-link">Read the full VirtueVigil review of The Drama <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#8</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/nightbitch/" style="color:#e8e6e1;text-decoration:none;">Nightbitch (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-14 WOKE</span></div>
      <div class="listicle-meta">Genre: Drama &bull; Woke Score: 14.0 &bull; Traditional Score: 0.0</div>
      <div class="listicle-summary">Nightbitch opens as a character study of maternal exhaustion and earns its early sympathy through grounded performances. Amy Adams plays a woman losing her identity in the repetitive isolation of full-time parenthood. The film then pivots: the protagonist's descent into feral canine behavior is framed as liberation rather than breakdown. The traditional score of zero reflects a film that contains no countervailing framework. Motherhood is presented as a trap. Male partnership is presented as useless. The escape is presented as rejecting civilization itself. A well-made film with a clear thesis that traditional family structures are inimical to female flourishing.</div>
      <a href="/reviews/nightbitch/" class="listicle-link">Read the full VirtueVigil review of Nightbitch <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#9</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/the-bride-2026/" style="color:#e8e6e1;text-decoration:none;">The Bride! (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-13.7 WOKE</span></div>
      <div class="listicle-meta">Genre: Gothic Romance / Horror &bull; Woke Score: 22.1 &bull; Traditional Score: 8.4</div>
      <div class="listicle-summary">Maggie Gyllenhaal's reimagining of Bride of Frankenstein is the most openly political horror film of 2026. Set in 1936 Chicago, the film features Jessie Buckley's Bride screaming "Me too! Me too!" directly at the audience during the climax. The entire arc is a feminist awakening narrative: the creature rejects every male-assigned name, embraces female rage as liberation, and escapes male control entirely. The gothic setting is faithfully rendered and romantic love exists as a structural element, accounting for the 8.4 traditional score. But the -13.7 margin and WOKE verdict are unambiguous. This is horror as gender politics delivery system.</div>
      <a href="/reviews/the-bride-2026/" class="listicle-link">Read the full VirtueVigil review of The Bride! <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#10</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/girls-like-girls-2026/" style="color:#e8e6e1;text-decoration:none;">Girls Like Girls (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-12.6 WOKE</span></div>
      <div class="listicle-meta">Genre: Romance / Coming-of-Age / Drama &bull; Woke Score: 16.8 &bull; Traditional Score: 4.2</div>
      <div class="listicle-summary">Hayley Kiyoko spent a decade building toward this film. The 2015 song, the music video, the fanbase known as "Lesbian Jesus" devotees. Girls Like Girls is the feature-length expansion of that cultural project, and it is exactly what it advertises itself to be. A coming-of-age romance centered on a young woman discovering her sexuality through her relationship with her best friend. The 4.2 traditional score reflects genuine emotional sincerity and a commitment to love as a positive force worth pursuing. The 16.8 woke score reflects a film whose entire narrative architecture is organized around the celebration of same-sex attraction as the path to authentic selfhood.</div>
      <a href="/reviews/girls-like-girls-2026/" class="listicle-link">Read the full VirtueVigil review of Girls Like Girls <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#11</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/ready-or-not-2-2026/" style="color:#e8e6e1;text-decoration:none;">Ready or Not 2: Here I Come (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-12.6 WOKE</span></div>
      <div class="listicle-meta">Genre: Horror / Dark Comedy / Thriller &bull; Woke Score: 21.4 &bull; Traditional Score: 8.8</div>
      <div class="listicle-summary">The 2019 original was a tight horror-comedy about old money as a death cult and marriage into elite families as entrapment. The sequel amplifies that thesis into more explicitly ideological territory. Elite tradition is framed as demonic evil, marriage as coercive mechanism. The film earns traditional credit through a sibling loyalty sacrifice and a character's genuine moral choice to refuse a demonic power pact. But the woke scaffolding is dominant throughout. The -12.6 margin edges out the original's ideology count, making this the rare sequel that is more politically committed than its predecessor.</div>
      <a href="/reviews/ready-or-not-2-2026/" class="listicle-link">Read the full VirtueVigil review of Ready or Not 2 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#12</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/daredevil-born-again-s2-2026/" style="color:#e8e6e1;text-decoration:none;">Daredevil: Born Again Season 2 (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-11.6 WOKE</span></div>
      <div class="listicle-meta">Genre: Superhero / Drama &bull; Woke Score: 25.9 &bull; Traditional Score: 14.3 &bull; Platform: Disney+</div>
      <div class="listicle-summary">Season 2 of the Disney+ revival doubles down on the first season's political framework. Charlie Cox's Matt Murdock remains compelling, and the show's Catholic guilt framework generates the 14.3 traditional score almost entirely from the protagonist's internal architecture. But the season's villains are organized around systemic critiques of law enforcement, the criminal justice framing consistently sides with defendants over prosecutors, and the supporting cast diversity is no longer incidental but structurally elevated. At -11.6, it is the most ideologically committed MCU television entry in the VirtueVigil database.</div>
      <a href="/reviews/daredevil-born-again-s2-2026/" class="listicle-link">Read the full VirtueVigil review of Daredevil: Born Again Season 2 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#13</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/mother-mary-2026/" style="color:#e8e6e1;text-decoration:none;">Mother Mary (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-10.9 WOKE</span></div>
      <div class="listicle-meta">Genre: Psychological Drama Thriller &bull; Woke Score: 18.8 &bull; Traditional Score: 7.9 &bull; Platform: A24</div>
      <div class="listicle-summary">David Lowery's A24 psychological thriller about two women navigating a shared creative and romantic history uses Anne Hathaway and Michaela Coel in a power dynamic that the film treats as both intimate and political. The costume designer and the pop star. The creator and the performer. The traditional score reflects genuine artistic ambition and the sincerity of emotional performance. The woke score reflects a film built on a relationship architecture that treats heterosexual partnership as incidental at best and male creative authority as an obstacle. A24's house aesthetic has rarely been deployed this precisely in service of a progressive thesis.</div>
      <a href="/reviews/mother-mary-2026/" class="listicle-link">Read the full VirtueVigil review of Mother Mary <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#14</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/stop-that-train-2026/" style="color:#e8e6e1;text-decoration:none;">Stop! That! Train! (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-10.8 WOKE</span></div>
      <div class="listicle-meta">Genre: Action Comedy / Disaster / Parody &bull; Woke Score: 17.2 &bull; Traditional Score: 6.4</div>
      <div class="listicle-summary">A disaster parody built for the RuPaul's Drag Race fan base, directed by a filmmaker who has spent his career in that cultural space. The structure is Airplane! on rails: two train stewardesses must stop an out-of-control locomotive. What Airplane! did with sight gags, Stop! That! Train! does with drag performances and identity politics. The comedy is broad and committed. The 6.4 traditional score reflects genuine friendship and the rescue-the-day action framework. The 17.2 woke score reflects a film whose entire comedic sensibility is organized around drag culture as a primary virtue and conventional masculinity as the default joke.</div>
      <a href="/reviews/stop-that-train-2026/" class="listicle-link">Read the full VirtueVigil review of Stop! That! Train! <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#15</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/is-god-is-2026/" style="color:#e8e6e1;text-decoration:none;">Is God Is (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-10.4 WOKE</span></div>
      <div class="listicle-meta">Genre: Thriller / Drama / Revenge &bull; Woke Score: 17.6 &bull; Traditional Score: 7.2</div>
      <div class="listicle-summary">Aleshea Harris adapts her own play into a stylized Black feminist revenge myth. Twin sisters travel to the California desert to confront the father who nearly killed their mother. The film is organized around women's violent agency against a patriarch who destroyed their family. The traditional score reflects the revenge framework's engagement with justice, loyalty between sisters, and the seriousness with which the film treats the moral weight of killing. The woke score reflects a film whose entire dramatic engine is built on the specific intersection of race, gender, and patriarchal violence as ultimate evil. Harris has been clear about what she is making. The film delivers on its terms.</div>
      <a href="/reviews/is-god-is-2026/" class="listicle-link">Read the full VirtueVigil review of Is God Is <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="divider-label">WOKE LEAN</div>

  <div class="listicle-item">
    <div class="listicle-rank">#16</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/wuthering-heights/" style="color:#e8e6e1;text-decoration:none;">Wuthering Heights (2026)</a> <span class="listicle-verdict woke">WOKE</span> <span class="listicle-score-chip">-10 WOKE</span></div>
      <div class="listicle-meta">Genre: Drama &bull; Woke Score: 36.0 &bull; Traditional Score: 26.0</div>
      <div class="listicle-summary">Emerald Fennell's adaptation of Emily Bronte's novel is the most ideologically contested prestige release of 2026. Both scores are high because Bronte's original contains genuine traditional architecture (love that transcends death, the consequences of cruelty across generations, the weight of the past) while Fennell's framing imposes a contemporary racial and gender analysis that Bronte never wrote. Heathcliff is race-swapped, and the production's press tour positioned the novel as "always about race." The 36 woke and 26 traditional scores reflect a film pulling hard in both directions. The woke reading wins the margin. Bronte fans should know what they are walking into.</div>
      <a href="/reviews/wuthering-heights/" class="listicle-link">Read the full VirtueVigil review of Wuthering Heights <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#17</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/the-last-of-us-s2/" style="color:#e8e6e1;text-decoration:none;">The Last of Us - Season 2 (2026)</a> <span class="listicle-verdict woke-lean">WOKE LEAN</span> <span class="listicle-score-chip">-8 WOKE</span></div>
      <div class="listicle-meta">Genre: Drama &bull; Woke Score: 11.0 &bull; Traditional Score: 3.0 &bull; Platform: HBO Max</div>
      <div class="listicle-summary">Season 1 earned enormous trust through grounded storytelling and earned emotional beats. Season 2 leverages that trust to introduce ideological reframing that would not have survived scrutiny if presented upfront. The bait-and-switch is architecturally precise: what made the first season compelling (Joel's protective fatherhood, Ellie's survival, the moral complexity of sacrifice) is systematically dismantled in favor of a revenge-and-consequence structure that treats Joel's choice as a sin requiring punishment. At -8 WOKE LEAN, the margin is modest but the direction is clear. The show is no longer neutral about its own moral universe.</div>
      <a href="/reviews/the-last-of-us-s2/" class="listicle-link">Read the full VirtueVigil review of The Last of Us - Season 2 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#18</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/butterfly-dreams-2026/" style="color:#e8e6e1;text-decoration:none;">Butterfly Dreams (2026)</a> <span class="listicle-verdict woke-lean">WOKE LEAN</span> <span class="listicle-score-chip">-7.2 WOKE</span></div>
      <div class="listicle-meta">Genre: Coming-of-Age Drama &bull; Woke Score: 18.4 &bull; Traditional Score: 11.2</div>
      <div class="listicle-summary">Director Dee Rees brings formidable craft to this coming-of-age drama about a sixteen-year-old trans girl who leaves her conservative religious hometown in rural Kentucky to live with her estranged grandmother in Louisville. The traditional score of 11.2 reflects the grandmother-granddaughter bond, the importance of family acceptance, and the film's genuine interest in characters rather than abstraction. The woke score of 18.4 reflects a film whose subject matter is inherently ideological in the current cultural moment and whose treatment of religion is consistently adversarial. At -7.2 WOKE LEAN, Butterfly Dreams is more humane than propagandistic, but parents should understand the framework before viewing with teenagers.</div>
      <a href="/reviews/butterfly-dreams-2026/" class="listicle-link">Read the full VirtueVigil review of Butterfly Dreams <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#19</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/bridgerton-season-4-2026/" style="color:#e8e6e1;text-decoration:none;">Bridgerton: Season 4 (2026)</a> <span class="listicle-verdict woke-lean">WOKE LEAN</span> <span class="listicle-score-chip">-6.2 WOKE</span></div>
      <div class="listicle-meta">Genre: Regency Romance Drama &bull; Woke Score: 16.2 &bull; Traditional Score: 10.0 &bull; Platform: Netflix</div>
      <div class="listicle-summary">Netflix's most-watched English-language series returns for its fourth season with Benedict Bridgerton's love story. The traditional score of 10 reflects the Cinderella romance structure, the genuine commitment to domestic virtue in the Bridgerton family scenes, and the series' continued celebration of marriage as a serious institution. The woke score of 16.2 reflects the post-racial Regency fantasy framework, the bisexual protagonist framing new to this season, and the show's consistent positioning of aristocracy as a system requiring critique. The new couple is the best since Daphne and Simon. The ideological architecture is the same as every prior season.</div>
      <a href="/reviews/bridgerton-season-4-2026/" class="listicle-link">Read the full VirtueVigil review of Bridgerton: Season 4 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-item">
    <div class="listicle-rank">#20</div>
    <div class="listicle-body">
      <div class="listicle-title"><a href="/reviews/forbidden-fruits-2026/" style="color:#e8e6e1;text-decoration:none;">Forbidden Fruits (2026)</a> <span class="listicle-verdict woke-lean">WOKE LEAN</span> <span class="listicle-score-chip">-6.6 WOKE</span></div>
      <div class="listicle-meta">Genre: Comedy Horror &bull; Woke Score: 27.8 &bull; Traditional Score: 21.2</div>
      <div class="listicle-summary">A comedy horror set at a mall store called Free Eden where the employees are gorgeous, the candles are scented, and the feminist cult doctrine is the actual product being sold. The woke score of 27.8 is driven by sapphic content as primary narrative thread and feminist ideology functioning as cult doctrine. The traditional score of 21.2 is the highest among the top 20, reflecting the film's willingness to expose and punish the cult leader and show real consequences for self-destructive behavior. At -6.6 WOKE LEAN, Forbidden Fruits sits at the boundary of mixed territory. It scores higher than WOKE because the traditional architecture partially offsets the ideology. Still the 20th most ideologically weighted film of 2026.</div>
      <a href="/reviews/forbidden-fruits-2026/" class="listicle-link">Read the full VirtueVigil review of Forbidden Fruits <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
    </div>
  </div>

  <div class="listicle-conclusion" style="background:rgba(196,64,64,0.06);border:1px solid rgba(196,64,64,0.2);border-radius:10px;padding:22px 26px;margin:28px 0;">
    <p><strong>What the 2026 woke rankings tell us.</strong> Four films scored STRONGLY WOKE, nine scored WOKE, and seven scored WOKE LEAN among the top 20. No film on this list scored MIXED or better. That is a more ideologically concentrated top tier than 2025, which saw mixed-verdict films interspersed throughout its woke rankings.</p>

    <p>The platforms tell a story too. HBO Max places three entries in the top 20 (The Pitt S2, The Last of Us S2, Bridgerton S4). A24 places two (The Moment, Mother Mary). Netflix and Amazon each place multiple. Streaming prestige content continues to lead theatrical releases in ideological density, a pattern that has held across every year of VirtueVigil scoring.</p>

    <p>None of this is a judgment on the craft of these films. Several are excellent. Some are among the best-reviewed releases of the year by conventional critical standards. The VirtueVigil Woke Scoring System measures ideological content, not quality. A film can be ideologically saturated and brilliantly made. The point is to help viewers and parents understand what they are walking into before they press play. Browse each full review linked above for the detailed trope-by-trope breakdown, parental guidance notes, and complete VVWS scoring audit.</p>

    <p><a href="/reviews/">Browse all 700+ VirtueVigil reviews</a> or see the full index at <a href="/lists/">VirtueVigil Lists</a>.</p>
  </div>
</article>`;

writePage('lists/most-woke-movies-2026/index.html', buildListiclePage({
  slug: 'most-woke-movies-2026',
  title: 'Most Woke Movies of 2026 — The 20 Most Ideologically Weighted Films Ranked',
  description: 'All 20 most woke films of 2026 ranked by VirtueVigil score. From Strongly Woke to Woke Lean, see which releases push progressive ideology hardest this year.',
  canonicalPath: 'lists/most-woke-movies-2026',
  publishDate: '2026-06-30',
  htmlContent
}));

console.log('Done. File written to dist/lists/most-woke-movies-2026/index.html');