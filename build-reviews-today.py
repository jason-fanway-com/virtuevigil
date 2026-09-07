#!/usr/bin/env python3
"""Build 3 reviews for Sept 7, 2026 and append to reviews.json"""
import json, sys, os

REVIEWS_FILE = "src/data/reviews.json"
with open(REVIEWS_FILE) as f:
    data = json.load(f)

original_count = len(data)

# ============================================================
# REVIEW 1: The Uprising (2026) -- New Release, pre-release
# ============================================================
review1 = {
    "id": "the-uprising-2026",
    "slug": "the-uprising-2026",
    "title": "The Uprising",
    "year": 2026,
    "type": "film",
    "platform": "Theaters (Sept 10, 2026)",
    "genre": "Action, Period Drama, Historical Epic",
    "date": "2026-09-07",
    "datePublished": "2026-09-07",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/the-uprising-2026.jpg",
    "releaseDate": "2026-09-10",
    "rating": "R (Violence, Brief Nudity, Disturbing Images)",
    "runtime": "128 minutes",
    "director": "Paul Greengrass",
    "writers": ["Paul Greengrass"],
    "cast": [
        {"name": "Andrew Garfield", "role": "The Ploughman"},
        {"name": "Jamie Bell", "role": "John Ball"},
        {"name": "Stephen Dillane", "role": "Simon Sudbury"},
        {"name": "Tom Hollander", "role": "King Richard II"},
        {"name": "Cosmo Jarvis", "role": "Wat Tyler"},
        {"name": "Thomasin McKenzie", "role": "Alice"},
        {"name": "Jonny Lee Miller", "role": "Sir Robert Hales"},
        {"name": "Woody Norman", "role": "Young Richard's Page"},
        {"name": "Katherine Waterston", "role": "Queen Mother Joan"}
    ],
    "studio": "Thank You Pictures, Supernix, Blumhouse Productions",
    "distributor": "Focus Features",
    "verdict": "PREDICTED: TRADITIONAL",
    "wokeScore": 11.28,
    "tradScore": 17.88,
    "authIndex": 61,
    "scoreMargin": "+7 TRAD",
    "preRelease": True,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Not a woke trap. The Uprising wears its class-warfare framing on its sleeve from the opening scene: crushing taxes on peasants, state sexual violence, a corrupt council ruling through a child-king. If anything, the film signals its politics so openly that the only surprise is the Robin Hood pivot at the end. There is no bait and switch here. The audience knows exactly what they are getting from Paul Greengrass and the 1381 Peasants' Revolt setting. The question is whether the political content is more classically populist or modern woke, and the answer is mixed enough to earn a Traditional verdict."
    },
    "seo": {
        "titleTag": "Is The Uprising (2026) Woke? Paul Greengrass's Robin Hood Origin Epic | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of The Uprising (2026), Paul Greengrass's Peasants' Revolt epic starring Andrew Garfield. Tax oppression sparks rebellion, ending in the birth of Robin Hood. Verdict: TRADITIONAL (+7 TRAD). Parental guidance included.",
        "keywords": "is the uprising woke, the uprising 2026 review, the uprising paul greengrass review, the uprising andrew garfield, the uprising robin hood origin, the uprising virtuevigil, 1381 peasants revolt movie, the uprising parents guide"
    },
    "externalScores": {
        "imdb": "N/A (Pre-Release)",
        "rottenTomatoes": "N/A (Pre-Release)",
        "metacritic": "N/A (Pre-Release)"
    },
    "creative_team": {
        "director": {
            "name": "Paul Greengrass",
            "ideology": "LEFT-LEANING (British Liberal)",
            "profile": "Paul Greengrass built his career on politically charged historical dramas (Bloody Sunday, United 93, Green Zone) and the Bourne action films. His worldview is left-of-center but more humanist than ideological: he is interested in how ordinary people respond when institutions fail them. Greengrass does not make propaganda. He makes films about systems and the people who get crushed by them, which can read as woke or populist depending on which system is being crushed. His signature handheld camera style gives his films a documentary urgency that resists easy moralizing."
        },
        "writer": {
            "name": "Paul Greengrass",
            "profile": "Greengrass wrote the screenplay himself, adapting the historical events of the 1381 Peasants' Revolt. The script draws clear parallels between medieval tax oppression and modern economic grievances but stops short of explicit contemporary commentary. The Robin Hood origin conceit is a genuinely clever narrative device that frames the revolt as the birth of a folk hero rather than merely a failed uprising."
        },
        "lead_producer": {
            "name": "Jason Blum, Paul Greengrass, Gregory Goodman",
            "company": "Blumhouse Productions / Thank You Pictures"
        },
        "composer": {
            "name": "Volker Bertelmann"
        },
        "top_cast": [
            {"name": "Andrew Garfield", "role": "The Ploughman"},
            {"name": "Jamie Bell", "role": "John Ball"},
            {"name": "Tom Hollander", "role": "King Richard II"},
            {"name": "Cosmo Jarvis", "role": "Wat Tyler"}
        ],
        "producers": ["Jason Blum", "Paul Greengrass", "Gregory Goodman", "Joanna Kaye", "Joe Neurauter", "Lars Sylvest"],
        "full_cast": [
            {"name": "Andrew Garfield", "role": "The Ploughman"},
            {"name": "Jamie Bell", "role": "John Ball"},
            {"name": "Stephen Dillane", "role": "Simon Sudbury"},
            {"name": "Tom Hollander", "role": "King Richard II"},
            {"name": "Cosmo Jarvis", "role": "Wat Tyler"},
            {"name": "Thomasin McKenzie", "role": "Alice"},
            {"name": "Jonny Lee Miller", "role": "Sir Robert Hales"},
            {"name": "Woody Norman", "role": "Young Richard's Page"},
            {"name": "Katherine Waterston", "role": "Queen Mother Joan"}
        ]
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "Common Man Against Tyranny (TRADITIONAL-008)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.60,
            "description": "The Ploughman is the archetypal common man driven to rebellion by an unjust system. He does not seek power. He seeks only to survive and, when that is denied, to fight back. The film frames his violence as reluctant and righteous: he kills only when the state leaves him no choice. This is the classic American and Western myth of the citizen who picks up arms against tyranny, transplanted to medieval England. Andrew Garfield plays him with the same wounded decency he brought to Hacksaw Ridge."
        },
        {
            "category": "Traditional",
            "trope": "Faith as Moral Compass (TRADITIONAL-043)",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.52,
            "description": "John Ball, the priest who joins the rebellion, is one of the film's three leaders. His egalitarian theology is portrayed as genuine Christian conviction, not political posturing. He quotes scripture to justify the revolt, and his imprisonment by the Church for heresy is depicted as institutional corruption rather than as an indictment of faith itself. The film takes Ball's priesthood seriously. The Church hierarchy may be the enemy, but the faith is not."
        },
        {
            "category": "Traditional",
            "trope": "Betrayal by Elites (TRADITIONAL-031)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "The king's betrayal is the film's emotional and moral center. Richard II, portrayed by Tom Hollander as a terrified teenager haunted by nightmares, promises the rebels self-determination and clemency, then has their leader murdered and their followers slaughtered in a trap. The message is unambiguous: the ruling class will say anything to preserve its power, and trusting them is fatal. This is populist rather than specifically woke: the film attacks the ruling class as corrupt, not the concept of hierarchy itself."
        },
        {
            "category": "Traditional",
            "trope": "The Destructive Nature of Greed (TRADITIONAL-039)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 2.88,
            "description": "The council's decision to tax the peasantry rather than the Church or merchant class is explicitly framed as greed dressed as governance. The tax collector's cruelty, the demand for death taxes on a man's dead family, the soldiers examining young women to determine tax status: every act of state power in the film is motivated by extraction. The film argues that a government that exists to take rather than to serve has forfeited its legitimacy."
        },
        {
            "category": "Traditional",
            "trope": "The Individual Versus the State (TRADITIONAL-014)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 3.84,
            "description": "The Ploughman begins as one man against the machinery of the state and ends as the leader of thousands. The film is fundamentally about what happens when the state becomes so predatory that individual resistance becomes collective revolution. This is a traditional framing of political action: the individual is the unit of moral agency, and collective action is legitimate only when grounded in individual grievance."
        },
        {
            "category": "Woke",
            "trope": "Class Warfare / Economic Justice (WOKE-007)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "The Peasants' Revolt is inherently a class-conflict story, and Greengrass does not soften this. The film draws a bright line between the suffering peasantry and the decadent ruling class. The peasants are virtuous, the nobles are corrupt, and the solution is violent redistribution of power. While this framing predates modern woke politics by centuries, it maps neatly onto contemporary progressive rhetoric about the 99% versus the 1%."
        },
        {
            "category": "Woke",
            "trope": "Anti-Religious Establishment (WOKE-005)",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.52,
            "description": "The Church hierarchy is portrayed as part of the oppressive establishment. John Ball is branded a heretic for preaching egalitarianism, and the Church is shown to be in league with the crown against the interests of ordinary people. However, the film distinguishes between the institutional Church (corrupt) and genuine faith (heroic), which moderates the severity of this trope."
        },
        {
            "category": "Minor Woke",
            "trope": "State Sexual Violence",
            "severity": 2,
            "authenticity": "Medium",
            "centrality": "Low",
            "weightedScore": 0.96,
            "description": "Early in the film, soldiers forcibly examine young women to determine whether they should be taxed as children or adults. This scene is brief but shocking, establishing the state's predation as not merely economic but physical. It serves the narrative purpose of justifying the Ploughman's violence and could be read as a #MeToo-era inclusion, though it is grounded in the historical reality of medieval tax collection."
        },
        {
            "category": "Minor Woke",
            "trope": "Egalitarian Redistribution",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Low",
            "weightedScore": 1.44,
            "description": "The rebels' demands include self-determination and economic justice, and the Robin Hood pivot at the end explicitly frames wealth redistribution as heroic. The film stops short of endorsing a specific economic program but clearly sides with the proposition that those who have too much should give to those who have too little. This is populist redistribution rather than Marxist revolution, but it is redistribution nonetheless."
        }
    ],
    "summary": {
        "overall": "The Uprising is Paul Greengrass doing what Paul Greengrass does best: taking a historical event, stripping it of romance, and filming it like a documentary that happens to have Andrew Garfield in the lead. Set during the 1381 Peasants' Revolt, the film follows a nameless Ploughman whose family has been destroyed by plague and whose livelihood is being destroyed by taxes. When he kills a soldier in self-defense, he accidentally starts a revolution. The film is gritty, violent, and visually muddy in the way all Greengrass films are, but it has a surprising final act: the Ploughman escapes the king's massacre, retreats to Sherwood Forest, and becomes Robin Hood. It is a genuinely clever origin story that recontextualizes the entire folk hero tradition as the aftermath of a failed popular uprising. The politics are populist rather than partisan, which is to say the film hates the ruling class but does not seem to have a specific alternative in mind beyond 'stop crushing the peasants.' Andrew Garfield anchors the film with wounded sincerity, and Tom Hollander's Richard II is a fascinating portrait of a terrified boy-king whose weakness is indistinguishable from cruelty.",
        "traditionalStrengths": "The Uprising is built on traditional foundations that predate the left-right binary. The common man rising against tyranny is the oldest story in the Western canon, and Greengrass tells it with conviction. The Ploughman is not an ideologue. He is a bereaved father and husband who has been pushed past the breaking point. His violence is reluctant and defensive. The film's treatment of faith through John Ball is nuanced: the Church hierarchy is corrupt, but the faith itself is genuine and animating. The king's betrayal is the film's darkest moment and carries the unmistakable message that power cannot be trusted. The ending, in which the Ploughman becomes Robin Hood and threatens the king from the shadows of Sherwood Forest, is a traditionalist's fantasy: the state cannot be reformed, but it can be resisted. This is not a film about building a better system. It is a film about refusing to accept a broken one.",
        "wokeElements": "The class-warfare framing is impossible to ignore. The film draws a bright line between virtuous peasants and villainous nobles in a way that maps cleanly onto modern progressive rhetoric about economic inequality. The state is portrayed as irredeemably predatory, with the genital-inspection scene serving as a blunt instrument to establish the regime's cruelty. The Church's complicity in oppression could be read as an anti-religious argument, though the film complicates this by making the rebel priest a figure of genuine moral authority. The Robin Hood pivot at the end frames wealth redistribution as heroic, which will please progressive audiences and annoy anyone who prefers their folk heroes apolitical. But these elements are embedded in a narrative structure that is fundamentally traditional: individual agency, reluctant violence, faith as a genuine moral force, and a deep suspicion of concentrated power regardless of its ideological justification.",
        "parentalGuidance": "Rated R for medieval battlefield violence including sword fighting, beheadings, and mass slaughter. The genital inspection scene is disturbing but not graphic. Brief nudity. Strong language is minimal given the period setting. The film's violence is brutal and matter-of-fact in the Greengrass style, not stylized or glorified. Not appropriate for children under 15. Parents should know the film takes a sympathetic view of violent rebellion against unjust authority, which may prompt conversations about when resistance is justified. The historical content is educational but grim.",
        "adultInsight": "The Uprising poses a question that will make everyone uncomfortable: when the state becomes predatory, is violence justified? The film's answer is a qualified yes, and it earns that qualification by showing exactly what state predation looks like: taxing the dead, humiliating young women, crushing families who have already lost everything. The film does not endorse revolution as a political program. It endorses resistance as a human response to inhumanity. The Robin Hood ending is the film's most subversive move: it suggests that the hero is not the one who wins the battle but the one who refuses to stop fighting after losing it. Greengrass has made a film that will be claimed by both the populist right and the progressive left, and the fact that it resists easy categorization is probably the point."
    }
}

