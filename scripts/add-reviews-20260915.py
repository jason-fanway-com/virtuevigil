#!/usr/bin/env python3
"""Add 3 reviews for 2026-09-15: Daniel and the Fiery Furnace, Ben-Hur (1959), Colin from Accounts"""
import json, sys, os
from datetime import date

REVIEWS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src', 'data', 'reviews.json')

today = date.today().isoformat()

reviews = []

# === 1. Daniel and the Fiery Furnace (2026) ===
reviews.append({
    "id": "daniel-and-the-fiery-furnace-2026",
    "slug": "daniel-and-the-fiery-furnace-2026",
    "title": "Daniel and the Fiery Furnace (2026)",
    "year": 2026,
    "type": "movie",
    "platform": "Theaters",
    "genre": "Faith, Drama, Historical",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "5 min read",
    "poster": "/images/posters/daniel-and-the-fiery-furnace-2026.jpg",
    "releaseDate": "2026-09-04",
    "rating": "PG",
    "runtime": "112 min",
    "director": "Kevin Downes",
    "writers": ["Chuck Konzelman", "Cary Solomon"],
    "cast": [
        {"name": "Mena Massoud", "role": "Daniel"},
        {"name": "Jim Caviezel", "role": "Nebuchadnezzar"},
        {"name": "Kevin Sorbo", "role": "Arioch"},
        {"name": "Corbin Bernsen", "role": "Ashpenaz"}
    ],
    "studio": "Kingdom Story Company",
    "distributor": "Lionsgate",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 0.25,
    "tradScore": 18.9,
    "authIndex": "Very Low",
    "scoreMargin": "+18 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "This is a straightforward biblical adaptation from a faith-based studio. The film delivers exactly what it promises: a dramatization of Daniel 3, where three young Hebrew men refuse to bow to a golden idol and are thrown into a furnace. There is no hidden progressive content, no bait-and-switch. The message is overtly religious from the opening scene."
    },
    "seo": {
        "titleTag": "Is Daniel and the Fiery Furnace (2026) Woke? Biblical Epic Scored | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Daniel and the Fiery Furnace (2026): Mena Massoud and Jim Caviezel in the biblical story of Shadrach, Meshach, and Abednego. VVWS verdict: STRONGLY TRADITIONAL (+18). Parental guidance included.",
        "keywords": "is daniel and the fiery furnace woke, daniel and the fiery furnace 2026 review, biblical movie review, shadrach meshach abednego, christian film review, virtuevigil biblical review"
    },
    "externalScores": {
        "imdb": "N/A",
        "rottenTomatoes": "N/A",
        "metacritic": "N/A"
    },
    "creative_team": {
        "director": "Kevin Downes",
        "writer": "Chuck Konzelman, Cary Solomon",
        "top_cast": [
            "Mena Massoud as Daniel",
            "Jim Caviezel as Nebuchadnezzar",
            "Kevin Sorbo as Arioch",
            "Corbin Bernsen as Ashpenaz"
        ],
        "full_cast": ["Mena Massoud", "Jim Caviezel", "Kevin Sorbo", "Corbin Bernsen"],
        "producers": [],
        "composer": ""
    },
    "parentalGuidance": {
        "violence": "Moderate. Depiction of the furnace as a death sentence, some intensity in scenes of imperial threat. No graphic violence.",
        "language": "None. Clean dialogue throughout.",
        "sexualContent": "None. The film contains no sexual content whatsoever.",
        "drugsAlcohol": "Minimal. Court scenes may show wine in historical context.",
        "intenseScenes": "The furnace sequence is tense. Young children may find the threat of death frightening, but the deliverance is triumphant.",
        "ageRecommendation": "8+. The PG rating fits. This is family-friendly faith entertainment. Parents can use it as a teaching tool for the biblical narrative."
    },
    "spoiler_alert": False,
    "tropeAudit": [
        {
            "id": "TRAD-DANFURN-001",
            "name": "Faith as the Central Organizing Principle",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "The entire film is structured around fidelity to God. The three Hebrews refuse to bow to the idol not out of political rebellion or cultural pride but because their faith forbids it. This is not subtext; it is the text. The film treats religious conviction as the highest virtue and makes no apology for it."
        },
        {
            "id": "TRAD-DANFURN-002",
            "name": "Resistance to State Coercion",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Nebuchadnezzar's demand that all subjects worship the golden image is totalitarian state power demanding ideological conformity. The film frames the three Hebrews' refusal as morally obligatory, not optional. Civil disobedience rooted in religious conscience is the heroic act."
        },
        {
            "id": "TRAD-DANFURN-003",
            "name": "Divine Deliverance as Narrative Climax",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The furnace sequence is the structural and emotional peak. God does not prevent the trial; He enters it. The angel in the fire is the film's most powerful image. Suffering is not meaningless, and deliverance is a divine act, not a human achievement."
        },
        {
            "id": "TRAD-DANFURN-004",
            "name": "Masculine Courage and Brotherhood",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.75,
            "explanation": "Shadrach, Meshach, and Abednego face death together. Their bond is not sentimentalized. It is a bond of shared faith and mutual resolve. The film shows men supporting each other in extremity without deconstructing or undermining their masculinity."
        },
        {
            "id": "TRAD-DANFURN-005",
            "name": "The Humble Servant: Daniel as Advisor",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.75,
            "explanation": "Daniel's role as a wise counselor in a pagan court models faithful engagement with a hostile culture. He serves competently, speaks truth to power, and does not compromise. The film presents integration without assimilation as the ideal."
        },
        {
            "id": "WOKE-DANFURN-001",
            "name": "Imperial Authority as One-Dimensional Villain",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.25,
            "explanation": "The Babylonian authorities serve as functional antagonists. Nebuchadnezzar gets some character shading (his rage, his eventual awe), but the court bureaucracy is flat. This is the expected cost of a faith film with a clear moral universe."
        }
    ],
    "review": "**Hollywood has never known what to do with faith audiences, and that confusion is exactly what makes a film like Daniel and the Fiery Furnace feel so subversive.** It is not subversive in the way Hollywood understands the word. There is no transgression, no deconstruction, no clever revisionist reading of the source material. What makes it subversive is that it takes the biblical text seriously and trusts the story to work on its own terms.\n\nThe film adapts the third chapter of the Book of Daniel: King Nebuchadnezzar builds a ninety-foot golden image and commands every person in Babylon to bow before it on pain of death by furnace. Three Jewish exiles, Shadrach, Meshach, and Abednego, refuse, and are thrown in. They are delivered by divine intervention, and the king acknowledges their God.\n\n**Kevin Downes directs with the workmanlike competence that has become the Kingdom Story Company signature. The budget shows on screen: Babylon feels like a lived-in city rather than a CGI backdrop, and the furnace set piece earns its tension.** Jim Caviezel plays Nebuchadnezzar with an intensity that recalls his work in The Passion of the Christ. He is imperial arrogance given a human face: petulant, dangerous, and ultimately humbled. Mena Massoud's Daniel operates in a lower key, serving as the moral center. He advises the king, advocates for his countrymen, and models what faithful presence in a hostile culture looks like.\n\n**The film's ideological content is exactly what you would expect: zero progressive messaging, a full-throated endorsement of religious liberty, and a conviction that fidelity to God matters more than survival.** The three Hebrews do not argue about pluralism, do not negotiate a compromise, do not explore the validity of other belief systems. They simply say no. The film treats this as heroic.\n\nThat is the important thing to understand about the culture war around faith films: what secular critics call simplistic, millions of believers call true. Daniel and the Fiery Furnace is made for those millions. It does not try to win over the New York Times. It does not embed progressive caveats to make the medicine go down easier. It is, from opening to closing frame, a film that believes what its characters believe.\n\n**For parents, this is the easiest recommendation we can make. There is no sexual content, no profanity, no ideological sucker punch.** The furnace sequence is tense but handled with restraint. Young children will find the threat frightening; the deliverance is triumphant. This is a film you can watch with your family and discuss afterward without having to explain or apologize for anything.\n\n**Final assessment: STRONGLY TRADITIONAL.** Daniel and the Fiery Furnace is not a great film by the standards of 1959's Ben-Hur, but it does not need to be. It is an honest, competent adaptation of a biblical story that respects its source material and its audience. In an industry that treats faith as something to be condescended to or ignored, that refusal to apologize is its own kind of artistic statement.",
    "summary": {
        "overall": "A straightforward biblical adaptation from Kingdom Story Company that takes the Book of Daniel seriously and delivers a clean, competent faith drama. Mena Massoud and Jim Caviezel anchor a film that knows exactly who it is for and does not apologize for it. STRONGLY TRADITIONAL."
    }
})

