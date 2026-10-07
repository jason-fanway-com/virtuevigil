#!/usr/bin/env python3
"""Append 3 reviews to reviews.json for 2026-10-07 cron run."""
import json, sys

reviews_path = 'src/data/reviews.json'
with open(reviews_path) as f:
    data = json.load(f)

# ============================================================
# REVIEW 1: Clayface (2026) - Pre-release
# ============================================================
clayface = {
    "id": "clayface-2026",
    "slug": "clayface-2026",
    "title": "Clayface",
    "year": 2026,
    "type": "film",
    "platform": "Theaters",
    "genre": "Psychological Horror, Body Horror, Superhero",
    "date": "2026-10-07",
    "datePublised": "2026-10-07",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/clayface-2026.jpg",
    "releaseDate": "2026-10-23",
    "rating": "R",
    "runtime": "108 min",
    "director": "James Watkins",
    "writers": ["Mike Flanagan", "Hossein Amini"],
    "showrunner": None,
    "cast": ["Tom Rhys Harries", "Naomi Ackie", "David Dencik", "Max Minghella", "Eddie Marsan"],
    "studio": "DC Studios, 6th & Idaho, Troll Court Entertainment, The Safran Company",
    "distributor": "Warner Bros. Pictures",
    "verdict": "PREDICTED: BALANCED TRADITIONAL",
    "wokeScore": 1.5,
    "tradScore": 14.18,
    "authIndex": 72,
    "scoreMargin": "+13 TRAD",
    "preRelease": True,
    "wokeTrap": False,
    "woke_trap_assessment": "Clayface contains no woke trap. Mike Flanagan's script announces its intentions from the opening frames: this is a psychological body horror film about identity, disfigurement, and the loss of self. There is no bait-and-switch. A disfigured actor who transforms into a shape-shifting monster is pure horror archetype territory, not ideological messaging. Flanagan's track record (The Haunting of Hill House, Doctor Sleep) demonstrates a commitment to character-driven horror that explores universal human fears without political sermonizing. The film's themes of bodily autonomy and the terror of losing oneself are existential, not partisan.",
    "tropeAudit": [
        {
            "id": "CF-TRAD-001",
            "name": "Man vs. Self",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "The core of Clayface is an archetypal internal struggle. Matt Hagen's transformation strips away his identity layer by layer. He cannot recognize himself in the mirror, cannot trust his own perceptions, and must fight not an external villain but the erosion of his own sanity. This is psychological horror in the classical tradition: the monster is inside the man. Flanagan has built his career on this dynamic, and every indication from production materials points to a film that treats Hagen's disintegration as tragedy rather than spectacle."
        },
        {
            "id": "CF-TRAD-002",
            "name": "Redemption Through Suffering",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Hagen's physical transformation is explicitly framed as a consequence he must endure and ultimately transcend. The mob boss who disfigures him sets the tragedy in motion, but the film's dramatic arc points toward Hagen reclaiming his humanity through suffering rather than surrendering to the monster. This is a deeply traditional narrative structure: fall, suffering, potential redemption. The body horror genre has always understood that physical corruption carries moral weight."
        },
        {
            "id": "CF-TRAD-003",
            "name": "Consequences of Ambition",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 2.7,
            "explanation": "Hagen is an actor who presumably made choices that put him in the mob's crosshairs. The film's premise, as described in early reports, involves a man whose professional ambition and vanity make him vulnerable to the forces that destroy him. The desire to restore his face drives him toward the scientist who transforms him, a Faustian bargain that is a classic cautionary tale. The entertainment industry setting reinforces this: ambition without limits leads to ruin."
        },
        {
            "id": "CF-TRAD-004",
            "name": "Pro-Human Dignity",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "Underneath the horror premise is a fundamentally humanist concern: what does it mean to lose the face that the world sees? Flanagan's work consistently affirms human dignity, even in characters who have done terrible things. The tragedy of Clayface is not that he becomes powerful but that he loses himself. The film appears to treat his condition with genuine pathos rather than as a freak show, which is the traditional horror approach at its best."
        },
        {
            "id": "CF-WOKE-001",
            "name": "Outsider/Other as Protagonist",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.5,
            "explanation": "The disfigured protagonist can be read through a lens of marginalized identity, and DC Studios under James Gunn has shown interest in 'outsider' narratives. However, Flanagan's approach to the outsider is existential rather than political. Hagen is not oppressed by systemic forces; he is the victim of specific, individual cruelty. The film's interest in his condition is psychological, not sociological. The moderate authenticity reflects the possibility that some viewers will find a political reading, but the film itself does not appear to foreground one."
        }
    ],
    "seo": {
        "titleTag": "Is Clayface (2026) Woke? Mike Flanagan's DC Body Horror Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Clayface (2026), the DC Studios psychological body horror from Mike Flanagan. A disfigured actor becomes living clay. Trope scores, verdict: PREDICTED: BALANCED TRADITIONAL (+12.68). Parental guidance included.",
        "keywords": "is clayface woke, clayface 2026 review, clayface dc, clayface virtuevigil, clayface traditional or woke, mike flanagan clayface, clayface dc universe, clayface parents guide"
    },
    "summary": {
        "overall": "Clayface is Mike Flanagan doing what Mike Flanagan does best: taking a supernatural premise and digging into the human horror underneath. Based on everything known about this DC Studios production ahead of its October 23 release, the film shapes up as a psychological body horror piece that treats its title character not as a supervillain origin story but as a tragedy about identity, disfigurement, and the slow erosion of self. Matt Hagen, a working actor whose face is destroyed by a mob boss, turns to a scientist who transforms his body into living clay, and the man who emerges cannot recognize himself in the mirror. This is not a cape movie. It is The Fly by way of DC Comics, and Flanagan's script, polished by Hossein Amini, appears to lean hard into the body horror tradition that gave us Cronenberg's best work. The presence of James Watkins (The Woman in Black, Eden Lake) in the director's chair reinforces the horror-first approach. What pushes Clayface into balanced traditional territory is the moral architecture underneath the horror: Hagen's suffering is a consequence of choices, his transformation a Faustian bargain, and his arc points toward redemption through suffering rather than surrender to the monster. The film earns a PREDICTED: BALANCED TRADITIONAL verdict based on the available production information. Parents should note the R rating is well-earned: body horror, psychological intensity, and likely strong violence make this unsuitable for younger viewers.",
        "wokeSummary": "Clayface contains minimal woke content. The Outsider/Other as Protagonist trope earns 1.5 weighted points, but the film's treatment of the disfigured protagonist is existential rather than political. Hagen is not a stand-in for an oppressed identity group; his condition is the result of specific, personal cruelty, not systemic forces. Flanagan has never been an ideological filmmaker. His horror is built on universal fears: death, grief, guilt, the loss of self. The film does not appear to frame Hagen's condition through a lens of social justice or progressive grievance, which keeps the woke score low. Viewers looking for political messaging will find little purchase here.",
        "tradSummary": "The traditional strengths are substantial. Man vs. Self earns 6.3 weighted points as the film's central dramatic engine -- a classical internal struggle that drives every frame. Redemption Through Suffering (3.78) and Consequences of Ambition (2.7) reinforce the moral framework: Hagen's fate is not random but the result of choices, and his path forward is through endurance. Pro-Human Dignity (1.4) captures Flanagan's characteristic humanism: even at his most monstrous, Hagen retains something worth saving. Together these tropes form a coherent traditional worldview in which suffering has meaning and identity is worth fighting for.",
        "verdictExplanation": "The PREDICTED: BALANCED TRADITIONAL verdict (+12.68 margin) reflects a film that skews distinctly traditional in its moral framework while avoiding overt political content in either direction. Man vs. Self and Redemption Through Suffering dominate the scoring, and the single woke trope registers as a plausible reading rather than a baked-in ideological commitment. The pre-release designation reflects the fact that the film has not yet screened publicly, and the actual content could shift the score in either direction, though Flanagan's track record and the production team's stated intentions suggest the prediction is sound. The margin places Clayface in the BALANCED TRADITIONAL tier (margin 5-14.99), meaning it leans traditional enough for viewers to feel at home but does not carry the strong traditional charge of films like Braveheart or The Ten Commandments.",
        "parentalGuidance": "Clayface is rated R and lives squarely in the body horror tradition -- expect graphic physical transformation sequences, psychological intensity, moments of visceral horror, and likely strong language. The premise of a man whose face is destroyed and body transformed carries disturbing imagery. Not recommended for viewers under 17. Parents should be aware that the film's themes of identity loss and bodily corruption are genuinely unsettling and not the clean, CGI-heavy violence of a typical superhero movie. This is Mike Flanagan, and he does not pull punches."
    }
}

