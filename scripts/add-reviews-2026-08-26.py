#!/usr/bin/env python3
"""Add 3 reviews: Reading Lolita in Tehran (2026), Return of the Jedi (1983), Baby Reindeer (2024).
Scores are exact: wokeScore/tradScore = sum of respective trope weightedScores.
Margin = tradScore - wokeScore drives verdict via locked threshold table."""
import json, sys

reviews_file = "src/data/reviews.json"
with open(reviews_file) as f:
    data = json.load(f)

existing = {r["slug"] for r in data}

reviews = []

# ============================================================
# REVIEW 1: Reading Lolita in Tehran (2026)  -> MIXED
# woke 15.96, trad 17.96, margin +2 TRAD
# ============================================================
r1 = {
    "id": "reading-lolita-in-tehran-2026",
    "slug": "reading-lolita-in-tehran-2026",
    "title": "Reading Lolita in Tehran (2026)",
    "year": 2026,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Drama, Historical, Biography",
    "date": "2026-08-26",
    "datePublished": "2026-08-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "11 min",
    "poster": "/images/posters/reading-lolita-in-tehran-2026.jpg",
    "releaseDate": "2026-08-21",
    "rating": "PG-13",
    "runtime": "128 min",
    "director": "Eran Riklis",
    "writers": "Marjorie David, based on the memoir by Azar Nafisi",
    "cast": [
        "Golshifteh Farahani",
        "Zar Amir Ebrahimi",
        "Mina Kavani",
        "Shohreh Aghdashloo",
        "Navid Negahban",
        "Ali Mosaffa",
        "Behnaz Jafari"
    ],
    "studio": "Maven Pictures, A+E Studios",
    "distributor": "Sony Pictures Classics",
    "verdict": "MIXED",
    "wokeScore": 15.96,
    "tradScore": 17.96,
    "authIndex": "High",
    "scoreMargin": "+2 TRAD",
    "preRelease": None,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Reading Lolita in Tehran is ideologically transparent from its opening frames. The film never hides its thesis: Western literature is liberating, and theocratic authoritarianism is oppressive. The audience knows exactly what they are getting from the first scene, which shows Nafisi refusing the mandatory veil, through the final meeting of the book club. There is no bait-and-switch, no hidden agenda unveiled after the midpoint. The film's critique of the Iranian regime is explicit throughout, not a late-inning reveal."
    },
    "summary": {
        "overall": "Reading Lolita in Tehran is a film that could only exist in the space between two ideological worlds, and it is better for that tension. Adapted from Azar Nafisi's 2003 memoir, it follows a university literature professor in Tehran during and after the Islamic Revolution who refuses the mandatory veil, is expelled from her teaching position, and forms a secret book club for seven of her female students. The books they read, Lolita, The Great Gatsby, Pride and Prejudice, are banned by the regime but become lifelines for women living under a system that treats them as property. The film is at its best when it lets the literature speak: the scenes of Nafisi and her students arguing about Nabokov and Fitzgerald in a Tehran living room, knowing the secret police could arrive at any moment, carry an electric tension. Golshifteh Farahani gives Nafisi a fierce dignity that never tips into sanctimony. The weakness is in the adaptation's framing: the memoir's nuanced portrait of pre-revolution Iran, which included passages critical of Western intervention, is compressed into a more straightforward oppression narrative. The regime is entirely villainous, which is historically defensible, and the West is entirely liberating, which is more debatable. The result is a film that lands in a genuinely mixed ideological space: it affirms traditional values of intellectual freedom, personal courage, and the primacy of classic literature while simultaneously adopting the idiom of secular liberal feminism. Parents should know this is not a children's film, though its PG-13 rating is earned through thematic weight rather than objectionable content.",
        "oneLiner": "An Iranian literature professor refuses the mandatory veil and forms a secret book club for seven female students, using banned Western classics to resist theocratic oppression.",
        "adultInsight": "The most interesting thing about Reading Lolita in Tehran is that it cannot be reduced to either side of the American culture war. The regime Nafisi defies is a theocratic authoritarian state that mandates religious observance, and she resists it by teaching secular Western novels. A traditionalist viewer will cheer the depiction of Islamic theocracy as oppressive and will recognize the value of teaching classic literature as an act of moral formation. But that same viewer will notice that the regime Nafisi opposes shares certain vocabulary with conservatism: submission to authority, obedience, modest dress, the primacy of the collective over the individual. The film never wrestles with this tension, and it should. The best scene is a quiet one: Nafisi holding her copy of Pride and Prejudice, explaining to her students that Austen understood, two hundred years ago and six thousand miles away, what it means to be a woman whose value is determined by men who do not know her. That is not woke, it is not traditional, it is simply true, and the film is strongest when it operates in that space beyond ideology.",
        "parentalGuidance": "Rated PG-13 for thematic material involving political oppression, some disturbing images of public punishment, and brief references to sexual content in literary discussion. No nudity, no graphic violence. The film depicts the emotional and psychological toll of living under a theocracy, including scenes of public shaming and discussion of executions. Parents should be prepared to discuss the historical context of the Iranian Revolution and the role of literature in resisting authoritarianism. Suitable for mature 13 and up."
    },
    "tropeAudit": [
        {
            "id": "WOKE-003",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Nafisi is the archetypal defiant woman defying patriarchal authority. She refuses the veil, talks back to regime officials, and leads her students in intellectual rebellion. Severity 3: Nafisi's defiance is the film's narrative engine. Authenticity High (0.7): this is an autobiographical account; Nafisi actually did these things. Centrality High (1.8): the entire film is structured around her resistance."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Evil",
            "category": "Woke",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "The Islamic Republic of Iran is presented as an irredeemably corrupt, cruel institution that degrades women and crushes intellectual freedom. Every interaction with the state is dehumanizing. Severity 5: the regime is the film's antagonist and the oppression it inflicts is the entire reason the story exists. Authenticity High (0.7): the regime's documented human rights abuses are historically real. Centrality High (1.8): the regime is the central antagonistic force."
        },
        {
            "id": "WOKE-015",
            "name": "Oppressive Domesticity",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "The regime's enforcement of traditional female domestic roles, covering, obedience to male guardians, is portrayed as a prison from which the female students must escape through literature. Severity 2: this is a recurring theme but not the sole focus. Authenticity High (0.7): the regime's restrictions on women are historically documented. Centrality Moderate (1.0): one of several intersecting oppressions."
        },
        {
            "id": "WOKE-012",
            "name": "The Smug Secularist",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Nafisi's intellectual authority is linked to her embrace of secular Western literature. Religious adherence is consistently depicted as the enemy of intellectual freedom. The regime's faith is presented as a tool of control rather than genuine belief. Severity 3: the secular-versus-religious framing is a major thematic spine. Authenticity High (0.7): consistent with the memoir's secular perspective, not injected by the adaptation. Centrality High (1.8): the clash between religious authority and secular literary culture structures the entire narrative."
        },
        {
            "id": "WOKE-016",
            "name": "Infallible Youth",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "The seven female students represent a generation awakening to their oppression through literature. Their intellectual journey is presented as purer and truer than the compromised accommodations of older characters. Severity 2: the student awakening is important but not the sole focus. Authenticity High (0.7): the memoir documents actual students; this is organic. Centrality Low (0.5): one element among many."
        },
        {
            "id": "TRADITIONAL-046",
            "name": "Heritage over Innovation",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The film's thesis is that classic literature, the accumulated wisdom of centuries, is the antidote to ideological tyranny. Nabokov, Fitzgerald, Austen, and James are presented not as outdated relics but as sources of timeless truth about the human condition. Severity 4: the primacy of literary heritage is the film's central argument. Authenticity High (0.7): faithful to Nafisi's memoir. Centrality High (1.8): the book club's reading of classics is the dramatic and thematic core."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The film presents a clear moral binary: the regime is evil, the women seeking freedom are good, and literature is a force for moral clarity. There are no morally ambiguous regime officials, no students who genuinely believe in the revolution. The moral poles are distinct and unapologetic. Severity 4: the good-versus-evil framing is a dominant structural element. Authenticity High (0.7): Nafisi's lived experience supports this framing. Centrality High (1.8): the moral clarity is the film's emotional engine."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Nafisi's motivation throughout is the protection of her students from a system that would devour them. She risks her safety to give them intellectual sanctuary. Her book club is, at its core, an act of maternal protection. Severity 3: this protective impulse drives many of Nafisi's key decisions. Authenticity High (0.7): organic to the memoir. Centrality High (1.8): the book club is the film's central action."
        },
        {
            "id": "TRADITIONAL-043",
            "name": "Faith in Adversity",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "explanation": "Though Nafisi's faith is in literature rather than religion, the film depicts the act of finding transcendent meaning under oppression as a source of strength. The students' commitment to their reading group, despite genuine danger, models a kind of secular faith. Severity 2: a recurring motif. Authenticity Moderate (1.0): the secular framing is true to the source but not obviously traditional. Centrality Moderate (1.0): important to the atmosphere but not the primary plot driver."
        },
        {
            "id": "TRADITIONAL-033",
            "name": "The Wise Elder",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Nafisi functions as the wise elder who connects her students to the literary heritage of the West, passing down knowledge that the regime would erase. Her authority derives from her learning and her willingness to transmit it, not from her position in a hierarchy. Severity 3: her role as mentor is central to the story. Authenticity High (0.7): organic to the memoir's teacher-student structure. Centrality Moderate (1.0): the mentorship frames but does not drive the plot."
        }
    ],
    "seo": {
        "titleTag": "Is Reading Lolita in Tehran (2026) Woke? Full VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Reading Lolita in Tehran (2026), the film adaptation of Azar Nafisi's memoir about a secret book club under theocratic rule. Verdict: MIXED (+2 TRAD). Trope scores, parental guidance included.",
        "keywords": "is reading lolita in tehran woke, reading lolita in tehran 2026 review, reading lolita in tehran virtuevigil, azar nafisi film review, reading lolita in tehran parents guide, golshifteh farahani movie review, eran riklis reading lolita in tehran"
    },
    "parentalGuidance": "Rated PG-13 for thematic material involving political oppression, some disturbing images of public punishment, and brief references to sexual content in literary discussion. No nudity, no graphic violence. The film depicts the emotional and psychological toll of living under a theocracy, including scenes of public shaming and discussion of executions. Suitable for mature 13 and up."
}

