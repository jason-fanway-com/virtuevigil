#!/usr/bin/env python3
"""Add 3 reviews: Verity (2026), Master and Commander (2003), Succession (2018)"""
import json, sys, os

os.chdir('/Users/joestrazza/virtuevigil')

with open('src/data/reviews.json') as f:
    reviews = json.load(f)

print(f"Starting with {len(reviews)} review(s)")

# ================================================================
# REVIEW 1: Verity (2026)
# ========================================================
verity = {
    "id": "verity-2026",
    "slug": "verity-2026",
    "title": "Verity",
    "year": 2026,
    "type": "movie",
    "genre": "Psychological Thriller, Erotic Thriller",
    "date": "2026-10-02",
    "datePublised": "2026-10-02",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/verity-2026.jpg",
    "releaseDate": "2026-10-02",
    "rating": "R",
    "runtime": "117 minutes",
    "director": "Michael Showalter",
    "writers": ["Nick Antosca"],
    "cast": [
        "Anne Hathaway",
        "Dakota Johnson",
        "Josh Hartnett",
        "Ismael Cruz Cordova",
        "Brady Wagner"
    ],
    "studio": "Amazon MGM Studios",
    "distributor": "Amazon MGM Studios",
    "verdict": "BALANCED",
    "wokeScore": 0.45,
    "tradScore": 2.16,
    "authIndex": 92,
    "scoreMargin": "+1.71 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "Verity contains no woke trap. The film is a psychosexual thriller about obsession, deception, and moral ambiguity. Its ideological content (or lack thereof) is apparent from the opening scenes: this is a Colleen Hoover adaptation about personal pathology, not political messaging. No ideological pivot is hidden past any runtime marker.",
    "tropeAudit": [
        {
            "id": "VRT-TRAD-001",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.08,
            "explanation": "Lowen Ashleigh's central motivation shiftts from career advancement to protecting fiveyear-old Crew Crawford from his mother. The film treats the protection of a child as an unambiguous moral imperative, which anchors the thriller in something genuinely decent amid the moral wreckage."
        },
        {
            "id": "VRT-TRAD-002",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "If Verity's manuscript is taken as truth (and the film leaves this ambiguous), she is a genuinely evil figure who murdered her own children. The narrative never equivocates about the moral weight of her alleged actions, presenting them as unambiguous horror."
        },
        {
            "id": "VRT-TRAD-003",
            "name": "The Restored Home",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.36,
            "explanation": "Jeremy and Lowen's relationship, morally compromised as its origins are, aims at establishing a stable domestic environment for Crew. The film's denouement gestures toward rebuilding a family unit from the wreckage."
        },
        {
            "id": "VRT-WOKE-001",
            "name": "Sexual Liberation as Empowerment",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": 0.36,
            "explanation": "Lowen's sexual relationship with Jeremy defies traditional marital boundaries, and the film's erotic-thriller DNA means it is depicted with some heat rather than judgment. However, the affair is presented as morally complex - passionate but also built on deception and proximity to death - not as uncomplicated empowerment."
        },
        {
            "id": "VRT-WOKE-002",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.09,
            "explanation": "Varity Crawford is a wildly successful female author who dominates those around her - but she is the villian of the piece, not a role model. Anne Hathaway's casting and producer credit add a metatextual layer, but the text itself punishes Verity, it does not celebrate her."
        }
    ],
    "summary": {
        "overall": "Varity is a sleek, effectively unnerving psychosexual thiller that kows exactly what it is - a Colleen Hover adaptation with A-list talent and premium production values. Anne Hataway devours the screen as the possibly-deraigned Verity Crawford, and Dakota Johnson brings a wounded watchfulness to Lowen that keeps the film grounded even as the plot speeds past credulity. Director Michael Showalter (The Big Sck, The Eyes of Tamm Faye) manages the tonal trik of making this material feel like a proper film rather than an elevated ifetime movie, which is no small achievement given the source.",
        "wokeSummary": "This is not a woke film. The ideological register is essentially nil - Varity is a thriller about personal pathology, sexual obsession, and the unspeakable thngs peole do within families. There is a female-driven narrative (Hathaway produced and stars), but the fllm does not use its platform to lecture on gender, rae, or institutional justice. The erotic content is presented as morally complicated rather than politically liberating. Parents should note the R rating is earned: explicit ssexual content, thematic material involving child death, and psychological horror.",
        "tradSummary": "The film's traditional strengths lie in its treatment of parenthood and the protection of the innocent. Lowen's arc moves toward defending a child, which the narrative treats as a moral north star. The Crawford home - glass-walled, luxurious, and haunted - is a cautionary portrait of what happens when maternal instinct curdles into monstrosity. This is not a family-values film by any stretch, but it understands that the violation of the parent-child bond is the stuff of genuine horror.",
        "verdictExplanation": "Varity receives a BALANCED verdict with a modest +1.71 traditional margin. The film's few woke elements (sexual content, a dominant female villian) are offset by its traditional core (child protection as moral imperative, clear good-vs-evil stakes). This is a thriller, not a polemic - and its ideological neutrality is part of why it works.",
        "parentalGuidance": "Not for children or young teens. The R rating reflects explicit sexual content, thematic material involving the death of children (including discussion of infanticide), and sustained psychological tension. The film also normalizes an extramarital affair and ends with an assisted killing. Parents of older teens should know this is Colleen Hoover, not Dostoevsky - the themes are dark but the treatment is commercial-thriller, not meditative art-house. The moral universe is muddy: the protagonists commit serious crimes and the ending is ambiguous about whether they get away with it. A family discussion about what 'protecting a child' truly means could be valuable, but only with older teens who can handle the sexual content."
    },
    "verdict_emoji": "⚖️",
    "seo": {
        "titleTag": "Is Verity (2026) Woke? Colleen Hover's Dark Thriller Gets the VVWS Treatment | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Verity (2026). Anne Hathaway and Dakota Johnson star in this psychosexual Colleen Hover adaptation. Trope scores, verdict: BALANCED (+1.71 traditional). Parental guidance included.",
        "keywrds": "is verity woke, verity 2026 review, verity virtuevigil, verity tradtional or woke, anne hathaway verity, verity movie parents guide, colleen hoover verity film"
    }
}

