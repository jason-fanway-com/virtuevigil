#!/usr/bin/env python3
"""Append 3 reviews to reviews.json for 2026-09-30 -- one per commit."""

import json, subprocess, sys, os
from datetime import date

REVIEWS_PATH = "src/data/reviews.json"
REPO = "/Users/joestrazza/virtuevigil"
TODAY = "2026-09-30"

# VVWS multipliers
AUTH_MAP = {"High": 1.0, "Moderate": 0.6, "Low": 0.3}
CENT_MAP = {"High": 1.05, "Moderate": 0.6, "Low": 0.2}

def ws(severity, authenticity, centrality):
    """Compute weighted score."""
    return round(severity * AUTH_MAP[authenticity] * CENT_MAP[centrality], 2)

def verdict_from_margin(margin):
    if margin >= 25:
        return "STRONGLY TRADITIONAL"
    elif margin >= 20:
        return "TRADITIONAL"
    elif margin >= 5:
        return "BALANCED TRADITIONAL"
    elif margin >= 2:
        return "TRADITIONAL LEAN"
    elif margin >= -1:
        return "BALANCED"
    elif margin >= -4:
        return "WOKE LEAN"
    elif margin >= -9:
        return "BALANCED WOKE"
    elif margin >= -19:
        return "WOKE"
    else:
        return "STRONGLY WOKE"

def format_margin(margin):
    if margin > 0:
        sm = f"+{margin:.0f}" if margin == int(margin) else f"+{margin:.2f}"
        return f"{sm} TRAD"
    elif margin < 0:
        sm = f"{margin:.0f}" if margin == int(margin) else f"{margin:.2f}"
        return f"{sm} WOKE"
    else:
        return "0 BALANCED"

# ============================================================
# REVIEW 1: The Mummy (1999)
# ============================================================
mummy_tropes = [
    {"id": "MUMMY-TRAD-001", "name": "The Rugged Individualist", "category": "Traditional",
     "severity": 4, "authenticity": "High", "centrality": "High",
     "weightedScore": ws(4, "High", "High"),
     "explanation": "Rick O'Connell is the classic American adventure hero -- a former Legionnaire who survives by his wits and courage, leads by instinct, and never waits for permission. His individual competence is the engine that saves everyone."},
    {"id": "MUMMY-TRAD-002", "name": "Heterosexual Romance as Organizing Principle", "category": "Traditional",
     "severity": 3, "authenticity": "High", "centrality": "High",
     "weightedScore": ws(3, "High", "High"),
     "explanation": "The Rick-Evelyn romance is the emotional core of the film -- it motivates Rick's heroism, grounds Evelyn's arc, and resolves at the climax with a kiss in the treasure chamber. The romance is treated as aspirational, not ironic."},
    {"id": "MUMMY-TRAD-003", "name": "Objective Good vs. Evil", "category": "Traditional",
     "severity": 3, "authenticity": "High", "centrality": "Moderate",
     "weightedScore": ws(3, "High", "Moderate"),
     "explanation": "Imhotep is unambiguous evil -- he wants to unleash the plagues of Egypt upon the world. The heroes fight him not because the system made him, but because he is a threat to the innocent that must be stopped."},
    {"id": "MUMMY-TRAD-004", "name": "Defense of the Innocent", "category": "Traditional",
     "severity": 2, "authenticity": "High", "centrality": "Moderate",
     "weightedScore": ws(2, "High", "Moderate"),
     "explanation": "Rick repeatedly risks his life to protect Evelyn, Jonathan, and ultimately the world from Imhotep. His motivation is not ideology but the simple imperative to defend those who cannot defend themselves."},
    {"id": "MUMMY-TRAD-005", "name": "Traditional Femininity", "category": "Traditional",
     "severity": 2, "authenticity": "Moderate", "centrality": "Moderate",
     "weightedScore": ws(2, "Moderate", "Moderate"),
     "explanation": "Evelyn is brilliant and bookish -- an Egyptologist -- but she is also feminine, romantic, and never masculinized. She screams, she needs rescue, she wears a dress, and none of this undercuts her intelligence."},
    {"id": "MUMMY-TRAD-006", "name": "Masculine Courage", "category": "Traditional",
     "severity": 3, "authenticity": "High", "centrality": "Moderate",
     "weightedScore": ws(3, "High", "Moderate"),
     "explanation": "Rick's physical courage is the film's action backbone -- gunfights, fistfights, and facing the undead without flinching. His bravery is treated as admirable, not toxic, and it inspires everyone around him."},
    {"id": "MUMMY-WOKE-001", "name": "Colonial/Imperial Guilt", "category": "Woke",
     "severity": 1, "authenticity": "Low", "centrality": "Low",
     "weightedScore": ws(1, "Low", "Low"),
     "explanation": "The British and American characters are treasure hunters in colonial-era Egypt (1926). The film does not critique this -- the colonial presence is background setting, played for comedy (the foppish Brits) rather than moral reckoning."},
]

