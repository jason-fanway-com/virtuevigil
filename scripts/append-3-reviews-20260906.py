#!/usr/bin/env python3
"""Append 3 reviews: Onslaught (2026), Airplane! (1980), The Sopranos (1999)"""
import json, sys
from datetime import datetime

with open("src/data/reviews.json", "r") as f:
    reviews = json.load(f)

existing_slugs = {r["slug"] for r in reviews}
print(f"Current count: {len(reviews)}")

# ============================================================
# REVIEW 1: Onslaught (2026)
# ============================================================
onslaught = {
    "id": "onslaught-2026",
    "slug": "onslaught-2026",
    "title": "Onslaught",
    "year": 2026,
    "type": "film",
    "platform": "Theaters",
    "genre": "Action Horror, Thriller, Sci-Fi",
    "date": "2026-09-06",
    "datePublished": "2026-09-06",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/onslaught-2026.jpg",
    "releaseDate": "2026-09-04",
    "rating": "R (Strong Bloody Violence, Gore, Language Throughout)",
    "runtime": "92 minutes",
    "director": "Adam Wingard",
    "writers": ["Simon Barrett"],
    "cast": [
        {"name": "Adria Arjona", "role": "Celeste"},
        {"name": "Dan Stevens", "role": "Dr. Hans Kammler"},
        {"name": "Rebecca Hall", "role": "Hanna Kammler"},
        {"name": "Reginald VelJohnson", "role": "Josiah"},
        {"name": "Michael Biehn", "role": "Baylor"},
        {"name": "Alex Pereira", "role": "The Butcher"},
        {"name": "Drew Starkey", "role": "Cyrus"},
        {"name": "Eric Wareheim", "role": "Kovacks"},
        {"name": "Blake Kennedy", "role": "Daisy"}
    ],
    "studio": "A24, Lyrical Media, Ryder Picture Company",
    "distributor": "A24",
    "verdict": "TRADITIONAL",
    "wokeScore": 4.59,
    "tradScore": 18.48,
    "authIndex": 80,
    "scoreMargin": "+14 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "No woke trap. Onslaught is a straightforward action-horror splatterfest from the first minute to the last. An army sniper protects her daughter and her trailer-park community from escaped Nazi-engineered super soldiers. There is no ideological bait and switch, no hidden political messaging that surfaces past the midpoint. The film's lone political nod is entirely external: director Adam Wingard compared the super soldiers to ICE in an Entertainment Weekly interview, but nothing in the actual movie supports that reading. On screen, the Kammlers are Nazi mad scientists and their creations are mindless killing machines. The politics stay on the press tour."
    },
    "seo": {
        "titleTag": "Is Onslaught (2026) Woke? A24 Action-Horror VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Onslaught (2026), Adam Wingard's A24 action-horror splatterfest starring Adria Arjona as an army sniper protecting her daughter from super soldiers. Verdict: TRADITIONAL (+14 TRAD). Parental guidance included.",
        "keywords": "is onslaught woke, onslaught 2026 review, onslaught virtuevigil, onslaught adam wingard, onslaught a24, onslaught parents guide, onslaught traditional or woke, adria arjona onslaught"
    },
    "externalScores": {
        "imdb": "6.1/10",
        "rottenTomatoes": "54%",
        "metacritic": "57"
    },
    "creative_team": {
        "director": {
            "name": "Adam Wingard",
            "ideology": "MODERATE (Genre Craftsman)",
            "profile": "Adam Wingard built his career on lean, stylish genre films: You're Next, The Guest, and the Godzilla x Kong monster-verse entries. His politics register as apathetic rather than activist. He told Entertainment Weekly that Onslaught's super soldiers are 'a metaphor for ICE,' but this reading appears nowhere in the finished film, which plays as a straight action-horror thrill ride. Wingard is a technician first and an ideologue a distant second: his films serve the genre, not a message."
        },
        "writer": {
            "name": "Simon Barrett",
            "profile": "Barrett has been Wingard's writing partner since You're Next (2011). His scripts favor tight, contained premises with practical effects and dark humor. Onslaught follows that template: one location (a trailer park), one night, one mom with a sniper rifle against an army of monsters. Barrett writes lean, functional screenplays that prioritize momentum over meaning. Nothing in the Onslaught script signals a political agenda."
        },
        "lead_producer": {
            "name": "Aaron Ryder, Andrew Swett",
            "company": "Ryder Picture Company / Lyrical Media"
        },
        "composer": {"name": "Matt Pusti"},
        "top_cast": [
            {"name": "Adria Arjona", "role": "Celeste"},
            {"name": "Dan Stevens", "role": "Dr. Hans Kammler"},
            {"name": "Rebecca Hall", "role": "Hanna Kammler"}
        ],
        "producers": ["Aaron Ryder", "Andrew Swett", "Adam Wingard", "Jeremy Platt", "Alexander Black", "Simon Barrett"],
        "full_cast": [
            {"name": "Adria Arjona", "role": "Celeste"},
            {"name": "Dan Stevens", "role": "Dr. Hans Kammler"},
            {"name": "Rebecca Hall", "role": "Hanna Kammler"},
            {"name": "Reginald VelJohnson", "role": "Josiah"},
            {"name": "Michael Biehn", "role": "Baylor"},
            {"name": "Alex Pereira", "role": "The Butcher"},
            {"name": "Drew Starkey", "role": "Cyrus"},
            {"name": "Eric Wareheim", "role": "Kovacks"},
            {"name": "Blake Kennedy", "role": "Daisy"},
            {"name": "Maurice Greene", "role": "Teddy"},
            {"name": "Jacob Scipio", "role": "Griffin"}
        ]
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "Defense of the Innocent (TRADITIONAL-045)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "Celeste's entire character is built around protecting her daughter Daisy. Every violent act she commits is in defense of a child who cannot defend herself. This is maternal protection as primal motivation, not girlboss posturing. When Josiah (Reginald VelJohnson) joins the fight, the film becomes a story of adults sacrificing themselves so that a child can survive. This is the most traditional narrative architecture available."
        },
        {
            "category": "Traditional",
            "trope": "Survival Competence and Self-Reliance",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 4.80,
            "description": "Celeste is competent because she trained, not because the script handed her superpowers. As an army sniper, her skills are earned and explicable. The film respects the logic of: she can do this because she prepared for this. The trailer-park community bands together using improvised weapons and local knowledge rather than waiting for outside rescue. Self-reliance is the organizing principle."
        },
        {
            "category": "Traditional",
            "trope": "Objective Good vs. Evil (TRADITIONAL-039)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 3.84,
            "description": "The Kammlers are Nazi mad scientists. Their creations are mindless killing machines with no redeeming qualities. There is no moral ambiguity, no 'the real monster is the military-industrial complex' pivot. The bad guys are Nazis who made monsters. The good guy is a mom with a rifle. The moral clarity is refreshingly pre-modern."
        },
        {
            "category": "Traditional",
            "trope": "Community Defense and Loyalty",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.52,
            "description": "The trailer park functions as a community. Josiah, the older veteran, doesn't hesitate to arm himself and stand beside Celeste. Baylor (Michael Biehn) contributes what he can. These are people who look out for each other because that's what neighbors do, not because a government program told them to. The film's vision of community is organic and voluntary."
        },
        {
            "category": "Traditional",
            "trope": "The Redemptive Arcs (TRADITIONAL-027)",
            "severity": 3,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 1.04,
            "description": "Celeste is introduced as a PTSD-suffering veteran estranged from normal life. The film gives her a quiet redemption arc through action: by doing what she was trained to do in defense of her family, she reclaims her sense of purpose. It's handled lightly but it's there."
        },
        {
            "category": "Woke",
            "trope": "The Girl Boss (WOKE-003)",
            "severity": 2,
            "authenticity": "Medium",
            "centrality": "Low",
            "weightedScore": 1.40,
            "description": "A female action lead in a genre historically dominated by men. But the film sidesteps the worst impulses of this trope: Celeste is not hyper-masculine, she does not dominate or humiliate men, and her competence is rooted in military training, not magical superiority. She's a mother, not a gender-studies thesis. The film never pauses to remind you that a woman is doing this."
        },
        {
            "category": "Minor Woke",
            "trope": "ICE Metaphor (External Commentary)",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 1.00,
            "description": "Director Adam Wingard told Entertainment Weekly that the super soldiers are 'a metaphor for ICE.' This is entirely external to the text. Nothing in the finished film supports this reading. The Kammlers are Nazi scientists. The Butcher and his fellow soldiers are genetically engineered killing machines. If Wingard intended a political allegory, it did not survive the editing room. We dock a minor point for the intent but note that the finished product is clean."
        }
    ],
    "summary": {
        "overall": "Adam Wingard's Onslaught is a lean, mean, 92-minute action-horror movie that knows exactly what it is and refuses to apologize for it. An army sniper (Adria Arjona, commanding and human) protects her young daughter from escaped super soldiers in a New Mexico trailer park, and that premise delivers exactly the gore-soaked, practical-effects showcase you'd hope for. Wingard and writer Simon Barrett return to the spirit of The Guest: tight genre filmmaking with real craft and no pretension. The moral universe is clear. Nazis made monsters. A mom with a sniper rifle stops them. The community bands together. The innocent are defended. That Onslaught manages this without a single lecture about gender, privilege, or structural anything is its quietest triumph. It's a movie that trusts you to notice the woman is the hero without needing to explain why that's important.",
        "traditionaStrengths": "Maternal protection is the film's moral engine. Celeste's violence is never glamorized; it's instrumental, measured, and entirely in service of her child's survival. The trailer-park community functions as an organic mutual-aid network: Josiah (a warm, welcome Reginald VelJohnson) arms himself without a second thought, Baylor contributes what he can, and nobody waits for institutional rescue. The villains are Nazi scientists with no redeeming qualities. There is no 'the real monster was the military-industrial complex' twist. Good and evil wear clearly labeled jerseys.",
        "wokeElements": "The score reflects one structural element and one external factor. Structurally, Celeste is a female action lead, and while the film handles this responsibly, it activates the Girl Boss trope at low intensity. More concerning is director Adam Wingard's press-tour claim that the super soldiers are 'a metaphor for ICE.' This reading has no textual support whatsoever. The Kammlers are literal Nazis who created literal monsters in a literal lab. If Wingard intended a political alleory, he buried it so deep that it is invisible to any viewer who didn't read the Entertainment Weekly interview. We dock a minor point for authorial intent but judge the finished work on its own terms.",
        "parentaGuidance": "Onslaught earns its R rating honestly. The violence is graphic, practical, and frequent. Limbs are torn. Heads explode. The body count is high and the gore is wet. A young child (approximately 8) is in constant peril, which is the film's emotional engine but may be intense for sensitive viewers. There is strong language throughout. No sexual content. No nudity. The villains are Nazi-adjacent, which may require context for younger teens. Recommended for: adults and older teens who can handle splater-horror violence. The moral clarity, maternal protection theme, and community loyalty make it a surprisingly wholesome choice within its genre, but the gore is the point."
    }
}

