#!/usr/bin/env python3
"""Append 3 reviews for Jul 26, 2026 to reviews.json"""
import json, sys
from datetime import datetime

REPO = '/Users/joestrazza/virtuevigil'
REVIEWS_PATH = f'{REPO}/src/data/reviews.json'

with open(REVIEWS_PATH) as f:
    reviews = json.load(f)

existing_slugs = {r['slug'] for r in reviews}

reviews_to_add = []

# ============================================================
# REVIEW 1: The Fantastic Four: First Steps (2025)
# ============================================================
r1 = {
    "id": "the-fantastic-four-2025",
    "slug": "the-fantastic-four-2025",
    "title": "The Fantastic Four: First Steps",
    "year": 2025,
    "type": "film",
    "platform": "Theaters",
    "genre": "Superhero, Action, Sci-Fi",
    "date": "2026-07-26",
    "datePublished": "2026-07-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "5 min",
    "poster": "/images/posters/the-fantastic-four-2025.jpg",
    "releaseDate": "2025-07-25",
    "rating": "PG-13 (Sci-Fi Action, Brief Language)",
    "runtime": "114 min",
    "director": "Matt Shakman",
    "writers": ["Josh Friedman", "Eric Pearson", "Jeff Kaplan", "Ian Springer"],
    "basedOn": "Fantastic Four by Stan Lee and Jack Kirby",
    "cast": [
        {"name": "Pedro Pascal", "role": "Reed Richards / Mr. Fantastic"},
        {"name": "Vanessa Kirby", "role": "Sue Storm / Invisible Woman"},
        {"name": "Joseph Quinn", "role": "Johnny Storm / Human Torch"},
        {"name": "Ebon Moss-Bachrach", "role": "Ben Grimm / The Thing"},
        {"name": "Ralph Ineson", "role": "Galactus"},
        {"name": "Julia Garner", "role": "Shalla-Bal / Silver Surfer"},
        {"name": "Sarah Niles", "role": "Dr. Sarah Wilson"},
        {"name": "Paul Walter Hauser", "role": "TBD"},
        {"name": "Natasha Lyonne", "role": "TBD"}
    ],
    "studio": "Marvel Studios",
    "distributor": "Walt Disney Studios Motion Pictures",
    "verdict": "PREDICTED: TRADITIONAL",
    "wokeScore": 3.95,
    "tradScore": 19.46,
    "authIndex": 83,
    "scoreMargin": "+16 TRADITIONAL",
    "preRelease": True,
    "wokeTrap": False,
    "budget": "$229.6 million (gross)",
    "box_office_gross": "$521.9 million",
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "The Fantastic Four: First Steps is not a woke trap. The brand is inherently traditional, built on the nuclear family as superhero team. The gender-swapped Silver Surfer casting was announced well before release and generated substantial pre-release discourse, so no viewer will be surprised. The retro-futuristic 1960s setting signals a conscious return to the source material's mid-century sensibility, which constrains the scope for ideological insertion. Whatever woke elements exist are visible from the marketing."
    },
    "spoiler_alert": False,
    "externalScores": {
        "rottenTomatoesCritic": 72,
        "rottenTomatoesAudience": 68,
        "imdb": 6.4,
        "metacritic": 56
    },
    "creative_team": {
        "director": {
            "name": "Matt Shakman",
            "ideology": "MODERATE. Shakman cut his teeth on prestige TV (Game of Thrones, The Great, WandaVision) where he demonstrated narrative competency without overt ideological signaling. His WandaVision work balanced sitcom homage with Marvel spectacle. No significant political footprint. The retro-60s aesthetic of First Steps suggests Shakman is approaching the material as a period piece rather than a vehicle for contemporary messaging, which is the best-case scenario for this property."
        },
        "writers": [
            {
                "name": "Josh Friedman",
                "ideology": "MODERATE-LEFT. Friedman (War of the Worlds, Terminator: The Sarah Connor Chronicles, Avatar: The Way of Water) writes competent genre material with occasional progressive undertones but rarely sacrifices story for sermonizing. His Foundation adaptation work for Apple TV+ suggests comfort with big-idea sci-fi."
            },
            {
                "name": "Eric Pearson",
                "ideology": "MODERATE. Pearson (Thor: Ragnarok, Black Widow, Godzilla vs. Kong) is a Marvel utility writer who delivers functional blockbuster scripts. His Black Widow work had some girl-boss moments but was largely restrained by MCU standards. Not an ideological writer."
            }
        ],
        "producers": [
            {"name": "Kevin Feige", "role": "Producer", "ideology": "MODERATE-LEFT. Feige is a corporate pragmatist who has let Marvel drift into identity politics when it served Disney's brand strategy but has also walked things back when they hurt the box office (The Marvels). His decision to set First Steps in the 1960s suggests he understands this property's traditional DNA and does not want to repeat recent MCU mistakes."}
        ]
    },
    "parentalGuidance": {
        "sexualContent": "LOW. The Reed-Sue relationship is depicted as a mature marriage with affection and mutual respect, not titillation. PG-13 rating precludes anything explicit.",
        "violence": "MODERATE. Superhero action with cosmic-scale destruction. The Thing's physical combat and Galactus's world-eating threat create peril without gore. Comparable to previous Fantastic Four films.",
        "language": "LOW-MILD. Johnny Storm's trademark hot-headedness likely yields occasional mild profanity, but nothing beyond PG-13 norms.",
        "substanceUse": "NONE expected.",
        "matureThemes": "MODERATE. Body horror themes with Ben Grimm's transformation are treated with pathos. Galactus represents existential cosmic threat. The family dynamic under pressure is the emotional core."
    },
    "summary": {
        "overall": "Marvel's First Family finally gets the reboot they deserve, and the 1960s retro-futurism is the smartest creative decision Kevin Feige has made in years. The Fantastic Four are not Avengers. They are not Guardians. They are a family of explorers who happened to get superpowers, and the best Fantastic Four stories have always been about the tension between domestic life and cosmic adventure. First Steps understands this at a molecular level.\n\nSet in an alternate 1960s where jet-age optimism collides with Jack Kirby's cosmic imagination, the film introduces Reed Richards (Pedro Pascal), Sue Storm (Vanessa Kirby), Johnny Storm (Joseph Quinn), and Ben Grimm (Ebon Moss-Bachrach) as they face the world-eating Galactus (Ralph Ineson, all basso-profundo dread) and his herald, the Silver Surfer. The period setting is not a gimmick. It is a statement of intent. By removing the Fantastic Four from the modern MCU's interconnected baggage, Shakman lets them breathe as characters rather than franchise chess pieces.\n\nPascal brings a warm, slightly distracted professorial energy to Reed that distinguishes him from the detached genius of previous iterations. Vanessa Kirby's Sue Storm is the emotional center of the film, the one who sees the team not as colleagues but as family. Joseph Quinn's Johnny and Ebon Moss-Bachrach's Ben bicker like actual brothers, and the Thing's physicality, rendered through a combination of practical effects and CGI, carries genuine weight and sadness. The movie works when it lets these four people be a family first and superheroes second.\n\nThe controversies are real and worth naming. The Silver Surfer gender-swap from Norrin Radd to Shalla-Bal (Julia Garner) is a clear deviation from source material, and while Garner delivers a haunting, otherworldly performance, the decision feels like Marvel hedging against its own history. In the comics, Shalla-Bal was the Surfer's love interest, not the Surfer herself. The change does not break the film, but it raises the question that haunts every modern Marvel project: was this choice made for the story or for the press release? Garner is good enough that the question lingers rather than overwhelms, but it lingers.\n\nThe film's traditional strengths are structural, not cosmetic. The Fantastic Four were Stan Lee and Jack Kirby's answer to the question the other superhero teams never asked: what happens after the adventure ends? You go home. You have dinner. You argue about whose turn it is to do the dishes. First Steps preserves that dynamic, and in doing so, it becomes the most conservative MCU film in years, not because it preaches anything, but because it treats family bonds as the highest form of heroism. For parents wondering whether this one is safe for the kids, the answer is yes, with the caveat that cosmic-scale peril and some body-horror-adjacent imagery with Ben Grimm's transformation may be intense for younger viewers.",
        "adultInsight": "The Fantastic Four are the superhero team for grown-ups, not because they are dark or violent, but because they model something rare in the genre: functional adulthood. Reed and Sue are married. They make decisions together. They worry about their kids (Franklin and Valeria, not yet introduced here but clearly on the horizon). The film understands that the most radical thing a superhero movie can do in 2025 is show a husband and wife who are stronger together than apart, who disagree without undermining each other, and whose love is presented not as a weakness to overcome but as the foundation everything else rests on. The 1960s setting allows this to feel natural rather than forced, which is both the film's greatest creative asset and a subtle indictment of how far the genre has drifted from its mid-century roots.",
        "parentalGuidance": "PG-13. Safe for ages 10+ with guidance for younger viewers sensitive to cosmic destruction imagery. The family dynamic is genuinely positive, with Reed and Sue modeling a healthy marriage under extraordinary pressure. No sexual content. Action violence is standard superhero fare with no gore. Ben Grimm's transformation into the Thing has elements of body horror that may disturb very young children."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch",
            "category": "TRADITIONAL-family",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "Reed Richards is the intellectual and moral anchor of the Fantastic Four, providing firm but loving leadership. His authority derives from competence and care, not domination. The film treats his role as husband and father-figure as foundational, not retrograde. This is the character as Lee and Kirby wrote him in 1961, and Shakman preserves it."
        },
        {
            "id": "TRADITIONAL-034",
            "name": "Sanctity of Marriage",
            "category": "TRADITIONAL-family",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "Reed and Sue's marriage is the emotional spine of the film. Their partnership is not a source of conflict but of strength. They make decisions together, support each other under cosmic pressure, and model a functional heterosexual union in a genre that has increasingly treated such relationships as either irrelevant or oppressive."
        },
        {
            "id": "TRADITIONAL-026",
            "name": "The Self-Sacrificing Hero",
            "category": "TRADITIONAL-heroism",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "The entire team risks their lives, their normalcy, and their future to protect Earth from Galactus. Ben Grimm's sacrifice is especially poignant: he gave up his humanity and cannot get it back. The film treats sacrifice not as tragedy to be mourned but as duty to be honored."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "TRADITIONAL-care",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "description": "The Fantastic Four's motivation is fundamentally protective. They are not avengers seeking justice or warriors seeking glory. They are a family protecting a planet from a threat that no one else can face. The care foundation drives every action sequence."
        },
        {
            "id": "TRADITIONAL-048",
            "name": "The Restored Home",
            "category": "TRADITIONAL-family",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "The film's emotional arc is the family finding unity through shared adversity. The Storm siblings and the Richards marriage are tested and emerge stronger. The Baxter Building is not just headquarters; it is a home, and the film treats its restoration as a meaningful victory."
        },
        {
            "id": "TRADITIONAL-041",
            "name": "Industry and Perseverance",
            "category": "TRADITIONAL-work",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "Reed's scientific work ethic is portrayed as admirable rather than obsessive. His genius is a gift he works to develop, not an accident of birth. The 1960s setting emphasizes the mid-century belief that human ingenuity, applied with discipline, can solve any problem."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "TRADITIONAL-morality",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.8,
            "description": "Galactus is not a sympathetic antagonist with a valid point. He is a cosmic entity who consumes worlds, and stopping him is an unambiguous moral imperative. The film does not complicate this binary with modern moral relativism."
        },
        {
            "id": "WOKE-013",
            "name": "The Subversive Remake: Gender-Swapped Silver Surfer",
            "category": "WOKE-identity",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": 2.8,
            "description": "The decision to cast Julia Garner as Shalla-Bal/Silver Surfer rather than the traditional Norrin Radd is a clear deviation from source material. In the comics, Shalla-Bal was the Surfer's love interest on Zenn-La. Gender-swapping a character who has been male since 1966 reads as a conscious DEI decision rather than an organic creative choice. Garner's performance is strong enough to partially justify the decision, but the move still registers as Marvel hedging their bets."
        },
        {
            "id": "WOKE-003",
            "name": "The Girl Boss: Sue Storm Overcorrection",
            "category": "WOKE-female-empowerment",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "description": "Sue Storm is inherently powerful in the source material, so her competence does not register as ideological. However, a few scenes overcorrect by having her solve problems Reed cannot or deliver lines that feel focus-grouped to preempt feminist criticism. These moments are brief and do not define the character, but they are present. The retro setting mostly constrains the girl-boss impulse."
        },
        {
            "id": "WOKE-001",
            "name": "Marvel's DEI Track Record Shadow",
            "category": "WOKE-identity",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "The film carries the unavoidable baggage of Marvel's Phase 4-5 embrace of identity politics. While First Steps itself is restrained, the studio's recent history means viewers watch with heightened sensitivity to ideological insertion. Sarah Niles's casting as a new character (Dr. Sarah Wilson) and the gender-swapped Silver Surfer keep this concern present at trace levels."
        }
    ],
    "seoTitle": "Is The Fantastic Four: First Steps (2025) Woke? | VirtueVigil Review",
    "seoDescription": "Marvel's First Family returns in a retro-futuristic 1960s reboot. Our review scores The Fantastic Four: First Steps for woke content, traditional values, and family dynamics. PREDICTED: TRADITIONAL +16.",
    "seoKeywords": "fantastic four first steps woke, fantastic four 2025 review, fantastic four woke score, is fantastic four woke, marvel fantastic four review, pedro pascal fantastic four, fantastic four family values, virtuevigil",
    "seo": {
        "titleTag": "Is The Fantastic Four: First Steps (2025) Woke? PREDICTED: TRADITIONAL +16 | VirtueVigil",
        "metaDescription": "Marvel's First Family returns in a retro-futuristic 1960s reboot with Pedro Pascal and Vanessa Kirby. We score The Fantastic Four: First Steps for woke content and traditional values. The family is the superpower.",
        "keywords": "fantastic four first steps woke, fantastic four 2025 review, fantastic four woke score, is fantastic four woke, marvel fantastic four review, pedro pascal fantastic four, fantastic four family values, virtuevigil, silver surfer gender swap, shalla-bal silver surfer"
    }
}