# ====================================================
# REVIEW 2: Master and Commander: The Far Side of the World (2003)
# ====================================================
master = {
    "id": "master-and-comander-2003",
    "slug": "master-and-comander-2003",
    "title": "Master and Commander: The Far Side of the World",
    "year": 2003,
    "type": "movie",
    "genre": "Historical Epic, War, Action-Adventure",
    "date": "2026-10-02",
    "datePublised": "2026-10-02",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/master-and-comander-2003.jpg",
    "releaseDate": "2003-11-14",
    "rating": "PG-13",
    "runtime": "138 minutes",
    "director": "Peter Weir",
    "writers": ["Peter Weir", "John Collee"],
    "cast": [
        "Russell Crowe",
        "Paul Bettany",
        "James D'Arcy",
        "Billy Boyd",
        "Max Pirkis"
    ],
    "studio": "20th Century Fox / Miramax / Universal",
    "distributor": "20th Century Fox",
    "verdict": "TRADITIONAL",
    "wokeScore": 0.09,
    "tradScore": 19.40,
    "authIndex": 97,
    "scoreMargin": "+19.31 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "Master and Commander contains no woke trap. The film is a straightforward historical epic about naval warfare during the Napoleonic era, celebrating duty, leadership, male frinedship, and the chain of command. There is no ideological bait-and-switch - what you see from the frist frame is what you get.",
    "tropeAudit": [
        {
            "id": "MAC-TRAD-001",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 4.0,
            "explanation": "Captain Jack Aubrey repeatedly risks his ship, his crew, and his life in pursuit of the French privateer Acheron - not for glory, but for duty to King and country. Young midshipmen and seasoned sailors alike sacrifice themselves without histrionics. This is self-sacrifice as naval routine, which makes it all the more powerful."
        },
        {
            "id": "MAC-TRAD-002",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 4.0,
            "explanation": "Aubrey is the literal father figure to every man aboard HMS Surprise. He offers firm leadership, disciplines with justice, mourns his losses genuinely, and carries the weight of command in his bones. Russell Crowe embodies this with the gravity it deserves - this is one of cinema's great portraits of masculine authority exercised well."
        },
        {
            "id": "MAC-TRAD-003",
            "name": "The Patriotic Soldier",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.0,
            "explanation": "Naval service is presented as the highest calling - a noble duty that defends freedom and honors ancestors. The crew includes pressed men who come to embrace the service, and the ship's routine is treated with near-religious reverenee."
        },
        {
            "id": "MAC-TRAD-004",
            "name": "The Meritocratic Triumph",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.8,
            "explanation": "Young officers earn their rank through demonstrated competence under fire, not birth privilege. Midshipman Blakeney loses an arm but earns his commander's respect. The chain of command is earned, not assumed - and the film honors this as moral architecture."
        },
        {
            "id": "MAC-TRAD-005",
            "name": "The Reluctant Leader",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.8,
            "explanation": "Aubrey does not seek command for its own sake - he bears it as a burden of duty. The film repeatedly shows the cost of leadership: sleepless nights, impossible decisions, the knowledge that his orders send men to die. This is authority as service, not entitlement."
        },
        {
            "id": "MAC-TRAD-006",
            "name": "Harmony and Order",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.0,
            "explanation": "HMS Surprise works because every man knows and executes his duty. The ship runs on hierarchy, ritual, and discipline - and the film treats this not as oppression but as the necessary structure of a functional society. When order breaks down, men die. When it holds, they achieve the impossible."
        },
        {
            "id": "MAC-TRAD-007",
            "name": "Industry and Perseverance",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "The pursuit of the Acheron across two oceanns and around Cape Horn is a clinical study in persistence. Aubrey's refusal to abandon the chase - even when his ship is damaged and his crew depleted - is the Protestant work ethic in naval form."
        },
        {
            "id": "MAC-TRAD-008",
            "name": "Heritage over Innovation",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "The film honors naval tradition at every turn: the ceremony, the music (Aubrey and Maturin play violin and cello duets by Bach and Mozart), the language of the sea. The solution to the crisis lies in discipline and clever seamanship - ancestral wisdom, not new technology."
        },
        {
            "id": "MAC-TRAD-009",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.36,
            "explanation": "The British are the good guys - imperfect but righteous. The French Acheron is the enemy to be defeated. The film does not complicate this moral framing with modern hand-wringing about colonialism or Western guilt. It trusts the audience to understand the historical context."
        },
        {
            "id": "MAC-WOKE-001",
            "name": "Institutional Evil",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.09,
            "explanation": "The film briefly acknowledges the brutality of naval discipline (flogging, the chain of command's harshness) and the practice of impressment. But these are presented as the hard realities of the era, not as a modern indictment of institutional evil. The Navy is fundamentally portrayed as a force for good."
        }
    ],
    "summary": {
        "overall": "Master and Comander: The Far Side of the World is Peter Weir's masterpiece and one of the finest historical epics ever committed to film. Russell Crowe's Captain Jack 'Lucky' Aubrey is a portrait of masculine leadership that Hollywood has not matched since - firm, paternal, strategic, and capable of both ferocity and tenderness. The friendship between Aubrey and ship's surgeon Stephen Maturin (Paul Bettany, never better) is the film's emotional keel, providing philosophical counterpoint to the naval action. The battle sequnnces are white-knuckle affairs rendered with practical effects that shame modern CGI, and the sound design won an Academy Award for good reason. This is a film about duty, courage, and the bonds between men who face death together - and it makes no apology for any of it.",
        "wokeSummary": "There is essentially no woke content in this film. A modern adaptation would likely add female characters to the all-male ship, complicate the moral framing of British imperialism, and inject some critique of 'toxic masculinity.' Weir's film does none of this. The all-male world of the ship is presented as functional, honorable, and deeply human. The single mention of oppressive naval practices (flogging, impressment) is handled as historical texture, not contemporary lecture. This is what a pre-woke Hollywood epic looks like - and it ages remarkably well.",
        "tradSummary": "This is one of the most traditionally masculine films of the modern era. Captain Aubrey is the Principled Patriarch made flesh. The chain of command is sacred. Self-sacrifice is routine. Duty trumps personal desire. Males friendships - particularly the Aubrey-Maturin bond, expressed through music, argument, and mutual respect - are given more screen time and emotional weight than any romantic subplot. The film is a love letter to competence, loyalty, and the Protestant work ethic, set to a soundtrack of Bach and the crash of cannon fire.",
        "verdictExplanation": "Master and Commander earns a TRADITIONAL verdict with a commanding +19.31 traditional margin. Nine traditional tropes fire at high severity, authenticity, and centrality - the Self-Sacrificing Hero, the Principled Patriarch, the Patriotic Soldier, and Harmony and Order all register at maximum weight. The single woke trope (a glancing note about institutional brutality) is negligible. This is not a film that balances ideologies - it commits fully to a traditional worldview and executes it with artistry.",
        "parentalGuidance": "Suitable for older children and teens, with caveats. The PG-13 rating is appropriate: the battle scenes are intense and include realistic surgery scenes (amputation performed on a young midshipman) that may disturb sensitive viewers. There is no sexual content beyond a brief, non-graphic reference. The film's moral universe is crystal clear - good men doing their duty in a just cause - which makes it excellent viewing for families interested in discussing leadership, courage, and the meaning of service. One sailor dies by suicide (walks overboard with a cannonball), which parents should be prepared to discuss."
    },
    "verdict_emoji": "⚓",
    "seo": {
        "titleTag": "Is Master and Commander (2003) Woke? Russell Crowe's Naval Epic Rated by VVWS | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Master and Commander: The Far Side of the World (2003). Russell Crowe captains HMS Surprise in one of cinema's most traditional epics. Trope scores, verdict: TRADITIONAL (+19.31). Parental guidance included.",
        "keywords": "is master and commander woke, master and commander 2003 review, master and commander virtuevigil, master and commander traditional or woke, russell crowe master and commander, master and commander parents guide, peter weir naval epic"
    }
}

