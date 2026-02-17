const fs = require('fs');
const path = require('path');

const reviewsPath = path.join(__dirname, 'src/data/reviews.json');
const reviews = JSON.parse(fs.readFileSync(reviewsPath, 'utf8'));

const newReviews = [
  {
    "id": "crime-101-2026",
    "slug": "crime-101-2026",
    "title": "Crime 101",
    "year": 2026,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Crime, Thriller",
    "date": "2026-02-17",
    "author": "VirtueVigil Editorial Team",
    "readTime": "14 min",
    "poster": "/images/posters/crime-101-2026.jpg",
    "verdict": "MIXED",
    "wokeScore": 6,
    "tradScore": 8,
    "authIndex": 72,
    "scoreMargin": "+2 TRAD",
    "wokeTrap": {
      "present": false,
      "degree": null,
      "explanation": "Crime 101 is not hiding an ideological agenda behind genre packaging. This is a straightforward crime thriller that wears its Michael Mann influences on its sleeve. The social commentary is present but secondary to the heist mechanics and character dynamics. Conservative viewers who enjoy a well-crafted crime film will not feel ambushed.",
      "viewerSentiment": null
    },
    "woke_trap_assessment": {
      "is_trap": false,
      "explanation": "Crime 101 is not hiding an ideological agenda behind genre packaging. This is a straightforward crime thriller that wears its Michael Mann influences on its sleeve. The social commentary is present but secondary to the heist mechanics and character dynamics."
    },
    "creative_team": {
      "director": {
        "name": "Bart Layton",
        "ideology": "NEUTRAL",
        "profile": "English filmmaker who made his name in documentaries before crossing into narrative features. His work is defined by a fascination with deception, identity, and the blurry line between truth and performance. He is not a political filmmaker. Three films, all centered on theft, deception, and consequences. No consistent political agenda."
      },
      "writer": {
        "name": "Bart Layton (with Peter Straughan contributions)",
        "profile": "Layton adapted Don Winslow's novella with contributions from Peter Straughan (Tinker Tailor Soldier Spy, Our Brand Is Crisis). The screenplay adds the workplace sexism subplot and the police corruption elements."
      },
      "lead_producer": {
        "name": "Tim Bevan & Eric Fellner",
        "company": "Working Title Films"
      },
      "composer": {
        "name": "Blanck Mass (Benjamin John Power)"
      },
      "top_cast": [
        { "name": "Chris Hemsworth", "role": "Mike / James Davis" },
        { "name": "Mark Ruffalo", "role": "Det. Lou Lubesnick" },
        { "name": "Halle Berry", "role": "Sharon Combs" },
        { "name": "Barry Keoghan", "role": "Ormon" },
        { "name": "Nick Nolte", "role": "Money" }
      ],
      "prediction": {
        "verdict": "TRADITIONAL-LEANING",
        "confidence": "moderate"
      },
      "producers": [
        { "name": "Tim Bevan & Eric Fellner", "company": "Working Title Films", "profile": "Britain's leading prestige house. Output ranges from romantic comedies to war films to crime thrillers. Ideologically mixed." },
        { "name": "Dimitri Doganis", "company": "Raw TV", "profile": "Layton's producing partner. Background in documentary and reality television. No political signal." },
        { "name": "Shane Salerno", "company": "The Story Factory", "profile": "Literary manager and producer. Represents Don Winslow. No consistent ideological signal." },
        { "name": "Chris Hemsworth & Ben Grayson", "profile": "Hemsworth produces through his banner. His production choices suggest an affinity for action and genre material rather than political projects." }
      ],
      "full_cast": [
        { "name": "Chris Hemsworth", "role": "Mike / James Davis" },
        { "name": "Mark Ruffalo", "role": "Det. Lou Lubesnick" },
        { "name": "Halle Berry", "role": "Sharon Combs" },
        { "name": "Barry Keoghan", "role": "Ormon" },
        { "name": "Monica Barbaro", "role": "Maya" },
        { "name": "Corey Hawkins", "role": "Det. Tillman" },
        { "name": "Jennifer Jason Leigh", "role": "Angie" },
        { "name": "Nick Nolte", "role": "Money" },
        { "name": "Tate Donovan", "role": "Steven Monroe" },
        { "name": "Devon Bostick", "role": "Devon" },
        { "name": "Payman Maadi", "role": "Sammy Kassem" },
        { "name": "Babak Tafti", "role": "Ali" },
        { "name": "Deborah Hedwall", "role": "Anne" },
        { "name": "Paul Adelstein", "role": "Mark" },
        { "name": "Drew Powell", "role": "Det. Townsend" },
        { "name": "Matthew Del Negro", "role": "Police Captain Stewart" },
        { "name": "Andra Nechita", "role": "Adrienne" },
        { "name": "John Douglas", "role": "Grant" }
      ]
    },
    "fidelity_casting": {
      "score": "ADJUSTED",
      "summary": "Sharon's race change from the source novella is the primary casting alteration, though it does not materially damage the story.",
      "detailed_analysis": "The primary casting question involves Halle Berry as Sharon Combs. In Winslow's novella, Sharon's race is not specified as central to her character. Casting Berry adds a dimension of racial representation without the film explicitly engaging with it. Mike Davis (Chris Hemsworth) tracks with the source material. Det. Lou Lubesnick (Mark Ruffalo) fits the rumpled, dogged character. The casting works dramatically even if it reflects industry diversity priorities."
    },
    "summary": {
      "overall": "Bart Layton's \"Crime 101\" is the kind of movie Hollywood used to make all the time and rarely bothers with anymore. A slick, sun-bleached Los Angeles crime thriller about professionals on both sides of the law, built on competence, tension, and the quiet rhythms of people who are very good at what they do. It owes a massive debt to Michael Mann. The night driving sequences look like outtakes from \"Heat\" and \"Collateral,\" and the central triangle of thief, cop, and reluctant accomplice echoes Mann's fascination with men (and women) defined by their work. The good news is that the debt is mostly paid off. This is a genuinely entertaining film.\n\nChris Hemsworth plays Mike Davis, a jewel thief who plans his scores with surgical precision and refuses to hurt anyone. He targets jewelry stores along the 101 highway, uses detailed intelligence on his targets' families to ensure compliance, and then vanishes. Hemsworth plays him quiet and controlled, miles away from his Thor persona. It works. There is something compelling about watching a physically imposing man exercise restraint rather than force. Mark Ruffalo's Detective Lou Lubesnick is the rumpled, dogged investigator who suspects a single thief is responsible for a string of unsolved robberies but can't get his department to care. And Halle Berry plays Sharon Combs, an insurance broker who has spent decades being passed over, patronized, and sidelined by her firm, and who ultimately agrees to help Mike with one last score.\n\nThe film's strongest material involves the heist mechanics and the cat-and-mouse between Mike and Lou. Layton comes from documentaries (The Imposter, American Animals) and he brings that instinct for grounded detail to the crime sequences. The opening diamond interception is tense and efficient. A car chase midway through the film is legitimately startling because it looks and feels real rather than CGI-glossy. Barry Keoghan's Ormon, a volatile young biker hired by Mike's fence to intercept his next job, provides the wild-card menace that the plot needs. Keoghan is doing his usual unhinged thing and it fits, even if the character is a bit one-note. Nick Nolte shows up as Money, the aging fence, looking rough and sounding rougher. He has maybe ten minutes of screen time and steals every one of them.\n\nWhere the film stumbles slightly is in its social commentary, which is sincere but occasionally heavy-handed. Sharon's workplace subplot hits every beat you expect it to. Her boss is a smirking corporate villain who hands her clients to younger women, cites her age as a liability, and generally behaves like a walking HR violation. When Sharon finally tells him off and quits, it is satisfying on a visceral level, but the setup is so stacked that the moment feels manufactured rather than earned. The film wants us to understand that Sharon turns to crime because \"the system\" failed her. That framing is recognizable as the progressive narrative of institutional failure driving individual transgression. A more traditional reading would note that Sharon makes a choice, a criminal one, and the film never fully grapples with the moral weight of that decision because it is too busy validating her grievance.\n\nSimilarly, the film frames Mike's criminality through a lens of economic disadvantage. He grew up in poverty, cycled through foster homes, and turned to theft because legitimate paths were closed to him. This backstory contextualizes his crimes rather than condemning them. The film is not interested in holding Mike morally accountable in any serious way. He is the cool protagonist, and we are meant to root for him. There is a long tradition of this in crime cinema, from Cary Grant to Steve McQueen to the Ocean's franchise. But Crime 101 adds the progressive garnish of systemic explanation, as if liking a charming thief isn't enough and we also need to understand that society made him this way.\n\nLou's subplot involves police corruption. He is suspended for refusing to help cover up the shooting of another suspect. The department is portrayed as more interested in optics than justice. Lou is the lone honest cop swimming against an institutional tide. This is a familiar trope that plays differently depending on your political lens. Conservatives might read it as a condemnation of bureaucratic rot. Progressives might read it as a critique of policing itself. The film is vague enough to support both readings, which is either admirably balanced or noncommittal, depending on your taste.\n\nBut here is the thing: for all its social commentary, the film's emotional engine runs on entirely traditional fuel. Mike is defined by self-reliance, discipline, and a personal code of honor. He abhors violence. He plans meticulously. He takes pride in his craft. These are fundamentally masculine virtues presented without irony or apology. Lou is a dogged professional who believes in doing the right thing even when his institution does not support him. That is individual moral conviction over institutional pressure, which is about as conservative a value as you can find. The relationship between Mike and Maya, while underdeveloped, is presented as genuinely romantic. Mike's inability to open up is treated as a flaw he needs to overcome, not a strength. The film's ending, in which Mike sends Maya a childhood photo asking for a second chance, is a small, human gesture that argues for vulnerability and connection over isolation. And the final resolution, where Lou lets Mike walk but ensures Sharon gets a fresh start, operates on a code of personal honor rather than institutional justice. Lou doesn't follow the rules. He follows his conscience. That is an old-fashioned moral framework dressed in modern clothes.\n\nConservative viewers should find more to enjoy here than to bristle at. The social commentary is present but it never overwhelms the genre pleasures. This is a film about competent people doing interesting things, shot beautifully, scored with driving electronic music, and anchored by three performers who take the material seriously. It is not trying to lecture you. It is trying to entertain you, and mostly succeeding. The woke elements are real but they sit alongside, rather than on top of, a fundamentally traditional crime narrative. Layton respects the genre too much to subordinate it entirely to a message.",
      "adultInsight": "Conservative viewers should approach Crime 101 as what it primarily is: a well-crafted genre thriller in the tradition of Heat, Thief, and the better Ocean's films. Bart Layton is not Steve McQueen. He is not using the crime genre as a vehicle for racial critique or institutional deconstruction. He is making a crime movie with the tools and sensibilities of contemporary Hollywood, which means some progressive seasoning is baked in. But it never overwhelms the dish. The workplace sexism subplot is the most overtly woke element, and even there, Berry's performance and the genre context soften the lecture. What conservative viewers will appreciate is the film's genuine respect for competence, self-reliance, personal honor, and masculine virtue.",
      "parentalGuidance": "Crime 101 is rated R for language throughout, some violence, and sexual material/nudity. Common Sense Media recommends age 15+. Violence includes a high-speed car chase with a vehicle flipping, a shooting in a hotel suite, and a character beaten to death. Barry Keoghan's Ormon is menacing and physically threatening, including a scene where he violently interrogates Sharon. Strong language is used throughout with frequent f-words. Brief nudity and some sexual material. Not appropriate for children under 13. For teenagers 15 and older, this is a solid conversation starter about moral complexity in storytelling and whether a film can celebrate a character's skills without endorsing their choices."
    },
    "tropeAudit": [
      { "trope": "Redeemed Criminal Systemic", "id": "WOKE-019", "category": "WOKE", "location": "Throughout -- Mike's criminality contextualized through poverty and foster care", "authenticity": "Mixed" },
      { "trope": "The Girl Boss", "id": "WOKE-003", "category": "WOKE", "location": "Sharon's workplace subplot -- crime framed as liberation from sexism", "authenticity": "Mixed" },
      { "trope": "Institutional Evil", "id": "WOKE-004", "category": "WOKE", "location": "Lou's police subplot -- LAPD portrayed as institutionally corrupt", "authenticity": "Mixed" },
      { "trope": "The Bigoted Traditionalist", "id": "WOKE-008", "category": "WOKE", "location": "Sharon's workplace -- boss as cartoonish corporate misogynist", "authenticity": "Low" },
      { "trope": "The Victimhood Meritocracy", "id": "WOKE-009", "category": "WOKE", "location": "Throughout -- all three protagonists positioned as victims of systems", "authenticity": "Mixed" },
      { "trope": "Race-Conscious Casting", "id": "WOKE-022", "category": "WOKE", "location": "Throughout -- Sharon's race changed from source novella", "authenticity": "N/A" },
      { "trope": "Industry and Perseverance", "id": "TRADITIONAL-041", "category": "TRAD", "location": "Throughout -- Mike's meticulous preparation and professional excellence", "authenticity": "Natural" },
      { "trope": "The Self-Sacrificing Hero", "id": "TRADITIONAL-026", "category": "TRAD", "location": "Climax -- Mike kills Ormon to save Lou, sacrifices his score", "authenticity": "Natural" },
      { "trope": "Masculine Competence", "id": "TRADITIONAL-035", "category": "TRAD", "location": "Throughout -- Mike and Lou defined by skill in their domains", "authenticity": "Natural" },
      { "trope": "Personal Honor Code", "id": "TRADITIONAL-029", "category": "TRAD", "location": "Throughout -- Mike's strict no-violence code drives the narrative", "authenticity": "Natural" },
      { "trope": "Romantic Vulnerability", "id": "TRADITIONAL-032", "category": "TRAD", "location": "Mike and Maya's subplot -- emotional openness as growth", "authenticity": "Natural" },
      { "trope": "Defense of the Innocent", "id": "TRADITIONAL-045", "category": "TRAD", "location": "Climax -- Mike breaks his code to protect others", "authenticity": "Natural" },
      { "trope": "Earned Redemption", "id": "TRADITIONAL-040", "category": "TRAD", "location": "Final act -- each character earns resolution through sacrifice", "authenticity": "Natural" },
      { "trope": "Loyalty and Brotherhood", "id": "TRADITIONAL-042", "category": "TRAD", "location": "Climax and resolution -- thief-cop mutual respect", "authenticity": "Natural" }
    ],
    "seo": {
      "titleTag": "Is Crime 101 (2026) Woke? Bart Layton Film Review | VirtueVigil",
      "metaDescription": "Is Crime 101 woke? VirtueVigil's analysis: Woke Score 6, Traditional 8, Fidelity Casting ADJUSTED. Full creative team deep dive, trope audit, and family guidance.",
      "keywords": "is crime 101 woke, crime 101 2026 review, crime 101 movie review conservative, crime 101 chris hemsworth, crime 101 woke score"
    },
    "spoiler_alert": true
  },
  {
    "id": "send-help-2026",
    "slug": "send-help-2026",
    "title": "Send Help",
    "year": 2026,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Horror, Thriller, Comedy",
    "date": "2026-02-17",
    "author": "VirtueVigil Editorial Team",
    "readTime": "12 min",
    "poster": "/images/posters/send-help-2026.jpg",
    "verdict": "MIXED",
    "wokeScore": 6,
    "tradScore": 7,
    "authIndex": 70,
    "scoreMargin": "+1 TRAD",
    "wokeTrap": {
      "present": false,
      "degree": null,
      "explanation": "Despite surface-level eat the rich and anti-corporate framing, the film actually subverts the class warfare narrative. The downtrodden worker who overthrows her entitled boss doesn't become a hero. She becomes a monster. Sam Raimi is not interested in lecturing anyone.",
      "viewerSentiment": null
    },
    "woke_trap_assessment": {
      "is_trap": false,
      "explanation": "Despite surface-level eat the rich and anti-corporate framing, the film subverts the class warfare narrative. The downtrodden worker who overthrows her entitled boss becomes a monster, not a hero. Raimi is interested in entertainment, not lectures."
    },
    "creative_team": {
      "director": {
        "name": "Sam Raimi",
        "ideology": "NEUTRAL",
        "profile": "One of the most durable genre directors in American cinema. He has been making movies since the early 1980s and his ideological footprint across four decades is remarkably light. He is a craftsman, not an activist. His heroes tend to be ordinary people with strong moral instincts."
      },
      "writer": {
        "name": "Mark Swift & Damian Shannon",
        "profile": "Horror/genre writing duo. Credits include Freddy vs. Jason (2003) and Friday the 13th reboot (2009). Genre professionals with no political track record."
      },
      "lead_producer": {
        "name": "Sam Raimi",
        "company": "Raimi Productions"
      },
      "composer": {
        "name": "Danny Elfman"
      },
      "top_cast": [
        { "name": "Rachel McAdams", "role": "Linda Liddle" },
        { "name": "Dylan O'Brien", "role": "Bradley Preston" },
        { "name": "Dennis Haysbert", "role": "Franklin" }
      ],
      "prediction": {
        "verdict": "MIXED",
        "confidence": "moderate"
      },
      "producers": [
        { "name": "Sam Raimi", "company": "Raimi Productions", "profile": "As producer of his own film, the creative vision is unified. No external ideological pressures detectable." },
        { "name": "Zainab Azizi", "profile": "Producer with credits alongside Raimi. No ideological signal detectable." }
      ],
      "full_cast": [
        { "name": "Rachel McAdams", "role": "Linda Liddle" },
        { "name": "Dylan O'Brien", "role": "Bradley Preston" },
        { "name": "Edyll Ismail", "role": "Zuri" },
        { "name": "Xavier Samuel", "role": "Donovan Murphy" },
        { "name": "Chris Pang", "role": "Chase" },
        { "name": "Dennis Haysbert", "role": "Franklin" },
        { "name": "Thaneth Warakulnukroh", "role": "Boat Captain" },
        { "name": "Emma Raimi", "role": "River" },
        { "name": "Kristy Best", "role": "Polly Perera" },
        { "name": "Bruce Campbell", "role": "Bradley's Father (photographs only)" }
      ]
    },
    "fidelity_casting": {
      "score": "N/A",
      "summary": "Original contemporary fiction with no historical or source material to assess.",
      "detailed_analysis": "Send Help is an original contemporary fiction. There is no historical event, literary source, or established IP to assess fidelity against. The casting is straightforward and unremarkable from an ideological standpoint."
    },
    "summary": {
      "overall": "Sam Raimi has been making gloriously unhinged movies for over forty years. From the cabin in the Tennessee woods to the streets of Manhattan to the multiverse itself, the guy has one consistent gear: controlled chaos delivered with a grin. \"Send Help\" is the purest distillation of Raimi's sensibilities since \"Drag Me to Hell.\" It's mean, funny, gory, and surprisingly well-acted. It also happens to contain just enough cultural subtext to warrant a closer look from conservative viewers who are tired of Hollywood using genre films as Trojan horses for progressive messaging.\n\nThe good news? This is not that kind of movie. Not really.\n\nThe setup is simple and effective. Linda Liddle, played by Rachel McAdams, is a brilliant but socially awkward corporate strategist who just got passed over for a promotion by her new boss, Bradley Preston, a nepo-baby CEO played with obnoxious precision by Dylan O'Brien. Bradley gives the VP slot to his fraternity buddy Donovan instead. When a business trip goes wrong and their private jet crashes in the Gulf of Thailand, only Linda and Bradley survive. Stranded on a deserted island with a man who treated her like furniture, Linda discovers that her obsessive fandom of the TV show \"Survivor\" has actually prepared her for this moment. She can fish. She can build shelter. She can hunt wild boar with a homemade spear. Bradley, meanwhile, can barely stand up on his busted leg.\n\nSo far, you might think you know where this is going. Plucky underdog proves her worth, arrogant boss learns humility, they share a moment of mutual respect, rescue arrives, roll credits. That would be the safe version. Raimi has zero interest in the safe version.\n\nWhat actually happens is that Linda gradually reveals herself to be something far more disturbing than a meek office worker finally standing up for herself. She deliberately avoids signaling a passing boat. She poisons Bradley with octopus toxin and stages a fake castration to punish him for trying to escape. When Bradley's fiancee Zuri arrives with a rescue boat, Linda murders both Zuri and the boat captain by pushing them off a cliff. When Bradley discovers Zuri's body, the two engage in a brutal fight that ends with Linda beating Bradley to death with a golf club inside a luxury beach house she'd known about the entire time.\n\nThe film's epilogue is its cruelest joke. One year later, Linda is a wealthy celebrity. She's written a best-selling survival memoir claiming to be the sole plane crash survivor. She drives off to a celebrity golf tournament with her pet cockatiel named \"Sweetie,\" singing along to Blondie's \"One Way or Another.\" She got everything she wanted, and the world is none the wiser.\n\nNow, here's where the ideological picture gets interesting for conservative viewers. On the surface, the film absolutely traffics in class resentment. Bradley is every lazy critique of corporate America personified: a rich kid who inherited his power, promotes his buddies over qualified workers, and treats the little people with open contempt. The \"boys' club\" dynamic is painted in broad strokes. But Raimi, whether intentionally or not, does something that undercuts the progressive reading completely. The oppressed worker who seizes power from the entitled elite doesn't use that power wisely or justly. She uses it to dominate, manipulate, and ultimately murder. Linda isn't a hero reclaiming what's rightfully hers. She's a psychopath who found the right circumstances to let her mask drop. The film even tells you this directly: Linda confesses that she let her abusive husband drink himself into a fatal car crash. She was never the innocent victim. She was always capable of this.\n\nThat's actually a deeply conservative insight wrapped in genre packaging. Power doesn't corrupt because corporations are evil. Power corrupts because human nature is fallen. Linda doesn't become a monster because capitalism failed her. She was always this person. The island just gave her permission.\n\nThe craft on display is top-tier. McAdams is genuinely phenomenal, toggling between pathetic, charming, and terrifying, sometimes within the same scene. O'Brien makes Bradley detestable enough that you initially root for Linda, which is essential for the later gut-punch. Danny Elfman's score is playful and dark in equal measure. Bill Pope's cinematography makes the island look beautiful and menacing at the same time. And Raimi himself is clearly having the time of his life.\n\nFor a January release horror-thriller, \"Send Help\" is shockingly good. It's also refreshingly free of the identity-politics baggage that weighs down so much of modern Hollywood. There's no DEI casting checkbox. No diversity lectures. No hamfisted representation moments. It's two people on an island trying to outlast each other, and the film trusts that premise to carry the full two hours. It does.",
      "adultInsight": "Conservative adult viewers should approach Send Help as a really good time at the movies. This is an original, well-crafted genre film with zero identity politics. There are no diversity speeches, no representation checkboxes, no lectures about systemic anything. The film's eat the rich surface reading is real but shallow. It argues, through Linda's arc, that power simply migrates to whoever is willing to do the most damage to get it. That's not a progressive message. It's a deeply cynical one, and cynicism about human nature has always been more compatible with conservative realism than progressive utopianism. Hollywood needs more films like this and fewer franchise installments with DEI consultants.",
      "parentalGuidance": "This is an R-rated film and the rating is well-earned. Parents should exercise significant caution. Violence is extensive and graphic: a plane crash with passengers sucked from the fuselage, a boar hunted and killed with blood spraying, a staged castration scene, characters pushed off a cliff, eye-gouging, stabbing, choking, and a character beaten to death with a golf club. Approximately 25 f-words and frequent profanity. Brief partial nudity. The film's darkest element for younger viewers is its moral nihilism: the protagonist is a murderer who faces no consequences and profits from her crimes. 17+ only. For older teenagers who see it, parents should discuss how stories manipulate our sympathies and at what point we stop rooting for a character."
    },
    "tropeAudit": [
      { "trope": "The Girl Boss", "id": "WOKE-003", "category": "WOKE", "location": "Throughout -- Linda transforms from meek employee to dominant survivor, initially framed as empowerment", "authenticity": "Mixed" },
      { "trope": "Anti-Corporate Satire / Eat the Rich", "id": "WOKE-012", "category": "WOKE", "location": "Acts one and two -- corporate world portrayed as shallow, nepotistic, and cruel", "authenticity": "Mixed" },
      { "trope": "The Bigoted Traditionalist", "id": "WOKE-008", "category": "WOKE", "location": "First act -- Bradley and Donovan represent fraternity-to-boardroom boys' club", "authenticity": "Mixed" },
      { "trope": "Moral Relativism", "id": "WOKE-023", "category": "WOKE", "location": "Epilogue -- Linda escapes justice entirely, no moral reckoning", "authenticity": "Mixed" },
      { "trope": "The Predatory Male", "id": "WOKE-022", "category": "WOKE", "location": "Mid-film -- Bradley coded as sexual predator in the workplace", "authenticity": "Mixed" },
      { "trope": "Industry and Perseverance / Self-Reliance", "id": "TRADITIONAL-041", "category": "TRAD", "location": "Throughout island sequences -- survival through competence and physical labor", "authenticity": "Natural" },
      { "trope": "Consequences of Moral Failure", "id": "TRADITIONAL-050", "category": "TRAD", "location": "Multiple instances -- bad behavior punished with brutal efficiency", "authenticity": "Natural" },
      { "trope": "The Entitled Are Exposed", "id": "TRADITIONAL-028", "category": "TRAD", "location": "Throughout Bradley's island arc -- stripped of infrastructure, revealed as helpless", "authenticity": "Natural" },
      { "trope": "Human Nature Is Fallen", "id": "TRADITIONAL-047", "category": "TRAD", "location": "Third act revelations -- Linda was always capable of evil, the island gave permission", "authenticity": "Natural" },
      { "trope": "Original Storytelling / Genre Craftsmanship", "id": "TRADITIONAL-038", "category": "TRAD", "location": "The entire film -- original R-rated mid-budget genre film with no franchise attachments", "authenticity": "Natural" }
    ],
    "seo": {
      "titleTag": "Is Send Help (2026) Woke? Sam Raimi Film Review | VirtueVigil",
      "metaDescription": "Is Send Help woke? VirtueVigil's analysis: Woke Score 6, Traditional 7. Sam Raimi's horror-thriller subverts the eat-the-rich narrative. Full trope audit and family guidance.",
      "keywords": "is send help woke, send help 2026 review, send help sam raimi woke, send help movie review conservative, send help rachel mcadams"
    },
    "spoiler_alert": true
  },
  {
    "id": "avatar-fire-and-ash-2025",
    "slug": "avatar-fire-and-ash-2025",
    "title": "Avatar: Fire and Ash",
    "year": 2025,
    "type": "film",
    "platform": "Theatrical",
    "genre": "Science Fiction, Action, Adventure",
    "date": "2026-02-17",
    "author": "VirtueVigil Editorial Team",
    "readTime": "16 min",
    "poster": "/images/posters/avatar-fire-and-ash-2025.jpg",
    "verdict": "WOKE",
    "wokeScore": 9,
    "tradScore": 8,
    "authIndex": 68,
    "scoreMargin": "+1 WOKE",
    "wokeTrap": {
      "present": false,
      "degree": null,
      "explanation": "The Avatar franchise has never hidden its ideological cards. Since 2009, James Cameron has openly described these films as political, environmentalist, and anti-colonialist. Fire and Ash continues that tradition without subterfuge. Conservative viewers will not be ambushed.",
      "viewerSentiment": null
    },
    "woke_trap_assessment": {
      "is_trap": false,
      "explanation": "The Avatar franchise has never hidden its ideological cards. Since 2009, James Cameron has openly described these films as political, environmentalist, and anti-colonialist. Fire and Ash continues that tradition without subterfuge."
    },
    "creative_team": {
      "director": {
        "name": "James Cameron",
        "ideology": "MODERATELY WOKE",
        "profile": "The most commercially successful director in film history. Committed environmentalist who runs sustainability businesses. His ideological signature is consistently anti-corporate, anti-military-industrial, pro-environment, but he simultaneously celebrates traditional family structures, maternal devotion, warrior courage, and self-sacrifice."
      },
      "writer": {
        "name": "James Cameron, Rick Jaffa & Amanda Silver",
        "profile": "Cameron co-wrote with Jaffa & Silver (Rise/Dawn of the Planet of the Apes, Avatar sequels). Story by Josh Friedman and Shane Salerno. The environmental and anti-colonial themes are Cameron's core creative vision."
      },
      "lead_producer": {
        "name": "James Cameron & Jon Landau",
        "company": "Lightstorm Entertainment"
      },
      "composer": {
        "name": "Simon Franglen"
      },
      "top_cast": [
        { "name": "Sam Worthington", "role": "Jake Sully" },
        { "name": "Zoe Saldana", "role": "Neytiri" },
        { "name": "Oona Chaplin", "role": "Varang" },
        { "name": "Sigourney Weaver", "role": "Kiri" },
        { "name": "Stephen Lang", "role": "Colonel Quaritch" }
      ],
      "prediction": {
        "verdict": "WOKE",
        "confidence": "high"
      },
      "producers": [
        { "name": "James Cameron", "company": "Lightstorm Entertainment", "profile": "Total creative control. The ideological signal is Cameron's." },
        { "name": "Jon Landau", "company": "Lightstorm Entertainment", "profile": "Cameron's producing partner since Titanic. Passed away in July 2024 during post-production. Logistics and production executive, not a creative voice." }
      ],
      "full_cast": [
        { "name": "Sam Worthington", "role": "Jake Sully" },
        { "name": "Zoe Saldana", "role": "Neytiri" },
        { "name": "Sigourney Weaver", "role": "Kiri / Dr. Grace Augustine (spirit)" },
        { "name": "Stephen Lang", "role": "Colonel Miles Quaritch" },
        { "name": "Kate Winslet", "role": "Ronal" },
        { "name": "Oona Chaplin", "role": "Varang" },
        { "name": "Cliff Curtis", "role": "Tonowari" },
        { "name": "Britain Dalton", "role": "Lo'ak" },
        { "name": "Jack Champion", "role": "Spider (Miles Socorro)" },
        { "name": "Trinity Jo-Li Bliss", "role": "Tuktirey (Tuk)" },
        { "name": "Bailey Bass", "role": "Tsireya" },
        { "name": "Filip Geljo", "role": "Aonung" },
        { "name": "Duane Evans Jr.", "role": "Rotxo" },
        { "name": "CCH Pounder", "role": "Mo'at" },
        { "name": "Joel David Moore", "role": "Dr. Norm Spellman" },
        { "name": "Edie Falco", "role": "General Frances Ardmore" },
        { "name": "Brendan Cowell", "role": "Captain Mick Scoresby" },
        { "name": "Jemaine Clement", "role": "Dr. Ian Garvin" },
        { "name": "Giovanni Ribisi", "role": "Parker Selfridge" },
        { "name": "David Thewlis", "role": "Peylak" },
        { "name": "Dileep Rao", "role": "Dr. Max Patel" }
      ]
    },
    "fidelity_casting": {
      "score": "N/A",
      "summary": "Original science fiction world with no historical source material to assess against.",
      "detailed_analysis": "Avatar is an original fictional universe. There is no historical or literary source material against which to assess casting fidelity. The Na'vi are alien beings performed through motion capture. The human characters are original creations. Fidelity casting analysis does not meaningfully apply."
    },
    "summary": {
      "overall": "James Cameron's \"Avatar: Fire and Ash\" is a three-hour-and-seventeen-minute spectacle that will make your eyeballs very happy while occasionally making your brain very tired. The third trip to Pandora cost somewhere north of $350 million, grossed $1.46 billion, and delivers exactly the experience you'd expect from the director who essentially invented the modern blockbuster. It is visually staggering. It is narratively familiar. And it is ideologically committed to the same anti-colonial, environmentalist worldview that has powered this franchise since day one.\n\nThe story picks up weeks after the death of Neteyam, the eldest Sully son, killed in the climax of The Way of Water. The family is broken by grief. Lo'ak narrates the opening with genuine emotional weight, wrestling with guilt over his brother's death. Neytiri has hardened into something frightening. Zoe Saldana described her own character as having become a \"full-blown racist\" toward humans, and that's not an exaggeration. The woman who once saw the good in Jake Sully now wants Spider, the human boy her family adopted, gone. She's abandoned Eywa's teachings. She's consumed by rage. It's the most interesting character work in the film, and to Cameron's credit, the movie doesn't frame her hatred as righteous. It frames it as destructive. That's a surprisingly nuanced choice.\n\nThe big new addition is the Mangkwan clan, volcano-dwelling Na'vi who rejected Eywa after a volcanic eruption destroyed their homeland. Led by the charismatic and terrifying Varang, played with real physical presence by Oona Chaplin, the Mangkwan are hedonistic, violent, and willing to collaborate with the human RDA forces. They're fascinating on paper. A Na'vi tribe that lost faith in their deity, turned to nihilism, and allied with the colonizers out of pure survival instinct. There's a genuinely interesting moral question buried in there about what happens when the gods fail you. Unfortunately, Cameron doesn't really dig into it. The Mangkwan are mostly just space orcs.\n\nThe colonialism allegory remains the franchise's central architecture, and it's as unsubtle as ever. The RDA is back doing what the RDA always does: strip-mining Pandora, hunting Tulkun whales for profit, and generally embodying every critique of Western corporate imperialism you've ever read. The film's most pointed new wrinkle is the discovery that Spider, having been infused with Pandoran mycelia by Kiri, can now breathe Pandora's atmosphere. The RDA immediately recognizes this could be reverse-engineered, making the planet habitable for all humans. It's Cameron's clearest statement yet: colonization isn't about resources anymore. It's about replacement.\n\nBut here's where it gets interesting for our purposes. Strip away the environmental messaging and the anti-colonial framework, and what's actually driving this movie? Family. Fatherhood. Sacrifice. Faith.\n\nJake Sully's arc in this film is fundamentally about fatherhood. He's trying to reconnect with Lo'ak after Neteyam's death. He's trying to hold his family together while Neytiri spirals. When the Mangkwan capture his children, he doesn't hesitate to surrender himself. The emotional climax of the film isn't the battle. It's the moment Jake decides not to kill Spider, and Neytiri finally accepts the human boy as family. That's a story about mercy, about the expansion of the family unit, about a father's protective love overcoming fear.\n\nKiri's storyline is overtly spiritual. She learns she was \"sired by Eywa,\" essentially the daughter of God in the Pandoran cosmology. She struggles to connect with her divine parent. She pleads for Eywa's intervention in the final battle, and Eywa answers. The Pandoran wildlife rises up to defend the Na'vi. Whatever you think of Cameron's pantheistic nature-worship, the narrative structure is unmistakable: a young woman of faith calls upon a higher power in humanity's darkest hour, and that higher power delivers.\n\nSpider's arc is the most emotionally complex in the film. A human boy caught between two worlds, rejected by Neytiri, used as a lab rat by the RDA, and torn between his adoptive Na'vi family and his biological father Quaritch. The film's resolution, Spider being initiated into the Na'vi people at the spirit trees, is essentially a conversion and adoption narrative. He chooses his family. He chooses his faith. He is welcomed in.\n\nThe warrior ethos is celebrated without reservation. Jake re-bonds with the apex predator Toruk, rallies the Na'vi clans, and leads them into battle. Ronal, pregnant and mortally wounded, fights to her last breath. The film treats martial courage and the willingness to defend your people as unambiguous goods.\n\nWhere the film earns its woke score is in the systemic framing. The RDA isn't a rogue operation. It's institutional evil. The military-industrial complex is the villain, always. The Tulkun whale hunt is an obvious environmental parable. Cameron's sympathies are never in doubt. Nature good. Corporation bad. Indigenous wisdom superior. Western technology destructive.\n\nTechnically, the film is extraordinary. The volcanic Mangkwan homeland is unlike anything seen in the previous films. The underwater sequences continue to push boundaries. The final battle is massive, chaotic, and genuinely thrilling. Cameron remains the best spectacle filmmaker alive, full stop.\n\nConservative viewers should know what they're getting. This is an anti-colonial, environmentalist, spiritually pantheistic blockbuster. It has been from the start. But it's also a movie about a father protecting his family, a young woman's faith, a boy choosing where he belongs, warriors defending their homeland, and mercy triumphing over vengeance. The woke scaffolding is impossible to miss. The traditional foundation is what makes the building stand.",
      "adultInsight": "Conservative adult viewers approaching Avatar: Fire and Ash should understand that they are walking into the third act of a franchise whose ideological commitments have been transparent since 2009. The anti-colonial allegory is the architecture. The environmentalism is the theology. What's worth knowing is that this installment's traditional elements are stronger than in either predecessor. The fatherhood narrative is genuine and emotionally powerful. Neytiri's arc from hatred to acceptance is about mercy overcoming vengeance. The warrior ethos is celebrated without apology. Cameron is not trying to trick you. He's a sincere environmentalist who also sincerely believes in family, sacrifice, and courage.",
      "parentalGuidance": "Violence is intense and sustained: burning ships, brutal combat, characters shot and killed on screen. Ronal dies in combat during childbirth, an emotionally intense scene. A whale hunt sequence shows intelligent beings killed for profit. Minimal sexual content beyond standard Na'vi body design. Mild language. The Mangkwan are described as hedonists with scenes suggesting ritualistic intoxication. Not recommended for children under 10. Ages 10-12 with parental discretion. Ages 13+ appropriate for most teens. Discussion topics include Spider's identity and conversion narrative, Neytiri's arc from hatred to acceptance, and how filmmakers use allegory to advance arguments."
    },
    "tropeAudit": [
      { "trope": "Institutional Evil", "id": "WOKE-004", "category": "WOKE", "location": "Throughout -- RDA as full-spectrum colonial enterprise", "authenticity": "Mixed" },
      { "trope": "Anti-Western Revisionism", "id": "WOKE-020", "category": "WOKE", "location": "Throughout -- franchise structured as allegory of Western colonialism", "authenticity": "Mixed" },
      { "trope": "Globalist Utopia / Environmental Pantheism", "id": "WOKE-017", "category": "WOKE", "location": "Kiri's communion with Eywa; wildlife intervention in final battle", "authenticity": "Mixed" },
      { "trope": "The Colonialist Villain", "id": "WOKE-024", "category": "WOKE", "location": "RDA whale hunts and Bridgehead City operations", "authenticity": "Mixed" },
      { "trope": "The Girl Boss", "id": "WOKE-003", "category": "WOKE", "location": "Throughout -- every faction led or decisively influenced by a woman", "authenticity": "Mixed" },
      { "trope": "The Marginalized Savant", "id": "WOKE-001", "category": "WOKE", "location": "Throughout -- Kiri's neurodivergent-coded difference is actually transcendent power", "authenticity": "Mixed" },
      { "trope": "Redeemed Criminal Systemic", "id": "WOKE-019", "category": "WOKE", "location": "Mangkwan backstory -- villainy framed as product of trauma and divine abandonment", "authenticity": "Mixed" },
      { "trope": "Infallible Youth", "id": "WOKE-016", "category": "WOKE", "location": "Lo'ak's leadership and Kiri's spiritual authority exceed adult capabilities", "authenticity": "Mixed" },
      { "trope": "The Bigoted Traditionalist", "id": "WOKE-008", "category": "WOKE", "location": "Neytiri's hatred of humans and Tulkun pacifism treated as obstacles", "authenticity": "Mixed" },
      { "trope": "Defense of the Innocent", "id": "TRADITIONAL-045", "category": "TRAD", "location": "Throughout -- parental protection as highest moral imperative", "authenticity": "Natural" },
      { "trope": "The Self-Sacrificing Hero", "id": "TRADITIONAL-026", "category": "TRAD", "location": "Jake's surrender, Ronal's death in childbirth, Quaritch's fall", "authenticity": "Natural" },
      { "trope": "Industry and Perseverance", "id": "TRADITIONAL-041", "category": "TRAD", "location": "Jake rallying the clans; Lo'ak's persistence with the Tulkun", "authenticity": "Natural" },
      { "trope": "Faith in Adversity", "id": "TRADITIONAL-043", "category": "TRAD", "location": "Kiri's faith in Eywa; spirit tree ceremony as baptism and communion", "authenticity": "Natural" },
      { "trope": "Traditional Femininity", "id": "TRADITIONAL-036", "category": "TRAD", "location": "Neytiri's maternal grief, Ronal's death giving birth, Neytiri adopting Pril", "authenticity": "Natural" },
      { "trope": "Restored Home", "id": "TRADITIONAL-048", "category": "TRAD", "location": "Final act -- family restored, Spider initiated, invaders repelled", "authenticity": "Natural" },
      { "trope": "Wise Elder", "id": "TRADITIONAL-033", "category": "TRAD", "location": "Mo'at's counsel; Tulkun elder council", "authenticity": "Natural" },
      { "trope": "Warrior Ethos", "id": "TRADITIONAL-028", "category": "TRAD", "location": "Final battle -- Jake's Toruk bond, clan rally, combat celebrated", "authenticity": "Natural" }
    ],
    "seo": {
      "titleTag": "Is Avatar: Fire and Ash (2025) Woke? James Cameron Film Review | VirtueVigil",
      "metaDescription": "Is Avatar Fire and Ash woke? VirtueVigil's analysis: Woke Score 9, Traditional 8. Cameron's anti-colonial spectacle with surprisingly strong traditional bones. Full trope audit.",
      "keywords": "is avatar fire and ash woke, avatar 3 woke review, avatar fire and ash conservative review, avatar fire and ash woke score, james cameron avatar politics"
    },
    "spoiler_alert": true
  }
];

// Deduplicate by slug
const existingSlugs = new Set(reviews.map(r => r.slug));
const toAdd = newReviews.filter(r => !existingSlugs.has(r.slug));

// Remove any existing entries with same slugs (for re-runs)
const filtered = reviews.filter(r => !newReviews.some(n => n.slug === r.slug));

// Add new reviews to front
const final = [...newReviews, ...filtered];

fs.writeFileSync(reviewsPath, JSON.stringify(final, null, 2));
console.log(`Added ${newReviews.length} reviews. Total: ${final.length}`);
