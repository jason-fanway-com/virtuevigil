#!/usr/bin/env python3
"""Append 3 reviews for 2026-08-29"""
import json, sys

PATH = "src/data/reviews.json"
with open(PATH) as f:
    data = json.load(f)

slugs = {r["slug"] for r in data}
reviews = []

# ================================================================
# 1. Project Hail Mary (2026)
# ================================================================
reviews.append({
    "id": "project-hail-mary-2026",
    "slug": "project-hail-mary-2026",
    "title": "Project Hail Mary",
    "year": 2026,
    "type": "film",
    "platform": "Theaters / Amazon Prime Video",
    "genre": "Science Fiction / Drama",
    "date": "2026-08-29",
    "datePublished": "2026-08-29",
    "author": "VirtueVigil Editorial Team",
    "readTime": "11 min",
    "poster": "/images/posters/project-hail-mary-2026.jpg",
    "releaseDate": "2026-03-20",
    "rating": "PG-13 (Some Language, Peril, Thematic Elements)",
    "runtime": "156 minutes",
    "director": "Phil Lord, Christopher Miller",
    "writers": ["Drew Goddard", "Andy Weir"],
    "cast": [
        {"name": "Ryan Gosling", "role": "Ryland Grace"},
        {"name": "Sandra Huller", "role": "Eva Stratt"},
        {"name": "James Ortiz", "role": "Rocky (voice/puppeteer)"},
        {"name": "Lionel Boyce", "role": "Yao"},
        {"name": "Milana Vayntrub", "role": "Ilyukhina"},
        {"name": "Sean Bridgers", "role": "Dubois"}
    ],
    "studio": "Metro-Goldwyn-Mayer / Lord Miller Productions",
    "distributor": "Amazon MGM Studios (US) / Sony Pictures (Intl)",
    "preRelease": False,
    "wokeTrap": False,
    "authIndex": 32,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "No woke trap. The film is earnestly pro-science, pro-cooperation, and pro-self-sacrifice from its opening minutes. No ideological bait-and-switch."
    },
    "seo": {
        "titleTag": "Is Project Hail Mary (2026) Woke? Ryan Gosling Sci-Fi Epic Reviewed | VirtueVigil",
        "metaDescription": "VVWS review of Project Hail Mary (2026), the Andy Weir adaptation starring Ryan Gosling. A hard sci-fi space odyssey about science, sacrifice, and friendship. Verdict: STRONGLY TRADITIONAL (+50). Parental guidance included.",
        "keywords": ["is project hail mary woke", "project hail mary 2026 review", "project hail mary virtuevigil", "ryan gosling project hail mary", "project hail mary traditional or woke", "andy weir hail mary review", "project hail mary parents guide"]
    },
    "summary": {
        "overview": "Project Hail Mary is the big-screen adaptation of Andy Weir's 2021 bestseller, directed by Phil Lord and Christopher Miller and starring Ryan Gosling as Ryland Grace, a middle-school science teacher who wakes up aboard an interstellar spacecraft with no memory of how he got there. The Sun is dying, infected by an energy-consuming microbe called Astrophage, and humanity's last hope rests on a one-way mission to the Tau Ceti star system. Grace discovers he is not alone: an alien engineer named Rocky, from the 40 Eridani system, has arrived on the same desperate errand. Together, the human and the spider-like alien must solve a problem neither species can solve alone. The film grossed $684 million worldwide and became MGM's highest-grossing domestic release.",
        "overall": "Project Hail Mary is that rarest of things in 2026: a big-budget studio film with no ideological axe to grind. It is a story about science working, about a man choosing sacrifice over safety, and about two creatures from different worlds discovering that competence and kindness transcend biology. Ryland Grace does not lecture anyone about privilege. He does not undergo a political awakening. He saves two civilizations with a whiteboard, a graduated cylinder, and the courage to stay behind. This is the kind of story that used to define science fiction, and Project Hail Mary proves the genre still has a pulse.",
        "adultInsight": "The film earned $684 million on a $200-million net budget. It is instructive as a case study in what happens when a studio bets on a proven IP and executes it straight, without inserting a parallel political narrative. The audience showed up. The critical reception was warm. The film did not become a culture-war flashpoint because there was nothing to fight about. A $684-million gross with zero controversy is healthier than an $800-million gross with a burned brand.",
        "parentalGuidance": "Rated PG-13 for language, peril, and thematic elements. No sexual content, no graphic violence, no drug use. The peril is existential rather than gory. Characters face suffocation, radiation, and the vacuum of space, but the film handles these with restraint. The alien Rocky is friendly and non-threatening, making the film suitable for families with children aged 10 and up who can follow the scientific concepts."
    },
    "parentalGuidance": {
        "rating": "PG-13",
        "contentWarnings": "Mild language. Peril throughout (space hazards). No sexual content, nudity, or graphic violence. Thematic elements include self-sacrifice and existential threat.",
        "recommendedAge": 10,
        "discussionTopics": "Self-sacrifice for the greater good. Scientific problem-solving under pressure. Friendship across radical difference.",
        "verdict": "Safe for families with children 10+. One of the cleanest blockbusters of 2026."
    },
    "externalScores": {
        "rottenTomatoesCritic": 85,
        "rottenTomatoesAudience": 89,
        "imdb": 7.8,
        "metacritic": 69,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "$200 million (net)",
        "globalBoxOffice": "$684 million"
    },
    "creative_team": {
        "director": {"name": "Phil Lord, Christopher Miller", "role": "Directors", "note": "The duo behind The Lego Movie and Spider-Man: Into the Spider-Verse bring their visual invention to live-action sci-fi for the first time."},
        "writers": [
            {"name": "Drew Goddard", "role": "Screenplay", "note": "Goddard previously adapted Weir's The Martian for Ridley Scott."},
            {"name": "Andy Weir", "role": "Novel", "note": "Weir's 2021 novel was a bestseller and Hugo Award finalist. He serves as producer on the film."}
        ]
    },
    "fidelityCasting": {
        "assessment": "HIGH FIDELITY",
        "explanation": "Ryan Gosling's Grace closely follows the book's characterization: an awkward, supremely competent teacher who rises to impossible circumstances. The film preserves the novel's core beats. Rocky is realized through James Ortiz's voice performance and five puppeteers."
    },
    "tropeAudit": [
        {"id": "TRAD-PHM-001", "name": "Male Heroism and Self-Sacrifice", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "Grace's entire arc is defined by self-sacrifice. He chooses to stay behind on Erid to save Rocky's species. The film treats male heroism as genuinely admirable."},
        {"id": "TRAD-PHM-002", "name": "Science and Reason as Salvation", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "The plot is driven by the scientific method. Grace and Rocky solve problems through experimentation and measurement. Science is humanity's best tool."},
        {"id": "TRAD-PHM-003", "name": "Cross-Species Friendship", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "High", "weightedScore": 12.0, "explanation": "The friendship between Grace and Rocky is the emotional core, built on mutual respect for competence. Rocky has his own culture and values. Friendship transcends difference when both parties bring good faith."},
        {"id": "TRAD-PHM-004", "name": "Redemption Through Work", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "Medium", "weightedScore": 7.5, "explanation": "Grace failed to complete his academic career. The mission gives him purpose and he rises through sustained effort. Competence matters more than credentials."},
        {"id": "WOKE-PHM-001", "name": "Global Governance", "category": "Woke", "severity": 2, "authenticity": "Low", "centrality": "Low", "weightedScore": 0.8, "explanation": "Eva Stratt receives nearly unlimited authority. This is framed as an emergency measure in an extinction scenario, not an endorsement of technocratic governance."},
        {"id": "WOKE-PHM-002", "name": "Environmental Catastrophe Framing", "category": "Woke", "severity": 1, "authenticity": "Low", "centrality": "Low", "weightedScore": 0.3, "explanation": "The Astrophage crisis superficially resembles climate-change allegory. But the film does not moralize about human behavior. No carbon-footprint lectures."}
    ],
    "wokeScore": 1.1,
    "tradScore": 51.5,
    "verdict": "STRONGLY TRADITIONAL",
    "scoreMargin": "+50 TRAD"
})

