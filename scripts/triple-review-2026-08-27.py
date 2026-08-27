#!/usr/bin/env python3
"""Append 3 reviews for 2026-08-27: The Dog Stars, Twilight, The Walking Dead"""
import json, os

REVIEWS_PATH = "src/data/reviews.json"

with open(REVIEWS_PATH) as f:
    reviews = json.load(f)

existing_slugs = {r["slug"] for r in reviews}

reviews_data = []

# ============================================================
# REVIEW 1: THE DOG STARS (2026) — New Release
# ============================================================
dogstars = {
    "id": "the-dog-stars-2026",
    "slug": "the-dog-stars-2026",
    "title": "The Dog Stars (2026)",
    "year": 2026,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Post-Apocalyptic, Science Fiction, Drama",
    "date": "2026-08-27",
    "datePublished": "2026-08-27",
    "author": "VirtueVigil Editorial Team",
    "readTime": "10 min",
    "poster": "/images/posters/the-dog-stars-2026.jpg",
    "releaseDate": "2026-08-28",
    "rating": "PG-13",
    "runtime": "118 min",
    "director": "Ridley Scott",
    "writers": "Mark L. Smith, Christopher Wilkinson",
    "cast": [
        "Jacob Elordi",
        "Josh Brolin",
        "Margaret Qualley",
        "Guy Pearce"
    ],
    "studio": "20th Century Studios, Scott Free Productions",
    "distributor": "20th Century Studios",
    "verdict": "TRADITIONAL",
    "wokeScore": 0.85,
    "tradScore": 17.98,
    "authIndex": "High",
    "scoreMargin": "+17 TRAD",
    "preRelease": None,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "The Dog Stars is ideologically transparent from its opening scenes. Hig's voiceover establishes his grief over his dead wife, his bond with his dog Jasper, and his reluctant partnership with survivalist Bangley, all before any plot mechanics kick in. The film is a post-apocalyptic story about human connection and the moral cost of survival, not a bait-and-switch. No woke content is hidden past the halfway point because there is essentially no woke content to hide. The film's worldview is rooted in personal responsibility, protective masculinity, and the sanctity of human bonds, and it never pretends otherwise."
    },
    "summary": {
        "overall": "Ridley Scott's adaptation of Peter Heller's 2012 novel is the kind of movie Hollywood used to make routinely before it forgot how: a quiet, sun-bleached survival story about a man, his dog, and the question of whether compassion can survive the end of the world. Jacob Elordi plays Hig, a former contractor living at an abandoned Colorado airfield nine years after a flu pandemic killed most of humanity. He flies patrols in a vintage Cessna, hunts and fishes in the mountains, and maintains an uneasy alliance with Bangley (Josh Brolin), a hardened survivalist who sees every stranger as a threat. The two men are the film's strange heart: Hig wants to believe in people, Bangley knows better, and their mutual dependence is more honest than friendship. When Hig's dog dies and he decides to fly beyond his fuel range to investigate a faint radio transmission from years ago, the film becomes something rarer than a thriller. It becomes a meditation on what a man owes to the dead and what he is allowed to want from the living. Scott shoots the Colorado wilderness with the reverence of a man who has spent 50 years learning what a camera can do. The mountains do not care that civilization collapsed. The rivers still run. The performance Scott gets from Elordi is the best of the young actor's career. He carries the film largely alone for long stretches, and his grief is not performed but inhabited. He is a man who kept going because there was a dog to feed and a plane to maintain, and when the dog dies, he has to find a new reason. Margaret Qualley's Cima, a physician surviving with her father in a hidden canyon, provides that reason without ever becoming a prize to be won. She is competent, wary, and fully realized, not a love interest but a partner in the old sense. Brolin's Bangley is all coiled menace and hard-won pragmatism, a man who stayed alive by treating sentiment as a liability and who is quietly, never-admitted, grateful that Hig did not. The film has no interest in the ideological fashions of 2026. It tells a story about self-reliance, protection of the vulnerable, the dignity of work, and the possibility of building something new from the ruins of the old. That it does so without preaching or winking at the audience is its quiet triumph.",
        "oneLiner": "Nine years after a pandemic wiped out most of humanity, a grieving pilot at an abandoned Colorado airfield risks everything to investigate a faint radio transmission from beyond his fuel range, and in the process discovers that survival without human connection is not survival at all.",
        "adultInsight": "The Dog Stars is not a political film, and that is precisely what makes it interesting in 2026. It participates in no culture war, signals no allegiance, and takes no position on the controversies that consume our discourse. What it does instead is tell a story that assumes certain things are true: that a man owes protection to those weaker than himself, that work and craft are dignifying, that grief is not a pathology but a proof of love, and that the people who survive the collapse of civilization are not the ones with the most ideology but the ones with the most skill. Hig is a pilot, a hunter, a fisherman, a mechanic. These are not political identities. They are the things a man becomes when he must keep himself and others alive. The film's worldview is traditional in the deepest sense, not because it argues for tradition but because it takes tradition for granted as the ground on which human life is possible. When Hig helps the Mennonite community near the airfield, he does not do it to make a point. He does it because they need help and he can help them. The film trusts the audience to understand that this is what good men do. That trust, in an era when every story seems to come with a lecture attached, feels like clean air.",
        "parentalGuidance": "PG-13 for thematic content involving a global pandemic and its aftermath, some violence and peril, and brief strong language. The post-apocalyptic setting includes scenes of abandoned towns and implied mass death. A dog dies peacefully of old age (emotional but not graphic). Human antagonists are killed in self-defense. No sexual content beyond a developing romantic relationship. Suitable for mature teenagers and up. The pandemic premise may be unsettling for younger viewers or those with pandemic-related trauma."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-028",
            "name": "The Rugged Individualist",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Hig is the definition of the rugged individualist: he flies his own plane, maintains his own equipment, hunts his own food, and survives through competence and self-reliance. The entire film is built around his solitary competence. The character arc does not challenge this individualism but deepens it by showing it is incomplete without human connection. Severity 4: Hig's self-reliance is the film's organizing principle. Authenticity High (0.7): consistent with Peter Heller's novel and the post-apocalyptic survival genre. Centrality High (1.8): the film IS Hig's solitary journey."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Hig repeatedly protects the vulnerable: delivering supplies to the Mennonite community, defending the airfield from armed raiders, rescuing Cima and Pops and bringing them to safety. His protective instinct is not framed as toxic but as the core of his moral identity. The climax involves protecting his new community from attackers at Grand Junction. Severity 4: protection is the primary moral action in the film. Authenticity High (0.7): organic to survival fiction and the source novel. Centrality High (1.8): every major plot beat involves protecting someone."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "explanation": "The moral framework is clear: those who prey on survivors (the Grand Junction ambushers, the raiders who pursue Hig) are evil; those who protect and help others (Hig, Bangley, Pops, the Mennonites) are good. The film does not moralize about the attackers' circumstances or suggest moral equivalence. Severity 2: present but not the film's primary argument. Authenticity Moderate (1.0): genre convention rather than unique to this adaptation. Centrality Moderate (1.0): supports the narrative without being its thesis."
        },
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Bangley is a protector figure who, despite his harshness, provides the defensive structure that keeps Hig alive. Pops, the elderly former Navy SEAL, has protected his daughter Cima for years and is willing to die for her. Hig himself grows into this role, becoming the protector of his new community. The film portrays protective masculinity as noble and necessary. Severity 3: a significant thematic strand. Authenticity High (0.7): deeply rooted in the novel and genre. Centrality Moderate (1.0): thematically important but not the sole focus."
        },
        {
            "id": "TRADITIONAL-034",
            "name": "Sanctity of Marriage",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "Hig's grief for his dead wife Melissa is the emotional foundation of his character. She was pregnant when she died, and his mourning is not something he overcomes but something he carries. His eventual relationship with Cima is treated as healing and recommitment to life, not casual replacement. The film honors the weight of the marital bond even in death. Severity 2: present as emotional truth rather than argument. Authenticity High (0.7): deeply authentic to the novel. Centrality Moderate (1.0): drives character motivation throughout."
        },
        {
            "id": "TRADITIONAL-041",
            "name": "Industry and Perseverance",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "The film lingers on Hig's daily labor: maintaining his plane, patrolling, hunting, repairing equipment. His survival is not luck or fate but the product of sustained work and skill. This dignifies manual competence as a moral quality. Severity 2: visible throughout. Authenticity High (0.7): authentic to the survival genre. Centrality Low (0.5): background texture rather than foreground theme."
        },
        {
            "id": "TRADITIONAL-040",
            "name": "Stewardship of Creation",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "The Colorado wilderness is not an obstacle to be conquered but a gift to be tended. Hig's hunting, fishing, and flying are acts of engagement with creation, not exploitation. The death of his dog Jasper is treated with genuine reverence, as a creature whose life had dignity. Severity 2: woven into the visual and emotional texture. Authenticity High (0.7): consistent with Heller's nature writing. Centrality Low (0.5): aesthetic rather than thematic."
        },
        {
            "id": "TRADITIONAL-043",
            "name": "Faith in Adversity",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.0,
            "explanation": "While not explicitly religious, the film depicts Hig finding meaning and purpose after devastating loss. His flight beyond the point of no return is an act of faith in something beyond survival, a belief that there is still something worth finding. The Mennonite community provides a quiet religious presence. Severity 2: spiritual undercurrent. Authenticity Moderate (1.0): present but not the explicit framework. Centrality Low (0.5): atmospheric rather than structural."
        },
        {
            "id": "WOKE-005",
            "name": "Chosen Family over Bio-Kin",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "Hig forms a new community with Bangley, Cima, and Pops that replaces his lost biological family. However, this is not portrayed as an ideological preference for chosen family over blood. His wife and unborn child are dead from the pandemic; he forms new bonds out of necessity and human need, not rejection of biological ties. Severity 1: trace element. Authenticity High (0.7): this is the reality of post-apocalyptic survival, not a political statement. Centrality Low (0.5): set dressing."
        },
        {
            "id": "WOKE-001",
            "name": "Institutional Collapse as Moral Vacuum",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "explanation": "The film's post-apocalyptic setting implies that government, medicine, and civil society failed during the pandemic. However, this is standard genre convention for post-apocalyptic fiction and the film does not linger on assigning blame to specific institutions. Severity 1: background premise. Authenticity Moderate (1.0): genre convention not political argument. Centrality Low (0.5): the setting, not the message."
        }
    ],
    "seo": {
        "titleTag": "Is The Dog Stars (2026) Woke? Ridley Scott's New Post-Apocalyptic Film | VirtueVigil",
        "metaDescription": "VirtueVigil's VVWS review of The Dog Stars (2026), Ridley Scott's post-apocalyptic survival drama starring Jacob Elordi and Josh Brolin. Verdict: TRADITIONAL (+17 TRAD). Full trope scores and parental guidance included.",
        "keywords": "is the dog stars woke, the dog stars 2026 review, the dog stars virtuevigil, ridley scott the dog stars review, jacob elordi the dog stars, the dog stars parents guide, the dog stars traditional or woke, dog stars movie 2026"
    },
    "parentalGuidance": "PG-13 for thematic content involving a global pandemic and its aftermath, some violence and peril, and brief strong language. The post-apocalyptic setting includes scenes of abandoned towns and implied mass death. A dog dies peacefully of old age (emotional but not graphic). Human antagonists are killed in self-defense. No sexual content beyond a developing romantic relationship. Suitable for mature teenagers and up."
}