# ============================================================
# REVIEW 2: Airplane! (1980)
# ============================================================
airplane = {
    "id": "airplane-1980",
    "slug": "airplane-1980",
    "title": "Airplane!",
    "year": 1980,
    "type": "film",
    "platorm": "Paramount+ / Digital Rental",
    "gene": "Comedy, Parody",
    "date": "2026-09-06",
    "datePublised": "2026-09-06",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min",
    "poster": "/images/posters/airplane-1980.jpg",
    "releaseDate": "1980-07-02",
    "rating": "PG (Comedic Violence, Suggestive Humor, Brief Nudity)",
    "runtime": "87 minutes",
    "director": "Jim Abrahams, David Zucker, Jerry Zucker",
    "writers": ["Jim Abrahams", "David Zucker", "Jerry Zucker"],
    "cast": [
        {"name": "Robert Hays", "role": "Ted Striker"},
        {"name": "Julie Hagerty", "role": "Elaine Dickinson"},
        {"name": "Leslie Nielsen", "role": "Dr. Rumack"},
        {"name": "Robert Stack", "role": "Captain Rex Kramer"},
        {"name": "Lloyd Bridges", "role": "Steve McCroskey"},
        {"name": "Peter Graves", "role": "Captain Clarence Oveur"},
        {"name": "Kareem Abdul-Jabbar", "role": "Roger Murdock"},
        {"name": "Lorna Patterson", "role": "Randy"}
    ],
    "studio": "Paramount Pictures, Howard W. Koch Productions",
    "distributor": "Paramount Pictures",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 2.16,
    "tradScore": 24.36,
    "authIndex": 91,
    "scoreMargin": "+22 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_tap": False,
        "pct_runtime": 0,
        "explanation": "No woke trap. Airplane! is a joke machine from 1980 that predates the modern ideological framing of comedy entirely. The film's only concern is landing the next gag. There is no political messaging hidden anywhere in the runtime, and the idea of a 'bait and switch' in a ZAZ parody is category error. This is comedy as pure craft."
    },
    "seo": {
        "titleTag": "Is Airplane! (1980) Woke? Classic ZAZ Parody VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Airplane! (1980), the ZAZ comedy classic starring Robert Hays, Julie Hagerty, and Leslie Nielsen. A traumatized pilot must land a passenger jet when food poisoning strikes the crew. Verdict: STRONGLY TRADITIONAL (+22 TRAD).",
        "keywords": "is airplane woke, airplane 1980 review, airplane virtuevigil, airplane zumor comedy, airplane parents guide, leslie nielsen airplane, airplane traditional or woke"
    },
    "externalScores": {
        "imdb": "7.7/10",
        "rottenTmatoes": "97%",
        "metacritic": "78"
    },
    "creative_team": {
        "director": {
            "name": "Jim Abrahams, David Zucker, Jerry Zucker",
            "ideology": "NONE (Comedy Craftsmen, Pre-Modern)",
            "profile": "The Zucker-Abrahams-Zucker (ZAZ) team created Airplane! as their feature debut after years of writing sketch comedy. Their politics, to the extent they had any, were libertarian-adjacent and entirely subordinated to the joke. ZAZ did not make message movies. They made comedy machines where every frame contains a gag, a setup, or a payoff. Attempting to read Airplane! through an ideological lens is a category error: the film operates in a pre-woke universe where the only sin is not being funny."
        },
        "writer": {
            "name": "Jim Abrahams, David Zucker, Jerry Zucker",
            "profile": "The trio wrote Airplane! by literally watching Zero Hour! (1957) and transcribing its dialogue, then layering jokes on top of the earnest disaster-movie template. They cast dramatic actors (Leslie Nielsen, Robert Stack, Lloyd Bridges, Peter Graves) and directed them to play every line completely straight. The result is a film where the comedy comes from the collision of serious performance and absurd material, a technique that required discipline, not ideology."
        },
        "lead_producer": {
            "name": "Jon Davison",
            "company": "Paramount Pictures"
        },
        "composer": {"name": "Elmer Bernstein"},
        "top_cast": [
            {"name": "Robert Hays", "role": "Ted Striker"},
            {"name": "Julie Hagerty", "role": "Elaine Dickinson"},
            {"name": "Leslie Nielsen", "role": "Dr. Rumack"}
        ],
        "producers": ["Jon Davison", "Howard W. Koch"],
        "full_cast": [
            {"name": "Robert Hays", "role": "Ted Striker"},
            {"name": "Julie Hagerty", "role": "Elaine Dickinson"},
            {"name": "Leslie Nielsen", "role": "Dr. Rumack"},
            {"name": "Robert Stack", "role": "Captain Rex Kramer"},
            {"name": "Lloyd Bridges", "role": "Steve McCroskey"},
            {"name": "Peter Graves", "role": "Captain Clarence Oveur"},
            {"name": "Kareem Abdul-Jabbar", "role": "Roger Murdock"},
            {"name": "Lorna Patterson", "role": "Randy"},
            {"name": "Stephen Stucker", "role": "Johnny"},
            {"name": "Jonathan Banks", "role": "Gunderson"}
        ]
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "The Redemptive Arcs (TRADITIONAL-027)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "Ted Striker's arc is the film's emotional spine. A traumatized war veteran who lost his squadron and his confidence, Striker must overcome his fear of flying to save the woman he loves and a plane full of passengers. The film plays this completely straight. Striker's PTSD is never mocked. His redemption through courage and competence is the engine that drives the plot. For all its absurdist gags, Airplane! treats Striker's heroism with genuine respect."
        },
        {
            "category": "Traditional",
            "trope": "The Self-Sacrificing Hero (TRADITIONAL-026)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "Striker gets on a plane despite a pathological fear of flying because Elaine is on it. He takes the controls when the crew is incapacitated. He lands the plane in a storm with no formal training on that aircraft type. Every narrative beat is a person risking everything for others. The film earns the emotional payoff of the landing because it never undercuts Striker's courage for a cheap laugh."
        },
        {
            "category": "Traditional",
            "trope": "Merit-Based Achievement",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.52,
            "description": "Striker saves the day because he was a fighter pilot who trained for exactly this kind of crisis. His competence is earned, not gifted. The film respects the logic that people who work hard and train hard are the ones you want in an emergency. No one questions why the man with flight experience should be the one flying the plane."
        },
        {
            "category": "Traditional",
            "trope": "Sanctity of Marriage (TRADITIONAL-034)",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.52,
            "description": "The romantic subplot between Striker and Elaine is played entirely straight. He lost her because he lost himself after the war. He wins her back by becoming the man he used to be. The film treats their relationship as something worth fighting for, not something to be deconstructed or mocked. When Elaine says 'I love you' over the radio as Striker lands the plane, it's the emotional climax of the film, and it lands."
        },
        {
            "category": "Traditional",
            "trope": "The Honest Worker (TRADITIONAL-044)",
            "severity": 3,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 1.04,
            "description": "The film's background characters, from the ground crew to the air traffic controllers, are portrayed as competent professionals doing their jobs in a crisis. McCroskey may have picked the wrong week to quit smoking (and drinking, and amphetamines, and sniffing glue), but he stays at his post and coordinates the rescue. The film respects the dignity of people who show up and do their work."
        },
        {
            "category": "Traditional",
            "trope": "Male Friendship and Loyalty",
            "severity": 2,
            "authenticity": "Medium",
            "centrality": "Low",
            "weightedScore": 1.40,
            "description": "Striker's backstory includes the loss of his squadron, a trauma rooted in male camaraderie and the guilt of surviving when his friends did not. The film treats this bond as sacred and Striker's grief as real. The flight crew (Oveur, Murdock) also model a casual, competent male friendship that is never the butt of the joke."
        },
        {
            "category": "Traditional",
            "trope": "Industry and Perseverance (TRADITIONAL-041)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 3.84,
            "description": "Striker lands the plane through pure perseverance: he's afraid, he's untrained on this aircraft, the weather is terrible, and he does it anyway. The film's structure is a sustained argument for grit. Keep going. Figure it out. The people counting on you deserve your best. None of this is played for irony."
        },
        {
            "category": "Minor Woke",
            "trope": "Suggestive Humor / Brief Nudity",
            "severity": 2,
            "authenticity": "Medium",
            "centrality": "Low",
            "weightedScore": 1.40,
            "description": "Airplane! contains some suggestive humor and a brief topless scene (played for shock-comedy value). By modern standards, some jokes read as dated, particularly the running gag about Joey visiting the cockpit and Captain Oveur's increasingly unhinged questions. These register as products of their era rather than ideological commitments. The film's sensibility is juvenile, not political."
        },
        {
            "category": "Minor Woke",
            "trope": "Gender Dynamics of 1980",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.76,
            "description": "Elaine is a stewardess whose primary narrative function is to be the love interest. Randy (Lorna Patterson) is another stewardess with limited agency. The film reflects 1980's gender norms honestly rather than subverting them. A 2026 viewer may notice the flatness of the female roles, but this is a period artifact, not an ideological statement. The film treats its female characters with affection, even if it doesn't give them much to do beyond the romantic plot."
        }
    ],
    "summary": {
        "overall": "Airplane! is the funniest movie ever made, and nearly half a century later, it still hasn't been topped. The ZAZ team (Jim Abrahams, David Zucker, Jerry Zucker) did something that should be impossible: they made a joke-a-second comedy where nearly every joke works, and wrapped it around a surprisingly sincere story about a traumatized veteran reclaiming his courage to save the woman he loves. Robert Hays plays Ted Striker so straight that his emotional breakdown in the cockpit lands with real weight. Leslie Nielsen reinvented his entire career playing Dr. Rumack with a sincerity so total it becomes the joke. The film is a masterclass in comedic craft, and its total indifference to politics is one of the reasons it endures.",
        "traditionaStrengths": "The film's moral architecture is bedrock traditional. A man overcomes his demons through courage and action. He saves the woman he loves and a plane full of strangers. Competence is earned through training and discipline. Professionals do their jobs in a crisis. The romantic relationship between Striker and Elaine is treated as something worth fighting for. For all its absurdist gags and surreal humor, Airplane! believes in things: bravery, loyalty, competence, love. It never winks at these values. It trusts them.",
        "wokeElements": "Virtually none. The film predates the culture war by decades. Some jokes read as dated by 2026 standards: the suggestive cockpit humor, a brief topless scene played for shock value, female characters whose roles are primarily romantic. These are period artifacts, not ideological positions. The film's sensibility is juvenile rather than political, and its disregard for propriety cuts in all directions. Anyone scanning Airplane! for a political agenda is committing a category error. This is comedy as pure craft, executed by masters who cared about one thing: the next laugh.",
        "parentaGuidance": "Airplane! is rated PG but reflects 1980 standards, not 2026's. There is a brief topless scene (a woman runs through the cabin in panic, shown from the side and back). Suggestive humor runs throughout, including a running gag about a pilot asking a young boy increasingly inappropriate questions. Mild comedic violence. Some ethnic stereotyping in the jive-talking passengers scene (played by Barbara Billingsley and June Cleaver in a joke about the disconnect between appearance and speech). No strong language. Recommended for: teenagers and up. Parents should know the PG rating is pre-PG-13, but the film's warmth and moral clarity make it suitable family viewing with a brief conversation about the topless scene."
    }
}