mummy_trad = sum(t["weightedScore"] for t in mummy_tropes if t["category"] == "Traditional")
mummy_woke = sum(t["weightedScore"] for t in mummy_tropes if t["category"] == "Woke")
mummy_margin = round(mummy_trad - mummy_woke, 2)
mummy_margin_str = format_margin(mummy_margin)
mummy_verdict = verdict_from_margin(mummy_margin)

review_mummy = {
    "id": "the-mummy-1999",
    "slug": "the-mummy-1999",
    "title": "The Mummy (1999)",
    "year": 1999,
    "type": "film",
    "platform": "Streaming",
    "genre": "Action Adventure Horror",
    "date": TODAY,
    "datePublised": TODAY,
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/the-mummy-1999.jpg",
    "releaseDate": "1999-05-07",
    "rating": "PG-13",
    "runtime": "125 min",
    "director": "Stephen Sommers",
    "writers": ["Stephen Sommers", "Lloyd Fonvielle", "Kevin Jarre"],
    "showrunner": None,
    "cast": ["Brendan Fraser", "Rachel Weisz", "John Hannah", "Arnold Vosloo", "Oded Fehr", "Jonathan Hyde", "Kevin J. O'Connor"],
    "studio": "Universal Pictures / Alphaville Films",
    "distributor": "Universal Pictures",
    "verdict": mummy_verdict,
    "wokeScore": mummy_woke,
    "tradScore": mummy_trad,
    "authIndex": round(mummy_trad / (mummy_trad + mummy_woke) * 100) if (mummy_trad + mummy_woke) > 0 else 50,
    "scoreMargin": mummy_margin_str,
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "No hidden woke content. The film is a straightforward adventure from start to finish with no late-act ideological pivot.",
    "tropeAudit": mummy_tropes,
    "summary": {
        "overall": "The Mummy is Stephen Sommers's 1999 reimagining of Universal's 1932 horror classic, and it arrived at exactly the right cultural moment -- the last gasp of the pre-9/11 action-adventure blockbuster, when a movie could be scary, funny, romantic, and swashbuckling all at once without apologizing for any of it. Brendan Fraser stars as Rick O'Connell, an American adventurer and former Legionnaire who leads a pair of British siblings -- librarian Egyptologist Evelyn Carnahan (Rachel Weisz) and her cowardly-charming brother Jonathan (John Hannah) -- to the lost city of Hamunaptra. There they accidentally resurrect Imhotep (Arnold Vosloo), an ancient high priest cursed for murdering the pharaoh, who now seeks to restore his lost love by sacrificing Evelyn and unleashing the plagues of Egypt. What follows is one of the most purely enjoyable blockbusters of the 1990s: a film that knows exactly what it is and never pretends otherwise. The $80 million budget returned $422 million worldwide and launched a franchise that defined adventure cinema for a generation.",
        "traditionalContent": "The Mummy is built entirely on a traditional moral chassis. Rick O'Connell is the rugged individualist par excellence -- he does not wait for orders, he does not seek approval, and he does not justify his courage with ideology. He fights because people need protecting. Evelyn is brilliant and bookish, the intellectual engine of the expedition, but her femininity is never sanded off in the name of empowerment. She screams, she needs rescue, she wears a dress to the climax -- and none of this diminishes her. The film treats her competence as natural rather than a political statement. The romance between Rick and Evelyn is the film's emotional spine: it is played straight, treated as aspirational, and resolved with a kiss in the treasure chamber. Imhotep is unambiguous evil -- a high priest who murdered his pharaoh and now seeks to sacrifice an innocent woman to resurrect his lost love. There is no moral ambiguity about stopping him. The Medjai, led by Ardeth Bay (Oded Fehr), are guardians of sacred duty, not victims of colonialism -- they are warriors who have protected the world for millennia. The film's values are courage, loyalty, romance, and the defense of the innocent. It asks nothing more complicated of its audience than to root for the good guys.",
        "wokeContent": "The woke case against The Mummy is thin to the point of transparency. The film is set in 1926 colonial Egypt, and the heroes are British and American treasure hunters who treat Egyptian antiquities as loot. But the film does not treat this as a moral crime to be prosecuted -- it treats it as the premise for an adventure story. The British comic-relief characters (including Jonathan) are feckless and greedy, and the one genuinely greedy American (Beni, played by Kevin J. O'Connor) dies horribly as a direct consequence of his betrayal. The Medjai are the most honorable characters in the film. If there is a colonial critique embedded, it is so submerged and inconsistent as to be invisible. Some viewers might flag Evelyn as a proto-girl-boss because she is intelligent and drives the intellectual half of the expedition, but the film never frames her competence as a challenge to male authority -- it frames it as charming and essential to the mission. She is respected because she is good at her job, not because the film is making a political point about women in academia."
    },
    "parentalGuidance": "The Mummy is rated PG-13 for pervasive adventure violence and some partial nudity. The violence is mostly swashbuckling in tone -- gunfights, fistfights, sword fights -- with little gore. The scarab beetles burrowing under skin is the most disturbing image and may frighten younger viewers. Imhotep's partially decomposed form is grotesque but not nightmare-inducing for most kids. There is mild sexual innuendo and one scene of implied nudity (Evelyn in translucent nightwear). The film uses mild profanity. Suitable for ages 10 and up. Parents should know the film treats ancient Egyptian religion respectfully and the Medjai as honorable guardians -- it is not dismissive of Middle Eastern culture.",
    "seo": {
        "titleTag": "Is The Mummy (1999) Woke? Brendan Fraser's Action Classic Reviewed | VirtueVigil",
        "metaDescription": f"VirtueVigil VVWS review of The Mummy (1999). Brendan Fraser and Rachel Weisz star in Stephen Sommers's adventure classic. Verdict: {mummy_verdict} ({mummy_margin_str}). Parental guidance included.",
        "keywords": ["is the mummy woke", "the mummy 1999 review", "the mummy virtuevigil", "the mummy traditional or woke", "the mummy parents guide", "brendan fraser the mummy", "stephen sommers the mummy"]
    }
}

