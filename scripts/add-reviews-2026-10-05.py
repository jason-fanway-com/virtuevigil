#!/usr/bin/env python3
"""Append 3 reviews to reviews.json for 2026-10-05."""
import json, sys, os

REVIEWS_PATH = "src/data/reviews.json"

# Load existing
with open(REVIEWS_PATH) as f:
    reviews = json.load(f)

existing_slugs = {r["slug"] for r in reviews}
print(f"Existing reviews: {len(reviews)} | slugs: {len(existing_slugs)}")

new_reviews = []

# ============================================================
# REVIEW 1: Forgotten Island (2026) — New Release
# ============================================================
slug1 = "forgotten-island-2026"
if slug1 not in existing_slugs:
    r1 = {
        "id": slug1,
        "slug": slug1,
        "title": "Forgotten Island",
        "year": 2026,
        "type": "movie",
        "platform": "Theaters",
        "genre": "Animated, Fantasy Comedy, Adventure",
        "date": "2026-10-05",
        "datePublised": "2026-10-05",
        "author": "VirtueVigil Editorial Team",
        "readTime": "7 min read",
        "poster": "/images/posters/forgotten-island-2026.jpg",
        "releaseDate": "2026-09-25",
        "rating": "PG",
        "runtime": "109 min",
        "director": "Joel Crawford, Januel Mercado",
        "writers": ["Joel Crawford", "Januel Mercado"],
        "showrunner": None,
        "cast": ["H.E.R.", "Liza Soberano", "Dave Franco", "Jenny Slate", "Manny Jacinto", "Dolly de Leon", "Jo Koy", "Ronny Chieng", "Lea Salonga"],
        "studio": "DreamWorks Animation",
        "distributor": "Universal Pictures",
        "verdict": "BALANCED TRADITIONAL",
        "wokeScore": 0.70,
        "tradScore": 12.32,
        "authIndex": 95,
        "scoreMargin": "+11.62 TRAD",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": "Forgotten Island contains no woke trap. The film is exactly what it markets itself as from the opening frames: a heartfelt animated adventure about friendship, memory, and Filipino folklore. There is no hidden ideological pivot, no third-act agenda delivery. Its celebration of Philippine mythology and female friendship is organic to the story and never weaponized for political messaging.",
        "tropeAudit": [
            {
                "id": "FORG-TRAD-001",
                "name": "Heritage over Innovation",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "explanation": "The entire film is built on Philippine mythology. The world of Nakali draws from pre-colonial Filipino folklore including the Manananggal, diwatas, and tikbalangs. Rather than inventing a generic fantasy realm, Crawford and Mercado rooted their world in specific cultural heritage. The solution to every crisis lies in understanding and honoring these traditions, not in replacing them with something new."
            },
            {
                "id": "FORG-TRAD-002",
                "name": "The Wise Elder",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 3.78,
                "explanation": "Fatima, Jo's grandmother, is the film's moral and narrative anchor. Her stories of Nakali are not presented as quaint folklore to be outgrown but as essential truth that saves the protagonists. Even after her death, her wisdom guides the girls through the mystical world. This is a grandmother treated with genuine reverence, not the wisecracking 'cool grandma' trope."
            },
            {
                "id": "FORG-TRAD-003",
                "name": "The Self-Sacrificing Hero",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.10,
                "explanation": "Jo and Raissa each risk their safety, and potentially their shared memories, to rescue the other from the dangers of Nakali. The film's central question is whether preserving a friendship is worth the ultimate cost, and both characters answer yes without hesitation."
            },
            {
                "id": "FORG-TRAD-004",
                "name": "Traditional Femininity",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 1.40,
                "explanation": "The friendship between Jo and Raissa is built on emotional support, creativity, and nurturing each other through grief and change. Their matching charm bracelets, crafted by hand, symbolize a bond rooted in care rather than competition. Neither girl dominates the other; they complement each other's strengths."
            },
            {
                "id": "FORG-WOKE-001",
                "name": "Chosen Friendship as Narrative Priority",
                "category": "Woke",
                "severity": 1,
                "authenticity": "Moderate",
                "centrality": "Low",
                "weightedScore": 0.50,
                "explanation": "A faint echo of 'chosen family over bio-kin' appears when Raissa's mother disapproves of her friendship with Jo and Raissa chooses to maintain the bond anyway. However, this is framed as a specific mother-daughter tension rather than a broad indictment of family structures. The film also honors Jo's relationship with her grandmother as sacred. The friendship itself is not presented as a replacement for family but as a complement to it."
            },
            {
                "id": "FORG-WOKE-002",
                "name": "Institutional Education as Antagonist",
                "category": "Woke",
                "severity": 1,
                "authenticity": "Moderate",
                "centrality": "Low",
                "weightedScore": 0.20,
                "explanation": "The film opens with a classmate mocking Jo's presentation about Nakali, and a school system that treats her cultural knowledge as a disruption. This is a very minor note that resolves quickly and never returns as a theme. Scored low because it is essentially set dressing in the opening act."
            }
        ],
        "summary": {
            "overall": "Forgotten Island is DreamWorks Animation's most culturally specific film since the Prince of Egypt, and it shares with that earlier work a genuine reverence for its source material that transcends the typical kids'-movie treatment of folklore as exotic wallpaper. Set in the 1990s Philippines, the story follows Jo and Raissa, two best friends who find themselves trapped in Nakali, a mystical realm drawn from pre-colonial Filipino mythology. Jo's grandmother Fatima spent her life telling stories of this hidden world, and after her death, the girls discover that those stories were not just tales but maps. The animation is lush and painterly, with character designs that feel handcrafted and environments that glow with the humid light of Southeast Asian jungles and seas. H.E.R. brings warmth and stubbornness to Jo, while Liza Soberano's Raissa is the more cautious counterweight. The film's great achievement is that it treats Filipino mythology not as a novelty but as a living tradition. The creatures of Nakali, voiced by a strong ensemble including Jo Koy, Ronny Chieng, and the legendary Lea Salonga, are rendered with personality and stakes. At 109 minutes the pacing sometimes drags through the middle act, and the film has underperformed at the box office ($38 million against an $80 million budget), which may say more about marketing than quality. This is a film that believes in heritage, friendship, and the wisdom of grandmothers, and it is all the better for it.",

            "wokeSummary": "Forgotten Island carries almost no ideological baggage. Its two female leads are well-drawn individuals rather than vehicles for girl-boss posturing. The film's celebration of Filipino culture comes from a place of pride rather than grievance, which distinguishes it from the more common 'marginalized culture's revenge' template. There is a brief moment where a classmate mocks Jo's cultural presentation and the school system sides against her, but this is resolved almost immediately and never expanded into a systemic critique. Raissa's mother expresses disapproval of the friendship, hinting faintly at a 'chosen family' dynamic, but the film balances this by treating Jo's bond with her grandmother Fatima as sacred and irreplaceable. The emotional core remains intergenerational and family-centered. No gender ideology, no climate messaging, no anti-Western subtext. The film simply wants to tell a story about friendship and memory, and it does so without a hidden agenda.",

            "tradSummary": "Forgotten Island is rich with traditional themes, beginning with its treatment of Philippine mythology as inherited wisdom rather than quaint superstition. Fatima, the grandmother, is the moral center of the film: her stories prove to be literally true and her love is the force that guides the protagonists through danger. This is Heritage over Innovation at full strength. The friendship between Jo and Raissa is built on mutual care, emotional honesty, and small acts of devotion (the charm bracelets they make for each other). Neither girl is masculinized; their strengths are complementary rather than competitive. The film's central conflict asks whether preserving what matters is worth personal sacrifice, and the answer is an unambiguous yes. There is no subversion of family, no mockery of tradition, no ironic distance from the culture being depicted. For parents looking for an animated film that respects heritage, honors elders, and presents female friendship without ideological additives, Forgotten Island delivers.",

            "verdictExplanation": "Forgotten Island earns a BALANCED TRADITIONAL verdict with a margin of +11.62 points. The traditional tropes are substantial and organic: the film is built on Heritage over Innovation (5.04), venerates a Wise Elder grandmother (3.78), and centers on Self-Sacrificing Heroism (2.10) and Traditional Femininity (1.40). The woke elements are minimal: a faint echo of Chosen Family (0.50) and a brief classroom misunderstanding (0.20) that never develop into sustained ideological critique. This is a culturally grounded animated film that respects its source material and its audience without preaching.",

            "parentalGuidance": "Forgotten Island is rated PG and is appropriate for children 7 and up. The film contains some intense sequences in the mystical world of Nakali, including encounters with the Manananggal (a creature from Philippine folklore that can detach its upper body) that may frighten very young viewers. The death of Jo's grandmother Fatima is handled with sensitivity but may prompt questions about loss. There is no profanity, no sexual content, and the violence is limited to fantasy action sequences with magical creatures. The film's themes of friendship, memory, and cultural heritage provide rich material for family discussion. The Philippine setting and incorporation of Tagalog phrases offers an organic opportunity to introduce children to a culture they may not be familiar with. Parents should know that one minor subplot involves Raissa's mother disapproving of her friendship with Jo, which may resonate with children navigating peer relationships and parental expectations."
        },
        "seo": {
            "titleTag": "Is Forgotten Island (2026) Woke? DreamWorks' Filipino Fantasy Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS review of Forgotten Island (2026). DreamWorks Animation's Philippine mythology fantasy about two friends trapped in a mystical world. Trope scores, verdict: BALANCED TRADITIONAL (+11.62 TRAD). Parental guidance included.",
            "keywords": "is forgotten island woke, forgotten island 2026 review, forgotten island dreamworks, forgotten island virtuevigil, forgotten island traditional or woke, joel crawford forgotten island, forgotten island parents guide, forgotten island filipino mythology"
        }
    }
    new_reviews.append(r1)
    print(f"  + {slug1}")

