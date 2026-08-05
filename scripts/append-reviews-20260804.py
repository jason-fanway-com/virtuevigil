#!/usr/bin/env python3
"""Append 3 reviews to reviews.json — 2026-08-04.
Films: Spider-Man (2002), Thor (2011), The Rock (1996)
"""
import json, subprocess, sys, os, urllib.request

REVIEWS_FILE = "src/data/reviews.json"
SITE_URL = "https://virtuevigil.com"
INDEXNOW_KEY = "c5c06a51b3df4a6fb07de4954187d031"

with open(REVIEWS_FILE) as f:
    reviews = json.load(f)

existing_slugs = {r["slug"] for r in reviews}
print(f"Loaded {len(reviews)} reviews. Checking slugs...")

new_slugs = ["spider-man-2002", "thor-2011", "the-rock-1996"]
for slug in new_slugs:
    if slug in existing_slugs:
        print(f"ERROR: slug '{slug}' already exists!")
        sys.exit(1)
print("All slugs clear.")

# ============================================================
# REVIEW 1: Spider-Man (2002)
# ============================================================
spider_man_2002 = {
    "id": "spider-man-2002",
    "slug": "spider-man-2002",
    "title": "Spider-Man",
    "year": 2002,
    "type": "film",
    "platform": "Theatrical / Max / Digital",
    "genre": "Action / Superhero / Adventure",
    "date": "2026-08-04",
    "datePublished": "2026-08-04",
    "author": "VirtueVigil Editorial Team",
    "readTime": "13 min read",
    "poster": "/images/posters/spider-man-2002.jpg",
    "releaseDate": "2002-05-03",
    "rating": "PG-13",
    "runtime": "121 min",
    "director": "Sam Raimi",
    "writers": ["David Koepp"],
    "cast": [
        {"name": "Tobey Maguire", "role": "Peter Parker / Spider-Man"},
        {"name": "Kirsten Dunst", "role": "Mary Jane Watson"},
        {"name": "James Franco", "role": "Harry Osborn"},
        {"name": "Willem Dafoe", "role": "Norman Osborn / Green Goblin"},
        {"name": "J.K. Simmons", "role": "J. Jonah Jameson"},
        {"name": "Cliff Robertson", "role": "Uncle Ben"},
        {"name": "Rosemary Harris", "role": "Aunt May"},
        {"name": "Joe Manganiello", "role": "Flash Thompson"}
    ],
    "studio": "Columbia Pictures / Marvel Enterprises",
    "distributor": "Columbia Pictures",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 0.70,
    "tradScore": 23.94,
    "authIndex": 97,
    "scoreMargin": "+23 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Not a woke trap. Spider-Man has no negative margin to trigger trap evaluation. The film is openly, unambiguously traditional from its opening frames: a teenage boy in Queens, raised by his aunt and uncle, who learns through tragedy that power obligates. The moral philosophy is stated plainly and repeated. No hidden progressive payload. STRONGLY TRADITIONAL by a wide margin."
    },
    "seoTitle": "Is Spider-Man (2002) Woke? Sam Raimi's Original Tobey Maguire Film Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil reviews Sam Raimi's Spider-Man (2002). Tobey Maguire, Willem Dafoe, and one of cinema's most explicit traditional moral philosophies. Full VVWS trope audit. Verdict: STRONGLY TRADITIONAL (+23).",
    "seoKeywords": [
        "is Spider-Man 2002 woke",
        "Spider-Man 2002 traditional values",
        "Sam Raimi Spider-Man review",
        "Tobey Maguire Spider-Man review",
        "Spider-Man 2002 conservative review",
        "Spider-Man 2002 VirtueVigil score",
        "is Spider-Man appropriate for kids",
        "Spider-Man 2002 parents guide",
        "Spider-Man with great power comes great responsibility",
        "Spider-Man 2002 woke or traditional",
        "original Spider-Man film review",
        "Willem Dafoe Green Goblin review",
        "Raimi Spider-Man vs new Spider-Man",
        "best traditional superhero movies",
        "Spider-Man moral lessons"
    ],
    "externalScores": {
        "rottenTomatoesCritic": "90%",
        "rottenTomatoesAudience": "73%",
        "imdb": "7.4/10",
        "metacritic": "62",
        "oscarNominations": 2,
        "oscarCategories": "Best Visual Effects (nominated), Best Sound Editing (nominated)",
        "budget": "$139 million",
        "globalBoxOffice": "$821.7 million"
    },
    "creative_team": {
        "director": {
            "name": "Sam Raimi",
            "ideology": "NEUTRAL. Raimi is a genre craftsman whose personal politics rarely surface in his work. The Evil Dead films are pure horror, with no ideological agenda beyond scaring the audience. Darkman (1990) is a disfigured-hero pulp thriller in the Universal Monsters tradition. The Quick and the Dead (1995) is a revisionist Western that questions masculine gun culture, the closest Raimi has come to a politically inflected genre piece. Spider-Man operates entirely within the moral universe Stan Lee established for the character in 1962. Raimi did not impose his own ideology on the material. He honored Lee's philosophy, which is traditionalist in the most direct sense: responsibility is the price of power, and the hero pays that price without complaint. His later Doctor Strange in the Multiverse of Madness (2022) similarly operated within the moral framework handed to him rather than subverting it. Raimi makes movies, not arguments.",
            "profile": "Sam Raimi grew up in Michigan obsessing over horror films and built his early career on the Evil Dead franchise with his college friends, including Bruce Campbell. Evil Dead II (1987) and Army of Darkness (1992) established him as a filmmaker with genuine genre instincts and a wild visual imagination. His studio debut, Darkman (1990), demonstrated he could direct action at scale. After The Quick and the Dead and A Simple Plan (1998), Sony gave him Spider-Man (2002), which broke the summer opening weekend record at the time. He directed Spider-Man 2 (2004), widely considered one of the best superhero films ever made, and Spider-Man 3 (2007), widely considered the weakest entry in the trilogy. His comeback with Drag Me to Hell (2009) reminded everyone why he was interesting. Marvel brought him in for Doctor Strange 2 in 2022."
        },
        "writers": {
            "names": "David Koepp (screenplay); Stan Lee, Steve Ditko (Marvel Comics characters)",
            "profile": "David Koepp wrote Jurassic Park (1993), Mission: Impossible (1996), War of the Worlds (2005), and several other major commercial thrillers before and after Spider-Man. His scripts are commercially oriented without discernible ideological content. He adapted the Spider-Man character faithful to Lee's core philosophy: a teenager who gains extraordinary abilities and chooses, with great difficulty, to use them responsibly rather than for personal gain. Koepp's contribution was structuring that philosophical premise into a three-act dramatic arc. He did it well. The plot of the 2002 film is clean, efficient, and morally clear."
        },
        "lead_producer": {
            "name": "Laura Ziskin, Ian Bryce",
            "company": "Columbia Pictures / Marvel Enterprises"
        },
        "composer": {
            "name": "Danny Elfman",
            "profile": "Danny Elfman wrote the Spider-Man theme that became one of the most recognizable superhero musical identities since John Williams's Superman score. The main theme is heroic without irony, driving without being aggressive. Elfman understood that Raimi wanted a score that made swinging through Manhattan feel genuinely exhilarating. He delivered it. His score for Spider-Man 2 is even better, but the original established the template."
        },
        "cinematographer": {
            "name": "Don Burgess",
            "profile": "Don Burgess shot Forrest Gump, Cast Away, and Contact for Robert Zemeckis before Spider-Man. His work here established the visual grammar for the Raimi trilogy: practical sets grounded in a recognizable New York, with the CGI swing sequences treated as ecstatic breaks from that grounded reality. The contrast between the domestic Queens interiors and the aerial spectacle of Manhattan is a visual argument for Spider-Man's double identity."
        },
        "top_cast": [
            {"name": "Tobey Maguire", "role": "Peter Parker / Spider-Man"},
            {"name": "Kirsten Dunst", "role": "Mary Jane Watson"},
            {"name": "James Franco", "role": "Harry Osborn"},
            {"name": "Willem Dafoe", "role": "Norman Osborn / Green Goblin"},
            {"name": "J.K. Simmons", "role": "J. Jonah Jameson"},
            {"name": "Cliff Robertson", "role": "Uncle Ben"},
            {"name": "Rosemary Harris", "role": "Aunt May"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "PG-13",
        "mpaaDescriptors": "Stylized violence and action",
        "recommendedAge": "10+",
        "contentWarnings": [
            "Uncle Ben is shot and killed in a carjacking sequence shown on screen. This is handled with restraint but it is the film's most emotionally impactful moment and may distress younger viewers.",
            "The Green Goblin's attacks involve grenades, razor blades, and brutal physical combat. One sequence involves him attacking civilians at a public festival.",
            "The film's climax involves the apparent death of Mary Jane and a brutal confrontation between Spider-Man and the Green Goblin.",
            "Norman Osborn's fractured personality scenes include disturbing dialogue with his mirror reflection.",
            "Mild language throughout. No sexual content."
        ],
        "parentalNotes": "Spider-Man is genuinely appropriate for most children 10 and up. The PG-13 rating is earned by violence, not sexual content or language. The film's moral philosophy, that power creates obligation and that responsibility sometimes costs you things you want, is exactly the kind of message worth sharing with children. Uncle Ben's death is handled with the weight it deserves: it's sad, it's consequential, and it's the point. Parents should be prepared for a quiet conversation afterward. The Goblin can be frightening for sensitive younger viewers. The film works on multiple levels and grows more meaningful as its audience grows older."
    },
    "fidelityCasting": {
        "assessment": "FAITHFUL",
        "explanation": "Spider-Man (2002) faithfully translates the character's visual and demographic identity from the source material. Peter Parker in the comics is a working-class white teenager in Queens, an academic overachiever from a modest household. Tobey Maguire's casting is appropriate. Mary Jane Watson is a red-haired aspiring actress in the source material. Kirsten Dunst's casting is appropriate. Norman Osborn is a business mogul and scientist. Willem Dafoe's casting is inspired. J.K. Simmons as J. Jonah Jameson was so faithful to the source material that Sony kept him in the role across three different Spider-Man reboots spanning twenty years, a record for Marvel casting continuity. No character races were altered. No gender swaps were made. The creative team trusted the source material."
    },
    "summary": {
        "overall": "Sam Raimi's Spider-Man hit theaters on May 3, 2002, cleared $114 million in its opening weekend, which was a box office record at the time, and grossed $821 million worldwide against a $139 million budget. The money is the second-most interesting thing about it.\n\nPeter Parker (Tobey Maguire) is a seventeen-year-old science nerd in Queens. He lives with his aunt and uncle in a modest rowhouse, is in love with the girl next door, and is invisible at school except to whoever's bullying him that week. A genetically enhanced spider bites him during a school field trip. His body rewrites itself overnight: superhuman strength, wall-crawling ability, web-shooters built into his wrists, and a precognitive 'spider-sense' that makes him nearly impossible to hit.\n\nHis first thought is to use it to make money. He enters a wrestling match to win cash for a car he wants to impress Mary Jane. He wins. The promoter stiffs him. On his way out, a thief sprints past. Peter doesn't stop him. He could. Minutes later, the same thief shoots Uncle Ben (Cliff Robertson) during a carjacking. Ben dies. Peter catches the thief that night and the thief falls to his death. It doesn't bring Ben back.\n\nThat is the entire engine of the movie. Peter failed to act when he could have. A man died because of that failure. The rest of Spider-Man is the consequence: he becomes a hero not because he wants to feel powerful but because not becoming one would mean Ben died for nothing.\n\nWillem Dafoe plays Norman Osborn, a weapons contractor whose experimental combat-enhancement compound fractured his personality. The brilliant scientist and a murderous alter ego share the same body and argue in the mirror. Dafoe plays both sides completely, and that commitment is what makes him work. He is the most frightening villain in any of the three Raimi films. Not because he is physically intimidating but because he is genuinely insane and has no idea what his Goblin persona does while he is not watching.\n\nNorman works out that Spider-Man's weakness is the people he loves. The Queensboro Bridge sequence, where the Goblin forces Peter to choose between saving Mary Jane and saving a cable car full of children, is the film's most explicit argument: the hero cannot put his personal attachments above his duty. Peter saves both. The Goblin almost kills him twice, and Peter keeps getting back up not because he's physically superior but because stopping would dishonor Ben.\n\nJ.K. Simmons as J. Jonah Jameson is one of cinema's greatest comic performances. He walks into every scene and makes the film 15 percent better by existing. Sony was so aware of this that they kept him in the role across three complete reboots over twenty-two years. That is not a business decision. That is an acknowledgment that the performance is irreplaceable.\n\nThe finale is where the film earns its traditional score most explicitly. Peter unmasks himself to a dying Norman, who asks him not to tell Harry who the Goblin was. Peter keeps the secret, protecting Harry from knowledge that would destroy him. Then Peter walks away from Mary Jane, who has told him she loves him, because being with him would make her a target. He does not get the girl. He does not get the recognition. He gets the obligation. The film treats that as heroic, not tragic.\n\nThat is what makes Spider-Man (2002) still remarkable twenty-four years later. Hollywood keeps trying to complicate the superhero's relationship to sacrifice, to inject irony into duty, to deconstruct the idea that responsibility is its own reward. Raimi's film does none of that. It believes in its thesis without hedging. Power creates obligation. The hero pays the price. That's the deal, and the film makes you feel why the deal is worth accepting.",
        "adultInsight": "The interesting question about Spider-Man (2002) from today's vantage is whether Hollywood could make it now. The film asks its audience to accept without irony that a seventeen-year-old who could have anything will choose nothing, because the people he loves would be safer without him. There is no deconstructive wink. Raimi plays it straight and Maguire plays it straight and Dunst plays it straight. A 2026 production would almost certainly undercut that ending. It would need to be complicated, or the sacrifice would need to be temporary, or there would be a post-credits scene restoring what was lost. Spider-Man just shows you the cost and lets it sit. That restraint is what makes the final scene hit as hard as it does. Peter Parker walks away from the woman he loves in broad daylight. No swell of triumph. Just duty. The film trusts you to understand why that matters.",
        "parentalGuidance": "Rated PG-13 for stylized violence and action. Spider-Man is genuinely appropriate for most children 10 and up. The violence is comic-book in style and scale. Uncle Ben's death is the most emotionally significant moment: it is handled with dignity and weight, and it is the point of the entire film. Parents should be prepared for a conversation afterward about responsibility and consequences. The Green Goblin can frighten sensitive younger viewers. The moral framework is completely traditional: with great power comes great responsibility. This is exactly the kind of film worth watching with children."
    },
    "tropeAudit": [
        {
            "id": "TRAD-SM2-001",
            "name": "With Great Power Comes Great Responsibility",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "description": "This is not a secondary theme. It is the film's stated thesis, delivered by Uncle Ben before his death and held by Peter as the reason he became Spider-Man at all. The moral logic is airtight: Peter failed to act when he could, a man died, and the lesson is that capability creates obligation. Stan Lee wrote this principle into the character in 1962 and it has never been more clearly dramatized than in Raimi's 2002 adaptation. Every scene after Ben's death is the consequence of Peter accepting this principle."
        },
        {
            "id": "TRAD-SM2-002",
            "name": "The Self-Sacrificing Male Hero",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "description": "By the final scene, Peter has sacrificed his relationship with Mary Jane, his friendship with Harry, his financial stability, and his public reputation to protect people who largely despise him. J. Jonah Jameson's newspaper calls him a criminal. The city does not know his name. He gets nothing from being Spider-Man except the knowledge that his duty is being met. The film presents this as heroic. Not complicated, not tragic, not something to be resolved in a sequel. Heroic."
        },
        {
            "id": "TRAD-SM2-003",
            "name": "The Traditional Family as Moral Foundation",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "Aunt May and Uncle Ben are the film's conscience. Their modest Queens home is the moral center of Peter's world. Ben's death is not a plot device. It is the price of irresponsibility, made permanent and specific. May's faith in Peter, her prayers when he is in danger, and her terror when the Goblin attacks her are the human stakes the action sequences are built around. The film treats the traditional family unit as irreplaceable and its loss as genuinely devastating."
        },
        {
            "id": "TRAD-SM2-004",
            "name": "Personal Responsibility and Consequence",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "description": "Peter receives his powers through a random event, but he earns his heroism through choice. The film makes no argument that systems or institutions are responsible for Peter's development. He chooses to stand aside when the thief runs past. He bears the consequence. He chooses to become Spider-Man. He bears that consequence too. When he fails, the results are immediate and permanent. The moral logic is classical: actions have consequences, and you are accountable for yours."
        },
        {
            "id": "TRAD-SM2-005",
            "name": "Traditional Courtship and Romantic Love",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "description": "Peter's love for Mary Jane is earnest, romantic, and chaste. There is no casual sex, no hook-up culture, no sexual transaction. He is in love with a girl and cannot tell her. The upside-down kiss in the rain is one of cinema's most iconic romantic images because it captures genuine longing without cheapening it. Peter lets her go at the end because he believes her safety matters more than his happiness. This is the traditional romance structure: sacrifice over gratification."
        },
        {
            "id": "TRAD-SM2-006",
            "name": "Moral Clarity",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "description": "Norman Osborn is unambiguously evil. He knows his Goblin persona is murdering people and he feeds it. The Green Goblin is not a metaphor for institutional violence or a response to systemic oppression. He is a man who chose power over conscience and is paying for it with his sanity. Spider-Man is unambiguously good. The moral universe of the film is clear and it never apologizes for that clarity."
        },
        {
            "id": "WOKE-SM2-001",
            "name": "Bullied Outsider Narrative",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "description": "Peter is bullied at school by Flash Thompson, and the film treats this as partly unjust. This is completely organic to the source material: Stan Lee designed Spider-Man as the antithesis of the golden-age hero, specifically to appeal to kids who did not see themselves in Superman. The bullying exists to make Peter's eventual restraint more meaningful. It is character building, not ideological positioning about social hierarchies."
        },
        {
            "id": "WOKE-SM2-002",
            "name": "Press as Institutional Antagonist",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "description": "J. Jonah Jameson's Daily Bugle frames Spider-Man as a criminal, and the media pressure briefly turns the city against him. This is a storytelling device, not a critique of institutional media from a progressive angle. Jameson is played entirely for comedy and his position is portrayed as wrong. The press-as-antagonist element is genre-organic and predates the contemporary media critique discourse by decades."
        }
    ],
    "seo": {
        "titleTag": "Is Spider-Man (2002) Woke? Sam Raimi's Tobey Maguire Film Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Sam Raimi's Spider-Man (2002) starring Tobey Maguire. Full VVWS trope audit. Verdict: STRONGLY TRADITIONAL (+23). Parental guidance included. One of cinema's most explicitly traditional superhero films.",
        "keywords": "is Spider-Man 2002 woke, Spider-Man 2002 traditional values, Sam Raimi Spider-Man review, Tobey Maguire Spider-Man parents guide, Spider-Man with great power comes great responsibility, best traditional superhero movies, Spider-Man conservative review"
    }
}

# ============================================================
# REVIEW 2: Thor (2011)
# ============================================================
thor_2011 = {
    "id": "thor-2011",
    "slug": "thor-2011",
    "title": "Thor",
    "year": 2011,
    "type": "film",
    "platform": "Theatrical / Disney+ / Digital",
    "genre": "Action / Adventure / Fantasy",
    "date": "2026-08-04",
    "datePublished": "2026-08-04",
    "author": "VirtueVigil Editorial Team",
    "readTime": "11 min read",
    "poster": "/images/posters/thor-2011.jpg",
    "releaseDate": "2011-05-06",
    "rating": "PG-13",
    "runtime": "115 min",
    "director": "Kenneth Branagh",
    "writers": ["Ashley Edward Miller", "Zack Stentz", "Don Payne"],
    "cast": [
        {"name": "Chris Hemsworth", "role": "Thor"},
        {"name": "Natalie Portman", "role": "Jane Foster"},
        {"name": "Tom Hiddleston", "role": "Loki"},
        {"name": "Anthony Hopkins", "role": "Odin"},
        {"name": "Stellan Skarsgard", "role": "Dr. Erik Selvig"},
        {"name": "Kat Dennings", "role": "Darcy Lewis"},
        {"name": "Clark Gregg", "role": "Agent Phil Coulson"},
        {"name": "Idris Elba", "role": "Heimdall"},
        {"name": "Rene Russo", "role": "Frigga"},
        {"name": "Jaimie Alexander", "role": "Sif"},
        {"name": "Ray Stevenson", "role": "Volstagg"},
        {"name": "Jeremy Renner", "role": "Clint Barton / Hawkeye"}
    ],
    "studio": "Marvel Studios",
    "distributor": "Paramount Pictures",
    "verdict": "TRADITIONAL",
    "wokeScore": 1.70,
    "tradScore": 18.20,
    "authIndex": 91,
    "scoreMargin": "+17 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Not a woke trap. The film's progressive elements are visible from its opening sequences. Heimdall's casting is apparent from the first Asgard scenes. S.H.I.E.L.D.'s antagonistic relationship with Jane's research is established early. The film's dominant value system is traditional: an arrogant prince learns humility through exile and self-sacrifice and earns back his birthright. No hidden payload. The woke elements are minor and front-loaded."
    },
    "seoTitle": "Is Thor (2011) Woke? The Original MCU Film Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil reviews Marvel's Thor (2011). Kenneth Branagh's Shakespearean take on the God of Thunder. Full VVWS trope audit. Verdict: TRADITIONAL (+17). Parental guidance included.",
    "seoKeywords": [
        "is Thor 2011 woke",
        "Thor 2011 traditional values",
        "Thor MCU review conservative",
        "Thor 2011 parents guide",
        "is Thor appropriate for kids",
        "Thor 2011 VirtueVigil score",
        "Kenneth Branagh Thor review",
        "Chris Hemsworth Thor woke or traditional",
        "Thor 2011 traditional or woke",
        "original Thor film review",
        "Thor Loki family dynamic traditional",
        "best MCU traditional films",
        "Thor Heimdall casting controversy",
        "Thor 2011 VVWS score"
    ],
    "externalScores": {
        "rottenTomatoesCritic": "77%",
        "rottenTomatoesAudience": "76%",
        "imdb": "7.0/10",
        "metacritic": "57",
        "oscarNominations": 1,
        "oscarCategories": "Best Visual Effects (nominated)",
        "budget": "$150 million",
        "globalBoxOffice": "$449.3 million"
    },
    "creative_team": {
        "director": {
            "name": "Kenneth Branagh",
            "ideology": "CENTER LEANING TRADITIONAL. Branagh built his reputation adapting Shakespeare for cinema, and he approaches superhero filmmaking as he approaches the Bard: with theatrical seriousness and a genuine interest in the moral stakes of the story. His Shakespeare films (Henry V, Much Ado About Nothing, Hamlet, Love's Labour's Lost) treat the source material with respect and affection, not deconstruction. When Marvel hired him for Thor, he treated it the same way: as a Shakespearean family tragedy about a prideful son, a wounded second child, and a flawed patriarch. His interest in Thor was not political. It was dramatic. His later work, including Belfast (2021), is openly autobiographical and emotionally conservative: a love letter to community, family, and home. He is not an ideological filmmaker.",
            "profile": "Kenneth Branagh is a Belfast-born actor and filmmaker best known for his Shakespeare film adaptations beginning with Henry V (1989). He has performed and directed across stage and screen for four decades, covering everything from Hamlet (1996, his four-hour uncut version) to Cinderella (2015, the Disney live-action remake) to Agatha Christie's Poirot mysteries. He received the opportunity to direct Thor after Marvel's Kevin Feige saw his work and believed his theatrical instincts could give the Asgard sequences the grandeur they required. Branagh's Asgard works precisely because he treats it like a Shakespeare history play: kings, betrayal, inheritance, and the question of who deserves to rule. He was replaced by Alan Taylor for Thor: The Dark World (2013), to that film's significant detriment."
        },
        "writers": {
            "names": "Ashley Edward Miller, Zack Stentz, Don Payne (screenplay); J. Michael Straczynski, Mark Protosevich (story)",
            "profile": "Ashley Edward Miller and Zack Stentz co-wrote X-Men: First Class (2011) and several episodes of Fringe before Thor. Don Payne wrote Fantastic Four: Rise of the Silver Surfer and My Super Ex-Girlfriend. J. Michael Straczynski created Babylon 5 and has written widely for Marvel. The writing team approached Thor's arc as a classical character reformation, which it is. Their contribution was structuring the humility arc without making it feel punitive: Thor loses power, encounters ordinary people, grows through the encounter, and earns his way back. That structure is traditional and durable."
        },
        "lead_producer": {
            "name": "Kevin Feige",
            "company": "Marvel Studios"
        },
        "composer": {
            "name": "Patrick Doyle",
            "profile": "Patrick Doyle has scored four of Branagh's films, including Henry V, Much Ado About Nothing, and Hamlet. His Thor score is appropriately grand for the Asgard sequences and grounded for the New Mexico sequences. The main Thor theme has genuine heroic weight. Doyle was replaced by Brian Tyler for later Thor films, and the loss of his orchestral approach is noticeable."
        },
        "top_cast": [
            {"name": "Chris Hemsworth", "role": "Thor"},
            {"name": "Tom Hiddleston", "role": "Loki"},
            {"name": "Natalie Portman", "role": "Jane Foster"},
            {"name": "Anthony Hopkins", "role": "Odin"},
            {"name": "Idris Elba", "role": "Heimdall"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "PG-13",
        "mpaaDescriptors": "Sequences of intense sci-fi action and violence",
        "recommendedAge": "10+",
        "contentWarnings": [
            "Extended fight sequences including Asgardian warriors battling Frost Giants with significant violence.",
            "The Destroyer, a robotic enforcer, attacks a small New Mexico town and is shown crushing vehicles and threatening civilians.",
            "Thor is hit by a truck and later by Mjolnir, with some physical injury depicted.",
            "Loki's manipulation of Odin, Thor, and the Frost Giant king involves significant deception and is emotionally intense.",
            "Odin falls into the Odinsleep, which is depicted with some urgency. Characters believe he may not wake.",
            "Loki releases the Destroyer to kill Thor in a sequence that may frighten younger viewers."
        ],
        "parentalNotes": "Thor is appropriate for most children 10 and up. The film's violence is fantastical in nature, involving mythological beings rather than realistic human combat. The emotional content is the more significant element: the father-son relationship between Odin and Thor, and the revelation of Loki's true origins, are genuinely affecting. The film's themes, about pride, humility, and earning the things you want, are worth discussing with children. The Frost Giants are visually distinctive but not especially frightening. Thor's fish-out-of-water scenes in New Mexico provide considerable light relief."
    },
    "fidelityCasting": {
        "assessment": "MOSTLY FAITHFUL WITH ONE NOTED DEVIATION",
        "explanation": "The core cast is appropriate: Chris Hemsworth's physical presence and earnest charisma capture the Thor of the comics, and Tom Hiddleston's Loki is widely regarded as one of the best villain performances in the MCU. Anthony Hopkins brings exactly the weight Odin requires. Natalie Portman's Jane Foster is somewhat flattened by the script but is appropriate to the character's comics origins. The noted deviation is Idris Elba as Heimdall, who in Norse mythology and the comics is white. Elba's performance is strong and Heimdall is not a central character, which limits the impact, but under VVWS v1.1 this registers as a diversity casting trope because Heimdall has an established racial identity in prior versions of the character. This has been scored accordingly."
    },
    "summary": {
        "overall": "Kenneth Branagh's Thor (2011) is the MCU film that established Marvel could do mythology at scale and not embarrass itself. It cost $150 million, grossed $449 million worldwide, and introduced both Chris Hemsworth and Tom Hiddleston to global audiences. More relevant to this review: it is one of the more traditional entries in the MCU's first phase, built on a character arc so classical it could have come from Aristotle.\n\nThor (Hemsworth) is the eldest son of Odin (Anthony Hopkins), king of Asgard, and he is insufferable about it. Arrogant, impulsive, and constitutionally incapable of backing down from a fight, he is days from taking the throne when Frost Giants infiltrate Asgard to reclaim the Casket of Ancient Winters. Thor's response is to lead a retaliatory raid into Jotunheim, the Frost Giant realm, breaking a peace that has held for centuries. Odin strips him of his powers, banishes him to Earth with his hammer Mjolnir, and places an enchantment on the hammer: only someone worthy may lift it.\n\nThor crash-lands in New Mexico, where astrophysicist Jane Foster (Natalie Portman) and her team are studying atmospheric anomalies. S.H.I.E.L.D. immediately seizes their equipment. Thor and Jane begin to connect while Thor adjusts to being a powerless mortal in a world he does not understand. His attempts to reclaim Mjolnir from a S.H.I.E.L.D. facility fail: he cannot lift it. He is not yet worthy.\n\nIn Asgard, Loki (Hiddleston) has discovered that he is not Odin's biological son but a Frost Giant infant taken in conquest. He makes a series of moves that ensure Thor cannot return and positions himself to consolidate power. He is not cartoonishly evil. He is wounded, brilliant, and operating from genuine pain, which makes him the most interesting villain in the MCU's first three phases.\n\nThe arc resolves when the Destroyer is sent to Puente Antiguo to eliminate Thor permanently. Thor, still mortal and powerless, walks out unarmed to face it and offer himself in exchange for the safety of the town's residents. He is willing to die for the people around him. The enchantment recognizes this as worthiness. Mjolnir returns. Thor becomes himself again.\n\nBranagh structures this as a Shakespearean family drama with superhero action as backdrop. The Asgard sequences feel appropriately grand: real sets, Hopkins playing Odin as a king who has been managing impossible tradeoffs for centuries, and Hiddleston playing Loki as the perpetual second son who was never going to inherit and always knew it. The father-son dynamic is the film's emotional backbone. Odin's decisions, including the decision to strip Thor of his power, are vindicated by events. The film trusts the patriarch's wisdom even when Thor cannot.\n\nThe New Mexico sequences are lighter: Thor trying to order coffee, demanding a horse, slamming an empty mug on a diner counter and declaring it delicious. Hemsworth's comedic timing proved here that his casting was right. He plays Thor's fish-out-of-water moments not as embarrassment but as wonder, which is the correct choice for a character who has never had reason to doubt his own greatness and is genuinely encountering its limits for the first time.\n\nThe film's woke elements are limited and mostly visible from the opening. Heimdall (Idris Elba), a Norse mythological figure who is white in the source tradition, is played by a Black British actor. The film makes nothing of this, which is either a defense or a further indication that the casting was a statement. S.H.I.E.L.D. confiscates Jane's research equipment without compensation and forces her from her work site, a government-agency-as-antagonist element that is organic to the MCU universe-building rather than ideologically injected. These elements have been scored and cost points; they do not define the film.\n\nWhat defines Thor is its central argument: worthiness is a moral condition, not a birthright. You cannot inherit it and you cannot claim it. You earn it through the willingness to sacrifice for others. Thor earns it by walking unarmed into the Destroyer's path to protect people he barely knows. That argument is as old as the hero myth and as clear as it gets in contemporary blockbuster cinema.",
        "adultInsight": "The Loki problem in Thor is the film's most interesting adult dimension. Loki discovers mid-film that he was adopted, that he is genetically a Frost Giant, and that the entire foundation of his identity was built on Odin's undisclosed decision. His breakdown is sympathetic. His subsequent actions are monstrous. The film does not offer him an easy resolution: Loki falls into the void at the end of his own choice. He is not redeemed. He is not punished externally. He makes a decision and lives with it, except he doesn't, because he comes back in The Avengers. But within the frame of this single film, Loki's arc is a genuine tragedy about what happens when the gap between who you believed you were and who you actually are cannot be bridged. It is a more psychologically serious examination of identity and inheritance than most superhero films attempt.",
        "parentalGuidance": "Rated PG-13 for sequences of intense sci-fi action and violence. Thor is appropriate for most children 10 and up. The Frost Giant battle sequences are intense but fantastical, with no realistic blood. The film's most emotionally significant moments involve family and inheritance: Odin stripping Thor of his powers, Loki's discovery of his true origins, and the reconciliation arc. These are genuinely affecting and worth discussing with older children. Younger viewers may find the Destroyer sequence frightening. The film's moral, that pride leads to loss and humility is the path back, is exactly the kind of lesson children are ready for."
    },
    "tropeAudit": [
        {
            "id": "TRAD-THOR-001",
            "name": "Redemption Through Humility",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "description": "Thor's entire arc is a classical character reformation. He begins arrogant, impulsive, and constitutionally incapable of restraint. Odin strips his power and casts him out not as punishment for incompetence but for pride. The exile works: Thor encounters ordinary mortals, develops genuine care for people who cannot defend themselves, and ultimately acts with selfless courage. The reformation is earned scene by scene and the film does not shortcut it."
        },
        {
            "id": "TRAD-THOR-002",
            "name": "Self-Sacrifice as the Measure of Worthiness",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "description": "The enchantment Odin places on Mjolnir is explicit: 'Whosoever holds this hammer, if he be worthy, shall possess the power of Thor.' The film defines worthiness through a specific act: Thor walks unarmed into the Destroyer's path to save the people of Puente Antiguo. He is willing to die for strangers. Mjolnir returns because that act of selfless sacrifice is exactly what the enchantment was designed to measure. The film does not state this as an abstract principle. It dramatizes it."
        },
        {
            "id": "TRAD-THOR-003",
            "name": "The Father-Son Bond and Patriarchal Wisdom",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.80,
            "description": "Odin's relationship with Thor is the film's emotional center. Odin is imperfect: his concealment of Loki's origins is a significant failure that drives the subplot. But his love for both sons is never in doubt, and his decision to strip Thor of his power is vindicated. The film treats the father's long-horizon wisdom as ultimately correct, even when the son cannot see it. Thor earns his way back into his father's trust. The arc affirms that paternal authority, when properly exercised, produces the conditions for genuine growth."
        },
        {
            "id": "TRAD-THOR-004",
            "name": "Traditional Courtship",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "description": "Thor and Jane's romance is earnest and completely chaste. Thor asks permission before touching Jane. He is straightforward about his attraction without being predatory. Jane's interest is based on genuine admiration for who Thor is, not manipulation or proximity. There is no sexual content. The romance is a secondary plot but it models the traditional courtship structure: genuine mutual interest, respect, and patience."
        },
        {
            "id": "TRAD-THOR-005",
            "name": "Warrior Ethos and Honor Culture",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.70,
            "description": "Asgardian warrior culture, with its emphasis on courage, loyalty, and the shame of cowardice, is portrayed as genuinely admirable. The Warriors Three follow Thor into exile out of loyalty, not obligation. Sif is a warrior who has earned her position through competence. The film treats military brotherhood and loyalty as binding obligations, not relics to be deconstructed."
        },
        {
            "id": "WOKE-THOR-001",
            "name": "Race-Swapped Established Character (Heimdall)",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.00,
            "description": "Heimdall, a Norse mythological figure with an established white racial identity in the source tradition and prior comics versions, is played by Idris Elba. The film provides no in-universe justification and makes nothing of it narratively. Elba's performance is strong and Heimdall is not a major character, limiting the centrality. Per VVWS v1.1, this registers as a diversity casting trope. The authenticity is scored as Moderate because the film does not make a statement of it."
        },
        {
            "id": "WOKE-THOR-002",
            "name": "Government Agency as Antagonist Force",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.70,
            "description": "S.H.I.E.L.D. confiscates Jane's research equipment without compensation and forces her from her work site. The agency is portrayed as high-handed, secretive, and unaccountable to the people it affects. This is organic to MCU universe-building rather than an ideological statement about government, and the centrality is low. It functions as plot mechanism more than political commentary."
        }
    ],
    "seo": {
        "titleTag": "Is Thor (2011) Woke? The Original MCU Thor Film Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Kenneth Branagh's Thor (2011). The MCU's God of Thunder earns his hammer back through humility and sacrifice. Full VVWS trope audit. Verdict: TRADITIONAL (+17). Parental guidance included.",
        "keywords": "is Thor 2011 woke, Thor MCU review, Thor 2011 traditional values, original Thor film, Thor Heimdall casting, Thor Loki father son, Thor parents guide, best traditional MCU films, Kenneth Branagh Thor"
    }
}

# ============================================================
# REVIEW 3: The Rock (1996)
# ============================================================
the_rock_1996 = {
    "id": "the-rock-1996",
    "slug": "the-rock-1996",
    "title": "The Rock",
    "year": 1996,
    "type": "film",
    "platform": "Theatrical / Max / Digital",
    "genre": "Action / Thriller",
    "date": "2026-08-04",
    "datePublished": "2026-08-04",
    "author": "VirtueVigil Editorial Team",
    "readTime": "12 min read",
    "poster": "/images/posters/the-rock-1996.jpg",
    "releaseDate": "1996-06-07",
    "rating": "R",
    "runtime": "136 min",
    "director": "Michael Bay",
    "writers": ["David Weisberg", "Douglas S. Cook", "Mark Rosner"],
    "cast": [
        {"name": "Sean Connery", "role": "John Patrick Mason"},
        {"name": "Nicolas Cage", "role": "Dr. Stanley Goodspeed"},
        {"name": "Ed Harris", "role": "General Frank Hummel"},
        {"name": "John Spencer", "role": "FBI Director James Womack"},
        {"name": "David Morse", "role": "Major Tom Baxter"},
        {"name": "William Forsythe", "role": "Special Agent Ernest Paxton"},
        {"name": "Michael Biehn", "role": "Commander Anderson"},
        {"name": "Tony Todd", "role": "Captain Darrow"}
    ],
    "studio": "Don Simpson/Jerry Bruckheimer Films",
    "distributor": "Hollywood Pictures / Buena Vista Pictures",
    "verdict": "TRADITIONAL",
    "wokeScore": 2.10,
    "tradScore": 20.02,
    "authIndex": 91,
    "scoreMargin": "+18 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Not a woke trap. The Rock has a positive margin and a TRADITIONAL verdict. The government cover-up element registers as woke because it frames institutions as capable of betrayal, but this is genre-organic to action thrillers and the film does not generalize to a critique of American society or military culture. The heroes act to protect civilians. The traditional elements dominate. No trap applies."
    },
    "seoTitle": "Is The Rock (1996) Woke? The Connery-Cage-Harris Action Classic Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil reviews The Rock (1996). Sean Connery, Nicolas Cage, Ed Harris, and one of the best action scripts of the 1990s. Full VVWS trope audit. Verdict: TRADITIONAL (+18). Parental guidance included.",
    "seoKeywords": [
        "is The Rock 1996 woke",
        "The Rock 1996 traditional values",
        "The Rock movie review conservative",
        "The Rock 1996 parents guide",
        "is The Rock appropriate for adults",
        "The Rock 1996 VirtueVigil score",
        "Michael Bay The Rock review",
        "Sean Connery Nicolas Cage Ed Harris",
        "The Rock 1996 woke or traditional",
        "best traditional action films 90s",
        "The Rock Alcatraz action film review",
        "Ed Harris villain The Rock",
        "The Rock military film review",
        "The Rock Don Simpson Jerry Bruckheimer"
    ],
    "externalScores": {
        "rottenTomatoesCritic": "67%",
        "rottenTomatoesAudience": "87%",
        "imdb": "7.4/10",
        "metacritic": "58",
        "oscarNominations": 1,
        "oscarCategories": "Best Sound (nominated)",
        "budget": "$75 million",
        "globalBoxOffice": "$335.1 million"
    },
    "creative_team": {
        "director": {
            "name": "Michael Bay",
            "ideology": "TRADITIONAL. Bay's filmography is the most commercially aggressive in Hollywood history, and its value system is consistently traditional. Bad Boys (1995) celebrates male friendship and police work. The Rock (1996) honors military service, even in tragedy. Armageddon (1998) is an explicit celebration of American working-class heroism. Pearl Harbor (2001) is a straightforward tribute to the Greatest Generation. The Transformers franchise is militarily pro-American in a way that has made Bay a reliable partner for the Department of Defense. Bay does not make films with progressive messaging. He makes films about American strength, male competence, and the defense of innocent life. His aesthetics are bombastic and his politics, to the extent they are legible, are right of center. The Rock is his best film because Weisberg and Cook's script gave him character and moral stakes to work with alongside the explosions.",
            "profile": "Michael Bay is a Wesleyan graduate and music video director who broke into features with Bad Boys (1995) for Don Simpson and Jerry Bruckheimer. The Rock followed in 1996, making Bay the go-to director for big-budget action spectacle. His career includes Armageddon, Pearl Harbor, the Transformers franchise (six films, $4.8 billion global gross), Pain and Gain, 13 Hours, Ambulance, and Bad Boys: Ride or Die. He is the most commercially successful director in the Bruckheimer stable. Critical reception has been consistently mixed, with The Rock generally regarded as the consensus peak of his craft: the film where his kinetic style served a story with genuine stakes rather than overwhelming one with no stakes at all."
        },
        "writers": {
            "names": "David Weisberg, Douglas S. Cook, Mark Rosner",
            "profile": "David Weisberg and Douglas S. Cook wrote the original spec script that sold to Bruckheimer and Simpson. They had previously written the thriller Double Jeopardy. Mark Rosner did additional work on the script. The writing on The Rock is substantially better than Bay's subsequent films: it gives Hummel a legitimate moral grievance, gives Goodspeed a genuine arc from desk-bound specialist to improvised hero, and gives Mason an interior life beyond his skills. Uncredited contributions reportedly came from Aaron Sorkin and Quentin Tarantino, which, if accurate, would explain why the dialogue has the snap it does."
        },
        "lead_producer": {
            "name": "Don Simpson, Jerry Bruckheimer",
            "company": "Don Simpson/Jerry Bruckheimer Films / Hollywood Pictures"
        },
        "composer": {
            "name": "Nick Glennie-Smith, Hans Zimmer",
            "profile": "The Rock score is a high-water mark for 1990s action film music: broad, muscular, and propulsive. Hans Zimmer's involvement, alongside Nick Glennie-Smith, produced the immediately recognizable main theme that has been used in trailers, sports broadcasts, and video games for thirty years. The score amplifies the film's emotional beats without overwhelming them."
        },
        "cinematographer": {
            "name": "John Schwartzman",
            "profile": "John Schwartzman shot The Rock before Armageddon and several other major productions. His work here is notable for its handheld urgency in the action sequences and its contrast between the sweeping San Francisco exterior shots and the claustrophobic Alcatraz interiors. Bay's trademark golden-hour cinematography is present but restrained compared to his later work."
        },
        "top_cast": [
            {"name": "Sean Connery", "role": "John Patrick Mason"},
            {"name": "Nicolas Cage", "role": "Dr. Stanley Goodspeed"},
            {"name": "Ed Harris", "role": "General Frank Hummel"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "R",
        "mpaaDescriptors": "Pervasive strong language and action violence",
        "recommendedAge": "17+",
        "contentWarnings": [
            "Multiple SEAL operatives killed in an ambush sequence early in the film, depicted with realistic violence.",
            "Chemical weapons (VX nerve agent) are depicted in use, including a scene where a Marine is killed by accidental exposure.",
            "Sustained gunfight sequences with realistic consequences and significant bloodshed.",
            "Several characters are killed in the climax, including one sympathetic villain who dies by chemical weapon.",
            "Pervasive strong language throughout.",
            "Nicolas Cage's character is shown briefly in a situation involving a sexual relationship before the mission."
        ],
        "parentalNotes": "The Rock is a hard-R action film appropriate for adults and mature 17-year-olds. The violence is realistic and consequential rather than stylized. The chemical weapons element adds a dimension of genuine dread that distinguishes this from standard action-movie violence. The film's moral framework is clear: military service deserves recognition, innocent civilians deserve protection, and the individual obligation to act in defense of others overrides personal risk. These are traditional values delivered with considerable visceral force. Not appropriate for younger audiences due to sustained violence, language, and thematic intensity."
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "The Rock is the film that defined the Michael Bay template before it became a cliche. It cost $75 million and grossed $335 million worldwide in 1996, which was significant. More importantly, it is the film in Bay's career where the style and the substance actually support each other, because the script gave him something real to work with.\n\nThe setup is clean and serious. General Frank Hummel (Ed Harris), a three-star Marine general with a Medal of Honor and a career built on classified black-ops, has taken a group of Marine veterans to Alcatraz. They have 81 civilian tourists as hostages. They have 15 VX poison gas rockets aimed at San Francisco. Hummel's demand: $100 million in reparations to the families of Marines who died on classified missions the government refuses to acknowledge. Those men exist in no official record. Their families receive nothing. Their deaths meant nothing. Hummel believes violence is the only language the government will hear.\n\nHe is probably right about the government. He is definitely wrong about the method.\n\nThe FBI's counter requires two specialists no one else can provide. Dr. Stanley Goodspeed (Nicolas Cage) is a chemical weapons expert who has spent his career in a lab studying nerve agents and has never been in the field. John Mason (Sean Connery) is a former British SAS agent who was imprisoned without trial by J. Edgar Hoover for stealing classified microfilm and who, thirty years ago, escaped from Alcatraz. He is the only man who has ever done it, which means he is also the only man who can lead a team back in.\n\nThis casting is the film's first great decision. Connery at 65 plays Mason as a man whose skills have not atrophied but whose patience has. He spent thirty years in a federal penitentiary for a crime that was, technically, just. He owes the government nothing and he is clear about that. His mercenary calculation shifts across the film as he watches Goodspeed operate with genuine courage and the situation demands more than self-interest.\n\nCage plays Goodspeed as a man who is good at his job and terrified of everything his job requires. He is excellent at identifying chemical agents in a laboratory. He is not excellent at staying calm when people are shooting at him. His transformation across the film is the one Bay's kinetic style actually earns: you watch Goodspeed go from scared to effective not through a training montage but through accumulated desperation. By the time he is crawling through Alcatraz alone, defusing rockets one by one, you believe in what it cost him.\n\nEd Harris's Hummel is the reason The Rock holds up when Bay's other films from the same period do not. Hummel is right about the injustice. He is wrong about the solution, and crucially, he knows it. His character's arc is the film's moral center: at what point does a legitimate grievance justify illegitimate action? The film does not answer that question by making Hummel a monster. It answers it by having him stop short of actually firing the rockets when the moment arrives. He cannot do it. He is still a general who served the country he is threatening. His subordinate Captain Darrow, who has no such moral anchor, kills him for hesitating.\n\nThe traditional elements are substantial. Goodspeed's arc is the reluctant hero discovering genuine courage. The film honors military service even in its tragedy: Hummel's men are presented as genuinely wronged, and the film takes that grievance seriously. Mason's mentorship of Goodspeed follows the classical structure: the older, more capable man forcing the younger one to develop by refusing to insulate him from the situation. Goodspeed's pregnant girlfriend Carla waits at home, and his commitment to returning to her is the personal human reason his survival matters beyond the mission.\n\nThe government cover-up element costs points under VVWS methodology. Institutions deceiving the people they serve is a woke-inflected framing when it generalizes to systemic critique. The Rock keeps it specific: the FBI and Pentagon covered up specific black-ops missions and failed specific families. That is a targeted institutional failure, not an ideological statement about American power. The heroes act despite that failure, not because of it. Goodspeed and Mason are not fighting the system. They are protecting civilians from someone who decided the system's failure justified mass murder. That distinction matters.\n\nBay at his best, and The Rock is Bay at his best, understands that action sequences only work if you care about the people in them. The film spends enough time on Goodspeed's fear, on Mason's quiet professionalism, and on Hummel's genuine moral struggle to earn the climax. The film runs 136 minutes, which is long for an action thriller, and it uses almost all of them.",
        "adultInsight": "Ed Harris deserved an Oscar nomination for General Hummel, and the fact that he was not nominated tells you something about how seriously the Academy took action films in 1996. Hummel is one of the most morally serious villains in the genre: decorated, principled, genuinely wronged, and fully aware that his response to that wrong is indefensible. His backstory is not a gimmick. It is the film's argument. The question The Rock asks is whether institutional betrayal, the kind that leaves soldiers' families with nothing, can ever justify the threat of mass civilian casualties. Hummel's answer, revealed when he cannot actually pull the trigger, is no. He could not go through with it because his forty years of service were spent protecting civilians, not threatening them. The film does not moralize about this. It dramatizes it. That is the difference between a good action script and a mediocre one.",
        "parentalGuidance": "Rated R for pervasive strong language and action violence. The Rock is an adult film in every sense: the violence is realistic, the moral stakes are serious, and the film's treatment of military service and institutional betrayal requires adult comprehension to fully engage with. The chemical weapons element adds a dimension of genuine dread to the violence. Not appropriate for younger viewers. Mature adults will find a film that takes its premise seriously and delivers on its moral questions. The reluctant hero arc, the mentorship dynamic between Mason and Goodspeed, and Hummel's tragedy are all worth discussing afterward."
    },
    "tropeAudit": [
        {
            "id": "TRAD-ROCK-001",
            "name": "The Reluctant Hero Discovers Courage",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "description": "Stanley Goodspeed is a desk analyst who has never been in the field. His arc across the film is the discovery of courage he did not know he possessed. This is not a training-montage arc: Goodspeed is scared throughout. He does not stop being scared. He acts anyway, because the alternative is watching San Francisco die. The film earns this arc because it does not pretend Goodspeed becomes a soldier. He becomes someone who acts like one when there is no one else left to act."
        },
        {
            "id": "TRAD-ROCK-002",
            "name": "Military Service Honored in Tragedy",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "The film presents Hummel's grievance as legitimate: soldiers who died on classified missions deserve recognition, and their families deserve compensation. The government's failure to provide either is treated as a genuine wrong. Hummel is a decorated general whose anger comes from a real place, not from abstract ideology. The film honors military service by taking the soldiers' sacrifice seriously, even as it condemns Hummel's response to institutional failure."
        },
        {
            "id": "TRAD-ROCK-003",
            "name": "Mentorship and the Father Figure",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "John Mason is the older, more capable man who forces Goodspeed to develop beyond his comfort zone. Mason does not coddle. He challenges, abandons Goodspeed to handle situations alone, and expects him to perform beyond his training. This is the classical mentorship structure: the young man does not become capable through encouragement. He becomes capable by being required to be capable. Mason's investment in Goodspeed's success grows across the film in a way that reads as genuine."
        },
        {
            "id": "TRAD-ROCK-004",
            "name": "Family as the Reason to Come Home",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "description": "Goodspeed's pregnant girlfriend Carla is waiting for him. His commitment to her and to the child they haven't met yet is his personal reason for surviving beyond the mission. The film does not dwell on this, but it establishes the connection early and it is clearly load-bearing. Family is the human reason the hero's survival matters."
        },
        {
            "id": "TRAD-ROCK-005",
            "name": "Duty to Protect Innocents Despite Institutional Failure",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "description": "The government failed Hummel's men. That failure is acknowledged and taken seriously. Goodspeed and Mason act to stop the attack anyway, because 81 hostages and a city of civilians did not commit the institutional betrayal Hummel is avenging. The film's patriotism is not blind allegiance. It is the instinct to protect people who cannot protect themselves, regardless of whether the institutions that should have prevented the crisis actually failed them."
        },
        {
            "id": "TRAD-ROCK-006",
            "name": "Masculine Physical and Professional Competence",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.70,
            "description": "Mason is presented as a physical marvel in his sixties, a former SAS operative whose skills are intact after decades in prison. The film celebrates this without irony. Physical competence in men, the ability to fight, navigate, and endure, is portrayed as genuinely impressive and valuable. Goodspeed's chemical expertise is also treated as real professional competence that matters enormously to the mission's outcome."
        },
        {
            "id": "WOKE-ROCK-001",
            "name": "Government Cover-Up and Institutional Deception",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "description": "The FBI and Pentagon covered up black-ops missions and refused to acknowledge or support the soldiers' families. This institutional betrayal is presented as a genuine wrong that motivated a decorated general to action. The framing of government institutions as capable of significant deception costs woke points. Authenticity is scored High because the cover-up is specific, targeted, and organic to the thriller genre rather than a generalized critique of American power."
        }
    ],
    "seo": {
        "titleTag": "Is The Rock (1996) Woke? The Connery-Cage-Harris Action Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil reviews The Rock (1996) with Sean Connery, Nicolas Cage, and Ed Harris. One of the best action films of the 1990s gets the full VVWS treatment. Verdict: TRADITIONAL (+18). Parental guidance included.",
        "keywords": "is The Rock 1996 woke, The Rock movie traditional values, Sean Connery Nicolas Cage Ed Harris, The Rock Michael Bay review, best traditional action films, The Rock Alcatraz military film, The Rock parents guide, conservative action film review"
    }
}

# Append all 3
reviews.append(spider_man_2002)
reviews.append(thor_2011)
reviews.append(the_rock_1996)

print(f"New total will be: {len(reviews)} reviews")

with open(REVIEWS_FILE, "w") as f:
    json.dump(reviews, f, indent=2, ensure_ascii=False)

print("Reviews written to reviews.json")
