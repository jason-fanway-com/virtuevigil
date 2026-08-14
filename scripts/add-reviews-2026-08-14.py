#!/usr/bin/env python3
"""Append 3 reviews to reviews.json for 2026-08-14."""
import json, sys, shutil, os
from datetime import date

REVIEWS_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'reviews.json')
TODAY = "2026-08-14"

reviews = [
{
    "id": "the-end-of-oak-street-2026",
    "slug": "the-end-of-oak-street-2026",
    "title": "The End of Oak Street",
    "year": 2026,
    "type": "film",
    "platform": "Theaters",
    "genre": "Sci-Fi / Survival / Thriller",
    "readTime": "8 min",
    "poster": "/images/posters/the-end-of-oak-street-2026.jpg",
    "releaseDate": "2026-08-14",
    "rating": "PG-13 (Sci-Fi Violence, Peril, Brief Language)",
    "runtime": "99 min",
    "director": "David Robert Mitchell",
    "writers": ["David Robert Mitchell"],
    "cast": [
        {"name": "Anne Hathaway", "role": "Denise Platt"},
        {"name": "Ewan McGregor", "role": "Greg Platt"},
        {"name": "Maisy Stella", "role": "Audrey Platt"},
        {"name": "Christian Convery", "role": "Brian Platt"},
        {"name": "Jordan Alexa Davis", "role": "Jeannette Christiansen"},
        {"name": "P. J. Byrne", "role": "Mel Jacobs"},
        {"name": "Emily Kuroda", "role": "Mrs. Valcourt"}
    ],
    "studio": "Bad Robot / Jackson Pictures",
    "distributor": "Warner Bros. Pictures",
    "verdict": "TRADITIONAL",
    "wokeScore": 2.35,
    "tradScore": 20.0,
    "scoreMargin": "+18 TRAD",
    "authIndex": 72,
    "preRelease": False,
    "wokeTrap": False,
    "date": TODAY,
    "datePublished": TODAY,
    "author": "VirtueVigil Editorial Team",
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "The End of Oak Street is not a woke trap. The film is a straightforward family survival story from its opening scene. The marriage-in-crisis setup is established in the first act, and the husband's sacrificial arc is visible from the midpoint onward. Nothing ideological is hidden past the halfway mark."
    },
    "seo": {
        "titleTag": "Is The End of Oak Street (2026) Woke? Anne Hathaway Sci-Fi Film Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of The End of Oak Street (2026). Anne Hathaway and Ewan McGregor star in this sci-fi survival thriller. Verdict: TRADITIONAL, +17 TRAD. Full trope audit covering family values, sacrifice, and marriage under fire.",
        "keywords": [
            "is the end of oak street woke",
            "the end of oak street 2026 review",
            "anne hathaway sci-fi film conservative review",
            "the end of oak street woke score",
            "the end of oak street parents guide",
            "the end of oak street virtuevigil",
            "is flowervale street woke",
            "the end of oak street traditional values",
            "david robert mitchell woke",
            "the end of oak street family movie review"
        ]
    },
    "summary": {
        "overview": "The End of Oak Street (2026), directed by David Robert Mitchell, follows the Platt family -- Denise (Anne Hathaway), Greg (Ewan McGregor), and their two children -- whose 1982 suburban neighborhood is abruptly transported millions of years into the past by a wormhole. Oak Street is now surrounded by prehistoric wilderness and, fatally, by dinosaurs. The family must navigate a crumbling marriage, a neighborhood in chaos, and a landscape that wants them dead to find their way home.",
        "overall": "The End of Oak Street is a tight, 99-minute family survival thriller that spends its runtime on exactly what the premise demands: parents trying to keep their children alive in an impossible situation. The film's ideological content is light, which is itself a decision worth noting in 2026. David Robert Mitchell does not use the prehistoric setting as a metaphor for climate change, the Platt family's crisis as a vehicle for gender politics, or the suburban setting as an indictment of middle-class America. He just tells a survival story. The marriage subplot is the film's emotional spine and its most traditionally resonant element. Denise is contemplating divorce when the wormhole hits. Greg has been hiding his job loss and working as a pizza delivery driver. The crisis forces them to be honest with each other, and Greg's arc ends in a sacrificial death protecting his family that the film treats with genuine weight, not as a cheap beat. The one ideological friction point is structural: Denise is the protagonist, the aspiring novelist who survives to write the book, and Greg is the man who dies so she can. The film does not frame this as a feminist statement -- Greg's death is heroic, not disposable -- but the configuration is worth noting. The dinosaur effects are sharp for an $80 million production. Michael Giacchino's score is one of his best in years. Parents should know the dinosaur attacks are PG-13 restrained but still involve on-screen deaths, including of children and the family dog faces real peril (he survives). For families with kids 12 and up, this is one of the safer theatrical bets of the summer.",
        "bestFor": "Families looking for a theatrical sci-fi adventure that does not lecture them, viewers who want a survival film with emotional stakes rather than political ones, Michael Giacchino score enthusiasts.",
        "skipIf": "You want hard sci-fi with rigorous time-travel mechanics. The wormhole is a plot device, not a physics problem. Also: the dog is in danger a lot. He lives, but sensitive viewers will squirm.",
        "wokeElements": "Denise is the protagonist and survivor who writes the book; Greg is the husband who dies. The film does not make a political point of this, but structurally the woman tells the story and the man is the sacrifice. A brief subplot about the husband's hidden job loss and shame gestures at a critique of male-provider pride, but it is resolved through honesty and reconciliation rather than condemnation.",
        "traditionalElements": "Greg's sacrificial death protecting his family is the film's moral climax and it is played without irony. The marriage that was ending is rebuilt through shared crisis. The family unit is the irreducible survival unit throughout. Children protect each other. The military and scientific authorities who appear in the epilogue are portrayed as competent and protective, not adversarial. The dog is a loyal family member who saves a child's life."
    },
    "parentalGuidance": {
        "rating": "PG-13",
        "contentWarnings": "Dinosaur attacks result in on-screen deaths, including of neighborhood children. The family dog is in repeated peril but survives. A father dies heroically protecting his family -- emotional but not gory. Brief language.",
        "ageRecommendation": "12+",
        "discussionTopics": [
            "What does Greg's choice to sacrifice himself say about fatherhood",
            "Why did the marriage crisis resolve under extreme pressure",
            "What does it mean that the family had to leave their world behind to save each other",
            "How does the film treat competence versus luck in survival"
        ]
    },
    "externalScores": {
        "imdb": "7.1/10",
        "rottenTomatoes": "86%",
        "metacritic": "68/100"
    },
    "creative_team": {
        "director": {
            "name": "David Robert Mitchell",
            "role": "Director / Writer",
            "note": "Director of It Follows and Under the Silver Lake. Known for genre films with emotional undercurrents. The End of Oak Street is his most commercial project to date and his first PG-13 film, trading his usual arthouse ambiguity for family-driven stakes."
        },
        "writer": {
            "name": "David Robert Mitchell",
            "role": "Screenwriter"
        },
        "lead_producer": {
            "name": "J. J. Abrams / Hannah Minghella / Matt Jackson",
            "role": "Producers"
        },
        "composer": {
            "name": "Michael Giacchino",
            "role": "Composer"
        }
    },
    "tropeAudit": [
        {
            "id": "WOKE-EOS-001",
            "name": "Female Protagonist as Author of the Story",
            "category": "Woke",
            "severity": 2,
            "authenticity": 1.0,
            "centrality": 0.5,
            "weightedScore": 1.0,
            "description": "Denise is the survivor who writes the book and tells the story; Greg is the man who dies to enable it. The film does not frame this as a political statement, but the structural choice of the wife as the narrative voice and the husband as the sacrifice is a recognizable contemporary pattern."
        },
        {
            "id": "WOKE-EOS-002",
            "name": "Male Provider Shame as Character Flaw",
            "category": "Woke",
            "severity": 2,
            "authenticity": 1.0,
            "centrality": 0.5,
            "weightedScore": 1.0,
            "description": "Greg's hidden job loss and his shame about delivering pizzas is presented as a failure of honesty that damages the marriage. The film resolves this through reconciliation rather than condemnation of Greg, but the framing of male-provider identity as something that needs to be surrendered is present."
        },
        {
            "id": "WOKE-EOS-003",
            "name": "Suburban Normalcy as Facade",
            "category": "Woke",
            "severity": 1,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 0.35,
            "description": "The opening act establishes the 1982 suburb as a place of hidden marital strife, quiet desperation, and secrets behind closed doors. The wormhole is almost a relief. This is a light touch but fits a familiar pattern of using genre to expose suburban emptiness."
        },
        {
            "id": "TRAD-EOS-001",
            "name": "The Father's Sacrificial Death",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 1.0,
            "centrality": 1.8,
            "weightedScore": 9.0,
            "description": "Greg dies protecting his family from an Allosaurus. The death is not subverted, mocked, or treated as disposable. It is the film's emotional and moral peak. The father gives his life so his wife and children can reach the wormhole. This is traditional heroism in its most direct form."
        },
        {
            "id": "TRAD-EOS-002",
            "name": "Marriage Rebuilt Through Shared Crisis",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.8,
            "description": "Denise and Greg's marriage was dying before the wormhole. The crisis forces honesty: Greg admits his shame, Denise admits her distance. They reconcile not because the film needs a happy ending but because extreme pressure clarifies what matters. The film argues that marriage can be saved when both people choose it."
        },
        {
            "id": "TRAD-EOS-003",
            "name": "Family as Irreducible Survival Unit",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 1.0,
            "centrality": 1.8,
            "weightedScore": 7.2,
            "description": "Every survival decision in the film is organized around the family. Parents search for children. Children protect each other. The dog is treated as family. No character survives alone. The film's thesis is that you survive because of your family, not despite them."
        },
        {
            "id": "TRAD-EOS-004",
            "name": "Competent, Non-Adversarial Authorities",
            "category": "Traditional",
            "severity": 2,
            "authenticity": 1.0,
            "centrality": 0.5,
            "weightedScore": 1.0,
            "description": "The epilogue shows the military and scientific community containing the prehistoric zone and studying it professionally. They are not villains, conspirators, or buffoons. The film treats institutional response as competent and protective, which is increasingly unusual for a genre film."
        }
    ]
},
{
    "id": "apollo-13-1995",
    "slug": "apollo-13-1995",
    "title": "Apollo 13",
    "year": 1995,
    "type": "film",
    "platform": "Netflix / Prime Video",
    "genre": "Drama / History / Thriller",
    "readTime": "9 min",
    "poster": "/images/posters/apollo-13-1995.jpg",
    "releaseDate": "1995-06-30",
    "rating": "PG (Mild Language, Peril, Emotional Intensity)",
    "runtime": "140 min",
    "director": "Ron Howard",
    "writers": ["William Broyles Jr.", "Al Reinert"],
    "cast": [
        {"name": "Tom Hanks", "role": "Jim Lovell"},
        {"name": "Kevin Bacon", "role": "Jack Swigert"},
        {"name": "Bill Paxton", "role": "Fred Haise"},
        {"name": "Ed Harris", "role": "Gene Kranz"},
        {"name": "Gary Sinise", "role": "Ken Mattingly"},
        {"name": "Kathleen Quinlan", "role": "Marilyn Lovell"}
    ],
    "studio": "Imagine Entertainment",
    "distributor": "Universal Pictures",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 0.35,
    "tradScore": 27.6,
    "scoreMargin": "+27 TRAD",
    "authIndex": 90,
    "preRelease": False,
    "wokeTrap": False,
    "date": TODAY,
    "datePublished": TODAY,
    "author": "VirtueVigil Editorial Team",
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Apollo 13 is not a woke trap. The film contains no hidden ideological content. It is a straightforward historical drama about American competence under pressure from its opening scene at Lovell's home to the final splashdown. What you see is what you get."
    },
    "seo": {
        "titleTag": "Is Apollo 13 (1995) Woke? Tom Hanks NASA Film Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of Apollo 13 (1995). Tom Hanks, Ed Harris, and Kevin Bacon star in Ron Howard's NASA drama. Verdict: STRONGLY TRADITIONAL, +27 TRAD. Full trope audit covering American ingenuity, teamwork, and marriage under pressure.",
        "keywords": [
            "is apollo 13 woke",
            "apollo 13 1995 review conservative",
            "apollo 13 tom hanks traditional values",
            "apollo 13 woke score",
            "apollo 13 parents guide",
            "apollo 13 virtuevigil",
            "ron howard apollo 13 conservative review",
            "best traditional movies about america",
            "apollo 13 failure is not an option",
            "apollo 13 family movie review"
        ]
    },
    "summary": {
        "overview": "Apollo 13 (1995), directed by Ron Howard, dramatizes the 1970 lunar mission that became a fight for survival after an oxygen tank exploded 200,000 miles from Earth. Jim Lovell (Tom Hanks), Jack Swigert (Kevin Bacon), and Fred Haise (Bill Paxton) are the three astronauts trapped in a crippled spacecraft. On the ground, Flight Director Gene Kranz (Ed Harris) leads a team of engineers at Mission Control who must invent solutions to impossible problems in real time, with three lives and the world watching.",
        "overall": "Apollo 13 is one of the most traditionally American films ever made, and it achieves this without a single speech about patriotism or a flag in the frame that wasn't there in 1970. Ron Howard understands that the most persuasive case for American greatness is Americans being great at something hard. The film is a procedural about competence: the astronauts trust Mission Control, Mission Control trusts the engineers, the engineers trust math, and math does not care about anyone's feelings. There is no villain in Apollo 13. The antagonist is physics, and physics is indifferent to identity, ideology, and intention. The only thing that works is getting the numbers right. This is a quietly radical position in an era that has elevated subjective experience over objective reality. Gene Kranz's line -- 'Failure is not an option' -- is not a motivational poster in context. It is a statement of professional obligation. These men will not let those men die because their job is to bring them home, and you do not fail at your job when lives depend on it. The film treats marriage with the same unsentimental respect it gives engineering. Marilyn Lovell (Kathleen Quinlan) is not a prop or a nag. She manages the home front with the same quiet competence her husband brings to the cockpit. When she loses her wedding ring down the shower drain before the launch, the film does not treat it as an omen. Jim finds it. That is the film's view of marriage: you lose things, you find them, you keep going. The one note of ideological interest is what the film omits. There are no diversity subplots, no critique of the space program's cost, no hand-wringing about American priorities. The film simply assumes that exploring space is worth doing and that the people who do it are worth admiring. That assumption was uncontroversial in 1995. In 2026, it registers as a political statement. Apollo 13 is rated PG and is suitable for nearly all ages. The peril is real and sustained but never gratuitous. This is a film you can watch with your children and then talk about what competence actually looks like.",
        "bestFor": "Families, anyone who wants to remember what American institutions looked like when they worked, viewers tired of films that apologize for excellence, parents who want to show their kids what problem-solving looks like.",
        "skipIf": "You want action set pieces. The explosions are mechanical failures, not combat. The tension is in whether a carbon dioxide filter will fit, not whether someone gets shot.",
        "wokeElements": "Effectively none. The mission control team includes women and people of color in historically accurate roles; the film does not tokenize or spotlight them, it simply depicts the team as it was. There is no critique of American institutions, no diversity messaging, and no ideological framing beyond 'smart people working together to save lives.'",
        "traditionalElements": "American institutional competence as heroic. Marriage as partnership under pressure. Objective reality as the only thing that matters in a crisis. The chain of command as a structure that saves lives, not oppresses them. Professional obligation as a moral category. Fathers who go to work and come home. Wives who hold the line. Engineers who do the math."
    },
    "parentalGuidance": {
        "rating": "PG",
        "contentWarnings": "Sustained peril and tension throughout. Brief mild language. A scene of an astronaut's wife experiencing fear about her husband's safety is emotionally intense but not graphic. No violence.",
        "ageRecommendation": "8+",
        "discussionTopics": [
            "What does 'failure is not an option' actually mean in practice",
            "Why did the chain of command work instead of breaking down",
            "How did Jim and Marilyn Lovell's marriage survive the crisis",
            "What does this film teach about competence versus credentialism"
        ]
    },
    "externalScores": {
        "imdb": "7.7/10",
        "rottenTomatoes": "96%",
        "metacritic": "78/100"
    },
    "creative_team": {
        "director": {
            "name": "Ron Howard",
            "role": "Director",
            "note": "Director of A Beautiful Mind, Cinderella Man, and Rush. Howard has spent his career making films about competence, and Apollo 13 is the purest expression of his central theme: ordinary people doing extraordinary things through discipline and teamwork."
        },
        "writer": {
            "name": "William Broyles Jr. / Al Reinert",
            "role": "Screenwriters"
        },
        "lead_producer": {
            "name": "Brian Grazer",
            "role": "Producer"
        },
        "composer": {
            "name": "James Horner",
            "role": "Composer"
        }
    },
    "tropeAudit": [
        {
            "id": "WOKE-A13-001",
            "name": "Historical Diversity Shown Without Commentary",
            "category": "Woke",
            "severity": 1,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 0.35,
            "description": "Mission Control includes women and people of color in historically accurate roles. The film does not comment on this or draw attention to it; it simply shows the historical team as it was. This registers as a trope only because contemporary films would make a point of it."
        },
        {
            "id": "TRAD-A13-001",
            "name": "American Institutional Competence as Heroic",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "NASA, as an American institution, is portrayed as a place where excellence is expected and delivered. The hierarchy works. The procedures work. The chain of command clarifies rather than obstructs. The film argues that American institutions can be worthy of the trust placed in them when staffed by people who take their obligations seriously."
        },
        {
            "id": "TRAD-A13-002",
            "name": "Competence and Teamwork Over Identity",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 1.0,
            "centrality": 1.8,
            "weightedScore": 7.2,
            "description": "No one in Apollo 13 cares who anyone else is. They care whether the math is right. The film is a sustained argument that objective reality exists, that it is indifferent to your feelings, and that the only way to survive it is to be good at what you do. This is the traditional worldview at its most operational."
        },
        {
            "id": "TRAD-A13-003",
            "name": "Marriage as Unspoken Partnership",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "Jim and Marilyn Lovell's marriage is not a subplot; it is the ground beneath the film. She manages the home, the children, the terror, and the press without needing to perform strength. He trusts her completely. The film treats marriage as a structure that holds when everything else breaks."
        },
        {
            "id": "TRAD-A13-004",
            "name": "Failure Is Not an Option Ethos",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 1.0,
            "centrality": 1.8,
            "weightedScore": 9.0,
            "description": "Gene Kranz's refusal to accept failure is not bravado. It is the organizing principle of Mission Control's response. The film treats this as a moral position: when lives are in your hands, failure is definitionally unacceptable. You find a way or you don't go home. The entire third act is a demonstration of this principle in practice."
        },
        {
            "id": "TRAD-A13-005",
            "name": "Respect for Institutions and Authority",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 1.0,
            "centrality": 1.0,
            "weightedScore": 3.0,
            "description": "NASA, the government, the military, the press -- all are treated as legitimate institutions staffed by people trying to do their jobs. There is no conspiracy, no cover-up, no institutional villainy. The film assumes that institutions exist to serve and that, in this case, they did."
        }
    ]
},
{
    "id": "we-were-soldiers-2002",
    "slug": "we-were-soldiers-2002",
    "title": "We Were Soldiers",
    "year": 2002,
    "type": "film",
    "platform": "Prime Video / Paramount+",
    "genre": "War / Action / History",
    "readTime": "9 min",
    "poster": "/images/posters/we-were-soldiers-2002.jpg",
    "releaseDate": "2002-03-01",
    "rating": "R (Graphic War Violence, Language)",
    "runtime": "138 min",
    "director": "Randall Wallace",
    "writers": ["Randall Wallace"],
    "cast": [
        {"name": "Mel Gibson", "role": "Lt. Col. Hal Moore"},
        {"name": "Madeleine Stowe", "role": "Julia Moore"},
        {"name": "Sam Elliott", "role": "Sgt. Maj. Basil Plumley"},
        {"name": "Greg Kinnear", "role": "Maj. Bruce Crandall"},
        {"name": "Barry Pepper", "role": "Joe Galloway"},
        {"name": "Chris Klein", "role": "2nd Lt. Jack Geoghegan"},
        {"name": "Keri Russell", "role": "Barbara Geoghegan"}
    ],
    "studio": "Icon Productions / Wheelhouse Entertainment",
    "distributor": "Paramount Pictures",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 3.92,
    "tradScore": 27.19,
    "scoreMargin": "+23 TRAD",
    "authIndex": 82,
    "preRelease": False,
    "wokeTrap": False,
    "date": TODAY,
    "datePublished": TODAY,
    "author": "VirtueVigil Editorial Team",
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "We Were Soldiers is not a woke trap. The film announces its perspective immediately: the opening French massacre sequence and Moore's address to his troops establish that this is a film about duty, sacrifice, and leadership. The anti-war notes are present from the first act, not hidden past the midpoint. The Vietnamese commander is introduced as a worthy adversary early, not as a late-stage moral reversal."
    },
    "seo": {
        "titleTag": "Is We Were Soldiers (2002) Woke? Mel Gibson Vietnam War Film Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil VVWS review of We Were Soldiers (2002). Mel Gibson stars as Lt. Col. Hal Moore. Verdict: STRONGLY TRADITIONAL, +24 TRAD. Full trope audit covering military leadership, sacrifice, faith, and the home front.",
        "keywords": [
            "is we were soldiers woke",
            "we were soldiers 2002 review conservative",
            "mel gibson vietnam war film traditional values",
            "we were soldiers woke score",
            "we were soldiers parents guide",
            "we were soldiers virtuevigil",
            "hal moore leadership review",
            "best traditional war movies",
            "we were soldiers faith and duty",
            "randall wallace conservative review"
        ]
    },
    "summary": {
        "overview": "We Were Soldiers (2002), written and directed by Randall Wallace, dramatizes the Battle of Ia Drang in November 1965, the first major engagement between the U.S. Army and the North Vietnamese Army. Lt. Col. Hal Moore (Mel Gibson) leads approximately 400 men of the 7th Cavalry into the Ia Drang Valley, where they discover they are opposed by a veteran NVA division of 4,000. The film follows the three-day battle from both the battlefield and the home front, where Moore's wife Julia (Madeleine Stowe) takes over the delivery of death notices to the wives of fallen soldiers.",
        "overall": "We Were Soldiers is the Vietnam War film that Hollywood would not make today. It honors the American soldiers who fought at Ia Drang without apologizing for them, while still showing the enemy as a competent military force led by a commander who is not a caricature. It is a film about leadership at every level: Hal Moore's promise to be the first man on the battlefield and the last man off, Sgt. Maj. Plumley's unshakeable presence, the wives who hold the home front together when the telegrams start arriving. The central tension of We Were Soldiers is not whether the war was justified. It is whether Hal Moore can keep his promise to bring his men home. That focus on duty over ideology is what makes the film distinct from almost every other Vietnam War picture. The film does not ask you to support the war. It asks you to respect the men who fought it. Randall Wallace, who wrote Braveheart, brings the same sensibility here: soldiers are not victims of history, they are agents of honor. Moore's leadership is the film's spine. He studies military history obsessively, prays before battle, refuses to leave his men, and weeps for them when they die. This is not toxic masculinity. It is traditional masculinity at its most complete: protective, accountable, reverent, and willing to break before it bends on principle. The home-front sequences are unusually strong for a war film. Julia Moore does not just wait. She organizes, she takes responsibility for the death notifications when the Army botches them with taxi drivers, and she leads the other wives through the worst days of their lives. The film treats military wives as partners in the mission, not accessories. The most ideologically interesting element is the portrayal of the Vietnamese commander, Nguyen Huu An. He is competent, strategic, and not a villain. His closing observation that the Americans will think this was their victory and that this will become an American war is historically accurate and not presented as a gotcha. The film allows the audience to hold two truths: the American soldiers fought with honor, and the war they were fighting was unwinnable on the terms it was fought. That is not woke. That is honest. We Were Soldiers is rated R for graphic combat violence. The battle sequences are intense and unflinching, including napalm strikes, close-quarters combat, and the deaths of named characters the film has made you care about. This is not a film for children. For older teenagers and adults, it is one of the most traditionally resonant war films ever made.",
        "bestFor": "Military families, viewers who want a war film that honors soldiers without glorifying war, anyone interested in leadership under extreme pressure, Mel Gibson fans who want his best non-Braveheart performance.",
        "skipIf": "Graphic combat violence is a dealbreaker. The film earns its R rating. Also: if you need a war film to take an explicit political position on the Vietnam War, this one is more interested in the men than the policy.",
        "wokeElements": "The Vietnamese commander is depicted as a competent, strategic leader rather than a villain. His closing line about the war becoming an American war is an anti-war note. The film acknowledges the futility of the larger conflict without condemning the soldiers who fought it. These elements are present from the first act and are historically accurate, not ideological insertions.",
        "traditionalElements": "Hal Moore's leadership philosophy: first in, last out, never leave a man behind. His Christian faith is presented without irony as a source of strength. Sgt. Maj. Plumley is an archetype of the warrior-NCO: lethal, loyal, and utterly dependable. The wives form their own chain of command at home. Joe Galloway, the civilian journalist, picks up a rifle when the perimeter is breached. The film argues that duty is a form of love."
    },
    "parentalGuidance": {
        "rating": "R",
        "contentWarnings": "Intense, sustained combat violence throughout. Soldiers are shot, burned by napalm, blown up, and killed in close-quarters fighting. Named characters die on screen in emotionally devastating ways. A friendly-fire incident kills American soldiers. The aftermath of battle shows significant blood and casualties. Brief strong language.",
        "ageRecommendation": "16+",
        "discussionTopics": [
            "What does it mean to be the first on the field and the last to leave",
            "Can a war be unwinnable and the men who fought it still honorable",
            "What role did faith play in Hal Moore's leadership",
            "How did the wives' response to tragedy compare to the soldiers' response to combat"
        ]
    },
    "externalScores": {
        "imdb": "7.2/10",
        "rottenTomatoes": "63%",
        "metacritic": "65/100"
    },
    "creative_team": {
        "director": {
            "name": "Randall Wallace",
            "role": "Director / Screenwriter",
            "note": "Screenwriter of Braveheart and director of The Man in the Iron Mask and Secretariat. Wallace specializes in stories about principled men facing overwhelming odds. We Were Soldiers is his most personal film, adapting the book by Hal Moore and Joseph Galloway with their cooperation."
        },
        "writer": {
            "name": "Randall Wallace",
            "role": "Screenwriter"
        },
        "lead_producer": {
            "name": "Bruce Davey / Stephen McEveety / Randall Wallace",
            "role": "Producers"
        },
        "composer": {
            "name": "Nick Glennie-Smith",
            "role": "Composer"
        }
    },
    "tropeAudit": [
        {
            "id": "WOKE-WWS-001",
            "name": "Vietnamese Commander as Sympathetic Adversary",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 1.4,
            "description": "Nguyen Huu An is portrayed as a competent, strategic commander, not a cartoon villain. The film shows him caring for his wounded and making sound tactical decisions. This is historically defensible but registers as a woke-adjacent choice in the context of war films, which traditionally dehumanize the enemy."
        },
        {
            "id": "WOKE-WWS-002",
            "name": "War's Futility Acknowledged",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 2.52,
            "description": "Huu An's closing observation that the Americans will think this was their victory and that this will become an American war is a statement about the unwinnability of the conflict. The film does not condemn the soldiers who fought, but it acknowledges that the larger war was a strategic failure. This is presented as historical truth, not ideological commentary."
        },
        {
            "id": "TRAD-WWS-001",
            "name": "First In, Last Out Leadership",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "Hal Moore's promise to be the first man on the battlefield and the last to leave is not a slogan. He keeps it. The film treats this as the definition of leadership: the commander does not ask his men to take risks he will not take himself. Moore refuses evacuation until every man, living and dead, is off the field."
        },
        {
            "id": "TRAD-WWS-002",
            "name": "Christian Faith in Combat",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 1.05,
            "description": "Moore prays before battle and his faith is woven into his leadership without apology. Plumley's stoic presence includes a quiet Christianity. The film treats religious faith as a normal part of a soldier's life, not as something to be explained away or pathologized."
        },
        {
            "id": "TRAD-WWS-003",
            "name": "Wives as the Home-Front Chain of Command",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.8,
            "description": "Julia Moore does not merely wait for news. When the Army starts using taxi drivers to deliver death telegrams, she takes over the notifications herself. She organizes the wives, absorbs their grief, and becomes the leader the home front needs. The film treats military spouses as essential to the mission."
        },
        {
            "id": "TRAD-WWS-004",
            "name": "Brotherhood in Arms",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 1.0,
            "centrality": 1.8,
            "weightedScore": 9.0,
            "description": "The relationships between the soldiers are the film's emotional engine. Men die for each other. The cut-off platoon holds its position through the night because Sgt. Savage refuses to let them break. Joe Galloway, a civilian journalist, picks up a rifle. The film argues that the bond between soldiers is sacred."
        },
        {
            "id": "TRAD-WWS-005",
            "name": "Honor Over Survival",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 5.04,
            "description": "Moore's refusal to leave his dead behind is not tactical; it is moral. He will not abandon the bodies of his men to the enemy because that would be a violation of the covenant between a commander and his soldiers. The film treats honor as a real thing with real costs."
        },
        {
            "id": "TRAD-WWS-006",
            "name": "A Civilian Who Becomes a Soldier",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 1.0,
            "centrality": 1.0,
            "weightedScore": 3.0,
            "description": "Joe Galloway, the UPI reporter, arrives to document the battle and ends up fighting in it. When the perimeter is breached, he picks up a rifle. The film does not frame this as a corruption of his journalistic neutrality. It frames it as a man doing what the moment demands."
        }
    ]
}
]