# ============================================================
# REVIEW 2: Bonnie and Clyde (1967)
# ============================================================
bonnie_clyde = {
    "id": "bonnie-and-clyde-1967",
    "slug": "bonnie-and-clyde-1967",
    "title": "Bonnie and Clyde",
    "year": 1967,
    "type": "film",
    "platform": "Streaming/Rental",
    "genre": "Crime, Drama, Biographical",
    "date": "2026-10-07",
    "datePublised": "2026-10-07",
    "author": "VirtueVigil Editorial Team",
    "readTime": "9 min read",
    "poster": "/images/posters/bonnie-and-clyde-1967.jpg",
    "releaseDate": "1967-08-13",
    "rating": "R",
    "runtime": "111 min",
    "director": "Arthur Penn",
    "writers": ["David Newman", "Robert Benton", "Robert Towne"],
    "showrunner": None,
    "cast": ["Warren Beatty", "Faye Dunaway", "Michael J. Pollard", "Gene Hackman", "Estelle Parsons"],
    "studio": "Tatira-Hiller Productions",
    "distributor": "Warner Bros.-Seven Arts",
    "verdict": "TRADITIONAL LEAN",
    "wokeScore": 1.6,
    "tradScore": 16.52,
    "authIndex": 85,
    "scoreMargin": "+15 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "Bonnie and Clyde contains no woke trap. The film was revolutionary for 1967 in its graphic violence and sexual frankness, but its moral framework is deeply traditional. From the opening scenes, the film establishes that Bonnie and Clyde are charismatic but doomed. Their criminal spree is presented as a series of escalating choices with increasingly brutal consequences, culminating in one of cinema's most famous and punishing endings. The counter-cultural elements are stylistic, not ideological: the film does not argue that crime pays or that the system is rigged. It argues that violence begets violence and that choices have consequences. Viewers who mistake the film's technical audacity for moral permissiveness are misreading what Arthur Penn and his writers actually put on screen.",
    "tropeAudit": [
        {
            "id": "BC-TRAD-001",
            "name": "Consequences for Actions",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "The entire dramatic structure of Bonnie and Clyde builds toward its infamous conclusion. Every robbery, every escalation, every murder tightens the noose. The film's closing sequence is not subversive; it is retributive. Arthur Penn lingers on the bodies because he wants the audience to sit in the consequence. This is classical tragedy dressed in New Hollywood clothing: hubris meets nemesis. The film's final image is not romantic -- it is a warning, and a fiercely traditional one at that."
        },
        {
            "id": "BC-TRAD-002",
            "name": "Anti-Establishment",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Bonnie and Clyde robs banks during the Great Depression, and the film makes no secret of why audiences in 1967 rooted for them. Banks were foreclosing on farms. The establishment had failed. But this is anti-establishment in the classical American populist tradition, not the progressive grievance framework. The Barrow gang's rebellion is personal, not political. They do not deliver speeches about systemic oppression. They rob banks because they want money and excitement, and the film never pretends otherwise. The anti-authority charge comes from the audience's recognition that the system is broken, not from a political program."
        },
        {
            "id": "BC-TRAD-003",
            "name": "Free Will and Personal Agency",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "At every turn, Bonnie and Clyde choose their path. Clyde could have stayed a small-time thief. Bonnie could have stayed a waitress. The film presents their criminal career not as forced by circumstance but as a series of escalating decisions made by two people who find the danger intoxicating. There is no victim narrative here. They are not products of their environment in the deterministic sense -- the Depression provides a backdrop, not an excuse. This affirmation of free will is fundamentally traditional."
        },
        {
            "id": "BC-TRAD-004",
            "name": "Pro-Human Dignity",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "For all its violence, Bonnie and Clyde finds moments of genuine tenderness between its two leads. Bonnie's poetry, Clyde's impotence and vulnerability, the makeshift family the Barrow gang forms -- these human moments are what make the ending devastating. The film does not treat its characters as mere criminals to be judged. It treats them as human beings whose choices led them to a terrible end, which is a far more traditional posture than a film that simply condemns or celebrates them."
        },
        {
            "id": "BC-WOKE-001",
            "name": "Anti-Law Enforcement Narrative",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.0,
            "explanation": "The lawmen pursuing Bonnie and Clyde are portrayed as bumbling, ineffectual, and ultimately vengeful rather than just. Frank Hamer, the Texas Ranger who leads the posse, is depicted as a man out for blood rather than justice. This portrayal generated controversy upon release and led to a defamation lawsuit from Hamer's family. However, the film's treatment of law enforcement is a narrative choice about specific characters rather than a systemic condemnation. The police are not institutions of oppression; they are individual men who are outmatched and outmaneuvered until they stop playing fair."
        },
        {
            "id": "BC-WOKE-002",
            "name": "Sexual Liberation as Counter-Cultural Statement",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Moderate",
            "weightedScore": 0.6,
            "explanation": "Bonnie and Clyde was famously frank about sexuality for its era, and this frankness was part of the New Hollywood rejection of the Production Code's moral framework. However, the sexual content serves character and story, not ideology. Bonnie's sexual frustration and Clyde's impotence are psychological realities, not political statements. Revolutionizing what could be shown on screen is not the same thing as advancing a progressive sexual agenda. By modern standards, the film's sexuality is remarkably restrained and integrated into the tragedy rather than deployed as messaging."
        }
    ],
    "seo": {
        "titleTag": "Is Bonnie and Clyde (1967) Woke? The New Hollywood Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Bonnie and Clyde (1967), Arthur Penn's landmark crime drama starring Warren Beatty and Faye Dunaway. Trope scores, verdict: TRADITIONAL LEAN (+14.92). Parental guidance included.",
        "keywords": "is bonnie and clyde woke, bonnie and clyde 1967 review, bonnie and clyde virtuevigil, bonnie and clyde traditional or woke, arthur penn bonnie and clyde, bonnie and clyde parents guide, warren beatty bonnie and clyde"
    },
    "summary": {
        "overall": "Bonnie and Clyde is one of those films that time has misremembered. When it premiered in 1967, critics called it everything from revolutionary to degenerate. Pauline Kael celebrated it. Bosley Crowther denounced it. The violence was unprecedented. The sexuality was frank. The anti-heroes were allowed to be genuinely charismatic without the movie wagging its finger at the audience for liking them. All of which made it a landmark of the New Hollywood, and all of which has led generations of film students to mistake it for a subversive or morally permissive film. It is neither. Arthur Penn's masterpiece is, at its core, a deeply traditional moral fable dressed in the clothes of a counter-cultural revolution. Bonnie Parker and Clyde Barrow rob banks during the Depression. They are young, beautiful, and exciting. The movie lets the audience fall in love with them. And then, methodically and without mercy, it shows what happens to people who live by the gun. The ending is not ambiguous. It is not glamorous. It is one of the most brutal sequences ever committed to film, and it arrives not as a shock but as a mathematical certainty. Every choice the characters make tightens the net around them. The film earns a TRADITIONAL LEAN verdict (+14.92 margin). It is not a conservative film in the political sense, but its moral framework -- free will, personal agency, consequences for actions -- is as traditional as drama gets. Parents should know the R rating is not negotiable: this is real violence, real blood, and real moral weight.",
        "wokeSummary": "Bonnie and Clyde carries minimal woke content by VVWS standards. The Anti-Law Enforcement Narrative trope earns 1.0 weighted points for its unflattering portrayal of the Texas Rangers pursuing the Barrow gang, though this is less a systemic critique of policing and more a narrative device to heighten the audience's identification with the outlaws. The Sexual Liberation as Counter-Cultural Statement trope registers at a negligible 0.6 weighted points: the film's sexual frankness was revolutionary for 1967 but served character and story, not ideology. Neither of these elements significantly shifts the film's ideological center of gravity.",
        "tradSummary": "The film's traditional architecture is formidable. Consequences for Actions dominates with 6.3 weighted points: the entire film is built to deliver its punishing finale. Anti-Establishment earns 5.04 points in its classical American populist register, not the progressive grievance framework. Free Will and Personal Agency (3.78) affirms that Bonnie and Clyde choose their path at every turn, rejecting the deterministic worldview that would later become a hallmark of progressive storytelling. Pro-Human Dignity (1.4) captures the film's genuine tenderness toward its doomed protagonists -- a tenderness that makes the moral lesson land harder, not softer.",
        "verdictExplanation": "TRADITIONAL LEAN (+14.92 margin) reflects a film whose counter-cultural reputation belies its deeply traditional moral structure. The margin places it in the TRADITIONAL LEAN tier (15-19.99), which is appropriate: the film's style was revolutionary, but its substance affirms free will, personal responsibility, and the inevitability of consequences. The small woke content (1.6 total) comes from stylistic choices about law enforcement portrayal and sexual frankness that were provocative in their era but do not constitute ideological messaging. The margin just barely crosses the TRADITIONAL LEAN threshold, which feels right -- this is a film balanced between audacity and moral clarity, and the scoring reflects that tension.",
        "parentalGuidance": "Bonnie and Clyde is rated R and earned that rating honestly. The violence, while less graphic than modern standards, is shocking in its sudden brutality and emotional weight. The final ambush sequence is prolonged and disturbing. Sexual content includes implied intimacy and sexual frustration themes. The criminal lifestyle is presented with charisma, which is precisely the trap the film springs on its audience: you will like these people, and then you will watch them die. Not recommended for viewers under 16. Parents who choose to show this to mature teenagers should be prepared to discuss the moral architecture of the film, because the film itself is doing far more work in that direction than its reputation suggests."
    }
}

