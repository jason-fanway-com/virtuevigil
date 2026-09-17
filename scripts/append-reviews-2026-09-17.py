#!/usr/bin/env python3
"""Append 3 reviews for 2026-09-17."""
import json, sys

with open('src/data/reviews.json') as f:
    reviews = json.load(f)

initial_count = len(reviews)

# ── Review 1: Resident Evil (2026) ──────────────────────────────────
resident_evil = {
    "id": "resident-evil-2026",
    "slug": "resident-evil-2026",
    "title": "Resident Evil (2026)",
    "year": 2026,
    "type": "movie",
    "platform": "Theaters",
    "genre": "Survival Horror, Action",
    "date": "2026-09-17",
    "datePublished": "2026-09-17",
    "author": "VirtueVigil Editorial Team",
    "readTime": "4 min read",
    "poster": "/images/posters/resident-evil-2026.jpg",
    "releaseDate": "2026-09-18",
    "rating": "R (Horror Violence, Language, Gore)",
    "runtime": "95 min",
    "director": "Zach Cregger",
    "writers": ["Zach Cregger", "Shay Hatten"],
    "cast": [
        {"name": "Austin Abrams", "role": "Bryan"},
        {"name": "Zach Cherry", "role": "Carl"},
        {"name": "Kali Reis", "role": "Maxine"},
        {"name": "Paul Walter Hauser", "role": "Paul"},
        {"name": "Johnno Wilson", "role": "Sheriff Wilson"},
        {"name": "Emily Piggford", "role": "Dr. Maria Stokes"}
    ],
    "studio": "Columbia Pictures / Constantin Film / PlayStation Productions",
    "distributor": "Sony Pictures Releasing",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 2.2,
    "tradScore": 7.98,
    "authIndex": "Low",
    "scoreMargin": "+5.78 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Resident Evil (2026) is a survival horror film that delivers exactly what it promises from the opening scene: a man fighting through a zombie outbreak in a city overrun by bioweapon monsters. The Umbrella Corporation's villainy is a genre convention taken directly from the video games, not an ideological statement about real-world capitalism. The film never pivots to political messaging."
    },
    "seo": {
        "titleTag": "Is Resident Evil (2026) Woke? Zach Cregger's Horror Reboot Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Resident Evil (2026): Zach Cregger's reboot starring Austin Abrams as a medical courier fighting through Raccoon City's zombie outbreak. VVWS verdict: TRADITIONAL LEAN (+5.78). Parental guidance included.",
        "keywords": "is resident evil 2026 woke, resident evil 2026 review, resident evil virtuevigil, resident evil reboot review, zach cregger resident evil, austin abrams resident evil, resident evil parents guide"
    },
    "externalScores": {
        "imdb": "N/A",
        "rottenTomatoes": "97%",
        "metacritic": "N/A"
    },
    "creative_team": {
        "director": "Zach Cregger",
        "writer": "Zach Cregger, Shay Hatten",
        "top_cast": [
            "Austin Abrams as Bryan",
            "Zach Cherry as Carl",
            "Kali Reis as Maxine",
            "Paul Walter Hauser as Paul",
            "Johnno Wilson as Sheriff Wilson"
        ],
        "full_cast": [
            "Austin Abrams", "Zach Cherry", "Kali Reis", "Paul Walter Hauser",
            "Johnno Wilson", "Emily Piggford", "Will Merrick", "Zoe Bellas",
            "Chris Lew Kum Hoi", "Griffin Newman", "Magdalena Sittovaas"
        ],
        "producers": [
            {"name": "Robert Kulzer"},
            {"name": "Zach Cregger"},
            {"name": "Roy Lee"},
            {"name": "Miri Yoon"},
            {"name": "Carter Swan"},
            {"name": "Asad Qizilbash"}
        ],
        "composer": "Hays Holladay, Ryan Holladay"
    },
    "parentalGuidance": {
        "violence": "Heavy. Zombie attacks, creature transformations, gunfire, and gore throughout. This is a hard-R horror film with visceral creature violence, body horror, and frequent death.",
        "language": "Moderate to heavy. F-bombs and profanity consistent with an R-rated horror film. Not gratuitous but present.",
        "sexualContent": "Minimal. No sexual content of note.",
        "drugsAlcohol": "Minimal. No significant drug or alcohol content.",
        "intenseScenes": "The opening outbreak sequence is relentless. Creature designs are grotesque. Several jump scares and sustained sequences of tension. The medical/hospital setting adds body horror elements.",
        "ageRecommendation": "17+. The R rating is earned through sustained horror violence and gore. This is not a supernatural thriller; it is a survival horror film with graphic creature violence. Not appropriate for children or most teenagers."
    },
    "spoiler_alert": False,
    "tropeAudit": [
        {
            "id": "TRAD-RE26-001",
            "name": "The Rugged Individualist",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.0,
            "explanation": "Bryan is a medical courier, a lone worker who must survive through his own resourcefulness and grit. He has no team, no backup, no institutional support. His survival depends entirely on his individual capability and will."
        },
        {
            "id": "TRAD-RE26-002",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 4.0,
            "explanation": "The moral universe of the film is stark: uninfected humans versus the monsters created by Umbrella's viral outbreak. There is no moral ambiguity about the infected; they are threats to be neutralized. The survivors are unambiguously the good guys."
        },
        {
            "id": "TRAD-RE26-003",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.98,
            "explanation": "Bryan's journey involves assisting other survivors he encounters, even at personal risk. While his primary drive is survival, he does not abandon others to save himself, which places him in the tradition of reluctant protectors."
        },
        {
            "id": "WOKE-RE26-001",
            "name": "The Evil Capitalist",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 2.1,
            "explanation": "The Umbrella Corporation is the cause of the outbreak, a pharmaceutical giant whose bioweapons research has destroyed Raccoon City. However, this is a direct adaptation of the video game source material and functions as a genre convention rather than a contemporary political statement. Umbrella is evil because it made monsters, not because it is a metaphor for capitalism."
        },
        {
            "id": "WOKE-RE26-002",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.1,
            "explanation": "Kali Reis appears as Maxine, an Umbrella enforcer. She is a physically imposing female antagonist, but she works for the villain and is not presented as a heroic ideal. The female action role exists in service of the genre, not as ideological positioning."
        }
    ],
    "fidelityCasting": {
        "genderSwaps": False,
        "raceSwaps": False,
        "deiCasting": False,
        "notes": "Original characters not drawn from existing IP with established demographics. No casting decisions made for ideological reasons."
    },
    "summary": {
        "overview": "Resident Evil (2026) is Zach Cregger's reboot of the long-running survival horror franchise based on Capcom's video game series. Austin Abrams stars as Bryan, a medical courier making a routine delivery to Raccoon City General Hospital when a viral outbreak transforms the city into a hellscape of infected monsters. Zach Cherry, Kali Reis, and Paul Walter Hauser co-star as Umbrella Corporation employees caught in the chaos. The film adapts the setting and events of Resident Evil 2 (1998) into a modern context with an original cast of characters.",
        "overall": "Resident Evil (2026) is the rare video game adaptation that understands its assignment. Zach Cregger, coming off the horror success of Barbarian, strips away two decades of franchise baggage and returns to what made the games work: one vulnerable person in a sealed environment where every corner might kill you.\n\nThe film's ideological content is refreshingly close to zero. This is a survival horror movie, and it never pretends to be anything else. Bryan is not a chosen one. He is not on a journey of self-discovery. He is a medical courier who picked the wrong day to make a delivery, and the film respects the audience enough to let that be enough.\n\nThe Umbrella Corporation is the antagonist, as it has been in every Resident Evil property since 1996. A viewer looking for anti-capitalist messaging could find it if they squint, but the film does not do the work for them. Umbrella is evil because it made monsters, not because it is a metaphor for free markets. The corporation's villainy is a genre convention as old as Frankenstein, and Cregger treats it as the furniture of the world rather than a sermon waiting to be delivered.\n\nKali Reis appears as Maxine, a physically imposing Umbrella enforcer, and Austin Abrams is a capable but fundamentally ordinary lead. Neither is presented as a political statement. The cast is diverse without the film drawing attention to it, which is the ideal: diversity as a fact of the world rather than a plank of a platform.\n\nThe film earns its TRADITIONAL LEAN verdict honestly. The moral universe is clear. The monsters are monsters, the survivors are survivors, and the path to safety runs through competence, courage, and the refusal to leave others behind. Those are older values than any political moment, and Resident Evil (2026) wears them well.",
        "bestFor": "Fans of survival horror who have been waiting for a Resident Evil film that respects the source material. Viewers who want a tight, well-crafted horror experience with no ideological baggage.",
        "skipIf": "You are sensitive to graphic horror violence and body horror. The R rating is not cosmetic. This is a genuinely intense horror film.",
        "wokeElements": "Minimal. The Umbrella Corporation's villainy is a genre convention from the games, not a contemporary political allegory. Kali Reis as a female enforcer is a character choice, not a statement.",
        "traditionalElements": "Bryan is a rugged individualist surviving on his own wits. The moral universe has clear lines between good and evil. Survival depends on competence and courage, not identity. The film never lectures.",
        "parentalGuidance": "Rated R for sustained horror violence, gore, and creature effects. The body horror is graphic, and the tension is unrelenting. Not appropriate for children or young teens. The zombie genre's violence is the primary concern; there is no ideological content that requires parental pre-screening.",
        "adultInsight": "Resident Evil (2026) is worth noting because it is a major studio release with a $75 million budget that commits fully to a traditional action-horror experience without ideological padding. In an era where genre films frequently carry political subtext, Cregger's film is notable for what it refuses to do: it does not lecture, it does not signal, it does not apologize for being exactly what it is. That restraint is a form of trust in the audience, and it is worth rewarding."
    }
}