# Verify trope audit sums
for r in reviews:
    woke = round(sum(t['weightedScore'] for t in r['tropeAudit'] if 'WOKE' in str(t.get('category','')).upper()), 2)
    trad = round(sum(t['weightedScore'] for t in r['tropeAudit'] if 'WOKE' not in str(t.get('category','')).upper()), 2)
    margin = round(trad - woke)
    print(f"{r['slug']}: woke={woke} (reported:{r['wokeScore']}) trad={trad} (reported:{r['tradScore']}) margin={margin} (reported:{r['scoreMargin']})")
    assert abs(woke - r['wokeScore']) < 0.6, f"WOKE MISMATCH: {woke} vs {r['wokeScore']}"
    assert abs(trad - r['tradScore']) < 0.6, f"TRAD MISMATCH: {trad} vs {r['tradScore']}"

# Load existing reviews
with open(REVIEWS_PATH) as f:
    data = json.load(f)

# Check no slug collisions
existing = {r.get('slug') for r in data}
for r in reviews:
    assert r['slug'] not in existing, f"DUPLICATE SLUG: {r['slug']}"

# Append
data.extend(reviews)

# Backup
bak = REVIEWS_PATH.replace('.json', '.bak.json')
shutil.copy2(REVIEWS_PATH, bak)

# Write
with open(REVIEWS_PATH, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✓ Added {len(reviews)} reviews to reviews.json (backup at {bak})")
print(f"Total reviews: {len(data)}")