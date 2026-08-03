#!/usr/bin/env python3
"""Append 3 reviews to reviews.json, then build, commit, push, and IndexNow ping."""
import json, subprocess, sys, os

REVIEWS_FILE = "src/data/reviews.json"

# Load existing
with open(REVIEWS_FILE) as f:
    reviews = json.load(f)

existing_slugs = {r["slug"] for r in reviews}
print(f"Loaded {len(reviews)} reviews. Checking slugs...")

for slug in ["seventy-two-hours-2026", "the-wizard-of-oz-1939", "batman-caped-crusader-s2-2026"]:
    if slug in existing_slugs:
        print(f"ERROR: slug '{slug}' already exists in reviews.json!")
        sys.exit(1)
print("All slugs are clear.")

# ============================================================
# REVIEW #1: 72 Hours (2026)
# ============================================================
review1 = {
    "id": "seventy-two-hours-2026",
    "slug": "seventy-two-hours-2026",
    "title": "72 Hours",
    "year": 2026,
    "type": "film",
    "platform": "Netflix",
    "genre": "Comedy",
    "date": "2026-08-03",
    "datePublished": "2026-08-03",
    "author": "VirtueVigil Editorial Team",
    "readTime": "6 min read",
    "poster": "",
    "releaseDate": "2026-07-24",
    "rating": "R",
    "runtime": "105 min",
    "director": "Tim Story",
    "writers": ["Jon Hurwitz", "Hayden Schlossberg", "Kevin Burrows", "Matt Mider"],
    "cast": [
        "Kevin Hart as Joe",
        "Marcello Hernandez",
        "Mason Gooding",
        "Kam Patterson",
        "Ben Marshall",
        "Teyana Taylor"
    ],
    "studio": "Sony Pictures / Davis Entertainment / Hartbeat Productions",
    "distributor": "Netflix",
    "verdict": "MIXED",
    "wokeScore": 8.4,
    "tradScore": 8.1,
    "authIndex": 0,
    "scoreMargin": "-0.3 WOKE",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Not a woke trap. The midlife crisis premise and Kevin Hart's immaturity is visible from the opening scenes. Joe is passed over for promotion and the bachelor-party setup is established in the first act. No hidden ideological payload."
    },
    "seoTitle": "Is 72 Hours (2026) Woke? Kevin Hart's Netflix Midlife Crisis Comedy | VirtueVigil",
    "seoDescription": "VirtueVigil reviews 72 Hours (2026) starring Kevin Hart. A 40-year-old crashes a bachelor party in Miami. Full VVWS trope audit, parental guidance. Verdict: MIXED (-0.3).",
    "seoKeywords": [
        "is 72 Hours 2026 woke",
        "72 Hours Kevin Hart review",
        "72 Hours Netflix comedy",
        "Kevin Hart new movie 2026",
        "72 Hours parents guide",
        "72 Hours appropriate for kids",
        "72 Hours conservative review",
        "72 Hours VirtueVigil score",
        "Tim Story 72 Hours",
        "Kevin Hart bachelor party movie",
        "72 Hours 2026 rating",
        "72 Hours woke or traditional"
    ],
    "externalScores": {
        "rottenTomatoesCritic": 16,
        "rottenTomatoesAudience": "N/A",
        "imdb": "N/A",
        "metacritic": 41,
        "budget": "Not disclosed",
        "globalBoxOffice": "N/A (streaming)"
    },
    "creative_team": {
        "director": {
            "name": "Tim Story",
            "ideology": "CENTER. Story is a commercial filmmaker whose career spans the Ride Along franchise, the 2005 Fantastic Four, and Barbershop. He does not make films with discernible ideological intent. His movies are designed for mainstream audiences and he has worked comfortably with Kevin Hart across multiple projects. No political profile to analyze.",
            "profile": "Tim Story has directed Kevin Hart in multiple projects including the Ride Along franchise and Think Like a Man. He is a reliable commercial director who delivers what studios ask for. His career reflects mainstream Hollywood comedy sensibilities rather than any political or ideological agenda. He recently directed The Pickup for Amazon MGM."
        },
        "writers": {
            "names": "Jon Hurwitz, Hayden Schlossberg, Kevin Burrows, Matt Mider",
            "profile": "Hurwitz and Schlossberg created the Harold and Kumar franchise and wrote American Reunion. Their comedy is raunchy but not politically motivated. Kevin Burrows and Matt Mider previously wrote The Package for Netflix, another R-rated comedy. The writing team's pedigree is in party comedies and broad humor, not ideological messaging."
        },
        "lead_producer": {
            "name": "Kevin Hart, John Cheng",
            "company": "Hartbeat Productions / Davis Entertainment / Sony Pictures"
        },
        "top_cast": [
            {"name": "Kevin Hart", "role": "Joe"},
            {"name": "Marcello Hernandez", "role": "Bachelor party member"},
            {"name": "Mason Gooding", "role": "Bachelor party member"},
            {"name": "Kam Patterson", "role": "Bachelor party member"},
            {"name": "Ben Marshall", "role": "Bachelor party member"},
            {"name": "Teyana Taylor", "role": "Girlfriend"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "R",
        "mpaaDescriptors": "Strong crude sexual content, drug use, pervasive language, alcohol abuse",
        "recommendedAge": "17+",
        "contentWarnings": [
            "Extensive drug use throughout the Miami party sequences",
            "Heavy drinking and alcohol abuse played for comedy",
            "Crude sexual humor and references throughout",
            "Pervasive strong language",
            "Thematic elements involving relationship breakdown and infidelity",
            "Depictions of reckless and dangerous party behavior"
        ],
        "parentalNotes": "72 Hours is a hard-R raunchy comedy in the tradition of The Hangover. The drug use is extensive and played for laughs. The film's moral arc -- a 40-year-old abandoning his relationship to party with strangers -- sends mixed messages that younger viewers may have difficulty parsing. The ending does restore some traditional values around commitment, but the journey there involves behavior that parents will want to discuss. Strictly for mature audiences."
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "72 Hours is a Netflix comedy that feels like it was assembled from leftover parts in the streaming factory. Kevin Hart stars as Joe, a 40-year-old advertising specialist who discovers he has been passed over for a promotion because management considers him 'too old.' On the same day, a stranger's bachelor party group chat accidentally adds him. Joe decides the universe is sending him a message: reclaim his youth by crashing a Miami weekend with twentysomethings he has never met.\n\nThe premise has the bones of a midlife crisis comedy with genuine potential. Joe books a lavish Airbnb. His longtime girlfriend, a doctor, mistakes his pre-trip jitters for an imminent proposal. When he kneels -- to tie a shoe, not to propose -- and tells her marriage is not a priority, she leaves and blocks his calls. Joe boards the plane anyway. What follows is drugs, drinking, and chaos.\n\nKevin Hart does what Kevin Hart does: he is small and loud and increasingly panicked as situations spiral. His comedic rhythm is precise and professional. The younger cast provides competent support, particularly Marcello Hernandez as the most chaotic member of the bachelor crew. Teyana Taylor as the girlfriend is given almost nothing to do beyond looking disappointed, which she does well.\n\nThe film operates in the shadow of The Hangover without approaching its anarchic invention. Tim Story's direction is competent but anonymous. The script from four credited writers -- Hurwitz, Schlossberg, Burrows, and Mider -- has the patchwork feel of a project that went through too many drafts without a unifying comic vision.\n\nThe arc lands where you expect: Joe realizes that chasing his twenties was a mistake, that his girlfriend represents genuine value, and that maturity is not a prison sentence. The film wants to have its raunchy cake and its moral redemption too. Whether it earns either is debatable. The traditional elements are present but never fully committed to, and the woke framing around workplace ageism and commitment avoidance feels more like accidental topicality than deliberate messaging.\n\nUnder VVWS methodology, the scores essentially cancel out. The film bounces between immature excess and last-reel moralizing without fully committing to either value system. The result is a comedy that is neither offensive enough to be memorable nor moral enough to be meaningful."
    },
    "tropeAudit": [
        {
            "id": "WOKE-002",
            "name": "Bumbling Patriarch",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 5.4,
            "description": "Joe is a 40-year-old man who refuses commitment, parties recklessly with twentysomethings, and is portrayed as fundamentally immature. His professional competence is undercut by his personal chaos. The film positions adult male responsibility as something to escape from."
        },
        {
            "id": "WOKE-022",
            "name": "Sexual Liberation as Empowerment",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "description": "The rejection of marriage and commitment is initially framed as the path to reclaiming youth and vitality. Joe's decision to prioritize the party weekend over his relationship is presented as liberation before the film eventually walks it back."
        },
        {
            "id": "WOKE-001",
            "name": "General Woke Element -- Ageism as Systemic Barrier",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.0,
            "description": "Joe's workplace passes him over for promotion explicitly because he is 'too old' at 40. This functions as a systemic-ageism plot point that kicks off the narrative, though it recedes in importance as the party chaos takes over."
        },
        {
            "id": "TRADITIONAL-027",
            "name": "Redemptive Arcs",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 5.4,
            "description": "Joe's journey ultimately involves realizing that maturity and commitment have more value than reckless youth. The film ends with him attempting to repair his relationship and accepting that being 40 is not a death sentence but a different stage of life."
        },
        {
            "id": "TRADITIONAL-041",
            "name": "Industry and Perseverance",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "Joe is established as a hardworking advertising specialist who has put in years at his company. His professional life, while the source of his initial crisis, shows genuine dedication and competence."
        },
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "description": "The character arc moves Joe toward accepting adult responsibility. By the film's end, he recognizes that the party lifestyle is empty and that his relationship has real value. The arc toward principled adulthood is the film's central traditional element."
        }
    ],
    "seo": {
        "titleTag": "Is 72 Hours (2026) Woke? Kevin Hart's Netflix Midlife Crisis Comedy | VirtueVigil",
        "metaDescription": "VirtueVigil reviews 72 Hours (2026) starring Kevin Hart. A 40-year-old crashes a stranger's bachelor party in Miami. Full VVWS trope audit, creative team ideology, parental guidance. Verdict: MIXED (-0.3).",
        "keywords": "is 72 Hours 2026 woke, 72 Hours Kevin Hart review, 72 Hours Netflix comedy parents guide, Kevin Hart new movie 2026, 72 Hours appropriate for kids, 72 Hours conservative review, 72 Hours VirtueVigil"
    }
}

