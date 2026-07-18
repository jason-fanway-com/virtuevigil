#!/usr/bin/env node
// Batch review writer: appends 3 reviews to src/data/reviews.json
// Run: node write-reviews-batch.js TITLE SLUG

const fs = require('fs');
const path = require('path');

const reviewsPath = path.join(__dirname, 'src/data/reviews.json');

// Read existing reviews
const reviews = JSON.parse(fs.readFileSync(reviewsPath, 'utf8'));

// REVIEW 1: Ride or Die: Season 1 (2026)
const review1 = {
  "id": "ride-or-die-s1-2026",
  "slug": "ride-or-die-s1-2026",
  "title": "Ride or Die: Season 1",
  "year": 2026,
  "type": "series",
  "platform": "Amazon Prime Video",
  "genre": "Action Adventure Comedy",
  "date": "2026-07-18",
  "datePublished": "2026-07-18",
  "author": "VirtueVigil Editorial Team",
  "readTime": "7 min",
  "poster": "/images/posters/ride-or-die-s1-2026.jpg",
  "releaseDate": "2026-07-15",
  "rating": "TV-MA (Violence, Language, Adult Themes)",
  "runtime": "8 episodes, 48-55 min each",
  "director": "Peyton Reed, Andy Muschietti",
  "writers": [
    "Tessa Coates",
    "Matt Miller"
  ],
  "cast": [
    { "name": "Octavia Spencer", "role": "Debbie Claybourne" },
    { "name": "Hannah Waddingham", "role": "Judith Burton" },
    { "name": "Bill Nighy", "role": "The Director" },
    { "name": "Ed Skrein", "role": "Billy Donovan" },
    { "name": "Calam Lynch", "role": "Sam" },
    { "name": "Savannah Steyn", "role": "Queenie" },
    { "name": "Jamie Parker", "role": "David Claybourne" },
    { "name": "Sylvia Hoeks", "role": "Ana" }
  ],
  "studio": "Melodie Productions / Orit Entertainment / Amazon MGM Studios",
  "distributor": "Amazon Prime Video",
  "verdict": "WOKE LEAN",
  "wokeScore": 10.36,
  "tradScore": 5.88,
  "authIndex": 36,
  "scoreMargin": "-4 WOKE",
  "preRelease": false,
  "wokeTrap": false,
  "woke_trap_assessment": {
    "is_trap": false,
    "explanation": "Ride or Die is not a woke trap because the woke elements (female assassin lead, girl-boss dynamics) are evident from the first episode and are the premise of the show, not a hidden payload. The series openly signals its identity as a female-led action comedy from frame one. It does not bait viewers with one premise and then switch to ideological content past the 50% mark."
  },
  "externalScores": {
    "rottenTomatoesCritic": 96,
    "rottenTomatoesAudience": 78
  },
  "creative_team": {
    "director": {
      "name": "Peyton Reed, Andy Muschietti",
      "ideology": "MODERATE. Reed directed Ant-Man films and is a journeyman comedy director without overt ideological baggage. Muschietti directed IT and The Flash and is known for horror/blockbuster work. Their involvement suggests the show is being positioned as mainstream entertainment rather than ideological messaging."
    },
    "writers": [
      {
        "name": "Tessa Coates",
        "ideology": "MODERATE TO PROGRESSIVE. Coates is a British comedian and writer. Her work emphasizes female friendship and empowerment themes but leans comedic rather than polemical."
      },
      {
        "name": "Matt Miller",
        "ideology": "MODERATE. Miller is a veteran TV showrunner (Lethal Weapon, Chuck) known for action-comedy with broad appeal. His presence suggests a focus on entertainment over messaging."
      }
    ]
  },
  "parentalGuidance": {
    "sexualContent": "MILD TO MODERATE. Comedic sexual references and situations consistent with TV-MA rating. No graphic depictions expected based on available reviews.",
    "violence": "HIGH. Action sequences with gunplay, hand-to-hand combat, and assassination depictions. Stylized rather than gratuitous, in keeping with the action-comedy tone.",
    "language": "MODERATE TO HIGH. TV-MA rating indicates strong language throughout.",
    "substanceUse": "MILD. Social drinking likely depicted given the European road trip setting.",
    "matureThemes": "MODERATE. Betrayal, moral ambiguity around assassination, secrets kept from loved ones. The core tension between Judith's violent profession and her friendship with the sheltered Debbie."
  },
  "summary": {
    "overall": "Ride or Die is Amazon Prime Video's glossy new action-comedy series that pairs Octavia Spencer and Hannah Waddingham as best friends on the run through Europe after one of them is revealed to be an elite international assassin. It is slick, fun, and sometimes very funny, carried by the genuine chemistry between its two leads. The series is also a clear product of the post-2016 entertainment formula: two female leads, one of them a hyper-competent killer, the traditional male action hero replaced by women who crack wise while cracking skulls. Created by British comedian Tessa Coates and showrun by Matt Miller (Chuck, Lethal Weapon), the series knows exactly what it is: popcorn entertainment designed for a broad streaming audience that wants its action sequences well-staged and its protagonists female. Whether that matters to you depends on what you are looking for. If you want a breezy summer binge with charismatic performances, Ride or Die delivers. If you are tired of the entertainment industry's reflexive substitution of female leads into traditionally masculine genre templates, this is yet another data point. The VVWS score lands at WOKE LEAN because the ideological architecture is present but not heavy-handed. Judith is the classic Girl Boss archetype (WOKE-003): physically dominant, emotionally guarded, and lethally competent in ways that were once the exclusive province of male action heroes. The show does not lecture, but it does not need to; the premise itself is the message. The casting of two women as the central action duo, the sidelining of the one notable male character (Debbie's MP husband David, who is mostly a plot device), and the chosen-family-over-biological-ties subtext all register on the VVWS scale. At the same time, the series earns points for traditional themes: Judith's willingness to risk everything to protect Debbie is genuine self-sacrifice (TRADITIONAL-026), and there is a clear moral binary between the criminal syndicate antagonists and our heroes (TRADITIONAL-039). The net result is a show that leans woke but is not a screed. If you are a conservative parent evaluating content, the violence and language are the primary concerns, not the ideology. The ideological content is more a matter of what the show represents (another female-led action franchise) than what it says.",
    "adultInsight": "Ride or Die is a case study in how modern streaming entertainment packages ideological assumptions as genre entertainment. The premise that a suburban housewife and a secret assassin would be best friends, that the assassin's violence is 'cool' and 'fun,' and that traditional male protector roles are obsolete are all baked into the show's DNA. None of this is argued; it is simply assumed. That is the modern media playbook: do not debate the ideology, just build the world where it is already true. For viewers who notice this, the series can feel like a well-produced but predictable formula. For those who do not, it is an entertaining summer binge with two charismatic leads. Both readings are valid.",
    "parentalGuidance": "TV-MA for a reason. The violence, while stylized, involves assassination and gunplay throughout. Strong language is frequent. Parents should know that the central premise (an assassin as a sympathetic protagonist) presents moral complexity that younger viewers may not be equipped to navigate. Recommended for mature teens and adults only."
  },
  "seo": {
    "titleTag": "Is Ride or Die Woke? | VirtueVigil Review (2026 Amazon Series)",
    "metaDescription": "Is Amazon's Ride or Die woke? We score the Octavia Spencer and Hannah Waddingham action-comedy series through the VVWS lens. 96% RT but WOKE LEAN on ideology.",
    "keywords": "ride or die woke, ride or die amazon review conservative, is ride or die woke, ride or die virtuevigil, ride or die parents guide, ride or die woke score"
  },
  "tropeAudit": [
    {
      "id": "WOKE-003",
      "name": "The Girl Boss",
      "category": "Woke",
      "severity": 3,
      "authenticity": "Low",
      "centrality": "High",
      "weightedScore": 7.56,
      "description": "Judith Burton is the quintessential Girl Boss: a hyper-competent international assassin who dominates every physical confrontation, keeps her emotions locked down, and operates in a world of violence that was once the exclusive territory of male action heroes. Waddingham's Judith is cool, lethal, and unflappable in ways that are coded masculine but delivered through a female body. The show frames this as aspirational rather than pathological, which is the Girl Boss formula in its purest form."
    },
    {
      "id": "WOKE-001",
      "name": "Female Action Hero Formula (Genre Replacement)",
      "category": "Woke",
      "severity": 2,
      "authenticity": "Low",
      "centrality": "Moderate",
      "weightedScore": 2.80,
      "description": "The series represents the post-2016 streaming template of replacing traditional male action heroes with female leads as a default rather than a creative choice. Two women headline the action sequences, the chases, and the gunfights. The male characters exist primarily as obstacles, love interests, or plot devices. This is not a show about women doing something new; it is a show about women doing what men used to do, and the entertainment industry presenting this as a neutral creative decision rather than an ideological one."
    },
    {
      "id": "TRADITIONAL-026",
      "name": "The Self-Sacrificing Hero",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 3.78,
      "description": "Despite the woke framing, Judith's core motivation is sacrificially protective. She risks her life, her career, and her safety to protect Debbie, her innocent best friend who has been dragged into a world of assassins and crime syndicates. This is a genuinely traditional narrative: the strong protecting the vulnerable at great personal cost. The sacrificial friendship arc is the emotional engine of the series."
    },
    {
      "id": "TRADITIONAL-045",
      "name": "Defense of the Innocent",
      "category": "Traditional",
      "severity": 2,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 1.40,
      "description": "Debbie is an innocent caught in the crossfire. She is a suburban wife and mother with no combat training, no criminal connections, and no experience with violence. Judith's protection of her is rooted in a traditional moral framework: the capable defend the incapable, the strong shield the weak. The show earns this traditional point even as it subverts other gender norms."
    },
    {
      "id": "TRADITIONAL-039",
      "name": "Objective Good vs. Evil",
      "category": "Traditional",
      "severity": 2,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.70,
      "description": "The antagonists (crime syndicate operatives, rival assassins, corrupt figures from Judith's past) are clearly positioned as evil. The show does not moralize about the assassins having a 'point' or the criminals being 'victims of the system.' There is a straightforward good-versus-evil framework, even if the 'good' side includes a professional killer."
    }
  ]
};

