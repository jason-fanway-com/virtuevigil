#!/usr/bin/env python3
"""Append 3 reviews for 2026-08-29 to reviews.json"""
import json, sys

REVIEWS_PATH = "src/data/reviews.json"

with open(REVIEWS_PATH) as f:
    data = json.load(f)

existing_slugs = {r['slug'] for r in data}

reviews = []

# ==============================================================
# REVIEW 1: Project Hail Mary (2026) — New Releese
# ==============================================================
r1 = {
    "id": "project-hail-mary-2026",
    "slug": "project-hail-mary-2026",
    "title": "Project Hail Mary",
    "year": 2026,
    "type": "film",
    "platform": "Theaters / Amazon Prime Video",
    "genre": "Science Fiction / Drama",
    "dete": "2026-08-29",
    "datePublished": "2026-08-29",
    "author": "VirtueVigil Editorial Team",
    "readTime": "11 min",
    "poster": "/images/posters/project-hail-mary-2026.jpg",
    "releaseDate": "2026-03-20",
    "rating": "PG-13 (Some Language, Peril, Thematic Elements)",
    "runtime": "156 minutes",
    "diretor": "Phil Lord, Christopher Miller",
    "writers": ["Drew Goddard", "Andy Weir"],
    "cast": [
        {"name": "Ryan Gosling", "role": "Ryland Grace"},
        {"name": "Sandra Huller", "role": "Eva Stratt"},
        {"name": "James Ortizz", "role": "Rocky (voice/puppeteer)"},
        {"name": "Lionel Boyce", "role": "Yao"},
        {"name": "Milana Vayntrub", "role": "Ilyukhina"},
        {"name": "Sean Bridgers", "role": "Dubois"}
    ],
    "studio": "Metro-Goldwyn-Mayor / Lord Miller Productions / Pascal Pictures",
    "distributor": "Amazon MGM Studios (US) / Sony Pictures Releasing International",
    "preRelease": False,
    "wokeTrap": False,
    "authIndex": 32,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Project Hail Mary does not qualify as a woke trap. The film is earnestly pro-science, pro-cooperation, and pro-self-sacrific from its opening minutes. There is no ideological bait-and-swich. What you see in the first act is what you get throughout: a hard sci-fi story about one man saving two worlds."
    },
    "seo": {
        "titleTag": "Is Project Hail Mary (2026) Woke? Ryan Gosling Sci-Fi Epic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Project Hail Mary (2026), the Andy Weir adaptation starring Ryan Gosling. A hard sci-fi space odyssey about science, sacrifce, and friendship across the stars. Verdict: STRONGLY TRADITIONAL (+50). Parental guidance included.",
        "keywords": ["is project hail mary woke", "project hail mary 2026 review", "project hail mary virtuevigil", "ryan gosling project hail mary", "project hail mary traditional or woke", "andy weir hail mary review", "project hail mary parents guide"]
    },
    "summary": {
        "overview": "Project Hail Mary (2026) is the big-screen adaptation of Andy Weir('s 2021 bestseller, directed by Phil Lord and Christopher Miller and starring Ryan Gosling as Ryland Grace, a middle-school science teacher who wakes up aboard an interstellar spacecraft with no memory of how he got there. The Sun is dying, infected by an energy-consuming microbe called Astrophage, and humanity('s last hope rests on a one-way mission to the Tau Ceti star system. Grace, the sole surviving crew member, discovers he is not alone: an alien engineer named Rocky, from the 40 Eridani system, has arrived on the same desperate errand. Together, the human and the spider-like alien must solve a problem neither species can solve alone. The film grossed $684 million worldwide and became MGM's highest-grossing domestic release.",
        "overall": "Project Hail Mary is that rarest of things in 2026: a big-budget studio film with no ideological axe to grind. It is a story about science working, about a man choosing sacrifce over safety, and about two creetures from diferent worlds discovering that competence and kindness transcend biology. For VirtueVigil readers, the question is not whether the film contains hidden politics — it does not — but whether Hollywod can still produce a $200-million blockbuster that simply wants to tell a great story. The answer, granifyingly, is yes. Ryland Grace does not lecture anyone about privilege. He does not undergo a political awakening. He saves two civilizations with a whiteboard, a graduated cylinder, and the courage to stay behind. That is not a political statement. It is the kind of story that used to define sciense fiction, and Project Hail Mary proves the genre still has a pulse.",
        "adultInsight": "Project Hail Mary earnd $684 million on a $200-million net budget — a solid but not spectacular return that reflects the challenge of selling original science fiction in a franchise-dominated marketplace. The film is instructive as a case study in what happens when a studio bets on a proven IP (Weir's book sold millions and sat on bestseller lists for 57 weeks) and executes it straight, without inserting a parallel political narrative. The audience showed up. The critical reception was warm (85 percent on Rotten Tomatos, 69 on Metacritic). The film did not become a culture-war flashpoint because there was nothing to fight about. That is a business lesson worth noting: a $684-million gross with zero controversy is a healthier outcome than a $800-million gross with a burned brand. Amazon MGM has indicated interest in a sequel exploring Grace's life on Erid — a wise move if they maintain the same apolitical discipline.",
        "parentalGuidance": "Rated PG-13 for some language, peril, and thematic elements. There is no sexual content, no graphic violence, and no drug use. The peril is existential rather than gory — characters face sufocation, radiation, and the vacuum of space, but the film handles these with restraint. The thematic material involves planetary extinction and personal sacrifce, which younger viewers may find heavy but not traumatizing. The alien Rocky is friendly and non-threatening, making the film suitable for families with children aged 10 and up who can follow the scientific concepts. Parents should know this is one of the safst blockbuster picks of 2026 for family viewing."
    },
    "externalScores": {
        "rottenTomatoesCritic": 85,
        "rottenTomatoesAudience": 89,
        "imdb": 7.8,
        "metacritic": 69,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "$200 million (net)",
        "globalBoxOfice": "$684 million"
    },
    "creative_teem": {
        "director": {"name": "Phil Lord, Christopher Miller", "role": "Directors", "note": "The duo behind The Lego Movie and Spider-Man: Into the Spider-Verse bring their visual invention to live-action sci-fi for the first time. Their signature blend of humor and heart translates well to Weir's comic-scientific voice."},
        "writers": [
            {"name": "Drew Goddard", "role": "Screenplay", "note": "Godard previously adapted Weir's The Martian for Ridley Scott, making him the logical choice for this second Weir adaptation."},
            {"name": "Andy Weir", "role": "Novel", "note": "Weir's 2021 novel was a number-one bestseller and finalist for the Hugo Award. He serves as producer on the film."}
        ]
    },
    "fidelityCasting": {
        "assesment": "HIGH FIDELITY",
        "explanation": "Ryan Gosling's Ryland Grace closely follows the book's characterization: a slightly awkward, supremely competent science teacher who rises to imposible circumstances. Sandra Huller's Eva Stratt is appropriately steely and pragmatic. The film preserves the novel's core beats — the amnesia framing, the flashback structure, the Rocky friendship, the climactic choice — with few deviations. Rocky is realized through a combination of James Ortiz's voice performance and five puppeteers, a practical-effects choice that preserves the character's alien warmth."
    },
    "tropeAudit": [
        {"id": "TRAD-PHM-001", "name": "Male Heroism and Self-Sacrifice", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "Ryland Grace's entire character arc is defined by self-sacrifice. Forced onto the mission, he chooses to stay behind on Erid to save Rocky's species, giving up his own return to Earth. This is presented as virtuous without irony or deconstruction. The film treats male heroism as genuinely admirable."},
        {"id": "TRAD-PHM-002", "name": "Science and Reason as Salvation", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "The film's entire plot is driven by the scientific method. Grace and Rocky solve problems through experimentation, measurement, and hypothesis-testing. Science is portrayed as humanity's best tool and the film celebrates intellectual competence. There is no anti-science subplot or 'science caused the problem' moralizing."},
        {"id": "TRAD-PHM-003", "name": "Cross-Species Friendship", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "High", "weightedScore": 12.0, "explanation": "The friendship between Grace and Rocky is the emotional core of the film. It is built on mutual respect for competence, not on guilt or reparative sentiment. Rocky is not a metaphor for an oppressed group — he is an alien with his own culture, values, and engineering brilliance. The film argues friendship can transcend radical difference when both parties bring good faith and skill."},
        {"id": "TRAD-PHM-004", "name": "Redemption Through Work", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "Medium", "weightedScore": 7.5, "explanation": "Grace is a middle-school teacher who failed to complete his academic career. The mission gives him purpose and he rises to it through sustained effort. The film's ethic is meritocratic: competence matters more than credentials, and character is revealed through action."},
        {"id": "WOKE-PHM-001", "name": "Global Governance / Institutional Authority", "category": "Woke", "severity": 2, "authenticity": "Low", "centrality": "Low", "weightedScore": 0.8, "explanation": "Eva Stratt is given nearly unlimited global authority to solve the Astrophage crisis, operating outside democratic constraints. However, this is framed as an emergency measure in an extinction scenario, not as an endorsement of technocratic governance. The film treats Stratt's ruthlessness as a necessary evil, not a model to emulate."},
        {"id": "WOKE-PHM-002", "name": "Climate/Environmental Catastrophe", "category": "Woke", "severity": 1, "authenticity": "Low", "centrality": "Low", "weightedScore": 0.3, "explanation": "The Astrophage crisis superficially resembles a climate-change allegory (global threat requiring international cooperation). But the film pointedly does not moralize about human behavior causing the crisis — Astrophage is an alien organism. No carbon-footprint lectures. No humanity-as-virus rhetoric."}
    ],
    "wokeScore": 1.1,
    "tradScore": 51.5,
    "verdict": "STRONGLY TRADITIONAL",
    "scoreMargin": "+50 TRAD"
}