# ============================================================
# REVIEW #2: The Wizard of Oz (1939)
# ============================================================
review2 = {
    "id": "the-wizard-of-oz-1939",
    "slug": "the-wizard-of-oz-1939",
    "title": "The Wizard of Oz",
    "year": 1939,
    "type": "film",
    "platform": "Various / Max",
    "genre": "Musical / Fantasy / Adventure",
    "date": "2026-08-03",
    "datePublished": "2026-08-03",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "",
    "releaseDate": "1939-08-25",
    "rating": "G",
    "runtime": "102 min",
    "director": "Victor Fleming",
    "writers": ["Noel Langley", "Florence Ryerson", "Edgar Allan Woolf"],
    "cast": [
        "Judy Garland as Dorothy Gale",
        "Frank Morgan as Professor Marvel / The Wizard",
        "Ray Bolger as Hunk / Scarecrow",
        "Bert Lahr as Zeke / Cowardly Lion",
        "Jack Haley as Hickory / Tin Man",
        "Billie Burke as Glinda the Good Witch",
        "Margaret Hamilton as Miss Gulch / Wicked Witch of the West"
    ],
    "studio": "Metro-Goldwyn-Mayer (MGM)",
    "distributor": "MGM / Warner Bros.",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 0.7,
    "tradScore": 24.72,
    "authIndex": 0,
    "scoreMargin": "+24 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Not a woke trap. The film's traditional values -- home, family, courage, friendship -- are visible from the opening sepia Kansas sequence. There is no hidden ideological payload. The female protagonist leads an adventure but does so in an organically traditional way without Girl Boss framing."
    },
    "seoTitle": "Is The Wizard of Oz (1939) Woke? The Classic's Traditional Values | VirtueVigil",
    "seoDescription": "VirtueVigil scores The Wizard of Oz (1939). Judy Garland, the yellow brick road, and 'there's no place like home.' Full VVWS trope audit. Verdict: STRONGLY TRADITIONAL (+24).",
    "seoKeywords": [
        "is The Wizard of Oz woke",
        "Wizard of Oz traditional values",
        "Wizard of Oz 1939 review",
        "Wizard of Oz conservative review",
        "Wizard of Oz parents guide",
        "is Wizard of Oz appropriate for children",
        "Wizard of Oz VirtueVigil score",
        "Judy Garland Wizard of Oz",
        "Wizard of Oz family values",
        "Wizard of Oz moral lessons",
        "there's no place like home meaning",
        "Wizard of Oz traditional or woke"
    ],
    "externalScores": {
        "rottenTomatoesCritic": 98,
        "rottenTomatoesAudience": 89,
        "imdb": 8.1,
        "metacritic": 92,
        "oscarNominations": 6,
        "oscarCategories": "Best Picture, Best Original Score (WON), Best Original Song 'Over the Rainbow' (WON), Best Art Direction, Best Cinematography (Color), Best Special Effects",
        "budget": "$2.8 million (1939)",
        "globalBoxOffice": "$33.6 million (including re-releases)"
    },
    "creative_team": {
        "director": {
            "name": "Victor Fleming (primary); King Vidor, George Cukor, Richard Thorpe (uncredited)",
            "ideology": "TRADITIONAL. Fleming directed both The Wizard of Oz and Gone with the Wind in the same year (1939). His films embody the classical Hollywood tradition: clear moral stakes, earned character arcs, and a worldview in which home, family, and personal courage are the highest virtues. Fleming's cinema is pre-ideological in the contemporary sense -- these films were made before Hollywood developed its explicit political consciousness.",
            "profile": "Victor Fleming was a top MGM contract director who replaced Richard Thorpe and George Cukor on The Wizard of Oz. He shot the majority of the film before being pulled away to salvage Gone with the Wind. King Vidor directed the sepia Kansas sequences. Fleming's career included Captains Courageous, Dr. Jekyll and Mr. Hyde, and Joan of Arc. He was a craftsman, not an auteur, but his films consistently affirmed traditional American values."
        },
        "writers": {
            "names": "Noel Langley, Florence Ryerson, Edgar Allan Woolf (screenplay); L. Frank Baum (novel)",
            "profile": "The screenplay adapted L. Frank Baum's 1900 novel The Wonderful Wizard of Oz, which Baum wrote as a modern American fairy tale. The screenwriters made significant changes -- the ruby slippers were silver in the book, the Wicked Witch is a much larger presence in the film, and the 'it was all a dream' framing was added for the screen. The adaptation preserved the novel's central moral architecture: home is where the heart is, courage comes from within, and the search for external solutions to internal problems is a fool's errand."
        },
        "lead_producer": {
            "name": "Mervyn LeRoy",
            "company": "Metro-Goldwyn-Mayer"
        },
        "composer": {
            "name": "Harold Arlen (music), E.Y. Harburg (lyrics)",
            "profile": "Harold Arlen and Yip Harburg wrote the score including 'Over the Rainbow,' which won the Academy Award for Best Original Song and became Judy Garland's signature. Harburg was a left-leaning lyricist whose politics occasionally surfaced in his work, but 'Over the Rainbow' is a universal expression of longing that transcends political categories."
        },
        "top_cast": [
            {"name": "Judy Garland", "role": "Dorothy Gale"},
            {"name": "Frank Morgan", "role": "Professor Marvel / The Wizard / Gatekeeper / Coachman / Guard"},
            {"name": "Ray Bolger", "role": "Hunk / Scarecrow"},
            {"name": "Bert Lahr", "role": "Zeke / Cowardly Lion"},
            {"name": "Jack Haley", "role": "Hickory / Tin Man"},
            {"name": "Billie Burke", "role": "Glinda the Good Witch"},
            {"name": "Margaret Hamilton", "role": "Miss Gulch / Wicked Witch of the West"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "G",
        "mpaaDescriptors": "General audiences -- all ages admitted",
        "recommendedAge": "5+",
        "contentWarnings": [
            "The Wicked Witch of the West and her flying monkeys may frighten very young children",
            "The tornado sequence in sepia Kansas has genuine menace",
            "The Witch's death by melting is startling in context",
            "Miss Gulch's threat to destroy Toto is emotionally intense for animal-loving children",
            "The forest sequence with the 'Lions and tigers and bears' has mild suspense"
        ],
        "parentalNotes": "The Wizard of Oz is one of the safest and most valuable family films ever made. The scares are real but proportionate -- children have been watching this film for 86 years and the consensus is that the Witch is the right amount of scary for a child's first encounter with screen villainy. The film's moral lessons about home, courage, intelligence, and heart are delivered with warmth and earned through character. Parents should know that the flying monkeys are still unsettling and very young children may need reassurance. The film works on multiple levels and rewards re-watching across a lifetime."
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "The Wizard of Oz is the most beloved film in American history, and it earns that status on every rewatch. Under VVWS methodology, it scores STRONGLY TRADITIONAL by a wide margin, and that scoring is not close. The film's moral architecture is built on values that contemporary progressivism has either abandoned or reframed beyond recognition: home as the ultimate good, courage as a choice rather than a feeling, intellect and heart as earned virtues, and the clear recognition that evil exists and must be confronted.\n\nDorothy Gale (Judy Garland) lives on a Kansas farm with Aunt Em and Uncle Henry. Her only crime is wanting something more -- a place 'where troubles melt like lemon drops.' When a tornado carries her to the Technicolor Land of Oz, her house lands on the Wicked Witch of the East. Glinda the Good Witch gives Dorothy the ruby slippers and a direction: follow the yellow brick road to the Emerald City, where the Wizard can send her home. The Wicked Witch of the West vows revenge for her sister's death.\n\nThe architecture is a quest narrative, and every character Dorothy befriends is searching for something they already possess. The Scarecrow wants a brain but is already the group's most inventive problem-solver. The Tin Man wants a heart but is the most emotionally expressive member of the party. The Cowardly Lion wants courage but is the first to act when his friends are threatened. The film's thesis is ancient and durable: what you seek is already within you, but you discover it through action, loyalty, and love.\n\nThe Wicked Witch represents pure malevolence. She is not given a sympathetic backstory or a trauma that explains her. She is evil because she chooses evil. The film's moral clarity on this point is precisely what makes it durable. Children understand it immediately. Adults who have been trained to look for moral ambiguity find none, which is the point.\n\nThe Wizard, when revealed as a 'humbug' operating a machine from behind a curtain, is not condemned. He is a flawed man from Kansas who got lost and made the best of it. His gifts to Dorothy's friends -- a diploma, a testimonial, a medal -- are symbols that recognize virtues already present. His real gift to Dorothy is the truth: he cannot take her home, but the journey has shown her she never really left it.\n\nGlinda's final revelation -- 'You've always had the power to go back to Kansas' -- is the film's deepest traditional value. Home was not something Dorothy lost. It was something she had to earn the wisdom to see. The ruby slippers were on her feet the whole time. She just needed the journey to understand what they meant.\n\nThe film's score under VVWS is notable: seven traditional tropes register, many at high centrality. The single woke element -- Dorothy as a female protagonist on an adventure -- is scored at minimal severity because the film's treatment of Dorothy is the opposite of contemporary Girl Boss feminism. She leads through nurturing, loyalty, and grace, not aggression or dominance. Her power is love. That is the most traditional kind of female heroism there is."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-048",
            "name": "The Restored Home",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "The entire film is built on the value of home. Dorothy's journey begins with her wanting to leave and ends with her desperate to return. 'There's no place like home' is the film's thesis statement, delivered in the final scene and earned through every step of the yellow brick road. The sepia Kansas that seemed dull at the opening is recognized as precious by the close. This is not a subplot or a theme -- it is the film's reason for existing."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "The Wicked Witch of the West is evil without qualification. Glinda the Good Witch is good without irony. There is no moral gray area, no attempt to humanize the villain, no suggestion that good and evil are culturally constructed. The film operates within a moral framework that contemporary storytelling has largely abandoned: evil exists, it is recognizable, and it must be defeated."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "Dorothy protects Toto from Miss Gulch in Kansas and from the Witch in Oz. Her friends defend her against the Witch's attacks. The flying monkey sequence is a rescue mission for an innocent. The instinct to protect the vulnerable recurs throughout."
        },
        {
            "id": "TRADITIONAL-032",
            "name": "Meritocratic Triumph",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 5.4,
            "description": "Each character earns what they seek through action, not entitlement. The Scarecrow demonstrates intelligence under pressure. The Tin Man shows compassion at every turn. The Lion acts bravely when his friends are in danger. The Wizard's gifts are recognition of merit already demonstrated, not unearned prizes."
        },
        {
            "id": "TRADITIONAL-036",
            "name": "Traditional Femininity",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "Dorothy embodies traditional feminine virtues: nurturing, grace, loyalty, and emotional intelligence. She does not lead through aggression or dominance. She leads through caring for her friends. Her strength is in her capacity to love and be loved. This is the opposite of the Girl Boss archetype and is presented as unambiguously heroic."
        },
        {
            "id": "TRADITIONAL-033",
            "name": "The Wise Elder",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "Professor Marvel in Kansas and Glinda in Oz provide wisdom from experience. Marvel's crystal-ball act is a gentle fraud that serves a real purpose: making Dorothy see that her aunt and uncle love her. Glinda's guidance is cryptic but always correct. The film respects wisdom that comes from age and experience."
        },
        {
            "id": "TRADITIONAL-049",
            "name": "The Humble Servant",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "description": "The Wizard's true power is in humble service to the travelers. Once the curtain is pulled back, he does not cling to authority. He immediately serves: giving the Scarecrow his diploma, the Tin Man his testimonial, the Lion his medal. His attempt to take Dorothy home in the balloon is sincere, if comically thwarted. The humbug revealed is more virtuous than the Wizard pretended."
        },
        {
            "id": "WOKE-001",
            "name": "General Woke Element -- Female-Led Adventure",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 0.7,
            "description": "Dorothy Gale is a female protagonist who leads an adventure, but she does so in an organically traditional way. She is not a Girl Boss. She does not dominate her male companions or assert superiority. She leads through nurturing, loyalty, and moral clarity. Her gender is incidental to her heroism, not the point of it. This is scored at minimal severity because the context is entirely traditional. Dorothy is one of the most feminine heroes in cinema, not a subversion of femininity."
        }
    ],
    "seo": {
        "titleTag": "Is The Wizard of Oz (1939) Woke? The Classic's Traditional Values | VirtueVigil",
        "metaDescription": "VirtueVigil scores The Wizard of Oz (1939). Judy Garland, the yellow brick road, and 'there's no place like home.' Full VVWS trope audit. Verdict: STRONGLY TRADITIONAL (+24). Parental guidance included.",
        "keywords": "is The Wizard of Oz woke, Wizard of Oz traditional values, Wizard of Oz 1939 review, Wizard of Oz parents guide, is Wizard of Oz appropriate for children, Wizard of Oz family values, there's no place like home, Judy Garland"
    }
}

