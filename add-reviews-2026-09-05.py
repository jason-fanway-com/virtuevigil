#!/usr/bin/env python3
"""Append 3 reviews to reviews.json for 2026-09-05 cron run."""
import json, sys, os

REVIEWS_PATH = "src/data/reviews.json"

with open(REVIEWS_PATH) as f:\n    reviews = json.load(f)\n\noriginal_count = len(reviews)\n\n# ============================================================\n# REVIEW 1: Mayday (2026)
# ============================================================
mayday = {
    "id": "mayday-2026",
    "slug": "mayday-2026",
    "title": "Mayday",
    "year": 2026,
    "type": "film",
    "platform": "Apple TV+",
    "genre": "Action Comedy, Thriller",
    "date": "2026-09-05",
    "datePublished": "2026-09-05",
    "author": "VirtueVigil Editorial Team",
    "readTime": "9 min",
    "poster": "/images/posters/mayday-2026.jpg",
    "releaseDate": "2026-09-04",
    "rating": "PG-13 (Action Violence, Language, Some Suggestive Material)",
    "runtime": "111 minutes",
    "director": "Jonathan Goldstein, John Francis Daley",
    "writers": ["Jonathan Goldstein", "John Francis Daley"],
    "cast": [
        {"name": "Ryan Reynolds", "role": "Troy 'Assassin' Kelly"},
        {"name": "Kenneth Branagh", "role": "Nikolai Ustinov"},
        {"name": "Maria Bakalova", "role": "Anna Ustinov"},
        {"name": "Marcin Dorocinski", "role": "Alexander Volkov"},
        {"name": "David Morse", "role": "Harold Kelly"}
    ],
    "studio": "Apple Studios, Skydance Media, Maximum Effort",
    "distributor": "Apple TV+",
    "verdict": "TRADITIONAL",
    "wokeScore": 5.04,
    "tradScore": 17.76,
    "authIndex": 82,
    "scoreMargin": "+13 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "No woke trap. Mayday is a straightforward Cold War action comedy from the first frame to the last. A US Navy SR-71 pilot crash-lands in Soviet territory and teams up with a former KGB agent to escape. There is no ideological bait and switch, no hidden progressive messaging in the back half. The buddy dynamic between Reynolds's American flyboy and Branagh's ex-KGB carpenter is built on mutual competence and respect, not on anyone being lectured about their privilege. Nothing past the 50% runtime mark subverts the film's traditional action-comedy framework."
    },
    "seo": {
        "titleTag": "Is Mayday (2026) Woke? Ryan Reynolds Cold War Action Comedy VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Mayday (2026), the Apple TV+ Cold War action comedy starring Ryan Reynolds and Kenneth Branagh. An SR-71 pilot teams up with an ex-KGB agent to escape Soviet territory. Verdict: TRADITIONAL (+13 TRAD). Parental guidance included.",
        "keywords": "is mayday woke, mayday 2026 review, mayday virtuevigil, mayday ryan reynolds, mayday traditional or woke, mayday parents guide, mayday apple tv review"
    },
    "externalScores": {
        "imdb": "6.8/10",
        "rottenTomatoes": "80%",
        "metacritic": "60"
    },
    "creative_team": {
        "director": {
            "name": "Jonathan Goldstein, John Francis Daley",
            "ideology": "MODERATE (Commercial Craftsmen)",
            "profile": "Goldstein and Daley are the writing-directing duo behind Game Night (2018) and Dungeons and Dragons: Honor Among Thieves (2023). Their signature is smart, fast-paced comedy that respects its characters rather than mocking them. Neither has a public history of political activism or ideological filmmaking. They write crowd-pleasers that work because the jokes are character-driven, not agenda-driven. Their work on Horrible Bosses and Spider-Man: Homecoming (writing credits) further confirms a commercial sensibility that prioritizes entertainment over messaging. For Mayday, they bring the same tone: a buddy action comedy where the laughs come from situation and character, not from anyone's identity being the punchline."
        },
        "writer": {
            "name": "Jonathan Goldstein, John Francis Daley",
            "profile": "The duo wrote Mayday as an original screenplay. The premise is a classic odd-couple setup: a cocky American pilot and a world-weary ex-KGB officer must cooperate to survive. The script leans into the absurdity of the pairing without making either man a joke. Reynolds's Troy Kelly is arrogant but competent. Branagh's Nikolai Ustinov is cynical but principled. The writing gives both men genuine arcs: Kelly learns humility, Ustinov rediscovers purpose. This is traditional buddy-movie architecture executed cleanly."
        },
        "lead_producer": {
            "name": "Ryan Reynolds, David Ellison",
            "company": "Maximum Effort / Skydance Media"
        },
        "composer": {
            "name": "Colin Stetson"
        },
        "top_cast": [
            {"name": "Ryan Reynolds", "role": "Troy 'Assassin' Kelly"},
            {"name": "Kenneth Branagh", "role": "Nikolai Ustinov"},
            {"name": "Maria Bakalova", "role": "Anna Ustinov"}
        ],
        "producers": ["David Ellison", "Dana Goldberg", "Don Granger", "Ryan Reynolds"],
        "full_cast": [
            {"name": "Ryan Reynolds", "role": "Troy 'Assassin' Kelly"},
            {"name": "Kenneth Branagh", "role": "Nikolai Ustinov"},
            {"name": "Maria Bakalova", "role": "Anna Ustinov"},
            {"name": "Marcin Dorocinski", "role": "Alexander Volkov"},
            {"name": "David Morse", "role": "Harold Kelly"},
            {"name": "Lovell Adams-Gray", "role": "Agent Williams"},
            {"name": "Clark Johnson", "role": "General Parrish"}
        ]
    },
    "fidelityCasting": "",
    "spoiler_alert": False,
    "summary": {
        "overall": "Mayday is the kind of movie Hollywood used to make without apology: a buddy action comedy set against a Cold War backdrop, with genuine stakes, real chemistry between its leads, and no interest whatsoever in lecturing the audience about anything. Ryan Reynolds plays Troy 'Assassin' Kelly, a US Navy SR-71 Blackbird pilot who ejects over Soviet territory in 1987 after a mid-air collision with a MiG-29. Stranded, hunted, and badly out of his depth, he stumbles into the life of Nikolai Ustinov (Kenneth Branagh), a former KGB officer who left the service to become a carpenter in a remote village. What follows is a two-man escape thriller that works because Goldstein and Daley understand something that has become weirdly rare in modern action comedies: you can make a movie about two men from enemy nations learning to trust each other without making one of them apologize for his country. Kelly is an American patriot. Ustinov is a Soviet defector who saw the KGB for what it was. Neither man is asked to renounce who he is. They are asked to survive together, and the film earns every beat of their partnership through action, humor, and Branagh's beautifully understated performance. Reynolds does his Reynolds thing, but Branagh is the anchor. His Ustinov is a man who traded a life of state-sanctioned violence for the quiet dignity of working with his hands, and when Kelly's arrival forces him back into a world he left behind, you believe both his reluctance and his competence. Maria Bakalova, as Ustinov's daughter Anna, provides emotional stakes without becoming a damsel: her relationship with her father is the film's quiet center. The Cold War setting is a feature, not a bug. In a cinematic landscape where every decade must be examined for its sins, Mayday simply uses 1987 as a playground for a thrilling, funny, ideologically clean two hours. That is not a small thing anymore. It is almost radical.\n\nThe film's action sequences are practical and legible, a welcome departure from CGI overload. The SR-71 sequences at the top of the film are genuinely tense, and a late-film set piece involving a Soviet train is the kind of practical action filmmaking that makes you remember why real stunts matter. Goldstein and Daley direct action with clarity: you always know where everyone is and what the stakes are. Colin Stetson's score, all low brass and propulsive percussion, gives the film a gravity that balances Reynolds's natural levity. The tone lands somewhere between The Hunt for Red October and Midnight Run, and if that sounds like a compliment, it is meant as one.\n\nWhat makes Mayday refreshing from a VirtueVigil perspective is what it does not do. It does not pause the action so a female character can explain to a male character why he is wrong about everything. It does not make the American pilot a bumbling fool who needs a foreigner to teach him humility. Kelly learns humility the old-fashioned way: by failing, nearly dying, and being forced to rely on someone who is better than him at certain things. That is character growth, not ideological reeducation. Ustinov's rejection of the KGB is personal, not political: he left because he saw what the institution did to people, not because he attended a seminar on decolonization. The film trusts its audience to understand that some men are good and some institutions are corrupt without needing a PowerPoint presentation to explain why. This trust is the defining feature of pre-woke cinema, and its presence here, in a 2026 streaming release, is worth noting explicitly.\n\nBranagh gives the film's best performance. His Ustinov is weary but not broken, cynical but not cruel. He has the bearing of a man who once held power and chose to walk away from it, and Branagh plays that choice as settled business rather than an ongoing crisis. When Kelly asks why he left the KGB, Ustinov gives a one-sentence answer that lands harder than any monologue could. Reynolds, to his credit, knows when to shut up and let Branagh work. Their chemistry is the movie. Without it, Mayday would be a competent but forgettable action comedy. With it, the film has a genuine emotional core that elevates the chase sequences into something resembling a friendship. Maria Bakalova, in a role that could have been thankless, gives Anna enough interior life that you understand why her father would risk everything to protect her.\n\nFor parents, the PG-13 rating is accurate. The action violence is present but not gory: gunfire, explosions, hand-to-hand combat, a few deaths that register without being lingered on. Language is what you would expect from a Ryan Reynolds movie (frequent but not obscene). There is some suggestive banter but no sex or nudity. The Cold War setting means the ideological lines are drawn cleanly: Americans are the good guys, Soviets are the bad guys, and the complexity comes from individuals on both sides who do not fit the categories. This is the kind of movie you can watch with teenagers and have a conversation afterward about what it means to serve a country versus what it means to serve an ideology, and why those two things are not the same.",
        "adultInsight": "Mayday rewards viewers who grew up on Cold War thrillers without demanding that they apologize for enjoying them. The film's pleasures are old-fashioned: charismatic leads, practical stunts, a script that respects the audience's intelligence, and a clear moral framework. Goldstein and Daley's direction is more confident here than in Game Night: the action beats land with real impact, and the comic beats never undercut the tension. Reynolds has spent the last decade playing variations on Deadpool, but Troy Kelly lets him dial the snark back about 30 percent and play a character who is funny because he is out of his depth, not because he is winking at the camera. The result is his most likable performance in years. Branagh, meanwhile, reminds everyone that he was one of the great Shakespearean actors before he became the guy who directed Thor. His Ustinov is a quiet triumph: a man who has made peace with his past and is not especially interested in explaining it to a cocky American pilot. The film's best scene is a fireside conversation between the two men, late in the second act, where Ustinov explains what the KGB took from him and Kelly, for once, just listens. It is the kind of scene that would have been cut from a modern studio comedy for being too slow, and its presence here is a sign that someone at Apple trusted the filmmakers.\n\nMaria Bakalova continues to prove that her breakout in Borat Subsequent Moviefilm was not a fluke. Anna Ustinov is a modest role in terms of screen time, but Bakalova gives her a stubbornness and intelligence that makes her more than a plot device. She is her father's daughter: pragmatic, watchful, slow to trust. Her scenes with Branagh have the ease of actors who genuinely like each other. Marcin Dorocinski, as the KGB officer Volkov tracking Kelly and Ustinov, makes a credible antagonist without descending into cartoon villainy. He is a man doing a job he believes in, which makes him more frightening than a mustache-twirler ever could be. David Morse appears briefly as Kelly's father in flashback, and his two scenes provide the emotional architecture for Kelly's entire character arc. Morse can do more with a look than most actors can with a monologue.\n\nIs Mayday a great film? No. It is not trying to be. It is a well-made, thoroughly entertaining action comedy that honors the traditions of its genre without apologizing for them. In 2026, that qualifies as a minor miracle. The critical reception has been mixed (60 on Metacritic), and that is probably fair: this is not a film that reinvents anything. But it executes everything it attempts with craft and conviction, and it does so without once asking the audience to feel bad about enjoying an American action hero. That is not nothing. That is worth supporting.",
        "parentalGuidance": "Rated PG-13 for action violence, language, and some suggestive material. The action includes gunfire, explosions, hand-to-hand combat, and several on-screen deaths, none of which are gory or lingered on. Language is frequent but not extreme: typical Reynolds banter with a few stronger words. Some suggestive humor and banter but no sex scenes or nudity. The Cold War setting involves Soviet military forces as antagonists, but the film draws a distinction between the Soviet state and individual Russian characters. The central relationship between Kelly and Ustinov models cross-cultural respect and cooperation without either man abandoning his principles. Suitable for teens 13 and up. Parents may want to discuss: What does it mean to serve your country? Can you love your country and still recognize its flaws? What makes someone decide to defect? How do Kelly and Ustinov earn each other's trust, and what does that say about trust in general?"
    },
    "tropeAudit": {
        "woke": [
            {
                "trope": "None material. A brief scene shows a female CIA analyst being competent (played by a supporting actress), but her competence is earned through demonstrated expertise rather than narrative fiat. No WOKE tropes register above the scoring threshold.",
                "id": "NONE",
                "category": "WOKE",
                "location": "N/A",
                "authenticity": "N/A"
            }
        ],
        "traditional": [
            {
                "trope": "The Rugged Individualist (TRADITIONAL-028)",
                "id": "TRADITIONAL-028",
                "category": "TRAD",
                "location": "Throughout. Kelly operates alone behind enemy lines, surviving through skill, improvisation, and refusal to quit. His competence is earned (he is a trained SR-71 pilot, not a random civilian who suddenly becomes a supersoldier). The film celebrates his resourcefulness without making it a political statement.",
                "authenticity": "Natural"
            },
            {
                "trope": "The Self-Sacrificing Hero (TRADITIONAL-026)",
                "id": "TRADITIONAL-026",
                "category": "TRAD",
                "location": "Second and third acts. Kelly repeatedly risks his life to protect Ustinov and Anna, and Ustinov returns the favor. Neither man's sacrifice is performative; both are the logical extension of characters who value others above themselves.",
                "authenticity": "Natural"
            },
            {
                "trope": "The Principled Patriarch (TRADITIONAL-029)",
                "id": "TRADITIONAL-029",
                "category": "TRAD",
                "location": "Ustinov's relationship with Anna. He is a father who provides firm, loving leadership. His protective instinct is portrayed as a virtue, not as 'toxic masculinity.' He has built a life for his daughter after leaving the KGB, and every decision he makes is filtered through his love for her.",
                "authenticity": "Natural"
            },
            {
                "trope": "Defense of the Innocent (TRADITIONAL-045)",
                "id": "TRADITIONAL-045",
                "category": "TRAD",
                "location": "Third act. Both Kelly and Ustinov place themselves between Anna and the pursuing KGB forces. The climactic confrontation is framed as good men protecting an innocent person from state violence, with no ironic distance or deconstruction.",
                "authenticity": "Natural"
            },
            {
                "trope": "Industry and Perseverance (TRADITIONAL-041)",
                "id": "TRADITIONAL-041",
                "category": "TRAD",
                "location": "Throughout. Survival is earned through hard work: navigation without technology, wilderness survival, mechanical repair, and physical endurance. The film shows characters getting tired, hungry, and injured, and continuing anyway. Success is the product of effort, not luck or identity.",
                "authenticity": "Natural"
            },
            {
                "trope": "Justice Restored (TRADITIONAL-047)",
                "id": "TRADITIONAL-047",
                "category": "TRAD",
                "location": "Third act resolution. The antagonists face consequences for their actions. The guilty are punished, the innocent are saved, and order is restored. The ending does not wink at the audience or suggest that 'justice' is a naive concept.",
                "authenticity": "Natural"
            }
        ]
    },
    "trope_analysis": {}
}

