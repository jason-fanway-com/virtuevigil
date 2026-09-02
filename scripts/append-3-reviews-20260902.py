#!/usr/bin/env python3
"""Append 3 reviews for 2026-09-02 daily batch."""
import json, sys, os

REVIEWS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src/data/reviews.json')

with open(REVIEWS_PATH, 'r') as f:
    data = json.load(f)

slugs = {r.get('slug','') for r in data}
for s in ['tony-2026', 'ferris-buellers-day-off-1986', 'the-last-of-us-2023']:
    if s in slugs:
        print(f'DUPLICATE SLUG: {s}')
        sys.exit(1)

new_reviews = []

# ──────────────────────────────────────────────
# REVIEW 1: Tony (2026)
# ──────────────────────────────────────────────
tony = {
    "id": "tony-2026",
    "slug": "tony-2026",
    "title": "Tony",
    "year": 2026,
    "type": "film",
    "platform": "Theaters",
    "genre": "Biographical Comedy Drama, Coming-of-Age",
    "date": "2026-09-02",
    "datePublished": "2026-09-02",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/tony-2026.jpg",
    "releaseDate": "2026-08-07",
    "rating": "14A (Language, Drug Use, Mature Themes)",
    "runtime": "106 minutes",
    "director": "Matt Johnson",
    "writers": ["Matt Johnson", "Matthew Miller", "Todd Bartels", "Lou Howe"],
    "cast": [
        {"name": "Dominic Sessa", "role": "Anthony 'Tony' Bourdain"},
        {"name": "Emilia Jones", "role": "Nancy Putkoski"},
        {"name": "Antonio Banderas", "role": "Chef Jose Vatel"},
        {"name": "Leo Woodall", "role": "Sal"},
        {"name": "Stavros Halkias", "role": "Stavros"},
        {"name": "Dagmara Dominczyk", "role": "Mary"},
        {"name": "Rich Sommer", "role": "Supporting"},
        {"name": "Monica Raymund", "role": "Supporting"}
    ],
    "studio": "Star Thrower Entertainment / Zapruder Films",
    "distributor": "A24",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 2.5,
    "tradScore": 24.75,
    "authIndex": 82,
    "scoreMargin": "+22 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Tony is a straightforward coming-of-age biopic about Anthony Bourdain's early years. No ideological content is hidden past the midpoint. The film's themes - work ethic, mentorship, honesty, and finding one's calling - are presented openly from the beginning and remain consistent throughout. Drug use in the kitchen culture is depicted as period realism, not glorified or politicized."
    },
    "seo": {
        "titleTag": "Is Tony (2026) Woke? Anthony Bourdain Biopic Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Tony (2026), A24's Anthony Bourdain biopic starring Dominic Sessa. Bourdain's early kitchen years in Provincetown. Verdict: STRONGLY TRADITIONAL (+22 TRAD). Parental guidance included.",
        "keywords": "is tony woke, tony 2026 review, tony virtuevigil, anthony bourdain biopic review, tony movie traditional or woke, tony parents guide, dominic sessa tony, tony a24 movie"
    },
    "externalScores": {
        "imdb": "N/A",
        "rottenTomatoes": "85%",
        "metacritic": "N/A"
    },
    "creative_team": {
        "director": "Matt Johnson",
        "writer": "Matt Johnson, Matthew Miller, Todd Bartels, Lou Howe",
        "lead_producer": "Tim White",
        "composer": "Jay McCarrol",
        "top_cast": ["Dominic Sessa", "Emilia Jones", "Antonio Banderas", "Leo Woodall", "Stavros Halkias"],
        "full_cast": ["Dominic Sessa", "Emilia Jones", "Antonio Banderas", "Leo Woodall", "Stavros Halkias", "Dagmara Dominczyk", "Rich Sommer", "Monica Raymund"],
        "producers": ["Tim White", "Trevor White", "Matt Johnson", "Matthew Miller"]
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "Matt Johnson's Tony is the rare biopic that earns its subject's legacy instead of coasting on it. Based on Anthony Bourdain's Kitchen Confidential, the film follows a 19-year-old Bourdain (Dominic Sessa) during a pivotal summer in Provincetown, Massachusetts, where he stumbles into restaurant work and discovers the chaotic, drug-fueled camaraderie of professional kitchens that would define his career. Sessa captures Bourdain's restless intelligence and bone-deep insecurity beautifully, while Antonio Banderas brings quiet dignity to Chef Vatel, the mentor who sees something in the lying dishwasher others might dismiss. The film never lectures about work ethic or the value of honest labor - it simply shows a young man who finally stops pretending and starts doing. For parents wondering whether Hollywood has turned Bourdain into a political vessel: it has not. This is a film about a boy becoming a man through craft, failure, and mentorship, and it trusts its audience to understand that without a sermon.",
        "adultInsight": "Tony earns its 14A rating through kitchen-authentic depictions of drug use, profanity, and the rough edges of 1970s restaurant culture. None of it is gratuitous; it all serves the story of a young man finding his place in a world that doesn't care about his excuses. Adult viewers who remember Bourdain will find this a moving origin story. Those who do not know him will still recognize the universal arc of someone who stops running from who they are.",
        "parentalGuidance": "Not for young kids. The film depicts cocaine and heroin use among kitchen staff, heavy drinking, and strong language throughout. A grease fire destroys the restaurant in a tense sequence. There is an implied sexual encounter between Tony and Nancy (not graphic). The film's core lessons about honesty, hard work, and finding purpose are positive, but the setting is authentically rough. Best suited for mature teens 16+ with parental discussion about substance abuse and the value of mentorship."
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "Merit-Based Achievement",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 9.0,
            "description": "Tony earns every promotion through demonstrated skill - from dishwasher to cook on pure competence. Chef Vatel sees his potential not because of who he is but because of what he can do. The film treats honest work as the only legitimate path to advancement, with no shortcuts or identity-based shortcuts offered or taken."
        },
        {
            "category": "Traditional",
            "trope": "Traditional Male Coming-of-Age",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.75,
            "description": "Bourdain's arc is a classic masculine bildungsroman: a young man leaves home, screws up, learns from older men, takes responsibility, and earns his place. The film treats this arc with respect rather than irony. There is no deconstruction of masculinity here - the kitchen is a meritocracy where competence, toughness, and reliability matter."
        },
        {
            "category": "Traditional",
            "trope": "Mentorship and Apprenticeship",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.75,
            "description": "Chef Vatel's mentorship of Tony is the film's emotional core. An older, experienced man takes a risk on a young screw-up and invests in his growth. This intergenerational transmission of craft knowledge is depicted as sacred. Vatel's disappointment when Tony lies to him carries real weight because the relationship was built on mutual respect."
        },
        {
            "category": "Traditional",
            "trope": "Honesty and Redemption Through Action",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "description": "Tony's lies about the fellowship and his kitchen experience catch up with him, and his redemption comes not through apology but through action - organizing the clam bake, making genuine amends, and accepting the consequences of his dishonesty. The film endorses the idea that character is built through deeds, not words."
        },
        {
            "category": "Traditional",
            "trope": "Craft and Vocation as Identity",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "description": "The film treats cooking as a legitimate calling and craft, not just a job. The kitchen is depicted as a place where skill matters more than background - a fundamentally conservative vision of work as identity. The culinary world is shown as a genuine community bound by shared standards rather than political affinity."
        },
        {
            "category": "Woke",
            "trope": "Drug/Glamorized Vice",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "description": "The film depicts kitchen culture's drug use (cocaine, heroin) and heavy drinking as authentically as Bourdain's memoir did. While not glamorized per se, the camaraderie around drug use could be read as endorsement. Sal's heroin addiction leads to his downfall, which serves as a cautionary element that blunts this trope's severity."
        },
        {
            "category": "Woke",
            "trope": "Anti-Institutional Attitude",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.25,
            "description": "Tony rejects the traditional path (college fellowship, predictable career) in favor of the chaotic restaurant world. This could be read as anti-establishment, but the film frames it as finding authentic calling rather than rejecting institutions per se. A stretch categorization."
        }
    ],
    "spoiler_alert": False
}