# ============================================================
# REVIEW 2: Return of the Jedi (1983)  -> STRONGLY TRADITIONAL
# woke 2.8, trad 25.83, margin +23 TRAD
# ============================================================
r2 = {
    "id": "return-of-the-jedi-1983",
    "slug": "return-of-the-jedi-1983",
    "title": "Return of the Jedi (1983)",
    "year": 1983,
    "type": "film",
    "platform": "Disney+",
    "genre": "Sci-Fi, Adventure, Fantasy",
    "date": "2026-08-26",
    "datePublished": "2026-08-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "10 min",
    "poster": "/images/posters/return-of-the-jedi-1983.jpg",
    "releaseDate": "1983-05-25",
    "rating": "PG",
    "runtime": "132 min",
    "director": "Richard Marquand",
    "writers": "Lawrence Kasdan, George Lucas",
    "cast": [
        "Mark Hamill",
        "Harrison Ford",
        "Carrie Fisher",
        "Billy Dee Williams",
        "Anthony Daniels",
        "David Prowse",
        "James Earl Jones",
        "Ian McDiarmid",
        "Frank Oz",
        "Alec Guinness"
    ],
    "studio": "Lucasfilm Ltd.",
    "distributor": "20th Century Fox",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 2.8,
    "tradScore": 25.83,
    "authIndex": "High",
    "scoreMargin": "+23 TRAD",
    "preRelease": None,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Return of the Jedi is ideologically transparent from its opening crawl to its closing celebration. The film wears its values openly: redemption is possible for even the most fallen soul, fathers and sons belong together, and evil is evil. Leia's active combat role was established in the first two films, not shoehorned into this one. The Ewoks defeating Imperial walkers with primitive technology is a classic underdog story, not an ideological injection. There is no hidden agenda here, just the completion of an honest myth."
    },
    "summary": {
        "overall": "Return of the Jedi completes the original Star Wars trilogy with an ending that is both emotionally satisfying and, in ways that are hard to appreciate until you have watched a lot of modern franchise cinema, ethically audacious. The film makes a bet that the first generation of Star Wars fans were capable of understanding that the climactic victory is not blowing up the Death Star, it is a father choosing to save his son at the cost of his own life. Luke Skywalker does not defeat the Emperor. He throws his lightsaber away. He refuses to fight. He trusts that the good man buried inside Darth Vader is still there, and he is right. This is a gesture of radical nonviolence that would feel at home in a sermon, and George Lucas had the nerve to put it at the center of a $32 million blockbuster aimed at children. The film's weaknesses are well documented: the Ewoks strain credibility as a military force, the Jabba's Palace sequence runs long, and the pacing of the three-act structure makes Endor feel like the C-plot for too much of the runtime. But these are quibbles against what the film achieves at its emotional peak. When Vader picks up the Emperor and throws him into the reactor shaft, it is not a moment of martial victory, it is an act of paternal love that redeems three films of villainy. No modern franchise would have the moral confidence to end its trilogy this way, and the absence of that confidence is one reason the original trilogy endures while so many successors fade.",
        "oneLiner": "Luke Skywalker confronts Darth Vader and the Emperor while the Rebel Alliance launches a final assault on a second Death Star in the conclusion to the original Star Wars trilogy.",
        "adultInsight": "The theological architecture of Return of the Jedi is more sophisticated than any film wearing a space-adventure costume has any right to be. The Emperor represents pure evil: he does not want to kill Luke, he wants to corrupt him. His victory condition is not Luke's death but Luke's embrace of hatred. He nearly wins. Luke lashes out in rage, drives Vader back, cuts off his mechanical hand, and stands over his defeated father as the Emperor applauds. In that moment Luke looks at his own mechanical hand and sees what he is about to become. The light comes from recognizing that he and his father are the same, not from defeating him. This is Christian morality in its most distilled form: the cycle of violence breaks when someone refuses to participate, and redemption is available to anyone who chooses it, even at the final hour. The film trusts children, and the adults they will become, with ideas that most modern entertainment treats as too complex or too religious for mass audiences.",
        "parentalGuidance": "Rated PG (1983, would likely be PG by modern standards). Contains sci-fi action violence including blaster fire, lightsaber combat, space battles with explosions, and the destruction of ships and a space station. The Jabba's Palace sequence includes grotesque creature designs, strangulation, and a character being dropped into a monster pit. Leia is briefly held in chains wearing a metal bikini, now iconic but worth noting for younger viewers. A major character dies by electrocution and falling down a shaft. The Ewok battle sequence shows small furry creatures being killed in combat. Suitable for ages 9 and up with guidance on the distinction between fantasy violence and real harm."
    },
    "tropeAudit": [
        {
            "id": "WOKE-003",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "Leia Organa is an active combatant who strangles Jabba the Hutt, shoots stormtroopers, and participates in the ground assault on Endor. Her combat capability was established in the first film and earned through the trilogy; this is not an ideological insertion. Severity 2: Leia's combat role is noticeable but secondary to her leadership and strategic functions. Authenticity High (0.7): consistent with her character across three films. Centrality Low (0.5): the B-plot on Endor rather than the film's thematic core."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Evil",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "The Galactic Empire is portrayed as an irredeemably evil institution, but this is classic myth-making rather than a commentary on real-world institutions. The Emperor's regime is so cartoonishly villainous, building planet-destroying weapons, that it functions as moral allegory, not political commentary. Severity 2: the Empire is evil but this is fantasy world-building. Authenticity High (0.7): organic to the genre. Centrality Low (0.5): the Empire is backdrop rather than thesis."
        },
        {
            "id": "WOKE-001",
            "name": "Primitive Triumph (Ewok Subplot)",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "The Ewoks, a technologically primitive species, defeat Imperial walkers using logs, rocks, and traps. This has been read as an anti-imperialist allegory where the colonized overcome technologically superior colonizers. Severity 2: the Ewok victory is significant but not the film's main point. Authenticity High (0.7): the underdog-victory trope predates modern anti-colonial theory by millennia; it is David and Goliath, not a political program. Centrality Moderate (1.0): the Ewok subplot occupies significant screen time."
        },
        {
            "id": "TRADITIONAL-026",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "Luke Skywalker surrenders himself to the Empire to save his friends, then refuses to fight the Emperor or kill Vader even at the cost of his own life. He explicitly states he is a Jedi like his father before him and submits to death rather than embrace the dark side. Severity 5: self-sacrifice is the film's defining moral act. Authenticity High (0.7): consistent with Luke's arc through the entire trilogy. Centrality High (1.8): the throne room confrontation is the emotional and philosophical climax of three films."
        },
        {
            "id": "TRADITIONAL-027",
            "name": "The Redemptive Arc (Personal)",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "Darth Vader's redemption is the most famous redemptive arc in cinema history. After three films as the embodiment of evil, he chooses to save his son by killing the Emperor, sacrificing his own life in the process. His last words and his appearance as a Force ghost alongside Obi-Wan and Yoda confirm that his redemption is complete and recognized by the moral order of the universe. Severity 5: Vader's redemption is the film's climactic action and its moral thesis. Authenticity High (0.7): earned through three films of careful setup. Centrality High (1.8): the entire trilogy has been building to this moment."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The moral architecture of the film is unambiguous: the Emperor is evil, Luke is good, Vader is fallen but redeemable. There is no moral relativism, no suggestion that the Rebels might be as bad as the Empire, no both-sides-ism about the conflict. Good is good, evil is evil, and courage consists in choosing good even when evil seems stronger. Severity 4: the clear moral binary structures every scene. Authenticity High (0.7): consistent with mythic storytelling traditions that predate modern equivocation. Centrality High (1.8): the moral clarity is the film's philosophical foundation."
        },
        {
            "id": "TRADITIONAL-042",
            "name": "The Forgiving Heart",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Luke forgives Vader for everything: cutting off his hand, torturing his friends, murdering his mentor, participating in genocide. The forgiveness is absolute and it is what saves the galaxy. Luke's refusal to hate his father is framed not as weakness but as the most powerful act in the film. Severity 3: forgiveness is the mechanism of Vader's redemption. Authenticity High (0.7): organic to Luke's character arc. Centrality Moderate (1.0): the forgiveness enables the redemption but is not the final act itself."
        },
        {
            "id": "TRADITIONAL-047",
            "name": "Justice Restored",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The Emperor is killed, the Death Star is destroyed, the Empire is toppled, and celebrations erupt across the galaxy. The final sequence shows the main characters reunited, the spirits of the redeemed (Anakin, Obi-Wan, Yoda) looking on in peace. Order is restored, the guilty are punished, the innocent are vindicated, and the moral arc of the trilogy closes with cosmic rightness. Severity 4: justice is the film's narrative resolution. Authenticity High (0.7): organic to the trilogy's structure. Centrality High (1.8): the entire third act is the restoration of justice."
        },
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 1.05,
            "explanation": "Anakin Skywalker's final act reclaims his role as father-protector. Though dead, his Force ghost stands alongside Obi-Wan and Yoda as a restored patriarch, his moral authority re-established through sacrifice. The ghost of Obi-Wan also functions as a spiritual father whose wisdom guides Luke to the final confrontation. Severity 3: the redeemed father figure is important but appears only in the final minutes. Authenticity High (0.7): the culmination of the trilogy's father-son arc. Centrality Low (0.5): the ghost appears briefly at the end."
        }
    ],
    "seo": {
        "titleTag": "Is Return of the Jedi (1983) Woke? Star Wars Original Trilogy Review | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Return of the Jedi (1983), the conclusion to the original Star Wars trilogy. Verdict: STRONGLY TRADITIONAL (+23 TRAD). Vader's redemption, Luke's sacrifice, and the moral clarity of Lucas's space opera scored against the VVWS system.",
        "keywords": "is return of the jedi woke, return of the jedi 1983 review, star wars episode 6 woke, return of the jedi virtuevigil, star wars traditional or woke, return of the jedi parents guide, george lucas star wars review"
    },
    "parentalGuidance": "Rated PG (1983). Contains sci-fi action violence including blaster fire, lightsaber combat, space battles with explosions, and the destruction of ships and a space station. The Jabba's Palace sequence includes grotesque creature designs and a character being dropped into a monster pit. Leia is briefly held in chains wearing a metal bikini. A major character dies by electrocution. Small creatures (Ewoks) are killed in combat. Suitable for ages 9 and up."
}

