#!/usr/bin/env python3
"""Append 3 reviews to reviews.json and run build + git + IndexNow."""

import json, subprocess, sys, os, urllib.request
from datetime import date

REVIEWS_PATH = "src/data/reviews.json"
INDEXNOW_KEY = "c5c06a51b3df4a6fb07de4954187d031"
BASE_URL = "https://virtuevigil.com"

reviews_to_add = []

# ============================================================
# REVIEW 1: Animals (2026) — New Release
# ============================================================
reviews_to_add.append({
    "id": "animals-2026",
    "slug": "animals-2026",
    "title": "Animals",
    "year": 2026,
    "type": "film",
    "platform": "Netflix",
    "genre": "Crime Thriller",
    "date": "2026-10-13",
    "datePublished": "2026-10-13",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/animals-2026.jpg",
    "releaseDate": "October 9, 2026",
    "rating": "R",
    "runtime": "108 minutes",
    "director": "Ben Affleck",
    "writers": "Connor O. McIntyre, Billy Ray, Ben Affleck",
    "cast": ["Ben Affleck", "Kerry Washington", "Gillian Anderson", "Adriana Paz", "Luis Gerardo Méndez", "Steven Yeun"],
    "studio": "Artists Equity, Makeready, Fifth Season",
    "distributor": "Netflix",
    "verdict": "TRADITIONAL",
    "wokeScore": "6.84",
    "tradScore": "29.52",
    "scoreMargin": "+22.68 TRAD",
    "preRelease": "False",
    "wokeTrap": False,
    "woke_trap_assessment": "The film's political thriller elements (campaign corruption, wealth inequality subtext, Latino voter targeting) are present from the opening scenes. The wife's infidelity and the kidnapper's class-motivated targeting of a wealthy candidate are established early. No ideological content is concealed past the midpoint. The film's moral framework is traditional from start to finish: the corrupting nature of political ambition, the primacy of family over career, and the consequences of moral compromise.",
    "seo": {
        "titleTag": "Is Animals (2026) Woke? Ben Affleck's Netflix Kidnapping Thriller Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Animals (2026). Ben Affleck directs and stars as a mayoral candidate whose son is kidnapped in this Netflix crime thriller. VVWS verdict: TRADITIONAL (+22.68 TRAD). Parental guidance included.",
        "keywords": "is animals 2026 woke, animals 2026 review, animals ben affleck review, animals netflix thriller, animals virtuevigil, ben affleck animals parents guide, animals movie woke agenda"
    },
    "summary": {
        "overall": "Animals is Ben Affleck's sixth directorial feature, a Netflix crime thriller that places a wealthy Los Angeles mayoral candidate in the worst position imaginable: his son has been kidnapped for a ransom he cannot pay because he has already bet everything on his political future. Starring Affleck as independent candidate Mark Kimball opposite Kerry Washington as his estranged wife Abigail, the film uses Halloween night in Los Angeles as the backdrop for a story about the cost of ambition and the clarifying power of a crisis. The VVWS assessment lands at TRADITIONAL (+22.68 TRAD), reflecting a film that gestures toward class and political critique but ultimately affirms traditional moral priorities: that family outranks ambition, that infidelity carries real consequences, and that protecting the innocent is the highest moral calling.",
        "woke_score": 6.84,
        "trad_score": 29.52,
        "margin": "+22.68 TRAD",
        "adultInsight": "Animals is a crime thriller that understands something the genre often forgets: the most effective pressure on a character is not a gun to his head but a demand that forces him to choose between everything he has built and everything that actually matters. Ben Affleck's Mark Kimball is an independent candidate for mayor of Los Angeles, and in the final days of his campaign he makes the kind of decision that sounds strategic and looks catastrophic in hindsight: he commits his entire remaining savings to an aggressive Latino voter outreach, expecting to recover it all after the election. He does not tell his wife Abigail (Kerry Washington). When their son Denny is kidnapped, Mark cannot pay the $7 million ransom because he has already spent it on the campaign. The kidnap itself is a botched job: the abductors actually take Hector, the son of the Kimballs' housekeeper Cecilia and her boyfriend Ramon, having mistaken him for Denny in a Halloween costume. The film is at its most interesting here, because the moral stakes shift: Mark must now decide whether to pay to save a boy who is not his son, from a kidnapping that was meant to target him. The film's political framing is present from the start. Kimball is an independent, running outside the two-party system, and the script is smart enough to show that independence from party machinery does not mean independence from moral compromise. His campaign manager Sam (Gillian Anderson) is a cold-eyed operative who treats the kidnapping as a public relations problem. Her solution is to hire Dayle, a shadowy fixer who demands a 20 percent fee regardless of outcome. Watching Mark negotiate with Dayle over the life of a child is the film's harshest sequence, and the credit belongs to Affleck the director for not softening it. The wokeScore of 6.84 reflects elements that might read as progressive: the film's depiction of a wealthy white candidate whose fate hinges on the Latino community, the class resentment baked into the kidnapping premise, and the presence of an amoral female fixer whose competence is never questioned. But these elements are not the film's moral center. The tradScore of 29.52 reflects what the film actually cares about: the corrupting nature of ambition, the primacy of family loyalty, the moral weight of infidelity (Abigail's affair with Ron is not celebrated or excused but shown as a symptom of a marriage hollowed out by political ambition), and the idea that the measure of a man is what he sacrifices when the cost is everything. Ramon, the kidnapped boy's father, is the film's moral anchor: he is a working-class immigrant who trusts no one with his son's life and acts accordingly. For adults, Animals rewards attention to what the film refuses to say: that the system is the villain, that the rich deserve what they get, or that moral clarity is a luxury. It is a lean, proficient thriller that knows its genre beats and trusts its actors to find the emotional truth beneath the plot machinery. It is not The Town. It is not Gone Baby Gone. It is something more modest and, in its refusal to sermonize, more honest.",
        "parentalGuidance": "Animals is rated R for language, some violence, and thematic elements involving kidnapping and marital infidelity. It is not suitable for children. The film contains sustained tension around a child kidnapping: a young boy is abducted by mistake, photographs of him are sent to the parents as proof, and his father undertakes a dangerous rescue attempt. The violence is largely off-screen or implied. One character is killed; the death is brief but consequential. Language is strong throughout, consistent with a crime thriller. The marital infidelity subplot involves characters discussing an affair and a plan to divorce; no sexual content beyond brief kissing is depicted. The film treats the affair as a moral failing, not as liberating or justified. The Latino household staff characters are portrayed with dignity and agency; the class dynamic is part of the story's tension rather than a didactic lecture. Recommended for ages 16 and up. Parents should know the kidnapping premise is the central engine of the film and may be distressing even for older teens."
    },
    "tropes": [
        {"name": "Father's Ultimate Sacrifice for Family", "type": "trad", "severity": 5, "authenticity": "High", "centrality": "High", "description": "Mark Kimball's entire arc is the choice between his political future and protecting his family. When the kidnapping happens, every subsequent decision is measured against the life of a child. The film's final act is built around the question of whether he will actually pay the ransom.", "weightedScore": 6.30},
        {"name": "Family Loyalty Over Political Ambition", "type": "trad", "severity": 5, "authenticity": "High", "centrality": "High", "description": "The entire premise of the film is that Mark's political ambition has hollowed out his marriage and now threatens his family. His redemption requires abandoning the race to save a child. The film is unambiguous that family is the higher good.", "weightedScore": 6.30},
        {"name": "Consequences of Moral Failures", "type": "trad", "severity": 4, "authenticity": "High", "centrality": "High", "description": "Every bad decision in the film produces consequences. Mark's secrecy about the campaign spending, Abigail's infidelity, Sam's amoral calculus -- all of it comes due. The film operates in a moral universe where actions have consequences.", "weightedScore": 5.04},
        {"name": "Redemption Through Protective Action", "type": "trad", "severity": 4, "authenticity": "High", "centrality": "High", "description": "Mark is not redeemed by speech or sentiment but by action: choosing to pay the ransom, choosing to risk everything for a child who is not even his own. The film's traditionalism is in its insistence that redemption is earned through sacrifice.", "weightedScore": 5.04},
        {"name": "Infidelity as Moral Failure", "type": "trad", "severity": 3, "authenticity": "Moderate", "centrality": "High", "description": "Abigail's affair with Ron is depicted as a symptom of a marriage damaged by ambition and neglect, not as romantic liberation. When Mark discovers it, the scene is played as a confrontation with his own failures, not as a justification for her betrayal.", "weightedScore": 2.64},
        {"name": "Male Protector Archetype", "type": "trad", "severity": 3, "authenticity": "High", "centrality": "Moderate", "description": "Ramon, the father of the kidnapped boy, is the film's moral compass. He does not wait for the wealthy family to solve the problem; he acts. His competence, courage, and refusal to delegate his son's safety are portrayed with respect.", "weightedScore": 2.10},
        {"name": "Competence Under Pressure", "type": "trad", "severity": 3, "authenticity": "High", "centrality": "Moderate", "description": "The film values people who can act under pressure. The characters who survive and succeed are those who make clear decisions in crisis, not those who talk or negotiate or posture.", "weightedScore": 2.10},
        {"name": "Anti-Wealth and Class Resentment Subtext", "type": "woke", "severity": 3, "authenticity": "Moderate", "centrality": "High", "description": "The kidnappers target the Kimballs because they are wealthy, and the film frames the candidate's Latino voter outreach as transactional and cynical. The class dynamic between the wealthy Kimballs and their working-class household staff is present throughout.", "weightedScore": 2.64},
        {"name": "Political Corruption as Systemic Critique", "type": "woke", "severity": 3, "authenticity": "Moderate", "centrality": "Moderate", "description": "Sam the campaign manager and Dayle the fixer represent a political ecosystem where money and loyalty are the only currencies. The film suggests that politics is inherently corrupting, though it stops short of systemic condemnation.", "weightedScore": 2.10},
        {"name": "Amoral Female Operative Archetype", "type": "woke", "severity": 2, "authenticity": "Moderate", "centrality": "Low", "description": "Dayle is a female fixer whose gender is incidental to her cold competence. The film presents a woman in a traditionally male role, but her amorality is the point, not her gender.", "weightedScore": 0.70},
        {"name": "Latino Community as Political Instrument", "type": "woke", "severity": 2, "authenticity": "Low", "centrality": "Moderate", "description": "The film's plot depends on Mark's outreach to Latino voters being cynical and transactional. The Latino characters are treated with more dignity than the white political class, but the framework still positions them as a constituency to be courted.", "weightedScore": 1.40}
    ]
})