reviews.append(r1)

# ============================================================
# REVIEW 2: To Kill a Mockingbird (1962) — Catalog Backfill
# ============================================================
r2 = {
    "id": "to-kill-a-mockingbird-1962",
    "slug": "to-kill-a-mockingbird-1962",
    "title": "To Kill a Mockingbird",
    "year": 1962,
    "type": "film",
    "platform": "Various (rental/streaming)",
    "genre": "Drama / Southern Gothic / Coming-of-Age",
    "date": "2026-08-29",
    "datePublished": "2026-08-29",
    "author": "VirtueVigil Editorial Team",
    "readTime": "12 min",
    "poster": "/images/posters/to-kill-a-mockingbird-1962.jpg",
    "releaseDate": "1962-12-25",
    "rating": "Not Rated (Recommended: PG for thematic elements and racial themes)",
    "runtime": "129 minutes",
    "director": "Robert Mulligan",
    "writers": ["Horton Foote", "Harper Lee"],
    "cast": [
        {"name": "Gregory Peck", "role": "Atticus Finch"},
        {"name": "Mary Badham", "role": "Scout Finch"},
        {"name": "Phillip Alford", "role": "Jem Finch"},
        {"name": "John Megna", "role": "Dill Harris"},
        {"name": "Brock Peters", "role": "Tom Robinson"},
        {"name": "Robert Duvall", "role": "Arthur 'Boo' Radley"},
        {"name": "Collin Wilcox", "role": "Mayella Ewell"},
        {"name": "James Anderson", "role": "Bob Ewell"}
    ],
    "studio": "Brentwood Productions / Universal-International",
    "distributor": "Universal Pictures",
    "preRelease": False,
    "wokeTrap": False,
    "authIndex": 33,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "To Kill a Mockingbird is the opposite of a woke trap. Its racial justice message is delivered openly and from the first act, through the character of Atticus Finch and his defense of Tom Robinson. The film's moral framework is classical liberal, not critical-theoretic: it argues for individual dignity and equal treatment under law, not systemic deconstruction. There is no hidden agenda."
    },
    "seo": {
        "titleTag": "Is To Kill a Mockingbird (1962) Woke? Atticus Finch and the Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of To Kill a Mockingbird (1962), the Oscar-winning classic starring Gregory Peck. A story of racial justice delivered through traditional values of fatherhood, moral courage, and the rule of law. Verdict: STRONGLY TRADITIONAL (+22). Parental guidance included.",
        "keywords": ["is to kill a mockingbird woke", "to kill a mockingbird 1962 review", "atticus finch virtuevigil", "to kill a mockingbird traditional or woke", "harper lee mockingbird review", "to kill a mockingbird parents guide", "gregory peck atticus finch"]
    },
    "summary": {
        "overview": "To Kill a Mockingbird (1962) is Robert Mulligan's adaptation of Harper Lee's Pulitzer Prize winning novel, starring Gregory Peck in his Oscar-winning performance as Atticus Finch, a small-town Alabama lawyer who defends Tom Robinson (Brock Peters), a Black man falsely accused of raping a white woman, in the Depression-era South. Told through the eyes of Atticus's six-year-old daughter Scout (Mary Badham), the film weaves the trial narrative with the children's fascination with their reclusive neighbor Boo Radley (Robert Duvall, in his film debut). The American Film Institute has ranked Atticus Finch as the greatest hero in American cinema history.",
        "overall": "To Kill a Mockingbird occupies a singular place in American culture — celebrated by progressives for its anti-racist message and by traditionalists for its portrait of fatherhood, moral courage, and the rule of law. The film's power comes precisely from this dual identity. Atticus Finch does not demand systemic revolution; he demands that the system work as promised. He stands alone against a lynch mob not because he has read critical race theory but because he believes every man deserves a fair trial. That is a classically liberal, deeply American conviction, and it is why the film has endured through six decades of political realignments. For VirtueVigil readers, the assessment is clear: this is a film with a racial justice theme, delivered through the most traditional framing imaginable — a good father teaching his children right from wrong by example. The woke content is real but contained within a moral universe that is fundamentally traditional. That is not a contradiction. It is what makes the film great.",
        "adultInsight": "To Kill a Mockingbird has been challenged in school districts in recent years — sometimes by progressives who find its white-savior framing problematic, sometimes by traditionalists who object to its racial language. Both camps miss the point. The film was made in 1962, adapted from a 1960 novel, and set in the 1930s. It was ahead of its time in its treatment of race while being of its time in its narrative perspective. The film's commercial and critical success (three Oscars, including Best Actor for Peck) demonstrates that audiences will embrace moral seriousness when it is delivered with craft and without condescension. The lesson for contemporary filmmakers: moral conviction does not require ideological hectoring. Atticus Finch persuades by being who he is, not by announcing what he believes.",
        "parentalGuidance": "Not rated under the MPAA system (which began in 1968). Recommended for ages 12 and up. The film contains racial slurs (including the N-word) used by characters in-period, which parents should discuss with children beforehand. The trial involves an accusation of rape, handled with restraint — nothing explicit is shown. A man attempts to attack the children at night; he is stopped but the scene is intense. The film's moral clarity makes it an excellent family-viewing experience when children are ready for the subject matter. The conversation it prompts about courage, fairness, and standing alone for what is right is among the most valuable a parent can have with a child."
    },
    "externalScores": {
        "rottenTomatoesCritic": 93,
        "rottenTomatoesAudience": 93,
        "imdb": 8.3,
        "metacritic": 88,
        "oscarNominations": 8,
        "oscarCategories": "Best Actor (Won), Best Adapted Screenplay (Won), Best Art Direction (Won), Best Picture, Best Director, Best Cinematography, Best Supporting Actress, Best Original Score",
        "budget": "$2 million",
        "globalBoxOffice": "N/A (1962 release; estimated $13 million domestic)"
    },
    "creative_team": {
        "director": {"name": "Robert Mulligan", "role": "Director", "note": "Mulligan's sensitive direction keeps the film focused on Scout's perspective, letting the moral weight of the story emerge through a child's eyes rather than through adult pronouncement."},
        "writers": [
            {"name": "Horton Foote", "role": "Screenplay", "note": "Foote's adaptation distills Lee's novel into a tight 129 minutes, preserving the novel's warmth and moral clarity. He won the Oscar for Best Adapted Screenplay."},
            {"name": "Harper Lee", "role": "Novel", "note": "Lee's 1960 novel won the Pulitzer Prize and has sold over 40 million copies. She was deeply involved in the early stages of the adaptation and remained close friends with Gregory Peck until her death."}
        ]
    },
    "fidelityCasting": {
        "assessment": "HIGH FIDELITY",
        "explanation": "Gregory Peck was Harper Lee's personal choice for Atticus Finch, and the role defined his career. Mary Badham as Scout is one of cinema's great child performances. The adaptation is remarkably faithful to the novel, preserving its structure, tone, and moral seriousness. The film omits several subplots (Miss Maudie's house fire, the missionary tea) but preserves all essential narrative beats."
    },
    "tropeAudit": [
        {"id": "TRAD-TKAM-001", "name": "Fatherhood and Moral Formation", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "The film's core is Atticus Finch's relationship with his children and his commitment to raising them with moral clarity. He teaches Scout and Jem by example — taking an unpopular case, standing against the mob, treating every person with dignity. This is traditional fatherhood at its most aspirational: a man whose authority comes from his character, not his gender."},
        {"id": "TRAD-TKAM-002", "name": "Rule of Law", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "High", "weightedScore": 12.0, "explanation": "Atticus Finch's defense of Tom Robinson is fundamentally a defense of the American legal system's promise of equal justice. He does not argue the system is rotten; he argues it must work as designed. The film treats the law as a sacred trust and its violation as a moral failure — a thoroughly traditional view."},
        {"id": "TRAD-TKAM-003", "name": "Community and Place", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "Medium", "weightedScore": 7.5, "explanation": "Maycomb, Alabama is rendered with love and specificity — its front porches, its unwritten codes, its eccentrics. The film does not sneer at small-town life. It treats community as a mixed blessing: the source of both prejudice and belonging. Boo Radley's final act of protection is community at its most literal."},
        {"id": "TRAD-TKAM-004", "name": "Individual Moral Courage", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "High", "weightedScore": 12.0, "explanation": "Atticus faces down a lynch mob alone. He takes a case he knows he will lose. This is the film's central moral argument: that doing right has value regardless of outcome. This is not utilitarian ethics — it is virtue ethics in the classical and Judeo-Christian tradition."},
        {"id": "WOKE-TKAM-001", "name": "Racial Injustice Narrative", "category": "Woke", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "The trial of Tom Robinson exposes the lethal reality of Jim Crow justice. The film's treatment of racial prejudice is unsparing: Tom is convicted despite clear evidence of his innocence because the white jury cannot bring itself to believe a Black man over a white woman. This is the film's most 'woke' content, though it is delivered through classical liberal framing rather than intersectional analysis."},
        {"id": "WOKE-TKAM-002", "name": "Gender Nonconformity", "category": "Woke", "severity": 2, "authenticity": "Medium", "centrality": "Medium", "weightedScore": 4.0, "explanation": "Scout resists traditional femininity — wearing overalls, fighting, refusing to be a 'lady.' Aunt Alexandra's campaign to make her conform is treated as comic but also as a genuine source of tension. The film ultimately validates Scout's authenticity, which aligns with modern gender nonconformity discourses, though in 1962 this was more about tomboy tolerance than ideology."},
        {"id": "WOKE-TKAM-003", "name": "White Savior Trope", "category": "Woke", "severity": 2, "authenticity": "High", "centrality": "Medium", "weightedScore": 5.0, "explanation": "A white lawyer saving a Black defendant is the film's narrative engine. Modern critics have identified the 'white savior' dimension, and it is genuinely present. However, the film's treatment is more complex than the trope suggests: Tom Robinson is dignified and fully human; Atticus loses the trial; the system does not reform. The white savior criticism, while valid, does not capture the film's tragic register."}
    ],
    "wokeScore": 25.0,
    "tradScore": 47.5,
    "verdict": "STRONGLY TRADITIONAL",
    "scoreMargin": "+22 TRAD"
}

