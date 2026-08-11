#!/usr/bin/env python3
"""Add 3 reviews for 2026-08-11: A Few Good Men (1992), Warrior (2011), The Equalizer (2014)"""
import json, subprocess, sys, os

REVIEWS_FILE = "src/data/reviews.json"

with open(REVIEWS_FILE) as f:
    all_reviews = json.load(f)

existing_slugs = {r["slug"] for r in all_reviews}

NEW_SLUGS = ["a-few-good-men-1992", "warrior-2011", "equalizer-2014"]
for s in NEW_SLUGS:
    if s in existing_slugs:
        print(f"ERROR: slug '{s}' already exists!")
        sys.exit(1)
print("All slugs clear. Building reviews...")

# ============================================================
# REVIEW 1: A Few Good Men (1992)
# ============================================================
review1 = {
    "id": "a-few-good-men-1992",
    "slug": "a-few-good-men-1992",
    "title": "A Few Good Men",
    "year": 1992,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Drama, Thriller, Courtroom",
    "date": "2026-08-11",
    "datePublished": "2026-08-11",
    "author": "VirtueVigil Editorial Team",
    "readTime": "9 min read",
    "poster": "/images/posters/a-few-good-men-1992.jpg",
    "releaseDate": "1992-12-11",
    "rating": "R",
    "runtime": "138 min",
    "director": "Rob Reiner",
    "writers": ["Aaron Sorkin"],
    "cast": [
        "Tom Cruise as Lt. Daniel Kaffee",
        "Jack Nicholson as Col. Nathan R. Jessup",
        "Demi Moore as Lt. Cmdr. JoAnne Galloway",
        "Kevin Bacon as Capt. Jack Ross",
        "Kiefer Sutherland as Lt. Jonathan Kendrick",
        "Kevin Pollak as Lt. Sam Weinberg",
        "J.T. Walsh as Lt. Col. Matthew Markinson",
        "James Marshall as PFC Louden Downey",
        "Wolfgang Bodison as Lance Cpl. Harold W. Dawson",
        "Cuba Gooding Jr. as Cpl. Carl Hammaker"
    ],
    "studio": "Castle Rock Entertainment",
    "distributor": "Columbia Pictures",
    "verdict": "TRADITIONAL",
    "wokeScore": 7.74,
    "tradScore": 21.14,
    "authIndex": 65,
    "scoreMargin": "+13 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "A Few Good Men is not a woke trap. The film's critique of military command culture is present from the first scene: a Marine is dead, his superiors ordered it, and the entire film is spent proving that. There is no bait-and-switch. The movie advertises itself honestly as a story about accountability in the military, and that is exactly what it delivers for all 138 minutes."
    },
    "externalScores": {
        "imdb": "7.7/10",
        "rottenTomatoes": "83%",
        "metacritic": "62/100"
    },
    "seoTitle": "Is A Few Good Men (1992) Woke? Tom Cruise Courtroom Classic Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil's full VVWS review of A Few Good Men (1992). Jack Nicholson, Tom Cruise, military honor, and the price of truth. Verdict: TRADITIONAL, +13 TRAD. Full trope audit.",
    "seoKeywords": "is a few good men woke, a few good men 1992 review, you cant handle the truth woke, a few good men traditional conservative, tom cruise military movie, jack nicholson col jessup, a few good men virtuevigil, a few good men parents guide",
    "creative_team": {
        "director": {
            "name": "Rob Reiner",
            "role": "Director",
            "note": "Reiner spent the late 1980s and early 1990s on one of the most consistent runs in Hollywood history: Stand By Me, The Princess Bride, When Harry Met Sally, Misery, and then this. He is a liberal filmmaker who chose Aaron Sorkin's most traditional material. The film's argument, that truth and accountability matter more than institutional comfort, is not a left or right argument. It is the kind of moral clarity that Reiner has always been best at putting on screen."
        },
        "writers": [
            {
                "name": "Aaron Sorkin",
                "role": "Screenwriter (adapted from his own Broadway play)"
            }
        ],
        "lead_producer": {
            "name": "David Brown",
            "role": "Producer"
        },
        "composer": {
            "name": "Marc Shaiman",
            "role": "Composer",
            "note": "Shaiman's score does what a courtroom drama score should: it stays out of the way until it needs to press. The music never tells you how to feel about the verdict. It waits until the verdict is rendered and then earns its emotional release."
        },
        "source_material": {
            "name": "Aaron Sorkin",
            "role": "Playwright",
            "note": "Sorkin wrote the play after his sister, a JAG lawyer, told him about a case at Guantanamo Bay involving a hazing incident. The play opened on Broadway in 1989 with Tom Hulce and Stephen Lang. Sorkin adapted it himself for the screen, sharpening the dialogue and expanding Jessup's role. The 'You can't handle the truth' speech is almost entirely Nicholson's delivery making Sorkin's construction sound like improvised genius."
        },
        "top_cast": [
            {
                "name": "Tom Cruise",
                "role": "Lt. Daniel Kaffee"
            },
            {
                "name": "Jack Nicholson",
                "role": "Col. Nathan R. Jessup"
            },
            {
                "name": "Demi Moore",
                "role": "Lt. Cmdr. JoAnne Galloway"
            },
            {
                "name": "Kevin Bacon",
                "role": "Capt. Jack Ross"
            },
            {
                "name": "Kiefer Sutherland",
                "role": "Lt. Jonathan Kendrick"
            },
            {
                "name": "Kevin Pollak",
                "role": "Lt. Sam Weinberg"
            },
            {
                "name": "Wolfgang Bodison",
                "role": "Lance Cpl. Harold W. Dawson"
            },
            {
                "name": "J.T. Walsh",
                "role": "Lt. Col. Matthew Markinson"
            }
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "R",
        "mpaaDescriptors": "Language",
        "recommendedAge": "14+",
        "contentWarnings": [
            "Strong language throughout, including multiple uses of the f-word and heavy military profanity",
            "A Marine is found dead at the film's start; cause of death (gagging on his own blood) is discussed in clinical detail during testimony",
            "Hazing violence is described in testimony but not shown graphically",
            "Intense courtroom confrontation; Jack Nicholson's final breakdown is genuinely frightening in its controlled rage",
            "Themes of cover-up, institutional corruption, and abuse of authority are central to the story",
            "A character's suicide is briefly referenced"
        ],
        "guidance": "The R rating is for language, not violence. The film contains almost no on-screen violence. What it does contain is a sustained adult argument about truth, institutional loyalty, and the price of moral courage. Teenagers who can follow a courtroom drama will find this film rewarding and its moral stakes clear. The scene where Nicholson's Jessup is finally broken on the stand is one of the great moments in American acting, and it is worth seeing with anyone old enough to understand what it means to be exposed for exactly what you are."
    },
    "summary": {
        "overall": "A Few Good Men is not about the military. It's about truth. That distinction matters, because Rob Reiner's 1992 courtroom drama has been misread for thirty years as a liberal takedown of military culture, when what it actually is is a conservative argument: that accountability is real, that rules exist for reasons, and that no one, not even a decorated colonel commanding a post in Cuba, gets to decide that the truth is too inconvenient to be told.\n\nThe setup is efficient. Two Marines, Lance Cpl. Harold Dawson and PFC Louden Downey, are charged with murdering a fellow Marine, Pfc. William Santiago, at Guantanamo Bay. They administered a 'Code Red,' an extrajudicial punishment hazing designed to discipline Santiago for going outside the chain of command. Santiago died. Dawson and Downey didn't mean to kill him. But Col. Nathan R. Jessup ordered the Code Red, and now the Marine Corps needs the death to look like Santiago's own fault.\n\nEnter Lt. Daniel Kaffee (Tom Cruise). He is a plea-deal machine. His father was a legendary attorney. Kaffee has spent his career avoiding the courtroom his father mastered, playing softball and collecting deal after deal without ever putting his back against anything difficult. His partner, Lt. Sam Weinberg (Kevin Pollak), loves him for it. His superior, Lt. Cmdr. JoAnne Galloway (Demi Moore), who has requested the case and pushed it onto Kaffee's desk, does not.\n\nGalloway is the film's conscience. She believes Dawson and Downey are telling the truth about the Code Red order and she believes it matters. Kaffee believes it might be true and it doesn't matter, because there's no proof. The film is the argument between them, with Dawson and Downey's lives as the stakes.\n\nThe prosecution is run by Capt. Jack Ross (Kevin Bacon), a friend of Kaffee's who is doing exactly what the institution needs him to do. Ross is not a villain. He is a man performing his function in a system that has decided the two Marines need to go to prison so that Col. Jessup doesn't. Ross knows the Code Red happened. He can't prove it, and he's smart enough not to look for proof he doesn't want.\n\nJessup, played by Jack Nicholson, is the film's architectural center. He arrives at the halfway point and commands every scene he's in. Nicholson plays Jessup not as a cartoonish bully but as a man who has spent decades genuinely believing that the safety of America rests on the willingness of men like him to do the things that civilian America cannot stomach. He is not wrong that his job is hard. He is catastrophically wrong about what that job entitles him to do.\n\nThe courtroom scenes build to what is probably the most famous confrontation in American legal drama: Kaffee, having spent the entire film avoiding the thing he knows he has to do, finally orders the truth into existence. 'Did you order the Code Red?' Jessup breaks. Not because Kaffee is smarter than him, but because Jessup cannot stand to be questioned by a man he has already decided is his inferior. He cannot resist the invitation to explain to the court why they cannot handle the truth. And in explaining it, he proves it.\n\nThe verdict is guilty, which is the right verdict. But Aaron Sorkin is not done. The film's moral climax is not Jessup's arrest. It's Dawson's response to Kaffee afterward. Dawson and Downey are discharged from the Marines, and Kaffee tells Dawson he should be proud of himself. Dawson answers: 'We were supposed to fight for people who couldn't fight for themselves. He couldn't fight for himself. I was the one who was supposed to fight for him.' He failed Santiago. He does not need a piece of paper to tell him what that means.\n\nThat line is the whole film. Not the speech about the wall. Not the courtroom theater. Dawson standing in a corridor, accepting that honor is a real thing, that it obligates you, and that he failed its demands. The film is a story about what happens when the institutions designed to enforce honor fail, and what it takes from the men inside them to put it right.",
        "wokeAnalysis": "The woke content in A Few Good Men concentrates in three areas, none of them particularly aggressive by modern standards.\n\nFirst, the film's central villain is not an individual aberration but a systemic one. Jessup is not a bad apple. He is what the institution produced when left unchecked. The film argues that military command culture, when insulated from accountability, will protect itself at the expense of the people it exists to serve. This is a critique, not a celebration. It scores as a woke element because the institution is the antagonist, not just the man.\n\nSecond, JoAnne Galloway is the film's conscience in a role that requires her to push the male protagonist into doing his job. The 1992 version of this feels more organic than it would today: Moore plays Galloway as genuinely driven by the case, not by any interest in proving a point about women in the military. But the structure, woman as moral conscience, man as reluctant hero who needs to be awakened, is a woke template that has since been used so frequently it's become a cliche.\n\nThird, the film resolves by having Kaffee reject his superiors' wishes and pursue the full court martial over the institution's objection. Individual moral judgment wins over institutional authority. This is the film's most clearly libertarian element: when the system protects itself, you go around the system.\n\nNone of these elements feel ideologically inserted. They are all organic to a courtroom drama about institutional cover-up. The woke score is real but modest.",
        "tradAnalysis": "The traditional content in A Few Good Men is much heavier than its woke elements, and it operates at a deeper level.\n\nThe film's core argument is that justice is real and must be pursued even when it's costly. Kaffee has every incentive to take the plea deal. It would protect his career, spare everyone the risk of a court martial, and probably keep Dawson and Downey out of prison. He doesn't take it because Galloway has forced him to look at the truth, and once he's looked at it, he cannot unsee it. This is the oldest conservative argument: some things are right and wrong, and the difference matters more than personal convenience.\n\nThe honor theme is the film's finest traditional element. Not Jessup's version of honor, which is loyalty to the institution over loyalty to truth. Dawson's version: the obligation to protect those who cannot protect themselves. Santiago could not fight for himself. Dawson had the power and the duty to do it for him. He followed orders instead. The discharge from the Marines is his punishment not for what the court found but for what he knows he failed to be. The film treats this with complete seriousness, without irony or condescension. Honor exists. It makes demands. Failing it has consequences.\n\nCourage over comfort is Kaffee's arc. His father was a famous lawyer. Kaffee has spent his career in his father's shadow, avoiding the thing he knows he should do. The film is a classic story about a man finding the spine to stop hiding. Tom Cruise plays this with less of his characteristic charisma than usual, which is exactly right: Kaffee is not supposed to be effortlessly competent. He's supposed to be someone learning, badly, under pressure, to do the right thing.\n\nRule of law is the film's institutional argument. The military exists to serve something beyond itself. When Jessup decides that his judgment supersedes the law, he has committed the same crime he accused Santiago of: going outside the chain of command. The law is the chain of command. Jessup's contempt for it is his downfall.\n\nThe final scene, Dawson and Downey standing in the corridor, is the film's purest traditional moment. No one rewards them. No one tells them they're heroes. The system discharged them. They are holding themselves accountable to a standard higher than what the discharge says about them. That is character. That is what the film has been about from the start."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-AFG-001",
            "name": "Justice and Rule of Law",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "The film's entire structure is a legal proceeding in service of truth. Kaffee doesn't pursue the court martial because he hates the military or because Galloway pressures him. He pursues it because he has looked at the evidence and he knows what happened. The law is the only legitimate mechanism for making Jessup answer. The film believes this completely."
        },
        {
            "id": "TRADITIONAL-AFG-002",
            "name": "Courage Over Comfort",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 5.04,
            "description": "Daniel Kaffee's arc is a textbook traditional hero's journey: a man who has spent his career choosing the easy path finally chooses the hard one. The easy path is a plea deal. The hard path is a court martial against a decorated Marine colonel with no documentary evidence. Kaffee takes the hard path. The film presents this choice as the only morally acceptable one."
        },
        {
            "id": "TRADITIONAL-AFG-003",
            "name": "Honor and Personal Integrity",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.8,
            "description": "Dawson's final lines are the film's moral summit. He and Downey were dishonorably discharged. They were not convicted of murder. They will walk free. Dawson is still devastated, because he knows he failed his own code. 'We were supposed to fight for people who couldn't fight for themselves.' The paper verdict is not the real verdict. Honor is a standard that exists independent of courts and commanding officers."
        },
        {
            "id": "TRADITIONAL-AFG-004",
            "name": "Military Service and Sacrifice",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "The film respects the Marines even while indicting their command culture. Dawson and Downey are not villains. They are men who believed in their orders and followed them without flinching. The film asks what that loyalty means when the orders are wrong, but it never condescends to the Marines who gave everything to a code that failed them."
        },
        {
            "id": "TRADITIONAL-AFG-005",
            "name": "Objective Morality",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "The Code Red killed Santiago. Jessup ordered it. This is wrong. The film never wavers on that basic moral claim, never suggests that Jessup's reasoning about national security justifies what happened. Wrong is wrong. The verdict of the tribunal, and the more important verdict of Dawson's own conscience, confirm the same moral truth."
        },
        {
            "id": "TRADITIONAL-AFG-006",
            "name": "Truth Over Expedience",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.8,
            "description": "Kaffee has every institutional incentive to take the deal and bury the truth. The deal would spare Dawson and Downey prison. It would spare the Marine Corps embarrassment. It would spare Kaffee a risky trial. He refuses because the truth of what happened to Santiago demands to be told. The film treats truth-telling as a moral obligation, not a tactical choice."
        },
        {
            "id": "WOKE-AFG-001",
            "name": "Military Institution as Corrupt and Truth-Suppressing",
            "category": "Woke",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 5.04,
            "description": "The villain in A Few Good Men is not just Jessup. It's the system that produced and protected him. Kendrick followed Jessup's orders because the culture demanded it. Markinson knew the truth and buried it rather than testify. The JAG command wanted a plea deal that would protect the Corps. The institution is portrayed as self-protective to the point of covering for a man who ordered a murder."
        },
        {
            "id": "WOKE-AFG-002",
            "name": "Female Officer as Moral Conscience",
            "category": "Woke",
            "severity": 2,
            "authenticity": 1.0,
            "centrality": 1.0,
            "weightedScore": 2.0,
            "description": "JoAnne Galloway is the person who sees the truth and won't let it go. She requests the case, she pushes Kaffee to fight rather than deal, and she is ultimately right about everything. Kaffee grows into the lawyer Galloway always knew he could be. The structure places female moral clarity above male institutional comfort, a woke template that Sorkin uses without apparent irony."
        },
        {
            "id": "WOKE-AFG-003",
            "name": "Individual Moral Judgment Over Institutional Authority",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 0.7,
            "description": "The resolution requires Kaffee to override his superiors, reject the plea deal they wanted, and pursue a court martial against the Corps' preferred outcome. The film endorses this: individual conscience wins over institutional loyalty. It's a small element compared to the overall message about rule of law, but it cuts against conservative deference to legitimate authority."
        }
    ],
    "seo": {
        "titleTag": "Is A Few Good Men (1992) Woke? Tom Cruise Courtroom Classic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of A Few Good Men (1992). Jack Nicholson, Tom Cruise, military honor, and the price of truth. Verdict: TRADITIONAL, +13 TRAD. Full trope audit.",
        "keywords": [
            "is a few good men woke",
            "a few good men 1992 review",
            "you cant handle the truth woke",
            "a few good men traditional conservative",
            "tom cruise military movie",
            "jack nicholson col jessup",
            "a few good men virtuevigil",
            "a few good men parents guide",
            "rob reiner 1992 film review",
            "a few good men woke score"
        ]
    }
}