# ============================================================
# REVIEW 2: The Big Lebowski (1998) — Catalog Backfill
# ============================================================
slug2 = "the-big-lebowski-1998"
if slug2 not in existing_slugs:
    r2 = {
        "id": slug2,
        "slug": slug2,
        "title": "The Big Lebowski",
        "year": 1998,
        "type": "movie",
        "platform": "Streaming / Home Video",
        "genre": "Comedy, Crime, Noir",
        "date": "2026-10-05",
        "datePublised": "2026-10-05",
        "author": "VirtueVigil Editorial Team",
        "readTime": "8 min read",
        "poster": "/images/posters/the-big-lebowski-1998.jpg",
        "releaseDate": "1998-03-06",
        "rating": "R",
        "runtime": "117 min",
        "director": "Joel Coen, Ethan Coen",
        "writers": ["Ethan Coen", "Joel Coen"],
        "showrunner": None,
        "cast": ["Jeff Bridges", "John Goodman", "Julianne Moore", "Steve Buscemi", "John Turturro", "Philip Seymour Hoffman", "Sam Elliott", "David Huddleston"],
        "studio": "Working Title Films",
        "distributor": "Gramercy Pictures",
        "verdict": "BALANCED TRADITIONAL",
        "wokeScore": 0.50,
        "tradScore": 3.50,
        "authIndex": 87,
        "scoreMargin": "+3.00 TRAD",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": "The Big Lebowski contains no woke trap. The Coen brothers' shaggy-dog noir comedy is a film about nothing in particular and everything at once, and its satire is too omnidirectional to function as a delivery vehicle for any ideology. Viewers who encounter the film expecting a hidden political agenda will find only a man who wants his rug back.",
        "tropeAudit": [
            {
                "id": "TBL-TRAD-001",
                "name": "The Rugged Individualist",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 1.40,
                "explanation": "Jeffrey 'The Dude' Lebowski solves his problems entirely outside institutional channels. He does not call the police about the rug theft, the kidnapping, or any of the escalating chaos. He navigates the world through a personal code of bowling, cannabis, and white Russians. The Dude is not anti-establishment in a political sense; he is simply outside the establishment, living on his own terms with complete indifference to status or approval."
            },
            {
                "id": "TBL-TRAD-002",
                "name": "Defense of the Innocent",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.70,
                "explanation": "Despite his lethargy, The Dude repeatedly acts to protect others: he tries to rescue Bunny (who does not actually need rescuing), he stands by Donny, and he refuses to abandon Walter even when Walter's decisions make everything worse. His protective instinct is understated but consistent. He is a caretaker in a bathrobe."
            },
            {
                "id": "TBL-TRAD-003",
                "name": "Small-Town Integrity",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.70,
                "explanation": "The bowling alley functions as the film's moral center, a community of regulars who know each other and maintain their own informal order. It provides more genuine human connection than any institution in the film, including the police, the Lebowski mansion, or the art world."
            },
            {
                "id": "TBL-TRAD-004",
                "name": "The Forgiving Heart",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.70,
                "explanation": "The Dude forgives almost everyone by the film's end. He forgives Walter for the chaos he causes. He forgives Maude for using him. He holds no lasting grudge against the Big Lebowski. His defining line, 'The Dude abides,' is essentially a statement of peaceful acceptance. This is Christian forgiveness filtered through a haze of cannabis smoke."
            },
            {
                "id": "TBL-WOKE-001",
                "name": "Sexual Liberation as Transaction",
                "category": "Woke",
                "severity": 1,
                "authenticity": "Moderate",
                "centrality": "Low",
                "weightedScore": 0.50,
                "explanation": "Maude Lebowski (Julianne Moore) treats sex as a purely transactional and procreative act, detached from intimacy or commitment. She conceives a child with The Dude with no intention of involving him in its upbringing, framing this as feminist autonomy. However, the Coens present Maude as an object of satire rather than admiration. Her avant-garde art, her sterile approach to reproduction, and her contempt for 'the male myth' are all played for laughs. The film does not endorse her worldview; it finds her as ridiculous as everyone else."
            }
        ],
        "summary": {
            "overall": "The Big Lebowski is the Coen brothers' shaggy-dog masterpiece, a film that opened to mixed reviews and modest box office in 1998 and has since become one of the most beloved American comedies ever made. Jeff Bridges plays Jeffrey Lebowski, known to everyone as The Dude, a Los Angeles slacker whose primary occupations are bowling, drinking white Russians, and listening to Creedence. When thugs mistake him for a different Jeffrey Lebowski (a millionaire philanthropist) and urinate on his rug, The Dude sets out to get compensation, triggering a chain of events involving a fake kidnapping, German nihilists, a severed toe, and a lot of bowling. The plot, lifted loosely from Raymond Chandler's The Big Sleep, barely matters, and that is the point. What matters is The Dude's philosophy: an unshakable commitment to taking it easy. John Goodman delivers a volcanic performance as Walter Sobchak, a Vietnam veteran who converts to Judaism and responds to every situation with absolute certainty and almost always catastrophic results. Steve Buscemi's Donny is the film's secret heart, a man who just wants to bowl and keeps getting dragged into chaos he never asked for. The film's genius is that it satirizes everyone equally: the rich, the poor, the artists, the veterans, the nihilists, the cops, the pornographers, and the audience. No one gets out clean, and no one is supposed to.",

            "wokeSummary": "The Big Lebowski is almost entirely free of woke content, which is remarkable for a film set in Los Angeles in the late 1990s. The Coens' satire is omnidirectional, and their target is human folly in all its forms rather than any particular political philosophy. Maude Lebowski comes closest to a woke archetype: a feminist performance artist who speaks of her 'vaginal' art and treats reproduction as a solo project. But the Coens are not endorsing her. They are laughing at her, just as they laugh at The Dude's sloth, Walter's intensity, and the nihilists' commitment to believing in nothing. The film's most overt ideological statement comes from the nihilists themselves, who are the unambiguous villains and whose philosophy is presented as empty and destructive. The Dude's response to their manifesto ('That must be exhausting') is the film's thesis: ideology of any kind is too much work. This is not conservatism or progressivism. It is a coherent philosophy of non-participation that has aged remarkably well.",

            "tradSummary": "Beneath the profanity, the cannabis, and the bowling arguments, The Big Lebowski is built on a surprisingly traditional foundation. The Dude is a Rugged Individualist who solves problems on his own terms, outside any system or hierarchy. He is also, in his own way, a defender of the innocent: he protects Donny, tries to rescue Bunny, and never abandons Walter despite Walter's near-constant catastrophes. The bowling alley serves as the film's version of Small-Town Integrity, a community of regulars who maintain their own order without institutional mediation. And The Dude's defining trait is forgiveness. He absorbs insult, injury, and indignity without bitterness. 'The Dude abides' is not passivity. It is a moral stance: the decision to accept the world as it is rather than rage against it. The friendship between The Dude, Walter, and Donny is one of cinema's great male bonds, built on loyalty that survives Walter's stupidity, The Dude's lethargy, and Donny's confusion. The film ends with a scattering of ashes and a hug. It earns the emotion it pretends not to have.",

            "verdictExplanation": "The Big Lebowski earns a BALANCED TRADITIONAL verdict with a margin of +3.00 points. Traditional tropes include the Rugged Individualist (1.40), Defense of the Innocent (0.70), Small-Town Integrity (0.70), and the Forgiving Heart (0.70). The sole woke element, Maude's Sexual Liberation as Transaction (0.50), is presented satirically and does not represent the film's perspective. The low scores on both sides reflect the film's essential apolitical nature. The Coens are not advancing an ideology; they are observing human absurdity. The traditional lean comes from the film's quiet celebration of friendship, forgiveness, and living on one's own terms.",

            "parentalGuidance": "The Big Lebowski is rated R and is not appropriate for children. The film contains pervasive profanity (including near-constant use of the F-word), drug use (The Dude smokes cannabis throughout), brief nudity, and sexual content (Maude's conception scene is clinical but explicit). There is also comedic violence including a scene where a character's toe is severed, a character is shot, and several physical altercations. The film's themes include nihilism and suicide, though both are treated satirically. The Dude's lifestyle is presented as charming but should not be confused with a recommendation. For teenagers, the film can serve as an entry point for discussions about satire, the difference between the filmmaker's perspective and a character's perspective, and the cultural context of post-Cold War Los Angeles. Parents who are comfortable with the R-rated content will find no hidden ideological messaging: the Coens mock everyone equally."
        },
        "seo": {
            "titleTag": "Is The Big Lebowski (1998) Woke? Coen Brothers Classic Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS review of The Big Lebowski (1998). The Coen brothers' cult comedy starring Jeff Bridges as The Dude. Trope scores, verdict: BALANCED TRADITIONAL (+3.00 TRAD). Parental guidance included.",
            "keywords": "is the big lebowski woke, the big lebowski 1998 review, big lebowski virtuevigil, the big lebowski traditional or woke, coen brothers the big lebowski, the big lebowski parents guide, the dude jeff bridges review"
        }
    }
    new_reviews.append(r2)
    print(f"  + {slug2}")

