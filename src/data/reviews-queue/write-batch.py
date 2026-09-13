#!/usr/bin/env python3
"""Write 3 VirtueVigil reviews for 2026-09-13 to the reviews queue."""

import json, os, sys

REQUIRED_FIELDS = [
    "id", "slug", "title", "year", "type", "platform", "genre",
    "date", "datePublished", "author", "readTime", "poster",
    "releaseDate", "rating", "runtime", "director", "writers",
    "cast", "studio", "distributor", "verdict", "wokeScore",
    "tradScore", "authIndex", "scoreMargin", "preRelease",
    "wokeTrap", "woke_trap_assessment", "seo", "externalScores",
    "creative_team", "fidelityCasting", "parentalGuidance",
    "spoiler_alert", "summary", "tropeAudit"
]

OUT_PATH = "/Users/joestrazza/virtuevigil/src/data/reviews-queue/2026-09-13-batch.json"

# ── REVIEW 1: The Fix (2026) ──────────────────────────────────────────────
review_1 = {
    "id": "the-fix-2026",
    "slug": "the-fix-2026",
    "title": "The Fix",
    "year": 2026,
    "type": "film",
    "platform": "Theaters",
    "genre": "Action / Thriller",
    "date": "2026-09-13",
    "datePublished": "2026-09-13",
    "author": "VirtueVigil Editorial Team",
    "readTime": "10 min",
    "poster": "/images/posters/the-fix-2026.jpg",
    "releaseDate": "2026-09-11",
    "rating": "R (Violence, Language, Brief Drug Use)",
    "runtime": "141 min",
    "director": "Guy Moshe",
    "writers": [
        "Guy Moshe",
        "Mark Bacci",
        "Ron Hutchinson"
    ],
    "cast": [
        {"name": "Zachary Levi", "role": "Tucker"},
        {"name": "Liam Neeson", "role": "Larry"},
        {"name": "Annet Mahendru", "role": "Sophie"},
        {"name": "Grant Harvey", "role": "Matt"},
        {"name": "Augusto Aguilera", "role": "Bruce"},
        {"name": "Elnaaz Norouzi", "role": "Zara"},
        {"name": "Wes Chatham", "role": "Alex"},
        {"name": "Despina Mirou", "role": "Katarina"},
        {"name": "Oliver Trevena", "role": "Colonel Wilkes"},
        {"name": "Lara Wolf", "role": "Maryam"}
    ],
    "studio": "Astral Future / Latigo Films / Dreamtime Films",
    "distributor": "Briarcliff Entertainment / Inaugural Entertainment",
    "verdict": "BALANCED TRADITIONAL",
    "wokeScore": 1.80,
    "tradScore": 8.62,
    "authIndex": 65,
    "scoreMargin": "+7 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_score": 1.80,
    "trad_score": 8.62,
    "score_margin": 6.82,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "The Fix does not qualify as a woke trap under VVWS v1.1. A woke trap requires negative margin with woke content hidden past 50% runtime. This film carries a +7 TRAD margin and its minor cynical/war-is-futile framing is visible throughout. The core narrative is a redemption-through-heroic-action story with team loyalty as the central value. No bait-and-switch."
    },
    "seo": {
        "titleTag": "Is The Fix (2026) Woke? Liam Neeson & Zachary Levi Action Thriller Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of The Fix (2026). Liam Neeson and Zachary Levi star as former CIA operators in Tehran. Verdict: BALANCED TRADITIONAL (+7). Parental guidance included.",
        "keywords": [
            "is the fix 2026 woke",
            "the fix movie review",
            "the fix virtuevigil",
            "the fix liam neeson zachary levi",
            "the fix traditional or woke",
            "the fix parents guide",
            "the fix 2026 conservative review",
            "liam neeson the fix review",
            "zachary levi the fix movie"
        ]
    },
    "externalScores": {
        "rottenTomatoesCritic": 19,
        "rottenTomatoesAudience": 79,
        "imdb": 0,
        "metacritic": 0,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "TBD",
        "globalBoxOffice": "TBD (wide release Sept 11, 2026)"
    },
    "summary": {
        "overview": "The Fix (2026) is an action thriller directed by Guy Moshe and starring Zachary Levi as Tucker, a former CIA operative disillusioned by the end of the Afghanistan war. When a former teammate is trapped in Tehran and a life-changing score is on the table, Tucker and his crew, led by the grizzled Larry (Liam Neeson), mount a daring rescue operation that spirals into something far more dangerous than they anticipated. The supporting cast includes Annet Mahendru as Sophie, Grant Harvey as Matt, and Wes Chatham as Alex. It is a globe-spanning heist-rescue hybrid set against the backdrop of post-withdrawal CIA disaffection.",
        "overall": "The Fix is a movie that critics have dismissed and audiences have embraced, and that split tells you most of what you need to know. At 19% on Rotten Tomatoes from critics versus 79% from audiences, the gap is not just about taste. It is about the kind of story this is and who it is for.\n\nThe premise is a Rotten Tomatoes trigger warning all by itself: former CIA operators, disillusioned by the Afghanistan withdrawal, mounting an off-the-books mission in Tehran. That is red meat for an audience that remembers the botched withdrawal and feels something about it, and it is precisely the kind of premise that makes critics reach for words like 'overlong' and 'narrative contrivances.' Both things can be true. The Fix is overlong at 141 minutes, and it does have narrative contrivances. But it also has tense sequences, committed performances, and a moral framework that is going to land differently with different viewers.\n\nThe ideological center of this film is the bond between Tucker and Larry. Zachary Levi, fresh off his public break with Hollywood orthodoxy, brings a sincerity to Tucker that the script does not always earn. Liam Neeson, now in his seventies and firmly in the 'grizzled mentor' phase of his action career, plays Larry as a man who has seen too much and still shows up. Their relationship is the film's anchor: an older man who still believes in the mission and a younger man who has lost faith, both willing to risk everything for their people. That is a traditional value dressed in modern action-movie clothing.\n\nThe cynical notes are real and should be noted. The Afghanistan frame is not neutral. Lines about being 'used and discarded' by the country they served carry a war-is-futile undertone that will grate on some viewers. The filmmakers are not making a conservative movie. They are making a movie about loyalty and redemption that happens to use post-war disillusionment as its emotional starting point. That does not make it woke. It makes it a story about men trying to find purpose after their purpose was taken from them, which is a far more interesting tension than a simple flag-waving action picture.\n\nThe diverse cast is justified by the Tehran setting. Annet Mahendru, Elnaaz Norouzi, Lara Wolf, and others play characters whose presence in Iran makes narrative sense. This is not a diversity checklist. It is casting that serves the geography and the story. No one is lecturing anyone about representation. Everyone is just trying to survive the mission.\n\nThe Fix is not a great movie. But it is a fundamentally honest one. It wants you to care about the mission and the men on it, and it does not apologize for that. In a genre where apologizing has become standard operating procedure, that honesty is worth something.",
        "adultInsight": "The Fix matters because it represents something rare in 2026 action cinema: a film that is willing to treat post-withdrawal CIA disillusionment as emotional fuel for a heroic story rather than an indictment of American foreign policy. It does not wave a flag, but it does honor the bond between men who served together. The cynicism is present, but it is the starting point, not the conclusion. The arc bends toward redemption. For viewers who feel abandoned by a culture that treats military service as either tragedy or propaganda, The Fix offers a third option: a story where the mission still matters because the people on it matter. That is a small thing, but small things add up.",
        "parentalGuidance": "Rated R for violence, language, and brief drug use. The film contains extended action sequences with firearms, hand-to-hand combat, and explosions. Several characters are killed, though the violence is stylized action-movie fare rather than graphic gore. Language is frequent. There is a tense sequence involving extraction under fire. A brief scene shows drug trafficking as part of the criminal underworld elements. Not for children. Appropriate for adults and older teens who enjoy Liam Neeson-style action thrillers."
    },
    "parentalGuidance": {
        "rating": "R",
        "contentWarnings": "Extended action violence including gunfights, hand-to-hand combat, and explosions. Frequent strong language. Brief drug-related content. Thematic material about post-war disillusionment, loss of purpose, and criminality. No sexual content of note.",
        "ageRecommendation": "16+. The violence is stylized action fare rather than graphic, but the subject matter and runtime are adult. Younger viewers will not engage with the post-war disillusionment themes.",
        "discussionTopics": [
            "How does the film handle post-war disillusionment: as a condition to be overcome or a permanent state?",
            "Is loyalty to your team a sufficient moral justification for illegal action?",
            "What does the film suggest about the relationship between institutional failure and personal honor?",
            "Why do critics and audiences see this film so differently, and what does that gap reveal?"
        ]
    },
    "creative_team": {
        "director": {
            "name": "Guy Moshe",
            "role": "Director",
            "note": "Moshe is an Israeli-born director whose previous work includes Bunraku (2010) and LX 2048 (2020). His films tend toward stylized genre work without overt ideological signaling. The Fix is his most mainstream commercial project to date."
        },
        "writers": [
            {"name": "Guy Moshe", "role": "Screenwriter"},
            {"name": "Mark Bacci", "role": "Screenwriter"},
            {"name": "Ron Hutchinson", "role": "Screenwriter"}
        ],
        "lead_producer": {
            "name": "Guy Moshe",
            "role": "Producer"
        },
        "composer": {
            "name": "Various",
            "role": "Composer"
        },
        "top_cast": [
            {"name": "Zachary Levi", "role": "Tucker"},
            {"name": "Liam Neeson", "role": "Larry"},
            {"name": "Annet Mahendru", "role": "Sophie"},
            {"name": "Grant Harvey", "role": "Matt"},
            {"name": "Augusto Aguilera", "role": "Bruce"},
            {"name": "Wes Chatham", "role": "Alex"}
        ],
        "full_cast": [
            {"name": "Zachary Levi", "role": "Tucker"},
            {"name": "Liam Neeson", "role": "Larry"},
            {"name": "Annet Mahendru", "role": "Sophie"},
            {"name": "Grant Harvey", "role": "Matt"},
            {"name": "Augusto Aguilera", "role": "Bruce"},
            {"name": "Elnaaz Norouzi", "role": "Zara"},
            {"name": "Wes Chatham", "role": "Alex"},
            {"name": "Despina Mirou", "role": "Katarina"},
            {"name": "Oliver Trevena", "role": "Colonel Wilkes"},
            {"name": "Lara Wolf", "role": "Maryam"}
        ],
        "producers": [
            {"name": "Guy Moshe", "role": "Producer"}
        ]
    },
    "fidelityCasting": {
        "assessment": "FAITHFUL",
        "explanation": "The Fix is an original screenplay set in contemporary Tehran. The diverse cast reflects the story's geography rather than a demographic agenda. Iranian characters are played by actors of Middle Eastern and South Asian descent (Elnaaz Norouzi is Iranian-born, Lara Wolf is of Iranian descent). The CIA team is multiethnic in a way that reflects actual Agency demographics. No race-swaps, gender-swaps, or fidelity violations."
    },
    "spoiler_alert": False,
    "tropeAudit": [
        {
            "id": "TRAD-FIX-001",
            "name": "Loyalty to teammates as highest value",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The entire plot is driven by team loyalty. Tucker and Larry risk their lives, their freedom, and a potential fortune to rescue their people. The film treats this as the natural and correct decision, never deconstructing or second-guessing it. When the team faces betrayal, loyalty is what separates the heroes from the villains."
        },
        {
            "id": "TRAD-FIX-002",
            "name": "Redemption through action",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.24,
            "explanation": "Tucker begins the film disillusioned and directionless after the Afghanistan withdrawal. His arc is explicitly redemptive: he finds purpose through action, not therapy. The film treats his disillusionment as something to overcome through duty and sacrifice, not something to marinate in."
        },
        {
            "id": "TRAD-FIX-003",
            "name": "Competence as virtue",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.96,
            "explanation": "The team's CIA training is framed as a genuine asset, not a mark of shame. Characters succeed because they are good at what they do. The film respects operational competence without irony."
        },
        {
            "id": "TRAD-FIX-004",
            "name": "Male friendship without deconstruction",
            "category": "Traditional",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 0.70,
            "explanation": "The bond between Tucker and Larry, and among the team broadly, is depicted as genuine and uncomplicated. No one rolls their eyes at male friendship or treats it as a pathology to be scrutinized."
        },
        {
            "id": "WOKE-FIX-001",
            "name": "Post-war disillusionment bordering on anti-military cynicism",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "explanation": "The film's emotional starting point is the Afghanistan withdrawal as a betrayal. Characters express bitterness about being 'used and discarded.' This could read as either a critique of specific policy decisions (traditional territory) or as a broader 'war is futile' message (woke territory). The film's arc toward redemption pushes it toward the former reading, but the early runtime is heavy with disillusionment."
        },
        {
            "id": "WOKE-FIX-002",
            "name": "CIA as morally compromised institution",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.10,
            "explanation": "There are faint notes of institutional critique, the CIA as an organization that uses people up and discards them, but this is more noir genre convention than ideological messaging. It serves the character motivation rather than driving a political argument."
        }
    ]
}

