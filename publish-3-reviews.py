#!/usr/bin/env python3
"""
Publish 3 reviews for July 29, 2026:
1. Motor City (2026) - Action/Revenge Thriller
2. The Usual Suspects (1995) - Neo-Noir Catalog Backfill
3. Furious S1 (2026) - TV Series Premiere
"""
import json, sys, os

REPO = "/Users/joestrazza/virtuevigil"
DATA = os.path.join(REPO, "src/data/reviews.json")

def load():
    with open(DATA, "r") as f:
        return json.load(f)

def save(reviews):
    with open(DATA, "w") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)

# ─── REVIEW 1: Motor City (2026) ───
motor_city = {
    "id": "motor-city-2026",
    "slug": "motor-city-2026",
    "title": "Motor City",
    "year": 2026,
    "type": "movie",
    "platform": "Theaters",
    "genre": "Action, Revenge Thriller, Crime",
    "date": "2026-07-29",
    "datePublished": "2026-07-29",
    "author": "VirtueVigil Editorial Team",
    "readTime": "5 min read",
    "poster": "/images/posters/motor-city-2026.jpg",
    "releaseDate": "2026-07-24",
    "rating": "R",
    "runtime": "103 minutes",
    "director": "Potsy Ponciroli",
    "writers": ["Chad St. John"],
    "cast": [
        "Alan Ritchson",
        "Shailene Woodley",
        "Ben Foster",
        "Pablo Schreiber",
        "Lionel Boyce",
        "Ben McKenzie",
        "Amar Chadha-Patel"
    ],
    "studio": "Stampede Ventures",
    "distributor": "IFC Films",
    "verdict": "TRADITIONAL",
    "wokeScore": 3.0,
    "tradScore": 16.1,
    "scoreMargin": 13.1,
    "authIndex": "72",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Not a woke trap. The corrupt cop subplot (WOKE-004) is visible from the first act. The dominant ideology is traditional: personal vengeance as justice, loyalty to loved ones, and a clear good-vs-evil moral framework."
    },
    "spoiler_alert": True,
    "parentalGuidance": "Rated R for strong violence throughout, including brutal hand-to-hand combat, gun violence, and disturbing imagery. Language throughout. Brief drug-related content. Not suitable for children. For adults, the film is a straightforward revenge thriller with a traditional moral core: the guilty are punished, love is worth fighting for, and justice, when denied by the system, is pursued by the individual.",
    "fidelityCasting": None,
    "creative_team": {
        "director": {"name": "Potsy Ponciroli", "role": "Director"},
        "writer": {"name": "Chad St. John", "role": "Screenwriter"},
        "top_cast": [
            {"name": "Alan Ritchson", "role": "John Miller"},
            {"name": "Shailene Woodley", "role": "Sophia Hammond"},
            {"name": "Ben Foster", "role": "Reynolds"},
            {"name": "Pablo Schreiber", "role": "Savick"},
            {"name": "Lionel Boyce", "role": "Youngblood"}
        ],
        "full_cast": [
            {"name": "Alan Ritchson", "role": "John Miller"},
            {"name": "Shailene Woodley", "role": "Sophia Hammond"},
            {"name": "Ben Foster", "role": "Reynolds"},
            {"name": "Pablo Schreiber", "role": "Savick"},
            {"name": "Ben McKenzie", "role": "Kent"},
            {"name": "Lionel Boyce", "role": "Youngblood"},
            {"name": "Amar Chadha-Patel", "role": "Singh"},
            {"name": "Rafael Cebrian", "role": "Athos"}
        ],
        "producers": [
            {"name": "Greg Silverman", "role": "Producer"},
            {"name": "Alan Ritchson", "role": "Producer"}
        ],
        "composer": {"name": "Steve Jablonsky", "role": "Composer"}
    },
    "externalScores": {
        "imdb": "N/A",
        "rottenTomatoes": "63%",
        "metacritic": "N/A"
    },
    "summary": {
        "overall": "Motor City arrives as a stripped-down revenge thriller that wears its 1970s grindhouse influences proudly. Directed by Potsy Ponciroli and starring Alan Ritchson as John Miller, a Detroit factory worker framed for a drug charge by a jealous gangster, the film dispenses with nearly all dialogue (reportedly only five spoken lines) in favor of a propulsive rock soundtrack and brutally choreographed action sequences. The result is a lean, visually striking throwback that knows exactly what it is and never pretends to be more.\n\nMiller is a man of few words and even fewer options. After being sentenced to 25 years for a crime he did not commit, he escapes prison with the help of loyal friends and embarks on a single-minded campaign of revenge against Reynolds (Ben Foster), the crime boss who framed him and stole his girlfriend Sophia (Shailene Woodley). The film unfolds across two timelines: a year before his imprisonment, showing his romance with Sophia and his betrayal, and the present-day revenge tour through Detroit's industrial decay.\n\nWhat separates Motor City from lesser revenge thrillers is its commitment to visual storytelling. Ponciroli and cinematographer John Matysiak paint Detroit as a rust-belt wasteland of abandoned factories and empty streets, a fitting backdrop for Miller's hollowed-out pursuit. The action is brutal and inventive: Miller crafts a bullet from his wedding ring, a symbol of the love he lost and the vengeance he now carries. When the ring-bullet finally finds its target decades later, the film earns its final shot.\n\nIdeologically, Motor City is refreshingly straightforward. The bad guys are bad. The hero is wronged. When the system fails (a corrupt cop, Savick, actively conspires with Reynolds), Miller does not petition for reform. He takes matters into his own hands. This is the rugged individualism at the heart of the American revenge genre, and Motor City wears it like a mechanic's jacket.\n\nThe corrupt cop subplot (Pablo Schreiber as Savick) reads as a mild institutional critique, but it is the kind of crooked-lawman trope that has existed in crime films since the 1930s. It does not reflect a contemporary DEI or progressive agenda. The film's worldview is fundamentally traditional: love is worth fighting for, loyalty to friends matters, and justice, when denied by the system, is the individual's responsibility.\n\nThe minimal dialogue conceit may frustrate viewers expecting Reacher-style banter from Ritchson. This is not that film. Motor City is closer to a silent-era revenge picture with a Steve Jablonsky score, and its box office returns ($1.7 million opening against a $30 million budget) suggest audiences were not entirely sure what to make of it. For those who appreciate a lean, mean action film with zero ideological baggage, it delivers exactly what it promises.",
        "adultInsight": "Motor City is not a subtext film. Its argument is worn on its sleeve: the state cannot always deliver justice, and when it fails, a man must deliver it himself. For anyone fatigued by revenge films that feel the need to apologize for their protagonist's violence or undermine him with moral equivocation, Motor City is a bracing corrective. The film does not ask you to feel conflicted about Miller's mission. It asks you to feel his loss, his rage, and ultimately his grim satisfaction. That clarity of purpose is its greatest strength and its only real ambition.",
        "parentalGuidance": "Rated R for strong violence including brutal hand-to-hand combat, gun violence, and disturbing imagery. Language throughout. Brief drug-related content. Not for children."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-028",
            "name": "The Rugged Individualist",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "John Miller takes justice into his own hands after the system fails him. He does not seek institutional reform or wait for the courts; he escapes prison, tracks down his enemies, and delivers retribution personally. The film presents this self-reliance as the only meaningful form of justice."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "Miller's entire quest is motivated by the desire to avenge Sophia, an innocent woman caught in Reynolds's orbit. His protective instinct extends to his friends who die helping him. The film frames this protective rage as noble, not toxic."
        },
        {
            "id": "TRADITIONAL-047",
            "name": "Justice Restored",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "Reynolds is punished for his crimes, and Miller's decades-long pursuit ends with the guilty man dead. The film delivers a complete moral accounting where the wicked are destroyed and the wronged find closure."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "The moral universe of Motor City is unambiguous. John Miller is wronged. Reynolds is evil. Savick is corrupt. There is no moral gray zone, no suggestion that Miller's rage is misplaced. The film operates within a clear moral binary."
        },
        {
            "id": "TRADITIONAL-034",
            "name": "Sanctity of Marriage",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "description": "Miller's love for Sophia is presented as sacred. He crafts a bullet from his wedding ring, a potent symbol of the bond Reynolds destroyed. The film treats romantic commitment as a covenant worth dying and killing for."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Evil (Corrupt Cop)",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 3.0,
            "description": "Detective Savick (Pablo Schreiber) is a corrupt cop in league with Reynolds. He actively persecutes Miller and participates in the frame-up. This is a standard noir/crime trope rather than a contemporary critique of policing, but it still depicts law enforcement as fundamentally compromised."
        }
    ],
    "seo": {
        "titleTag": "Is Motor City (2026) Woke? Alan Ritchson's Revenge Thriller Review | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Motor City (2026). Alan Ritchson stars in a near-silent revenge thriller set in 1977 Detroit. Trope scores, verdict: TRADITIONAL (+13.1). Parental guidance included.",
        "keywords": "is motor city woke, motor city 2026 review, motor city virtuevigil, motor city traditional or woke, alan ritchson motor city, motor city parents guide, motor city ifc films"
    }
}

