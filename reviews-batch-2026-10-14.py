#!/usr/bin/env python3
"""Append 3 reviews to src/data/reviews.json for 2026-10-14."""
import json, copy

AUTH_MAP = {"High": 0.7, "Moderate": 0.5, "Low": 0.3}
CENT_MAP = {"High": 1.8, "Moderate": 1.0, "Low": 0.5}

def ws(sev, auth, cent):
    return round(sev * AUTH_MAP[auth] * CENT_MAP[cent], 2)

# ──────────────────────────────────────────────
# REVIEW 1: The Shape of Water (2017)
# ──────────────────────────────────────────────
shape_of_water = {
    "id": "the-shape-of-water-2017",
    "slug": "the-shape-of-water-2017",
    "title": "The Shape of Water",
    "year": 2017,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Fantasy, Romance, Drama",
    "date": "2026-10-14",
    "datePublished": "2026-10-14",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/the-shape-of-water.jpg",
    "releaseDate": "December 1, 2017",
    "rating": "R",
    "runtime": "123 min",
    "director": "Guillermo del Toro",
    "writers": "Guillermo del Toro, Vanessa Taylor",
    "cast": [
        "Sally Hawkins",
        "Michael Shannon",
        "Richard Jenkins",
        "Doug Jones",
        "Octavia Spencer"
    ],
    "studio": "Fox Searchlight Pictures",
    "distributor": "Fox Searchlight Pictures",
    "verdict": "WOKE",
    "wokeScore": "17.85",
    "tradScore": "7.84",
    "scoreMargin": "-10.01 WOKE",
    "preRelease": "False",
    "wokeTrap": False,
    "woke_trap_assessment": "The film's ideological framework is established from the opening scenes. Elisa's marginalization as a mute woman, Strickland's toxic masculinity, the government lab as an institution of cruelty -- all are present in the first act. The film's progressive politics are worn openly from start to finish; there is no hidden ideological pivot past the midpoint. The creature is introduced immediately as a sympathetic 'other,' and the parallel between his captivity and Elisa's voicelessness is explicit within the first thirty minutes.",
    "creative_team": None,
    "fidelityCasting": None,
    "externalScores": None,
    "seo": {
        "titleTag": "Is The Shape of Water Woke? 2017 Best Picture Winner Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Guillermo del Toro's The Shape of Water (2017), the Best Picture winner about a mute woman and an amphibian creature. Full trope audit, woke and traditional scores, and parental guidance. Verdict: WOKE (-10.01 WOKE).",
        "keywords": ["is the shape of water woke", "shape of water review", "virtuevigil shape of water", "guillermo del toro shape of water", "shape of water parents guide", "shape of water woke score"]
    },
    "summary": {
        "overall": "Guillermo del Toro's The Shape of Water won the Academy Award for Best Picture in 2018, and watching it nearly a decade later, the VVWS assessment lands at WOKE (-10.01 margin). The film is a Cold War fairy tale about Elisa Esposito (Sally Hawkins), a mute janitor at a government aerospace facility who discovers an amphibian creature held captive by the lab and falls in love with it. Del Toro constructs a story in which every marginalized identity -- the mute, the gay, the Black, the non-human -- finds solidarity against the straight white patriarchal order embodied by Richard Strickland (Michael Shannon), a sadistic government agent with a cattle prod and a rotting set of fingers. The film is visually ravishing and emotionally sincere. It also announces its political loyalties with a bullhorn. Strickland is not a character; he is an indictment. He represents everything the film despises: American militarism, traditional masculinity, patriarchal control, and racial hierarchy. His sex with his wife is perfunctory and sterile, while Elisa's love for the creature is tender and transcendent. The film does not argue for its worldview -- it assumes it. By the time Giles (Richard Jenkins) delivers a line about being born 'either too early or too late,' the audience has already been sorted into those who will weep at the beauty of the marginalized finding each other and those who will notice they have been attending a sermon. The film's traditional virtues are real but peripheral. Elisa's willingness to sacrifice herself for the creature is a genuinely moving expression of selfless love. Her determination to protect an innocent being from torture is honorable. Zelda (Octavia Spencer) is a loyal friend. But the film frames these virtues as resistance to patriarchal order, not as goods in themselves. Love is valid here only when it transgresses boundaries; sacrifice is praiseworthy only when it defies authority. The VVWS verdict is WOKE, not STRONGLY WOKE, because del Toro is a genuine auteur making art he believes in. This is not a committee-built diversity product. It is a director's vision, executed with craft and passion. But that vision is fundamentally progressive in its moral architecture, and the film never complicates its own premises. Strickland remains a monster. The creature remains an innocent. The government remains evil. The counterculture remains righteous. That is not storytelling with tension; it is storytelling with a predetermined conclusion.",
        "woke_score": 17.85,
        "trad_score": 7.84,
        "margin": "-10.01 WOKE",
        "adultInsight": "The Shape of Water is Guillermo del Toro at his most emotionally unguarded, and for viewers who share his romantic sensibility -- that monsters are the true outsiders and outsiders are the true heroes -- the film is a transporting experience. Sally Hawkins delivers a performance entirely without spoken dialogue that carries the film's considerable emotional weight. Michael Shannon, tasked with playing a one-note villain, gives Strickland a physicality and menace that almost transcends the thinness of the writing. The creature design is a triumph of practical effects, and the underwater cinematography by Dan Laustsen is luminous. The film's weakness, from the VVWS perspective, is its refusal to grant any interiority to the traditional world it condemns. Strickland has no complexity, no motivation beyond cruelty, no moment of doubt. He is a punching bag for the film's moral certainty. Compare this to the villains in del Toro's own Pan's Labyrinth: Captain Vidal is monstrous, but he is also a human being with a wound you can see. Strickland is Vidal without the wound. That difference is instructive. When a film cannot imagine what it opposes, it cannot persuade anyone who does not already agree. The Shape of Water preaches to the choir beautifully, but it is still preaching. For viewers who can accept the sermon in exchange for the craft, the film remains a striking achievement. For those who notice they are being lectured, the craft may not be enough.",
        "parentalGuidance": "The Shape of Water is rated R for sexual content, graphic nudity, violence, and language. It is not suitable for children or most teenagers. The film contains full-frontal nudity (both human and creature), a scene of female masturbation, and an implied sexual relationship between a woman and a non-human creature. Violence includes a man's fingers being bitten off (shown graphically), a cat being eaten, a man being shot in the face, and repeated scenes of torture and electrocution of a captive creature. Language is strong throughout, including racial slurs and sexual harassment. The film's moral framework portrays traditional heterosexual marriage as sterile and unfulfilling, which may conflict with some families' values. Recommended for adults only. For older teens (17+), the film could provide productive discussion material about how art can be simultaneously beautiful in execution and ideologically one-sided in argument. Parents should know the creature-human romance is central and explicit, and the film's treatment of sexuality is frank and adult."
    },
    "parentalGuidance": "The Shape of Water is rated R for sexual content, graphic nudity, violence, and language. It is not suitable for children or most teenagers. The film contains full-frontal nudity (both human and creature), a scene of female masturbation, and an implied sexual relationship between a woman and a non-human creature. Violence includes a man's fingers being bitten off (shown graphically), a cat being eaten, a man being shot in the face, and repeated scenes of torture and electrocution of a captive creature. Language is strong throughout, including racial slurs and sexual harassment. The film's moral framework portrays traditional heterosexual marriage as sterile and unfulfilling, which may conflict with some families' values. Recommended for adults only. For older teens (17+), the film could provide productive discussion material about how art can be simultaneously beautiful in execution and ideologically one-sided in argument. Parents should know the creature-human romance is central and explicit, and the film's treatment of sexuality is frank and adult.",
    "tropeAudit": [
        {
            "id": "VV-SOW-001",
            "name": "The Toxic Masculinity Critique",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Low",
            "centrality": "High",
            "weightedScore": ws(5, "Low", "High"),
            "explanation": "Richard Strickland is a pure embodiment of toxic masculinity: violent, controlling, sexually predatory, obsessed with dominance. He is not a character with an interior life but a thesis statement about what the film believes men in power are. His rotting fingers, his sterile marriage, his impotent rage -- every detail is designed to condemn traditional masculinity as diseased."
        },
        {
            "id": "VV-SOW-002",
            "name": "Chosen Family over Bio-Kin",
            "category": "Woke",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": ws(5, "High", "High"),
            "explanation": "Elisa, Giles, Zelda, and the creature form a found family of outsiders whose bond transcends blood. The film treats this chosen community as morally superior to any biological or traditional family structure. Del Toro genuinely believes in this vision of solidarity among the marginalized, and it is the emotional center of the film."
        },
        {
            "id": "VV-SOW-003",
            "name": "Institutional Evil",
            "category": "Woke",
            "severity": 4,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": ws(4, "Moderate", "High"),
            "explanation": "The government aerospace facility is depicted as inherently corrupt, cruel, and opposed to everything good. The military chain of command enables Strickland's sadism. General Hoyt is a bureaucrat of evil. The institution exists to control, contain, and destroy -- a progressive vision of institutional power that the film makes no effort to complicate."
        },
        {
            "id": "VV-SOW-004",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 4,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": ws(4, "Moderate", "High"),
            "explanation": "Elisa is mute and physically small, yet she is sexually autonomous, morally decisive, and the active agent of every major plot development. She initiates the relationship with the creature, she plans the escape, she confronts Strickland. The film frames female sexual agency as inherently virtuous and revolutionary, and Elisa's inability to speak becomes not a disability but a kind of moral purity -- she communicates in a way the patriarchal world cannot hear."
        },
        {
            "id": "VV-SOW-005",
            "name": "Heteronormativity as Harm",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": ws(3, "Moderate", "Low"),
            "explanation": "Strickland's marriage is a cold transaction. Giles's homosexuality is suppressed by a society that cannot accept him, leading him to loneliness and a failed pass at a pie-shop clerk. The film presents traditional heterosexual norms as either sterile (Strickland) or oppressive (the world that closets Giles). This is present but not central -- it serves as set dressing for the main argument."
        },
        {
            "id": "VV-SOW-006",
            "name": "Anti-Western Revisionism",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": ws(3, "Low", "Moderate"),
            "explanation": "The Cold War setting is used to frame American military power as morally equivalent to Soviet brutality. The American government is not defending freedom; it is inflicting cruelty. This is a revisionist lens that treats Western institutions as inherently predatory, but it serves as backdrop rather than thesis -- the film is more interested in the personal than the geopolitical."
        },
        {
            "id": "VV-SOW-007",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": ws(4, "High", "High"),
            "explanation": "Elisa risks her job, her freedom, and ultimately her life to free the creature and protect it from the government agents hunting it. This sacrifice is genuine, moving, and presented without irony. It is the film's strongest traditional element and the reason the verdict is WOKE rather than STRONGLY WOKE."
        },
        {
            "id": "VV-SOW-008",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": ws(3, "High", "Moderate"),
            "explanation": "The creature is presented as a morally innocent being who has been captured, tortured, and threatened with vivisection. Elisa's determination to protect it -- and Zelda and Giles's willingness to help -- is framed as a moral obligation to defend the defenseless. The film treats cruelty to the innocent as the worst of sins."
        },
        {
            "id": "VV-SOW-009",
            "name": "The Forgiving Heart",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": ws(2, "High", "Low"),
            "explanation": "Elisa forgives Giles for his moment of cowardice when he initially refuses to help with the escape, and she bears no resentment toward Zelda for the risks their friendship imposes. Forgiveness is present as a quiet virtue, though it is not thematically developed and remains a minor grace note."
        }
    ]
}

