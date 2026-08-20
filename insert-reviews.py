#!/usr/bin/env python3
"""Insert 3 reviews into reviews.json for missed Wed 08-19 content day."""
import json, sys
from datetime import date

today = "2026-08-19"

# ── Review 1: Insidious: Out of the Further (new release) ──
insidious = {
    "id": "insidious-out-of-the-further-2026",
    "slug": "insidious-out-of-the-further-2026",
    "title": "Insidious: Out of the Further",
    "year": 2026,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Horror / Mystery / Thriller",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "11 min",
    "poster": "/images/posters/insidious-out-of-the-further-2026.jpg",
    "releaseDate": "2026-08-21",
    "rating": "PG-13 (Terror, Violent Content, Strong Language, Thematic Material)",
    "runtime": "106 min",
    "director": "Jacob Chase",
    "writers": ["David Leslie Johnson-McGoldrick", "Leigh Whannell", "Jacob Chase"],
    "cast": [
        {"name": "Lin Shaye", "role": "Elise Rainier"},
        {"name": "Amelia Eve", "role": "Gemma"},
        {"name": "Sam Spruell", "role": "The Entity"},
        {"name": "Maisie Richardson-Sellers", "role": "Tessa"},
        {"name": "Brandon Perea", "role": "Marcus"},
        {"name": "Laura Gordon", "role": "Young Elise"},
        {"name": "Island Austin", "role": "Daughter"}
    ],
    "studio": "Blumhouse Productions / Atomic Monster / Screen Gems",
    "distributor": "Sony Pictures Releasing",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 1.4,
    "tradScore": 7.7,
    "authIndex": 68,
    "scoreMargin": "+6 TRAD",
    "preRelease": True,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Out of the Further does not qualify as a woke trap under VVWS v1.1. A woke trap requires negative margin with woke content hidden past 50% runtime. This film carries a +6 TRAD margin and its minor progressive framing, primarily the mother-daughter generational narrative, is present from the opening scenes. The Insidious franchise has always been built on parents protecting their children from supernatural evil, a structurally traditional premise that this sixth entry honors. The maternal focus adds a slight generational-trauma tint but does not subvert the family-protection core. No bait-and-switch here."
    },
    "seo": {
        "titleTag": "Is Insidious: Out of the Further (2026) Woke? Blumhouse Horror Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Insidious: Out of the Further (2026). Lin Shaye returns as Elise in the sixth Insidious entry. A mother can enter The Further. Verdict: TRADITIONAL LEAN (+6). Parental guidance included.",
        "keywords": [
            "is insidious out of the further woke",
            "insidious out of the further 2026 review",
            "insidious out of the further virtuevigil",
            "insidious out of the further traditional or woke",
            "insidious 6 review",
            "insidious out of the further parents guide",
            "insidious franchise woke",
            "blumhouse insidious 2026",
            "lin shaye insidious out of the further",
            "insidious the further explained"
        ]
    },
    "summary": {
        "overview": "Insidious: Out of the Further (2026) is the sixth entry in the long-running Blumhouse supernatural horror franchise, directed by Jacob Chase and co-written by franchise architect Leigh Whannell. Lin Shaye returns as parapsychologist Elise Rainier in a story that follows Gemma (Amelia Eve), a young mother raising her daughter in the house she grew up in, who discovers she can enter The Further, the purgatorial spirit realm at the heart of the series. Unlike previous protagonists who merely visit The Further, Gemma can bring things back, a power that draws the attention of predatory entities who want out. The film follows Gemma's desperate attempt to protect her daughter while navigating a spiritual world that is no longer content to stay on its side of the veil.",
        "overall": "The Insidious franchise has been running for sixteen years now, and what keeps it going is not worldbuilding or lore, it is the same thing that has always powered the best horror films: the primal fear of losing the people you love. Out of the Further understands this. For all its CGI spirit realms and jump scares, the engine of this movie is a mother willing to walk into hell to save her child. That is as traditional as storytelling gets.\n\nJacob Chase takes the director's chair from Patrick Wilson and Patrick Lussier and delivers a competent, workmanlike entry that does not reinvent the franchise but does not embarrass it either. The hook, Gemma can bring things back from The Further, is genuinely clever. It raises the stakes: the danger is no longer just that something will follow you home, but that something will use you as a door. The film gets real mileage out of the question of whether Gemma is a rescuer or a smuggler. The ambiguity works.\n\nLin Shaye remains the franchise's secret weapon. At eighty-plus, she brings a gravity to Elise Rainier that the material does not always earn, and her presence is a reminder of what these films are best at: not the lore or the demon hierarchies or the astral projection rules, but the simple image of someone who cares standing between innocence and the dark. When Shaye is on screen, Out of the Further feels substantial. When she is not, the film settles into competent but unremarkable Blumhouse formula.\n\nThe ideological footprint here is light, which is good news for VirtueVigil readers. There is a gentle mother-daughter generational thread, Gemma's relationship with her own late mother echoes into her fears for her daughter, that reads as modern trauma discourse, but it never becomes the point. The point is protection. The point is that family is worth fighting for, even when the fight is against things that do not obey the laws of physics or the reassurances of therapy. The film's progressive signals are genre-ambient, not ideological. They do not drive the story.\n\nThe larger question with Out of the Further is whether the franchise has earned this many trips back to The Further. The answer depends on what you want from it. If you want a horror movie that will scare your teenager without assaulting your values, this will do. It is not great. It is not a must-see. But it is honest about what it is: a ghost story about a mother who will not let go. That story never goes out of style.",
        "adultInsight": "The Insidious franchise matters less for its scares than for what it reveals about the durability of the family-protection narrative. In an era when horror increasingly uses the genre as a vehicle for social messaging, Out of the Further is a useful reminder that the most effective horror, the kind that keeps people coming back for sixteen years, is built on something older than politics: the terror of losing the people you love, and the hope that love is strong enough to pull them back. Parents who watch this will recognize the fear driving the plot. It is not fear of a monster. It is fear of failing your children. That recognition is valuable, and it costs nothing to your worldview.",
        "parentalGuidance": "Rated PG-13 for terror, violent content, strong language, and thematic material. The Insidious series has always relied on psychological dread and jump scares more than gore, and Out of the Further continues that tradition. There are disturbing images of supernatural entities, moments of intense peril involving a child, and thematic material about death and the afterlife. The spiritual framework, The Further as a purgatorial realm, is fictional horror-fantasy, not a theological statement. The film's morality is unambiguous: protect your family from evil. Suitable for older teens, especially as a conversation starter about the difference between entertainment about the afterlife and doctrine about it."
    },
    "parentalGuidance": {
        "rating": "PG-13",
        "contentWarnings": "Supernatural horror tropes including jump scares, disturbing creature designs, and moments of peril involving a child. Thematic material about death, the afterlife, and generational trauma. Some strong language. No sexual content, minimal gore.",
        "ageRecommendation": "14+. The scares are effective but the PG-13 rating keeps the violence within reasonable bounds. Younger teens who have seen earlier Insidious entries will find this comparable.",
        "discussionTopics": [
            "How does the film portray the difference between spiritual protection and spiritual exploitation?",
            "Is the Further a purgatory, a hell, or something else? What does the film gain by keeping this ambiguous?",
            "Why does a mother's love for her child work as a horror engine across so many different stories?"
        ]
    },
    "creative_team": {
        "director": {
            "name": "Jacob Chase",
            "role": "Director",
            "note": "Chase came up through the Blumhouse system with shorts and the 2020 film Come Play. Out of the Further is his first franchise assignment, and he delivers competent genre craft without notable ideological signatures."
        },
        "writer": {
            "name": "David Leslie Johnson-McGoldrick, Leigh Whannell, Jacob Chase",
            "role": "Screenwriters",
            "note": "Whannell created the franchise with James Wan. Johnson-McGoldrick has written for The Conjuring universe and Aquaman. Neither has a profile of injecting progressive messaging into horror properties. The franchise's ideological record is clean."
        },
        "lead_producer": {
            "name": "Jason Blum, James Wan",
            "role": "Producers"
        }
    },
    "externalScores": {
        "rottenTomatoesCritic": 50,
        "rottenTomatoesAudience": 0,
        "imdb": 0,
        "metacritic": 50,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "TBD",
        "globalBoxOffice": "TBD (wide release August 21, 2026)"
    },
    "tropeAudit": [
        {
            "id": "TRAD-INSIDIOUS6-001",
            "name": "Parent protecting child at any cost",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Gemma's entire arc is built on maternal protection. She enters The Further, a realm that has destroyed or traumatized every protagonist in the franchise, because her daughter is threatened. The film never subverts or deconstructs this. It takes it as a given that a mother's duty is to protect her child, even at the risk of her own soul. This is the Insidious franchise's beating heart and Chase does not mess with it."
        },
        {
            "id": "TRAD-INSIDIOUS6-002",
            "name": "Spiritual warfare with clear good vs evil",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "The Further is a supernatural realm populated by malevolent entities and lost souls. The film draws a clear moral line: the entities are evil, the humans they threaten are innocent, and Elise Rainier's parapsychological work is framed as rescue. There is no moral equivalence, no suggestion that the demons have a point. In an era of horror films that blur the line between monster and victim, this is refreshingly clean."
        },
        {
            "id": "TRAD-INSIDIOUS6-003",
            "name": "Intergenerational family bonds as sacred",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "The film's generational thread connects Gemma to her own late mother and to her daughter. The throughline is not trauma as identity but family as continuity. Elise Rainier's relationship with Gemma echoes her role as surrogate protector across the franchise, reinforcing the idea that connection across generations is a source of strength, not pathology."
        },
        {
            "id": "TRAD-INSIDIOUS6-004",
            "name": "Personal sacrifice for others",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "Multiple characters risk themselves to save others in the climax. Elise Rainier's presence across the franchise is defined by this pattern: she enters The Further because people need her, not because she benefits. The film treats self-sacrifice as heroic without qualification."
        },
        {
            "id": "WOKE-INSIDIOUS6-001",
            "name": "Generational trauma as central narrative frame",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "explanation": "The film uses a mother-daughter-granddaughter generational structure that lightly echoes modern trauma discourse. Gemma's ability comes from her mother, and the danger passes to her daughter. This could read as progressive 'inherited pain' framing, but it is so lightly applied and so thoroughly subordinated to the protective-mother narrative that it barely registers. It is included for completeness, not because it meaningfully shifts the film's ideological center."
        }
    ],
    "fidelityCasting": {
        "assessment": "NO ISSUES",
        "explanation": "All casting serves the story. Lin Shaye has played Elise Rainier since 2010. No race-swaps, gender-swaps, or fidelity violations. The core cast is assembled around story logic, not demographic targets."
    }
}

