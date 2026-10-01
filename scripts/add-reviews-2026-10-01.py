#!/usr/bin/env python3
"""Add 3 reviews for 2026-10-01 daily cron run."""
import json
import sys

REVIEWS_PATH = "src/data/reviews.json"

reviews = json.load(open(REVIEWS_PATH))

new_reviews = []

# ============================================================
# REVIEW 1: Heart of the Beast (2026) — New Release
# ============================================================
heart_of_the_beast = {
    "id": "heart-of-the-beast-2026",
    "slug": "heart-of-the-beast-2026",
    "title": "Heart of the Beast",
    "year": 2026,
    "type": "movie",
    "platform": "Theaters",
    "genre": "Survival Thriller Adventure Drama",
    "date": "2026-10-01",
    "datePublised": "2026-10-01",
    "author": "VirtueVigil Editorial Team",
    "readTime": "7 min read",
    "poster": "/images/posters/heart-of-the-beast-2026.jpg",
    "releaseDate": "2026-09-25",
    "rating": "PG-13",
    "runtime": "1h 41m",
    "director": "David Ayer",
    "writers": ["Cameron Alexander"],
    "cast": [
        "Brad Pitt",
        "J.K. Simmons",
        "Anna Lambe",
        "Justin Melnick",
        "Shaun DeZern",
        "Odin (Uber II / Seeka / Ryker / Hondo)"
    ],
    "studio": "Paramount Pictures",
    "distributor": "Paramount Pictures",
    "verdict": "BALANCED TRADITIONAL",
    "wokeScore": 0.06,
    "tradScore": 8.55,
    "authIndex": 99,
    "scoreMargin": "+8.49 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "Heart of the Beast is exactly what it advertises: a survival thriller about a man and his dog. There is no ideological Trojan horse and nothing hidden past any runtime marker. The film is sincere from the opening crash to the final frame.",
    "tropeAudit": [
        {
            "id": "HOTB-TRAD-001",
            "name": "Competence as Virtue",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 1.8,
            "explanation": "James Belmont's Special Forces training is the engine of survival. Every decision he makes is rooted in professional competence, and the film treats that competence with genuine respect, never undermining it for dramatic convenience."
        },
        {
            "id": "HOTB-TRAD-002",
            "name": "Duty and Protection",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 1.8,
            "explanation": "The bond between James and Odin is defined by mutual protection. James risks his life for his dog, and Odin returns the favor. This is the emotional heart of the film and it operates on a deeply traditional framework of loyalty and self-sacrifice."
        },
        {
            "id": "HOTB-TRAD-003",
            "name": "Male competence as narrative engine",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.08,
            "explanation": "Brad Pitt carries the film almost entirely on his shoulders. His character's physical endurance, tactical thinking, and emotional restraint drive every scene. The film has no interest in apologizing for centering a capable man."
        },
        {
            "id": "HOTB-TRAD-004",
            "name": "Loyalty to teammates",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.15,
            "explanation": "The man-dog bond is the purest expression of loyalty the survival genre can offer. Odin's devotion to James is absolute and uncomplicated, and James's reciprocal loyalty is the film's moral center. This is the kind of relationship that modern Hollywood often complicates with irony or subversion; Heart of the Beast plays it straight."
        },
        {
            "id": "HOTB-TRAD-005",
            "name": "Traditional Masculinity",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "The film's vision of masculinity is old-fashioned in the best sense: stoic, resourceful, physically capable, and emotionally available only through action rather than confession. James Belmont is not a toxic caricature or a deconstructed archetype. He is a competent man in a hard situation doing what needs to be done."
        },
        {
            "id": "HOTB-WOKE-001",
            "name": "General Woke Element (Diverse Casting)",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.06,
            "explanation": "Anna Lambe, an Inuk actress, plays a small role as a local woman who briefly assists Belmont. The casting is respectful and the character is not used for political messaging. This is functionally invisible as an ideological element."
        }
    ],
    "summary": {
        "overall": "Heart of the Beast is the kind of movie that does not need to explain itself. David Ayer directs Brad Pitt as James Belmont, a Special Forces veteran who survives a plane crash in the Alaskan wilderness with his combat dog Odin, and what follows is 101 minutes of two beings trying to not die. That is the whole movie. It knows what it is, it knows what you came for, and it delivers without a single moment of pretension or messaging. After years of survival thrillers that could not resist turning the wilderness into a metaphor for something or the survivor into a vessel for trauma-as-identity, Heart of the Beast feels like a corrective. It is not artful in the way The Revenant was artful. It is not psychologically complex. It is a well-made, deeply sincere, occasionally brutal story about a man and his dog, and it trusts that to be enough.",
        "traditionalContent": "The traditional content in Heart of the Beast is not subtext because there is no subtext. It is text. James Belmont is a capable man whose capability is the film's organizing principle. His military training is not a source of trauma or moral complication. It is a toolkit, and the film respects the toolkit. When he sets a broken leg, builds a shelter, or fights off a wolf, the camera does not cut away to suggest his actions are suspect. It lingers. It admires. Ayer, who directed Fury and End of Watch, has always had a feel for masculine competence as a dramatic value, and here he strips away every distraction. There is no love interest, no flashback family, no redemption arc from a past sin. There is only the present tense of survival, and the bond between James and Odin that makes survival worth pursuing. Odin is not a metaphor. He is a combat dog who does combat-dog things: he scouts, he guards, he attacks, he stays. The loyalty between them is the film's only emotional currency, and it is rendered with a sincerity that will catch audiences off guard. In an era when most studio films feel the need to wink at the audience or layer in social commentary, Heart of the Beast refuses both impulses. Its vision of masculinity is stoic, protective, and expressed through action rather than confession. The film does not deconstruct its hero or apologize for him. It simply watches him work, and the watching is satisfying.",
        "wokeContent": "There is essentially no woke content in Heart of the Beast. The closest thing to a progressive signal is the brief appearance of Anna Lambe, an Inuk actress, as a local woman living near the crash site. She delivers a few lines of practical guidance and is never seen again. Her character is not a repository of indigenous wisdom, nor is she positioned as morally superior to the white protagonist. She is a person who lives where the crash happened and who helps, as any decent person would. The film does not lecture about environmental stewardship, colonial guilt, or the nobility of native peoples. It does not use the Alaskan wilderness as a stage for climate messaging. It does not make James Belmont confront his privilege before nature humbles him. These absences are notable precisely because they represent discipline. Ayer and screenwriter Cameron Alexander clearly understood that the survival-thriller audience is not showing up for a sermon, and they made the decision to serve the genre rather than use it. That decision deserves acknowledgment because it is increasingly rare in studio filmmaking. The diverse casting of the supporting military unit in the film's opening sequence is similarly unremarkable: soldiers of various backgrounds appear, none of them are made to represent their demographic category, and the film moves on. If there is an ideology in Heart of the Beast, it is the oldest one: the world is dangerous, and you survive it with skill, courage, and whoever is loyal enough to stay by your side."
    },
    "parentalGuidance": "Heart of the Beast is rated PG-13 for intense survival action, some violence, and thematic material. The film contains several sequences of animal threat including encounters with wolves and a bear that may be intense for younger viewers. The violence is survival-oriented rather than gratuitous: injuries are shown realistically, and there are moments of genuine peril. James Belmont sets his own broken leg in one sequence that squeamish viewers will find difficult. There is no sexual content, minimal language, and no drug use. The dog, Odin, is placed in danger multiple times, and parents of sensitive children should be aware that the film does not guarantee his safety until the final frames. Families with children over 12 who enjoy survival stories and can handle animal-in-peril sequences will find this a rewarding watch. The film contains a positive message about loyalty, courage, and the bond between humans and animals that makes for good family discussion. Parents should know that younger children who are attached to dogs may find several scenes emotionally difficult, even if the ultimate resolution is satisfying."
}