# ─── REVIEW 2: The Usual Suspects (1995) ───
usual_suspects = {
    "id": "the-usual-suspects-1995",
    "slug": "the-usual-suspects-1995",
    "title": "The Usual Suspects",
    "year": 1995,
    "type": "movie",
    "platform": "Streaming",
    "genre": "Neo-Noir, Crime Thriller, Mystery",
    "date": "2026-07-29",
    "datePublished": "2026-07-29",
    "author": "VirtueVigil Editorial Team",
    "readTime": "5 min read",
    "poster": "/images/posters/the-usual-suspects-1995.jpg",
    "releaseDate": "1995-08-16",
    "rating": "R",
    "runtime": "106 minutes",
    "director": "Bryan Singer",
    "writers": ["Christopher McQuarrie"],
    "cast": [
        "Kevin Spacey",
        "Gabriel Byrne",
        "Benicio Del Toro",
        "Stephen Baldwin",
        "Kevin Pollak",
        "Chazz Palminteri",
        "Pete Postlethwaite"
    ],
    "studio": "PolyGram Filmed Entertainment / Bad Hat Harry",
    "distributor": "Gramercy Pictures",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 1.0,
    "tradScore": 4.9,
    "scoreMargin": 3.9,
    "authIndex": "55",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Not a woke trap. The film has minimal woke content (corrupt cops as standard noir trope). This 1995 film predates the identity-politics era of Hollywood. Any institutional critique is genre convention, not ideological signaling."
    },
    "spoiler_alert": True,
    "parentalGuidance": "Rated R for strong violence and language. Intense thematic material including criminal conspiracy, murder, and a deeply unsettling climax. Not suitable for children. For adults, the film is a masterclass in narrative construction with a twist ending that rewards attentive viewing.",
    "fidelityCasting": None,
    "creative_team": {
        "director": {"name": "Bryan Singer", "role": "Director"},
        "writer": {"name": "Christopher McQuarrie", "role": "Screenwriter"},
        "top_cast": [
            {"name": "Kevin Spacey", "role": "Roger 'Verbal' Kint"},
            {"name": "Gabriel Byrne", "role": "Dean Keaton"},
            {"name": "Benicio Del Toro", "role": "Fred Fenster"},
            {"name": "Chazz Palminteri", "role": "Dave Kujan"},
            {"name": "Kevin Pollak", "role": "Todd Hockney"},
            {"name": "Stephen Baldwin", "role": "Michael McManus"},
            {"name": "Pete Postlethwaite", "role": "Kobayashi"}
        ],
        "full_cast": [
            {"name": "Kevin Spacey", "role": "Roger 'Verbal' Kint"},
            {"name": "Gabriel Byrne", "role": "Dean Keaton"},
            {"name": "Benicio Del Toro", "role": "Fred Fenster"},
            {"name": "Chazz Palminteri", "role": "Dave Kujan"},
            {"name": "Kevin Pollak", "role": "Todd Hockney"},
            {"name": "Stephen Baldwin", "role": "Michael McManus"},
            {"name": "Pete Postlethwaite", "role": "Kobayashi"},
            {"name": "Suzy Amis", "role": "Edie Finneran"},
            {"name": "Giancarlo Esposito", "role": "Jack Baer"}
        ],
        "producers": [
            {"name": "Bryan Singer", "role": "Producer"},
            {"name": "Michael McDonnell", "role": "Producer"}
        ],
        "composer": {"name": "John Ottman", "role": "Composer"}
    },
    "externalScores": {
        "imdb": "8.5/10",
        "rottenTomatoes": "88%",
        "metacritic": "77"
    },
    "summary": {
        "overall": "The Usual Suspects endures nearly three decades after its release because it understands something that most twist-ending thrillers forget: the twist is not the point. The point is the story. Christopher McQuarrie's Oscar-winning screenplay constructs a nested Russian doll of criminal intrigue, where every layer you peel back reveals another deception beneath, and Bryan Singer's taut direction keeps the whole machine humming at precisely the right temperature.\n\nThe setup is iconic. Five criminals are brought together for a police lineup, and after their release, they execute a series of heists that increasingly point toward a shadowy figure: Keyser Söze, a Turkish crime lord whose myth is built on a single, horrific act of will. Kevin Spacey's Verbal Kint, a physically disabled con man with a halting delivery, recounts the entire saga to Customs Agent Dave Kujan (Chazz Palminteri) from a cluttered LAPD office. The flashbacks are vivid, detailed, and entirely a lie.\n\nViewed through the VirtueVigil lens three decades later, The Usual Suspects is a fascinating artifact of pre-woke Hollywood. It contains elements that a 2026 production would inevitably politicize, but in 1995, they are simply genre machinery. The corrupt NYPD detectives who force the lineup are not a commentary on systemic racism in policing; they are a plot device lifted from a century of crime fiction. The all-male ensemble is not a statement about excluding women; it is the natural composition of a story about a criminal fraternity. The film's amorality is aesthetic rather than ideological: it does not argue that crime is good, only that the best criminals are great storytellers.\n\nWhat makes the film tilt traditional rather than neutral is its structural commitment to the rule of law. Agent Kujan is not portrayed as a fool or a villain. He is a sharp, driven investigator who comes heartbreakingly close to the truth. The film frames his pursuit of justice as noble even as it shows him being outmaneuvered. The reveal that Verbal is Keyser Söze is not a victory lap for evil; it is a horror-movie sting designed to make you gasp, then recoil. The film wants you to be awed by Söze's brilliance and terrified by what it means.\n\nIn a 2026 context, The Usual Suspects is best appreciated as what it was: a crackerjack crime thriller from an era when movies did not need to signal their politics in every frame. It has aged remarkably well, its central performances (Spacey, Byrne, Del Toro's incomprehensible Fenster) still magnetic, its structure still studied in screenwriting courses. The question of whether you can separate the art from the artist (Spacey, Singer) is one each viewer must answer individually.",
        "adultInsight": "The Usual Suspects is a film about the power of narrative. Verbal Kint does not defeat Kujan with a gun or a knife. He defeats him with a story so compelling that Kujan abandons every investigatory instinct to believe it. In this sense, the film was eerily prescient about the information age, where the most dangerous people are not those with the most firepower but those with the most persuasive fiction. That Söze escapes, that evil wins, is not a celebration but a warning: the greatest trick the devil ever pulled was convincing the world he didn't exist. The film leaves you with the unsettling knowledge that you, like Kujan, would have been fooled too.",
        "parentalGuidance": "Rated R for strong violence and language. Intense thematic material including criminal conspiracy, murder, and a deeply unsettling climax. Not for children."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-035",
            "name": "The Just Lawman",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "Customs Agent Dave Kujan is a dedicated, intelligent investigator who pursues the truth relentlessly. His commitment to justice is presented as admirable, not naive. Even when he is outwitted, the film frames his effort as noble rather than futile."
        },
        {
            "id": "TRADITIONAL-028",
            "name": "The Rugged Individualist",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "The criminal underworld depicted in the film operates entirely on individual skill, nerve, and reputation. Keyser Söze built his legend through a single act of ruthless will, and every character rises or falls based on their own competence, not institutional support or identity-based advantage."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "The film maintains a clear distinction between law enforcement and criminality. Keyser Söze is not glamorized as an antihero; he is a monster. The film's twist ending is framed as a horror reveal, not a celebration."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Evil (Police Corruption)",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.0,
            "description": "The NYPD detectives who run the lineup are corrupt, arresting the five criminals on thin pretexts. Several dozen officers are later implicated in broader corruption revealed through press leaks. This is standard noir convention rather than political commentary, but it depicts law enforcement as compromised."
        }
    ],
    "seo": {
        "titleTag": "Is The Usual Suspects (1995) Woke? Classic Neo-Noir Review | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of The Usual Suspects (1995). Bryan Singer's twist-ending masterpiece starring Kevin Spacey. Trope scores, verdict: TRADITIONAL LEAN (+3.9). Parental guidance included.",
        "keywords": "is the usual suspects woke, the usual suspects 1995 review, usual suspects virtuevigil, usual suspects traditional or woke, bryan singer usual suspects, keyser soze movie, usual suspects parents guide"
    }
}