# ============================================================
# REVIEW 2: Yellow Eyes (2026)
# ============================================================
yellow_eyes_tropes = [
    {"id": "YE-TRAD-001", "name": "Objective Good vs. Evil", "category": "Traditional",
     "severity": 3, "authenticity": "High", "centrality": "High",
     "weightedScore": ws(3, "High", "High"),
     "explanation": "The ancient cursed artifact represents unambiguous supernatural evil threatening the young couple. The film operates on a clear moral axis: the artifact is dangerous and must be contained or destroyed, and the protagonists are innocent people caught in its wake."},
    {"id": "YE-TRAD-002", "name": "Defense of the Innocent", "category": "Traditional",
     "severity": 3, "authenticity": "High", "centrality": "Moderate",
     "weightedScore": ws(3, "High", "Moderate"),
     "explanation": "Julia and Brad are ordinary people thrust into supernatural danger. Their primary motivation throughout is protecting each other -- not ideological grievance, not systemic complaint, but the primal human imperative to defend the person you love."},
    {"id": "YE-TRAD-003", "name": "Heterosexual Romance as Organizing Principle", "category": "Traditional",
     "severity": 2, "authenticity": "High", "centrality": "High",
     "weightedScore": ws(2, "High", "High"),
     "explanation": "The film centers on a young heterosexual couple whose relationship is tested by supernatural horror. Their bond is the emotional stakes of the story -- if they survive together, the audience wins. No deconstruction, no ironic distance."},
    {"id": "YE-TRAD-004", "name": "Respect for rural working-class life", "category": "Traditional",
     "severity": 1, "authenticity": "Moderate", "centrality": "Low",
     "weightedScore": ws(1, "Moderate", "Low"),
     "explanation": "The rural New England setting is treated with atmospheric seriousness rather than condescension -- it is isolated and dangerous, but never mocked. The inherited property carries weight and history."},
    {"id": "YE-TRAD-005", "name": "Family Loyalty", "category": "Traditional",
     "severity": 2, "authenticity": "Moderate", "centrality": "Low",
     "weightedScore": ws(2, "Moderate", "Low"),
     "explanation": "The inheritance of the rural property anchors the narrative in family legacy, however cursed. The couple's commitment to building a life together on this inherited land is treated as a meaningful, not ironic, aspiration."},
    {"id": "YE-WOKE-001", "name": "General Woke Element (Diverse Ensemble Casting)", "category": "Woke",
     "severity": 1, "authenticity": "Low", "centrality": "Low",
     "weightedScore": ws(1, "Low", "Low"),
     "explanation": "The cast includes actors of diverse backgrounds (Nena Martins, Jimmy Chung, DeVaughn Loman) in an indie horror production. This appears to be organic casting rather than a diversity mandate -- no character's race is made into a plot point."},
]