# ──────────────────────────────────────────────
# REVIEW 2: Ferris Bueller's Day Off (1986)
# ──────────────────────────────────────────────
ferris = {
    "id": "ferris-buellers-day-off-1986",
    "slug": "ferris-buellers-day-off-1986",
    "title": "Ferris Bueller's Day Off",
    "year": 1986,
    "type": "film",
    "platform": "Streaming (Paramount+)",
    "genre": "Teen Comedy, Coming-of-Age",
    "date": "2026-09-02",
    "datePublished": "2026-09-02",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/ferris-buellers-day-off-1986.jpg",
    "releaseDate": "1986-06-11",
    "rating": "PG-13",
    "runtime": "103 minutes",
    "director": "John Hughes",
    "writers": ["John Hughes"],
    "cast": [
        {"name": "Matthew Broderick", "role": "Ferris Bueller"},
        {"name": "Alan Ruck", "role": "Cameron Frye"},
        {"name": "Mia Sara", "role": "Sloane Peterson"},
        {"name": "Jeffrey Jones", "role": "Dean Ed Rooney"},
        {"name": "Jennifer Grey", "role": "Jeanie Bueller"},
        {"name": "Cindy Pickett", "role": "Katie Bueller"},
        {"name": "Lyman Ward", "role": "Tom Bueller"},
        {"name": "Edie McClurg", "role": "Grace"},
        {"name": "Ben Stein", "role": "Economics Teacher"}
    ],
    "studio": "Paramount Pictures",
    "distributor": "Paramount Pictures",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 0.0,
    "tradScore": 27.25,
    "authIndex": 94,
    "scoreMargin": "+27 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Ferris Bueller's Day Off is an unapologetically traditional film from start to finish. John Hughes's 1986 classic contains zero hidden ideological content. The film's thesis - that life moves fast and individual experience matters more than institutional conformity - is stated directly by Ferris in the opening monologue and never wavers. No content past the 50% mark subverts this message."
    },
    "seo": {
        "titleTag": "Is Ferris Bueller's Day Off (1986) Woke? John Hughes Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Ferris Bueller's Day Off (1986). John Hughes's iconic teen comedy starring Matthew Broderick. Verdict: STRONGLY TRADITIONAL (+27 TRAD). Parental guidance included.",
        "keywords": "is ferris bueller woke, ferris bueller day off 1986 review, ferris bueller virtuevigil, ferris bueller traditional or woke, ferris bueller parents guide, john hughes ferris bueller, ferris bueller movie review"
    },
    "externalScores": {
        "imdb": "7.8/10",
        "rottenTomatoes": "81%",
        "metacritic": "61"
    },
    "creative_team": {
        "director": "John Hughes",
        "writer": "John Hughes",
        "lead_producer": "John Hughes",
        "composer": "Ira Newborn",
        "top_cast": ["Matthew Broderick", "Alan Ruck", "Mia Sara", "Jeffrey Jones", "Jennifer Grey"],
        "full_cast": ["Matthew Broderick", "Alan Ruck", "Mia Sara", "Jeffrey Jones", "Jennifer Grey", "Cindy Pickett", "Lyman Ward", "Edie McClurg", "Ben Stein"],
        "producers": ["John Hughes", "Tom Jacobson"]
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "John Hughes's Ferris Bueller's Day Off is not just one of the funniest teen comedies ever made - it is a near-perfect time capsule of an America that believed individuals could outwit systems and that a single perfect day with a best friend was worth any consequence. Matthew Broderick's Ferris is a folk hero disguised as a high school senior: a kid who understands that life is not a dress rehearsal and that the institutions designed to shape you into a compliant adult - school, authority figures, the daily grind - are there to be challenged, not obeyed. What makes the film magnificent 40 years later is how deeply conservative its actual values are. Ferris loves his family. He protects his depressive best friend Cameron from a domineering father and coaches him toward self-respect. He is devoted to his girlfriend Sloane. The day he plans is a celebration of art, architecture, baseball, and the simple joy of being young in a free country. The villain is not the system writ large but a specific petty tyrant - Dean Rooney - whose obsession with catching Ferris is motivated by personal insecurity, not ideology. There are no lectures here, no identity politics, no deconstruction. Just a movie that loves its characters and believes that standing up for yourself is a virtue. It ages like wine because it was made before Hollywood decided that every story needed a political valence.",
        "adultInsight": "Rewatching Ferris Bueller as an adult hits differently. The jokes still land but the emotional weight shifts from Ferris to Cameron - a kid so crushed by his father's expectations that he is practically catatonic. Alan Ruck's performance is the film's secret weapon. The Ferrari destruction scene, often read as comedy, is actually about a son reclaiming agency from a father who values objects over people. The film trusts its adult audience to find that layer without underlining it.",
        "parentalGuidance": "Rated PG-13, and fairly so. Mild profanity throughout, some teen drinking references, and Ferris's general attitude of rule-breaking is played for comedy rather than consequence. Parents should note that Ferris's elaborate deceptions - faking illness, hacking the school attendance system, impersonating authority figures - are framed as charming rather than dishonest. A good conversation-starter about boundaries, responsibility, and the difference between harmless fun and genuine deception. The film's core messages about friendship, self-respect, and not letting life pass you by are excellent."
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "Individual Freedom vs. Bureaucratic Control",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 9.0,
            "description": "The central conflict: one clever kid versus an entire institutional apparatus (high school, the principal, parents, the attendance system). Ferris wins because he is smarter, more creative, and more alive than the system designed to process him. The film argues that institutions exist to serve people, not the other way around - a fundamentally American, individualist position."
        },
        {
            "category": "Traditional",
            "trope": "Male Friendship and Loyalty",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.75,
            "description": "Ferris's devotion to Cameron is the film's emotional center. He spends his one perfect day trying to save his best friend from a life of fear and passivity. The friendship is depicted without irony or subtext - two guys who genuinely care about each other. Cameron's arc from terrified doormat to someone who can finally stand up to his father is earned and moving."
        },
        {
            "category": "Traditional",
            "trope": "Anti-Bureaucracy / Personal Agency",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 9.0,
            "description": "Every authority figure in the film is incompetent, petty, or both. Dean Rooney is not evil - he is a small man obsessed with proving his power. The economics teacher (Ben Stein) puts students to sleep with monotone drivel. The film's message is not 'burn down the system' but 'do not let the system define your worth.' It champions personal initiative over institutional credentialing."
        },
        {
            "category": "Traditional",
            "trope": "Traditional Teen Romance",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "description": "Ferris and Sloane's relationship is straightforward, monogamous, and genuinely sweet. No love triangle, no sexual politics, no deconstruction. They are a couple who enjoy each other's company and face the world together. Sloane is capable but not masculinized; Ferris is confident but not domineering. A healthy teenage relationship presented without commentary."
        },
        {
            "category": "Traditional",
            "trope": "Nuclear Family as Functional Unit",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "description": "The Bueller parents are present, loving, and functional. They are not the problem - they are just easily deceived by a charming son. Ferris is not rebelling against his family; he is taking a day off from school, not from his life. His closing line about his sister Jeanie shows genuine sibling affection. The family unit is treated as normal and healthy, which is notable for an 80s teen film."
        }
    ],
    "spoiler_alert": False
}

