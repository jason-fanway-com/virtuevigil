#!/usr/bin/env python3
"""Generate 3 review JSONs for 2026-10-09 and append to reviews.json."""

import json, sys, os
from datetime import datetime, timezone

REVIEWS_PATH = "src/data/reviews.json"

# Load existing
with open(REVIEWS_PATH) as f:
    reviews = json.load(f)

existing_slugs = {r['slug'] for r in reviews}
print(f"Current count: {len(reviews)}")

# ──────────────────────────────────────────────────
# REVIEW 1: X-Men (2000)
# ──────────────────────────────────────────────────
xmen = {
    "id": f"x-men-2000",
    "slug": "x-men-2000",
    "title": "X-Men",
    "year": 2000,
    "type": "movie",
    "runtime": 104,
    "genre": "Action, Adventure, Sci-Fi, Superhero",
    "director": "Bryan Singer",
    "cast": [
        "Patrick Stewart",
        "Hugh Jackman",
        "Ian McKellen",
        "Halle Berry",
        "Famke Janssen",
        "James Marsden",
        "Anna Paquin",
        "Bruce Davison",
        "Rebecca Romijn",
        "Ray Park"
    ],
    "rating": "PG-13",
    "imdbRating": 7.4,
    "metacriticRating": 64,
    "date": "2026-10-09",
    "datePublished": "2026-10-09",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/x-men-2000.jpg",
    "releaseDate": "2000-07-14",
    "tropeAudit": [
        {
            "id": "XMEN-TRAD-001",
            "name": "Heroic Self-Sacrifice",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Wolverine transfers his healing power to Rogue at the climax, knowing it could kill him. This is the classic heroic sacrifice: one life given to save an innocent. The film treats this moment without irony, letting it land as genuine nobility rather than deconstructing it. Wolverine does not give a speech about privilege first; he just acts."
        },
        {
            "id": "XMEN-TRAD-002",
            "name": "Good vs. Evil Framework",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The X-Men and the Brotherhood are not morally equivalent. Xavier's team wants peaceful coexistence; Magneto's wants mutant supremacy enforced by violence. The film allows viewers to understand Magneto's pain without endorsing his methods. This is moral clarity, not moral relativism -- a traditional storytelling value that was still the default in 2000."
        },
        {
            "id": "XMEN-TRAD-003",
            "name": "Mentor and Found Family",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Charles Xavier runs a school where lost young mutants find structure, purpose, and belonging. The X-Mansion functions as a surrogate family for kids rejected by the world. Xavier is the wise father-figure who teaches discipline and moral responsibility. The found-family structure is one of the most durable traditional storytelling frameworks and is central to the film's emotional architecture."
        },
        {
            "id": "XMEN-TRAD-004",
            "name": "Protecting the Innocent",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "The X-Men's mission is defensive: protect a world that fears and hates them. They could easily justify retaliation against humans, but Xavier's ethic is protection, not revenge. When Magneto targets world leaders at Ellis Island, the X-Men risk everything to stop him, even though those same leaders support the Mutant Registration Act. This is moral maturity, not grievance politics."
        },
        {
            "id": "XMEN-WOKE-001",
            "name": "Discrimination-as-Oppression Allegory",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 2.7,
            "explanation": "The X-Men metaphor has always been a civil rights allegory: mutants as the feared and hated minority. The Mutant Registration Act directly evokes segregationist legislation, and Senator Kelly's rhetoric ('Do you want your children to go to school with mutants?') mirrors real-world bigotry. In the film's 2000 context, this allegory was handled with more philosophical balance than it would be today -- the audience is allowed to feel the fear of 'normal' people without being called bigots for it. But judged by VVWS standards, the framework is inherently progressive in its structure."
        },
        {
            "id": "XMEN-WOKE-002",
            "name": "Identity-as-Destiny Narrative",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.5,
            "explanation": "The film's 'mutant and proud' ethos and the coming-out narrative for young mutants (Rogue hiding her nature, Bobby 'not telling' his parents) maps directly onto LGBTQ identity frameworks. Magneto's speech about not having to hide 'what we are' functions as a pride declaration. The film frames mutant identity not as a condition to manage but as an essence to celebrate -- a progressive framework that would become the dominant mode in later decades."
        },
        {
            "id": "XMEN-WOKE-003",
            "name": "Diversity-by-Design Casting",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.6,
            "explanation": "Storm is a black woman leading the team; the international lineup includes characters from Africa, Germany, Russia, and Canada. The 2000 film was ahead of its time on representation, but in its era this felt less like quota-checking and more like the natural result of adapting a team that had always been diverse in the comics. Still, the casting choices were not accidental -- Singer's X-Men consciously presented diversity as a strength."
        },
        {
            "id": "XMEN-WOKE-004",
            "name": "Conservative-as-Villain Coding",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.6,
            "explanation": "Senator Kelly is coded as a conservative politician whose anti-mutant bigotry drives the legislation that threatens mutant-kind. He is not portrayed as having legitimate safety concerns; he is a straw-man bigot who gets a redemption arc only after being forcibly mutated himself. The 'conservative politician as villain' is a durable Hollywood trope that was already established by 2000."
        },
        {
            "id": "XMEN-WOKE-005",
            "name": "Female Empowerment Lite",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.3,
            "explanation": "Storm and Jean Grey are powerful, competent, and never damsels. Jean Grey is the team medic and telepath who ultimately saves the day by using Cerebro after Xavier is incapacitated. Storm has several command moments. In 2000 this was refreshing rather than ideological -- the characters are people first, women second -- but the pattern is still present."
        }
    ],
    "wokeScore": 5.7,
    "tradScore": 14.28,
    "scoreMargin": "+8.58",
    "authIndex": 72,
    "verdict": "BALANCED TRADITIONAL",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "X-Men (2000) does not employ a woke trap. The discrimination allegory is visible from the opening scene in 1944 Poland and the Senate hearing that follows minutes later. The film's thematic framework is announced up front and remains consistent throughout. There is no hidden ideological payload that subverts the first half; what you see in the first act is what you get for the whole film. The movie is transparent about being a civil rights metaphor wrapped in a superhero action film, and that transparency is itself a mark of its pre-woke-era production: it does not feel the need to disguise its message because the message was not yet weaponized.",
    "seo": {
        "titleTag": "Is X-Men (2000) Woke? Bryan Singer's Superhero Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of X-Men (2000), the Bryan Singer superhero film that launched a franchise. Wolverine, Xavier, and Magneto square off. Trope scores, verdict: BALANCED TRADITIONAL (+8.58). Parental guidance included.",
        "keywords": "is x-men woke, x-men 2000 review, x-men virtuevigil, x-men traditional or woke, bryan singer x-men, x-men parents guide, hugh jackman wolverine review, marvel movies woke content"
    },
    "summary": {
        "overall": "X-Men (2000) is the superhero movie that proved comic-book films could be taken seriously, and more than two decades later, it holds up as one of the more philosophically balanced entries in the genre. Bryan Singer's film takes the X-Men's civil-rights metaphor -- a team of genetic mutants feared and hated by the humans they protect -- and plays it as a genuine moral drama rather than a lecture. The result is a film that has progressive DNA but a traditional heart: it believes in self-sacrifice, found family, and the obligation of the strong to protect the weak. The discrimination allegory is baked in and impossible to ignore, but the 2000 vintage means it is delivered with more restraint than a modern Disney+ series would attempt. This is the X-Men before the franchise became a delivery vehicle for identity politics -- still the best balance the series ever struck.",
        "whatWeLove": "The film's moral architecture is more traditional than its reputation suggests. Xavier's philosophy is one of restraint and service: protect a world that fears you, not because it deserves protection, but because that is what good people do. Wolverine's character arc -- from amnesiac loner to someone willing to die for a teenage girl he barely knows -- is a pure heroic redemption story. The X-Mansion functions as a school, not an activist headquarters. The climax at the Statue of Liberty is honest-to-goodness heroism: climbing a national monument to stop a terrorist from mutating world leaders. Hugh Jackman's Wolverine, in his debut, brings a raw physicality that grounds the film in something human and unpolished. Patrick Stewart and Ian McKellen give the ideological conflict between Xavier and Magneto the weight of a Shakespearean drama. The film trusts its audience to grasp nuance: Magneto is wrong, but you understand why he became what he became -- and the film never asks you to agree with him.",
        "whatToWatchFor": "The discrimination allegory is the film's central operating system, and viewers sensitive to identity-politics messaging should know what they are signing up for. The Mutant Registration Act hearings, Senator Kelly's fear-mongering rhetoric, and the 'coming out' dynamics for young mutants like Rogue and Bobby Drake map directly onto contemporary progressive frameworks. 'Mutant and proud' is the film's emotional rallying cry, and while it lands as universal in 2000, the same language serves very different ideological purposes in 2026. Magneto's backstory -- a Holocaust survivor who sees history repeating -- is powerful and genuinely earned, but it also means the villain is coded with a moral legitimacy that complicates the good-vs-evil framework. The subplot about Mystique infiltrating the school disguised as Bobby Drake to manipulate Rogue into leaving reads differently in the post-grooming-panic era than it did in 2000. One caution for parents: there is a brief but intense scene of Rogue absorbing her boyfriend's life force through a kiss that puts him in a coma, which may be frightening for younger viewers."
    }
}