# ============================================================
# REVIEW 2: TWILIGHT (2008) — Catalog Backfill
# ============================================================
twilight = {
    "id": "twilight-2008",
    "slug": "twilight-2008",
    "title": "Twilight (2008)",
    "year": 2008,
    "type": "film",
    "platform": "Theatrical / Streaming",
    "genre": "Romantic Fantasy, Drama",
    "date": "2026-08-27",
    "datePublished": "2026-08-27",
    "author": "VirtueVigil Editorial Team",
    "readTime": "11 min",
    "poster": "/images/posters/twilight-2008.jpg",
    "releaseDate": "2008-11-21",
    "rating": "PG-13",
    "runtime": "121 min",
    "director": "Catherine Hardwicke",
    "writers": "Melissa Rosenberg",
    "cast": [
        "Kristen Stewart",
        "Robert Pattinson",
        "Billy Burke",
        "Peter Facinelli",
        "Ashley Greene",
        "Taylor Lautner"
    ],
    "studio": "Summit Entertainment, Temple Hill Entertainment, Maverick Films",
    "distributor": "Summit Entertainment",
    "verdict": "TRADITIONAL",
    "wokeScore": 0.85,
    "tradScore": 19.8,
    "authIndex": "High",
    "scoreMargin": "+19 TRAD",
    "preRelease": None,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Twilight is ideologically transparent from its first scenes. Bella's voiceover establishes her dislocation, her move to Forks, and her immediate fascination with Edward Cullen, all within the first fifteen minutes. The film's central dynamic, a supernatural romance built on Edward's self-restraint and Bella's willing vulnerability, is established early and never hidden. The film's traditional sexual ethics (Edward's refusal of premarital sex, the marriage-before-intimacy arc across the series) are explicit. The film does not pretend to be something other than what it is: a romantic fantasy grounded in self-denial, protection, and permanent commitment. No ideological bait-and-switch occurs because the ideology is worn on its sleeve from the opening credits."
    },
    "summary": {
        "overall": "Twilight is one of the most ideologically misunderstood films of the 21st century. It was mocked by cultural conservatives as vampire drivel for teenage girls and condemned by feminists as a regressive fantasy of female submission. Both camps missed the obvious: Twilight is, by the standards of modern Hollywood, a deeply conservative movie. Bella Swan (Kristen Stewart) moves to the perpetually overcast town of Forks, Washington, to live with her father Charlie, the town's gentle but slightly hapless police chief. At school she encounters the Cullen family, five eerily beautiful adopted siblings who keep to themselves. One of them, Edward (Robert Pattinson), seems to loathe her on sight. He is actually a 108-year-old vampire fighting an overwhelming urge to kill her, because her blood smells to him like nothing he has encountered in a century of self-denial. The central plot, once the two admit their attraction, is whether Edward can keep Bella alive long enough to love her without destroying her. A rival coven of vampires led by the tracker James arrives and targets Bella for sport, forcing the Cullen family to defend her in a climactic ballet-studio confrontation. The film works as romance because Pattinson and Stewart sell the longing, and as melodrama because Catherine Hardwicke's direction understands that teenage emotions feel like life and death. The blue-tinted Pacific Northwest is genuinely beautiful, and the baseball game in the thunderstorm remains one of the most purely enjoyable sequences in any YA adaptation. What makes Twilight ideologically remarkable is what it refuses to do. Edward is a male lead in a 2008 teen romance who insists on waiting until marriage. He does not struggle with this because he thinks sex is dirty; he struggles because he is a predator who could kill Bella by accident and wants to do nothing that might harm her. His self-restraint is framed as romantic and noble, not repressed and pathological. Bella is not a girlboss. She is clumsy, bookish, devoted to her father, and willing to give up her humanity for the man she loves. Her choice is hers, but what she chooses is permanent commitment. The film's feminism, insofar as it has one, is not the feminism of independence and career ambition but the older feminism of choosing your own chains. Dr. Carlisle Cullen (Peter Facinelli) leads a family of vampires who have chosen to drink animal blood rather than human, a discipline he enforces as both patriarch and moral exemplar. The Cullens are functional precisely because they adhere to a code. The villains, James and his coven, are predators who indulge their appetites. The moral contrast is not subtle. Twilight is not a conservative polemic. It is a love story. But the love it valorizes is built on self-denial, protection, permanence, and the belief that some things are worth dying for. In 2008, that was enough to get it laughed out of the room. In 2026, it reads like a dispatch from a lost civilization.",
        "oneLiner": "A teenage girl moves to a small Washington town and falls in love with a 108-year-old vampire who must fight his own predatory nature to protect her from himself and from a rival coven that wants her dead.",
        "adultInsight": "Twilight became a cultural punching bag for reasons that had almost nothing to do with what is actually on screen. The mockery was about the audience (teenage girls) and the genre (supernatural romance), not the content. Rewatching the film in 2026, what strikes you is not the silliness of sparkly vampires but the seriousness with which the film takes its moral premises. Edward's refusal to have sex with Bella until they are married is not a joke the film is in on. It is the emotional center of the character. When Bella asks him why he is waiting, he says he does not want to take anything from her that she cannot get back. In a culture that has spent two decades insisting that sexual restraint is either impossible or pathological, a film where the male lead's entire romantic appeal is that he will not touch the girl he loves is genuinely transgressive. The film's feminism debate is likewise more interesting than either side admitted. Bella chooses Edward. She chooses to become a vampire. She chooses permanent, irreversible commitment to one person. These are choices that progressive feminism cannot honor because they look like submission, and that traditional conservatism cannot honor because they are made by a teenage girl without consulting her father. But Twilight takes Bella's choices seriously, and that is more than most films do with their female protagonists. The tragedy of Twilight's cultural reception is that a film about the beauty of restraint was dismissed by both the left (which saw repression) and the right (which saw vampire trash). Both were wrong.",
        "parentalGuidance": "PG-13 for some violence and a scene of sensuality. The film contains vampire-related violence including a character being bitten, a broken neck, and a fight sequence in a ballet studio with some blood. Edward and Bella share intense kisses and one scene of them lying together fully clothed in a bed after an intimate conversation; the scene is emotionally charged but physically chaste. No nudity, no sex, no profanity beyond mild language. The central relationship involves a significant age gap (108 years vs 17), though Edward is physically and emotionally portrayed as a teenager. Suitable for teenagers and up. The film's positive portrayal of abstinence and commitment may be useful for parent-teen conversations."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-034",
            "name": "Sanctity of Marriage",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Edward Cullen refuses to have sex with Bella before marriage. This is not a minor character detail; it is the defining feature of their relationship across the entire saga. In a 2008 teen romance, the male lead's insistence on waiting until marriage was genuinely countercultural. The film presents sexual restraint as romantic, noble, and an expression of love rather than repression. Severity 3: a major thematic element. Authenticity High (0.7): Stephenie Meyer is Mormon and the abstinence theme is deliberate authorial intent. Centrality High (1.8): drives the central relationship."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The entire climax of the film is the Cullen family's coordinated effort to protect Bella from James, a tracker vampire who wants to kill her for sport. Edward races to save her; Carlisle and the family mobilize as a unit; Bella herself tries to sacrifice herself to protect her mother. Protection of the vulnerable is the film's central moral action. Severity 4: the protection arc is the entire third act. Authenticity High (0.7): deeply embedded in Meyer's moral universe. Centrality High (1.8): the climactic sequence revolves entirely around who will protect whom."
        },
        {
            "id": "TRADITIONAL-026",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Edward is willing to leave Bella to protect her from himself and his world; Bella is willing to trade her life to James to save her mother; Edward races toward James knowing he may die. Self-sacrificial love is the film's emotional currency. Severity 3: a recurring motif across multiple characters. Authenticity High (0.7): consistent with the novel's moral framework. Centrality High (1.8): self-sacrifice shapes multiple character decisions at key plot points."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 3.0,
            "explanation": "The Cullen family are 'vegetarian' vampires who drink only animal blood and live by a moral code. James, Victoria, and Laurent are predatory vampires who kill humans without remorse. The moral binary is explicit and undisputed: the Cullens choose restraint and are good; the nomads choose predation and are evil. Carlisle's leadership is built on moral conviction, not mere survival strategy. Severity 3: the moral contrast between the two covens defines the conflict. Authenticity Moderate (1.0): genre convention in vampire fiction. Centrality Moderate (1.0): important but not the deepest theme."
        },
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Carlisle Cullen is the moral and organizational center of the Cullen family. He established their dietary code centuries ago, leads with gentle authority, and is framed as the ideal patriarch: protective, wise, and committed to an ethical principle (do no harm). The family functions because of his moral leadership. Severity 3: Carlisle's role is significant to the story's moral framework. Authenticity High (0.7): Meyer constructed Carlisle as a Christ-like figure. Centrality Moderate (1.0): important supporting character, not the protagonist."
        },
        {
            "id": "TRADITIONAL-030",
            "name": "Biblical Morality",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "The film's moral framework (sexual restraint before marriage, self-sacrificial love, the valorization of permanent commitment, the notion of resisting one's darker nature through moral discipline) aligns with Judeo-Christian ethics. This is not accidental: Stephenie Meyer is a practicing Mormon and her worldview permeates the material. The Cullens' choice to abstain from human blood is essentially a dietary version of original sin and redemption. Severity 2: present as subtext and worldview, not explicit preaching. Authenticity High (0.7): deliberate authorial intent. Centrality Moderate (1.0): informs the whole but is never foregrounded."
        },
        {
            "id": "TRADITIONAL-036",
            "name": "Traditional Femininity",
            "category": "Traditional",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 0.7,
            "explanation": "Bella is distinctly non-girlboss. She cooks for her father, she is clumsy and physically vulnerable, she is bookish and introspective rather than assertive, and her desires are oriented toward permanent commitment and family rather than independence or career. The film does not frame these traits as weaknesses or as something she needs to overcome. Severity 1: present as character traits, not as an ideological argument. Authenticity High (0.7): Meyer wrote Bella as intentionally non-feminist. Centrality Moderate (1.0): Bella's nature shapes the story but is not its thesis."
        },
        {
            "id": "WOKE-002",
            "name": "The Bumbling Patriarch",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "Charlie Swan, Bella's father, is the town police chief but is portrayed as slightly hapless in domestic life. Bella cooks for him, and he is awkward about emotional conversations. However, he is also loving, protective, and taken seriously as a father figure. The film does not mock him as incompetent; it portrays him as a decent man who has been a single father doing his best. Severity 1: mild and affectionate rather than hostile. Authenticity High (0.7): consistent with Meyer's sympathetic portrayal of the character. Centrality Low (0.5): supporting character texture."
        },
        {
            "id": "WOKE-005",
            "name": "Chosen Family over Bio-Kin",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.5,
            "explanation": "Bella's emotional center of gravity shifts from her biological parents (Charlie in Forks, her mother Renee in Arizona) toward the Cullen family. However, this is portrayed as a romantic trajectory (she is joining a family through marriage), not a rejection of biological ties. She maintains a loving relationship with Charlie throughout. Severity 1: present as romance convention, not ideological statement. Authenticity Moderate (1.0): young adult genre convention. Centrality Low (0.5): the Cullens are her future, not a rebuttal to her past."
        }
    ],
    "seo": {
        "titleTag": "Is Twilight (2008) Woke? The Surprising Traditional Values of the Twilight Saga | VirtueVigil",
        "metaDescription": "VirtueVigil's VVWS review of Twilight (2008) starring Kristen Stewart and Robert Pattinson. The vampire romance you thought was progressive is actually quite traditional. Verdict: TRADITIONAL (+19 TRAD). Full analysis.",
        "keywords": "is twilight woke, twilight 2008 review, twilight virtuevigil, twilight traditional or woke, twilight parents guide, bella and edward relationship analysis, twilight saga woke score, stephenie meyer twilight ideology"
    },
    "parentalGuidance": "PG-13 for some violence and a scene of sensuality. Vampire-related violence includes a character being bitten, a broken neck, and a climactic fight sequence with some blood. Edward and Bella share intense kisses; one scene shows them lying together fully clothed after an intimate conversation, emotionally charged but physically chaste. No nudity, no sex, no significant profanity. Suitable for teenagers and up. The film's positive portrayal of abstinence and commitment may be a useful conversation starter."
}