# ============================================================
# REVIEW 2: The Godfather Part III (1990) — Catalog Backfill
# ============================================================
reviews_to_add.append({
    "id": "the-godfather-part-iii-1990",
    "slug": "the-godfather-part-iii-1990",
    "title": "The Godfather Part III",
    "year": 1990,
    "type": "film",
    "platform": "Various",
    "genre": "Crime Drama, Epic",
    "date": "2026-10-13",
    "datePublished": "2026-10-13",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/the-godfather-part-iii-1990.jpg",
    "releaseDate": "December 25, 1990",
    "rating": "R",
    "runtime": "162 minutes",
    "director": "Francis Ford Coppola",
    "writers": "Mario Puzo, Francis Ford Coppola",
    "cast": ["Al Pacino", "Diane Keaton", "Talia Shire", "Andy Garcia", "Eli Wallach", "Joe Mantegna", "Bridget Fonda", "George Hamilton", "Sofia Coppola"],
    "showrunner": "None",
    "studio": "Paramount Pictures, Zoetrope Studios",
    "distributor": "Paramount Pictures",
    "verdict": "TRADITIONAL",
    "wokeScore": "4.74",
    "tradScore": "37.24",
    "scoreMargin": "+32.50 TRAD",
    "preRelease": "False",
    "wokeTrap": False,
    "woke_trap_assessment": "The film's depiction of Vatican Bank corruption is a fictionalized account of real historical events (the 1978 death of Pope John Paul I and the Papal banking scandal of 1981-1982) and is established from the opening scenes. It serves as the backdrop for Michael Corleone's attempt at legitimation, not as a lecture against the Church. The institutional corruption is the problem Michael must navigate, not a thesis the film is preaching. No woke content is concealed past the midpoint; the film's moral framework is Catholic and traditional throughout.",
    "seo": {
        "titleTag": "Is The Godfather Part III (1990) Woke? Coppola's Controversial Trilogy Finale Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of The Godfather Part III (1990). Al Pacino's Michael Corleone seeks redemption in Coppola's crime epic finale. VVWS verdict: TRADITIONAL (+32.50 TRAD). Parental guidance included.",
        "keywords": "is the godfather part iii woke, godfather 3 review, godfather part iii virtuevigil, godfather 3 woke agenda, francis ford coppola godfather, michael corleone redemption, godfather 3 parents guide"
    },
    "summary": {
        "overall": "The Godfather Part III is Francis Ford Coppola's 1990 conclusion to the Corleone family saga, completing the story of Michael Corleone's attempt to legitimize his criminal empire through a deal with the Vatican Bank. Set in 1979, the film finds Michael (Al Pacino) approaching 60, burdened by guilt over his ruthless rise to power and especially the murder of his brother Fredo. The VVWS assessment lands at TRADITIONAL (+32.50 TRAD), reflecting a film whose entire moral architecture is Catholic: sin demands consequences, redemption requires sacrifice, and no amount of money or power can buy absolution.",
        "woke_score": 4.74,
        "trad_score": 37.24,
        "margin": "+32.50 TRAD",
        "adultInsight": "The Godfather Part III has lived for 36 years under the shadow of its two predecessors, a reputation only partly deserved. Watch it now, removed from the 1990 expectations of topping two of the greatest films ever made, and what emerges is a serious, often beautiful meditation on guilt, consequence, and the impossibility of washing blood from money. Michael Corleone is a man who has won every battle and lost his soul. In Part III, he knows it. Al Pacino plays him as hollowed out, a man whose wealth and power have brought him nothing but the certainty of damnation. The plot operates on two tracks. On one, Michael negotiates a controlling interest in Internazionale Immobiliare, a Vatican-held real estate conglomerate, through a $600 million deal with Archbishop Gilday. This is the business track: the attempt to go legitimate, to convert criminal capital into respectable wealth. On the other track is Vincent Mancini (Andy Garcia), the illegitimate son of Michael's murdered brother Sonny, who arrives at a Corleone reception and immediately proves he has inherited his father's temper: he bites a rival's ear during a confrontation. Michael recognizes Sonny's fire in Vincent and, despite his misgivings, begins grooming him as successor. What makes Part III work on its own terms is the seriousness with which it takes Michael's Catholic faith. The film opens with a Papal Order induction ceremony at St. Patrick's Old Cathedral, and the rituals of confession, absolution, and final judgment are not decorative. They are the film's structuring principle. Michael wants to be forgiven. He wants to be legitimate. He wants his son Anthony to become an opera singer rather than a gangster. He wants his daughter Mary never to know what he has done. And the film's answer, as unsparing as anything in the trilogy, is that some sins cannot be forgiven in this life. The tradScore of 37.24 reflects the film's total commitment to a Catholic moral universe. Every frame assumes that actions have moral weight, that guilt is real, and that the only thing worse than the consequences of sin is the attempt to escape them. The film's seven tropes on the traditional side include Catholic Faith as Moral Framework, Consequences of Sin Across Generations, and Redemption Through Sacrifice and Confession, each at maximum severity, authenticity, and centrality. The wokeScore of 4.74 comes from three elements: the depiction of institutional church corruption (which is, in the film's defense, a dramatization of real Vatican scandals), the treatment of women as collateral damage of male violence, and the soft critique embedded in the Italian-American criminal stereotype. None of these constitute a progressive agenda. The church corruption is a plot mechanism, not a sermon. The women in the Godfather saga have always been excluded from the family's inner circle, and Part III does not celebrate this exclusion; it mourns it. The famous complaint about Part III is Sofia Coppola's performance as Mary. She is not a trained actress and it shows, but her presence in the role carries a strange, unintended weight: the director cast his own daughter as the daughter who must die for her father's sins. The final opera sequence, in which Cavalleria Rusticana plays while assassinations unfold and Mary is shot on the steps of the opera house, is the kind of operatic filmmaking Coppola does better than anyone alive. Michael's silent scream, released in the 2020 Coda recut, is one of the most devastating images in American cinema. For adults who last watched this film decades ago and dismissed it, the Coda is worth a revisit. For those who have never seen it, approach it not as a sequel that must match the first two but as an epilogue about what happens after you have won everything and discovered it was not worth winning. That is a story worth telling, and Coppola tells it with the moral seriousness that has become vanishingly rare in mainstream filmmaking.",
        "parentalGuidance": "The Godfather Part III is rated R for violence and language. It is the concluding chapter in a trilogy about organized crime, and its understanding of violence is serious rather than exploitative. The film contains several sequences of gun violence, including a helicopter attack on a mafia conference that kills multiple characters, and the climactic opera sequence in which several assassinations are intercut with a performance of Cavalleria Rusticana. The most disturbing moment is the death of Mary Corleone, who is shot on the steps of the opera house in a sequence of genuine emotional devastation. Language is consistent with a crime drama but not excessive by modern standards. There is one brief scene of a partially clothed woman; no explicit sexual content. The film's Catholic subject matter includes confession, religious ceremony, and extensive discussion of sin, guilt, and absolution. The Vatican corruption subplot may require explanation for younger viewers unfamiliar with the historical events. The film treats violence as morally weighty: every killing has consequences, and the film's thesis is that violence, however rationalized, destroys the one who commits it. Recommended for ages 16 and up. Parents should know this film assumes familiarity with the first two Godfather films; the emotional impact of Mary's death depends on understanding Michael Corleone's full arc."
    },
    "tropes": [
        {"name": "Catholic Faith as Moral Framework", "type": "trad", "severity": 5, "authenticity": "High", "centrality": "High", "description": "The film opens with a Papal Order ceremony and uses Catholic ritual (confession, absolution, last rites) as its structural spine. Michael's entire arc is a theological one: sin, guilt, attempted repentance, and the tragic truth that some sins cannot be outrun.", "weightedScore": 6.30},
        {"name": "Consequences of Sin Across Generations", "type": "trad", "severity": 5, "authenticity": "High", "centrality": "High", "description": "The film's central thesis is that Michael's sins visit tragedy upon his children. Mary's death at the opera is the price Michael pays for a lifetime of violence. The Corleone saga insists that moral debts are real and heritable.", "weightedScore": 6.30},
        {"name": "Redemption Through Sacrifice and Confession", "type": "trad", "severity": 5, "authenticity": "High", "centrality": "High", "description": "Michael's confession to Cardinal Lamberto is the film's emotional center. He names his sins, including the murder of his brother, and receives absolution -- but the film knows that absolution does not erase consequences. Redemption in this universe requires suffering.", "weightedScore": 6.30},
        {"name": "Family Loyalty Above All Else", "type": "trad", "severity": 5, "authenticity": "High", "centrality": "High", "description": "The Corleone family remains the organizing principle of the entire trilogy. Vincent's loyalty to Michael, Connie's protection of the family, and Michael's desperate love for his children are all expressions of the conviction that family is the only thing that endures.", "weightedScore": 6.30},
        {"name": "Patriarch Seeking Legitimacy and Peace", "type": "trad", "severity": 4, "authenticity": "High", "centrality": "High", "description": "Michael wants to stop being a criminal. His $600 million deal with the Vatican is not about money but about legitimacy: he wants to be remembered as something other than a gangster. The film respects this desire even as it shows its impossibility.", "weightedScore": 5.04},
        {"name": "Duty and Honor as Male Virtues", "type": "trad", "severity": 4, "authenticity": "High", "centrality": "Moderate", "description": "Vincent Mancini is introduced as a young man with his father Sonny's fire, and his arc is about learning to channel that fire into duty. The film values loyalty, courage, and the willingness to act when action is required.", "weightedScore": 2.80},
        {"name": "Opera as Transcendent Art", "type": "trad", "severity": 3, "authenticity": "High", "centrality": "Moderate", "description": "Anthony Corleone's operatic debut in Cavalleria Rusticana functions as the film's climax. Opera here represents high culture, European tradition, and the transcendence that the Corleone family has always reached for but never achieved.", "weightedScore": 2.10},
        {"name": "Legitimate Business Over Criminal Enterprise", "type": "trad", "severity": 3, "authenticity": "High", "centrality": "Moderate", "description": "The entire Immobiliare deal is Michael's attempt to convert crime proceeds into legitimate business. The film treats this as morally preferable to continued criminality, even as it acknowledges the impossibility of a clean transition.", "weightedScore": 2.10},
        {"name": "Institutional Church Corruption", "type": "woke", "severity": 3, "authenticity": "Moderate", "centrality": "High", "description": "Archbishop Gilday and elements of the Vatican Bank are depicted as corrupt and complicit in financial crimes. This is based on actual historical events (the Banco Ambrosiano scandal and the suspicious death of Pope John Paul I), not a progressive critique of the Church as institution.", "weightedScore": 2.64},
        {"name": "Women as Tragic Collateral Damage", "type": "woke", "severity": 2, "authenticity": "Moderate", "centrality": "Moderate", "description": "Mary Corleone's death is the ultimate price paid for Michael's sins. Kay is excluded from the family's inner life. The film could be read as treating women as symbols rather than agents, though Coppola's intent is tragic rather than exploitative.", "weightedScore": 1.40},
        {"name": "Italian-American Criminal Stereotype", "type": "woke", "severity": 1, "authenticity": "Low", "centrality": "Low", "description": "The Godfather trilogy has been criticized for associating Italian-American identity with organized crime. This is a legacy critique that applies to the entire trilogy, not unique to Part III, and the films' treatment of Italian culture is mostly reverent.", "weightedScore": 0.70}
    ]
})

