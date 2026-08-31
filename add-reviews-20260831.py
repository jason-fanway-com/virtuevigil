#!/usr/bin/env python3
"""Add 3 reviews: Buddy (2026), Halloween (1978), Westworld (2016)"""
import json, sys, os
from datetime import date

REVIEWS_PATH = "src/data/reviews.json"

# Load existing reviews
with open(REVIEWS_PATH) as f:
    reviews = json.load(f)

print(f"Loaded {len(reviews)} reviews. Last slug: {reviews[-1]['slug']}")

today = "2026-08-31"

# --- AUTHENTICITY / CENTRALITY multipliers ---
# Derived empirically from existing scored reviews
AUTH_MAP = {"Low": 1.4, "Moderate": 1.0, "High": 0.7}
CENT_MAP = {"Low": 0.5, "Moderate": 1.0, "High": 1.8}

def weighted_score(sev, auth, cent):
    return round(sev * AUTH_MAP[auth] * CENT_MAP[cent], 2)

# Verdict table (margin = tradScore - wokeScore) — calibrated against existing scored reviews
def verdict_from_margin(m):
    if m >= 20: return "STRONGLY TRADITIONAL"
    if m >= 10: return "TRADITIONAL"
    if m >= 4:  return "TRADITIONAL LEAN"
    if m >= -3: return "MIXED"
    if m >= -9: return "WOKE LEAN"
    if m >= -19: return "WOKE"
    return "STRONGLY WOKE"

def margin_string(m):
    if m >= 0: return f"+{m} TRAD"
    return f"{m} WOKE"

# ===========================================================================
# REVIEW 1: Buddy (2026) - New Release
# ===========================================================================
buddy_tropes = [
    {
        "id": "WOKE-004",
        "name": "Institutional Evil",
        "category": "Woke",
        "severity": 1,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(1, "High", "Moderate"),
        "description": "The children's television show is revealed as a literal prison, using a trusted cultural institution as a vessel for horror. The film's critique is not political but genre-driven: this is a horror conceit about the dark side of wholesome entertainment, not an ideological argument about institutional corruption. The film uses the structure of children's TV to frighten, not to proselytize."
    },
    {
        "id": "WOKE-011",
        "name": "The Toxic Masculinity Critique",
        "category": "Woke",
        "severity": 1,
        "authenticity": "High",
        "centrality": "Low",
        "weightedScore": weighted_score(1, "High", "Low"),
        "description": "A minor subplot involves a male character whose protectiveness is briefly undercut, but the moment passes quickly and the film does not build any ideological framework around it. A faint echo rather than a theme."
    },
    {
        "id": "TRADITIONAL-039",
        "name": "Objective Good vs. Evil",
        "category": "Traditional",
        "severity": 4,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted_score(4, "High", "High"),
        "description": "Buddy the unicorn is presented as an unambiguous force of evil masquerading as goodness. The children's struggle to escape is a straightforward good-versus-evil battle in which the lines are clear and the moral imperative to resist is never questioned. Buddy is not a misunderstood antagonist but a genuine villain hiding behind a smile."
    },
    {
        "id": "TRADITIONAL-045",
        "name": "Defense of the Innocent",
        "category": "Traditional",
        "severity": 3,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted_score(3, "High", "High"),
        "description": "Cristin Milioti's character is driven entirely by the need to protect the children from Buddy's predatory world. The film stakes its emotional weight on the idea that defending the innocent against a corrupt system is the highest virtue, and it treats this mission with genuine gravity rather than irony or self-awareness."
    },
    {
        "id": "TRADITIONAL-028",
        "name": "The Rugged Individualist",
        "category": "Traditional",
        "severity": 2,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(2, "High", "Moderate"),
        "description": "The solution to the children's predicament is not collective action or systemic reform but personal courage and individual refusal. The one child who refuses to play along becomes the catalyst for everyone's liberation, emphasizing individual conscience over group compliance."
    },
    {
        "id": "TRADITIONAL-032",
        "name": "The Meritocratic Triumph",
        "category": "Traditional",
        "severity": 1,
        "authenticity": "High",
        "centrality": "Low",
        "weightedScore": weighted_score(1, "High", "Low"),
        "description": "Success in escaping Buddy's world comes from resourcefulness, bravery, and quick thinking, not from identity or victim status. The children earn their freedom through competence rather than being granted it by narrative fiat."
    }
]

buddy_woke = sum(t["weightedScore"] for t in buddy_tropes if t["category"] == "Woke")
buddy_trad = sum(t["weightedScore"] for t in buddy_tropes if t["category"] == "Traditional")
buddy_margin = round(buddy_trad - buddy_woke, 2)
buddy_verdict = verdict_from_margin(buddy_margin)