# ============================================================
# REVIEW 3: THE WALKING DEAD (2010) — TV/Series
# ============================================================
twd = {
    "id": "the-walking-dead-2010",
    "slug": "the-walking-dead-2010",
    "title": "The Walking Dead (2010)",
    "year": 2010,
    "type": "series",
    "platform": "AMC",
    "genre": "Post-Apocalyptic, Horror, Drama",
    "date": "2026-08-27",
    "datePublished": "2026-08-27",
    "author": "VirtueVigil Editorial Team",
    "readTime": "12 min",
    "poster": "/images/posters/the-walking-dead-2010.jpg",
    "releaseDate": "2010-10-31",
    "rating": "TV-MA",
    "runtime": "11 seasons, 177 episodes",
    "director": "Frank Darabont (developer)",
    "writers": "Frank Darabont, Robert Kirkman, Angela Kang, Scott M. Gimple, Glen Mazzara",
    "cast": [
        "Andrew Lincoln",
        "Norman Reedus",
        "Melissa McBride",
        "Danai Gurira",
        "Lauren Cohan",
        "Chandler Riggs",
        "Steven Yeun",
        "Jeffrey Dean Morgan"
    ],
    "studio": "AMC Studios, Circle of Confusion, Valhalla Entertainment",
    "distributor": "AMC Networks",
    "verdict": "TRADITIONAL",
    "wokeScore": 5.45,
    "tradScore": 23.34,
    "authIndex": "High",
    "scoreMargin": "+18 TRAD",
    "preRelease": None,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "The Walking Dead announces its ideological framework from the pilot episode. Rick Grimes wakes from a coma, discovers the world has ended, and immediately begins searching for his wife and son. The first season establishes the series' core thesis: civilization has collapsed, and the question is what kind of society will replace it. The series' traditional elements (Rick's protective leadership, the valorization of family, the insistence that community requires moral limits) and its progressive elements (diverse casting, eventually same-sex relationships) are both present from early on and neither is hidden. The show has never pretended to be a light zombie thriller; it has always been a moral drama about what people owe each other when the law is gone. The woke content is woven into the fabric of the show from the beginning, not concealed past the halfway point."
    },
    "summary": {
        "overall": "The Walking Dead ran for 11 seasons, 177 episodes, and at its peak was the most-watched scripted series in cable television history. It absorbed an enormous amount of cultural energy and then, like most phenomena, faded. Reassessed as a complete work, it is a more interesting and ideologically complex artifact than either its fans or its detractors gave it credit for. Andrew Lincoln plays Rick Grimes, a Georgia sheriff's deputy who wakes from a coma to find the world overrun by the reanimated dead. He finds his wife Lori and son Carl alive in a camp outside Atlanta, and from that point forward the series is a sustained study in what leadership costs, what community requires, and how thin the membrane of civilization really is. The walkers are not the real threat. They are the setting. The real threat is what the survivors become in the absence of law, the groups and tribes and would-be emperors who fill the vacuum. The Governor runs Woodbury as a cult of personality. Negan runs the Saviors as a protection racket with a baseball bat. The survivors at Terminus solve the food problem by becoming cannibals. Each antagonist forces Rick's group to confront a version of what they might become if they lose the thread of their own humanity. The series' greatest strength and its greatest limitation are the same thing: it is morally serious in a way that television almost never is, but it is not ideologically sophisticated. It believes in leadership, but has no theory of legitimacy beyond whoever is least bad. It believes in community, but cannot decide whether democracy (Alexandria's council), monarchy (Ezekiel's Kingdom), or strongman rule (Rick's de facto dictatorship) is the answer. It believes in family, but kills off so many characters that family becomes a revolving door. It believes in redemption, but the body count makes redemption feel like a rounding error. Nevertheless, the show's moral instincts are remarkably traditional. Rick is a protector and a father before he is anything else. His defining speech is not about freedom or rights but about responsibility: 'This is not a democracy anymore.' He says this not to seize power but because he has accepted that protecting people sometimes requires making decisions they will not like. The series endorses the hard truth that in a crisis, someone must lead, and that leadership means bearing what others cannot. Daryl Dixon (Norman Reedus) is the series' conscience: a man from an abusive background who discovers his own capacity for loyalty and sacrifice. Carol Peletier (Melissa McBride) is the series' most audacious arc: an abused housewife who becomes the deadliest survivor in the group, not through empowerment rhetoric but through tragedy and necessity. Glenn and Maggie's romance is the series' moral center, a conventional love story treated with absolute sincerity. The show's progressive elements, the diverse casting, the same-sex relationships in later seasons, the strong female characters who fight and lead, are integrated into this traditional framework rather than competing with it. The show does not frame Carol's transformation as a feminist triumph over patriarchy but as a woman who lost everything and learned to fight so she would not lose anyone else. It does not frame Michonne as a girlboss but as a grieving mother who found a new family. It does not frame Aaron's homosexuality as a political statement but as an ordinary fact about a character who happens to be gay. This is, in its way, more genuinely integrative than most shows that make identity their subject. The Walking Dead is too long, too repetitive, and too uneven to be called a masterpiece. But it is more ambitious than it needed to be, and its ambition was moral. It wanted to know what happens to people when everything is stripped away. Its answer, repeated across 177 hours, is that some become monsters, some become martyrs, and some, the ones the show admires most, become leaders who carry the weight so others do not have to. That is not a woke answer. It is not even a particularly modern answer. It is the oldest answer we have.",
        "oneLiner": "A Georgia sheriff's deputy wakes from a coma to find the world overrun by the reanimated dead and must lead a group of survivors through 11 seasons of moral collapse, community-building, and the question of what humanity costs when civilization is gone.",
        "adultInsight": "The Walking Dead's politics resist easy categorization, which is why both cultural poles have alternately claimed and rejected it. The show is skeptical of authority but insists on leadership. It distrusts institutions but valorizes communities. It features strong female characters who fight and lead but does not frame their strength as a rejection of femininity. It includes same-sex relationships but treats them as unremarkable. The progressive viewer can find a show that centers a Black female lead (Michonne), features multiple gay characters, and depicts traditional masculinity as a trap that gets people killed. The conservative viewer can find a show that insists on the necessity of strong fathers, the sanctity of marriage vows, the limits of democracy in a crisis, and the moral superiority of people who protect the weak over people who prey on them. Both viewers would be right, and that is the show's most interesting quality. It is not ideologically incoherent. It is ideologically capacious. It has room for both Michonne's arc as a warrior-mother and Rick's arc as a protective patriarch because the show's moral framework is not identity-based but action-based. What matters is not who you are but what you do when the choice costs you something. This framework, in which character is revealed by action under pressure rather than by membership in a category, is the core of classical drama. The Walking Dead is classical drama with a zombie apocalypse skin. Its limitations are the limitations of that form: it can show you what a good man does in a crisis but cannot tell you what a good society looks like in peacetime. It can valorize the family but cannot, after 11 seasons of killing off characters, sustain one. It can insist on the importance of moral limits but cannot, given its genre, avoid normalizing the violence it is supposed to be questioning. But these are the problems of ambition, not of failure. The show reached for something, and what it reached for was a portrait of human decency under pressure. In the television landscape of 2010, and still in 2026, that is not nothing.",
        "parentalGuidance": "TV-MA. This series contains extreme and graphic violence throughout, including depictions of zombies eating humans, humans killing zombies in gruesome ways, and humans killing other humans in brutal fashion. Decapitation, dismemberment, gun violence, blunt force trauma, and torture are depicted. Sexual content is minimal (implied rather than shown) but the series deals with dark themes including rape, suicide, infanticide, and child death. Strong language throughout. Not suitable for viewers under 17. Parents should know that while the series has a strong moral framework (protecting the innocent, the importance of family, the cost of leadership), the violence required to convey that framework is intense and unrelenting."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-029",
            "name": "The Principled Patriarch",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "Rick Grimes is the defining principled patriarch of 21st-century television. He begins as a sheriff's deputy whose first act upon waking from a coma is to find his wife and son. His entire arc across 11 seasons is the burden and cost of protecting his family and his people. His most famous line is not a threat but a statement of responsibility: he will do what must be done so others do not have to. The series frames his protective leadership as noble, necessary, and personally devastating. Severity 5: Rick's protective fatherhood IS the series. Authenticity High (0.7): consistent with Robert Kirkman's comic and the post-apocalyptic survival genre. Centrality High (1.8): every major plot decision flows through Rick's role as patriarch."
        },
        {
            "id": "TRADITIONAL-045",
            "name": "Defense of the Innocent",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The protection of the vulnerable (children, the elderly, the weak) is the moral throughline of the entire series. The group's decisions are consistently framed around who can be protected and at what cost. The series valorizes those who protect (Rick, Daryl, Michonne, Glenn) and condemns those who prey on the weak (the Governor, Negan, the Terminus cannibals). Hershel's farm, the prison, Alexandria: every community is evaluated by how it treats its most vulnerable. Severity 4: the moral framework of the series. Authenticity High (0.7): deeply embedded in the source material and genre. Centrality High (1.8): every season revolves around who will protect whom."
        },
        {
            "id": "TRADITIONAL-026",
            "name": "The Self-Sacrificing Hero",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 3.0,
            "explanation": "Self-sacrifice is the series' recurring motif. Dale tries to reason with a walker to buy the group time. Hershel risks his life to treat the sick. Glenn saves others repeatedly until it costs him his life. Daryl repeatedly takes the hardest jobs so others do not have to. Rick sacrifices his peace, his sanity, and eventually his presence in his children's lives for the group. Severity 3: a recurring and prominent theme. Authenticity Moderate (1.0): authentically embedded in the narrative but also a genre convention of zombie fiction. Centrality Moderate (1.0): important supporting theme rather than the primary subject."
        },
        {
            "id": "TRADITIONAL-034",
            "name": "Sanctity of Marriage",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Glenn and Maggie's marriage is the series' moral and emotional anchor. Their relationship is presented without irony as a genuine, committed union that gives both characters something worth fighting for. Rick and Lori's marriage, strained by her affair with Shane during Rick's coma, is portrayed as a tragedy of circumstance rather than an endorsement of infidelity. The series treats marriage vows as binding and significant. Severity 3: the Glenn-Maggie relationship is central to the show's emotional architecture. Authenticity High (0.7): deeply authentic to the characters and their arcs. Centrality Moderate (1.0): a significant strand but not the only one."
        },
        {
            "id": "TRADITIONAL-039",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "While the series explores moral gray areas, it maintains a clear moral framework: those who protect the weak and build community are good (Rick's group, Alexandria, Hilltop, the Kingdom); those who prey on the weak and rule through fear are evil (the Governor, Negan's Saviors, Terminus, the Wolves). The series never equivocates about who the audience should root for. Severity 3: the moral binary is explicit and driving. Authenticity High (0.7): consistent with the comic's moral universe. Centrality Moderate (1.0): defines the conflict structure but the series also explores moral complexity within the good camp."
        },
        {
            "id": "TRADITIONAL-035",
            "name": "The Just Lawman",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.1,
            "explanation": "Rick begins as a sheriff's deputy and his law enforcement identity shapes his entire leadership style. Even as he moves beyond the formal law, he creates and enforces a moral code for his group. The series takes law enforcement seriously as a moral vocation. When Rick kills, he does so as an act of protection and justice, not revenge. Severity 3: Rick's lawman identity is foundational. Authenticity High (0.7): authentic to the character's construction. Centrality Moderate (1.0): shapes his decisions throughout but the law is mostly gone."
        },
        {
            "id": "TRADITIONAL-037",
            "name": "Small-Town Integrity",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "explanation": "The communities that survive and thrive (Alexandria, Hilltop, the Kingdom) are essentially small towns with local governance, mutual obligation, and face-to-face relationships. The series consistently frames local community as the only viable form of social organization after the collapse. Bureaucratic or authoritarian large-scale systems (the CRM in later seasons) are framed as corrupt or inhuman. Severity 2: visible as structural preference. Authenticity Moderate (1.0): post-apocalyptic survival logic rather than political argument. Centrality Moderate (1.0): the community scale shapes many seasons."
        },
        {
            "id": "TRADITIONAL-042",
            "name": "The Forgiving Heart",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "Rick's decision to spare Negan rather than execute him after the war is the series' most controversial moral choice and its most traditionally Christian. Rick chooses mercy over vengeance, arguing that the new civilization they are building must be better than the one they destroyed. Carl's deathbed wish is that his father find peace rather than more enemies to kill. Severity 2: significant but a late-series development. Authenticity High (0.7): consistent with Rick's character arc toward moral rehabilitation. Centrality Low (0.5): a climactic decision but not the series' overall structure."
        },
        {
            "id": "WOKE-003",
            "name": "The Girl Boss",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 2.0,
            "explanation": "Michonne, Carol, and Maggie all become highly competent warriors and leaders. Carol's transformation from abused housewife to deadliest fighter in the group has elements of the girlboss arc, and Michonne's katana-wielding warrior persona can read as the aggressive, hyper-masculinized female lead. However, the series frames their strength as born of tragedy and necessity rather than gender ideology, and none of the three pathologizes femininity or promotes gender antagonism. Severity 2: visible but not the show's framing. Authenticity Moderate (1.0): partly genuine character development, partly satisfying a cultural expectation. Centrality Moderate (1.0): these are major characters whose arcs could not be removed."
        },
        {
            "id": "WOKE-018",
            "name": "Heteronormativity as Harm",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 1.4,
            "explanation": "Several same-sex relationships are introduced in later seasons (Tara, Aaron, Jesus, Yumiko/Magna). These are presented as normal and unremarkable, which is the 'integration' approach to LGBT representation. However, the late-series concentration and the fact that these characters are among the show's most virtuous creates a pattern of progressivism-as-goodness. Severity 2: multiple recurring characters. Authenticity Low (1.4): these feel like representational checkmarks rather than organically developed character elements. Centrality Low (0.5): these characters are supporting cast members whose sexuality is not central to the plot."
        },
        {
            "id": "WOKE-008",
            "name": "The Bigoted Traditionalist",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 1.0,
            "explanation": "Merle Dixon (Michael Rooker) is a racist, sexist redneck whose bigotry is presented as a moral failing he must (and partially does) overcome. The series uses Merle to show that old prejudices are a liability in the new world. Severity 2: Merle is a significant recurring character in seasons 1-3. Authenticity Moderate (1.0): Merle is a well-drawn character with complexity, not a cardboard bigoted strawman. Centrality Low (0.5): his arc is supporting and he dies in season 3."
        },
        {
            "id": "WOKE-001",
            "name": "Anachronistic Diversity Casting",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.7,
            "explanation": "The series features deliberate diversity in its casting that, while admirable, sometimes strains credibility for the rural Georgia setting. A Korean-American pizza delivery boy, a Black lawyer with a katana, and multiple interracial relationships in the deep South feel more like 2010s Hollywood casting sensibilities than organic 2010 Georgia demographics. The comic source material was similarly diverse by design. Severity 1: present but unobtrusive for most viewers. Authenticity Low (1.4): deliberate representational casting rather than organic to the setting. Centrality Low (0.5): the diversity is visual rather than thematic."
        },
        {
            "id": "WOKE-004",
            "name": "Institutional Evil",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.35,
            "explanation": "Government and military institutions have completely collapsed and are often revealed to have been corrupt or incompetent before the fall (the CDC, the military's Operation Cobalt). However, this is genre convention in zombie apocalypse fiction and the series does not dwell on assigning political blame. Severity 1: background premise. Authenticity High (0.7): consistent with the zombie genre. Centrality Low (0.5): the collapse is setting, not message."
        }
    ],
    "seo": {
        "titleTag": "Is The Walking Dead (2010) Woke? AMC's Zombie Series Full VVWS Review | VirtueVigil",
        "metaDescription": "VirtueVigil reviews The Walking Dead (2010), AMC's 11-season zombie drama starring Andrew Lincoln. A morally complex series with traditional instincts. Verdict: TRADITIONAL (+18 TRAD). Full trope scores and parental guidance.",
        "keywords": "is the walking dead woke, the walking dead 2010 review, walking dead virtuevigil, the walking dead traditional or woke, walking dead parents guide, rick grimes leadership analysis, amc walking dead woke score, the walking dead series review"
    },
    "parentalGuidance": "TV-MA. Extreme and graphic violence throughout all 11 seasons, including depictions of zombies eating humans, humans killing zombies in gruesome ways, and humans killing other humans. Decapitation, dismemberment, gun violence, and torture are regularly depicted. Sexual content is minimal and typically implied rather than shown. The series deals with dark themes including rape, suicide, domestic abuse, infanticide, and child death. Strong language. Not suitable for viewers under 17."
}