# ── Review 2: Paths of Glory (1957) ─────────────────────────────────
paths_of_glory = {
    "id": "paths-of-glory-1957",
    "slug": "paths-of-glory-1957",
    "title": "Paths of Glory (1957)",
    "year": 1957,
    "type": "movie",
    "platform": "Streaming / Physical Media",
    "genre": "War, Drama, Anti-War",
    "date": "2026-09-17",
    "datePublished": "2026-09-17",
    "author": "VirtueVigil Editorial Team",
    "readTime": "5 min read",
    "poster": "/images/posters/paths-of-glory-1957.jpg",
    "releaseDate": "1957-12-20",
    "rating": "Not Rated (War Violence, Thematic Intensity)",
    "runtime": "88 min",
    "director": "Stanley Kubrick",
    "writers": ["Stanley Kubrick", "Calder Willingham", "Jim Thompson"],
    "cast": [
        {"name": "Kirk Douglas", "role": "Colonel Dax"},
        {"name": "Ralph Meeker", "role": "Corporal Paris"},
        {"name": "Adolphe Menjou", "role": "Major General Broulard"},
        {"name": "George Macready", "role": "Brigadier General Mireau"},
        {"name": "Wayne Morris", "role": "Lieutenant Roget"},
        {"name": "Richard Anderson", "role": "Major Saint-Auban"},
        {"name": "Timothy Carey", "role": "Private Ferol"},
        {"name": "Joe Turkel", "role": "Private Arnaud"}
    ],
    "studio": "Bryna Productions / Harris-Kubrick Pictures",
    "distributor": "United Artists",
    "verdict": "BALANCED TRADITIONAL",
    "wokeScore": 3.6,
    "tradScore": 17.2,
    "authIndex": "Low",
    "scoreMargin": "+13.6 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Paths of Glory is not a woke trap. It is an anti-war film from 1957 that critiques military corruption through a universal moral framework, not a progressive political one. The film's criticisms are specific to corrupt individuals who abuse their authority, not to the institution of the military or to Western civilization broadly. Colonel Dax, the hero, is himself a military officer who represents the ideals the institution claims to uphold."
    },
    "seo": {
        "titleTag": "Is Paths of Glory (1957) Woke? Stanley Kubrick's Anti-War Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Paths of Glory (1957): Stanley Kubrick's WWI masterpiece starring Kirk Douglas as a colonel defending soldiers against a corrupt court-martial. VVWS verdict: BALANCED TRADITIONAL (+13.6). Parental guidance included.",
        "keywords": "is paths of glory woke, paths of glory 1957 review, paths of glory virtuevigil, stanley kubrick paths of glory, kirk douglas paths of glory, paths of glory parents guide, wwi movie review"
    },
    "externalScores": {
        "imdb": "8.4/10",
        "rottenTomatoes": "96%",
        "metacritic": "90/100"
    },
    "creative_team": {
        "director": "Stanley Kubrick",
        "writer": "Stanley Kubrick, Calder Willingham, Jim Thompson",
        "top_cast": [
            "Kirk Douglas as Colonel Dax",
            "Ralph Meeker as Corporal Paris",
            "Adolphe Menjou as Major General Broulard",
            "George Macready as Brigadier General Mireau",
            "Wayne Morris as Lieutenant Roget"
        ],
        "full_cast": [
            "Kirk Douglas", "Ralph Meeker", "Adolphe Menjou", "George Macready",
            "Wayne Morris", "Richard Anderson", "Timothy Carey", "Joe Turkel"
        ],
        "producers": [
            {"name": "James B. Harris"}
        ],
        "composer": "Gerald Fried"
    },
    "summary": {
        "overview": "Paths of Glory (1957) is Stanley Kubrick's anti-war masterpiece set in the trenches of World War I France. Kirk Douglas stars as Colonel Dax, a French officer ordered to lead his regiment in a suicidal assault on a German stronghold called the Anthill. When the attack fails and soldiers refuse to leave the trenches under impossible fire, the French high command scapegoats three enlisted men for cowardice. Dax, a criminal defense lawyer in civilian life, volunteers to defend them at a court-martial that is a transparent farce. Ralph Meeker, Adolphe Menjou, and George Macready co-star in one of the most devastating war films ever made.",
        "overall": "Paths of Glory runs 88 minutes and lands with more moral force than films three times its length. Stanley Kubrick was 29 years old when he made it, and the precision of his outrage is still shocking nearly 70 years later.\n\nThe film is often described as anti-war, and it is, but the label undersells what it actually does. Paths of Glory is not anti-soldier. It is not anti-military. It is anti-corruption, and it distinguishes with surgical care between the institution and the men who betray it. Colonel Dax is a French Army officer who believes in duty, honor, and the chain of command. The tragedy is that the men above him in that chain believe in nothing but their own advancement.\n\nThis distinction matters enormously for how we score the film. A modern viewer might see the French generals conspiring to execute innocent men and conclude the film shares their distrust of institutions. It does not. Dax is the institution too, and Dax is the hero. The film's target is not the military, the state, or Western civilization. Its target is the specific, recognizable sin of powerful men who treat other men as disposable.\n\nKubrick was adapting Humphrey Cobb's 1935 novel, which was itself based on the real Souain corporals affair, in which four French soldiers were executed as scapegoats for a failed offensive. The film's anger is grounded in historical fact, not ideological posture. It is a film about justice denied, and that is a theme as old as the Book of Job.\n\nThe film earns its BALANCED TRADITIONAL verdict through the weight of its traditional elements. Dax is a principled patriarch risking his career for his men. The moral universe is stark: corrupt generals are evil, dutiful soldiers are good, and the difference is knowable. Justice, even when denied, is recognized as a real thing worth fighting for. These are not woke commitments. They are the moral language of the West at its best.\n\nThe woke elements that do appear are artifacts of the film's anti-authoritarian stance being retroactively claimed by modern sensibilities. The French high command's corruption could be read as a blanket indictment of institutional authority, but the film itself does not make that argument. It is too precise for that. Broulard and Mireau are villains because of what they did, not because of what they represent.",
        "bestFor": "Anyone who cares about the moral tradition of Western cinema. Students of Kubrick. Viewers who want to see a great actor (Douglas) at the peak of his powers in a role that required genuine courage to play.",
        "skipIf": "You need a happy ending. The executions happen. The film is honest about what it is doing and does not offer false comfort. It is emotionally devastating.",
        "wokeElements": "The film's portrayal of a corrupt military hierarchy could be read as Institutional Evil, but this is a specific critique of specific men, not a blanket condemnation of military or state authority. Colonel Dax represents the ideals the institution is supposed to uphold.",
        "traditionalElements": "Colonel Dax is a self-sacrificing hero who risks his career and life for his men. The moral universe is objective: corrupt generals are evil, innocent soldiers are good. Justice is presented as a real standard, even when denied. Dax embodies principled masculine leadership under impossible pressure.",
        "parentalGuidance": "Not rated when released. Contains war violence, execution by firing squad (disturbing but not graphic by modern standards), and intense thematic material about injustice and death. The emotional weight is heavier than the visual content. Appropriate for mature teens and up.",
        "adultInsight": "Paths of Glory matters for VirtueVigil readers because it demonstrates that moral clarity in art transcends political fashion. A film made in 1957 about events from 1915 speaks directly to 2026 because it deals in permanent things: courage, cowardice, justice, and the cost of betraying men who trust you. The fact that modern progressives might claim this film as anti-institutional does not make it theirs. The film's moral framework is older than the left-right split and deeper than any ideology. That is what makes it a classic."
    },
    "parentalGuidance": {
        "violence": "War violence in the WWI trench setting. The court-martial and firing squad execution sequence is emotionally brutal but not graphically explicit by modern standards. The psychological weight is the primary concern.",
        "language": "Minimal by modern standards. No profanity of note. The film's intensity comes from its themes, not its language.",
        "sexualContent": "None.",
        "drugsAlcohol": "Background drinking among officers is period-appropriate and not emphasized.",
        "intenseScenes": "The execution sequence is among the most devastating in cinema history, not for its violence but for its moral weight. The court-martial is infuriating to watch. The trench warfare sequences are tense but not gory.",
        "ageRecommendation": "14+. The film is not graphically violent. The primary challenge is its emotional and moral weight. Mature teenagers studying history or film would benefit enormously from viewing it."
    },
    "spoiler_alert": False,
    "tropeAudit": [
        {
            "id": "TRAD-POG-001",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.0,
            "explanation": "Colonel Dax risks his military career, his reputation, and potentially his life to defend three condemned soldiers. He leads the initial charge himself, refuses to let his men face fire he would not face, and then volunteers to defend them at a court-martial he knows is rigged. Self-sacrifice is the organizing principle of his character."
        },
        {
            "id": "TRAD-POG-002",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 4.0,
            "explanation": "The three condemned men are innocent of cowardice. One was chosen by lot, one was selected by a corrupt officer to silence him, and one was deemed a social undesirable. Dax's defense of them is the moral center of the film, and his failure to save them is the tragedy."
        },
        {
            "id": "TRAD-POG-003",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 4.0,
            "explanation": "The moral universe of the film is unambiguous. Generals Broulard and Mireau are evil; Dax and the condemned soldiers are good. The film does not blur these lines or ask the audience to see both sides. It presents a clear moral binary and demands a response."
        },
        {
            "id": "TRAD-POG-004",
            "name": "Justice Restored",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 2.1,
            "explanation": "While the three soldiers are executed, Dax ensures that General Mireau faces investigation for ordering artillery fire on his own men. Broulard's offer of promotion to Dax, which Dax rejects with contempt, reveals the corruption of the system. Partial justice is achieved: the guilty are exposed, even if the punishment is incomplete."
        },
        {
            "id": "TRAD-POG-005",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Colonel Dax functions as a father figure to his regiment. He provides moral leadership, refuses to sacrifice his men for personal gain, and speaks truth to power even when it costs him. His authority is rooted in service, not ambition."
        },
        {
            "id": "WOKE-POG-001",
            "name": "Institutional Evil",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 3.5,
            "explanation": "The French military high command is portrayed as corrupt, self-serving, and willing to execute innocent men to cover its failures. However, the film's critique is specific: Generals Broulard and Mireau are villains because of their individual actions, not because all military institutions are inherently evil. Dax is a military officer and the hero. The film criticizes corruption within an institution, not the institution itself."
        },
        {
            "id": "WOKE-POG-002",
            "name": "Anti-Western Revisionism",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.1,
            "explanation": "The film's portrayal of French military incompetence could be read by a modern audience as a critique of Western military tradition, but this is not the film's intent. It is based on a specific historical event and targets specific individuals. Kubrick's concerns are universal, not ideological."
        }
    ],
    "fidelityCasting": {
        "genderSwaps": False,
        "raceSwaps": False,
        "deiCasting": False,
        "notes": "1957 film with period-appropriate casting. No identity-based casting decisions. Kirk Douglas, a Jewish actor, plays the French Colonel Dax, a casting choice based on star power and performance, not identity."
    }
}