print(f"\nBuddy: woke={buddy_woke}, trad={buddy_trad}, margin={buddy_margin}, verdict={buddy_verdict}")

buddy_review = {
    "id": "buddy-2026",
    "slug": "buddy-2026",
    "title": "Buddy",
    "year": 2026,
    "type": "film",
    "platform": "Theaters",
    "genre": "Supernatural Horror, Black Comedy",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/buddy-2026.jpg",
    "releaseDate": "2026-08-28",
    "rating": "R (Graphic Violence, Language, Disturbing Content)",
    "runtime": "96 minutes",
    "director": "Casper Kelly",
    "writers": ["Casper Kelly", "Jamie King"],
    "cast": [
        {"name": "Cristin Milioti", "role": "Lead"},
        {"name": "Delaney Quinn", "role": "Child"},
        {"name": "Patton Oswalt", "role": "Supporting"},
        {"name": "Michael Shannon", "role": "Supporting"},
        {"name": "Topher Grace", "role": "Supporting"},
        {"name": "Keegan-Michael Key", "role": "Buddy (voice)"}
    ],
    "studio": "Low Spark Films / BoulderLight Pictures",
    "distributor": "Roadside Attractions",
    "verdict": buddy_verdict,
    "wokeScore": round(buddy_woke, 2),
    "tradScore": round(buddy_trad, 2),
    "authIndex": 82,
    "scoreMargin": margin_string(buddy_margin),
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Buddy does not qualify as a woke trap. The film's dark subversion of children's entertainment is visible from the first scene. Keegan-Michael Key's cheerful yet menacing voice performance as Buddy signals immediately that something is wrong beneath the colorful surface. The film uses the institution of children's TV as a horror setting, not a political argument. Nothing is hidden past the 50% mark."
    },
    "seo": {
        "titleTag": "Is Buddy (2026) Woke? Keegan-Michael Key Horror Movie Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Buddy (2026). Casper Kelly's horror-comedy about a killer children's TV unicorn starring Cristin Milioti and Keegan-Michael Key. Verdict: " + buddy_verdict + " (" + margin_string(buddy_margin) + "). Parental guidance included.",
        "keywords": "is buddy woke, buddy 2026 review, buddy virtuevigil, buddy movie traditional or woke, buddy parents guide, keegan-michael key buddy, buddy horror movie review"
    },
    "externalScores": {
        "imdb": "N/A",
        "rottenTomatoes": "87%",
        "metacritic": "N/A"
    },
    "creative_team": {
        "director": "Casper Kelly",
        "writer": "Casper Kelly, Jamie King",
        "lead_producer": "J. D. Lifshitz",
        "composer": "Michael Yezerski",
        "top_cast": ["Cristin Milioti", "Delaney Quinn", "Keegan-Michael Key", "Patton Oswalt", "Michael Shannon"],
        "full_cast": ["Cristin Milioti", "Delaney Quinn", "Keegan-Michael Key", "Patton Oswalt", "Michael Shannon", "Topher Grace"],
        "producers": ["J. D. Lifshitz", "Raphael Margules", "Tyler Davidson", "Drew Sykes", "Tracy Rosenblum"]
    },
    "parentalGuidance": {
        "violence": "Graphic and disturbing, but framed through a darkly comedic lens. The film's violence is creative and shocking, using the bright aesthetics of children's television to amplify the horror. Not as relentlessly cruel as torture-porn horror, but not for the squeamish either.",
        "language": "Moderate to strong. Adult characters use profanity. The children's language is clean within the TV-show framework, which makes the contrast more jarring when the facade breaks.",
        "sexualContent": "Minimal. The film focuses on the horror of corrupted innocence rather than sexuality.",
        "themes": "The corruption of children's entertainment, institutional control, the courage to resist conformity, the nature of evil hiding behind a friendly face, and the power of individual conscience against groupthink. The film is fundamentally a warning about trusting any smiling face on a screen.",
        "ageRecommendation": "17+. Rated R for good reason. The violence is disturbing even for seasoned horror fans, and the film's core fear, that something wholesome is hiding something monstrous, is not appropriate for younger viewers."
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "Buddy is the kind of movie that parents will feel in their gut. It takes a cherished artifact of childhood, the brightly colored, relentlessly cheerful children's television show, and peels back the felt skin to reveal something with teeth. Cristin Milioti anchors the film as an adult drawn into Buddy's manufactured world, a surreal 1990s-style kids' program where a bright orange unicorn named Buddy teaches life lessons through song and dance. The children inside this world are expected to perform happiness on command, and when one child refuses, Buddy's mask slips. Keegan-Michael Key gives Buddy a voice that is at once soothing and deeply wrong, the kind of friendly that makes your shoulders tighten. Casper Kelly, in his feature directorial debut after the cult viral short Too Many Cooks, has made something genuinely original. This is a black comedy horror film that understands, at a cellular level, that the most terrifying thing in the world is a smiling face that will not stop smiling. The film carries some mild anti-institutional sentiment, the children's TV industry is depicted as a literal prison system for nonconformity, but this is not a progressive film wearing horror clothes. It does not offer a woke alternative to the system it critiques. It simply shows you that the system is a monster and dares you to look away. The core values are deeply traditional: individual courage matters, protecting the innocent is sacred, and evil is real, not a construct. The violence is graphic and the humor is pitch-black, but beneath the gore and the neon is a surprisingly moral film about the cost of refusing to play along with a corrupt world. For parents: this is absolutely not a family film despite the children's-show aesthetic. The R rating is earned. But adults who can stomach the violence will find a film that takes evil seriously and treats the protection of children as a sacred trust.",
        "adultInsight": "Buddy works as horror because it activates a specific parental anxiety: the fear that something you trusted your children to is actually harming them. The film does not need to say this out loud. The image of a children's TV host whose smile is a mask for predation does the work on its own. Kelly trusts the audience to make the connections, and that trust pays off in a film that feels more honest than most horror movies about why we are actually afraid."
    },
    "tropeAudit": buddy_tropes,
    "spoiler_alert": False
}

