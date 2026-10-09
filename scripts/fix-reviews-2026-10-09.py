#!/usr/bin/env python3
"""Fix the 3 just-added reviews: add adultInsight/parentalGuidance, fix pre-release verdict prefix."""

import json

REVIEWS_PATH = "src/data/reviews.json"

with open(REVIEWS_PATH) as f:
    reviews = json.load(f)

targets = ['x-men-2000', 'loki-2021', 'blood-sacrifice-2026']

additions = {
    'x-men-2000': {
        'adultInsight': "X-Men (2000) is a rare example of a superhero film that delivers a social allegory without making the allegory the entire point. The discrimination metaphor is the story's engine, but it does not override character or spectacle. Bryan Singer understood that audiences come for Wolverine's claws, not for a lecture on tolerance, and the film's restraint is its greatest virtue. Parents considering this for family viewing should know that beneath the superhero action is a film that treats good and evil as real categories, that values self-sacrifice over grievance, and that presents Xavier's school as a place where lost kids find discipline and purpose. In 2026, that combination is harder to find than it should be. The film earns its BALANCED TRADITIONAL score because the progressive framework is there, but it is held in tension with genuinely traditional moral instincts. That tension is what makes the movie work -- and what makes it feel, 26 years later, like a relic of a less ideologically predictable era.",
        'parentalGuidance': "X-Men (2000) is rated PG-13 for sci-fi action violence. The combat is comic-book stylized: energy blasts, claws, fistfights, no blood or gore. There is a brief but intense scene where Rogue absorbs her boyfriend's life force through a kiss, putting him in a coma, which may frighten younger viewers. Magneto's backstory as a Holocaust survivor is handled with gravity and includes a brief concentration camp scene with a child being separated from his parents. The film deals with themes of discrimination, forced registration of a minority group, and political demagoguery, which parents may want to discuss with kids old enough to engage with those ideas. Wolverine's amnesia implies a history of violence and experimentation. One character (Mystique) appears nude but covered in blue scales with no visible anatomy. There is no sexual content, no drug use, and minimal language. Recommended for ages 10 and up with parental discussion."
    },
    'loki-2021': {
        'adultInsight': "Loki is the Marvel Disney+ series that proves the franchise can still produce emotionally honest storytelling when it stops worrying about message delivery and commits to character. The progressive elements are present and undeniable -- the gender-fluid signaling, the girlboss variant, the dismantle-the-system framework -- but they are not the point. The point is a man who spent a thousand years as a villain learning, across 12 episodes, that he is capable of love and worthy of redemption. That arc works because Tom Hiddleston and the writers believe in it, not because it checks a diversity box. For parents, Loki offers something rare in the current Marvel lineup: a story about moral transformation that treats transformation as hard, earned, and worthwhile. The finale's emotional power comes from Loki choosing sacrifice over self-interest, and the series does not undermine that moment with a quip. In an era where studios seem embarrassed by sincerity, Loki lets its hero be sincere and lets the audience feel it.",
        'parentalGuidance': "Loki is rated TV-14 for sci-fi violence, thematic elements, and mild language. The violence is Marvel-standard: energy weapons, hand-to-hand combat, magical blasts, and several on-screen deaths. One sequence involves a character being 'pruned' (erased from existence) while conscious and visible; this may disturb younger viewers. There are existential themes about mortality, free will, and the meaning of identity that younger children will not follow. The series includes one kiss (Loki and Sylvie, who is a variant of himself) and no sexual content. There is a brief gag about Loki's genitals in the context of a TVA file, played for comedy. One character (Jonathan Majors) was later convicted of domestic assault, which parents may want to discuss with teens in the context of separating art from artist. The series is darker and more philosophical than most Marvel content. Recommended for ages 13 and up."
    },
    'blood-sacrifice-2026': {
        'adultInsight': "Blood Sacrifice arrives with a strong traditional premise and significant execution risk. The father-son detective framework is a story engine that has powered everything from The Searchers to True Detective -- two men, broken apart by pride or history, forced back together by a crime that only they can solve. That is not ideology; it is anthropology. The risk, as with any 2026 Netflix production, is that the estrangement becomes a vehicle for therapeutic language about male emotional deficiency rather than a genuine exploration of two stubborn men learning to trust each other again. George Kay's track record suggests a competent writer who defaults to progressive casting but does not make essays out of his thrillers. The Swedish setting introduces another variable: Nordic crime dramas have a history of embedding social-democratic messaging about immigration, gender, and institutional authority. Whether Blood Sacrifice follows that tradition or resists it will determine whether this score holds. As always, VirtueVigil will update this review after full viewing -- pre-release assessments carry a structural humility that post-release reviews do not need.",
        'parentalGuidance': "Blood Sacrifice is rated TV-MA for violence, language, and likely disturbing content consistent with Nordic noir traditions. The crime-thriller framework means depictions of murder victims, crime scenes, and sustained psychological tension. Swedish crime dramas are known for unflinching portrayals of violence and their willingness to explore dark psychological territory. This is not a family watch. Expect subtitled Swedish dialogue alongside English. Sexual content is possible but not confirmed. The series deals with murder investigation as its central premise, and children should not be present for viewing. Recommended for adults only. Pre-release assessment -- this guidance will be updated after full viewing."
    }
}

for r in reviews:
    if r['slug'] in targets:
        r['summary']['adultInsight'] = additions[r['slug']]['adultInsight']
        r['summary']['parentalGuidance'] = additions[r['slug']]['parentalGuidance']
        # Fix Blood Sacrifice pre-release verdict
        if r['slug'] == 'blood-sacrifice-2026' and not r['verdict'].startswith('PREDICTED'):
            r['verdict'] = 'PREDICTED: ' + r['verdict']
        print(f"Fixed: {r['slug']}")

with open(REVIEWS_PATH, 'w') as f:
    json.dump(reviews, f, indent=2)

print("Done fixing. Rebuilding...")