#!/usr/bin/env python3
"""Append 3 daily reviews: Twilight (2008), The Walking Dead (2010), The Dog Stars (2026)."""
import json, sys, os

REVIEWS_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'reviews.json')

with open(REVIEWS_PATH) as f:
    reviews = json.load(f)

# ────────────────────────────────────────────────────────────
# 1. TWILIGHT (2008) — Catalog Backfill
# ────────────────────────────────────────────────────────────
twilight = {
    "id": "twilight-2008",
    "slug": "twilight-2008",
    "title": "Twilight",
    "year": 2008,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Romantic Fantasy, Drama",
    "date": "2026-08-26",
    "datePublished": "2026-08-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min",
    "poster": "/images/posters/twilight-2008.jpg",
    "releaseDate": "2008-11-21",
    "rating": "PG-13",
    "runtime": 121,
    "director": "Catherine Hardwicke",
    "writers": "Melissa Rosenberg",
    "cast": [
        "Kristen Stewart as Bella Swan",
        "Robert Pattinson as Edward Cullen",
        "Billy Burke as Charlie Swan",
        "Peter Facinelli as Carlisle Cullen",
        "Ashley Greene as Alice Cullen",
        "Kellan Lutz as Emmett Cullen",
        "Nikki Reed as Rosalie Hale",
        "Jackson Rathbone as Jasper Hale",
        "Cam Gigandet as James"
    ],
    "studio": "Temple Hill Entertainment, Maverick Films",
    "distributor": "Summit Entertainment",
    "verdict": "TRADITIONAL",
    "wokeScore": 6.1,
    "tradScore": 16.31,
    "authIndex": 79,
    "scoreMargin": "+10 TRAD",
    "preRelease": None,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Twilight is exactly what it appears to be: a teen vampire romance with Mormon theological undertones. The abstinence message is visible from the first act. Edward's refusal of premarital sex is the central romantic tension. There is no ideological bait-and-switch."
    },
    "summary": {
        "overall": "Twilight is the most successful Mormon conversion narrative ever smuggled into a mainstream multiplex, and it is not even trying to hide. Catherine Hardwicke's adaptation of Stephenie Meyer's novel made $412 million worldwide off a $37 million budget while preaching premarital abstinence, eternal commitment, and the proposition that a century-old vampire has more sexual restraint than most high school boys. Kristen Stewart's Bella Swan is a cipher by design: the audience is meant to insert themselves into her place, to be courted by Robert Pattinson's Edward Cullen, who despite being a vampire has the moral code of a youth pastor. The film's dialogue is famously wooden, its pacing is glacial, and its central romance has the intellectual depth of a greeting card. None of that matters. Twilight connected because it told teenage girls something the culture had stopped telling them: that waiting is romantic, that restraint is attractive, and that a man who protects you from himself is more desirable than one who simply takes. The woke score reflects elements that will concern traditional viewers: the age-gap power dynamic between a century-old immortal and a high school junior is troubling no matter how chastely it is handled, and the Cullen coven functions as a replacement family in a way that sidelines Bella's biological father Charlie. But the traditional score is higher because the film's moral architecture is unmistakably conservative. Edward Cullen is the most traditional romantic lead in 21st-century studio cinema: he refuses sex before marriage, he puts Bella's safety above his own desires, and his entire family operates on a code of self-denial that would make Jonathan Edwards blush. The Cullens are vegetarians. They drink animal blood instead of human blood. This is a metaphor for chastity so heavy-handed it practically comes with a study guide. For parents wondering whether Twilight is safe for their teenagers: the film's values are far more conservative than anything else in the YA genre. The concern is not the ideology. The concern is how effectively the film sells its romance, because the relationship it romanticizes is genuinely unhealthy in ways that have nothing to do with politics.",
        "adultInsight": "Twilight is best understood as a cultural artifact of the late Bush era: a repudiation of the anything-goes sexual culture that the 1990s and early 2000s normalized, dressed in vampire mythology and set to a moody indie-rock soundtrack. Stephenie Meyer is Mormon, and her theology saturates every frame. The Cullens are an eternal family sealed together by choice and covenant, not blood, which is essentially the Mormon doctrine of sealing. Edward's refusal to have sex with Bella until marriage despite her physical desire for him is the exact inversion of every teen sex comedy and CW drama of the era. The series was mocked relentlessly by critics who found it prudish, melodramatic, and anti-feminist, and it is all of those things, which is precisely why audiences showed up in numbers that no critic could explain. The cast is worth noting. Kristen Stewart has spent the years since Twilight establishing herself as one of the most interesting actresses of her generation, working with Olivier Assayas, Kelly Reichardt, and Pablo Larrain. Robert Pattinson followed a similar trajectory through David Cronenberg, the Safdie brothers, and eventually the Batman franchise. Both have spoken ambivalently about the franchise in interviews, which is its own kind of traditional morality play: the artists who made the thing now distance themselves from it, but the audience that loved it never stopped.",
        "parentalGuidance": "Rated PG-13 for some violence and a scene of sensuality. The violence is largely bloodless vampire action: a baseball game in a thunderstorm, a ballet-studio confrontation, and a climactic fight that results in dismemberment without gore. The sensuality is limited to passionate kissing and one scene of Bella and Edward in bed together fully clothed, where Edward insists they stop. No nudity. No sex. No profanity of note. The romantic intensity is the real parental concern: the relationship between Bella and Edward is portrayed as all-consuming, obsessive, and literally life-threatening, which may model unhealthy relationship expectations for younger teens. The age gap between a century-old immortal and a high school junior is never addressed as problematic by the film. Recommended for 13 and up, with parental discussion about the difference between romantic devotion and emotional dependency."
    },
    "parentalGuidance": "Rated PG-13 for some violence and a scene of sensuality. Vampire action is bloodless. The central romance is emotionally intense but physically chaste: Edward refuses sex before marriage. No nudity, no profanity. The age-gap dynamic between a century-old immortal and a teenager is the most concerning element for parents, as the film romanticizes what would be a predatory relationship in any other context. Recommended 13+ with discussion about healthy relationship boundaries.",
    "tropeAudit": [
        {
            "id": "TRADITIONAL-034",
            "name": "Sanctity of Marriage",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Edward's refusal of premarital sex is the central romantic tension. He insists on waiting until marriage despite Bella's desire. This is the most explicit abstinence message in any studio film of the 2000s. Severity 4: drives the romantic arc. Authenticity High (0.7): Meyer's Mormon theology. Centrality High (1.8): the organizing principle of the relationship. 4 x 0.7 x 1.8 = 5.04."
        },
        {
            "id": "TRADITIONAL-026",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Edward repeatedly puts himself between Bella and mortal danger: pulling her from a skidding van, fighting James to save her life, and ultimately offering to leave her entirely to keep her safe. His defining trait is willingness to sacrifice everything for her protection. Severity 4: defines his character. Authenticity High (0.7): organic to the Gothic romance tradition. Centrality High (1.8): the plot turns on it. 4 x 0.7 x 1.8 = 5.04."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "The Cullen family unites to protect Bella from James the tracker vampire. Carlisle organizes the defense, Alice provides strategic foresight, and the entire family accepts personal risk to defend a human they barely know. Severity 3: the third-act driver. Authenticity High (0.7): protective instinct is natural. Centrality High (1.8): the climax. 3 x 0.7 x 1.8 = 3.78."
        },
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "Charlie Swan is a police chief, a loving but awkward father, and the film's only consistent source of normal human morality. He is protective without being overbearing and provides Bella with a stable home after her mother's remarriage. Severity 2: supporting character. Authenticity High (0.7): small-town police chief is an organic archetype. Centrality Low (0.5): present throughout but not the focus. 2 x 0.7 x 0.5 = 0.7."
        },
        {
            "id": "TRADITIONAL-036",
            "name": "Traditional Femininity",
            "category": "Traditional",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "Bella's first acts upon arriving in Forks are domestic: she shops for groceries, cooks for Charlie, and takes over household management. Her nurturing instinct is presented without irony as a natural trait. Severity 1: trace-level characterization. Authenticity High (0.7): Meyer's portrayal of teenage girlhood. Centrality Low (0.5): background detail. 1 x 0.7 x 0.5 = 0.35."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs Evil",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "The Cullens (vegetarian vampires who protect human life) are unambiguously good; James and his coven (vampires who hunt humans) are unambiguously evil. There is no moral gray area, no sympathetic backstory for the villains. Severity 2: clear but simple. Authenticity High (0.7): classic good/evil binary. Centrality Moderate (1.0): drives the conflict. 2 x 0.7 x 1.0 = 1.4."
        },
        {
            "id": "WOKE-022",
            "name": "Sexual Liberation as Empowerment",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "Bella's persistent desire for physical intimacy with Edward, even as he refuses, is framed as her sexual agency and self-knowledge. The film validates her wanting him in opposition to his restraint, creating an undertow of sexual empowerment that runs counter to the abstinence message. Severity 1: subtextual, never explicit. Authenticity Low (1.4): reads as a modern Hollywood insert into Meyer's chaste source material. Centrality Low (0.5): a few scenes. 1 x 1.4 x 0.5 = 0.7."
        },
        {
            "id": "WOKE-001",
            "name": "Glamorized Age-Gap Romance",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 5.4,
            "explanation": "The central romance is between a 108-year-old immortal and a 17-year-old high school student. This is never framed as concerning; it is framed as destiny. From a traditional values perspective, the normalization of a vast power-imbalanced relationship with a minor is more ideologically corrosive than any political messaging could be. Severity 3: the entire premise of the franchise. Authenticity Moderate (1.0): vampires are canonically old, but Meyer frames the age gap as aspirational rather than monstrous. Centrality High (1.8): it is the film. 3 x 1.0 x 1.8 = 5.4."
        }
    ],
    "seo": {
        "titleTag": "Is Twilight (2008) Woke? The Mormon Vampire Romance Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Twilight (2008), the Kristen Stewart and Robert Pattinson vampire romance that preached abstinence to $412M at the box office. Verdict: TRADITIONAL (+10 margin). Full trope audit and parental guidance included.",
        "keywords": [
            "is twilight 2008 woke",
            "twilight movie review",
            "twilight parents guide",
            "kristen stewart robert pattinson twilight",
            "twilight virtuevigil review",
            "twilight conservative review",
            "stephenie meyer movie review",
            "twilight woke or traditional",
            "twilight abstinence message",
            "twilight mormon themes",
            "catherine hardwicke twilight",
            "twilight age gap controversy"
        ]
    },
    "externalScores": {
        "rt_critics": 56,
        "rt_audience": 73,
        "imdb": 5.3,
        "metacritic": 56,
        "budget": "$37 million",
        "globalBoxOffice": "$412 million"
    },
    "fidelity_casting": {
        "sourceType": "Book Adaptation",
        "assessment": "Twilight is a faithful adaptation of Stephenie Meyer's 2005 novel. The casting of Kristen Stewart and Robert Pattinson was initially controversial among the book's fanbase, with Meyer herself initially preferring other actors, but both leads became so identified with their roles that the characters are now inseparable from the actors who played them. The film makes no meaningful changes to the source material's racial or gender composition. Fidelity casting concerns do not apply."
    }
}