# ─── REVIEW 3: Furious S1 (2026) ───
furious = {
    "id": "furious-s1-2026",
    "slug": "furious-s1-2026",
    "title": "Furious",
    "year": 2026,
    "type": "series",
    "platform": "Hulu",
    "genre": "Crime Drama, Thriller",
    "date": "2026-07-29",
    "datePublished": "2026-07-29",
    "author": "VirtueVigil Editorial Team",
    "readTime": "5 min read",
    "poster": "/images/posters/furious-s1-2026.jpg",
    "releaseDate": "2026-07-27",
    "rating": "TV-MA",
    "runtime": "8 episodes, ~50-54 min each",
    "director": None,
    "writers": ["Elizabeth Meriwether"],
    "showrunners": ["Elizabeth Meriwether"],
    "cast": [
        "Emmy Rossum",
        "Lola Petticrew",
        "Scoot McNairy",
        "Quincy Tyler Bernstine",
        "Jake Lacy"
    ],
    "studio": "Searchlight Television / 20th Television",
    "distributor": "Hulu",
    "verdict": "WOKE",
    "wokeScore": 17.76,
    "tradScore": 7.98,
    "scoreMargin": -9.78,
    "authIndex": "42",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Not a woke trap. The woke content is visible from the premise: a female serial killer targeting wealthy men, framed as a comprehensible response to systemic failure. No hidden ideological payload."
    },
    "spoiler_alert": False,
    "parentalGuidance": "TV-MA for strong violence, sexual content, drug references, and intense psychological themes including abuse and trauma. Not suitable for children. For adults, the series is a well-crafted thriller that rewards attentive viewing but arrives with a clear ideological framework that parents should be aware of.",
    "fidelityCasting": None,
    "creative_team": {
        "showrunners": [
            {"name": "Elizabeth Meriwether", "role": "Creator / Showrunner"}
        ],
        "writers": [
            {"name": "Elizabeth Meriwether", "role": "Writer / Creator"}
        ],
        "lead_producer": {
            "name": "Elizabeth Meriwether",
            "role": "Executive Producer"
        },
        "top_cast": [
            {"name": "Emmy Rossum", "role": "Alice Black"},
            {"name": "Lola Petticrew", "role": "Catherine"},
            {"name": "Scoot McNairy", "role": "Danny Kelly"},
            {"name": "Quincy Tyler Bernstine", "role": "Nora Washington"},
            {"name": "Jake Lacy", "role": "Marshall"}
        ],
        "full_cast": [
            {"name": "Emmy Rossum", "role": "Alice Black"},
            {"name": "Lola Petticrew", "role": "Catherine"},
            {"name": "Scoot McNairy", "role": "Danny Kelly"},
            {"name": "Quincy Tyler Bernstine", "role": "Nora Washington"},
            {"name": "Jake Lacy", "role": "Marshall"}
        ],
        "producers": [
            {"name": "Elizabeth Meriwether", "role": "Executive Producer"},
            {"name": "Emmy Rossum", "role": "Executive Producer"},
            {"name": "Ronald Bass", "role": "Executive Producer"}
        ],
        "composer": {"name": "Ariel Marx", "role": "Composer"}
    },
    "externalScores": {
        "imdb": "N/A",
        "rottenTomatoes": "100%",
        "metacritic": "N/A"
    },
    "summary": {
        "overall": "Elizabeth Meriwether's Furious arrives on Hulu with a 100% Rotten Tomatoes score and a premise that reads like an algorithm trained on the post-MeToo, post-Epstein zeitgeist. Emmy Rossum stars as FBI agent Alice Black, a former NYPD homicide detective hunting a female serial killer named Catherine (Lola Petticrew) who murders wealthy men using lethal doses of fentanyl. Loosely inspired by the 1987 film Black Widow, the series stretches a two-hour movie concept into eight hours of prestige crime drama, and the results are what you would expect: technically accomplished, well-acted, and ideologically pre-chewed.\n\nThe series follows two parallel tracks. Alice is a probationary FBI agent recovering from an abusive relationship with her former NYPD partner Marshall (Jake Lacy), who still circulates in her professional orbit. Catherine is a survivor of sexual exploitation who now targets wealthy predators, dispensing a kind of vigilante justice the legal system never provided. As their paths converge, the series asks how much sympathy a serial killer deserves when society failed her first.\n\nPerformances are strong across the board. Rossum brings coiled intensity to Alice, a woman whose professional competence masks personal damage. Petticrew plays Catherine with unnerving stillness, a predator shaped by predation. Quincy Tyler Bernstine provides grounding as the head of the FBI's sex crimes unit, and Lacy is effectively loathsome as the abusive ex who weaponizes institutional connections.\n\nWhere Furious stumbles is in its ideological homework. The series is built on a foundation of contemporary progressive assumptions: wealthy men are predatory by nature, institutions designed to protect women are complicit in their abuse, and violence against men who exploit women is, if not justified, at least comprehensible. The series walks this line with some sophistication, never quite endorsing Catherine's killings but consistently framing them as a rational response to systemic failure. Critics have praised the show's \"complexity,\" and it is complex in the way a well-argued op-ed is complex. The conclusion is never seriously in doubt.\n\nThe Corbyn-era influences are clear. This is the Epstein moment processed through the prestige-crime-drama filter, and it will appeal to audiences who want their entertainment to validate their worldview. For viewers seeking a crime thriller that does not double as a position paper on gender and power, Furious will feel like being cornered at a dinner party by someone who just discovered intersectionality.\n\nThat said, Furious is not a bad show. It is a well-made show with a clear point of view that happens to align with the dominant ideology of its production ecosystem. The question is whether you want eight hours of that ecosystem's preferred narrative or whether you would rather spend your time on a series that trusts you to draw your own conclusions.",
        "adultInsight": "Furious is fascinating as a case study in how prestige television processes cultural moments. The Epstein scandal was a genuine atrocity that exposed real institutional failure. Furious channels that outrage into the familiar structure of the serial-killer thriller, with a crucial inversion: the killer is the victim, and the victims are the predators. This is not inherently invalid as a dramatic premise, but it reveals the limits of an entertainment industry that can only tell one kind of story about gender and power: the one where men are monsters and women, even murderous ones, are their victims. The series is at its best when it complicates this frame rather than merely illustrating it.",
        "parentalGuidance": "TV-MA for strong violence, sexual content including references to sexual exploitation, drug references (fentanyl), and intense psychological themes including abuse and trauma. Not for children."
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
            "description": "Both Catherine (the calculating serial killer) and Alice (the driven FBI agent) are women operating with ruthless competence in male-dominated spaces. Catherine in particular embodies the Girl Boss archetype taken to homicidal extremes, dispensing her own justice against wealthy men. The series frames her lethal skill set as a dark but comprehensible response to systemic victimization."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Evil (Systemic Complicity)",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 3.0,
            "description": "The FBI, NYPD, and broader legal system are depicted as institutions that systematically fail to protect women from sexual exploitation and abuse. The series argues that this failure is not incidental but structural, making Catherine's vigilante justice a comprehensible, if not endorsed, response."
        },
        {
            "id": "WOKE-011",
            "name": "The Toxic Masculinity Critique",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": 4.2,
            "description": "The wealthy men Catherine kills are uniformly portrayed as predatory exploiters whose wealth and status shield them from consequences. Alice's ex-boyfriend Marshall is an abusive NYPD detective who leverages institutional connections to maintain control. The series presents male predation as pervasive and male power as inherently corrupting."
        },
        {
            "id": "WOKE-019",
            "name": "The Redeemed Criminal (Systemic)",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 3.0,
            "description": "Catherine's serial killings are framed as a response to systemic failure. The series asks viewers to understand her violence as a comprehensible reaction to a society that ignores the exploitation of girls and young women. While the show does not fully endorse her actions, it consistently invites sympathy for her rather than her victims."
        },
        {
            "id": "TRADITIONAL-035",
            "name": "The Just Lawman",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "Alice Black is a dedicated FBI agent who genuinely wants to stop the killings and protect potential victims. Her commitment to law enforcement, despite her personal trauma from an abusive cop ex-boyfriend, is presented as admirable. Her pursuit of justice through institutional channels provides a counterweight to Catherine's extrajudicial approach."
        },
        {
            "id": "TRADITIONAL-047",
            "name": "Justice Restored",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "description": "The series maintains a tension between Catherine's vigilante justice and Alice's institutional pursuit. The FBI investigation represents the legitimate path to justice, and Alice's work embodies the principle that the guilty should be held accountable through due process, not fentanyl."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "description": "Alice's motivation includes protecting potential future victims. Her work in the FBI sex crimes unit reflects a genuine desire to shield the vulnerable from exploitation, exercising protective strength through institutional channels."
        },
        {
            "id": "TRADITIONAL-027",
            "name": "The Redemptive Arcs (Personal)",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "description": "Alice's backstory involves recovery from an abusive relationship. Her arc in the series includes processing this trauma and reclaiming her agency through legitimate law enforcement work rather than destructive rage, offering a redemptive counterpoint to Catherine's path of vengeance."
        }
    ],
    "seo": {
        "titleTag": "Is Furious (2026) Woke? Hulu's Emmy Rossum Thriller Review | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Furious S1 (2026). Emmy Rossum stars as an FBI agent hunting a female serial killer in Elizabeth Meriwether's post-Epstein thriller. Trope scores, verdict: WOKE (-9.8). Parental guidance included.",
        "keywords": "is furious woke, furious 2026 review, furious hulu review, furious virtuevigil, furious traditional or woke, emmy rossum furious, elizabeth meriwether furious, furious parents guide, furious tv series"
    }
}

# Append all three
reviews = load()
print(f"Loaded {len(reviews)} reviews")
reviews.append(motor_city)
print(f"Added Motor City -> {len(reviews)} reviews")
reviews.append(usual_suspects)
print(f"Added The Usual Suspects -> {len(reviews)} reviews")
reviews.append(furious)
print(f"Added Furious -> {len(reviews)} reviews")
save(reviews)
print("Saved reviews.json")