# === 2. Ben-Hur (1959) ===
reviews.append({
    "id": "ben-hur-1959",
    "slug": "ben-hur-1959",
    "title": "Ben-Hur (1959)",
    "year": 1959,
    "type": "movie",
    "platform": "Theatrical (MGM)",
    "genre": "Epic, Historical Drama, Biblical",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/ben-hur-1959.jpg",
    "releaseDate": "1959-11-18",
    "rating": "G",
    "runtime": "212 min",
    "director": "William Wyler",
    "writers": ["Karl Tunberg", "Gore Vidal (uncredited)", "Christopher Fry (uncredited)"],
    "cast": [
        {"name": "Charlton Heston", "role": "Judah Ben-Hur"},
        {"name": "Stephen Boyd", "role": "Messala"},
        {"name": "Jack Hawkins", "role": "Quintus Arrius"},
        {"name": "Haya Harareet", "role": "Esther"},
        {"name": "Hugh Griffith", "role": "Sheik Ilderim"},
        {"name": "Martha Scott", "role": "Miriam"},
        {"name": "Cathy O'Donnell", "role": "Tirzah"}
    ],
    "studio": "Metro-Goldwyn-Mayer",
    "distributor": "Loew's Inc.",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 0.7,
    "tradScore": 25.2,
    "authIndex": "Very Low",
    "scoreMargin": "+25 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Ben-Hur is what its title promises from the first sequence: a film about a man's journey from privilege through suffering to redemption. Its Christian framework is explicit (Christ appears at critical moments), its values are conservative (family, honor, forgiveness over vengeance), and nothing in the film's 212 minutes contradicts this reading. This is 1950s Hollywood at its most earnest and traditional."
    },
    "seo": {
        "titleTag": "Is Ben-Hur (1959) Woke? Charlton Heston Biblical Epic Scored | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of William Wyler's Ben-Hur (1959). The 11-Oscar epic starring Charlton Heston. Verdict: STRONGLY TRADITIONAL (+25). One of the most traditionally-structured films ever made.",
        "keywords": "is ben-hur woke, ben-hur 1959 review, ben-hur traditional values, charlton heston ben-hur, ben-hur virtuevigil, ben-hur parents guide, biblical epic review"
    },
    "externalScores": {
        "imdb": "8.1",
        "rottenTomatoes": "86%",
        "metacritic": "90"
    },
    "creative_team": {
        "director": "William Wyler",
        "writer": "Karl Tunberg (with uncredited contributions from Gore Vidal and Christopher Fry)",
        "top_cast": [
            "Charlton Heston as Judah Ben-Hur",
            "Stephen Boyd as Messala",
            "Jack Hawkins as Quintus Arrius",
            "Haya Harareet as Esther"
        ],
        "full_cast": ["Charlton Heston", "Stephen Boyd", "Jack Hawkins", "Haya Harareet", "Hugh Griffith", "Martha Scott", "Cathy O'Donnell"],
        "producers": [{"name": "Sam Zimbalist"}],
        "composer": "Miklos Rozsa"
    },
    "parentalGuidance": {
        "violence": "Significant but not graphic by modern standards. The galley battle is brutal; the chariot race is one of the most visceral action sequences ever filmed, with genuine stunt danger. No gore.",
        "language": "None. Clean throughout.",
        "sexualContent": "Minimal. A chaste romance subplot between Judah and Esther. No nudity, no suggestive content.",
        "drugsAlcohol": "Period-appropriate wine consumption in social settings.",
        "intenseScenes": "The galley sequence and the chariot race are intense. The leper colony scenes depicting Miriam and Tirzah may disturb younger viewers. Christ's crucifixion is depicted with restraint and reverence.",
        "ageRecommendation": "10+. The G rating reflects 1959 standards but the film deals with serious themes: betrayal, slavery, revenge, leprosy, and crucifixion. The chariot race alone makes it worth watching with older children and discussing afterward."
    },
    "spoiler_alert": False,
    "tropeAudit": [
        {
            "id": "TRAD-BENHUR-001",
            "name": "Redemption Through Suffering and Faith",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "The film's central arc is Judah's transformation from a man consumed by revenge to one who finds peace through encountering Christ. His mother and sister are healed of leprosy at the crucifixion. The film treats this as literal divine intervention. This is the spiritual core of the film and it is entirely sincere."
        },
        {
            "id": "TRAD-BENHUR-002",
            "name": "Family Loyalty as Sacred Duty",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Judah's entire motivation for the first half of the film is his family: his mother, his sister, and his family name. When Messala imprisons them and seizes the house, Judah's quest for vengeance is driven by filial piety. The film never questions this motivation or frames it as unhealthy. It treats family loyalty as the moral bedrock of a man's character."
        },
        {
            "id": "TRAD-BENHUR-003",
            "name": "Masculine Honor and the Enmity of Equals",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The relationship between Judah and Messala is the film's dramatic engine. It is a study in masculine betrayal: two men who were brothers, divided by pride and empire, whose conflict can only end in one man's destruction. The chariot race is not just an action sequence; it is a duel. The film takes male honor codes seriously as a source of meaning."
        },
        {
            "id": "TRAD-BENHUR-004",
            "name": "Christianity as the Fulfillment of Human Longing",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Christ appears on screen (his face unseen, as was the convention) at three critical moments: giving Judah water during the march to the galleys, at the Sermon on the Mount, and at the crucifixion. Each appearance marks a stage in Judah's moral development. The film presents Christianity not as one valid path among many but as the answer to the human condition."
        },
        {
            "id": "TRAD-BENHUR-005",
            "name": "The Rugged Individualist: Judah's Perseverance",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 2.25,
            "explanation": "Judah survives the galleys through sheer will and physical competence. He earns Quintus Arrius's respect through merit, not luck or favor. The film valorizes endurance, discipline, and the refusal to break. These are classically traditional masculine virtues presented without irony."
        },
        {
            "id": "TRAD-BENHUR-006",
            "name": "The Forgiving Heart: Vengeance Renounced",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.75,
            "explanation": "After defeating Messala in the chariot race, Judah visits the dying man and hears his final words: 'The race is not over.' This hollow victory does not satisfy. The film resolves Judah's arc not through triumph over enemies but through forgiveness, culminating in the healing at the crucifixion. This is a deeply traditional moral resolution."
        },
        {
            "id": "WOKE-BENHUR-001",
            "name": "Roman Imperialism Depicted as Unjust",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "The film is sharply critical of Roman occupation. This could be read as a progressive critique of empire, but it is more accurately a biblical one: earthly power is corrupt and temporary. The film's sympathies are with the Jewish people of occupied Judea, which aligns with both traditional religious values and the literal historical record."
        }
    ],
    "review": "**There is a reason Ben-Hur won eleven Academy Awards, held the record for most Oscars until Titanic, and remains one of the most-watched films in history. It is not subtle, it is not ambiguous, and it is not trying to be either.** William Wyler's epic is a film of absolute moral clarity, and that clarity is what makes it feel so alien to modern audiences raised on irony and deconstruction.\n\nThe story is simple: Judah Ben-Hur (Charlton Heston) is a wealthy Jewish prince in first-century Jerusalem. His childhood friend Messala (Stephen Boyd) returns as a Roman tribune and demands Judah's cooperation in suppressing Jewish unrest. When Judah refuses, Messala imprisons his family and sends Judah to the galleys. Judah survives, returns, and defeats Messala in the chariot race. But his mother and sister have contracted leprosy, and Judah must learn that revenge will not heal what has been broken. His path crosses with a carpenter from Nazareth whose death will change everything.\n\n**Heston was arguably the last American actor who could deliver a line like 'I will live to see this man dead' without a trace of self-consciousness.** He is earnest in a way that modern cinema has pathologized. His Judah Ben-Hur believes what he says. His rage is real, his suffering is real, and his conversion at the foot of the cross is real. The performance has been parodied for decades, but the parodies miss the point: Heston's sincerity is the film's secret weapon. In an age of winking meta-commentary, watching an actor commit this completely is bracing.\n\n**The ideological content is unmistakable.** Ben-Hur is a Christian film wrapped in an adventure epic. The cross appears on screen (Christ's face unseen, in the reverent convention of the era) at three pivotal moments in Judah's journey. Each appearance marks a stage in his transformation from a man of vengeance to a man of faith. The healing of his mother and sister at the crucifixion is presented as literal divine intervention. The film believes this. It expects you to believe it too.\n\nThe chariot race deserves its own paragraph. Shot with real horses, real chariots, and real stuntmen at genuine risk of death, it is perhaps the single greatest action sequence in the history of cinema. No CGI, no safe compromises, no second unit with digital doubles. Just nine minutes of men and animals pushed to their absolute limit. The sequence works at the level of pure spectacle, but it also works dramatically because the race is not about winning a trophy. It is about honor, about the enmity between two men who were once brothers, about whether the man who destroyed your family gets to walk away. Every frame of that sequence carries dramatic weight.\n\n**For parents: Ben-Hur is rated G, which reflects 1959 standards rather than modern classification.** The violence is significant (galleys, chariot crashes, the crucifixion) but there is no gore, no profanity, no sexual content beyond a chaste romance. The film deals with serious themes: betrayal, slavery, revenge, leprosy, and death. Children under ten may find the leper colony scenes frightening. But for families willing to discuss what they have watched, Ben-Hur is one of the richest texts available. It takes faith seriously, honors family loyalty, and shows a man learning that vengeance is a dead end.\n\n**The most telling detail about Ben-Hur's place in the culture is that the 2016 remake removed the Christian content almost entirely and the audience responded by not showing up.** The 1959 original is what it is because it refuses to hedge. It believes that the story of Judah Ben-Hur is ultimately the story of a man meeting God, and that this is the most important thing that can happen to anyone. That conviction, as much as the chariot race, is why the film endures.\n\n**Final assessment: STRONGLY TRADITIONAL.** Ben-Hur is one of the most traditionally structured films in the history of the medium. It takes faith, family, honor, and masculine perseverance seriously and presents them as virtues without caveat. In 1959 this was mainstream entertainment. In 2026 it reads as countercultural.",
    "summary": {
        "overall": "William Wyler's 11-Oscar epic is a film of total moral clarity: a Jewish prince's journey from vengeance to redemption through encounter with Christ. Charlton Heston anchors one of cinema's richest traditional texts. The chariot race remains the greatest action sequence ever filmed. STRONGLY TRADITIONAL."
    }
})