# ── Review 3: Neagley (2026) ────────────────────────────────────────
neagley = {
    "id": "neagley-2026",
    "slug": "neagley-2026",
    "title": "Neagley (2026)",
    "year": 2026,
    "type": "series",
    "platform": "Amazon Prime Video",
    "genre": "Action, Crime, Thriller",
    "date": "2026-09-17",
    "datePublished": "2026-09-17",
    "author": "VirtueVigil Editorial Team",
    "readTime": "5 min read",
    "poster": "/images/posters/neagley-2026.jpg",
    "releaseDate": "2026-09-16",
    "rating": "TV-MA (Violence, Language)",
    "runtime": "8 episodes (41-57 min each)",
    "director": "Sam Hill, Gary Fleder, Phil Abraham, MJ Bassett",
    "writers": ["Nick Santora", "Nicholas Wootton", "Adam Higgs", "Kyle Long", "Lacey Herbert"],
    "showrunner": "Nick Santora, Nicholas Wootton",
    "cast": [
        {"name": "Maria Sten", "role": "Frances Neagley"},
        {"name": "Greyston Holt", "role": "Detective Hudson Riley"},
        {"name": "Adeline Rudolph", "role": "Renee Birdwhistle"},
        {"name": "Jasper Jones", "role": "Keno"},
        {"name": "Matthew Del Negro", "role": "Pierce Woodrow"},
        {"name": "Damon Herriman", "role": "Lawrence Cole"},
        {"name": "Alan Ritchson", "role": "Jack Reacher (guest)"}
    ],
    "studio": "Amazon MGM Studios / Paramount Television Studios / Skydance Television",
    "distributor": "Amazon Prime Video",
    "verdict": "BALANCED TRADITIONAL",
    "wokeScore": 0.45,
    "tradScore": 12.08,
    "authIndex": "Low",
    "scoreMargin": "+11.63 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Neagley is a straightforward crime thriller in the Reacher universe, a franchise built on traditional masculine virtues. The show features a female lead but does not frame her competence as a political statement. There is no bait-and-switch into ideological territory. The series delivers what it promises: a procedural investigation with action beats."
    },
    "seo": {
        "titleTag": "Is Neagley (2026) Woke? Amazon's Reacher Spin-Off Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Neagley (2026): Amazon Prime's Reacher spin-off starring Maria Sten as Frances Neagley investigating a friend's suspicious death. VVWS verdict: BALANCED TRADITIONAL (+11.63). Parental guidance included.",
        "keywords": "is neagley woke, neagley review, neagley 2026 virtuevigil, reacher spin-off review, maria sten neagley, neagley amazon prime, neagley parents guide"
    },
    "externalScores": {
        "imdb": "N/A",
        "rottenTomatoes": "90%",
        "metacritic": "69/100"
    },
    "creative_team": {
        "director": "Sam Hill, Gary Fleder, Phil Abraham, MJ Bassett",
        "writer": "Nick Santora, Nicholas Wootton, Adam Higgs, Kyle Long, Lacey Herbert",
        "top_cast": [
            "Maria Sten as Frances Neagley",
            "Greyston Holt as Detective Hudson Riley",
            "Adeline Rudolph as Renee Birdwhistle",
            "Jasper Jones as Keno",
            "Matthew Del Negro as Pierce Woodrow"
        ],
        "full_cast": [
            "Maria Sten", "Greyston Holt", "Adeline Rudolph", "Jasper Jones",
            "Matthew Del Negro", "Damon Herriman", "Alan Ritchson"
        ],
        "producers": [
            {"name": "Nick Santora"},
            {"name": "Nicholas Wootton"},
            {"name": "Adam Higgs"},
            {"name": "Sam Hill"},
            {"name": "Lisa Kussner"},
            {"name": "Paula Wagner"},
            {"name": "Lee Child"},
            {"name": "Don Granger"},
            {"name": "David Ellison"},
            {"name": "Dana Goldberg"},
            {"name": "Matt Thunell"}
        ],
        "composer": "Tony Morales"
    },
    "summary": {
        "overview": "Neagley (2026) is Amazon Prime Video's spin-off of the hit series Reacher, created by Nick Santora and Nicholas Wootton. Maria Sten reprises her role as Frances Neagley, a former military police investigator with a particular set of skills and a personal code. When an old friend dies under suspicious circumstances, Neagley pursues the truth through a web of corruption and violence, assembling a team of allies along the way. Greyston Holt, Adeline Rudolph, Jasper Jones, Matthew Del Negro, and Damon Herriman co-star, with Alan Ritchson appearing as Jack Reacher in a guest role. All eight episodes dropped September 16, 2026.",
        "overall": "Neagley arrives with a question baked into its premise: can you spin off a Reacher character into her own show without turning the franchise's traditional masculinity into a problem to be solved? The answer, gratifyingly, is yes.\n\nThe show's ideological restraint is its quietest virtue. Maria Sten's Frances Neagley is competent, disciplined, and lethal. She is also loyal, principled, and haunted by the things she has done. None of this is framed as a political statement about women in action roles. She simply is what she is: a former military police investigator who is very good at finding people who do not want to be found.\n\nThis is the difference between a female lead and a Girl Boss. A Girl Boss exists to prove something about gender. Her competence is a thesis. Her toughness is a rebuke. Neagley, by contrast, exists to solve a mystery and avenge a friend. Her competence is treated as a given, not an argument. The show trusts the audience to accept a capable woman without needing to explain why she is capable. That confidence is the mark of a production that respects its viewers.\n\nThe Reacher DNA is intact. The show values physical competence, personal loyalty, and the refusal to let the powerful crush the powerless. Neagley does not have Reacher's size, but she has his moral clarity and his willingness to walk into danger when someone needs protection. When Alan Ritchson shows up for his guest appearance, it feels like a seal of approval rather than a handoff. The franchise's values have been preserved.\n\nThe cast is diverse, and the show handles it correctly: by not handling it at all. Maria Sten is Danish, Adeline Rudolph is of Korean and German descent, Jasper Jones is Black. The show does not call attention to any of this. Characters are characters, not demographic checkboxes. This is diversity as it should be: a reflection of the world that exists, not a thesis about the world that should exist.\n\nThe series earns its BALANCED TRADITIONAL verdict through the accumulated weight of its Reacher-universe values. Justice, loyalty, competence, and the willingness to defend those who cannot defend themselves drive every episode. The show's female lead does not make it woke. A woke show would use her as an argument. Neagley uses her as a protagonist, and the difference is everything.",
        "bestFor": "Fans of Reacher who want more of that universe's moral clarity. Viewers who enjoy competent, well-paced crime thrillers with action beats. Anyone who has been waiting for a female-led action series that does not feel the need to announce its politics.",
        "skipIf": "You need Reacher's physical presence to enjoy the franchise. Neagley solves problems differently, with more planning and less punching, though the violence is still present.",
        "wokeElements": "Minimal to none. A female lead in a traditionally male genre could be a Girl Boss signal, but the show treats Neagley's competence as a fact rather than a political point. The diverse cast is handled with the correct instinct: present it without commenting on it.",
        "traditionalElements": "The Reacher-universe values are intact: personal loyalty, physical competence, defense of the innocent, and the conviction that justice is worth pursuing even when the system won't help. Neagley's investigation is driven by loyalty to a dead friend, a bond the show treats as sacred.",
        "parentalGuidance": "Rated TV-MA for violence and language. The violence is consistent with the Reacher franchise: brutal, efficient, and consequential. Profanity is present. The show deals with themes of corruption, murder, and personal trauma. Not for children.",
        "adultInsight": "Neagley is valuable as a case study in how to do a female-led spin-off without betraying the source material's values. The show proves that you can hand the lead to a woman without turning the franchise into a lecture. Parents who enjoyed Reacher can watch this with the same expectations: moral clarity, competent action, and a protagonist who believes in justice. The packaging is different but the product is the same."
    },
    "parentalGuidance": {
        "violence": "Brutal and efficient, consistent with the Reacher franchise. Fistfights, gunfire, and physical confrontations. Violence is consequential and not glamorized.",
        "language": "Moderate to heavy profanity, consistent with the Reacher universe's tone.",
        "sexualContent": "Minimal. No significant sexual content.",
        "drugsAlcohol": "Background drinking. No significant drug content.",
        "intenseScenes": "Several action sequences with genuine tension. The investigation deals with murder and corruption. Some scenes of personal trauma and emotional intensity.",
        "ageRecommendation": "16+. The TV-MA rating is earned through violence and language. Consistent with the parent series Reacher. Not appropriate for children."
    },
    "spoiler_alert": False,
    "tropeAudit": [
        {
            "id": "TRAD-NEA-001",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.0,
            "explanation": "Neagley risks her safety, her freedom, and her emotional well-being to investigate a friend's death. She is not paid for this; she is not ordered to do it. The investigation is an act of loyalty that costs her, and she pays the cost willingly."
        },
        {
            "id": "TRAD-NEA-002",
            "name": "The Meritocratic Triumph",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Neagley's skills and position are presented as the result of her own effort and ability. She earned her place in military police through competence, not identity. The show does not frame her achievements as a victory over systemic barriers; it frames them as the natural result of being very good at what she does."
        },
        {
            "id": "TRAD-NEA-003",
            "name": "The Just Lawman",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.0,
            "explanation": "Neagley operates outside official channels but in service of justice. Her investigation is not an attack on the system but a supplement to it, pursuing truth where the system has failed. She represents the ideal of justice that institutions are supposed to serve."
        },
        {
            "id": "TRAD-NEA-004",
            "name": "Justice Restored",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.0,
            "explanation": "The season's arc drives toward the uncovering of truth and the punishment of those responsible for harm. Justice is the organizing principle of the narrative, and the show treats it as a real and achievable thing, not an abstract concept."
        },
        {
            "id": "TRAD-NEA-005",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.98,
            "explanation": "Neagley's investigation is motivated by loyalty to a dead friend, but it expands to encompass the protection of others who would be victimized by the same forces. Her protective instinct is a throughline."
        },
        {
            "id": "WOKE-NEA-001",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": 0.45,
            "explanation": "A female lead in an action-crime series could be read as Girl Boss positioning, but the show does not do the work of making her gender a political point. Neagley is competent because she is competent, not because the show wants to prove women can be tough. Her abilities are treated as a given, which removes the ideological charge."
        }
    ],
    "fidelityCasting": {
        "genderSwaps": False,
        "raceSwaps": False,
        "deiCasting": False,
        "notes": "Maria Sten was established as Neagley in the Reacher series (2022). This is a spin-off of an existing character, not a reimagining. The diverse supporting cast is handled without ideological signaling. Alan Ritchson appears as Reacher, maintaining continuity."
    }
}

# Append
reviews.extend([resident_evil, paths_of_glory, neagley])
final_count = len(reviews)

with open('src/data/reviews.json', 'w') as f:
    json.dump(reviews, f, indent=2)

print(f"Appended 3 reviews. {initial_count} → {final_count}")
print(f"1. resident-evil-2026 → TRADITIONAL LEAN (+5.78)")
print(f"2. paths-of-glory-1957 → BALANCED TRADITIONAL (+13.6)")
print(f"3. neagley-2026 → BALANCED TRADITIONAL (+11.63)")