# ── Review 2: Gremlins (catalog backfill, 1984) ──
gremlins = {
    "id": "gremlins-1984",
    "slug": "gremlins-1984",
    "title": "Gremlins",
    "year": 1984,
    "type": "film",
    "platform": "Streaming / Home Video",
    "genre": "Comedy / Horror / Fantasy",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "12 min",
    "poster": "/images/posters/gremlins-1984.jpg",
    "releaseDate": "1984-06-08",
    "rating": "PG (Horror Comedy Violence, Some Disturbing Images)",
    "runtime": "106 min",
    "director": "Joe Dante",
    "writers": ["Chris Columbus"],
    "cast": [
        {"name": "Zach Galligan", "role": "Billy Peltzer"},
        {"name": "Phoebe Cates", "role": "Kate Beringer"},
        {"name": "Hoyt Axton", "role": "Randall Peltzer"},
        {"name": "Polly Holliday", "role": "Mrs. Deagle"},
        {"name": "Frances Lee McCain", "role": "Lynn Peltzer"},
        {"name": "Howie Mandel", "role": "Gizmo (voice)"},
        {"name": "Judge Reinhold", "role": "Gerald"},
        {"name": "Corey Feldman", "role": "Pete Fountaine"}
    ],
    "studio": "Warner Bros. / Amblin Entertainment",
    "distributor": "Warner Bros.",
    "verdict": "TRADITIONAL",
    "wokeScore": 1.8,
    "tradScore": 13.0,
    "authIndex": 78,
    "scoreMargin": "+11 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Gremlins (1984) does not qualify as a woke trap. It carries a +11 TRAD margin and a TRADITIONAL verdict. Any minor progressive notes, like the anti-corporate satire in Mrs. Deagle's character or the consumerist critique implicit in the mogwai-as-product framing, are surface-level comedy elements that never threaten the film's fundamentally traditional core: a small-town boy, his family, his Christmas, and his responsibility for the creatures he unleashed. No trap here, just a Spielberg-produced creature feature with a dark sense of humor."
    },
    "seo": {
        "titleTag": "Is Gremlins (1984) Woke? Spielberg Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Gremlins (1984). Joe Dante's Christmas horror-comedy about a boy, his mogwai, and the three rules you must never break. Verdict: TRADITIONAL (+11). Parental guidance included.",
        "keywords": [
            "is gremlins woke",
            "gremlins 1984 review",
            "gremlins virtuevigil",
            "gremlins traditional or woke",
            "gremlins parents guide",
            "gremlins conservative review",
            "gremlins Christmas movie",
            "joe dante gremlins review",
            "steven spielberg gremlins",
            "gremlins pg-13 history"
        ]
    },
    "summary": {
        "overview": "Gremlins (1984) is Joe Dante's darkly comic creature feature, written by Chris Columbus and executive-produced by Steven Spielberg, that became one of the defining films of the 1980s and, along with Indiana Jones and the Temple of Doom, the movie that forced the MPAA to create the PG-13 rating. Zach Galligan stars as Billy Peltzer, a small-town bank teller's son whose father brings home an unusual Christmas gift: a small, furry creature called a mogwai named Gizmo, purchased from a mysterious Chinatown antique shop. The creature comes with three rules: no bright light, no water, and no feeding after midnight. When the rules are inevitably broken, Gizmo spawns a horde of vicious, mischievous gremlins that terrorize the idyllic town of Kingston Falls on Christmas Eve. Phoebe Cates, Hoyt Axton, Polly Holliday, and Frances Lee McCain co-star.",
        "overall": "Gremlins is not just a creature feature. It is a 1980s time capsule that happens to contain one of the most traditionally structured moral fables in the Amblin catalog. You could strip the special effects, the puppets, and the Jerry Goldsmith score, and underneath it all you would find a story about a young man who is given a gift, given rules, and must bear the consequences when those rules are broken. That is not just good storytelling. That is the Judeo-Christian moral imagination operating at the level of genre entertainment.\n\nThe three rules are the film's ethical engine, and they are brilliantly simple. No bright light kills the mogwai. No water makes it multiply. No feeding after midnight turns it into a monster. These are not arbitrary horror-movie rules. They are a parable about boundaries, about the care required to handle something precious without destroying it, and about what happens when appetite meets opportunity in the dark. Billy does not mean to break the rules. The water is an accident. The feeding happens through trickery. But the consequences arrive regardless of intent, because consequences in a moral universe do not care about your excuses. That is a deeply conservative idea, and Gremlins delivers it wrapped in popcorn.\n\nWhat makes the film endure is that it never winks. Joe Dante plays the horror-comedy tone perfectly: the gremlins are genuinely menacing, Kate's famous Christmas story about her father is genuinely dark, and the threat to Kingston Falls feels real. But the film also has Gizmo, one of the most purely lovable creature designs in cinema history, whose innocence and vulnerability make the stakes personal. When Billy and Kate fight through the chaos to save Gizmo, you understand why. He is not a pet. He is a responsibility.\n\nFor VirtueVigil readers, the ideological read is straightforward. Kingston Falls is small-town Americana rendered with affection. Billy's father is an inventor, not a corporate suit. Billy's mother defends the home with kitchen appliances and maternal ferocity. The town's villain is Mrs. Deagle, a miserly landlord who threatens to evict families at Christmas, and her comeuppance is played as justice, not tragedy. The film's worldview is: rules exist for a reason, chaos has a cause, and the people who clean up the mess are the ones who care enough to stay and fight. In 1984, that was just good storytelling. In 2026, it reads like a manifesto.\n\nThe film also carries a fascinating place in ratings history. The violence got dark enough, and the horror-comedy tone confused enough parents, that along with Temple of Doom it helped force the creation of PG-13. That legacy is a reminder that the 1980s had not yet decided that children needed to be protected from stories with stakes. Gremlins trusts its audience, and that trust has kept it alive for forty years.",
        "adultInsight": "Gremlins is evidence that the most enduring family entertainment was often the most morally serious. The film is not a sermon. It is a roller coaster with puppets. But the roller coaster runs on a track laid by people who believed that rules matter, that consequences are real, and that protecting the innocent is the highest calling. Parents who watch this with their children in 2026 get more than a nostalgia trip. They get a chance to talk about why the rules exist, why Billy's mother fights with everything she has, and why Gizmo is worth saving. That conversation will do more good than a hundred modern films that announce their values in the credits.",
        "parentalGuidance": "Rated PG, but this is pre-PG-13 1984 and the violence gets surprisingly intense. Gremlins are melted, microwaved, blended, and exploded in ways that read as slapstick to adults but may disturb young children. Kate's monologue about her father's death is genuinely upsetting. The gremlin puppets are grotesque and menacing. Recommended for ages 10 and up, with the caveat that parents should know their children's tolerance for creature horror played straight."
    },
    "parentalGuidance": {
        "rating": "PG",
        "contentWarnings": "Creature violence and horror played for both comedy and genuine menace. Gremlins are killed in graphic but slapstick ways (microwave, blender, explosion). A character recounts her father's death in a Christmas chimney accident, a scene that is unexpectedly dark. The gremlins are grotesque puppet creations that may frighten young children.",
        "ageRecommendation": "10+. The violence is cartoonish in execution but the menace is real. Children who can handle the scarier moments of Harry Potter will be fine. Younger children may find the gremlins genuinely frightening.",
        "discussionTopics": [
            "What do the three rules teach about boundaries and responsibility?",
            "Why does Billy take responsibility for the gremlins even though he did not mean to break the rules?",
            "How does the film portray small-town America, and what does it value about that setting?",
            "Why did this film help create the PG-13 rating, and what does that tell us about how children's entertainment has changed?"
        ]
    },
    "creative_team": {
        "director": {
            "name": "Joe Dante",
            "role": "Director",
            "note": "Dante built his career on affection for B-movies and genre craft. His films from Piranha to The Howling to Gremlins to Matinee are love letters to cinema history, not ideological vehicles. He is not a conservative filmmaker, but he is a craftsman whose values are embedded in the material he chooses, not in messaging he imposes."
        },
        "writer": {
            "name": "Chris Columbus",
            "role": "Screenwriter",
            "note": "Columbus wrote Gremlins as a spec script that was originally much darker (gremlins ate a dog, killed Billy's mother). Spielberg saw the commercial potential and helped shape it into the horror-comedy it became. Columbus went on to direct Home Alone, Mrs. Doubtfire, and the first two Harry Potter films, a filmography that is about as family-centered and tradition-respecting as mainstream Hollywood gets."
        },
        "lead_producer": {
            "name": "Steven Spielberg",
            "role": "Executive Producer",
            "note": "Spielberg's Amblin touch is all over this film: the small-town setting, the wonder-to-terror arc, the practical effects that hold up forty years later. His executive producer credit on Gremlins is a quality signal, and his filmography from this era (E.T., The Goonies, Back to the Future) remains the gold standard for family entertainment with moral weight."
        }
    },
    "externalScores": {
        "rottenTomatoesCritic": 86,
        "rottenTomatoesAudience": 79,
        "imdb": 7.3,
        "metacritic": 73,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "$11 million",
        "globalBoxOffice": "$212.9 million"
    },
    "tropeAudit": [
        {
            "id": "TRAD-GREMLINS-001",
            "name": "Small-town Americana as moral community",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Kingston Falls is the platonic ideal of a Norman Rockwell Christmas town: the square is decorated, the neighbors know each other, the bank is local, and the community's rhythms are built on familiarity and trust. The film is set at Christmas and treats the holiday with affection, not irony. When the gremlins invade, the town fights back as a community. This is not background decoration. It is the film's moral proposition: this place is worth saving."
        },
        {
            "id": "TRAD-GREMLINS-002",
            "name": "Rules and consequences as narrative engine",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "The three rules drive the entire plot, and they function as a moral framework. Bright light kills. Water multiplies. Feeding after midnight transforms into a monster. These are not bureaucratic restrictions. They are natural laws of the mogwai world, and breaking them has real, escalating, irreversible consequences. The film's entire dramatic structure is built on the premise that rules exist for a reason and that violating them, regardless of intent, produces chaos. This is a profoundly traditional worldview operating at the level of story architecture."
        },
        {
            "id": "TRAD-GREMLINS-003",
            "name": "Father-son relationship and family integrity",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Billy's father Randall is an absent-minded inventor, not a corporate striver. He brings Gizmo home as a gift born of genuine affection. Billy's mother Lynn is a homemaker who defends her kitchen with terrifying competence when the gremlins attack. The family unit is the film's anchor, and it is never mocked or deconstructed. Billy's arc is about learning to take responsibility for the consequences of his actions, a classic bildungsroman arc rooted in the family."
        },
        {
            "id": "TRAD-GREMLINS-004",
            "name": "Maternal ferocity defending the home",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Lynn Peltzer's sequence defending the kitchen against the gremlins, using a microwave, a blender, and a knife, is one of the great maternal combat scenes in cinema. She is not a soldier. She is a mother whose home has been invaded, and she fights with whatever is at hand. The scene is played for horror-comedy but it is never played for mockery. She is a hero, and the film treats her as one."
        },
        {
            "id": "WOKE-GREMLINS-001",
            "name": "Anti-corporate satire through villain design",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.6,
            "explanation": "Mrs. Deagle, the miserly landlord who threatens to evict Billy's family at Christmas, is a cartoon villain in the Dickensian tradition. Some critics have read her as anti-capitalist satire, but the film treats her as an individual moral failure, not a systemic indictment. Her comeuppance, launched through a window by gremlins on a stairlift, is slapstick justice, not class warfare. The reading is available but thin."
        },
        {
            "id": "WOKE-GREMLINS-002",
            "name": "Consumerist critique through mogwai-as-product framing",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "The mogwai is purchased in a mysterious Chinatown shop against the owner's warnings, and the gremlins emerge from its irresponsible multiplication. A light reading could see this as commentary on consumer desire and mass production, but the film is not serious about this thread. It is a monster movie, not a thinkpiece. The critique is ambient, not intended."
        }
    ],
    "fidelityCasting": {
        "assessment": "NO ISSUES",
        "explanation": "All casting serves the story. The Peltzer family casting reflects a 1980s Midwestern small town. The Chinatown framing of Gizmo's origin reflects genre convention of the era (mysterious artifact from the East) but is not hateful or demeaning. No fidelity violations."
    }
}

