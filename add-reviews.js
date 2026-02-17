const fs = require('fs');
const path = require('path');

const newReviews = [
  {
    id: "stranger-things",
    slug: "stranger-things",
    title: "Stranger Things",
    year: 2025,
    type: "series",
    platform: "Netflix",
    genre: "Sci-Fi, Horror",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "18 min",
    poster: "/images/posters/stranger-things.jpg",
    verdict: "WOKE",
    wokeScore: 13,
    tradScore: 8,
    authIndex: 62,
    scoreMargin: "-5 WOKE",
    wokeTrap: {
      present: true,
      degree: "severe",
      explanation: "Stranger Things is the textbook multi-season woke trap. Seasons 1 and 2 are practically a love letter to traditional America. Small-town Indiana. A nuclear family torn apart by supernatural forces. Boys on bikes solving mysteries through courage and loyalty. Then it started to shift. By Season 5, Will's coming-out scene became the emotional centerpiece of the final season. His acceptance of his gay identity literally unlocks telekinetic superpowers. The trap works because the first two seasons are genuinely excellent television that earns deep audience investment.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: true,
      explanation: "Stranger Things is the textbook multi-season woke trap. Seasons 1-2 earn massive goodwill with traditional values, then the ideology kicks in gradually through Seasons 3-5 until Will's coming-out is the emotional centerpiece of the finale."
    },
    creative_team: {
      director: { name: "Matt & Ross Duffer", ideology: "PROGRESSIVE", profile: "Twin brothers who created and controlled the series across all five seasons. Their progressive content escalates methodically, and they confirmed Will's sexuality was always the planned emotional culmination." },
      writer: { name: "Matt & Ross Duffer", profile: "Also serve as primary writers across all seasons." },
      lead_producer: { name: "Shawn Levy", company: "21 Laps Entertainment" },
      composer: { name: "Kyle Dixon & Michael Stein" },
      top_cast: [
        { name: "Millie Bobby Brown", role: "Eleven" },
        { name: "Finn Wolfhard", role: "Mike Wheeler" },
        { name: "Winona Ryder", role: "Joyce Byers" },
        { name: "David Harbour", role: "Jim Hopper" },
        { name: "Noah Schnapp", role: "Will Byers" }
      ],
      prediction: { verdict: "WOKE", confidence: "high" }
    },
    fidelity_casting: {
      score: "FORCED DIVERSITY",
      summary: "Cast diversity increased significantly in later seasons beyond what 1980s rural Indiana demographics would support.",
      detailed_analysis: "The core cast is appropriate for 1980s Hawkins. Later seasons add characters and expand diversity beyond the demographic reality of rural Indiana in the 1980s. Robin Buckley was specifically created as an LGBTQ vehicle. By Season 5, the cast and ideological framing reflect Netflix progressive content standards more than period accuracy."
    },
    summary: {
      overall: "There was a time when Stranger Things felt like a miracle. In the summer of 2016, Netflix dropped this weird little show about a missing kid in small-town Indiana, and it captured something audiences had been starving for. It was nostalgia for a kind of storytelling that Hollywood had largely abandoned. Kids solving problems. Fathers protecting families. Communities pulling together. Good and evil clearly defined.\n\nSeason 1 is a near-perfect piece of television from a traditional values perspective. Joyce Byers is a mother whose entire existence collapses into a single primal mission: find her son. Jim Hopper channels his grief into protecting someone else's child. Mike, Dustin, and Lucas are brave, loyal, and resourceful in the way that boys in adventure stories used to be. And Eleven earns her strength through suffering and sacrifice, not through a girlboss speech.\n\nThen comes Season 3, and the ground starts to shift. Robin Buckley comes out as a lesbian in the finale. Season 4 leans harder into Robin's sexuality and Will's unspoken feelings for Mike. By Season 5, the transformation is complete. Will's coming-out scene becomes the emotional centerpiece. His acceptance of his gay identity literally unlocks telekinetic superpowers. The male characters are largely reduced to bumbling sidekicks. The military and government are the real villains.\n\nHere is what makes the Stranger Things woke trap so effective: the traditional elements in Seasons 1 and 2 are genuinely good. They're not cynical bait. The Duffer Brothers clearly have real affection for Spielberg, Stephen King, and the adventure storytelling of the 1980s. But over the course of nine years and five seasons, those traditional elements were slowly hollowed out and replaced. The nuclear family gave way to chosen family. Masculine heroism gave way to female-led action and male buffoonery. The small town went from being a place worth protecting to a place full of bigots.\n\nFor conservative viewers who watched this show from the beginning, Stranger Things is a lesson in how long-form storytelling can be weaponized. You invest in the characters. You trust the world. And then, season by season, the world changes around you until you're watching a completely different show than the one you signed up for. Stranger Things started as a celebration of the America conservatives remember. It ended as a lecture about the America progressives want.",
      adultInsight: "Stranger Things is worth watching, at least the early seasons. Seasons 1 and 2 are genuinely excellent genre television with strong traditional values. Season 3 is the transition point where progressive elements begin but don't yet dominate. Seasons 4 and 5 are where the ideological freight becomes heavy. The most important thing for conservative viewers to understand is the mechanism. This show is the clearest example in modern television of how progressive ideology can be introduced gradually into a fundamentally traditional story. Study it. Notice how the shifts happen. The traditional elements, particularly in the early seasons, are genuinely worth celebrating. The tragedy of Stranger Things is that these genuine strengths were ultimately subordinated to an ideological project the creators valued more.",
      parentalGuidance: "Violence is significant across all seasons with monster attacks, body horror, and character deaths. Season 4 features Vecna killing teenagers by breaking their bones and gouging their eyes. Not appropriate for young children. Increasing LGBTQ content in Seasons 4-5, culminating in Will's coming-out and the explicit linking of gay identity to superpowers. Moderate profanity throughout. Teen drinking, smoking, and marijuana use depicted. Seasons 1-2 are appropriate for 12+ with parental engagement. Seasons 3-4 are 14+ with parental awareness of progressive content. Season 5 is 14+ with active parental discussion about ideological elements."
    },
    tropeAudit: [
      { trope: "Queer Normalization", id: "WOKE-007", category: "WOKE", location: "S3E8, S4E2-8, S5E1-8 -- Robin comes out, Will comes out, gay identity unlocks superpowers", authenticity: "Will's quiet difference was present from S1 but supernatural-powers-through-gay-acceptance is pure progressive fantasy" },
      { trope: "The Girl Boss", id: "WOKE-003", category: "WOKE", location: "S3 onward -- Female characters increasingly dominate action while male characters drift toward comic relief", authenticity: "Eleven's power was established but broader shift has no narrative justification" },
      { trope: "The Bigoted Traditionalist", id: "WOKE-008", category: "WOKE", location: "S4E1-7, S5 -- Satanic Panic subplot frames conservative religious culture as ignorant mob behavior", authenticity: "Satanic Panic was real but show presents zero townspeople who balance concern with reason" },
      { trope: "Institutional Evil", id: "WOKE-004", category: "WOKE", location: "All seasons esp S4-S5 -- Government and military consistently portrayed as malevolent", authenticity: "Government conspiracy is native to the genre but escalation to military-as-primary-antagonist goes beyond convention" },
      { trope: "Infallible Youth", id: "WOKE-016", category: "WOKE", location: "All seasons -- Kids consistently outperform adults, every adult institution fails", authenticity: "Genre convention with progressive amplification" },
      { trope: "Historical Revisionism", id: "WOKE-012", category: "WOKE", location: "S5E7 -- Will comes out in 1987 Indiana to universal immediate group acceptance", authenticity: "Universal enthusiastic group acceptance in 1987 rural Indiana strains credulity" },
      { trope: "Anti-Western Revisionism", id: "WOKE-020", category: "WOKE", location: "S4-S5 -- Hawkins shifts from nostalgic small-town America to suffocating bigoted community", authenticity: "Show's treatment goes beyond complexity into critique" },
      { trope: "The Victimhood Meritocracy", id: "WOKE-009", category: "WOKE", location: "S5E5-8 -- Will's suffering retroactively reframed as closeted gay trauma outranking interdimensional horror", authenticity: "Will's otherness was always present but reframe feels imposed" },
      { trope: "The Marginalized Savant", id: "WOKE-001", category: "WOKE", location: "S5E6-8 -- Will's gay identity literally unlocks telekinetic powers", authenticity: "Queerness equals power, repression equals weakness -- impossible to read as anything other than ideological" },
      { trope: "Emasculation Comedy", id: "WOKE-014", category: "WOKE", location: "S3-S5 -- Steve and Jonathan reduced to bickering sidekicks, all male characters decline", authenticity: "All male characters declining while all female characters increase is a pattern" },
      { trope: "Redeemed Criminal Systemic", id: "WOKE-019", category: "WOKE", location: "S4E1-7 -- Eddie Munson framed as victim of systemic prejudice, outsider culture inherently virtuous", authenticity: "Mixed -- Eddie is well-drawn but used for ideological purposes" },
      { trope: "Globalist Utopia", id: "WOKE-017", category: "WOKE", location: "S5 finale -- Diverse queer-inclusive found family transcends 1980s social norms", authenticity: "Presenting found family as ideologically superior to traditional family is an editorial choice" },
      { trope: "The Therapeutic Resolution", id: "WOKE-006", category: "WOKE", location: "S5 finale -- Characters collectively expel trauma, resolution is therapeutic rather than heroic", authenticity: "Prioritizing therapy over heroism is an ideological choice" },
      { trope: "Defense of the Innocent", id: "TRADITIONAL-045", category: "TRADITIONAL", location: "S1-S2 -- Joyce's relentless search for Will, Hopper's protection of Eleven", authenticity: "Genuine and deeply felt, the show cannot function without this traditional foundation" },
      { trope: "Traditional Femininity", id: "TRADITIONAL-036", category: "TRADITIONAL", location: "S1-S2 -- Joyce Byers coded as devoted mother, strength from maternal ferocity", authenticity: "One of the most honest portrayals of maternal devotion in recent genre television" },
      { trope: "The Self-Sacrificing Hero", id: "TRADITIONAL-026", category: "TRADITIONAL", location: "S1 Eleven, S2 Bob Newby, S3 Hopper and Billy, S4 Eddie Munson", authenticity: "Genuine -- the show treats these sacrifices with appropriate gravity" },
      { trope: "Industry and Perseverance", id: "TRADITIONAL-041", category: "TRADITIONAL", location: "S1-S3 -- Kids' determination through intelligence, effort, and teamwork", authenticity: "Genuine and consistent with Spielbergian influences" },
      { trope: "Wise Elder", id: "TRADITIONAL-033", category: "TRADITIONAL", location: "S1-S3 -- Hopper as patriarchal anchor, flawed but protective", authenticity: "Genuine -- David Harbour's performance is consistently strong" },
      { trope: "Faith in Adversity", id: "TRADITIONAL-043", category: "TRADITIONAL", location: "S1-S2 -- Implicit Christian undertones, Upside Down as spiritual battle", authenticity: "Genuine in early seasons, completely absent by Season 5" },
      { trope: "Restored Home", id: "TRADITIONAL-048", category: "TRADITIONAL", location: "S1-S2 finales -- Homecomings and family reconstitution", authenticity: "Genuine in Seasons 1-2, ideologically reframed by Season 5" },
      { trope: "Brotherhood and Loyalty", id: "TRADITIONAL-027", category: "TRADITIONAL", location: "S1-S2 -- Core friendship between Mike, Dustin, Lucas, and Will", authenticity: "Genuine in early seasons, diminished as show progresses" }
    ]
  },
  {
    id: "ozark",
    slug: "ozark",
    title: "Ozark",
    year: 2022,
    type: "series",
    platform: "Netflix",
    genre: "Crime, Thriller",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "16 min",
    poster: "/images/posters/ozark.jpg",
    verdict: "WOKE",
    wokeScore: 9,
    tradScore: 5,
    authIndex: 64,
    scoreMargin: "-4 WOKE",
    wokeTrap: {
      present: true,
      degree: "moderate",
      explanation: "Season 1 hooks conservative viewers with a compelling premise: a middle-class father desperately trying to keep his family alive after getting in too deep with a Mexican drug cartel. The family unit is front and center. Then the drift begins. By Season 2, Wendy starts muscling into Marty's operation. By Season 4, Marty has been reduced to a passive shell while Wendy operates as a ruthless political operator who faces zero meaningful consequences.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: true,
      explanation: "Season 1 hooks with a patriarchal family-protection premise, then systematically replaces Marty's competence with Wendy's ruthless dominance while every character who maintains traditional values is destroyed."
    },
    creative_team: {
      director: { name: "Jason Bateman (12 episodes)", ideology: "NEUTRAL", profile: "Standard Hollywood liberal. Not a driving force behind ideological content." },
      writer: { name: "Bill Dubuque & Mark Williams (creators), Chris Mundy (showrunner)", profile: "Dubuque is a St. Louis native with institutional cynicism. Mundy architected Wendy's ascent and the controversial finale." },
      lead_producer: { name: "Jason Bateman", company: "Aggregate Films" },
      composer: { name: "Danny Bensi & Saunder Jurriaans" },
      top_cast: [
        { name: "Jason Bateman", role: "Marty Byrde" },
        { name: "Laura Linney", role: "Wendy Byrde" },
        { name: "Julia Garner", role: "Ruth Langmore" },
        { name: "Tom Pelphrey", role: "Ben Davis" },
        { name: "Sofia Hublitz", role: "Charlotte Byrde" }
      ],
      prediction: { verdict: "MIXED", confidence: "moderate" }
    },
    fidelity_casting: {
      score: "N/A",
      summary: "Original property with no source material to assess fidelity against.",
      detailed_analysis: "Ozark is an original property. The cast is predominantly white, consistent with the Missouri Ozarks setting. The most prominent non-white characters are cartel members and one FBI agent, Maya Miller, who is eventually corrupted by the Byrdes."
    },
    summary: {
      overall: "Ozark is genuinely good television. Across its four-season run, it delivered some of the tightest crime-thriller writing on any streaming platform. Jason Bateman proved he could carry dramatic weight, Julia Garner's Ruth Langmore became one of the most electrifying characters in recent TV history, and the Ozarks setting brought a moody, oppressive atmosphere that made every episode feel like a slow-motion car crash you couldn't look away from.\n\nSeason 1 works almost perfectly on conservative terms. Marty Byrde is a Chicago financial advisor who launders money for the Navarro cartel. What follows is a survival story centered squarely on the nuclear family. Marty is the competent father making impossible choices. The central tension is simple and timeless: can this family survive?\n\nSeason 2 is where the shift starts. Wendy begins asserting herself in the business, making unilateral decisions and pushing the family deeper into the cartel's orbit. The show frames this as Wendy stepping up. The marriage dynamics flip. Season 3 drops any pretense of ambiguity. Wendy orchestrates the murder of her own brother, Ben Davis, a kind, genuine, mentally ill man. The show doesn't punish Wendy for this.\n\nSeason 4 completes the transformation. Ruth Langmore, the show's moral center and the only character who maintained a recognizable code of honor, is murdered. The series finale sees the Byrdes walk free. Private investigator Mel Sattem confronts them with evidence, declaring \"You don't get to win.\" Then Jonah picks up a shotgun, and the screen cuts to black. Evil prevails.\n\nThe systematic emasculation of Marty Byrde is striking. In Season 1, he is the competent patriarch. By Season 4, he is a hollow man unable to make decisions without Wendy's direction. The portrayal of rural America is equally concerning: the Lake of the Ozarks locals are overwhelmingly depicted as criminals, addicts, or rubes. The Chicago-educated Byrdes are the smartest people in every room.\n\nWhere Ozark retains genuine traditional value is in Ruth's arc. She embodies loyalty, honor, hard work, and a willingness to fight. The show kills her for it. Julia Garner's performance was the show's beating heart. Ruth proves that traditional values are more compelling than Wendy's ruthless pragmatism, which is why her death lands so hard.\n\nOzark is a show that conservative audiences will enjoy watching if they go in prepared. But go in with your eyes open. This is not a show that affirms the family. It uses the family as a Trojan horse, drawing you in with the promise of a patriarch fighting for his loved ones, then slowly revealing that the real power was always with the woman willing to sacrifice everything to win.",
      adultInsight: "Conservative adult viewers should understand what they are watching. Season 1 is a legitimately great thriller with a traditional family-protection premise. Seasons 2 and 3 are where the ideological drift happens, and once you see the pattern you can engage critically rather than absorbing passively. The finale will frustrate you if you expect moral resolution. It is designed to frustrate you. Ozark's creators believe the rich and ruthless prevail, and they built four seasons to prove it. One practical note: binge-watching makes the ideological drift harder to notice. Watch one season per week rather than plowing through all four.",
      parentalGuidance: "Ozark is emphatically not for children. Violence is graphic and frequent with characters shot, drowned, beaten, and tortured. Frequent sexual content across all seasons including marital infidelity and strip club scenes. Pervasive strong language with constant F-bombs. Drug manufacturing and distribution are central plot elements. The psychological darkness is more damaging than the physical violence: the show depicts the corruption of children by their parents, mental illness exploited for narrative purposes, and a worldview in which moral people are systematically destroyed. 18+ without reservation."
    },
    tropeAudit: [
      { trope: "The Girl Boss", id: "WOKE-003", category: "WOKE", location: "S2-S4 -- Wendy's arc from supportive spouse to ruthless operator who outmaneuvers everyone", authenticity: "N/A (original property)" },
      { trope: "The Emasculated Man", id: "WOKE-010", category: "WOKE", location: "S2-S4 -- Marty's systematic reduction from competent patriarch to passive enabler", authenticity: "N/A" },
      { trope: "The Bigoted Traditionalist", id: "WOKE-008", category: "WOKE", location: "Throughout -- Rural Missouri characters express crude, ignorant views; Byrdes coded as educated cosmopolitans", authenticity: "N/A" },
      { trope: "Redeemed Criminal Systemic", id: "WOKE-019", category: "WOKE", location: "S1-S4 -- Ruth's criminality consistently contextualized through upbringing and systemic disadvantage", authenticity: "N/A" },
      { trope: "Institutional Evil", id: "WOKE-004", category: "WOKE", location: "S1-S4 -- Every institution is corrupt or corruptible, the one man who insists the system should work is killed", authenticity: "N/A" },
      { trope: "The Disposable White Male", id: "WOKE-025", category: "WOKE", location: "S3 -- Ben Davis exists to be sacrificed for Wendy's arc", authenticity: "N/A" },
      { trope: "Globalist Utopia (inverted)", id: "WOKE-017", category: "WOKE", location: "S3-S4 -- Byrdes help cartel transition into legitimate global foundation, national borders as obstacles", authenticity: "N/A" },
      { trope: "The Corrupt Church", id: "WOKE-012", category: "WOKE", location: "S1-S4 -- Pastor Mason's faith is naive or instrumental, churches used as laundering tools", authenticity: "N/A" },
      { trope: "Moral Relativism as Enlightenment", id: "WOKE-015", category: "WOKE", location: "Series-wide -- Every character with fixed moral position is punished, moral clarity coded as liability", authenticity: "N/A" },
      { trope: "Defense of the Innocent", id: "TRADITIONAL-045", category: "TRADITIONAL", location: "S1 -- Marty's original motivation is pure parental protection", authenticity: "Authentically traditional in Season 1, increasingly hollow" },
      { trope: "Loyalty and Honor", id: "TRADITIONAL-028", category: "TRADITIONAL", location: "S1-S4 -- Ruth operates by a code, protects her people, avenges wrongs", authenticity: "Authentically traditional -- Ruth is the show's moral center" },
      { trope: "Industry and Perseverance", id: "TRADITIONAL-041", category: "TRADITIONAL", location: "S1-S4 -- Marty and Ruth demonstrate relentless work ethic", authenticity: "Authentically traditional" },
      { trope: "The Self-Sacrificing Hero", id: "TRADITIONAL-026", category: "TRADITIONAL", location: "S1-S4 -- Buddy Dieker, Ruth, Wyatt sacrifice for people they love", authenticity: "Present but subverted -- self-sacrifice is consistently punished" },
      { trope: "Consequences of Sin", id: "TRADITIONAL-044", category: "TRADITIONAL", location: "S1-S3 -- Crime carries visible costs, abandoned in S4 finale", authenticity: "Traditional through Season 3, deliberately betrayed in Season 4" }
    ]
  },
  {
    id: "the-bear",
    slug: "the-bear",
    title: "The Bear",
    year: 2024,
    type: "series",
    platform: "Hulu / FX",
    genre: "Drama, Comedy",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "15 min",
    poster: "/images/posters/the-bear.jpg",
    verdict: "TRADITIONAL",
    wokeScore: 5,
    tradScore: 9,
    authIndex: 82,
    scoreMargin: "+4 TRAD",
    wokeTrap: {
      present: false,
      degree: null,
      explanation: "The Bear is not a woke trap. Season 1 is about as close to an anti-woke prestige show as modern television produces. Blue-collar Chicago, masculine codes of honor, grief processed through work rather than therapy-speak. The diversity in the cast feels organic to the setting. Season 3 has some creative self-indulgence and therapy-culture drift, but its problems are creative, not ideological.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: false,
      explanation: "The Bear is not a woke trap. Its diversity is organic to Chicago's restaurant world, its values center on competence and craft, and its later-season drift is creative self-indulgence rather than ideological capture."
    },
    creative_team: {
      director: { name: "Christopher Storer", ideology: "MILDLY PROGRESSIVE", profile: "Chicago-area native. Collaborators tend progressive (Burnham, Minhaj, Youssef) but The Bear represents a craft-first departure that prioritizes authenticity over ideology." },
      writer: { name: "Christopher Storer & Joanna Calo", profile: "Calo co-showruns and writes. Previous credits include Bojack Horseman. Character-focused writer whose progressive instincts are tempered by craft." },
      lead_producer: { name: "Hiro Murai", company: "FX Productions" },
      composer: { name: "Jeffrey Qaiyum (JAQ) & Johnny Iguana" },
      top_cast: [
        { name: "Jeremy Allen White", role: "Carmen 'Carmy' Berzatto" },
        { name: "Ebon Moss-Bachrach", role: "Richard 'Richie' Jerimovich" },
        { name: "Ayo Edebiri", role: "Sydney Adamu" },
        { name: "Liza Colon-Zayas", role: "Tina Marrero" },
        { name: "Oliver Platt", role: "Jimmy Cicero" }
      ],
      prediction: { verdict: "MIXED", confidence: "moderate" }
    },
    fidelity_casting: {
      score: "AUTHENTIC",
      summary: "The cast reflects the actual demographic reality of Chicago's restaurant industry. No forced diversity.",
      detailed_analysis: "The Bear's casting is one of its greatest strengths. The show is set in Chicago's restaurant world, which is genuinely one of the most diverse workplaces in America. Every casting choice reflects demographic reality: Italian-American chef, Nigerian-American sous chef, Latina line cook, Somali veteran cook. This is what authentic casting looks like."
    },
    summary: {
      overall: "Season 1 of The Bear is genuinely great television. Carmen Berzatto returns to Chicago after his brother Michael's suicide, inheriting a failing Italian beef shop, a mountain of debt, and a staff that ranges from hostile to barely functional. The show's first season is a reconstruction story driven by competence. Carmy doesn't win people over with speeches or feelings. He wins them over by being better at the work than anyone else in the room.\n\nThe supporting cast is diverse in a way that never calls attention to itself. Sydney Adamu shows up as Carmy's sous chef. She's talented, ambitious, and occasionally in over her head. The show doesn't make her race A Thing. Tina, a Latina line cook, is initially hostile to change. Her resistance is framed as pride and fear, not ignorance. When she comes around, it's because she sees the value. This is what organic diversity looks like.\n\nSeason 2 expands the world and hits its highest notes. The Richie episode, Forks, might be the single best episode of television produced in the last five years. Richie stages at a high-end restaurant and discovers that service is a form of excellence he never knew existed. No therapy. No intervention. Just exposure to a higher standard and the decision to rise to it. That's a profoundly conservative arc.\n\nSeason 3 is a creative mess but not an ideological one. The show disappears into itself. Carmy spends entire episodes staring at walls. The therapy-industrial complex has arrived with characters processing feelings in clinical language. But even in its weakest season, The Bear doesn't go where you'd expect a captured show to go. There are no diversity lectures. The restaurant's financial struggles are treated as the brutal economics of a small business, not a commentary on capitalism.\n\nThe Bear is a show that started as one of the most traditionally-coded prestige dramas on television. Hard work. Competence hierarchies. Male friendship and rivalry. Grief processed through action rather than words. The show hasn't been captured. It's been bloated. There's a difference, and it matters.",
      adultInsight: "Conservative adult viewers should approach The Bear with enthusiasm for seasons 1 and 2 and measured expectations for season 3. This is not a show trying to sneak progressive politics past you. Its politics are the politics of the kitchen: hierarchy, competence, respect for craft, and loyalty to people rather than ideas. The diversity question is easy: the cast looks like a real Chicago kitchen because it IS modeled on real Chicago kitchens. If more shows handled diversity this way, the culture war around casting would evaporate overnight.",
      parentalGuidance: "The Bear is rated TV-MA. Extremely heavy profanity throughout all three seasons with the F-word used dozens of times per episode. Limited but intense violence including a stabbing incident. The show deals heavily with the aftermath of suicide which is discussed frankly. Minimal sexual content. Moderate substance use with addiction discussed extensively. Anxiety, panic attacks, PTSD, and family dysfunction are major themes. The kitchen scenes are intentionally stressful and can be genuinely anxiety-inducing. 16+ with parental awareness. For mature teenagers interested in cooking or restaurant culture, the show could be a valuable window into the real costs of pursuing excellence."
    },
    tropeAudit: [
      { trope: "Therapy Culture", id: "WOKE-023", category: "WOKE", location: "S3 and S1 Al-Anon scenes -- Clinical emotional processing increasingly replaces blue-collar emotional vocabulary", authenticity: "Mixed -- Al-Anon is real in the industry but S3 clinical language feels writerly" },
      { trope: "The Victimhood Meritocracy", id: "WOKE-009", category: "WOKE", location: "S3 Donna Berzatto flashbacks -- Abusive parenting contextualized as product of her own trauma", authenticity: "Mixed -- real families have this complexity but editorial emphasis softens accountability" },
      { trope: "Infallible Youth", id: "WOKE-016", category: "WOKE", location: "S1-S3 -- Sydney consistently the most talented and emotionally intelligent person in the room", authenticity: "Largely authentic -- young hungry chefs do shake up established kitchens" },
      { trope: "Fragile Masculinity Framing", id: "WOKE-012", category: "WOKE", location: "S2-S3 -- Carmy's intensity increasingly framed as toxic patterns rather than price of excellence", authenticity: "Mixed -- restaurant kitchens do have toxic cultures but progressive tendency to pathologize is visible" },
      { trope: "Globalist Utopia", id: "WOKE-017", category: "WOKE", location: "S3 celebrity chef appearances -- Culinary world as borderless meritocracy", authenticity: "Authentic -- the fine dining world is genuinely global" },
      { trope: "Industry and Perseverance", id: "TRADITIONAL-041", category: "TRADITIONAL", location: "S1-S3 -- The entire show is built on hard work and pursuit of excellence through physical labor", authenticity: "Authentic -- anyone who has worked in a professional kitchen will recognize this" },
      { trope: "The Self-Sacrificing Hero", id: "TRADITIONAL-026", category: "TRADITIONAL", location: "S1 Michael's legacy, S2 multiple arcs -- The weight of what these characters give up", authenticity: "Authentic -- restaurant industry has well-documented history of burnout and self-destruction" },
      { trope: "Competence Hierarchy", id: "TRADITIONAL-042", category: "TRADITIONAL", location: "S1-S3 -- The kitchen operates on strict hierarchy based on skill, Yes Chef is a code", authenticity: "Authentic -- the brigade system is real and functions exactly as depicted" },
      { trope: "Wise Elder / Mentor", id: "TRADITIONAL-033", category: "TRADITIONAL", location: "S2 Chef Terry (Olivia Colman), S1-S3 Cicero -- Mentorship through high standards", authenticity: "Authentic -- this is how mentorship works in serious culinary programs" },
      { trope: "Defense of the Innocent", id: "TRADITIONAL-045", category: "TRADITIONAL", location: "S1-S3 -- Natalie's pregnancy, protecting next generation from family dysfunction", authenticity: "Authentic -- generational trauma cycle presented honestly" },
      { trope: "Traditional Femininity", id: "TRADITIONAL-036", category: "TRADITIONAL", location: "S2 Tina's arc, S2-S3 Natalie's arc -- Women defined by competence not gender grievance", authenticity: "Authentic -- the women on this show feel real" },
      { trope: "Male Friendship and Brotherhood", id: "TRADITIONAL-039", category: "TRADITIONAL", location: "S1-S3 -- Carmy and Richie relationship is the emotional spine of the series", authenticity: "Deeply authentic -- most honest depiction of male friendship on TV since The Sopranos" },
      { trope: "Small Business Grit", id: "TRADITIONAL-044", category: "TRADITIONAL", location: "S1-S3 -- Financial pressure of running a restaurant presented with brutal honesty", authenticity: "Authentic -- the financial pressures depicted are realistic and specific" },
      { trope: "Generational Legacy", id: "TRADITIONAL-047", category: "TRADITIONAL", location: "S1-S3 -- The entire series is about inheritance both literal and spiritual", authenticity: "Authentic -- the weight of family legacy in ethnic and working-class communities portrayed with genuine understanding" }
    ]
  },
  {
    id: "yellowjackets",
    slug: "yellowjackets",
    title: "Yellowjackets",
    year: 2025,
    type: "series",
    platform: "Showtime / Paramount+",
    genre: "Thriller, Horror",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "16 min",
    poster: "/images/posters/yellowjackets.jpg",
    verdict: "MIXED",
    wokeScore: 8,
    tradScore: 6,
    authIndex: 70,
    scoreMargin: "-2 WOKE",
    wokeTrap: {
      present: true,
      degree: "moderate",
      explanation: "Season one sells itself as a brutal survival thriller with a genuinely transgressive hook. The show uses that savage premise as a delivery mechanism for feminist themes about female rage, queer identity, and the deconstruction of male authority. Conservative viewers drawn in by the cannibal thriller premise will find themselves watching a show increasingly interested in validating female darkness as empowerment rather than examining it as moral failure.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: true,
      explanation: "The survival thriller premise hooks viewers, then the feminist scaffolding becomes increasingly prominent. The show frames female savagery as liberation rather than cautionary tale."
    },
    creative_team: {
      director: { name: "Karyn Kusama (pilot)", ideology: "WOKE", profile: "Explicitly feminist filmmaker. Jennifer's Body is her ideological signature. Career organized around placing women in traditionally male genre spaces." },
      writer: { name: "Ashley Lyle & Bart Nickerson", profile: "Married couple who co-created the show. Lyle has spoken about wanting to explore what happens when girls are freed from societal expectations. Deliberately feminist project from inception." },
      lead_producer: { name: "Drew Comins", company: "Lionsgate Television" },
      composer: { name: "Theodore Shapiro; Craig Wedren & Anna Waronker (theme)" },
      top_cast: [
        { name: "Melanie Lynskey", role: "Adult Shauna" },
        { name: "Christina Ricci", role: "Adult Misty" },
        { name: "Sophie Thatcher", role: "Teen Natalie" },
        { name: "Tawny Cypress", role: "Adult Taissa" },
        { name: "Juliette Lewis", role: "Adult Natalie" }
      ],
      prediction: { verdict: "MIXED", confidence: "moderate" }
    },
    fidelity_casting: {
      score: "N/A",
      summary: "Original IP with no source material to assess fidelity against.",
      detailed_analysis: "The cast is racially diverse in ways that track with a suburban New Jersey high school soccer team in the 1990s, which is demographically plausible. The more relevant observation is the deliberate alignment between actors' real-life identities and their characters. Jasmin Savoy Brown is openly queer. Liv Hewson is nonbinary. This identity-casting pattern signals the production's ideological orientation."
    },
    summary: {
      overall: "Yellowjackets arrived with a pitch that practically dared you to watch: a girls' soccer team crashes in the Canadian wilderness, and over nineteen months they descend into tribal violence and cannibalism. Season one delivers on that promise, mostly. The dual timeline structure creates genuine tension. Melanie Lynskey is terrific as adult Shauna. Christina Ricci is genuinely unsettling as adult Misty. Ella Purnell as Jackie is the season's most compelling tragedy.\n\nThe show's central question, what are people really capable of when civilization's guardrails come off, is a fundamentally conservative question. And in its best moments, Yellowjackets treats that question with the gravity it deserves. But the show doesn't frame the girls' descent as a cautionary tale. It frames it as liberation. The wilderness strips away society's expectations, and what emerges is depicted as authenticity rather than horror.\n\nThe male characters are systematically dismantled. Coach Ben, the sole adult and natural authority figure, is progressively stripped of authority and ultimately executed by the girls in season three. Travis functions primarily as a love interest. The men don't drive the story. They are consumed by it.\n\nThe LGBTQ representation is significant and deliberate. Taissa and Van's relationship spans both timelines. Coach Ben is gay. The queer representation is woven into the fabric of the show's identity. The supernatural element consistently validates spiritual, intuitive, feminine reading over rational skepticism. Characters who resist the mysticism are marginalized or destroyed.\n\nWhat's genuinely traditional about Yellowjackets deserves credit. The show takes consequences seriously. Every major character is damaged by what they did. Laura Lee, the group's devout Christian, is treated with surprising warmth and sincerity. Her death is a turning point, and what follows is worse. Shauna's relationship with Callie demonstrates how parental moral failure transmits across generations.\n\nFor conservative viewers, Yellowjackets keeps touching genuinely important truths about human nature and then flinching away from the conclusions those truths demand. The show's own narrative keeps making the conservative case even as its creators push a progressive one.",
      adultInsight: "Conservative adults should approach Yellowjackets knowing exactly what they are getting into: a survival thriller with a feminist engine. The first season is genuinely excellent television on almost any ideological terms. As seasons progress, the ideological framing becomes more prominent. There is something genuinely valuable in the show's accidental traditionalism: it keeps trying to tell a story about female empowerment through savagery, and it keeps accidentally demonstrating why civilization, authority, and moral structure matter. Watch it as a case study in how a talented creative team can build a show whose narrative engine runs on traditional truths while its marketing runs on progressive ones.",
      parentalGuidance: "Yellowjackets is absolutely not appropriate for children. Violence is graphic and sustained with characters impaled, burned, dismembered, and cannibalized. Multiple sex scenes across both timelines including between teenagers and same-sex relationships. Frequent strong profanity. Significant drug and alcohol addiction storylines. The show depicts sustained psychological deterioration, group psychosis, cult behavior, dissociative episodes, and suicidal ideation. The psychological horror is often more disturbing than the physical violence. 18+ firmly."
    },
    tropeAudit: [
      { trope: "The Girl Boss Collective", id: "WOKE-003", category: "WOKE", location: "Throughout -- Survivors establish explicitly matriarchal society, every significant role filled by women", authenticity: "N/A (original fiction)" },
      { trope: "Incompetent Male Authority", id: "WOKE-008", category: "WOKE", location: "S1-S3 Coach Ben -- Sole adult male stripped of authority, tried and executed by the girls", authenticity: "N/A" },
      { trope: "Queer Normalization", id: "WOKE-017", category: "WOKE", location: "Throughout -- Taissa and Van's relationship, Coach Ben's homosexuality, Walter's flamboyance", authenticity: "N/A" },
      { trope: "Female Violence as Liberation", id: "WOKE-009", category: "WOKE", location: "Throughout -- Girls' descent into violence coded as primal feminine power and authenticity", authenticity: "N/A" },
      { trope: "Anti-Institutional Framing", id: "WOKE-020", category: "WOKE", location: "Present-day timeline -- Every institution fails the survivors, civilization is inadequate", authenticity: "N/A" },
      { trope: "Intuition Over Rationality", id: "WOKE-016", category: "WOKE", location: "Throughout Lottie's arc -- Feminine intuitive framework validated, rational skepticism punished", authenticity: "N/A" },
      { trope: "Systemic Excuse for Moral Failure", id: "WOKE-004", category: "WOKE", location: "Present-day -- Adult dysfunction contextualized through trauma rather than moral failure", authenticity: "N/A" },
      { trope: "The Marginalized Savant", id: "WOKE-001", category: "WOKE", location: "S1-S2 -- Taissa as most strategically competent survivor, intersectional identity stacking", authenticity: "N/A" },
      { trope: "Consequences of Moral Collapse", id: "TRADITIONAL-045", category: "TRADITIONAL", location: "Both timelines -- Every major character permanently damaged, no one is okay", authenticity: "The psychological realism of long-term trauma is well-handled" },
      { trope: "Sacrifice and Death", id: "TRADITIONAL-026", category: "TRADITIONAL", location: "S2 finale -- Natalie sacrifices herself for Lottie, genuinely moving", authenticity: "N/A" },
      { trope: "Survival Through Hard Work", id: "TRADITIONAL-041", category: "TRADITIONAL", location: "Wilderness timeline -- Practical survival elements presented with respect", authenticity: "N/A" },
      { trope: "The Cost of Abandoning Faith", id: "TRADITIONAL-033", category: "TRADITIONAL", location: "S1 Laura Lee's arc -- Christian moral compass treated with warmth, her death lets darkness rush in", authenticity: "N/A" },
      { trope: "Generational Damage", id: "TRADITIONAL-048", category: "TRADITIONAL", location: "S1-S3 Shauna and Callie -- Parental moral failure transmits across generations", authenticity: "N/A" },
      { trope: "The Fallen Nature of Humanity", id: "TRADITIONAL-036", category: "TRADITIONAL", location: "Throughout -- Entire premise is that ordinary people are capable of terrible things without civilizing structures", authenticity: "The show's core premise is a profound argument for civilizing structures even if dressed in feminist clothing" }
    ]
  },
  {
    id: "snow-white-2025",
    slug: "snow-white-2025",
    title: "Snow White",
    year: 2025,
    type: "film",
    platform: "Theatrical",
    genre: "Fantasy, Musical",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "14 min",
    poster: "/images/posters/snow-white-2025.jpg",
    verdict: "WOKE",
    wokeScore: 9,
    tradScore: 4,
    authIndex: 58,
    scoreMargin: "-5 WOKE",
    wokeTrap: {
      present: false,
      degree: null,
      explanation: "Disney's live-action Snow White makes no attempt to disguise its ideological overhaul. From the pre-release marketing to Rachel Zegler's own public comments dismissing the 1937 original, this film announces its progressive intentions loudly and early. Conservative viewers will know exactly what they are getting within the first ten minutes.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: false,
      explanation: "Snow White announces its progressive intentions loudly and early. No bait-and-switch. The traditional elements that survive exist alongside rather than underneath the progressive reframing."
    },
    creative_team: {
      director: { name: "Marc Webb", ideology: "NEUTRAL", profile: "Known for 500 Days of Summer and Amazing Spider-Man. Not an ideological filmmaker. The ideology in Snow White is Disney's, not Webb's." },
      writer: { name: "Erin Cressida Wilson", profile: "Primarily known for Secretary (2002). Sparse credits make her selection for a $270M Disney tentpole notable. The screenplay's changes align with Disney's corporate progressive direction." },
      lead_producer: { name: "Marc Platt", company: "Marc Platt Productions / Disney" },
      composer: { name: "Jeff Morrow" },
      top_cast: [
        { name: "Rachel Zegler", role: "Snow White" },
        { name: "Gal Gadot", role: "Evil Queen" },
        { name: "Andrew Burnap", role: "Jonathan" }
      ],
      prediction: { verdict: "WOKE", confidence: "high" }
    },
    fidelity_casting: {
      score: "REPLACED",
      summary: "Color-blind casting of a Latina Snow White; prince replaced entirely with rebel love interest; dwarfs rendered as CGI creatures rather than people.",
      detailed_analysis: "Snow White's name in every prior version refers to her pale complexion. Casting a Latina actress is a legitimate choice, but the film changes the name's origin to a snowstorm to accommodate it rather than being straightforward. The Prince has been entirely replaced by a rebel thief. The Seven Dwarfs have been replaced by CGI magical beings, erasing the very representation the decision claimed to protect."
    },
    summary: {
      overall: "Disney's live-action Snow White arrives carrying more baggage than a royal carriage. The question conservative viewers want answered is simple: is the finished product as aggressively ideological as the marketing suggested? The honest answer is yes, but it's more complicated than a simple thumbs-down.\n\nRachel Zegler can sing. That much is beyond dispute. Gal Gadot is having a grand time as the Evil Queen, chewing scenery with campy relish. The production design is lavish.\n\nBut the film's problems run deeper than its surface polish. The central project of this Snow White is demolition. Not adaptation. Not updating. Demolition. Snow White has been rewritten from a character defined by kindness into a character defined by empowerment. The rebellion storyline replaces the romance as the central plot engine. Snow White organizes a resistance movement. The climax is a political uprising. It's less fairy tale and more young-adult dystopian franchise.\n\nThe dwarfs situation perfectly encapsulates Disney's ideological confusion. After Peter Dinklage criticized the concept, Disney replaced them with CGI magical beings rather than casting actors with dwarfism. The result pleases nobody. The disability community gets tokenized through a side character rather than centered in the roles they were born to play.\n\nThe box office told the story. At $206 million worldwide against a $270 million budget, Snow White qualifies as a genuine box office bomb. Audiences on both sides stayed home.\n\nConservative viewers should know that true love's kiss survives. The Evil Queen is genuinely evil and defeated by her own vanity. Kindness and inner beauty matter in the climax. These are real and worth noting. But they exist within a framework so thoroughly overhauled that they feel like survivors of a demolition rather than foundations of a story.",
      adultInsight: "Adult conservative viewers should approach Snow White 2025 with clear eyes. This is Disney's most aggressive ideological overhaul of a classic property. That said, the film is not without redeeming moments. True love's kiss survives. The Evil Queen is a genuine villain defined by traditional vices. The most instructive element is the box office: Snow White bombed spectacularly, losing Disney an estimated $100-150 million. The market spoke. Contempt for your own heritage is not a commercial strategy.",
      parentalGuidance: "Snow White is rated PG and relatively mild in terms of content. Violence is fairy-tale level. No sexual content, substance use, or strong language. The concern for conservative parents is ideological rather than content-based. For families who value the original fairy tale, this film requires a conversation about adaptation and cultural heritage. Compare the 1937 version and the 2025 version side by side and ask which story your children find more compelling. Appropriate for children 6 and up from a content perspective. Ideological engagement recommended for children 10 and up."
    },
    tropeAudit: [
      { trope: "The Girl Boss", id: "WOKE-003", category: "WOKE", location: "Throughout -- Snow White rewritten from gentle princess to rebellion leader", authenticity: "Fabricated -- source material contains no rebellion" },
      { trope: "The Disposable Prince", id: "WOKE-022", category: "WOKE", location: "Throughout -- Prince entirely eliminated, replaced by poor thief rebel", authenticity: "Fabricated -- Jonathan does not exist in any version of the source material" },
      { trope: "Diversity Retrofit", id: "WOKE-012", category: "WOKE", location: "Casting -- Latina Snow White with name origin changed from complexion to snowstorm", authenticity: "Fabricated -- the name has always referred to complexion" },
      { trope: "The Bigoted Traditionalist", id: "WOKE-008", category: "WOKE", location: "Subtext -- Traditional beauty standards coded as the villain's domain", authenticity: "Mixed -- Queen's vanity is original but expanded critique is modern" },
      { trope: "Erased Heritage", id: "WOKE-026", category: "WOKE", location: "Throughout -- Seven Dwarfs replaced with CGI magical beings", authenticity: "Fabricated -- every version of Snow White features actual dwarfs" },
      { trope: "The Girl Boss (climax)", id: "WOKE-003", category: "WOKE", location: "Climax -- Snow White leads citizens in uprising, persuades guards through political speech", authenticity: "Fabricated -- no version includes a popular uprising" },
      { trope: "Anti-Western Revisionism", id: "WOKE-020", category: "WOKE", location: "Throughout -- Film treats 1937 original as problem to be corrected, Someday My Prince Will Come replaced", authenticity: "N/A -- metatextual trope about posture toward heritage" },
      { trope: "Monarchy Bad Democracy Good", id: "WOKE-015", category: "WOKE", location: "Climax -- Rebellion frames monarchy as tyranny, anti-monarchy subtext present", authenticity: "Fabricated -- the fairy tale has no political content" },
      { trope: "The Apology Film", id: "WOKE-028", category: "WOKE", location: "Entire film -- Cumulative effect reads as sustained apology for the 1937 original", authenticity: "N/A -- metatextual trope" },
      { trope: "True Love's Kiss", id: "TRADITIONAL-051", category: "TRADITIONAL", location: "Late third act -- Jonathan kisses Snow White, breaking the Sleeping Death spell", authenticity: "Authentic -- the fairy tale's most iconic moment preserved" },
      { trope: "Defense of the Innocent", id: "TRADITIONAL-045", category: "TRADITIONAL", location: "Early film -- Huntsman refuses to kill Snow White, mercy over duty", authenticity: "Authentic -- preserved from the original" },
      { trope: "Vanity as Vice", id: "TRADITIONAL-039", category: "TRADITIONAL", location: "Throughout -- Evil Queen's vanity is her defining sin and undoing", authenticity: "Authentic -- preserved from all versions of the fairy tale" },
      { trope: "Kindness as Power", id: "TRADITIONAL-033", category: "TRADITIONAL", location: "Climax -- Magic Mirror declares kindness and inner beauty make Snow White the fairest", authenticity: "Authentic -- preserved from original's core moral framework" }
    ]
  },
  {
    id: "captain-america-brave-new-world",
    slug: "captain-america-brave-new-world",
    title: "Captain America: Brave New World",
    year: 2025,
    type: "film",
    platform: "Theatrical",
    genre: "Action, Superhero",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "14 min",
    poster: "/images/posters/captain-america-brave-new-world.jpg",
    verdict: "WOKE",
    wokeScore: 8,
    tradScore: 5,
    authIndex: 65,
    scoreMargin: "-3 WOKE",
    wokeTrap: {
      present: true,
      degree: "partial",
      explanation: "More insidious than Snow White because it wraps progressive messaging inside a genuinely entertaining superhero framework. The racial subtext is present but not always front-and-center. Harrison Ford's charisma and Anthony Mackie's likability paper over a script that is fundamentally about a Black Captain America navigating a racist America.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: true,
      explanation: "The entertaining superhero framework and charismatic leads paper over persistent racial subtext and institutional evil framing. Conservative viewers who didn't watch Falcon and the Winter Soldier may not immediately clock the subtext."
    },
    creative_team: {
      director: { name: "Julius Onah", ideology: "PROGRESSIVE", profile: "Nigerian-American filmmaker. His most significant prior work, Luce, is explicitly about race in America. His selection to direct a Black Captain America film was intentional." },
      writer: { name: "Rob Edwards, Malcolm Spellman & Dalan Musson, Julius Onah & Peter Glanz", profile: "Committee screenplay with five credited writers. Spellman carried over from Falcon and the Winter Soldier is responsible for the MCU's most explicit engagement with race." },
      lead_producer: { name: "Kevin Feige", company: "Marvel Studios" },
      composer: { name: "Laura Karpman" },
      top_cast: [
        { name: "Anthony Mackie", role: "Sam Wilson / Captain America" },
        { name: "Harrison Ford", role: "President Thaddeus Ross / Red Hulk" },
        { name: "Giancarlo Esposito", role: "Sidewinder" },
        { name: "Tim Blake Nelson", role: "Samuel Sterns / The Leader" },
        { name: "Danny Ramirez", role: "Joaquin Torres / Falcon" }
      ],
      prediction: { verdict: "WOKE", confidence: "high" }
    },
    fidelity_casting: {
      score: "DIVERGENT",
      summary: "Sam Wilson as Captain America bypasses the more narratively logical choice of Bucky Barnes; supporting cast features heavy artificial diversity.",
      detailed_analysis: "The original Captain America is a white man from Brooklyn chosen for moral character. Sam Wilson in the comics eventually carries the shield, but the MCU's choice of Sam over Bucky Barnes was clearly influenced by diversity priorities. Mackie is excellent in the role. Ruth Bat-Seraph is stripped of most Israeli identity. Harrison Ford as Ross is excellent casting."
    },
    summary: {
      overall: "Captain America: Brave New World is a Frankenstein's monster of a movie, stitched together from at least three different scripts, multiple rounds of reshoots, and the remnants of a 2008 plotline nobody was asking to resolve. The core problem isn't wokeness. It's competence. The film doesn't know what it wants to be.\n\nAnthony Mackie deserves better. The man is genuinely charismatic, physically committed, and capable of carrying a franchise. Harrison Ford brings exactly what you'd expect: gruff, commanding, and instantly credible as a president with secrets. His transformation into Red Hulk is the film's best visual sequence, and the scene where Sam talks him down by reminding him of cherry blossoms with his daughter Betty is the emotional high point.\n\nThe action is where things go sideways. Sam Wilson does not have super soldier serum, yet he survives G-forces that should liquify him and holds his own against a rampaging Hulk. Shira Haas as Ruth Bat-Seraph is roughly five feet tall and the film expects us to believe she can launch two-hundred-pound men across rooms. Tim Blake Nelson's Leader looks like a radioactive sweet potato.\n\nThe racial subtext deserves honest assessment. Isaiah Bradley, the Black super soldier experimented on by the U.S. government, is a recurring presence. When President Ross calls Sam \"son,\" Sam reacts with tension clearly coded as racial. The Japanese Prime Minister's line about America being \"a country used to taking what it wants\" is presented as righteous truth. None of this is fabricated in isolation, but the cumulative effect creates a political subtext that conservative viewers will find impossible to ignore.\n\nThe film grossed $415 million worldwide, technically profitable but deeply disappointing for a Captain America film. Conservative viewers who can stomach the racial subtext will find a serviceable superhero film carried by two charismatic leads. The traditional elements, including Sam's loyalty, the father-daughter reconciliation, and accountability for leaders, are genuine but insufficient to overcome the film's structural problems and ideological freight.",
      adultInsight: "Conservative adult viewers should approach Brave New World as a deeply flawed but occasionally entertaining superhero film that carries persistent racial subtext. The film's strongest moments are its most traditional: Sam's genuine heroism, the Ross-Betty reconciliation, and the theme of accountability for leaders. For viewers who can compartmentalize, Mackie and Ford deliver genuinely good performances worth seeing. For viewers who found Falcon and the Winter Soldier's racial themes off-putting, Brave New World offers more of the same, just slightly quieter.",
      parentalGuidance: "Rated PG-13 for intense sequences of violence and action. Standard MCU fare: gunfights, explosions, superhero combat. The Red Hulk transformation may frighten younger children. A character is killed and another seriously injured. No sexual content, substance use, or strong language. For conservative parents, the racial subtext is worth discussing with older children. The Isaiah Bradley storyline presents historically grounded material with modern progressive framing. The film presents a U.S. president who is literally a monster underneath his human exterior. Appropriate for children 10 and up. Ideological discussion recommended for 12 and up."
    },
    tropeAudit: [
      { trope: "The Victimhood Meritocracy", id: "WOKE-009", category: "WOKE", location: "Throughout -- Isaiah Bradley's storyline positions America's treatment of Black super soldiers as defining moral failure", authenticity: "Mixed -- based on real history and comics canon but emphasis is editorially modern" },
      { trope: "Institutional Evil", id: "WOKE-004", category: "WOKE", location: "Throughout -- Government imprisoned and experimented on Bradley, imprisoned Sterns, President is literally a monster", authenticity: "Mixed -- real institutions have real failures but totality of corruption is editorial" },
      { trope: "The Girl Boss", id: "WOKE-003", category: "WOKE", location: "Multiple action sequences -- Five-foot-tall Ruth Bat-Seraph launches 200-pound men across rooms", authenticity: "Fabricated -- human biomechanics do not work this way" },
      { trope: "Diversity Retrofit", id: "WOKE-012", category: "WOKE", location: "Throughout -- Supporting cast assembled with visible demographic quotas", authenticity: "Mixed" },
      { trope: "Anti-Western Revisionism", id: "WOKE-020", category: "WOKE", location: "Summit sequence -- Japanese PM declares America is a country used to taking what it wants", authenticity: "Mixed -- critique has real-world basis but presented one-dimensionally" },
      { trope: "The Bigoted Traditionalist", id: "WOKE-008", category: "WOKE", location: "Son scene -- Ross calling Sam son charged with racial significance by the writers", authenticity: "Mixed -- the scene's racial coding is the writers' editorial choice" },
      { trope: "The Legacy Replacement", id: "WOKE-023", category: "WOKE", location: "Entire film -- Sam replaces Steve Rogers with race positioned as central to his experience", authenticity: "Mixed -- Sam was Captain America in comics but MCU choice influenced by diversity priorities" },
      { trope: "Redeemed Criminal Systemic", id: "WOKE-019", category: "WOKE", location: "Sterns storyline -- Villain partially sympathetic because government broke its promise", authenticity: "Mixed" },
      { trope: "Defense of the Innocent", id: "TRADITIONAL-045", category: "TRADITIONAL", location: "Throughout -- Sam shields civilians, intercepts planes, risks his life without superpowers", authenticity: "Authentic -- Captain America's core identity preserved" },
      { trope: "The Self-Sacrificing Hero", id: "TRADITIONAL-026", category: "TRADITIONAL", location: "Multiple sequences -- Sam risks mortal danger without super soldier protection, Torres critically injured", authenticity: "Authentic" },
      { trope: "Father-Daughter Reconciliation", id: "TRADITIONAL-044", category: "TRADITIONAL", location: "Climax -- Sam talks Red Hulk down by reminding Ross of cherry blossoms with Betty", authenticity: "Authentic -- built on seventeen years of MCU continuity" },
      { trope: "Accountability for Leaders", id: "TRADITIONAL-041", category: "TRADITIONAL", location: "Final act -- Ross resigns and has himself incarcerated, accepts consequences", authenticity: "Authentic" },
      { trope: "Industry and Perseverance", id: "TRADITIONAL-041", category: "TRADITIONAL", location: "Throughout -- Sam perseveres without superpowers, refuses the serum as principled choice", authenticity: "Authentic" }
    ]
  },
  {
    id: "a-minecraft-movie",
    slug: "a-minecraft-movie",
    title: "A Minecraft Movie",
    year: 2025,
    type: "film",
    platform: "Theatrical",
    genre: "Adventure, Comedy",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "12 min",
    poster: "/images/posters/a-minecraft-movie.jpg",
    verdict: "MILD WOKE",
    wokeScore: 5,
    tradScore: 4,
    authIndex: 68,
    scoreMargin: "-1 WOKE",
    wokeTrap: {
      present: true,
      degree: "mild",
      explanation: "Presents itself as harmless family entertainment. The woke elements are baked into the character dynamics rather than the plot. No overt political messaging. What there is, reliably and predictably, is the women are competent, men are idiots formula that has become Hollywood's default setting. Kids won't notice it. Parents will.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: true,
      explanation: "Harmless family entertainment packaging with subtle but persistent gender-competence messaging baked into character dynamics. The kind of woke that operates below the radar."
    },
    creative_team: {
      director: { name: "Jared Hess", ideology: "TRADITIONAL", profile: "Known for Napoleon Dynamite, a loving portrait of rural American weirdness with deeply traditional sensibilities. The film's woke elements come from the studio/writing committee, not his directorial vision." },
      writer: { name: "Chris Bowman, Hubbel Palmer, Neil Widener, Gavin James, Chris Galletta", profile: "Committee screenplay from five writers. Nobody is responsible for the final product, and Hollywood's institutional progressivism fills the gaps." },
      lead_producer: { name: "Warner Bros. / Mojang Studios", company: "Warner Bros. Pictures" },
      composer: { name: "Various" },
      top_cast: [
        { name: "Jason Momoa", role: "Garrett 'The Garbage Man' Garrison" },
        { name: "Jack Black", role: "Steve" },
        { name: "Emma Myers", role: "Natalie" },
        { name: "Danielle Brooks", role: "Dawn" },
        { name: "Sebastian Hansen", role: "Henry" }
      ],
      prediction: { verdict: "NEUTRAL", confidence: "medium" }
    },
    fidelity_casting: {
      score: "LOOSE",
      summary: "Characters are original creations loosely inspired by the game. Steve (Jack Black) is the only character from the game itself.",
      detailed_analysis: "The film creates mostly original characters. Steve is transformed into Jack Black doing Jack Black things. The remaining cast plays original characters with no game counterparts."
    },
    summary: {
      overall: "A Minecraft Movie is not a good film. It is not a particularly bad one either. It is a loud, colorful, expensive screensaver with Jack Black yelling his way through two hours and Jason Momoa trying his hardest to make man-child former arcade champion work as a character. Kids will enjoy it. Adults will survive it. Nobody will remember it in six months.\n\nJason Momoa gives it everything he has got, and the guy shows surprising range as Garrett. He is committed, physical, and the closest thing the film has to genuine emotional investment. But the script wastes him. Jack Black is Jack Black. If that is what you want, you will get it. His Steve is a one-note performance pitched at stadium volume.\n\nThe film's most fundamental problem is that the writers had no idea how to build a narrative from Minecraft's open-ended gameplay. It is a theme park ride, not a movie. There is no narrative logic connecting the set pieces, no character development that could not be summarized on a Post-it note.\n\nThe CGI Overworld is the film's strongest element. The translation of Minecraft's blocky aesthetic into live-action/CGI hybrid is technically impressive. Emma Myers and Danielle Brooks play the two female leads and are the vehicle for the film's most persistent woke element: the competent-women, incompetent-men dynamic. The men get kicked in embarrassing places and act like children. The women are composed, competent, and in control.\n\nDespite its problems, A Minecraft Movie made enormous money at the box office, driven by the game's massive global fanbase. This is IP-driven economics, not quality filmmaking. For conservative families, A Minecraft Movie is mostly harmless. The cinematic equivalent of a fast-food meal. It will not hurt you. It will not nourish you. You will forget about it by morning.",
      adultInsight: "Conservative adult viewers should approach A Minecraft Movie as a mediocre family film with subtle but persistent gender-role messaging. It is not aggressively ideological. It will not indoctrinate your children. It is another data point in Hollywood's campaign to establish competent women, incompetent men as the default framework for family entertainment. If your kids want to see it because they love Minecraft, let them. The content is genuinely family-friendly and the woke elements are the ambient kind.",
      parentalGuidance: "Rated PG and one of the most family-friendly films in this batch. Violence is cartoonish and game-faithful with enemies transforming into steaks when defeated. The flying scene includes mildly suggestive dialogue that most children will miss. Minimal language with tool bag and hell the strongest words. No substance use. The Ender Dragon may frighten very young children under 5. Appropriate for children 5 and up. No ideological discussion necessary for younger viewers."
    },
    tropeAudit: [
      { trope: "Smart Women Dumb Men", id: "WOKE-006", category: "WOKE", location: "Throughout -- Women dispatch zombies casually while men act like children", authenticity: "Fabricated -- the Minecraft game has no gendered competence dynamic" },
      { trope: "The Emasculated Male", id: "WOKE-010", category: "WOKE", location: "Multiple scenes -- Momoa repeatedly emasculated for comedy despite being physically imposing", authenticity: "Fabricated" },
      { trope: "The Absent Father", id: "WOKE-007", category: "WOKE", location: "Background -- Father abandoned Henry and Natalie, mother is mourned", authenticity: "Original to the film" },
      { trope: "Homoerotic Comedy", id: "WOKE-025", category: "WOKE", location: "Flying sequence -- Suggestive dialogue added to physical comedy between Black and Momoa", authenticity: "Original to the film" },
      { trope: "Infallible Youth", id: "WOKE-016", category: "WOKE", location: "Throughout -- Adults defined by failings while youngest character Henry is most sensible", authenticity: "Genre convention" },
      { trope: "The Journey Home", id: "TRADITIONAL-048", category: "TRADITIONAL", location: "Entire film -- Classical homecoming narrative from the Odyssey to Wizard of Oz", authenticity: "Authentic -- classical storytelling" },
      { trope: "Industry and Creativity", id: "TRADITIONAL-041", category: "TRADITIONAL", location: "Throughout -- Characters survive by learning to craft, build, and create", authenticity: "Authentic -- Minecraft's core value honestly translated" },
      { trope: "Sibling Loyalty", id: "TRADITIONAL-045", category: "TRADITIONAL", location: "Henry and Natalie's bond -- Genuine emotional thread of sibling care", authenticity: "Authentic" },
      { trope: "Teamwork and Fellowship", id: "TRADITIONAL-046", category: "TRADITIONAL", location: "Throughout -- Misfits learn to work together, individual weaknesses compensated by collective strength", authenticity: "Authentic" }
    ]
  },
  {
    id: "thunderbolts",
    slug: "thunderbolts",
    title: "Thunderbolts*",
    year: 2025,
    type: "film",
    platform: "Theatrical",
    genre: "Action, Superhero",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "14 min",
    poster: "/images/posters/thunderbolts.jpg",
    verdict: "WOKE",
    wokeScore: 7,
    tradScore: 5,
    authIndex: 66,
    scoreMargin: "-2 WOKE",
    wokeTrap: {
      present: true,
      degree: "partial",
      explanation: "Presents itself as a gritty antihero team-up. What the trailers did not emphasize is that this is fundamentally a Yelena Belova vehicle in which every female character is hyper-competent and snarky while every male character exists to be emasculated, mocked, or emotionally broken. The girl-boss energy is woven into every interaction.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: true,
      explanation: "Marketed as a rough-edged antihero film but actually a two-hour exercise in female superiority and male inadequacy, dressed up with enough explosions to disguise the agenda."
    },
    creative_team: {
      director: { name: "Jake Schreier", ideology: "NEUTRAL", profile: "Indie filmmaker making his blockbuster debut. Robot & Frank was charming and traditional. The film's ideology comes from Marvel, not Schreier." },
      writer: { name: "Eric Pearson & Joanna Calo", profile: "Pearson wrote Thor: Ragnarok and Black Widow. Calo is best known for The Bear. Pearson is a reliable studio hand; Calo likely brought the character-study ambitions." },
      lead_producer: { name: "Kevin Feige", company: "Marvel Studios" },
      composer: { name: "Various" },
      top_cast: [
        { name: "Florence Pugh", role: "Yelena Belova" },
        { name: "Sebastian Stan", role: "Bucky Barnes" },
        { name: "David Harbour", role: "Red Guardian" },
        { name: "Wyatt Russell", role: "John Walker / U.S. Agent" },
        { name: "Lewis Pullman", role: "Bob Reynolds / Sentry" }
      ],
      prediction: { verdict: "WOKE", confidence: "medium-high" }
    },
    fidelity_casting: {
      score: "SHIFTED",
      summary: "The MCU version centers characters chosen from recent MCU projects rather than faithfully adapting a specific comics roster.",
      detailed_analysis: "Yelena Belova as Black Widow successor is faithful to comics concept. Bucky Barnes is faithful but badly underserved. Red Guardian is reimagined as buffoonish-but-loving. The Sentry is reduced from one of Marvel's most complex characters to a therapy narrative."
    },
    summary: {
      overall: "Thunderbolts asks you to care about six characters you either forgot existed or could not name at gunpoint. The question is whether it delivers a story worth telling. The answer, with significant reservations, is: sort of.\n\nDavid Harbour is having the time of his life as Red Guardian, and his energy is infectious. He is the oxygen that keeps the audience breathing. Florence Pugh is a genuinely exceptional actress, but the film surrounds her talent with a framework that undercuts it. Yelena is compelling not because she earns our respect through struggle but because the film has been engineered to ensure she is the most competent person in every room.\n\nSebastian Stan's Bucky Barnes, a character with one of the most compelling arcs in the MCU, is reduced to an afterthought. He shows up, gets beaten with his own metal arm, and serves as emotional furniture. Wyatt Russell's U.S. Agent has been systematically dismantled into a loudmouth punchline. Florence Pugh literally separates two bickering men and the audience is meant to cheer the woman putting the men in their place.\n\nThe Sentry storyline is the film's most interesting element and most frustrating. One of Marvel's most powerful beings is ultimately defeated by being talked through his feelings. The action pits street-level characters against a Superman-level being, and they bring knives.\n\nThe film's tonal identity is its deepest flaw. It wants to be a character study about broken people finding connection, a snarky action comedy, a Sentry introduction, and a Valentina political thriller all at once. These ambitions compete rather than complement. The result is too depressing to be fun, too jokey to be dramatic, and too rushed to be epic.\n\nFor conservative viewers, Thunderbolts is a representative example of the MCU's current priorities: female characters elevated at male characters' expense, emotional vulnerability treated as the highest virtue, and traditional heroism replaced by group therapy. The traditional elements that exist, Red Guardian's paternal instincts, Bucky's quiet loyalty, misfits finding family, are genuine but perpetually undermined.",
      adultInsight: "Conservative adult viewers should approach Thunderbolts understanding it is a moderately entertaining but deeply flawed MCU entry that treats its male characters as second-class citizens. David Harbour's performance and the found-family theme provide enough entertainment value for a passable watch. The more instructive experience is to notice what the MCU values now versus Phase One: the shift from heroism-through-excellence to heroism-through-vulnerability is the MCU's most significant ideological evolution, and Thunderbolts is its purest expression.",
      parentalGuidance: "Rated PG-13 for action violence, language, and thematic elements. Extended fight sequences, characters getting beaten seriously, building destruction. Moderate language. No sexual content or substance use. Depression, loneliness, trauma, and abandonment are major themes. The Sentry is explicitly depicted as mentally ill. The tonal darkness and thematic weight make this unsuitable for younger MCU fans. 12 and up. For teens, the film could prompt discussion about how Hollywood depicts masculinity and whether the men are broken, women are strong framework reflects reality or an agenda."
    },
    tropeAudit: [
      { trope: "The Girl Boss (pervasive)", id: "WOKE-003", category: "WOKE", location: "Throughout -- Every female character snarky and hyper-competent, every male character a punchline", authenticity: "Fabricated -- comics Thunderbolts had no such gender dynamic" },
      { trope: "The Emasculated Male", id: "WOKE-010", category: "WOKE", location: "Throughout -- Bucky beaten with own arm, U.S. Agent a moron, Red Guardian a lovable idiot, Sentry a depressed wreck", authenticity: "Divergent from source material" },
      { trope: "The Girl Boss (combat)", id: "WOKE-003", category: "WOKE", location: "Action sequences -- Yelena of average build tosses 200-pound men, courtesy fighting choreography", authenticity: "MCU power scaling exaggerated beyond source material" },
      { trope: "The Bad Father", id: "WOKE-007", category: "WOKE", location: "Throughout -- Red Guardian absent and unreliable, U.S. Agent explicitly a bad father", authenticity: "Mixed -- Red Guardian in comics is complicated but MCU emphasis on paternal failure is editorial" },
      { trope: "Therapy as Heroism", id: "WOKE-029", category: "WOKE", location: "Sentry confrontation -- Most powerful being stopped by getting in touch with his feelings", authenticity: "Divergent -- comics Sentry stories don't resolve through group therapy" },
      { trope: "Institutional Evil", id: "WOKE-004", category: "WOKE", location: "Valentina storyline -- CIA director assembles team as death trap, government is primary antagonist", authenticity: "Mixed -- government distrust has been a Marvel theme since the 1970s" },
      { trope: "The Legacy Replacement", id: "WOKE-023", category: "WOKE", location: "Entire film -- Yelena as Black Widow successor, Thunderbolts positioned as New Avengers replacing legacy heroes", authenticity: "Mixed -- rosters change in comics but MCU approach is demographic" },
      { trope: "Found Family", id: "TRADITIONAL-046", category: "TRADITIONAL", location: "Throughout -- Broken people finding connection, Red Guardian names them with paternal pride", authenticity: "Authentic -- classical narrative structure" },
      { trope: "The Self-Sacrificing Hero", id: "TRADITIONAL-026", category: "TRADITIONAL", location: "Multiple sequences -- Team risks lives for each other, Red Guardian willing to sacrifice for strangers", authenticity: "Authentic" },
      { trope: "Paternal Love", id: "TRADITIONAL-044", category: "TRADITIONAL", location: "Red Guardian's storyline -- Love for Yelena is real and unconditional despite buffoonery", authenticity: "Authentic -- Harbour's performance sells it" },
      { trope: "Redemption", id: "TRADITIONAL-047", category: "TRADITIONAL", location: "Throughout -- Every member seeking redemption for their past, narrative spine of the film", authenticity: "Authentic" },
      { trope: "Loyalty Under Fire", id: "TRADITIONAL-041", category: "TRADITIONAL", location: "Second and third acts -- Team chooses to stand together when running would be rational", authenticity: "Authentic" }
    ]
  }
];

// Read existing reviews
const filePath = 'src/data/reviews.json';
const existing = JSON.parse(fs.readFileSync(filePath, 'utf8'));

// Deduplicate by slug
const existingSlugs = new Set(existing.map(r => r.slug));
const toAdd = newReviews.filter(r => !existingSlugs.has(r.slug));

// Add to front
const combined = [...toAdd, ...existing];
fs.writeFileSync(filePath, JSON.stringify(combined, null, 2));
console.log(`Added ${toAdd.length} new reviews. Total: ${combined.length}`);