ye_trad = sum(t["weightedScore"] for t in yellow_eyes_tropes if t["category"] == "Traditional")
ye_woke = sum(t["weightedScore"] for t in yellow_eyes_tropes if t["category"] == "Woke")
ye_margin = round(ye_trad - ye_woke, 2)
ye_margin_str = format_margin(ye_margin)
ye_verdict = verdict_from_margin(ye_margin)

review_yellow_eyes = {
    "id": "yellow-eyes-2026",
    "slug": "yellow-eyes-2026",
    "title": "Yellow Eyes (2026)",
    "year": 2026,
    "type": "film",
    "platform": "Streaming",
    "genre": "Supernatural Horror",
    "date": TODAY,
    "datePublised": TODAY,
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/yellow-eyes-2026.jpg",
    "releaseDate": "2026-08-18",
    "rating": "Not Rated",
    "runtime": "86 min",
    "director": "Jesse Korman",
    "writers": ["Mickey Solis"],
    "showrunner": None,
    "cast": ["Nena Martins", "Michael Kunicki", "Margo O'Connell", "Jimmy Chung", "Brian Rooney"],
    "studio": "Terror Town / Great Escape / Yale Productions",
    "distributor": "Inaugural Entertainment",
    "verdict": ye_verdict,
    "wokeScore": ye_woke,
    "tradScore": ye_trad,
    "authIndex": round(ye_trad / (ye_trad + ye_woke) * 100) if (ye_trad + ye_woke) > 0 else 50,
    "scoreMargin": ye_margin_str,
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "No hidden ideological content. The film is a straightforward supernatural horror that stays within genre conventions from opening to closing credits.",
    "tropeAudit": yellow_eyes_tropes,
    "summary": {
        "overall": "Yellow Eyes is a 2026 independent supernatural horror film from director Jesse Korman that arrived on Screambox in August 2026 with little fanfare but a clear sense of what kind of movie it wants to be: an old-fashioned possession-and-curse story shot through with the gritty, DIY texture of the modern indie horror scene. Produced by mumblecore veteran Joe Swanberg and written by Mickey Solis, it stars Nena Martins and Michael Kunicki as Julia and Brad, a young couple whose lives unravel after they inherit a remote New England property that turns out to be home to an ancient, cursed artifact. At 86 minutes, the film moves briskly and wears its influences on its sleeve without descending into pastiche. The score, featuring contributions from Korman's own mathcore band The Number Twelve Looks Like You, gives the film a jagged, contemporary energy that distinguishes it from the orchestral grandiosity of studio horror. Critics noted the film's willingness to avoid standard exorcism cliches -- no Latin chanting, no victims tied to bedposts -- in favor of a darker, character-driven approach.",
        "traditionalContent": "Yellow Eyes anchors itself in one of the oldest and most reliable moral frameworks in horror: ordinary people confronting extraordinary evil and discovering what they are made of in the process. Julia and Brad are not activists, not grievance-bearers, and not characters whose identities are defined by group membership. They are a couple who inherit a cursed property and must survive it. The film's moral engine is defense of the innocent -- Brad protecting Julia, Julia refusing to abandon Brad, both of them fighting to preserve the life they planned together. There is no systemic critique, no political allegory, no institutional villain behind the supernatural threat. The evil is ancient, pre-political, and indifferent to human social arrangements. This is horror as moral testing ground: the characters are measured by their courage, their loyalty, and their refusal to give up on each other. The rural New England setting is treated as genuinely threatening and genuinely beautiful -- not as a symbol of backwardness to be escaped. The film respects the isolation and history of the land in a way that feels grounded rather than performative.",
        "wokeContent": "Yellow Eyes is about as ideologically inert as a horror film can be in 2026. It has no political message, no social commentary, and no identity-politics framework. The diverse casting of the ensemble -- Nena Martins, Jimmy Chung, DeVaughn Loman -- appears to be the result of normal casting decisions rather than a diversity mandate, and no character's race or background is made into a narrative point. The one element that could be read through a woke lens is the film's reported desire to subvert horror cliches, but this is a creative ambition, not a political one: avoiding tired exorcism tropes is a craft decision, not an ideological statement. The film's female lead, Julia, is neither a girl-boss nor a passive victim -- she is simply a person in danger, fighting to survive, which is what horror protagonists have been for decades. The absence of woke content is not an oversight. It is the natural result of a film whose ambition is to scare you, not lecture you."
    },
    "parentalGuidance": "Yellow Eyes is an unrated independent horror film with supernatural horror content typical of the possession subgenre. Expect jump scares, disturbing imagery involving the cursed artifact, and sustained tension. The film reportedly avoids the more graphic extremes of the genre -- no extended torture, no sexual violence -- but the psychological horror of a couple trapped with an ancient evil will be intense for younger viewers. There may be some strong language and brief violence. Best suited for horror fans 15 and up. Parents should know the film draws on traditional supernatural horror tropes (cursed objects, rural isolation, ancient evil) without the nihilistic cruelty that marks some modern horror.",
    "seo": {
        "titleTag": "Is Yellow Eyes (2026) Woke? Screambox Horror Review | VirtueVigil",
        "metaDescription": f"VirtueVigil VVWS review of Yellow Eyes (2026), the indie supernatural horror from director Jesse Korman. Verdict: {ye_verdict} ({ye_margin_str}). Parental guidance included.",
        "keywords": ["is yellow eyes woke", "yellow eyes 2026 review", "yellow eyes virtuevigil", "yellow eyes horror movie", "yellow eyes parents guide", "jesse korman yellow eyes", "screambox yellow eyes"]
    }
}