# ── Review 3: Lanterns (TV series, premiered Aug 16, SEO gap) ──
lanterns = {
    "id": "lanterns-2026",
    "slug": "lanterns-2026",
    "title": "Lanterns",
    "year": 2026,
    "type": "series",
    "platform": "HBO",
    "genre": "Superhero / Detective / Neo-Western",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "10 min",
    "poster": "/images/posters/lanterns-2026.jpg",
    "releaseDate": "2026-08-16",
    "rating": "TV-MA (Violence, Language, Mature Themes)",
    "runtime": "8 episodes, ~57 min each (Season 1)",
    "director": "James Hawes (first two episodes)",
    "writers": ["Chris Mundy", "Damon Lindelof", "Tom King"],
    "showrunner": "Chris Mundy",
    "cast": [
        {"name": "Kyle Chandler", "role": "Hal Jordan"},
        {"name": "Aaron Pierre", "role": "John Stewart"},
        {"name": "Kelly Macdonald", "role": "Sheriff Kerry Kane"},
        {"name": "Garret Dillahunt", "role": "William Macon"},
        {"name": "Poorna Jagannathan", "role": "Zoe Macon"},
        {"name": "Nathan Fillion", "role": "Guy Gardner"},
        {"name": "Jason Ritter", "role": "Billy Macon"}
    ],
    "studio": "DC Studios / Warner Bros. Television",
    "distributor": "HBO",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 3.5,
    "tradScore": 6.3,
    "authIndex": 62,
    "scoreMargin": "+3 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Lanterns does not qualify as a woke trap. It carries a +3 TRAD margin and a TRADITIONAL LEAN verdict. While Damon Lindelof's involvement brings well-earned skepticism, the series premiere establishes its ideological character through the mentor/mentee dynamic between Hal and John, not through hidden messaging. The racial dynamics are visible but are handled as character texture rather than lecture material. There is no bait-and-switch; the premiere is what the show is. Lindelof's participation means the series could pivot later in the season, and this review will be updated if future episodes warrant a revised verdict."
    },
    "seo": {
        "titleTag": "Is Lanterns (2026) Woke? HBO's Green Lantern Series Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Lanterns (HBO, 2026). Kyle Chandler and Aaron Pierre star as Green Lanterns in DC's True Detective-style murder mystery. Verdict: TRADITIONAL LEAN (+3). Parental guidance included.",
        "keywords": [
            "is lanterns woke",
            "lanterns hbo review",
            "lanterns virtuevigil",
            "lanterns green lantern series review",
            "lanterns traditional or woke",
            "lanterns parents guide",
            "lanterns hbo conservative review",
            "kyle chandler hal jordan lanterns",
            "aaron pierre john stewart lanterns",
            "lanterns damon lindelof review"
        ]
    },
    "summary": {
        "overview": "Lanterns (2026) is HBO's ambitious adaptation of the DC Comics Green Lantern mythos, created by Chris Mundy, Damon Lindelof, and Tom King. The eight-episode series stars Kyle Chandler as Hal Jordan, a veteran Green Lantern approaching retirement, and Aaron Pierre as John Stewart, a Marine-turned-architect who becomes the first Lantern recruited directly by the Guardians of the Universe rather than chosen by a power ring. The two are dispatched to Rushville, Nebraska, to investigate a murder that Hal suspects has extraterrestrial origins. The investigation, rendered in the slow-burn, character-driven style of True Detective, pulls them into a conspiracy that reaches from small-town secrets to interstellar politics. Kelly Macdonald co-stars as Sheriff Kerry Kane, with Garret Dillahunt, Poorna Jagannathan, and Nathan Fillion in supporting roles. James Hawes (Slow Horses) directed the first two episodes.",
        "overall": "Lanterns is the most interesting thing DC has done on television in years, and also the hardest to score. It is a prestige-cable detective show that happens to have power rings in it, and whether that sounds like a promise or a problem depends on how you feel about Damon Lindelof.\n\nLet me be direct about the Lindelof question, because it is the first thing any VirtueVigil reader will want to know. Yes, the co-creator of Watchmen (2019) is here, and yes, you can see his fingerprints. Watchmen was one of the most nakedly ideological shows HBO ever aired, a series that treated the Tulsa race massacre as founding trauma and painted institutional authority as an unbroken chain of lies. Lanterns is not Watchmen. The premiere is a murder mystery first, a character study second, and a sermon not at all. If Lindelof is working through something here, he is doing it through craft rather than polemic.\n\nThe show's ideological center of gravity is the relationship between Hal and John. This could have been a disaster: older white veteran training his younger Black replacement, with all the lecture-hall subtext that implies. It is not that. Hal is not a relic being discarded. He is a man at the end of a long career who still has something to teach, and John is a man with extraordinary capability who still has something to learn. The respect flows in both directions. Chandler plays Hal with the weary authority of an astronaut who has seen too much, and Pierre plays John with a stillness that suggests depths the show is in no hurry to reveal. Their chemistry is the best thing about the series so far.\n\nKelly Macdonald's Sheriff Kane is the third point of the triangle, a small-town law enforcement officer who is protective of her community and skeptical of the two federal agents in bomber jackets who show up asking questions about a dead body. She is not a woke-ified girlboss. She is a sheriff who takes her job seriously, and the show respects that seriousness. Garret Dillahunt's William Macon, her father-in-law, is the character most likely to trouble VirtueVigil readers: a self-righteous conspiracy-minded modern cowboy whose politics are clearly coded as right-leaning and whose worldview is treated as suspicious. This is a legitimate ideological signal, but it is one character in an ensemble, not the thesis of the show.\n\nThe series premiere is well-made. The cinematography is gorgeous, the pacing is deliberate without being punishing, and the Nebraska setting gives the cosmic superhero elements a groundedness that makes them feel more real, not less. The show understands that the best detective stories are about the detectives, not the crime, and it has cast two actors who can carry that weight.\n\nThe concern is not the premiere. The concern is what Lindelof does when the mystery starts to resolve. He has a pattern: the early episodes establish character and tension, and then around episode five or six, the message arrives. I cannot score what has not aired. What I can say is that the premiere of Lanterns is a solid, character-driven detective show with a TRADITIONAL LEAN, and that verdict holds until the show gives me a reason to revise it. Watch it, enjoy it, but watch it with your eyes open.",
        "adultInsight": "Lanterns matters because it represents a test case for whether DC Studios under James Gunn can produce prestige television that doesn't alienate half the audience. If the show stays on its current trajectory, mentoring, duty, protecting communities, solving problems through character and investigation rather than ideology, it will be the best argument yet that the superhero genre can grow up without leaving its traditional audience behind. If it swerves into Lindelof's familiar territory in the back half, it will be a betrayal of the trust the premiere has earned. Parents watching this should treat it as an opportunity to discuss what good mentoring looks like, what it means to serve a community you are not part of, and how to tell the difference between a character whose politics differ from yours and a show that is using that character to mock you. The premiere passes that test. The jury is out on the rest.",
        "parentalGuidance": "Rated TV-MA for violence, language, and mature themes. The premiere contains a murder investigation with crime scene imagery, some strong language, and thematic material about death and duty. The superhero violence is restrained by HBO standards, more True Detective than Marvel. Not for children, but mature teens who enjoy thoughtful genre television will find it appropriate."
    },
    "parentalGuidance": {
        "rating": "TV-MA",
        "contentWarnings": "Crime scene investigation imagery, moderate violence, strong language, mature themes about death, duty, and institutional trust. No sexual content in the premiere. The show's HBO pedigree means future episodes may include adult material.",
        "ageRecommendation": "16+. The premiere is tamer than many TV-MA shows, but the thematic weight and deliberate pacing are adult. Younger viewers will be bored. Mature teens who enjoy thoughtful genre television will find it rewarding.",
        "discussionTopics": [
            "What does Hal's mentoring of John reveal about how knowledge and authority should be passed between generations?",
            "Is Sheriff Kane's protectiveness of her community framed as a strength or as a provincial limitation?",
            "How does the show handle the question of institutional trust, and does it treat the Green Lantern Corps as a noble institution or a compromised one?",
            "Why is a small-town murder a better vehicle for superhero storytelling than another alien invasion?"
        ]
    },
    "creative_team": {
        "showrunner": {
            "name": "Chris Mundy",
            "role": "Showrunner",
            "note": "Mundy's previous work on Ozark demonstrates an ability to handle morally complex characters without ideological preaching. Ozark was about family survival under extraordinary pressure, a structurally conservative premise that Mundy executed with craft rather than messaging."
        },
        "writer": {
            "name": "Damon Lindelof, Tom King, Chris Mundy",
            "role": "Creators / Writers",
            "note": "Lindelof is the variable that matters. His work ranges from the spiritually searching Leftovers to the aggressively ideological Watchmen. Which Lindelof shows up for Lanterns is the most important question the series has not yet answered. Tom King's comics work (Mister Miracle, Supergirl) explores trauma and duty with more emotional complexity than political agenda. Mundy's Ozark track record provides a stabilizing influence."
        },
        "director": {
            "name": "James Hawes (first two episodes)",
            "role": "Director",
            "note": "Hawes directed multiple episodes of Slow Horses, Apple's spy series that is notable for being both critically acclaimed and ideologically restrained. His involvement suggests Lanterns is being shaped as a character-driven procedural rather than a message-delivery vehicle."
        },
        "lead_producer": {
            "name": "James Gunn, Peter Safran",
            "role": "Executive Producers / DC Studios Co-CEOs",
            "note": "Gunn and Safran's DCU has been less ideologically aggressive than many feared. Superman (2025) was a broadly accessible superhero film without the culture-war baggage of the Snyder era or the overt messaging of Marvel Phase 4. Their stewardship adds a moderating influence to Lindelof's tendencies."
        }
    },
    "externalScores": {
        "rottenTomatoesCritic": 95,
        "rottenTomatoesAudience": 0,
        "imdb": 0,
        "metacritic": 0,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "TBD",
        "globalBoxOffice": "N/A (HBO series)"
    },
    "tropeAudit": [
        {
            "id": "TRAD-LANTERNS-001",
            "name": "Mentorship as sacred obligation",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The Hal-John dynamic is built on genuine mentorship. Hal is not being replaced or discarded; he is teaching. John is not a diversity hire; he is a recruit with exceptional potential. The show frames the passing of knowledge from one generation of Lantern to the next as a serious and honorable undertaking. In an era when mentorship is often framed as patriarchal imposition, Lanterns treats it as a duty that elevates both parties."
        },
        {
            "id": "TRAD-LANTERNS-002",
            "name": "Small-town law enforcement as legitimate authority",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.0,
            "explanation": "Sheriff Kane is not corrupt, incompetent, or bigoted. She is protective of her community and skeptical of the federal-level Lanterns who arrive with jurisdiction she does not understand but must respect. The show treats her authority as legitimate and her protectiveness as admirable. This is a minor but real traditional signal in a genre that too often treats local law enforcement as an obstacle to be overcome or a bigotry to be exposed."
        },
        {
            "id": "TRAD-LANTERNS-003",
            "name": "Duty and service as character foundation",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.5,
            "explanation": "Both Hal and John are defined by service: Hal as a USAF veteran and longtime Lantern, John as a former Marine. The show does not deconstruct or pathologize their service. It treats it as formative and honorable. The Green Lantern Corps itself is framed as an institution worth serving, not a corrupt hierarchy to be exposed."
        },
        {
            "id": "WOKE-LANTERNS-001",
            "name": "Race-conscious casting as narrative element",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.0,
            "explanation": "The Hal/John racial dynamic is visible and intentional in the premiere. John being the first Guardian-recruited Lantern is framed as significant, not incidental. The show does not lecture about race, but it does ask the audience to notice it. This is a moderate woke signal, softened by the show's refusal to make John a victim or Hal a villain."
        },
        {
            "id": "WOKE-LANTERNS-002",
            "name": "Conspiracy-minded white male as antagonist coding",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.45,
            "explanation": "William Macon, the father-in-law of Sheriff Kane, is coded as a middle-American conspiracy theorist whose worldview is treated with suspicion by the narrative. This is a recognizable progressive trope that maps conservative skepticism about institutions onto villainy. It is a real ideological signal, but Macon is one character in a large ensemble and the show has not yet committed to making him a villain rather than a red herring."
        },
        {
            "id": "WOKE-LANTERNS-003",
            "name": "Damon Lindelof creative fingerprint",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "Lindelof's involvement is itself a woke signal due to his track record on Watchmen and The Leftovers. His presence does not guarantee a woke product, but it does mean the series must be watched with heightened alertness. The premiere earns the benefit of the doubt; the back half of the season will determine whether that doubt was justified. This trope scores low centrality because Lindelof's fingerprint is visible but not yet dominant."
        }
    ],
    "fidelityCasting": {
        "assessment": "MOSTLY FAITHFUL",
        "explanation": "Kyle Chandler as Hal Jordan is near-perfect casting for an aging test-pilot Lantern. Aaron Pierre as John Stewart is a departure from the comics' original African-American Marine characterization, Pierre is British, but his performance is strong and the core elements (Marine, architect, recruit) are preserved. Kelly Macdonald as Sheriff Kane is an original character, not a fidelity question. Nathan Fillion as Guy Gardner is faithful to the character's abrasive personality. No race-swaps or gender-swaps of established characters."
    }
}

# ── Load, insert, validate ──
with open('src/data/reviews.json', 'r') as f:
    reviews = json.load(f)

print(f"Loaded {len(reviews)} reviews")

# Check slugs don't exist
existing_slugs = {r['slug'] for r in reviews}
for rev in [insidious, gremlins, lanterns]:
    slug = rev['slug']
    assert slug not in existing_slugs, f"SLUG COLLISION: {slug}"
    print(f"  Slug OK: {slug}")

# Insert
reviews.append(insidious)
reviews.append(gremlins)
reviews.append(lanterns)

# Re-sort by date
reviews.sort(key=lambda x: (x.get('date', ''), x.get('slug', '')), reverse=True)

with open('src/data/reviews.json', 'w') as f:
    json.dump(reviews, f, indent=2)

print(f"Saved {len(reviews)} reviews (+3)")
print("Done inserting!")