reviews_data = [dogstars, twilight, twd]

# Validate
for rev in reviews_data:
    slug = rev["slug"]
    if slug in existing_slugs:
        print(f"ERROR: {slug} already exists!")
        exit(1)
    # Verify scoring
    calc_trad = sum(t["weightedScore"] for t in rev["tropeAudit"] if t["category"] == "Traditional")
    calc_woke = sum(t["weightedScore"] for t in rev["tropeAudit"] if t["category"] == "Woke")
    calc_margin = round(calc_trad - calc_woke)
    print(f"{slug}: trad={calc_trad:.2f} woke={calc_woke:.2f} margin={calc_margin}")
    print(f"  stored: tradScore={rev['tradScore']} wokeScore={rev['wokeScore']} scoreMargin={rev['scoreMargin']}")
    assert abs(calc_trad - rev["tradScore"]) < 0.01, f"{slug}: tradScore mismatch: stored {rev['tradScore']} vs calculated {calc_trad}"
    assert abs(calc_woke - rev["wokeScore"]) < 0.01, f"{slug}: wokeScore mismatch"
    expected_label = f"+{calc_margin} TRAD" if calc_margin > 0 else f"{calc_margin} WOKE" if calc_margin < 0 else "0 NEUTRAL"
    print(f"  expected label: {expected_label}")

# Append
reviews.extend(reviews_data)
with open(REVIEWS_PATH, "w") as f:
    json.dump(reviews, f, indent=2, ensure_ascii=False)
print(f"\nAppended {len(reviews_data)} reviews. Total: {len(reviews)}")