// REVIEW 2: Psycho (1960)
const review2 = {
  "id": "psycho-1960",
  "slug": "psycho-1960",
  "title": "Psycho",
  "year": 1960,
  "type": "film",
  "platform": "Theaters",
  "genre": "Horror / Thriller",
  "date": "2026-07-18",
  "datePublished": "2026-07-18",
  "author": "VirtueVigil Editorial Team",
  "readTime": "8 min",
  "poster": "/images/posters/psycho-1960.jpg",
  "releaseDate": "1960-09-08",
  "rating": "R (Graphic Violence, Mature Themes, Psychological Horror)",
  "runtime": "109 min",
  "director": "Alfred Hitchcock",
  "writers": [
    "Joseph Stefano"
  ],
  "cast": [
    { "name": "Anthony Perkins", "role": "Norman Bates" },
    { "name": "Janet Leigh", "role": "Marion Crane" },
    { "name": "Vera Miles", "role": "Lila Crane" },
    { "name": "John Gavin", "role": "Sam Loomis" },
    { "name": "Martin Balsam", "role": "Milton Arbogast" },
    { "name": "John McIntire", "role": "Sheriff Al Chambers" },
    { "name": "Simon Oakland", "role": "Dr. Richman" }
  ],
  "studio": "Shamley Productions",
  "distributor": "Paramount Pictures",
  "verdict": "TRADITIONAL",
  "wokeScore": 0,
  "tradScore": 12.04,
  "authIndex": 100,
  "scoreMargin": "+12 TRAD",
  "preRelease": false,
  "wokeTrap": false,
  "woke_trap_assessment": {
    "is_trap": false,
    "explanation": "Psycho cannot be a woke trap because it contains zero woke content. The verdict is TRADITIONAL with a margin of +12. The film is a 1960 horror-thriller about crime, punishment, and psychological deviance told through a deeply traditional moral framework. There is no ideological payload, hidden or otherwise."
  },
  "externalScores": {
    "imdb": 8.5,
    "rottenTomatoesCritic": 96,
    "rottenTomatoesAudience": 95,
    "metacritic": 97
  },
  "creative_team": {
    "director": {
      "name": "Alfred Hitchcock",
      "ideology": "TRADITIONAL. Hitchcock was a Catholic-raised British director whose entire body of work is steeped in themes of guilt, punishment, voyeurism, and moral consequence. Psycho is arguably his most morally direct film: Marion Crane steals money and is punished with death. Norman Bates violates the natural order (murdering his mother, preserving her corpse, adopting her identity) and is destroyed by it. Hitchcock's moral universe is Old Testament in its clarity: transgression brings consequence, and evil, no matter how sympathetically portrayed, is evil."
    },
    "writers": [
      {
        "name": "Joseph Stefano",
        "ideology": "TRADITIONAL. Stefano's screenplay adapts Robert Bloch's novel while heightening the moral framework. He made Norman younger and more sympathetic (casting Anthony Perkins was his idea), but the moral trajectory is unchanged: Marion's theft leads to her death, Norman's psychosis is a result of his original sin (the murder of his mother and her lover), and justice ultimately prevails."
      }
    ]
  },
  "parentalGuidance": {
    "sexualContent": "MODERATE. The opening scene shows Marion and Sam in a hotel room after a lunchtime tryst (implied, not explicit). Norman's voyeurism (watching Marion undress through a peephole) is presented as disturbing, not titillating. The film's treatment of sexuality is inseparable from its moral framework: illicit sex is connected to guilt, danger, and death.",
    "violence": "DEFINING. The shower murder is one of the most famous scenes in cinema history and remains genuinely shocking despite being relatively bloodless by modern standards. Arbogast's death on the staircase is also intense. The violence is psychological more than graphic. Hitchcock understood that what the audience imagines is worse than what is shown.",
    "language": "MILD. 1960 standards; no strong profanity.",
    "substanceUse": "MILD. Social drinking depicted. No drug use.",
    "matureThemes": "DEFINING. Murder, theft, voyeurism, split personality, matricide, necrophilia (implied in Norman's preservation of his mother's corpse), institutionalization. This is a deeply adult film that confronts psychological horror and moral transgression directly. Not for children under any circumstances."
  },
  "summary": {
    "overall": "Psycho is Alfred Hitchcock's most influential film and one of the few movies that genuinely changed what cinema was allowed to do. Made in 1960 on a television crew's budget in black and white, it shattered taboos about violence, sexuality, and psychological horror that had governed Hollywood for three decades. The plot is deceptively simple: Marion Crane (Janet Leigh) steals forty thousand dollars from her employer and flees Phoenix for Fairvale, California, to reunite with her debt-ridden lover Sam Loomis. A rainstorm forces her off the highway. She stops at the Bates Motel, a lonely twelve-room establishment overseen by a shy young man named Norman Bates (Anthony Perkins) and his unseen, domineering mother. By the end of the night, Marion is dead, stabbed in the shower by a shadowy female figure. A private investigator (Martin Balsam) arrives, then Marion's sister Lila (Vera Miles) and Sam himself, and the truth of the Bates Motel is gradually, horrifyingly revealed. The VVWS scores Psycho at TRADITIONAL with no woke content whatsoever. This is a film governed by a moral framework so traditional it borders on Old Testament: Marion steals, and she is punished with death. Norman commits matricide, and his guilt literally consumes him, fracturing his psyche into two personalities locked in a permanent, hellish argument. The psychiatrist's concluding monologue (often criticized as clunky exposition) is in fact a traditional moral verdict dressed in clinical language: Norman's crimes are the direct result of his original sin, and his punishment is a living death inside his own mind. There is no DEI calculus, no gender politics, no ideological subtext. The film is interested in guilt, punishment, voyeurism, and the wages of sin. It is a masterpiece of traditional storytelling: a crime committed, a punishment exacted, and a moral order restored, however uneasily, by the final frame.",
    "adultInsight": "Psycho rewards adult viewers not with answers but with questions that linger for decades. Why does Hitchcock spend the first third of the film making us care about Marion Crane, only to kill her? Why is Norman Bates, a murderer and a monster, also the character we feel the most complicated sympathy for? The film is a trap: it makes us complicit in Norman's voyeurism (we watch Marion undress too), then punishes us for our complicity. The shower scene is not just a murder; it is a violation of the viewer's expectations, a declaration that no one is safe and that the filmmaker is in complete control. For parents considering whether to show this to teenagers: the film's power lies in what it suggests, not what it shows. Teenagers who have been desensitized by modern gore may find Psycho more disturbing, not less, because Hitchcock forces the imagination to do the work.",
    "parentalGuidance": "Absolutely not for children. The film earned its R rating retroactively and would be a hard R by modern standards despite its lack of gore. The shower scene, the staircase murder, the final revelation of Mother's corpse, and the climactic basement sequence are all genuinely frightening. The psychological content (split personality, implied necrophilia, voyeurism) is mature in ways that a simple slasher film is not. Recommended only for mature teenagers (16+) with parental guidance. The film's moral seriousness makes it worth showing to older teens, but parents should watch it first or watch it with them."
  },
  "seo": {
    "titleTag": "Is Psycho Woke? | VirtueVigil Review (1960 Hitchcock Classic)",
    "metaDescription": "Is Hitchcock's Psycho woke? We score the 1960 masterpiece through the VVWS lens. A TRADITIONAL verdict for cinema's most influential horror film. No woke content, pure moral clarity.",
    "keywords": "psycho woke, psycho hitchcock review conservative, is psycho woke, psycho virtuevigil, psycho parents guide, psycho woke score, psycho 1960 review"
  },
  "tropeAudit": [
    {
      "id": "TRADITIONAL-039",
      "name": "Objective Good vs. Evil",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "Hitchcock draws a clear moral line. Marion's theft may be understandable (she wants to marry Sam), but it is still theft, and the film punishes her for it. Norman Bates is portrayed with sympathy (Perkins makes him oddly endearing), but the film never suggests his actions are anything but evil. The psychiatrist's final speech, often dismissed as dated exposition, is in fact a traditional moral verdict: Norman's crimes are the product of his original sin (matricide), and his punishment is permanent psychological damnation. The film never equivocates."
    },
    {
      "id": "TRADITIONAL-035",
      "name": "The Just Lawman",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.10,
      "description": "Private investigator Milton Arbogast is a model of professional diligence. Hired to recover the stolen money, he methodically tracks Marion to the Bates Motel and, through careful questioning and observation, uncovers the inconsistencies in Norman's story. He is competent, calm, and brave. His death is tragic not because he was foolish but because he was thorough. Sheriff Chambers, though initially dismissive, ultimately assists in the investigation. Law enforcement is portrayed as a force for order and justice."
    },
    {
      "id": "TRADITIONAL-030",
      "name": "Biblical Morality",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.10,
      "description": "The film's moral logic is Judeo-Christian through and through. Marion Crane sins (theft, adultery) and is struck down. Norman Bates commits the ultimate sin (murdering his mother) and is consumed by guilt so profound it destroys his identity. The wages of sin is death. There is no redemption arc because Norman is beyond redemption. Hitchcock, raised Catholic, builds a moral universe where transgression is always punished, and the punishment fits the crime with terrible precision."
    },
    {
      "id": "TRADITIONAL-047",
      "name": "Justice Restored",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.80,
      "description": "By the film's end, Norman Bates is in custody and his crimes have been explained. The guilty party is punished. Marion's body (and the stolen money) are recovered from the swamp. Lila and Sam survive to carry the truth forward. The moral order, shattered by Norman's violence, is restored. The final shot (Marion's car being pulled from the swamp) is a visual metaphor for justice: what was hidden is brought to light, what was buried is unearthed, and what was done in darkness is exposed to judgment."
    }
  ]
};