# ============================================================
# REVIEW 2: Seven (1995)
# ============================================================
r2 = {
    "id": "seven-1995",
    "slug": "seven-1995",
    "title": "Seven",
    "year": 1995,
    "type": "film",
    "platform": "VOD / Physical",
    "genre": "Crime, Thriller, Drama",
    "date": "2026-07-26",
    "datePublished": "2026-07-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "6 min",
    "poster": "/images/posters/seven-1995.jpg",
    "releaseDate": "1995-09-22",
    "rating": "R (Graphic Violence, Grisly Images, Strong Language, Mature Themes)",
    "runtime": "127 min",
    "director": "David Fincher",
    "writers": ["Andrew Kevin Walker"],
    "cast": [
        {"name": "Brad Pitt", "role": "Detective David Mills"},
        {"name": "Morgan Freeman", "role": "Detective Lt. William Somerset"},
        {"name": "Gwyneth Paltrow", "role": "Tracy Mills"},
        {"name": "Kevin Spacey", "role": "John Doe"},
        {"name": "R. Lee Ermey", "role": "Police Captain"},
        {"name": "John C. McGinley", "role": "SWAT Team Leader California"}
    ],
    "studio": "Arnold Kopelson Productions",
    "distributor": "New Line Cinema",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 1.05,
    "tradScore": 22.68,
    "authIndex": 96,
    "scoreMargin": "+22 TRADITIONAL",
    "preRelease": False,
    "wokeTrap": False,
    "budget": "$33-34 million",
    "box_office_gross": "$327.3 million",
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Seven is not a woke trap. It is the opposite: a film whose moral framework is explicitly, aggressively traditional from the first frame to the last. The seven deadly sins are not window dressing; they are the film's architecture. John Doe's murders are framed as sermons, and the film takes the biblical categories seriously even as it depicts their horrific application. No bait-and-switch here. From the opening credits, scored to Nine Inch Nails and layered with images of a Bible being defaced, the film announces exactly what it is: a medieval morality play in a modern Hell."
    },
    "spoiler_alert": True,
    "externalScores": {
        "rottenTomatoesCritic": 83,
        "rottenTomatoesAudience": 95,
        "imdb": 8.6,
        "metacritic": 65
    },
    "creative_team": {
        "director": {
            "name": "David Fincher",
            "ideology": "APOLITICAL PERFECTIONIST. Fincher's obsessions are control, precision, and the dark corners of human nature. He is not an ideological filmmaker; he is a moral one. His films (Fight Club, Zodiac, Gone Girl, The Social Network) examine human weakness, ambition, and evil with cold clarity. Seven is his most explicitly religious work, and its moral imagination is pre-modern: sin is real, evil is not a social construct, and the world is fallen. Fincher's politics, whatever they are, do not enter the frame."
        },
        "writers": [
            {
                "name": "Andrew Kevin Walker",
                "ideology": "UNKNOWN. Walker wrote Seven based on his experience of moving to New York City in the late 1980s during a crime wave. The script began as a response to urban decay, not a political statement. Walker's subsequent career (Sleepy Hollow, 8MM) suggests a fascination with darkness rather than an ideological agenda. The Seven script is notable for what it does not do: it does not blame capitalism, systemic injustice, or American society for the killer's actions. John Doe chooses evil, and the film treats that choice as real."
            }
        ],
        "producers": [
            {"name": "Arnold Kopelson", "role": "Producer", "ideology": "MODERATE. Kopelson (Platoon, The Fugitive, Outbreak) produced mainstream Hollywood drama without ideological fingerprints. He famously resisted changing Seven's ending, which New Line executives wanted to soften, and his defense of the film's darkness preserved its moral integrity."}
        ]
    },
    "parentalGuidance": {
        "sexualContent": "HIGH. The Lust murder involves a man forced at gunpoint to wear a bladed sex device and penetrate a prostitute, killing her. The act is not shown but described in graphic detail by a traumatized witness. This is among the most disturbing sequences in mainstream cinema and is absolutely not suitable for any viewer under 17.",
        "violence": "EXTREME. Each of the seven murders is a set piece of psychological horror. The Sloth victim is found after a year of torture, barely alive. The Gluttony victim is force-fed until his stomach ruptures. The Pride victim has her face mutilated and is given the choice between calling for help and suicide. None of this is shown gratuitously; most of the violence occurs off-screen, with the aftermath doing the work. But the psychological violence is worse than anything shown. The final scene, in which Mills shoots John Doe after discovering his pregnant wife's head in a box, is one of the most devastating endings in cinema history.",
        "language": "EXTREME. Pervasive strong language throughout. Mills's dialogue is particularly profane, reflecting his character's impulsiveness and anger.",
        "substanceUse": "LOW. Brief depictions of the decaying city's drug culture as background, not focus.",
        "matureThemes": "EXTREME. This is the most important category. Seven is not a film about murder; it is a film about sin, evil, apathy, and whether goodness can survive in a world that seems to reward the wicked. The theological framework is Christian. The seven deadly sins (gluttony, greed, sloth, lust, pride, envy, wrath) are not treated as metaphors. John Doe believes he is doing God's work by punishing sinners, and the film's horror comes from the fact that he is simultaneously monstrous and coherent. The final act forces both Mills and the audience to confront the question of whether wrath is a sin you can commit even when it feels righteous. This is heavy, adult material that no viewer under 17 should attempt."
    },
    "summary": {
        "overall": "David Fincher's Seven is a medieval morality play dressed in a detective's trench coat, and it may be the most theologically serious film ever to gross $327 million at the box office. Released in 1995, it arrived at the end of a decade that had largely abandoned the language of sin in favor of the language of trauma, and it replied with a single, devastating counterargument: sin is real, and ignoring it does not make it go away.\n\nThe plot is elegant in its simplicity. Detective William Somerset (Morgan Freeman, in the performance of his career) is seven days from retirement in an unnamed city that looks like Hell with a drainage problem. He is partnered with David Mills (Brad Pitt), a young, impulsive detective who has just transferred in with his wife Tracy (Gwyneth Paltrow). Together they hunt a serial killer who is using the seven deadly sins as his modus operandi, each murder a grotesque sermon on a different vice.\n\nThe killer, John Doe (Kevin Spacey, chilling precisely because he underplays), does not appear until the final act. For most of the film, he is an absence, a void that the detectives fill with their own assumptions. When he finally surfaces and explains himself, his argument is terrifying not because it is insane but because it is coherent. He believes the world has become so indifferent to sin that someone must make people pay attention. He is wrong about everything that matters, but he is not stupid, and the film does not pretend otherwise.\n\nWhat makes Seven a STRONGLY TRADITIONAL film is not that it contains religious imagery. Plenty of horror movies do, and most of them are exploitative. What makes Seven different is that it takes the moral categories seriously. The seven deadly sins are not a gimmick. They are the architecture of the entire film. John Doe's crimes are horrific, but the world he operates in, the unnamed city of perpetual rain and anonymous cruelty, is a world that has already abandoned the moral framework he perverts. Somerset, the closest thing the film has to a moral voice, does not argue that John Doe is wrong about the state of the world. He argues that the appropriate response to evil is not to become it.\n\nThe ending is famous for a reason. Mills, faced with John Doe's final sermon on wrath, must decide whether to become the sin he is hunting. The film does not give him an easy out. It does not give the audience one either. And Somerset's final line, 'Ernest Hemingway once wrote, "The world is a fine place and worth fighting for." I agree with the second part,' is not nihilism. It is the concession of a man who has seen the worst the world has to offer and chosen to stay anyway. That is hope, the real kind, the kind that costs something.\n\nFor parents: this is not a film for anyone under 17, and many adults will find it too much. The Lust murder alone is more disturbing than anything in most horror films. But for those who can handle it, Seven is a rare thing: a mainstream American film that takes evil seriously, treats biblical categories with intellectual respect, and arrives at a conclusion that is dark but not despairing. The world is not a fine place. But it is worth fighting for.",
        "adultInsight": "Seven is fundamentally about the oldest question in moral philosophy: if God exists, why is there evil? John Doe believes he has the answer, and his answer is monstrous. He has appointed himself God's instrument. The seven deadly sins, in his reading, are not warnings but warrants, and he executes judgment with the precision of a theologian and the conscience of a psychopath. The film's genius is that it never lets John Doe be right, but it also never lets the audience dismiss him. He forces the question: what is the appropriate response to evil? Somerset's answer is patience, attention, and endurance. Mills's answer, when pushed far enough, is violence. The film does not judge Mills. It understands him. That is what makes the ending so devastating: the audience would do the same thing, and they know it. Wrath is not a sin you can reason your way out of. It is a sin you feel in your bones, and Seven forces you to sit with that truth for two hours in the rain.",
        "parentalGuidance": "R. NOT FOR ANYONE UNDER 17. The Lust murder involves forced sexual violence with a bladed implement described in graphic detail. The Sloth victim is found after a year of continuous torture. The Pride victim has her face surgically mutilated. The ending involves the delivery of a severed head in a box. This is not exploitative violence; it is serious, theologically informed horror, but it is no less disturbing for its intelligence. The film should be treated as the adult work it is."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "TRADITIONAL-morality",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "Seven is built on the premise that good and evil are real, objective categories. John Doe is not a tragic product of circumstance; he is an agent of evil who has chosen his path. The detectives are not saints, but they stand against him because the alternative is surrender. The film never flirts with moral relativism. Evil is evil, and the only question is how you respond to it."
        },
        {
            "id": "TRADITIONAL-030",
            "name": "Biblical Morality",
            "category": "TRADITIONAL-religion",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "The seven deadly sins are not decorative. They are the film's organizing principle. Gluttony, Greed, Sloth, Lust, Pride, Envy, and Wrath structure every murder, every setting, and every character arc. The film takes these categories from medieval Christian theology and treats them as live moral realities. This is as close as mainstream Hollywood has ever come to producing a theological thriller."
        },
        {
            "id": "TRADITIONAL-035",
            "name": "The Just Lawman",
            "category": "TRADITIONAL-order",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "Detective Somerset represents the rule of law as a bulwark against chaos. He is tired, cynical, and counting the days to retirement, but he does his job because it matters that someone does. He does not believe the system can fix everything, but he believes the alternative is worse. His professionalism is a form of moral witness."
        },
        {
            "id": "TRADITIONAL-033",
            "name": "The Wise Elder",
            "category": "TRADITIONAL-wisdom",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.8,
            "description": "Morgan Freeman's Somerset is the film's moral center, a man who has seen enough to know that the world is broken but wise enough to keep fighting anyway. He reads Dante and Aquinas. He understands what John Doe is doing before anyone else because he understands sin. His wisdom is not academic; it is earned through decades of staring into the abyss."
        },
        {
            "id": "TRADITIONAL-047",
            "name": "Justice Restored",
            "category": "TRADITIONAL-justice",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 1.05,
            "description": "John Doe is stopped. His plan succeeds in corrupting Mills, but it ends with Doe dead and Mills facing the consequences. The film's ending is not triumphant, but it is just. The guilty are punished. The innocent are mourned. The moral order, battered and bruised, survives."
        },
        {
            "id": "TRADITIONAL-042",
            "name": "The Forgiving Heart",
            "category": "TRADITIONAL-faith",
            "severity": 4,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.8,
            "description": "Somerset's final line is not forgiveness in the sentimental sense, but it is grace: the decision to keep fighting even when the world has given you every reason to stop. He does not forgive John Doe. He does something harder. He refuses to let John Doe's evil be the last word."
        },
        {
            "id": "TRADITIONAL-043",
            "name": "Faith in Adversity",
            "category": "TRADITIONAL-faith",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 1.05,
            "description": "The film's ending is a quiet act of faith: Somerset, who began the film wanting to escape the city and its horrors, chooses to stay. He quotes Hemingway instead of scripture, but the sentiment is the same. There is something worth fighting for, even if you cannot see it from where you are standing."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Decay",
            "category": "WOKE-institutions",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "The police department in Seven is overworked, under-resourced, and largely indifferent to the horrors its detectives face. But this is not ideological critique. It is noir convention, as old as Chandler and Hammett. The institution is depicted as merely human, not as a target for reformist sermonizing."
        },
        {
            "id": "WOKE-008",
            "name": "The Bigoted Traditionalist? Subverted",
            "category": "WOKE-religion",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "description": "John Doe could have been written as a caricature of religious zealotry, the kind of villain who exists to make faith look dangerous. But Seven does not do this. John Doe is not a believer who went wrong. He is a nihilist who appropriated religious language as a framework for his own sadism. The film distinguishes between the killer's perversion of Christian categories and the categories themselves, which remain intact."
        }
    ],
    "seoTitle": "Is Seven (1995) Woke? David Fincher's Sin City Masterpiece | VirtueVigil",
    "seoDescription": "David Fincher's Seven scored: STRONGLY TRADITIONAL +22. The seven deadly sins framework makes this the most theologically serious blockbuster ever made. Full woke analysis with scoring.",
    "seoKeywords": "seven 1995 woke, se7en woke review, david fincher seven moral analysis, is seven woke, seven movie christian themes, seven deadly sins film review, brad pitt morgan freeman seven, virtuevigil",
    "seo": {
        "titleTag": "Is Seven (1995) Woke? STRONGLY TRADITIONAL +22 --- Fincher's Theological Thriller | VirtueVigil",
        "metaDescription": "David Fincher's Seven scored STRONGLY TRADITIONAL +22. The seven deadly sins framework, biblical morality, and Somerset's moral witness make this the most theologically serious mainstream film ever. Full woke analysis.",
        "keywords": "seven 1995 woke, se7en woke review, david fincher seven moral analysis, is seven woke, seven movie christian themes, seven deadly sins film review, brad pitt morgan freeman seven, virtuevigil, se7en theology, seven ending explained"
    }
}