# ============================================================
# REVIEW 2: Warrior (2011)
# ============================================================
review2 = {
    "id": "warrior-2011",
    "slug": "warrior-2011",
    "title": "Warrior",
    "year": 2011,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Drama, Sports, Action",
    "date": "2026-08-11",
    "datePublished": "2026-08-11",
    "author": "VirtueVigil Editorial Team",
    "readTime": "10 min read",
    "poster": "/images/posters/warrior-2011.jpg",
    "releaseDate": "2011-09-09",
    "rating": "PG-13",
    "runtime": "140 min",
    "director": "Gavin O'Connor",
    "writers": ["Gavin O'Connor", "Anthony Tambakis", "Cliff Dorfman"],
    "cast": [
        "Tom Hardy as Tommy Conlon",
        "Joel Edgerton as Brendan Conlon",
        "Nick Nolte as Paddy Conlon",
        "Jennifer Morrison as Tess Conlon",
        "Frank Grillo as Frank Campana",
        "Kevin Dunn as Dan Taylor",
        "Noah Emmerich as Mark",
        "Bryan Callen as Bas Rutten"
    ],
    "studio": "Lionsgate",
    "distributor": "Lionsgate",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 0.7,
    "tradScore": 30.94,
    "authIndex": 80,
    "scoreMargin": "+30 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "Warrior is not a woke trap. The film's one arguably woke element, sympathy for a Marine who deserted, is present from the moment Tommy's backstory is established. Nothing is hidden. The film is a family reconciliation story and a combat sports film in equal measure, and it advertises both honestly from the first frame."
    },
    "externalScores": {
        "imdb": "8.1/10",
        "rottenTomatoes": "83%",
        "metacritic": "71/100"
    },
    "seoTitle": "Is Warrior (2011) Woke? Tom Hardy and Joel Edgerton MMA Drama Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil's full VVWS review of Warrior (2011). Tom Hardy, Joel Edgerton, Nick Nolte. Family, brotherhood, and redemption. Verdict: STRONGLY TRADITIONAL, +30 TRAD. Full trope audit.",
    "seoKeywords": "is warrior 2011 woke, warrior 2011 review, tom hardy joel edgerton warrior, warrior mma movie traditional, warrior 2011 family movie, is warrior traditional conservative, warrior 2011 virtuevigil, warrior 2011 parents guide",
    "creative_team": {
        "director": {
            "name": "Gavin O'Connor",
            "role": "Director / Co-Writer",
            "note": "O'Connor's career is built on stories about men in conflict with each other and with themselves. Tumbleweeds (1999), Pride and Glory (2008), and this film form an informal trilogy about damaged families and the things they cannot say to each other. Warrior is his best work: a film that earns its emotional payoff through two hours of meticulous character work. He understood that the fights only matter if the family rupture underneath them matters first."
        },
        "writers": [
            {
                "name": "Gavin O'Connor",
                "role": "Story, Screenplay"
            },
            {
                "name": "Anthony Tambakis",
                "role": "Screenplay"
            },
            {
                "name": "Cliff Dorfman",
                "role": "Screenplay"
            }
        ],
        "lead_producer": {
            "name": "Greg O'Connor",
            "role": "Producer"
        },
        "composer": {
            "name": "Mark Isham",
            "role": "Composer",
            "note": "Isham's score is largely atmospheric until it isn't. The final fight sequence, scored against the Icelandic band Asgeir's spare acoustic arrangements, is one of the most effective deployments of non-original music in a sports film. The Ennio Morricone piece used during the climactic moment arrives like a truck. O'Connor timed it perfectly."
        },
        "top_cast": [
            {
                "name": "Tom Hardy",
                "role": "Tommy Conlon"
            },
            {
                "name": "Joel Edgerton",
                "role": "Brendan Conlon"
            },
            {
                "name": "Nick Nolte",
                "role": "Paddy Conlon"
            },
            {
                "name": "Jennifer Morrison",
                "role": "Tess Conlon"
            },
            {
                "name": "Frank Grillo",
                "role": "Frank Campana"
            },
            {
                "name": "Kevin Dunn",
                "role": "Dan Taylor"
            }
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "PG-13",
        "mpaaDescriptors": "Sequences of intense action and combat violence, some language, brief drug content",
        "recommendedAge": "13+",
        "contentWarnings": [
            "Sustained MMA combat with realistic portrayals of strikes, chokes, and joint manipulation; competitors lose consciousness, bleed, and suffer visible pain",
            "A father's alcoholism is central to the story; depicted with honesty about its destructive effects on family",
            "A character briefly relapses into alcohol use; shown without glamorization",
            "Brief prescription drug misuse",
            "A character has clearly experienced severe trauma and PTSD from military combat; depicted sympathetically but with intensity",
            "Moderate language throughout; brief use of stronger profanity",
            "Themes of family abandonment and the lasting damage it does to children who become adults"
        ],
        "guidance": "The PG-13 rating fits the film, though parents should know the MMA sequences are genuinely intense. The fights are choreographed to feel real, which means they look like people actually trying to hurt each other. That said, there is almost no blood and no grotesque injury. The harder content is emotional: a father trying to earn back sons who have every reason to refuse him, and two brothers who have been shaped by the same damage in completely opposite directions. Teenagers who can handle the emotional weight will find this one of the more honest films about what forgiveness actually costs. It does not pretend forgiveness is easy. It shows the work."
    },
    "summary": {
        "overall": "Warrior (2011) is the best sports film of the decade and it isn't close. Gavin O'Connor's MMA drama about two estranged brothers competing in the same tournament is built on the oldest dramatic engine there is: a broken family trying to find its way back to itself. The fights are real and brutal, but they're not why the film works. The film works because by the time the brothers face each other in the cage, you are not watching a sporting event. You are watching thirty years of grief and love and abandonment collapse into a single moment.\n\nThe setup takes its time. Tommy Conlon (Tom Hardy) shows up drunk on his father Paddy's doorstep in Pittsburgh at two in the morning after years of no contact. Paddy (Nick Nolte) answers the door, sober, having been sober for a thousand days. Tommy is not impressed. Paddy was a brutal alcoholic who let his wife take the boys and leave him. He has since found God and AA and sobriety, and Tommy does not care about any of it. What Tommy wants is a trainer. Paddy trained both boys when they were young. Tommy still needs him for that and only that.\n\nMeanwhile, across Pennsylvania, Brendan Conlon (Joel Edgerton) is a high school physics teacher with a wife, two daughters, and a house whose mortgage is ninety days delinquent. He used to fight professionally. He quit to have a family. Now he's fighting again, small venues, low pay, because the bank is serious and the family needs the money. His school finds out and suspends him. He keeps fighting anyway, because what choice does he have?\n\nThe film cuts between these two stories with precision, establishing the characters separately before the tournament draws them into the same bracket. Tommy entered the tournament because there's a two million dollar prize and his dead comrades' families need it. He has a reason to win that has nothing to do with himself. Brendan has a reason to win that has everything to do with himself: his family, his house, his role as the man who provides.\n\nHardy's Tommy is one of the great physical performances of his generation. He barely speaks. He radiates controlled fury the way a furnace radiates heat. He destroys opponents in seconds, without hesitation, without celebration. He eats alone. He listens to Beethoven in his hotel room at night. He is a man so thoroughly armored that the only time the armor cracks is when Paddy slips and lets on that he still knows every move Tommy ever learned from him. That is when the grief shows: Tommy does not want to be someone his father still knows.\n\nEdgerton's Brendan is the film's heart. He is not the better fighter. He's a journeyman who wins by surviving. His game plan in every fight is to absorb punishment until his opponent makes a mistake, then find the submission hold. He is a man who knows how to endure. This is not accidental. He and Tommy survived the same childhood, and Brendan's method, absorb and endure and wait for the opening, is how he survived it too. He stayed with Tess when Tommy left with their mother. Staying was Brendan's version of fighting.\n\nNick Nolte received an Oscar nomination for Paddy, and he earned it. Paddy is the film's most painful presence. He is a man who destroyed his family and knows it, who has rebuilt himself into something better and has no illusions about whether the rebuilding earns him anything back. He takes the job training Tommy because it's what Tommy asked for, and he does it with something like reverence: grateful for the proximity, not expecting more than that. In one scene, drunk again after a brutal evening with Tommy's contempt, he listens to Moby Dick on a Walkman with tears running down his face. It is not a scene about alcoholism. It is a scene about a man who has read the same book so many times because it's the one thing that tells him the truth about what he is.\n\nThe tournament sequences are spectacular. O'Connor shot them with three cameras and real MMA fighters as opponents, and the coverage makes each fight feel genuinely dangerous. Tommy moves through his bracket like a force of nature. Brendan scrapes through by luck and grit and the submission game that his trainer Frank Campana (Frank Grillo, excellent) drilled into him.\n\nThey meet in the final. The fight is extraordinary not for what happens physically but for what it means. Tommy is winning. He has always been physically superior. And then Brendan catches him in a shoulder lock and the choice becomes clear: Tommy can let the joint break or he can tap out. He is too stubborn to tap. He fights on with a destroyed shoulder. His brother is destroying him. And then, in the moment that has been coming for 140 minutes, Brendan gets his arm around Tommy's neck and locks in the choke.\n\nTommy could tap out and still hate his brother. He could lose on a technical stoppage. Instead, in the moment before unconsciousness, he taps Brendan's arm. It is the first voluntary surrender of his adult life. And when Brendan pulls him to his feet and holds him in the cage and Tommy's arm goes around his brother's neck, it is not a victory celebration. It is the two of them finally in the same place at the same time, choosing each other.\n\nThe film earns this completely. Every scene before it has been in service of this moment: not a sports climax but a family resolution, accomplished in a cage in Atlantic City with two men who grew up in the same house and forgot how to be brothers.",
        "wokeAnalysis": "Warrior has almost nothing that registers on the woke scale. The one genuine element is the film's treatment of Tommy Conlon's military desertion. Tommy is technically a deserter: he went AWOL from the Marines. The film reveals, late in the story, that his desertion was an act of heroism. He commandeered a vehicle and evacuated wounded Marines under fire and without authorization. He saved lives. Then he ran. The film presents this as understandable: a traumatized man who did something extraordinary and then could not face what came after. The Marine Corps would disagree with the film's sympathetic framing, and that framing is a real woke element. Desertion is desertion, regardless of what preceded it. The film asks you to forgive Tommy for it, and most audiences do.\n\nThat's genuinely it. There is no diversity agenda, no ideology imposed on the story, no lecture inserted into the drama. The film is about fathers, sons, brothers, and the specific weight of grief that comes from a family that tore itself apart and cannot quite put itself back together.",
        "tradAnalysis": "Warrior is one of the most thoroughly traditional films made in the past twenty years, and what makes it remarkable is how little it feels like it's trying to be. The traditional content is not announced. It's just the shape of the story.\n\nBrotherhood and family reconciliation are the film's thesis. The tournament is the plot. The brothers getting back to each other is what the film is about. O'Connor structures the story so that every fight sequence moves the characters toward or away from each other emotionally, not just physically. By the time Tommy and Brendan meet in the cage, the fight has already been decided in the corridor scenes and the hotel-room scenes and the moments of silence between men who have too much to say.\n\nForgiveness is the film's hardest theme. Paddy has done the work. He is sober. He has found God. He has apologized repeatedly. Neither son is ready to forgive him. The film does not tell them they are wrong. It shows what unforgiveness costs: Tommy is consumed by rage, Paddy is consumed by grief, and Brendan is the only one who finds his way back to something like peace. The film suggests, carefully, that forgiveness is possible without requiring the audience to believe it has to happen. Brendan's grace and Tommy's hardness are both presented as reasonable responses to the same damage.\n\nThe self-sacrificing provider is Brendan's entire arc. He does not fight for glory or identity. He fights because his daughters need a home and he is the one who has to provide it. His wife Tess (Jennifer Morrison) is a full partner in this: she hates the fighting, she fears what it will cost him, and she comes to watch anyway when she understands that this is what her husband has chosen to do for the family. Their marriage is a working partnership under pressure, and it holds.\n\nMilitary sacrifice runs through Tommy's character like a current. His capacity for violence is the product of his training and his service. He does not use it for himself. He wins fights in seconds and gives the prize money away. He entered the tournament because he watched his friends die and their families need the money. His entire story is a man who gave everything to something larger than himself and cannot figure out how to live without that mission.\n\nMasculine virtue through discipline is everywhere. Both brothers are men who have shaped themselves through physical training. Tommy's preparation is ascetic, solitary, almost punishing. Brendan's is methodical, professional, family-friendly: he trains when the kids are in school. Both men define themselves by what they can endure. The film presents this as admirable, as it should be.\n\nThe honor of the fallen is Tommy's deepest wound. His friends are dead. Their families are struggling. He is still alive and he cannot reconcile that. The tournament money is the one way he has found to make the surviving mean something. When the film finally reveals why he ran, it becomes clear that Tommy has been punishing himself for being the one who got away. His violence in the cage is not aggression. It's penance."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-WAR-001",
            "name": "Brotherhood and Family Reconciliation",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "The entire film builds toward two estranged brothers choosing each other. Not just winning or losing the fight, but finding each other again. The final cage sequence is the most emotionally devastating family reunion in sports cinema. Every scene before it has been building to the moment Tommy taps his brother's arm and Brendan lifts him up."
        },
        {
            "id": "TRADITIONAL-WAR-002",
            "name": "Redemption and Forgiveness",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "Paddy Conlon is a recovered alcoholic trying to earn back his sons. The film asks the hardest question about forgiveness: how much do you owe someone who has genuinely changed after doing genuine damage? The film does not answer it cleanly. Brendan finds a way back. Tommy cannot. Both responses are presented as human."
        },
        {
            "id": "TRADITIONAL-WAR-003",
            "name": "The Self-Sacrificing Provider",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "Brendan Conlon is a husband and a father and a man with a mortgage 90 days past due. He fights because his family needs the money and he is the only one who can provide it. He risks his career, his physical health, and his marriage to do it. The film treats this as heroism, because it is."
        },
        {
            "id": "TRADITIONAL-WAR-004",
            "name": "Military Service and Sacrifice",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 5.04,
            "description": "Tommy Conlon's combat skill is entirely the product of his Marine service. The film treats this with respect: his violence is not pathological, it is trained, disciplined, and in service of something larger than himself. Even his desertion was in service of others. The film honors his service while acknowledging what it cost him."
        },
        {
            "id": "TRADITIONAL-WAR-005",
            "name": "Masculine Virtue Through Discipline",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.8,
            "description": "Both brothers are men who have shaped themselves through rigorous physical preparation. Tommy's training is monastic, almost self-punishing. Brendan's is methodical and professional. The film presents physical discipline as a form of moral discipline: men who take the time to prepare themselves to endure are men who can endure what life actually brings."
        },
        {
            "id": "TRADITIONAL-WAR-006",
            "name": "Marriage as a Rock",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "Brendan and Tess's marriage is tested by the fighting, the financial stress, and the school suspension. It holds. Tess objects, worries, and then shows up to watch when she understands what Brendan has decided to do. Their marriage is a real partnership between two people who have chosen each other under difficult circumstances and keep choosing each other."
        },
        {
            "id": "TRADITIONAL-WAR-007",
            "name": "Honoring the Fallen",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "Tommy entered the tournament because his friends died in combat and their families need money. He does not keep his winnings. He fights in silence, wins in silence, and carries the weight of surviving in silence. The film treats grief for fallen comrades as a genuine and serious obligation, not a symptom."
        },
        {
            "id": "WOKE-WAR-001",
            "name": "Sympathetic Treatment of Military Deserter",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 0.7,
            "description": "Tommy Conlon deserted the Marines. The film eventually reveals that he did it after an act of heroism under fire, and presents his desertion sympathetically: a traumatized man who could not face what came next. The Marine Corps would not agree with this framing. The film asks audiences to forgive Tommy for going AWOL, and most do. It's a real woke element, even if it's buried in a deeply traditional story."
        }
    ],
    "seo": {
        "titleTag": "Is Warrior (2011) Woke? Tom Hardy and Joel Edgerton MMA Drama Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Warrior (2011). Tom Hardy, Joel Edgerton, Nick Nolte. Family, brotherhood, redemption. Verdict: STRONGLY TRADITIONAL, +30 TRAD. Full trope audit.",
        "keywords": [
            "is warrior 2011 woke",
            "warrior 2011 review",
            "tom hardy joel edgerton warrior",
            "warrior mma movie traditional",
            "warrior 2011 family movie",
            "is warrior traditional conservative",
            "warrior 2011 virtuevigil",
            "warrior 2011 parents guide",
            "nick nolte warrior oscar",
            "warrior 2011 woke score"
        ]
    }
}