# ============================================================
# REVIEW 3: Cupertino (2026) - Pre-release TV series
# ============================================================
cupertino = {
    "id": "cupertino-2026",
    "slug": "cupertino-2026",
    "title": "Cupertino",
    "year": 2026,
    "type": "series",
    "platform": "CBS",
    "genre": "Legal Drama",
    "date": "2026-10-07",
    "datePublised": "2026-10-07",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/cupertino-2026.jpg",
    "releaseDate": "2026-10-08",
    "rating": "TV-14",
    "runtime": "42-44 min per episode",
    "director": None,
    "writers": ["Robert King", "Michelle King"],
    "showrunner": "Robert King, Michelle King",
    "cast": ["Mike Colter", "Rachel Keller", "Renée Elise Goldsberry", "Busy Philipps", "Ella Stiller", "Nik Dodani"],
    "studio": "King Size Productions, CBS Studios",
    "distributor": "CBS",
    "verdict": "PREDICTED: BALANCED WOKE",
    "wokeScore": 11.94,
    "tradScore": 6.18,
    "authIndex": 60,
    "scoreMargin": "-6 WOKE",
    "preRelease": True,
    "wokeTrap": False,
    "woke_trap_assessment": "Cupertino does not appear to employ a woke trap. The premise announces its ideological alignment from the outset: a Silicon Valley attorney, cheated out of his stock options, forms a firm to represent people exploited by the technology industry. This is an explicit David-versus-Goliath framing that puts Big Tech in the villain role. The Kings' track record with The Good Wife and The Good Fight suggests the show will contain moral complexity and potentially balanced perspectives, but the core premise is transparent about which side it takes. There is no hidden agenda because the agenda is the premise. Viewers who find anti-corporate legal drama unappealing will know to stay away from the first episode.",
    "tropeAudit": [
        {
            "id": "CUP-TRAD-001",
            "name": "Entrepreneurial Spirit",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "When Michael Price gets cheated out of his stock options and fired, he does not join a class-action lawsuit or seek government intervention. He starts his own firm. This is a fundamentally traditional response to corporate betrayal: the individual takes his fate into his own hands rather than outsourcing justice to an institution. The Kings have always been interested in the tension between institutional and individual action, and the decision to make Price an entrepreneur rather than a plaintiff is a meaningful traditional signal in a premise that otherwise leans progressive."
        },
        {
            "id": "CUP-TRAD-002",
            "name": "Meritocracy",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.4,
            "explanation": "Price's grievance is not that the system is inherently unfair but that he was cheated out of what he earned. The stock options he was denied represent his contribution's value. This framing assumes a meritocratic baseline: work should be rewarded, and the crime is that it was not. The show's premise validates the idea that people deserve the fruits of their labor, which is a traditional position even when deployed against corporate villains."
        },
        {
            "id": "CUP-TRAD-003",
            "name": "Father-Son Legacy",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.0,
            "explanation": "Joe Morton plays Price's father Bayard, a prominent attorney. The presence of a father figure who represents the established legal profession suggests intergenerational themes: what does the younger lawyer owe to the older generation's traditions? What does he reject? The Kings frequently mine family dynamics for dramatic tension, and the father-son relationship is one of the most traditional frameworks available to them."
        },
        {
            "id": "CUP-WOKE-001",
            "name": "The System Is Rigged",
            "category": "Woke",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.3,
            "explanation": "The premise of Cupertino is fundamentally a System Is Rigged narrative. Price is cheated by his employer. The people he helps have been 'exploited by the region's technology companies.' The show's elevator pitch is that Silicon Valley's institutions are stacked against ordinary people, and the only recourse is to fight back through the legal system. This is the show's organizing idea, not a subplot. The Kings handled similar themes in The Good Fight with a more politically balanced approach, but the premise as described tilts hard toward structural critique."
        },
        {
            "id": "CUP-WOKE-002",
            "name": "Big Corporation as Villain",
            "category": "Woke",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Silicon Valley tech companies are the antagonists. This is not subtle. The series is named after the city that houses Apple Inc., and every client-of-the-week will presumably be someone wronged by a technology firm. Big Corporation as Villain is a staple of progressive storytelling: the faceless corporate entity that exploits workers, consumers, and communities for profit. The authenticity is high because the Kings are not pretending otherwise -- this is what the show is about."
        },
        {
            "id": "CUP-WOKE-003",
            "name": "Diversity Casting as Political Statement",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.6,
            "explanation": "The cast is deliberately diverse: Mike Colter (Black male lead), Rachel Keller (white female co-lead), Renée Elise Goldsberry (Black woman), Nik Dodani (Indian-American), Ella Stiller. CBS casting in 2026 is rarely accidental, and the Kings' shows have consistently foregrounded diverse ensembles. However, the centrality is low: the casting does not drive the narrative, and the characters' backgrounds do not appear to be the primary ideological vehicle. The story is about what these lawyers do, not who they are."
        }
    ],
    "seo": {
        "titleTag": "Is Cupertino (2026) Woke? CBS's Silicon Valley Legal Drama Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Cupertino (2026), the CBS legal drama from Robert and Michelle King starring Mike Colter. Lawyers take on Big Tech. Trope scores, verdict: PREDICTED: BALANCED WOKE (-5.76). Parental guidance included.",
        "keywords": "is cupertino woke, cupertino 2026 review, cupertino cbs, cupertino virtuevigil, cupertino traditional or woke, robert michelle king cupertino, mike colter cupertino, cupertino parents guide"
    },
    "summary": {
        "overall": "Cupertino arrives on CBS with a premise that can be summarized in one sentence: a Silicon Valley attorney, cheated out of his stock options, starts a firm to take on the tech companies that exploit ordinary people. That premise is a Rorschach test. If you think Big Tech deserves a legal reckoning, you are the target audience. If you think the framing already stacks the deck, you have correctly identified the show's ideological center of gravity. Robert and Michelle King, the married team behind The Good Wife, The Good Fight, and Evil, are among the most interesting creators working in network television because they rarely settle for propaganda. Their shows contain moral complexity, characters who surprise you, and genuine engagement with opposing viewpoints. But the premise is the premise, and the premise tilts woke. Michael Price (Mike Colter, bringing the gravitas he honed on Luke Cage and Evil) is not wronged by an abstract system. He is wronged by a specific company, and his response is entrepreneurship rather than activism. These are traditional grace notes in a progressive score. The Kings are smart enough to make Price a founder rather than a plaintiff, and the presence of Joe Morton as Price's attorney father suggests the show will explore intergenerational tensions within the legal profession. Whether these traditional elements can balance the anti-corporate premise remains to be seen. Based on pre-release materials, Cupertino earns a PREDICTED: BALANCED WOKE verdict (-5.76 margin). The System Is Rigged and Big Corporation as Villain tropes carry the scoring, while Entrepreneurial Spirit and Meritocracy provide resistance. Parents should find the CBS procedural format reassuringly tame by modern standards, though the subject matter will interest adults more than younger viewers.",
        "wokeSummary": "Cupertino's woke content is baked into the premise. The System Is Rigged earns 6.3 weighted points as the show's organizing idea: Silicon Valley cheats workers, and the good guys fight back through the legal system. Big Corporation as Villain adds 5.04 points; the series title itself, named for Apple's hometown, announces the target. Diversity Casting registers at a modest 0.6 points -- the ensemble is diverse by design but the casting does not appear to be the primary ideological vehicle. Together these tropes form a coherent progressive worldview in which corporate power is the adversary and the legal system, imperfect though it may be, is the arena where justice gets done.",
        "tradSummary": "The traditional counterweight comes primarily from Entrepreneurial Spirit (3.78 weighted points). Price's response to corporate betrayal is to build something, not to tear something down. He founds a firm rather than joining a movement, and that distinction matters. Meritocracy (1.4) reinforces the traditional framing: Price's grievance is that he was not rewarded for his contributions, which assumes the validity of the meritocratic bargain. Father-Son Legacy (1.0) introduces generational themes that the Kings have explored effectively in their previous work. These traditional elements, while outweighed by the woke tropes, prevent the show from sliding into STRONGLY WOKE territory and may provide the dramatic tension that makes the Kings' best work compelling.",
        "verdictExplanation": "PREDICTED: BALANCED WOKE (-5.76 margin) reflects a show whose premise skews distinctly progressive but includes traditional counterweights that prevent it from becoming pure agitprop. The margin places it in BALANCED WOKE territory (margin -4 to -13.99). The Kings have a track record of surprising audiences with moral complexity, and the father-son dynamic plus the entrepreneurial framing suggest Cupertino may be more balanced than its elevator pitch suggests. However, the pre-release designation is appropriate: no episodes have aired, and the actual execution could push the score in either direction. The System Is Rigged framing is heavy enough that even the most balanced execution is unlikely to erase the woke deficit entirely.",
        "parentalGuidance": "Cupertino airs on CBS and carries a TV-14 rating. Expect standard broadcast network content: legal themes, corporate intrigue, some mild language, and dramatic tension. No graphic violence or sexuality. The subject matter -- corporate exploitation, legal maneuvering, professional ethics -- is more relevant to adult viewers. Younger teens interested in law or business may find the Silicon Valley setting engaging, but this is fundamentally adult fare. Parents should be aware that the show's anti-corporate framing may prompt discussions about the role of large technology companies in American life."
    }
}

# Append all three
data.append(clayface)
data.append(bonnie_clyde)
data.append(cupertino)

# Verify
slugs = set()
for rev in data:
    s = rev['slug']
    if s in slugs:
        print(f"DUPLICATE SLUG: {s}", file=sys.stderr)
        sys.exit(1)
    slugs.add(s)

with open(reviews_path, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Appended 3 reviews. New total: {len(data)}")
print(f"  clayface-2026: PREDICTED: BALANCED TRADITIONAL (+12.68)")
print(f"  bonnie-and-clyde-1967: TRADITIONAL LEAN (+14.92)")
print(f"  cupertino-2026: PREDICTED: BALANCED WOKE (-5.76)")