# ============================================================
# REVIEW 2: Dead Poets Society (1989) -- Catalog Backfill
# ============================================================
review2 = {
    "id": "dead-poets-society-1989",
    "slug": "dead-poets-society-1989",
    "title": "Dead Poets Society",
    "year": 1989,
    "type": "film",
    "platform": "Amazon Prime / Digital Rental",
    "genre": "Drama, Coming-of-Age",
    "date": "2026-09-07",
    "datePublished": "2026-09-07",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/dead-poets-society-1989.jpg",
    "releaseDate": "1989-06-02",
    "rating": "PG (Thematic Elements, Brief Language, Teen Suicide)",
    "runtime": "128 minutes",
    "director": "Peter Weir",
    "writers": ["Tom Schulman"],
    "cast": [
        {"name": "Robin Williams", "role": "John Keating"},
        {"name": "Robert Sean Leonard", "role": "Neil Perry"},
        {"name": "Ethan Hawke", "role": "Todd Anderson"},
        {"name": "Josh Charles", "role": "Knox Overstreet"},
        {"name": "Gale Hansen", "role": "Charlie Dalton"},
        {"name": "Dylan Kussman", "role": "Richard Cameron"},
        {"name": "Allelon Ruggiero", "role": "Steven Meeks"},
        {"name": "James Waterston", "role": "Gerard Pitts"},
        {"name": "Norman Lloyd", "role": "Headmaster Gale Nolan"},
        {"name": "Kurtwood Smith", "role": "Mr. Perry"}
    ],
    "studio": "Touchstone Pictures, Silver Screen Partners IV",
    "distributor": "Buena Vista Pictures Distribution",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 14.04,
    "tradScore": 18.12,
    "authIndex": 56,
    "scoreMargin": "+4 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Dead Poets Society wears its themes openly from the first scene. Keating's 'carpe diem' philosophy and anti-authoritarian teaching methods are the film's entire premise, not a hidden agenda. There is no bait and switch: the film tells you exactly what it is about from the moment Robin Williams asks students to rip pages out of their poetry textbooks. The tragedy of Neil's suicide and the film's ambivalent ending mean the messaging is complicated rather than propagandistic."
    },
    "seo": {
        "titleTag": "Is Dead Poets Society (1989) Woke? Robin Williams Classic VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Dead Poets Society (1989), Peter Weir's coming-of-age classic starring Robin Williams. An English teacher inspires prep school boys to seize the day, with tragic consequences. Verdict: MILDLY TRADITIONAL (+4 TRAD).",
        "keywords": "is dead poets society woke, dead poets society 1989 review, dead poets society virtuevigil, dead poets society parents guide, robin williams dead poets society, carpe diem dead poets society, dead poets society traditional or woke"
    },
    "externalScores": {
        "imdb": "8.1/10",
        "rottenTomatoes": "84%",
        "metacritic": "79"
    },
    "creative_team": {
        "director": {
            "name": "Peter Weir",
            "ideology": "NONE (Humanist Storyteller)",
            "profile": "Peter Weir is one of cinema's great humanists, interested in the collision between individual spirit and institutional constraint across cultures (Gallipoli, Witness, The Truman Show, Master and Commander). His films resist ideological categorization because they take both sides of the individual-versus-system tension seriously. Dead Poets Society is not a polemic for or against traditional education. It is a film about what happens when a genuinely inspiring figure enters a system that cannot accommodate inspiration, and Weir is too honest a filmmaker to supply a clean resolution."
        },
        "writer": {
            "name": "Tom Schulman",
            "profile": "Schulman won the Academy Award for Best Original Screenplay for Dead Poets Society, drawing on his own experiences at a Tennessee prep school. Interestingly, his script was originally titled 'Sultans of String' and was conceived as a more comedic take before Peter Weir pushed it toward drama. Schulman's subsequent career did not produce another film of comparable cultural impact, making Dead Poets Society something of a one-hit wonder in screenwriting terms."
        },
        "lead_producer": {
            "name": "Steven Haft, Paul Junger Witt, Tony Thomas",
            "company": "Touchstone Pictures"
        },
        "composer": {
            "name": "Maurice Jarre"
        },
        "top_cast": [
            {"name": "Robin Williams", "role": "John Keating"},
            {"name": "Robert Sean Leonard", "role": "Neil Perry"},
            {"name": "Ethan Hawke", "role": "Todd Anderson"},
            {"name": "Kurtwood Smith", "role": "Mr. Perry"}
        ],
        "producers": ["Steven Haft", "Paul Junger Witt", "Tony Thomas"],
        "full_cast": [
            {"name": "Robin Williams", "role": "John Keating"},
            {"name": "Robert Sean Leonard", "role": "Neil Perry"},
            {"name": "Ethan Hawke", "role": "Todd Anderson"},
            {"name": "Josh Charles", "role": "Knox Overstreet"},
            {"name": "Gale Hansen", "role": "Charlie Dalton"},
            {"name": "Dylan Kussman", "role": "Richard Cameron"},
            {"name": "Allelon Ruggiero", "role": "Steven Meeks"},
            {"name": "James Waterston", "role": "Gerard Pitts"},
            {"name": "Norman Lloyd", "role": "Headmaster Gale Nolan"},
            {"name": "Kurtwood Smith", "role": "Mr. Perry"}
        ]
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "The Importance of Mentorship (TRADITIONAL-016)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "John Keating is one of cinema's great mentors, and the film takes his relationship with his students seriously. He does not merely teach poetry. He teaches them how to see. His methods are unconventional, but his goal is deeply traditional: the formation of character. The film's tragedy is that Keating cannot protect his students from the world outside his classroom, but it never suggests that his mentorship was a mistake. On the contrary, the final scene in which the students stand on their desks is one of the most powerful affirmations of the mentor-student bond ever filmed."
        },
        {
            "category": "Traditional",
            "trope": "Consequences of Rebellion (TRADITIONAL-019)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "This is where Dead Poets Society earns its traditional score. Neil Perry's rebellion against his father ends in suicide. Charlie Dalton's act of defiance gets him expelled. The film is explicit: rebellion has costs, and those costs can be fatal. Keating's philosophy of 'carpe diem' is beautiful, but the film shows what happens when a philosophy of individual expression collides with a world that does not care about your poetry. Neil's death is not the system's fault alone. It is the result of a father who cannot see his son and a son who cannot communicate with his father. The film distributes blame with painful even-handedness."
        },
        {
            "category": "Traditional",
            "trope": "Father-Son Relationships (TRADITIONAL-012)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "The relationship between Neil Perry and his father is the film's central conflict, and it is more nuanced than the 'authoritarian parent crushes free spirit' reading would suggest. Mr. Perry is a controlling, cold man who has mapped out his son's entire life. But the film also shows that he genuinely believes he is doing what is best for Neil. He is wrong, catastrophically wrong, but he is not a villain. He is a father who cannot see his son as a separate person. The film's treatment of this relationship is traditional in the deepest sense: it believes that fathers and sons matter, that their bond is sacred, and that its failure is tragedy, not liberation."
        },
        {
            "category": "Traditional",
            "trope": "Brotherhood and Male Friendship (TRADITIONAL-047)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 2.88,
            "description": "The Dead Poets Society is, at its heart, a brotherhood. The boys sneak out to a cave to read poetry together. They support each other through failure and tragedy. Charlie takes a beating rather than betray his friends. The film takes male friendship seriously as a site of moral formation and mutual support. This is not a 'boys will be boys' glorification but a genuine portrait of how young men form bonds that sustain them through difficulty."
        },
        {
            "category": "Woke",
            "trope": "Anti-Institutional Attitude (WOKE-002)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.96,
            "description": "Welton Academy is portrayed as a soul-crushing institution built on tradition, discipline, and conformity. The school's four pillars (Tradition, Honor, Discipline, Excellence) are exposed as hollow slogans. The headmaster is a bureaucrat who values order over life. The film is explicitly anti-institutional in its sympathies, aligning the audience entirely with Keating's subversive teaching methods and against the school's rigid structure."
        },
        {
            "category": "Woke",
            "trope": "Individualism Over Conformity (WOKE-003)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "Keating's entire pedagogy is built on the proposition that individual expression is more valuable than social conformity. He tells students to rip out textbook introductions, to walk their own way, to stand on desks and see the world differently. This is the film's most visible message and the one that has made it a touchstone for generations of students who felt crushed by institutional expectations. The film's progressive credentials on this score are unambiguous."
        },
        {
            "category": "Minor Woke",
            "trope": "Deconstruction of Traditional Authority (WOKE-008)",
            "severity": 2,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 1.68,
            "description": "The film systematically undermines every figure of traditional authority except Keating. The headmaster is a coward. Neil's father is a tyrant. The school board is faceless and punitive. Only the teacher who breaks the rules is worthy of respect. This is a mild but consistent anti-authoritarian thread that runs through the entire film."
        },
        {
            "category": "Minor Woke",
            "trope": "Suicide as Critique of Patriarchy (WOKE-013)",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.52,
            "description": "Neil's suicide can be read as an indictment of patriarchal parenting: his father's refusal to see him as anything other than a vessel for his own ambitions drives Neil to take his own life. The film does not frame this as Neil's failure but as the system's. However, the film is more complex than the simple 'patriarchy kills' reading. Neil's inability to confront his father directly is also a factor, and the film does not absolve him of agency. The tragedy is mutual, not didactic."
        }
    ],
    "summary": {
        "overall": "Dead Poets Society is the rare film that has been claimed by both conservatives and progressives for thirty-seven years, and the reason is that it contains enough ammunition for both sides. Robin Williams plays John Keating, an English teacher at a rigid Vermont prep school in 1959 who teaches his students that poetry is not about meter and rhyme but about passion, individuality, and seizing the day. His methods are thrilling and his students are transformed. One of them, Neil Perry, discovers a love of acting and defies his authoritarian father to perform in A Midsummer Night's Dream. His father withdraws him from school. Neil kills himself. The school blames Keating, who is fired. In the film's final scene, the students stand on their desks in silent defiance, saluting the teacher who taught them to think for themselves. The film works because it takes both sides of the freedom-versus-order equation seriously. Keating's philosophy is intoxicating, but it cannot protect his students from the world. Neil's father is cruel, but he is not a monster. The result is a film that is more complicated than either its fans or its detractors remember.",
        "traditionalStrengths": "Despite its reputation as an anti-establishment film, Dead Poets Society is built on deeply traditional foundations. Mentorship is sacred: Keating's relationship with his students is portrayed with genuine reverence, and the film argues that a great teacher can change lives. Father-son bonds are treated as existentially significant: Neil's tragedy is not that his father has expectations but that his father cannot see him. The film takes the father-son relationship seriously as something that matters, and Neil's death is the result of its failure, not its existence. Consequences are real: every act of rebellion in the film carries a cost. Charlie's defiance gets him expelled. Neil's gets him killed. The film does not endorse rebellion as a lifestyle. It shows it as a high-stakes gamble. Brotherhood is honored: the Dead Poets Society is a genuine community of young men supporting each other, and the film takes that seriously as a site of moral formation. The final 'O Captain! My Captain!' scene is not a rejection of authority but an affirmation of the right kind of authority: authority earned through love and wisdom rather than imposed by hierarchy.",
        "wokeElements": "The film's anti-institutional stance is its most visible political feature. Welton Academy is a monument to conformity, and the film systematically dismantles its pretensions. Keating's 'carpe diem' philosophy maps onto modern progressive individualism more comfortably than it maps onto any traditional framework. The film sides with the individual against the institution in every conflict, and while it shows the costs of this stance, it never repudiates it. Neil's suicide, read through a progressive lens, is an indictment of patriarchal parenting and the suppression of artistic identity. The film's elevation of self-expression over duty, passion over discipline, and poetry over pragmatism aligns with a worldview that prioritizes personal fulfillment over social obligation. But the film complicates every one of these readings by showing what happens when they are pursued without restraint, and its refusal to supply a clean moral makes it more honest than most films on either side of the culture war.",
        "parentalGuidance": "Rated PG but heavier than the rating suggests. Neil's suicide is depicted off-screen but is emotionally devastating and may be difficult for younger viewers. The film deals frankly with parental conflict, academic pressure, and the consequences of defiance. Brief language and mild romantic content. The thematic content is sophisticated and will resonate most with teenagers who have experienced academic pressure or conflict with parents. Parents should be prepared to discuss suicide, particularly given the film's nuanced treatment that does not offer easy answers about blame. The film could be valuable viewing for families willing to have those conversations, but it should not be treated as light entertainment.",
        "adultInsight": "The most adult thing about Dead Poets Society is what it refuses to resolve. The film has been argued over for decades because it does not tell you whose fault Neil's death is. Mr. Perry's authoritarian parenting? Neil's inability to confront his father? Keating's philosophy, which gave Neil the courage to defy his father but no tools to survive the consequences? The school's rigid institutional culture? All of them. The film distributes blame across every character and institution, and its wisdom is that there is no single answer. Keating is right that poetry matters, but he is also wrong that passion is enough to survive on. Mr. Perry is wrong to crush his son's dreams, but he is also right that dreams do not pay bills. The film is not about choosing between tradition and individuality. It is about the impossibility of choosing, and the tragedy that results when the choice is forced."
    }
}

