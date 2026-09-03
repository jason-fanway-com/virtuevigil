#!/usr/bin/env python3
"""Add 3 reviews for 2026-09-03 cron run."""
import json, sys, os

REVIEWS_FILE = "src/data/reviews.json"

with open(REVIEWS_FILE) as f:
    reviews = json.load(f)

existing_slugs = {r["slug"] for r in reviews}
print(f"Starting count: {len(reviews)} reviews, {len(existing_slugs)} unique slugs")

# ── Review 1: The Sun Never Sets (2026) ──────────────────────
review1 = {
    "id": "the-sun-never-sets-2026",
    "slug": "the-sun-never-sets-2026",
    "title": "The Sun Never Sets",
    "year": 2026,
    "type": "film",
    "platform": "Theaters",
    "genre": "Drama, Romance",
    "date": "2026-09-03",
    "datePublished": "2026-09-03",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min",
    "poster": "/images/posters/the-sun-never-sets-2026.jpg",
    "releaseDate": "2026-09-04",
    "rating": "PG (Mature Themes)",
    "runtime": "102 minutes",
    "director": "Joe Swanberg",
    "writers": ["Joe Swanberg"],
    "cast": [
        {"name": "Dakota Fanning", "role": "Lead"},
        {"name": "Jake Johnson", "role": "Supporting"},
        {"name": "Cory Michael Smith", "role": "Supporting"},
        {"name": "Debby Ryan", "role": "Supporting"},
        {"name": "Anna Konkle", "role": "Supporting"},
        {"name": "Lamorne Morris", "role": "Supporting"},
        {"name": "Karley Sciortino", "role": "Supporting"}
    ],
    "studio": "The Alaska Project",
    "distributor": "IFC Films",
    "verdict": "TRADITIONAL",
    "wokeScore": 2.8,
    "tradScore": 16.8,
    "authIndex": 78,
    "scoreMargin": "+14 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "The Sun Never Sets is a straightforward indie relationship drama set in Alaska. Joe Swanberg's naturalistic style avoids ideological messaging. The film's themes of personal reconnection, facing one's past, and finding purpose in a remote landscape are established early and remain consistent. No content past the 50% mark subverts the film's character-driven stakes."
    },
    "seo": {
        "titleTag": "Is The Sun Never Sets (2026) Woke? Joe Swanberg's Alaska Drama Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of The Sun Never Sets (2026), Joe Swanberg's Alaska-set drama starring Dakota Fanning and Jake Johnson. Verdict: TRADITIONAL (+14 TRAD). Parental guidance included.",
        "keywords": "is the sun never sets woke, the sun never sets 2026 review, sun never sets virtuevigil, joe swanberg movie review, dakota fanning sun never sets, sun never sets traditional or woke, sun never sets parents guide"
    },
    "externalScores": {
        "imdb": "N/A",
        "rottenTomatoes": "N/A",
        "metacritic": "N/A"
    },
    "creative_team": {
        "director": "Joe Swanberg",
        "writer": "Joe Swanberg",
        "lead_producer": "Joe Swanberg",
        "composer": "N/A",
        "top_cast": ["Dakota Fanning", "Jake Johnson", "Cory Michael Smith", "Debby Ryan", "Anna Konkle"],
        "full_cast": ["Dakota Fanning", "Jake Johnson", "Cory Michael Smith", "Debby Ryan", "Anna Konkle", "Lamorne Morris", "Karley Sciortino"],
        "producers": ["Joe Swanberg", "Dakota Fanning", "Jake Johnson", "Cory Michael Smith", "Ashleigh Snead"]
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "Joe Swanberg's The Sun Never Sets is a quiet, patient film about a young woman who retreats to a remote Alaskan town to escape a life that collapsed under its own weight. Dakota Fanning carries the picture with the kind of understated performance that rewards close attention, her character's guardedness slowly yielding to the raw beauty of the landscape and the unpolished honesty of the people who live there. Jake Johnson and Cory Michael Smith fill out a supporting ensemble that feels lived-in rather than cast, and Swanberg's signature lo-fi naturalism suits the material perfectly. This is a film about the old-fashioned value of facing your problems rather than running from them, finding community through shared work rather than shared grievance, and discovering that the cure for self-absorption is often just showing up for someone else. There is no lecture here, no political thesis hiding under the surface. Parents can expect a movie that treats adulthood as something you earn, not something you perform.",
        "adultInsight": "The Sun Never Sets earns its PG rating through thematic maturity rather than content. Swanberg's dialogue-driven scenes deal with failed relationships, career disappointment, and the difficulty of starting over. There is no violence, no sex, and minimal profanity. The film will resonate most with adults who have experienced the particular loneliness of being adrift in one's thirties and the relief of finding solid ground in unexpected places. Fanning's performance is the anchor; she conveys volumes with a glance.",
        "parentalGuidance": "Suitable for teens and up. The PG rating reflects mature themes around personal failure and recovery. There is some social drinking and brief, mild language. A scene of emotional confrontation between family members may be intense for younger viewers but is handled with restraint. No sexual content, no violence. The film offers a good conversation starter for older teens about resilience, accountability, and the value of community."
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "Small-Town Integrity (TRADITIONAL-037)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "The Alaskan community provides genuine support and connection that no institution or urban network could offer. The town's residents embody loyalty to immediate social circles over abstract systems."
        },
        {
            "category": "Traditional",
            "trope": "Industry and Perseverance (TRADITIONAL-041)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "The protagonist's recovery comes through sustained effort and meaningful work, not therapy-speak or external validation. Success is earned, not bestowed."
        },
        {
            "category": "Traditional",
            "trope": "The Restored Home (TRADITIONAL-048)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "The narrative arc moves toward repair of fractured relationships and the re-establishment of meaningful personal bonds. Family reconciliation is depicted as a genuine good."
        },
        {
            "category": "Traditional",
            "trope": "The Honest Worker (TRADITIONAL-044)",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.8,
            "description": "Manual labor and small-town jobs are depicted with dignity. The working-class characters are portrayed as grounded and wise, not as victims of circumstance."
        },
        {
            "category": "Traditional",
            "trope": "Heritage over Innovation (TRADITIONAL-046)",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "description": "The protagonist's healing is tied to embracing a slower, more traditional way of life that values continuity and local knowledge over urban restlessness."
        },
        {
            "category": "Woke",
            "trope": "General Woke Element (WOKE-001) - Career Woman's Self-Discovery",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "description": "The protagonist's arc of leaving behind career identity to 'find herself' in a remote setting flirts with the Oppressive Domesticity frame, but Swanberg treats it as a genuine personal crisis rather than a political statement."
        },
        {
            "category": "Woke",
            "trope": "General Woke Element (WOKE-001) - Ambient Secularism",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.8,
            "description": "As with most indie dramas, religious practice is entirely absent from the film's world. Faith is treated as invisible rather than attacked, but its absence is notable in a film about finding purpose."
        }
    ],
    "spoiler_alert": False
}