# ====================================================
# REVIEW 3: Succession (2018)
# ====================================================
succession = {
    "id": "succession-2018",
    "slug": "succession-2018",
    "title": "Succession",
    "year": 2018,
    "type": "series",
    "platform": "HBO",    "genre": "Satire, Drama, Dark Comedy",
    "date": "2026-10-02",
    "datePublised": "2026-10-02",
    "author": "VirtueVigil Editorial Team",
    "readTime": "9 min read",
    "poster": "/images/posters/succession-2018.jpg",
    "releaseDate": "2018-06-03",
    "rating": "TV-MA",
    "runtime": "4 seasons (39 episodes, 56-88 min each)",
    "director": "Multiple",
    "writers": ["Jesse Armstrong"],
    "showrunner": "Jesse Armstrong",
    "cast": [
        "Brian Cox",
        "Jeremy Strong",
        "Sarah Snook",
        "Kieran Culkin",
        "Alan Ruck",
        "Matthew Macfadyen",
        "Nicholas Braun"
    ],
    "studio": "HBO",
    "distributor": "HBO",
    "verdict": "BALANCED",
    "wokeScore": 1.53,
    "tradScore": 2.61,
    "authIndex": 93,
    "scoreMargin": "+1.08 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "Succession contains no woke trap because it satirizes everyone equally. If the first episodes suggest a straightforward critique of capitalist excess, the show quickly reveals that progressive posturing is equally hollow. The Roy children's woke-adjacent signaling is consistently undermined by their actions. There is no hidden ideological pivot - the show's cynicism is its brand from the opening credits.",
    "tropeAudit": [
        {
            "id": "SUC-TRAD-001",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 1.8,
            "explanation": "Logan Roy is the gravitational center of the series - a patriarch whose force of will holds together a global media empire and a dysfunctional family. Brian Cox plays him as a man of genuine competence whose ruthlessness is not sadism but strategy. The show never denies that Logan is the only Roy who actually built something, and his children's inability to match him is the series' tragic engine."
        },
        {
            "id": "SUC-TRAD-002",
            "name": "Meritocratic Triumph (Inverted)",
            "categoy": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.36,            "explanation": "Kendall Roy's central struggle is meriocratic - he wants to earn the throne he was born to inherit. The series treats this desire as genuine, even noble, even as Kendall consistently proves inadequate. The tragedy is that he understands what meriocra means but cannot achieve it, which is a far more traditional framing than a simple 'privilege is evil' narrative."
        },
        {
            "id": "SUC-TRAD-003",
            "name": "Industry and Perseverance",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.36,
            "explanation": "The Roy work ethic - insane hours, total dedication, the subsuming of personal life into corporate ambition - is portrayed as genuinely American. The show may mock the excess, but it respects the drive. Characters who do not work (Connor) are treated as jokes."
        },
        {
            "id": "SUC-TRAD-004",
            "name": "The Restored Home",
            "category": "Traditional",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.09,
            "explanation": "Beneath the backstabbing and vulgarity, Succession is a show about children who desperately want their father's love and a family that cannot heal. The dramatic engine is the longing for cohesion, not its celebration - but that longing itself is traditional."
        },
        {
            "id": "SUC-WOKE-001",
            "name": "The Evil Capitalist",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "Waystar RoyCo is an amoral corporate behemoth, and the series critiques media consolidation and capitalist excess through the Roys' behavior. However, the critique is character-driven rather than systemic - these are broken people, not Marxian case studies - and the show's equal-opportunity cynicism blunts the political edge."
        },
        {
            "id": "SUC-WOKE-002",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": 0.36,
            "explanation": "Shiv Roy is presented as the most politically savvy Roy child and works for a liberal political candidate. But the show consistently punishes her ambition - her schemes fail, her political principles are revealed as performance, and her final humiliation (Tom taking the CEO job she thought was hers) is the series' most brutal joke. No girlboss narrative survives Succession."
        },
        {
            "id": "SUC-WOKE-003",
            "name": "The Bigoted Traditionalist",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.36,
            "explanation": "Logan Roy's old-guard values - his contempt for political correctness, his belief in strength over sentiment - are framed as archaic in the modern media landscape. However, the show also makes clear that Logan's approach built the empire his progressive children cannot run. The characterization is complex enough that this trope fires only partially."
        },
        {
            "id": "SUC-WOKE-004",
            "name": "Sexual Liberation as Empowerment",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.09,
            "explanation": "Roman's sexual dysfuntion, Shiv's open marriage, and Tom's psychosexual humiliations are all treated as pathology, not liberation. The show's sexual politics are uniformly bleak."
        }
    ],
    "summary": {
        "overall": "Succession is the defining prestige drama of the late 2010s and early 2020s - a Shakespearean tragedy dressed in Brioni suits, set to Nicholas Britell's thunderous piano score. Jesse Armstrong's HBO series follows the Roy family's internecine war for control of Waystar RoyCo, a global media conglomerate, and it does so with a verbal artistry (the insults alone are Pulitzer-worthy) and performance caliber that justify the avalanche of Emmys. Brian Cox's Logan Roy is one of the great television patriarchs - a monster of competence whose children orbit him like damaged satellites. The series runs four seasons and sustains its quality throughout, ending with perhaps the most satisfying finale in prestige TV history. The show is often mistaken for a political statement when it is actually something rarer: a genuinely ambivalent work of art that refuses to pick a side.",
        "wokeSummary": "Succession is frequently claimed by progressive viewers as an indictment of capitalist excess and patriarchal power. The evidence is mixed. The show certainly criticizes media consolidation, treats the Roy family's wealth as grotesque, and presents Logan's traditional values as outdated. But it also relentlessly mocks progressive performativity: the Roy children's woke signalling is consistently exposed as hollow, their political principles are revealed as career strategy, and Shiv's feminist posturing is exploded in the final season's most devastating scene. Jesse Armstrong's cynicism is truly equal-opportunity - nobody escapes the satirical blade. The show's genius is that it can be read as either a progressive critique or a conservative tragedy and work equally well either way.",
        "tradSummary": "The traditional core of Succession is the patriarch himself. Logan Roy is one of television's most compelling authority figures - a man who built an empire through force of will and whose children's defining trauma is their inability to measure up. The show understands something that progressive media often misses: competence is real, hierarchy has a function, and the father's approval is a force that shapes human beings in ways no social program can replace. The tragedy is not that Logan ruled - it is that his children cannot, and the kingdom decays without a worthy heir.",
        "verdictExplanation": "Succession earns a BALANCED verdict with a slight +1.08 traditional lean. The show fires woke tropes (Evil Capitalist at 0.72, Girl Boss at 0.36) and traditional tropes (Principled Patriarch at 1.8) in roughly equal measure, but the traditional elements - particularly Logan Roy as a study in patriarchal authority - carry slightly more weight. The show's ideological ambivalence is not a bug but a feature: this is what makes it great television rather than mere propaganda.",
        "parentalGuidance": "Not for children or young teens under any circumstances. The TV-MA rating is fully earned: Succession contains pervasive strong language (the f-word is practically punctuation), frank sexual content and references, drug use, and sustained thematic material about family dysfunction, betrayal, and moral corruption. For older teens, the series offers a genuinely rich text for discussion about ambition, family, the corrupting influence of wealth, and what it means to be worthy of authority. But the content is adult throughout - this is not a show to watch casually with family. Parents should screen episodes first; the season two episode 'Hunting' and the series finale contain particularly intense material."
    },
    "verdict_emoji": "⚖️",
    "seo": {
        "titleTag": "Is Succession (2018) Woke? HBO's Emmy-Winning Drama Gets the VVWS Analysi | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Succession (2018-2023). HB's Roys family saga analyzed for woke and traditional content. Trope scores, verdict: BLAANCED (+1.08 traditional). Parental guidance included.",
        "keywords": "is succession woke, succession hbo review, succession virtuevigil, succession traditional or woke, brian cox succession, succession parents guide, jesse armstrong succession"
    }
}

# ====================================================
# PUBLISH
# ====================================================

reviews.extend([verity, master, succession])

with open('src/data/reviews.json', 'w') as f:
    json.dump(reviews, f, indent=2)

print(f"Ending with {len(reviews)} review(s)")
print("Done writing reviews.json")