# ──────────────────────────────────────────────────
# REVIEW 2: Loki (2021)
# ──────────────────────────────────────────────────
loki = {
    "id": "loki-2021",
    "slug": "loki-2021",
    "title": "Loki",
    "year": 2021,
    "type": "series",
    "platform": "Disney+",
    "genre": "Action-Adventure, Crime Thriller, Fantasy, Sci-Fi, Superhero",
    "date": "2026-10-09",
    "datePublished": "2026-10-09",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/loki-2021.jpg",
    "releaseDate": "2021-06-09",
    "rating": "TV-14",
    "runtime": "2 seasons, 12 episodes, ~41-56 min each",
    "director": None,
    "writers": None,
    "showrunner": "Michael Waldron",
    "cast": [
        "Tom Hiddleston",
        "Owen Wilson",
        "Gugu Mbatha-Raw",
        "Sophia Di Martino",
        "Wunmi Mosaku",
        "Eugene Cordero",
        "Tara Strong",
        "Jonathan Majors",
        "Richard E. Grant"
    ],
    "studio": "Marvel Studios",
    "distributor": "Disney+",
    "tropeAudit": [
        {
            "id": "LOKI-TRAD-001",
            "name": "Redemption Arc",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Loki's transformation from narcissistic trickster to self-sacrificing hero is the spine of the entire series. The character who once tried to conquer Earth ends the series by choosing to spend eternity alone, holding the multiverse's timelines together so everyone else can live free. This is not a redemption by lecture or therapy; it is earned through suffering, friendship, and genuine moral growth. The finale makes explicit that Loki's final act is the opposite of his defining trait -- he was always the god of chaos who hated being alone, and he chooses isolation as an act of love. This is one of the most traditionally structured redemption arcs in the modern MCU."
        },
        {
            "id": "LOKI-TRAD-002",
            "name": "Male Friendship",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "The relationship between Loki and Mobius is the emotional center of the series. It is a non-romantic, non-sexualized male friendship built on mutual challenge, trust, and genuine affection. Mobius sees through Loki's defenses and chooses to believe in him anyway. In an era where male friendships in media are often pathologized, deconstructed, or sexualized, this is a quietly traditional portrait of two men making each other better."
        },
        {
            "id": "LOKI-TRAD-003",
            "name": "Order vs. Chaos / Cosmic Purpose",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.5,
            "explanation": "The Sacred Timeline represents cosmic order against the chaos of the multiverse. The TVA, for all its bureaucratic flaws, is preserving a single coherent reality against fragmentation. Season 2's conclusion -- Loki choosing to become the living loom that holds time together -- is fundamentally about sacrificing individual freedom for the preservation of order and existence itself. This is a traditional philosophical framework: order is hard, chaos is easy, and the hero chooses the hard thing."
        },
        {
            "id": "LOKI-TRAD-004",
            "name": "Love as Redemption, Not Desire",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.84,
            "explanation": "Loki's feelings for Sylvie are the catalyst for his transformation, but the series handles this with unusual restraint. It is not a romance plot; it is a self-confrontation. Loving Sylvie -- a variant of himself -- forces Loki to see himself clearly for the first time. The love story is chaste, psychological, and ultimately tragic. When Sylvie kills He Who Remains, Loki does not condemn her; he keeps trying to save her anyway. This is love as moral commitment, not as desire or identity performance."
        },
        {
            "id": "LOKI-WOKE-001",
            "name": "Gender-Swapped Superior Variant",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 2.7,
            "explanation": "Sylvie is a female Loki variant who is, in many respects, more competent than the male Loki. She evaded the TVA for years as a child, taught herself enchantment magic, and came closer to destroying the TVA than Loki ever did. She is more decisive, less vain, and clearer about her goals. The series does not present her as 'better because she is a woman,' but the structural message is unambiguous: the female version of this character is the more effective one. Sylvie gets the moral clarity that Loki has to earn, and the series never interrogates her choices with the same rigor it applies to him."
        },
        {
            "id": "LOKI-WOKE-002",
            "name": "Dismantle-the-System Narrative",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.5,
            "explanation": "The TVA begins as an authoritarian bureaucracy enforcing a single 'sacred' timeline -- a system that must be exposed as fraudulent and dismantled. The Time-Keepers are revealed as puppets. The entire premise is that centralized order is a lie imposed by a hidden power. This is the 'dismantle oppressive systems' framework that is fundamental to progressive storytelling. Season 2 complicates this by showing that destroying the system without a replacement risks annihilation, but the thrust of the narrative is still anti-institutional."
        },
        {
            "id": "LOKI-WOKE-003",
            "name": "Gender Fluidity Signaling",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.84,
            "explanation": "A blink-and-you-miss-it shot of Loki's TVA file shows his sex listed as 'Fluid.' This is a direct nod to comic-book Loki's gender fluidity and to contemporary identity politics. It serves no narrative purpose and is never explored; it exists purely as signaling. Whether you find this harmless Easter egg or ideological product placement depends on your priors, but it is undeniably a woke marker inserted into a Disney+ property."
        },
        {
            "id": "LOKI-WOKE-004",
            "name": "Institutional Authority Transfer",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.36,
            "explanation": "By the end of Season 2, Hunter B-15 -- a black woman who began as a loyal TVA enforcer -- has become the moral leader of the reformed organization. The original patriarchal structure (the male-presenting Time-Keepers, the male He Who Remains) is replaced by leadership that is notably diverse. The series does not make a speech about this; it simply does it. For some viewers this will read as natural character development; for others, as the now-standard Disney pattern of transferring institutional authority to non-white, non-male characters as the resolution."
        },
        {
            "id": "LOKI-WOKE-005",
            "name": "Multiverse as Deconstruction",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.36,
            "explanation": "The multiverse framework, as deployed in Phase 4-5 Marvel, functions as a deconstructive engine: every established hero can now have infinite variants, undermining the idea of coherent identity, singular heroism, or fixed moral meaning. Loki participates in this by making its protagonist one variant among many and ending with the multiverse fully unleashed. The long-term effect is to replace concrete stakes ('this hero matters') with infinite optionality ('every version matters, therefore none does')."
        }
    ],
    "wokeScore": 5.76,
    "tradScore": 9.48,
    "scoreMargin": "+3.72",
    "authIndex": 62,
    "verdict": "BALANCED TRADITIONAL",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "Loki does not employ a woke trap. The series announces its thematic concerns in the first episode: this is a story about identity, free will, and whether a villain can become something more. The gender-fluid file reveal and Sylvie's introduction as a female Loki variant both happen early (episodes 1-2), and the anti-bureaucratic framework is visible from the moment Loki arrives at the TVA. The series is structurally transparent. If anything, the woke elements become less dominant as the series progresses: Season 2 is more focused on Loki's redemption and cosmic responsibility than on progressive messaging, which is one reason the finale landed as strongly as it did.",
    "seo": {
        "titleTag": "Is Loki (2021) Woke? Disney+'s Tom Hiddleston Marvel Series Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Loki (2021-2023), the Disney+ Marvel series starring Tom Hiddleston and Owen Wilson. Time-traveling trickster faces a female variant of himself. Trope scores, verdict: BALANCED TRADITIONAL (+3.72). Parental guidance included.",
        "keywords": "is loki woke, loki 2021 review, loki disney plus, loki virtuevigil, tom hiddleston loki series, loki traditional or woke, loki parents guide, loki gender fluid"
    },
    "summary": {
        "overall": "Loki is the best thing Marvel Studios has produced for Disney+, and it succeeds in large part because it cares more about its protagonist's moral transformation than about the ideological messaging that drags down so many of its contemporaries. Tom Hiddleston's Loki -- the 2012 variant who grabbed the Tesseract and escaped in Endgame -- is forced through a redemption machine disguised as a time-travel crime thriller, and the result is genuinely moving. The series has progressive elements baked into its DNA: a female Loki variant who outclasses the original, a gender-fluid file reveal, and a 'dismantle the oppressive system' framework. But these are not the point. The point is a narcissist learning to care about someone other than himself, and the series earns that arc rather than declaring it. The two-season structure lets the redemption breathe, and the finale -- Loki choosing eternal solitude to hold the timelines together -- is one of the most emotionally satisfying moments in the entire MCU. Parents should know this is darker and more philosophical than most Marvel fare, with existential stakes, some violence, and a villain who is erased from existence on screen.",
        "whatWeLove": "Tom Hiddleston's performance is career-best work. He plays Loki's journey from arrogant trickster to self-sacrificing hero with such precision that you can track the change frame by frame. Owen Wilson's Mobius is the perfect foil: a weary bureaucrat who has seen every variant of every being in the universe and still chooses to believe in this one. The production design of the TVA -- midcentury bureaucratic nightmare meets cosmic horror -- is genuinely creative and unlike anything else in the MCU. Natalie Holt's score is outstanding. The series has the courage to be strange: an entire episode set in a dying moon at the end of time, a climax that is two people talking in a citadel, a finale in which the hero does not punch his way to victory but makes a choice that costs him everything. For parents who want to talk to their kids about redemption, Loki is a richer text than most Sunday school curricula.",
        "whatToWatchFor": "Sylvie's introduction as the female Loki who is more competent, more decisive, and morally clearer than the male original is the series' most overt progressive structural choice. It is handled with more art than the typical Disney+ 'girlboss' insertion, but the underlying message is familiar. The gender-fluid file reveal in Episode 1 is a pure signaling moment that adds nothing to the story. The series' anti-institutional framework -- the TVA as a fascist bureaucracy whose founding mythology is a lie -- will land differently depending on whether you think centralized control over reality is inherently evil or sometimes necessary. The Jonathan Majors situation adds an uncomfortable layer: He Who Remains/Kang is played by an actor later convicted of domestic assault, and the character's role as the hidden puppet master of all reality now carries an unintended resonance that the series did not anticipate. One sequence may disturb younger viewers: a TVA agent is 'pruned' -- erased from existence -- and we see him dissolve into nothing while conscious of what is happening. The series has no sexual content beyond a single kiss. Violence is Marvel-standard: punching, stabbing, energy blasts, no gore."
    }
}