# ============================================================
# REVIEW 3: The Equalizer (2014)
# ============================================================
review3 = {
    "id": "equalizer-2014",
    "slug": "equalizer-2014",
    "title": "The Equalizer",
    "year": 2014,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Action, Thriller, Crime",
    "date": "2026-08-11",
    "datePublished": "2026-08-11",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/equalizer-2014.jpg",
    "releaseDate": "2014-09-26",
    "rating": "R",
    "runtime": "132 min",
    "director": "Antoine Fuqua",
    "writers": ["Richard Wenk"],
    "cast": [
        "Denzel Washington as Robert McCall",
        "Marton Csokas as Teddy (Nicolai Itchenko)",
        "Chloe Grace Moretz as Teri (Alina Zokova)",
        "David Harbour as Masters",
        "Bill Pullman as Brian Plummer",
        "Melissa Leo as Susan Plummer",
        "Johnny Skourtis as Ralphie",
        "Haley Bennett as Mandy"
    ],
    "studio": "Escape Artists / Village Roadshow Pictures",
    "distributor": "Columbia Pictures",
    "verdict": "STRONGLY TRADITIONAL",
    "wokeScore": 0.7,
    "tradScore": 25.9,
    "authIndex": 75,
    "scoreMargin": "+25 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": {
        "is_trap": False,
        "pct_runtime": 0,
        "explanation": "The Equalizer is not a woke trap. The film is exactly what it presents itself as: a man with lethal skills choosing to use them in defense of people who cannot defend themselves. This is established in the first twenty minutes and it never changes. No ideological bait-and-switch, no late-film pivot to progressive messaging. The moral universe is consistent from first scene to last."
    },
    "externalScores": {
        "imdb": "7.2/10",
        "rottenTomatoes": "60%",
        "metacritic": "48/100"
    },
    "seoTitle": "Is The Equalizer (2014) Woke? Denzel Washington Action Film Reviewed | VirtueVigil",
    "seoDescription": "VirtueVigil's full VVWS review of The Equalizer (2014). Denzel Washington as Robert McCall, the ultimate protector. Verdict: STRONGLY TRADITIONAL, +25 TRAD. Full trope audit.",
    "seoKeywords": "is the equalizer 2014 woke, the equalizer 2014 review, denzel washington equalizer traditional, the equalizer conservative movie, is the equalizer woke or traditional, equalizer 2014 virtuevigil, equalizer 2014 parents guide, denzel washington traditional values movie",
    "creative_team": {
        "director": {
            "name": "Antoine Fuqua",
            "role": "Director",
            "note": "Fuqua made Training Day (2001), which won Denzel Washington his second Oscar by putting him on the wrong side of the moral ledger. The Equalizer is the correction: Denzel on the right side, the very right side, the side that eliminates every villain in a hardware store. Fuqua is a precise action filmmaker who understands that violence on screen is only compelling when the audience understands what is at stake, which is why his collaborations with Washington work. The stakes are always clear."
        },
        "writers": [
            {
                "name": "Richard Wenk",
                "role": "Screenplay"
            },
            {
                "name": "Michael Sloan",
                "role": "TV Series Creator"
            },
            {
                "name": "Richard Lindheim",
                "role": "TV Series Creator"
            }
        ],
        "lead_producer": {
            "name": "Todd Black",
            "role": "Producer"
        },
        "composer": {
            "name": "Harry Gregson-Williams",
            "role": "Composer",
            "note": "Gregson-Williams's score is restrained and deliberate, which matches McCall. When the music does accelerate, it does so with the same precision McCall brings to a room full of Russian mobsters. The hardware store sequence is scored to feel like a clock running down."
        },
        "source_material": {
            "name": "Michael Sloan / Richard Lindheim",
            "role": "Creators of the CBS television series (1985-1989)",
            "note": "The original series starred Edward Woodward as Robert McCall, a retired CIA agent who helps people in need. The CBS show ran for four seasons and was beloved for its moral clarity: a competent man choosing to use his skills in service of the vulnerable. Richard Wenk's screenplay updates the setting to Boston and replaces the CIA backstory with something more ambiguous, but the core premise, a man of exceptional skill who refuses to look away, is unchanged."
        },
        "top_cast": [
            {
                "name": "Denzel Washington",
                "role": "Robert McCall"
            },
            {
                "name": "Marton Csokas",
                "role": "Teddy (Nicolai Itchenko)"
            },
            {
                "name": "Chloe Grace Moretz",
                "role": "Teri (Alina Zokova)"
            },
            {
                "name": "David Harbour",
                "role": "Masters"
            },
            {
                "name": "Johnny Skourtis",
                "role": "Ralphie"
            },
            {
                "name": "Frank Grillo",
                "role": "Cosi"
            }
        ]
    },
    "parentalGuidance": {
        "mpaaRating": "R",
        "mpaaDescriptors": "Strong bloody violence and language throughout, including some sexual references",
        "recommendedAge": "17+",
        "contentWarnings": [
            "Sustained graphic violence throughout: stabbings, drowning, gunshots, blunt-force trauma; several sequences are deliberately brutal and prolonged",
            "A teenager is depicted as a victim of sex trafficking and shown in scenes that establish her exploitation without being explicit",
            "Strong profanity used frequently, including the f-word",
            "Russian organized crime depicted in detail; murder and intimidation are routine within the villain group",
            "Sexual references; brief suggestion of prostitution",
            "Corrupt law enforcement depicted working in service of organized crime"
        ],
        "guidance": "This is a hard R and not appropriate for anyone under seventeen without parental co-viewing and discussion. The violence is not gratuitous in the sense that it serves the story, but it is genuinely brutal. The hardware store finale, in particular, is an extended sequence of precise lethal violence that is designed to be satisfying and is. Parents should understand that the film's moral framework is clear: a good man killing bad men to protect vulnerable people. For audiences who accept that framework, the violence functions as justice. For audiences who don't, it's just carnage. The trafficking subplot is handled with restraint but its implications are clear. Not for young teenagers."
    },
    "summary": {
        "overall": "The Equalizer (2014) is a film about a man who knows the right thing to do and does it, at considerable personal cost, with extraordinary precision. That's the whole movie. It sounds simple. It isn't, because Denzel Washington is not a simple actor, and Antoine Fuqua is not a filmmaker who settles for straightforward.\n\nRobert McCall (Washington) works at a Home Mart in Boston, a Lowe's-adjacent hardware store where he knows every employee by name and is working through a reading list he and his late wife never finished. He wakes before dawn. He times himself making oatmeal. He eats alone at a diner most nights, reading whatever book he's on, and he is genuinely at peace there. The diner is where he meets Teri (Chloe Grace Moretz), a teenage girl who is too knowing for her age and living in an arrangement that McCall is too experienced not to recognize immediately.\n\nHe talks to her on successive nights. She shows him a picture she drew of herself standing in front of the Eiffel Tower. She wants to be a singer. He tells her she can be anything she wants to be. She smiles like she doesn't believe that anymore but likes hearing it anyway.\n\nThen she is beaten nearly to death by her handlers and McCall goes to their apartment to offer them money to let her go. They laugh at him. He kills all five of them in nineteen seconds. He times it with his watch.\n\nThis is the inciting incident of The Equalizer, and what makes it work is what comes after it. McCall is not filled with adrenaline or exhilaration. He goes home, scrubs the blood off his hands, and sits in the dark thinking about what he has just started. He is not surprised by what he did. He is thinking about what comes next.\n\nWhat comes next is Teddy (Marton Csokas), a fixer sent from Russia to investigate the deaths of five connected men. Csokas plays Teddy as a man of genuine intelligence and complete amorality. He is not a blunt instrument. He understands power, leverage, and institutional dynamics. He has a counterpart for every move McCall makes. The film's middle act is a chess match between two highly competent men who have both spent decades operating in darkness, and the dialogue between them, when they finally meet, is some of the best villain-hero exchange in recent action cinema.\n\nFuqua stages the violence with the same deliberateness Washington brings to the character. The action sequences are not chaotic. They are planned, executed, and concluded. McCall does not spray bullets. He moves through space with awareness of every object in it, using whatever is at hand: a cork, a wire, a shelf bracket. The hardware store finale, widely cited as one of the best action sequences of the 2010s, is a masterclass in environmental storytelling. McCall is home. The antagonists are not.\n\nBut the film is not just about the violence. It's about what the violence is in service of. McCall mentors Ralphie (Johnny Skourtis), the overweight kid at the store who wants to be a security guard but won't do the push-ups to pass the physical. McCall pushes him. He sets a standard and enforces it because he believes Ralphie is capable of meeting it. When Ralphie passes his test, McCall is as pleased as he is about anything in the film. The mentorship is not incidental. It is the film's argument about what a good man with exceptional skills should actually be doing with his life.\n\nThe ending is decisive. McCall does not disappear back into his quiet life. He posts his number online: got a problem, no one else can help? He will find you. It is the most traditional ending possible for this kind of film, and it works because Washington has spent 132 minutes making it feel earned rather than inevitable.",
        "wokeAnalysis": "The Equalizer has almost nothing that registers as woke content. The single element worth noting is the corrupt law enforcement subplot: Masters (David Harbour) is a dirty cop working in service of Russian organized crime, and McCall has to operate outside any legitimate institutional framework to achieve justice because the institutions are compromised. The film presents this anti-establishment element organically, as it's intrinsic to the genre, but it does cut against conservative deference to law enforcement authority.\n\nThe film features a diverse cast in a naturalistic Boston setting. This is not diversity casting. This is original IP set in a diverse American city with the people who actually live there. Denzel Washington in an action role is not a political statement. He's the best actor working in this genre and he plays this part like it was written for him, because it effectively was.\n\nThe sex trafficking subplot treats its subject with dignity and without exploitation. Teri is shown as a victim, not a narrative device. The film's sympathy for her is genuine and its anger on her behalf is the emotional foundation of everything McCall does. This is the opposite of a woke treatment: it presents exploitation as wrong, its victims as deserving protection, and a man with the capacity to stop it as having the obligation to do so.",
        "tradAnalysis": "The Equalizer is one of the cleaner examples of traditional values filmmaking in twenty-first century action cinema. The film does not lecture. It does not editorialize. It presents a moral framework through action and lets the audience draw their own conclusions. The conclusions it wants you to draw are not ambiguous.\n\nThe protector is the film's central archetype. McCall is not defined by his backstory or his regrets or his internal conflict about using violence. He is defined by what he does with his capacity: he uses it to protect people who cannot protect themselves. Aristotle would recognize this character. The man of virtue who has the power to act and chooses to act on behalf of the powerless is one of the oldest moral figures in Western tradition.\n\nObjective good and evil are the film's moral bedrock. The Russian mob traffics, exploits, and murders. McCall is justice. There is no complexity in the villains that the film asks you to weigh against their crimes. Teddy is intelligent, which makes him interesting, but his intelligence is entirely in service of evil. The film does not ask you to understand him. It asks you to recognize that what he represents must be stopped.\n\nProtecting the innocent is the inciting event and the throughline. McCall cannot watch Teri be exploited and do nothing. His ability to act creates an obligation to act. This is the traditional argument for intervention that goes back to just war theory: the capacity to protect the innocent, combined with proximity to their suffering, creates a moral duty. McCall does not calculate. He acts.\n\nMasculine discipline is expressed through McCall's routines. The oatmeal. The stopwatch. The reading list. The push-ups he does alone in the dark. McCall is a man of extraordinary self-control, and his violence is the extension of that control. He does not explode. He executes. There is no emotion wasted and no movement wasted. This is the film's vision of what masculine virtue looks like: not feeling less, but governing what you feel so that what you do remains precise and purposeful.\n\nMentorship is the film's gentlest traditional element. McCall's relationship with Ralphie is the other half of his character: not just destroying evil but building good. He sees what Ralphie could be and refuses to accept Ralphie's excuses for not becoming it. When Ralphie passes his security exam, the film treats this as a genuine victory, comparable in emotional weight to any of the action sequences. The good man uses his gifts not just to eliminate the bad but to lift up the next generation.\n\nRedemption through moral obligation is how the film frames McCall's return to action. He did not come out of retirement for money or personal satisfaction. He could not look away. This is the traditional argument that the good man does not get to choose neutrality when the innocent are being harmed in his presence. Looking away is itself a moral act, and it's the wrong one."
    },
    "tropeAudit": [
        {
            "id": "TRADITIONAL-EQL-001",
            "name": "The Protector",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "Robert McCall is the classical masculine protector: a man of superior skill who uses it entirely in service of people who cannot defend themselves. Every element of his character, the discipline, the preparation, the willingness to step into harm's way, exists in service of this function. The film presents this as the right way to use exceptional capacity."
        },
        {
            "id": "TRADITIONAL-EQL-002",
            "name": "Objective Good vs. Evil",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "The moral universe of The Equalizer is completely clear. The Russian mob traffics, exploits, murders, and corrupts law enforcement. McCall is justice. There is no moral relativism, no suggestion that the villains have understandable motivations that complicate the audience's judgment. The film knows what it is and commits to it."
        },
        {
            "id": "TRADITIONAL-EQL-003",
            "name": "Protecting the Innocent",
            "category": "Traditional",
            "severity": 5,
            "authenticity": 0.7,
            "centrality": 1.8,
            "weightedScore": 6.3,
            "description": "The inciting event is McCall watching a teenager be abused and deciding he cannot look away. This is the moral core of the entire film. He does not help Teri because it benefits him or because he was hired to. He helps her because she is a person in his presence who cannot protect herself and he can. This is the traditional argument for intervention: capacity plus proximity creates obligation."
        },
        {
            "id": "TRADITIONAL-EQL-004",
            "name": "Masculine Virtue Through Discipline",
            "category": "Traditional",
            "severity": 4,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.8,
            "description": "McCall times himself making oatmeal. He reads his way through a list of books he and his wife planned to finish together. He does push-ups in the dark. His violence is the extension of his self-discipline: precise, purposeful, nothing wasted. The film presents this kind of rigorous self-governance as the foundation of the man's moral character."
        },
        {
            "id": "TRADITIONAL-EQL-005",
            "name": "Mentorship",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "McCall's relationship with Ralphie is the film's most explicitly traditional element. He sees what Ralphie could be and refuses to accept his excuses for not becoming it. When Ralphie passes his security exam, the film treats it as a genuine victory, the passing of a moral standard from a man who holds it to a younger man learning to hold it himself."
        },
        {
            "id": "TRADITIONAL-EQL-006",
            "name": "Redemption Through Moral Obligation",
            "category": "Traditional",
            "severity": 3,
            "authenticity": 0.7,
            "centrality": 1.0,
            "weightedScore": 2.1,
            "description": "McCall had a life. He was at peace. He comes back to fighting not for money or revenge or personal satisfaction. He comes back because he cannot stand by while the innocent are preyed upon in his presence. The film frames this as moral obligation: the good man who can act and does not is not neutral. He has made a choice. McCall refuses to make that choice."
        },
        {
            "id": "WOKE-EQL-001",
            "name": "Corrupt Authority Figures",
            "category": "Woke",
            "severity": 2,
            "authenticity": 0.7,
            "centrality": 0.5,
            "weightedScore": 0.7,
            "description": "The film's corrupt law enforcement element, Masters working in service of the Russian mob, requires McCall to operate entirely outside institutional authority. Justice cannot come from the institutions because the institutions are compromised. This is an anti-establishment element that cuts against conservative trust in law enforcement, though it's handled as genre convention rather than political statement."
        }
    ],
    "seo": {
        "titleTag": "Is The Equalizer (2014) Woke? Denzel Washington Action Film Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of The Equalizer (2014). Denzel Washington as Robert McCall. Verdict: STRONGLY TRADITIONAL, +25 TRAD. Protector trope, moral clarity, full audit.",
        "keywords": [
            "is the equalizer 2014 woke",
            "the equalizer 2014 review",
            "denzel washington equalizer traditional",
            "the equalizer conservative movie",
            "is the equalizer woke or traditional",
            "equalizer 2014 virtuevigil",
            "equalizer 2014 parents guide",
            "denzel washington traditional values movie",
            "the equalizer 2014 woke score",
            "antoine fuqua denzel equalizer review"
        ]
    }
}