# ============================================================
# REVIEW 3: The Day of the Jackal (2024)
# ============================================================
jackal_tropes = [
    {"id": "JACKAL-TRAD-001", "name": "Competence as Virtue", "category": "Traditional",
     "severity": 4, "authenticity": "High", "centrality": "High",
     "weightedScore": ws(4, "High", "High"),
     "explanation": "Both the Jackal and Bianca are defined entirely by professional excellence. The Jackal's precision as an assassin is treated with genuine admiration, and Bianca's detective work as an MI6 agent is shown as demanding and impressive. The show's central rivalry is a contest of skill, not ideology."},
    {"id": "JACKAL-TRAD-002", "name": "Male competence as narrative engine", "category": "Traditional",
     "severity": 3, "authenticity": "High", "centrality": "High",
     "weightedScore": ws(3, "High", "High"),
     "explanation": "Eddie Redmayne's Jackal drives the plot through his extraordinary abilities -- disguise, marksmanship, tradecraft. The show does not apologize for making a male assassin the most compelling character on screen. His skill is the show's gravitational center."},
    {"id": "JACKAL-TRAD-003", "name": "Duty and Protection", "category": "Traditional",
     "severity": 2, "authenticity": "Moderate", "centrality": "Moderate",
     "weightedScore": ws(2, "Moderate", "Moderate"),
     "explanation": "Bianca's pursuit of the Jackal is framed as professional duty -- she takes the assignment seriously and is willing to sacrifice for it. The Jackal's motivations, partially rooted in protecting his family, echo a traditional framework even when the actions are monstrous."},
    {"id": "JACKAL-TRAD-004", "name": "Loyalty to teammates", "category": "Traditional",
     "severity": 2, "authenticity": "Moderate", "centrality": "Low",
     "weightedScore": ws(2, "Moderate", "Low"),
     "explanation": "Bianca's loyalty to her MI6 team and the reciprocal loyalty among the Jackal's contacts create a professional-honor framework that operates independently of ideology."},
    {"id": "JACKAL-WOKE-001", "name": "Gender Role Inversion", "category": "Woke",
     "severity": 2, "authenticity": "Moderate", "centrality": "Moderate",
     "weightedScore": ws(2, "Moderate", "Moderate"),
     "explanation": "The series reimagines the MI6 hunter as a Black woman (Lashana Lynch), a deliberate gender-and-race swap from the traditionally male role. The character is written as competent rather than grievance-driven, but the casting choice is unmistakably contemporary."},
    {"id": "JACKAL-WOKE-002", "name": "Female Power Structure", "category": "Woke",
     "severity": 2, "authenticity": "Low", "centrality": "Moderate",
     "weightedScore": ws(2, "Low", "Moderate"),
     "explanation": "Bianca occupies a position of institutional authority within MI6, and the agency's power structure includes women in leadership. This is presented as unremarkable within the show's world -- it is not a plot point but a production choice."},
    {"id": "JACKAL-WOKE-003", "name": "General Woke Element (Diverse Ensemble Casting)", "category": "Woke",
     "severity": 1, "authenticity": "Low", "centrality": "Low",
     "weightedScore": ws(1, "Low", "Low"),
     "explanation": "The ensemble cast is visibly diverse, consistent with 2024 UK/US co-production standards. This does not drive the narrative and is not remarked upon within the show."},
]