# ================================================================
# 2. To Kill a Mockingbird (1962)
# ================================================================
reviews.append({
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
    "rating": "Not Rated (Recommended: 12+)",
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
        "explanation": "The opposite of a woke trap. The racial justice message is delivered openly from the first act through Atticus Finch and his defense of Tom Robinson. The moral framework is classical liberal, not critical-theoretic. No hidden agenda."
    },
    "seo": {
        "titleTag": "Is To Kill a Mockingbird (1962) Woke? Atticus Finch and the Classic Reviewed | VirtueVigil",
        "metaDescription": "VVWS review of To Kill a Mockingbird (1962), the Oscar-winning classic starring Gregory Peck. Racial justice delivered through traditional values of fatherhood, moral courage, and the rule of law. Verdict: STRONGLY TRADITIONAL (+22). Parental guidance included.",
        "keywords": ["is to kill a mockingbird woke", "to kill a mockingbird 1962 review", "atticus finch virtuevigil", "to kill a mockingbird traditional or woke", "harper lee mockingbird review", "to kill a mockingbird parents guide", "gregory peck atticus finch"]
    },
    "summary": {
        "overview": "To Kill a Mockingbird is Robert Mulligan's adaptation of Harper Lee's Pulitzer Prize winning novel, starring Gregory Peck in his Oscar-winning performance as Atticus Finch, a small-town Alabama lawyer who defends Tom Robinson (Brock Peters), a Black man falsely accused of raping a white woman, in the Depression-era South. Told through the eyes of Atticus's six-year-old daughter Scout (Mary Badham), the film weaves the trial narrative with the children's fascination with their reclusive neighbor Boo Radley (Robert Duvall, in his film debut). The American Film Institute has ranked Atticus Finch as the greatest hero in American cinema history.",
        "overall": "To Kill a Mockingbird occupies a singular place in American culture, celebrated by progressives for its anti-racist message and by traditionalists for its portrait of fatherhood, moral courage, and the rule of law. The film's power comes precisely from this dual identity. Atticus Finch does not demand systemic revolution; he demands that the system work as promised. He stands alone against a lynch mob not because he has read critical race theory but because he believes every man deserves a fair trial. That is a classically liberal, deeply American conviction, and it is why the film has endured through six decades of political realignments. The woke content is real but contained within a moral universe that is fundamentally traditional.",
        "adultInsight": "The film has been challenged in school districts in recent years, sometimes by progressives who find its white-savior framing problematic, sometimes by traditionalists who object to its racial language. Both camps miss the point. The film was made in 1962, adapted from a 1960 novel, and set in the 1930s. It was ahead of its time in its treatment of race while being of its time in its narrative perspective. Moral conviction does not require ideological hectoring. Atticus Finch persuades by being who he is.",
        "parentalGuidance": "Not rated under the MPAA system. Recommended for ages 12 and up. The film contains racial slurs used by characters in-period, which parents should discuss with children beforehand. The trial involves an accusation of rape, handled with restraint; nothing explicit is shown. A man attempts to attack the children at night; the scene is intense. The film's moral clarity makes it an excellent family-viewing experience. The conversation it prompts about courage, fairness, and standing alone for what is right is among the most valuable a parent can have with a child."
    },
    "parentalGuidance": {
        "rating": "Not Rated (Recommended: 12+)",
        "contentWarnings": "Racial slurs used in historical context. Thematic material involving rape accusation (non-explicit). A nighttime attack scene that is intense but non-graphic. Ultimately edifying.",
        "recommendedAge": 12,
        "discussionTopics": "Racial prejudice and equal justice. Moral courage. Standing for what is right even alone. Understanding others by walking in their shoes. Lawful authority vs. mob rule.",
        "verdict": "Highly recommended for families with children 12+. An essential film for teaching moral reasoning."
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
        "director": {"name": "Robert Mulligan", "role": "Director", "note": "Mulligan's sensitive direction keeps the film focused on Scout's perspective, letting the moral weight of the story emerge through a child's eyes."},
        "writers": [
            {"name": "Horton Foote", "role": "Screenplay", "note": "Foote won the Oscar for Best Adapted Screenplay, distilling Lee's novel into a tight 129 minutes."},
            {"name": "Harper Lee", "role": "Novel", "note": "Lee's 1960 novel won the Pulitzer Prize and has sold over 40 million copies. She was involved in the early stages of the adaptation and remained close with Gregory Peck until her death in 2016."}
        ]
    },
    "fidelityCasting": {
        "assessment": "HIGH FIDELITY",
        "explanation": "Gregory Peck was Harper Lee's personal choice for Atticus Finch, and the role defined his career. Mary Badham as Scout is one of cinema's great child performances. The adaptation is remarkably faithful to the novel, preserving its structure, tone, and moral seriousness."
    },
    "tropeAudit": [
        {"id": "TRAD-TKAM-001", "name": "Fatherhood and Moral Formation", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "Atticus Finch's relationship with his children is the film's core. He teaches Scout and Jem by example, taking an unpopular case, standing against the mob, treating every person with dignity. Traditional fatherhood at its most aspirational."},
        {"id": "TRAD-TKAM-002", "name": "Rule of Law", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "High", "weightedScore": 12.0, "explanation": "Atticus defends the American legal system's promise of equal justice. He argues the system must work as designed. The film treats the law as a sacred trust and its violation as a moral failure."},
        {"id": "TRAD-TKAM-003", "name": "Community and Place", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "Medium", "weightedScore": 7.5, "explanation": "Maycomb, Alabama is rendered with love and specificity. The film does not sneer at small-town life. It treats community as a mixed blessing: the source of both prejudice and belonging."},
        {"id": "TRAD-TKAM-004", "name": "Individual Moral Courage", "category": "Traditional", "severity": 3, "authenticity": "High", "centrality": "High", "weightedScore": 12.0, "explanation": "Atticus faces down a lynch mob alone. He takes a case he knows he will lose. The central moral argument: doing right has value regardless of outcome. This is virtue ethics in the classical and Judeo-Christian tradition."},
        {"id": "WOKE-TKAM-001", "name": "Racial Injustice Narrative", "category": "Woke", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "The trial of Tom Robinson exposes the lethal reality of Jim Crow justice. Tom is convicted despite clear evidence of his innocence. The film's most 'woke' content, delivered through classical liberal framing rather than intersectional analysis."},
        {"id": "WOKE-TKAM-002", "name": "Gender Nonconformity", "category": "Woke", "severity": 2, "authenticity": "Medium", "centrality": "Medium", "weightedScore": 4.0, "explanation": "Scout resists traditional femininity, wearing overalls and refusing to be a 'lady.' The film ultimately validates her authenticity, which aligns with modern gender nonconformity discourses, though in 1962 this was more about tomboy tolerance than ideology."},
        {"id": "WOKE-TKAM-003", "name": "White Savior Trope", "category": "Woke", "severity": 2, "authenticity": "High", "centrality": "Medium", "weightedScore": 5.0, "explanation": "A white lawyer saving a Black defendant is the narrative engine. The criticism is valid but the film's treatment is more complex: Tom Robinson is dignified; Atticus loses the trial; the system does not reform."}
    ],
    "wokeScore": 25.0,
    "tradScore": 47.5,
    "verdict": "STRONGLY TRADITIONAL",
    "scoreMargin": "+22 TRAD"
})