# ============================================================
# REVIEW 2: American Psycho (2000)
# ============================================================
american_psycho = {
    "id": "american-psycho-2000",
    "slug": "american-psycho-2000",
    "title": "American Psycho",
    "year": 2000,
    "type": "film",
    "platform": "VOD, Physical Media",
    "genre": "Psychological Thriller, Satire, Horror",
    "date": "2026-09-05",
    "datePublished": "2026-09-05",
    "author": "VirtueVigil Editorial Team",
    "readTime": "10 min",
    "poster": "/images/posters/american-psycho-2000.jpg",
    "releaseDate": "2000-04-14",
    "rating": "R (Strong Violence, Sexuality, Drug Use, Language)",
    "runtime": "102 minutes",
    "director": "Mary Harron",
    "writers": ["Mary Harron", "Guinevere Turner"],
    "cast": [
        {"name": "Christian Bale", "role": "Patrick Bateman"},
        {"name": "Willem Dafoe", "role": "Donald Kimball"},
        {"name": "Jared Leto", "role": "Paul Allen"},
        {"name": "Josh Lucas", "role": "Craig McDermott"},
        {"name": "Chloe Sevigny", "role": "Jean"},
        {"name": "Reese Witherspoon", "role": "Evelyn Williams"},
        {"name": "Samantha Mathis", "role": "Courtney Rawlinson"},
        {"name": "Justin Theroux", "role": "Timothy Bryce"}
    ],
    "studio": "Edward R. Pressman Productions, Muse Productions",
    "distributor": "Lions Gate Films",
    "verdict": "TRADITIONAL",
    "wokeScore": 7.50,
    "tradScore": 15.60,
    "authIndex": 75,
    "scoreMargin": "+8 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Not a woke trap. American Psycho was released in 2000, well before Hollywood's ideological capture. Director Mary Harron is a feminist, and the film does critique male vanity and violence, but this critique is present from the opening scene and is integral to the satire, not hidden. The film does not present itself as apolitical and then spring a progressive lecture in the third act. It is a psychological thriller about a monster from the first frame to the last. Harron's feminist lens is applied to the source material honestly—she is adapting Bret Easton Ellis's novel, which was itself a satire of consumerism and male narcissism. The film treats Patrick Bateman as unambiguously evil, and its moral framework is clear: murder is wrong, vanity is hollow, and the Wall Street culture that enables Bateman is a vacuum of meaning. None of this is hidden or subverted past the midpoint."
    },
    "seo": {
        "titleTag": "Is American Psycho (2000) Woke? Christian Bale Cult Classic VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of American Psycho (2000), Mary Harron's psychological thriller starring Christian Bale as Patrick Bateman. Verdict: TRADITIONAL (+8 TRAD). Full trope analysis and parental guidance included.",
        "keywords": "is american psycho woke, american psycho review, american psycho virtuevigil, patrick bateman, american psycho traditional or woke, american psycho parents guide, christian bale american psycho"
    },
    "externalScores": {
        "imdb": "7.6/10",
        "rottenTomatoes": "68%",
        "metacritic": "64"
    },
    "creative_team": {
        "director": {
            "name": "Mary Harron",
            "ideology": "FEMINIST (Artistic, Not Activist)",
            "profile": "Mary Harron is a Canadian director and screenwriter known for I Shot Andy Warhol (1996), American Psycho (2000), and The Notorious Bettie Page (2005). She began her career as a music journalist and was part of the 1970s New York punk scene. Harron identifies as a feminist, but her filmmaking is more interested in character and psychology than in political messaging. She fought to direct American Psycho after the studio initially wanted a male director, and her vision—toning down the novel's graphic violence while amplifying its satirical edge—is the reason the film works. Harron's feminism is of the second-wave variety: interested in power dynamics, gender roles, and the male gaze, but expressed through art rather than lecture. She does not fit the contemporary 'woke' filmmaker profile. Her subsequent work (The Notorious Bettie Page, Charlie Says) confirms a consistent interest in complicated women and the systems that shape them, but she approaches these subjects as a storyteller, not an activist."
        },
        "writer": {
            "name": "Mary Harron, Guinevere Turner",
            "profile": "Harron and Turner co-wrote the screenplay, adapting Bret Easton Ellis's controversial 1991 novel. Their adaptation is widely considered superior to its source material: they excised the novel's most gratuitous violence while preserving its satirical bite, and they added a layer of dark humor that Ellis's prose, for all its shock value, lacked. Turner is an actress and screenwriter (Go Fish, The Watermelon Woman) whose work often explores lesbian identity and feminist themes. In American Psycho, her contribution can be felt in the script's sharper observations about the way the film's female characters are treated by the men around them. The screenplay is a genuinely collaborative work that balances Ellis's nihilism with Harron and Turner's more humane perspective."
        },
        "lead_producer": {
            "name": "Edward R. Pressman, Chris Hanley, Christian Halsey Solomon",
            "company": "Edward R. Pressman Productions / Muse Productions"
        },
        "composer": {
            "name": "John Cale"
        },
        "top_cast": [
            {"name": "Christian Bale", "role": "Patrick Bateman"},
            {"name": "Willem Dafoe", "role": "Donald Kimball"},
            {"name": "Jared Leto", "role": "Paul Allen"}
        ],
        "producers": ["Edward R. Pressman", "Chris Hanley", "Christian Halsey Solomon"],
        "full_cast": [
            {"name": "Christian Bale", "role": "Patrick Bateman"},
            {"name": "Willem Dafoe", "role": "Donald Kimball"},
            {"name": "Jared Leto", "role": "Paul Allen"},
            {"name": "Josh Lucas", "role": "Craig McDermott"},
            {"name": "Chloe Sevigny", "role": "Jean"},
            {"name": "Reese Witherspoon", "role": "Evelyn Williams"},
            {"name": "Samantha Mathis", "role": "Courtney Rawlinson"},
            {"name": "Justin Theroux", "role": "Timothy Bryce"},
            {"name": "Bill Sage", "role": "David Van Patten"},
            {"name": "Cara Seymour", "role": "Christie"},
            {"name": "Guinevere Turner", "role": "Elizabeth"}
        ]
    },
    "fidelityCasting": "",
    "spoiler_alert": True,
    "summary": {
        "overall": "American Psycho is a film that has been misunderstood by almost everyone at some point. It has been claimed by men's rights activists as a celebration of masculine aggression. It has been claimed by feminists as a condemnation of male violence. It has been memed into oblivion by people who have never seen it. The truth, as with most things, is more interesting than any of the reductive readings: American Psycho is a pitch-black satire of consumerism, vanity, and the emptiness of a life defined entirely by surfaces, and it happens to star one of the most frightening and funny performances in American film history. Christian Bale's Patrick Bateman is a Wall Street investment banker whose entire identity is a performance. He cares about his skincare routine, his business card, his reservations at Dorsia, and the bodies he stacks in his apartment. The film, directed by Mary Harron from a script she co-wrote with Guinevere Turner, is explicitly a feminist reading of Bret Easton Ellis's novel, and that is not an insult. Harron and Turner understood something that Ellis's defenders often miss: the book is not celebrating Bateman. It is diagnosing a type of man who is so hollow that even serial murder cannot fill the void. The film makes this diagnosis sharper, funnier, and more coherent than the novel ever managed.\n\nThe question for VirtueVigil is whether this feminist diagnosis constitutes 'woke' content, and the answer requires a distinction that matters. Harron's feminism is not the identitarian progressivism of 2026. It is a second-wave critique of male power and violence, expressed through art rather than activism. The film does not argue that masculinity is inherently toxic. It argues that a specific type of masculinity—rooted in consumerism, competition, and emotional vacancy—is corrosive. That is a narrower, more defensible claim than the modern 'toxic masculinity' framework, which tends to pathologize male protectiveness and ambition wholesale. Bateman is not a stand-in for men. He is a stand-in for a culture that values surfaces over substance, and the film's critique of that culture is earned through ninety minutes of meticulous characterization. The difference between Harron's approach and a contemporary woke director's approach is that Harron trusts the audience to reach the conclusion. She does not have a character look at the camera and explain the thesis. She shows you Bateman, makes you laugh at him, makes you fear him, and lets you draw your own conclusions. That is the difference between art and propaganda, and American Psycho is art.\n\nThe film's moral framework is traditionally coherent, which is notable given the subject matter. Bateman is evil. The film never wavers on this point. His victims are innocent. The violence, while stylized, is never glamorous. Harron films the murders with a clinical distance that makes them more disturbing, not less. When Bateman kills Paul Allen (Jared Leto) while monologuing about Huey Lewis and the News, the scene is simultaneously hilarious and horrifying. You laugh because Bateman's earnest music criticism is so absurd in context. You recoil because you are watching a man be murdered with an axe. The film holds both reactions in tension and trusts you to sort them out. That trust in the audience is the film's greatest formal achievement and the clearest evidence that Harron is a filmmaker, not a propagandist. A woke director would have made sure you knew exactly what to think. Harron lets you think for yourself, and the film is more powerful because of it.\n\nSome have read the ending as morally ambiguous: does Bateman get away with it? The film leaves this genuinely unclear, and that ambiguity is the point. In a world where everyone is interchangeable and no one pays attention, a monster can hide in plain sight. This is not an endorsement of relativism. It is a diagnosis of a specific cultural pathology, and the film presents that diagnosis without celebrating it. The ambiguity is chilling, not liberating. Compare this to a modern equivalent that would frame Bateman's escape from consequences as evidence that 'the system protects white men'—a reductive political claim that turns ambiguity into agitprop. Harron's ambiguity is richer and more honest. It says: sometimes evil goes unpunished because the world is not paying attention. That is a traditional moral insight dressed in postmodern clothes.",
        "adultInsight": "American Psycho rewards rewatching more than most films. The first viewing is a visceral experience: Bale's performance is so committed, so physically precise, that you spend most of the runtime trying to figure out if you are allowed to laugh. On subsequent viewings, with the shock absorbed, the film reveals itself as a meticulous character study and a genuinely funny dark comedy. Bale's Bateman is a man who has studied human behavior without ever understanding it. His conversations are recitations of magazine articles and restaurant reviews. His relationships are transactions. His violence is the only thing that makes him feel anything, and even that is becoming routine. Bale plays this with a physical commitment that borders on method-actor insanity: the way his jaw tightens when someone has a better business card, the way his eyes go dead during sex, the way he runs, naked and sweaty and screaming, through his apartment building. It is one of the great American film performances, and it is hard to imagine anyone else in the role. (The studio initially wanted Leonardo DiCaprio, which would have been a different movie entirely and almost certainly a worse one.)\n\nWillem Dafoe, as the detective Kimball investigating Paul Allen's disappearance, plays his scenes with Harron's cleverest directorial choice: she told Dafoe to play some takes as if Kimball knows Bateman is guilty, some as if he suspects nothing, and some as if he is not sure. The editor then cut between takes, making Kimball's intentions genuinely unknowable. The result is a character who feels like a threat even when he is asking polite questions. Chloe Sevigny, as Bateman's secretary Jean, gives the film's most human performance. Jean is the only person in Bateman's orbit who seems to see him as a person rather than a status symbol, and Sevigny plays her with a vulnerability that makes the film's darkest scene—Bateman nearly killing her, then stopping—genuinely moving rather than merely tense. Reese Witherspoon, in a small role as Bateman's fiancee Evelyn, plays vapid perfection with comic precision. Her scene planning a wedding while Bateman stares through her like she is made of glass is a miniature masterpiece of obliviousness.\n\nThe film's use of music is legendary for good reason. Bateman's monologues about Huey Lewis, Phil Collins, and Whitney Houston are simultaneously accurate music criticism and chilling preludes to violence. The juxtaposition of 'Sussudio' with a murder scene is one of cinema's great tonal achievements. John Cale's score, all droning strings and ambient dread, provides the psychological undercurrent that Bale's performance rides. The production design, all white apartments and gleaming surfaces, creates a world where nothing feels real because nothing is real. That is the film's thesis, and every formal choice reinforces it.\n\nIs American Psycho a conservative film? No. Is it a woke film? Also no. It is a film made by talented people who had something to say about the culture they lived in, and who said it through character and craft rather than through lecture. If that distinction seems too fine, consider this: a truly woke American Psycho would end with a speech about male privilege. Harron's American Psycho ends with Bateman staring at a television, realizing that nothing he has done matters because no one was paying attention. That is a more disturbing ending, and a truer one, than any political statement could be. The film diagnoses a sickness. It does not prescribe a cure. And in an era when every film is expected to both diagnose and prescribe, that restraint feels like integrity.",
        "parentalGuidance": "Rated R for strong violence, sexuality, drug use, and language. This is a hard R. The violence includes multiple murders with weapons (axe, chainsaw, knife, gun), some depicted with graphic detail. A chainsaw chase through an apartment building is particularly intense. Sexual content includes multiple scenes of sex and nudity, some of which are intertwined with violence. Drug use (cocaine) is frequent and depicted casually. Language is extremely strong throughout. The film's subject matter—a serial killer who targets women—is inherently disturbing. Not suitable for anyone under 17. Even for adults, the film should be understood as a satire, not a thriller to be enjoyed uncritically. Parents considering watching with older teens (17+) should be prepared for a conversation about the difference between depicting evil and endorsing it. The film does not endorse Bateman's violence; it condemns it through every formal and narrative choice. But the condemnation is artistic, not explicit, and younger viewers may need help articulating what they are seeing."
    },
    "tropeAudit": {
        "woke": [
            {
                "trope": "The Toxic Masculinity Critique (WOKE-011)",
                "id": "WOKE-011",
                "category": "WOKE",
                "location": "Throughout. The film is explicitly a critique of male violence, vanity, and emotional repression. Bateman embodies a specific type of masculinity that is competitive, consumerist, and fundamentally hollow. His violence is the logical endpoint of his inability to connect with other humans. However, Harron's critique is specific rather than universal: she is diagnosing a cultural pathology, not arguing that masculinity per se is toxic. The film distinguishes between Bateman's monstrousness and the ordinary masculinity of characters like Kimball (Willem Dafoe).",
                "authenticity": "Natural"
            },
            {
                "trope": "The Evil Capitalist (WOKE-014)",
                "id": "WOKE-014",
                "category": "WOKE",
                "location": "Throughout. Wall Street is portrayed as a vacuum of meaning where wealth, status, and appearance are the only values. Bateman and his colleagues are indistinguishable from one another (the running joke about mistaken identities). The film's satire of 1980s finance culture is sharp and earned. However, the critique is of consumerism and emptiness, not of capitalism as an economic system. Bateman is not evil because he is a capitalist; he is evil because he is empty, and capitalism happens to be the arena where his emptiness plays out.",
                "authenticity": "Natural"
            }
        ],
        "traditional": [
            {
                "trope": "Objective Good vs. Evil (TRADITIONAL-039)",
                "id": "TRADITIONAL-039",
                "category": "TRAD",
                "location": "Throughout. Bateman is unambiguously evil. The film never wavers, never 'complicates' his villainy, never suggests that his actions might be justified by systemic forces. He kills because he wants to. The moral framework is clear: murder is wrong, Bateman is a murderer, and his charm and wealth do not mitigate that. This clarity is rare in contemporary cinema and is the strongest traditional element in the film.",
                "authenticity": "Natural"
            },
            {
                "trope": "The Redemptive Arcs (Personal) (TRADITIONAL-027)",
                "id": "TRADITIONAL-027",
                "category": "TRAD",
                "location": "The Jean scene (third act). Bateman's secretary Jean (Chloe Sevigny) represents genuine goodness—kindness, modesty, decency—and when Bateman has the opportunity to kill her, he stops himself. He does not understand why he stops, but the film suggests that Jean's authentic humanity touches something in him that his superficial world cannot reach. This is not a full redemption arc, but it is a traditional acknowledgment that even the worst person may retain a sliver of moral awareness.",
                "authenticity": "Natural"
            },
            {
                "trope": "The Principled Patriarch (TRADITIONAL-029)",
                "id": "TRADITIONAL-029",
                "category": "TRAD",
                "location": "Absent in Bateman but present by inversion. The film shows what happens when male authority is stripped of all principle: Bateman is a patriarch without principles, and the result is monstrosity. The film's horror depends on the audience understanding what a principled patriarch would look like by showing the absence of one. This is traditional morality operating as negative space.",
                "authenticity": "Natural"
            },
            {
                "trope": "Justice Restored (TRADITIONAL-047)",
                "id": "TRADITIONAL-047",
                "category": "TRAD",
                "location": "The ending is ambiguous about whether Bateman faces legal consequences, but the moral consequence is clear: he is trapped in a hell of his own making. His confession goes unheard. His crimes go unpunished. But he is not free—he is condemned to continue being himself, and the film frames this as a fate worse than prison. Traditional justice operates morally even when it fails legally.",
                "authenticity": "Natural"
            },
            {
                "trope": "Biblical Morality (TRADITIONAL-030)",
                "id": "TRADITIONAL-030",
                "category": "TRAD",
                "location": "The film's moral universe is Judeo-Christian in structure. Murder is a sin. Vanity is a sin. Greed is a sin. Bateman commits all of them and is damned by the narrative even if he is not damned by the legal system. The film judges him. The audience is meant to judge him. This is a moral framework that would be recognizable to any traditional religious tradition.",
                "authenticity": "Natural"
            }
        ]
    },
    "trope_analysis": {}
}

