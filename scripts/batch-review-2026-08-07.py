#!/usr/bin/env python3
"""Batch append 3 reviews for Aug 7, 2026: Ice Cream Man, Rear Window, Ted Lasso S1"""
import json, os, sys

REVIEWS_FILE = "src/data/reviews.json"

reviews = [
    # ===== REVIEW 1: Ice Cream Man (2026) =====
    {
        "id": "ice-cream-man-2026",
        "slug": "ice-cream-man-2026",
        "title": "Ice Cream Man",
        "year": 2026,
        "type": "film",
        "platform": "Theaters",
        "genre": "Horror, Thriller, Comedy",
        "date": "2026-08-07",
        "datePublished": "2026-08-07",
        "author": "VirtueVigil Editorial Team",
        "readTime": "5 min",
        "poster": "",
        "releaseDate": "2026-08-03",
        "rating": "R",
        "runtime": "86 min",
        "director": "Eli Roth",
        "writers": ["Eli Roth", "Noah Belson"],
        "cast": ["Ari Millen", "Charlie Zeltzer", "Shiloh O'Reilly", "Kiori Mirza Waldman", "Sarah Abbott", "Benjamin Byron Davis", "Karen Cliche"],
        "studio": "The Solution Entertainment Group / VMI Worldwide",
        "distributor": "VMI Worldwide",
        "verdict": "TRADITIONAL",
        "wokeScore": 1.5,
        "tradScore": 14.76,
        "authIndex": 10,
        "scoreMargin": "+13 TRAD",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": {
            "is_trap": False,
            "pct_runtime": 0,
            "explanation": "No woke content is hidden or bait-and-switched. The film is upfront about its horror premise from the opening scene."
        },
        "externalScores": {"imdb": "N/A", "rottenTomatoes": "N/A", "metacritic": "N/A"},
        "creative_team": {
            "director": {"name": "Eli Roth", "role": "Director", "note": "Known for Hostel, Cabin Fever, Thanksgiving"},
            "writer": {"name": "Eli Roth, Noah Belson", "role": "Writers"},
            "lead_producer": {"name": "Eli Roth, Christopher Woodrow", "role": "Producers"},
            "top_cast": [
                {"name": "Ari Millen", "role": "Ice Cream Man"},
                {"name": "Charlie Zeltzer", "role": "Lead Child"},
                {"name": "Shiloh O'Reilly", "role": "Town Resident"}
            ]
        },
        "parentalGuidance": {
            "ageRating": "R",
            "violence": "Graphic horror violence including gore and disturbing imagery involving children",
            "language": "Strong language throughout",
            "sexualContent": "None significant",
            "drugs": "None",
            "intensity": "High - intense horror sequences and sustained dread",
            "recommendation": "Not appropriate for children or young teens. Adults only."
        },
        "fidelityCasting": None,
        "summary": {
            "overall": "Eli Roth returns to his grindhouse roots with Ice Cream Man, a summer horror that knows exactly what it is: a bloody, darkly comic crowd-pleaser about a demonic ice cream vendor terrorizing an idyllic small town. The film makes no pretense of deeper meaning or political messaging. It is a straight-ahead monster movie dressed in a stained apron, and for viewers simply looking for scares and practical-effects gore, it delivers without the ideological baggage that weighs down so much contemporary horror.",
            "adultInsight": "Roth's film is refreshing precisely because it does not try to be about anything other than what it is. There is no anti-capitalist lecture disguised as a slasher, no trauma-as-metaphor framework that dominates A24-style horror. Ice Cream Man is a throwback to the preachy-free era of 1980s creature features. The small-town setting is treated with affection rather than condescension, and the community's effort to fight back reads as fundamentally human rather than politically coded. For conservative viewers tired of horror films that use the genre as a delivery mechanism for progressive ideology, this is a welcome palate cleanser.",
            "parentalGuidance": "The R rating is earned through graphic violence and gore. Children are central to the story and are placed in genuine peril throughout. There is strong language. No sexual content or drug use. The horror is visceral and may disturb sensitive viewers despite the darkly comic tone. Strictly for mature audiences."
        },
        "tropeAudit": [
            {
                "id": "WOKE-001",
                "name": "General Woke Element",
                "category": "Woke",
                "severity": 1,
                "authenticity": "Moderate",
                "centrality": "Low",
                "weightedScore": 0.5,
                "description": "Barely perceptible traces of anti-small-town condescension in the opening act, but the film quickly drops any pretense of social commentary in favor of pure horror. The summer town is ultimately portrayed with warmth, not as a locus of hidden evil."
            },
            {
                "id": "WOKE-004",
                "name": "Institutional Evil",
                "category": "Woke",
                "severity": 2,
                "authenticity": "Moderate",
                "centrality": "Low",
                "weightedScore": 1.0,
                "description": "Local law enforcement is ineffective against the supernatural threat, but this is standard horror-genre convention rather than a political statement about policing. The sheriff is portrayed as genuinely trying his best, not as corrupt or malevolent."
            },
            {
                "id": "TRADITIONAL-039",
                "name": "Objective Good vs. Evil",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "The ice cream man is unambiguously evil, a demonic force preying on children. The townspeople are unambiguously good, fighting to protect the innocent. No moral gray area or 'he's actually a victim of society' framework."
            },
            {
                "id": "TRADITIONAL-045",
                "name": "Defense of the Innocent",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "The entire third act centers on adults risking their lives to protect children from the ice cream man. The protective instinct is portrayed as the highest virtue, never mocked or deconstructed."
            },
            {
                "id": "TRADITIONAL-037",
                "name": "Small-Town Integrity",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 1.4,
                "description": "The summer town setting is depicted with genuine affection. Neighbors know each other, community bonds matter, and when the crisis hits, the town rallies together rather than descending into selfish anarchy."
            },
            {
                "id": "TRADITIONAL-047",
                "name": "Justice Restored",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.1,
                "description": "The evil is confronted and defeated by the end. Order is restored to the town. Evil does not get the last word or a sequel-bait ambiguous ending."
            },
            {
                "id": "TRADITIONAL-041",
                "name": "Industry and Perseverance",
                "category": "Traditional",
                "severity": 1,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.35,
                "description": "The town's working-class characters use practical skills and determination to fight back. No one is rescued by outside authorities or deus ex machina."
            }
        ],
        "seo": {
            "titleTag": "Is Ice Cream Man (2026) Woke? Eli Roth's Summer Horror Returns to Grindhouse Roots | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS review of Ice Cream Man (2026). Eli Roth's horror-comedy about a demonic ice cream vendor terrorizing a summer town. Trope scores, verdict: TRADITIONAL (+13). Parental guidance included.",
            "keywords": "is ice cream man woke, ice cream man 2026 review, ice cream man virtuevigil, ice cream man traditional or woke, eli roth ice cream man, ice cream man parents guide, ice cream man horror review, ice cream man conservative review"
        }
    },

    # ===== REVIEW 2: Rear Window (1954) =====
    {
        "id": "rear-window-1954",
        "slug": "rear-window-1954",
        "title": "Rear Window",
        "year": 1954,
        "type": "film",
        "platform": "Amazon Prime / Apple TV / Blu-ray",
        "genre": "Thriller, Mystery, Drama",
        "date": "2026-08-07",
        "datePublished": "2026-08-07",
        "author": "VirtueVigil Editorial Team",
        "readTime": "6 min",
        "poster": "",
        "releaseDate": "1954-09-01",
        "rating": "PG",
        "runtime": "112 min",
        "director": "Alfred Hitchcock",
        "writers": ["John Michael Hayes"],
        "cast": ["James Stewart", "Grace Kelly", "Wendell Corey", "Thelma Ritter", "Raymond Burr"],
        "studio": "Paramount Pictures / Patron Inc.",
        "distributor": "Paramount Pictures",
        "verdict": "TRADITIONAL",
        "wokeScore": 0.35,
        "tradScore": 15.79,
        "authIndex": 10,
        "scoreMargin": "+15 TRAD",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": {
            "is_trap": False,
            "pct_runtime": 0,
            "explanation": "The film has no woke content to hide. Its themes of voyeurism, commitment, and community are explored without any political or ideological subtext."
        },
        "externalScores": {"imdb": "8.5/10", "rottenTomatoes": "98%", "metacritic": "100/100"},
        "creative_team": {
            "director": {"name": "Alfred Hitchcock", "role": "Director", "note": "The Master of Suspense. Vertigo, Psycho, North by Northwest."},
            "writer": {"name": "John Michael Hayes", "role": "Screenplay", "note": "Based on 'It Had to Be Murder' by Cornell Woolrich"},
            "lead_producer": {"name": "Alfred Hitchcock", "role": "Producer"},
            "top_cast": [
                {"name": "James Stewart", "role": "L.B. 'Jeff' Jefferies"},
                {"name": "Grace Kelly", "role": "Lisa Carol Fremont"},
                {"name": "Wendell Corey", "role": "Detective Thomas J. Doyle"},
                {"name": "Thelma Ritter", "role": "Stella"},
                {"name": "Raymond Burr", "role": "Lars Thorwald"}
            ]
        },
        "parentalGuidance": {
            "ageRating": "PG",
            "violence": "Off-screen murder is discussed; brief physical struggle at the climax; no gore",
            "language": "Mild by modern standards; no profanity",
            "sexualContent": "Implied adult relationships and discussion of marriage; a brief glimpse of a dancer in revealing clothing through a window",
            "drugs": "Characters drink socially",
            "intensity": "Moderate - sustained suspense and themes of murder and voyeurism",
            "recommendation": "Suitable for teens and up. The suspense is masterful but not graphic."
        },
        "fidelityCasting": None,
        "summary": {
            "overall": "Alfred Hitchcock's Rear Window is not merely one of the greatest thrillers ever made. It is a masterclass in storytelling that operates entirely within a traditional moral framework, and its enduring power after more than seventy years makes a quiet argument against the modern assumption that films must be 'updated' with progressive ideology to remain relevant. Confined almost entirely to a single apartment set, Rear Window builds unbearable suspense from the simplest of premises: a man with a broken leg, watching his neighbors, who becomes convinced he has witnessed a murder. James Stewart and Grace Kelly deliver perfect performances in what remains Hitchcock's most elegantly constructed film.",
            "adultInsight": "What makes Rear Window fascinating through a VVWS lens is not what it contains but what it does not need to contain. There is no diversity checklist, no subversion of gender roles for political points, no institutional critique masquerading as character development. Lisa Fremont (Grace Kelly) is one of cinema's great feminine characters: elegant, resourceful, courageous, and deeply committed to the man she loves. Her bravery when she climbs into Thorwald's apartment is not about 'proving women can do what men do.' It is about love and loyalty. Jeff's arc from detached observer to engaged protector is a masculine journey toward responsibility and commitment, not a deconstruction of masculinity. The film treats voyeurism as a moral question, not a metaphor for patriarchal oppression. These are human themes, not political ones, and the film is richer for it.",
            "parentalGuidance": "The PG rating is accurate. The violence is almost entirely implied rather than shown. The murder at the center of the plot is discussed but never depicted. The climax features a physical struggle with some intensity. There are adult themes around marriage, commitment, and voyeurism that may go over younger children's heads. Recommended for teenagers and adults who can appreciate Hitchcock's mastery of suspense."
        },
        "tropeAudit": [
            {
                "id": "WOKE-001",
                "name": "General Woke Element",
                "category": "Woke",
                "severity": 1,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.35,
                "description": "A 1954 film contains essentially no woke content. The single possible trace is Miss Torso, the dancer whose window Jeff watches, but her portrayal is more about Jeff's voyeurism than any ideological point about female objectification. The film neither endorses nor condemns her lifestyle."
            },
            {
                "id": "TRADITIONAL-034",
                "name": "Sanctity of Marriage",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 1.4,
                "description": "The film's central crime is the destruction of a marriage through murder. The Thorwalds' relationship, observed through Jeff's window, serves as a dark counterpoint to Jeff and Lisa's developing commitment. Marriage is treated as a serious, binding institution."
            },
            {
                "id": "TRADITIONAL-036",
                "name": "Traditional Femininity",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.1,
                "description": "Grace Kelly's Lisa Fremont is the definitive portrait of feminine grace and courage. She brings dinner from '21,' wears a $1,100 dress to a crime scene, and climbs into a murderer's apartment without hesitation. Her femininity is never treated as weakness; it is her strength."
            },
            {
                "id": "TRADITIONAL-039",
                "name": "Objective Good vs. Evil",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "Lars Thorwald is evil without qualification. He murdered his wife, dismembered her body, and buried the pieces in the garden. Jeff and Lisa are good without ambiguity. Hitchcock provides no moral equivalency, no 'Thorwald was driven to it by society' explanation."
            },
            {
                "id": "TRADITIONAL-045",
                "name": "Defense of the Innocent",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "The entire second half of the film is driven by Jeff, Lisa, and Stella's determination to prove Thorwald's guilt and bring justice for his murdered wife. Lisa risks her life by entering Thorwald's apartment. Jeff risks his remaining mobility to protect her."
            },
            {
                "id": "TRADITIONAL-047",
                "name": "Justice Restored",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "description": "Thorwald is caught, confesses, and will face justice. The final shot shows the courtyard returned to peace, with Jeff and Lisa together, their relationship strengthened by the ordeal. Order is fully restored."
            },
            {
                "id": "TRADITIONAL-035",
                "name": "The Just Lawman",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.7,
                "description": "Detective Doyle is skeptical of Jeff's theory but follows procedure properly. He is not corrupt or incompetent, merely cautious, and when evidence emerges he acts appropriately."
            }
        ],
        "seo": {
            "titleTag": "Is Rear Window (1954) Woke? Hitchcock's Masterpiece of Suspense and Traditional Values | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS review of Rear Window (1954). Alfred Hitchcock's suspense classic starring James Stewart and Grace Kelly. Verdict: TRADITIONAL (+15). A timeless thriller built on traditional moral foundations. Parental guidance included.",
            "keywords": "is rear window woke, rear window 1954 review, rear window virtuevigil, rear window traditional or woke, alfred hitchcock rear window, james stewart grace kelly, rear window parents guide, rear window conservative review, classic hitchcock review"
        }
    },

    # ===== REVIEW 3: Ted Lasso — Season 1 (2020) =====
    {
        "id": "ted-lasso-s1-2020",
        "slug": "ted-lasso-s1-2020",
        "title": "Ted Lasso (Season 1)",
        "year": 2020,
        "type": "series",
        "platform": "Apple TV+",
        "genre": "Comedy, Drama, Sports",
        "date": "2026-08-07",
        "datePublished": "2026-08-07",
        "author": "VirtueVigil Editorial Team",
        "readTime": "6 min",
        "poster": "",
        "releaseDate": "2020-08-14",
        "rating": "TV-MA",
        "runtime": "10 episodes (~30 min each)",
        "director": "Various (developed by Jason Sudeikis, Bill Lawrence, Brendan Hunt, Joe Kelly)",
        "writers": ["Jason Sudeikis", "Bill Lawrence", "Brendan Hunt", "Joe Kelly"],
        "cast": ["Jason Sudeikis", "Hannah Waddingham", "Juno Temple", "Brett Goldstein", "Phil Dunster", "Nick Mohammed", "Brendan Hunt", "Jeremy Swift"],
        "studio": "Ruby's Tuna / Doozer / Warner Bros. Television / Universal Television",
        "distributor": "Apple TV+",
        "verdict": "TRADITIONAL",
        "wokeScore": 4.35,
        "tradScore": 16.31,
        "authIndex": 10,
        "scoreMargin": "+12 TRAD",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": {
            "is_trap": False,
            "pct_runtime": 0,
            "explanation": "Ted Lasso's progressive elements are visible from episode one. The diverse cast, female team owner, and critique of toxic behavior are upfront. Nothing is hidden or bait-and-switched. The show's traditional core values are also present from the start, making this an honest offering that lets viewers know what they are getting."
        },
        "externalScores": {"imdb": "8.8/10", "rottenTomatoes": "92%", "metacritic": "71/100"},
        "creative_team": {
            "director": {"name": "Various", "role": "Directors", "note": "Developed by Jason Sudeikis, Bill Lawrence, Brendan Hunt, and Joe Kelly"},
            "writer": {"name": "Jason Sudeikis, Bill Lawrence, Brendan Hunt, Joe Kelly", "role": "Creators/Writers"},
            "lead_producer": {"name": "Bill Lawrence, Jason Sudeikis", "role": "Executive Producers"},
            "top_cast": [
                {"name": "Jason Sudeikis", "role": "Ted Lasso"},
                {"name": "Hannah Waddingham", "role": "Rebecca Welton"},
                {"name": "Juno Temple", "role": "Keeley Jones"},
                {"name": "Brett Goldstein", "role": "Roy Kent"},
                {"name": "Phil Dunster", "role": "Jamie Tartt"},
                {"name": "Nick Mohammed", "role": "Nathan Shelley"}
            ]
        },
        "parentalGuidance": {
            "ageRating": "TV-MA",
            "violence": "Minimal - soccer-related physical contact, one episode features a brief scuffle",
            "language": "Frequent strong language throughout; Roy Kent uses profanity in nearly every line",
            "sexualContent": "References to sexual relationships and brief suggestive scenes; no nudity",
            "drugs": "Social drinking throughout; references to drug use in one episode",
            "intensity": "Low to moderate - the show's warmth offsets most mature content",
            "recommendation": "The TV-MA rating is almost entirely for language. Thematic content about divorce, mental health, and toxic relationships may require parental discussion. Suitable for mature teens and adults."
        },
        "fidelityCasting": None,
        "summary": {
            "overall": "Ted Lasso arrived in 2020 like a warm blanket in a cold year. On the surface, Apple TV+'s flagship comedy looks like a progressive show: a diverse ensemble cast, a female Premier League team owner, frank discussions of mental health, and an American fish-out-of-water premise that could easily have been weaponized into yet another lecture about toxic masculinity. But Ted Lasso Season 1 is something far more interesting, and far more traditional, than its surface suggests. It is a show whose progressive window dressing conceals a deeply conservative heart, one built on the radical proposition that kindness, forgiveness, hard work, and authentic male friendship can heal nearly any wound.",
            "adultInsight": "The VVWS scoring on Ted Lasso reveals a fascinating tension. The woke tropes are real: the show features a female team owner (Rebecca) in a male-dominated sport, treats mental health with modern therapeutic language, critiques Jamie Tartt's arrogance and Roy Kent's rage as forms of toxic masculine expression, and casts London's AFC Richmond with the natural diversity one would expect in a Premier League club. These earn a modest woke score of 4.35. But the traditional tropes are far more numerous and deeply embedded in the show's DNA. Ted Lasso himself is a Principled Patriarch who leads not through dominance but through servant-hearted care. Every major character undergoes a redemptive arc. The team succeeds through industry and perseverance, not identity-based shortcuts. And the show's central dramatic turn is Rebecca's forgiveness of those who wronged her and Ted's forgiveness of Rebecca's sabotage. These are explicitly Christian moral frameworks delivered without once mentioning Christianity. The result is a show that scored +12 TRAD in Season 1 alone, earning a TRADITIONAL verdict with room to spare. Ted Lasso is proof that warm, popular entertainment need not abandon traditional values to feel modern.",
            "parentalGuidance": "The TV-MA rating is driven almost entirely by Roy Kent's creative profanity, which is frequent and emphatic. Sexual content is limited to references and brief suggestive scenes. The show deals honestly with divorce, mental health struggles, and toxic relationship dynamics. These themes are handled with care and could provide good discussion material for families with older teens. The language makes it inappropriate for younger children despite the show's otherwise wholesome tone."
        },
        "tropeAudit": [
            {
                "id": "WOKE-003",
                "name": "The Girl Boss",
                "category": "Woke",
                "severity": 1,
                "authenticity": "Moderate",
                "centrality": "Moderate",
                "weightedScore": 1.0,
                "description": "Rebecca Welton takes over AFC Richmond as owner. This could register as Girl Boss territory, but the show handles it with nuance. Rebecca initially seeks to destroy the team out of personal revenge, not 'prove women can do it.' Her arc is about redemption, not domination. She does not display hyper-masculine traits or demean men."
            },
            {
                "id": "WOKE-011",
                "name": "The Toxic Masculinity Critique",
                "category": "Woke",
                "severity": 2,
                "authenticity": "Moderate",
                "centrality": "Moderate",
                "weightedScore": 2.0,
                "description": "Jamie Tartt's arrogance and Roy Kent's simmering rage are explicitly critiqued as forms of toxic masculine expression. However, the show does not condemn masculinity itself. Roy's protectiveness is celebrated. Jamie's competitive drive is channeled rather than crushed. The critique is of broken expressions, not of the underlying male nature."
            },
            {
                "id": "WOKE-013",
                "name": "The Subversive Remake / Diversity Casting",
                "category": "Woke",
                "severity": 1,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.35,
                "description": "AFC Richmond features a naturally diverse cast reflecting modern London. Nigerian player Sam Obisanya, Mexican player Dani Rojas, and others are integrated organically. No character exists solely to check a diversity box. This is diversity done right: reflective of reality, not imposed for ideology."
            },
            {
                "id": "WOKE-001",
                "name": "General Woke Element - Mental Health Focus",
                "category": "Woke",
                "severity": 1,
                "authenticity": "Moderate",
                "centrality": "Low",
                "weightedScore": 0.5,
                "description": "The show's emphasis on therapy and emotional vulnerability uses modern therapeutic language. But it treats these as complements to, not replacements for, traditional sources of strength like community, duty, and self-discipline."
            },
            {
                "id": "TRADITIONAL-027",
                "name": "The Redemptive Arcs (Personal)",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "Every major character undergoes a redemptive arc in Season 1. Rebecca moves from sabotage to genuine care. Jamie begins his journey from arrogant star to team player. Roy starts opening himself to vulnerability and connection. These redemptions come through repentance and changed behavior, not external validation."
            },
            {
                "id": "TRADITIONAL-029",
                "name": "The Principled Patriarch",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "description": "Ted Lasso is the Principled Patriarch of AFC Richmond. He leads through moral example, not force. He is firm when needed (benching Jamie for selfish play) and tender when needed (supporting players through personal crises). His leadership style is fatherly: demanding, loving, and always oriented toward the growth of those in his care."
            },
            {
                "id": "TRADITIONAL-042",
                "name": "The Forgiving Heart",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "Ted's forgiveness of Rebecca's season-long sabotage is the emotional climax of Season 1. He forgives not because it is easy but because it is right. This is Christian ethics without the Christian label: grace freely given to someone who does not deserve it. Rebecca's own arc of forgiving her ex-husband runs parallel."
            },
            {
                "id": "TRADITIONAL-032",
                "name": "The Meritocratic Triumph",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 1.4,
                "description": "Players earn their positions through effort and performance. Sam Obisanya is promoted because he works harder and plays better, not because of identity-based considerations. The show affirms that talent plus effort equals success."
            },
            {
                "id": "TRADITIONAL-041",
                "name": "Industry and Perseverance",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.7,
                "description": "The team's gradual improvement through the season is framed as a result of hard work, practice, and team cohesion. No shortcuts. No deus ex machina. Just showing up and doing the work."
            },
            {
                "id": "TRADITIONAL-049",
                "name": "The Humble Servant",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.7,
                "description": "Ted's daily ritual of bringing Rebecca biscuits is the show's perfect symbol of servant leadership. A man in authority performing a small, consistent act of care with no expectation of return. Leadership as service, not dominance."
            }
        ],
        "seo": {
            "titleTag": "Is Ted Lasso (Season 1) Woke? Why Apple's Hit Comedy Is Surprisingly Traditional | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS review of Ted Lasso Season 1 (2020). Jason Sudeikis's beloved comedy looks progressive on the surface but scored TRADITIONAL (+12). Trope analysis, verdict, and parental guidance included.",
            "keywords": "is ted lasso woke, ted lasso season 1 review, ted lasso virtuevigil, ted lasso traditional or woke, jason sudeikis ted lasso, ted lasso parents guide, ted lasso conservative review, is ted lasso traditional, apple tv ted lasso review"
        }
    }
]

# Load existing reviews
with open(REVIEWS_FILE, 'r') as f:
    existing = json.load(f)

# Check for duplicates
existing_slugs = {r['slug'] for r in existing}
for review in reviews:
    if review['slug'] in existing_slugs:
        print(f"ERROR: Duplicate slug {review['slug']} - ABORTING")
        sys.exit(1)

# Append
existing.extend(reviews)
with open(REVIEWS_FILE, 'w') as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"Appended {len(reviews)} reviews. Total: {len(existing)}")
for r in reviews:
    print(f"  {r['slug']}: {r['verdict']} ({r['scoreMargin']})")