# ============================================================
# REVIEW 3: Baby Reindeer (2024)  -> WOKE LEAN
# woke 18.63, trad 10.92, margin -8 WOKE
# ============================================================
r3 = {
    "id": "baby-reindeer-2024",
    "slug": "baby-reindeer-2024",
    "title": "Baby Reindeer (2024)",
    "year": 2024,
    "type": "series",
    "platform": "Netflix",
    "genre": "Drama, Thriller, Black Comedy, Biography",
    "date": "2026-08-26",
    "datePublished": "2026-08-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "12 min",
    "poster": "/images/posters/baby-reindeer-2024.jpg",
    "releaseDate": "2024-04-11",
    "rating": "TV-MA",
    "runtime": "7 episodes, 27-45 min each",
    "director": "Weronika Tofilska, Josephine Bornebusch",
    "writers": "Richard Gadd",
    "cast": [
        "Richard Gadd",
        "Jessica Gunning",
        "Nava Mau",
        "Tom Goodman-Hill",
        "Shalom Brune-Franklin",
        "Nina Sosanya"
    ],
    "studio": "Clerkenwell Films",
    "distributor": "Netflix",
    "verdict": "WOKE LEAN",
    "wokeScore": 18.63,
    "tradScore": 10.92,
    "authIndex": "High",
    "scoreMargin": "-8 WOKE",
    "preRelease": None,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Baby Reindeer announces its thematic territory from the first episode. Donny's trauma, his confused sexuality, Martha's mental illness, and the culture of a London comedy scene that enables predation are all present from the opening scenes. The series never pretends to be a light comedy about stalking; it is explicitly about the wounds people carry and how those wounds make them wound others. The trans relationship subplot (Teri) arrives early in the season, and the graphic sexual assault flashback is the emotional center of Episode 4, not a late reveal. The show is ideologically transparent: Gadd is telling an autobiographical story about the intersection of trauma, sexuality, and self-destruction, and he never hides what kind of story it is."
    },
    "summary": {
        "overall": "Baby Reindeer is a difficult series to score and an even more difficult series to recommend, but it is also one of the most harrowingly honest pieces of television in recent memory. Richard Gadd plays Donny Dunn, a fictionalized version of himself, an aspiring comedian working a bar job in London who offers a free cup of tea to a crying customer named Martha. What follows is a stalking nightmare that gradually reveals itself to be about something much deeper: Donny's unresolved trauma from a past sexual assault, his arrested development as an artist, and his profound confusion about his own sexuality. The series is built on a paradox that Gadd dramatizes with unnerving precision: Donny is simultaneously Martha's victim and her enabler, terrified of her and drawn to the attention she gives him, repulsed by his own passivity and unable to change it. The performances are exceptional. Jessica Gunning's Martha is not a monster but a desperately ill woman whose pain is as real as Donny's. The revelation of Donny's sexual assault by a male mentor figure (played with chilling ordinariness by Tom Goodman-Hill) in Episode 4 is among the most effective depictions of grooming and abuse ever filmed. Where the series loses its footing ideologically is in its treatment of Donny's relationship with Teri, a transgender woman he meets on a dating site. This subplot is treated with kid gloves in a way nothing else in the series is; Teri is the one character who is never allowed to be messy, culpable, or fully human in the way Donny and Martha are. She functions as a symbol of Donny's sexual awakening rather than a person with her own agenda and flaws. The series is not propaganda, it is too raw and self-lacerating for that, but it carries the ideological assumptions of its milieu: that sexual fluidity is inherently liberating, that traditional masculinity is a cage, and that self-acceptance means shedding inherited moral frameworks. These are not Gadd's inventions; they are the water he swims in. The result is a show of extraordinary craft and genuine emotional power that nonetheless scores on the woke side of the ledger, not because it preaches, but because it assumes a worldview that goes uninterrogated.",
        "oneLiner": "An aspiring comedian in London offers a free cup of tea to a stranger and becomes the target of a relentless stalking campaign that forces him to confront his own buried trauma, confused sexuality, and complicity in his own destruction.",
        "adultInsight": "The most provocative thing about Baby Reindeer, and the reason it transcends its ideological assumptions, is its insistence on Donny's agency in his own victimhood. The series refuses the clean categories of the culture war. Donny was sexually assaulted, and he is a victim of that crime. He is also a man who repeatedly chooses to engage with his stalker, who lies to the police to protect her, who records her voicemails and listens to them alone. The show does not excuse Martha, she is dangerous and her actions are criminal, but it refuses to reduce Donny to a pure innocent. This is morally serious in a way that neither the woke believe-all-victims framework nor the traditional personal-responsibility framework fully captures. The problem is not that Baby Reindeer is woke; the problem is that it thinks its most ideological elements, the trans relationship, the sexual fluidity, the rejection of traditional masculinity, are simply reality rather than a particular view of reality. That assumption, shared by almost all prestige television, is what keeps the show from being truly radical. It is radical about everything except its own priors.",
        "parentalGuidance": "TV-MA. This is not a series for children or young teenagers under any circumstances. Contains graphic depictions of sexual assault (Episode 4), pervasive discussions of stalking and sexual violence, drug use, explicit sexual content including full male nudity, frank discussion of transgender identity and sexuality, and sustained psychological distress. The series depicts grooming, drug-facilitated sexual assault, and the long-term psychological consequences of abuse in detail. Even adult viewers should approach with caution. No content suitable for viewers under 18."
    },
    "tropeAudit": [
        {
            "id": "WOKE-007",
            "name": "Gender Fluidity as Awakening",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Donny's relationship with Teri, a transgender woman, is presented as a key component of his journey toward self-understanding. His embrace of his attraction to a trans woman is framed as growth, a shedding of inhibition and inherited norms. Severity 3: the sexual identity exploration is a major character arc. Authenticity High (0.7): based on Gadd's autobiographical experiences. Centrality Moderate (1.0): a significant subplot but not the central plot which is the stalking."
        },
        {
            "id": "WOKE-011",
            "name": "The Toxic Masculinity Critique",
            "category": "Woke",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The series presents Donny's inability to report his assault, his inability to reject Martha's advances, and his inability to assert himself in his comedy career as symptoms of a specifically masculine pathology. His shame about the assault is linked to his shame about his sexuality, and both are linked to his inability to perform traditional masculine stoicism. The male predator (Darrien) represents a corrupted form of masculine mentorship. Severity 4: the critique of masculine silence and shame is a dominant theme. Authenticity High (0.7): Gadd is dramatizing his own experience; this is not politically imposed. Centrality High (1.8): Donny's relationship with masculinity structures his entire character arc."
        },
        {
            "id": "WOKE-022",
            "name": "Sexual Liberation as Empowerment",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Donny's exploration of his sexuality, including casual encounters, dating a trans woman, and confronting his history of abuse, is framed as a necessary path toward self-acceptance and healing. The series does not endorse the harmful behavior but presents sexual openness as inherently therapeutic. Severity 3: sexual exploration is a significant character arc. Authenticity High (0.7): autobiographical material. Centrality Moderate (1.0): important but secondary to the stalking narrative."
        },
        {
            "id": "WOKE-018",
            "name": "Heteronormativity as Harm",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "explanation": "Donny's inability to form a stable heterosexual relationship is linked to societal expectations of what a man should be and want. His relationship with Keeley, his ex-girlfriend, fails partly because he cannot be honest about his attraction to a trans woman. The implication is that society's expectation of heterosexuality is a source of his dysfunction. Severity 2: present as subtext rather than explicit argument. Authenticity Moderate (1.0): the connection between Donny's sexuality confusion and societal norms is interpretive rather than directly autobiographical. Centrality Moderate (1.0): one of several themes."
        },
        {
            "id": "WOKE-009",
            "name": "The Victimhood Meritocracy",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "explanation": "The series operates within a framework where Donny's trauma confers a kind of narrative authority. His victimhood is the lens through which all his behavior is understood and excused. This is mitigated by the series' own willingness to show Donny as complicit in his predicament, but the framing still centers trauma as the organizing principle of identity. Severity 2: present as structural assumption rather than explicit argument. Authenticity Moderate (1.0): the show self-consciously interrogates this framing but operates within it. Centrality Moderate (1.0): the trauma-as-identity framework is everywhere but not the thesis."
        },
        {
            "id": "WOKE-005",
            "name": "Chosen Family over Bio-Kin",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "Donny's biological family is largely absent. His support structures are his ex-girlfriend Keeley, his landlord's mother, and eventually Teri. The absence of any biological family as a source of support fits the chosen-family-over-bio-kin pattern. Severity 1: background detail rather than stated argument. Authenticity High (0.7): consistent with autobiographical framing of a struggling London comedian. Centrality Low (0.5): set dressing rather than thematic focus."
        },
        {
            "id": "WOKE-001",
            "name": "Male Predator as Systemic Norm",
            "category": "Woke",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The character of Darrien O'Connor, Donny's comedy mentor who grooms, drugs, and sexually assaults him, is presented as an ordinary, respected figure in the entertainment industry whose predation is enabled by institutional indifference. The show connects Donny's inability to report to the culture that protects powerful men. Severity 4: the sexual assault is the emotional center of the series, framed through an institutional-enablement lens. Authenticity High (0.7): Gadd has stated this is autobiographical; the story of his real assault is the reason the series exists. Centrality High (1.8): the assault and its aftermath are the psychological engine of every episode."
        },
        {
            "id": "TRADITIONAL-027",
            "name": "The Redemptive Arc (Personal)",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Despite the woke framing, the series' emotional arc is deeply traditional: Donny must confront the truth about what happened to him, tell someone, and begin the long work of recovery. The final episode shows him listening to Martha's voicemails and finding not anger but understanding, a kind of forgiveness that does not excuse her actions but recognizes her as a fellow sufferer. This is a redemptive arc in secular language. Severity 4: Donny's recovery is the series' narrative destination. Authenticity High (0.7): autobiographical. Centrality High (1.8): the entire series builds toward Donny's self-confrontation."
        },
        {
            "id": "TRADITIONAL-042",
            "name": "The Forgiving Heart",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "The series' most audacious move is its treatment of Martha not as a monster but as a profoundly damaged human being. The final episode, in which Donny listens to her voicemails and weeps, is an act of compassionate understanding that borders on grace. He does not forgive her in the sense of absolving her, but he recognizes her suffering as real and her humanity as irreducible. Severity 3: this compassionate reframing is the series' emotional climax. Authenticity High (0.7): consistent with Gadd's stated intentions. Centrality High (1.8): the ending reframes the entire series."
        },
        {
            "id": "TRADITIONAL-043",
            "name": "Faith in Adversity",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "Donny's survival through the worst period of his life, his determination to perform, to connect, to tell his story, is a form of faith in the possibility of meaning. The series does not reach for religious language but depicts the human capacity to endure and find purpose after devastation. Severity 2: present as emotional undercurrent. Authenticity High (0.7): autobiographical truth. Centrality Moderate (1.0): supports rather than drives the narrative."
        },
        {
            "id": "TRADITIONAL-032",
            "name": "The Meritocratic Triumph",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "Donny's comedy career begins to succeed when he channels his suffering into his art. The series frames his final breakthrough as earning his voice through the work of confronting his trauma. This is a meritocratic framework: the art gets better when the artist gets honest. Severity 2: visible but not central. Authenticity High (0.7): Gadd's real career trajectory. Centrality Low (0.5): the comedy career is backdrop rather than primary narrative."
        }
    ],
    "seo": {
        "titleTag": "Is Baby Reindeer (2024) Woke? Netflix Series Full VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Baby Reindeer (2024), the Emmy-winning Netflix miniseries about stalking, trauma, and identity. Verdict: WOKE LEAN (-8 WOKE). Trope scores, parental guidance, and adult insight included.",
        "keywords": "is baby reindeer woke, baby reindeer 2024 review, baby reindeer netflix virtuevigil, richard gadd baby reindeer review, baby reindeer parents guide, baby reindeer traditional or woke, baby reindeer trauma analysis"
    },
    "parentalGuidance": "TV-MA. Contains graphic depictions of sexual assault (Episode 4), pervasive discussions of stalking and sexual violence, drug use, explicit sexual content including full male nudity, and sustained psychological distress. Not suitable for viewers under 18."
}