# ──────────────────────────────────────────────
# REVIEW 2: Gone with the Wind (1939)
# ──────────────────────────────────────────────
gone_with_the_wind = {
    "id": "gone-with-the-wind-1939",
    "slug": "gone-with-the-wind-1939",
    "title": "Gone with the Wind",
    "year": 1939,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Drama, Romance, Historical Epic",
    "date": "2026-10-14",
    "datePublished": "2026-10-14",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/gone-with-the-wind.jpg",
    "releaseDate": "December 15, 1939",
    "rating": "G",
    "runtime": "238 min",
    "director": "Victor Fleming",
    "writers": "Sidney Howard",
    "cast": [
        "Vivien Leigh",
        "Clark Gable",
        "Leslie Howard",
        "Olivia de Havilland",
        "Hattie McDaniel"
    ],
    "studio": "Selznick International Pictures",
    "distributor": "MGM",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": "2.50",
    "tradScore": "31.92",
    "scoreMargin": "+29.42 TRAD",
    "preRelease": "False",
    "wokeTrap": False,
    "woke_trap_assessment": "Gone with the Wind is a 1939 film that wears its values openly from the opening title card about 'a land of Cavaliers and Cotton Fields.' The film's romanticization of the antebellum South, its treatment of the Civil War as tragedy visited upon a noble civilization, and its framing of Scarlett's survival through grit and perseverance are established in the first act and sustained throughout the four-hour runtime. No progressive content is concealed past any midpoint. The film's moral universe -- land, family, survival, tradition -- is present from the first frame to the last.",
    "creative_team": None,
    "fidelityCasting": None,
    "externalScores": None,
    "seo": {
        "titleTag": "Is Gone with the Wind Woke? 1939 Classic Reviewed by the VVWS | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Gone with the Wind (1939), the Civil War epic starring Vivien Leigh and Clark Gable. Full trope audit, woke and traditional scores, and parental guidance. Verdict: STRONGLY TRADITIONAL (+29.42 TRAD).",
        "keywords": ["is gone with the wind woke", "gone with the wind review", "virtuevigil gone with the wind", "gone with the wind woke score", "gone with the wind parents guide", "scarlett ohara traditional values"]
    },
    "summary": {
        "overall": "Gone with the Wind is one of the most traditional films in the VirtueVigil catalog, landing at STRONGLY TRADITIONAL with a margin of +29.42. Victor Fleming's 1939 adaptation of Margaret Mitchell's novel is a four-hour epic of the Civil War and Reconstruction, told through the life of Scarlett O'Hara (Vivien Leigh), a Southern belle who loses everything and claws her way back through sheer will. The VVWS assessment identifies seven traditional tropes at high centrality against three woke tropes that register as minor artifacts of the film's age rather than ideological arguments the film is making. The film's moral architecture is built on land, family, perseverance, and faith. Tara -- the O'Hara plantation -- is not merely property but identity. Gerald O'Hara tells Scarlett early in the film that 'land is the only thing worth working for, worth fighting for, worth dying for, because it's the only thing that lasts.' The entire four-hour runtime is a demonstration of that thesis. Scarlett loses her father, her husbands, her daughter, and finally Rhett Butler, but she keeps Tara. The film argues that attachment to place, to heritage, and to the soil your family worked is the deepest and most durable human connection. Scarlett O'Hara is a moral education in what perseverance costs. She is vain, manipulative, and self-interested. She marries men she does not love for their money. She runs a lumber business with the ruthlessness of a war profiteer. She lies, schemes, and betrays. But she also survives. When Atlanta burns and the social order collapses, Scarlett delivers Melanie's baby alone, then drives a wagon through a burning city to get her family to safety. When she arrives at Tara to find it looted and her mother dead, she does not collapse -- she digs up radishes in the garden, eats them raw, and vows, 'As God is my witness, I'll never be hungry again.' The film does not celebrate Scarlett's ruthlessness; it documents its cost. By the time Rhett delivers his famous exit line, Scarlett has lost everything her perseverance was meant to protect. The film's judgment on her is precise and devastating: survival without love is not triumph, it is tragedy. Melanie Wilkes is the film's moral compass. While Scarlett schemes, Melanie endures. She is gentle without being weak, loyal without being naive, and she dies in childbirth having given her husband the child she was told she could not survive. Melanie is the film's argument that traditional femininity is not oppression but strength of a different kind: the strength to care for others when you are dying, to see the best in people even when they have wronged you, to build a home that others want to return to. The woke elements in Gone with the Wind are real but accidental. The Mammy character (Hattie McDaniel in a historic Oscar-winning performance) embodies a racial stereotype that modern viewers rightly find uncomfortable. McDaniel's performance transcends the writing -- Mammy is the most perceptive and morally authoritative character in the film -- but the stereotype is present. The film's romanticization of the antebellum South as a lost civilization of grace and honor is a historical fiction, and the 'happy slave' portrayal is indefensible by modern standards. The VVWS scores these as woke tropes of low centrality because the film is not arguing for slavery or racial hierarchy; it is telling a story whose assumptions about race are of its time. The film's moral engine is not racial politics but the claim that survival, land, faith, and family are the most important things in human life. That claim is the definition of the traditional worldview, and Gone with the Wind makes it with the full orchestral force of 1939 Hollywood at its peak.",
        "woke_score": 2.5,
        "trad_score": 31.92,
        "margin": "+29.42 TRAD",
        "adultInsight": "Gone with the Wind is one of the few films that deserves the word 'epic' without apology. At 238 minutes, it demands an afternoon, and the sheer scale of the production -- the burning of Atlanta, the field hospital sequence with its endless rows of wounded, the crane shot that pulls back to reveal thousands of Confederate dead -- remains staggering nearly a century later. Vivien Leigh delivers a performance of astonishing range: she makes Scarlett petulant, seductive, cruel, desperate, and heartbreaking, often within the same scene. Clark Gable's Rhett Butler is the rogue who sees through Scarlett from the first moment and loves her anyway, and Gable brings a weary, amused warmth to a character who could easily have been just a smirk. The color cinematography (the film was one of the first major Technicolor productions) is painterly and precise, with the red earth of Tara functioning as a visual motif that reinforces the theme of attachment to land. The film's treatment of race is what modern viewers will notice first, and it requires historical context. Hattie McDaniel became the first Black actor to win an Academy Award for this performance, and her Mammy is the film's moral center: she sees every character clearly, speaks truth without fear, and is the only person in Scarlett's world whose judgment both Scarlett and the audience trust. The performance is brilliant. The role is a stereotype. Both things are true. The film's greatest achievement is that it makes you care about a woman who is, by most measures, not a good person. Scarlett is frustrating, infuriating, and ultimately tragic. The film does not ask you to admire her; it asks you to understand her. That is a harder and more interesting artistic project than asking you to admire a hero. When Rhett tells Scarlett he is leaving and she asks, 'Where shall I go? What shall I do?' and he answers, 'Frankly, my dear, I don't give a damn,' the silence that follows is earned across four hours of watching her destroy every relationship that mattered. For adults who can watch a 1939 film on its own terms -- as a work of its time that also transcends its time in its understanding of human nature -- Gone with the Wind remains one of the essential achievements of American cinema.",
        "parentalGuidance": "Gone with the Wind is rated G by modern standards, though it was originally released under the Hays Code. The film contains no profanity, no sexual content beyond a single scene of marital assault (Rhett carries a struggling Scarlett up the stairs -- the scene cuts away, and the next scene shows her waking with a satisfied expression, which has its own troubling implications), and no graphic violence, though the Civil War sequences depict death, injury, and the burning of Atlanta at scale. The film's racial portrayals -- particularly the depiction of enslaved people as contented and loyal, and the framing of the Ku Klux Klan as a protective response to threats against white women -- require historical context and parental discussion. Modern families should be prepared to discuss how a film made in 1939 reflects the racial assumptions of its era. The film's moral framework is traditional throughout: marriage, family loyalty, perseverance through hardship, and the sanctity of home are presented as the highest goods. The character of Belle Watling (a brothel madam) appears in several scenes but her profession is only implied. Recommended for ages 13 and up with parental guidance on the historical context of racial portrayals. The film's length (nearly four hours) is itself a consideration for younger viewers."
    },
    "parentalGuidance": "Gone with the Wind is rated G by modern standards, though it was originally released under the Hays Code. The film contains no profanity, no sexual content beyond a single scene of marital assault (Rhett carries a struggling Scarlett up the stairs -- the scene cuts away, and the next scene shows her waking with a satisfied expression, which has its own troubling implications), and no graphic violence, though the Civil War sequences depict death, injury, and the burning of Atlanta at scale. The film's racial portrayals -- particularly the depiction of enslaved people as contented and loyal, and the framing of the Ku Klux Klan as a protective response to threats against white women -- require historical context and parental discussion. Modern families should be prepared to discuss how a film made in 1939 reflects the racial assumptions of its era. The film's moral framework is traditional throughout: marriage, family loyalty, perseverance through hardship, and the sanctity of home are presented as the highest goods. The character of Belle Watling (a brothel madam) appears in several scenes but her profession is only implied. Recommended for ages 13 and up with parental guidance on the historical context of racial portrayals. The film's length (nearly four hours) is itself a consideration for younger viewers.",
    "tropeAudit": [
        {
            "id": "VV-GWTW-001",
            "name": "The Restored Home",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": ws(5, "High", "High"),
            "explanation": "Tara is the moral and emotional center of the entire film. Gerald O'Hara's speech about land being the only thing that lasts is the film's thesis statement. Scarlett's entire arc -- her scheming, her marriages, her survival -- is in service of keeping and restoring Tara. The final shot of the film is Scarlett silhouetted against the Tara sky, vowing to return home. No theme in the film is more central."
        },
        {
            "id": "VV-GWTW-002",
            "name": "Industry and Perseverance",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": ws(5, "High", "High"),
            "explanation": "Scarlett's defining trait is refusal to be defeated. When Atlanta burns, she drives a wagon through fire to save her family. When Tara is looted, she works the fields herself. When she needs money, she starts a lumber business. The film treats perseverance as a virtue even as it shows the moral compromises it can demand. 'As God is my witness, I'll never be hungry again' is not a threat; it is a vow."
        },
        {
            "id": "VV-GWTW-003",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": ws(4, "High", "High"),
            "explanation": "Melanie Wilkes embodies self-sacrifice as the highest form of love. She gives her food to wounded soldiers. She defends Scarlett against gossip at the cost of her social standing. She dies in childbirth because she chose to give her husband a child knowing it would kill her. The film presents Melanie not as naive but as the moral standard by which every other character falls short."
        },
        {
            "id": "VV-GWTW-004",
            "name": "Heritage over Innovation",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": ws(4, "High", "High"),
            "explanation": "The film's opening title card mourns a 'land of Cavaliers and Cotton Fields... a Civilization gone with the wind.' The entire narrative is an elegy for a lost way of life. Ashley Wilkes represents the old order -- educated, honorable, and helpless in the new world. The film treats the destruction of this civilization as genuine tragedy, not as progress. Heritage is not something to escape; it is something to mourn."
        },
        {
            "id": "VV-GWTW-005",
            "name": "Faith in Adversity",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": ws(3, "High", "Moderate"),
            "explanation": "Religious faith is woven throughout the film. Characters pray in moments of crisis. Melanie reads scripture to the dying. The film treats faith as a genuine source of strength, not as superstition or social convention. When Scarlett finally prays, the film treats the moment with sincerity rather than ironic distance."
        },
        {
            "id": "VV-GWTW-006",
            "name": "Family Loyalty Above All Else",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": ws(4, "High", "High"),
            "explanation": "Scarlett's every decision, however ruthless, is motivated by the survival of her family. She marries for money to save Tara. She keeps Melanie alive during the siege of Atlanta because she promised Ashley she would. Her failure as a mother and wife is the film's final indictment, but her loyalty to family as a concept -- to the O'Hara name, the O'Hara land, the O'Hara continuation -- is absolute."
        },
        {
            "id": "VV-GWTW-007",
            "name": "Traditional Femininity",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": ws(3, "High", "Moderate"),
            "explanation": "Melanie Wilkes is the film's model of traditional femininity: gentle, nurturing, loyal, self-effacing. The film presents her as morally superior to Scarlett precisely because of these qualities. Traditional womanhood is not depicted as a cage but as a form of strength that Scarlett, for all her vitality, cannot access."
        },
        {
            "id": "VV-GWTW-008",
            "name": "The Lost Cause Romanticization",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": ws(3, "Moderate", "Moderate"),
            "explanation": "The film frames the Confederate cause as a noble lost civilization rather than a rebellion to preserve slavery. This is historical revisionism, but the film is making an aesthetic argument about the passing of a way of life, not a political argument about slavery. The VVWS scores this as woke (it aligns with Anti-Western Revisionism) at moderate authenticity because the film genuinely believes in its elegy, and moderate centrality because the film's moral engine is survival, not politics."
        },
        {
            "id": "VV-GWTW-009",
            "name": "Scarlett as Proto-Girl Boss",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": ws(2, "Low", "Low"),
            "explanation": "Scarlett's ruthlessness, business acumen, and disregard for male authority could be read through a modern lens as proto-feminist empowerment. She runs a lumber mill, manipulates men for her own ends, and refuses to be controlled. But the film does not celebrate these traits -- it documents their cost. Scarlett loses everything. Scoring this as a woke trope at low centrality acknowledges the reading without endorsing it as the film's argument."
        },
        {
            "id": "VV-GWTW-010",
            "name": "Racial Stereotyping in Service of Narrative",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": ws(2, "High", "Low"),
            "explanation": "The portrayal of enslaved Black characters as contented and loyal to their white owners is historically false and offensive by modern standards. The 'happy slave' imagery is embedded in the film's world-building. However, Hattie McDaniel's Mammy transcends the stereotype: she is the most perceptive, morally authoritative, and emotionally intelligent character in the film. The scoring reflects that the stereotype is present (severity 2, authenticity High because it reflects the film's genuine worldview) but not central to the film's moral argument (centrality Low)."
        }
    ]
}