# ──────────────────────────────────────────────
# REVIEW 3: The Last of Us (2023)
# ──────────────────────────────────────────────
tlou = {
    "id": "the-last-of-us-2023",
    "slug": "the-last-of-us-2023",
    "title": "The Last of Us",
    "year": 2023,
    "type": "series",
    "platform": "HBO / Max",
    "genre": "Post-Apocalyptic Drama, Thriller",
    "date": "2026-09-02",
    "datePublished": "2026-09-02",
    "author": "VirtueVigil Editorial Team",
    "readTime": "9 min",
    "poster": "/images/posters/the-last-of-us-2023.jpg",
    "releaseDate": "2023-01-15",
    "rating": "TV-MA (Violence, Language, Sexual Content, Disturbing Imagery)",
    "runtime": "2 seasons, 16 episodes (43-81 min each) - Season 3 filming 2026",
    "director": "Craig Mazin (showrunner), Neil Druckmann (showrunner)",
    "writers": ["Craig Mazin", "Neil Druckmann", "Halley Gross"],
    "cast": [
        {"name": "Pedro Pascal", "role": "Joel Miller"},
        {"name": "Bella Ramsey", "role": "Ellie Williams"},
        {"name": "Gabriel Luna", "role": "Tommy Miller"},
        {"name": "Isabela Merced", "role": "Dina"},
        {"name": "Young Mazino", "role": "Jesse"},
        {"name": "Kaitlyn Dever", "role": "Abby Anderson"},
        {"name": "Anna Torv", "role": "Tess"},
        {"name": "Nick Offerman", "role": "Bill"},
        {"name": "Murray Bartlett", "role": "Frank"},
        {"name": "Jeffrey Wright", "role": "Isaac"}
    ],
    "studio": "Sony Pictures Television / PlayStation Productions / Naughty Dog",
    "distributor": "HBO",
    "verdict": "TRADITIONAL",
    "wokeScore": 16.75,
    "tradScore": 31.25,
    "authIndex": 72,
    "scoreMargin": "+15 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "The Last of Us does not qualify as a woke trap despite significant LGBTQ content across both seasons. Season 1's Bill/Frank episode (episode 3) and Left Behind flashback (episode 7) establish LGBTQ themes early and openly. Season 2's Ellie/Dina relationship and the structural shift toward Abby are visible from their respective season premieres. Nothing is hidden past the 50% mark - the show's ideological commitments are worn on its sleeve from the start. Viewers know what they are getting."
    },
    "seo": {
        "titleTag": "Is The Last of Us (2023) Woke? HBO Series Full VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of The Last of Us (2023), HBO's hit post-apocalyptic drama starring Pedro Pascal and Bella Ramsey. Full 2-season tropes scored. Verdict: TRADITIONAL (+15 TRAD). Parental guidance included.",
        "keywords": "is the last of us woke, the last of us 2023 review, the last of us virtuevigil, the last of us traditional or woke, the last of us parents guide, pedro pascal joel, bella ramsey ellie, is last of us hbo woke"
    },
    "externalScores": {
        "imdb": "8.7/10",
        "rottenTomatoes": "96%",
        "metacritic": "84"
    },
    "creative_team": {
        "director": "Craig Mazin, Neil Druckmann (showrunners)",
        "writer": "Craig Mazin, Neil Druckmann, Halley Gross",
        "lead_producer": "Craig Mazin",
        "composer": "Gustavo Santaolalla",
        "top_cast": ["Pedro Pascal", "Bella Ramsey", "Kaitlyn Dever", "Gabriel Luna", "Isabela Merced"],
        "full_cast": ["Pedro Pascal", "Bella Ramsey", "Kaitlyn Dever", "Gabriel Luna", "Isabela Merced", "Young Mazino", "Anna Torv", "Nick Offerman", "Murray Bartlett", "Jeffrey Wright"],
        "producers": ["Craig Mazin", "Neil Druckmann", "Carolyn Strauss", "Rose Lam", "Evan Wells"]
    },
    "fidelityCasting": "Bella Ramsey, who is non-binary, plays the female lead Ellie. This is a notable departure from the video game source material, where Ellie was modeled and voiced by a female actor (Ashley Johnson). The casting received mixed audience reception; Ramsey's performance received critical acclaim, though some viewers noted the physical divergence from the game's version of the character.",
    "summary": {
        "overall": "The Last of Us is the best argument HBO could make that prestige television can still carry traditional values even when it checks every progressive box on the diversity checklist. Across two seasons (with a third on the way), the series adaptation of Naughty Dog's video game franchise tells a story that is, at its core, about a father's love - a broken, violent, morally compromised father whose decision to save his surrogate daughter at the cost of humanity's potential cure is the defining moral moment of the entire narrative. Pedro Pascal's Joel Miller is one of the most traditionally masculine protagonists on television in years: competent, protective, emotionally reserved, and willing to commit unspeakable violence to protect what is his. The show earns its traditional credentials through this character and through Bella Ramsey's wounded, fierce Ellie. The complication - and the reason this is not a STRONGLY TRADITIONAL verdict - is Season 2, which structurally dismantles the hero narrative Season 1 built. Joel's death at Abby's hands early in the second season is not just a plot twist; it is a moral argument that his actions in Season 1 were monstrous rather than heroic, and the subsequent episodes demand the audience sympathize with his killer. This is where the show's progressive commitments show their hand. Season 1 features a standalone episode about Bill and Frank, a gay couple in the apocalypse, that is among the finest hours of television in recent memory - not because of their sexuality but because it tells a universal story of love and devotion. Season 1's Left Behind episode introduces Ellie's sexuality with similar restraint and skill. Season 2 makes Ellie's relationship with Dina more central and places a physically imposing female antagonist (Abby) in the protagonist role by season's end. The show does not lecture; it integrates its progressive elements into character-driven storytelling. But the moral framework of Season 2 - that there are 'no heroes, only perspectives' - is the kind of moral relativism that conservatives have long identified as a progressive project. For parents weighing whether to let teens watch: the show is genuinely great television. It is also genuinely violent, and its Season 2 turn will be a breaking point for viewers who want their heroes to stay heroes. The traditional values in Season 1 are strong enough to carry the overall verdict into TRADITIONAL territory, but the gap is closing.",
        "adultInsight": "The Last of Us rewards adult viewers who can hold two thoughts at once: that Joel's choice to save Ellie was both an act of love and a profound moral failure, and that the show's attempt to make Abby sympathetic in Season 2 is both narratively ambitious and ideologically loaded. The craft is undeniable - the production design, the performances, Gustavo Santaolalla's score. But Season 2 asks a lot of viewers who invested in Joel as a hero, and not all of them will want to pay that price. The Bill and Frank episode in Season 1 is an all-timer regardless of one's views on the content.",
        "parentalGuidance": "This is TV-MA for a reason and is not appropriate for children or young teens. The violence is graphic and frequent: headshots, dismemberment, people being torn apart by infected, a character's face beaten to death with a golf club (Season 2). The show deals with suicide, sexual assault implications, child endangerment, and profound moral darkness. The Bill/Frank episode depicts a loving gay relationship including a sex scene (tasteful but present). Ellie's relationship with Dina includes kissing and intimate scenes. The language is strong throughout. For mature older teens (17+) with parental guidance, the show can spark meaningful conversations about love, sacrifice, moral choice, and the cycle of violence. But know your kid - this is heavy material."
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "Paternal Protection as Ultimate Virtue",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 11.25,
            "description": "Joel's entire character arc - and the moral center of the series - is his decision to protect Ellie at any cost. He massacres a hospital full of Fireflies, potentially dooming humanity to a continued cordyceps plague, to save a girl who has become his daughter. The show presents this as morally complex but emotionally true: a father's love overriding every other consideration. This is the most traditional value the series traffics in, and it is the axis on which the entire story turns."
        },
        {
            "category": "Traditional",
            "trope": "Family as Ultimate Value",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 9.0,
            "description": "Every positive outcome in The Last of Us flows from family bonds - Joel and Ellie's found family, Tommy and Maria's marriage and community in Jackson, even Bill and Frank's decades-long partnership. The Jackson settlement works precisely because it is organized around family units and communal mutual obligation rather than revolutionary ideology. The Fireflies, by contrast, are willing to sacrifice a child for abstract goals."
        },
        {
            "category": "Traditional",
            "trope": "Sacrifice for Loved Ones",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 9.0,
            "description": "From Tess's self-sacrifice in episode 2 to Joel's bloody rampage in the finale, characters repeatedly give up everything - their lives, their souls, the fate of civilization - for the people they love. The show consistently frames this as admirable rather than foolish. Henry's suicide after being forced to kill his infected brother Sam is devastating because the bond was everything."
        },
        {
            "category": "Traditional",
            "trope": "Survival Competence and Self-Reliance",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 3.0,
            "description": "Characters survive through practical competence: Joel's violence and wilderness skills, Ellie's quick thinking, Bill's prepper paranoia. The world of The Last of Us rewards capability, not ideology. There are no safe spaces, no administrative solutions to cordyceps. The show respects the conservative insight that civilization is thinner than we think and that competent individuals matter more than systems when things fall apart."
        },
        {
            "category": "Woke",
            "trope": "LGBTQ Representation as Central Narrative",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 6.0,
            "description": "HBO devotes an entire episode (S1E3 'Long, Long Time') to Bill and Frank's gay relationship, and Ellie's sexuality is a significant subplot across both seasons. The representation is artful rather than preachy - Bill and Frank's story is genuinely moving television - but the sheer amount of narrative real estate devoted to LGBTQ relationships exceeds what is proportionate to the source material and to the broader plot. Season 2 centers Ellie and Dina's relationship prominently."
        },
        {
            "category": "Woke",
            "trope": "Non-Traditional Gender Casting",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "description": "Bella Ramsey, who identifies as non-binary, plays the female lead Ellie. While Ramsey's performance has been widely praised, the casting diverges significantly from the video game's character design, where Ellie was modeled on and voiced by Ashley Johnson. This affects viewer immersion for those familiar with the source material. The impact on the show itself is minor; the trope registers more as a casting signal than a narrative choice."
        },
        {
            "category": "Woke",
            "trope": "Moral Relativism and Destruction of the Traditional Hero",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 9.0,
            "description": "Season 2 kills Joel brutally early and demands the audience spend the rest of the season sympathizing with Abby, his killer. The narrative framework argues that heroism is a matter of perspective and that Joel's Season 1 choices were monstrous rather than heroic. This is the show's most aggressively progressive move: the structural argument that traditional masculine protectors are actually villains when viewed from the right angle. The 'both sides' moral framing is a textbook progressive project."
        },
        {
            "category": "Woke",
            "trope": "Physically Dominant Female Antagonist",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.0,
            "description": "Abby's hyper-muscular physique is central to her character design in a way that subverts traditional gender expectations. She is presented as a physical match for any male character, capable of brutal hand-to-hand violence. While this serves a legitimate narrative purpose (she has trained obsessively for revenge), the character design leans into a broader cultural pattern of depicting women with male-coded physical traits as aspirational."
        }
    ],
    "spoiler_alert": True
}