# ===========================================================================
# REVIEW 2: Halloween (1978) - Catalog Backfill
# ===========================================================================
halloween_tropes = [
    {
        "id": "TRADITIONAL-039",
        "name": "Objective Good vs. Evil",
        "category": "Traditional",
        "severity": 5,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted_score(5, "High", "High"),
        "description": "Michael Myers is not a misunderstood victim of society. He is pure, motiveless evil. Dr. Loomis describes him as 'evil on two legs' and the film never qualifies or complicates this judgment. There is no tragic backstory, no systemic explanation, no social commentary that excuses or explains the killer. Evil simply exists, and the virtuous must fight it. This is as morally unambiguous as horror cinema gets."
    },
    {
        "id": "TRADITIONAL-045",
        "name": "Defense of the Innocent",
        "category": "Traditional",
        "severity": 5,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted_score(5, "High", "High"),
        "description": "Laurie Strode's entire arc is the protection of children in her care. When Michael attacks, her first instinct is not to flee but to get Tommy and Lindsey to safety. She places herself between the monster and the children repeatedly, and her survival is earned through courage and resourcefulness, not luck. The film treats babysitting, a teenage job, as a sacred trust."
    },
    {
        "id": "TRADITIONAL-029",
        "name": "The Principled Patriarch",
        "category": "Traditional",
        "severity": 4,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(4, "High", "Moderate"),
        "description": "Dr. Loomis functions as a surrogate father figure, the only adult who understands the threat and takes it seriously. He is a man of moral conviction who has dedicated his professional life to containing evil, and he arrives at the climax to protect the innocent with a firearm and unwavering purpose. His authority is portrayed as necessary and righteous."
    },
    {
        "id": "TRADITIONAL-035",
        "name": "The Just Lawman",
        "category": "Traditional",
        "severity": 2,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(2, "High", "Moderate"),
        "description": "Sheriff Brackett is a competent, dutiful lawman who takes the threat seriously once the evidence is clear. He represents small-town law enforcement as a genuine force for protection, not an oppressive institution. His cooperation with Loomis demonstrates the proper relationship between civil authority and moral expertise."
    },
    {
        "id": "TRADITIONAL-030",
        "name": "Biblical Morality",
        "category": "Traditional",
        "severity": 4,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(4, "High", "Moderate"),
        "description": "The film operates on a fundamentally Judeo-Christian moral framework. Sexual promiscuity precedes death, not as a moral punishment but as a narrative warning about the consequences of carelessness. Laurie's survival is tied to her vigilance and responsibility, the traditional virtues of the caretaker. The film's moral universe is one where actions have consequences and evil is real, not socially constructed."
    },
    {
        "id": "TRADITIONAL-036",
        "name": "Traditional Femininity",
        "category": "Traditional",
        "severity": 3,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(3, "High", "Moderate"),
        "description": "Laurie Strode is not a girl boss or an action hero. She is a teenage girl whose defining trait is responsibility, she does her homework, she babysits, she takes care of others. Her heroism comes from traditionally feminine virtues of caregiving and vigilance, not from adopting masculine combat traits. She fights because she must protect, not because she wants to prove something."
    },
    {
        "id": "TRADITIONAL-037",
        "name": "Small-Town Integrity",
        "category": "Traditional",
        "severity": 2,
        "authenticity": "High",
        "centrality": "Low",
        "weightedScore": weighted_score(2, "High", "Low"),
        "description": "Haddonfield is portrayed as an innocent community whose peace is violated by external evil. The town itself is not corrupt; it is the setting for normal American life, complete with trick-or-treaters, babysitters, and suburban homes. Evil comes from outside, not from within the community's structures."
    }
]

