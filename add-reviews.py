#!/usr/bin/env python3
"""Add/update 3 reviews to reviews.json: F1, LOTR:ROTK, House of the Dragon S1"""

import json

with open('src/data/reviews.json') as f:
    data = json.load(f)

# Remove old F1-2025 if it exists at wrong slot
data = [r for r in data if r['slug'] != 'f1-2025']

# ============================================================
# REVIEW 1: F1 (2025)
# ============================================================
f1 = {
  "id": "f1-2025",
  "slug": "f1-2025",
  "title": "F1",
  "year": 2025,
  "type": "movie",
  "contentType": "movie",
  "platform": "Theatrical / Apple TV+",
  "genre": "Action / Sports Drama",
  "date": "2026-07-15",
  "datePublished": "2026-07-15",
  "author": "VirtueVigil Editorial Team",
  "readTime": "10 min",
  "poster": "/images/posters/f1-2025.jpg",
  "releaseDate": "2025-06-27",
  "rating": "PG-13 (Intense Racing Action, Language)",
  "runtime": "155 minutes",
  "director": "Joseph Kosinski",
  "writers": ["Ehren Kruger"],
  "cast": [
    {"name": "Brad Pitt", "role": "Sonny Hayes"},
    {"name": "Damson Idris", "role": "Joshua Pearce"},
    {"name": "Kerry Condon", "role": "Kate"},
    {"name": "Javier Bardem", "role": "Ruben"},
    {"name": "Tobias Menzies", "role": "Shaw"},
    {"name": "Kim Bodnia", "role": "Nikola"}
  ],
  "studio": "Apple Studios / Jerry Bruckheimer Films / Plan B Entertainment",
  "distributor": "Warner Bros. Pictures / Apple Original Films",
  "verdict": "STRONGLY TRADITIONAL",
  "wokeScore": 1.05,
  "tradScore": 32.41,
  "authIndex": 95,
  "scoreMargin": "+31 TRAD",
  "preRelease": False,
  "wokeTrap": False,
  "woke_trap_assessment": {
    "is_trap": False,
    "explanation": "NOT A WOKE TRAP. F1 is exactly what the trailers promise: a big, loud, gorgeous sports movie built around a masculine comeback story. There is no delayed ideological pivot. Brad Pitt plays a stoic man's man who prays before races, mentors a younger driver through toughness not therapy, and sacrifices his own victory for the team. The film's female technical director is presented as a love interest and competent professional, never as a feminist statement. The diverse casting is organic and never politicized. Conservative audiences can watch this without flinching."
  },
  "externalScores": {
    "imdb": 7.2,
    "rottenTomatoesCritic": 78,
    "rottenTomatoesAudience": 92,
    "metacritic": 65
  },
  "creative_team": {
    "director": {
      "name": "Joseph Kosinski",
      "ideology": "APOLITICAL CRAFTSMAN. Kosinski has never made a politically coded film. His body of work (Tron: Legacy, Oblivion, Only the Brave, Top Gun: Maverick) is defined by visual precision, practical-effects devotion, and reverence for masculine competence. Top Gun: Maverick became a cultural flashpoint precisely because it felt refreshingly free of ideology. F1 continues that tradition."
    },
    "writer": {
      "name": "Ehren Kruger",
      "ideology": "APOLITICAL WORKMAN. Kruger writes lean, archetypal blockbuster scripts (Top Gun: Maverick, Transformers). His F1 screenplay prioritizes momentum and spectacle over thematic ambition. No political profile."
    }
  },
  "parentalGuidance": {
    "sexualContent": "Minimal. Implied sex scene between adults (nothing shown). A flirtation over poker. One kiss. No nudity.",
    "violence": "Moderate. Multiple high-speed racing crashes, some resulting in fire and injury. A car catches fire with the driver inside (he is rescued). No gore, no graphic violence. Intensity is sports-action standard.",
    "language": "Moderate to strong. Multiple instances of profanity. Standard for PG-13 blockbusters.",
    "substanceUse": "Mild. Social drinking. Gambling (poker). Nothing prominent or glamorized.",
    "matureThemes": "Redemption, aging, mentorship, self-sacrifice, and confronting past failure. A character conceals a dangerous medical condition to keep racing. Corporate sabotage and betrayal."
  },
  "fidelityCasting": {
    "raceSwaps": 0,
    "genderSwaps": 0,
    "orientationChanges": 0,
    "notes": "ORIGINAL SCREENPLAY. Not an adaptation, so no source material to evaluate for casting fidelity. Damson Idris as a Black F1 driver is ahistorical (only Lewis Hamilton has competed as a Black driver in real F1) but the film never addresses race. Kerry Condon as a female technical director is similarly ahistorical but presented without commentary."
  },
  "summary": {
    "overall": "F1 is the purest strain of old-school Hollywood blockbuster filmmaking released in 2025. It is a comeback story about a broken man who finds redemption through grit, self-sacrifice, and the refusal to quit. No lectures. No deconstruction of masculinity. No identity politics. Just Brad Pitt driving very, very fast.\n\nJoseph Kosinski, the director who turned Top Gun: Maverick into the biggest crowd-pleaser of 2022, has done it again. F1 is not as tight or as emotionally precise as Maverick, and its story beats are as predictable as a safety car on lap one. But what it does, it does at 200 miles per hour with absolute conviction.\n\nBrad Pitt plays Sonny Hayes, a former F1 prodigy who crashed out in the 1990s and never recovered. Three decades later, he is a nomadic racer-for-hire, drifting through life with the quiet desperation of a man who peaked at 25 and knows it. When his former teammate Ruben (Javier Bardem) recruits him to save the struggling APXGP team from collapse, Sonny reluctantly straps in for one last shot. The setup is pure sports movie DNA: underdog team, old veteran, young hotshot (Damson Idris as Joshua Pearce), corporate villain. You have seen this before in Rocky, in Hoosiers, in Maverick itself. Kosinski does not pretend otherwise. He leans into the formula the way a good driver leans into a corner: with speed and commitment.\n\nPitt is magnetic. At 61, he plays Sonny with a weathered cool that only an actual movie star can pull off. The character is simple on paper: a man haunted by what he could not finish, running from the thing he loves because it almost killed him. Pitt fills in the margins with physical economy. A smirk here. A long stare at the track there. And a quiet prayer before every race, crossing himself in the cockpit while the engines roar. The movie never explains the prayer. It does not need to. It just sits there, a small, genuine detail that tells you everything about who this man is.\n\nDamson Idris holds his own as Joshua, the ambitious rookie who resents being saddled with an aging has-been. Their mentor-protege dynamic is the emotional core of the film. Joshua does not learn humility through a diversity workshop. He learns it by crashing, burning, getting rescued by the old man, and then crashing again because he was too arrogant to listen. The movie respects the process of earning wisdom through failure. That is a traditional value presented without a single ounce of self-consciousness.\n\nKerry Condon plays Kate, APXGP's technical director and Sonny's ex-wife. Here is where some reviewers expected the culture-war angle to show up. It does not. Kate is competent and brilliant at her job, but the movie never turns her into a soapbox. No scene where someone doubts her because she is a woman. No montage of her proving the doubters wrong. She designs upgrades, calls strategies, and falls for Sonny because he is Brad Pitt. She feels like a person instead of a position paper.\n\nBut let us talk about what everyone actually came for: the racing. F1 contains the best motorsport cinematography ever committed to film. That is not hyperbole. Kosinski shot extensive footage during real 2023 and 2024 F1 Grand Prix weekends, with Pitt and Idris driving modified Formula 2 cars on actual circuits. Lewis Hamilton, who served as a producer, ensured the racing sequences reflected how the sport actually works. The result is something no green screen can replicate: real speed, real danger, real physics. When a car spins at Monza and catches fire, you feel it in your chest. Hans Zimmer's score is propulsive and relentless, raising your heart rate before you consciously register why.\n\nThe film's weaknesses are the ones you would expect from a 155-minute blockbuster. Supporting characters are underdeveloped. The corporate conspiracy subplot feels obligatory. And there is a third-act monologue where Sonny explains what racing means to him that stops the movie cold for about ninety seconds. The mid-section drags during the European stretch. The film could have lost fifteen minutes without sacrificing anything of value.\n\nBut these are nitpicks about a movie that accomplishes something remarkable in 2025: it is a blockbuster built on craft, charisma, and the radical notion that audiences want to feel something without being told what to think. The culture-war verdict is clear: F1 is one of the safest watches of the year for conservative audiences. The protagonist is an old-school masculine hero who earns redemption through sacrifice, not therapy. He prays. He mentors through tough love. He puts the team above himself in the climactic race. The diverse casting is organic and unforced. The female characters serve the story without serving an agenda.\n\nGo see it. In IMAX. Do not drive too fast on the way home.",
    "quickTake": "Pure old-school blockbuster. Masculine hero. No lectures. Just fast cars and earned redemption.",
    "recommendation": "See it. In IMAX if possible. The racing cinematography is the best ever committed to film.",
    "bestFor": "Fans of Top Gun: Maverick, motorsport enthusiasts, anyone who misses blockbusters that entertain without lecturing.",
    "skipIf": "You found Top Gun: Maverick too traditional. Or if 155 minutes of racing sounds exhausting rather than exciting.",
    "highlights": ["Brad Pitt's weathered, magnetic lead performance", "The best motorsport cinematography ever filmed", "Hans Zimmer's propulsive, electrifying score", "A mentor-protege arc built on tough love, not therapy", "Sonny's quiet pre-race prayer: a character detail that speaks volumes"],
    "lowlights": ["155-minute runtime with a saggy mid-section", "Underdeveloped supporting characters", "A third-act monologue that stops the movie cold", "The corporate conspiracy subplot feels obligatory"]
  },
  "seo": {
    "titleTag": "Is F1 (2025) Woke? Review | VirtueVigil",
    "metaDescription": "VirtueVigil's full VVWS review of F1 (2025). Brad Pitt stars in a pure old-school racing blockbuster. Trope scores, verdict: STRONGLY TRADITIONAL. Parental guidance included.",
    "keywords": "is F1 woke, F1 2025 review, F1 VirtueVigil, F1 parents guide, Brad Pitt F1 review"
  },
  "tropeAudit": [
    {
      "id": "TRADITIONAL-027",
      "name": "Redemptive Arcs",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.3,
      "description": "Sonny Hayes's entire arc is redemption: a man who crashed out of F1 in disgrace, spent 30 years running from his failure, and earns his way back through sacrifice, courage, and refusing to quit. The film's moral thesis is that redemption must be earned through action, not declared through self-acceptance."
    },
    {
      "id": "TRADITIONAL-032",
      "name": "Meritocratic Triumph",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "Nobody is handed anything. Sonny proves he can still drive. Joshua proves he can learn humility. Kate's engineering has to pass real scrutiny. The villain tries to buy success and fails. The film argues that competence and courage are the only currencies that matter."
    },
    {
      "id": "TRADITIONAL-033",
      "name": "Wise Elder / Reluctant Mentor",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "Sonny becomes the reluctant mentor to Joshua, passing down hard-won wisdom earned through failure. He teaches by doing, by sacrificing, by demanding better. Joshua learns respect through consequences, not conversation."
    },
    {
      "id": "TRADITIONAL-041",
      "name": "Industry and Perseverance",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "The entire film is about working harder than everyone else. APXGP is the underfunded backmarker that succeeds through grit, engineering ingenuity, and sheer determination. The racing sequences are sustained arguments for the value of practice, preparation, and persistence."
    },
    {
      "id": "TRADITIONAL-026",
      "name": "Self-Sacrificing Hero",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "The climactic moral beat: Sonny sacrifices his shot at personal victory to hold off the competition so his young teammate can take the lead. Selflessness is rewarded. Individual glory matters less than the team. The film's moral architecture is classically traditional."
    },
    {
      "id": "TRADITIONAL-028",
      "name": "Rugged Individualist",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.1,
      "description": "Sonny is an archetype of rugged individualism: a lone wolf who lives out of motels, races for cash, answers to no one, and earns his place through sheer ability. The film respects him for it rather than pathologizing his independence."
    },
    {
      "id": "TRADITIONAL-029",
      "name": "Principled Patriarch",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.1,
      "description": "Javier Bardem's Ruben is a team owner who genuinely loves his people, believes in Sonny when no one else does, and makes hard decisions from principle rather than profit. He is a father figure to the entire team."
    },
    {
      "id": "TRADITIONAL-043",
      "name": "Faith in Adversity",
      "category": "Traditional",
      "severity": 2,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.7,
      "description": "Sonny crosses himself and silently prays before every race. The film never explains it, never comments on it, never makes it a plot point. It is simply part of who he is: a man who asks for help from something bigger than himself before doing something dangerous."
    },
    {
      "id": "TRADITIONAL-044",
      "name": "Honest Worker",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 1.05,
      "description": "The APXGP crew are working-class professionals: mechanics, engineers, strategists. The film respects their expertise and treats their labor as essential to the team's success. The star driver is nothing without the crew."
    },
    {
      "id": "WOKE-014",
      "name": "Evil Capitalist / Corporate Villain",
      "category": "Woke",
      "severity": 2,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.7,
      "description": "Tobias Menzies plays a corporate saboteur working to destroy APXGP from within for financial gain. This is a genre convention of sports movies (corporate greed as antagonist), not an ideological critique of capitalism. The villain is greedy, not politically coded."
    },
    {
      "id": "WOKE-003",
      "name": "Girl Boss",
      "category": "Woke",
      "severity": 1,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.35,
      "description": "Kerry Condon as Kate, the female technical director. Historically unrealistic for F1, but the film never frames it as a statement. Kate is competent, but she is primarily a love interest and functional character, not a girlboss delivering lectures. The authenticity is High because the character is written as a person, not a political vessel. Trace severity."
    }
  ]
}