# ============================================================
# REVIEW 2: City of God (2002) — Catalog Backfill
# ============================================================
city_of_god = {
    "id": "city-of-god-2002",
    "slug": "city-of-god-2002",
    "title": "City of God",
    "year": 2002,
    "type": "movie",
    "platform": "Multiple Streaming",
    "genre": "Crime Drama Epic",
    "date": "2026-10-01",
    "datePublised": "2026-10-01",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/city-of-god-2002.jpg",
    "releaseDate": "2002-08-30",
    "rating": "R",
    "runtime": "2h 10m",
    "director": "Fernando Meirelles",
    "writers": ["Braulio Mantovani"],
    "cast": [
        "Alexandre Rodrigues",
        "Leandro Firmino",
        "Phellipe Haagensen",
        "Douglas Silva",
        "Jonathan Haagensen",
        "Seu Jorge",
        "Alice Braga"
    ],
    "studio": "O2 Filmes / VideoFilmes / Globo Filmes",
    "distributor": "Miramax Films",
    "verdict": "BALANCED TRADITIONAL",
    "wokeScore": 0.30,
    "tradScore": 6.12,
    "authIndex": 95,
    "scoreMargin": "+5.82 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "City of God is not a woke trap. The violence and systemic poverty it depicts are foregrounded from the opening frame. There is no hidden ideological pivot. The film's criticism of institutional failure (corrupt police, absent government) is rooted in direct observation of real conditions, not in imported American academic frameworks.",
    "tropeAudit": [
        {
            "id": "COG-TRAD-001",
            "name": "Competence as Virtue",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 1.8,
            "explanation": "Rocket's escape from the cycle of violence comes through his skill as a photographer. The film treats competence as the only reliable exit from poverty, not activism or grievance. His camera is his ladder, and the film respects the climb."
        },
        {
            "id": "COG-TRAD-002",
            "name": "Male competence as narrative engine",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 1.8,
            "explanation": "The entire narrative is driven by male characters and male choices. Li'l Ze's ruthlessness, Knockout Ned's descent, and Rocket's ambition form a triptych of male agency. Women are largely positioned as prizes or casualties, which is a limitation of the source material rather than a political statement."
        },
        {
            "id": "COG-TRAD-003",
            "name": "Redemption arc (escape through work)",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 1.08,
            "explanation": "Rocket's arc is fundamentally traditional: a young man chooses craft over crime, discipline over chaos, and is rewarded for that choice. The film is not sentimental about this. Rocket does not succeed because the system works. He succeeds because he is talented and persistent, and the film frames this as admirable rather than problematic."
        },
        {
            "id": "COG-TRAD-004",
            "name": "Loyalty to teammates",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "Various gang loyalties and friendships, particularly between Benny and Li'l Ze, structure the emotional beats of the film. Betrayal is the ultimate sin, and loyalty, however misapplied, is presented as a genuine value."
        },
        {
            "id": "COG-TRAD-005",
            "name": "Natural Hierarchy",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "The drug trade operates on a clear hierarchy, and the film does not frame this hierarchy as inherently unjust. The problem is not the structure but who occupies it. Li'l Ze's violence is a perversion of natural order, not a consequence of it."
        },
        {
            "id": "COG-WOKE-001",
            "name": "Systemic Oppression Narrative",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.12,
            "explanation": "The film depicts institutional failure: corrupt police, absent social services, an economy that offers only crime or subsistence. However, this is observation, not ideology. The film was made in 2002 Brazil, long before American critical frameworks colonized international cinema. The poverty is real, not metaphorical."
        },
        {
            "id": "COG-WOKE-002",
            "name": "General Woke Element (Diverse Casting)",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.06,
            "explanation": "The cast is almost entirely Black and mixed-race Brazilian, which is organic to the setting rather than a diversity mandate. Most actors were actual favela residents. This is not DEI casting. It is verisimilitude."
        },
        {
            "id": "COG-WOKE-003",
            "name": "Anti-Police Sentiment",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.12,
            "explanation": "The police are depicted as corrupt and complicit in the drug trade. This is a matter of factual reportage in the context of 1970s-80s Rio favelas, not a political thesis about policing as an institution. The film does not suggest police corruption is universal or that defunding is the answer."
        }
    ],
    "summary": {
        "overall": "City of God is one of the great films of the 21st century, and it is also one of the hardest to score on a framework designed for American culture-war content. The film is Brazilian, made in 2002, set in the 1960s through early 1980s, and its primary subject is the rise of organized crime in a Rio de Janeiro favela. None of this maps cleanly onto the American ideological binary that VirtueVigil's scoring system was built to assess. But the film is on IMDb's Top 250, it has been canonized by international critics for two decades, and parents look up reviews of it before letting their teenagers watch it. So here we are. Directed by Fernando Meirelles and co-directed by Katia Lund, City of God follows a young man named Rocket (Alexandre Rodrigues) as he navigates a world where the only available paths are crime, poverty, or escape. The film spans roughly two decades and is structured as a series of interconnected stories about the drug lords, street kids, and ordinary residents of the Cidade de Deus housing project. Its visual language is kinetic, violent, and occasionally beautiful. It earned four Academy Award nominations. It holds a 91 percent on Rotten Tomatoes. It is, by any measure, a masterpiece.",
        "traditionalContent": "The traditional content in City of God is embedded in its narrative architecture rather than its ideology. Rocket's story is a classic Horatio Alger arc translated into the language of Brazilian poverty: a young man of no particular advantage rises through talent and persistence. His camera becomes his escape route, and the film treats his ambition as admirable rather than as a symptom of internalized oppression. The gangland hierarchy, while brutal, operates on principles that are legible within a traditional framework: loyalty matters, betrayal is punished, and competence determines rank. Li'l Ze is terrifying precisely because he violates natural limits. He kills without cause, humiliates without purpose, and rules through fear rather than respect. The film does not present his violence as a rational response to systemic injustice. It presents it as evil, and the distinction matters. Knockout Ned's tragic arc -- from peaceful ex-soldier to vengeful killer -- is a moral fall, not a liberation story. The film understands that violence corrupts the violent regardless of their grievances. Beneath the flashy editing and the machine-gun pacing, City of God is a deeply conservative film about what happens when order collapses. It does not celebrate the collapse. It mourns it.",
        "wokeContent": "The woke reading of City of God is available to anyone who wants it: systemic poverty, corrupt police, institutional abandonment of the poor, the criminalization of Black youth. All of these elements are objectively present in the film. What is not present is a Western progressive framework that interprets these elements through the lens of identity politics. The police in City of God are corrupt because the police in 1970s Rio were corrupt, not because policing is an inherently oppressive institution. The residents of the favela are poor because Brazil's economic inequality is staggering, not because capitalism is inherently racist. The film is reportage, not polemic. It was made before the American culture war colonized the way international cinema is discussed, and it resists that colonization by being specific rather than general. The favela is a real place, the story is based on a real novel by Paulo Lins who grew up there, and the actors were mostly actual favela residents. This is not a film that weaponizes poverty to make a point. It is a film that shows poverty because the story takes place in a poor neighborhood. The distinction is important. Woke audiences will find material here. Traditional audiences will find a film that respects their intelligence rather than insulting it with a lecture. Both readings are defensible, which is why the margin lands where it does."
    },
    "parentalGuidance": "City of God is rated R for strong brutal violence, sexuality, drug content, and language. This is one of the more graphically violent films in the American canon, and parents should take the rating seriously. Children are shown handling firearms, committing murder, and being murdered. The film's aesthetic (rapid editing, stylized cinematography) can make the violence feel exciting in a way that is more troubling than straightforward gore. There is sexual content including a rape scene. Drug use and drug dealing are depicted throughout. The film is in Portuguese with English subtitles, which may make it harder for younger viewers to follow but does not reduce the impact of what is shown. Not appropriate for anyone under 16, and parents should watch it first before deciding whether their older teens are ready for it. For mature viewers, City of God is a legitimate work of art that rewards discussion about poverty, choice, violence, and the cost of escaping a bad situation. The thematic content is rich enough to justify its place in film history, but the R rating is not a suggestion."
}