# ============================================================
# REVIEW 3: Brokeback Mountain (2005) -- Catalog Backfill
# ============================================================
review3 = {
    "id": "brokeback-mountain-2005",
    "slug": "brokeback-mountain-2005",
    "title": "Brokeback Mountain",
    "year": 2005,
    "type": "film",
    "platform": "Peacock / Digital Rental",
    "genre": "Romantic Drama, Neo-Western",
    "date": "2026-09-07",
    "datePublished": "2026-09-07",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/brokeback-mountain-2005.jpg",
    "releaseDate": "2005-12-09",
    "rating": "R (Sexuality, Nudity, Language, Some Violence)",
    "runtime": "134 minutes",
    "director": "Ang Lee",
    "writers": ["Larry McMurtry", "Diana Ossana"],
    "cast": [
        {"name": "Heath Ledger", "role": "Ennis Del Mar"},
        {"name": "Jake Gyllenhaal", "role": "Jack Twist"},
        {"name": "Michelle Williams", "role": "Alma Beers Del Mar"},
        {"name": "Anne Hathaway", "role": "Lureen Newsome Twist"},
        {"name": "Randy Quaid", "role": "Joe Aguirre"},
        {"name": "Linda Cardellini", "role": "Cassie Cartwright"},
        {"name": "Anna Faris", "role": "Lashawn Malone"},
        {"name": "David Harbour", "role": "Randall Malone"},
        {"name": "Roberta Maxwell", "role": "Jack's Mother"},
        {"name": "Peter McRobbie", "role": "John Twist"}
    ],
    "studio": "River Road Entertainment",
    "distributor": "Focus Features",
    "verdict": "MIXED",
    "wokeScore": 18.00,
    "tradScore": 18.00,
    "authIndex": 50,
    "scoreMargin": "+0 (MIXED)",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Brokeback Mountain is not a woke trap. The film's depiction of a same-sex relationship is its entire premise, openly advertised from the poster to the trailer to the awards campaign. There is no hidden agenda because the agenda is the movie. Audiences in 2005 knew exactly what they were buying a ticket to see, and the film's critical and commercial success came from the honesty with which it delivered on that premise. A woke trap requires concealment, and Brokeback Mountain conceals nothing."
    },
    "seo": {
        "titleTag": "Is Brokeback Mountain (2005) Woke? Ang Lee's Western Romance VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Brokeback Mountain (2005), Ang Lee's Oscar-winning neo-Western starring Heath Ledger and Jake Gyllenhaal. A decades-spanning secret romance between two cowboys, and the cost it exacts. Verdict: NEUTRAL (0). Parental guidance included.",
        "keywords": "is brokeback mountain woke, brokeback mountain 2005 review, brokeback mountain virtuevigil, brokeback mountain parents guide, heath ledger jake gyllenhaal brokeback, brokeback mountain traditional or woke, ang lee brokeback"
    },
    "externalScores": {
        "imdb": "7.7/10",
        "rottenTomatoes": "88%",
        "metacritic": "87"
    },
    "creative_team": {
        "director": {
            "name": "Ang Lee",
            "ideology": "NONE (Universal Humanist)",
            "profile": "Ang Lee may be the least ideological major director working. He has made films about gay cowboys (Brokeback Mountain), Chinese martial artists (Crouching Tiger, Hidden Dragon), Marvel superheroes (Hulk), Jane Austen adaptations (Sense and Sensibility), and a boy adrift at sea with a tiger (Life of Pi). His subject is not politics but human longing, and his gift is finding the universal in the specific. Brokeback Mountain is not a political film in Lee's hands. It is a love story that happens to be between two men, and Lee approaches it with the same classical restraint he brought to Sense and Sensibility. This is the film's great strength and also, from a VVWS perspective, what makes its ideological content so difficult to categorize."
        },
        "writer": {
            "name": "Larry McMurtry, Diana Ossana",
            "profile": "Larry McMurtry was one of the great chroniclers of the American West (Lonesome Dove, The Last Picture Show) and brought to Brokeback Mountain a deep understanding of Western masculinity and its costs. Diana Ossana discovered Annie Proulx's short story in The New Yorker and pursued the adaptation for years before McMurtry agreed to collaborate. The screenplay's great achievement is expanding a 30-page short story into a feature film without adding ideological commentary. The script tells the story that Proulx wrote, with the same restraint and the same refusal to editorialize."
        },
        "lead_producer": {
            "name": "Diana Ossana, James Schamus",
            "company": "River Road Entertainment"
        },
        "composer": {
            "name": "Gustavo Santaolalla"
        },
        "top_cast": [
            {"name": "Heath Ledger", "role": "Ennis Del Mar"},
            {"name": "Jake Gyllenhaal", "role": "Jack Twist"},
            {"name": "Michelle Williams", "role": "Alma Beers Del Mar"},
            {"name": "Anne Hathaway", "role": "Lureen Newsome Twist"}
        ],
        "producers": ["Diana Ossana", "James Schamus"],
        "full_cast": [
            {"name": "Heath Ledger", "role": "Ennis Del Mar"},
            {"name": "Jake Gyllenhaal", "role": "Jack Twist"},
            {"name": "Michelle Williams", "role": "Alma Beers Del Mar"},
            {"name": "Anne Hathaway", "role": "Lureen Newsome Twist"},
            {"name": "Randy Quaid", "role": "Joe Aguirre"},
            {"name": "Linda Cardellini", "role": "Cassie Cartwright"},
            {"name": "Anna Faris", "role": "Lashawn Malone"},
            {"name": "David Harbour", "role": "Randall Malone"},
            {"name": "Roberta Maxwell", "role": "Jack's Mother"},
            {"name": "Peter McRobbie", "role": "John Twist"}
        ]
    },
    "tropes": [
        {
            "category": "Traditional",
            "trope": "Consequences of Infidelity (TRADITIONAL-019)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.60,
            "description": "Brokeback Mountain is, among other things, one of the most devastating films about infidelity ever made. Ennis and Jack's affair spans twenty years and destroys two marriages. Alma's silent agony as she discovers her husband's secret, her eventual divorce, and her tears at Thanksgiving when Ennis cannot even be honest with her years later: these are not woke talking points. They are the wages of betrayal, rendered with brutal specificity. The film never glamorizes the affair. It shows what it costs, and the cost is measured in ruined lives and broken families."
        },
        {
            "category": "Traditional",
            "trope": "Marriage and Betrayal (TRADITIONAL-022)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "Both Ennis and Jack marry women they do not love and keep secrets that poison their marriages. The film treats marriage not as a disposable institution but as a covenant whose violation exacts a terrible price. Alma's pain is not an abstraction. It is given full dramatic weight. Lureen's growing coldness is a direct result of Jack's emotional absence. The film's treatment of marriage is deeply traditional in the most painful way: it shows what happens when marriage is betrayed, and it refuses to pretend the betrayal is costless."
        },
        {
            "category": "Traditional",
            "trope": "Self-Denial and Stoic Suffering (TRADITIONAL-044)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "Ennis Del Mar is a portrait of a man who has swallowed his entire emotional life. Heath Ledger's performance is a masterclass in repression: the clenched jaw, the mumbled monosyllables, the explosive violence that is the only emotion he can express. The film does not celebrate this repression. But it takes it seriously as a way of being in the world, and it shows that some men are simply incapable of the emotional openness that progressive culture demands. Ennis is not a villain. He is a product of a world that gave him no tools to be anything else."
        },
        {
            "category": "Traditional",
            "trope": "Violence as Consequence of Transgression (TRADITIONAL-034)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 2.88,
            "description": "Ennis's childhood memory of his father showing him the mutilated body of a man killed for being gay is the film's darkest scene and its most traditional moment. The message is unambiguous: stepping outside the norms of your community can get you killed. This is not an endorsement of homophobic violence. It is a recognition that such violence exists and that the fear of it shapes lives. The film suggests, implicitly, that Ennis's repression is not cowardice but survival, and that is a deeply traditional calculation."
        },
        {
            "category": "Woke",
            "trope": "LGBTQ Normalization (WOKE-001)",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.60,
            "description": "This is the film's reason for existing and its primary ideological content. Brokeback Mountain takes a same-sex relationship and treats it with the full apparatus of classical Hollywood romance: sweeping landscapes, a lush score, close-ups of longing faces, and a tragic ending worthy of Romeo and Juliet. The normalization project is not didactic but aesthetic: by making the love story beautiful and tragic in the conventional mode, the film argues that gay love deserves the same cultural treatment as straight love. This was revolutionary in 2005 and remains the film's most significant political achievement."
        },
        {
            "category": "Woke",
            "trope": "Deconstruction of Masculinity (WOKE-004)",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.28,
            "description": "Brokeback Mountain takes the most masculine American archetype, the cowboy, and reveals him as capable of tenderness, longing, and love for another man. The film does not mock masculinity. It expands it. Ennis and Jack are not softened or feminized. They are cowboys who happen to be in love with each other, and the film respects their cowboy-ness even as it complicates what cowboy-ness can contain. This is deconstruction in the best sense: not destruction but expansion, showing that the category is larger than we thought."
        },
        {
            "category": "Minor Woke",
            "trope": "Marriage as Trap (WOKE-009)",
            "severity": 3,
            "authenticity": "Medium",
            "centrality": "Medium",
            "weightedScore": 2.52,
            "description": "Both marriages in the film are portrayed as prisons from which the men escape to each other. Alma's domesticity is suffocating. Lureen's Texas respectability is hollow. The film suggests that these heterosexual marriages are performances that the men undertake because society demands them, not because they are fulfilling. This could be read as a critique of marriage itself, though the film is more interested in the specific tragedy of these particular marriages than in making a general argument against the institution."
        },
        {
            "category": "Minor Woke",
            "trope": "Sympathy for the Queer Other (WOKE-015)",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Medium",
            "weightedScore": 2.88,
            "description": "The film extends profound sympathy to its two leads, and that sympathy is inseparable from their sexuality. The audience is asked to feel for Ennis and Jack not despite their love but because of it. Their suffering is framed as a product of social intolerance, not personal failure. The film's emotional logic is: these men deserved better than the world gave them, and the world was wrong. This is the film's most explicitly progressive argument."
        }
    ],
    "summary": {
        "overall": "Brokeback Mountain is the rare film that is both a landmark of progressive culture and a deeply traditional tragedy. Ang Lee's adaptation of Annie Proulx's short story follows Ennis Del Mar and Jack Twist, two Wyoming ranch hands who spend a summer herding sheep on Brokeback Mountain in 1963 and fall into a sexual and romantic relationship that neither man has the vocabulary for. They marry women, have children, and spend the next twenty years stealing weekends together in the wilderness while their families crumble around them. The film ends with Jack dead, possibly murdered in a hate crime, and Ennis alone in a trailer with a postcard of Brokeback Mountain and a shirt that still smells like the man he loved. Heath Ledger gives one of the great screen performances as Ennis, a man so clenched that even his vowels are strangled. Jake Gyllenhaal's Jack is the one who believes love can conquer all, and the film's tragedy is that he is wrong. Brokeback Mountain is not a political argument dressed as a movie. It is a love story that happens to be politically charged because of who is doing the loving. The film's neutrality score reflects a genuine balance: its progressive sexual politics are offset by its traditional treatment of marriage, infidelity, consequence, and the weight of a world that does not care about your feelings.",
        "traditionalStrengths": "For a film that became a progressive cultural touchstone, Brokeback Mountain is built on surprisingly traditional foundations. Marriage is treated as a sacred institution whose violation carries devastating consequences: Alma's silent suffering, her eventual divorce, and her tears at Thanksgiving dinner years later are given full dramatic weight. Infidelity is not glamorized but shown as a force that destroys everything it touches. Ennis's stoic repression is not celebrated but it is understood: the film acknowledges that some men are incapable of emotional expression, and it treats this as a tragedy rather than a pathology. The childhood memory of his father showing him a murdered gay man is the film's darkest scene, and its logic is brutally traditional: transgress the norms of your community and you may die. The film's ending, with Ennis alone in a trailer with nothing but memories, is one of cinema's most powerful depictions of the cost of a life lived against its own nature. The film's moral universe is conservative in the deepest sense: actions have consequences, covenants matter, and you cannot have everything you want without losing what you have.",
        "wokeElements": "The film's progressive content is impossible to ignore because it is the film's entire premise. Brokeback Mountain takes a same-sex relationship and gives it the full Hollywood prestige treatment: sweeping western landscapes, an Oscar-winning score, and a tragic love story that asks the audience to weep for two men who cannot be together because society will not let them. The normalization project is aesthetic, not didactic: the film argues by showing that gay love is as beautiful and as tragic as straight love. Ennis's masculinity is deconstructed not through mockery but through expansion, showing that a cowboy can contain tenderness, longing, and love for another man without ceasing to be a cowboy. The heterosexual marriages are portrayed as hollow performances that trap the characters in lives they did not choose. The film extends profound sympathy to its leads and frames their suffering as the product of social intolerance. These are progressive arguments, executed with the full force of classical Hollywood cinema. They are also inseparable from the film's artistic achievement, which is why assigning Brokeback Mountain a simple ideological label feels inadequate.",
        "parentalGuidance": "Rated R for sexual content including a brief but explicit sex scene, nudity, and strong thematic material. The sexual content is not pornographic but is frank. Language is period-appropriate and includes homophobic slurs. The film deals with adult themes including infidelity, divorce, and homophobic violence including an implied hate crime murder. The emotional content is heavy and the ending is devastating. Not appropriate for children or young teens. Older teenagers (16+) may find value in the film's treatment of love, loss, and the cost of living inauthentically, but parents should be aware that the film treats a same-sex relationship with full dramatic legitimacy. Parents who object to that framing on moral grounds should know that the film's emotional power makes it unusually persuasive. The film is likely to prompt conversations about sexuality, marriage, and social tolerance that parents may or may not want to have with their teenagers.",
        "adultInsight": "Brokeback Mountain is a film about what happens when you cannot say what you mean. Ennis Del Mar's entire life is a failure of communication. He cannot tell Jack he loves him. He cannot tell Alma the truth. He cannot even tell himself what he is. The film's great insight is not about homosexuality but about inarticulacy: the tragedy of a man who feels everything and can express nothing. Heath Ledger's performance is built on this insight. Every mumbled line, every averted glance, every explosive burst of violence is the language of a man who was never taught to speak. The film is devastating because it shows what that costs: a life half-lived, a love never fully claimed, and a future that could have been different if either man had possessed the words to make it so. Brokeback Mountain endures not because it is a political film but because it is a human one, and the boundary between those two categories is the space where the best art lives."
    }
}

# Append all 3 reviews
data.append(review1)
data.append(review2)
data.append(review3)

with open(REVIEWS_FILE, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Reviews appended: {original_count} -> {len(data)} ({len(data) - original_count} new)")
print(f"Review 1: {review1['title']} ({review1['slug']}) - {review1['verdict']}")
print(f"Review 2: {review2['title']} ({review2['slug']}) - {review2['verdict']}")
print(f"Review 3: {review3['title']} ({review3['slug']}) - {review3['verdict']}")