# ──────────────────────────────────────────────
# REVIEW 3: She-Hulk: Attorney at Law (2022)
# ──────────────────────────────────────────────
she_hulk = {
    "id": "she-hulk-attorney-at-law-2022",
    "slug": "she-hulk-attorney-at-law-2022",
    "title": "She-Hulk: Attorney at Law",
    "year": 2022,
    "type": "series",
    "platform": "Disney+",
    "genre": "Superhero, Comedy, Legal",
    "date": "2026-10-14",
    "datePublished": "2026-10-14",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/she-hulk-attorney-at-law.jpg",
    "releaseDate": "August 18, 2022",
    "rating": "TV-14",
    "runtime": "1 season (9 episodes)",
    "director": None,
    "writers": "Jessica Gao",
    "showrunner": "Jessica Gao",
    "cast": [
        "Tatiana Maslany",
        "Mark Ruffalo",
        "Tim Roth",
        "Benedict Wong",
        "Ginger Gonzaga"
    ],
    "studio": "Marvel Studios",
    "distributor": "Disney+",
    "verdict": "STRONGLY WOKE",
    "wokeScore": "20.10",
    "tradScore": "1.00",
    "scoreMargin": "-19.10 WOKE",
    "preRelease": "False",
    "wokeTrap": False,
    "woke_trap_assessment": "She-Hulk announces its ideological commitments in the first episode. Jennifer Walters gains Hulk powers and immediately surpasses Bruce Banner's decades of struggle within a single training montage, explaining that she controls her anger effortlessly because as a woman she has been managing male aggression her entire life. This thesis -- that female experience inherently produces moral and practical superiority -- is stated explicitly and never complicated. The show's progressive framework is established before the title sequence of episode one and sustained through the fourth-wall-breaking finale in which Jennifer confronts the writers' room AI to demand a better ending. No woke content is concealed past any midpoint; the entire series is a progressive argument wearing a superhero costume.",
    "creative_team": None,
    "fidelityCasting": None,
    "externalScores": None,
    "seo": {
        "titleTag": "Is She-Hulk: Attorney at Law Woke? Disney+ MCU Series Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of She-Hulk: Attorney at Law (2022), the Disney+ MCU series starring Tatiana Maslany. Full trope audit, woke and traditional scores, and parental guidance. Verdict: STRONGLY WOKE (-19.10 WOKE).",
        "keywords": ["is she-hulk woke", "she-hulk attorney at law review", "virtuevigil she-hulk", "she-hulk woke score", "she-hulk parents guide", "marvel she-hulk review", "she-hulk disney plus woke"]
    },
    "summary": {
        "overall": "She-Hulk: Attorney at Law is one of the most aggressively woke properties in the Marvel Cinematic Universe, and the VVWS assessment lands at STRONGLY WOKE with a margin of -19.10. The series, created by Jessica Gao, follows Jennifer Walters (Tatiana Maslany), a lawyer who gains Hulk powers after a car accident with her cousin Bruce Banner (Mark Ruffalo) and immediately demonstrates that she is better at being a Hulk than he ever was. In the first episode, Jennifer explains that she does not need Bruce's decades of training in anger management because as a woman, she deals with male anger constantly -- catcalling, workplace condescension, the daily friction of existing in a world run by men. She has been managing rage her entire life. Bruce, a man who survived childhood abuse, years on the run from the military, and the trauma of losing everyone he loved, is told to his face that his suffering taught him nothing she did not already know. This is the show in miniature. Jennifer is not a character who grows; she is a character who already knows. Every obstacle she faces is an opportunity for the show to demonstrate that she was right all along. The men in her life are incompetent (her paralegal Pug), toxic (the online troll Intelligencia who becomes the season's villain), or condescending (Bruce, her boss, every date she goes on). The women are supportive and perceptive (her paralegal Nikki, the various female superhero cameos). The show's politics are not subtext; they are the text, presented with the fourth-wall-breaking confidence of a protagonist who can turn to the camera and tell you what to think. The finale is a case study in woke storytelling as self-congratulation. Jennifer, dissatisfied with the finale the show is giving her, literally breaks through the Disney+ menu interface to confront K.E.V.I.N., an AI version of Kevin Feige, and demand that the finale be rewritten to give her what she wants. This is the show telling the audience that its own corporate creative structure is the enemy, while simultaneously being a product of that structure. The smugness is total: the show critiques the system that produced it and congratulates itself for the critique, without ever facing the consequence that a real critique would imply. The traditional score of 1.00 reflects two thin threads: Jennifer genuinely wants to be a good lawyer, and the concept of justice appears as window dressing. But the show subverts both: her legal work consists of defending superpowered clients in cases the show treats as jokes, and the finale's resolution is that the villain should face 'consequences' -- while Jennifer herself rewrites the story to give herself the ending she prefers. Justice, in the She-Hulk universe, is what the protagonist decides it is. The VVWS verdict is STRONGLY WOKE because the show's nine identified woke tropes are all high-severity with high centrality, and the pattern is consistent: every traditional value the show appears to gesture toward is immediately undermined by the progressive framework. This is not a story with woke elements; it is a woke argument that happens to contain characters.",
        "woke_score": 20.1,
        "trad_score": 1.0,
        "margin": "-19.10 WOKE",
        "adultInsight": "She-Hulk is a fascinating artifact of Marvel's streaming-era identity crisis -- a show that seems to despise the audience that made the MCU the most successful franchise in film history. Tatiana Maslany is genuinely talented, and her natural charisma nearly keeps the show afloat through sheer likeability. The problem is that the show will not let Jennifer be a person; she must be a thesis. Every scene is a teaching moment: men are clueless, corporate structures are oppressive, the audience is toxic, and the only correct response to criticism is to wave it away with a meta-joke. The fourth-wall-breaking device, borrowed from the comics, works against the show because Jennifer's direct address to the camera functions as a shortcut past dramatic tension. When a character can tell you what to think about every situation she is in, the show no longer needs to earn its conclusions through storytelling. The season finale's K.E.V.I.N. sequence is the clearest example of the problem. It is designed to be clever: Jennifer confronts the literal algorithm that produces Marvel content and demands changes. But the satire has no teeth because the show is still a Marvel product, still produced by the very system it mocks. The result is not critique but cosplay at critique -- the aesthetic of rebellion without the risk. The show's treatment of Bruce Banner is instructive. Bruce's Hulk is the product of trauma, abuse, and years of isolation. His struggle with the Hulk is the MCU's most developed character arc across multiple films. She-Hulk dismisses all of it in one episode. Jennifer is better at being a Hulk because she is a woman, and the show presents this as obvious and correct. This is not empowerment; it is erasure, and it is the show's fundamental move: to elevate its protagonist by diminishing everything around her. For viewers who want to see how thoroughly a major studio product can adopt progressive cultural assumptions and abandon dramatic fundamentals in the process, She-Hulk is an essential case study. For viewers who want to watch a superhero show about a lawyer who happens to be a Hulk, wait for the creative team that figures out how to tell that story without treating the audience as the villain.",
        "parentalGuidance": "She-Hulk: Attorney at Law is rated TV-14 for language, suggestive content, and comic-book violence. It is suitable for teenagers and up with parental awareness of the show's ideological framework. Violence is typical MCU-level: CGI fights with superpowered opponents, property destruction, and occasional mild blood. There is no graphic violence or gore. Sexual content includes dating scenarios, discussion of sex and relationships, and a subplot in which a man impersonates a female superhero to commit fraud (played for comedy). Language is moderate, with occasional mild profanity. The show's overarching message -- that female experience inherently confers moral and practical superiority, that male competence is an illusion, and that traditional structures (legal, corporate, social) are inherently oppressive -- is pervasive and should be understood by parents deciding whether the show aligns with their family's values. The show also includes extended meta-commentary about online criticism and 'toxic fandom,' which may be confusing for younger viewers unfamiliar with these discourses. Recommended for ages 14 and up, with the caveat that the show's ideological content is more intense than its content ratings suggest."
    },
    "parentalGuidance": "She-Hulk: Attorney at Law is rated TV-14 for language, suggestive content, and comic-book violence. It is suitable for teenagers and up with parental awareness of the show's ideological framework. Violence is typical MCU-level: CGI fights with superpowered opponents, property destruction, and occasional mild blood. There is no graphic violence or gore. Sexual content includes dating scenarios, discussion of sex and relationships, and a subplot in which a man impersonates a female superhero to commit fraud (played for comedy). Language is moderate, with occasional mild profanity. The show's overarching message -- that female experience inherently confers moral and practical superiority, that male competence is an illusion, and that traditional structures (legal, corporate, social) are inherently oppressive -- is pervasive and should be understood by parents deciding whether the show aligns with their family's values. The show also includes extended meta-commentary about online criticism and 'toxic fandom,' which may be confusing for younger viewers unfamiliar with these discourses. Recommended for ages 14 and up, with the caveat that the show's ideological content is more intense than its content ratings suggest.",
    "tropeAudit": [
        {
            "id": "VV-SHULK-001",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Low",
            "centrality": "High",
            "weightedScore": ws(5, "Low", "High"),
            "explanation": "Jennifer Walters is the Girl Boss archetype at its most explicit. She is a successful lawyer who gains Hulk powers and instantly surpasses the male original. She needs no training, no struggle, no growth. The show frames her effortless superiority as the natural consequence of female experience -- managing male anger is something women 'do infinitely more than' men. This is the most central trope in the series: Jennifer is better than Bruce because she is a woman, and the show treats this as a truth that requires no dramatic justification."
        },
        {
            "id": "VV-SHULK-002",
            "name": "The Smug Secularist",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Low",
            "centrality": "High",
            "weightedScore": ws(5, "Low", "High"),
            "explanation": "Jennifer's lecture to Bruce about anger management is a paradigm case of the Smug Secularist: the person whose lived experience supposedly provides an insight that decades of expertise cannot match. She dismisses Bruce's trauma, his training, and his hard-won wisdom in a single monologue because she, a woman, has to deal with catcalling. The show presents this not as arrogance but as clarity. The structural certainty that personal identity trumps earned knowledge pervades the entire series."
        },
        {
            "id": "VV-SHULK-003",
            "name": "The Fourth-Wall Troll",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Low",
            "centrality": "High",
            "weightedScore": ws(5, "Low", "High"),
            "explanation": "The season finale features Jennifer breaking through the Disney+ menu to confront K.E.V.I.N., an AI version of Kevin Feige, and demanding that the finale be rewritten. This meta-conceit congratulates the show for being smarter than the corporate structure that produced it while changing nothing about that structure. It is the aesthetic of rebellion without the cost -- a smug in-joke that prioritizes self-congratulation over storytelling."
        },
        {
            "id": "VV-SHULK-004",
            "name": "The Victimhood Meritocracy",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Low",
            "centrality": "High",
            "weightedScore": ws(5, "Low", "High"),
            "explanation": "Jennifer's moral authority derives entirely from her identity as a woman who has experienced sexism. The show argues that experiencing marginalization confers wisdom that no amount of effort or reflection by non-marginalized people can match. When Jennifer tells Bruce that her anger management skills come from being a woman in a world of men, she is asserting that victimhood is a credential -- and the show agrees with her without reservation."
        },
        {
            "id": "VV-SHULK-005",
            "name": "The Toxic Masculinity Critique",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Low",
            "centrality": "High",
            "weightedScore": ws(5, "Low", "High"),
            "explanation": "The season's villain, Intelligencia, is a collective of online men who hate Jennifer because she is a successful woman. The show reduces its antagonist to a caricature of 'toxic fandom' in which male criticism of female-led media is inherently misogynistic. There is no complexity, no legitimate grievance, no room for the possibility that some criticism might be about craft rather than gender. The villain is a straw man built to justify the show's contempt for its own audience."
        },
        {
            "id": "VV-SHULK-006",
            "name": "Man-Hating / Male Incompetence",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Low",
            "centrality": "High",
            "weightedScore": ws(5, "Low", "High"),
            "explanation": "Every male character in the series is either incompetent (Pug, Bruce, Jennifer's dates), predatory (the Intelligencia trolls, the man who impersonates a female superhero), or an obstacle (her boss, the legal system). The show does not present a single man who is both competent and admirable. Bruce Banner, one of the MCU's most beloved and developed characters, is reduced to a clueless mansplainer who needs to be taught basic emotional skills by his cousin."
        },
        {
            "id": "VV-SHULK-007",
            "name": "Anti-Fan Meta-Commentary",
            "category": "Woke",
            "severity": 4,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": ws(4, "Low", "Moderate"),
            "explanation": "Throughout the series, Jennifer and the show's framing comment on the supposed toxicity of the Marvel fanbase. The show anticipates criticism and incorporates it as villainy, immunizing itself against negative reception by making criticism itself the mark of the villain. This is a defensive posture rather than a central argument, but it recurs throughout the season."
        },
        {
            "id": "VV-SHULK-008",
            "name": "The Diversity Hire",
            "category": "Woke",
            "severity": 5,
            "authenticity": "Low",
            "centrality": "High",
            "weightedScore": ws(5, "Low", "High"),
            "explanation": "Jennifer is given Hulk powers essentially by accident (a drop of Bruce's blood) and immediately outperforms the original. The show frames this as proof that the new, diverse, female version of the legacy character is inherently better than the original. No training montage, no earned competence, no struggle. The message is unsubtle: the old guard (male, legacy) is obsolete, and the replacement (female, diverse) is self-evidently superior."
        },
        {
            "id": "VV-SHULK-009",
            "name": "The Honest Worker",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": ws(2, "Moderate", "Low"),
            "explanation": "Jennifer genuinely wants to practice law and help clients. Before her transformation, she is a competent attorney who cares about her work. This is a thin traditional thread -- the dignity of honest professional work -- but it is present at the margins and prevents the tradScore from being zero."
        },
        {
            "id": "VV-SHULK-010",
            "name": "Justice as Virtue",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": ws(2, "Moderate", "Low"),
            "explanation": "The show gestures toward justice as a concept -- Jennifer is a lawyer, the legal system is the show's setting, and the finale includes a statement that wrongdoers should face consequences. But the show's meta-finale, in which Jennifer rewrites reality to give herself the ending she wants, undermines any genuine commitment to justice as an objective standard. Justice, in She-Hulk, is what the protagonist decides it is."
        }
    ]
}