# ────────────────────────────────────────────────────────────
# 2. THE WALKING DEAD (2010) — TV Series
# ────────────────────────────────────────────────────────────
walking_dead = {
    "id": "the-walking-dead-2010",
    "slug": "the-walking-dead-2010",
    "title": "The Walking Dead",
    "year": 2010,
    "type": "series",
    "platform": "AMC",
    "genre": "Post-Apocalyptic Horror Drama",
    "date": "2026-08-26",
    "datePublished": "2026-08-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/the-walking-dead-2010.jpg",
    "releaseDate": "2010-10-31",
    "rating": "TV-MA",
    "runtime": "11 seasons, 177 episodes",
    "director": "Frank Darabont (developer)",
    "writers": "Frank Darabont, Robert Kirkman (comic), Glen Mazzara, Scott M. Gimple, Angela Kang (showrunners)",
    "cast": [
        "Andrew Lincoln as Rick Grimes",
        "Jon Bernthal as Shane Walsh",
        "Sarah Wayne Callies as Lori Grimes",
        "Norman Reedus as Daryl Dixon",
        "Melissa McBride as Carol Peletier",
        "Danai Gurira as Michonne",
        "Jeffrey Dean Morgan as Negan",
        "Lauren Cohan as Maggie Greene",
        "Steven Yeun as Glenn Rhee",
        "Chandler Riggs as Carl Grimes"
    ],
    "studio": "AMC Studios, Idiot Box Productions, Circle of Confusion",
    "distributor": "AMC Networks",
    "verdict": "TRADITIONAL",
    "wokeScore": 7.5,
    "tradScore": 21.14,
    "authIndex": 74,
    "scoreMargin": "+14 TRAD",
    "preRelease": None,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "The Walking Dead never concealed its ideological tensions. From the pilot, the show was about whether civilization's collapse meant the end of traditional morality or its necessity. Rick Grimes's lawman ethos was tested from Season 1. The show's progressive elements (found family, strong female warriors, critique of institutional authority) were visible from the beginning and never hidden behind a false promise of conservative values."
    },
    "summary": {
        "overall": "The Walking Dead ran for eleven seasons and 177 episodes on AMC from 2010 to 2022, which is either a testament to its creative durability or proof that television executives will never stop milking a franchise until the cow is a skeleton, depending on your disposition toward zombie media. Developed by Frank Darabont from Robert Kirkman's comic series, the show follows sheriff's deputy Rick Grimes (Andrew Lincoln) as he wakes from a coma to find civilization collapsed and the dead walking. He finds his family, assembles a group of survivors, and spends the next decade discovering that the living are far more dangerous than the dead. The series is, at its core, a sustained argument about what happens to morality when institutions collapse. Rick Grimes begins as a lawman who believes in due process, and the show's entire dramatic arc is the slow, brutal education in what due process cannot survive. By Season 5, he is executing people without trial. By Season 8, he is leading a war. The question the show asks, over and over, is whether traditional morality is a luxury of civilization or its foundation. The Walking Dead's traditional score is driven overwhelmingly by Rick Grimes: the reluctant leader, the father who will do anything to protect his son, the sheriff who cannot stop being the sheriff even when there is no law left. Andrew Lincoln's performance anchors the entire series in a moral seriousness that the later seasons sometimes strain against but never fully abandon. Rick's defining speech, delivered in the Season 4 finale, is essentially a declaration of feudal lordship: 'There's a compound bow and a machete and a thousand rounds of ammo. If you want to live, you have to accept my authority.' That is not democracy. It is the return of the war chief. The show knows this and does not flinch. The woke score reflects elements that will bother traditional viewers: the survivor group functions as a found family that repeatedly supersedes biological kinship, government and military institutions are portrayed as either incompetent or malevolent, and the show's female characters evolve from traditional roles into hardened warriors in ways that occasionally strain credibility for ideological effect. But these elements exist in tension with the show's deeper traditional instincts rather than overriding them. The Walking Dead is fundamentally conservative in its pessimism: it believes that civilization is thin, that violence is inescapable, and that the only thing standing between order and chaos is a good man with a gun who is willing to do terrible things.",
        "adultInsight": "The Walking Dead's cultural peak, roughly Seasons 3 through 6, coincided with the Obama-era zenith of prestige television, and the show's politics are best understood in that context. The survival group is multicultural by design—a Korean pizza delivery boy, a redneck tracker, a Black lawyer with a katana, a battered housewife turned sniper—not because the show had a DEI mandate but because Kirkman's comic was always about assembling a coalition from the wreckage. The show's handling of race is notably colorblind for its era: Glenn and Maggie's interracial relationship in Season 2 was treated as unremarkable, and the show never made identity the point. What is the point, and what traditional viewers should appreciate, is the show's sustained argument that masculine protectiveness is not toxic but necessary. Rick, Daryl, Glenn, Abraham, and eventually Negan are all variations on the same theme: men who are dangerous and useful because they are dangerous. The show occasionally feints toward criticizing this, especially in later seasons, but it cannot escape its own premise. In a world where the dead eat the living, pacifism is suicide and gentleness gets people killed. The Walking Dead is ultimately more honest about human nature than the prestige dramas that looked down on it.",
        "parentalGuidance": "Rated TV-MA for sustained graphic violence, gore, and disturbing imagery throughout all eleven seasons. This is one of the most violent shows ever aired on basic cable. Zombies are dispatched via headshots, bludgeoning, dismemberment, and immolation. Human-on-human violence includes executions, torture, cannibalism, and a famous scene involving a barbed-wire baseball bat. Sexual content is present but not explicit; nudity is minimal given cable standards. The show's emotional violence is arguably harder to watch than its physical violence: children die, spouses are forced to kill infected partners, and characters the audience has known for seasons are killed without warning or ceremony. NOT suitable for viewers under 16. Even older teens should watch with parental awareness of the show's unrelenting bleakness. The series contains positive traditional values—self-sacrifice, paternal protection, loyalty to one's group—but they are embedded in a world so grim that the values feel more like survival instincts than moral choices."
    },
    "parentalGuidance": "Rated TV-MA. One of the most violent series in cable history. Sustained graphic zombie violence, human-on-human brutality including torture and cannibalism, and numerous child deaths. No sexual nudity but some sexual situations. Profanity limited by basic cable standards. The show's traditional values (paternal protection, self-sacrifice, loyalty) are genuine but earned through relentless suffering. NOT for viewers under 16. Even adults should be prepared for the emotional toll of characters they care about dying regularly and without ceremony.",
    "tropeAudit": [
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Rick Grimes is the moral and physical center of the series, a father whose every decision is filtered through the imperative to protect his son Carl and his group. He is the principled patriarch archetype at its most extreme: the father who will kill to protect his children. Severity 4: the series' organizing consciousness. Authenticity High (0.7): Rick's lawman background makes his protective instinct organic. Centrality High (1.8): the show is about Rick. 4 x0.7 x 1.8 = 5.04."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The entire premise of the survivor group is mutual defense. Every major arc involves protecting the vulnerable: Carl, Judith, the Alexandrians, the Hilltop residents. Rick's most defining moments are decisions to fight rather than flee when innocents are at risk. Severity 4: the show's moral engine. Authenticity High (0.7): protective instinct is natural. Centrality High (1.8): every season. 4 x 0.7 x 1.8 = 5.04."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs Evil",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "The Governor, the Terminus cannibals, Negan, and Alpha are presented as unambiguously evil. The show may complicate their psychology but never justifies their actions. The moral binary is clear: our group protects life; their group destroys it. Severity 3: present throughout. Authenticity High (0.7): Kirkman's comic has always been morally binary. Centrality High (1.8): drives every conflict. 3 x0.7 x1.8 = 3.78."
        },
        {
            "id": "TRADITIONAL-038",
            "name": "The Reluctant Leader",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Rick never wants leadership; it is forced on him by crisis and competence. He repeatedly tries to share power through councils and democracy, and the show repeatedly demonstrates that in extremis, councils fail and one person must decide. Severity 3: recurring theme. Authenticity High (0.7): leadership as burden is a classic trope. Centrality High (1.8): Rick's arc across eleven seasons. 3 x0.7 x1.8 = 3.78."
        },
        {
            "id": "TRADITIONAL-041",
            "name": "Industry and Perseverance",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Survival in The Walking Dead is a function of unrelenting labor: fortifying walls, scavenging supplies, farming, training. The group that works hardest survives longest. The show celebrates practical competence over ideology. Severity 3: constant background. Authenticity High (0.7): post-apocalyptic premise demands it. Centrality Moderate (1.0): not the focus but omnipresent. 3 x0.7 x1.0 = 2.1."
        },
        {
            "id": "TRADITIONAL-035",
            "name": "The Just Lawman",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "Rick begins as a sheriff's deputy who believes in law and order. The series traces his transformation from lawman to warlord, but his original identity as a servant of civil order is never forgotten. Severity 2: origin point. Authenticity High (0.7): law enforcement background is given. Centrality Moderate (1.0): shapes his early decisions. 2 x0.7 x1.0 = 1.4."
        },
        {
            "id": "WOKE-005",
            "name": "Chosen Family over Bio-Kin",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 3.6,
            "explanation": "The survivor group repeatedly replaces and supersedes biological family. Rick's group becomes his family in ways that eclipse blood ties. Glenn and Maggie's relationship, Carol's adoption of various children, and the group's self-identification as a family unit all elevate chosen bonds over biological ones. Severity 2: persistent subtext. Authenticity Moderate (1.0): organic to the post-apocalypse genre. Centrality High (1.8): the group dynamic is the show. 2 x1.0 x 1.8 = 3.6."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Evil",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "explanation": "Government and military collapse entirely, and what remains of institutional authority (the CDC, the Saviors' extortion racket, the Commonwealth's class system) is portrayed as corrupt, incompetent, or malevolent. The show's thesis is that institutions cannot be trusted and individuals must rebuild from scratch. Severity 2: recurring. Authenticity Moderate (1.0): genre convention but the show leans into it. Centrality Moderate (1.0): subplot level. 2 x 1.0 x 1.0 = 2.0."
        },
        {
            "id": "WOKE-003",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "Carol evolves from battered housewife to the group's most lethal member. Michonne is introduced as a katana-wielding lone warrior. These arcs are largely earned through character development, but the show occasionally strains credibility to elevate female competence beyond what the setting can justify, particularly in later seasons. Severity 2: present. Authenticity High (0.7): Carol and Michonne's arcs are organic to their circumstances. Centrality Moderate (1.0): notable but not the focus. 2 x 0.7 x 1.0 = 1.4."
        },
        {
            "id": "WOKE-001",
            "name": "Progressive Relationship Norms",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "explanation": "The series normalizes interracial and non-traditional relationships without comment. Glenn (Korean-American) and Maggie (white Southern) are the show's central romance. Later seasons introduce same-sex relationships. Severity 1: trace. Authenticity Moderate (1.0): Kirkman's comic was always diverse. Centrality Low (0.5): background to the survival drama. 1 x1.0 x 0.5 = 0.5."
        }
    ],
    "seo": {
        "titleTag": "Is The Walking Dead (2010) Woke? AMC's Zombie Epic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil reviews AMC's The Walking Dead (2010-2022). Eleven seasons, 177 episodes. Rick Grimes, zombie apocalypse, parental guidance. Verdict: TRADITIONAL (+14 margin). Full trope audit.",
        "keywords": [
            "is the walking dead woke",
            "the walking dead review",
            "the walking dead parents guide",
            "rick grimes traditional values",
            "the walking dead conservative review",
            "amc the walking dead woke",
            "the walking dead virtuevigil",
            "robert kirkman walking dead politics",
            "zombie apocalypse tv series review",
            "the walking dead appropriate for teens"
        ]
    },
    "externalScores": {
        "rt_critics": 79,
        "rt_audience": 77,
        "imdb": 8.1,
        "metacritic": 72
    },
    "fidelity_casting": {
        "sourceType": "Comic Book Adaptation",
        "assessment": "The Walking Dead takes significant departures from Kirkman's comic, including killing characters who survived in the source material, extending others' arcs, and creating original characters like Daryl Dixon. The show's racial composition largely mirrors the comic's, though some characters were race-swapped from the page to the screen. None of these changes were ideologically motivated in ways that affect the show's scoring."
    }
}