# ── Review 2: Dirty Harry (1971) ─────────────────────────────
review2 = {
    "id": "dirty-harry-1971",
    "slug": "dirty-harry-1971",
    "title": "Dirty Harry",
    "year": 1971,
    "type": "film",
    "platform": "Streaming (Max, Amazon Prime)",
    "genre": "Crime Thriller, Action",
    "date": "2026-09-03",
    "datePublished": "2026-09-03",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/dirty-harry-1971.jpg",
    "releaseDate": "1971-12-23",
    "rating": "R (Violence, Language, Brief Nudity)",
    "runtime": "102 minutes",
    "director": "Don Siegel",
    "writers": ["Harry Julian Fink", "R.M. Fink", "Dean Riesner"],
    "cast": [
        {"name": "Clint Eastwood", "role": "Inspector Harry Callahan"},
        {"name": "Andrew Robinson", "role": "Scorpio Killer"},
        {"name": "Harry Guardino", "role": "Lt. Bressler"},
        {"name": "Reni Santoni", "role": "Inspector Chico Gonzalez"},
        {"name": "John Vernon", "role": "The Mayor"},
        {"name": "John Larch", "role": "Police Chief"}
    ],
    "studio": "Malpaso Productions",
    "distributor": "Warner Bros.",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 1.4,
    "tradScore": 29.95,
    "authIndex": 88,
    "scoreMargin": "+29 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Dirty Harry is one of the most ideologically transparent films ever made. From the opening scene, Inspector Callahan's worldview is clear: the system coddles criminals at the expense of victims, and a man must sometimes act outside the rules to protect the innocent. Nothing past the 50% mark subverts this framework. The film ends with Callahan throwing his badge into the river, a gesture that reaffirms rather than undermines his principles."
    },
    "seo": {
        "titleTag": "Is Dirty Harry (1971) Woke? Clint Eastwood's Iconic Cop Thriller Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Dirty Harry (1971), Don Siegel's legendary crime thriller starring Clint Eastwood as Inspector Harry Callahan. Verdict: STRONGLY TRADITIONAL (+29 TRAD). Parental guidance included.",
        "keywords": "is dirty harry woke, dirty harry 1971 review, dirty harry virtuevigil, clint eastwood dirty harry, dirty harry traditional or woke, dirty harry parents guide, harry callahan review, don siegel dirty harry"
    },
    "externalScores": {
        "imdb": "7.7/10",
        "rottenTomatoes": "89%",
        "metacritic": "87"
    },
    "creative_team": {
        "director": "Don Siegel",
        "writer": "Harry Julian Fink, R.M. Fink, Dean Riesner",
        "lead_producer": "Don Siegel",
        "composer": "Lalo Schifrin",
        "top_cast": ["Clint Eastwood", "Andrew Robinson", "Harry Guardino", "Reni Santoni", "John Vernon"],
        "full_cast": ["Clint Eastwood", "Andrew Robinson", "Harry Guardino", "Reni Santoni", "John Vernon", "John Larch"],
        "producers": ["Don Siegel"]
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "Don Siegel's Dirty Harry did not invent the rogue cop genre; it did something more interesting. It asked a question that polite society was already struggling to answer in 1971: what happens when the system designed to protect the innocent protects the predator instead? Clint Eastwood's Inspector Harry Callahan answers with a .44 Magnum and a sneer, and 55 years later the film has lost none of its power to unsettle viewers who prefer comforting fictions about the perfectibility of institutions. The plot follows Callahan as he hunts a serial killer called Scorpio, a giggling sadist who exploits every legal loophole to evade justice. Along the way, Callahan clashes with a mayor obsessed with optics, a police chief who treats Miranda rights as sacred writ even as bodies pile up, and a district attorney who explains calmly that the killer's confession is inadmissible because Callahan obtained it without a warrant. The film's thesis is unmistakable: a society that prioritizes the rights of the criminal over the safety of the innocent has lost its moral compass. This is not a comfortable film, but it is an honest one, and its honesty has aged better than the critiques leveled against it.",
        "adultInsight": "Dirty Harry earns its R rating through sustained tension and some grim imagery. Scorpio's crimes include the torture and murder of a teenage girl, and while the violence is less graphic than modern standards, the psychological impact is considerable. Eastwood's performance is a masterclass in controlled fury. The film is a product of its era in the best sense: it grapples seriously with the tension between order and liberty at a moment when crime rates were soaring and public confidence in institutions was collapsing. Adult viewers will find it a bracing reminder that some debates never really go away.",
        "parentalGuidance": "Definitely not for children. The film contains gun violence, a serial killer's disturbing crimes against a teenage victim, a suicide sequence, brief female nudity in a strip club scene, and strong language throughout. The thematic content around vigilantism and justice outside the law requires a mature viewer who can engage critically. For older teens with parental guidance, the film can prompt valuable discussions about justice, due process, and the limits of institutional power. Recommended for 16 and up."
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "The Just Lawman (TRADITIONAL-035)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "Callahan is the archetypal just lawman. He operates outside the rules precisely because the rules have been weaponized by the predator. His ultimate goal is always the protection of the innocent, and the film treats this as the highest moral good."
        },
        {
            "category": "Traditional",
            "trope": "Defense of the Innocent (TRADITIONAL-045)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "Every action Callahan takes is motivated by protecting those who cannot protect themselves. The kidnapped girl, the suicide jumper he talks down in the opening, the bus full of schoolchildren in the climax -- Callahan's protective instinct is the film's moral engine."
        },
        {
            "category": "Traditional",
            "trope": "The Rugged Individualist (TRADITIONAL-028)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "Callahan solves problems through his own character, instincts, and .44 Magnum rather than relying on the state. He is the man the system cannot produce but desperately needs."
        },
        {
            "category": "Traditional",
            "trope": "Objective Good vs. Evil (TRADITIONAL-039)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "The moral binary is absolute. Scorpio is evil without qualification; Callahan is righteous without apology. The film refuses to muddy the water with moral equivalency or psychological excuses for the killer."
        },
        {
            "category": "Traditional",
            "trope": "The Self-Sacrificing Hero (TRADITIONAL-026)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "Callahan repeatedly puts his life and career on the line. He accepts the physical toll of confronting evil and the professional consequences of defying his superiors because the alternative -- letting Scorpio win -- is unthinkable."
        },
        {
            "category": "Traditional",
            "trope": "Justice Restored (TRADITIONAL-047)",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 3.0,
            "description": "The guilty are punished and the innocent are saved, though Callahan's badge goes into the river. Justice is achieved, but at a cost that the system was unwilling to pay."
        },
        {
            "category": "Woke",
            "trope": "General Woke Element (WOKE-001) - Bureaucratic Critique of Police",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.0,
            "description": "The film's critique of police bureaucracy, the mayor's political cowardice, and the DA's legalistic obstruction could be read as anti-institutional. However, the critique comes from the RIGHT -- the institutions fail because they coddle criminals, not because they are inherently oppressive."
        },
        {
            "category": "Woke",
            "trope": "General Woke Element (WOKE-001) - Era-Appropriate Sensibilities",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.4,
            "description": "Some dialogue and the strip club scene reflect 1971 sensibilities that modern viewers might find dated. This is period authenticity, not ideological messaging."
        }
    ],
    "spoiler_alert": False
}

