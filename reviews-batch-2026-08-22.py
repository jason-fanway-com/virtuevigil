#!/usr/bin/env python3
"""Add Gladiator II review to reviews.json"""

import json

REVIEWS_PATH = "src/data/reviews.json"

with open(REVIEWS_PATH) as f:
    reviews = json.load(f)

def weighted(severity, authenticity, centrality):
    auth_map = {"High": 0.7, "Moderate": 1.0, "Low": 1.4}
    cent_map = {"High": 1.8, "Medium": 1.05, "Low": 0.4}
    a = auth_map.get(authenticity, 1.0)
    c = cent_map.get(centrality, 1.0)
    return round(severity * a * c, 2)

def compute_verdict(trad_score, woke_score):
    margin = round(trad_score - woke_score, 2)
    if margin >= 20: verdict = "STRONGLY TRADITIONAL"
    elif margin >= 10: verdict = "TRADITIONAL"
    elif margin >= 3: verdict = "TRADITIONAL LEAN"
    elif margin >= -3: verdict = "MIXED"
    elif margin >= -10: verdict = "WOKE LEAN"
    elif margin >= -20: verdict = "WOKE"
    else: verdict = "STRONGLY WOKE"
    auth = round((trad_score / (trad_score + woke_score + 0.01)) * 100)
    return verdict, margin, auth

gladiator_tropes = [
    {
        "id": "TRADITIONAL-029",
        "name": "The Principled Patriarch / Father's Legacy",
        "category": "Traditional",
        "severity": 5,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted(5, "High", "High"),
        "explanation": "The entire film revolves around Lucius discovering and embracing his identity as Maximus's son. The father's legacy is the moral and narrative engine. When Lucius finally puts on Maximus's armor and declares 'I am Maximus Decimus Meridius's son,' it is the film's emotional peak. Severity 5: this IS the movie. Authenticity High (0.7): organic to the sequel premise. Centrality High (1.8): defines every story beat."
    },
    {
        "id": "TRADITIONAL-046",
        "name": "Corruption of Power / Tyranny vs. Freedom",
        "category": "Traditional",
        "severity": 4,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted(4, "High", "High"),
        "explanation": "The twin emperors Geta and Caracalla represent decadent, unaccountable power. The film's political argument is blunt: tyranny corrupts absolutely, and free men must fight for their liberty. This is classical republicanism, not modern progressivism. Severity 4: the political framework of the film. Authenticity High (0.7): consistent with ancient Roman history. Centrality High (1.8): the rebellion drives the climax."
    },
    {
        "id": "TRADITIONAL-028",
        "name": "The Rugged Individualist",
        "category": "Traditional",
        "severity": 3,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted(3, "High", "High"),
        "explanation": "Lucius fights his way from enslaved captive to leader of a rebellion through individual will and combat prowess. He does not organize a committee. He earns respect through action. Severity 3: the gladiator genre baseline. Authenticity High (0.7): organic to the character. Centrality High (1.8): Lucius's journey is the entire narrative."
    },
    {
        "id": "TRADITIONAL-018",
        "name": "Self-Sacrifice for the Greater Good",
        "category": "Traditional",
        "severity": 3,
        "authenticity": "High",
        "centrality": "Medium",
        "weightedScore": weighted(3, "High", "Medium"),
        "explanation": "Lucilla and Lucius both risk and ultimately sacrifice for the dream of a free Rome. The film treats sacrifice for principle as the highest virtue. Severity 3: consistent throughout. Authenticity High (0.7): the original Gladiator was built on this. Centrality Medium (1.05): supports rather than drives the main arc."
    },
    {
        "id": "TRADITIONAL-044",
        "name": "The Natural Family (Reunion and Legacy)",
        "category": "Traditional",
        "severity": 4,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted(4, "High", "High"),
        "explanation": "Lucius's reunion with his mother Lucilla, his discovery of his true father, and the death of his wife at the film's opening create a web of family loyalty that drives every decision. The film treats family bonds as sacred and the severing of them as the greatest tragedy. Severity 4: the emotional core. Authenticity High (0.7): universal. Centrality High (1.8): Lucius fights for his family's legacy."
    },
    {
        "id": "WOKE-019",
        "name": "Strong Female Character (Female Gladiator / Warrior)",
        "category": "Woke",
        "severity": 2,
        "authenticity": "Moderate",
        "centrality": "Low",
        "weightedScore": weighted(2, "Moderate", "Low"),
        "explanation": "There is a female archer in the Colosseum battle sequence -- a move that departs from historical accuracy. The scene is brief, but it reads as a concession to contemporary expectations. Severity 2: a single scene. Authenticity Moderate (1.0): clearly added for modern sensibilities. Centrality Low (0.4): the archer is a background figure, not a character."
    },
    {
        "id": "WOKE-035",
        "name": "Diverse Casting Without Historical Justification",
        "category": "Woke",
        "severity": 2,
        "authenticity": "High",
        "centrality": "Medium",
        "weightedScore": weighted(2, "High", "Medium"),
        "explanation": "Denzel Washington plays Macrinus, a former slave turned arms dealer and political manipulator. The film presents Macrinus as the most cunning and dangerous character -- and he is the villain. Washington's casting is color-blind and his performance is extraordinary. The character's race is never commented upon. Severity 2: notable but narratively neutral. Authenticity High (0.7): Washington brings gravitas. Centrality Medium (1.05): Macrinus is a major character."
    },
    {
        "id": "WOKE-004",
        "name": "Dream of Rome / Democracy Worship",
        "category": "Woke",
        "severity": 1,
        "authenticity": "Moderate",
        "centrality": "Low",
        "weightedScore": weighted(1, "Moderate", "Low"),
        "explanation": "The film's climactic speech about 'the dream of Rome' -- a republic where power is shared -- could be read as a thinly veiled endorsement of democratic idealism. However, the original film had the same theme, and it is presented as classical civic virtue rather than contemporary ideology. Severity 1: benign in context. Authenticity Moderate (1.0): could read either way. Centrality Low (0.4): a speech, not a structural commitment."
    }
]