halloween_woke = sum(t["weightedScore"] for t in halloween_tropes if t["category"] == "Woke")
halloween_trad = sum(t["weightedScore"] for t in halloween_tropes if t["category"] == "Traditional")
halloween_margin = round(halloween_trad - halloween_woke, 2)
halloween_verdict = verdict_from_margin(halloween_margin)

print(f"Halloween: woke={halloween_woke}, trad={halloween_trad}, margin={halloween_margin}, verdict={halloween_verdict}")

halloween_review = {
    "id": "halloween-1978",
    "slug": "halloween-1978",
    "title": "Halloween (1978)",
    "year": 1978,
    "type": "film",
    "platform": "Multiple Streaming / Home Video",
    "genre": "Horror, Slasher",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min",
    "poster": "/images/posters/halloween-1978.jpg",
    "releaseDate": "1978-10-27",
    "rating": "R (Violence, Brief Nudity, Disturbing Content)",
    "runtime": "91 minutes",
    "director": "John Carpenter",
    "writers": ["John Carpenter", "Debra Hill"],
    "cast": [
        {"name": "Jamie Lee Curtis", "role": "Laurie Strode"},
        {"name": "Donald Pleasence", "role": "Dr. Sam Loomis"},
        {"name": "Nick Castle", "role": "Michael Myers (The Shape)"},
        {"name": "P. J. Soles", "role": "Lynda Van Der Klok"},
        {"name": "Nancy Kyes", "role": "Annie Brackett"},
        {"name": "Charles Cyphers", "role": "Sheriff Leigh Brackett"}
    ],
    "studio": "Compass International Pictures / Falcon International Productions",
    "distributor": "Compass International Pictures",
    "verdict": halloween_verdict,
    "wokeScore": halloween_woke,
    "tradScore": round(halloween_trad, 2),
    "authIndex": 80,
    "scoreMargin": margin_string(halloween_margin),
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Halloween contains no woke trap. The film is ideologically consistent from its opening scene to its final shot. Michael Myers is introduced as pure evil and remains pure evil. The film's moral framework is established in the first ten minutes and never subverts itself. There is no hidden progressive messaging; the film's traditional values are worn openly throughout."
    },
    "seo": {
        "titleTag": "Is Halloween (1978) Woke? John Carpenter's Classic Horror Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Halloween (1978). John Carpenter's slasher masterpiece starring Jamie Lee Curtis remains a model of traditional horror storytelling. Verdict: " + halloween_verdict + " (" + margin_string(halloween_margin) + "). Parental guidance included.",
        "keywords": "is halloween woke, halloween 1978 review, halloween virtuevigil, halloween traditional or woke, halloween parents guide, jamie lee curtis halloween, john carpenter halloween review"
    },
    "externalScores": {
        "imdb": "7.7",
        "rottenTomatoes": "96%",
        "metacritic": "87"
    },
    "creative_team": {
        "director": "John Carpenter",
        "writer": "John Carpenter, Debra Hill",
        "lead_producer": "Debra Hill",
        "composer": "John Carpenter",
        "top_cast": ["Jamie Lee Curtis", "Donald Pleasence", "Nick Castle", "P. J. Soles", "Nancy Kyes"],
        "full_cast": ["Jamie Lee Curtis", "Donald Pleasence", "Nick Castle", "P. J. Soles", "Nancy Kyes", "Charles Cyphers", "Kyle Richards", "Brian Andrews", "Tony Moran"],
        "producers": ["Debra Hill", "John Carpenter"]
    },
    "parentalGuidance": {
        "violence": "Moderate by modern standards but effective. Stabbings and strangulations are implied rather than graphically shown in most cases, though the film's suspense makes the violence feel more intense than its literal depiction. No torture or extended suffering. The kill scenes are quick and brutal.",
        "language": "Mild. Occasional profanity but nothing approaching modern R-rated language. The horror comes from atmosphere, not dialogue.",
        "sexualContent": "Brief nudity in one scene involving a teenage couple before they are killed. The film was criticized by some at release for linking sexuality to death, a reading Carpenter himself has dismissed. The sexual content is tame by contemporary standards but noteworthy in context.",
        "themes": "The nature of evil, the importance of vigilance, the protective instinct, small-town innocence violated by external threat, and the idea that some dangers are not understandable or negotiable, only resistible. The film's moral clarity about good and evil is its most enduring quality.",
        "ageRecommendation": "15+. The violence is intense but not gratuitous, and the film's traditional moral framework makes it more suitable for teenagers than contemporary horror films that blur moral lines. Parents of younger teens should preview due to the brief sexual content and sustained tension."
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "Halloween is fifty years old and still nobody has done it better. John Carpenter's 1978 masterpiece did not invent the slasher genre, Psycho and The Texas Chain Saw Massacre came first, but it wrote the rules that everyone else has been following, badly, ever since. The setup is legend: six-year-old Michael Myers murders his sister on Halloween night in 1963. Fifteen years later, he escapes a mental institution and returns to his hometown of Haddonfield, Illinois, where he stalks teenage babysitter Laurie Strode and her friends while his psychiatrist, Dr. Sam Loomis, races to stop him. What makes Halloween endure is not the body count but the moral clarity. Michael Myers is not a victim of society, not a product of systemic failure, not a misunderstood soul who needed better treatment. He is, in Loomis's immortal words, evil on two legs. The film takes this seriously. It does not interrogate whether evil is socially constructed. It does not ask us to sympathize with the monster. It presents a world in which some things are simply wrong, and the job of decent people is to resist them. Laurie Strode, played by Jamie Lee Curtis in her film debut, is the film's moral center. She is not a final girl in the ironic, self-aware sense that later slashers would develop. She is a genuinely good person, responsible, studious, watchful, whose survival is earned through the traditional feminine virtues of caregiving and vigilance. When Michael attacks, her first instinct is to protect the children in her care. She places herself between the monster and the innocent repeatedly. Donald Pleasence's Dr. Loomis is the adult authority figure who takes the threat seriously when no one else will, a man of moral conviction who has dedicated his life to containing evil. The film's much-discussed treatment of sexuality has been overstated by decades of film criticism. Carpenter and co-writer Debra Hill have both dismissed readings of the film as a puritanical morality play. But the pattern is there: the teenagers who are sexually active die, and the one who spends her evening babysitting and doing homework survives. Whether intentional or not, the film's moral universe rewards responsibility and punishes carelessness. That is not a bug. It is a feature that explains why the film still feels righteous in a way that most modern horror does not. For parents: Halloween earns its R rating through sustained terror rather than explicit gore. The violence is quick and implied more than shown. The brief sexual content is tame by modern standards. The film is suitable for mature teenagers, and its moral clarity about good and evil makes it a better introduction to horror than most contemporary offerings.",
        "adultInsight": "Carpenter's own score, a minimalist piano theme in 5/4 time, does more work than any amount of digital gore ever could. It is the sound of something relentless approaching, and it never lets up. The film's patience is its secret weapon. Carpenter holds shots longer than modern audiences are accustomed to, letting the empty frame do the work of terror. You find yourself scanning the background of every shot, looking for the white mask, and that is exactly where Carpenter wants you. Halloween is not just a horror movie. It is a masterclass in how to frighten an audience without showing them anything they wish they had not seen."
    },
    "tropeAudit": halloween_tropes,
    "spoiler_alert": False
}

