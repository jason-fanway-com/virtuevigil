#!/usr/bin/env python3
"""Add 3 reviews: Deadpool & Wolverine, Princess Mononoke, Ted Lasso — Oct 12, 2026"""
import json, sys

with open('src/data/reviews.json') as f:
    reviews = json.load(f)

existing_slugs = {r['slug'] for r in reviews}
date_str = "2026-10-12"

# ============================================================
# REVIEW 1: Deadpool & Wolverine (2024) — New Release bucket
# wokeScore: 4.03 | tradScore: 21.60 | margin: +17.57 → TRADITIONAL
# ============================================================
dpw = {
    "id": "deadpool-and-wolverine-2024",
    "slug": "deadpool-and-wolverine-2024",
    "title": "Deadpool & Wolverine",
    "year": "2024",
    "type": "film",
    "platform": "Disney+ / Digital",
    "genre": "Superhero, Action-Comedy",
    "date": date_str,
    "datePublished": date_str,
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/deadpool-and-wolverine-2024.jpg",
    "releaseDate": "July 26, 2024",
    "rating": "R",
    "runtime": "128 min",
    "director": "Shawn Levy",
    "writers": "Ryan Reynolds, Rhett Reese, Paul Wernick, Zeb Wells, Shawn Levy",
    "showrunner": None,
    "cast": "['Ryan Reynolds', 'Hugh Jackman', 'Emma Corrin', 'Matthew Macfadyen', 'Morena Baccarin', 'Rob Delaney', 'Leslie Uggams', 'Aaron Stanford', 'Jennifer Garner']",
    "studio": "Marvel Studios, Maximum Effort, 21 Laps Entertainment",
    "distributor": "Walt Disney Studios Motion Pictures",
    "verdict": "TRADITIONAL",
    "wokeScore": "4.03",
    "tradScore": "21.60",
    "authIndex": "88",
    "scoreMargin": "+17.57 TRAD",
    "preRelease": "False",
    "wokeTrap": "False",
    "woke_trap_assessment": "Deadpool's pansexual identity and the film's self-aware meta-commentary are present from the opening scene and are established character traits carried from previous films. The TVA's bureaucratic villainy is introduced early. No woke content is concealed past the midpoint; the film's traditional core (friendship, sacrifice, redemption) dominates the entire runtime.",
    "seo": {
        "titleTag": "Is Deadpool & Wolverine (2024) Woke? Marvel's $1.3B Merc With a Mouth Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Deadpool & Wolverine (2024). Ryan Reynolds and Hugh Jackman's R-rated MCU team-up is profane, violent, and surprisingly traditional. VVWS verdict: TRADITIONAL (+17.57 TRAD). Parental guidance included.",
        "keywords": "is deadpool and wolverine woke, deadpool 3 review, deadpool wolverine virtuevigil, deadpool 2024 traditional or woke, shawn levy deadpool, deadpool wolverine parents guide, hugh jackman wolverine return"
    },
    "summary": {
        "overall": "Deadpool & Wolverine is Shawn Levy's 2024 MCU debut for the Merc with a Mouth, reuniting Ryan Reynolds' Deadpool with Hugh Jackman's Wolverine for the first time since 2009's X-Men Origins: Wolverine, and the result is a $1.3 billion phenomenon. The plot finds Wade Wilson's timeline dying after the death of its anchor being (Logan, from 2017's Logan), and Deadpool recruits a variant Wolverine, a guilt-ridden failure from another universe, to save it. The TVA's rogue operator Mr. Paradox (Matthew Macfadyen) plans to mercy-kill the timeline, and the duo must survive the Void and its ruler Cassandra Nova (Emma Corrin) to prevent it. The VVWS assessment lands at TRADITIONAL (+17.57 TRAD), and the finding will surprise people who only see the surface: beneath the relentless profanity, meta-commentary, and Deadpool's pansexual identity schtick is a movie about male friendship, self-sacrifice, and redemption that is more emotionally traditional than most PG-13 family films released this year.",
        "adultInsight": "Deadpool & Wolverine is a Rorschach test for culture-war movie criticism. If you only read the content tags, you would expect maximum wokeness: a pansexual male lead who rejects binary identity, an institutional villain (the TVA) that embodies bureaucratic heartlessness, self-aware mockery of corporate franchise machinery, and a diverse supporting cast. That is the surface reading, and it is wrong. The film's actual moral substance is the friendship between Wade and Logan, a bond forged through shared misery and mutual contempt that transforms into the kind of loyalty that would literally walk through fire for the other person. Wolverine's arc is the film's spine: a man who failed everyone he loved, who retreated into alcoholic self-pity, and who is pulled back into purpose by a motormouthed mercenary who refuses to let him quit. The scene in the Honda Odyssey where Wade and Logan trade the worst things that ever happened to them is quieter and more emotionally honest than anything in the last five MCU entries. When Logan puts on the cowl and charges into battle to save Wade's friends, the moment lands not because of nostalgia but because the film has earned the character beat: this man has chosen to be a hero again. The film mocks Marvel's corporate diversity machinery relentlessly (Deadpool literally tells the TVA to stop trying to make 'diversity' happen), yet it also embraces the Fox Marvel legacy -- Elektra, Blade, Gambit, Johnny Storm -- with genuine affection. It is a weird, sometimes incoherent, deeply profane movie whose takeaway is that the only things worth dying for are the people who choose to stand next to you when the fight comes.",
        "parentalGuidance": "Rated R for strong bloody violence and language throughout, gore, and sexual references. The film contains: near-constant graphic violence with swords, claws, guns, and explosives resulting in dismemberment, decapitation, and massive blood splatter; a fight scene set to Madonna's 'Like a Prayer' that features dozens of Deadpool variants being slaughtered in creatively gruesome ways; prolific profanity (hundreds of f-bombs, plus Deadpool's signature fourth-wall-breaking sexual commentary); crude sexual humor throughout including extended jokes about pegging, masturbation, and sexual positions; drug references (cocaine use is shown and joked about); one scene of Deadpool's flesh regenerating in graphic close-up; and a cameo montage that includes Deadpool variants such as 'Kidpool' and 'Dogpool.' The film is not appropriate for children under any circumstances. It earns its R rating in the first five minutes with a bone-crunching fight sequence that uses Logan's adamantium skeleton as a weapon. For parents of teenagers: if your older teen can handle Deadpool's specific brand of humor (which treats nothing as sacred, including sex and death), the underlying themes of friendship and redemption are genuinely positive. Recommended for adults and mature older teenagers (16+) who are already familiar with the Deadpool tone and can process the violence as comic-book stylized rather than realistic. No sexual content beyond verbal references and one brief scene of Deadpool without pants (played for comedy).",
        "whatToWatchFor": "The film earns its R rating in the opening credits: Deadpool digs up Logan's corpse from the end of Logan (2017) and uses the adamantium skeleton as a weapon, beating a squad of TVA agents to death with it to the tune of NSYNC's 'Bye Bye Bye.' This sets the tone for the next two hours. The violence is constant, creative, and extremely bloody. The fight in the Void against a small army of Deadpool variants includes a close-up of Nicepool (a Deadpool variant with a golden retriever personality) being graphically shot in the head in slow motion. The language would make a sailor blush: hundreds of f-bombs, plus Deadpool's running commentary on sexual acts, bodily functions, and the Marvel corporate org chart. Cassandra Nova's power (she can reach inside people's heads and manipulate their brains with her fingers) is viscerally disturbing in multiple scenes. A major sequence involves her killing multiple characters by reaching into their skulls. The film's emotional content includes frank discussion of suicide, failure, and self-loathing, particularly in Wolverine's backstory. The cameo cavalcade in the Void (Jennifer Garner's Elektra, Wesley Snipes' Blade, Channing Tatum's Gambit, Chris Evans' Johnny Storm) is pure fan service. For parents: the profanity and violence are surface-level; the moral content beneath them is about sacrifice, friendship, and choosing to be better. That said, the surface is a lot of surface.",
        "whatWeLove": "Hugh Jackman's return as Wolverine is the reason this movie works on a level beyond the jokes. He is not playing the same Logan from the X-Men films. This is a broken man, a Wolverine who let his entire team die and who has spent years drinking himself numb in a bar, wearing his yellow suit as a mockery of who he used to be. When Deadpool finds him, he is a shell, and Jackman plays every scene with a weariness that makes the eventual turn toward heroism genuinely moving. Ryan Reynolds has his Deadpool formula dialed to 11, but the film gives him moments of surprising sincerity: his plea to the TVA to save his friends, his confession to Logan about needing a real friend, his belief that Vanessa left him because he stopped trying to be better. These beats are not undercut by jokes. They are allowed to land, and they do. Emma Corrin's Cassandra Nova is a chilling villain who operates on a plane of detached cruelty that neither Deadpool nor Wolverine can joke their way out of. The cameos from the Fox Marvel era -- particularly Wesley Snipes returning as Blade after 20 years and Channing Tatum finally playing Gambit in a performance that is 50% accent and 50% commitment to the bit -- are the kind of legacy tributes that the MCU has struggled to deliver since Endgame. This is a movie that loves what came before it, even as it mocks everything in sight."
    },
    "tropeAudit": [
        {
            "id": "dpw-WOKE-001",
            "name": "Pansexual/Bisexual Male Lead Normalization",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.40,
            "explanation": "Deadpool's pansexuality is an established character trait carried from previous films and the comics. The film references his attraction to men and women in dialogue and visual gags (a brief fantasy sequence with shirtless Wolverine, jokes about pegging, references to male romantic partners). While played entirely for comedy rather than didactic messaging, the normalization of a non-straight male action hero is a progressive cultural marker."
        },
        {
            "id": "dpw-WOKE-002",
            "name": "Institutional Evil (TVA as Corrupt Bureaucracy)",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "explanation": "Mr. Paradox and the TVA function as bureaucratic villains who treat entire timelines and their inhabitants as disposable paperwork. The film positions institutional authority as callous, self-serving, and willing to commit mass murder in the name of efficiency. This is a standard woke institutional-critique trope, though the film uses it as plot machinery rather than political argument."
        },
        {
            "id": "dpw-WOKE-003",
            "name": "Meta-Mockery of Corporate Hollywood as Self-Awareness",
            "category": "Woke",
            "severity": 1,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.32,
            "explanation": "The film's constant fourth-wall-breaking about Marvel's corporate practices, diversity mandates, and franchise fatigue functions as progressive self-awareness. Deadpool tells the TVA not to force diversity, jokes about the MCU's decline, and mocks Disney's acquisition of Fox. This ironic distance from corporate product is a modern progressive sensibility, though the film ultimately participates in everything it mocks."
        },
        {
            "id": "dpw-WOKE-004",
            "name": "Female Villain as Ultimate Power Threat",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Moderate",
            "centrality": "Low",
            "weightedScore": 0.21,
            "explanation": "Cassandra Nova, Charles Xavier's twin sister, is the film's most powerful character, able to reach inside people's minds and kill them with a thought. This registers as a mild woke signal (female character as the apex threat in a male-dominated superhero film), but the character is not framed in gendered terms and the performance is more otherworldly creature than girlboss."
        },
        {
            "id": "dpw-TRAD-001",
            "name": "Male Friendship as Sacred Bond",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "explanation": "The film's entire emotional architecture rests on the friendship between Wade and Logan. What begins as mutual contempt grows through shared survival into genuine loyalty. The Honda Odyssey scene where they trade their traumas is the film's emotional center. By the climax, Wade is willing to die to save Logan, and Logan puts on the cowl one last time because Wade made him believe he could be a hero again. This is male friendship treated with complete sincerity beneath the jokes."
        },
        {
            "id": "dpw-TRAD-002",
            "name": "Redemption Through Sacrifice and Service",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Wolverine's arc is a redemption narrative: a man who let his entire team die finds purpose again by protecting Deadpool's friends. The film argues that failure is not final, that a man can choose to be better, and that the way back is through service to others. When Logan sacrifices himself to destroy the Time Ripper and save Wade's timeline, the moment is earned through two hours of character work that took his self-loathing seriously."
        },
        {
            "id": "dpw-TRAD-003",
            "name": "Self-Sacrifice for Loved Ones",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Both Wade and Logan are willing to die for each other and for Wade's friends by the film's climax. Wade's entire motivation is to save his timeline and the people he loves. He refuses to let the TVA kill his world, not out of principle but out of specific love for specific people. This is traditional: loyalty to your people is the highest moral obligation."
        },
        {
            "id": "dpw-TRAD-004",
            "name": "Found Family and Loyalty Under Pressure",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Wade's chosen family (Vanessa, Peter, Blind Al, Dopinder, Colossus, Negasonic Teenage Warhead, Yukio) is what he fights to protect. When the TVA offers to send him to the Sacred Timeline (the main MCU), he rejects it because his friends are in his own timeline. The film treats chosen community as worth more than cosmic importance, which is a fundamentally conservative valuation of the particular over the universal."
        },
        {
            "id": "dpw-TRAD-005",
            "name": "Legacy Nostalgia and Honoring the Past",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 2.10,
            "explanation": "The film's extended tribute to the Fox Marvel era (Elektra, Blade, Gambit, Johnny Storm, X-23) is not cheap nostalgia but genuine reverence. The resistance fighters in the Void are characters the MCU discarded, and the film treats them as heroes who deserve their moment. This honoring of the past and its legacy against corporate erasure is a traditional impulse wrapped in meta-comedy packaging."
        },
        {
            "id": "dpw-TRAD-006",
            "name": "Male Competence and Brotherhood in Action",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.60,
            "explanation": "The film's action sequences are built on male competence: Wade and Logan are highly skilled warriors who complement each other's fighting styles. The partnership in combat, where each man covers the other's weakness, is a traditional masculine cooperation trope presented without irony or deconstruction."
        }
    ]
}

