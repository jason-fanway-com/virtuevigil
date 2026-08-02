#!/usr/bin/env python3
"""Add 3 reviews for 2026-08-02: Taxi Driver, The Deer Hunter, Chinatown."""

import json

with open("src/data/reviews.json", "r") as f:
    reviews = json.load(f)

existing_slugs = {r["slug"] for r in reviews}
print(f"Current count: {len(reviews)}")
print(f"Existing slugs check: taxi-driver-1976={'taxi-driver-1976' in existing_slugs}, deer-hunter-1978={'the-deer-hunter-1978' in existing_slugs}, chinatown-1974={'chinatown-1974' in existing_slugs}")

new_reviews = [
    {
        "id": "taxi-driver-1976",
        "slug": "taxi-driver-1976",
        "title": "Taxi Driver",
        "year": 1976,
        "type": "film",
        "platform": "Various / Peacock / Criterion Channel",
        "genre": "Crime / Drama / Psychological Thriller",
        "date": "2026-08-02",
        "datePublished": "2026-08-02",
        "author": "VirtueVigil Editorial Team",
        "readTime": "13 min",
        "poster": "/images/posters/taxi-driver-1976.jpg",
        "releaseDate": "1976-02-08",
        "rating": "R",
        "runtime": "113 min",
        "director": "Martin Scorsese",
        "writers": ["Paul Schrader"],
        "cast": [
            {"name": "Robert De Niro", "role": "Travis Bickle"},
            {"name": "Jodie Foster", "role": "Iris Steensma"},
            {"name": "Cybill Shepherd", "role": "Betsy"},
            {"name": "Harvey Keitel", "role": "Sport (Matthew)"},
            {"name": "Albert Brooks", "role": "Tom"},
            {"name": "Peter Boyle", "role": "Wizard"},
            {"name": "Leonard Harris", "role": "Senator Charles Palantine"}
        ],
        "studio": "Bill/Phillips Productions",
        "distributor": "Columbia Pictures",
        "verdict": "MIXED",
        "wokeScore": 12.6,
        "tradScore": 11.9,
        "authIndex": 52,
        "scoreMargin": "-1 WOKE",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": {
            "is_trap": False,
            "explanation": "Taxi Driver does not qualify as a woke trap. The film's cynical worldview and institutional critique are present from the opening frame, not concealed beneath accessible packaging. Travis Bickle's instability is on display immediately; the film announces itself as a portrait of a disturbed man in a decaying city and delivers exactly that. The margin is barely negative, and the woke content is not strategically hidden to lure in traditional audiences. No trap conditions are met."
        },
        "seoTitle": "Is Taxi Driver (1976) Woke? Scorsese's Classic Reviewed | VirtueVigil",
        "seoDescription": "VirtueVigil's full VVWS v1.1 review of Taxi Driver (1976). We score every trope, analyze the creative team ideology, and answer: is Scorsese's vigilante classic woke or traditional? Verdict: MIXED.",
        "seoKeywords": [
            "is Taxi Driver woke",
            "Taxi Driver 1976 review",
            "Taxi Driver conservative review",
            "Travis Bickle analysis",
            "Scorsese woke or traditional",
            "Taxi Driver VirtueVigil score",
            "is Taxi Driver appropriate for kids",
            "Taxi Driver MPAA rating parents",
            "Paul Schrader ideology",
            "Taxi Driver traditional values",
            "Robert De Niro Taxi Driver",
            "Jodie Foster Taxi Driver review",
            "vigilante film traditional values",
            "1970s New York film review",
            "Taxi Driver Criterion review"
        ],
        "externalScores": {
            "rottenTomatoesCritic": 99,
            "rottenTomatoesAudience": 95,
            "imdb": 8.2,
            "metacritic": 94,
            "oscarNominations": 4,
            "oscarCategories": "Best Picture, Best Director, Best Supporting Actress (Jodie Foster), Best Original Score",
            "budget": "$1.3 million",
            "globalBoxOffice": "$28.3 million (1976)"
        },
        "creative_team": {
            "director": {
                "name": "Martin Scorsese",
                "ideology": "WOKE LEANING. Scorsese's public record is consistently progressive. His charitable and civic affiliations align with the American cultural left. His filmography contains both ideologically charged work and apolitical genre craft. Taxi Driver falls between: it is not a political screed, but it is made by a filmmaker who reads mid-70s New York's collapse as a structural critique of American society rather than a series of individual moral failures.",
                "profile": "Martin Scorsese was born in New York City's Little Italy in 1942 and has spent his career making films about the city that formed him. Taxi Driver was shot in 1975 when New York was genuinely in crisis: near municipal bankruptcy, violent crime rates spiking, 42nd Street a theater district turned open-air sex market. Scorsese filmed on location, capturing actual streets rather than studio approximations. His visual approach, saturated reds and ambers, slow-motion crowd shots, steam rising from manholes like hellfire, turns New York into a moral landscape. Travis Bickle does not just live in a decaying city; he inhabits a city that has externalized his interior state. Scorsese went on to make Raging Bull, Goodfellas, Casino, Gangs of New York, The Departed, The Irishman, and Killers of the Flower Moon among many others. His career breadth is extraordinary. Taxi Driver remains his most concentrated character study."
            },
            "writers": {
                "names": "Paul Schrader",
                "profile": "Paul Schrader wrote Taxi Driver in 1971 during a period of personal crisis: thrown out of his Christian Reformed household for attending movies, his marriage failing, sleeping in his car in Los Angeles. He said later he barely remembers writing the script and finished it in two weeks. The autobiographical dimension is essential: Travis Bickle is not a political manifesto but a psychological portrait, and the psychology is Schrader's own alienation projected onto a Vietnam veteran's body. Schrader was born in Grand Rapids, Michigan in 1946 into a strict Calvinist household that banned movies entirely; he did not see a film until age 17. He went on to write Raging Bull, The Last Temptation of Christ, and Bringing Out the Dead for Scorsese, and directed American Gigolo, Affliction, and First Reformed. His films circle obsessively around isolation, guilt, and men who cannot connect with other people. Taxi Driver is the purest expression of this. Schrader's religious background gives his work a moral seriousness that distinguishes it from ordinary liberal filmmaking; his films are not political arguments but spiritual crises."
            },
            "lead_producer": {
                "name": "Michael Phillips / Julia Phillips",
                "company": "Bill/Phillips Productions"
            },
            "composer": {
                "name": "Bernard Herrmann",
                "profile": "Bernard Herrmann composed the Taxi Driver score in 1975, making it his final work. He died on December 24, 1975, the night he completed the recording sessions. The score is a masterwork: jazz-inflected, anxious, capable of soaring romanticism and grinding menace in the same cue. The main theme, built on a saxophone melody over a slow rhythm section, captures Travis's internal contradiction. There is something yearning and romantic in him, which makes the violence more disturbing rather than less. Herrmann had scored Citizen Kane, Vertigo, Psycho, North by Northwest, and Cape Fear. His final score for Scorsese is among his greatest achievements."
            },
            "cinematographer": {
                "name": "Michael Chapman",
                "profile": "Michael Chapman developed a visual language for Taxi Driver that turned New York's actual decay into expressionist cinema. The saturated ambers and reds flooding the nighttime sequences are not color correction effects but the actual look of Times Square in the mid-70s: neon signs, heat haze, garbage. Chapman's slow-motion wide shots treat pedestrians as phenomena rather than people, reinforcing Travis's disconnection from the humanity around him. He went on to shoot Raging Bull, The Fugitive, and Kindergarten Cop. His work on Taxi Driver remains his defining achievement."
            },
            "casting_director": {
                "name": "Juliet Taylor",
                "profile": "Juliet Taylor cast Robert De Niro, Jodie Foster, Cybill Shepherd, Harvey Keitel, and Peter Boyle in a film that would define all of their careers. The most discussed decision is Jodie Foster as the 12-year-old Iris. Foster was 13 during filming; California law required a psychological evaluation before production could proceed. Her performance is remarkable: she plays Iris not as a victim who knows she is a victim but as a girl who has rationalized her circumstances into a kind of defensive independence. Harvey Keitel as Sport plays the character without early villainy signals; he is persuasive and low-key, which makes the horror of the situation land harder."
            },
            "top_cast": [
                {"name": "Robert De Niro", "role": "Travis Bickle"},
                {"name": "Jodie Foster", "role": "Iris Steensma"},
                {"name": "Cybill Shepherd", "role": "Betsy"},
                {"name": "Harvey Keitel", "role": "Sport (Matthew)"},
                {"name": "Albert Brooks", "role": "Tom"},
                {"name": "Peter Boyle", "role": "Wizard"}
            ]
        },
        "parentalGuidance": {
            "mpaaRating": "R",
            "mpaaDescriptors": "Violence, strong language, sexual content, adult themes",
            "recommendedAge": "18+",
            "contentWarnings": [
                "Graphic gun violence in the final sequence: close-range shootings with significant bloodshed and explicit aftermath",
                "A 12-year-old character depicted as a child prostitute; no explicit sexual content shown but the situation is made explicit through dialogue",
                "Strong language throughout, including period-accurate racial slurs",
                "Depiction of psychological instability, obsession, and violent ideation",
                "A sequence depicting preparation and planning for a political assassination",
                "Brief sexual references and adult-oriented dialogue",
                "Drug use references"
            ],
            "parentalNotes": "Taxi Driver is not appropriate for anyone under 18. The film centers on a psychologically unstable man who channels violent action as a response to urban decay. His final act of violence results in the rescue of a child, but the film does not present this as a model; it presents it as an accidental positive outcome from a disturbed psychology. The child prostitution element, while not depicted explicitly, requires adult comprehension. For adults interested in American cinema history and the artistic examination of alienation, Taxi Driver is a landmark. For everyone else under 18: wait."
        },
        "fidelityCasting": {
            "assessment": "NOT APPLICABLE",
            "explanation": "Taxi Driver is an original screenplay with no prior source material. The characters are invented. Robert De Niro's casting as Travis Bickle defines the character in all subsequent cultural memory. Harvey Keitel as Sport, charismatic and soft-spoken rather than coded as a villain from frame one, is a deliberate choice that makes the situation land harder. Jodie Foster at 13 playing Iris holds up: she plays the character's defensive self-possession with a maturity that reads as adaptive psychology rather than precocity. No diversity casting or race-swapping concerns apply."
        },
        "summary": {
            "overall": "Fifty years later, Taxi Driver remains the most uncomfortable film in the American canon. Not because of the violence, which is extreme but not gratuitous. Not because of the child prostitution storyline, depicted with more restraint than Hollywood would manage today. Because of the question it refuses to answer: was Travis Bickle right?\n\nThe film's answer is something like: not exactly, but kind of, by accident. That hedged non-answer is more honest than any firm stance would be.\n\nPaul Schrader wrote the script while sleeping in his car, freshly expelled from a religious household, drowning in personal failure. Travis Bickle is what Schrader feared he was becoming: a man so alienated from normal human connection that the world had become an enemy. The Vietnam veteran framework is a period detail that also functions as permission; society gave Travis a specific reason for his damage. But the damage is recognizable without the war. It's the damage of a man who cannot reach other people and cannot stop trying.\n\nMartin Scorsese filmed on the actual streets of mid-70s New York, a city in genuine crisis. The steam rising from manholes was not art direction. The characters Travis encounters exist in a city where institutional collapse is the condition of daily life. The police cannot clean the streets. The politicians are performance. The adults who should protect Iris have either abandoned her or are exploiting her.\n\nTravis decides to act. He prepares obsessively, building a weapon rig into his arm, doing pushups, rehearsing in mirrors. The famous 'Are you talking to me?' monologue is not a moment of clarity. It's a man conducting a conversation with an imaginary enemy because he has no real one yet.\n\nThe Palantine assassination attempt fails because of luck, not virtue. What Travis does instead, in the film's blood-soaked finale, is kill Sport and his associates and retrieve Iris. He is celebrated as a hero in the press. He returns to cab driving. Betsy rides in his taxi; he drives away without speaking. The film ends before Travis can become the monster he was assembling himself to be.\n\nBernard Herrmann's final score deserves its own note. The main theme, a saxophone melody over slow rhythm section, holds Travis's internal contradiction in suspension: romantic and menacing in equal measure, like the man himself. Herrmann finished the recording sessions on December 24, 1975, and died that night.\n\nVVWS scores MIXED at a margin of -0.7. That's exactly right. The film's traditional core is powerful: a man who will not let a child be exploited, who acts when institutions fail, who pays personally for standing up. The woke architecture is also real: cities are sick, veterans are broken, institutions are hollow, and the only person who does anything is a lunatic. Both are true simultaneously. That simultaneous truth is what makes Taxi Driver great.",
            "adultInsight": "The Taxi Driver debate that matters for adult viewers is about the hero-worship problem. Schrader has spoken publicly about being troubled by the fanbase Travis Bickle attracted after the film's release. The film is very careful not to endorse Travis's worldview or his violence. His assassination attempt on Palantine fails. He succeeds with Sport only because he catches him by surprise. The heroism is accidental: he happened to direct his violence at people who deserved it, which is not a formula anyone should try to reproduce. Adult viewers engaging seriously with the film should carry away a clear distinction between the outcome Travis achieves (child rescued) and the process he used (psychotic vigilantism). The film does not provide a clean way to separate those things. That's precisely its point.",
            "parentalGuidance": "Rated R for graphic violence, strong language including period-accurate racial slurs, and a storyline centered on the sexual exploitation of a 12-year-old girl. The child is not shown explicitly, but the situation is made fully clear through dialogue. Robert De Niro's performance and the film's subject matter require adult comprehension. Not appropriate for anyone under 18."
        },
        "tropeAudit": [
            {
                "id": "WOKE-TAXI-001",
                "name": "Urban decay as systemic societal indictment",
                "category": "Woke",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "description": "The film frames New York City in 1975 as a cesspool of prostitution, drug addiction, and crime, with every institution helpless or complicit. The 'filth' Travis wants to wash away is not a random collection of bad individuals but a specific urban ecosystem that exists because systems have failed. The city's decay is not incidental; it is the film's argument about what American society allowed to happen."
            },
            {
                "id": "WOKE-TAXI-002",
                "name": "Vietnam veteran as psychologically broken",
                "category": "Woke",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "Travis Bickle is a Vietnam veteran whose combat experience left him unable to sleep, unable to connect, and ultimately willing to commit mass violence. The film presents his veteran status not as a source of discipline or competence but as the origin of his damage. His service is what broke him. This is an anti-war framing built into the character's premise."
            },
            {
                "id": "WOKE-TAXI-003",
                "name": "Nihilistic moral irony: society celebrates a disturbed man",
                "category": "Woke",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "description": "The film's ending is its most subversive moment: Travis is celebrated as a hero in the press. Iris's parents write him a thank-you letter. The city that had no use for him now lionizes him. Scorsese and Schrader frame this as an indictment of a society whose moral judgment is so broken it cannot distinguish between vigilante psychosis and heroism. The celebration is the critique."
            },
            {
                "id": "TRAD-TAXI-001",
                "name": "Lone vigilante protects child from sexual predators",
                "category": "Traditional",
                "severity": 5,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 6.3,
                "description": "Whatever else Travis Bickle is, his core motivation in the film's final act is unambiguous: rescue a 12-year-old girl from the men exploiting her for sex. The child protection imperative is not morally complicated. Sport is a pimp selling a child. Iris needs to go home. Travis acts when no institution will. The film frames this action as necessary, whatever questions it raises about the method."
            },
            {
                "id": "TRAD-TAXI-002",
                "name": "Individual moral clarity against institutional failure",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.1,
                "description": "Travis observes institutions failing: the police do not clean up the streets, politicians perform rather than govern. He concludes that individual action is required. This is traditional American frontier logic: when the law will not act, a man must. The film does not straightforwardly endorse this, but it presents it as Travis's genuine moral framework."
            },
            {
                "id": "TRAD-TAXI-003",
                "name": "Predators clearly coded as evil (no rehabilitation for Sport)",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.1,
                "description": "The film offers no rehabilitation narrative for Sport or the other men exploiting Iris. They are predators. The film does not ask the audience to understand their circumstances or consider the social forces that shaped them. They are obstacles between Iris and safety, and the film treats their removal as the plot's necessary resolution."
            },
            {
                "id": "TRAD-TAXI-004",
                "name": "Masculine self-preparation and self-reliance",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 1.4,
                "description": "Travis's preparation sequence, the pushups, the weapon modifications, the physical discipline, is presented without irony as functional self-improvement. He identifies a problem and systematically builds the capacity to address it. The film treats this preparedness as real capability, even if the psychology behind it is disturbed."
            }
        ],
        "seo": {
            "titleTag": "Is Taxi Driver (1976) Woke? Scorsese's Classic Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS v1.1 review of Taxi Driver (1976) directed by Martin Scorsese. Trope audit, creative team ideology, parental guidance. Verdict: MIXED (margin -0.7).",
            "keywords": "is Taxi Driver woke, Taxi Driver 1976 review, Travis Bickle vigilante, Scorsese traditional values, Taxi Driver conservative, is Taxi Driver appropriate, Taxi Driver rating parents, Paul Schrader ideology"
        }
    },
    {
        "id": "the-deer-hunter-1978",
        "slug": "the-deer-hunter-1978",
        "title": "The Deer Hunter",
        "year": 1978,
        "type": "film",
        "platform": "Various / Peacock / Max",
        "genre": "Drama / War",
        "date": "2026-08-02",
        "datePublished": "2026-08-02",
        "author": "VirtueVigil Editorial Team",
        "readTime": "14 min",
        "poster": "/images/posters/the-deer-hunter-1978.jpg",
        "releaseDate": "1978-12-08",
        "rating": "R",
        "runtime": "182 min",
        "director": "Michael Cimino",
        "writers": ["Deric Washburn", "Michael Cimino", "Louis Garfinkle", "Quinn K. Redeker"],
        "cast": [
            {"name": "Robert De Niro", "role": "Michael Vronsky"},
            {"name": "Christopher Walken", "role": "Nick"},
            {"name": "John Savage", "role": "Steven"},
            {"name": "Meryl Streep", "role": "Linda"},
            {"name": "John Cazale", "role": "Stan"},
            {"name": "George Dzundza", "role": "John Welsh"},
            {"name": "Chuck Aspegren", "role": "Axel"}
        ],
        "studio": "EMI Films",
        "distributor": "Universal Pictures",
        "verdict": "TRADITIONAL",
        "wokeScore": 7.14,
        "tradScore": 21.0,
        "authIndex": 74,
        "scoreMargin": "+14 TRAD",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": {
            "is_trap": False,
            "explanation": "The Deer Hunter does not qualify as a woke trap. Its margin is firmly positive and its verdict is TRADITIONAL. The film's anti-war dimension is present from its premise and does not constitute concealed ideology. The Russian roulette sequences and the damage done to the three men are not woke content hidden beneath a traditional surface; they are the honest costs the film demands its audience reckon with alongside its traditional values. A traditional film that acknowledges war's price is not a trap. It is honest."
        },
        "seoTitle": "Is The Deer Hunter (1978) Woke? Cimino's Classic Reviewed | VirtueVigil",
        "seoDescription": "VirtueVigil's full VVWS v1.1 review of The Deer Hunter (1978). We score every trope, analyze the creative team ideology, and answer: is Michael Cimino's Vietnam masterpiece woke or traditional? Verdict: TRADITIONAL.",
        "seoKeywords": [
            "is The Deer Hunter woke",
            "The Deer Hunter 1978 review",
            "The Deer Hunter conservative review",
            "Michael Cimino ideology",
            "The Deer Hunter traditional values",
            "is The Deer Hunter appropriate for kids",
            "The Deer Hunter parental guidance",
            "Robert De Niro Deer Hunter",
            "Christopher Walken Deer Hunter",
            "Meryl Streep Deer Hunter",
            "The Deer Hunter VirtueVigil score",
            "Vietnam War film traditional",
            "The Deer Hunter Oscar winner",
            "working class Americana film",
            "The Deer Hunter Russian roulette"
        ],
        "externalScores": {
            "rottenTomatoesCritic": 93,
            "rottenTomatoesAudience": 93,
            "imdb": 8.1,
            "metacritic": 94,
            "oscarNominations": 9,
            "oscarCategories": "Best Picture (WON), Best Director (WON), Best Supporting Actor Christopher Walken (WON), Best Film Editing (WON), Best Sound (WON), Best Actor De Niro, Best Supporting Actress Streep, Best Supporting Actor Cazale, Best Cinematography",
            "budget": "$15 million",
            "globalBoxOffice": "$49.1 million (1978-1979)"
        },
        "creative_team": {
            "director": {
                "name": "Michael Cimino",
                "ideology": "MIXED. Cimino's career defies clean ideological classification. The Deer Hunter is a film of deep patriotic feeling that also grapples honestly with what the war cost American men. Cimino's follow-up, Heaven's Gate (1980), is explicitly a revisionist Western that casts immigrant laborers as heroes against corrupt capitalist landowners, a markedly progressive ideological frame. The gap between these two films represents a genuine ambiguity in Cimino's politics. The Deer Hunter does not read as a director with an agenda; it reads as a director who loved these characters and their world.",
                "profile": "Michael Cimino was born in New York City in 1939 and trained as an architect and painter before turning to film. He directed Thunderbolt and Lightfoot (1974) before The Deer Hunter made him Hollywood's most celebrated director at 39. The film won Best Picture and Best Director. Two years later, Heaven's Gate bankrupted United Artists and nearly ended his career. He directed only four more films before his death in 2016. The Deer Hunter is his masterpiece and possibly the only film in which his personal investment in working-class American life was perfectly matched to subject matter. He spent months researching the Ukrainian-American steel towns of Pennsylvania, the Orthodox church ceremonies, the specific culture of the mill workers. That research is visible in every frame of the first hour, which many critics have called the best opening hour in American cinema."
            },
            "writers": {
                "names": "Deric Washburn / Michael Cimino / Louis Garfinkle / Quinn K. Redeker",
                "profile": "The screenplay for The Deer Hunter has a complicated origin. Quinn K. Redeker and Louis Garfinkle wrote an early story treatment called 'The Man Who Came to Play' that established the Russian roulette concept. Cimino and Deric Washburn developed the shooting script. Washburn later claimed he wrote the final screenplay alone; Cimino maintained joint credit. The WGA assigned credit to Washburn for the screenplay. Whatever the actual collaboration, the script achieves something unusual in American cinema: it spends 50 minutes establishing a community before it tests it. The wedding sequence, the steel mill, the bar, the hunting trip: these are not prologue. They are the film's emotional investment account that the Vietnam sequences spend down. By the time Michael holds Nick in Saigon, you know exactly what he is fighting to save."
            },
            "lead_producer": {
                "name": "Barry Spikings / Michael Deeley",
                "company": "EMI Films"
            },
            "composer": {
                "name": "Stanley Myers",
                "profile": "Stanley Myers composed the score for The Deer Hunter, with guitarist John Williams (not the Star Wars composer; a different musician) performing the film's central theme, 'Cavatina.' The piece is a classical guitar melody of such simplicity and melancholy that it became, for many listeners, permanently associated with Vietnam. Myers composed for theater and film throughout his career; The Deer Hunter is his best-known work. 'Cavatina' won an Ivor Novello Award and has been performed countless times outside the film context. As a piece of score writing, it does something difficult: it gives the film an emotional register that is neither triumphant nor despairing but something harder to name, something like grief held at arm's length."
            },
            "cinematographer": {
                "name": "Vilmos Zsigmond",
                "profile": "Vilmos Zsigmond shot The Deer Hunter and received an Academy Award nomination for it. His photography of the Pennsylvania steel town sequences has a warm, amber quality that makes the community feel real and precious before the war removes it from the characters. The Saigon sequences are shot in Thailand and have a chaotic, humid quality that contrasts deliberately with the ordered beauty of Pennsylvania. Zsigmond's signature is a kind of earned intimacy: his camera stays close to faces, trusting that what the actors are doing is worth watching. With De Niro, Walken, and Streep, that trust is justified in every scene."
            },
            "casting_director": {
                "name": "Cis Corman",
                "profile": "The ensemble Cis Corman assembled for The Deer Hunter is one of the finest in American cinema. Robert De Niro as Michael Vronsky is the gravitational center: controlled, watchful, carrying the weight of the film's moral code without stating it. Christopher Walken as Nick was a relatively unknown stage actor at the time; his performance won the Oscar and defined his film career. Meryl Streep's Linda is the film's most undervalued performance: a woman who has been left behind, who loves two men, and who survives by adapting to loss without becoming callous. John Cazale, who was dying of cancer during filming and whose illness required De Niro to personally guarantee his performance before the studio would insure him, plays Stan with a low-key authenticity that matches the ensemble's documentary feel. The entire cast was committed to behaving as though they had actually grown up together in Clairton, Pennsylvania."
            },
            "top_cast": [
                {"name": "Robert De Niro", "role": "Michael Vronsky"},
                {"name": "Christopher Walken", "role": "Nick"},
                {"name": "John Savage", "role": "Steven"},
                {"name": "Meryl Streep", "role": "Linda"},
                {"name": "John Cazale", "role": "Stan"},
                {"name": "George Dzundza", "role": "John Welsh"}
            ]
        },
        "parentalGuidance": {
            "mpaaRating": "R",
            "mpaaDescriptors": "Strong violence, strong language, drug use, disturbing content",
            "recommendedAge": "17+",
            "contentWarnings": [
                "Extended Russian roulette sequences in which characters are forced to fire revolvers at their own heads, with on-screen deaths",
                "Graphic depictions of combat violence in Vietnam, including executions and explosions",
                "Heroin addiction depicted in later sequences involving a major character",
                "Strong language throughout, including frequent profanity",
                "A deer hunt depicting the killing of an animal",
                "Intense sequences of imprisonment, torture, and psychological abuse",
                "Implied sexual assault in prisoner sequences"
            ],
            "parentalNotes": "The Deer Hunter is a three-hour film rated R for very serious reasons. The Russian roulette sequences are among the most tension-saturating scenes in cinema history; they are not action sequences but endurance tests. The film's depictions of Vietnam, addiction, and permanent psychological damage are not sensationalized but they are graphic and honest. The film's moral framework is deeply traditional: male friendship, duty, sacrifice, and the cost of war. Mature teenagers 16+ who have already engaged with serious war films such as Platoon or Full Metal Jacket may be ready for The Deer Hunter. The three-hour runtime and the deliberate pace of the first hour require patience and attention that younger viewers typically lack."
        },
        "fidelityCasting": {
            "assessment": "FAITHFUL",
            "explanation": "The Deer Hunter is an original story set in a specific Ukrainian-American working-class community in Pennsylvania. The cast reflects this: De Niro, Walken, and Savage play men from this community with full commitment to the cultural specificity Cimino researched. The film does not make casting choices for demographic representation; it makes casting choices for authenticity to the world it depicts. No race-swapping, no diversity casting, no anachronistic representation. Meryl Streep as Linda is cast for her ability to embody a specific kind of working-class American woman, and she delivers exactly that."
        },
        "summary": {
            "overall": "The Deer Hunter opens with a steel mill. Men in masks pour metal in a Pittsburgh suburb. The shot lasts long enough to feel like work. Then it cuts to a wedding, and Michael Cimino spends the next 50 minutes at that wedding with real care, letting us learn who these people are before the war takes them.\n\nThis is not how most war films operate. Most war films establish characters just enough to make you care when they die. The Deer Hunter establishes a community. By the time Michael Vronsky, Nick, and Steven board a bus for Vietnam, you have watched them drink together, argue, hunt a deer at dawn, and dance at a wedding that refuses to end. You know who they are. You know what the war will cost.\n\nThe cost is enormous.\n\nMichael Cimino made this film in 1978 when the Vietnam War had been over for three years and America had not yet figured out what to do with it. The film does not offer a political position on the war. It offers something more demanding: a portrait of what the war did to three specific men from a specific place who had specific things to lose.\n\nThe Russian roulette sequences are the film's defining images. American prisoners forced to play the game for their Vietnamese captors' entertainment. Men betting their lives on chance while other men bet money on the outcome. Cimino shot these sequences with a physical immediacy that makes them almost unwatchable. The first time Nick fires the gun and survives, Christopher Walken's face does something that cannot be described in a review.\n\nWhat makes The Deer Hunter a TRADITIONAL film under VVWS methodology is not that it is pro-war. It is not pro-war. It is, in some ways, one of the more devastating portraits of war's cost in American cinema. What makes it traditional is everything it loves and how it loves it.\n\nIt loves the community in Clairton. It loves the wedding, the church, the mill, the bar, the hunt. It loves male friendship in the specific way that men love each other: without words, through presence, through showing up. Michael's journey back to Saigon to find Nick is not a plot device. It is the film's moral center. You do not leave your friend behind. You go back. Even if it costs you everything.\n\nThe 'God Bless America' ending, friends gathered after Nick's funeral, voices rising slowly and then together, is the film's final argument. They can love their country and grieve what it asked of them. Those two things are not contradictions to be resolved. They are the condition of being American men of their generation and class. The film holds both without flinching.\n\nStanley Myers's 'Cavatina,' performed on guitar throughout the film, is one of cinema's great scores. It is not triumphant or despairing. It is something harder to name. Something like grief held at arm's length, which is exactly what Michael Vronsky does for the entire film.",
            "adultInsight": "The Deer Hunter presents the traditional masculine code at its most demanding: Michael's 'one shot' principle applies to deer hunting and to everything else. You prepare, you commit, you do not waste. You do not give the animal a bad death. Michael lives by this code in Vietnam and he continues living by it after, at great personal cost. The film suggests that men like Michael, men with a code, bear the weight of a world that has none. Nick loses his code in Saigon and it kills him. Stan never had one and floats through life without consequence. Michael's code is his cross and his salvation simultaneously. For adult viewers interested in serious engagement with traditional masculine values and what it costs to hold them, The Deer Hunter is one of the most honest films ever made about that question.",
            "parentalGuidance": "Rated R for strong violence, language, and drug use. The Russian roulette sequences are among cinema's most harrowing. The depiction of heroin addiction is graphic and unglamorized. The film's Vietnam combat sequences include executions and explosive violence. Runtime is 182 minutes with a deliberate pace that requires sustained attention. Appropriate for mature viewers 17+ who are prepared for serious engagement with war's psychological and physical cost."
        },
        "tropeAudit": [
            {
                "id": "WOKE-DEER-001",
                "name": "Anti-war thesis through Vietnam trauma",
                "category": "Woke",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "The film depicts Vietnam as a place that destroys American men, physically and psychologically. Nick's descent into addiction and death, Michael's inability to readjust, Steven's permanent disability: all accumulate into a portrait of Vietnam as a machine for destroying working-class American boys. This is an anti-war thesis built on grief rather than politics, which is why it scores High authenticity rather than Low."
            },
            {
                "id": "WOKE-DEER-002",
                "name": "PTSD and war damage as permanent condition",
                "category": "Woke",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.1,
                "description": "Michael returns from Vietnam changed in ways he cannot name. He cannot pull the trigger on a deer he once would have shot without hesitation. Nick never comes home psychologically. The film refuses the comforting arc of healing. This is an honest portrayal of war trauma rather than an ideological one, but it contributes to the film's overall argument that the war took something that cannot be repaid."
            },
            {
                "id": "TRAD-DEER-001",
                "name": "Male friendship as sacred, unconditional bond",
                "category": "Traditional",
                "severity": 5,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 6.3,
                "description": "The central relationship in The Deer Hunter is between Michael, Nick, and Steven: three men who grew up together, served together, and whose friendship is the film's moral center. Michael's journey back to Saigon to find Nick is not motivated by sentiment but by obligation. You do not leave your friend behind. That bond, honored to the point of death, is the film's most powerful traditional value."
            },
            {
                "id": "TRAD-DEER-002",
                "name": "Working-class Americana: community, church, tradition",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "description": "The first 50 minutes of The Deer Hunter are spent in Clairton, Pennsylvania, at a wedding and a steel mill and a bar and a hunting trip. Cimino films this world with love: the Orthodox church ceremony, the community celebration, the shared labor, the ritual of the hunt. This is a specific, embodied portrait of working-class American life. The film treats this world as worthy of the same attention it would give a royal court."
            },
            {
                "id": "TRAD-DEER-003",
                "name": "The hunt as masculine ritual and moral proving ground",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "description": "The deer hunt establishes Michael's code: one shot. You prepare, you aim, you do not waste. You do not give the animal a bad death. This code, which he tries to teach Stan and which Stan dismisses, becomes the film's moral measuring stick. Michael's values are old-fashioned and demanding and they are presented as superior to Stan's casual carelessness."
            },
            {
                "id": "TRAD-DEER-004",
                "name": "Patriotic grief: God Bless America ending",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "description": "The final scene, friends gathering after Nick's funeral and slowly singing 'God Bless America' together, is one of cinema's most debated endings. It does not resolve the film's contradictions. It holds them. They can love their country and grieve what their country asked of them. The patriotism is real; so is the cost. The film refuses to choose between them."
            },
            {
                "id": "TRAD-DEER-005",
                "name": "Duty and service without protest",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.1,
                "description": "The three men go to Vietnam. The film does not show a recruitment scene or patriotic fervor. They go because that is what men in their world do. There is no protest, no conscientious objection, no political debate. This is the working-class American experience of Vietnam: you serve. The film does not sentimentalize this, but it does not mock it either."
            }
        ],
        "seo": {
            "titleTag": "Is The Deer Hunter (1978) Woke? Cimino's Vietnam Classic Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS v1.1 review of The Deer Hunter (1978). Trope audit, creative team ideology, parental guidance. Verdict: TRADITIONAL (+13.86 margin).",
            "keywords": "is The Deer Hunter woke, Deer Hunter 1978 review, Michael Cimino ideology, Deer Hunter traditional values, Robert De Niro Deer Hunter, Christopher Walken, Vietnam War film traditional"
        }
    },
    {
        "id": "chinatown-1974",
        "slug": "chinatown-1974",
        "title": "Chinatown",
        "year": 1974,
        "type": "film",
        "platform": "Paramount+ / Various",
        "genre": "Crime / Drama / Mystery / Noir",
        "date": "2026-08-02",
        "datePublished": "2026-08-02",
        "author": "VirtueVigil Editorial Team",
        "readTime": "12 min",
        "poster": "/images/posters/chinatown-1974.jpg",
        "releaseDate": "1974-06-20",
        "rating": "R",
        "runtime": "130 min",
        "director": "Roman Polanski",
        "writers": ["Robert Towne"],
        "cast": [
            {"name": "Jack Nicholson", "role": "J.J. 'Jake' Gittes"},
            {"name": "Faye Dunaway", "role": "Evelyn Mulwray"},
            {"name": "John Huston", "role": "Noah Cross"},
            {"name": "Diane Ladd", "role": "Ida Sessions"},
            {"name": "Burt Young", "role": "Curly"},
            {"name": "Perry Lopez", "role": "Lieutenant Escobar"},
            {"name": "John Hillerman", "role": "Yelburton"},
            {"name": "Darrell Zwerling", "role": "Hollis Mulwray"}
        ],
        "studio": "Long Road Productions",
        "distributor": "Paramount Pictures",
        "verdict": "WOKE",
        "wokeScore": 19.18,
        "tradScore": 5.88,
        "authIndex": 36,
        "scoreMargin": "-13 WOKE",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": {
            "is_trap": False,
            "explanation": "Chinatown does not qualify as a woke trap, though the case is worth examining. The film markets itself as a noir mystery, a genre associated with moral complexity rather than ideological messaging. The nihilistic ending and total victory of corrupt institutional power could surprise audiences expecting genre satisfaction. However, the VVWS trap rule requires that woke content not appear until at least 50% of the runtime, and Chinatown's institutional corruption and cynicism are present from the first reel. The film is openly and consistently what it is. No deceptive packaging applies."
        },
        "seoTitle": "Is Chinatown (1974) Woke? Polanski's Noir Classic Reviewed | VirtueVigil",
        "seoDescription": "VirtueVigil's full VVWS v1.1 review of Chinatown (1974). We score every trope, analyze the creative team ideology, and answer: is Polanski's noir masterpiece woke or traditional? Verdict: WOKE.",
        "seoKeywords": [
            "is Chinatown 1974 woke",
            "Chinatown 1974 review",
            "Chinatown conservative review",
            "Roman Polanski ideology",
            "Chinatown traditional values",
            "is Chinatown appropriate for kids",
            "Chinatown parental guidance",
            "Jack Nicholson Chinatown",
            "Faye Dunaway Chinatown",
            "Chinatown VirtueVigil score",
            "Robert Towne screenplay",
            "Chinatown film noir",
            "Chinatown Oscar nominations",
            "1970s noir film review",
            "Chinatown institutional corruption"
        ],
        "externalScores": {
            "rottenTomatoesCritic": 99,
            "rottenTomatoesAudience": 95,
            "imdb": 8.2,
            "metacritic": 92,
            "oscarNominations": 11,
            "oscarCategories": "Best Picture, Best Director, Best Actor (Nicholson), Best Actress (Dunaway), Best Original Screenplay (WON - Robert Towne), Best Cinematography, Best Art Direction, Best Costume Design, Best Film Editing, Best Original Score, Best Sound",
            "budget": "$6 million",
            "globalBoxOffice": "$29.2 million (1974)"
        },
        "creative_team": {
            "director": {
                "name": "Roman Polanski",
                "ideology": "WOKE. Polanski's films are consistently pessimistic about institutions, authority, and power structures. Rosemary's Baby presents trusted community as a conspiracy against the individual. The Tenant presents bureaucratic systems as engines of psychological destruction. Chinatown presents power as irredeemably self-perpetuating. Polanski's worldview is that the powerful will always win and the individual is nearly helpless against organized wealth. This is a recognizably leftist framework, though Polanski has never been a political filmmaker in the programmatic sense. His politics emerge from experience: a Holocaust survivor and exile whose biography shaped a fundamental distrust of institutions and authority.",
                "profile": "Roman Polanski was born in Paris in 1933 and grew up in occupied Poland during World War II. His mother died at Auschwitz. He survived the Krakow ghetto and spent part of the war hidden by Polish families. This biography is not separable from his art: his recurring themes of powerlessness, conspiracy, and the failure of institutions to protect the individual are rooted in direct experience of what happens when institutions become predatory. He directed Knife in the Water, Repulsion, Rosemary's Baby, and Chinatown before the events of 1977 that resulted in his exile from the United States. He has continued making films in Europe, including The Pianist, which won him an Academy Award for Best Director he could not collect in person. The moral complexity of his biography is not something VirtueVigil can resolve; we note it and score the film."
            },
            "writers": {
                "names": "Robert Towne",
                "profile": "Robert Towne wrote Chinatown and it is the finest original screenplay in American cinema. He wrote it as a tribute to California history, to Raymond Chandler's Philip Marlowe, and to the real events of the Owens Valley water wars in which Los Angeles's growth in the early 20th century was built on the theft of water from a farming community. The historical research is embedded in the screenplay but never displayed for its own sake. Towne wrote an ending in which Evelyn escapes and Katherine is saved. Polanski rejected this ending and insisted on the opposite, one in which evil wins completely. Towne has said he was heartbroken by the change. The film as shot is Polanski's vision. The screenplay as written was Towne's. Towne went on to write Shampoo, The Yakuza, and personal revisions of Mission: Impossible. Chinatown remains his masterpiece and his most contested work."
            },
            "lead_producer": {
                "name": "Robert Evans",
                "company": "Long Road Productions / Paramount Pictures"
            },
            "composer": {
                "name": "Jerry Goldsmith",
                "profile": "Jerry Goldsmith composed the Chinatown score in nine days after Bernard Herrmann was dismissed from the project following a conflict with producer Robert Evans over his approach. Goldsmith's score is one of the great achievements of film music: a solo trumpet theme that is simultaneously romantic and elegiac, evoking the noir tradition while giving Chinatown its own distinct emotional register. The score mourns the story before it ends. Goldsmith went on to score hundreds of films including Patton, Alien, Poltergeist, Total Recall, and L.A. Confidential. Chinatown is among his finest."
            },
            "cinematographer": {
                "name": "John A. Alonzo",
                "profile": "John A. Alonzo photographed Chinatown in a warm, sun-bleached palette that gives 1930s Los Angeles a look of false paradise: beautiful on the surface, something wrong underneath. The brightness of his photography is deliberate and subversive. Noir typically uses darkness and shadow. Chinatown uses sunlight, because in California, the corruption happens in daylight. Water board meetings are not held at midnight. Land fraud happens in city hall. Alonzo's palette makes the familiar feel sinister, which is the film's central trick."
            },
            "casting_director": {
                "name": "Jane Feinberg / Mike Fenton",
                "profile": "Jack Nicholson as J.J. Gittes is the casting decision the film could not survive without. Nicholson at 37 had the combination of charm, intelligence, and underlying menace the role requires. Gittes is not a passive detective; he is an active intruder into a world that is prepared to destroy him. Nicholson gives him the confidence of a man who has always been underestimated and has learned to weaponize it. Faye Dunaway as Evelyn Mulwray is the film's greatest performance: a woman who cannot tell the truth because the truth is too terrible, and who cannot stop trying to protect her daughter even when protection is impossible. John Huston as Noah Cross is the definitive cinematic villain of the 1970s: grandfatherly, avuncular, entirely evil. Huston's casting was Polanski's; it is a stroke of genius."
            },
            "top_cast": [
                {"name": "Jack Nicholson", "role": "J.J. 'Jake' Gittes"},
                {"name": "Faye Dunaway", "role": "Evelyn Mulwray"},
                {"name": "John Huston", "role": "Noah Cross"},
                {"name": "Diane Ladd", "role": "Ida Sessions"},
                {"name": "Perry Lopez", "role": "Lieutenant Escobar"}
            ]
        },
        "parentalGuidance": {
            "mpaaRating": "R",
            "mpaaDescriptors": "Violence, adult themes, sexual content, disturbing content",
            "recommendedAge": "17+",
            "contentWarnings": [
                "A revelation of incest between a father and daughter that is central to the plot",
                "A graphic scene in which the protagonist's nose is sliced open with a knife",
                "On-screen shooting death of a major character in the final sequence",
                "Sexual content including brief nudity and implied affairs",
                "Strong language throughout",
                "Complex themes of power, corruption, and the abuse of wealth",
                "A child in danger in the film's final sequence"
            ],
            "parentalNotes": "Chinatown is a film for adult audiences. The incest revelation, presented as the film's central horror, requires adult comprehension. The nihilistic ending, in which evil wins completely and the protagonist fails to save anyone, is emotionally demanding for viewers of any age and devastating without the frame of genre expectation. The violence is not graphic by contemporary standards but is startling in context. Appropriate for mature adults interested in the history of American cinema, noir filmmaking, and the legacy of 1970s Hollywood. Not appropriate for viewers under 17."
        },
        "fidelityCasting": {
            "assessment": "FAITHFUL",
            "explanation": "Chinatown is an original screenplay set in 1930s Los Angeles. The characters are invented, though the historical water theft plot is based on real events. Jack Nicholson's Jake Gittes is cast for his specific combination of charm and underlying volatility, which the role requires. Faye Dunaway's Evelyn Mulwray is cast for her ability to sustain a performance built on concealment and suppressed terror. John Huston as Noah Cross is cast against his directorial persona, weaponizing the audience's affection for the man who made The Maltese Falcon. No race-swapping or diversity casting concerns apply. The period setting is reproduced with historical consistency."
        },
        "summary": {
            "overall": "Robert Towne wrote a different ending for Chinatown. In his version, Evelyn shoots her father Noah Cross and escapes with Katherine. Good wins. The detective's efforts mean something. Roman Polanski refused to shoot it.\n\nPolanski had survived the Krakow ghetto and Auschwitz had taken his mother. He knew something Towne's ending did not account for: sometimes evil wins completely. Sometimes the powerful do what they want, and the individual who stands against them ends up on the street watching it happen.\n\nThe ending Polanski shot is the ending Chinatown has. Evelyn is shot by the police. Cross takes Katherine. Jake stands on the street while his associate walks him away: 'Forget it, Jake. It's Chinatown.' The evil wins. The detective's competence is not merely insufficient; it is causal. His investigation led Cross to Evelyn and Katherine. His decision to call the police triggered Evelyn's death. The hero's involvement made everything worse.\n\nThis is not a traditional narrative. Under VVWS methodology, Chinatown scores WOKE by a substantial margin, and that scoring is correct. The film's thesis is that institutional power in America belongs to men like Noah Cross, wealthy enough to own the water and buy the government and corrupt the police, and that nothing Jake Gittes can do will change this. Individual competence is no match for systemic corruption. Good detective work delivers tragedy.\n\nAnd yet. Chinatown is also one of the few American films that presents the incest revelation without moral relativism. Noah Cross is not given a backstory that explains him. He is not shown as a product of his circumstances. He did what he did because he had the power to do it and he wanted to. The film's moral judgment on him is absolute. That clarity, in the middle of nihilism, is its own kind of traditional value.\n\nJack Nicholson's Jake Gittes operates by a professional code: he follows evidence wherever it leads, he refuses to be bought off, he insists on the truth even when the truth destroys him. The code is right. The world is not configured to reward it. That gap between a man's values and the world's indifference to them is the film's emotional core.\n\nJerry Goldsmith scored Chinatown in nine days after Bernard Herrmann was fired from the project. His solo trumpet theme mourns the story before it happens. It is romantic and elegiac in the same breath. It understands something about Los Angeles that Polanski understood: the city was built on fraud, the sun shines beautifully on top of it, and the people who live there are mostly fine with that.\n\nChinatown is a great film and a WOKE film. These things are not contradictory. The VVWS scores what is there, not whether the film succeeds at what it attempts. What is there is a coherent and sustained argument that power is irredeemably corrupt and individual action cannot meaningfully oppose it. That argument scores what it scores.",
            "adultInsight": "The Chinatown conversation worth having for adult viewers is about what the film says about civic engagement. Jake Gittes does everything right: he investigates, he persists, he refuses to be bought, he acts when he has enough information. The outcome is catastrophe. Polanski's argument is that in a system where wealth is sufficiently entrenched, civic virtue is not enough. You cannot out-detect Noah Cross. You cannot out-attorney him or out-vote him. He owns the water and the land and the police. For conservative viewers who believe in civic institutions, Chinatown is the darkest possible challenge to that belief. For progressive viewers who believe in systemic critique, it is confirmation. For viewers who simply watch films: it is an experience of watching competence meet its absolute limit and break.",
            "parentalGuidance": "Rated R for adult themes including incest, violence, and disturbing content. The incest revelation is the film's central horror and requires adult comprehension. The on-screen shooting death of a major character in the final sequence is sudden and devastating. The nihilistic ending, in which evil triumphs completely, is emotionally demanding without the comfort of genre resolution. Appropriate for mature adults. Not appropriate for viewers under 17."
        },
        "tropeAudit": [
            {
                "id": "WOKE-CHINA-001",
                "name": "Institutional power is irredeemably corrupt",
                "category": "Woke",
                "severity": 5,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 6.3,
                "description": "Chinatown's central argument is that power in America belongs to men like Noah Cross, wealthy enough to corrupt the police, own the water, and buy the politicians, and that nothing the individual can do will change this. The water board, the police department, and city government are all instruments of Cross's will. This is not incidental corruption; it is the film's thesis about institutional power and who it actually serves."
            },
            {
                "id": "WOKE-CHINA-002",
                "name": "Nihilistic ending: evil wins completely",
                "category": "Woke",
                "severity": 5,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 6.3,
                "description": "The final scene of Chinatown is among the most deliberately despairing endings in American cinema. Evelyn is killed by the police. Cross takes Katherine. Jake is walked away from the scene by his associates. The evil wins completely, and the most a good man can do is survive it and try to forget. Polanski insisted on this ending over Towne's more hopeful alternative. The nihilism is total and intentional."
            },
            {
                "id": "WOKE-CHINA-003",
                "name": "Incest and abuse as extension of unchecked power",
                "category": "Woke",
                "severity": 4,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.8,
                "description": "The revelation that Noah Cross fathered a child with his own daughter functions as the film's ultimate power statement: he can do anything to anyone. The incest is presented not as aberration but as extension of who Cross is. Men with his resources face no limits, not even the most fundamental ones. This is a coherent ideological argument about the relationship between wealth and moral constraint."
            },
            {
                "id": "WOKE-CHINA-004",
                "name": "Detective's competence causes the tragedy",
                "category": "Woke",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "description": "Jake's investigation is not just ineffective; it is directly causal of the worst outcome. His involvement leads Cross to Evelyn and Katherine. His decision to call the police triggers Evelyn's death. The film suggests that individual competence cannot overcome entrenched institutional power and that trying may make things worse. The heroic private detective narrative is turned against itself."
            },
            {
                "id": "TRAD-CHINA-001",
                "name": "Private detective competence and professional code",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "description": "Jake Gittes is genuinely good at his job. He is methodical, perceptive, and persistent. His professional ethics are clearly defined: follow evidence wherever it leads, refuse to be bought off, insist on the truth. In the context of a genre that centers male professional competence, Chinatown gives Gittes legitimate credentials. His failure is not a failure of skill but of the world he is operating in."
            },
            {
                "id": "TRAD-CHINA-002",
                "name": "Absolute moral clarity on some wrongs",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.1,
                "description": "Chinatown never suggests that Cross's relationship with his daughter is morally complex or contextually explicable. It is presented as evil without qualification. The film does not give Cross a rehabilitating backstory or ask the audience to understand. He did what he did because he could. Even in a deeply nihilistic film, that moral clarity is significant: some acts are unambiguously wrong."
            }
        ],
        "seo": {
            "titleTag": "Is Chinatown (1974) Woke? Polanski's Noir Classic Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS v1.1 review of Chinatown (1974) directed by Roman Polanski. Trope audit, creative team ideology, parental guidance. Verdict: WOKE (margin -13.3).",
            "keywords": "is Chinatown woke, Chinatown 1974 review, Roman Polanski ideology, Chinatown traditional values, Jack Nicholson Chinatown, Faye Dunaway, Robert Towne screenplay, Chinatown film noir review"
        }
    }
]

# Check no slugs already exist
for r in new_reviews:
    if r["slug"] in existing_slugs:
        print(f"ERROR: {r['slug']} already exists!")
        exit(1)

reviews.extend(new_reviews)

with open("src/data/reviews.json", "w") as f:
    json.dump(reviews, f, indent=2)

print(f"New count: {len(reviews)}")
print("Added:")
for r in new_reviews:
    print(f"  {r['slug']}: {r['verdict']} (margin {r['scoreMargin']})")