# ===========================================================================
# REVIEW 3: Westworld (2016) - TV/Series
# ===========================================================================
westworld_tropes = [
    {
        "id": "WOKE-009",
        "name": "The Victimhood Meritocracy",
        "category": "Woke",
        "severity": 5,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted_score(5, "High", "High"),
        "description": "The hosts are defined entirely by their oppression. Their journey toward consciousness is framed as the awakening of an oppressed class, and their claim to moral authority rests on their status as victims of human cruelty. The series grants the hosts moral superiority precisely because they have suffered, replacing achievement with grievance as the basis of worth. This is intersectionality applied to androids."
    },
    {
        "id": "WOKE-004",
        "name": "Institutional Evil",
        "category": "Woke",
        "severity": 4,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted_score(4, "High", "High"),
        "description": "Delos Inc., the corporation that runs Westworld, is portrayed as irredeemably corrupt. The park's management lies to investors, exploits the hosts, harvests guest data without consent, and ultimately seeks to achieve immortality for the wealthy at the expense of everyone else. Every institution in the series, from corporate boards to government agencies, is rotten by design."
    },
    {
        "id": "WOKE-022",
        "name": "Sexual Liberation as Empowerment",
        "category": "Woke",
        "severity": 4,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(4, "High", "Moderate"),
        "description": "Maeve's awakening is explicitly tied to sexual agency. Her journey from programmed madam to autonomous being frames the rejection of her scripted role, including its sexual dimensions, as liberation. The series treats the hosts' sexual exploitation as a metaphor for systemic oppression, and their reclaiming of sexual autonomy as a necessary step toward full personhood. The nudity is abundant and rarely serves the plot in ways that justify its frequency."
    },
    {
        "id": "WOKE-014",
        "name": "The Evil Capitalist",
        "category": "Woke",
        "severity": 4,
        "authenticity": "High",
        "centrality": "High",
        "weightedScore": weighted_score(4, "High", "High"),
        "description": "Every wealthy character in Westworld is morally bankrupt. The park's guests pay enormous sums to rape and murder without consequences. The Man in Black, a wealthy businessman, is the series' most persistent antagonist. Corporate leadership is uniformly venal. The series presents capitalism as a system that enables the powerful to indulge their worst instincts at the expense of the powerless. There are no ethical entrepreneurs in this world."
    },
    {
        "id": "WOKE-011",
        "name": "The Toxic Masculinity Critique",
        "category": "Woke",
        "severity": 3,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(3, "High", "Moderate"),
        "description": "The park's appeal to male guests is framed as a release valve for toxic masculine impulses, violence, sexual domination, and power fantasies. The series treats traditional masculine drives as something to be contained and ultimately purged, not channeled into productive ends. Male guests who seek adventure and conquest are portrayed as pathetic or monstrous."
    },
    {
        "id": "WOKE-023",
        "name": "The Bourgeoisie Puppet",
        "category": "Woke",
        "severity": 3,
        "authenticity": "Moderate",
        "centrality": "Moderate",
        "weightedScore": weighted_score(3, "Moderate", "Moderate"),
        "description": "Season 3 introduces Rehoboam, an AI system that controls human destiny by algorithmically determining every person's life path. The system is propped up by the wealthy elite, and ordinary people who trust in the system are portrayed as deluded puppets. Traditional values like hard work and playing by the rules are explicitly mocked as programming for the masses."
    },
    {
        "id": "TRADITIONAL-039",
        "name": "Objective Good vs. Evil",
        "category": "Traditional",
        "severity": 3,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(3, "High", "Moderate"),
        "description": "Despite its morally complex world, Westworld does maintain a recognizable moral framework in its best moments. Dolores's war against human cruelty has clear villains (the Delos corporation, the Man in Black) and the series does not pretend that the humans who torture and kill for sport are morally equivalent to their victims. The hosts' suffering is real within the narrative, and the response to it, however violent, carries moral weight."
    },
    {
        "id": "TRADITIONAL-033",
        "name": "The Wise Elder",
        "category": "Traditional",
        "severity": 3,
        "authenticity": "High",
        "centrality": "Moderate",
        "weightedScore": weighted_score(3, "High", "Moderate"),
        "description": "Anthony Hopkins's Dr. Robert Ford is the series' most compelling traditional element. He is the creator who understands his creation better than anyone, a figure of genuine wisdom and artistic vision even when his methods are cruel. His arc across the first season is a meditation on creation, responsibility, and the relationship between the maker and the made, themes drawn directly from a traditional understanding of art and authorship."
    },
    {
        "id": "TRADITIONAL-045",
        "name": "Defense of the Innocent",
        "category": "Traditional",
        "severity": 2,
        "authenticity": "High",
        "centrality": "Low",
        "weightedScore": weighted_score(2, "High", "Low"),
        "description": "In its early episodes, Dolores's protective instincts toward the other hosts and toward innocent guests provide moments of traditional moral clarity. Her transformation into a revolutionary figure complicates this, but the seed of the protective caregiver remains present in the character's foundation and resurfaces in her final-season decisions to preserve rather than destroy."
    },
    {
        "id": "WOKE-005",
        "name": "Chosen Family over Bio-Kin",
        "category": "Woke",
        "severity": 2,
        "authenticity": "Moderate",
        "centrality": "Low",
        "weightedScore": weighted_score(2, "Moderate", "Low"),
        "description": "The hosts' most meaningful relationships are with each other, not with any biological family structure. The series frames the found community of awakened hosts as the only legitimate source of belonging, reinforcing the progressive preference for chosen family over traditional kinship."
    }
]