# Compute scores
woke_tropes = [t for t in f1['tropeAudit'] if t['category'] == 'Woke']
trad_tropes = [t for t in f1['tropeAudit'] if t['category'] == 'Traditional']
f1['wokeScore'] = round(sum(t['weightedScore'] for t in woke_tropes), 2)
f1['tradScore'] = round(sum(t['weightedScore'] for t in trad_tropes), 2)
margin = f1['tradScore'] - f1['wokeScore']

print(f"F1: woke={f1['wokeScore']}, trad={f1['tradScore']}, margin={margin}")

# ============================================================
# REVIEW 2: The Lord of the Rings: The Return of the King (2003)
# ============================================================
lotr = {
  "id": "the-lord-of-the-rings-the-return-of-the-king-2003",
  "slug": "the-lord-of-the-rings-the-return-of-the-king-2003",
  "title": "The Lord of the Rings: The Return of the King",
  "year": 2003,
  "type": "movie",
  "contentType": "movie",
  "platform": "Theatrical",
  "genre": "Fantasy / Epic / Adventure",
  "date": "2026-07-15",
  "datePublished": "2026-07-15",
  "author": "VirtueVigil Editorial Team",
  "readTime": "12 min",
  "poster": "/images/posters/the-lord-of-the-rings-the-return-of-the-king-2003.jpg",
  "releaseDate": "2003-12-17",
  "rating": "PG-13 (Intense Epic Battle Sequences, Frightening Images)",
  "runtime": "201 minutes",
  "director": "Peter Jackson",
  "writers": ["Fran Walsh", "Philippa Boyens", "Peter Jackson"],
  "cast": [
    {"name": "Elijah Wood", "role": "Frodo Baggins"},
    {"name": "Ian McKellen", "role": "Gandalf"},
    {"name": "Viggo Mortensen", "role": "Aragorn"},
    {"name": "Sean Astin", "role": "Samwise Gamgee"},
    {"name": "Andy Serkis", "role": "Gollum"},
    {"name": "Orlando Bloom", "role": "Legolas"},
    {"name": "John Rhys-Davies", "role": "Gimli"},
    {"name": "Bernard Hill", "role": "Theoden"},
    {"name": "Miranda Otto", "role": "Eowyn"},
    {"name": "David Wenham", "role": "Faramir"},
    {"name": "Karl Urban", "role": "Eomer"},
    {"name": "John Noble", "role": "Denethor"},
    {"name": "Cate Blanchett", "role": "Galadriel"},
    {"name": "Liv Tyler", "role": "Arwen"},
    {"name": "Hugo Weaving", "role": "Elrond"}
  ],
  "studio": "New Line Cinema / WingNut Films",
  "distributor": "New Line Cinema",
  "verdict": "STRONGLY TRADITIONAL",
  "wokeScore": 0.35,
  "tradScore": 64.47,
  "authIndex": 98,
  "scoreMargin": "+64 TRAD",
  "preRelease": False,
  "wokeTrap": False,
  "woke_trap_assessment": {
    "is_trap": False,
    "explanation": "NOT A WOKE TRAP. Return of the King is arguably the most traditionally-themed blockbuster ever made, adapted from a source written by a devout Catholic. The Christian allegory runs deep: Frodo as a Christ-figure bearing the weight of sin, Gandalf's death and resurrection, Aragorn as the returning king, the clear moral binary of good versus evil, and the triumph of humility over power. Eowyn's battlefield courage is organically rooted in Tolkien's text and motivated by love and loyalty, not ideology. The film contains zero hidden progressive agendas. It is exactly what it appears to be: a grand moral epic about sacrifice, mercy, and the restoration of order."
  },
  "externalScores": {
    "imdb": 9.0,
    "rottenTomatoesCritic": 94,
    "rottenTomatoesAudience": 86,
    "metacritic": 94
  },
  "creative_team": {
    "director": {
      "name": "Peter Jackson",
      "ideology": "APOLITICAL STORYTELLER. Jackson is a New Zealand filmmaker whose work is defined by imaginative world-building and technical innovation rather than political messaging. His reverence for Tolkien's source material is evident in every frame. He has no significant political profile."
    },
    "writer": {
      "name": "Fran Walsh, Philippa Boyens, Peter Jackson",
      "ideology": "FAITHFUL ADAPTATIONISTS. The screenwriting team approached Tolkien's work with extraordinary fidelity to its themes, characters, and moral framework. Their adaptations honor the source material's traditional values without imposing modern sensibilities."
    }
  },
  "parentalGuidance": {
    "sexualContent": "NONE. No sexual content whatsoever. The romance between Aragorn and Arwen is chaste and courtly.",
    "violence": "INTENSE EPIC BATTLE SEQUENCES. Large-scale medieval warfare with swords, arrows, siege weapons, and fantastical creatures. Characters are struck down, crushed, and killed. Some frightening imagery including the Nazgul, Shelob (giant spider), and orcs. Blood is present but not gratuitous.",
    "language": "MILD. Fantasy-appropriate exclamations. No modern profanity.",
    "substanceUse": "MILD. Pipe-weed (Tolkien's fantasy tobacco) smoked by hobbits. Ale consumed at celebrations. Never glamorized as intoxication.",
    "matureThemes": "Death, sacrifice, the corruption of power, despair, the burden of duty, the cost of war, PTSD (Frodo's lasting wounds), temptation, mercy versus vengeance, the nature of evil."
  },
  "fidelityCasting": {
    "raceSwaps": 0,
    "genderSwaps": 0,
    "orientationChanges": 0,
    "notes": "EXTREMELY FAITHFUL. Jackson's casting adheres to Tolkien's descriptions with remarkable precision. Every major character matches their book counterpart in ethnicity, gender, and essential character. The films were made before the era of identity-based casting and stand as a monument to faithful adaptation."
  },
  "summary": {
    "overall": "The Return of the King is not merely the greatest fantasy film ever made. It is arguably the most traditionally-themed blockbuster in Hollywood history. Adapted from J.R.R. Tolkien's devoutly Catholic epic, it is a work of profound moral seriousness dressed in the armor of a crowd-pleasing spectacle. Eleven Oscars, including Best Picture, confirm what audiences already knew: this is cinema operating at its highest possible register.\n\nThe film opens with Smeagol's murder of Deagol over the Ring, a prologue that establishes the central thesis: evil corrupts absolutely, beginning with the smallest betrayal. From there, Jackson weaves three narrative threads. Frodo (Elijah Wood) and Sam (Sean Astin) follow Gollum (Andy Serkis) into Mordor to destroy the One Ring in the fires of Mount Doom. Aragorn (Viggo Mortensen) must embrace his destiny as the rightful King of Gondor and unite the armies of men against Sauron. Gandalf (Ian McKellen) orchestrates the defense of Minas Tirith while navigating the madness of Steward Denethor (John Noble). Each thread converges on the same moral question: will you choose the hard right over the easy wrong?\n\nTolkien was a devout Roman Catholic who described The Lord of the Rings as 'a fundamentally religious and Catholic work.' The Christian architecture is unmistakable once you look for it. Frodo is a Christ-figure: the innocent who takes the weight of sin (the Ring) upon himself and carries it to its destruction, knowing it will cost him everything. Gandalf dies and returns transfigured: 'I am Gandalf the White, and I come back to you now at the turn of the tide.' Aragorn is the returning king, the rightful heir who walks the Paths of the Dead and emerges to claim his crown. And the hobbits, the smallest and weakest creatures in Middle-earth, are the ones through whom the great evil is finally undone. 'Even the smallest person can change the course of the future.' This is not therapeutic self-actualization. This is theology.\n\nThe film's moral clarity is absolute and unembarrassed. There is no moral equivalence between Sauron's forces and the free peoples of Middle-earth. The orcs are not misunderstood. The Ring does not have a point. Evil is real, it is seductive, and it must be resisted to the point of death. When Theoden rallies the Rohirrim at Pelennor Fields, 'Ride now! Ride for ruin and the world's ending! Death!', the charge is framed as noble sacrifice, not tragic futility. The men of Rohan are defending their homes, their families, their civilization. The film treats this defense as the highest moral calling.\n\nSean Astin's Samwise Gamgee is the film's moral center and one of the greatest depictions of servant leadership in cinema. Sam is not a warrior. He is a gardener. His heroism is the heroism of fidelity: staying when staying is impossible, carrying Frodo when Frodo cannot carry himself, refusing despair even at the Cracks of Doom. 'I can't carry it for you, but I can carry you.' That single line contains more moral truth than most films manage in their entire runtime. Sam is the humble servant exalted, and the film treats his simple goodness as more powerful than all the armies of Mordor.\n\nViggo Mortensen's Aragorn completes his three-film arc from ranger to king with quiet authority. His kingship is not about power but service: he bows to the hobbits at his own coronation. 'My friends, you bow to no one.' The king who serves is greater than the king who conquers. This is the traditional model of authority elevated to its highest expression.\n\nBernard Hill's Theoden delivers the film's most emotionally devastating arc. A king who despaired at Helm's Deep, who feared he had failed his ancestors, rises to lead the greatest cavalry charge in cinema history. His death is not tragedy but consummation: a man who redeemed himself through sacrifice, who 'goes to his fathers in whose mighty company he shall not now feel ashamed.' This is the redemptive arc in its purest form.\n\nMiranda Otto's Eowyn deserves particular attention because she is sometimes misread as a feminist icon. She is not, and Tolkien would have been horrified by the suggestion. Eowyn's battlefield heroism is motivated by love for her uncle Theoden and loyalty to her people, not by ideology. She kills the Witch-king not to prove women can fight but because 'no living man' can kill him, and she is a woman. The moment is a fulfillment of prophecy, not a statement about gender equality. Her resolution is to find healing and love with Faramir in the Houses of Healing: 'I will be a healer, and love all things that grow and are not barren.' This is traditional femininity as restoration, not regression. The film treats both her courage and her healing as noble, complementary, and whole.\n\nThe film's technical achievements remain staggering. Howard Shore's score is the greatest ever composed for cinema, a Wagnerian masterpiece that gives every culture in Middle-earth its own musical language. The siege of Minas Tirith is the most ambitious battle sequence ever filmed, blending practical effects, miniatures (bigatures, Jackson called them), and early CGI into a seamless whole. The charge of the Rohirrim at Pelennor Fields is perhaps the single most emotionally overwhelming sequence in film history. Gollum, played by Andy Serkis through groundbreaking motion capture, remains the most convincing fully digital character ever created: pitiable, terrifying, and tragically human.\n\nReturn of the King is not perfect. The multiple endings stretch the denouement past what some audiences can tolerate, though the extended edition's additional material makes them feel more earned. The Army of the Dead resolution is a deus ex machina that resolves the Pelennor Fields battle a bit too neatly. Denethor's arc is reduced from the book's tragedy to something closer to madness, and the Scouring of the Shire is omitted entirely. These are valid criticisms, but they are criticisms at the margins of a monumental achievement.\n\nWhat matters most is this: The Lord of the Rings is the last great blockbuster trilogy built on a foundation of faith, honor, and objective morality. It was made before identity politics colonized popular entertainment, and it stands as a permanent refutation of the idea that traditional values cannot produce great art. Twenty years later, nothing has come close. Nothing will.\n\nThe culture-war verdict could not be simpler. Return of the King is STRONGLY TRADITIONAL. Its moral universe is Christian. Its heroes are humble servants, reluctant kings, and self-sacrificing friends. Its evil is absolute and must be destroyed. Its women are courageous but find their fulfillment in healing, love, and family. Its ending affirms that goodness, order, and mercy ultimately prevail, even if the cost is terrible and permanent for those who bore the burden.\n\nIf you only watch one film that affirms traditional values this year, make it this one. Even if you have seen it before. Especially if you have seen it before.",
    "quickTake": "The most traditionally-themed blockbuster in Hollywood history. Christian allegory, moral clarity, and the triumph of humility over power.",
    "recommendation": "Essential. This is not merely a great film; it is a moral education in the form of epic spectacle. Watch the extended edition if possible.",
    "bestFor": "Anyone who wants to see traditional values elevated to the highest level of cinematic art. Families. Christians. Lovers of epic storytelling.",
    "skipIf": "You cannot tolerate a 201-minute runtime. You prefer morally ambiguous antiheroes. You require modern identity politics in your entertainment.",
    "highlights": ["The charge of the Rohirrim: the single greatest cavalry sequence in cinema", "Sam carrying Frodo up Mount Doom: servant leadership in its purest form", "Aragorn bowing to the hobbits: 'My friends, you bow to no one'", "Howard Shore's Wagnerian score, the greatest ever composed for film", "Gollum: the most convincing digital character ever created", "The moral clarity: evil is real, sacrifice is noble, mercy is transformative"],
    "lowlights": ["Multiple endings stretch the denouement past two hours of resolution", "Army of the Dead resolves Pelennor Fields too conveniently", "Denethor's arc is simplified from tragedy to madness", "The Scouring of the Shire is omitted entirely"]
  },
  "seo": {
    "titleTag": "Is The Lord of the Rings: The Return of the King Woke? Review | VirtueVigil",
    "metaDescription": "VirtueVigil's full VVWS review of The Return of the King (2003). The most traditionally-themed blockbuster ever made. Verdict: STRONGLY TRADITIONAL. Trope scores, parental guidance included.",
    "keywords": "is Lord of the Rings woke, Return of the King review, LOTR VirtueVigil, Return of the King parents guide, LOTR traditional values"
  },
  "tropeAudit": [
    {
      "id": "TRADITIONAL-039",
      "name": "Objective Good vs. Evil",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.3,
      "description": "Sauron is pure, absolute evil. There is no moral equivalence, no tragic backstory, no 'both sides.' The orcs are not misunderstood. Mordor is not a legitimate alternative political system. The film treats the fight against evil as the highest moral calling and frames victory as the restoration of goodness, order, and light. Tolkien's Catholic worldview insists that evil is a corruption of good, not an equal force, and the film honors this completely."
    },
    {
      "id": "TRADITIONAL-026",
      "name": "Self-Sacrificing Hero",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.3,
      "description": "Frodo's entire arc is sacrificial. He volunteers to carry the Ring to Mordor knowing it will destroy him. He accepts that he will never return to the Shire he saved. 'I'm glad to be with you, Samwise Gamgee, here at the end of all things.' This is the Christ-figure: the innocent who bears the weight of sin so that others may live free. The film treats his sacrifice as the noblest act imaginable."
    },
    {
      "id": "TRADITIONAL-038",
      "name": "Reluctant Leader",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.3,
      "description": "Aragorn spends three films resisting his destiny as king. He fears the weakness of his bloodline (Isildur's failure). He prefers the anonymity of the ranger. But when Middle-earth needs a king, he walks the Paths of the Dead and claims Anduril. His kingship is service, not ambition: he bows to the hobbits at his coronation. 'My friends, you bow to no one.' This is the traditional model of authority perfected."
    },
    {
      "id": "TRADITIONAL-049",
      "name": "Humble Servant",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.3,
      "description": "Samwise Gamgee is the moral center of the entire trilogy. He is not a warrior or a wizard. He is a gardener. His heroism is fidelity: staying when staying is impossible, carrying Frodo up Mount Doom, refusing despair. 'I can't carry it for you, but I can carry you.' The film insists that simple, steadfast goodness is more powerful than armies. Sam is the humble servant exalted, and it is deeply moving."
    },
    {
      "id": "TRADITIONAL-045",
      "name": "Defense of the Innocent",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.3,
      "description": "Every battle in the film is defensive. Gondor defends Minas Tirith against Sauron's armies. Rohan rides to Gondor's aid. Aragorn marches on the Black Gate to draw Sauron's eye away from Frodo. The film frames armed defense of home, family, and civilization as the highest moral obligation. The men who die at Pelennor Fields die as heroes protecting the innocent."
    },
    {
      "id": "TRADITIONAL-027",
      "name": "Redemptive Arcs",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "Theoden's arc is the film's most emotionally devastating: a king who despaired, who feared he failed his ancestors, rises to lead the greatest cavalry charge in cinema history. His death is not tragedy but consummation: 'I go to my fathers in whose mighty company I shall not now feel ashamed.' Faramir earns his father's love through sacrificial obedience. Both arcs insist that redemption is possible but must be purchased with blood."
    },
    {
      "id": "TRADITIONAL-042",
      "name": "Forgiving Heart",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "Frodo's mercy toward Gollum is the act that saves Middle-earth. 'My heart tells me that Gollum has some part to play yet, for good or ill.' Without Frodo's repeated forgiveness, Gollum would not have been at the Cracks of Doom to take the Ring and fall. The film's thesis is that mercy is not weakness but the decisive strategic virtue. Pity stays Bilbo's hand. Pity saves the world."
    },
    {
      "id": "TRADITIONAL-030",
      "name": "Biblical Morality",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 5.04,
      "description": "Tolkien's Catholic worldview saturates every frame. Gandalf's death and resurrection ('I come back to you now at the turn of the tide'). The temptation of the Ring as original sin. The triumph of the humble over the mighty. The King as healer ('The hands of the king are the hands of a healer'). The bittersweet ending where victory costs the victor everything. This is Christian art at its most sublime."
    },
    {
      "id": "TRADITIONAL-031",
      "name": "Patriotic Soldier / Defending the Homeland",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.8,
      "description": "The Rohirrim are warrior-patriots who ride to defend Gondor because 'the beacons are lit.' Their charge at Pelennor Fields is motivated by love of country, loyalty to allies, and the duty to fight evil. The film treats their sacrifice as the highest expression of martial virtue. Eomer's grief when he finds Eowyn on the battlefield is devastating precisely because the love of kin is what makes the sacrifice meaningful."
    },
    {
      "id": "TRADITIONAL-047",
      "name": "Justice Restored",
      "category": "Traditional",
      "severity": 5,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 6.3,
      "description": "The entire trilogy builds toward the restoration of rightful order. Aragorn returns as king. Gondor and Arnor are reunited. Sauron is destroyed. The Ring is unmade. Evil is not merely defeated but its foundations are shattered. The ending is a restoration, not a revolution. The old order, having proven itself worthy through sacrifice, returns renewed."
    },
    {
      "id": "TRADITIONAL-046",
      "name": "Heritage over Innovation",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.1,
      "description": "Narsil, reforged as Anduril, is the literal embodiment of heritage as power. Aragorn does not build something new; he reclaims what was lost. The wisdom of the past (Elrond, Galadriel, the Ents) is treated as authoritative. The film respects tradition, lineage, and ancestral obligation as sources of moral authority."
    },
    {
      "id": "TRADITIONAL-050",
      "name": "Harmony and Order",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.8,
      "description": "The film's vision of victory is not conquest but harmony: the King returns, the peoples of Middle-earth live in peace, and the Shire continues its quiet agricultural rhythms. The final image is Sam returning to his garden and his family: 'Well, I'm back.' Order, domesticity, and peace are the rewards of sacrifice, not the enemies of progress."
    },
    {
      "id": "TRADITIONAL-033",
      "name": "Wise Elder",
      "category": "Traditional",
      "severity": 4,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 2.8,
      "description": "Gandalf the White is wisdom incarnate: the guide who directs without dominating, who counsels without commanding, who fights only when necessary and then with overwhelming authority. His relationship with Pippin on the battlements of Minas Tirith, explaining death as 'a far green country,' is one of the most tender depictions of elder wisdom in cinema."
    },
    {
      "id": "TRADITIONAL-036",
      "name": "Traditional Femininity",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 1.05,
      "description": "Arwen chooses mortality out of love for Aragorn, sacrificing her immortality and her people for her husband. Eowyn's resolution is healing and love: 'I will be a healer, and love all things that grow.' The film treats traditional femininity, devotion, healing, and nurturing, as noble and fulfilling rather than oppressive. Neither woman is diminished by her choice."
    },
    {
      "id": "WOKE-003",
      "name": "Girl Boss",
      "category": "Woke",
      "severity": 1,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.35,
      "description": "Eowyn's battlefield heroism (killing the Witch-king) could be read as girlboss if stripped of context. In context, it is organically rooted in Tolkien's 1950s text and motivated by love for her uncle and loyalty to her people. Her resolution finds fulfillment in healing and love with Faramir. The authenticity is High because it reflects the source material faithfully rather than imposing a modern agenda. Trace severity only."
    }
  ]
}