# ──────────────────────────────────────────────────
# REVIEW 3: Blood Sacrifice (2026)
# ──────────────────────────────────────────────────
blood_sacrifice = {
    "id": "blood-sacrifice-2026",
    "slug": "blood-sacrifice-2026",
    "title": "Blood Sacrifice",
    "year": 2026,
    "type": "series",
    "platform": "Netflix",
    "genre": "Crime, Thriller, Drama",
    "date": "2026-10-09",
    "datePublished": "2026-10-09",
    "author": "VirtueVigil Editorial Team",
    "readTime": "6 min read",
    "poster": "/images/posters/blood-sacrifice-2026.jpg",
    "releaseDate": "2026-10-03",
    "rating": "TV-MA",
    "runtime": "Limited series, ~6 episodes",
    "director": None,
    "writers": None,
    "showrunner": "George Kay",
    "cast": ["TBD"],
    "studio": "Netflix Sweden / B-Reel Films",
    "distributor": "Netflix",
    "tropeAudit": [
        {
            "id": "BLS-TRAD-001",
            "name": "Father-Son Reconciliation",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The core premise pairs a semi-estranged father and son as detective partners forced back together by a murder investigation. This is one of the most durable narrative engines in storytelling: fractured family repaired through shared mission. The father-son dynamic is inherently traditional -- it is about lineage, obligation, forgiveness, and the transmission of values across generations. Whether the series handles this with honesty or uses it as a vehicle for a toxic-masculinity lecture will determine the final score, but the premise itself scores traditional."
        },
        {
            "id": "BLS-TRAD-002",
            "name": "Justice and Law Enforcement",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "This is a crime thriller about catching a killer. The framework assumes that murder is wrong, justice is worth pursuing, and law enforcement -- however flawed -- is the mechanism for achieving it. Traditional stories treat the detective as a force for order against chaos; the genre itself makes traditional philosophical commitments. Whether the series subverts this by making the cops the real villains (a now-common progressive move in crime dramas) is the risk, but the premise does not announce that intention."
        },
        {
            "id": "BLS-TRAD-003",
            "name": "Male Professional Competence",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.5,
            "explanation": "The two leads are male detectives defined by their professional skill. The crime genre has historically been a space where male competence, intuition, and physical courage are celebrated without apology. A father-son detective team doubling as a family drama gives the series two traditional tracks to run on simultaneously."
        },
        {
            "id": "BLS-WOKE-001",
            "name": "Swedish/Netflix Progressive Default",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": 0.6,
            "explanation": "Swedish crime dramas (Wallander, The Bridge, The Girl with the Dragon Tattoo) have a long tradition of embedding progressive social commentary about immigration, gender, and class into their detective frameworks. Netflix Originals amplify this tendency. George Kay's previous work (Lupin, Hijack, Criminal) defaults to diverse casts and progressive undertones without being explicitly ideological. The risk here is that the Stockholm setting becomes a delivery mechanism for Nordic social-democratic messaging about multiculturalism or gender politics. This is probabilistic, not confirmed."
        },
        {
            "id": "BLS-WOKE-002",
            "name": "Established Creator Pattern",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.36,
            "explanation": "George Kay's Lupin features a Senegalese-French lead in a race-swapped adaptation of the classic gentleman-thief stories. His Criminal series foregrounds diversity in its ensemble casts. His working pattern suggests a creator who considers representation a baseline requirement rather than an artistic choice. This does not mean Blood Sacrifice will be woke, but the creator's established preferences lower the probability that it will be ideologically neutral."
        },
        {
            "id": "BLS-WOKE-003",
            "name": "Estrangement as Toxic Masculinity",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.54,
            "explanation": "The father-son estrangement premise could be played straight -- two stubborn men who stopped talking -- or it could be weaponized as an indictment of male emotional incompetence. If the father's distance is framed as 'toxic masculinity' and his redemption requires him to adopt emotionally expressive, therapy-informed communication, the traditional reconciliation structure gets hollowed out and replaced with progressive moralizing. This is a known pattern in post-2020 streaming dramas and is the highest-risk woke entry point in the premise. Note: this is scored as speculative based on industry pattern analysis, not confirmed viewing."
        }
    ],
    "wokeScore": 1.5,
    "tradScore": 10.32,
    "scoreMargin": "+8.82",
    "authIndex": 87,
    "verdict": "BALANCED TRADITIONAL",
    "preRelease": True,
    "wokeTrap": False,
    "woke_trap_assessment": "Blood Sacrifice does not appear to employ a woke trap. The premise -- father-son detective duo reunites to catch a killer -- announces its dramatic commitments transparently. This is a crime thriller first, a family drama second. The risk is not a hidden ideological payload but rather a progressive framing of the father-son estrangement (toxic masculinity narrative) that would surface early and remain visible. Based on the premise alone, the series is structurally unlikely to conceal its ideological content past the midpoint. If it turns out to be a polemic about male emotional incompetence dressed as a crime thriller, that would be apparent by Episode 2, not Episode 5.",
    "seo": {
        "titleTag": "Is Blood Sacrifice (2026) Woke? Netflix's Swedish Crime Thriller Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Blood Sacrifice (2026), the Netflix Sweden crime thriller from Lupin creator George Kay. Father-son detectives hunt a Stockholm killer. Trope scores, verdict: BALANCED TRADITIONAL (+8.82). Parental guidance included.",
        "keywords": "is blood sacrifice woke, blood sacrifice 2026 review, blood sacrifice netflix, blood sacrifice virtuevigil, george kay blood sacrifice, blood sacrifice parents guide, swedish crime thriller netflix, blood sacrifice traditional or woke"
    },
    "summary": {
        "overall": "Blood Sacrifice is a Netflix Sweden limited series from George Kay, the creator of Lupin and Hijack, that pairs a semi-estranged father and son as detective partners hunting a mysterious killer in Stockholm. The premise is a two-engine story: a crime thriller and a family reconciliation drama running on parallel tracks. On paper, this scores strongly traditional. The father-son dynamic, the justice-seeking framework, and the male-competence-through-profession structure are all durable traditional storytelling elements that predate and outlast any ideological fashion. The risk is execution: Kay works in the Netflix ecosystem, Swedish crime dramas have a long history of embedding progressive social commentary, and the estranged-father premise could easily become a toxic-masculinity lecture. This review is pre-release and will be updated after viewing.",
        "whatWeLove": "The father-son detective premise is a rock-solid traditional foundation. Stories about fractured families repairing themselves through shared purpose are not political -- they are human, and they work across every culture and century. Kay's track record with Lupin and Hijack shows he knows how to build tension and character simultaneously; he is a competent craftsman. The Stockholm setting is fresh territory for English-language crime drama. If the series plays the reconciliation straight -- two men learning to trust each other again through action, not through therapy-speak -- it could be genuinely satisfying. The limited-series format suggests a complete, closed story rather than an endlessly extending franchise, which is itself a traditional value: stories that know when to end.",
        "whatToWatchFor": "The highest-risk element is the father-son estrangement. If the father's distance is framed as emotional failure requiring a progressive re-education in vulnerability and 'doing the work,' the traditional reconciliation engine gets hijacked and the series becomes a morality play about male deficiency. Swedish productions default to progressive social frameworks; Netflix amplifies this. George Kay's Lupin turned Arsene Lupin into a Senegalese immigrant story, which worked on its own terms but signaled a creator who sees representation as a creative baseline. Parents should know this is rated TV-MA: expect crime-scene violence, possibly sexual content, and the grim psychological terrain that Nordic noir specializes in. This is not a family watch. The series will almost certainly include subtitled Swedish dialogue alongside English. As this is a pre-release assessment based on premise and creator analysis, scores and verdict will be updated after full viewing."
    }
}