new_reviews = [tony, ferris, tlou]

# Validate each review
for r in new_reviews:
    assert 'seo' in r, f'{r["id"]} missing seo'
    assert 'titleTag' in r['seo'], f'{r["id"]} missing seo.titleTag'
    assert 'metaDescription' in r['seo'], f'{r["id"]} missing seo.metaDescription'
    assert 'keywords' in r['seo'], f'{r["id"]} missing seo.keywords'
    assert 'summary' in r, f'{r["id"]} missing summary'
    assert 'overall' in r['summary'], f'{r["id"]} missing summary.overall'
    assert 'adultInsight' in r['summary'], f'{r["id"]} missing summary.adultInsight'
    assert 'parentalGuidance' in r['summary'], f'{r["id"]} missing summary.parentalGuidance'
    assert isinstance(r['summary'].get('parentalGuidance', ''), str), f'{r["id"]} missing summary.parentalGuidance'
    assert 'tropes' in r, f'{r["id"]} missing tropes'
    assert len(r['tropes']) >= 3, f'{r["id"]} too few tropes'
    # Check no em dashes in any string field
    import re
    def check_em_dash(obj, path=''):
        if isinstance(obj, str):
            if '\u2014' in obj or '\u2013' in obj or '--' in obj:
                # allow -- in some contexts like scoreMargin
                if '--' in obj and path not in ['scoreMargin']:
                    # but -- is fine in prose; em dashes are the real problem
                    pass
            if '\u2014' in obj:  # em dash
                print(f'EM DASH FOUND in {r["id"]} at {path}: ...{obj[max(0,obj.index(chr(8212))-20):obj.index(chr(8212))+20]}...')
                return True
            if '\u2013' in obj:  # en dash
                print(f'EN DASH FOUND in {r["id"]} at {path}: ...{obj[max(0,obj.index(chr(8213))-20):obj.index(chr(8213))+20]}...')
                return True
        elif isinstance(obj, dict):
            for k, v in obj.items():
                if check_em_dash(v, f'{path}.{k}'):
                    return True
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                if check_em_dash(v, f'{path}[{i}]'):
                    return True
        return False
    
    # Actually, let me just check for em dash in summary prose
    for field in ['overall', 'adultInsight', 'parentalGuidance']:
        val = r['summary'].get(field, '')
        if isinstance(val, str) and '\u2014' in val:
            print(f'EM DASH FOUND in {r["id"]} summary.{field}')
    
    print(f'  ✓ {r["id"]}: verdict={r["verdict"]}, woke={r["wokeScore"]}, trad={r["tradScore"]}, margin={r["scoreMargin"]}, seo=OK, tropes={len(r["tropes"])}')

# Append
data.extend(new_reviews)

with open(REVIEWS_PATH, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'\nTotal reviews now: {len(data)}')
print('Done.')