# ────────────────────────────────────────────────────────────
# 3. THE DOG STARS (2026) — New Release, Pre-Release
# ────────────────────────────────────────────────────────────
dog_stars = {
    "id": "the-dog-stars-2026",
    "slug": "the-dog-stars-2026",
    "title": "The Dog Stars",
    "year": 2026,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Post-Apocalyptic Science Fiction, Drama",
    "date": "2026-08-26",
    "datePublished": "2026-08-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min",
    "poster": "/images/posters/the-dog-stars-2026.jpg",
    "releaseDate": "2026-08-28",
    "rating": "R",
    "runtime": 118,
    "director": "Ridley Scott",
    "writers": "Mark L. Smith",
    "cast": [
        "Jacob Elordi as Hig",
        "Josh Brolin as Bangley",
        "Margaret Qualley",
        "Guy Pearce"
    ],
    "studio": "20th Century Studios, Scott Free Productions",
    "distributor": "20th Century Studios",
    "verdict": "PREDICTED: TRADITIONAL",
    "wokeScore": 0.7,
    "tradScore": 15.19,
    "authIndex": 88,
    "scoreMargin": "+14 TRAD",
    "preRelease": True,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Based on Peter Heller's 2012 novel which is essentially a meditation on masculine competence, loyalty, and the will to survive. Ridley Scott is not a director who embeds hidden ideological payloads. The pre-release materials, trailer, and source novel all indicate a straightforward post-apocalyptic survival drama. No bait-and-switch detected."
    },
    "summary": {
        "overall": "The Dog Stars arrives August 28, 2026, directed by Ridley Scott from a screenplay by Mark L. Smith (The Revenant), adapting Peter Heller's acclaimed 2012 novel. Jacob Elordi stars as Hig, a former civilian pilot, opposite Josh Brolin as Bangley, a hardened ex-Marine, in a post-apocalyptic survival drama set after a flu pandemic has nearly erased humanity. The two men defend a small compound in Colorado, fending off raiders while Hig makes reconnaissance flights in his aging Cessna, holding onto the possibility that something better exists beyond their perimeter. This is Ridley Scott operating in stripped-down mode: no massive ensemble, no CGI cities, no franchise obligations. Just two men, a dog, an airplane, and the question of what survival is worth if there is nothing left to survive for. The source material is explicitly traditional in its moral architecture. Heller's novel is narrated by Hig in a voice that is part Hemingway and part Wendell Berry: a man who kills when he must, loves a dog with the devotion most men reserve for children, and finds transcendence in the natural world even as it is trying to kill him. Bangley is the counterweight: a man for whom survival is the only value, because survival is the precondition for all other values. Their dynamic—the dreamer and the pragmatist, the man who flies toward hope and the man who digs in and waits—is the film's engine. No pre-release materials suggest progressive ideological injection. The casting is diverse in ways that serve the story: Josh Brolin brings the flinty authority of a man who has been killing things for so long he has forgotten why he started, and Jacob Elordi brings the bruised sensitivity of someone who remembers exactly why. Margaret Qualley and Guy Pearce appear in supporting roles that the source material treats with seriousness. The predicted TRADITIONAL verdict reflects a film that appears built on values of masculine competence, loyalty, stewardship of the land, and the proposition that hope is a survival strategy rather than a luxury. VirtueVigil will update this review after theatrical release with a full trope audit based on the completed film.",
        "adultInsight": "Peter Heller's novel is a literary cousin to Cormac McCarthy's The Road, but with an important difference: Heller believes in the possibility of renewal. Where McCarthy's father is carrying the fire through absolute darkness, Heller's Hig is flying toward it. The novel is narrated in a voice that blends terse action prose with passages of startling beauty about rivers, mountains, and the persistence of the natural world after humanity has largely departed. Ridley Scott has been making films about men in extremis since The Duellists in 1977. At 88 years old, he is still directing at a pace that exhausts filmmakers half his age. His late-career output has been inconsistent—The Last Duel was brilliant and nobody saw it, Napoleon was ambitious and nobody liked it—but Gladiator II demonstrated that Scott still knows how to stage action with clarity and weight. The Dog Stars is a smaller canvas, and Scott's best films have often been the ones where the scale forces him to focus on performance rather than spectacle. The casting of Jacob Elordi is significant. Elordi has spent the last several years carefully constructing a career that alternates between mainstream visibility (Saltburn, Priscilla) and auteur credibility (Paul Schrader's Oh, Canada). Choosing a Ridley Scott post-apocalyptic drama as his next move signals ambition beyond the heartthrob lane. Josh Brolin is Josh Brolin: one of the most reliable actors in American cinema when the role requires a man who has seen too much and is still standing.",
        "parentalGuidance": "Rated R for violence, language, and thematic material. Based on the source novel, expect: sustained post-apocalyptic violence including gunfights and hand-to-hand combat, some of it brutal; strong language throughout given the ex-military characters; thematic material involving pandemic, mass death, and the collapse of civilization. The novel contains a scene of sexual assault that is treated with gravity; whether and how Scott adapts this will affect the final parental guidance assessment. The film's core values—loyalty, courage, the defense of one's home—are traditional. The violence is in service of those values, not gratuitous. Recommended for 16 and up, pending final theatrical release review."
    },
    "parentalGuidance": "Rated R for violence, language, and thematic material. Expect post-apocalyptic combat violence, strong language, and themes of pandemic and civilizational collapse. Base on source novel: one scene of sexual assault treated seriously. Core values are traditional: loyalty, courage, defense of home. Not for viewers under 16. Full updated parental guidance will follow theatrical release review.",
    "tropeAudit": [
        {
            "id": "TRADITIONAL-028",
            "name": "The Rugged Individualist",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Hig survives through his own skills as a pilot, his knowledge of the land, and his refusal to rely on anyone but himself and his dog. The novel is essentially a hymn to self-reliance in the American West tradition. Severity 3: defines Hig's character. Authenticity High (0.7): organic to the post-apocalyptic survival genre. Centrality High (1.8): Hig's self-reliance is the book. 3 x 0.7 x 1.8 = 3.78."
        },
        {
            "id": "TRADITIONAL-031",
            "name": "The Patriotic Soldier",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Bangley is a former Marine whose military training is the reason the compound survives. His competence in violence is presented as a genuine good, not a pathology. The novel respects martial skill without irony. Severity 3: Bangley's defining trait. Authenticity High (0.7): ex-military survivalists are a post-apocalyptic genre staple. Centrality High (1.8): Bangley is co-lead. 3 x 0.7 x 1.8 = 3.78."
        },
        {
            "id": "TRADITIONAL-041",
            "name": "Industry and Perseverance",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Survival in the novel is a function of daily, grinding labor: maintaining the plane, fortifying the compound, growing food, patrolling the perimeter. Hard work is the only currency that matters. Severity 3: the texture of daily life. Authenticity High (0.7): post-apocalyptic setting demands it. Centrality High (1.8): survival through work is the premise. 3 x 0.7 x 1.8 = 3.78."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "The compound exists to protect the vulnerable. Hig's flights search for survivors and a better future. The impulse to defend rather than prey on the weak is what separates the protagonists from the raiders. Severity 3: moral differentiator. Authenticity High (0.7): protective instinct. Centrality Moderate (1.0): one of several themes. 3 x 0.7 x 1.0 = 2.1."
        },
        {
            "id": "TRADITIONAL-038",
            "name": "The Reluctant Leader",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "Hig does not seek authority; it accrues to him through competence and the vacuum left by civilization's collapse. He leads because someone must and he is the one who can. Severity 2: character dynamic. Authenticity High (0.7): the reluctant hero is a classic archetype. Centrality Moderate (1.0): present but not foregrounded. 2 x 0.7 x 1.0 = 1.4."
        },
        {
            "id": "TRADITIONAL-040",
            "name": "Stewardship of Creation",
            "category": "Traditional",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "Heller's novel contains extended passages of natural description that treat the post-pandemic landscape with reverence rather than environmentalist polemic. The natural world is a gift to be stewarded, not a victim to be avenged. Severity 1: atmospheric. Authenticity High (0.7): the Western literary tradition. Centrality Low (0.5): background texture. 1 x 0.7 x 0.5 = 0.35."
        },
        {
            "id": "WOKE-010",
            "name": "Climate Guilt Propaganda",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "The pandemic in the novel is a flu, not climate change, and the natural world is depicted as reclaiming human spaces neutrally rather than vengefully. A Hollywood adaptation could insert climate guilt messaging, but Scott's track record and the source material argue against it. Severity 1: not present in source. Authenticity High (0.7): the novel treats nature as setting, not politics. Centrality Low (0.5): at most subtext. 1 x 0.7 x 0.5 = 0.35."
        },
        {
            "id": "WOKE-001",
            "name": "Diverse Casting in Post-Apocalyptic Setting",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "The cast is multi-ethnic. In a post-apocalyptic America, diverse casting is organic to the setting and does not register as ideological intervention. No characters appear to have been race-swapped from their book descriptions. Severity 1: not ideological. Authenticity High (0.7): organic to modern casting practice. Centrality Low (0.5): background. 1 x 0.7 x 0.5 = 0.35."
        }
    ],
    "seo": {
        "titleTag": "Is The Dog Stars (2026) Woke? Ridley Scott Post-Apocalyptic Film Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's pre-release review of The Dog Stars (2026), Ridley Scott's adaptation of Peter Heller's post-apocalyptic novel starring Jacob Elordi and Josh Brolin. Verdict: PREDICTED TRADITIONAL (+14 margin). In theaters August 28.",
        "keywords": [
            "is the dog stars 2026 woke",
            "the dog stars ridley scott review",
            "the dog stars movie parents guide",
            "jacob elordi josh brolin dog stars",
            "peter heller dog stars adaptation",
            "post-apocalyptic movies 2026",
            "the dog stars virtuevigil",
            "ridley scott new movie 2026",
            "the dog stars conservative review",
            "the dog stars traditional values",
            "20th century studios dog stars",
            "august 28 2026 movies"
        ]
    },
    "externalScores": {
        "rt_critics": "TBD (pre-release)",
        "rt_audience": "TBD (pre-release)",
        "imdb": "TBD (pre-release)",
        "metacritic": "TBD (pre-release)",
        "budget": "$110 million",
        "globalBoxOffice": "TBD (pre-release)"
    },
    "creative_team": {
        "director": {
            "name": "Ridley Scott",
            "ideology": "UNKNOWN/CENTER. Scott is a genre craftsman whose filmography spans Gladiator, Black Hawk Down, American Gangster, The Martian, and The Last Duel. He does not make films with discernible ideological intent. His work consistently celebrates masculine competence, honor codes, and individual agency against institutional failure.",
            "profile": "Ridley Scott has been directing major motion pictures since The Duellists in 1977. His filmography is too large and varied to reduce to a political position, but the pattern is consistent: Scott is interested in competent people doing difficult things under pressure. His heroes are soldiers, warriors, explorers, and survivors. His villains are bureaucrats, cowards, and ideologues. The Dog Stars fits squarely within this tradition."
        },
        "writers": {
            "names": "Mark L. Smith",
            "profile": "Mark L. Smith wrote The Revenant, which won Alejandro G. Inarritu an Oscar and demonstrated that Smith knows how to adapt survival literature for the screen without sentimentalizing or politicizing it. He also wrote Overlord and the Twisted Metal series. His work consistently prioritizes physical storytelling and character over ideology."
        },
        "lead_producer": {
            "name": "Ridley Scott, Michael Pruss, Mark L. Smith, Cliff Roberts",
            "company": "20th Century Studios / Scott Free Productions"
        },
        "top_cast": [
            {
                "name": "Jacob Elordi",
                "role": "Hig",
                "notes": "Lead actor; civilian pilot and protagonist"
            },
            {
                "name": "Josh Brolin",
                "role": "Bangley",
                "notes": "Co-lead; ex-Marine survivalist"
            }
        ],
        "prediction": {
            "verdict": "PREDICTED: TRADITIONAL",
            "confidence": "moderate-high"
        }
    },
    "fidelity_casting": {
        "sourceType": "Novel Adaptation",
        "assessment": "The Dog Stars adapts Peter Heller's 2012 novel of the same name. No evidence of race or gender-swapping from the source material. Jacob Elordi as Hig and Josh Brolin as Bangley are physically appropriate to their literary counterparts. Fidelity casting concerns do not apply."
    },
    "comparison_films": [
        {
            "title": "The Road",
            "year": 2009,
            "comparison": "Cormac McCarty's novel adapted by John Hillcoat. The closest thematic cousin to The Dog Stars: a father and son traveling through post-apocalyptic America. Where The Road is relentlessly bleak, The Dog Stars hold out hope. Both treat survival as a moral proposition rather than a biological imperative."
        },
        {
            "title": "The Martian",
            "year": 2015,
            "comparison": "Ridley Scott's most optimistic film, and his purest expression of the value of competence. Matt Damon's Mark Watney solves problems through science and determination. Hig solves problems through flying and fighting. Both films are arguments for human ingenuity as a moral good."
        }
    ]
}


# Append all three
reviews.extend([twilight, walking_dead, dog_stars])

with open(REVIEWS_PATH, 'w') as f:
    json.dump(reviews, f, indent=2)

print(f"Wrote {len(reviews)} reviews to {REVIEWS_PATH}")
print("Appended: twilight-2008, the-walking-dead-2010, the-dog-stars-2026")