# ============================================================
# REVIEW 3: East of Eden (2026) — TV/Series
# ============================================================
east_of_eden = {
    "id": "east-of-eden-2026",
    "slug": "east-of-eden-2026",
    "title": "East of Eden",
    "year": 2026,
    "type": "series",
    "platform": "Netflix",
    "genre": "Drama Literary Adaptation",
    "date": "2026-10-01",
    "datePublised": "2026-10-01",
    "author": "VirtueVigil Editorial Team",
    "readTime": "8 min read",
    "poster": "/images/posters/east-of-eden-2026.jpg",
    "releaseDate": "2026-09-30",
    "rating": "TV-MA",
    "runtime": "7 episodes (55-65 min each)",
    "director": "Garth Davis, Laure de Clermont-Tonnerre",
    "writers": ["Zoe Kazan", "Alexander Chee"],
    "showrunner": "Zoe Kazan, Jeb Stuart",
    "cast": [
        "Florence Pugh",
        "Christopher Abbott",
        "Mike Faist",
        "Joseph Zada",
        "Joe Anders",
        "Martha Plimpton",
        "Ciaran Hinds",
        "Tracy Letts",
        "Hoon Lee"
    ],
    "studio": "Anonymous Content / Fifth Season",
    "distributor": "Netflix",
    "verdict": "BALANCED TRADITIONAL",
    "wokeScore": 0.30,
    "tradScore": 10.59,
    "authIndex": 97,
    "scoreMargin": "+10.29 TRAD",
    "preRelease": False,
    "wokeTrap": False,
    "woke_trap_assessment": "East of Eden contains no woke trap. The series is a faithful adaptation of John Steinbeck's 1952 novel, and its ideological content (the battle between good and evil, the concept of timshel) is visible from the first episode. The casting of Florence Pugh as the villainous Cathy Ames and the diverse supporting cast are production decisions, not ideological pivots. Nothing is hidden past any runtime marker.",
    "tropeAudit": [
        {
            "id": "EOE-TRAD-001",
            "name": "Moral Choice ('Timshel')",
            "category": "Traditional",
            "severity": 4,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 4.2,
            "explanation": "The Hebrew concept of 'timshel' -- 'thou mayest' -- is the philosophical spine of Steinbeck's novel and this adaptation. The idea that human beings can choose between good and evil, that they are not predetermined by their nature or circumstances, is profoundly antithetical to modern progressive frameworks that emphasize systemic determinism. This theme runs through every episode."
        },
        {
            "id": "EOE-TRAD-002",
            "name": "Biblical allusion (Cain and Abel)",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "High",
            "centrality": "High",
            "weightedScore": 3.15,
            "explanation": "The Cal/Aron dynamic is an explicit Cain-and-Abel retelling, and the series treats the biblical framework with the gravity Steinbeck intended. This is not comparative mythology being deconstructed. It is moral architecture being built."
        },
        {
            "id": "EOE-TRAD-003",
            "name": "Family and Heritage",
            "category": "Traditional",
            "severity": 3,
            "authenticity": "Moderate",
            "centrality": "High",
            "weightedScore": 1.8,
            "explanation": "The Trask and Hamilton family sagas span generations, and the series treats lineage, inheritance, and the weight of family history as forces that shape character. This is a multi-generational American story in the classic mold."
        },
        {
            "id": "EOE-TRAD-004",
            "name": "Male competence as narrative engine",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "Adam Trask, Charles Trask, and Samuel Hamilton are traditionally masculine figures whose actions drive the plot. The series does not undermine their authority or competence. Adam's attempt to be a good father, however flawed, is treated as noble rather than patriarchal."
        },
        {
            "id": "EOE-TRAD-005",
            "name": "Duty and Protection",
            "category": "Traditional",
            "severity": 2,
            "authenticity": "Moderate",
            "centrality": "Moderate",
            "weightedScore": 0.72,
            "explanation": "Adam Trask's commitment to protecting his sons from the truth about their mother is a protective impulse rooted in duty. The series does not mock this as naive. It treats it as tragic, which is the correct register for the material."
        },
        {
            "id": "EOE-WOKE-001",
            "name": "Female Power Structure (Production)",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.12,
            "explanation": "Zoe Kazan created, wrote, and showran the series, and Florence Pugh is both star and executive producer. These are production-level facts that do not distort the source material. Kazan's adaptation is faithful to Steinbeck's text, and Pugh's Cathy is evil, not empowered."
        },
        {
            "id": "EOE-WOKE-002",
            "name": "Gender Role Inversion (Cathy Ames)",
            "category": "Woke",
            "severity": 2,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.12,
            "explanation": "Cathy Ames is one of literature's great female villains, and while a modern adaptation could reframe her as a victim of patriarchal oppression, this one does not. She is presented as genuinely monstrous, which is true to Steinbeck. The casting of Pugh adds star power but does not change the character's moral valence."
        },
        {
            "id": "EOE-WOKE-003",
            "name": "General Woke Element (Diverse Casting)",
            "category": "Woke",
            "severity": 1,
            "authenticity": "Low",
            "centrality": "Low",
            "weightedScore": 0.06,
            "explanation": "Hoon Lee plays Lee, the Trask family's Chinese servant, a role traditionally played by Asian actors but given significantly more dignity in Steinbeck's novel than contemporary readers might expect. The casting choice is faithful to the character's prominence in the book and is not a diversity insertion."
        }
    ],
    "summary": {
        "overall": "East of Eden is the best thing Netflix has done with classic American literature, and it arrives at a moment when the streaming platform desperately needs a prestige win that does not feel like homework. Created by Zoe Kazan and starring Florence Pugh as the malevolent Cathy Ames, this seven-episode limited series adapts John Steinbeck's 1952 novel with a fidelity that will surprise anyone who expected the usual Netflix treatment. The novel is a sprawling multi-generational saga about the Trask and Hamilton families in California's Salinas Valley, built around the biblical story of Cain and Abel and anchored by the Hebrew concept of timshel: thou mayest. The series is directed by Garth Davis (Lion) and Laure de Clermont-Tonnerre (The Mustang), and the production values reflect the kind of investment Netflix reserves for its awards-season contenders. Christopher Abbott plays Adam Trask with the right mixture of goodness and weakness, Mike Faist brings a coiled physicality to Charles, and Joseph Zada and Joe Anders play the twin sons Cal and Aron with a rawness that serves the material. But the series belongs to Pugh, whose Cathy Ames is chilling precisely because she is never allowed to become sympathetic. This is not a revisionist take on a misunderstood woman. It is a portrait of evil, and the series has the courage to leave it at that.",
        "traditionalContent": "The traditional heart of East of Eden is the question Steinbeck spent his entire novel asking: can a person choose to be good, or is character predetermined by blood, circumstance, and history? The answer the novel gives is timshel -- thou mayest -- and the series preserves this answer intact. In an era when progressive storytelling increasingly treats individuals as products of systemic forces, a drama that insists on the reality of moral choice is inherently countercultural. Cal Trask's struggle is not with structural oppression. It is with himself. He believes he has inherited his mother's evil and is doomed to replicate it, and the series treats this belief as a temptation rather than a truth. The resolution -- that he can choose differently, that he is not bound by his nature -- is one of the most traditional ideas in American literature, and the series delivers it without apology or ironic distance. The biblical architecture of the story is not deconstructed or critiqued. It is used. The Cain-and-Abel dynamic between Cal and Aron structures the entire narrative, and the series assumes the audience can engage with biblical allusion without needing it explained or debunked. Samuel Hamilton, played by Ciaran Hinds with the warmth of a man who has earned his wisdom, is a patriarch in the best sense: he dispenses guidance, loves his family, and models a form of masculine authority that is earned through character rather than demanded through power. The Trask family saga treats inheritance, duty, and the burden of knowing too much about your parents as serious themes, and the series does not undercut them with contemporary irony. East of Eden is not a conservative show in a political sense. It is a show built on conservative premises about human nature, free will, and the reality of evil, and those premises are allowed to stand.",
        "wokeContent": "The woke content in East of Eden is almost entirely located at the production and casting level rather than in the text. Zoe Kazan created, wrote, and showran the series, making this a female-led production of a male-authored classic. Florence Pugh is both star and executive producer. These are facts about who made the show, not what the show says, and they do not alter the ideological content of the source material. Kazan's adaptation is notably faithful. She does not use Steinbeck's novel as a Trojan horse for contemporary messaging. Cathy Ames is allowed to be evil without being reframed as a victim of the patriarchy. The Trask brothers' conflicts are left in their biblical register rather than being updated to reflect modern gender politics. Hoon Lee's casting as Lee, the Chinese servant, is the one casting choice that could have become ideologically freighted, but the character was written by Steinbeck as unusually intelligent and dignified for a servant role in 1952 fiction, and the series preserves that dignity without turning him into a lecture about representation. There is no scene in which Lee explains racism to the white characters. There is no moment where the series pauses to signal its awareness of historical inequities. It trusts the audience to notice that Lee is the smartest person in the room without needing to announce it. That trust is the difference between a show that respects its audience and a show that thinks its audience needs to be educated. East of Eden respects its audience. The production team happens to include women in positions of creative authority, but the product they have made is a work of traditional American storytelling that preserves the moral gravity of its source. The woke elements are present but peripheral, and they do not change the score."
    },
    "parentalGuidance": "East of Eden is rated TV-MA for adult themes, violence, and some sexual content. The series deals with murder, betrayal, suicide, and the psychological abuse of children. Cathy Ames is a character who abandons her newborn twins and later runs a brothel, and the series does not sanitize this. There are scenes of implied sexual violence and several moments of sudden, realistic violence. The themes are adult: moral responsibility, the inheritance of sin, the nature of evil. This is not a show for children or young teens. Older teenagers who are studying Steinbeck in school may find the adaptation illuminating, but parents should be aware that the series is darker than the 1955 Elia Kazan film adaptation. The language is period-appropriate and not gratuitous. There is no explicit nudity, though Cathy's work in a brothel is clearly established. Families who watch this together will have excellent material for discussing free will, moral choice, jealousy between siblings, and what it means to overcome a difficult family history. The timshel theme -- that you can choose to be good regardless of your circumstances -- makes this one of the more spiritually nutritious prestige dramas available."
}