# ============================================================
# REVIEW #3: Batman: Caped Crusader Season 2 (2026)
# ============================================================
review3 = {
    "id": "batman-caped-crusader-s2-2026",
    "slug": "batman-caped-crusader-s2-2026",
    "title": "Batman: Caped Crusader",
    "year": 2026,
    "type": "series",
    "platform": "Prime Video",
    "genre": "Animated / Action / Crime / Noir",
    "date": "2026-08-03",
    "datePublished": "2026-08-03",
    "author": "VirtueVigil Editorial Team",
    "readTime": "6 min read",
    "poster": "",
    "releaseDate": "2026-07-31",
    "rating": "TV-14",
    "runtime": "10 episodes",
    "director": "Bruce Timm",
    "writers": ["Bruce Timm", "Matt Reeves", "J.J. Abrams", "Ed Brubaker"],
    "cast": [
        {"name": "Hamish Linklater", "role": "Bruce Wayne / Batman (voice)"},
        {"name": "Jamie Chung", "role": "Harley Quinn (voice)"},
        {"name": "Christina Ricci", "role": "Catwoman / Selina Kyle (voice)"},
        {"name": "Lacey Chabert", "role": "Vicki Vale (voice)"},
        {"name": "Matthew Needham", "role": "Joker (voice)"},
        {"name": "Ronan Raftery", "role": "Eddie Nygma / Riddler (voice)"},
        {"name": "Wunmi Mosaku", "role": "Roxy Rocket (voice)"}
    ],
    "studio": "Warner Bros. Animation / Bad Robot / 6th & Idaho",
    "distributor": "Prime Video",
    "verdict": "TRADITIONAL",
    "wokeScore": 4.5,
    "tradScore": 22.74,
    "authIndex": 0,
    "scoreMargin": "+18 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Not a woke trap. Woke elements -- gender-swapped Penguin (Oswalda Cobblepot), diverse voice casting beyond period-appropriate demographics, and assertive Barbara Gordon -- are visible from the first episodes of Season 1 through Season 2. The dominant ideology is traditional: Batman fights clearly evil criminals, sacrifices for Gotham, and restores order. Viewers know what they are getting."
    },
    "seoTitle": "Is Batman: Caped Crusader S2 (2026) Woke? Amazon's Noir Batman Returns | VirtueVigil",
    "seoDescription": "VirtueVigil reviews Batman: Caped Crusader Season 2 (2026) on Prime Video. Full VVWS trope audit. Verdict: TRADITIONAL (+18.2). Parental guidance included.",
    "seoKeywords": [
        "is Batman Caped Crusader woke",
        "Batman Caped Crusader S2 review",
        "Batman Caped Crusader 2026",
        "Batman Caped Crusader conservative review",
        "Batman animated series parents guide",
        "Batman Caped Crusader traditional or woke",
        "Batman Caped Crusader VirtueVigil",
        "Bruce Timm Batman 2026",
        "Batman Caped Crusader woke elements",
        "is Batman Caped Crusader appropriate for kids"
    ],
    "externalScores": {
        "rottenTomatoesCritic": "N/A",
        "rottenTomatoesAudience": "N/A",
        "imdb": "N/A",
        "metacritic": "N/A",
        "budget": "Not disclosed",
        "globalBoxOffice": "N/A (streaming)"
    },
    "creative_team": {
        "director": {
            "name": "Bruce Timm (creator/showrunner); Matt Reeves, J.J. Abrams, Ed Brubaker (executive producers)",
            "ideology": "MIXED LEANING TRADITIONAL. Bruce Timm created Batman: The Animated Series, the definitive screen version of Batman. His work has always prioritized character and noir atmosphere over politics. Matt Reeves (The Batman, 2022) makes morally serious superhero films with traditional underpinnings. J.J. Abrams and Ed Brubaker are career liberals whose best work transcends ideology. The creative team overall prioritizes craft and storytelling over messaging, though the show contains progressive elements (gender-swapped Penguin, diverse voice cast). The traditional elements of Batman's character -- sacrifice, justice, the protection of innocents -- dominate the show's value system.",
            "profile": "Bruce Timm defined Batman for television with Batman: The Animated Series (1992-1995), widely considered the gold standard of superhero animation. His return to the character with Caped Crusader represents a deliberate effort to recapture the noir aesthetic of the original series while updating the storytelling for 2020s sensibilities. Matt Reeves directed The Batman (2022), which scored TRADITIONAL on this site. J.J. Abrams brings Bad Robot production resources. Ed Brubaker is one of the most respected crime comic writers working, with a body of work (Criminal, The Fade Out, Gotham Central) that treats crime fiction with literary seriousness."
        },
        "writers": {
            "names": "Bruce Timm, Ed Brubaker, Greg Rucka, and writers room",
            "profile": "The writing team combines animation veterans with crime-comics royalty. Greg Rucka wrote Gotham Central and is known for strong female characters that read as organic rather than performative. Ed Brubaker's crime fiction is morally serious without being ideological. The writers room has produced a season that feels like a 1940s crime serial animated with modern craft. The progressive elements are present but subordinate to the noir atmosphere and the Batman archetype."
        },
        "lead_producer": {
            "name": "Bruce Timm, Matt Reeves, J.J. Abrams, Ed Brubaker",
            "company": "Warner Bros. Animation / Bad Robot / 6th & Idaho / Amazon MGM Studios"
        },
        "composer": {
            "name": "Frederik Wiedmann",
            "profile": "Wiedmann's score for Caped Crusader leans into noir orchestration -- muted trumpets, shadowy strings, and percussive tension that recalls 1940s crime cinema. The music serves atmosphere rather than making any statement of its own."
        },
        "top_cast": [
            {"name": "Hamish Linklater", "role": "Bruce Wayne / Batman (voice)"},
            {"name": "Jamie Chung", "role": "Harley Quinn (voice)"},
            {"name": "Christina Ricci", "role": "Catwoman / Selina Kyle (voice)"},
            {"name": "Lacey Chabert", "role": "Vicki Vale (voice)"},
            {"name": "Matthew Needham", "role": "Joker (voice)"},
            {"name": "Ronan Raftery", "role": "Eddie Nygma / Riddler (voice)"},
            {"name": "Wunmi Mosaku", "role": "Roxy Rocket (voice)"}
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "TV-14",
        "mpaaDescriptors": "Violence, dark themes, psychological horror elements, mild language",
        "recommendedAge": "13+",
        "contentWarnings": [
            "Animated violence including gunplay, fistfights, and death depicted within noir conventions",
            "Psychological horror elements including Scarecrow's fear toxin sequences",
            "Joker's appearances include disturbing psychological manipulation",
            "Murder via laughing toxin depicted in the Rupert Thorne arc",
            "Dark thematic material including corruption, murder, and institutional decay",
            "Some sequences may be too intense for younger viewers despite the animated format"
        ],
        "parentalNotes": "Batman: Caped Crusader is not the Batman cartoon parents remember from the 1990s. This is a darker, more adult-oriented take on the character, animated in a noir style that honors the 1940s setting. The violence is stylized but the psychological elements -- particularly Scarecrow's fear toxins and the Joker's manipulation -- are genuinely unsettling. The show is appropriate for teenagers and adults. Younger children should stick with the original Batman: The Animated Series or more age-appropriate superhero content. The gender-swapped Penguin (Oswalda Cobblepot) may confuse kids familiar with the traditional version but is not a content concern. Parents should know this is prestige noir animation, not Saturday morning cartoon fare."
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "Batman: Caped Crusader Season 2 arrives on Prime Video with ten episodes that deepen the show's commitment to 1940s noir. The season is darker, more serialized, and more focused on Gotham's institutional rot than the first, while maintaining the visual elegance and vocal performances that made Season 1 distinctive.\n\nHamish Linklater's Batman remains the show's anchor -- a growling, haunted presence whose detective instincts are as sharp as his fists. Linklater plays Batman as a man hollowed out by trauma who fills the void with mission. There is no quipping, no self-awareness, no irony. This is a Batman who does not know how to be anything other than what he is, and the tragedy of that is the show's central emotional frequency.\n\nSeason 2's major arcs include the murder of Rupert Thorne via laughing toxin while awaiting trial, a development that sends the Gotham underworld into chaos and introduces the Riddler (Ronan Raftery) as a major player working alongside Hugo Strange. Roxanne Sutton / Roxy Rocket (Wunmi Mosaku) pursues revenge against corrupt industrialists, and her arc is the season's most direct engagement with class and corporate power. Barbara Gordon forces Batman and Commissioner Gordon into collaboration, a dynamic that works because it treats Barbara as a genuine peer rather than a token insertion. Jonathan Crane Jr.'s Scarecrow uses fear toxins in genuinely disturbing sequences that push the TV-14 rating to its limit. The Joker (Matthew Needham) arrives in the final episodes as an agent of chaos, a force that neither Batman nor the criminal underworld can predict or control.\n\nThe show's woke elements are real and should be noted. The Penguin was gender-swapped in Season 1 to Oswalda Cobblepot, which remains an unnecessary alteration to an established character. The voice cast is diverse in ways that stretch the period setting's plausibility. Barbara Gordon is written with assertive Girl Boss energy that occasionally feels like a 2020s character in a 1940s suit. These elements cost points under VVWS methodology.\n\nBut they cost far fewer points than the traditional elements earn. Batman's entire mission is the defense of innocents against clearly evil criminals. The moral clarity of the Batman archetype -- good versus evil, order versus chaos, sacrifice versus selfishness -- is the show's gravitational center. Commissioner Gordon represents honest policing in a corrupt city. Batman sacrifices any chance at a normal life for his mission. Villains face consequences. Order is restored, week after week, because that is what the genre demands.\n\nBruce Timm and his team understand something that many contemporary superhero adaptations have forgotten: Batman does not work as a deconstruction. He is a man who turned trauma into mission, who fights evil because evil exists, and who protects the innocent because they deserve protection. Caped Crusader Season 2 honors that architecture. The progressive elements are window dressing on a traditional frame. The frame holds."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "Batman's entire mission is fighting clearly evil criminals. The Riddler murders, the Joker creates chaos, Scarecrow weaponizes fear, and corrupt industrialists destroy lives for profit. The show never equivocates: these are villains doing villainous things. Batman is not a 'complex antihero.' He is a hero who fights evil because evil exists. This moral clarity is the show's foundation."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "Protecting the innocent is Batman's core motivation. Every episode centers on preventing harm to civilians, rescuing victims, and stopping predators. This is not a side effect of Batman's mission. It is the mission. The show treats the protection of innocents as the highest moral good."
        },
        {
            "id": "TRADITIONAL-035",
            "name": "The Just Lawman",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 3.0,
            "description": "Commissioner Gordon represents honest policing in a corrupt system. He refuses to look the other way, stands up to political pressure, and maintains his integrity even when it costs him. His collaboration with Batman is built on mutual respect for justice, not convenience."
        },
        {
            "id": "TRADITIONAL-026",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "Batman sacrifices any chance at a normal life for Gotham. Bruce Wayne is a mask. The man underneath has given up personal happiness, relationships, and peace of mind to protect a city that will never know his name. This is presented as noble, not pathological."
        },
        {
            "id": "TRADITIONAL-047",
            "name": "Justice Restored",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "Villains face consequences. The Riddler is stopped. Scarecrow's schemes are foiled. Order is restored each episode. The show does not end on ambiguity or moral equivalence. Justice is served, even if the war continues. Every episode affirms that right action produces right outcomes."
        },
        {
            "id": "WOKE-013",
            "name": "The Subversive Remake",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 2.1,
            "description": "The Penguin is gender-swapped to Oswalda Cobblepot, an alteration to an established character that serves no narrative purpose. The character functions identically to the male Penguin -- a crime boss operating a nightclub. The gender swap is a cosmetic change that signals progressive intent without improving the story."
        },
        {
            "id": "WOKE-003",
            "name": "Girl Boss",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.0,
            "description": "Barbara Gordon takes an assertive lead role, forcing Batman and Commissioner Gordon to collaborate on her terms. While Barbara Gordon is an established character with agency in the comics, the show's framing occasionally leans into Girl Boss energy that feels anachronistic for a 1940s setting."
        },
        {
            "id": "WOKE-001",
            "name": "General Woke Element -- Diverse Casting Beyond Period Demographics",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 1.4,
            "description": "The voice cast includes diverse actors in roles that, in a 1940s Gotham setting, would plausibly be held by a narrower demographic range. This is voice acting in an animated show, where visual appearance is not a factor, but the casting choices reflect a deliberate effort to diversify a period setting."
        }
    ],
    "seo": {
        "titleTag": "Is Batman: Caped Crusader S2 (2026) Woke? Amazon's Noir Batman Returns | VirtueVigil",
        "metaDescription": "VirtueVigil reviews Batman: Caped Crusader Season 2 (2026) on Prime Video. Bruce Timm's noir Batman returns with Riddler, Joker, and Scarecrow. Full VVWS trope audit. Verdict: TRADITIONAL (+18.2). Parental guidance included.",
        "keywords": "is Batman Caped Crusader woke, Batman Caped Crusader S2 review, Batman Caped Crusader 2026 animated, Batman animated series parents guide, Batman Caped Crusader traditional or woke, Bruce Timm Batman, Batman noir animated"
    }
}

# Append all 3
reviews.append(review1)
reviews.append(review2)
reviews.append(review3)

print(f"Appending reviews. New count will be: {len(reviews)}")

with open(REVIEWS_FILE, "w") as f:
    json.dump(reviews, f, indent=2)

print("Reviews appended successfully.")
