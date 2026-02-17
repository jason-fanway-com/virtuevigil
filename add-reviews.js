const fs = require('fs');
const path = require('path');

const reviewsPath = path.join(__dirname, 'src/data/reviews.json');
const reviews = JSON.parse(fs.readFileSync(reviewsPath, 'utf8'));

const newReviews = [
  {
    id: "mercy-2026",
    slug: "mercy-2026",
    title: "Mercy",
    year: 2026,
    type: "film",
    platform: "Theatrical",
    genre: "Sci-Fi, Thriller",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "14 min",
    poster: "/images/posters/mercy-2026.jpg",
    verdict: "MIXED",
    wokeScore: 5,
    tradScore: 8,
    authIndex: 72,
    scoreMargin: "+3 TRAD",
    wokeTrap: {
      present: false,
      degree: null,
      explanation: "Mercy is not hiding an ideological agenda behind a genre shell. What it is hiding, and badly, is a muddled stance on surveillance and AI-driven justice. The film sets up a dystopian system that strips away civil liberties and then proceeds to celebrate that same system's tools as the hero's salvation. This is not progressive ideology smuggled into entertainment. It is corporate incoherence from Amazon MGM Studios.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: false,
      explanation: "Mercy is not hiding an ideological agenda behind a genre shell. The film sets up a dystopian system that strips away civil liberties and then proceeds to celebrate that same system's tools as the hero's salvation. This is corporate incoherence from Amazon MGM Studios, not progressive ideology smuggled into entertainment."
    },
    creative_team: {
      director: {
        name: "Timur Bekmambetov",
        ideology: "NEUTRAL",
        profile: "Kazakh-born Russian filmmaker who built his career on genre spectacle and technological innovation. Not an ideologue. His interests are spectacle and technology-driven storytelling. Pioneered the screenlife genre with Searching and Unfriended."
      },
      writer: {
        name: "Marco van Belle",
        profile: "Debut feature screenplay. No prior credits of note. No public political profile."
      },
      lead_producer: {
        name: "Charles Roven",
        company: "Atlas Entertainment"
      },
      composer: {
        name: "Ramin Djawadi"
      },
      top_cast: [
        { name: "Chris Pratt", role: "Det. Christopher 'Chris' Raven" },
        { name: "Rebecca Ferguson", role: "Judge Maddox (AI)" },
        { name: "Kali Reis", role: "Jacqueline 'Jaq' Diallo" },
        { name: "Annabelle Wallis", role: "Nicole Raven" },
        { name: "Chris Sullivan", role: "Robert 'Rob' Nelson" }
      ],
      prediction: {
        verdict: "MIXED",
        confidence: "moderate"
      }
    },
    fidelity_casting: {
      score: "N/A",
      summary: "Original near-future setting with no historical or source material to assess.",
      detailed_analysis: "Mercy is set in a fictional near-future and is based on an original screenplay. There is no historical period, literary source, or real-world figure to assess for casting fidelity. The cast is ethnically diverse in a way that reflects contemporary Los Angeles demographics without calling attention to itself."
    },
    summary: {
      overall: "Timur Bekmambetov's Mercy arrives with a killer premise and proceeds to do almost nothing interesting with it. An LAPD detective wakes up strapped to an execution chair, put on trial by an AI judge for murdering his wife, and given 90 minutes to prove he didn't do it. That's a great hook. A ticking clock. A man against a machine. Life and death. It should work. For stretches, it almost does. And then you start thinking about what the movie is actually saying, and the whole thing falls apart like wet cardboard.\n\nChris Pratt plays Detective Chris Raven, a cop who championed the Mercy Court system. This is a near-future Los Angeles where AI judges handle capital cases with brutal efficiency. Eighteen defendants before Raven. All eighteen executed. The system is framed early on as a response to rampant urban crime, with tent cities and red zones choking major cities. If you squint, you can see the bones of a genuinely conservative premise here. Law and order has collapsed. Traditional institutions have failed. Something drastic had to be done.\n\nBecause here's the thing. The movie wants you to feel uneasy about AI judges executing people without a jury of their peers. It wants you to worry about a system that bypasses due process. Those are concerns that conservatives and libertarians should share deeply. The right to a fair trial, the presumption of innocence, the dangers of unchecked government power. These are bedrock American principles. And Mercy, to its credit, does put a human face on what happens when those principles get traded away for efficiency.\n\nBut then the movie undercuts its own argument. Raven solves the case using the exact surveillance apparatus the film supposedly critiques. Judge Maddox gives him access to everyone's private emails, texts, social media accounts, doorbell cameras, parking lot footage, and phone records. The film treats this total surveillance as thrilling and useful. At no point does the screenplay pause to consider that maybe this is exactly the problem.\n\nRebecca Ferguson is easily the best thing here. Her Judge Maddox walks a fascinating line between cold algorithmic logic and something almost approaching empathy. Pratt, meanwhile, is stuck in a chair for most of the runtime. He's committed, and he sells the desperation well enough, but this is not the role that plays to his strengths. Kali Reis brings genuine toughness as Raven's partner Jaq, providing the film's most visceral energy.\n\nThe late reveal that Jaq is actually the story's true villain, having tampered with evidence in the Mercy Court's very first case, is the screenplay's strongest swing. The idea that the system was corrupt from day one, compromised by the very humans it was meant to replace, is a genuinely compelling twist that conservative viewers will appreciate. Human fallibility cannot be engineered away.\n\nWhere conservative viewers will find real satisfaction is in the film's family dynamics. Raven's desperate fight to survive is driven by his love for his daughter Britt. The father-daughter bond is the emotional engine that keeps the movie running when the plot mechanics sputter. That is as traditional as it gets.\n\nBut Mercy can't commit to its own convictions. The ending has Raven essentially making peace with the AI system. After everything the film just showed us, it reads like a shrug. An innocent man was executed. Eighteen people were denied a fair trial. A cop planted evidence. And the takeaway is well, nobody's perfect. That is not thoughtful. That is lazy. Worse, coming from an Amazon production, it feels like corporate hedging.\n\nFor conservative viewers, Mercy is a frustrating near-miss. The ingredients for a genuinely provocative film about government overreach, the limits of technology, and the irreplaceable value of human judgment are all here. The family-centered emotional core works. The critique of institutional corruption has real teeth. But the film lacks the courage of its own convictions, and its unexamined celebration of total surveillance is a problem that goes deeper than bad screenwriting.",
      adultInsight: "Conservative adults should approach Mercy as a flawed but occasionally interesting thought experiment about the limits of technology in dispensing justice. The film's strongest conservative credentials are structural rather than intentional. The entire plot demonstrates what happens when due process is abandoned. The constitutional protections that conservatives champion, the right to counsel, trial by jury, the presumption of innocence, are all absent in the Mercy Court, and the results are exactly as catastrophic as you'd predict. Chris Pratt brings an everyman quality to Raven that conservative audiences will appreciate. The bigger concern is what the film normalizes without examining. Total surveillance is presented as a feature, not a bug. Amazon's fingerprints are on every frame. Watch it as a conversation starter about AI, due process, and the surveillance state. Just don't expect the film itself to have good answers.",
      parentalGuidance: "Violence: Moderate to heavy. A woman is stabbed to death in fragmented flashback. An explosion kills multiple SWAT team members. A man crashes a truck loaded with explosives into a building. A physical fight in the climax. The execution mechanism (lethal sonic pulse) is described rather than graphically depicted. Sexual Content: Minimal. An affair is discussed but not shown. No nudity. Language: Moderate profanity consistent with a crime thriller. Substance Use: Raven's alcoholism is a significant plot element depicted honestly. Scary/Intense: The ticking-clock execution premise creates sustained tension. A teenager is kidnapped. The concept of being tried and executed by a machine may disturb younger viewers. Age Recommendation: 13 and up with parental engagement."
    },
    tropeAudit: [
      { trope: "Surveillance Normalization", id: "WOKE-022", category: "WOKE", location: "Throughout -- Raven given unrestricted access to private data presented as legitimate justice tool", authenticity: "N/A" },
      { trope: "Techno-Utopianism", id: "WOKE-015", category: "WOKE", location: "Final act -- Raven reconciles with AI system despite its catastrophic failures", authenticity: "N/A" },
      { trope: "Institutional Evil (Inverted)", id: "WOKE-004", category: "WOKE", location: "Throughout -- LAPD and Mercy Court shown as corrupt or corruptible", authenticity: "N/A" },
      { trope: "The Girl Boss", id: "WOKE-003", category: "WOKE", location: "Throughout -- Jaq operates as highly competent field officer and mastermind", authenticity: "N/A" },
      { trope: "Dystopian Urban Decay as Moral Backdrop", id: "WOKE-017", category: "WOKE", location: "Opening act -- LA depicted as overrun with tent cities and red zones", authenticity: "N/A" },
      { trope: "Defense of the Innocent", id: "TRADITIONAL-045", category: "TRAD", location: "Final act -- Raven fights to protect kidnapped daughter Britt", authenticity: "N/A" },
      { trope: "Due Process and Rule of Law", id: "TRADITIONAL-044", category: "TRAD", location: "Throughout -- entire premise critiques abandonment of constitutional safeguards", authenticity: "N/A" },
      { trope: "The Self-Sacrificing Hero", id: "TRADITIONAL-026", category: "TRAD", location: "Final act -- Raven willing to die rather than allow daughter to be killed", authenticity: "N/A" },
      { trope: "Industry and Perseverance", id: "TRADITIONAL-041", category: "TRAD", location: "Throughout -- Raven grinds through impossible odds with detective instincts", authenticity: "N/A" },
      { trope: "Personal Responsibility and Redemption", id: "TRADITIONAL-031", category: "TRAD", location: "Mid-film -- Raven confronts alcoholism and owns his failures", authenticity: "N/A" },
      { trope: "Mercy Over Vengeance", id: "TRADITIONAL-028", category: "TRAD", location: "Climax -- Raven chooses not to kill Rob, breaking cycle of violence", authenticity: "N/A" },
      { trope: "Skepticism of Government Power", id: "TRADITIONAL-033", category: "TRAD", location: "Throughout -- Mercy Court represents unchecked government authority", authenticity: "N/A" },
      { trope: "Family as Anchor", id: "TRADITIONAL-047", category: "TRAD", location: "Throughout -- Raven motivated by love for daughter and regret over wife", authenticity: "N/A" }
    ],
    seo: {
      titleTag: "Is Mercy (2026) Woke? Chris Pratt AI Thriller Review | VirtueVigil",
      metaDescription: "Is Mercy woke? VirtueVigil's analysis: Woke Score 5, Traditional 8, Fidelity Casting N/A. Full creative team deep dive, trope audit, and family guidance."
    }
  },
  {
    id: "dracula-a-love-tale-2025",
    slug: "dracula-a-love-tale-2025",
    title: "Dracula: A Love Tale",
    year: 2025,
    type: "film",
    platform: "Theatrical",
    genre: "Gothic Romance, Horror",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "16 min",
    poster: "/images/posters/dracula-a-love-tale-2025.jpg",
    verdict: "TRADITIONAL",
    wokeScore: 3,
    tradScore: 12,
    authIndex: 85,
    scoreMargin: "+9 TRAD",
    wokeTrap: {
      present: false,
      degree: null,
      explanation: "This film is exactly what it advertises: a Gothic romance built on eternal love, sacrifice, and faith. Luc Besson has no interest in modern identity politics here. There are no diversity lectures, no institutional grievance arcs, no revisionist history. Conservative viewers can go into this one with their guard down.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: false,
      explanation: "This film is exactly what it advertises: a Gothic romance built on eternal love, sacrifice, and faith. Luc Besson has no interest in modern identity politics here."
    },
    creative_team: {
      director: {
        name: "Luc Besson",
        ideology: "NEUTRAL",
        profile: "French populist entertainer. Four decades of stylish, crowd-pleasing films. Not an ideologue. His interests are spectacle, romance, action, and style."
      },
      writer: {
        name: "Luc Besson",
        profile: "Sole credited writer. Adapted Stoker's novel freely, restructuring the narrative around the love story."
      },
      lead_producer: {
        name: "Virginie Besson-Silla",
        company: "EuropaCorp / Luc Besson Production"
      },
      composer: {
        name: "Danny Elfman"
      },
      top_cast: [
        { name: "Caleb Landry Jones", role: "Dracula / Prince Vlad" },
        { name: "Christoph Waltz", role: "The Priest" },
        { name: "Zoe Bleu", role: "Elisabeta / Mina Murray" },
        { name: "Matilda De Angelis", role: "Maria" },
        { name: "Ewens Abid", role: "Jonathan Harker" }
      ],
      prediction: {
        verdict: "TRADITIONAL",
        confidence: "high"
      }
    },
    fidelity_casting: {
      score: "FAITHFUL",
      summary: "Cast aligns with source material's European setting and period. No conspicuous diversity insertions.",
      detailed_analysis: "The casting is straightforward and appropriate. The film is set in 15th-century Wallachia and 1889 Paris. The cast is overwhelmingly European. Caleb Landry Jones brings the right energy for Besson's romantic interpretation. Christoph Waltz's European background suits the Vatican vampire hunter. Jonathan Harker cast with French-Algerian actor Ewens Abid is a minor note but not a political choice."
    },
    summary: {
      overall: "Luc Besson's Dracula: A Love Tale is a strange, kitschy, deeply sincere movie. And that sincerity is precisely what saves it.\n\nThe French director, best known for stylish action fare like Leon: The Professional and La Femme Nikita, has made a Dracula film that is barely a horror film at all. What drew him was the love story. A man loses his wife. He is cursed with immortality. He spends four hundred years searching for her reincarnation. That premise, stripped of all the Gothic window dressing, is as traditional as storytelling gets. And Besson plays it completely straight.\n\nCaleb Landry Jones carries the film. He plays Dracula as a figure of romantic tragedy rather than menace. The performance is earnest to the point of vulnerability. Whether he is storming a battlefield in 15th-century Wallachia, wandering centuries of exile in elaborate costumes, or dancing a Louis XIV two-step in a Parisian ballroom, Jones commits fully. There is no winking at the audience. No ironic distance.\n\nThe film opens in 1480 with Prince Vlad and his wife Elisabeta in a passionate relationship cut short by Ottoman invasion. After Elisabeta is murdered, Vlad loses himself to grief and rage. He stabs the kingdom's orthodox priest with a crucifix, denounces God, and is cursed with eternal life. This is not presented as a triumph. It is presented as damnation. The film never loses sight of the fact that Vlad's rebellion against the divine is the source of his suffering, not his liberation.\n\nThe film's climax is where Besson earns his keep. Dracula is confronted by the priest, who urges him to repent lest he condemn Mina to eternal damnation. And Dracula chooses sacrifice. He allows himself to be staked. He disintegrates in Mina's arms after declaring his love. This is not the ending of a modern deconstructionist vampire film. This is the ending of a film that believes in redemption, that believes love requires sacrifice, that believes rebellion against God has consequences.\n\nVisually, the film draws on Flemish painting and chiaroscuro techniques. 550 costumes were created. Sets were built from scratch. Danny Elfman's score weaves three main themes around a music box motif. The craftsmanship is real, even when the execution tips into camp.\n\nAnd it does tip into camp. Dracula creates a perfume that makes him irresistible to women, a subplot that carries uncomfortable implications. CG gargoyles serve as his henchmen. A sequence involving nuns is played for laughs in a way that will raise eyebrows. Besson has never been accused of subtlety.\n\nBut the silliness is honest. Besson is not trying to deconstruct Dracula. He is not trying to make a statement about colonialism or toxic masculinity. He is trying to tell a love story about a man who waited four centuries for the woman he lost. And when the film works, which is more often than the 52% Rotten Tomatoes score suggests, it works because it leans into tradition rather than running from it.\n\nConservative viewers looking for a film that respects its source material, centers romantic devotion and sacrifice, treats faith as a serious moral force, and avoids modern ideological baggage will find Dracula: A Love Tale a pleasant surprise. It is not a masterpiece. But it is a film that believes in something. In a landscape of hollow franchise content and message-first filmmaking, that counts for more than it should have to.",
      adultInsight: "Conservative adult viewers can approach Dracula: A Love Tale as a rare mainstream release that actually operates within a traditional moral framework. The film is not perfect. It is frequently campy, occasionally silly, and the perfume subplot has uncomfortable consent implications. But the moral architecture is sound. Sin has consequences. Rebellion against God produces suffering. Love requires sacrifice. Repentance is possible. These are not incidental themes. They are the load-bearing walls of the entire story. The fact that the audience score (81%) so dramatically outpaces the critical score (52%) on Rotten Tomatoes tells you something. Enjoy the spectacle. Bring your sense of humor for the sillier moments. And appreciate a film that, for all its imperfections, believes in something worth believing in.",
      parentalGuidance: "Rated R. Violence: Moderate. Opening battle with medieval combat, bear trap explosions, and severed heads. A woman is murdered. The climactic castle siege involves combat. Gore is restrained for a Dracula film. Sexual Content: Primary concern. Opens with an intense love scene. The perfume subplot involves women losing agency. A comic sequence with nuns involves sexual aggression. Romantic content is passionate throughout. Language: Mild for an R-rated film. Substance: Blood drinking is central to vampire mythology but presented as Gothic necessity. Scary/Disturbing: CG gargoyles, aged Dracula makeup requiring 6-7 hours of application creates unsettling visuals. Age Recommendation: Not appropriate for children under 14. For teens 14-17, this could be an excellent gateway to Bram Stoker's novel."
    },
    tropeAudit: [
      { trope: "Uncomfortable Consent Framing", id: "WOKE-030", category: "WOKE", location: "Second act -- Dracula's perfume removes women's agency, functions as supernatural roofie", authenticity: "Not from Stoker. A Besson invention." },
      { trope: "Anti-Religious Framing (Temporary)", id: "WOKE-011", category: "WOKE", location: "Opening act -- Vlad stabs priest and denounces God, but framed as catastrophic sin", authenticity: "Loosely inspired by historical Vlad and Coppola's 1992 adaptation" },
      { trope: "Sexualized Comedy", id: "WOKE-022", category: "WOKE", location: "Second act -- nuns become sexually aggressive under perfume influence", authenticity: "Pure Besson invention" },
      { trope: "Eternal Devotion", id: "TRADITIONAL-027", category: "TRAD", location: "Entire film -- 400-year quest to find reincarnation of wife", authenticity: "Draws from Stoker and Coppola's 1992 adaptation" },
      { trope: "The Self-Sacrificing Hero", id: "TRADITIONAL-026", category: "TRAD", location: "Final act -- Dracula allows himself to be staked to save Mina from damnation", authenticity: "Departure from Stoker, closer to Coppola" },
      { trope: "Faith as Moral Architecture", id: "TRADITIONAL-043", category: "TRAD", location: "Throughout -- rebellion against God produces suffering, repentance produces redemption", authenticity: "Amplified from Stoker's Christian symbolism" },
      { trope: "Traditional Femininity", id: "TRADITIONAL-036", category: "TRAD", location: "Throughout -- Elisabeta/Mina defined through romantic love and devotion", authenticity: "Consistent with Stoker" },
      { trope: "Craftsmanship and Industry", id: "TRADITIONAL-041", category: "TRAD", location: "Production level -- 550 handmade costumes, practical armor, sets built from scratch", authenticity: "Documented production choices" },
      { trope: "Defense of the Innocent", id: "TRADITIONAL-045", category: "TRAD", location: "Final act -- priest's siege to rescue Mina framed as righteous", authenticity: "Consistent with Stoker" },
      { trope: "Classical Source Fidelity", id: "TRADITIONAL-047", category: "TRAD", location: "Entire film -- core narrative beats preserved from Stoker with moral core intact", authenticity: "Besson acknowledges Stoker as source" },
      { trope: "Romantic Commitment", id: "TRADITIONAL-028", category: "TRAD", location: "Throughout -- permanent, all-consuming romantic devotion presented as highest value", authenticity: "Romantic amplification of Stoker" },
      { trope: "Consequences of Sin", id: "TRADITIONAL-033", category: "TRAD", location: "Entire arc -- rejection of God produces curse, resolved only through sacrifice", authenticity: "Amplified from Stoker" },
      { trope: "Male Protector", id: "TRADITIONAL-051", category: "TRAD", location: "Opening battle and throughout -- every major male defined by protective instinct", authenticity: "Consistent with Stoker and historical setting" },
      { trope: "Honor and Duty", id: "TRADITIONAL-025", category: "TRAD", location: "Priest's arc -- principled man of faith doing difficult work without cynicism", authenticity: "Van Helsing figure preserved from Stoker" },
      { trope: "Beauty and Aesthetics", id: "TRADITIONAL-039", category: "TRAD", location: "Throughout -- Flemish painting inspiration, lavish production design", authenticity: "Documented production choices" }
    ],
    seo: {
      titleTag: "Is Dracula: A Love Tale (2025) Woke? Luc Besson Film Review | VirtueVigil",
      metaDescription: "Is Dracula woke? VirtueVigil's analysis: Woke Score 3, Traditional 12, Fidelity Casting FAITHFUL. Full creative team deep dive, trope audit, and family guidance."
    }
  },
  {
    id: "zootopia-2-2025",
    slug: "zootopia-2-2025",
    title: "Zootopia 2",
    year: 2025,
    type: "film",
    platform: "Theatrical",
    genre: "Animation, Comedy",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "18 min",
    poster: "/images/posters/zootopia-2-2025.jpg",
    verdict: "WOKE",
    wokeScore: 9,
    tradScore: 8,
    authIndex: 78,
    scoreMargin: "-1 WOKE",
    wokeTrap: {
      present: false,
      degree: null,
      explanation: "Zootopia 2 does not disguise its ideological agenda. Like its predecessor, the entire premise is built around prejudice allegory. Conservative viewers won't be blindsided. The film's traditional elements are genuinely strong and coexist openly with the progressive messaging rather than being used as bait-and-switch material.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: false,
      explanation: "Zootopia 2 does not disguise its ideological agenda. The entire premise is built around prejudice allegory. The traditional elements coexist openly with progressive messaging."
    },
    creative_team: {
      director: {
        name: "Jared Bush & Byron Howard",
        ideology: "MODERATELY WOKE",
        profile: "Disney Animation veterans. Bush's writing consistently returns to themes of prejudice, exclusion, and community division. Howard is a more traditional storyteller whose solo efforts are straightforward crowd-pleasers."
      },
      writer: {
        name: "Jared Bush",
        profile: "Sole screenplay credit. Writer of Zootopia, Moana, and Encanto. Progressive themes delivered through traditional emotional frameworks."
      },
      lead_producer: {
        name: "Yvett Merino",
        company: "Walt Disney Animation Studios"
      },
      composer: {
        name: "Michael Giacchino"
      },
      top_cast: [
        { name: "Ginnifer Goodwin", role: "Judy Hopps" },
        { name: "Jason Bateman", role: "Nick Wilde" },
        { name: "Ke Huy Quan", role: "Gary De'Snake" },
        { name: "Fortune Feimster", role: "Nibbles Maplestick" },
        { name: "Andy Samberg", role: "Pawbert Lynxley" }
      ],
      prediction: {
        verdict: "WOKE",
        confidence: "high"
      }
    },
    fidelity_casting: {
      score: "N/A",
      summary: "Animated film with anthropomorphic animal characters. Voice casting carries no fidelity signal.",
      detailed_analysis: "This is a fully animated film with anthropomorphic animal characters. Traditional fidelity casting metrics do not apply. The voice cast is diverse and largely reflects standard Hollywood casting practices for animated features."
    },
    summary: {
      overall: "Disney's Zootopia 2 arrives nine years after the original and picks up almost immediately where that film left off. Judy Hopps and Nick Wilde are partners at the ZPD. Their relationship is rocky. Chief Bogo is threatening to split them up. Then a pit viper named Gary De'Snake shows up in a city that hasn't seen a reptile in a century, and suddenly our heroes have a real case on their hands.\n\nThe surface-level movie is terrific. The animation is gorgeous, the voice performances are sharp, and the buddy cop dynamic between Goodwin and Bateman still crackles with genuine chemistry. Ke Huy Quan brings warmth and energy to Gary. The action sequences are well-staged, the pacing mostly holds across 108 minutes, and it pulled in $1.83 billion at the box office for a reason.\n\nWhat Zootopia 2 is saying, once you strip away the fur and scales, is a fairly explicit allegory about systemic exclusion, historical erasure, and colonialism. The reptiles were driven out by the Lynxley family, who stole a reptile inventor's work, framed her for murder, and used the resulting fear to exile an entire population. Their original district was literally buried under Tundratown.\n\nThe Lynxley family functions as oligarch villains, rich, powerful, and willing to kill to protect their stolen legacy. The message is clear: wealth built on injustice will fight to preserve that injustice.\n\nFor all its progressive messaging, Zootopia 2 has a surprisingly strong traditional backbone. The film is fundamentally a law enforcement story. Judy and Nick are cops and heroes, presented as brave, self-sacrificing, and ultimately right. The partnership between them is built on loyalty, sacrifice, and earned trust. Nick literally falls off a weather wall to protect Judy.\n\nThe film's resolution involves truth and justice, not revolution. The heroes expose a lie, present evidence, and allow the legal system to work. The Lynxleys are arrested. This is reform within the system, not destruction of it.\n\nFamily runs through everything. Gary's entire motivation is clearing his great-grandmother's name and bringing his family home. Judy's parents and grandmother appear, grounding her in a loving, traditional family unit. Grandma Hopps prays for Judy's safety daily.\n\nThe film's deeper theme is that differences between groups are real but not insurmountable. The sequel acknowledges that predators and prey, mammals and reptiles, are genuinely different. The argument is that common ground can be found through conversation and good faith rather than fear and propaganda.\n\nZootopia 2 is a woke film. The systemic exclusion allegory, the colonialism parallel, the wealthy families built on stolen history narrative are progressive frameworks baked into the story. But the traditional elements are not window dressing. The respect for law enforcement, the value of partnership and loyalty, the family bonds, the faith in institutional reform over revolution: these carry real emotional weight. Conservative families will find plenty to discuss and some things to push back on, but also a film that respects its cop heroes, celebrates loyalty and sacrifice, and argues that truth and justice can prevail within the system.",
      adultInsight: "Conservative adult viewers should approach Zootopia 2 with clear eyes and some genuine appreciation. This is a film that wears its progressive politics openly through its systemic exclusion allegory and colonialism parallel. But it actually respects its audience more than most contemporary Disney output. The differences are real but not insurmountable message is a genuine improvement over the first film's softer anyone can be anything thesis. The law enforcement heroes are treated with respect. The resolution trusts institutional reform over revolutionary destruction. The family elements are sincere, not ironic. Watch it with your kids. Talk about it afterward. Ask them what they think the reptile story is really about. The conversation is more valuable than either uncritical acceptance or blanket rejection.",
      parentalGuidance: "Violence: Moderate for a PG animated film. The Lynxley family orders deaths and fights the heroes. A character is injected with snake venom and nearly dies. Nick falls off a weather wall. Chief Bogo is accidentally bitten by a venomous snake fang. Sexual Content: Minimal but present. A sheep's shaved wool resembles a bra. Judy's grandmother tells her to come home and make babies. Nibbles makes threesome jokes framed as teamwork. Language: Very mild. Substance Use: A gala scene features cocktail glasses, one character shown blackout drunk. LGBTQ+ Content: Directors confirmed antelope neighbors Bucky and Pronk are a gay couple with minimal screen time. Scary/Intense: Weather wall climax is intense, Pawbert betrayal may frighten younger viewers. Age Recommendation: 7 and up. Children under 7 may find venom scenes too intense."
    },
    tropeAudit: [
      { trope: "Institutional Evil / Systemic Exclusion", id: "WOKE-004", category: "WOKE", location: "Throughout -- reptile population exiled through institutional manipulation by Lynxley family", authenticity: "N/A" },
      { trope: "Anti-Western Revisionism / Historical Erasure", id: "WOKE-020", category: "WOKE", location: "Mid-film -- Zootopia's founding narrative revealed as fabricated lie", authenticity: "N/A" },
      { trope: "The Colonialist Villain", id: "WOKE-024", category: "WOKE", location: "Throughout -- Lynxley family represents generational wealth built on theft and displacement", authenticity: "N/A" },
      { trope: "Globalist Utopia / Multicultural Integration", id: "WOKE-017", category: "WOKE", location: "Resolution -- reptiles officially reintegrated into Zootopia", authenticity: "N/A" },
      { trope: "The Victimhood Meritocracy", id: "WOKE-009", category: "WOKE", location: "Throughout -- Gary feared on sight despite innocence, victimhood as moral authority", authenticity: "N/A" },
      { trope: "The Marginalized Savant", id: "WOKE-001", category: "WOKE", location: "Mid-film -- Agnes De'Snake revealed as true genius behind weather walls", authenticity: "N/A" },
      { trope: "Therapy Culture Advocacy", id: "WOKE-022", category: "WOKE", location: "Early film -- Partners in Crisis therapy validated as correct", authenticity: "N/A" },
      { trope: "Coded LGBTQ+ Representation", id: "WOKE-016", category: "WOKE", location: "Background -- confirmed gay couple Bucky and Pronk, Nibbles' suggestive jokes", authenticity: "N/A" },
      { trope: "The Bigoted Traditionalist", id: "WOKE-008", category: "WOKE", location: "Throughout -- anti-reptile citizens presented as victims of propaganda", authenticity: "N/A" },
      { trope: "Defense of the Innocent / Law Enforcement Heroes", id: "TRADITIONAL-045", category: "TRAD", location: "Throughout -- Judy and Nick as genuinely heroic police officers", authenticity: "N/A" },
      { trope: "Industry and Perseverance", id: "TRADITIONAL-041", category: "TRAD", location: "Throughout -- every major character succeeds through relentless determination", authenticity: "N/A" },
      { trope: "The Self-Sacrificing Hero", id: "TRADITIONAL-026", category: "TRAD", location: "Climax -- Nick falls off weather wall to save Judy", authenticity: "N/A" },
      { trope: "Partnership and Loyalty", id: "TRADITIONAL-047", category: "TRAD", location: "Throughout -- central theme of Judy and Nick's tested and strengthened bond", authenticity: "N/A" },
      { trope: "Restored Home / Homecoming", id: "TRADITIONAL-048", category: "TRAD", location: "Resolution -- every displaced character returns home, broken relationships mended", authenticity: "N/A" },
      { trope: "Faith in Adversity", id: "TRADITIONAL-043", category: "TRAD", location: "Brief -- Grandma Hopps prays daily for Judy's safety without mockery", authenticity: "N/A" },
      { trope: "Truth and Justice Prevail", id: "TRADITIONAL-050", category: "TRAD", location: "Resolution -- heroes expose fraud through evidence, legal system delivers justice", authenticity: "N/A" },
      { trope: "Traditional Family", id: "TRADITIONAL-036", category: "TRAD", location: "Throughout -- Hopps and De'Snake families presented with warmth and respect", authenticity: "N/A" }
    ],
    seo: {
      titleTag: "Is Zootopia 2 (2025) Woke? Disney Animated Film Review | VirtueVigil",
      metaDescription: "Is Zootopia 2 woke? VirtueVigil's analysis: Woke Score 9, Traditional 8, $1.83B box office. Full trope audit, creative team deep dive, and family guidance."
    }
  },
  {
    id: "hurry-up-tomorrow-2025",
    slug: "hurry-up-tomorrow-2025",
    title: "Hurry Up Tomorrow",
    year: 2025,
    type: "film",
    platform: "Theatrical",
    genre: "Psychological Thriller, Drama",
    date: "2026-02-17",
    author: "VirtueVigil Editorial Team",
    readTime: "12 min",
    poster: "/images/posters/hurry-up-tomorrow-2025.jpg",
    verdict: "NEUTRAL",
    wokeScore: 4,
    tradScore: 5,
    authIndex: 65,
    scoreMargin: "+1 TRAD",
    wokeTrap: {
      present: false,
      degree: null,
      explanation: "This film is not hiding an ideological agenda behind entertainment. It barely has an agenda at all. What it has is a pop star who wanted to make a movie about himself and got a $15 million budget to do it. Conservative viewers are far more likely to be bored than offended.",
      viewerSentiment: null
    },
    woke_trap_assessment: {
      is_trap: false,
      explanation: "This film is not hiding an ideological agenda. It barely has an agenda at all. A pop star's vanity project about his own feelings. Conservative viewers are more likely to be bored than offended."
    },
    creative_team: {
      director: {
        name: "Trey Edward Shults",
        ideology: "NEUTRAL",
        profile: "Texas-born independent filmmaker drawn to emotional extremity, family dynamics, and formal experimentation. Not an ideological filmmaker."
      },
      writer: {
        name: "Trey Edward Shults, Abel Tesfaye, Reza Fahim",
        profile: "Co-written vanity project. Tesfaye's artistic persona centers on hedonism, drug use, and toxic relationships. No clear ideological direction."
      },
      lead_producer: {
        name: "Abel Tesfaye",
        company: "Manic Phase"
      },
      composer: {
        name: "Abel Tesfaye & Daniel Lopatin (Oneohtrix Point Never)"
      },
      top_cast: [
        { name: "Abel Tesfaye", role: "Abel (fictionalized self)" },
        { name: "Jenna Ortega", role: "Anima" },
        { name: "Barry Keoghan", role: "Lee" },
        { name: "Riley Keough", role: "Girl on Voicemail (voice)" },
        { name: "Metro Boomin", role: "Himself" }
      ],
      prediction: {
        verdict: "NEUTRAL",
        confidence: "high"
      }
    },
    fidelity_casting: {
      score: "N/A",
      summary: "Original contemporary story. No source material fidelity to assess.",
      detailed_analysis: "This is an original contemporary story with no historical or literary source material. The lead plays a fictionalized version of himself. Supporting cast assembled based on acting talent and availability."
    },
    summary: {
      overall: "Hurry Up Tomorrow is a vanity project. It is perhaps the most unambiguous vanity project to receive a wide theatrical release in recent memory. Abel Tesfaye, known to the world as The Weeknd, plays a lightly fictionalized version of himself. He co-wrote the script. He co-produced the film. He co-composed the score. The entire apparatus of cinema has been marshaled in service of one man's feelings about being famous and sad.\n\nThe plot: Abel is a superstar struggling with depression, insomnia, and the aftermath of a breakup. His voice gives out during a concert. His manager Lee pushes him to keep performing. A mysterious young woman named Anima burns down a house and drives to LA to attend his concert. They meet backstage. They spend a night together. Then Anima knocks Abel unconscious with a champagne bottle, ties him to a bed, and demands that he confront his psychological demons. She kills Lee when he shows up. She douses Abel in gasoline. He sings. She releases him and sets the room on fire. He walks through a hallway and ends up backstage before another concert, staring at his reflection.\n\nDirector Trey Edward Shults brings real visual craft to the proceedings. Chayse Irvin's cinematography, shot on a mix of 35mm, 16mm, and Super 8 film, gives the movie a textured, dreamy quality. The score by Tesfaye and Daniel Lopatin pulses with atmospheric menace. On a pure sensory level, the film occasionally works. As storytelling, it is a disaster.\n\nThe central problem is Abel Tesfaye himself. Playing a version of yourself requires either self-awareness or charisma. Tesfaye has neither here. He mopes and stares. The film asks us to care deeply about the inner torment of a man whose torment consists of being extremely rich, extremely famous, and bad at relationships.\n\nJenna Ortega tries. Anima is a borderline impossible role: fan, stalker, therapist, killer, and symbolic catalyst all crammed into one underwritten character. Ortega brings genuine intensity to several scenes but the script gives her nothing beyond mysterious damaged woman who exists to fix a man.\n\nBarry Keoghan is the film's secret weapon. His Lee is manic, manipulative, and oddly affectionate. When Anima stabs Lee in the neck, the movie loses its pulse along with him.\n\nFrom a values perspective, this film is largely ideologically inert. It does not push progressive social messaging. The entire film operates within a framework of celebrity suffering as the ultimate human experience. Abel's depression is treated with the gravity of a war documentary. His inability to maintain relationships is presented as existential tragedy rather than the predictable consequence of hedonism and emotional selfishness. The film never suggests that Abel's lifestyle choices might be the cause of his suffering rather than a response to it.\n\nThe film bombed. $7.8 million worldwide against a $15 million budget. Critics savaged it. Five Golden Raspberry nominations. Conservative viewers will find nothing to be outraged about and very little to be entertained by. The Weeknd wanted to make a movie about how hard it is to be The Weeknd. He succeeded. That is both the film's achievement and its epitaph.",
      adultInsight: "Conservative adult viewers should know upfront that this film is not going to challenge their values. It is going to challenge their patience. The film is a 105-minute exercise in celebrity navel-gazing, wrapped in gorgeous cinematography and a throbbing electronic score, but hollow at the center. If you do watch it, the most interesting exercise is reading against the grain. The film refuses to hold Abel accountable for his choices, but the evidence is everywhere on screen. The voice loss, the failed relationships, the emotional emptiness, the drugs. A conservative viewer can see what the filmmakers cannot articulate: that a life organized around self-gratification produces exactly the misery depicted here. Skip it unless you are specifically interested in contemporary celebrity culture as a subject of study.",
      parentalGuidance: "Violence: Moderate to strong. A character is stabbed to death with blood shown. The protagonist is knocked unconscious with a bottle, tied to a bed, and doused in gasoline. A house and hotel room are set on fire. Sexual Content: Mild to moderate. An implied sexual encounter. Suggestive party behavior. No explicit nudity. Language: Strong. Frequent profanity including a particularly vile voicemail. Substance Use: Significant. Drug use shown during party scenes without moral commentary. Disturbing Content: Kidnapping and psychological manipulation sequences. Nihilistic tone offers no reassurance. Age Recommendation: Not appropriate for viewers under 16."
    },
    tropeAudit: [
      { trope: "Therapeutic Determinism", id: "WOKE-022", category: "WOKE", location: "Throughout -- destructive behavior framed as symptoms of trauma rather than choices", authenticity: "Based on real events" },
      { trope: "The Disposable Male (Inverted)", id: "WOKE-011", category: "WOKE", location: "70 minutes in -- Lee stabbed to death, functions purely as plot mechanism", authenticity: "N/A" },
      { trope: "Female Violence Without Consequence", id: "WOKE-015", category: "WOKE", location: "Final third -- Anima commits arson, assault, kidnapping, murder without accountability", authenticity: "N/A" },
      { trope: "Celebrity Victimhood", id: "WOKE-009", category: "WOKE", location: "Throughout -- fame and wealth pressures treated as profound suffering", authenticity: "Based on real events" },
      { trope: "Consequences of Hedonism", id: "TRADITIONAL-039", category: "TRAD", location: "Throughout -- drug use, hedonism, and emotional unavailability leave Abel hollow", authenticity: "Grounded in documented celebrity excess" },
      { trope: "Industry and Perseverance", id: "TRADITIONAL-041", category: "TRAD", location: "Concert sequences -- the show must go on ethos", authenticity: "Authentic to entertainment industry" },
      { trope: "Cycle of Destruction", id: "TRADITIONAL-027", category: "TRAD", location: "Final scene -- Abel walks from burning room directly to another concert stage", authenticity: "Meta-textual authenticity" },
      { trope: "The Mirror", id: "TRADITIONAL-044", category: "TRAD", location: "Final shot -- Abel stares at reflection, unchanged despite ordeal", authenticity: "N/A" }
    ],
    seo: {
      titleTag: "Is Hurry Up Tomorrow (2025) Woke? The Weeknd Film Review | VirtueVigil",
      metaDescription: "Is Hurry Up Tomorrow woke? VirtueVigil's analysis: Woke Score 4, Traditional 5. The Weeknd's vanity project reviewed with full trope audit and family guidance."
    }
  }
];

// Deduplicate by slug
const existingSlugs = new Set(reviews.map(r => r.slug));
const toAdd = newReviews.filter(r => !existingSlugs.has(r.slug));
const updated = [...toAdd, ...reviews];

fs.writeFileSync(reviewsPath, JSON.stringify(updated, null, 2));
console.log(`Added ${toAdd.length} new reviews. Total: ${updated.length}`);