# ============================================================
# Append and Save
# ============================================================
all_reviews.extend([review1, review2, review3])

with open(REVIEWS_FILE, "w") as f:
    json.dump(all_reviews, f, indent=2, ensure_ascii=False)

print(f"Saved {len(all_reviews)} reviews to {REVIEWS_FILE}.")

# ============================================================
# Build
# ============================================================
print("Running build.js...")
result = subprocess.run(["node", "build.js"], capture_output=True, text=True)
if result.returncode != 0:
    print("BUILD FAILED:")
    print(result.stderr[-3000:])
    sys.exit(1)
print("Build complete.")

# ============================================================
# Git commit and push
# ============================================================
subprocess.run(["git", "add", "src/data/reviews.json", "dist/"], check=True)
commit_msg = "Add 3 reviews: A Few Good Men (1992), Warrior (2011), The Equalizer (2014)"
subprocess.run(["git", "commit", "-m", commit_msg], check=True)
print("Committed.")

subprocess.run(["git", "push", "origin", "main"], check=True)
print("Pushed.")

# ============================================================
# IndexNow
# ============================================================
urls = [
    "https://virtuevigil.com/reviews/a-few-good-men-1992/",
    "https://virtuevigil.com/reviews/warrior-2011/",
    "https://virtuevigil.com/reviews/equalizer-2014/"
]
print("Submitting to IndexNow...")
result = subprocess.run(
    ["bash", "scripts/submit-indexnow.sh"] + urls,
    capture_output=True, text=True
)
print(result.stdout)
if result.returncode != 0:
    print("IndexNow error:", result.stderr)

print("Done!")