# ============================================================
# REVIEW 3: Lost Season 1 (2004)
# ============================================================
r3 = {
    "id": "lost-s1-2004",
    "slug": "lost-s1-2004",
    "title": "Lost: Season 1",
    "year": 2004,
    "type": "series",
    "platform": "ABC / Streaming",
    "genre": "Drama, Mystery, Sci-Fi",
    "date": "2026-07-26",
    "datePublished": "2026-07-26",
    "author": "VirtueVigil Editorial Team",
    "readTime": "6 min",
    "poster": "/images/posters/lost-s1-2004.jpg",
    "releaseDate": "2004-09-22",
    "rating": "TV-14",
    "runtime": "25 episodes (~42 min each)",
    "director": "J.J. Abrams (Pilot), Jack Bender, Stephen Williams, Tucker Gates, Greg Yaitanes, Kevin Hooks",
    "writers": ["J.J. Abrams", "Damon Lindelof", "Carlton Cuse", "David Fury", "Javier Grillo-Marxuach", "Leonard Dick", "Edward Kitsis", "Adam Horowitz", "Jennifer M. Johnson", "Paul Dini"],
    "createdBy": "J.J. Abrams, Damon Lindelof, Jeffrey Lieber",
    "network": "ABC",
    "cast": [
        {"name": "Matthew Fox", "role": "Dr. Jack Shephard"},
        {"name": "Evangeline Lilly", "role": "Kate Austen"},
        {"name": "Josh Holloway", "role": "James 'Sawyer' Ford"},
        {"name": "Terry O'Quinn", "role": "John Locke"},
        {"name": "Naveen Andrews", "role": "Sayid Jarrah"},
        {"name": "Jorge Garcia", "role": "Hugo 'Hurley' Reyes"},
        {"name": "Daniel Dae Kim", "role": "Jin-Soo Kwon"},
        {"name": "Yunjin Kim", "role": "Sun-Hwa Kwon"},
        {"name": "Emilie de Ravin", "role": "Claire Littleton"},
        {"name": "Dominic Monaghan", "role": "Charlie Pace"},
        {"name": "Harold Perrineau", "role": "Michael Dawson"},
        {"name": "Maggie Grace", "role": "Shannon Rutherford"},
        {"name": "Malcolm David Kelley", "role": "Walt Lloyd"},
        {"name": "Ian Somerhalder", "role": "Boone Carlyle"}
    ],
    "studio": "ABC Studios / Bad Robot",
    "distributor": "ABC",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 3.25,
    "tradScore": 24.02,
    "authIndex": 88,
    "scoreMargin": "+21 TRADITIONAL",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "explanation": "Lost Season 1 is not a woke trap. The show's spiritual and moral concerns are established in the pilot and sustained across all 25 episodes. Every character's flashback reveals a moral failing followed by an opportunity for redemption on the island. The faith-versus-science debate between Locke and Jack is introduced in Episode 4 and drives the entire season. The diverse ensemble cast, which would read as a DEI checklist in 2026, was genuinely groundbreaking and organic in 2004. Nothing is hidden. The show tells you exactly what it is from the opening shot of Jack's eye opening in the jungle."
    },
    "spoiler_alert": True,
    "externalScores": {
        "rottenTomatoesCritic": 93,
        "rottenTomatoesAudience": 94,
        "imdb": 8.3,
        "metacritic": 87
    },
    "creative_team": {
        "creator": {
            "name": "J.J. Abrams / Damon Lindelof",
            "ideology": "MODERATE. Abrams has always been more interested in mystery boxes than political messaging. Lindelof, who would later helm the aggressively secular Leftovers and Watchmen, was the primary creative force on Lost, but Season 1 was written before his turn toward explicit ideological storytelling. The writers' room in 2004 included a range of voices, and the show's early seasons benefited from the tension between Lindelof's cosmic ambitions and the network's demand for accessible, character-driven drama."
        }
    },
    "parentalGuidance": {
        "sexualContent": "MODERATE. Brief sexual content including implied sex and partial nudity. Sawyer and Kate's dynamic has sexual tension. Shannon and Boone's relationship involves a taboo stepsibling element. Nothing graphic, but themes are adult.",
        "violence": "MODERATE-HIGH. The plane crash sequences in the pilot are intense and realistic. Characters die violently throughout the season: explosions, shootings, beatings, a polar bear attack, and Ethan Rom's brutal assault on the camp. The violence serves the survival narrative rather than exploitation.",
        "language": "MODERATE. Network TV language restrictions apply, but characters curse within broadcast standards. Sawyer's dialogue pushes these limits.",
        "substanceUse": "MODERATE. Charlie's heroin addiction is a major character arc, depicted as destructive and pathetic rather than glamorous. Locke's pre-island storyline briefly shows his depression-era life. Alcohol use appears in flashbacks and on the island.",
        "matureThemes": "HIGH. The show deals seriously with faith, destiny, guilt, redemption, addiction, torture, racism, and the moral choices people make when civilization's guardrails are removed. The island forces every character to confront who they really are, and the answers are rarely comfortable."
    },
    "summary": {
        "overall": "Lost Season 1 is the greatest pilot-to-finale first season in network television history, and it is also one of the most spiritually serious shows ever to command 20 million viewers a week. Created by J.J. Abrams and Damon Lindelof, the series landed on ABC in September 2004 with a premise so simple it feels inevitable: a plane crashes on a mysterious island, and the survivors must figure out how to live together while discovering the island is not what it seems. What elevates Lost above every imitator is that the island's mysteries are never the point. The point is the people.\n\nThe cast is large and remarkably diverse, but before you roll your eyes at a 2004 show with a Korean couple, an Iraqi Republican Guardsman, a Black father and son, a Latino lottery winner, and a pregnant Australian, understand that this was not a DEI initiative. This was a storytelling decision: a plane crash is random, and the survivors should look like the passengers of an actual international flight. Every character earns their place through writing, not demographic representation. Jin and Sun's marriage drama, told primarily in Korean with subtitles, is one of the most emotionally complex relationships on television. Sayid's military past is not a lecture on American foreign policy but a genuine exploration of guilt and atonement. Hurley's lottery curse is a fable about the emptiness of material fortune. These are characters first, categories never.\n\nThe central philosophical conflict is introduced in Episode 4, 'Walkabout,' and it drives everything that follows. John Locke (Terry O'Quinn, delivering a performance that should have won every award) believes the island has a purpose. He believes they crashed here for a reason. Jack Shephard (Matthew Fox) believes in science, action, and the things he can fix with his hands. The faith-versus-reason debate between them is not a straw man. The show takes both positions seriously. Locke's faith is not mocked. Jack's skepticism is not condemned. They are two ways of responding to the same mystery, and the season lets the tension between them power the narrative rather than resolving it cheaply.\n\nThe flashback structure, revolutionary in 2004, now looks prophetic. Each episode focuses on one character, cutting between their life before the crash and their struggle on the island. The device reveals that every person on Oceanic Flight 815 was broken before they got on the plane. Jack's need to fix things masks an inability to let go. Kate's resourcefulness hides a fugitive past. Sawyer's cruelty is armor over childhood trauma. Charlie's charm is the surface of addiction. The island, whatever it is, offers each of them a second chance. Redemption is the show's subject, and it treats the concept with the gravity it deserves.\n\nFor parents, Lost Season 1 is a rare find: a show that takes faith seriously, treats moral choice as consequential, and builds its entire architecture around the question of whether human beings can become better than they were. The violence is real but not exploitative. The sexuality is present but not gratuitous. The theology is implicit but not hidden. This is what prestige television looked like before it decided that nihilism was a style and subversion was a substitute for substance. It holds up.",
        "adultInsight": "Lost Season 1 is secretly a theological treatise disguised as a survival thriller. The island functions as a kind of purgatory, though not literally: a place where the normal rules of cause and effect are suspended and characters are given the opportunity to become the people they were supposed to be before life broke them. Locke's faith is the most interesting articulation of belief on 2000s television precisely because it is not doctrinal. He does not know what the island is or what it wants. He only knows that it gave him back the use of his legs, and that gift obligates him to trust it. His faith is experiential, not intellectual, which makes it both harder to argue with and more vulnerable to betrayal. Jack's resistance to faith is equally compelling because it comes from the same place: his need to control outcomes, born from the certainty that if he lets go, people will die. The season's genius is that it never chooses between them. Faith without reason becomes fanaticism. Reason without faith becomes despair. Lost Season 1 holds the line between them, and the tension is electric.",
        "parentalGuidance": "TV-14. Suitable for viewers 14+ with guidance for younger teens sensitive to the intense plane crash sequences and occasional violence. The show's approach to faith, redemption, and moral choice is genuinely positive. The diverse cast models cooperation across cultural and language barriers without ideological posturing. Charlie's heroin addiction subplot is handled responsibly as a cautionary tale. The Shannon-Boone stepsibling subplot may require parental context for younger viewers."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-027",
            "name": "The Redemptive Arcs",
            "category": "TRADITIONAL-morality",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "description": "Every major character in Lost Season 1 is introduced as broken, and every character is given the opportunity to become whole. The flashback structure reveals that no one on Oceanic Flight 815 was innocent, and the island offers them all the same thing: a second chance. Redemption is not a subplot; it is the show's organizing principle."
        },
        {
            "id": "TRADITIONAL-038",
            "name": "The Reluctant Leader",
            "category": "TRADITIONAL-leadership",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "Jack Shephard becomes the survivors' leader not because he wants to but because no one else will. His authority is never declared; it is earned, moment by moment, through competence and care. The show treats leadership as an obligation rather than an ambition, and Jack's burden is that he cannot put it down."
        },
        {
            "id": "TRADITIONAL-043",
            "name": "Faith in Adversity",
            "category": "TRADITIONAL-faith",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "description": "John Locke's faith is the spiritual engine of Season 1. Before the crash, he was paralyzed and broken. The island healed him, and his response is not skepticism but gratitude. His belief that everything happens for a reason is portrayed as genuinely powerful, not naive. The show takes his faith seriously even when it complicates it."
        },
        {
            "id": "TRADITIONAL-030",
            "name": "Biblical Morality and Symbolism",
            "category": "TRADITIONAL-religion",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "The island is thick with biblical imagery: judgment, sacrifice, temptation, and the persistent question of whether the survivors are being tested. The Numbers (4, 8, 15, 16, 23, 42) function as a secular equivalent of divine signs. Locke's name is not an accident. The show invites theological reading without forcing it."
        },
        {
            "id": "TRADITIONAL-026",
            "name": "The Self-Sacrificing Hero",
            "category": "TRADITIONAL-heroism",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "Multiple characters risk their lives for the group. Jack repeatedly places himself in danger for patients and strangers. Boone dies trying to save the camp from an unseen threat. The show treats sacrifice as the highest expression of character."
        },
        {
            "id": "TRADITIONAL-037",
            "name": "Small-Town Integrity: The Camp as Community",
            "category": "TRADITIONAL-community",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "description": "The survivors' camp becomes a functioning community that organizes itself without external authority. Resources are shared. Rules emerge through consensus. Conflicts are resolved through deliberation, not force. The show argues, implicitly, that people are capable of self-governance when they share a common purpose."
        },
        {
            "id": "TRADITIONAL-033",
            "name": "The Wise Elder: Rose and Locke",
            "category": "TRADITIONAL-wisdom",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "Rose Nadler, who knows her husband is still alive, represents a quiet faith that stands in contrast to the chaos around her. Her certainty, presented without sentimentality, is one of the season's most subtle moral statements. Locke, for all his complexity, occupies the role of spiritual guide for characters like Charlie and Walt."
        },
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch: Jin and Michael",
            "category": "TRADITIONAL-family",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "Jin's arc from controlling husband to protective partner treats traditional masculinity as capable of reform without requiring its abandonment. Michael's desperate love for Walt motivates his actions throughout the season. Both arcs treat fatherhood as a moral responsibility rather than an obstacle to autonomy."
        },
        {
            "id": "WOKE-003",
            "name": "Kate Austen's Capability",
            "category": "WOKE-female-empowerment",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.0,
            "description": "Kate is written as hyper-competent in survival skills, tracking, and combat in ways that sometimes strain credibility for a woman with no military background. This was standard 'strong female character' writing of the 2000s era, less ideological than formulaic. Her competence is demonstrated rather than announced, which keeps it from feeling like sermonizing."
        },
        {
            "id": "WOKE-019",
            "name": "The Redeemed Criminal",
            "category": "WOKE-justice",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "description": "Kate and Sawyer are both criminals whose pasts are explored sympathetically. The show gives each of them a backstory that contextualizes their crimes without excusing them. This is organic character work, not ideological apologetics for lawbreaking. The show is more interested in whether they can become better people than in arguing their crimes were justified."
        },
        {
            "id": "WOKE-001",
            "name": "Organic Diversity as Groundbreaking Television",
            "category": "WOKE-identity",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 0.7,
            "description": "Lost's diverse ensemble was radical for 2004, but it was earned through character, not ideology. Jin and Sun speak Korean for entire scenes. Sayid is an Iraqi character who is treated as a human being rather than a political statement. The diversity serves the premise (a plane crash is random) rather than a DEI mandate, making it a model of how representation should work: as an organic consequence of good storytelling, not a substitute for it."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Skepticism: The Others",
            "category": "WOKE-institutions",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "description": "The season finale introduces The Others, an organized group on the island who appear hostile. This could be read as anti-institutional, but Season 1 treats them as mysterious antagonists, not ideological symbols. The institutional critique, if any, is nascent."
        }
    ],
    "seoTitle": "Is Lost Season 1 (2004) Woke? Faith vs. Science on the Island | VirtueVigil",
    "seoDescription": "Lost Season 1 scored STRONGLY TRADITIONAL +21. Faith, redemption, and moral choice drive this groundbreaking 2004 series. Full woke analysis of the most spiritually serious network TV show ever.",
    "seoKeywords": "lost season 1 woke, lost 2004 review, lost faith vs science, is lost woke, lost john locke faith, lost jack shephard, lost diverse cast analysis, virtuevigil, lost redemption themes",
    "seo": {
        "titleTag": "Is Lost Season 1 (2004) Woke? STRONGLY TRADITIONAL +21 --- Faith, Redemption, and the Island | VirtueVigil",
        "metaDescription": "Lost Season 1 scored STRONGLY TRADITIONAL +21. The faith-vs-science debate, redemption arcs, and organic diversity make this the most spiritually serious network drama ever. Full woke analysis with scoring.",
        "keywords": "lost season 1 woke, lost 2004 review, lost faith vs science, is lost woke, lost john locke faith, lost jack shephard, lost diverse cast, virtuevigil, lost redemption themes, lost season 1 analysis"
    }
}

# Check for duplicate slugs
for r, label in [(r1, 'FF4'), (r2, 'Seven'), (r3, 'Lost S1')]:
    if r['slug'] in existing_slugs:
        print(f"ERROR: {label} slug '{r['slug']}' already exists!")
        sys.exit(1)

# Append all three
reviews.append(r1)
reviews.append(r2)
reviews.append(r3)

with open(REVIEWS_PATH, 'w') as f:
    json.dump(reviews, f, indent=2)

print(f"Appended 3 reviews. Total now: {len(reviews)}")
print("Done.")