# ── REVIEW 2: Stand by Me (1986) ──────────────────────────────────────────
review_2 = {
    "id": "stand-by-me-1986",
    "slug": "stand-by-me-1986",
    "title": "Stand by Me",
    "year": 1986,
    "type": "film",
    "platform": "Streaming",
    "genre": "Coming-of-Age / Drama / Adventure",
    "date": "2026-09-13",
    "datePublished": "2026-09-13",
    "author": "VirtueVigil Editorial Team",
    "readTime": "9 min",
    "poster": "/images/posters/stand-by-me-1986.jpg",
    "releaseDate": "1986-08-22",
    "rating": "R (Language, Brief Violence, Thematic Material)",
    "runtime": "89 min",
    "director": "Rob Reiner",
    "writers": [
        "Raynold Gideon",
        "Bruce A. Evans"
    ],
    "cast": [
        {"name": "Wil Wheaton", "role": "Gordie Lachance"},
        {"name": "River Phoenix", "role": "Chris Chambers"},
        {"name": "Corey Feldman", "role": "Teddy Duchamp"},
        {"name": "Jerry O'Connell", "role": "Vern Tessio"},
        {"name": "Kiefer Sutherland", "role": "Ace Merrill"},
        {"name": "John Cusack", "role": "Denny Lachance"},
        {"name": "Richard Dreyfuss", "role": "The Writer (Adult Gordie)"}
    ],
    "studio": "Act III Productions",
    "distributor": "Columbia Pictures",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 0.72,
    "tradScore": 9.68,
    "authIndex": 80,
    "scoreMargin": "+14 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_score": 0.72,
    "trad_score": 9.68,
    "score_margin": 8.96,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Stand by Me predates the concept of woke traps by roughly thirty years. It carries a +14 TRAD margin and contains zero woke content. The film is a pre-woke artifact that treats male friendship, rural working-class life, and coming-of-age through genuine adversity with complete sincerity. No bait-and-switch of any kind."
    },
    "seo": {
        "titleTag": "Is Stand by Me (1986) Woke? Stephen King Coming-of-Age Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Stand by Me (1986), Rob Reiner's classic adaptation of Stephen King's The Body. A timeless story of boyhood friendship. Verdict: TRADITIONAL LEAN (+14). Parental guidance included.",
        "keywords": [
            "is stand by me woke",
            "stand by me review",
            "stand by me virtuevigil",
            "stand by me traditional or woke",
            "stand by me parents guide",
            "stand by me 1986 conservative review",
            "stephen king the body movie review",
            "stand by me river phoenix review",
            "rob reiner stand by me review",
            "stand by me 40th anniversary"
        ]
    },
    "externalScores": {
        "rottenTomatoesCritic": 92,
        "rottenTomatoesAudience": 94,
        "imdb": 8.1,
        "metacritic": 75,
        "oscarNominations": 1,
        "oscarCategories": "Best Adapted Screenplay",
        "budget": "$7,500,000",
        "globalBoxOffice": "$54,300,000"
    },
    "summary": {
        "overview": "Stand by Me (1986) is Rob Reiner's adaptation of Stephen King's 1982 novella The Body, starring Wil Wheaton as Gordie Lachance, a sensitive twelve-year-old boy in the summer of 1959. When Vern Tessio (Jerry O'Connell) overhears his older brother talking about a dead body near the train tracks, Gordie and his friends Chris (River Phoenix), Teddy (Corey Feldman), and Vern set out on a two-day hike to find it, hoping to become local heroes. Along the way, they face junkyard dogs, leeches, a speeding train, and the town's older bullies led by Ace Merrill (Kiefer Sutherland). But the real journey is inward: each boy is carrying something heavier than he knows how to name. Richard Dreyfuss narrates as the adult Gordie, a writer looking back on the friends who made him who he is.",
        "overall": "There is a moment in Stand by Me, about two-thirds of the way through, when Gordie tells a campfire story about a fat kid who gets his revenge. It is a gross, juvenile, genuinely funny story, and his friends listen to it with the rapt attention of boys who know this is what friendship looks like. They are not analyzing each other. They are not processing trauma. They are just there, together, and that is enough. That moment, as much as any in American cinema, is what VirtueVigil exists to celebrate.\n\nForty years after its release, Stand by Me remains the gold standard for stories about male friendship. It understands something that modern coming-of-age films have largely forgotten: boys do not bond through emotional disclosure. They bond through shared experience, shared risk, and the unspoken knowledge that the other guy will be there when it matters. Gordie and Chris do not sit down and talk about their feelings. They walk thirty miles, nearly get killed by a train, stand up to bullies with a gun neither of them wants to use, and somewhere in all of that, they become brothers.\n\nThe film's ideological purity is almost disorienting in 2026. There is nothing to flag. No lectures. No subversion of authority for its own sake. The boys respect Gordie's parents even though the parents are neglecting him in their grief. Chris is being groomed by his town as the next Chambers family failure, and he fights it not by blaming the system but by deciding to take the college prep courses anyway. The film's answer to adversity is resilience, not grievance. It treats poverty, abusive parents, and small-town stagnation as things you carry and overcome, not things that define you.\n\nThe rural Oregon setting is treated with affection, not condescension. Castle Rock, King's fictional small town, is a place of limited horizons but genuine community. The working-class parents are not villains. They are people doing their best with what they have. When Gordie's father says, of Denny's football talent, 'That's my boy,' and looks past Gordie, the film does not invite you to hate him. It invites you to understand him, which is harder and more honest.\n\nAnd then there is the ending. The adult Gordie types: 'I never had any friends later on like the ones I had when I was twelve. Jesus, does anyone?' That line has been quoted to death, but it is quoted to death because it is true. It lands because Stand by Me has earned it. The film has spent eighty-nine minutes showing you exactly what those friendships were, and by the time you reach that sentence, you miss them too.\n\nThis film came out the year before the culture wars went hot. It is a pre-woke artifact in the best sense: not because it is fighting anything, but because it has never heard of the fight. It just tells the truth about boys and friendship and growing up, and that truth turns out to be entirely traditional.",
        "adultInsight": "Stand by Me is forty years old now, and it has aged better than almost any other film from its era. Why? Because the things it values, friendship as a sacred bond, resilience through genuine adversity, the irreplaceable importance of a peer who believes in you, are not generational. They are human. The film's 40th anniversary re-release in 2026 is a chance to show your sons a version of boyhood that is not being made anymore: one where boys are allowed to be boys, where their struggles are real and their friendships are profound, and where no adult is standing just off-camera to explain what it all means. Watch it with your kids. They will see something they have been missing.",
        "parentalGuidance": "Rated R for language and brief violence. The language is frequent but authentically 12-year-old-boy profanity, not gratuitous. The violence includes a scene with a gun, a dead body that is shown but not exploited, and some scuffles with older bullies. The thematic material includes parental neglect, grief, and the social pressure of a small town that has already decided who you are. No sexual content. The R rating is a product of its era and the language; today it would likely be PG-13. Appropriate for thoughtful 12-year-olds and up, especially boys who will recognize themselves in these characters."
    },
    "parentalGuidance": {
        "rating": "R (would be PG-13 today)",
        "contentWarnings": "Frequent profanity from young boys, authentic to the period and characters. Brief violence including a confrontation with a gun. A dead body is shown without gore. Thematic material: parental grief and neglect, abusive home environments, coming-of-age through genuine risk. No sexual content.",
        "ageRecommendation": "12+. The R rating is a historical artifact of 1986 standards. The content is tamer than most modern PG-13 films. This is an excellent father-son viewing experience.",
        "discussionTopics": [
            "What does Chris mean when he says 'I'm never going to get out of this town'? Is his fate predetermined?",
            "How does Gordie's relationship with his father change when we learn about Denny?",
            "Why does the adult Gordie say he never had friends like the ones he had at twelve? What was special about those friendships?",
            "How does the film treat small-town working-class life: as a limitation or as a real community?"
        ]
    },
    "creative_team": {
        "director": {
            "name": "Rob Reiner",
            "role": "Director",
            "note": "Reiner was at the peak of his powers in 1986, coming off This Is Spinal Tap (1984) and about to make The Princess Bride (1987). His direction of the four young actors is the film's secret weapon: he treats their performances with absolute seriousness, never winking at the audience or softening the material. Reiner's later career drifted toward political advocacy, but in 1986 he was just a great storyteller."
        },
        "writers": [
            {"name": "Raynold Gideon", "role": "Screenwriter"},
            {"name": "Bruce A. Evans", "role": "Screenwriter"}
        ],
        "lead_producer": {
            "name": "Bruce A. Evans",
            "role": "Producer"
        },
        "composer": {
            "name": "Jack Nitzsche",
            "role": "Composer"
        },
        "top_cast": [
            {"name": "Wil Wheaton", "role": "Gordie Lachance"},
            {"name": "River Phoenix", "role": "Chris Chambers"},
            {"name": "Corey Feldman", "role": "Teddy Duchamp"},
            {"name": "Jerry O'Connell", "role": "Vern Tessio"},
            {"name": "Kiefer Sutherland", "role": "Ace Merrill"},
            {"name": "John Cusack", "role": "Denny Lachance"},
            {"name": "Richard Dreyfuss", "role": "The Writer (Adult Gordie)"}
        ],
        "full_cast": [
            {"name": "Wil Wheaton", "role": "Gordie Lachance"},
            {"name": "River Phoenix", "role": "Chris Chambers"},
            {"name": "Corey Feldman", "role": "Teddy Duchamp"},
            {"name": "Jerry O'Connell", "role": "Vern Tessio"},
            {"name": "Kiefer Sutherland", "role": "Ace Merrill"},
            {"name": "John Cusack", "role": "Denny Lachance"},
            {"name": "Richard Dreyfuss", "role": "The Writer (Adult Gordie)"},
            {"name": "Marshall Bell", "role": "Mr. Lachance"},
            {"name": "Frances Lee McCain", "role": "Mrs. Lachance"},
            {"name": "Bradley Gregg", "role": "Eyeball Chambers"},
            {"name": "Casey Siemaszko", "role": "Billy Tessio"}
        ],
        "producers": [
            {"name": "Bruce A. Evans", "role": "Producer"},
            {"name": "Raynold Gideon", "role": "Producer"},
            {"name": "Andrew Scheinman", "role": "Producer"}
        ]
    },
    "fidelityCasting": {
        "assessment": "FAITHFUL",
        "explanation": "Stand by Me is adapted from Stephen King's novella The Body (from the collection Different Seasons). The novella describes Gordie, Chris, Teddy, and Vern as white working-class boys in 1959 Maine (the film relocates to Oregon). The casting is period-accurate and faithful to the source material. No race-swaps or gender-swaps. Richard Dreyfuss as the adult Gordie was an inspired choice that the novella did not specify."
    },
    "spoiler_alert": False,
    "tropeAudit": [
        {
            "id": "TRAD-SBM-001",
            "name": "Male friendship as sacred bond",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "explanation": "The entire emotional architecture of the film is built on male friendship. Gordie and Chris's relationship is treated with complete sincerity: they save each other's lives, both literally and figuratively. Chris tells Gordie he will be a great writer someday. Gordie stands between Chris and a knife. The film treats this as the most natural thing in the world: boys who love each other without needing to say so."
        },
        {
            "id": "TRAD-SBM-002",
            "name": "Coming-of-age through genuine risk and adversity",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The boys are not shielded from difficulty. They hike thirty miles through the woods, face real physical danger, and confront death in a way that changes them. The film treats this as a necessary part of growing up, not as trauma to be managed by adults. No one is calling their parents to come get them."
        },
        {
            "id": "TRAD-SBM-003",
            "name": "Resilience over grievance",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.24,
            "explanation": "Chris is being destroyed by his town's expectations: his family are criminals, so everyone assumes he will be too. His response is not to complain about systemic injustice. It is to steal the milk money back, enroll in college prep courses, and try to be better. The film honors this as moral courage."
        },
        {
            "id": "TRAD-SBM-004",
            "name": "Respect for rural working-class life",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.96,
            "explanation": "Castle Rock is not mocked. Its limitations are real, but so are its people. The parents who fail their children are doing so out of grief, not malice. The film extends understanding to everyone, even the ones who do not deserve it."
        },
        {
            "id": "TRAD-SBM-005",
            "name": "Nostalgia treated as genuine, not ironic",
            "category": "Traditional",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 0.70,
            "explanation": "The frame narrative of the adult Gordie looking back contains zero irony. He is not deconstructing his childhood or apologizing for it. He is honoring it. The film trusts that sincerity will land, and it does."
        }
    ]
}