# ──────────────────────────────────────────────
# VALIDATE SCORES
# ──────────────────────────────────────────────
def validate(review):
    slug = review["slug"]
    ta = review["tropeAudit"]
    woke_sum = round(sum(t["weightedScore"] for t in ta if t["category"] == "Woke"), 2)
    trad_sum = round(sum(t["weightedScore"] for t in ta if t["category"] == "Traditional"), 2)
    reported_woke = float(review["wokeScore"])
    reported_trad = float(review["tradScore"])
    reported_margin = round(reported_trad - reported_woke, 2)
    score_margin = float(review["scoreMargin"].split()[0])
    
    issues = []
    if abs(woke_sum - reported_woke) > 0.05:
        issues.append(f"WOKE drift: sum={woke_sum}, reported={reported_woke}")
    if abs(trad_sum - reported_trad) > 0.05:
        issues.append(f"TRAD drift: sum={trad_sum}, reported={reported_trad}")
    if abs(reported_margin - score_margin) > 0.05:
        issues.append(f"MARGIN drift: calc={reported_margin}, reported={score_margin}")
    
    # Verdict check
    m = reported_margin
    if m >= 20: expected = "STRONGLY TRADITIONAL"
    elif m >= 10: expected = "TRADITIONAL"
    elif m >= 3: expected = "TRADITIONAL LEAN"
    elif m >= -2: expected = "MIXED"
    elif m >= -9: expected = "WOKE LEAN"
    elif m >= -19: expected = "WOKE"
    else: expected = "STRONGLY WOKE"
    
    if review["verdict"] != expected:
        issues.append(f"VERDICT mismatch: reported={review['verdict']}, expected={expected} for margin={m}")
    
    status = "PASS" if not issues else "FAIL: " + "; ".join(issues)
    print(f"  {slug}: woke={woke_sum}/{reported_woke} trad={trad_sum}/{reported_trad} margin={reported_margin} ({review['verdict']}) -> {status}")
    return len(issues) == 0

print("VALIDATION:")
all_ok = all(validate(r) for r in [shape_of_water, gone_with_the_wind, she_hulk])

if not all_ok:
    print("FATAL: Score validation failed. Aborting.")
    exit(1)

# ──────────────────────────────────────────────
# APPEND TO reviews.json
# ──────────────────────────────────────────────
with open("src/data/reviews.json", "r") as f:
    reviews = json.load(f)

orig_len = len(reviews)
reviews.extend([shape_of_water, gone_with_the_wind, she_hulk])

with open("src/data/reviews.json", "w") as f:
    json.dump(reviews, f, indent=2, ensure_ascii=False)

print(f"\nAppended {len(reviews) - orig_len} reviews. Total: {len(reviews)}")