new_reviews.append(heart_of_the_beast)
new_reviews.append(city_of_god)
new_reviews.append(east_of_eden)

# Add SEO objects separately
heart_of_the_beast["seo"] = {
    "titleTag": "Is Heart of the Beast (2026) Woke? Brad Pitt's Survival Thriller Reviewed | VirtueVigil",
    "metaDescription": "VirtueVigil VVWS review of Heart of the Beast (2026), David Ayer's Alaskan survival thriller starring Brad Pitt and his combat dog Odin. Verdict: BALANCED TRADITIONAL (+8.49 TRAD). Parental guidance included.",
    "keywords": ["is heart of the beast woke", "heart of the beast 2026 review", "heart of the beast virtuevigil", "heart of the beast woke or traditional", "brad pitt heart of the beast", "heart of the beast parents guide", "david ayer heart of the beast"]
}

city_of_god["seo"] = {
    "titleTag": "Is City of God (2002) Woke? The Brazilian Crime Classic Reviewed | VirtueVigil",
    "metaDescription": "VirtueVigil VVWS review of City of God (2002), Fernando Meirelles's Brazilian crime epic set in Rio's favelas. Verdict: BALANCED TRADITIONAL (+5.82 TRAD). Parental guidance included.",
    "keywords": ["is city of god woke", "city of god 2002 review", "city of god virtuevigil", "city of god woke or traditional", "city of god parents guide", "fernando meirelles city of god", "brazilian crime film"]
}

east_of_eden["seo"] = {
    "titleTag": "Is East of Eden (2026) Woke? Netflix's Steinbeck Miniseries Reviewed | VirtueVigil",
    "metaDescription": "VirtueVigil VVWS review of East of Eden (2026), Netflix's limited series adaptation of Steinbeck's novel starring Florence Pugh. Verdict: BALANCED TRADITIONAL (+10.29 TRAD). Parental guidance included.",
    "keywords": ["is east of eden woke", "east of eden 2026 review", "east of eden virtuevigil", "east of eden netflix woke", "florence pugh east of eden", "east of eden parents guide", "steinbeck adaptation 2026"]
}

# Write all three
for review in new_reviews:
    reviews.append(review)

json.dump(reviews, open(REVIEWS_PATH, "w"), indent=2)
print(f"Added {len(new_reviews)} reviews. Total: {len(reviews)}")
for r in new_reviews:
    print(f"  {r['id']}: {r['verdict']} ({r['scoreMargin']})")