#!/usr/bin/env python3
"""Append 3 reviews for 2026-08-09: First Blood, John Wick Chapter 2, Mission Impossible Fallout"""
import json, subprocess, sys, os

REVIEWS_FILE = "src/data/reviews.json"

with open(REVIEWS_FILE) as f:
    all_reviews = json.load(f)

existing_slugs = {r["slug"] for r in all_reviews}

NEW_SLUGS = ["first-blood-1982", "john-wick-chapter-2-2017", "mission-impossible-fallout-2018"]
for s in NEW_SLUGS:
    if s in existing_slugs:
        print(f"ERROR: slug '{s}' already exists!")
        sys.exit(1)
print("All slugs clear. Building reviews...")

# ============================================================
# REVIEW 1: First Blood (1982)
# ============================================================
review1 = {
    "id": "first-blood-1982",
    "slug": "first-blood-1982",
    "title": "First Blood",
    "year": 1982,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Action, Thriller, Drama",
    "date": "2026-08-09",
    "datePublished": "2026-08-09",
    "author": "Debra Ducane",
    "readTime": "9 min",
    "poster": "/images/posters/first-blood-1982.jpg",
    "releaseDate": "1982-10-22",
    "rating": "R",
    "runtime": "93 min",
    "director": "Ted Kotcheff",
    "writers": ["Michael Kozoll", "William Sackheim", "Sylvester Stallone"],
    "cast": [
        "Sylvester Stallone",
        "Richard Crenna",
        "Brian Dennehy",
        "Bill McKinney",
        "Jack Starrett",
        "Michael Talbot",
        "Chris Mulkey"
    ],
    "studio": "Anabasis N.V.",
    "distributor": "Orion Pictures",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 8.54,
    "tradScore": 16.44,
    "authIndex": 65,
    "scoreMargin": "+8 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "First Blood is not a woke trap. The film's antiwar and anti-institutional subtext is present from the opening scene: Rambo arrives looking for a dead friend, killed by Agent Orange, and the film's critique of how Vietnam veterans were treated is the entire engine. There is no bait-and-switch. Conservative audiences know what they are getting within the first ten minutes, even if they choose to weigh the traditional elements more heavily than the progressive ones."
    },
    "externalScores": {
        "imdb": "7.7/10",
        "rottenTomatoes": "87%",
        "metacritic": "61/100",
        "boxOffice": "$125.2M worldwide on a $14.5M budget"
    },
    "seoTitle": "Is First Blood (1982) Woke? Sylvester Stallone's Rambo Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil's full VVWS review of First Blood (1982). The original Rambo film scored TRADITIONAL LEAN (+8). Military brotherhood, masculine competence, and a complicated Vietnam critique analyzed. Full trope audit included.",
    "seoKeywords": "is first blood woke, first blood 1982 review, rambo traditional or woke, first blood conservative review, sylvester stallone rambo 1982, virtuevigil first blood, first blood VVWS score, rambo vietnam movie review, is rambo woke, first blood patriotic",
    "creative_team": {
        "director": {
            "name": "Ted Kotcheff",
            "role": "Director",
            "note": "Canadian director known for Weekend at Bernie's and Uncommon Valor. Non-ideological craftsman. First Blood is his career-defining work."
        },
        "writer": {
            "name": "Michael Kozoll, William Sackheim, Sylvester Stallone",
            "role": "Screenwriters",
            "note": "Based on the 1972 novel by David Morrell. Stallone rewrote the script substantially, softening the original's darker ending where Rambo is killed."
        },
        "lead_producer": {
            "name": "Buzz Feitshans",
            "role": "Producer"
        },
        "composer": {
            "name": "Brian May",
            "role": "Composer",
            "note": "Australian composer (not the Queen guitarist). Score is lean and effective, heavy on tension rather than patriotic swells."
        },
        "top_cast": [
            {"name": "Sylvester Stallone", "role": "John J. Rambo"},
            {"name": "Richard Crenna", "role": "Colonel Sam Trautman"},
            {"name": "Brian Dennehy", "role": "Sheriff Will Teasle"},
            {"name": "Bill McKinney", "role": "Deputy Sergeant Galt"},
            {"name": "Jack Starrett", "role": "Deputy Lester"},
            {"name": "David Caruso", "role": "Mitch (early role)"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "R",
        "mpaaDescriptors": "Violence",
        "recommendedAge": "15+",
        "contentWarnings": [
            "Combat violence: Rambo fights deputies with martial arts, improvised weapons, and survival tactics",
            "A deputy falls from a helicopter and dies on impact",
            "Rambo sutures his own arm in a graphic close-up scene",
            "Rambo sets traps in the forest, one of which severely injures a deputy",
            "The final scene involves an extended emotional breakdown including graphic descriptions of combat deaths",
            "Moderate profanity throughout",
            "Brief flashback imagery suggesting torture during POW captivity",
            "No sexual content",
            "The film treats PTSD and combat trauma as real and debilitating"
        ],
        "guidance": "Rated R for violence that is sustained but not gratuitous by 1982 or current standards. The most difficult scene for younger viewers may be the emotional breakdown at the end, which involves Stallone describing the deaths of fellow soldiers in graphic terms. The film is not appropriate for young children. For teenagers and adults, it is a serious drama about the costs of war and the failures of institutions, which makes it suitable for discussion rather than pure entertainment."
    },
    "summary": {
        "overall": "First Blood is not what the franchise became. The sequels are muscular fantasies about a one-man army tearing through jungles with increasingly absurd firepower. This first film is quieter and stranger: a study in PTSD before the term existed in the cultural mainstream, and a portrait of a man who has been so thoroughly transformed by war that he cannot find his way back to ordinary life.\n\nJohn Rambo (Sylvester Stallone) walks into a small town in Washington state looking for the last surviving member of his Vietnam unit. The friend is dead. Cancer from Agent Orange. Rambo gets back on the road, nowhere to be and nobody waiting for him, and runs into Sheriff Will Teasle (Brian Dennehy), who decides a long-haired drifter with no address is exactly the kind of problem he does not need in his town. He takes Rambo in. During processing a deputy gets rough. Something in Rambo's mind trips, and he breaks out, vanishes into the Cascades, and begins what turns into a siege.\n\nTed Kotcheff directs this with real restraint. The early scenes in town have an almost documentary quality: Teasle is not a monster, he is a man with a job who makes a bad call and then cannot back down without losing face. The escalation from local police to National Guard to Army feels bureaucratically accurate. Nobody in a position of authority wants to admit they caused this.\n\nStallone barely speaks for the first hour. He communicates in movement: the coiled wariness of a man waiting for something bad, the sudden explosive efficiency when it comes. There is a scene where Rambo sutures his own arm with a crude needle and thread, his face steady, his hands steady, and it says more about what the Army made him than any amount of dialogue could.\n\nRichard Crenna as Colonel Trautman arrives not as cavalry but as something more complicated: the man who built the weapon, coming to dismantle it before it destroys too much. His scenes with Stallone in the final act are the film's best. Trautman does not pretend Rambo is broken or wrong. He acknowledges what was done to him. He asks him to stop because stopping is what soldiers do when ordered by someone they respect.\n\nFrom a VirtueVigil lens, the traditional elements are substantial. The male bonds carry weight, especially the grief that opens the film. Rambo traveled to find his last friend, learned he was gone, and walked back out into a world that has no place for either of them. Military competence is portrayed with complete seriousness. Rambo's skills are not played for comedy or irony. They are the real thing.\n\nThe critique of how America treated Vietnam veterans is, however, the film's real engine. That critique has progressive applications that the film cannot control. The antiwar subtext is real. The PTSD framing anticipates a decade of progressive veterans' advocacy. The government is portrayed as callous and ultimately dangerous.\n\nStill: the film's argument is conservative at its root. Rambo is not asking for a social program. He is asking to be allowed to live. He served. He paid. He is owed the basic dignity of being left alone. When the system cannot provide even that much, the failure belongs to the system.",
        "wokeAnalysis": "The antiwar dimension is the film's biggest ideological complication. First Blood emerged from the post-Vietnam cultural moment, when the main mode of processing the war in American film was grief and critique. It shares DNA with Coming Home and The Deer Hunter: it treats the war as a wound and the veterans as its primary casualties.\n\nRambo's breakdown in the final scene is explicitly critical of the government's treatment of returning soldiers. He could get a job in Vietnam, drive a tank, run things, be somebody. Back home he cannot hold a position washing dishes. That contrast is a direct indictment, not of the war itself, but of the civilian world's failure to honor or accommodate its warriors.\n\nThe PTSD framing was unusual in 1982 and has since become a standard element of both progressive veterans' advocacy and mainstream military drama. The film treats Rambo's psychological damage as a legitimate wound, caused by combat, inflicted by a government policy, deserving of recognition.\n\nThe individual vs. institution structure also runs in directions that conservatives would not always endorse. Not just Teasle is wrong: the National Guard is trigger-happy and incompetent, the Army brass want to kill Rambo to avoid a scene, and the civilian authority structure at every level fails to handle the situation with competence or care.",
        "tradAnalysis": "The traditional weight in First Blood comes from its portrait of masculine competence and military brotherhood. Rambo's skills are never mocked or undercut. When he defeats an entire county's law enforcement using nothing but training and terrain, the film means it as genuine tribute to what special operations training produces. This man is extraordinary because extraordinary things were done to him, and the film holds that with complete seriousness.\n\nThe male bonds are specific and earned. The film opens with Rambo grieving a friend, not in a showy way, but privately, in a farmhouse doorway, absorbing information he was not ready to receive. That is the traditional masculine model: grief held rather than performed, expressed through action rather than words.\n\nTrautman represents the best of military mentorship. He did not come to rescue Rambo from himself. He came because the man is his responsibility. The relationship between trainer and trained is one of the most traditional bonds in military culture: a form of fatherhood, a form of duty. Crenna plays it without sentiment and without manipulation. He tells Rambo the truth, including the hard part: that even justified grievance does not make a prolonged firefight acceptable.\n\nThe film's conservatism runs deepest in its critique of abandonment. Not of military culture, which the film treats with respect, but of the civilian institutions that failed to receive the men military culture produced. That failure is the conservative's objection to Vietnam, not the progressive's."
    },
    "tropeAudit": [
        {
            "id": "TRAD-FB-001",
            "name": "Military Brotherhood and Grief for the Fallen",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 5.04,
            "description": "The film opens with Rambo learning his last surviving unit member died of Agent Orange-related cancer. This grief is the moral engine of everything that follows. The bond between soldiers, between men who served together and survived together, is treated as sacred and defining. Rambo's unmoored existence is inseparable from the loss of that brotherhood."
        },
        {
            "id": "TRAD-FB-002",
            "name": "Masculine Competence (Special Forces Training as Real and Extraordinary)",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "The film treats Rambo's Green Beret training as genuinely extraordinary. His ability to defeat an entire county's law enforcement using terrain, improvised weapons, and trained instincts is presented with complete seriousness. The film does not play this for comedy. It is reverent about what military training produces, even when the product is a man the system no longer knows what to do with."
        },
        {
            "id": "TRAD-FB-003",
            "name": "Military Mentorship (Trautman-Rambo Bond)",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "Colonel Trautman's relationship with Rambo is the film's most explicitly traditional element. Trautman built him, trained him, and owes him something for it. He arrives not to contain a problem but to honor a responsibility. The trainer-soldier bond is presented as a form of fatherhood: you shaped a man, you carry him with you."
        },
        {
            "id": "TRAD-FB-004",
            "name": "Corrupt Local Authority Properly Checked",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 1.0,
            "centrality": 1.0,
            "weightedScore": 3.0,
            "description": "Teasle's harassment of Rambo is portrayed as clearly wrong. A law enforcement officer abusing his authority against a man who has done nothing is not a conservative endorsement of law enforcement per se but a reminder that authority requires justification. The film punishes the abuse without undermining the institution."
        },
        {
            "id": "WOKE-FB-001",
            "name": "Vietnam Veteran Abandonment Critique",
            "category": "Woke",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 5.04,
            "description": "The film's emotional argument is that America failed its Vietnam veterans. Rambo's breakdown in the final scene articulates this directly: he could function in war, he cannot function at home, and the gap is the country's failure, not his. This critique overlaps with progressive framing of the Vietnam era, even if it is also a legitimate conservative complaint about institutional abandonment."
        },
        {
            "id": "WOKE-FB-002",
            "name": "PTSD as Legitimate Wound",
            "category": "Woke",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "In 1982, treating combat trauma as a real psychological condition rather than weakness was culturally associated with progressive veterans' advocacy. The film portrays Rambo's PTSD with sympathy and specificity. The flashback triggers during processing are depicted as involuntary and disabling. This is accurate to the condition, but the sympathetic framing added progressive ideological weight in its historical context."
        },
        {
            "id": "WOKE-FB-003",
            "name": "Individual vs. Corrupt Institution",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 1.4,
            "description": "The film's authority figures, Teasle, the National Guard, the Army brass, all fail. The only trustworthy figure is Trautman, who exists outside the normal chain of command. This skepticism of institutional authority runs in directions that conservatives and progressives can both use. Here the failure is specific and earned rather than ideological."
        }
    ],
    "seo": {
        "titleTag": "Is First Blood (1982) Woke? Rambo's Origin Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of First Blood (1982) starring Sylvester Stallone as Rambo. TRADITIONAL LEAN verdict, +8 TRAD margin. Military brotherhood, masculine competence, and Vietnam critique fully scored.",
        "keywords": [
            "is first blood woke",
            "first blood 1982 review",
            "rambo traditional or woke",
            "sylvester stallone first blood",
            "virtuevigil first blood",
            "first blood VVWS",
            "rambo vietnam review",
            "first blood conservative",
            "first blood parents guide",
            "is rambo conservative"
        ]
    }
}

# ============================================================
# REVIEW 2: John Wick: Chapter 2 (2017)
# ============================================================
review2 = {
    "id": "john-wick-chapter-2-2017",
    "slug": "john-wick-chapter-2-2017",
    "title": "John Wick: Chapter 2",
    "year": 2017,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Action, Thriller",
    "date": "2026-08-09",
    "datePublished": "2026-08-09",
    "author": "Debra Ducane",
    "readTime": "10 min",
    "poster": "/images/posters/john-wick-chapter-2-2017.jpg",
    "releaseDate": "2017-02-10",
    "rating": "R",
    "runtime": "122 min",
    "director": "Chad Stahelski",
    "writers": ["Derek Kolstad"],
    "cast": [
        "Keanu Reeves",
        "Riccardo Scamarcio",
        "Common",
        "Claudia Gerini",
        "Laurence Fishburne",
        "Ian McShane",
        "Lance Reddick",
        "Ruby Rose",
        "John Leguizamo"
    ],
    "studio": "87Eleven Entertainment / Summit Entertainment",
    "distributor": "Lionsgate",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 2.1,
    "tradScore": 22.54,
    "authIndex": 74,
    "scoreMargin": "+20 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "John Wick: Chapter 2 is not a woke trap. The film's traditional content, its honor codes, oath structures, and masculine competence, is present from frame one. The woke content is minimal to the point of near-irrelevance. No bait-and-switch occurs."
    },
    "externalScores": {
        "imdb": "7.5/10",
        "rottenTomatoes": "89%",
        "metacritic": "75/100",
        "boxOffice": "$171.5M worldwide on a $40M budget"
    },
    "seoTitle": "Is John Wick Chapter 2 (2017) Woke? Honor, Code, and Keanu Reeves Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil's full VVWS review of John Wick: Chapter 2 (2017). STRONGLY TRADITIONAL verdict, +20 TRAD margin. The film's honor codes, masculine competence, and consequences for betrayal fully scored and analyzed.",
    "seoKeywords": "is john wick chapter 2 woke, john wick 2 review, john wick traditional or woke, john wick conservative, virtuevigil john wick, john wick VVWS score, keanu reeves john wick 2 review, john wick chapter 2 conservative review, john wick honor codes",
    "creative_team": {
        "director": {
            "name": "Chad Stahelski",
            "role": "Director",
            "note": "Former stuntman and Keanu Reeves' stunt double. Non-ideological craftsman whose entire artistic vision is the choreography of violence as a form of masculine expression. No political record."
        },
        "writer": {
            "name": "Derek Kolstad",
            "role": "Screenwriter",
            "note": "Creator of the John Wick world and its mythology. Also wrote Nobody (2021). His scripts consistently center masculine honor codes and consequences for betrayal."
        },
        "lead_producer": {
            "name": "Basil Iwanyk",
            "role": "Producer"
        },
        "composer": {
            "name": "Tyler Bates and Joel J. Richard",
            "role": "Composers",
            "note": "Score blends industrial percussion with orchestral swells. Supports the action without drowning it."
        },
        "top_cast": [
            {"name": "Keanu Reeves", "role": "John Wick"},
            {"name": "Riccardo Scamarcio", "role": "Santino D'Antonio"},
            {"name": "Common", "role": "Cassian"},
            {"name": "Claudia Gerini", "role": "Gianna D'Antonio"},
            {"name": "Laurence Fishburne", "role": "The Bowery King"},
            {"name": "Ian McShane", "role": "Winston"},
            {"name": "Lance Reddick", "role": "Charon"},
            {"name": "Ruby Rose", "role": "Ares"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "R",
        "mpaaDescriptors": "Strong violence throughout, some language, brief nudity",
        "recommendedAge": "17+",
        "contentWarnings": [
            "Extremely high body count throughout; John Wick kills dozens of people across the film",
            "A major character commits suicide on screen (off-camera but clearly depicted)",
            "Violence is stylized but relentless; includes point-blank gunshots, knife wounds, and hand-to-hand combat",
            "Brief female nudity in a bath scene",
            "Moderate profanity throughout",
            "The film presents no moral judgment on the protagonist's violence; killing is framed as craft",
            "No sexual content beyond the brief nudity",
            "No drug use"
        ],
        "guidance": "Rated R for sustained stylized violence. This is not realistic violence in the way that war films are realistic; it is choreography taken to an extreme. For older teenagers who enjoy action films, this is appropriate viewing. The moral amorality of the protagonist, no legal framework, no accountability, should be noted. The film does not endorse killing as a lifestyle; it presents an enclosed mythological world that operates on its own rules."
    },
    "summary": {
        "overall": "John Wick: Chapter 2 is a better film than it has any business being. The first John Wick was a stripped-down revenge story that worked on pure execution. This sequel expands the mythology while retaining the thing that made the original worth watching: an absolute commitment to the idea that honor, even honor among killers, means something.\n\nThe premise hinges on a marker, a blood oath Wick made years ago to a Roman crime lord named Santino D'Antonio (Riccardo Scamarcio). Santino calls it in. Wick is compelled to travel to Rome and assassinate Santino's sister so Santino can claim the High Table seat she holds. The premise is clean: Wick made a promise. He is a man of his word. He hates this, but he does it.\n\nWhat follows is a masterpiece of genre filmmaking. Chad Stahelski, a former stuntman, choreographs action sequences that function as argument rather than spectacle. The catacomb fight beneath Rome, the mirror sequence at the end, the pencil: each set piece is building toward a point about what John Wick is. He is not a superhero. He is a professional who has turned a terrible skill into a kind of art form, and who operates by a code that is older and more binding than any law.\n\nThe High Table and the Continental Hotel are the film's most interesting invention. This is a world with functioning honor codes, inviolable sanctuary rules, and real consequences for breaking them. Winston (Ian McShane) presides over the Continental like a judge. Charon (Lance Reddick) enforces it with perfect courtesy. The assassins who populate this world follow rules that would be alien in the real world: you do not kill on Continental grounds, you honor the marker, you respect the code. When Santino breaks the sanctuary, the system activates against him. Immediately. Without appeal.\n\nThis is the film's traditional argument made concrete: rules are worth having. Not because rules are always comfortable or fair, but because the alternative is chaos. Santino's problem is not that he is evil, it is that he thinks rules are for other people. The system responds accordingly.\n\nThe woke content is minimal to the point of irrelevance. Ruby Rose plays a mute female assassin, a piece of colorful casting that does not pretend she is a match for Wick in a straight fight. Common plays Cassian, a peer assassin, in one of the film's best sequences. Neither casting decision carries ideological freight. They are simply characters in a world full of characters.\n\nKeanu Reeves has made a career of playing men of few words and absolute competence. John Wick is his best role because the character's silence is load-bearing. There is nothing performative about Wick's grief or his professionalism. He does what he does because it is what he is.\n\nChapter 2 ends on a note of deliberate chaos: the rules have been broken so badly that the system has to reset. Winston gives Wick an hour's head start before every assassin in New York comes for him. What follows is the third film's problem. This one ends having done what sequels almost never do: made the world larger without making the story smaller.",
        "wokeAnalysis": "The woke content in John Wick: Chapter 2 is light enough to require deliberate effort to find. Ruby Rose's casting as Ares brings an LGBTQ-adjacent presence into the film, though the character's sexuality is never addressed and her function is purely adversarial. Common's Cassian is a Black character in a significant role, though again the film does not frame this as a statement. The Continental's cosmopolitan underworld simply reflects the cosmopolitan city it inhabits.\n\nThe moral amorality of the protagonist is the film's only genuine ideological complication. Wick operates without a moral framework that a traditional audience could fully endorse. He kills, as one character puts it, with a pencil. He does not spare the innocent because there are no innocents in his world, and the film does not ask him to. This is not progressive messaging; it is genre convention.\n\nThe film's treatment of institutional authority is complicated by the High Table structure. The institutions here are criminal. They function on honor rather than law. The film presents their functioning as admirable, which cuts across both conservative and progressive lines: it is not the state being endorsed, but the principle of order itself.",
        "tradAnalysis": "The traditional content in John Wick: Chapter 2 is its entire thesis. The film is about what happens when you take honor seriously in a world that has largely abandoned the concept.\n\nThe marker structure is the clearest expression of this. Santino calls in a blood debt. Wick honoring it is presented not as weakness but as integrity. He could refuse. He has the skill to survive refusal. He honors it anyway, because a man who does not keep his word is not a man worth being. The film states this without irony or quotation marks.\n\nThe Continental as ordered society is an unusual piece of world-building for mainstream action cinema. Winston presides over it like a magistrate over a small republic: with ceremony, with consequence, and with genuine authority. The rules of the Continental are not suggestions. They are the organizing principle of an entire civilization. When Santino violates sanctuary, the entire system turns against him within minutes. That is what functioning institutions look like: violations have costs.\n\nWick's professional excellence carries traditional masculine weight. The film treats his skill as a calling, not a curse. The extended action sequences are not chaos; they are choreography. Every move has a reason. Every weapon is appropriate to the situation. The film's aesthetic is of masculine competence pushed to its absolute limit, and it watches that competence with open admiration.\n\nThe consequences-for-betrayal structure is the film's most explicitly traditional element. Santino betrays Wick, violates sanctuary, and then hides behind the rules he spent the whole film breaking. The system does not protect him. John Wick shoots him in the face in the Continental, knowing exactly what that will cost, because some things are worth the cost. That is a traditional moral argument: there are acts so wrong that suffering punishment for stopping them is acceptable."
    },
    "tropeAudit": [
        {
            "id": "TRAD-JW2-001",
            "name": "Honor and Oath-Keeping (The Marker)",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "The entire plot is driven by a blood oath. Santino invokes the marker; Wick honors it at enormous personal cost. The film treats keeping your word as an absolute obligation, not a matter of convenience or negotiation. This is the film's thesis, stated through action rather than dialogue."
        },
        {
            "id": "TRAD-JW2-002",
            "name": "Masculine Competence as Artistry",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "The gun-fu choreography is treated as craft, not spectacle. The film frames Wick's skill as something earned and extraordinary, a form of masculine excellence analogous to how a master swordsman or craftsman is regarded in traditional cultures. The action sequences are extended precisely because the film wants you to appreciate what competence at this level looks like."
        },
        {
            "id": "TRAD-JW2-003",
            "name": "Society Ordered by Inviolable Rules (The Continental)",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.8,
            "description": "The Continental Hotel and the High Table represent a world built on binding rules rather than fluid negotiation. Winston enforces these rules without favoritism. The system responds to violations instantly and without appeal. This presents ordered society, even criminal ordered society, as preferable to chaos. Rules have value independent of who benefits."
        },
        {
            "id": "TRAD-JW2-004",
            "name": "Brotherhood and Professional Respect Among Warriors",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "Wick's interactions with other assassins, especially Cassian, are built on professional respect and an acknowledgment that they are both doing a job within rules both understand. The film presents this warrior brotherhood as a legitimate form of honor, even when applied to men who kill for money."
        },
        {
            "id": "TRAD-JW2-005",
            "name": "Consequences for Betrayal",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 5.04,
            "description": "Santino betrays Wick, destroys his house, and then hides behind the sanctuary rules he spent the film violating. The film does not let him get away with it. Wick executes him in the Continental, accepting the consequences, because the alternative is allowing a man who breaks all the rules to benefit from those he chooses to invoke. Betrayal has a cost in this world."
        },
        {
            "id": "WOKE-JW2-001",
            "name": "Female Character in Significant Combat Role",
            "category": "Woke",
            "severity": 1,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 0.35,
            "description": "Ruby Rose's Ares is a mute female bodyguard and assassin. Her inclusion adds diversity to the film's cast of killers. The film does not pretend she is a match for Wick in a straight fight: she operates through strategy and ambush. The casting is colorful rather than ideological."
        },
        {
            "id": "WOKE-JW2-002",
            "name": "Moral Amorality of Protagonist",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 1.4,
            "description": "Wick operates with no moral framework a traditional audience could straightforwardly endorse. He kills without reservation, at volume, and the film presents no judgment on this. This is genre convention carried to an extreme, but genre conventions carry ideological content. A world where violence is normalized as craft rather than condemned as wrong is not a fully traditional world."
        },
        {
            "id": "WOKE-JW2-003",
            "name": "Cosmopolitan International Underworld (Diverse Power Figures)",
            "category": "Woke",
            "severity": 1,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 0.35,
            "description": "The film's assassin world is populated with characters of diverse backgrounds holding positions of authority. Fishburne's Bowery King, Reddick's Charon, and the Rome-based High Table all reflect a cosmopolitan world. This is organic to the film's international setting rather than ideologically motivated."
        }
    ],
    "seo": {
        "titleTag": "Is John Wick: Chapter 2 (2017) Woke? Honor and Code Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of John Wick: Chapter 2 (2017). STRONGLY TRADITIONAL verdict, +20 TRAD margin. Honor codes, masculine competence, and consequences for betrayal fully scored.",
        "keywords": [
            "is john wick chapter 2 woke",
            "john wick 2 review conservative",
            "john wick traditional",
            "john wick chapter 2 VVWS",
            "virtuevigil john wick 2",
            "john wick honor codes review",
            "john wick keanu reeves traditional",
            "is john wick woke or traditional",
            "john wick 2017 parents guide",
            "john wick strongly traditional"
        ]
    }
}

# ============================================================
# REVIEW 3: Mission: Impossible - Fallout (2018)
# ============================================================
review3 = {
    "id": "mission-impossible-fallout-2018",
    "slug": "mission-impossible-fallout-2018",
    "title": "Mission: Impossible - Fallout",
    "year": 2018,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Action, Thriller, Spy",
    "date": "2026-08-09",
    "datePublished": "2026-08-09",
    "author": "Debra Ducane",
    "readTime": "9 min",
    "poster": "/images/posters/mission-impossible-fallout-2018.jpg",
    "releaseDate": "2018-07-27",
    "rating": "PG-13",
    "runtime": "147 min",
    "director": "Christopher McQuarrie",
    "writers": ["Christopher McQuarrie"],
    "cast": [
        "Tom Cruise",
        "Henry Cavill",
        "Ving Rhames",
        "Simon Pegg",
        "Rebecca Ferguson",
        "Sean Harris",
        "Angela Bassett",
        "Vanessa Kirby",
        "Alec Baldwin",
        "Michelle Monaghan"
    ],
    "studio": "Skydance Media / Bad Robot Productions",
    "distributor": "Paramount Pictures",
    "verdict": "TRADITIONAL",
    "wokeScore": 4.2,
    "tradScore": 17.5,
    "authIndex": 72,
    "scoreMargin": "+13 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Mission: Impossible - Fallout is not a woke trap. The film's traditional content, its loyalty themes, masculine sacrifice, and duty-over-self structure, is present and obvious from the opening scene. The woke elements are modest and organic to the franchise. No bait-and-switch occurs."
    },
    "externalScores": {
        "imdb": "7.7/10",
        "rottenTomatoes": "97%",
        "metacritic": "86/100",
        "boxOffice": "$791.1M worldwide on a $178M budget"
    },
    "seoTitle": "Is Mission: Impossible Fallout (2018) Woke? Tom Cruise Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil's full VVWS review of Mission: Impossible - Fallout (2018). TRADITIONAL verdict, +13 TRAD margin. Masculine duty, loyalty, and sacrifice fully scored. Tom Cruise at his best.",
    "seoKeywords": "is mission impossible fallout woke, mission impossible fallout review, mission impossible traditional or woke, tom cruise fallout conservative review, virtuevigil mission impossible, mission impossible VVWS score, is mission impossible conservative, mission impossible fallout parents guide",
    "creative_team": {
        "director": {
            "name": "Christopher McQuarrie",
            "role": "Director",
            "note": "Oscar-winning screenwriter (The Usual Suspects) who became Tom Cruise's primary collaborator. Non-ideological. His films are about loyalty, duty, and physical courage. No political record."
        },
        "writer": {
            "name": "Christopher McQuarrie",
            "role": "Screenwriter"
        },
        "lead_producer": {
            "name": "Tom Cruise and Christopher McQuarrie",
            "role": "Producers"
        },
        "composer": {
            "name": "Lorne Balfe",
            "role": "Composer",
            "note": "Builds on Lalo Schifrin's iconic theme while adding his own orchestral weight to the climax sequences."
        },
        "top_cast": [
            {"name": "Tom Cruise", "role": "Ethan Hunt"},
            {"name": "Henry Cavill", "role": "August Walker"},
            {"name": "Ving Rhames", "role": "Luther Stickell"},
            {"name": "Simon Pegg", "role": "Benji Dunn"},
            {"name": "Rebecca Ferguson", "role": "Ilsa Faust"},
            {"name": "Angela Bassett", "role": "Erica Sloane"},
            {"name": "Vanessa Kirby", "role": "Alanna Mitsopolis"},
            {"name": "Sean Harris", "role": "Solomon Lane"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "PG-13",
        "mpaaDescriptors": "Violence and intense sequences of action, and for brief strong language",
        "recommendedAge": "13+",
        "contentWarnings": [
            "Sustained action violence throughout including gunfights, fistfights, and vehicular chases",
            "Ethan Hunt is beaten severely in multiple scenes; injuries are shown",
            "A character suffers a broken ankle during a stunt (referenced but not graphically depicted)",
            "The film's threat involves nuclear weapons capable of killing millions",
            "Brief strong language (one F-bomb)",
            "A character is executed off-screen",
            "No sexual content",
            "No drug use"
        ],
        "guidance": "PG-13 rating is accurate. The action is intense and sustained but not graphic in the way R-rated action films are. The film's stakes, nuclear weapons, mass casualties are heavy for younger viewers but handled without exploitation. Suitable for teenagers who handle action films well. The stunts performed by Tom Cruise are genuinely dangerous and should be contextualized: this is not CGI."
    },
    "summary": {
        "overall": "Mission: Impossible - Fallout is the sixth film in the franchise, the best, and one of the few blockbusters in recent memory that treats physical danger as a genuine moral matter rather than a spectacle.\n\nThe setup is familiar: Ethan Hunt (Tom Cruise) loses three plutonium cores to a terrorist group called the Apostles during a failed extraction. The CIA assigns a handler named August Walker (Henry Cavill) to shadow Hunt's team and ensure the mission actually succeeds, by any means. The two men do not like each other, which is not surprising since Walker is the film's actual villain, a revelation the movie earns through patience rather than telegraphing.\n\nWhat makes Fallout different from the other entries is Christopher McQuarrie's insistence on consequence. Ethan Hunt gets hurt in this movie. He gets hurt badly, repeatedly, and the film refuses to cut away from the aftermath. The helicopter sequence in the third act involves Cruise doing stunts that were genuinely life-threatening during production; Cruise broke his ankle on the building jump and McQuarrie shot the rest of the film around the injury. That commitment reads on screen. The action sequences feel like they matter because the actors involved were willing to pay something for them.\n\nThe film's central argument is stated plainly and early: Ethan Hunt is the kind of man who cannot sacrifice a few for the many. Luther (Ving Rhames) is captured as leverage. Ethan refuses to let him die even when completing the mission requires it. This is not portrayed as strategic wisdom. It is portrayed as a character flaw that is also a virtue: the refusal to treat people as acceptable losses. A more utilitarian operative would have left Luther and completed the mission. Hunt is not utilitarian.\n\nThat choice costs. The plutonium cores slip further away. The body count rises. And the film insists that Hunt's choice was still right, not because the math works out, but because the math is not the point. Some loyalties are not negotiable. Some people are not acceptable losses.\n\nThe creative team around Cruise is worth noting. Rebecca Ferguson as Ilsa Faust continues her arc from Rogue Nation as the franchise's most interesting supporting character: a woman with her own agenda, her own loyalty structure, and her own extremely capable violence. Angela Bassett as CIA Director Sloane is initially positioned as an obstacle before the film gives her the grace of being correct about Walker. Both women function as characters rather than symbols, which the franchise has generally managed better than most action series.\n\nFallout is a deeply traditional film wearing action movie clothes. The values at its center, loyalty, duty, sacrifice, honor under pressure, are the same values that Westerns were built on before Hollywood decided they were embarrassing. McQuarrie presents them without apology.",
        "wokeAnalysis": "The woke content in Fallout is present but light. The CIA under Sloane is portrayed skeptically: it is bureaucratic, short-sighted, and willing to sacrifice operatives for political cover. This critique of intelligence agencies reads as skepticism of institutions rather than ideological progressivism, but the CIA-as-obstacle framing has been a staple of progressive thriller culture since the 1970s.\n\nThe film's three most significant female characters, Ilsa, Sloane, and the White Widow, all hold positions of genuine authority and competence. None of them are diversity inserts: Ilsa has been a developed character since Rogue Nation, Sloane is the CIA director, and the White Widow runs an international arms network. The casting reflects a franchise decision to populate the supporting cast with capable female figures, which carries some progressive freight even when the characters themselves are well-drawn.\n\nThe moral ambiguity of operating entirely outside legal frameworks is the franchise's original structural complication. Ethan Hunt answers to nobody in any practical sense. The IMF is officially disavowed. This creates a protagonist who functions as a rogue agent with no accountability, which sits awkwardly with any conservative endorsement of rule of law.",
        "tradAnalysis": "The traditional content in Fallout is its spine. The film is built on masculine virtue: duty, loyalty, physical courage, and the refusal to cut corners on what you owe the people who trust you.\n\nThe loyalty theme is the clearest traditional element. Ethan cannot leave Luther behind. He cannot leave Ilsa behind. He cannot leave the hostages behind. This is not presented as tactical intelligence. The film explicitly acknowledges that his loyalty is a vulnerability that enemies have learned to exploit. And then it presents that vulnerability as the thing that makes Ethan Hunt worth following. Men who treat people as acceptable losses are efficient. They are also not worth trusting.\n\nThe physical courage on display is extraordinary in a way that is genuinely difficult to find in contemporary cinema. Tom Cruise, at 55, ran on a broken ankle, flew helicopters at altitude, jumped across buildings. McQuarrie frames this not as entertainment but as a kind of devotion: to the character, to the audience, to the idea that some things are worth doing properly rather than faking. That commitment to doing hard things correctly is a traditional value.\n\nThe sacrifice theme runs through the entire third act. Ethan Hunt descends with a detonator into a Kashmiri wasteland to prevent a nuclear catastrophe. He does this alone, at the limit of his body's capacity, with no guarantee of survival. The film does not treat this as heroic posturing. It treats it as the only thing a person like Ethan Hunt could do when faced with those circumstances. Duty is not a concept he holds at arm's length. It is what he is.\n\nThe father-figure relationship between Ethan and his team carries traditional masculine weight. Luther and Benji are not employees. They are brothers in the old sense: men who have faced hard things together and cannot imagine not facing them together."
    },
    "tropeAudit": [
        {
            "id": "TRAD-MIF-001",
            "name": "Masculine Duty and Self-Sacrifice",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "Ethan Hunt's defining trait is that he will sacrifice himself before he sacrifices others. The film's entire climax is built on this: one man, alone, doing the physically impossible thing because it is the right thing. Duty is not a concept he holds at arm's length. The film treats this as the defining masculine virtue, not foolishness."
        },
        {
            "id": "TRAD-MIF-002",
            "name": "Loyalty to Teammates Above Mission Success",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "Ethan refuses to let Luther die even when the mission requires it. This is the film's central moral argument: some people are not acceptable losses. The film explicitly codes this as a character flaw and then explicitly endorses it. A man who would abandon his people to complete a mission is not the kind of man the film wants to be about."
        },
        {
            "id": "TRAD-MIF-003",
            "name": "Physical Courage Through Personal Risk",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.8,
            "description": "Tom Cruise's stunt work is not a marketing gimmick in this film; it is a moral statement. He broke his ankle on the building jump and kept shooting. McQuarrie framed the helicopter sequence to show that the danger is real. This commitment to doing hard things without faking them is a traditional value: competence, courage, and the refusal to take the easy path."
        },
        {
            "id": "TRAD-MIF-004",
            "name": "Brotherhood and Male Bond Under Pressure",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "Ethan, Luther, and Benji are brothers in the traditional sense: men whose bond has been forged under fire and who cannot imagine abandoning each other. Luther's capture is what drives the plot. Ethan's refusal to let him die is what costs the mission. That relationship is presented as sacred, not sentimental."
        },
        {
            "id": "WOKE-MIF-001",
            "name": "CIA as Antagonistic Bureaucracy",
            "category": "Woke",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "Erica Sloane and the CIA are portrayed as bureaucratic obstacles who prioritize political cover over operational effectiveness. This critique of intelligence agencies has been a staple of progressive thriller culture since the Church Committee hearings. Here it is grounded in plot rather than ideology, but the structural framing has a long progressive pedigree."
        },
        {
            "id": "WOKE-MIF-002",
            "name": "Female Characters in Significant Authority and Combat Roles",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 1.4,
            "description": "Three significant female characters hold positions of genuine power: Ilsa Faust as an elite operative, Erica Sloane as CIA director, and Alanna Mitsopolis as an international arms dealer. None are diversity inserts; all are developed characters. But the franchise decision to consistently populate these roles with women reflects a deliberate progressive casting strategy."
        },
        {
            "id": "WOKE-MIF-003",
            "name": "Moral Ambiguity of Operating Outside Legal Frameworks",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 0.7,
            "description": "Ethan Hunt is officially disavowed and operates with no legal accountability. The franchise presents this as heroic rather than problematic. A rogue agent answering to no state is a structurally libertarian protagonist, which cuts against conservative endorsement of rule of law and legitimate authority."
        }
    ],
    "seo": {
        "titleTag": "Is Mission: Impossible - Fallout (2018) Woke? Tom Cruise Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Mission: Impossible - Fallout (2018). TRADITIONAL verdict, +13 TRAD margin. Duty, loyalty, and sacrifice at the highest level. Full trope audit.",
        "keywords": [
            "is mission impossible fallout woke",
            "mission impossible fallout review",
            "tom cruise conservative traditional",
            "mission impossible VVWS score",
            "virtuevigil mission impossible",
            "mission impossible fallout parents guide",
            "is mission impossible traditional",
            "mission impossible fallout woke or not",
            "henry cavill mission impossible",
            "christopher mcquarrie traditional"
        ]
    }
}

# ============================================================
# Append and Save
# ============================================================
all_reviews.extend([review1, review2, review3])

with open(REVIEWS_FILE, "w") as f:
    json.dump(all_reviews, f, indent=2, ensure_ascii=False)

print(f"Saved {len(all_reviews)} reviews to {REVIEWS_FILE}.")

# ============================================================
# Build
# ============================================================
print("Running build.js...")
result = subprocess.run(["node", "build.js"], capture_output=True, text=True)
if result.returncode != 0:
    print("BUILD FAILED:")
    print(result.stderr)
    sys.exit(1)
print("Build complete.")

# ============================================================
# Git commit and push
# ============================================================
subprocess.run(["git", "add", "src/data/reviews.json", "dist/"], check=True)
commit_msg = "Add 3 reviews: First Blood (1982), John Wick Chapter 2 (2017), Mission Impossible Fallout (2018)"
subprocess.run(["git", "commit", "-m", commit_msg], check=True)
print("Committed.")

subprocess.run(["git", "push", "origin", "main"], check=True)
print("Pushed.")

# ============================================================
# IndexNow
# ============================================================
urls = [
    "https://virtuevigil.com/reviews/first-blood-1982/",
    "https://virtuevigil.com/reviews/john-wick-chapter-2-2017/",
    "https://virtuevigil.com/reviews/mission-impossible-fallout-2018/"
]
print("Submitting to IndexNow...")
result = subprocess.run(
    ["bash", "scripts/submit-indexnow.sh"] + urls,
    capture_output=True, text=True
)
print(result.stdout)
if result.returncode != 0:
    print("IndexNow error:", result.stderr)

print("Done!")