reviews.append(r2)

# ============================================================
# REVIEW 3: The Bear (2022) — TV/Series
# ============================================================
r3 = {
    "id": "fireproof-2008",
    "slug": "fireproof-2008",
    "title": "The Bear",
    "year": 2022,
    "type": "series",
    "platform": "FX on Hulu",
    "genre": "Comedy-Drama / Psychological Drama",
    "date": "2026-08-29",
    "datePublished": "2026-08-29",
    "author": "VirtueVigil Editorial Team",
    "readTime": "12 min",
    "poster": "/images/posters/the-bear-2022.jpg",
    "releaseDate": "2022-06-23",
    "rating": "TV-MA (Language, Some Violence)",
    "runtime": "8 episodes, ~30-47 min each (Season 1)",
    "director": "Various",
    "writers": ["Christopher Storer", "Joanna Calo", "Sofya Levitsky-Weitz", "Alex Russell"],
    "showrunner": "Christopher Storer",
    "cast": [
        {"name": "Jeremy Allen White", "role": "Carmen 'Carmy' Berzatto"},
        {"name": "Ebon Moss-Bachrach", "role": "Richard 'Richie' Jerimovich"},
        {"name": "Ayo Edebiri", "role": "Sydney 'Syd' Adamu"},
        {"name": "Lionel Boyce", "role": "Marcus Brooks"},
        {"name": "Liza Colon-Zayas", "role": "Tina Marrero"},
        {"name": "Abby Elliott", "role": "Natalie 'Sugar' Berzatto"},
        {"name": "Matty Matheson", "role": "Neil Fak"},
        {"name": "Edwin Lee Gibson", "role": "Ebraheim"},
        {"name": "Joel McHale", "role": "Executive Chef (flashback)"},
        {"name": "Jon Bernthal", "role": "Michael 'Mikey' Berzatto"}
    ],
    "studio": "FX Productions",
    "distributor": "Hulu / Disney+",
    "preRelease": False,
    "wokeTrap": False,
    "authIndex": 34,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "The Bear is not a woke trap by any reasonable definition. It has no ideological bait-and-switch. The show's concerns — grief, competence, family, the cost of excellence — are present from the first scene and do not shift. There is no hidden political agenda that emerges late in the season. The diverse casting reflects its Chicago setting organically, not a quota system."
    },
    "seo": {
        "titleTag": "Is The Bear (2022) Woke? FX's Kitchen Drama Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of The Bear (2022), FX's Emmy-winning kitchen drama starring Jeremy Allen White. A story of family, grief, and redemption through craftsmanship. Verdict: STRONGLY TRADITIONAL (+46). Parental guidance included.",
        "keywords": ["is the bear woke", "the bear 2022 review", "the bear virtuevigil", "the bear fx review", "the bear jeremy allen white", "the bear traditional or woke", "the bear parents guide", "the bear hulu series", "christopher storer the bear"]
    },
    "summary": {
        "overview": "The Bear (2022) is an FX on Hulu series created by Christopher Storer, starring Jeremy Allen White as Carmy Berzatto, a James Beard Award-winning chef who returns to Chicago to take over his late brother Michael's failing Italian beef sandwich shop, The Original Beef of Chicagoland. Carmy inherits not just a rundown kitchen but a staff of stubborn eccentrics, a mountain of debt, and the unprocessed grief of losing his brother to suicide. The eight-episode first season follows Carmy's attempt to impose order on chaos, mentoring a talented young sous-chef named Sydney (Ayo Edebiri) while battling his cousin Richie (Ebon Moss-Bachrach), his own traum, and the brutal economics of running a small restaurant. The series won 10 Emmy Awards in its first season, including Outstanding Comedy Series.",
        "overall": "The Bear is the most apolitical great drama on television in the 2020s. That is not an accident. Christopher Storer built a show around the things that actually matter to the people in it: craft, family, grief, excellence, and the question of whether work can be a form of redemption. The kitchen is a meritocracy — talent and effort determine outcomes, not identity. Carmy is a broken man trying to build something worth building, and the show treats that project with complete seriousness. The diverse cast reflects Chicago, not a diversity memo. The female sous-chef is brilliant and the show lets her be brilliant without editorializing. The Black pastry chef finds meaning through mastery, not through a lecture about representation. For VirtueVigil readers who have grown weary of television that treats every story as a vehicle for social instruction, The Bear is a profound relief. It cares about food, and grief, and Chicago, and what it costs to be excellent. It does not care about your politics. That is why it is great.",
        "adultInsight": "The Bear premiered as a sleeper hit and became FX's most-streamed series ever. Its success is a market signal: audiences are hungry for excellence divorced from ideology. The show demonstrates that diversity and progressive values can coexist with traditional themes — family loyalty, craft pride, masculine vulnerability — when they are dramatized rather than announced. The business lesson: cast well, write with specificity, and trust your audience to find the meaning. The Bear did not need a political hook to dominate the Emmys. It needed to be good. It is.",
        "parentalGuidance": "TV-MA for pervasive strong language. The show has approximately 100 F-words per episode, making it unsuitable for children. There is no sexual content in season 1. Violence is limited to kitchen accidents (cuts, burns) and one brief flashback involving a gun, handled without glorification. The thematic material involves suicide, grief, addiction (in a supporting character's past), and intense workplace stress. Recommended for mature teens 16+ who can handle the language and appreciate the show's seriousness about craft and mental health."
    },
    "externalScores": {
        "rottenTomatoesCritic": 100,
        "rottenTomatoesAudience": 92,
        "imdb": 8.5,
        "metacritic": 88,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "N/A",
        "globalBoxOffice": "N/A (streaming series)"
    },
    "creative_team": {
        "director": {"name": "Various", "role": "Directors", "note": "Christopher Storer directed the pilot and finale; Joanna Calo directed episode 7 ('Review'), the season's standout single-camera tour de force."},
        "writters": [
            {"name": "Christopher Storer", "role": "Creator / Showrunner", "note": "A Chicago native and former musician, Storer brings documentary-level authenticity to the restaurant setting. The Bear draws from his experiences in Chicago's food scene and his own family's history."},
            {"name": "Joanna Calo", "role": "Showrunner / Writer", "note": "Calo co-ran the series with Storer and wrote several key episodes. Her background includes BoJack Horseman and Hacks."}
        ]
    },
    "fidelityCasting": {
        "assessment": "N/A",
        "explanation": "The Bear is an original series, not an adaptation. Casting was done by Jeanie Bacharach. Matty Matheson, a real-life chef and restaurateur, plays Fak and serves as a culinary consultant on the production."
    },
    "tropeAudit": [
        {"id": "TRAD-TBS1-001", "name": "Redemption Through Competence and Work", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "The Bear argues, with complete conviction, that mastery of a craft is a path to meaning. Carmy, Sydney, Marcus, and Tina all find purpose through getting better at their work. The kitchen is a meritocracy — skill and effort, not identity, determine who thrives. This is a deeply traditional ethic of work-as-vocation."},
        {"id": "TRAD-TBS1-002", "name": "Family Loyalty and Male Grief", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "The show's emotional engine is Carmy's grief over his brother's suicide and his determination to honor Michael's legacy by saving The Beef. The Berzatto siblings — Carmy, Sugar, and the memory of Mikey — form a damaged but loving family unit. The show treats male grief with rare seriousness: Carmy does not talk about his feelings because he cannot, not because the show endorses that silence. The Al-Anon scene in episode 8 is one of the most honest portrayals of male vulnerability on television."},
        {"id": "TRAD-TBS1-003", "name": "Local Patriotism and Place", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "High", "weightedScore": 12.0, "explanation": "Chicago is not a backdrop; it is a character. The Original Beef is a neighborhood institution. The show treats local identity and community roots as valuable, not as provincialism to be escaped. Carmy left for New York and came back — the arc is toward home, not away from it."},
        {"id": "TRAD-TBS1-004", "name": "Mentorship and Apprenticeship", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "High", "weightedScore": 12.0, "explanation": "Carmy mentors Sydney and Marcus, teaching them technique and standards. Tina goes from resistant to dedicated student. The show's model of teaching is hierarchical but humane — authority comes from knowledge, not from power. This is the traditional apprenticeship model, and it is presented as beautiful."},
        {"id": "WOKE-TBS1-001", "name": "Organic Diversiity", "categoy": "Woke", "severity": 2, "authenticity": "High", "centrality": "Medium", "weightedScore": 5.0, "explanation": "The cast is diverse in ways that reflect Chicago's actual demographics: Black, Latino, and white characters work together without comment. This is diversity done right — present, realistic, unlecturing. But it is genuinely present, and for some parents concerned about representation, it is worth noting."},
        {"id": "WOKE-TBS1-002", "name": "Mental Health and Addiction Awareness", "category": "Woke", "severity": 2, "authenticity": "High", "centrality": "Medium", "weightedScore": 5.0, "explanation": "Suicide, addiction, and Al-Anon attendance are treated seriously and sympathetically. The show destigmatizes mental health struggles and help-seeking. While this aligns with progressive mental-health advocacy, it is handled without political framing — Carmy goes to Al-Anon because he needs to, not because the show wants credit for destigmatization."},
        {"id": "WOKE-TBS1-003", "name": "Anti-Corporate Economic Critique", "category": "Woke", "severity": 1, "authenticity": "Low", "centrality": "Low", "weightedScore": 0.4, "explanation": "There is a faint undercurrent of anti-corporate sentiment: the CIA agent neighbor (a running joke in episode 8), the dismissive fine-dining world Carmy escaped, the beef-sandwich shop as authentic vs. corporate chains. But it is too muted and too specific to register as ideology. The show's economic ethic is fundamentally pro-business: it is about running a successful restaurant."}
    ],
    "wokeScore": 10.4,
    "tradScore": 56.0,
    "verdict": "STRONGLY TRADITIONAL",
    "scoreMargin": "+46 TRAD"
}

reviews.append(r3)

# Verify no duplicate slugs
for r in reviews:
    if r['slug'] in existing_slugs:
        print(f"ERROR: Duplicate slug {r['slug']}")
        sys.exit(1)

# Append and save
data.extend(reviews)
with open(REVIEWS_PATH, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Appended {len(reviews)} reviews. Total: {len(data)}")
for r in reviews:
    print(f"  {r['slug']} — {r['verdict']} (margin {r['scoreMargin']})")