# ============================================================
# REVIEW 3: WandaVision (2021)
# ============================================================
wandavision = {
    "id": "wandavision-2021",
    "slug": "wandavision-2021",
    "title": "WandaVision",
    "year": 2021,
    "type": "series",
    "platform": "Disney+",
    "genre": "Superhero, Drama, Mystery, Sitcom",
    "date": "2026-09-05",
    "datePublished": "2026-09-05",
    "author": "VirtueVigil Editorial Team",
    "readTime": "11 min",
    "poster": "/images/posters/wandavision-2021.jpg",
    "releaseDate": "2021-01-15",
    "rating": "TV-14 (Violence, Thematic Elements, Emotional Distress)",
    "runtime": "9 episodes, 30-50 min each",
    "director": "Matt Shakman",
    "writers": ["Jac Schaeffer"],
    "showrunner": "Jac Schaeffer",
    "cast": [
        {"name": "Elizabeth Olsen", "role": "Wanda Maximoff / Scarlet Witch"},
        {"name": "Paul Bettany", "role": "Vision"},
        {"name": "Kathryn Hahn", "role": "Agatha Harkness"},
        {"name": "Teyonah Parris", "role": "Monica Rambeau"},
        {"name": "Randall Park", "role": "Jimmy Woo"},
        {"name": "Kat Dennings", "role": "Darcy Lewis"},
        {"name": "Evan Peters", "role": "Ralph Bohner / 'Pietro'"},
        {"name": "Josh Stamberg", "role": "Director Tyler Hayward"}
    ],
    "studio": "Marvel Studios",
    "distributor": "Disney+",
    "verdict": "WOKE",
    "wokeScore": 16.20,
    "tradScore": 8.40,
    "authIndex": 42,
    "scoreMargin": "-8 WOKE",
    "preRelease": False,
    "wokeTrap": True,
    "woke_trap_assessment": {
        "is_trap": True,
        "pct_runtime": 58,
        "explanation": "WandaVision is a textbook woke trap under VVWS criteria. The first three episodes (approximately 35% of runtime) present as a loving, puzzling sitcom homage: a married couple navigating suburban life in different TV eras. The mystery is intriguing, the tone is warm, and the ideological content is near zero. Episodes 4-5 (the next 25%) transition to the 'real world' outside Westview, introducing SWORD agent Monica Rambeau and FBI agent Jimmy Woo, but the ideological framework is still ambiguous. It is not until episodes 6-9 (the final 40%, well past the 50% threshold) that the full woke architecture locks in: Director Hayward is revealed as a cartoonishly villainous male authority figure who tries to kill children, SWORD is exposed as a corrupt institution that experimented on Vision's corpse, Monica Rambeau gains superpowers by 'persevering' through a misogynistic superior's orders, Wanda's enslavement of an entire town is reframed as her personal grief journey rather than a crime, and Agatha Harkness is set up for her own redemption-spin-off. The show sells itself as a charming mystery and delivers a sermon on female empowerment, institutional corruption, and victimhood-as-moral-currency. The first half is bait. The second half is the switch."
    },
    "seo": {
        "titleTag": "Is WandaVision (2021) Woke? Disney+ Marvel Series VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of WandaVision (2021), the Disney+ Marvel series starring Elizabeth Olsen and Paul Bettany. Sitcom homage reveals woke trap. Verdict: WOKE (-8). Full trope analysis and parental guidance.",
        "keywords": "is wandavision woke, wandavision review, wandavision virtuevigil, wandavision woke, wandavision parents guide, wandavision traditional or woke, scarlet witch review"
    },
    "externalScores": {
        "imdb": "7.9/10",
        "rottenTomatoes": "91%",
        "metacritic": "77"
    },
    "creative_team": {
        "director": {
            "name": "Matt Shakman",
            "ideology": "MODERATE (Hired Gun)",
            "profile": "Matt Shakman is a television director whose primary credit before WandaVision was It's Always Sunny in Philadelphia. He was hired to execute Jac Schaeffer's vision, not to impose his own. His direction is technically accomplished: the period-specific sitcom pastiches are note-perfect, and the transition from multi-camera comedy to single-camera superhero action is smoothly handled. Shakman's subsequent assignment to direct Fantastic Four for Marvel suggests the studio was happy with his work. He does not have a public ideological profile."
        },
        "writer": {
            "name": "Jac Schaeffer",
            "profile": "Jac Schaeffer is the creator, head writer, and showrunner of WandaVision. Her previous credits include writing The Hustle (2019) and contributing to Captain Marvel (2019) and Black Widow (2021). Schaeffer has spoken in interviews about her interest in 'female interiority' and 'deconstructing the male gaze.' Her approach to WandaVision was explicitly to center Wanda's grief and trauma as the engine of the narrative. This is not inherently political, but Schaeffer's execution reveals her ideological commitments: the male authority figure (Hayward) is cartoonishly evil, the female characters are given moral passes for behavior that would be condemned in male characters, and the series' resolution treats Wanda's enslavement of Westview as a tragedy that happened to her rather than a crime she committed. Schaeffer's subsequent creation of Agatha All Along confirms this pattern."
        },
        "lead_producer": {
            "name": "Kevin Feige",
            "company": "Marvel Studios"
        },
        "composer": {
            "name": "Christophe Beck"
        },
        "top_cast": [
            {"name": "Elizabeth Olsen", "role": "Wanda Maximoff"},
            {"name": "Paul Bettany", "role": "Vision"},
            {"name": "Kathryn Hahn", "role": "Agatha Harkness"}
        ],
        "producers": ["Kevin Feige", "Louis D'Esposito", "Victoria Alonso", "Matt Shakman", "Jac Schaeffer"],
        "full_cast": [
            {"name": "Elizabeth Olsen", "role": "Wanda Maximoff / Scarlet Witch"},
            {"name": "Paul Bettany", "role": "Vision"},
            {"name": "Kathryn Hahn", "role": "Agatha Harkness"},
            {"name": "Teyonah Parris", "role": "Monica Rambeau"},
            {"name": "Randall Park", "role": "Jimmy Woo"},
            {"name": "Kat Dennings", "role": "Darcy Lewis"},
            {"name": "Evan Peters", "role": "Ralph Bohner"},
            {"name": "Josh Stamberg", "role": "Director Tyler Hayward"},
            {"name": "Debra Jo Rupp", "role": "Mrs. Hart"},
            {"name": "Fred Melamed", "role": "Arthur Hart"},
            {"name": "Julian Hilliard", "role": "Billy Maximoff"},
            {"name": "Jett Klyne", "role": "Tommy Maximoff"}
        ]
    },
    "fidelityCasting": "",
    "spoiler_alert": True,
    "summary": {
        "overall": "WandaVision is the best thing Marvel Studios has ever made, and also the clearest demonstration of why Marvel Studios cannot be trusted. The series, created by Jac Schaeffer and directed by Matt Shakman, begins as a genuinely brilliant formal experiment: nine episodes that progress through the history of American television sitcoms, from the 1950s through the 2010s, with Wanda Maximoff (Elizabeth Olsen) and Vision (Paul Bettany) as the married couple at the center of an increasingly wrong suburban fantasy. The first three episodes are so good, so committed to their premise, so unusual for a superhero property, that you almost forget you are watching a Disney+ series designed to sell the next phase of the Marvel Cinematic Universe. Almost. Because by episode four, the spell breaks, and what replaces it is a competent but ideologically conventional MCU product that uses its formal innovation as camouflage for a deeply progressive moral framework. The show's defenders will tell you it is about grief. That is true, but it is about grief in the way that a Times op-ed is about current events: the surface is accurate, but the framing does all the work. WandaVision is about a woman whose personal trauma is so profound, so cosmically unfair, that her enslavement of an entire town of innocent people is presented as something that happened to her, not something she did. That framing is the show's central ideological move, and everything else—the sitcom pastiche, the mystery-box plotting, the fan-service cameos—is in service of making you accept it.\n\nThe show's treatment of Wanda is instructive. In any morally coherent story, a character who imprisons thousands of people in a psychic nightmare against their will, who forces them to play roles in her domestic fantasy, who causes them physical and psychological distress every moment of every day—that character would be the villain. WandaVision does not make Wanda the villain. It makes her the protagonist whose grief we are meant to understand and forgive. When the citizens of Westview are finally freed in the finale, one of them tells Wanda, 'They'll never know what you sacrificed for them.' This line, delivered to a woman who has just ended the torture she chose to inflict, is so morally inverted that it functions as a kind of Rorschach test. If you hear that line and think it is beautiful, WandaVision has worked on you exactly as intended. If you hear it and think it is grotesque, you are seeing the show's ideological machinery for what it is. The line is not an accident. It is the thesis. Wanda's victimhood is the only moral currency that matters. The people she victimized are an afterthought, a prop in her healing journey. Their suffering exists to make her sacrifice meaningful. This is victimhood meritocracy in its purest form: the more you have suffered, the less accountable you are for the suffering you cause.\n\nThe show's secondary characters reinforce this framework. Monica Rambeau (Teyonah Parris) is introduced as a capable SWORD agent who returns from the Blip to find her mother has died of cancer. She is immediately undermined by the acting director, Tyler Hayward (Josh Stamberg), who disrespects her expertise and eventually tries to kill her and Wanda's children. Hayward is not a character; he is a function. He exists to make Monica look good and to give the audience someone to hate more than Wanda. His villainy is so cartoonish—experimenting on Vision's corpse, shooting at children, lying to the FBI—that it serves as a misdirection: if Hayward is this evil, how bad can Wanda really be? The answer the show wants you to give is 'not that bad.' The answer the show's own evidence suggests is 'worse than Hayward, actually, because she did it to thousands of people for weeks while he was just a corrupt bureaucrat.' But the show does not want you to do that math. It wants you to feel for Wanda and hate Hayward, and the juxtaposition is designed to short-circuit your moral reasoning.\n\nAgatha Harkness (Kathryn Hahn) is the show's best character and its most honest one. She is a witch who has been alive for centuries, and she sees Wanda's Westview project for what it is: an immense, uncontrolled expression of power by a woman who does not understand what she is doing. Agatha's theme song, 'Agatha All Along,' is the show's high point—a genuinely clever meta-joke that works as both parody and plot revelation. But Agatha, like Hayward, serves a structural purpose that undermines Wanda's moral accountability. By making Agatha the 'real' antagonist—the one who wants to steal Wanda's power—the show gives Wanda someone to defeat, which transforms her from perpetrator to hero without her ever having to reckon with what she did to Westview. The finale features Wanda fighting Agatha while the citizens of Westview beg her to let them go. She lets them go. She is celebrated for it. The show treats this as a resolution when it is actually an abdication.",
        "adultInsight": "The performances in WandaVision range from excellent to functional. Elizabeth Olsen does career-best work as Wanda, grounding the character's cosmic grief in recognizable human behavior. Her sitcom performances, shifting styles from decade to decade, are technically impressive and emotionally legible. When the show gives her moments of raw pain—discovering Vision's dismantled body in the SWORD lab, saying goodbye to her constructed children in the finale—Olsen sells them completely. The problem is not the performance. The problem is that the show asks Olsen to sell a moral framework that does not hold up to scrutiny. She is being asked to make you feel for a character who is doing monstrous things, and because she is a gifted actor, she succeeds. But the show's sympathy for Wanda is authorial, not just performative. Schaeffer's writing treats Wanda's grief as inherently ennobling, as if suffering great loss automatically makes your subsequent actions more understandable, if not more defensible. This is a common progressive assumption—that victimhood confers moral authority—and it runs through WandaVision like a spine.\n\nPaul Bettany has the more difficult job. Vision is dead. The Vision in Westview is a construct Wanda created from her grief and her memory of the Mind Stone. Bettany plays him as a sitcom husband who gradually becomes aware that something is wrong with his reality, and his growing unease gives the middle episodes their dramatic tension. His debate with the 'real' Vision (also Bettany, also a construct, it is complicated) in the finale, resolved through a discussion of the Ship of Theseus paradox, is the show's most intellectually ambitious sequence. It also has nothing to do with the moral question at the heart of the series, which is: what do we owe the people we hurt? The philosophical detour is elegant, but it is a detour. The show would rather discuss identity metaphysics than moral accountability because the former is safely abstract and the latter would require condemning its protagonist.\n\nKathryn Hahn's Agatha is so much fun to watch that you almost miss how cynical her function is. She is the villain the show can safely defeat, the external threat that allows Wanda to transition from problem to solution without ever having to face justice for Westview. Hahn plays her with such relish—the wink, the cackle, the theme song—that she becomes the audience surrogate for the show's more honest impulses. Agatha is the only character who treats Wanda's power as genuinely dangerous and her actions as genuinely monstrous. The show needs to defeat her to complete Wanda's arc, but Agatha is not wrong. She is just mean about it.\n\nTechnically, WandaVision is remarkable. The period-specific production design, costume work, and cinematography are among the best things Marvel has ever done. The progression from 1950s Dick Van Dyke Show aesthetics through 2000s Modern Family mockumentary is executed with obsessive detail. Christophe Beck's score weaves period-appropriate sitcom themes into the broader MCU musical vocabulary. The theme songs by Kristen Anderson-Lopez and Robert Lopez are miniature masterpieces of pastiche. All of this craft is in service of a show that ultimately wants you to feel sorry for a woman who enslaved a town, and the gap between the formal achievement and the moral content is where WandaVision lives. It is beautiful. It is wrong.",
        "parentalGuidance": "Rated TV-14 for violence, thematic elements, and emotional distress. The violence is mostly superhero-appropriate: energy blasts, witch magic, some hand-to-hand combat. More disturbing are the psychological elements: the citizens of Westview are shown experiencing Wanda's grief as their own, unable to move, unable to speak, trapped in their own minds while Wanda's fantasy plays out around them. One scene where the townspeople beg Wanda to let them die rather than continue suffering is genuinely upsetting and may be too intense for younger viewers. The series also deals heavily with grief, loss, and trauma. Vision's physical form is shown being dismantled in a laboratory. Wanda visits the property deed for a house they planned to build together, a scene of quiet devastation. Thematic elements include mind control, imprisonment, and moral relativism. The show's treatment of Wanda's actions as sympathetic rather than villainous may require parental discussion: younger viewers may absorb the show's framing uncritically, believing that grief justifies harmful behavior. Parents should be prepared to discuss the difference between understanding why someone does something wrong and excusing them for doing it. Suitable for teens 14 and up with parental guidance on the moral framework."
    },
    "tropeAudit": {
        "woke": [
            {
                "trope": "The Girl Boss (WOKE-003)",
                "id": "WOKE-003",
                "category": "WOKE",
                "location": "Throughout, primarily Monica Rambeau (Teyonah Parris) and Wanda. Monica is a SWORD agent who is consistently undermined by the male director (Hayward) but proves herself through 'perseverance,' gaining superpowers by repeatedly entering and exiting the Westview Hex. Her power acquisition is framed as a reward for being disrespected. Wanda's arc treats her immense, dangerous power as a natural extension of her emotional depth rather than something she should learn to control before it hurts more people.",
                "authenticity": "Forced"
            },
            {
                "trope": "The Bumbling Patriarch (WOKE-002)",
                "id": "WOKE-002",
                "category": "WOKE",
                "location": "Director Tyler Hayward (Josh Stamberg). The acting director of SWORD is incompetent, dishonest, and eventually murderous. He lies about Wanda stealing Vision's body, experiments on Vision's corpse to create a weapon, shoots at children, and is generally wrong about everything. His only narrative function is to be worse than Wanda so that Wanda looks better by comparison. A classic example of a male authority figure written to make female characters look competent and moral by contrast.",
                "authenticity": "Forced"
            },
            {
                "trope": "Institutional Evil (WOKE-004)",
                "id": "WOKE-004",
                "category": "WOKE",
                "location": "SWORD throughout the series. The agency that was supposed to protect people from extraterrestrial threats is revealed to be corrupt at its highest levels, experimenting on sentient beings and prioritizing weapon development over human life. The show draws no distinction between specific corrupt individuals and the institution itself; SWORD is presented as systemically rotten. This is standard MCU institutional cynicism but is particularly aggressive here.",
                "authenticity": "Forced"
            },
            {
                "trope": "The Victimhood Meritocracy (WOKE-009)",
                "id": "WOKE-009",
                "category": "WOKE",
                "location": "Wanda's entire character arc. Her grief over losing Vision and her parents is treated as moral currency that entitles her to the audience's sympathy regardless of her actions. The citizens of Westview—who have been imprisoned, mind-controlled, and forced to experience Wanda's nightmares—are given approximately thirty seconds of screen time as victims before the show returns to centering Wanda's pain. A Westview resident explicitly tells Wanda, 'They'll never know what you sacrificed for them,' which reframes the perpetrator as the victim and the victims as ungrateful. This is the show's clearest ideological statement.",
                "authenticity": "Forced"
            },
            {
                "trope": "The Toxic Masculinity Critique (WOKE-011)",
                "id": "WOKE-011",
                "category": "WOKE",
                "location": "Hayward's characterization. His villainy is coded as specifically masculine: he is aggressive, dismissive of female expertise, obsessed with weapons, and willing to sacrifice children for his goals. The show contrasts him with the nurturing female characters (Monica, Darcy, even Wanda) who value connection and empathy over power. The critique is less about toxic behavior and more about male authority per se being inherently suspect.",
                "authenticity": "Forced"
            },
            {
                "trope": "The Fourth-Wall Troll (WOKE-021)",
                "id": "WOKE-021",
                "category": "WOKE",
                "location": "Agatha's theme song and the broader meta-commentary. 'Agatha All Along' functions as a self-congratulatory wink at the audience about how clever the show is. While not a direct social justice lecture, this kind of fourth-wall self-awareness is frequently used in woke media to signal that the creators are smarter than the genre they are working in. The show's sitcom pastiche is, at times, more critique than homage—it is showing you how television used to be, with the implicit understanding that we are all too sophisticated for that now.",
                "authenticity": "Natural"
            }
        ],
        "traditional": [
            {
                "trope": "The Self-Sacrificing Hero (TRADITIONAL-026)",
                "id": "TRADITIONAL-026",
                "category": "TRAD",
                "location": "Vision's sacrifice in the finale. Vision chooses to be erased from existence along with the Westview hex, knowing that his continued existence depends on Wanda's continued enslavement of the town. His choice—to die so that others may live free—is the most traditionally moral act in the series. Bettany plays it with understated dignity. The show undercuts this somewhat by having Wanda's 'sacrifice' of her family be treated as the greater loss, but Vision's moment stands on its own.",
                "authenticity": "Natural"
            },
            {
                "trope": "Sanctity of Marriage (TRADITIONAL-034)",
                "id": "TRADITIONAL-034",
                "category": "TRAD",
                "location": "Wanda and Vision's relationship is the emotional core of the series. Their love is portrayed as genuine, deep, and worth fighting for. The sitcom framework—a married couple navigating life together—is treated with affection rather than irony. The show's best moments are the quiet domestic scenes between Olsen and Bettany, which capture the texture of a real marriage more convincingly than most prestige dramas. This is a genuine traditional element, even if it is in service of a morally compromised protagonist.",
                "authenticity": "Natural"
            },
            {
                "trope": "The Redemptive Arcs (Personal) (TRADITIONAL-027)",
                "id": "TRADITIONAL-027",
                "category": "TRAD",
                "location": "Wanda's decision to release Westview in the finale. After confronting Agatha and the full scope of her power, Wanda chooses to end the hex and let her constructed family disappear. This is framed as growth and redemption. The problem is that the show treats this as sufficient—Wanda's 'redemption' does not involve facing consequences, apologizing to her victims, or being held accountable. The arc is personal (she accepts her grief) but not moral (she accepts her guilt). A traditional redemption arc would require both. WandaVision delivers half of one.",
                "authenticity": "Forced"
            }
        ]
    },
    "trope_analysis": {}
}

# Append all three
reviews.append(mayday)
reviews.append(american_psycho)
reviews.append(wandavision)

# Write back
with open(REVIEWS_PATH, "w") as f:\n    json.dump(reviews, f, indent=2)\n\nprint(f"Reviews: {original_count} -> {len(reviews)} (+3)")
print("Done.")