# === 3. Colin from Accounts (2022-2026) ===
reviews.append({
    "id": "colin-from-accounts-2022",
    "slug": "colin-from-accounts-2022",
    "title": "Colin from Accounts (2022)",
    "year": 2022,
    "type": "series",
    "platform": "Binge / Paramount+ / BBC Two",
    "genre": "Romantic Comedy, Dramedy",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "5 min read",
    "poster": "/images/posters/colin-from-accounts-2022.jpg",
    "releaseDate": "2022-12-01",
    "rating": "TV-MA",
    "runtime": "24 episodes (30 min each)",
    "director": "Trent O'Donnell, Madeleine Dyer",
    "writers": ["Harriet Dyer", "Patrick Brammall"],
    "cast": [
        {"name": "Harriet Dyer", "role": "Ashley"},
        {"name": "Patrick Brammall", "role": "Gordon"},
        {"name": "Emma Harvie", "role": "Megan"},
        {"name": "Helen Thomson", "role": "Lynelle"}
    ],
    "studio": "Easy Tiger Productions / CBS Studios",
    "distributor": "Binge / Paramount+",
    "verdict": "BALANCED TRADITIONAL",
    "wokeScore": 1.4,
    "tradScore": 6.3,
    "authIndex": "Low",
    "scoreMargin": "+5 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Colin from Accounts is a relationship dramedy about two flawed adults navigating romance, aging parents, and a disabled dog. It is what it appears to be from the first scene. There is no hidden ideological content, no mid-season turn into political messaging. The show's occasional progressive markers (the gay best friend, the diversity of Sydney's dating scene) are background texture, not platform."
    },
    "seo": {
        "titleTag": "Is Colin from Accounts (2022) Woke? Australian Rom-Com Scored | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Colin from Accounts: the Australian rom-com created by real-life married couple Harriet Dyer and Patrick Brammall. 3 seasons, 24 episodes. Verdict: BALANCED TRADITIONAL (+5). Parental guidance included.",
        "keywords": "is colin from accounts woke, colin from accounts review, colin from accounts virtuevigil, colin from accounts traditional or woke, australian rom com review, colin from accounts parents guide"
    },
    "externalScores": {
        "imdb": "7.9",
        "rottenTomatoes": "100% (S1), 100% (S2), 100% (S3)",
        "metacritic": "N/A"
    },
    "creative_team": {
        "director": "Trent O'Donnell, Madeleine Dyer",
        "writer": "Harriet Dyer, Patrick Brammall (real-life spouses)",
        "top_cast": [
            "Harriet Dyer as Ashley",
            "Patrick Brammall as Gordon",
            "Emma Harvie as Megan",
            "Helen Thomson as Lynelle"
        ],
        "full_cast": ["Harriet Dyer", "Patrick Brammall", "Emma Harvie", "Helen Thomson"],
        "producers": [{"name": "Rob Gibson"}, {"name": "Ian Collie"}, {"name": "Kevin Greene"}],
        "composer": "Matt Blackman"
    },
    "parentalGuidance": {
        "violence": "Minimal. No action sequences. One character is injured in an accident in the first episode.",
        "language": "Strong. Australian profanity throughout, including frequent use of coarse language. This is adult comedy.",
        "sexualContent": "Moderate. Sexual situations are discussed and occasionally depicted but are not graphic. The tone is adult romantic comedy rather than erotic.",
        "drugsAlcohol": "Social drinking in adult contexts. Not a focus.",
        "intenseScenes": "The dog's accident in the pilot is distressing. Themes of infertility, aging parents, and relationship breakdown are handled with emotional weight.",
        "ageRecommendation": "16+. The TV-MA rating is driven by language and adult relationship themes. The show is fundamentally warm and human, but the dialogue is not child-friendly."
    },
    "spoiler_alert": False,
    "tropeAudit": [
        {
            "id": "TRAD-COLIN-001",
            "name": "Committed Romantic Relationship as Central Value",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 2.25,
            "explanation": "The show's entire premise is the development of a committed relationship between two flawed adults. Ashley and Gordon's romance is messy, imperfect, and profoundly human. The series treats finding and keeping love as life's central project. It does not mock monogamy or treat commitment as a trap."
        },
        {
            "id": "TRAD-COLIN-002",
            "name": "Intergenerational Care and Family Obligation",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.75,
            "explanation": "Gordon's relationship with his aging mother is one of the show's emotional pillars. The series treats care for elderly parents as a moral obligation, not a burden to be outsourced. This is handled without sentimentality but with genuine weight."
        },
        {
            "id": "TRAD-COLIN-003",
            "name": "Male Vulnerability and Emotional Growth as Arc",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.5,
            "explanation": "Gordon is not a stereotype. He is a man who struggles with emotional expression but genuinely tries. The show does not punish him for being male or treat his emotional limitations as toxic pathology. His growth arc is about learning to be present for people who need him."
        },
        {
            "id": "TRAD-COLIN-004",
            "name": "The Child as Moral Catalyst",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.75,
            "explanation": "Without spoiling specifics: the prospect of parenthood becomes a significant narrative thread in later seasons. The show treats the desire for children as natural and parenthood as a meaningful life milestone, not a patriarchal imposition."
        },
        {
            "id": "WOKE-COLIN-001",
            "name": "Casual Progressive Background Noise",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "The show includes a gay best friend, the occasional progressive aside, and Sydney's diverse social landscape. These elements are present but not preachy. They function as set decoration rather than sermon. The show's heart is in the central relationship, not in social messaging."
        },
        {
            "id": "WOKE-COLIN-002",
            "name": "Modern Sexual Mores as Unquestioned Default",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "Ashley and Gordon's relationship begins with a sexual encounter between near-strangers. The show treats casual sex and cohabitation as normal adult behavior without moral framing. This is standard for the genre but worth noting for parents considering the show for older teens."
        },
        {
            "id": "WOKE-COLIN-003",
            "name": "Single Motherhood Normalized Without Judgment",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "A secondary character is a single mother. The show presents this as a normal life arrangement without exploring the intentionality or trade-offs involved. This is background normalization rather than advocacy."
        }
    ],
    "review": "**The backstory is almost too good to be true: a married couple writes and stars in a television show about two people who meet because one of them accidentally hits a dog with a car.** Harriet Dyer and Patrick Brammall are both accomplished Australian actors and writers. They created Colin from Accounts together, wrote every episode together, and play the two leads. The result is a romantic comedy that feels genuinely alive in a way few shows in the genre manage.\n\nAshley (Dyer) is crossing a Sydney street when Gordon (Brammall) brakes too late and hits a dog. They take the injured animal to a vet together. The dog survives, they name him Colin, and a relationship begins. That is the setup. What follows across three seasons and twenty-four episodes is a study in how two people who are not especially good at relationships learn to be good at one.\n\n**The show's great strength is that it does not mistake cynicism for sophistication.** Many modern rom-coms feel the need to prove they are above the genre. They wink at the audience, subvert expectations, refuse sentiment. Colin from Accounts does none of this. It is warm. It is sincere. It believes that finding someone and building a life with them matters. When a scene is meant to be moving, the show commits to it without a safety net of irony.\n\nThe ideological content is a mixed bag, but the balance tips traditional. On the woke side: the show assumes casual sex and cohabitation as the normal baseline. There is a gay best friend character who functions as comic relief and confidant. The progressive assumptions of urban Australia are baked into the social fabric of the show. None of this is preachy, but it is present.\n\n**What tips the balance toward traditional is the show's core commitments.** The central romance is treated as life's most important project. Gordon's relationship with his aging mother is handled with moral seriousness: taking care of family is not presented as a burden but as a basic obligation. The prospect of parenthood, when it arrives, is treated as a meaningful life milestone rather than a patriarchal trap. Gordon's growth arc is about learning to be emotionally present and reliable, which the show frames as what a man should be rather than a concession to progressive expectations.\n\n**The fact that Dyer and Brammall are married in real life is not a trivia detail; it is visible on screen.** These two people know each other. The rhythm of their dialogue, the way they fight, the way they reconcile, the way they look at each other in silence: it all carries the texture of actual intimacy. This is not acting-school chemistry. It is the product of two people who share a life writing scenes about what it is like to share a life.\n\n**For parents: this is adult television.** The language is strong, sexual situations are discussed and occasionally depicted, and the themes are relationship- and fertility-focused. It is not appropriate for children under sixteen, but for older teens and adults, it is one of the most genuinely warm shows on streaming. The dog lives, in case you were worried.\n\n**Final assessment: BALANCED TRADITIONAL.** Colin from Accounts earns its traditional lean not through ideology but through emotional sincerity. In a genre that has spent decades proving how above-it-all it is, this show simply believes that love is worth getting right. That counts for more than the occasional progressive aside.",
    "summary": {
        "overall": "The Australian rom-com hit created by real-life married couple Harriet Dyer and Patrick Brammall is warm, sincere, and committed to the idea that building a relationship matters. Casual progressive assumptions are present but the show's emotional core is deeply traditional: family, commitment, and care for those you love. BALANCED TRADITIONAL."
    }
})

# Append to reviews.json
with open(REVIEWS_PATH, 'r') as f:
    data = json.load(f)

for review in reviews:
    data.append(review)

with open(REVIEWS_PATH, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(reviews)} reviews to {REVIEWS_PATH}")
print(f"Total reviews: {len(data)}")
for r in reviews:
    print(f"  - {r['slug']} ({r['verdict']})")