# Validate
reviews_to_add = [xmen, loki, blood_sacrifice]
for r in reviews_to_add:
    assert r['slug'] not in existing_slugs, f"DUPLICATE: {r['slug']}"
    assert 'seo' in r, f"Missing SEO: {r['slug']}"
    assert 'titleTag' in r['seo'], f"Missing titleTag: {r['slug']}"
    assert 'metaDescription' in r['seo'], f"Missing metaDescription: {r['slug']}"
    assert isinstance(r['tropeAudit'], list) and len(r['tropeAudit']) >= 5, f"Too few tropes: {r['slug']}"
    # Verify scores
    trad = sum(t['weightedScore'] for t in r['tropeAudit'] if t['category'] == 'Traditional')
    woke = sum(t['weightedScore'] for t in r['tropeAudit'] if t['category'] == 'Woke')
    assert abs(trad - r['tradScore']) < 0.01, f"tradScore mismatch for {r['slug']}: computed {trad} != stored {r['tradScore']}"
    assert abs(woke - r['wokeScore']) < 0.01, f"wokeScore mismatch for {r['slug']}: computed {woke} != stored {r['wokeScore']}"
    margin = round(trad - woke, 2)
    expected_margin = float(r['scoreMargin'].replace('+',''))
    assert abs(margin - expected_margin) < 0.01, f"scoreMargin mismatch for {r['slug']}: computed {margin} != stored {expected_margin}"
    print(f"✅ {r['slug']}: trad={trad}, woke={woke}, margin={margin}, verdict={r['verdict']}")

# Append to reviews
for r in reviews_to_add:
    reviews.append(r)

with open(REVIEWS_PATH, 'w') as f:
    json.dump(reviews, f, indent=2)

print(f"\nAppended 3 reviews. New total: {len(reviews)}")
print("All validations passed.")