# ============================================================
# REVIEW 2: Princess Mononoke (1997) — Catalog Backfill (pre-2015, IMDB Top 250, Miyazaki masterpiece)
# wokeScore: 4.90 | tradScore: 19.04 | margin: +14.14 → TRADITIONAL
# ============================================================
mononoke = {
    "id": "princess-mononoke-1997",
    "slug": "princess-mononoke-1997",
    "title": "Princess Mononoke",
    "year": "1997",
    "type": "film",
    "platform": "Max / Digital",
    "genre": "Animated, Fantasy, Adventure, Historical Epic",
    "date": date_str,
    "datePublished": date_str,
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/princess-mononoke-1997.jpg",
    "releaseDate": "July 12, 1997",
    "rating": "PG-13",
    "runtime": "133 min",
    "director": "Hayao Miyazaki",
    "writers": "Hayao Miyazaki",
    "showrunner": None,
    "cast": "['Yoji Matsuda', 'Yuriko Ishida', 'Yuko Tanaka', 'Kaoru Kobayashi', 'Billy Crudup', 'Claire Danes', 'Minnie Driver', 'Billy Bob Thornton', 'Gillian Anderson', 'Jada Pinkett Smith']",
    "studio": "Studio Ghibli",
    "distributor": "Toho (Japan), Miramax (US)",
    "verdict": "TRADITIONAL",
    "wokeScore": "4.90",
    "tradScore": "19.04",
    "authIndex": "88",
    "scoreMargin": "+14.14 TRAD",
    "preRelease": "False",
    "wokeTrap": "False",
    "woke_trap_assessment": "Environmental and anti-industrial themes are present from the opening sequence. Lady Eboshi's operation and the forest conflict are the film's central premise, established within the first 20 minutes. No woke content is concealed past the midpoint. The film's moral complexity avoids ideological capture throughout.",
    "seo": {
        "titleTag": "Is Princess Mononoke (1997) Woke? Miyazaki's Environmental Epic Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Princess Mononoke (1997). Hayao Miyazaki's animated masterpiece pits industry against nature but refuses easy answers. VVWS verdict: TRADITIONAL (+14.14 TRAD). Parental guidance included.",
        "keywords": "is princess mononoke woke, princess mononoke review, princess mononoke virtuevigil, miyazaki traditional or woke, princess mononoke 1997 parents guide, studio ghibli environmental message, hayao miyazaki princess mononoke"
    },
    "summary": {
        "overall": "Princess Mononoke is Hayao Miyazaki's 1997 animated epic set in the late Muromachi period of Japan, where a young prince named Ashitaka is cursed by a demon boar god and must journey west to find a cure for a wound that grants him supernatural strength but will eventually kill him. What he finds is Iron Town, a thriving industrial settlement led by Lady Eboshi, whose iron production is clear-cutting the ancient forest and provoking war with the animal gods. The VVWS assessment lands at TRADITIONAL (+14.14 TRAD), reflecting a film that is frequently misread as a simple environmental parable but is in fact one of the most morally complex animated films ever made. Miyazaki refuses to give either side a monopoly on virtue: Eboshi rescues lepers and former prostitutes and gives them dignified work, while the animal gods are capable of cruelty, vengeance, and self-destructive rage. The film's traditionalism lies in its rejection of simplistic morality, its reverence for the natural order, and its core argument that peace is harder than war and therefore more worth doing.",
        "adultInsight": "Princess Mononoke is often described as an environmental film, and it is, but the word does not capture what makes it great. The film's argument is not that industry is evil and nature is good. It is that human beings are part of nature, not separate from it, and that the conflict between human flourishing and natural preservation is real rather than rhetorical. Lady Eboshi is one of the most interesting characters in animation: a woman who rescued prostitutes from brothels and lepers from the streets and gave them purpose and income through iron production. She is kind, courageous, and completely unapologetic about clear-cutting the forest because her people need to eat. The wolf goddess Moro, by contrast, is magnificent and terrifying, but also cruel. She hates humans absolutely and would see them all dead if she could. San, the human girl raised by wolves, is fierce and principled but also trapped by her hatred, unable to see any path forward except war. Ashitaka's role is that of the peacemaker, a role that requires him to take wounds from both sides and offer no judgment. He sees clearly what the gods and the humans cannot: that they are all going to destroy each other unless someone breaks the cycle. The film's climax, in which the Forest Spirit is beheaded and transforms into a nightwalker that destroys everything, is a vision of what happens when balance is violated. The resolution is not a victory for either side but a restoration of the natural order, with Eboshi humbled and committed to building a better town. This is not progressive environmentalism, which tends to pit humanity against nature in a zero-sum framework. It is an older, more conservative vision of stewardship, in which human industry and natural reverence must coexist or both will perish.",
        "parentalGuidance": "Rated PG-13 for images of violence and gore. The film contains: frequent battles involving arrows, swords, and guns that result in visible wounds and deaths; a boar god transformed into a demon whose body is covered in writhing, worm-like tendrils and who dies in gruesome fashion; a sequence where Ashitaka's cursed arm shoots an arrow that decapitates a samurai; wolves and boars that speak and are shown dying in battle; the Forest Spirit's death and the subsequent destruction is intense and may be frightening to younger children. The film's thematic content deals with hatred, vengeance, and the possibility of peace in a world of intractable conflict. Younger children (under 10) may find the demon imagery and battle violence overwhelming. The film is suitable for mature pre-teens and teenagers, particularly as a starting point for discussions about environmental stewardship, moral complexity, and the costs of conflict. There is no sexual content. The English dub (with Billy Crudup, Claire Danes, Minnie Driver) is excellent and accessible for younger viewers who cannot read subtitles.",
        "whatToWatchFor": "The film is rated PG-13 for images of violence and gore, and parents should take this rating seriously. The opening sequence features a demon boar whose body is covered in thrashing black tendrils, a genuinely horrifying image for young viewers. Ashitaka's cursed arm gives him supernatural archery power, and one early shot shows a samurai's arms being severed by a single arrow. The battle between Iron Town and the animal gods features casualties on both sides, including wolves and boars shown dying with visible wounds. The Forest Spirit's transformation into the nightwalker (a massive, oozing, blind giant that kills everything it touches) is one of the most viscerally intense sequences in animation history. The film discusses themes of hatred, vengeance, and the cycle of violence with unusual seriousness. Lady Eboshi's backstory involves rescuing women from brothels (mentioned, not shown). The wolf goddess Moro speaks of humans with open contempt and hatred. Recommended for ages 12 and up, with parental pre-screening for sensitive younger viewers.",
        "whatWeLove": "Joe Hisaishi's score is one of the great film compositions of the 1990s, a sweeping orchestral work that captures the grandeur of the ancient forest and the tragedy of its destruction. The animation, all hand-drawn before Studio Ghibli transitioned to digital, has a tactile weight and beauty that no CGI has ever matched. The forest sequences, with the kodama (tree spirits) clicking their heads and the Forest Spirit walking on water that blooms into life and dies beneath its feet, are transcendent. Miyazaki's refusal to give either side easy moral victory is the film's deepest strength. Lady Eboshi is not a villain but a tragic figure whose industry is both necessary and destructive. San is not a hero but a wounded creature of pure rage. Only Ashitaka, the outsider who sees with unclouded eyes, can navigate between them, and the film treats his peacemaking not as a triumph but as a continual, costly act of will. The English-language voice cast, assembled by Neil Gaiman for Miramax's 1999 release, is unusually strong: Billy Crudup's Ashitaka is gentle and resolute, Minnie Driver's Lady Eboshi is regal and complicated, and Gillian Anderson's Moro is haunting. This is the film that broke Studio Ghibli into the American market, and it remains arguably Miyazaki's masterpiece."
    },
    "tropeAudit": [
        {
            "id": "mononoke-WOKE-001",
            "name": "Environmental and Industrial Critique",
            "category": "Woke",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 2.10,
            "explanation": "The film's central conflict is between Iron Town's industrial expansion and the ancient forest. Eboshi's iron production poisons the land and enrages the animal gods. While the film could function as a progressive environmental parable, it complicates this reading by making Eboshi's industry genuinely beneficial to the marginalized humans who depend on it. The critique is present but never simplistic or propagandistic."
        },
        {
            "id": "mononoke-WOKE-002",
            "name": "Female Leader Subverting Traditional Hierarchy",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.40,
            "explanation": "Lady Eboshi runs Iron Town as an absolute authority, having rescued women from brothels and given them industrial work (operating the bellows) that makes them central to the town's economy. Men are laborers and soldiers, but the women run the core operation. This inverts feudal Japanese gender hierarchy, though the film treats it as practical rather than ideological."
        },
        {
            "id": "mononoke-WOKE-003",
            "name": "Man-Made Destruction of the Natural World",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.40,
            "explanation": "The film's climax shows humanity's ambition (Eboshi beheading the Forest Spirit) triggering apocalyptic destruction. The nightwalker's rampage is a direct consequence of human greed and disrespect for the natural order. This aligns with progressive environmental messaging about human-caused ecological catastrophe, though the film's resolution (Eboshi surviving and committing to do better) softens the condemnation."
        },
        {
            "id": "mononoke-TRAD-001",
            "name": "Moral Complexity and Rejection of Simple Ideology",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The film's deepest traditional commitment is its refusal to assign moral purity to either side. The animal gods are vengeful and capable of evil. Iron Town's industry is both destructive and life-giving. Ashitaka's mission is not to pick a side but to see clearly and make peace. This rejection of ideological simplicity in favor of seeing the world as it actually is -- messy, tragic, inhabited by flawed beings on all sides -- is a fundamentally conservative disposition."
        },
        {
            "id": "mononoke-TRAD-002",
            "name": "Male Hero as Mediator and Peacemaker",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "Ashitaka is a traditional masculine hero: competent with a bow, willing to take wounds, and committed to protecting the innocent regardless of which side they belong to. His defining act is to stand between San and Eboshi and declare that both are worth saving. He is not a warrior seeking glory but a peacemaker willing to pay the price of peace with his own body. This is a classical vision of masculine virtue."
        },
        {
            "id": "mononoke-TRAD-003",
            "name": "Reverence for the Natural and Spiritual Order",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "The forest is not merely an ecosystem but a spiritual domain inhabited by gods who demand respect. The Forest Spirit is an ancient being whose death nearly destroys the world. The kodama, the animal gods, and the ancient cedars are treated with genuine reverence. This is not secular environmentalism but something closer to animist spirituality: the world is sacred, and violating it has cosmic consequences."
        },
        {
            "id": "mononoke-TRAD-004",
            "name": "Self-Sacrifice for the Common Good",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Ashitaka's curse is a death sentence that he could potentially escape by staying in his village and waiting. Instead, he journeys into danger to understand the source of the corruption. He takes wounds meant for others multiple times. His final act is to help return the Forest Spirit's head, knowing it may cost him his life. The film treats sacrifice for peace and for others as the highest moral act."
        },
        {
            "id": "mononoke-TRAD-005",
            "name": "Industry and Perseverance as Human Virtues",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.40,
            "explanation": "Lady Eboshi's Iron Town is, despite its environmental cost, a testament to human industry and ingenuity. The women who work the bellows take pride in their labor. The lepers who craft the guns are given dignity through work. The film never condemns human striving or industrial achievement. It argues instead that industry must be responsible to the natural order, which is a traditional rather than progressive position."
        }
    ]
}

