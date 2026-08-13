#!/usr/bin/env python3
"""Append 3 new reviews to reviews.json — 2026-08-13 batch."""

import json, sys

REVIEWS_PATH = "src/data/reviews.json"

new_reviews = [
    {
        "id": "man-on-fire-2004",
        "slug": "man-on-fire-2004",
        "title": "Man on Fire",
        "year": 2004,
        "type": "movie",
        "platform": "Hulu / Amazon Prime Video",
        "genre": "Action / Thriller",
        "readTime": "8 min",
        "poster": "/images/posters/man-on-fire-2004.jpg",
        "releaseDate": "2004-04-23",
        "rating": "R (Graphic Violence, Torture, Language)",
        "runtime": "146 min",
        "director": "Tony Scott",
        "writers": ["Brian Helgeland"],
        "cast": [
            {"name": "Denzel Washington", "role": "John Creasy"},
            {"name": "Dakota Fanning", "role": "Pita Ramos"},
            {"name": "Marc Anthony", "role": "Samuel Ramos"},
            {"name": "Radha Mitchell", "role": "Lisa Ramos"},
            {"name": "Christopher Walken", "role": "Rayburn"},
            {"name": "Mickey Rourke", "role": "Jordan Kalfus"},
            {"name": "Giancarlo Giannini", "role": "Manzano"}
        ],
        "studio": "Regency Enterprises",
        "distributor": "20th Century Fox",
        "verdict": "STRONGLY TRADITIONAL",
        "wokeScore": 1.4,
        "tradScore": 27.58,
        "scoreMargin": "+26 TRAD",
        "authIndex": 88,
        "preRelease": False,
        "wokeTrap": False,
        "date": "2026-08-13",
        "datePublished": "2026-08-13",
        "author": "VirtueVigil Editorial Team",
        "woke_trap_assessment": {
            "is_trap": False,
            "pct_runtime": 0,
            "explanation": "Man on Fire is not a woke film and makes no attempt to disguise itself as one. The corruption critique of Mexican institutions is present but functions as world-building, not ideology. The film's entire moral engine is traditional: protect the innocent, avenge the wronged, sacrifice yourself for someone you love. There is no trap here."
        },
        "seo": {
            "titleTag": "Is Man on Fire (2004) Woke? Denzel Washington Revenge Film Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil VVWS review of Man on Fire (2004). Denzel Washington as John Creasy. Verdict: STRONGLY TRADITIONAL, +26 TRAD. Full trope audit of Tony Scott's revenge thriller.",
            "keywords": [
                "is man on fire woke",
                "man on fire 2004 review",
                "denzel washington traditional film",
                "man on fire conservative review",
                "man on fire woke score",
                "man on fire parents guide",
                "man on fire virtuevigil",
                "tony scott revenge film",
                "man on fire traditional values",
                "is man on fire appropriate"
            ]
        },
        "summary": {
            "overview": "Man on Fire (2004), directed by Tony Scott, follows John Creasy (Denzel Washington), a burned-out former CIA operative and counterterrorism specialist who takes a job as a bodyguard for Pita Ramos (Dakota Fanning), the nine-year-old daughter of a wealthy family in Mexico City. Creasy is a drunk, a spiritual wreck, and a man who has long since stopped believing his life means anything. Then he meets Pita. She chips away at his armor. He starts to care. Then the cartel takes her, and Creasy stops being a bodyguard. He becomes a weapon.",
            "overall": "Man on Fire is one of the purest traditional value systems in American cinema, delivered at 146 minutes of operatic vengeance. The whole film runs on a single premise: protecting the innocent is not just a job. It's the thing that gives a broken man a reason to exist. Creasy goes from a man who can barely function to a one-man war, and it happens because a nine-year-old girl looked at him and saw something worth saving. When she's taken and presumed dead, the film stops being a thriller and becomes a reckoning. Not legal justice. Vengeance. Old-fashioned, relentless, unambiguous vengeance against people who hurt a child. Tony Scott shoots it with the urgency of a director who knows exactly what he's doing: the kinetic editing, the saturated color, the text burned into the screen. It shouldn't work as well as it does. It works completely. The corruption critique is real but narrow. The film isn't arguing that all institutions are rotten or that systemic forces explain evil. It's arguing that individuals make choices. The kidnappers chose to be monsters. Creasy chooses, at the cost of his life, to be something else. That moral framework, clear-eyed and uncomplicating, is exactly what Hollywood has spent the last decade dismantling. Man on Fire was made right before that dismantling got serious. It shows. Parents should not bring younger viewers anywhere near this. The torture sequences are graphic, the executions are specific, and the violence has real weight and consequence. The R rating is earned. For adults who can handle it, this is one of the finest revenge films ever made.",
            "bestFor": "Adults who want action with genuine emotional stakes, fans of Denzel Washington at the peak of his powers, anyone who responds to films where sacrifice is the point and not the subtext.",
            "skipIf": "You cannot tolerate graphic violence or torture sequences, or you need your action films to resolve cleanly with the hero walking away intact.",
            "wokeElements": "Minimal. The film depicts widespread corruption in Mexican law enforcement and government institutions, which functions as world-building consistent with documented realities rather than ideological messaging. Denzel Washington as Creasy is original IP; there is no diversity casting dimension. The film has no progressive social agenda.",
            "traditionalElements": "Comprehensive. Sacrifice for the innocent as the highest human act, righteous vengeance as morally defensible when justice fails, the redemptive power of genuine love and connection, masculine competence in service of something greater than the self, and the idea that a broken person can choose to become something worthy. Man on Fire is built on every one of these foundations."
        },
        "parentalGuidance": {
            "rating": "R",
            "contentWarnings": "Graphic action violence including shootings, explosions, and torture sequences. A villain has a bomb inserted rectally and is executed in a particularly brutal fashion. Kidnapping of a child is central to the plot. Strong language throughout. Brief depiction of alcoholism and self-destructive behavior.",
            "ageRecommendation": "17+",
            "discussionTopics": [
                "What makes a person worth redeeming",
                "The difference between vengeance and justice",
                "Sacrifice as an expression of love",
                "Institutional corruption and individual moral responsibility"
            ]
        },
        "externalScores": {
            "imdb": "7.7/10",
            "rottenTomatoes": "39%",
            "metacritic": "41/100"
        },
        "creative_team": {
            "director": {
                "name": "Tony Scott",
                "role": "Director",
                "note": "Ridley Scott's younger brother and one of the most kinetically gifted action directors of his generation. Non-ideological filmmaker whose films are built on loyalty, love, and the capacity for ordinary people to do extraordinary things. No political record."
            },
            "writer": {
                "name": "Brian Helgeland",
                "role": "Screenwriter",
                "note": "Oscar winner for L.A. Confidential. Known for crime thrillers with moral weight. No significant ideological record."
            },
            "lead_producer": {
                "name": "Arnon Milchan / Tony Scott / Lucas Foster",
                "role": "Producers"
            },
            "composer": {
                "name": "Harry Gregson-Williams",
                "role": "Composer"
            }
        },
        "tropeAudit": [
            {
                "id": "WOKE-MOF-001",
                "name": "Institutional Corruption Critique",
                "category": "Woke",
                "severity": 2,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 1.4,
                "description": "The film depicts widespread corruption in Mexican law enforcement, judiciary, and government. Crooked cops, complicit officials, and cartel connections reach into official institutions. The critique is real but functions as setting, not ideology. The film doesn't argue for systemic solutions; it argues that Creasy is going to handle it personally."
            },
            {
                "id": "TRAD-MOF-001",
                "name": "The Self-Sacrificing Hero",
                "category": "Traditional",
                "severity": 5,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 6.3,
                "description": "The entire third act is Creasy trading his life piece by piece to rescue Pita. He is shot, tortured, and dying by the final exchange. He hands himself over to La Hermandad knowing he won't survive, because getting Pita home alive is worth more than his life. This is not a rhetorical sacrifice; it is literal. The film's final shot confirms it."
            },
            {
                "id": "TRAD-MOF-002",
                "name": "The Surrogate Father and Protector",
                "category": "Traditional",
                "severity": 5,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 6.3,
                "description": "Creasy becomes a surrogate father to Pita. She draws out what's left of his humanity. He teaches her to swim; she gives him a reason to stop drinking. The father-child bond is not metaphorical; it's the film's emotional spine. When she is taken, Creasy's rampage is not professional; it's personal in the way only parental love makes it personal."
            },
            {
                "id": "TRAD-MOF-003",
                "name": "Redemption Through Purpose",
                "category": "Traditional",
                "severity": 4,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 5.04,
                "description": "Creasy opens the film without purpose. A former elite operative reduced to drinking himself unconscious in an empty apartment. His friend Rayburn (Walken) talks about God having a purpose for everything. Creasy doesn't believe it. Then Pita gives him one. The film argues, without irony, that a man without something worth dying for is already dead."
            },
            {
                "id": "TRAD-MOF-004",
                "name": "Righteous Vengeance as Justice",
                "category": "Traditional",
                "severity": 4,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 5.04,
                "description": "When legal channels fail because they're corrupt, Creasy handles it himself. The film does not frame this as morally complex. It frames it as necessary. The people who hurt Pita are evil; they should face consequences; institutional corruption means Creasy has to deliver those consequences personally. This is the vigilante justice tradition in its clearest form."
            },
            {
                "id": "TRAD-MOF-005",
                "name": "Objective Good vs. Evil",
                "category": "Traditional",
                "severity": 4,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 2.8,
                "description": "The kidnappers are not humanized, sympathized with, or given trauma backstories to explain their choices. They kidnap children for money. They are evil because they chose to be. Creasy is the instrument of their consequences. The moral clarity is complete and unapologetic."
            },
            {
                "id": "TRAD-MOF-006",
                "name": "Warrior Competence as Virtue",
                "category": "Traditional",
                "severity": 3,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 2.1,
                "description": "Creasy's combat skills, acquired through decades of service, are presented as genuinely valuable. The film does not apologize for his effectiveness or frame his violence as a symptom of trauma. He is good at what he does. That competence, in service of protecting the innocent, is treated as admirable."
            }
        ]
    },
    {
        "id": "arrival-2016",
        "slug": "arrival-2016",
        "title": "Arrival",
        "year": 2016,
        "type": "movie",
        "platform": "Paramount+ / Apple TV+",
        "genre": "Science Fiction / Drama",
        "readTime": "7 min",
        "poster": "/images/posters/arrival-2016.jpg",
        "releaseDate": "2016-11-11",
        "rating": "PG-13 (Brief Strong Language)",
        "runtime": "116 min",
        "director": "Denis Villeneuve",
        "writers": ["Eric Heisserer"],
        "cast": [
            {"name": "Amy Adams", "role": "Louise Banks"},
            {"name": "Jeremy Renner", "role": "Ian Donnelly"},
            {"name": "Forest Whitaker", "role": "Colonel Weber"},
            {"name": "Michael Stuhlbarg", "role": "Agent Halpern"},
            {"name": "Tzi Ma", "role": "General Shang"}
        ],
        "studio": "FilmNation Entertainment / Lava Bear Films",
        "distributor": "Paramount Pictures",
        "verdict": "WOKE LEAN",
        "wokeScore": 12.3,
        "tradScore": 9.24,
        "scoreMargin": "-3 WOKE",
        "authIndex": 62,
        "preRelease": False,
        "wokeTrap": False,
        "date": "2026-08-13",
        "datePublished": "2026-08-13",
        "author": "VirtueVigil Editorial Team",
        "woke_trap_assessment": {
            "is_trap": False,
            "pct_runtime": 0,
            "explanation": "Arrival is not a woke trap. The progressive framing is present from the start: Louise is introduced as the only person with the wisdom and empathy to prevent catastrophe while the military men want to shoot first. The film does not bait-and-switch. The messaging is consistent throughout."
        },
        "seo": {
            "titleTag": "Is Arrival (2016) Woke? Amy Adams Sci-Fi Film Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil VVWS review of Arrival (2016). Denis Villeneuve's Amy Adams sci-fi drama. Verdict: WOKE LEAN, -3 WOKE. Full trope audit covering female savior, anti-military themes, and sacrifice.",
            "keywords": [
                "is arrival woke",
                "arrival 2016 review",
                "arrival amy adams traditional",
                "arrival conservative review",
                "arrival woke score",
                "arrival parents guide",
                "arrival virtuevigil",
                "denis villeneuve woke",
                "arrival 2016 political",
                "is arrival appropriate for kids"
            ]
        },
        "summary": {
            "overview": "Arrival (2016), directed by Denis Villeneuve and written by Eric Heisserer, is an adaptation of Ted Chiang's short story 'Story of Your Life.' Twelve extraterrestrial spacecraft appear at various locations around the world. Linguist Louise Banks (Amy Adams) is recruited by the U.S. military to attempt communication with the beings inside. As nations race to decode the aliens' intentions and some governments edge toward military action, Louise discovers that learning the aliens' language is changing how she perceives time itself.",
            "overall": "There is a genuinely extraordinary film buried inside Arrival. The central mystery, the alien language that rewires the brain's experience of time, and the devastating final revelation about Louise's daughter are among the most emotionally intelligent sci-fi conceits in recent memory. The film's emotional payload lands. When you understand what Louise knows and when she knows it, the weight of her choices is real. The problem is the frame Villeneuve puts around it. The film has a political argument, and it keeps interrupting the science fiction to make it. Louise is the only person on earth with the right instincts. The military, represented by Colonel Weber and especially the trigger-happy nations around the world, wants to treat the aliens as a threat. Louise knows they aren't. The male authority figures are obstacles. The female linguist is the savior. It's not subtle. The globalism message is baked in too: humanity's survival depends on nations setting aside their competitive instincts and cooperating, while nationalist reactions to the unknown are the actual danger. That's a political thesis, not just a story. It doesn't ruin the film. Amy Adams gives one of the better performances of the decade, the cinematography is stunning, and Villeneuve builds atmosphere the way few directors can. But you're watching a film that could have been purely about the profound strangeness of time and love and grief, and keeps pulling back to argue about militarism. It's a narrower film than it could have been, and the narrowing is ideological.",
            "bestFor": "Science fiction fans who can hold the political messaging at arm's length, people who want genuinely adult emotional content in a blockbuster, fans of Denis Villeneuve's visual style.",
            "skipIf": "You're going in for pure traditional-values content. The film has real traditional elements but frames them within a female-savior-over-military-men structure that's hard to miss.",
            "wokeElements": "Louise Banks is the female savior whose empathy and communication skills prevent the militaristic men from starting an interstellar war. The military is consistently framed as a reactive, emotionally limited institution prone to escalation. The film's resolution depends on a woman reaching across national and species lines while governments fail. The globalism message in the final act, where Louise convinces a Chinese general to stand down by sharing a personal detail, is particularly pointed.",
            "traditionalElements": "Louise's central choice, to experience Hannah's life knowing it will end in terrible grief, is a profound traditional statement about love and sacrifice. She chooses love over self-protection. She accepts the full weight of what love costs. The film also carries genuine themes of duty to one's vocation; Louise doesn't hesitate when called, and her commitment to understanding the aliens is absolute."
        },
        "parentalGuidance": {
            "rating": "PG-13",
            "contentWarnings": "Brief strong language. Emotional content involving the death of a child from illness. Some tense military standoff scenes. The film is not violent but the emotional weight of the ending can be intense.",
            "ageRecommendation": "13+ (mature themes)",
            "discussionTopics": [
                "Would you choose love if you knew how much it would cost you",
                "How should humanity respond to the unknown",
                "The relationship between language and thought",
                "Whether military escalation is ever justified in the face of uncertainty"
            ]
        },
        "externalScores": {
            "imdb": "7.9/10",
            "rottenTomatoes": "94%",
            "metacritic": "81/100"
        },
        "creative_team": {
            "director": {
                "name": "Denis Villeneuve",
                "role": "Director",
                "note": "Canadian filmmaker responsible for Sicario, Blade Runner 2049, Dune Part One, and Dune Part Two. Broadly apolitical as a director but Arrival is his most ideologically pointed film. Known for extraordinary technical craft and atmospheric tension."
            },
            "writer": {
                "name": "Eric Heisserer",
                "role": "Screenwriter",
                "note": "Known for horror adaptations (Lights Out, Bird Box). Arrival was his breakthrough into prestige material. The female-savior framing is amplified from Ted Chiang's more neutral source story."
            },
            "lead_producer": {
                "name": "Shawn Levy / Dan Levine / Aaron Ryder / David Linde",
                "role": "Producers"
            },
            "composer": {
                "name": "Johann Johannsson",
                "role": "Composer"
            }
        },
        "tropeAudit": [
            {
                "id": "WOKE-ARR-001",
                "name": "Female Savior",
                "category": "Woke",
                "severity": 4,
                "authenticity": 1.0,
                "centrality": 1.8,
                "weightedScore": 7.2,
                "description": "Louise Banks is the only human being with the empathy, intelligence, and instinct to prevent first contact from becoming a war. The men around her, the military brass, the hawkish generals, the government agents, are consistently wrong. Louise is consistently right. Her gender is tied explicitly to her method: she communicates and connects where the men want to threaten and control. The film presents this as more than character design; it's the argument."
            },
            {
                "id": "WOKE-ARR-002",
                "name": "Military as Obstacle and Antagonist",
                "category": "Woke",
                "severity": 3,
                "authenticity": 1.0,
                "centrality": 1.0,
                "weightedScore": 3.0,
                "description": "Colonel Weber and the military apparatus surrounding Louise are repeatedly presented as emotionally limited obstacles to genuine understanding. They want metrics, weapons assessments, and exit strategies. Louise needs time and trust. The film frames military caution as a failure of imagination and empathy, while Louise's civilian approach is vindicated at every turn."
            },
            {
                "id": "WOKE-ARR-003",
                "name": "Globalist Message",
                "category": "Woke",
                "severity": 3,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 2.1,
                "description": "The film's climactic geopolitical resolution requires a Chinese general to stand down because Louise shares a personal detail about his dying wife. National competitive instincts are the villain; cross-cultural human connection is the solution. The message is that humanity's survival depends on transcending nationalism. This is organic to the story's logic but remains a political thesis."
            },
            {
                "id": "TRAD-ARR-001",
                "name": "Sacrificial Love",
                "category": "Traditional",
                "severity": 4,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 5.04,
                "description": "Louise knows, because of what the alien language has done to her perception, that her daughter Hannah will die young from an incurable illness. She chooses to have her anyway. She chooses love at its full cost rather than self-protection. This is the film's deepest traditional value: genuine love does not opt out of suffering. It accepts what love requires and does it with eyes open."
            },
            {
                "id": "TRAD-ARR-002",
                "name": "Acceptance of Painful Fate",
                "category": "Traditional",
                "severity": 3,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 2.1,
                "description": "Louise does not rage against the knowledge of what will happen. She does not try to change it or find a loophole. She accepts the full weight of what she knows and moves through it. This is a classically traditional response to mortality and grief: not avoidance but acceptance, not despair but endurance."
            },
            {
                "id": "TRAD-ARR-003",
                "name": "Duty and Vocation",
                "category": "Traditional",
                "severity": 3,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 2.1,
                "description": "Louise is called and she shows up. No hesitation. No negotiation. She is a linguist; there is a language to decipher; she goes. The film treats professional dedication as a form of honor, not just employment. Her commitment to understanding the aliens is absolute and comes before personal comfort or safety."
            }
        ]
    },
    {
        "id": "the-last-samurai-2003",
        "slug": "the-last-samurai-2003",
        "title": "The Last Samurai",
        "year": 2003,
        "type": "movie",
        "platform": "Max / Tubi",
        "genre": "Action / Drama / Historical Epic",
        "readTime": "9 min",
        "poster": "/images/posters/the-last-samurai-2003.jpg",
        "releaseDate": "2003-12-05",
        "rating": "R (Strong Sequences of War Violence, Some Disturbing Images)",
        "runtime": "154 min",
        "director": "Edward Zwick",
        "writers": ["John Logan", "Marshall Herskovitz", "Edward Zwick"],
        "cast": [
            {"name": "Tom Cruise", "role": "Captain Nathan Algren"},
            {"name": "Ken Watanabe", "role": "Katsumoto"},
            {"name": "Tony Goldwyn", "role": "Colonel Bagley"},
            {"name": "Hiroyuki Sanada", "role": "Ujio"},
            {"name": "Koyuki", "role": "Taka"},
            {"name": "Timothy Spall", "role": "Simon Graham"}
        ],
        "studio": "Warner Bros. Pictures / Bedford Falls Company",
        "distributor": "Warner Bros. Pictures",
        "verdict": "TRADITIONAL",
        "wokeScore": 9.24,
        "tradScore": 26.04,
        "scoreMargin": "+17 TRAD",
        "authIndex": 75,
        "preRelease": False,
        "wokeTrap": False,
        "date": "2026-08-13",
        "datePublished": "2026-08-13",
        "author": "VirtueVigil Editorial Team",
        "woke_trap_assessment": {
            "is_trap": False,
            "pct_runtime": 0,
            "explanation": "The Last Samurai is not a woke trap. The film is upfront about its thesis: Western modernization is spiritually hollow and the samurai embody something worth dying to preserve. The anti-Western elements are present from the beginning, not revealed midway through. The film is what it says it is."
        },
        "seo": {
            "titleTag": "Is The Last Samurai (2003) Woke? Tom Cruise Film Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil VVWS review of The Last Samurai (2003). Tom Cruise and Ken Watanabe. Verdict: TRADITIONAL, +17 TRAD. Full trope audit covering warrior code, honor, and anti-Western themes.",
            "keywords": [
                "is the last samurai woke",
                "the last samurai 2003 review",
                "tom cruise traditional film",
                "the last samurai conservative review",
                "the last samurai woke score",
                "the last samurai parents guide",
                "the last samurai virtuevigil",
                "is the last samurai appropriate",
                "the last samurai bushido traditional values",
                "edward zwick samurai"
            ]
        },
        "summary": {
            "overview": "The Last Samurai (2003), directed by Edward Zwick, follows Captain Nathan Algren (Tom Cruise), a traumatized Civil War and Indian Wars veteran who is hired by the Japanese Meiji government to train their modern conscript army against a samurai rebellion led by Katsumoto (Ken Watanabe). Algren is captured in battle and brought to the samurai village to spend a winter. What he finds there, a code of honor that makes his own culture look like a fever dream of money and violence, begins to change him. When spring comes, Algren chooses sides.",
            "overall": "The Last Samurai is a film about what honor actually costs, and it doesn't flinch at the answer. Katsumoto and his men know they're going to lose. They know the rifles and cannons and conscript armies of the new Japan will eventually overwhelm them. They ride to the final battle anyway, because some things are worth dying for and Bushido is one of them. That is a traditional statement of almost shocking clarity. The film's weakness is the frame around it. The anti-Western argument is there and it's not subtle: American modernization brings booze, PTSD, and moral corruption; the Japanese warrior tradition brings discipline, beauty, and purpose. The film presents this as a clean binary. It's not historically accurate and it's not philosophically honest. Real Meiji Japan was complicated; Katsumoto's rebellion was not purely noble; and the 'Western modernity is empty' thesis has been the default position of a certain strand of Hollywood for decades. The film borrows that thesis. The difference here is that what the film puts on the other side of the ledger, honor, sacrifice, loyalty, the warrior code, the willingness to die for something real, is genuinely traditional. Katsumoto is not a progressive icon; he's a conservative one. He's dying to preserve something, not to dismantle it. That tension makes The Last Samurai more interesting than it looks. It's anti-Western, but it's anti-Western in a way that valorizes tradition over progress. That's a different complaint than most woke films make. Ken Watanabe is extraordinary throughout. The final battle sequence is one of the great set pieces in American historical epic cinema. Parents should note the R rating is merited: the battle sequences are brutal and the deaths are not bloodless.",
            "bestFor": "Fans of historical epics, viewers who can engage with a film's ideology critically without it breaking the experience, anyone who wants to see Ken Watanabe at the top of his game.",
            "skipIf": "You want a purely traditional film without ideological friction. The anti-Western modernization thesis is central and sustained.",
            "wokeElements": "The American and Western characters are consistently framed as corrupted by materialism, violence, and moral emptiness. Colonel Bagley is a war criminal who slaughtered civilian villages. Algren drinks himself unconscious. Western industrialism is portrayed as the destroyer of authentic culture. The film argues that non-Western traditional culture is spiritually superior to Western modernity. This is the film's central thesis, not a subplot.",
            "traditionalElements": "Bushido as an actual code worth dying for, self-sacrifice as honorable rather than tragic, the transformation of a broken man through contact with genuine honor, loyalty to one's lord and to one's principles over personal survival, and the argument that some things are worth preserving at the cost of everything. The film celebrates tradition, hierarchy, warrior virtue, and the willingness to stand against overwhelming force for something real."
        },
        "parentalGuidance": {
            "rating": "R",
            "contentWarnings": "Extended battle sequences with sword violence, gunfire, and significant on-screen deaths. Characters are shown wounded, dying, and dead in detail. Brief disturbing imagery including a burning village. A scene of attempted sexual assault is interrupted quickly. Alcoholism depicted in early scenes.",
            "ageRecommendation": "15+",
            "discussionTopics": [
                "What makes something worth dying for",
                "Whether progress is always improvement",
                "The difference between honor culture and guilt culture",
                "What the West gained and lost through industrialization"
            ]
        },
        "externalScores": {
            "imdb": "7.7/10",
            "rottenTomatoes": "66%",
            "metacritic": "55/100"
        },
        "creative_team": {
            "director": {
                "name": "Edward Zwick",
                "role": "Director",
                "note": "Director of Glory, Legends of the Fall, and Blood Diamond. Known for prestige historical dramas with strong male leads and moral weight. His films tend toward nuanced rather than propagandistic politics, but The Last Samurai is among his more ideologically pointed works."
            },
            "writer": {
                "name": "John Logan / Marshall Herskovitz / Edward Zwick",
                "role": "Screenwriters"
            },
            "lead_producer": {
                "name": "Tom Cruise / Paula Wagner / Scott Kroopf / Tom Engelman",
                "role": "Producers"
            },
            "composer": {
                "name": "Hans Zimmer",
                "role": "Composer"
            }
        },
        "tropeAudit": [
            {
                "id": "WOKE-TLS-001",
                "name": "Anti-Western Imperialism",
                "category": "Woke",
                "severity": 4,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 5.04,
                "description": "American and Western influence on Meiji Japan is portrayed as uniformly corrupting. Colonel Bagley is a war criminal. Algren's Americanism has made him a drunk and a moral wreck. The weapons, tactics, and modernization that the Meiji government imports from the West are the instruments of the samurai's destruction. The film presents no counterargument: Western modernity brings nothing worth keeping."
            },
            {
                "id": "WOKE-TLS-002",
                "name": "Western Civilization as Spiritually Empty",
                "category": "Woke",
                "severity": 3,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 2.1,
                "description": "Algren's arc is explicitly a rejection of Western materialism and moral chaos for Japanese warrior tradition. He finds purpose, discipline, and meaning in the samurai village that his own culture denied him. The film frames this as a discovery of something his culture lacked, not as a cross-cultural appreciation. Western civilization is the problem; Bushido is the answer."
            },
            {
                "id": "WOKE-TLS-003",
                "name": "Non-Western Culture as Morally Superior",
                "category": "Woke",
                "severity": 3,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 2.1,
                "description": "The samurai village is presented as an idealized community: spiritually coherent, aesthetically beautiful, honorable in its every interaction. The contrast with Western society Algren left behind is not subtle. The film argues that the non-Western traditional culture it depicts is superior to what replaced it. This is organic to the story but is a sustained political thesis."
            },
            {
                "id": "TRAD-TLS-001",
                "name": "The Self-Sacrificing Hero",
                "category": "Traditional",
                "severity": 5,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 6.3,
                "description": "Katsumoto and his samurai ride into a final battle they cannot win against rifles and cannon because their honor demands it. They die beautifully, in the traditional Japanese sense, and the film treats their deaths as transcendence rather than tragedy. Algren survives, but only to carry the testimony of what they stood for. Sacrifice for principle, not survival, is the film's highest value."
            },
            {
                "id": "TRAD-TLS-002",
                "name": "Honor Culture and Warrior Code",
                "category": "Traditional",
                "severity": 5,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 6.3,
                "description": "Bushido is not window dressing here. The film spends its entire second act showing what an honor culture actually looks like in practice: discipline, respect, loyalty, the willingness to die rather than violate one's principles. Katsumoto teaches Algren these values by living them. The warrior code is presented not as a relic but as a superior way of organizing a life."
            },
            {
                "id": "TRAD-TLS-003",
                "name": "The Reluctant Hero's Transformation",
                "category": "Traditional",
                "severity": 4,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 5.04,
                "description": "Algren arrives as a broken man and leaves as an honorable one. The transformation is earned: he watches the samurai, fights alongside them, is judged by their standards and found capable. His recovery is not therapy or self-discovery in the modern sense. It's discipline, contact with genuine virtue, and the slow return of something he'd lost. The traditional model of character formation through challenge and example."
            },
            {
                "id": "TRAD-TLS-004",
                "name": "Defense of Tradition Against Modernity",
                "category": "Traditional",
                "severity": 5,
                "authenticity": 0.7,
                "centrality": 1.8,
                "weightedScore": 6.3,
                "description": "The entire conflict is Katsumoto fighting to preserve the samurai way of life against forced modernization imposed by a government that has abandoned its own traditions for Western efficiency and profit. The film is an argument that some things should not be allowed to die simply because they're inconvenient to progress. This is the conservative case against unchecked modernization, made explicitly and at length."
            },
            {
                "id": "TRAD-TLS-005",
                "name": "Objective Good vs. Evil",
                "category": "Traditional",
                "severity": 3,
                "authenticity": 0.7,
                "centrality": 1.0,
                "weightedScore": 2.1,
                "description": "The political villain, Omura, is corrupt, venal, and willing to sell Japan's soul for personal profit and Western approval. Katsumoto is noble, principled, and honest. Colonel Bagley has committed actual war crimes. The moral lines are clear. The film does not ask you to understand the villains; it asks you to understand the cost of defeating them."
            }
        ]
    }
]

# Load existing reviews
with open(REVIEWS_PATH, "r", encoding="utf-8") as f:
    existing = json.load(f)

existing_slugs = {r.get("slug") for r in existing}
print(f"Before: {len(existing)} reviews")

added = 0
for review in new_reviews:
    slug = review["slug"]
    if slug in existing_slugs:
        print(f"SKIP (exists): {slug}")
        continue
    existing.append(review)
    existing_slugs.add(slug)
    added += 1
    print(f"Added: {slug}")

with open(REVIEWS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"After: {len(existing)} reviews (+{added})")