for r in [r1, r2, r3]:
    if r["slug"] in existing:
        print(f"ERROR: slug {r['slug']} already exists")
        sys.exit(1)

data.extend([r1, r2, r3])

with open(reviews_file, "w") as f:
    json.dump(data, f, indent=2)

# Validation: woke/trad must equal trope sums; margin must match verdict
def verdict_for(margin):
    if margin >= 20: return "STRONGLY TRADITIONAL"
    if margin >= 10: return "TRADITIONAL"
    if margin >= 3: return "TRADITIONAL LEAN"
    if margin >= -2: return "MIXED"
    if margin >= -9: return "WOKE LEAN"
    if margin >= -19: return "WOKE"
    return "STRONGLY WOKE"

for r in [r1, r2, r3]:
    woke_sum = round(sum(t["weightedScore"] for t in r["tropeAudit"] if t["category"] == "Woke"), 2)
    trad_sum = round(sum(t["weightedScore"] for t in r["tropeAudit"] if t["category"] == "Traditional"), 2)
    margin = round(trad_sum - woke_sum, 2)
    v = verdict_for(margin)
    ok_woke = abs(woke_sum - r["wokeScore"]) < 0.01
    ok_trad = abs(trad_sum - r["tradScore"]) < 0.01
    ok_verdict = (v == r["verdict"])
    print(f"{r['slug']}:")
    print(f"  woke_sum={woke_sum} (field={r['wokeScore']}) ok={ok_woke}")
    print(f"  trad_sum={trad_sum} (field={r['tradScore']}) ok={ok_trad}")
    print(f"  margin={margin} verdict={v} (field={r['verdict']}) ok={ok_verdict}")
    print(f"  seo={bool(r.get('seo'))} titleTag={bool(r.get('seo',{}).get('titleTag'))}")

print(f"\nTotal reviews after: {len(data)}")
print("Done appending 3 reviews.")