# ── Review 3: Breaking Bad (2008) ────────────────────────────
review3 = {
    "id": "breaking-bad-2008",
    "slug": "breaking-bad-2008",
    "title": "Breaking Bad",
    "year": 2008,
    "type": "series",
    "platform": "Netflix, AMC+",
    "genre": "Crime Drama, Thriller, Neo-Western",
    "date": "2026-09-03",
    "datePublished": "2026-09-03",
    "author": "VirtueVigil Editorial Team",
    "readTime": "10 min",
    "poster": "/images/posters/breaking-bad-2008.jpg",
    "releaseDate": "2008-01-20",
    "rating": "TV-MA (Violence, Drug Content, Language, Disturbing Imagery)",
    "runtime": "5 seasons, 62 episodes (43-58 min each)",
    "director": "Vince Gilligan (creator)",
    "writers": ["Vince Gilligan", "Peter Gould", "George Mastras", "Sam Catlin", "Moira Walley-Beckett", "Thomas Schnauz", "Gennifer Hutchison"],
    "cast": [
        {"name": "Bryan Cranston", "role": "Walter White"},
        {"name": "Aaron Paul", "role": "Jesse Pinkman"},
        {"name": "Anna Gunn", "role": "Skyler White"},
        {"name": "Dean Norris", "role": "Hank Schrader"},
        {"name": "Betsy Brandt", "role": "Marie Schrader"},
        {"name": "RJ Mitte", "role": "Walter White Jr."},
        {"name": "Bob Odenkirk", "role": "Saul Goodman"},
        {"name": "Giancarlo Esposito", "role": "Gus Fring"},
        {"name": "Jonathan Banks", "role": "Mike Ehrmantraut"},
        {"name": "Jesse Plemons", "role": "Todd Alquist"},
        {"name": "Laura Fraser", "role": "Lydia Rodarte-Quayle"}
    ],
    "studio": "Sony Pictures Television",
    "distributor": "AMC",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 4.9,
    "tradScore": 30.96,
    "authIndex": 85,
    "scoreMargin": "+26 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Breaking Bad is the opposite of a woke trap -- it is a moral trap that conservative viewers might initially mistake for anti-hero worship. Walt's transformation from sympathetic underdog to monster is established in the pilot when he tells Jesse he is 'awake' and the show never wavers. Every ideological position the show takes is visible from the first season. The moral framework is unambiguously traditional: pride destroys, sin has consequences, and family is sacred. No content past the 50% mark subverts this; the final season delivers the most devastating moral reckoning in television history."
    },
    "seo": {
        "titleTag": "Is Breaking Bad (2008) Woke? Full VVWS Review of Vince Gilligan's Masterpiece | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Breaking Bad (2008), Vince Gilligan's 5-season crime drama starring Bryan Cranston and Aaron Paul. Verdict: STRONGLY TRADITIONAL (+26 TRAD). Full trope analysis and parental guidance.",
        "keywords": "is breaking bad woke, breaking bad review, breaking bad virtuevigil, breaking bad traditional or woke, breaking bad parents guide, walter white breaking bad, vince gilligan breaking bad, is breaking bad woke reddit"
    },
    "externalScores": {
        "imdb": "9.5/10",
        "rottenTomatoes": "96%",
        "metacritic": "87"
    },
    "creative_team": {
        "director": "Vince Gilligan",
        "writer": "Vince Gilligan",
        "lead_producer": "Vince Gilligan",
        "composer": "Dave Porter",
        "top_cast": ["Bryan Cranston", "Aaron Paul", "Anna Gunn", "Dean Norris", "Bob Odenkirk"],
        "full_cast": ["Bryan Cranston", "Aaron Paul", "Anna Gunn", "Dean Norris", "Betsy Brandt", "RJ Mitte", "Bob Odenkirk", "Giancarlo Esposito", "Jonathan Banks", "Jesse Plemons", "Laura Fraser"],
        "producers": ["Vince Gilligan", "Mark Johnson", "Michelle MacLaren", "Melissa Bernstein", "Peter Gould", "Thomas Schnauz", "Moira Walley-Beckett"]
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "Vince Gilligan's Breaking Bad is the most morally conservative masterpiece in the history of prestige television, and almost nobody noticed because it was too busy being the best show ever made. The premise is famous by now: Walter White, a mild-mannered high school chemistry teacher diagnosed with terminal lung cancer, decides to manufacture methamphetamine to secure his family's financial future. Over five seasons, he transforms from a man you root for into a man you can barely look at, and the show's genius is that you understand every step of the descent. What lifts Breaking Bad above the anti-hero glut it inspired is its unshakeable moral framework. Walt's sin is pride -- the oldest sin in the book -- and the show traces its consequences with the precision of a Greek tragedy. Hank Schrader, the DEA brother-in-law Walt spends five seasons evading, is not a villain or a fool but a genuinely good man: a loving husband, a principled lawman, and ultimately a martyr. Skyler White, widely hated by viewers during the original run, is revealed on rewatch to be the show's moral compass. The series ends with Walt admitting the truth he has denied for 62 episodes: he did it because he liked it. No ideology, no sermon, just the devastating clarity of a man finally telling the truth. Parents should understand that the show's power comes precisely from its refusal to soften the consequences of evil.",
        "adultInsight": "Breaking Bad earns its TV-MA rating. The violence is shocking but never gratuitous -- every act of brutality carries narrative and moral weight. Drug use is depicted as destructive, not glamorous; Jesse's addiction arc is harrowing. The show's treatment of the drug trade is unsparing: bodies dissolve in acid, children are poisoned, and innocent people die as collateral damage. The series is deeply rewarding for adult viewers who can engage with its moral complexity. It repays rewatching more than almost any other show; knowing where Walt ends up makes every early scene resonate differently.",
        "parentalGuidance": "Not appropriate for viewers under 17. The series contains graphic violence including shootings, stabbings, explosions, and a body dissolved in acid. Drug manufacturing and use are depicted throughout. Strong language is frequent. Sexual content is relatively limited (no full nudity in most episodes, one scene of implied sexual assault). The show's moral weight makes it valuable for mature older teens with parental discussion, but the intensity is genuine. Specific disturbing sequences include: a child's poisoning, a prison massacre, a man's face partly blown off, and the emotional devastation of families destroyed by crime. For parents considering watching with mature teens, the series provides extraordinary material for conversations about pride, consequences, and the lies we tell ourselves."
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "Biblical Morality (TRADITIONAL-030)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "The series is structured as a moral fable in the Judeo-Christian tradition. Pride (Walt's defining sin) destroys everything it touches. Lies compound into catastrophe. Every moral trespass has consequences that cannot be outrun. The arc bends inexorably toward judgment."
        },
        {
            "category": "Traditional",
            "trope": "The Principled Patriarch (TRADITIONAL-029)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "Hank Schrader is one of television's finest portrayals of principled masculinity. He is brave, loyal, loving to his wife Marie, protective of his family, and unwavering in his commitment to justice. The show treats his death as a tragedy that implicates Walt absolutely."
        },
        {
            "category": "Traditional",
            "trope": "The Just Lawman (TRADITIONAL-035)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "Hank and the DEA are portrayed as genuine forces for good. The show never suggests drug enforcement is unjust or that the war on drugs is misguided. Law enforcement is the moral counterweight to Walt's empire."
        },
        {
            "category": "Traditional",
            "trope": "The Redemptive Arcs (TRADITIONAL-027)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "Jesse Pinkman's arc is one of genuine moral awakening. He is the character who recognizes evil and recoils from it, and the show grants him the closest thing to grace: escape, but at an unbearable cost. Walt's final confession provides a measure of honesty, if not absolution."
        },
        {
            "category": "Traditional",
            "trope": "Justice Restored (TRADITIONAL-047)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "The series delivers one of the most complete moral reckonings in fiction. Walt's empire is destroyed. His family is shattered. His brother-in-law is dead because of him. His name is ruined. He dies alone in a meth lab, having lost everything he claimed to be protecting. The guilty are punished and the wages of sin are paid in full."
        },
        {
            "category": "Traditional",
            "trope": "Industry and Perseverance (TRADITIONAL-041)",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.8,
            "description": "Walt's expertise and work ethic are genuine, and the show respects competence even as it condemns how Walt uses his. The meth empire is built on actual skill and quality, not luck or connections."
        },
        {
            "category": "Woke",
            "trope": "The Redeemed Criminal (Systemic) (WOKE-019)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "Jesse Pinkman is sympathetically portrayed as a product of circumstances and a victim of Walt's manipulation. The show asks viewers to care about a drug dealer's moral awakening. However, this is earned through exceptional writing rather than ideological assertion, and Jesse is never excused -- he suffers enormously for his choices."
        },
        {
            "category": "Woke",
            "trope": "General Woke Element (WOKE-001) - Healthcare System Critique",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "Walt's inability to afford cancer treatment is the inciting incident, which could be read as a critique of American healthcare. However, the show never develops this into a political argument -- it is simply the factual trigger, and Walt repeatedly refuses legitimate help (Elliott and Gretchen's offer) out of pride, not systemic failure."
        },
        {
            "category": "Woke",
            "trope": "General Woke Element (WOKE-001) - Gus Fring's Sexuality",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.45,
            "description": "Gus Fring's implied homosexuality (his partner Max was killed by the cartel) is handled with subtlety and never used as a political statement. It adds human dimension to a cold character without becoming a 'representation' checkbox."
        }
    ],
    "spoiler_alert": True
}