# ── REVIEW 3: Slow Horses (2022) ──────────────────────────────────────────
review_3 = {
    "id": "slow-horses-2022",
    "slug": "slow-horses-2022",
    "title": "Slow Horses",
    "year": 2022,
    "type": "series",
    "platform": "Apple TV+",
    "genre": "Spy Thriller / Black Comedy / Drama",
    "date": "2026-09-13",
    "datePublished": "2026-09-13",
    "author": "VirtueVigil Editorial Team",
    "readTime": "11 min",
    "poster": "/images/posters/slow-horses-2022.jpg",
    "releaseDate": "2022-04-01",
    "rating": "TV-MA (Violence, Language, Brief Nudity)",
    "runtime": "30 episodes, 40-53 min each (5 series); Series 6 premieres Sept 16, 2026",
    "director": "James Hawes, Jeremy Lovering, Saul Metzstein, Adam Randall",
    "writers": [
        "Will Smith",
        "Morwenna Banks",
        "Mark Denton",
        "Jonny Stockwood"
    ],
    "showrunner": "Will Smith",
    "cast": [
        {"name": "Gary Oldman", "role": "Jackson Lamb"},
        {"name": "Jack Lowden", "role": "River Cartwright"},
        {"name": "Kristin Scott Thomas", "role": "Diana Taverner"},
        {"name": "Jonathan Pryce", "role": "David Cartwright"},
        {"name": "Hugo Weaving", "role": "Frank Harkness"},
        {"name": "Saskia Reeves", "role": "Catherine Standish"},
        {"name": "Rosalind Eleazar", "role": "Louisa Guy"},
        {"name": "Christopher Chung", "role": "Roddy Ho"},
        {"name": "Aimee-Ffion Edwards", "role": "Shirley Dander"},
        {"name": "Sophie Okonedo", "role": "Ingrid Tearney"},
        {"name": "Katherine Waterston", "role": "Alison Dunn"},
        {"name": "Sope Dirisu", "role": "Sean Donovan"}
    ],
    "studio": "See-Saw Films / Flying Studio Pictures",
    "distributor": "Apple TV+",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 1.36,
    "tradScore": 9.12,
    "authIndex": 74,
    "scoreMargin": "+12 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_score": 1.36,
    "trad_score": 9.12,
    "score_margin": 7.76,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Slow Horses does not qualify as a woke trap. It carries a +12 TRAD margin and its ideological character is established from the first episode: competence honored over ideology, loyalty to your people, a politically incorrect hero who is secretly the most competent person in the room. The diverse casting is organically integrated into the contemporary MI5 setting. No bait-and-switch across five complete series."
    },
    "seo": {
        "titleTag": "Is Slow Horses (2022) Woke? Gary Oldman Apple TV+ Spy Series Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Slow Horses (Apple TV+, 2022-present). Gary Oldman stars as Jackson Lamb in the anti-woke spy thriller. Verdict: TRADITIONAL LEAN (+12). Parental guidance included.",
        "keywords": [
            "is slow horses woke",
            "slow horses review",
            "slow horses virtuevigil",
            "slow horses apple tv review",
            "slow horses traditional or woke",
            "slow horses parents guide",
            "gary oldman slow horses review",
            "slow horses conservative review",
            "mick herron slow horses series",
            "is slow horses worth watching"
        ]
    },
    "externalScores": {
        "rottenTomatoesCritic": 98,
        "rottenTomatoesAudience": 93,
        "imdb": 8.1,
        "metacritic": 0,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "TBD",
        "globalBoxOffice": "N/A (Apple TV+ series)"
    },
    "summary": {
        "overview": "Slow Horses (2022-present) is an Apple TV+ spy thriller based on Mick Herron's Slough House novels, starring Gary Oldman as Jackson Lamb, the flatulent, chain-smoking, verbally abusive head of Slough House, the administrative purgatory where MI5 sends its embarrassing failures. Lamb presides over a team of rejects: River Cartwright (Jack Lowden), a once-promising agent who botched a training exercise and will never live it down; Catherine Standish (Saskia Reeves), an alcoholic administrative savant haunted by her former boss's treason; Roddy Ho (Christopher Chung), an insufferable tech genius no one can stand; Louisa Guy (Rosalind Eleazar), competent but scarred by a partner's death; and Shirley Dander (Aimee-Ffion Edwards), aggressive and unmanageable. Across five completed series (and a sixth premiering September 2026), these rejects keep stumbling into real intelligence crises that the sleek, politically savvy agents at Regent's Park either miss or cause, while Kristin Scott Thomas's Diana Taverner, MI5's Second Desk, schemes to keep her own hands clean.",
        "overall": "Slow Horses is the best spy show on television by a margin that is almost embarrassing. It has nothing to do with gadgetry or geopolitics. It has everything to do with Gary Oldman giving the performance of his career as Jackson Lamb, a character who would be a villain in any other series and is instead its moral center.\n\nJackson Lamb is the anti-woke hero we did not know we needed and absolutely do not deserve. He is unkempt, flatulent, casually cruel, and physically repulsive. He eats terrible food with his mouth open. He insults everyone around him with surgical precision. He farts audibly and without apology. He is also the most brilliant intelligence officer in the service, a man who sees through every scheme, protects his people with a ferocity that borders on paternal, and has zero interest in what anyone thinks of him. Lamb is what happens when competence and loyalty are the only values that matter and everything else gets burned off like morning fog.\n\nThe ideological architecture of Slow Horses is fascinating because it is doing something genuinely subversive, just not in the direction anyone expected. The show satirizes British bureaucracy, institutional cowardice, political correctness, and the careerist rot at the top of the intelligence services. But it does not deconstruct the institution itself. MI5 is worth saving. The people who have corrupted it are not. Diana Taverner, played by Kristin Scott Thomas with ice-cold precision, is a political animal who treats field agents as disposable assets and mission integrity as a public relations problem. She is the show's real villain, not any foreign adversary, and her villainy is not ideological. It is bureaucratic. She is what happens when the Peter Principle meets zero accountability.\n\nThe Slough House team is diverse: Rosalind Eleazar, Christopher Chung, Sope Dirisu, and Sophie Okonedo bring a multiethnic cast to the ensemble. But the show wears this lightly. No one is there to represent anything. They are there because they are broken, and their brokenness has nothing to do with their identity. Louisa Guy's grief over her partner's death is the same grief any operative would carry. Roddy Ho is insufferable because of his personality, not his background. The show treats its characters as individuals first and demographic categories never. That is how it should be done.\n\nFive series in, Slow Horses has never once lectured its audience. It has never asked you to feel a certain way about anything except the characters. Its moral framework is simple and consistent: loyalty to your people is the highest virtue, competence is the measure of a person, and the system will eat you if you let it. That framework is not political. It is human. And in 2026, it feels like a cold drink of water in the desert.",
        "adultInsight": "Slow Horses matters because it proves a thesis that VirtueVigil has been advancing since day one: you can make great television without preaching. Gary Oldman's Jackson Lamb is a character who would be canceled in five minutes if he existed in the real world and had a Twitter account, and yet the show has run for five series, been renewed for a sixth, and holds a 98% critical approval rating. How? Because competence is the great unifier. When a character is genuinely good at what they do, audiences will forgive almost anything else. Slow Horses understands this. It trusts you to form your own judgments. That trust is the rarest thing in television, and it is why the show will be studied long after the message-delivery vehicles have been forgotten.",
        "parentalGuidance": "Rated TV-MA for violence, language, and brief nudity. The violence is spy-thriller grade: shootings, beatings, occasional torture, handled with British restraint rather than American gore. Language is frequent and creative, largely delivered by Gary Oldman's Jackson Lamb, who swears like a man who has exhausted all other forms of self-expression. Brief nudity in a few episodes across five series. Thematic material: institutional betrayal, murder, political corruption, suicide referenced. Not for children. Excellent for adults who enjoy smart, character-driven spy fiction."
    },
    "parentalGuidance": {
        "rating": "TV-MA",
        "contentWarnings": "Spy-thriller violence including shootings, beatings, and occasional torture sequences, handled with British restraint. Frequent profanity, often creative and character-driven. Brief nudity in isolated episodes. Thematic material: institutional corruption, murder, betrayal, suicide references, political manipulation.",
        "ageRecommendation": "16+. The violence is less graphic than most premium cable fare, but the moral complexity and bureaucratic cynicism are adult territory. Older teens who enjoy smart spy fiction will find it rewarding.",
        "discussionTopics": [
            "Jackson Lamb is objectively repulsive and also the show's moral center. What does this tell us about how we measure character?",
            "How does Slow Horses satirize MI5's bureaucracy without attacking the institution itself? Where is the line?",
            "Why is loyalty to your people treated as the highest virtue in the Slough House universe?",
            "How does the show handle its diverse cast without ever making identity the point?"
        ]
    },
    "creative_team": {
        "showrunner": {
            "name": "Will Smith",
            "role": "Showrunner / Creator",
            "note": "Will Smith (the UK comedian and writer, not the actor) adapted Mick Herron's novels with a deep respect for the source material. His background in British comedy gives the show its dark humor without ever undercutting the thriller stakes. His adaptation decisions consistently privilege character over message."
        },
        "writers": {
            "names": "Will Smith, Morwenna Banks, Mark Denton, Jonny Stockwood",
            "role": "Writers",
            "note": "The writing room draws heavily from British comedy and drama, with contributors from Peep Show, The Thick of It, and other UK series known for satirical bite without ideological agenda. The scripts respect Herron's novels and have not introduced progressive messaging absent from the source material."
        },
        "director": {
            "name": "James Hawes, Jeremy Lovering, Saul Metzstein, Adam Randall (rotating)",
            "role": "Directors",
            "note": "The directors rotate across series but maintain a consistent visual language: grimy, overcast London exteriors contrasting with the sterile glass of Regent's Park. James Hawes (Black Mirror, The Alienist) established the template and remains a key creative force."
        },
        "lead_producer": {
            "name": "See-Saw Films",
            "role": "Production Company",
            "note": "See-Saw has a track record of prestige literary adaptations (The King's Speech, The Power of the Dog, Heartstopper). Their involvement signals quality without a specific ideological signature."
        },
        "composer": {
            "name": "Daniel Pemberton, Toydrum",
            "role": "Composer"
        },
        "top_cast": [
            {"name": "Gary Oldman", "role": "Jackson Lamb"},
            {"name": "Jack Lowden", "role": "River Cartwright"},
            {"name": "Kristin Scott Thomas", "role": "Diana Taverner"},
            {"name": "Jonathan Pryce", "role": "David Cartwright"},
            {"name": "Hugo Weaving", "role": "Frank Harkness"},
            {"name": "Saskia Reeves", "role": "Catherine Standish"},
            {"name": "Rosalind Eleazar", "role": "Louisa Guy"},
            {"name": "Christopher Chung", "role": "Roddy Ho"}
        ],
        "full_cast": [
            {"name": "Gary Oldman", "role": "Jackson Lamb"},
            {"name": "Jack Lowden", "role": "River Cartwright"},
            {"name": "Kristin Scott Thomas", "role": "Diana Taverner"},
            {"name": "Jonathan Pryce", "role": "David Cartwright"},
            {"name": "Hugo Weaving", "role": "Frank Harkness"},
            {"name": "Saskia Reeves", "role": "Catherine Standish"},
            {"name": "Rosalind Eleazar", "role": "Louisa Guy"},
            {"name": "Christopher Chung", "role": "Roddy Ho"},
            {"name": "Aimee-Ffion Edwards", "role": "Shirley Dander"},
            {"name": "Sophie Okonedo", "role": "Ingrid Tearney"},
            {"name": "Katherine Waterston", "role": "Alison Dunn"},
            {"name": "Sope Dirisu", "role": "Sean Donovan"}
        ],
        "producers": [
            {"name": "See-Saw Films", "role": "Production Company"}
        ]
    },
    "fidelityCasting": {
        "assessment": "FAITHFUL",
        "explanation": "Slow Horses adapts Mick Herron's Slough House novels. The novels describe Jackson Lamb as an aging white man, which Gary Oldman embodies completely. The diverse MI5 cast reflects a contemporary London intelligence service and is consistent with Herron's descriptions. River Cartwright, Catherine Standish, and Roddy Ho are cast faithfully to their literary counterparts. No race-swaps or gender-swaps of consequence. The adaptation's casting decisions serve the characters, not demographic targets."
    },
    "spoiler_alert": {
        "present": True,
        "details": "This review discusses major plot points from Series 1 through 5, including character deaths, betrayals, and the overarching conspiracy involving Frank Harkness. Series 6 plot details are not discussed."
    },
    "tropeAudit": [
        {
            "id": "TRAD-SLH-001",
            "name": "Competence as the highest virtue",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "explanation": "The entire moral framework of Slow Horses is built on competence. Jackson Lamb is repulsive in every dimension except results, and the show treats those results as what matters. The Regent's Park characters are well-dressed, politically savvy, and utterly useless. The Slough House characters are disasters, but they get the job done. The show's contempt for the competent-looking incompetent and its respect for the incompetent-looking competent is its core ideological statement."
        },
        {
            "id": "TRAD-SLH-002",
            "name": "Loyalty to your people",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Lamb protects his people with a ferocity that borders on paternal. He insults them constantly and would kill anyone who actually threatened them. This is the organizing principle of Slough House: you are failures, you are mine, and no one gets to hurt you except me. The show honors this as the only kind of institutional loyalty worth having."
        },
        {
            "id": "TRAD-SLH-003",
            "name": "Patriotism without jingoism",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "explanation": "The characters serve MI5 because they believe in the mission, even when the institution has failed them. River Cartwright in particular is motivated by a genuine desire to protect his country. The show never mocks this. It treats patriotism as a legitimate motivation that the system has betrayed rather than a naive impulse to be deconstructed."
        },
        {
            "id": "TRAD-SLH-004",
            "name": "Satire of bureaucracy without institutional deconstruction",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "explanation": "Slow Horses savages MI5's internal politics, careerism, and risk-aversion, but it never suggests the institution itself should not exist. The show distinguishes between a corrupt leadership class and a legitimate national security function. This is a fundamentally conservative distinction: fix the people, not abolish the institution."
        },
        {
            "id": "TRAD-SLH-005",
            "name": "Jackson Lamb as anti-woke hero",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Lamb is entirely indifferent to how he is perceived. He does not perform virtue. He does not use the approved vocabulary. He says things that would end careers and does not care. The show frames this not as a character flaw to be corrected but as a form of integrity: Lamb is the only person in the service who tells the truth, and his unfiltered offensiveness is inseparable from that honesty."
        },
        {
            "id": "TRAD-SLH-006",
            "name": "Diverse casting organically integrated",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.40,
            "explanation": "The Slough House ensemble is diverse, but the show treats every character as an individual first. No one is their identity. No one lectures. Rosalind Eleazar, Christopher Chung, and Sope Dirisu are judged by their competence and loyalty, not their backgrounds. This is diversity done right: present without being the point."
        },
        {
            "id": "WOKE-SLH-001",
            "name": "Diana Taverner as institutional villain",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": 0.70,
            "explanation": "A case could be made that the show's most prominent female character being a cold, manipulative careerist is anti-woman subtext. The counter-reading is that Taverner is a specific character, not a statement, and that the show's other female characters (Catherine, Louisa, Shirley) are sympathetic. The complaint is theoretical and does not hold up against the text. Included for completeness."
        }
    ]
}

# ── Assemble and write ─────────────────────────────────────────────────────
reviews = [review_1, review_2, review_3]

# Ensure output directory
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

# Validate
all_ok = True
for i, review in enumerate(reviews):
    missing = [f for f in REQUIRED_FIELDS if f not in review]
    if missing:
        print(f"❌ Review {i+1} ({review.get('slug','?')}): MISSING {missing}")
        all_ok = False
    else:
        print(f"✅ Review {i+1} ({review['slug']}): {review['verdict']} ({review['scoreMargin']})")

if all_ok:
    with open(OUT_PATH, "w") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Wrote {len(reviews)} reviews to {OUT_PATH}")
    print(f"   File size: {os.path.getsize(OUT_PATH)}\u200d bytes")
else:
    print("\n❌ Validation failed. Fix missing fields before writing.")
    sys.exit(1)