# ============================================================
# REVIEW 3: Network (1976) — Catalog Backfill
# ============================================================
slug3 = "network-1976"
if slug3 not in existing_slugs:
    r3 = {
        "id": slug3,
        "slug": slug3,
        "title": "Network",
        "year": 1976,
        "type": "movie",
        "platform": "Streaming / Home Video",
        "genre": "Satire, Black Comedy, Drama",
        "date": "2026-10-05",
        "datePublised": "2026-10-05",
        "author": "VirtueVigil Editorial Team",
        "readTime": "8 min read",
        "poster": "/images/posters/network-1976.jpg",
        "releaseDate": "1976-11-27",
        "rating": "R",
        "runtime": "121 min",
        "director": "Sidney Lumet",
        "writers": ["Paddy Chayefsky"],
        "showrunner": None,
        "cast": ["Faye Dunaway", "William Holden", "Peter Finch", "Robert Duvall", "Wesley Addy", "Ned Beatty", "Beatrice Straight"],
        "studio": "Metro-Goldwyn-Mayer",
        "distributor": "United Artists",
        "verdict": "BALANCED TRADITIONAL",
        "wokeScore": 4.60,
        "tradScore": 8.89,
        "authIndex": 66,
        "scoreMargin": "+4.29 TRAD",
        "preRelease": False,
        "wokeTrap": False,
        "woke_trap_assessment": "Network contains no woke trap. Paddy Chayefsky's satire of television and corporate power announces its intentions from the first scene. Howard Beale's mental breakdown and subsequent exploitation by the network is shocking but never hidden. The film wears its fury on its sleeve. There is no bait-and-switch; the audience knows exactly what kind of film they are watching within the first ten minutes.",
        "tropeAudit": [
            {
                "id": "NET-TRAD-001",
                "name": "Biblical Morality",
                "category": "Traditional",
                "severity": 4,
                "authenticity": "High",
                "centrality": "High",
                "weightedScore": 5.04,
                "explanation": "Howard Beale's broadcasts are framed as prophetic warnings, not political speeches. He does not advocate for a policy; he calls the nation to moral awakening. His famous 'I'm as mad as hell and I'm not going to take this anymore' is a Jeremiad, a call to repentance rooted in the tradition of Old Testament prophets. The character is explicitly positioned as a modern-day seer whose message is not ideological but moral."
            },
            {
                "id": "NET-TRAD-002",
                "name": "Sanctity of Marriage",
                "category": "Traditional",
                "severity": 3,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 2.10,
                "explanation": "Max Schumacher's marriage to Louise is presented as the film's only stable human relationship. His affair with Diana Christensen is depicted as a destructive descent into a cold, transactional world. When Max leaves Diana and returns to Louise, the film treats this not as cowardice but as a return to sanity. Louise's monologue about the meaning of a long marriage (which won Beatrice Straight an Oscar in under six minutes of screen time) is one of the most powerful defenses of marital commitment in American cinema."
            },
            {
                "id": "NET-TRAD-003",
                "name": "The Self-Sacrificing Hero",
                "category": "Traditional",
                "severity": 2,
                "authenticity": "High",
                "centrality": "Moderate",
                "weightedScore": 1.40,
                "explanation": "Max Schumacher repeatedly sacrifices his position, his reputation, and ultimately his career to protect Howard Beale from the network's exploitation. He fails, but his failure is not presented as inevitable or as a reason not to try. His moral stand, however futile, is the film's ethical center."
            },
            {
                "id": "NET-TRAD-004",
                "name": "The Forgiving Heart",
                "category": "Traditional",
                "severity": 1,
                "authenticity": "High",
                "centrality": "Low",
                "weightedScore": 0.35,
                "explanation": "After Max ends his affair with Diana, he does not condemn her. He recognizes her as a product of the system that created her: 'You are television incarnate, Diana, indifferent to suffering, insensitive to joy.' This is not forgiveness in the redemptive sense but rather a refusal to hate, a recognition that Diana is as much a victim of the corporate machine as anyone else."
            },
            {
                "id": "NET-WOKE-001",
                "name": "The Evil Capitalist",
                "category": "Woke",
                "severity": 3,
                "authenticity": "Moderate",
                "centrality": "High",
                "weightedScore": 3.60,
                "explanation": "The corporation CCA and its executives, particularly Frank Hackett (Robert Duvall) and Arthur Jensen (Ned Beatty), are portrayed as entities that strip human beings of their dignity in service of profit. Jensen's famous monologue about the 'corporate cosmology' frames capitalism as a religion that replaces God with the balance sheet. Chayefsky's critique is specific: he targets the dehumanizing logic of corporate consolidation, not free markets per se. But the film's rhetoric occasionally bleeds into a broader anti-capitalist sentiment, particularly in Jensen's speech, which presents international capital as an amoral force that has rendered nations and individuals obsolete."
            },
            {
                "id": "NET-WOKE-002",
                "name": "Sexual Liberation as Empowerment",
                "category": "Woke",
                "severity": 2,
                "authenticity": "Moderate",
                "centrality": "Low",
                "weightedScore": 1.00,
                "explanation": "Diana Christensen treats sex as a power transaction and schedules her orgasms around ratings meetings. Her approach to relationships is entirely instrumental. However, the film does not celebrate this; it diagnoses it as pathology. Diana's sexual 'liberation' is presented as a symptom of her dehumanization by the television industry, not as a model to emulate. The contrast with Max's loving marriage to Louise makes this critique explicit."
            }
        ],
        "summary": {
            "overall": "Network is the angriest comedy ever made, a film that predicted the merger of news and entertainment so precisely that watching it in 2026 feels less like satire and more like prophecy fulfilled. Paddy Chayefsky's screenplay, which won him his third Academy Award, follows the descent of the UBS television network into moral bankruptcy after its longtime news anchor Howard Beale (Peter Finch, in a posthumous Oscar-winning performance) announces on air that he will kill himself. When ratings spike, the network's programming executive Diana Christensen (Faye Dunaway) seizes on Beale's breakdown as entertainment gold, transforming him from a respected journalist into a 'mad prophet of the airwaves.' Meanwhile, network news president Max Schumacher (William Holden) watches in horror as the institution he built is gutted for profit by the corporate conglomerate CCA. The film is structured as a series of increasingly unhinged monologues, each one more prescient than the last: Beale's populist rage, Jensen's corporate cosmology, Diana's ratings-is-God philosophy. Sidney Lumet directs with the controlled fury of a man who has seen the future and is trying to warn us. The performances are uniformly extraordinary: Finch's trembling fury, Dunaway's icy ambition, Holden's wounded decency, and Beatrice Straight's devastating five-minute turn as Max's wife, which remains the shortest performance ever to win an acting Oscar. Network is occasionally too much -- too loud, too rhetorical, too convinced of its own importance. But it earns that conviction. The film was right about everything.",

            "wokeSummary": "Network occupies an unusual position: its critique of corporate power and the commodification of human emotion aligns with certain left-wing arguments, but its moral framework is fundamentally traditional. The film has two significant woke-coded elements. The first is its depiction of CCA as an amoral corporate entity that prioritizes profit over human dignity, which maps onto the Evil Capitalist trope. Chayefsky, however, was not a Marxist. His critique is humanist: he objects to the way corporate logic strips people of their humanity, not to capitalism as an economic system. The second element is Diana Christensen's sexual behavior, which fits the Sexual Liberation as Empowerment template. But again, the film does not endorse Diana; it diagnoses her. Her cold, transactional approach to sex is presented as a symptom of the same dehumanizing force that turns Beale's mental illness into programming. The film's most striking scene in this regard is not Diana's seduction of Max but Louise's monologue about what a real marriage means. Network is a film that uses the language of corporate critique to advance what is ultimately a conservative argument: that human beings need moral anchors, that institutions should serve people rather than the reverse, and that some things (dignity, love, the truth) are not for sale.",

            "tradSummary": "For all its reputation as a radical film, Network is deeply conservative in its moral vision. The central metaphor of Howard Beale as a prophet calling the nation to repentance is Biblical Morality operating at full strength. Beale does not advocate for a political program; he demands moral awakening. His rants are Jeremiads, a form that stretches back to the Old Testament and forward to the American jeremiad tradition of Jonathan Edwards and Martin Luther King Jr. The film's treatment of marriage is equally traditional. Max Schumacher's marriage to Louise is presented as the only intact sanctuary in the film's moral landscape, and his affair with Diana is a descent into a cold, dehumanized world. When he returns to Louise, it is not a defeat but a homecoming. Louise's monologue about the meaning of a shared life together is one of the most powerful defenses of marital commitment in American cinema. Max himself is a Self-Sacrificing Hero who gives up his position to protect Beale, and while he ultimately fails, the film treats his effort as noble rather than naive. The Forgiving Heart appears in his final conversation with Diana, where he refuses to condemn her even as he leaves her, recognizing her as a product of the machine that made her. Network's traditionalism is not cultural or political conservatism. It is deeper than that: a belief that human beings require moral grounding, that love and loyalty matter more than ratings, and that a society that forgets these things is already dead.",

            "verdictExplanation": "Network earns a BALANCED TRADITIONAL verdict with a margin of +4.29 points. The traditional tropes are anchored by Biblical Morality in Beale's prophetic rants (5.04), the Sanctity of Marriage embodied in Max's return to Louise (2.10), Max's Self-Sacrificing Heroism (1.40), and the Forgiving Heart (0.35). The woke elements come from the Evil Capitalist depiction of CCA (3.60) and Diana's Sexual Liberation as Empowerment (1.00). The traditional side prevails because the film's moral framework, despite its anti-corporate rhetoric, is built on timeless values: truth, loyalty, commitment, and the irreducible dignity of the human person. Chayefsky was a humanist who believed in moral absolutes, and Network is a traditionalist's critique of modern media dressed in the language of satire.",

            "parentalGuidance": "Network is rated R and contains adult themes throughout. There is profanity, including several uses of the F-word. The film deals frankly with mental illness, suicide (Beale's on-air announcement of his planned suicide), adultery (Max's affair with Diana is depicted including a bedroom scene with brief nudity), and the moral corruption of institutions. There is also violence, including Beale's on-air assassination at the film's climax. The film's tone is profoundly cynical, and its depiction of a media landscape that exploits human suffering for profit may be disturbing to sensitive viewers. For mature teenagers, Network offers an extraordinary entry point for discussions about media literacy, the relationship between commerce and truth, and the moral responsibility of institutions. The film argues, with considerable force, that some things should not be for sale. That is a conversation worth having."
        },
        "seo": {
            "titleTag": "Is Network (1976) Woke? Sidney Lumet's Prophetic Satire Reviewed | VirtueVigil",
            "metaDescription": "VirtueVigil's full VVWS review of Network (1976). Paddy Chayefsky and Sidney Lumet's Oscar-winning media satire. Trope scores, verdict: BALANCED TRADITIONAL (+4.29 TRAD). Parental guidance included.",
            "keywords": "is network woke, network 1976 review, network sidney lumet, network virtuevigil, network traditional or woke, paddy chayefsky network, network parents guide, howard beale mad as hell"
        }
    }
    new_reviews.append(r3)
    print(f"  + {slug3}")

if not new_reviews:
    print("ERROR: All 3 slugs already exist!")
    sys.exit(1)

# Append and write
reviews.extend(new_reviews)
with open(REVIEWS_PATH, "w") as f:
    json.dump(reviews, f, indent=2)

print(f"\nDone. {len(reviews)} total reviews (was {len(reviews) - len(new_reviews)}, +{len(new_reviews)}).")