# Compute scores
woke_tropes = [t for t in lotr['tropeAudit'] if t['category'] == 'Woke']
trad_tropes = [t for t in lotr['tropeAudit'] if t['category'] == 'Traditional']
lotr['wokeScore'] = round(sum(t['weightedScore'] for t in woke_tropes), 2)
lotr['tradScore'] = round(sum(t['weightedScore'] for t in trad_tropes), 2)
margin = lotr['tradScore'] - lotr['wokeScore']
lotr['scoreMargin'] = f"+{int(margin)} TRAD"

print(f"LOTR: woke={lotr['wokeScore']}, trad={lotr['tradScore']}, margin={margin}")

# ============================================================
# REVIEW 3: House of the Dragon (Season 1) (2022)
# ============================================================
hotd = {
  "id": "house-of-the-dragon-s1-2022",
  "slug": "house-of-the-dragon-s1-2022",
  "title": "House of the Dragon (Season 1)",
  "year": 2022,
  "type": "tv",
  "contentType": "tv",
  "platform": "HBO / Max",
  "genre": "Fantasy / Drama",
  "date": "2026-07-15",
  "datePublished": "2026-07-15",
  "author": "VirtueVigil Editorial Team",
  "readTime": "11 min",
  "poster": "/images/posters/house-of-the-dragon-s1-2022.jpg",
  "releaseDate": "2022-08-21",
  "rating": "TV-MA (Graphic Violence, Sexual Content, Nudity, Language)",
  "runtime": "10 episodes, ~60 min each",
  "director": "Miguel Sapochnik, Greg Yaitanes, Clare Kilner, Geeta Vasant Patel",
  "writers": ["Ryan Condal", "George R.R. Martin"],
  "cast": [
    {"name": "Paddy Considine", "role": "King Viserys I Targaryen"},
    {"name": "Matt Smith", "role": "Daemon Targaryen"},
    {"name": "Emma D'Arcy", "role": "Rhaenyra Targaryen (adult)"},
    {"name": "Milly Alcock", "role": "Rhaenyra Targaryen (young)"},
    {"name": "Olivia Cooke", "role": "Alicent Hightower (adult)"},
    {"name": "Emily Carey", "role": "Alicent Hightower (young)"},
    {"name": "Rhys Ifans", "role": "Otto Hightower"},
    {"name": "Steve Toussaint", "role": "Corlys Velaryon"},
    {"name": "Eve Best", "role": "Rhaenys Targaryen"},
    {"name": "Fabien Frankel", "role": "Criston Cole"},
    {"name": "Graham McTavish", "role": "Harrold Westerling"},
    {"name": "Sonoya Mizuno", "role": "Mysaria"}
  ],
  "studio": "HBO",
  "distributor": "HBO / Warner Bros. Discovery",
  "verdict": "TRADITIONAL",
  "wokeScore": 5.22,
  "tradScore": 7.43,
  "authIndex": 85,
  "scoreMargin": "+2 TRAD",
  "preRelease": False,
  "wokeTrap": False,
  "woke_trap_assessment": {
    "is_trap": False,
    "explanation": "NOT A WOKE TRAP. House of the Dragon presents a succession conflict (daughter named heir vs. first-born son) with genuine nuance and avoids the heavy-handed moralizing that defines genuine woke traps. Rhaenyra is not a girlboss; she is flawed, makes costly mistakes, and suffers real consequences. The Greens are not cartoonish misogynists; they make legitimate arguments based on law, tradition, and precedent. The gender dynamics are period-appropriate to a medieval fantasy setting. The race-blind casting of Corlys Velaryon (Steve Toussaint) is a production choice the show treats as irrelevant to the narrative. The ideological elements are visible from episode one and never escalate into hidden preaching."
  },
  "externalScores": {
    "imdb": 8.3,
    "rottenTomatoesCritic": 93,
    "rottenTomatoesAudience": 81,
    "metacritic": 69
  },
  "creative_team": {
    "director": {
      "name": "Miguel Sapochnik, Greg Yaitanes, Clare Kilner, Geeta Vasant Patel",
      "ideology": "MIXED. Sapochnik (Game of Thrones veteran) is a visual craftsman focused on spectacle and character. The rotating directors serve the story rather than pushing individual agendas. The show's ideological fingerprints belong primarily to the writers' room."
    },
    "writer": {
      "name": "Ryan Condal, George R.R. Martin",
      "ideology": "NUANCED. Martin's source material (Fire and Blood) was written as a faux-historical chronicle exploring succession, power, and human fallibility. Condal's adaptation is notably more restrained than Game of Thrones in its treatment of gender dynamics. The writers present both sides of the succession conflict with intellectual honesty."
    }
  },
  "parentalGuidance": {
    "sexualContent": "HIGH. Multiple explicit sex scenes including a brothel sequence. Incestuous themes consistent with Targaryen lore. A graphic childbirth scene that is more disturbing than any of the sex scenes.",
    "violence": "EXTREME. Graphic medieval violence including beheadings, dismemberment, dragon attacks, battle sequences, and a notorious episode where a character's eye is cut out. The violence serves the narrative rather than existing for shock value alone.",
    "language": "MODERATE. Period-appropriate profanity. Less modern-sounding than Game of Thrones.",
    "substanceUse": "MODERATE. Wine drinking consistent with medieval court life. Not glamorized.",
    "matureThemes": "Succession and civil war, the burden of rule, dynastic loyalty and betrayal, the cost of ambition, gender and inheritance law, the corruption of power, arranged marriage as political tool, maternal mortality, bodily autonomy in a medieval context."
  },
  "fidelityCasting": {
    "raceSwaps": 1,
    "genderSwaps": 0,
    "orientationChanges": 0,
    "notes": "Steve Toussaint as Corlys Velaryon is a race-blind casting choice. In Martin's source material, the Velaryons are described as pale-skinned with silver hair (like the Targaryens). The show treats this change as narratively irrelevant and never addresses it. Toussaint's performance is excellent and the casting does not distort the story."
  },
  "summary": {
    "overall": "House of the Dragon faces an impossible task: follow Game of Thrones while avoiding the ideological rot that infected its predecessor in later seasons. Against all odds, it mostly succeeds. Season 1 is a smart, morally serious drama about succession, legacy, and the human cost of civil war. It is not free of progressive elements, but it handles them with a restraint that will surprise conservative viewers who have written off HBO entirely.\n\nThe series adapts George R.R. Martin's Fire and Blood, a faux-historical chronicle of the Targaryen civil war known as the Dance of the Dragons. Season 1 spans roughly 25 years, from the reign of the Old King Jaehaerys to the death of King Viserys I (Paddy Considine) and the crowning of Aegon II. At the center is the question that drives the entire season: when a king names his daughter as heir but later fathers sons, what happens when he dies?\n\nViserys names Rhaenyra (played by Milly Alcock as a teenager and Emma D'Arcy as an adult) as his heir after the death of his wife and infant son. The lords of Westeros swear fealty. But when Viserys remarries Alicent Hightower (Emily Carey/Olivia Cooke) and she bears him sons, the succession crisis becomes inevitable. The Greens (Alicent's faction) argue that Aegon, as first-born son, is the rightful heir by every law and tradition of Westeros. The Blacks (Rhaenyra's faction) argue that the king's decree and the lords' oaths supersede custom. Both sides have a point. That is what makes this compelling television instead of a sermon.\n\nThe show's greatest strength is its refusal to pick an ideological side. Rhaenyra is not a girlboss. She is impulsive, politically naive, and makes catastrophic mistakes (having three obvious bastards and insisting they are legitimate heirs is not the move of a master strategist). Her claim is rooted in Viserys's love for his daughter, not in any abstract principle about gender equality. The show never pretends that Westeros is a meritocracy or that the patriarchy is the villain. The patriarchy is simply the world these characters inhabit, and the drama comes from how they navigate it.\n\nThe Greens, for their part, are not the villains the title might suggest. Alicent is arguably the season's most sympathetic character: a dutiful daughter forced into marriage with an aging king, who endures years of obligation and finds meaning in her children and her faith. When she believes Viserys's dying words name Aegon as heir, she acts on genuine conviction, not malice. Otto Hightower (Rhys Ifans) is ambitious but not evil. He genuinely believes Aegon is the lawful heir and that Rhaenyra's ascension would mean civil war. He is right about the civil war part. Aemond, the season's ostensible antagonist, is a bullied child who loses an eye and grows into something dangerous and understandable.\n\nPaddy Considine's King Viserys is the performance that elevates the entire season. He plays a good man who is not a good king, a loving father whose love creates the catastrophe he spent his reign trying to prevent. Episode 8, where the dying Viserys makes one final walk to the throne to defend his daughter's claim, is some of the best television HBO has ever produced. Viserys is a principled patriarch in the truest sense: a man who holds his family together through sheer decency, and whose death releases the chaos he contained. The show respects him, and by extension respects the ideal of patriarchal authority exercised with love and duty.\n\nThe gender dynamics deserve serious attention because they are the axis on which the entire show turns. House of the Dragon is about whether a woman can inherit a throne in a patriarchal society. The smartest thing the show does is refuse to answer that question as a political argument. It treats it as a dramatic question. Rhaenyra's gender is a plot complication, not a thesis statement. The suffering of women in this world (childbirth, arranged marriage, lack of legal personhood) is presented as tragic reality, not as evidence for an indictment of the audience. Compare this to later seasons of Game of Thrones, where every female character became a quippy girlboss delivering anachronistic lectures about smashing the patriarchy. House of the Dragon has learned from that mistake. Its women suffer and scheme and triumph and fail within the world they inhabit, not in defiance of it.\n\nThe race-blind casting of Steve Toussaint as Corlys Velaryon, the Sea Snake, is the one production choice that reads as a concession to modern sensibilities. In Martin's source material, the Velaryons are pale-skinned Valyrian stock. The show cast a Black actor and never addresses the change. Toussaint is excellent, bringing natural gravitas and wounded pride to the role. His race is irrelevant to the story the show tells. Conservative viewers who objected to this casting choice missed the point: it is a cosmetic decision that affects nothing about the narrative.\n\nThe show's weaknesses are real. The ten-year time jump between episodes 5 and 6 is jarring, requiring recasting of Rhaenyra and Alicent mid-season. Losing Milly Alcock and Emily Carey, both excellent, disrupts emotional continuity. Emma D'Arcy and Olivia Cooke are strong in their own right, but the adjustment period costs the show momentum. The pacing in the middle episodes drags as the show shuffles pieces for the war to come. And the season ends on a cliffhanger (Lucerys's death at the hands of Aemond and Vhagar) that is effective as tragedy but frustrating as a season finale. The real story is just beginning when the credits roll.\n\nThe show also shares Game of Thrones's discomfort with overt religiosity. The Faith of the Seven is depicted as a political institution rather than a genuine spiritual force, and Alicent's faith (expressed through prayer and the Seven-Pointed Star) is treated with a slightly anthropological distance rather than genuine respect. This is HBO's house style, not a specific ideological attack, but it is worth noting for viewers who care about how faith is portrayed.\n\nOn balance, House of the Dragon Season 1 earns a TRADITIONAL verdict by a narrow but clear margin. The show's strengths are traditional: it takes duty seriously, respects legitimate authority, portrays flawed but sympathetic patriarchs, and treats civil war as tragedy rather than revolution. Its progressive elements are present but restrained. Rhaenyra is a flawed claimant, not a feminist hero. The Greens have legitimate arguments rooted in law and tradition. The smallfolk suffer no matter which dragon wins.\n\nThis is not Game of Thrones Season 8. It is something better: a show that remembers that moral complexity does not mean moral confusion, and that the best drama comes from characters who believe in something, even when those beliefs collide.",
    "quickTake": "Surprisingly restrained. A succession drama that respects both sides. No girlboss sermonizing. Viserys is a career-best Paddy Considine.",
    "recommendation": "Watch it. Conservative viewers will find more to respect here than they expect.",
    "bestFor": "Game of Thrones fans burned by Season 8. Viewers who want morally serious fantasy without ideological preaching.",
    "skipIf": "You cannot tolerate the TV-MA content (graphic violence, sex, childbirth). Or if any race-blind casting is a dealbreaker.",
    "highlights": ["Paddy Considine's King Viserys: a principled patriarch whose decency cannot prevent catastrophe", "Both sides of the succession conflict get fair, nuanced treatment", "Rhaenyra is flawed, not a girlboss; the Greens have legitimate arguments", "Episode 8: one of HBO's finest hours", "Learned from Game of Thrones' mistakes with gender dynamics"],
    "lowlights": ["The mid-season time jump and recasting disrupts emotional continuity", "Middle episodes sag as pieces are shuffled for war", "Anti-climactic season finale: the real story is just beginning", "HBO's default discomfort with genuine religiosity"]
  },
  "seo": {
    "titleTag": "Is House of the Dragon (S1) Woke? Review | VirtueVigil",
    "metaDescription": "VirtueVigil's full VVWS review of House of the Dragon Season 1 (2022). A succession drama with surprising restraint. Verdict: TRADITIONAL. Trope scores, parental guidance included.",
    "keywords": "is House of the Dragon woke, HOTD review, House of the Dragon VirtueVigil, HOTD parents guide, House of the Dragon traditional"
  },
  "tropeAudit": [
    {
      "id": "TRADITIONAL-029",
      "name": "Principled Patriarch",
      "category": "Traditional",
      "severity": 3,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 3.78,
      "description": "King Viserys I is the Principled Patriarch in its purest form: a good man who rules through decency and love rather than fear. His fatal flaw is an excess of the patriarchal virtues (he loves his daughter too much, he trusts his council too readily, he wants peace too badly). Considine's performance is a career-best. The show treats Viserys with genuine respect rather than ironic distance."
    },
    {
      "id": "TRADITIONAL-038",
      "name": "Reluctant Leader",
      "category": "Traditional",
      "severity": 2,
      "authenticity": "High",
      "centrality": "Moderate",
      "weightedScore": 1.4,
      "description": "Rhaenyra does not initially seek the throne. She accepts the burden out of duty to her father. Her claim is not about ambition or ideology but about honoring Viserys's wishes. The show frames the crown as a burden, not a prize, and Rhaenyra's reluctance gives her claim moral weight."
    },
    {
      "id": "TRADITIONAL-039",
      "name": "Objective Good vs. Evil",
      "category": "Traditional",
      "severity": 1,
      "authenticity": "Moderate",
      "centrality": "Low",
      "weightedScore": 0.5,
      "description": "The moral framework is more ambiguous than Tolkien but still exists. Cruelty (Aemond's bullying, Daemon's brutality) is presented as wrong. Loyalty and honor are presented as virtues. The show does not descend into nihilism or moral equivalence. Evil acts have evil consequences."
    },
    {
      "id": "TRADITIONAL-046",
      "name": "Heritage over Innovation",
      "category": "Traditional",
      "severity": 2,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.7,
      "description": "The Greens' argument rests on the weight of tradition: Aegon is the first-born son, and primogeniture is the foundation of Westerosi law. The show does not dismiss this argument as bigotry. It treats tradition as having genuine moral and legal force, even when it conflicts with a king's decree."
    },
    {
      "id": "TRADITIONAL-050",
      "name": "Harmony and Order",
      "category": "Traditional",
      "severity": 2,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.7,
      "description": "Viserys's entire reign is devoted to maintaining peace and order. The show treats his commitment to harmony as noble rather than naive. The tragedy is that his death unleashes chaos, proving that order must be defended, not assumed. Civil war is framed as the ultimate catastrophe."
    },
    {
      "id": "TRADITIONAL-035",
      "name": "Just Lawman",
      "category": "Traditional",
      "severity": 1,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.35,
      "description": "Harrold Westerling (Graham McTavish) as Lord Commander of the Kingsguard represents lawful authority exercised with honor. He resigns rather than participate in the Green Council's scheme. The show respects institutional loyalty when it is genuinely principled."
    },
    {
      "id": "WOKE-001",
      "name": "Woke Catch-All / Gender Succession Theme",
      "category": "Woke",
      "severity": 2,
      "authenticity": "High",
      "centrality": "High",
      "weightedScore": 2.52,
      "description": "The entire season revolves around whether a woman can inherit the throne. This is indisputably the central dramatic question. However, the show's treatment is nuanced rather than polemical. Rhaenyra is flawed, not a feminist icon. The Greens have legitimate arguments. The gender theme comes from Martin's source material (written decades ago), not from a 2022 writers' room inserting progressive messaging. High authenticity because it is organic to the narrative."
    },
    {
      "id": "WOKE-003",
      "name": "Girl Boss",
      "category": "Woke",
      "severity": 2,
      "authenticity": "Moderate",
      "centrality": "Moderate",
      "weightedScore": 2.0,
      "description": "Rhaenyra has girlboss framing in the early episodes (defiant princess who rides dragons, 'I will not be a tyrant' speech, rejecting traditional femininity). The season undercuts this steadily: by the end she is politically isolated, her bastard children are a liability, and her claim leads to her son's death. The show does not reward her with unearned victories. But the early framing is clearly meant to appeal to the 'strong female character' sensibility, and it takes half a season to fully subvert."
    },
    {
      "id": "WOKE-004",
      "name": "Institutional Evil / Monarchy's Corruption",
      "category": "Woke",
      "severity": 2,
      "authenticity": "High",
      "centrality": "Low",
      "weightedScore": 0.7,
      "description": "The monarchy and its institutions are portrayed as corrupting and ultimately self-destructive. The Small Council schemes, the Kingsguard splinters, and the realm suffers. This is standard Martin fare (all power corrupts) and a genre convention, not a woke sermon. The show does not propose progressive alternatives; it simply depicts the tragedy of flawed institutions."
    }
  ]
}

# Compute scores
woke_tropes = [t for t in hotd['tropeAudit'] if t['category'] == 'Woke']
trad_tropes = [t for t in hotd['tropeAudit'] if t['category'] == 'Traditional']
hotd['wokeScore'] = round(sum(t['weightedScore'] for t in woke_tropes), 2)
hotd['tradScore'] = round(sum(t['weightedScore'] for t in trad_tropes), 2)
margin = hotd['tradScore'] - hotd['wokeScore']
hotd['scoreMargin'] = f"+{round(margin, 1)} TRAD"

print(f"HOTD: woke={hotd['wokeScore']}, trad={hotd['tradScore']}, margin={margin}")
print(f"HOTD verdict: {hotd['verdict']}")

# Append and write
data.append(f1)
data.append(lotr)
data.append(hotd)

with open('src/data/reviews.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f'Total reviews: {len(data)}')
print('Done.')