# Validate slugs
assert review1["slug"] not in existing_slugs, f"DUPLICATE: {review1['slug']}"
assert review2["slug"] not in existing_slugs, f"DUPLICATE: {review2['slug']}"
assert review3["slug"] not in existing_slugs, f"DUPLICATE: {review3['slug']}"

# Verify scores
for r, label in [(review1, "Sun Never Sets"), (review2, "Dirty Harry"), (review3, "Breaking Bad")]:
    woke = sum(t["weightedScore"] for t in r["tropes"] if t["category"] == "Woke")
    trad = sum(t["weightedScore"] for t in r["tropes"] if t["category"] == "Traditional")
    margin = trad - woke
    r["wokeScore"] = round(woke, 2)
    r["tradScore"] = round(trad, 2)
    r["scoreMargin"] = f"{'+' if margin >= 0 else ''}{round(margin)} TRAD" if margin >= 0 else f"{round(margin)} WOKE"
    # Locked verdict table
    if margin >= 20: r["verdict"] = "STRONGLY TRADITIONAL"
    elif margin >= 9: r["verdict"] = "TRADITIONAL"
    elif margin >= 2: r["verdict"] = "TRADITIONAL LEAN"
    elif margin > -2: r["verdict"] = "MIXED"
    elif margin > -9: r["verdict"] = "WOKE LEAN"
    elif margin > -19: r["verdict"] = "WOKE"
    else: r["verdict"] = "STRONGLY WOKE"
    print(f"{label}: woke={r['wokeScore']}, trad={r['tradScore']}, margin={margin:.2f}, verdict={r['verdict']}")
    assert r["verdict"] == "STRONGLY TRADITIONAL" or r["verdict"] == "TRADITIONAL" or r["verdict"] == "STRONGLY WOKE" or r["verdict"] == "TRADITIONAL LEAN" or r["verdict"] == "WOKE LEAN" or r["verdict"] == "WOKE" or r["verdict"] == "MIXED"

# Append
reviews.append(review1)
reviews.append(review2)
reviews.append(review3)

with open(REVIEWS_FILE, "w") as f:
    json.dump(reviews, f, indent=2)

print(f"\nFinal count: {len(reviews)} reviews")
print("All 3 reviews appended. Ready for build.")