# ============================================================
# REVIEW 3: The Sopranos (1999)
# ============================================================
sopranos = {
    "id": "the-sopranos-1999",
    "slug": "the-sopranos-1999",
    "title": "The Sopranos",
    "year": 1999,
    "type": "tv",
    "platform": "HBO / Max",
    "genre": "Crime Drama, Psychological Drama, Black Comedy",
    "date": "2026-09-06",
    "datePublished": "2026-09-06",
    "author": "VirtueVigil Editorial Team",
    "readTime": "9 min",
    "poster": "/images/posters/the-sopranos-1999.jpg",
    "releaseDate": "1999-01-10",
    "rating": "TV-MA (Graphic Violence, Strong Language, Nudity, Sexual Content, Adult Themes)",
    "runtime": "6 Seasons, 86 Episodes (43-75 minutes)",
    "director": "David Chase (Creator / Showrunner)",
    "writers": ["David Chase", "Terence Winter", "Matthew Weiner", "Robin Green", "Mitchell Burgess"],
    "cast": [
        {"name": "James Gandolfini", "role": "Tony Soprano"},
        {"name": "Edie Falco", "role": "Carmela Soprano"},
        {"name": "Lorraine Bracco", "role": "Dr. Jennifer Melfi"},
        {"name": "Michael Imperioli", "role": "Christopher Moltisanti"},
        {"name": "Dominic Chianese", "role": "Corrado 'Junior' Soprano"},
        {"name": "Steven Van Zandt", "role": "Silvio Dante"},
        {"name": "Tony Sirico", "role": "Paulie 'Walnuts' Gualtieri"},
        {"name": "Robert Iler", "role": "Anthony Soprano Jr."},
        {"name": "Jamie-Lynn Sigler", "role": "Meadow Soprano"}
    ],
    "studio": "Chase Films, Brad Grey Television, HBO Entertainment",
    "distributor": "HBO",
    "verdict": "TRADITIONAL",
    "wokeScore": 8.47,
    "tradScore": 20.16,
    "authIndex": 70,
    "scoreMargin": "+12 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "No woke trap. The Sopranos is remarkably consistent across its 86 episodes. The show's central preoccupations: family, masculinity, mental health, mortality, and the costs of a life outside the law: are established in the pilot and deepen without changing direction. Meadow's college-years leftism is introduced as satire, not advocacy. The show never pivots to progressive messaging past any point in its runtime. If anything, the later seasons grow darker and more morally conservative, culminating in the grim, cut-to-black finale that refuses to romanticize Tony's world."
    },
    "seo": {
        "titleTag": "Is The Sopranos (1999) Woke? HBO Crime Drama VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of The Sopranos (1999), David Chase's landmark HBO crime drama starring James Gandolfini. A mob boss in therapy examines family, masculinity, and the American dream. Verdict: TRADITIONAL (+12 TRAD). Parental guidance included.",
        "keywords": "is the sopranos woke, the sopranos 1999 review, sopranos virtuevigil, sopranos traditional or woke, james gandolfini sopranos, sopranos parents guide, david chase sopranos"
    },
    "externalScores": {
        "imdb": "9.2/10",
        "rottenTomatoes": "92%",
        "metacritic": "94"
    },
    "creative_team": {
        "director": {
            "name": "David Chase",
            "ideology": "AMBIVALENT (Culturally Conservative Skeptic)",
            "profile": "David Chase is a difficult figure to pin down ideologically, which is exactly why The Sopranos works. Raised Catholic in New Jersey, Chase has expressed contempt for organized religion while simultaneously filling The Sopranos with genuine spiritual yearning. He has described himself as 'not a political person' and the show bears this out: every character who adopts a political identity, from Meadow's campus activism to Tony's flag-wrapped patriotism, is portrayed as performing rather than believing. Chase's real obsession is mortality and the failure of modern life to provide meaning. This is a deeply conservative artistic project dressed in HBO's signature transgressive clothing."
        },
        "writer": {
            "name": "David Chase, Terence Winter, Matthew Weiner, Robin Green, Mitchell Burgess",
            "profile": "The Sopranos writers' room produced some of the sharpest scripts in television history. Terence Winter's episodes lean into the criminal mechanics. Matthew Weiner's contributions explore suburban ennui and masculinity in crisis (themes he would later expand in Mad Men). Robin Green and Mitchell Burgess wrote many of the show's most domestic, therapy-centered episodes. The room's diversity of perspective kept the show from falling into any single ideological channel. Chase's supervising voice ensured that cynicism never hardened into nihilism: the show always believed that family, however broken, mattered."
        },
        "lead_producer": {
            "name": "David Chase, Brad Grey",
            "company": "Chase Films / Brad Grey Television / HBO"
        },
        "composer": {"name": "Alabama 3 (Theme)"},
        "top_cast": [
            {"name": "James Gandolfini", "role": "Tony Soprano"},
            {"name": "Edie Falco", "role": "Carmela Soprano"},
            {"name": "Lorraine Bracco", "role": "Dr. Jennifer Melfi"}
        ],
        "producers": ["David Chase", "Brad Grey", "Robin Green", "Mitchell Burgess", "Ilene S. Landress", "Terence Winter", "Matthew Weiner"],
        "full_cast": [
            {"name": "James Gandolfini", "role": "Tony Soprano"},
            {"name": "Edie Falco", "role": "Carmela Soprano"},
            {"name": "Lorraine Bracco", "role": "Dr. Jennifer Melfi"},
            {"name": "Michael Imperioli", "role": "Christopher Moltisanti"},
            {"name": "Dominic Chianese", "role": "Corrado 'Junior' Soprano"},
            {"name": "Steven Van Zandt", "role": "Silvio Dante"},
            {"name": "Tony Sirico", "role": "Paulie 'Walnuts' Gualtieri"},
            {"name": "Robert Iler", "role": "Anthony Soprano Jr."},
            {"name": "Jamie-Lynn Sigler", "role": "Meadow Soprano"},
            {"name": "Drea de Matteo", "role": "Adriana La Cerva"},
            {"name": "Steve Schirripa", "role": "Bobby Baccalieri"},
            {"name": "Vincent Pastore", "role": "Salvatore 'Big Pussy' Bonpensiero"}
        ]
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "The Importance of Family (TRADITIONAL-006)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.60,
            "description": "Family is The Sopranos' organizing principle, explored in both its meanings: the nuclear family (Tony, Carmela, AJ, Meadow) and the criminal family. Across 86 episodes, the show argues that family is the only institution that endures. Every character who abandons their family obligations suffers. Every character who honors them, however imperfectly, finds meaning. The show's final season is a sustained meditation on what a father owes his children, and the answer it arrives at is devastatingly traditional: everything."
        },
        {
            "category": "Traditional",
            "trope": "The Principled Patriarch (TRADITIONAL-029)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "Tony Soprano is a murderer, an adulterer, and a criminal. The show never lets you forget this. But he is also, in his own broken way, a traditional patriarch who believes his role is to provide for and protect his family. His rage at AJ's fecklessness, his terror that Meadow will date men like him, his genuine love for Carmela even when he's betraying her. These are not ironic postures. The show takes Tony's self-conception as a family man seriously, even as it exposes the gap between his self-image and his actions."
        },
        {
            "category": "Traditional",
            "trope": "Consequences of Hedonism (TRADITIONAL-019)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 3.84,
            "description": "Every character who pursues pleasure without limits is destroyed by it. Christopher's drug addiction. Tony's affairs. The Bing as a temple of empty gratification. The show is relentless in documenting the costs of hedonism: broken marriages, dead friends, hollowed-out souls. The strip club is a monument to loneliness. The show's moral arithmetic is unforgiving: pleasure extracted at the expense of others is debt that always comes due."
        },
        {
            "category": "Traditional",
            "trope": "Faith in Adversity (TRADITIONAL-043)",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.52,
            "description": "The Sopranos is suffused with Catholic imagery and genuine spiritual hunger. Tony's near-death experiences. Carmela's wrestle with her complicity. The recurring motif of confession and absense of absolution. The show treats faith as real and consequential, even when its characters fail to live up to it. Father Phil is a punchline, but the question he represents: can a person be forgiven? is the show's central theological inquiry."
        },
        {
            "category": "Traditional",
            "trope": "The Destructive Nature of Greed (TRADITIONAL-039)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 2.88,
            "description": "The mob life is portrayed as spiritually bankrupting. Money flows in and humanity drains out. Every character who pursues wealth through violence ends up dead, imprisoned, or hollow. Tony's material success (the house, the boat, the cars) is framed as a gilded cage, not a victory. The show never glamorizes the money. It shows you the price tag."
        },
        {
            "category": "Traditional",
            "trope": "Marriage and Betrayal (TRADITIONAL-022)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 3.84,
            "description": "Tony and Carmela's marriage is the show's second engine. Through infidelity, financial dependence, and moral compromise, the show examines what holds a marriage together when everything that should make it work is broken. Carmela's decision to stay is never portrayed as weakness. The show treats marriage as a covenant that survives its violations, and Carmela's arc is the show's most quietly radical argument for the institution."
        },
        {
            "category": "Woke",
            "trope": "Deconstruction of Masculinity (WOKE-004)",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.64,
            "description": "Tony's therapy sessions with Dr. Melfi are built around examining and deconstructing his masculinity. The show suggests that traditional male stoicism is a pathology that requires treatment. Tony's panic attacks are explicitly linked to his inability to process emotion in healthy ways. However, the show complicates this: the therapy never 'cures' Tony, and the men who reject therapy (like Paulie) are portrayed as functional in their own limited way. The show asks whether masculinity needs fixing but refuses to supply an easy answer."
        },
        {
            "category": "Minor Woke",
            "trope": "Progressive Sexual Politics (WOKE-016)",
            "severity": 2,
            "authenticity": "Medium",
            "centrality": "Low",
            "weightedScore": 1.40,
            "description": "The show includes LGBTQ characters (Vito Spatafore's arc in Season 6) and treats non-traditional relationships matter-of-factly. The mob's violent homophobia is portrayed as a feature of their moral bankruptcy, and Vito's storyline is genuinely sympathetic. This registers as mildly woke primarily because the show extends empathy to characters whom its milieu rejects, but Vito remains a tragic figure whose attempt to live authentically ends in brutal murder."
        },
        {
            "category": "Minor Woke",
            "trope": "Meadow's Campus Idealism",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.76,
            "description": "Meadow Soprano's evolution from suburban teen to Columbia student spouting progressive orthodoxy about race and privilege is played almost entirely for satire. The show undercuts her at every turn: her politics are sincerely held but performative, funded by her father's blood money, and deployed as a rebellion against parents she cannot escape. This is not woke advocacy. It's a portrait of how ideology functions as identity in the absence of genuine moral formation."
        },
        {
            "category": "Woke",
            "trope": "Anti-Institutional Attitude (WOKE-004)",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.76,
            "description": "The show is cynical about institutions: the Church (corrupt), the FBI (incompetent and manipulative), the medical establishment (aloof), corporate America (empty). This registers as anti-institutional but not specifically woke. The Sopranos is equal-opportunity cynical. The mob is the worst institution of all, and the show's disdain for organized crime is more thorough than its critique of any legitimate institution. The Cchurch may be corrupt, but the priest is still a priest."
        }
    ],
    "summary": {
        "overall": "The Sopranos is the most important television show ever made, and twenty-seven years after it premiered, it remains the standard against which all prestige drama is measured. David Chase's mobster-in-therapy premise could have been a gimmick. Instead, it became a six-season examination of family, masculinity, mortality, and the American dream that gets richer with every rewatch. James Gandolfini's Tony Soprano is the greatest performance in television history: a man so large he contains multitudes, by turns terrifying, hilarious, pathetic, and tender. The show's genius is that it never lets you forget what Tony is while making you understand why he is that way. This is not sympathy for the devil. It's a clear-eyed look at how evil operates in a man who believes himself to be good.",
        "traditionalStrengths": "The Sopranos is, at its core, a deeply traditional show wearing HBO's transgressive clothes. Family is the organizing principle. Marriage is a covenant that survives its violations. The consequences of hedonism are documented with brutal precision. Faith is treated as real and consequential, even for characters who fail to live up to it. Tony's role as patriarch is taken seriously even as it's exposed as a contradiction. The show's moral architecture is conservative in the deepest sense: it believes in duty, loyalty, and the costs of abandoning either. Every character who betrays their obligations to family pays a price. The finale's famous cut to black is the ultimate conservative gesture: you do not get to know. You do the work and you live with not knowing. This is not nihilism. This is the human condition rendered honestly.",
        "wokeElements": "The Sopranos contains threads that a modern progressive viewer might claim, but the show consistently complicates or undercuts them. Tony's therapy deconstructs traditional masculinity but never offers a replacement, and the suggestion that stoicism is purely pathological is balanced by characters who function precisely because they do not examine themselves. Vito's homosexuality arc is sympathetic but ends in his brutal murder, which is the show's way of saying that the mob world destroys anyone who deviates from its code. Meadow's campus leftism is affectionate satire, not advocacy: her politics are sincere but performative, funded by blood money, and her arc suggests that ideology is a poor substitute for moral formation. The show's cynicism about institutions is equal-opportunity rather than specifically woke: the Church, the FBI, and corporate America are all corrupt, but the mob is worse than any of them. The Sopranos earns its mixed ideological score not because it pushes a progressive agenda but because it depicts a world where progressive concerns exist as genuine questions that the show declines to answer definitively.",
        "parentalGuidance": "The Sopranos is TV-MA and earns every letter. Graphic violence throughout: shootings, beatings, strangulations, and one infamous curb-stomp. Strong language in every episode. Nudity and sexual content are frequent, centered on the Bada Bing strip club and Tony's affairs. Drug use (cocaine, heroin, prescription pills) is portrayed as destructive but depicted graphically. The show's moral universe assumes adult viewers who can distinguish depiction from endorsement. This is not a series for children or young teens under any circumstances. For older teens (16+), it may have value as a study in moral consequences and character, but parents should watch first and decide. The violence is not glamorized but it is extremely graphic. The sexual content serves character and theme rather than titillation but is explicit by television standards."
    }
}

# Validate all 3 before appending
for r in [onslaught, airplane, sopranos]:
    slug = r["slug"]
    if slug in existing_slugs:
        print(f"ERROR: {slug} already exists!")
        sys.exit(1)
    if "seo" not in r:
        print(f"ERROR: {slug} missing SEO!")
        sys.exit(1)
    if "titleTag" not in r.get("seo", {}):
        print(f"ERROR: {slug} missing titleTag!")
        sys.exit(1)
    print(f"VALIDATED: {slug}")

# Append all 3
reviews.append(onslaught)
reviews.append(airplane)
reviews.append(sopranos)

with open("src/data/reviews.json", "w") as f:
    json.dump(reviews, f, indent=2)

print(f"Done. New count: {len(reviews)}")