// REVIEW 3: One Flew Over the Cuckoo's Nest (1975)
const review3 = {
  "id": "one-flew-over-the-cuckoos-nest-1975",
  "slug": "one-flew-over-the-cuckoos-nest-1975",
  "title": "One Flew Over the Cuckoo's Nest",
  "year": 1975,
  "type": "film",
  "platform": "Theaters",
  "genre": "Psychological Drama",
  "date": "2026-07-18",
  "datePublished": "2026-07-18",
  "author": "VirtueVigil Editorial Team",
  "readTime": "9 min",
  "poster": "/images/posters/one-flew-over-the-cuckoos-nest-1975.jpg",
  "releaseDate": "1975-11-19",
  "rating": "R (Language, Violence, Mature Themes, Sexual Content)",
  "runtime": "133 min",
  "director": "Milos Forman",
  "writers": [
    "Lawrence Hauben",
    "Bo Goldman"
  ],
  "cast": [
    { "name": "Jack Nicholson", "role": "Randle McMurphy" },
    { "name": "Louise Fletcher", "role": "Nurse Ratched" },
    { "name": "Will Sampson", "role": "Chief Bromden" },
    { "name": "Brad Dourif", "role": "Billy Bibbit" },
    { "name": "Danny DeVito", "role": "Martini" },
    { "name": "Christopher Lloyd", "role": "Taber" },
    { "name": "Sydney Lassick", "role": "Charlie Cheswick" },
    { "name": "William Redfield", "role": "Dale Harding" }
  ],
  "studio": "Fantasy Films",
  "distributor": "United Artists",
  "verdict": "TRADITIONAL",
  "wokeScore": 3.78,
  "tradScore": 22.68,
  "authIndex": 86,
  "scoreMargin": "+19 TRAD",
  "preRelease": false,
  "wokeTrap": false,
  "woke_trap_assessment": {
    "is_trap": false,
    "explanation": "One Flew Over the Cuckoo's Nest is not a woke trap. While it contains a critique of institutional power (WOKE-004), this critique is specific to 1960s-era mental health care and is organic to Ken Kesey's 1962 source novel. The institutional element is present from the opening scenes and is the film's explicit subject, not a hidden payload. Moreover, the film's dominant mode is deeply traditional: McMurphy is a Christ-like sacrificial hero who dies to free the others, which dramatically outweighs the institutional critique in the VVWS calculus."
  },
  "externalScores": {
    "imdb": 8.7,
    "rottenTomatoesCritic": 93,
    "rottenTomatoesAudience": 96,
    "metacritic": 83
  },
  "creative_team": {
    "director": {
      "name": "Milos Forman",
      "ideology": "MODERATE. Forman was a Czech emigre who fled communist Czechoslovakia and had a deep, personal understanding of institutional oppression. His sympathy for the individual against the system is not a fashionable political posture but a lived experience. He directs Cuckoo's Nest with empathy for every character, including Nurse Ratched, whom he insisted be portrayed as believing she is doing the right thing. His perspective is humanist, not ideological."
    },
    "writers": [
      {
        "name": "Lawrence Hauben, Bo Goldman",
        "ideology": "MODERATE. The screenplay adapts Ken Kesey's counterculture novel but strips away the psychedelic excess and first-person narrative gimmickry. What remains is a classical story about one man's spirit against a repressive system, rendered in terms that would have been recognizable to Sophocles. The writers focus on character and drama, not ideology."
      }
    ]
  },
  "parentalGuidance": {
    "sexualContent": "MODERATE. McMurphy arranges for his girlfriend Candy and her friend Rose to visit the ward for a Christmas party. Billy Bibbit loses his virginity to Candy in a scene that is more tender than explicit. Nurse Ratched's weaponization of Billy's sexuality against him (threatening to tell his mother) is psychologically brutal. No nudity.",
    "violence": "HIGH. McMurphy attacks and nearly strangles Nurse Ratched to death. He is subjected to electroconvulsive therapy (shown). Chief Bromden smothers the lobotomized McMurphy with a pillow (a mercy killing). Billy Bibbit slits his own throat. The violence is emotional and psychological as much as physical.",
    "language": "HIGH. Strong profanity throughout, consistent with the institutional setting and McMurphy's character. 1975 standards were looser than earlier decades.",
    "substanceUse": "MODERATE. Alcohol is smuggled into the ward for the Christmas party. Patients get drunk. Medication abuse (forced sedation) is portrayed as part of the institutional cruelty.",
    "matureThemes": "DEFINING. Involuntary commitment, electroconvulsive therapy, lobotomy, suicide, the abuse of institutional power, the destruction of the individual spirit by bureaucracy. This is one of the most emotionally devastating films ever made. It requires emotional maturity to process."
  },
  "summary": {
    "overall": "One Flew Over the Cuckoo's Nest is not merely one of the greatest films ever made. It is one of the most profoundly traditional stories American cinema has ever told, wrapped in the superficially countercultural packaging of Ken Kesey's 1962 novel. The VVWS scores it at TRADITIONAL with a margin of +19, and that score reflects a truth about the film that fifty years of critical commentary has often missed: Randle McMurphy is a Christ figure. He arrives among the lost, challenges the Pharisees, brings joy and liberation to the oppressed, and is ultimately destroyed by the system he threatens, only for his spirit to inspire others to freedom. Jack Nicholson, in the defining performance of his career, plays McMurphy as a small-time con man who feigns insanity to escape a prison work farm and lands in a mental institution run by Nurse Ratched (Louise Fletcher in one of cinema's great villain performances). Ratched maintains order through passive-aggressive cruelty, group therapy as humiliation ritual, and the constant threat of worse punishment. McMurphy, with his irreverent humor and instinctive decency, becomes the patients' champion. He teaches them to laugh, to play cards, to assert themselves. He takes them on a stolen fishing boat into open water and makes them feel like men for the first time in years. The tragedy is that McMurphy's revolution cannot survive Ratched's institutional power. Billy Bibbit, the stuttering young man whom McMurphy has helped find his voice, is destroyed by Ratched's cruel threat to tell his mother about his sexual encounter. Billy kills himself. McMurphy, enraged, attacks Ratched and nearly strangles her. For this, he is lobotomized, reduced to a vacant shell. Chief Bromden (Will Sampson), the towering Native American who has feigned deaf-muteness for years, cannot bear to see his friend like this. He smothers McMurphy with a pillow, then tears the hydrotherapy fountain from the floor and hurls it through the window, escaping into the Oregon countryside as the other patients cheer. The VVWS scoring captures what makes this film so powerful and so contested. The institutional critique (WOKE-004, the mental hospital as oppressive institution) registers at 3.78 points, but this is organic to the source material and to the historical reality of 1960s mental health care. It is not an ideological insertion. The traditional elements dominate the calculus overwhelmingly: McMurphy's rugged individualism (TRADITIONAL-028), his self-sacrifice (TRADITIONAL-026), his defense of the vulnerable patients (TRADITIONAL-045), and the film's clear moral binary between McMurphy's life-affirming rebellion and Ratched's death-dealing order (TRADITIONAL-039). This is a film about one man who will not bend, who pays the ultimate price for refusing to submit, and whose death sets others free. That is the story of the Cross, translated to 1960s Oregon. It is as traditional as narrative gets.",
    "adultInsight": "Cuckoo's Nest endures because it works on multiple levels simultaneously. As a drama about mental health care, it is a devastating indictment of institutional cruelty. As a character study, it is one of the great performances in cinema history, with Nicholson radiating charm, danger, and vulnerability in equal measure. As a political allegory, it speaks to anyone who has ever felt crushed by a system too large to fight. But as a moral story, which is what the VVWS scores, it is a deeply traditional narrative about sacrifice, liberation, and the unconquerable human spirit. The paradox is that a film adapted from a counterculture novel, directed by a Czech emigre, and beloved by the anti-establishment left is, at its core, the most conservative story imaginable: a man dies so that others may live. For parents considering showing this to older teenagers: the film is emotionally shattering but morally instructive. It teaches through tragedy that institutional power without mercy is evil, that laughter and friendship are worth fighting for, and that some things are worth dying to protect.",
    "parentalGuidance": "Rated R and fully earning it. The violence is psychological as much as physical. The electroconvulsive therapy scenes are disturbing. Billy's suicide and McMurphy's lobotomy are devastating. The language is strong throughout. This is a film for mature viewers only (17+). Parents should know that the emotional impact is much greater than the sum of the content warnings. The film will stay with a viewer for life. It is worth showing to mature older teenagers, but it should be watched together and discussed afterward."
  },
  "seo": {
    "titleTag": "Is One Flew Over the Cuckoo's Nest Woke? | VirtueVigil Review (1975)",
    "metaDescription": "Is Cuckoo's Nest woke? We score the 1975 Best Picture winner through the VVWS lens. TRADITIONAL verdict for Nicholson's Christ-like sacrifice against institutional oppression.",
    "keywords": "one flew over the cuckoos nest woke, cuckoos nest review conservative, is cuckoos nest woke, cuckoos nest virtuevigil, cuckoos nest parents guide, cuckoos nest woke score"
  },
  "tropeAudit": [
    {
      "id": "WOKE-004",
      "name": "Institutional Evil",
      "category": "Woke",
      "severity": 3,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 3.78,
      "description": "The mental institution is portrayed as a fundamentally corrupt system where Nurse Ratched maintains control through psychological manipulation, forced medication, electroconvulsive therapy, and ultimately lobotomy. However, this critique is specific to 1960s-era mental health care rather than a general anti-institutional screed, and it is organic to Ken Kesey's 1962 source novel (Kesey worked as an orderly in a VA hospital). The authenticity multiplier (0.7) is High because the critique arises from genuine observation, not ideological insertion."
    },
    {
      "id": "TRADITIONAL-028",
      "name": "The Rugged Individualist",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "McMurphy is the archetypal rugged individualist: a man who solves problems through his own character, charm, and force of will rather than appeal to authority. He does not ask permission. He does not fill out forms. He sees a group of broken men and decides, on his own initiative, to teach them how to live again. His methods (gambling, fishing, laughter, whiskey) are distinctly American and distinctly anti-bureaucratic. He is Huck Finn in a mental ward."
    },
    {
      "id": "TRADITIONAL-026",
      "name": "The Self-Sacrificing Hero",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.30,
      "description": "McMurphy's arc is sacrificial from the moment he learns his sentence can be extended indefinitely. He could have escaped after the fishing trip, but he stays. He throws the Christmas party knowing it will cost him. He attacks Ratched after Billy's suicide, knowing it will destroy him. And it does: he is lobotomized, reduced to a vegetative state. Chief Bromden's mercy killing (smothering McMurphy with a pillow) completes the Christ parallel: the sacrifice is accepted, the spirit is freed, and the body is left behind so that others may live. This is the most profound traditional narrative in modern American cinema."
    },
    {
      "id": "TRADITIONAL-045",
      "name": "Defense of the Innocent",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.30,
      "description": "Everything McMurphy does is in defense of the vulnerable patients: Billy Bibbit, whom he helps find his voice; Chief Bromden, whom he treats as a man when everyone else treats as furniture; Cheswick, whose tantrums McMurphy channels into dignity; even Harding, the repressed intellectual who finally stands up to Ratched. McMurphy is not in the ward for himself. He is there for them. His protective instinct is the engine of the entire film."
    },
    {
      "id": "TRADITIONAL-039",
      "name": "Objective Good vs. Evil",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "The moral binary is unambiguous. McMurphy is life, laughter, and liberation. Ratched is death, control, and submission. The film does not suggest Ratched has a point or that McMurphy is reckless. It takes a clear side. Ratched's evil is all the more terrifying for being dressed in professional calm rather than villainous sneering. She is evil precisely because she believes she is good, and the film's moral clarity on this point has not aged a day."
    }
  ]
};

// Append all three reviews
reviews.push(review1, review2, review3);
fs.writeFileSync(reviewsPath, JSON.stringify(reviews, null, 2));
console.log('Appended 3 reviews. New count:', reviews.length);