# ============================================================
# REVIEW 3: Inside the Circle (2026) — TV/Series
# ============================================================
reviews_to_add.append({
    "id": "inside-the-circle-2026",
    "slug": "inside-the-circle-2026",
    "title": "Inside the Circle",
    "year": 2026,
    "type": "series",
    "platform": "Netflix",
    "genre": "Mystery, Thriller, Crime",
    "date": "2026-10-13",
    "datePublished": "2026-10-13",
    "author": "VirtueVigil Editorial Team",
    "readTime": "6 min read",
    "poster": "/images/posters/inside-the-circle-2026.jpg",
    "releaseDate": "October 7, 2026",
    "rating": "TV-MA",
    "runtime": "1 season",
    "director": "None",
    "writers": "Alejandro Lozano, Bernardo de la Rosa",
    "showrunner": "Alejandro Lozano",
    "cast": ["Michel Brown", "Zuria Vega", "Raúl Briones", "Osvaldo Benavides", "Jorge Zárate"],
    "studio": "Netflix",
    "distributor": "Netflix",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": "2.80",
    "tradScore": "19.14",
    "scoreMargin": "+16.34 TRAD",
    "preRelease": "False",
    "wokeTrap": False,
    "woke_trap_assessment": "The blackmail premise involving a leaked intimate video is established from the first episode. The show's moral framework -- that secrets carry consequences and that trust is the price of betrayal -- is present from the opening scenes. No progressive ideological content is concealed past the midpoint; the show is a crime thriller that uses moral questions as its engine, not a platform for social messaging.",
    "seo": {
        "titleTag": "Is Inside the Circle (2026) Woke? Netflix's Spanish-Language Blackmail Thriller Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Inside the Circle (2026). Four friends face blackmail after a leaked video threatens their secrets in this Netflix Spanish-language thriller. VVWS verdict: TRADITIONAL LEAN (+16.34 TRAD). Parental guidance included.",
        "keywords": "is inside the circle woke, inside the circle netflix review, inside the circle virtuevigil, inside the circle 2026 series, alejandro lozano netflix, spanish thriller netflix, inside the circle parents guide"
    },
    "summary": {
        "overall": "Inside the Circle is a 2026 Netflix Spanish-language crime thriller series created by Alejandro Lozano that follows four lifelong friends whose bond is tested when a leaked video threatens to expose the secrets they have kept from one another. Set in Mexico and starring Michel Brown, Zuria Vega, Raúl Briones, Osvaldo Benavides, and Jorge Zárate, the series uses the classic noir premise of hidden truths and moral compromise to explore what happens when the people who know you best become the people you can trust least. The VVWS assessment lands at TRADITIONAL LEAN (+16.34 TRAD), reflecting a show that prioritizes classic moral questions (trust, loyalty, consequences) over political messaging.",
        "woke_score": 2.80,
        "trad_score": 19.14,
        "margin": "+16.34 TRAD",
        "adultInsight": "Inside the Circle is the kind of series that Netflix has become reliably good at producing: a tight, Spanish-language crime thriller with strong local talent, a contained premise, and the confidence to let the tension build without resorting to the streaming era's worst habit of padding six episodes of story into ten. Creator Alejandro Lozano, working with co-writer Bernardo de la Rosa, has built a show around a premise that is practically a moral laboratory: what happens when the worst thing you have ever done is suddenly in the hands of someone who wants to use it against you? The four friends at the center of Inside the Circle are not strangers to one another. They have decades of shared history, and that history includes secrets that each of them has kept from the others. When a leaked video surfaces, it becomes the key that unlocks every locked door they have built. The show is structured as a pressure cooker: each episode tightens the screws on one character's secret while deepening the mystery of who is behind the blackmail. The tradScore of 19.14 reflects what the show actually values. Trust and loyalty are not just plot mechanics; they are the moral spine of the story. When a character betrays a friend, the show treats it as a genuine moral failure, not as a clever strategic move. The consequence of a broken confidence is not that someone loses leverage; it is that a relationship that took decades to build is destroyed in an instant. The show takes this seriously, and that seriousness is what separates a moral thriller from a cynical one. The wokeScore of 2.80 comes from two elements: the leaked video premise, which involves intimate content (the show treats this as a violation and a weapon, not as liberation), and the TV-MA rating, which allows for casual sexual content and language that would not be possible under stricter ratings. Neither of these constitutes a progressive agenda. The show is what it appears to be: a crime thriller about people who thought their secrets were safe. For adults who enjoy the kind of lean, foreign-language crime series that Netflix has done well with (think Criminal or The Snitch Cartel but more intimate in scope), Inside the Circle is a solid addition to the catalog. It is not groundbreaking. It is not aiming to be. It is a competent, well-acted thriller that respects the moral gravity of its premise and trusts its audience to follow the tension without being told how to feel. That is more than enough.",
        "parentalGuidance": "Inside the Circle is rated TV-MA for language, sexual content, and thematic intensity involving blackmail. It is not suitable for children or younger teenagers. The series revolves around a leaked intimate video used for blackmail, and this premise involves discussion of sexual content and the violation of privacy, though the show does not depict explicit sexual acts. Language is strong and consistent with an adult-targeted crime thriller. Violence is present but not gratuitous: the danger is primarily psychological rather than physical, with the threat of exposure functioning as the primary weapon. The show's moral framework treats betrayal of trust as genuinely consequential, which may provide productive discussion material for families with older teens about privacy, consent, and the permanent nature of digital content. The Spanish-language setting means viewers should be comfortable with subtitles or dubbing. Recommended for ages 16 and up. Parents should know the blackmail premise involves intimate material and may be triggering for viewers who have experienced similar violations."
    },
    "tropes": [
        {"name": "Trust and Loyalty as Tested Virtues", "type": "trad", "severity": 4, "authenticity": "High", "centrality": "High", "description": "The entire premise of the series is a pressure test on friendship and loyalty. When secrets emerge, the characters must decide whether their bond is stronger than their fear. The show treats loyalty as a genuine virtue, not a naive sentiment.", "weightedScore": 5.04},
        {"name": "Moral Consequences of Hidden Secrets", "type": "trad", "severity": 4, "authenticity": "High", "centrality": "High", "description": "Every character in the circle has something they are hiding, and the show's moral engine is the insistence that secrets carry weight. What you hide from the people you love will eventually find the light, and the reckoning will be proportional to the deception.", "weightedScore": 5.04},
        {"name": "Friendship Forged Through Adversity", "type": "trad", "severity": 3, "authenticity": "High", "centrality": "High", "description": "The four friends' shared history is not just backstory; it is the emotional foundation the blackmail threatens. The show values long-term friendship and the trust that only time can build.", "weightedScore": 3.78},
        {"name": "Truth as Ultimate Redemptive Force", "type": "trad", "severity": 3, "authenticity": "Moderate", "centrality": "High", "description": "The arc of the season moves toward the truth coming out, whether the characters want it to or not. The show operates on the traditional assumption that the truth, however painful, is preferable to a life built on lies.", "weightedScore": 2.64},
        {"name": "Personal Accountability for Past Actions", "type": "trad", "severity": 3, "authenticity": "Moderate", "centrality": "High", "description": "The blackmail only works because the characters have done things they are ashamed of. The show does not excuse their past actions; it demands they account for them. This is fundamentally a traditional moral framework.", "weightedScore": 2.64},
        {"name": "Leaked Intimate Content as Plot Device", "type": "woke", "severity": 2, "authenticity": "Moderate", "centrality": "Moderate", "description": "The premise involves an intimate video used for blackmail. The show treats this as a violation and a weapon, not as a commentary on sexual liberation. However, the premise itself normalizes the existence of such content in a way that traditional viewers may find uncomfortable.", "weightedScore": 1.40},
        {"name": "Casual Sexual Content and Language", "type": "woke", "severity": 2, "authenticity": "Low", "centrality": "Moderate", "description": "The TV-MA rating allows for content that is standard in adult-targeted streaming series but would be considered casual about sexuality from a traditional perspective. This is an ambient feature of the series rather than a thematic focus.", "weightedScore": 1.40}
    ]
})

# ============================================================
# Stage 1: Load and verify
# ============================================================
with open(REVIEWS_PATH) as f:
    data = json.load(f)

existing_slugs = {r["slug"] for r in data}
subprocess.run(["git", "add", "-A"], check=True)
msg = f"3 reviews: Animals (TRADITIONAL), Godfather Part III (TRADITIONAL), Inside the Circle (TRADITIONAL LEAN)"
subprocess.run(["git", "commit", "-m", msg], check=True)
subprocess.run(["git", "push"], check=True)
print("GIT PUSH OK")

# ============================================================
# Stage 5: IndexNow
# ============================================================