# ================================================================
# 3. Fireproof (2008)
# ================================================================
reviews.append({
    "id": "fireproof-2008",
    "slug": "fireproof-2008",
    "title": "Fireproof",
    "year": 2008,
    "type": "film",
    "platform": "Rental / Streaming",
    "genre": "Christian Drama / Romance",
    "date": "2026-08-29",
    "datePublished": "2026-08-29",
    "author": "VirtueVigil Editorial Team",
    "readTime": "10 min",
    "poster": "/images/posters/fireproof-2008.jpg",
    "releaseDate": "2008-09-26",
    "rating": "PG (Thematic Material, Some Peril)",
    "runtime": "122 minutes",
    "director": "Alex Kendrick",
    "writers": ["Alex Kendrick", "Stephen Kendrick"],
    "cast": [
        {"name": "Kirk Cameron", "role": "Caleb Holt"},
        {"name": "Erin Bethea", "role": "Catherine Holt"},
        {"name": "Ken Bevel", "role": "Michael Simmons"},
        {"name": "Stephen Dervan", "role": "Wayne Floyd"},
        {"name": "Harris Malcom", "role": "John Holt"},
        {"name": "Phyllis Malcom", "role": "Cheryl Holt"}
    ],
    "studio": "Sherwood Pictures",
    "distributor": "Samuel Goldwyn Films / Affirm Films",
    "preRelease": False,
    "wokeTrap": False,
    "authIndex": 34,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Fireproof is the opposite of a woke trap. It is an explicitly Christian film from the opening scene. The Love Dare, gospel presentation, and salvation arc are not hidden payloads. No bait-and-switch. No hidden agenda."
    },
    "seo": {
        "titleTag": "Is Fireproof (2008) Woke? The Kirk Cameron Faith-Based Marriage Film Reviewed | VirtueVigil",
        "metaDescription": "VVWS review of Fireproof (2008), the Kirk Cameron Christian marriage drama. A faith-based story about marriage, pornography, and redemption through Christ. Verdict: STRONGLY TRADITIONAL (+88). Parental guidance included.",
        "keywords": ["is fireproof woke", "fireproof 2008 review", "fireproof movie virtuevigil", "kirk cameron fireproof", "fireproof the love dare", "fireproof christian movie", "fireproof parents guide", "fireproof marriage movie"]
    },
    "summary": {
        "overview": "Fireproof (2008) is an independent Christian drama directed by Alex Kendrick and starring Kirk Cameron as Caleb Holt, an Albany fire captain whose marriage to Catherine (Erin Bethea) is collapsing. Caleb's addiction to internet pornography and financial selfishness have driven Catherine to demand a divorce. At the urging of his father John, Caleb reluctantly undertakes the Love Dare, a 40-day challenge of selfless acts toward his spouse, while grappling with his need for faith. Produced on a $500,000 budget by Sherwood Pictures, a ministry of Sherwood Baptist Church in Albany, Georgia, Fireproof grossed $33.5 million, becoming the highest-grossing independent film of 2008.",
        "overall": "Fireproof is not a good film in the conventional cinematic sense. The acting is uneven, the dialog is didactic, and the structure is functionally a sermon with characters. But grading Fireproof on cinematic merits misses the point entirely. This film has a singular purpose: to save marriages by pointing husbands toward Christ. On those terms, it is extraordinarily effective. For VirtueVigil readers who are parents, Fireproof is a tool — a movie you can watch with your teenage son to talk about pornography, about what a husband owes his wife, and about what it means to love someone when you get nothing back. That is rare in any era of cinema and almost nonexistent in Hollywood's output. The film is explicit in its Christianity, including a full gospel presentation and an on-screen conversion. It treats marriage as a covenant, not a contract. It treats pornography as sin, not a lifestyle choice. It treats men as called to lead their households in sacrificial love. Every one of those commitments is countercultural in 2026, and every one of them is why this film matters.",
        "adultInsight": "Fireproof earned $33.5 million against a $500,000 budget — a 67x return. The Kendrick brothers built an audience the studios ignored: churchgoing Americans who wanted movies that shared their values. The film opened at No. 4 at the box office despite playing in fewer than 900 theaters. The Love Dare companion book became a New York Times bestseller. This was not a fluke. It was market validation of a demand Hollywood still refuses to meet at scale. There are tens of millions of Americans who will pay to see films that take their faith and families seriously. The Kendricks proved it.",
        "parentalGuidance": "Rated PG for thematic material and some peril. The film deals frankly with pornography addiction and marital conflict, including a scene where Caleb smashes his computer with a baseball bat to remove temptation. There is no sexual content or nudity. Firefighting sequences involve realistic danger but no graphic injury. The film contains an explicit Christian gospel message, including a salvation prayer and biblical references throughout. Parents of non-Christian households should preview before sharing with children. For Christian families, this is one of the most valuable discussion starters available on marriage, manhood, and sacrificial love."
    },
    "parentalGuidance": {
        "rating": "PG",
        "contentWarnings": "Frank discussion of pornography addiction and marital conflict. Peril in firefighting scenes. Explicit Christian evangelism including gospel presentation and prayer.",
        "recommendedAge": 12,
        "discussionTopics": "Marriage as covenant vs. contract. The destructive effects of pornography. What sacrificial love looks like in practice. Faith and personal transformation.",
        "verdict": "Highly recommended for Christian families. Parents should preview the explicit gospel content before sharing with non-Christian children. Excellent starting point for father-son conversations about marriage and pornography."
    },
    "externalScores": {
        "rottenTomatoesCritic": 38,
        "rottenTomatoesAudience": 73,
        "imdb": 6.5,
        "metacritic": 28,
        "oscarNominations": 0,
        "oscarCategories": "",
        "budget": "$500,000",
        "globalBoxOffice": "$33.5 million"
    },
    "creative_team": {
        "director": {"name": "Alex Kendrick", "role": "Director / Co-Writer / Actor", "note": "A pastor at Sherwood Baptist Church, Kendrick directed his first film in 2003 with church volunteers. Fireproof was his third feature and the one that broke through to mainstream audiences."},
        "writers": [
            {"name": "Alex Kendrick", "role": "Co-Writer / Director", "note": "Kendrick co-wrote the screenplay with his brother Stephen, basing the Love Dare concept on biblical principles of covenant marriage."},
            {"name": "Stephen Kendrick", "role": "Co-Writer / Producer", "note": "Stephen co-founded Sherwood Pictures with his brother and serves as producer on all their films. He co-authored The Love Dare book."}
        ]
    },
    "fidelityCasting": {
        "assessment": "N/A (original screenplay)",
        "explanation": "Fireproof is an original story, not an adaptation. Kirk Cameron, a former child star and prominent evangelical, was cast after the producers struggled to find a name actor willing to work for the film's tiny budget. Cameron insisted the film include an explicit gospel message rather than a vaguer spiritual theme."
    },
    "tropeAudit": [
        {"id": "TRAD-FP-001", "name": "Christian Faith as Solution", "category": "Traditional", "severity": 5, "authenticity": "High", "centrality": "High", "weightedScore": 20.0, "explanation": "The film's entire framework is that Caleb's marital problems cannot be solved through human effort alone. He must accept Christ to become capable of the love his wife needs. This is the explicit theological position, presented without apology."},
        {"id": "TRAD-FP-002", "name": "Marriage as Sacred Covenant", "category": "Traditional", "severity": 5, "authenticity": "High", "centrality": "High", "weightedScore": 20.0, "explanation": "The film treats marriage as a permanent covenant before God, not a civil contract dissolved when feelings change. Divorce is a moral failure. The Love Dare is structured to restore the covenant, not to negotiate a more equitable partnership."},
        {"id": "TRAD-FP-003", "name": "Male Leadership and Sacrifice", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "Responsibility for healing the marriage rests squarely on Caleb. He is called to love his wife as Christ loved the church — sacrificially, without guarantee of reciprocation. The film's theology is complementarian: the husband leads through servanthood."},
        {"id": "TRAD-FP-004", "name": "Pornography as Sin and Destruction", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "Caleb's pornography addiction is presented as a form of adultery that poisons his marriage. The film treats it as sin requiring repentance, not a harmless outlet. Caleb destroys his computer as an act of repentance. No mainstream Hollywood film has ever treated pornography this seriously."},
        {"id": "TRAD-FP-005", "name": "Redemption Through Repentance", "category": "Traditional", "severity": 4, "authenticity": "High", "centrality": "High", "weightedScore": 16.0, "explanation": "Caleb's arc is a classical conversion narrative: sin, conviction, repentance, restoration. He is not improved by therapy or self-help. He is transformed by Christ. The film's psychology is thoroughly Augustinian."},
        {"id": "WOKE-FP-001", "name": "Female Career Independence", "category": "Woke", "severity": 1, "authenticity": "Medium", "centrality": "Low", "weightedScore": 0.3, "explanation": "Catherine works as a hospital administrator and has a career identity separate from her marriage. This is presented neutrally, not as a feminist statement. The problem is Caleb's neglect, not her career."},
        {"id": "WOKE-FP-002", "name": "Racial Diversity in Cast", "category": "Woke", "severity": 1, "authenticity": "Low", "centrality": "Low", "weightedScore": 0.1, "explanation": "Caleb's best friend Michael and his wife are Black, as are several other characters. This reflects the diversity of Sherwood Baptist Church congregation. Organic and uncommented upon, not an ideological signal."}
    ],
    "wokeScore": 0.4,
    "tradScore": 88.0,
    "verdict": "STRONGLY TRADITIONAL",
    "scoreMargin": "+88 TRAD"
})

# Verify no duplicate slugs
for r in reviews:
    if r["slug"] in slugs:
        print(f"ERROR: Duplicate slug {r['slug']}")
        sys.exit(1)

# Append and save
data.extend(reviews)
with open(PATH, "w") as f:
    json.dump(data, f, indent=2)

print(f"Appended {len(reviews)} reviews. Total: {len(data)}.")
for r in reviews:
    print(f"  {r['slug']} {r['verdict']} ({r['scoreMargin']})")