gtrad = sum(t["weightedScore"] for t in gladiator_tropes if t["category"] == "Traditional")
gwoke = sum(t["weightedScore"] for t in gladiator_tropes if t["category"] == "Woke")
gverdict, gmargin, gauth = compute_verdict(gtrad, gwoke)

gladiator = {
    "id": "gladiator-2-2024",
    "slug": "gladiator-2-2024",
    "title": "Gladiator II",
    "year": 2024,
    "type": "film",
    "genre": "Action, Epic, Historical Drama",
    "date": "2026-08-22",
    "datePublished": "2026-08-22",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min",
    "poster": "/images/posters/gladiator-2-2024.jpg",
    "director": "Ridley Scott",
    "writers": "David Scarpa",
    "cast": [
        "Paul Mescal",
        "Pedro Pascal",
        "Joseph Quinn",
        "Fred Hechinger",
        "Connie Nielsen",
        "Denzel Washington"
    ],
    "studio": "Scott Free Productions, Red Wagon Entertainment",
    "distributor": "Paramount Pictures",
    "releaseDate": "2024-11-22",
    "runtime": "2h 28m",
    "verdict": gverdict,
    "wokeScore": round(gwoke, 2),
    "tradScore": round(gtrad, 2),
    "authIndex": gauth,
    "scoreMargin": f"+{round(gmargin)} TRADITIONAL" if gmargin >= 0 else f"{round(gmargin)} WOKE",
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Gladiator II is faithful to the original's moral and political template. The traditional values -- legacy, honor, sacrifice for freedom -- are present from the opening scene and never subverted. A female gladiator in the Colosseum sequence is a brief concession to modern expectations, but it is a single scene and does not alter the film's core worldview."
    },
    "summary": {
        "overall": "Ridley Scott's Gladiator II arrives twenty-four years after its predecessor carrying one of the heaviest legacies in modern blockbuster cinema. The original Gladiator won Best Picture, made Russell Crowe a star, and left Maximus dead with nothing left to resolve. A sequel seemed impossible and perhaps unwise. And yet, Gladiator II is not the disaster logic would predict. It is a big, bloody, earnest historical epic that respects its source material and delivers exactly the kind of spectacle audiences paid for. Paul Mescal stars as Lucius, the son of Lucilla (Connie Nielsen, returning) who was sent away from Rome as a child to protect him from political enemies. Now grown and living in Numidia with a wife of his own, Lucius watches the Roman army -- led by General Acacius (Pedro Pascal) -- conquer his adopted homeland and kill his wife. Enslaved and sold to the gladiator circuit, Lucius falls under the ownership of Macrinus (Denzel Washington), a former slave turned arms dealer who sees in Lucius a weapon to aim at the twin emperors Geta (Joseph Quinn) and Caracalla (Fred Hechinger). What follows is a film that mirrors the original's structure almost beat for beat, which is both its greatest strength and its most obvious limitation. Mescal is not Crowe, but he does not need to be. His Lucius is a different kind of hero: younger, rawer, consumed by grief rather than seasoned by betrayal. Washington, meanwhile, steals every scene he is in. His Macrinus is the film's true creation -- a man who climbed out of slavery through cunning and is now using the empire's corruption to destroy it from within. His final confrontation with Lucius, fought not with swords but with words about what kind of Rome should rise from the ashes, is the film's best scene.",
        "oneLiner": "Ridley Scott's long-delayed sequel is not the equal of the original but honors its legacy with spectacle, sincerity, and a towering Denzel Washington performance.",
        "adultInsight": "The most interesting thing about Gladiator II is what it chooses not to update. Scott and writer David Scarpa could have turned this into an allegory about modern populism, or made Lucius a reluctant hero who needs convincing that violence is wrong, or given the twin emperors a redemption arc. They do none of these things. The film's moral framework is the same one that powered the original: a good man fights for his family and his freedom, and in doing so, inspires others to overthrow tyranny. It is not subtle. It was never meant to be. Where the film does show signs of its era is in small, avoidable concessions. A female archer in the Colosseum fight is ahistorical and clearly inserted for modern sensibilities. The climactic speech about 'the dream of Rome' edges close to a democratic sermon that would have been more powerful if left implicit. But these are minor irritations in a film that otherwise refuses to apologize for its traditionalism. The legacy of Maximus is not deconstructed. It is honored. That alone makes Gladiator II a rarity in 2024.",
        "parentalGuidance": "Rated R for strong, bloody violence throughout. This is a Ridley Scott historical epic: expect beheadings, impalement, sword combat, naval battle carnage, and animal attacks (including a rhinoceros rider and baboons). The violence is graphic but not sadistic. No sexual content or nudity. Language is mild for an R rating. Recommended for ages 16+. Parents should know the film's moral worldview is fundamentally traditional: a son honors his father's legacy by fighting tyranny and defending the innocent."
    },
    "tropeAudit": gladiator_tropes,
    "seo": {
        "titleTag": "Is Gladiator II (2024) Woke? Full VVWS Review | VirtueVigil",
        "metaDescription": f"VirtueVigil reviews Gladiator II (2024). Ridley Scott's sequel starring Paul Mescal and Denzel Washington honors the original's traditional values. Verdict: {gverdict} ({round(gmargin)} margin). Parental guidance included.",
        "keywords": "is gladiator 2 woke, gladiator ii review, gladiator 2 virtuevigil, gladiator 2 woke score, gladiator ii parents guide, paul mescal gladiator, denzel washington gladiator"
    },
    "parentalGuidance": "Rated R for strong, bloody violence throughout. Beheadings, impalement, sword combat, naval battle carnage, and animal attacks. No sexual content. Recommended for ages 16+.",
    "debateQuestion": "Gladiator II refuses to deconstruct its hero's legacy or apologize for celebrating masculine violence in defense of freedom. In 2024, is that artistic integrity or a missed opportunity to update the genre for modern sensibilities?"
}

reviews.append(gladiator)

# Verify no duplicates
slugs = [r["slug"] for r in reviews]
assert len(slugs) == len(set(slugs)), f"Duplicate slugs found"
assert "gladiator-2-2024" in slugs
assert "2001-a-space-odyssey-1968" in slugs
assert "shogun-s1-2024" in slugs

with open(REVIEWS_PATH, 'w') as f:
    json.dump(reviews, f, indent=2)

print(f"Total reviews: {len(reviews)}")
print(f"\nGladiator II (2024): {gverdict} ({round(gmargin)} margin, authIndex {gauth})")
print(f"  trad={round(gtrad,2)}, woke={round(gwoke,2)}")
for r in reviews[-3:]:
    assert "seo" in r and "titleTag" in r["seo"] and "metaDescription" in r["seo"] and "keywords" in r["seo"], f"SEO fail: {r['slug']}"
print("\nAll 3 reviews verified ✅")