jackal_trad = sum(t["weightedScore"] for t in jackal_tropes if t["category"] == "Traditional")
jackal_woke = sum(t["weightedScore"] for t in jackal_tropes if t["category"] == "Woke")
jackal_margin = round(jackal_trad - jackal_woke, 2)
jackal_margin_str = format_margin(jackal_margin)
jackal_verdict = verdict_from_margin(jackal_margin)

review_jackal = {
    "id": "the-day-of-the-jackal-2024",
    "slug": "the-day-of-the-jackal-2024",
    "title": "The Day of the Jackal (2024)",
    "year": 2024,
    "type": "series",
    "platform": "Peacock / Sky Atlantic",
    "genre": "Spy Thriller Action Drama",
    "date": TODAY,
    "datePublised": TODAY,
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/the-day-of-the-jackal-2024.jpg",
    "releaseDate": "2024-11-07",
    "rating": "TV-MA",
    "runtime": "10 episodes (46-61 min each)",
    "director": "Brian Kirk",
    "writers": ["Ronan Bennett"],
    "showrunner": "Ronan Bennett",
    "cast": ["Eddie Redmayne", "Lashana Lynch", "Ursula Corbero", "Chukwudi Iwuji", "Khalid Abdalla", "Lia Williams", "Charles Dance"],
    "studio": "Sky Studios / Universal International Studios / Carnival Film and Television",
    "distributor": "Sky Atlantic / Peacock",
    "verdict": jackal_verdict,
    "wokeScore": jackal_woke,
    "tradScore": jackal_trad,
    "authIndex": round(jackal_trad / (jackal_trad + jackal_woke) * 100) if (jackal_trad + jackal_woke) > 0 else 50,
    "scoreMargin": jackal_margin_str,
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "No hidden ideological content. The gender-swapped MI6 lead is visible from episode one and never used as a Trojan horse for progressive messaging. The show's politics are institutional cynicism, not identity politics.",
    "tropeAudit": jackal_tropes,
    "summary": {
        "overall": "The Day of the Jackal is Sky Atlantic and Peacock's 10-episode reimagining of Frederick Forsyth's 1971 novel and the 1973 film adaptation, transplanted into a contemporary political landscape with a reported budget of 100 million pounds -- making it one of the most expensive British television productions ever mounted. Eddie Redmayne stars as the Jackal, a ruthlessly precise international assassin whose identity is as fluid as his moral boundaries, while Lashana Lynch plays Bianca, the MI6 firearms officer who makes it her mission to track him down. Created and written by Ronan Bennett (Top Boy) and directed by Brian Kirk, the series strips the story of its Cold War architecture and rebuilds it as a cat-and-mouse thriller about two professionals who are mirror images of each other: both obsessive, both willing to sacrifice anyone, both utterly convinced of their own necessity. The series earned two Golden Globe nominations -- Best Drama Series and Best Actor for Redmayne -- and was renewed for a second season within weeks of its premiere. It is a sleek, expensive, and morally unsettled piece of television that raises questions about what it means to be good at something terrible.",
        "traditionalContent": "The Day of the Jackal's traditional strengths lie in its commitment to competence as the organizing value of its world. Both the Jackal and Bianca are extraordinarily good at their jobs, and the show treats this excellence with genuine admiration. Redmayne's Jackal is not a traumatized victim of the system or an ideologue with a grievance -- he is a professional who chose his trade and pursues it with the precision of a surgeon. His craftsmanship is the show's most reliable pleasure. Bianca is similarly defined by her ability: she is a gifted investigator whose doggedness makes her the only person capable of connecting the dots. The show refuses to make her a symbol of female empowerment in a man's world -- it simply shows her being competent and lets the audience draw conclusions. The Jackal's family life -- a wife and child who know nothing of his work -- introduces a traditional domestic stake that makes his danger real. The series respects professional hierarchy, institutional procedure, and the weight of duty in a way that more ideologically freighted spy dramas (Homeland, Tehran) often subordinate to political messaging. The moral framework is not about which side is righteous; it is about whether excellence can coexist with evil, and whether duty demands you become a little monstrous yourself.",
        "wokeContent": "The Day of the Jackal's primary woke element is the casting of Lashana Lynch as Bianca, a role that in any previous adaptation would have gone to a white man. This is a deliberate choice, and the show knows it. But the execution is notably restrained: Bianca is given no speeches about representation, no backstory of overcoming systemic barriers, and no moments where her identity is invoked as a source of authority or grievance. She is a professional who happens to be a Black woman, and the show treats this as unremarkable. Whether this restraint is principled or merely commercial -- an acknowledgment that spy-thriller audiences do not want a lecture -- is open to debate. The diverse ensemble casting across the MI6 team and the international locales reflects 2024 production norms, but none of it is foregrounded as political commentary. The show's actual politics are institutional cynicism: MI6 is bureaucratic, the government is self-interested, and the Jackal's clients are the global rich whose ideology is money. This is not a woke critique of Western power -- it is a noir suspicion of all power, which is a much older tradition."
    },
    "parentalGuidance": "The Day of the Jackal is rated TV-MA for strong violence, language, and adult themes. The violence is professional and cold rather than gratuitous, but it is frequent and lethal -- the Jackal is an assassin and the show does not sanitize his work. There are several intense shooting sequences, close-quarters killings, and moments of sustained tension. Sexual content is minimal but present. Strong language throughout. The series also deals with moral corruption, institutional betrayal, and the psychological cost of living a double life. Not appropriate for children or young teens. Older teens and adults who enjoy spy thrillers will find a sophisticated, morally complex drama. Parents should know the show does not glamorize the Jackal's violence -- it makes it look professional, which is in some ways more disturbing.",
    "seo": {
        "titleTag": "Is The Day of the Jackal (2024) Woke? Eddie Redmayne Spy Thriller Reviewed | VirtueVigil",
        "metaDescription": f"VirtueVigil VVWS review of The Day of the Jackal (2024), Sky/Peacock's spy thriller starring Eddie Redmayne and Lashana Lynch. Verdict: {jackal_verdict} ({jackal_margin_str}). Parental guidance included.",
        "keywords": ["is the day of the jackal woke", "the day of the jackal 2024 review", "day of the jackal virtuevigil", "day of the jackal woke or traditional", "day of the jackal parents guide", "eddie redmayne jackal", "lashana lynch jackal"]
    }
}