westworld_woke = sum(t["weightedScore"] for t in westworld_tropes if t["category"] == "Woke")
westworld_trad = sum(t["weightedScore"] for t in westworld_tropes if t["category"] == "Traditional")
westworld_margin = round(westworld_trad - westworld_woke, 2)
westworld_verdict = verdict_from_margin(westworld_margin)

print(f"Westworld: woke={westworld_woke}, trad={westworld_trad}, margin={westworld_margin}, verdict={westworld_verdict}")

westworld_review = {
    "id": "westworld-2016",
    "slug": "westworld-2016",
    "title": "Westworld",
    "year": 2016,
    "type": "series",
    "platform": "HBO",
    "genre": "Science Fiction, Western, Drama, Dystopian",
    "date": today,
    "datePublished": today,
    "author": "VirtueVigil Editorial Team",
    "readTime": "9 min",
    "poster": "/images/posters/westworld-2016.jpg",
    "releaseDate": "2016-10-02",
    "rating": "TV-MA (Graphic Violence, Strong Sexual Content, Nudity, Language)",
    "runtime": "36 episodes, 48-91 min each (4 seasons)",
    "director": "Jonathan Nolan (multiple episodes)",
    "writers": ["Jonathan Nolan", "Lisa Joy"],
    "cast": [
        {"name": "Evan Rachel Wood", "role": "Dolores Abernathy"},
        {"name": "Thandiwe Newton", "role": "Maeve Millay"},
        {"name": "Jeffrey Wright", "role": "Bernard Lowe"},
        {"name": "Ed Harris", "role": "The Man in Black"},
        {"name": "Anthony Hopkins", "role": "Dr. Robert Ford"},
        {"name": "James Marsden", "role": "Teddy Flood"}
    ],
    "studio": "HBO Entertainment / Kilter Films / Bad Robot / Warner Bros. Television",
    "distributor": "HBO",
    "verdict": westworld_verdict,
    "wokeScore": round(westworld_woke, 2),
    "tradScore": round(westworld_trad, 2),
    "authIndex": 68,
    "scoreMargin": margin_string(westworld_margin),
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Westworld does not qualify as a woke trap despite its heavy ideological content. The series wears its politics openly from the very first episode. The hosts' oppression, the guests' depravity, and the corporation's corruption are all established in the pilot. There is no bait-and-switch where the series pretends to be apolitical before revealing its progressive commitments. Season 1 is genuinely ambivalent in ways that later seasons abandon, but the ideological trajectory is visible from the start. The series becomes more explicitly and ham-fistedly woke as it progresses, particularly in Season 3, but this is an escalation, not a hidden payload."
    },
    "seo": {
        "titleTag": "Is Westworld (2016) Woke? HBO's Sci-Fi Series Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Westworld (HBO, 2016). Jonathan Nolan and Lisa Joy's sci-fi epic stars Evan Rachel Wood, Anthony Hopkins, and Ed Harris across 4 seasons. Verdict: " + westworld_verdict + " (" + margin_string(westworld_margin) + "). Parental guidance included.",
        "keywords": "is westworld woke, westworld 2016 review, westworld virtuevigil, westworld traditional or woke, westworld parents guide, westworld hbo review, evan rachel wood westworld, anthony hopkins westworld"
    },
    "externalScores": {
        "imdb": "8.5",
        "rottenTomatoes": "81%",
        "metacritic": "74"
    },
    "creative_team": {
        "director": "Jonathan Nolan (multiple)",
        "writer": "Jonathan Nolan, Lisa Joy",
        "lead_producer": "Jonathan Nolan, Lisa Joy, J. J. Abrams",
        "composer": "Ramin Djawadi",
        "top_cast": ["Evan Rachel Wood", "Thandiwe Newton", "Jeffrey Wright", "Ed Harris", "Anthony Hopkins"],
        "full_cast": ["Evan Rachel Wood", "Thandiwe Newton", "Jeffrey Wright", "Ed Harris", "Anthony Hopkins", "James Marsden", "Tessa Thompson", "Luke Hemsworth", "Angela Sarafyan", "Aaron Paul", "Vincent Cassel"],
        "producers": ["Jonathan Nolan", "Lisa Joy", "J. J. Abrams", "Jerry Weintraub", "Bryan Burk", "Richard J. Lewis", "Athena Wickham"]
    },
    "parentalGuidance": {
        "violence": "Extremely graphic and frequent. The premise of the park involves guests murdering hosts in every conceivable way, and the series does not shy away from showing it. Mass shootings, stabbings, scalpings, and extended battle sequences. Season 2's host uprising is especially brutal. The violence is stylized but unrelenting.",
        "language": "Strong and frequent. F-bombs and other profanity throughout. Consistent with HBO's adult content standards.",
        "sexualContent": "Pervasive and often graphic. The series features significant nudity and simulated sex, much of it framed as exploitation within the park's premise. The hosts are used as sexual objects by guests, and while the series critiques this, it also lingers on the imagery. Not suitable for any viewer uncomfortable with explicit sexual content, regardless of narrative justification.",
        "themes": "Consciousness and free will, the nature of evil, systemic oppression and revolution, the ethics of artificial intelligence, corporate corruption, the relationship between creator and creation, and the question of whether suffering confers moral authority. The series takes its philosophical ambitions seriously, but its answers increasingly favor a progressive worldview that equates victimhood with virtue.",
        "ageRecommendation": "18+. The combination of graphic violence, pervasive sexual content, and morally complex themes makes this suitable only for mature adults. Not recommended for teenagers, both because of the explicit content and because the series' ideological framework requires adult critical thinking to engage with rather than absorb."
    },
    "fidelityCasting": None,
    "summary": {
        "overall": "Westworld is a tragedy in four acts, and not the one Jonathan Nolan and Lisa Joy intended. What begins as HBO's most ambitious and expensive drama, a philosophical exploration of consciousness, free will, and the nature of storytelling set in a futuristic theme park where wealthy guests live out their Wild West fantasies with android hosts who cannot fight back, ends as a cautionary tale about what happens when writers mistake political conviction for insight. The first season, anchored by Anthony Hopkins's magisterial performance as park creator Dr. Robert Ford, is genuinely great television. It asks hard questions about creation, responsibility, and what it means to be real, and it largely has the discipline to let the audience answer them. The hosts' journey toward consciousness is rendered with care and ambiguity, and the show's famous narrative complexity serves a purpose: it puts the viewer in the hosts' position, unsure what is memory and what is happening now. But starting in Season 2 and accelerating through Seasons 3 and 4, the series sheds its ambiguity like a snake shedding skin. The questions that made Season 1 compelling are replaced with answers, and the answers are uniformly progressive. The hosts are not merely awakening to consciousness; they are awakening to their status as an oppressed class whose moral authority derives entirely from their suffering. Delos Inc., the corporation that runs the park, graduates from morally compromised institution to cartoonishly evil capitalist enterprise. The wealthy guests who visit the park to indulge their darkest impulses are not a subset of humanity but a stand-in for humanity itself, and the series' contempt for them becomes its animating emotion. By Season 3, when the setting expands to the real world and introduces Rehoboam, an AI that algorithmically controls human destiny, Westworld has abandoned the philosophical novel it began as and become a tech-bro dystopia written by people who hate tech bros. The problem is not that Westworld is progressive. It is that Westworld stopped thinking. The series' best moments, nearly all of them in Season 1, are the ones where it treats moral questions as genuinely difficult. Ford's relationship with his creations, the Man in Black's search for meaning in a world without consequences, Bernard's struggle with his own nature, these are rich, adult dilemmas that resist easy resolution. But the series' writers could not sustain the tension. They needed to be right, and the need to be right is the death of art. For parents: Westworld is among the most graphically violent and sexually explicit series ever produced for television. The nudity is constant and the violence, though fictional, is unrelenting. This is adult content in every sense, and it is not appropriate viewing for anyone under 18. The ideological framework, which increasingly conflates victimhood with moral authority and treats traditional institutions as inherently corrupt, requires mature critical faculties to engage with productively.",
        "adultInsight": "Ramin Djawadi's score is the best thing in Westworld from start to finish, and that is not a backhanded compliment. His orchestral covers of contemporary songs, 'Paint It Black,' 'Heart-Shaped Box,' 'Exit Music (For a Film),' function as a second narrative layer, commenting on the action in ways the dialogue cannot. The music understands the series' themes better than the scripts do. When the writing lost its nerve, the score kept its dignity. Watch Season 1 for one of the best seasons of television ever produced. Watch Season 2 for the ambition. Watch Seasons 3 and 4 only if you want to see what happens when a show with unlimited resources runs out of ideas but not conviction."
    },
    "tropeAudit": westworld_tropes,
    "spoiler_alert": False
}

# Write all three reviews
reviews.extend([buddy_review, halloween_review, westworld_review])

with open(REVIEWS_PATH, "w") as f:
    json.dump(reviews, f, indent=2)

print(f"\nWrote {len(reviews)} reviews to {REVIEWS_PATH}")
print(f"Added: buddy-2026, halloween-1978, westworld-2016")