# ============================================================
# REVIEW 3: Ted Lasso (2020) — TV/Series bucket
# wokeScore: 8.38 | tradScore: 21.56 | margin: +13.18 → TRADITIONAL LEAN
# ============================================================
ted_lasso = {
    "id": "ted-lasso-2020",
    "slug": "ted-lasso-2020",
    "title": "Ted Lasso",
    "year": "2020",
    "type": "series",
    "platform": "Apple TV+",
    "genre": "Sports Comedy-Drama",
    "date": date_str,
    "datePublished": date_str,
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/ted-lasso-2020.jpg",
    "releaseDate": "August 14, 2020",
    "rating": "TV-MA",
    "runtime": "4 seasons, 44 episodes",
    "director": "None",
    "writers": "None",
    "showrunner": "Jason Sudeikis, Bill Lawrence, Brendan Hunt, Joe Kelly",
    "cast": "['Jason Sudeikis', 'Hannah Waddingham', 'Brett Goldstein', 'Juno Temple', 'Brendan Hunt', 'Nick Mohammed', 'Jeremy Swift', 'Phil Dunster', 'Toheeb Jimoh', 'Sarah Niles']",
    "studio": "Ruby's Tuna Inc., Doozer, Universal Television, Warner Bros. Television",
    "distributor": "Apple TV+",
    "verdict": "TRADITIONAL",
    "wokeScore": "8.48",
    "tradScore": "21.56",
    "authIndex": "88",
    "scoreMargin": "+13.08 TRAD",
    "preRelease": "False",
    "wokeTrap": "False",
    "woke_trap_assessment": "The show's progressive elements (therapy-positive messaging, diverse casting, LGBTQ+ storylines, women's soccer subplot, corporate DEI themes) are distributed throughout all four seasons from the pilot onward. No woke content is concealed past the midpoint; the show's inclusive framing is part of its identity from episode one. The traditional values it teaches are also present throughout, creating an unusual hybrid rather than a hidden agenda.",
    "seo": {
        "titleTag": "Is Ted Lasso (2020) Woke? Apple's Feel-Good Soccer Comedy Reviewed | VirtueVigil",
        "metaDescription": "VirtueVigil's full VVWS review of Ted Lasso (2020). Jason Sudeikis' Apple TV+ comedy wears progressive packaging but teaches traditional values. VVWS verdict: TRADITIONAL (+13.08 TRAD). Parental guidance included.",
        "keywords": "is ted lasso woke, ted lasso review, ted lasso virtuevigil, ted lasso traditional or woke, jason sudeikis ted lasso, ted lasso parents guide, apple tv ted lasso, afc richmond"
    },
    "summary": {
        "overall": "Ted Lasso is Jason Sudeikis' Apple TV+ sports comedy-drama about a relentlessly optimistic American college football coach hired to manage a struggling Premier League soccer team despite knowing nothing about the sport. Running four seasons from 2020 to 2026, the show follows Ted Lasso's improbable success at A.F.C. Richmond, not through tactical genius but through a philosophy of kindness, forgiveness, and belief in people that gradually transforms everyone around him. The VVWS assessment lands at TRADITIONAL (+13.08 TRAD), reflecting a show that wears progressive Hollywood's costume (diverse casting, therapy-positive messaging, LGBTQ+ characters, corporate feminism) while teaching fundamentally traditional values at its core: that loyalty is sacred, that forgiveness is stronger than revenge, that men should be emotionally available but also accountable, and that community built through shared purpose is the highest good.",
        "adultInsight": "Ted Lasso is the Trojan horse of traditional values in the streaming era. On the surface, it checks every progressive box: the cast is racially diverse, the female characters run businesses and sports teams, multiple episodes deal with mental health and therapy, characters come out as gay with full narrative support, and Season 3 introduces a women's soccer team subplot that addresses gender equity in sports. If you described the show's demographic representation to someone who had not seen it, they would assume it was a sermon. But the show's actual moral engine is profoundly traditional. Ted's relentless optimism is not naivete but a conscious philosophical choice: he believes that people are capable of becoming better versions of themselves, and he extends that belief to everyone, including those who have wronged him. The show's central arcs are about forgiveness (Rebecca's sabotage is discovered and forgiven; Nate's betrayal is met with grace and a path back; Jamie Tartt's toxic arrogance is transformed through mentorship and accountability). The male relationships in the show (Ted and Coach Beard, Roy and Jamie, the team as a whole) are built on loyalty, honesty, and care, with no ironic distance or deconstruction. Roy Kent's arc from rage-fueled former star to vulnerable mentor to Jamie Tartt is one of the best depictions of masculine growth on television. The show takes marriage seriously. The show takes fatherhood seriously, and Ted's relationship with his son is the emotional spine of the entire series. This is a show that teaches that being a good man means showing up, being kind, and taking responsibility for the people in your care. That is not a progressive message. It is the oldest message there is, delivered with enough charm and wit that nobody notices they are being taught it.",
        "parentalGuidance": "Rated TV-MA for language and adult themes. The show contains: frequent strong language throughout all seasons (British and American profanity is a running motif, with Roy Kent's f-bombs being a character trait); adult sexual situations and references, including casual sex, infidelity, and discussions of sexual performance (not graphically depicted); drinking and pub culture presented as normal and largely positive; emotional themes including divorce, panic attacks, childhood trauma, and parental death; a storyline involving a character coming out as gay, handled with sensitivity and tact; and storylines about mental health including therapy sessions and discussions of suicide (Season 2). The show's tone is overwhelmingly warm and optimistic despite these elements. The language makes it inappropriate for young children. The emotional content, particularly Ted's panic attacks and his processing of his father's suicide, requires a degree of maturity to process. Suitable for teenagers 14+ who can handle the language, with parental discussion around the mental health themes. The show contains no graphic violence and no nudity.",
        "whatToWatchFor": "The show is rated TV-MA primarily for language. Roy Kent alone delivers enough profanity for a Scorsese film, and the British cast members are not shy about using the full arsenal of English cursing. Parents should know that the language is the main age-gating factor and that the content is otherwise suitable for older teenagers. The Season 2 arc dealing with Ted's mental health, including on-screen therapy sessions with Dr. Sharon Fieldstone and the revelation of his father's suicide, is emotionally intense and handled with real care, but it may be triggering for viewers with similar experiences. The show features drinking and pub life as a cornerstone of British culture, presented warmly. Sexual content is limited to conversations and situations rather than depictions. The show's treatment of LGBTQ+ characters (Colin's coming out in Season 3) is integrated naturally rather than presented as teachable moments. The corporate feminist messaging in the Keeley/Rebecca storylines in Season 3 can feel didactic but is ultimately harmless. For parents: the show teaches kindness, resilience, accountability, and the value of community. The profanity is a surface feature, not a moral one.",
        "whatWeLove": "Jason Sudeikis' performance as Ted Lasso is the kind of thing that sounds impossible on paper (a relentlessly optimistic, folksy American who wins over cynical Brits through sheer force of decency) and works entirely because Sudeikis commits to it without a shred of irony. He never winks at the audience, never undercuts the character with a knowing smirk. Ted's optimism is the point, and the show treats it as a legitimate worldview rather than a punchline. Hannah Waddingham's Rebecca Welton is a commanding presence whose arc from vengeful ex-wife to genuine leader is one of the best character journeys in modern television. Brett Goldstein's Roy Kent is a creation of pure joy: a man who expresses every emotion through variations of rage, whose tenderness is always just beneath the surface, and whose mentorship of Jamie Tartt becomes the show's most rewarding relationship. Nick Mohammed's Nate Shelley undergoes the series' most radical transformation from kit man to antagonist to prodigal son, and the show earns every beat of it. The writing room understands that kindness is not weakness, that forgiveness is not passivity, and that a show about people being good to each other does not have to be boring. In an era of prestige television that equates darkness with depth, Ted Lasso is a quiet argument that light is just as hard to do well, and just as worth doing."
    },
    "tropeAudit": [
        {
            "id": "tedlasso-WOKE-001",
            "name": "Therapy and Mental Health as Central Framework",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "Season 2 makes Ted's mental health (his panic attacks, his repressed trauma from his father's suicide, his work with therapist Dr. Sharon Fieldstone) the emotional center of the show. The therapeutic frame is presented positively and is central to Ted's character development. While the show handles this material with sensitivity rather than ideology, the 'therapy is necessary and good for men' message is a progressive cultural signifier."
        },
        {
            "id": "tedlasso-WOKE-002",
            "name": "Corporate Feminist and Women's Empowerment Subplots",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.40,
            "explanation": "Rebecca's arc involves taking control of the team from her ex-husband and becoming a powerful female owner. Keeley Jones starts her own PR firm. Season 3 introduces a women's soccer team at Richmond with explicit messaging about gender equity in sports. These subplots carry progressive framing about female empowerment in male-dominated spaces, though the show treats them as character growth rather than political argument."
        },
        {
            "id": "tedlasso-WOKE-003",
            "name": "LGBTQ+ Normalization",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.95,
            "explanation": "Colin Hughes' coming-out arc in Season 3 is handled with genuine sensitivity but is a peripheral storyline. Keeley's exploration of bisexuality is referenced but not central. The show includes LGBTQ+ content as part of its inclusive worldview, which registers as woke signaling, but it never becomes the primary narrative focus and is integrated naturally rather than didactically."
        },
        {
            "id": "tedlasso-WOKE-004",
            "name": "Anti-Racism Corporate Protest Subplot",
            "category": "Woke",
            "severity": 3,
            "authenticity": "High",
            "centrality": "Low",
            "weightedScore": 0.95,
            "explanation": "Season 2 features an arc where Sam Obisanya protests the team's sponsorship by Dubai Air, which is linked to environmental destruction and corruption in his native Nigeria. The arc functions as a progressive corporate accountability storyline, but it is resolved within a few episodes and is not central to the show's ongoing narrative."
        },
        {
            "id": "tedlasso-WOKE-005",
            "name": "Anti-Toxic Masculinity Messaging",
            "category": "Woke",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.40,
            "explanation": "The show explicitly critiques traditional masculine stoicism and aggression through character arcs (Jamie Tartt's toxic bravado, Roy Kent's emotional repression, the team's bullying of Nate). Men who express vulnerability, cry, go to therapy, and support each other emotionally are rewarded. This 'emotionally available masculinity' framing is popular in progressive cultural messaging."
        },
        {
            "id": "tedlasso-TRAD-001",
            "name": "Optimism and Kindness as Genuine Moral Strength",
            "category": "Traditional",
            "severity": 5,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 6.30,
            "explanation": "Ted Lasso's defining character trait is his belief that kindness, patience, and optimism are not weaknesses but the most effective ways to lead and live. The show treats this not as a joke or a character flaw to be overcome but as a genuine philosophical position. Ted's optimism is tested (Season 2's mental health crisis, Season 3's challenges to his worldview) but never discarded. The show argues that being good is hard work and that it is worth doing."
        },
        {
            "id": "tedlasso-TRAD-002",
            "name": "Male Mentorship, Fatherhood, and Accountability",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The show's most rewarding relationships are between men who hold each other accountable. Ted's mentorship of the entire team is built on setting standards of behavior and enforcing them. Roy Kent's evolution into Jamie Tartt's mentor (after being his antagonist) is a masterclass in masculine growth: the older man takes responsibility for the younger one, teaches him to be better, and is himself changed by the process. Ted's relationship with his son is the emotional anchor of the series. The show takes fatherhood seriously as a moral obligation."
        },
        {
            "id": "tedlasso-TRAD-003",
            "name": "Forgiveness and Redemption as Central Values",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 5.04,
            "explanation": "The show's narrative engine is forgiveness. Rebecca spends Season 1 trying to destroy the team as revenge against her ex-husband and is forgiven when Ted discovers her betrayal. Nate betrays Ted in Season 2 and spends Season 3 earning his way back through genuine remorse and changed behavior. Jamie Tartt transforms from a bullying narcissist into a team player who earns the respect of those he once tormented. The show treats forgiveness as a process that requires the offender to change and the offended to extend grace. This is a deeply traditional, even Christian, moral framework."
        },
        {
            "id": "tedlasso-TRAD-004",
            "name": "Loyalty and Brotherhood as Sacred Bonds",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.78,
            "explanation": "The team's identity is built on loyalty to each other. Ted and Coach Beard's friendship is unbreakable. The Richmond players form a genuine brotherhood that transcends individual talent or ego. The show treats the bonds between teammates as sacred, and betrayal of the group (Nate's defection to West Ham, Jamie's early selfishness) as the gravest sin. This is a fundamentally traditional vision of male community."
        },
        {
            "id": "tedlasso-TRAD-005",
            "name": "Marriage, Commitment, and Family as Aspirational",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "High",
            "centrality": "Moderate",
            "weightedScore": 1.40,
            "explanation": "While the show depicts divorce (Ted's marriage ends, Rebecca's does as well), it treats committed relationships and family bonds as aspirational goods. Ted's devotion to his son is the show's moral center. Roy and Keeley's relationship is treated with genuine investment. The show never mocks or deconstructs marriage as an institution; it treats failed relationships as genuine losses and successful ones as worth fighting for."
        }
    ]
}

# Validate and write
for review in [dpw, mononoke, ted_lasso]:
    slug = review['slug']
    if slug in existing_slugs:
        print(f"ERROR: {slug} already exists!")
        sys.exit(1)
    reviews.append(review)
    existing_slugs.add(slug)
    
    # Score verification
    woke = round(sum(t['weightedScore'] for t in review['tropeAudit'] if t['category'] == 'Woke'), 2)
    trad = round(sum(t['weightedScore'] for t in review['tropeAudit'] if t['category'] == 'Traditional'), 2)
    margin = round(trad - woke, 2)
    print(f"OK: {slug}")
    print(f"   wokeScore: {woke} | tradScore: {trad} | margin: +{margin} TRAD" if margin > 0 else f"   wokeScore: {woke} | tradScore: {trad} | margin: {margin}")

with open('src/data/reviews.json', 'w') as f:
    json.dump(reviews, f, indent=2)

print(f"\nTotal reviews: {len(reviews)}")