# ============================================================
# PROCESSING -- one review at a time
# ============================================================
reviews = [review_mummy, review_yellow_eyes, review_jackal]
review_names = ["the-mummy-1999", "yellow-eyes-2026", "the-day-of-the-jackal-2024"]

os.chdir(REPO)

for i, review in enumerate(reviews):
    slug = review["slug"]
    print(f"\n{'='*60}")
    print(f"REVIEW {i+1}/3: {review['title']} ({slug})")
    print(f"Verdict: {review['verdict']} | Margin: {review['scoreMargin']}")
    print(f"Trad: {review['tradScore']} | Woke: {review['wokeScore']}")
    print(f"{'='*60}")

    # Load and append
    with open(REVIEWS_PATH, "r") as f:
        data = json.load(f)

    # Verify slug not present
    slugs = {item["slug"] for item in data}
    if slug in slugs:
        print(f"ERROR: Slug {slug} already exists!")
        sys.exit(1)

    data.append(review)
    print(f"Review count before: {len(data)-1}")

    with open(REVIEWS_PATH, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Review count after: {len(data)}")

    # Build
    result = subprocess.run(["node", "build.js"], capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(f"BUILD FAILED: {result.stderr[-500:]}")
        sys.exit(1)
    print("Build: EXIT 0")

    # Commit
    verdict_short = review['verdict'].replace(" ", "-").lower()
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", f"review: {review['title']} -- {review['verdict']} ({review['scoreMargin']})"], check=True)

    # Push
    subprocess.run(["git", "push"], check=True, timeout=30)

    # IndexNow
    subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
        f"https://api.indexnow.org/indexnow?url=https://virtuevigil.com/reviews/{slug}/&key=c5c06a51b3df4a6fb07de4954187d031"],
        check=False)

    # Verify live
    time.sleep(5)  # wait for Netlify
    curl_result = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
        f"https://virtuevigil.com/reviews/{slug}/"], capture_output=True, text=True)
    print(f"Live check: HTTP {curl_result.stdout}")

    # Verify SEO
    with open(REVIEWS_PATH) as f:
        check_data = json.load(f)
    last = check_data[-1]
    seo_ok = "seo" in last and "titleTag" in last.get("seo", {})
    print(f"SEO fields: {'OK' if seo_ok else 'MISSING!'}")

    print(f"✓ Review {i+1}/3 complete: {slug}")

# Final summary
with open(REVIEWS_PATH) as f:
    final_data = json.load(f)
print(f"\n{'='*60}")
print(f"DONE. Final review count: {len(final_data)} (was {len(final_data)-3})")