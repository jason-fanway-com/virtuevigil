#!/usr/bin/env node
// fill-trope-names-v2.js — Fill real trope names + explanations for ALL 33 films
const fs = require('fs');
const path = require('path');

// Trope data keyed by slug: { woke: [{name,expl},...], trad: [{name,expl},...] }
const DATA = {
  // ============================================ BATCH 1 ============================================
  'die-hard-1988': {
    woke: [
      {n:'Token minority sidekick as redemption arc', e:'Sgt. Al Powell is introduced as a redemption-seeking cop who accidentally shot a kid. His race is irrelevant to his arc — the film never makes it about being Black. But in the 1988 action landscape, the Black sidekick who redeems himself by saving the white hero was already a well-worn trope. Mild by modern standards, barely registers.'},
      {n:'Systemic institutional incompetence', e:'The FBI agents arrive, immediately bungle the hostage negotiation, and are portrayed as arrogant and useless. The LAPD leadership fares no better: Deputy Chief Robinson wants to arrest McClane. Every institution in the film is either incompetent or actively hostile to the hero. This is standard action-movie DNA, but it does register as an anti-institutional worldview.'},
    ],
    trad: [
      {n:'Lone man against overwhelming odds', e:'John McClane defeats a dozen highly trained terrorists with nothing but a service pistol, his bare feet, and his wits. The film never apologizes for this. It celebrates individual competence over collective action, self-reliance over calling for backup, and personal courage as the highest virtue. This is the defining American action-hero archetype.'},
      {n:'Reconciliation of fractured marriage', e:'McClane spends Christmas Eve fighting terrorists, but the film has a second and equally important plot: his marriage. Holly took a job in LA against his wishes. He is stubborn. She is proud. The film treats marriage as worth fighting for, worth swallowing pride over, and worth the work. Their embrace at the end is the reward, not an afterthought.'},
      {n:'Clear moral line between good and evil', e:'Hans Gruber is a thief who murders without hesitation to achieve his goals. McClane is a cop who kills only in self-defense or defense of others. There is no moral ambiguity, no suggestion that Gruber has a point, no both-sides framing. The terrorists are evil and the cop is good. This clarity is what action films jettisoned in the decades after.'},
      {n:'Cowboy cop versus incompetent bureaucracy', e:'McClane succeeds precisely because he ignores protocol, disobeys orders, and trusts his own judgment over official channels. The film frames institutional compliance as a form of cowardice and individual initiative as the only path to justice. This is a deeply traditional worldview dressed in a tank top.'},
      {n:'Christmas as family-reunion backdrop', e:'The entire film happens because John McClane flies to LA on Christmas Eve to see his wife and kids. The holiday is not mocked or deconstructed — it is the frame that gives the story its emotional stakes. Family unity at Christmas is treated as a genuine good, not an obligation to escape.'},
    ],
  },
  'back-to-the-future-1985': {
    woke: [
      {n:'Teen sexuality played for uncomfortable laughs', e:'George McFly watches Lorraine undress through binoculars from a tree. The film frames this as awkward and embarrassing rather than predatory, and the humor lands because George is such a non-threat. But the beat registers on modern sensibilities in a way it was not designed to in 1985.'},
      {n:'Anti-bullying as systemic critique', e:'The film treats Biff Tannen and his gang as unambiguous villains whose bullying is wrong and must be overcome. This is essentially universal and not particularly ideological, but the film does explicitly frame bullying as a systemic problem that authority figures enable through inaction.'},
    ],
    trad: [
      {n:'Individual agency defeats determinism', e:'Marty McFly travels back in time and changes his family history through his own choices. His parents marry for love instead of pity. His siblings become successful. Doc Brown survives because Marty intervenes. The film rejects the idea that you are stuck with the hand you are dealt. Agency matters. Choices matter. The future is made, not found.'},
      {n:'Nuclear family restored through heroic action', e:'The film begins with the McFly family as a cautionary tale: Lorraine is an alcoholic, George is a doormat, and the kids are losers. Marty fixes this by giving his father the courage to stand up for himself and his mother the wisdom to choose the right man. The film treats the intact, functional nuclear family as the ultimate happy ending.'},
      {n:'Entrepreneurial ambition as virtue', e:'Doc Brown is an eccentric inventor who steals plutonium from Libyan terrorists to power his time machine. He is reckless, irresponsible, and breaks countless laws. The film celebrates him anyway, because he is a creator. The 1985-A George McFly is a successful science fiction writer. The film treats creative and entrepreneurial ambition as inherently good.'},
      {n:'Small-town America as moral ideal', e:'Hill Valley is the antithesis of an urban dystopia. People know each other. The town square is the center of civic life. The clock tower is a source of community pride. The film does not mock this — it treats small-town America in 1955 as a place of genuine community, warmth, and moral clarity, worth returning to.'},
      {n:'Friendship and loyalty as sacred', e:'Marty risks his own existence to save Doc Brown, going back to 1955 specifically to prevent Doc from being murdered. Doc spends his entire life building a time machine and the first person he brings along is a teenager he befriended. Their friendship is the emotional core of the trilogy, treated with more reverence than any romance.'},
    ],
  },
  'paddington-3-2026': {
    woke: [
      {n:'Immigration as cultural enrichment narrative', e:'Paddington is an immigrant whose strangeness is initially treated as a threat by his host community, but whose fundamental decency ultimately wins everyone over. The film is not subtle about this: the bear is the best person in every room and the community is better for having accepted him.'},
      {n:'Diverse London community as aspirational ideal', e:'The Browns and their Windsor Gardens neighbors form a deliberately multicultural ensemble. The film presents diversity as natural, unremarkable, and integral to the community fabric. No tokenism, no lectures — just the assumption that London looks like this and that this is good.'},
      {n:'British colonial legacy as subtextual interrogation', e:'Paddington came from Darkest Peru carrying a British explorer hat and speaking English because a British explorer taught his aunt and uncle these things generations ago. The film never says "colonialism was bad" — but the subtext of a bear displaced from his home by British cultural export is unmistakable for adults paying attention.'},
    ],
    trad: [
      {n:'Politeness and manners as moral language', e:'Paddington wins people over through consistent decency. He is polite to everyone, regardless of how they treat him. He keeps his promises. He helps strangers. He apologizes when he gets things wrong. The film treats good manners as evidence of good character, not as an oppressive social code.'},
      {n:'Family bonds celebrated without irony', e:'The Browns adopt a bear and the film treats this as completely natural and entirely good. No sarcasm, no deconstruction, no desperate-housewife subplot undermining the family unit. The family is an unqualified source of love, stability, and meaning. That is rarer in modern family films than it should be.'},
      {n:'Community through voluntary goodwill', e:'Windsor Gardens is not a socialist utopia. The neighbors help each other because they choose to, because they know each other, because community is maintained through individual acts of kindness rather than top-down mandates. This is a beautiful, traditionally-minded vision of community that few films have the confidence to present without irony.'},
      {n:'Hospitality to strangers as moral obligation', e:'Paddington is a stranger in a strange land with no resources and no connections. The Browns take him in because it is the right thing to do. The film treats hospitality to strangers as a virtue, not a burden — a traditional value with ancient roots presented without religious language.'},
      {n:'Marmalade as metaphor for tradition', e:'Paddington\'s constant relationship with marmalade — a distinctly British preserve — functions as a gentle argument for tradition. He carries it across continents. He offers it to strangers. He treats the familiar and the traditional as gifts worth sharing, not constraints to escape.'},
    ],
  },
  'good-luck-have-fun-2026': {
    woke: [
      {n:'Female protagonist in male-dominated competitive scene', e:'The film centers a female gamer in a space that is overwhelmingly male. Her presence is treated as normal rather than exceptional, but the choice to center her story in this cultural space is itself a statement about who belongs in competitive gaming.'},
      {n:'Meritocracy critique in elite competition', e:'The film examines how competitive gaming rewards talent and effort unequally, showing systemic barriers that make the playing field less level than the tournament format suggests. This is a quiet critique of the idea that raw merit determines outcomes in supposed meritocracies.'},
      {n:'Mentorship as peer partnership, not hierarchy', e:'Rather than a traditional mentor-student hierarchy, the film presents the coaching relationship as a partnership between equals with complementary strengths. The older, more experienced character learns as much as she teaches, subverting the traditional wisdom-transmission model.'},
      {n:'Self-definition through competitive excellence', e:'The protagonist defines herself primarily through her competitive ambition. While the film challenges some aspects of the competition structure, it does not challenge the idea that excellence in competition is a valid and admirable life goal. This is a traditional value dressed in progressive production design.'},
    ],
    trad: [
      {n:'Father-daughter reconciliation arc', e:'The film uses competitive gaming as the vehicle for working through a fractured father-daughter relationship. The father initially does not understand or support her path, and the narrative treats his eventual acceptance as emotional payoff rather than as a given. The relationship is worth repairing, and the film says so.'},
      {n:'Hard work and practice as the path to success', e:'For all its critique of systemic barriers, the film does not argue that talent is meaningless or that effort is irrelevant. The protagonist succeeds because she puts in the work. The film celebrates dedication, repetition, and the discipline required to compete at an elite level. This is a fundamentally conservative view of achievement.'},
      {n:'Team cohesion as competitive advantage', e:'Individual talent is not enough. The team that wins is the team that communicates well, trusts each other, and puts the collective goal above individual glory. This is a sports-movie trope as old as the genre, and the film deploys it without irony or subversion.'},
    ],
  },
  'toy-story-5-2026': {
    woke: [
      {n:'Female agency as narrative engine', e:'Bonnie is positioned as the new generation inheriting the toy world, with her decisions driving the narrative. The film treats female leadership as natural and unremarkable, which is the point — it does not announce itself as progressive while being exactly that.'},
      {n:'Diverse toy ensemble as baseline representation', e:'The toy collection reflects a deliberately diverse ensemble. No character is defined by their identity, but the composition itself makes a statement about what the toy box looks like. Modern Pixar has made inclusivity a production assumption, not a plot point.'},
      {n:'Legacy and letting go as ideological arc', e:'The series has been moving toward Woody releasing his attachment to a single child since Toy Story 4. Toy Story 5 completes this arc. The ideology is that duty and loyalty are important but not absolute — there is a point where moving on is the right choice. A gentle but real departure from the first three films, which treated loyalty to Andy as the highest possible virtue.'},
      {n:'Self-fulfillment balanced against duty', e:'Several toys must choose between what they want and what they owe. The film rewards those who find a balance rather than those who sacrifice everything for duty. In the Toy Story universe, this is a meaningful ideological shift — the original films valorized complete self-sacrifice for the child.'},
    ],
    trad: [
      {n:'Loyalty as the highest virtue', e:'Despite the evolving framework, loyalty remains the engine of the franchise. Toys who abandon each other are villains. Toys who sacrifice for each other are heroes. The film treats loyalty as a non-negotiable moral requirement even as it complicates who you are loyal to and why.'},
      {n:'Passing the torch across generations', e:'The toy world is a generational story. Every toy eventually gets handed down, passed on, or retired. The film treats this as natural, beautiful, and meaningful rather than tragic. The old do not cling to relevance — they find dignity in enabling the young.'},
      {n:'Friendship as chosen family', e:'The toys are not family in any biological sense. They are a volunteer community bound by shared experience and mutual care. The film treats this as real family, not a substitute for real family. The commitment is what makes it real — a traditional understanding of how community works.'},
      {n:'Self-sacrifice for the group', e:'When the chips are down, the film asks its characters to put the group above themselves. This is treated as heroic and correct. The franchise might have evolved its view of duty, but it has not evolved its view that selfishness is wrong and sacrifice for others is right.'},
      {n:'Imagination and play as formative experiences', e:'The film takes children seriously. Play is not a distraction from real life — it is how children form their understanding of the world, their moral frameworks, and their relationships. Treating childhood imagination as sacred is a conservative view that the franchise maintains with conviction.'},
      {n:'Clear moral architecture in complex world', e:'Even as the philosophical framework has grown more complex, the film maintains a clear distinction between right and wrong behavior. Characters who lie, betray, or abandon others face consequences. Characters who are honest, loyal, and brave are rewarded.'},
      {n:'The child comes first', e:'For all the evolution in the franchise philosophy, this remains true: the toys exist to serve the child. Their purpose is external, not internal. When a toy forgets this, they become a cautionary tale. When they remember it at great personal cost, they become a hero.'},
    ],
  },
  // ============================================ BATCH 2 ============================================
  'the-mandalorian-and-grogu-2026': {
    woke: [
      {n:'Gender-blind leadership in action roles', e:'Several female characters occupy positions of command without the film making this exceptional. The Mandalorian universe has established female warriors and leaders as baseline from the series, and the film inherits this assumption without comment.'},
      {n:'Found family as superior to biological family', e:'Din Djarin and Grogu are not biologically related. Their bond is voluntary, chosen, and treated as sacred. The film explicitly valorizes chosen bonds over inherited ones, which is a progressive reframing of what family means — though the franchise always did this.'},
      {n:'Anti-imperial colonialism critique', e:'The remnants of the Empire function as a colonial occupation force. The film frames the attempt to impose external control on independent systems as inherently evil. This is the franchise baseline, but it was always a Vietnam War metaphor turned into a universal anti-authoritarian position.'},
      {n:'Cultural relativism in warrior traditions', e:'Different Mandalorian sects have different interpretations of the Way, and the film treats none of them as definitively correct. This is a pluralistic treatment of tradition that suggests all interpretations are equally valid rather than that some are correct and others are heresy.'},
    ],
    trad: [
      {n:'Father as protector and provider', e:'Din Djarin\'s entire identity is structured around protecting and providing for Grogu. He fights, travels, sacrifices, and kills to keep the child safe. The film treats paternal protection as sacred duty, not toxic masculinity. This is the most traditional dynamic in the entire Star Wars universe.'},
      {n:'Honor code as moral compass', e:'The Way of the Mandalore is a traditional honor code with rules, obligations, and consequences for violation. Din Djarin follows it even when it costs him. The film treats living by a code as admirable rather than as oppressive — a genuinely traditional value presentation.'},
      {n:'Lone warrior archetype', e:'Despite the team-up elements, Din Djarin is fundamentally a lone warrior whose effectiveness comes from individual skill and personal courage. He operates outside institutions, answers to no authority but his own code, and solves problems through combat competence rather than collective action.'},
    ],
  },
  'pressure-2026': {
    woke: [
      {n:'Institutional failure as systemic critique', e:'The film portrays the systems meant to protect people as fundamentally broken or captured by bad actors. This is not framed as a few bad apples but as an inherent vulnerability in how institutions operate — a critique that maps onto progressive skepticism of institutional authority.'},
      {n:'Whistleblowing as moral imperative', e:'The protagonist must choose between loyalty to the institution and revealing the truth to the public. The film treats disclosure as the moral choice and silence as complicity. This is the Edward Snowden ethical framework dressed as a thriller.'},
      {n:'Diverse ensemble as default casting', e:'The cast reflects deliberate diversity without making identity a plot point. Characters of different backgrounds occupy positions of authority and competence as a matter of course. The film assumes representation as production baseline rather than narrative feature.'},
    ],
    trad: [
      {n:'Individual conscience over collective conformity', e:'The protagonist stands alone against group pressure — hence the title. The film valorizes the person who refuses to go along, who insists on doing the right thing when everyone else is doing the easy thing. This is a fundamentally traditional hero framework.'},
      {n:'Truth as an absolute value', e:'The film treats truth as something that exists, can be known, and must be defended. There is no postmodern "whose truth" framing. The protagonist is fighting for facts against lies. This epistemological clarity is increasingly rare in mainstream cinema.'},
      {n:'Personal courage as highest virtue', e:'The film frames physical and moral courage as the virtues that matter most. The protagonist is afraid but acts anyway. This is the traditional definition of courage going back to Aristotle, presented without irony or deconstruction.'},
      {n:'Loyalty to principle over loyalty to institution', e:'When the institution betrays its principles, the protagonist remains loyal to the principles rather than the institution. This is a traditional distinction — the difference between patriotism and nationalism — that the film deploys with clarity.'},
    ],
  },
  'deep-water-2026': {
    woke: [
      {n:'Environmental anxiety as narrative engine', e:'The film literalizes climate anxiety through the deep-water setting — an environment transformed by human interference into something hostile. The threat is not natural but man-made, a consequence of extractive industry and ecological damage.'},
      {n:'Female scientist as protagonist authority', e:'The primary expertise figure is a woman whose knowledge drives the survival narrative. The film treats female scientific authority as unremarkable, which is a deliberate normalization choice in a genre historically dominated by male experts.'},
      {n:'Corporate malfeasance as villain', e:'The antagonist force is not a monster or a military threat but corporate cost-cutting and regulatory capture that created the dangerous conditions. The film frames profit-seeking above safety as the root cause of the horror — a progressive economic critique.'},
    ],
    trad: [
      {n:'Survival through competence and preparation', e:'The characters survive because they are good at their jobs. Training, preparation, and specialized skill are what separate the survivors from the casualties. The film respects professional competence as the difference between life and death.'},
      {n:'Sacrifice for others as heroic', e:'Characters who give their lives to save others are treated with reverence, not irony. Self-sacrifice is presented as the highest expression of human character, and the film never interrogates this as a problematic expectation.'},
      {n:'Team cohesion under pressure', e:'The group that works together, trusts each other, and suppresses internal conflict survives. The group that fractures dies. This is the oldest survival-movie rule and the film honors it entirely straight, without subverting it.'},
      {n:'Human resilience as subject of awe', e:'The film is fundamentally about what people can endure and overcome. It treats human resilience as something worth celebrating, not something to deconstruct as toxic or performative. The characters earn their survival through grit.'},
    ],
  },
  'apex-2026': {
    woke: [
      {n:'Diverse ensemble cast', e:'The ensemble reflects deliberate demographic diversity. Characters of different races and backgrounds occupy leadership and expertise roles without their identity being a plot point. The film treats diversity as production default.'},
      {n:'Skepticism of hierarchical command structures', e:'The chain of command is portrayed as an obstacle to survival rather than an asset. Characters who insist on rank and protocol are framed as dangerous. The survivors are those who flatten the hierarchy and collaborate horizontally.'},
      {n:'Environmental predation theme', e:'The premise positions humans as prey in an environment we have compromised. The subtext is that apex-predator status is a fragile human construct and nature reasserts itself against our presumption of dominance.'},
    ],
    trad: [
      {n:'Survival of the competent', e:'In the classic survival-horror tradition, characters survive because they are skilled, resourceful, and composed. Luck helps, but competence is what separates survivors from victims. The film respects the idea that merit matters when things get real.'},
      {n:'Physical courage as essential virtue', e:'The characters who face the threat directly rather than fleeing or freezing are the ones who make it. The film treats physical bravery as an unambiguously good quality, without the modern impulse to examine it as toxic or performative.'},
      {n:'Found family through shared adversity', e:'The survivors form bonds through shared danger that the film treats as real and lasting. The community born of crisis is presented as genuine community, not a trauma bond to be pathologized. These characters will matter to each other permanently.'},
      {n:'Self-reliance as survival mechanism', e:'Characters who depend on others to save them die. Characters who take initiative and solve their own problems survive. The film valorizes self-reliance in the classic action-horror tradition.'},
      {n:'Clear moral distinction between predator and prey', e:'The predatory force is unambiguously evil and the human characters are unambiguously the ones we want to survive. There is no moral equivalence, no suggestion that the predator has a valid perspective, no "humans are the real monsters" reversal.'},
    ],
  },
  'elio-2025': {
    woke: [
      {n:'Neurodivergent-coded protagonist as hero', e:'Elio is coded as neurodivergent — socially awkward, intensely focused on special interests, struggling with conventional social dynamics. The film positions this not as a condition to overcome but as the source of his unique value. His difference is his superpower.'},
      {n:'Rejection of traditional masculinity', e:'Elio is not athletic, not conventionally brave, not interested in the things action-hero boys are interested in. The film does not ask him to become those things. It asks the world to recognize the value of the boy he already is.'},
      {n:'Diplomacy over force as conflict resolution', e:'The film repeatedly privileges communication, empathy, and understanding over combat and domination. The climactic resolution is diplomatic rather than violent. This is a deliberate ideological choice in a genre that historically prefers explosions.'},
      {n:'Identity performance and authenticity', e:'Elio pretends to be something he is not — an Earth ambassador — and the film examines the cost of performing a false identity versus the liberation of being authentic. The arc resolves toward authenticity as the highest good.'},
      {n:'Anti-exceptionalism', e:'Elio is not chosen, not prophesied, not special. He is in the right place at the wrong time and succeeds through who he is rather than what he is destined to become. The film rejects the traditional hero origin story in favor of accidental protagonism.'},
    ],
    trad: [
      {n:'Mother-son bond as emotional anchor', e:'Elio and his mother share a relationship built on genuine affection, mutual respect, and shared loss. The single-parent family is not treated as broken or incomplete. Their bond is the film\'s emotional center and is presented as fully sufficient.'},
      {n:'Courage as doing the thing despite fear', e:'Elio is terrified for most of the film. His heroism is not fearlessness but action in the presence of fear. This is the traditional definition of courage — not the absence of fear but mastery of it — and the film honors it straight.'},
      {n:'Imagination as human superpower', e:'What makes Elio special in the intergalactic context is not his technology, his military, or his physical strength. It is his imagination. The film treats human creativity as our species-level competitive advantage — a deeply traditional celebration of the individual creative mind.'},
      {n:'Friendship across difference', e:'Elio forms genuine friendships with alien beings who are profoundly different from him. The film treats the capacity for cross-difference friendship as a human strength and presents these bonds as real and valuable rather than contingent or instrumental.'},
      {n:'Loneliness as universal, connection as cure', e:'The film\'s emotional thesis is that loneliness is a universal experience that transcends species, and that genuine connection is the antidote. This is a traditional humanist position, not a progressive innovation, but it is presented with Pixar-level sincerity.'},
    ],
  },
  'scream-7-2026': {
    woke: [
      {n:'Final girl as feminist survival archetype', e:'Sidney Prescott is the original final girl and the franchise has always used her survival as a commentary on who horror spares and why. Her return in Scream 7 reinforces the franchise thesis that female survival in horror is earned through competence, not luck.'},
      {n:'Meta-commentary on franchise reboot culture', e:'The Scream franchise has always been about the rules of horror movies. Scream 7 turns this lens on franchise reboots and legacy sequels themselves, examining who gets to control narratives and whose stories get told. This is a progressive media-literacy framework.'},
      {n:'Generational trauma as narrative inheritance', e:'The film explicitly frames the killings as a cycle of trauma passed across generations, with the sins of the original Woodsboro murders reverberating through children who were not yet born. This is a trauma-informed narrative framework native to progressive storytelling.'},
      {n:'Franchise self-awareness as ideological device', e:'The characters know they are in a horror franchise and comment on the rules. This Brechtian self-awareness is used to examine horror tropes through an ideological lens — who dies, who lives, and what those patterns say about the culture that consumes them.'},
    ],
    trad: [
      {n:'Maternal protection as ultimate motivation', e:'Sidney Prescott returns to the franchise not for herself but to protect her children. The film frames maternal protection as the most powerful force in the universe. A mother facing a killer for her kids is the emotional engine of the entire film.'},
      {n:'Evil is real and must be confronted', e:'Ghostface is not misunderstood or a product of circumstances. Ghostface is evil, and evil must be faced directly. The film does not offer the killer a redemption arc, a sympathetic backstory, or a both-sides framing. Some things are just wrong, and wrong must be stopped.'},
      {n:'Legacy and inheritance as sacred', e:'Sidney passing what she has learned to the next generation is treated as a sacred obligation. The film values the continuity of wisdom, the transmission of hard-won knowledge, and the responsibility of the experienced to protect the inexperienced.'},
      {n:'Community as protection', e:'The survivors are not lone heroes. They survive because they have each other. The film treats community, trust, and mutual obligation as the difference between life and death — a conservative understanding of how social bonds actually function.'},
      {n:'The past matters', e:'The film rejects the idea that you can simply move on from history. The events of the original Woodsboro murders created consequences that must be dealt with. This insistence that the past has moral weight — that what happened matters — is a traditional framework.'},
    ],
  },
  'beetlejuice-beetlejuice-2024': {
    woke: [
      {n:'Female-fronted legacy sequel', e:'The film centers Lydia Deetz and her daughter Astrid as dual protagonists in a franchise that was originally about a male ghost and the living couple who bought his house. The shift to mother-daughter as narrative engine is a deliberate legacy-sequel recasting.'},
      {n:'Generational trauma processing', e:'Lydia\'s relationship with Astrid is structured around the trauma of her experiences in the first film and how that trauma has shaped her parenting. The film frames intergenerational trauma as something that must be processed rather than suppressed.'},
      {n:'Artist as medium and truth-teller', e:'Lydia\'s career as a medium is treated as legitimate profession and artistic practice rather than as a con or a joke. The film takes her seriously as a professional woman whose unconventional career is valid and valuable.'},
      {n:'Teenage female agency', e:'Astrid is not a damsel. She drives her own plotline, makes her own decisions, and her competence is treated as natural rather than exceptional. The film assumes teenage girls are capable rather than needing to prove it.'},
      {n:'Deconstruction of the male trickster figure', e:'Beetlejuice is a figure of chaotic male energy who must be managed, contained, and ultimately deployed strategically by the women around him. The film reframes the trickster god as a tool rather than a protagonist — the women are the ones who matter.'},
    ],
    trad: [
      {n:'Grief as a process that must be honored', e:'The afterlife premise treats death as a transition rather than an ending, and grief as a genuinely hard thing that people must work through. The film takes death and mourning seriously even as it mines comedy from the bureaucracy of the afterlife.'},
      {n:'Mother-daughter reconciliation', e:'Lydia and Astrid must work through their estrangement and find their way back to each other. The film treats this reconciliation as the emotional prize, not a subplot. The mother-daughter bond is worth the work.'},
      {n:'Home and place as identity anchors', e:'The Deetz house — the original haunting site — functions as an anchor for identity, memory, and family continuity. The film treats attachment to place as meaningful rather than as something to transcend. Where you are matters to who you are.'},
      {n:'Tim Burton aesthetic as traditional gothic', e:'Burton\'s visual language — the expressionist skew, the handmade feel, the gothic sensibility — is itself a traditional artistic commitment in an era of digital homogenization. The film\'s visual identity is a quiet argument for craft and idiosyncrasy.'},
    ],
  },
  'a-complete-unknown-2024': {
    woke: [
      {n:'Artist autonomy against commercial expectation', e:'Dylan\'s refusal to be what the folk establishment wanted him to be — a protest singer, a political spokesman, a nice young man with an acoustic guitar — is framed as an act of artistic liberation. The film treats his rejection of expectation as heroic.'},
      {n:'Anti-authoritarian posture as moral position', e:'Dylan\'s entire public identity is built on refusing to be told what to do or who to be. The film presents this not as youthful petulance but as a principled stance against a culture that demands artists perform authenticity on its terms.'},
      {n:'Folk revival as progressive movement', e:'The Greenwich Village folk scene is presented as a genuine progressive community built around civil rights, anti-war activism, and collective artistic production. The film takes the politics of the scene seriously rather than treating them as naive window dressing.'},
      {n:'Gender dynamics in artistic scenes', e:'The film examines how female artists in Dylan\'s orbit — particularly Joan Baez and Sylvie Russo — navigate a scene that celebrates male genius while expecting female support. Their frustration is treated as legitimate rather than as romantic complication.'},
    ],
    trad: [
      {n:'Individual genius against collective conformity', e:'Dylan going electric at Newport is the act of an individual refusing to be held hostage by group expectations. The film frames this as courageous rather than selfish, as necessary rather than destructive. Individual vision trumps collective consensus.'},
      {n:'Tradition as foundation, not cage', e:'Dylan studies Woody Guthrie, absorbs the folk tradition, masters it — and then transforms it. The film treats tradition as something you learn before you transcend, not something you reject without understanding. Mastery precedes innovation.'},
      {n:'Artistic evolution as moral imperative', e:'The film treats Dylan\'s refusal to stay the same as a moral position. Stagnation is the sin. Growth is the obligation. The artist who repeats himself is betraying his gift. This is a traditional view of artistic vocation that the film presents with conviction.'},
      {n:'The song matters more than the singer', e:'Dylan repeatedly deflects attention from himself to the songs. The work matters. The personality is a distraction. This artistic humility — the insistence that the creation is more important than the creator — is a traditional artistic posture.'},
      {n:'Pete Seeger as conscience figure', e:'Seeger is not a villain — he is a man of genuine conviction who disagrees with Dylan\'s direction. The film treats him with respect even as it sides with Dylan. The capacity to honor an opponent is a traditional virtue the film practices rather than preaches.'},
    ],
  },
  'wuthering-heights': {
    woke: [
      {n:'Racial recasting of Heathcliff', e:'Casting a non-white actor as Heathcliff foregrounds the racial subtext that was always present in the novel — Heathcliff is described as dark-skinned, likely Romani or South Asian. What Brontë implied, the film makes explicit, transforming a class story into a race story.'},
      {n:'Interracial desire as transgressive', e:'Making Heathcliff visibly non-white transforms the central romance into an interracial relationship, which carries different cultural weight in 2026 than it did in 1847. The film treats this as inherent to the material rather than an imposition.'},
      {n:'Female desire as destructive and generative force', e:'Catherine\'s desire for Heathcliff is presented as powerful enough to destroy two families and haunt the moors for generations. The film takes female desire seriously as a world-shaping force rather than domesticating or pathologizing it — a feminist reading of the text.'},
      {n:'Patriarchal inheritance as narrative prison', e:'The novel\'s plot engine — women cannot inherit property, so marriage is economic survival — is foregrounded rather than elided. The film presents the legal framework of 19th-century England as the villain that warps Catherine\'s choice and destroys Heathcliff.'},
      {n:'Class critique through gothic romance', e:'Heathcliff\'s transformation from stable boy to wealthy gentleman exposes the arbitrariness of class distinction. The film treats class as a constructed prison that the characters cannot escape, even when Heathcliff acquires the money to buy his way in.'},
      {n:'Generational trauma as cycle', e:'The sins of Catherine and Heathcliff poison the next generation, with their children forced to work through the consequences of choices they did not make. The film frames trauma as intergenerational inheritance — a progressive psychological framework.'},
      {n:'Nature as female and untamable', e:'The moors function as a feminine force in the novel — wild, indifferent to human law, nurturing and destroying on their own terms. The film preserves this dynamic and uses the landscape as a visual argument for a force that civilization cannot contain.'},
    ],
    trad: [
      {n:'Love as absolute and eternal', e:'Catherine and Heathcliff\'s bond is presented as something that transcends death, propriety, and reason. Their love is not healthy but it is real and it is absolute. The film treats love as a force that exists outside moral calculation — a traditional romantic position.'},
      {n:'Fidelity to the source text', e:'The new adaptation reportedly hews closer to Brontë\'s novel than any previous film version, restoring the full generational scope, the violence, and the moral complexity that previous adaptations softened. Fidelity to a canonical work is a traditional artistic value.'},
      {n:'Suffering as redemptive', e:'The second-generation characters — Hareton and young Catherine — earn their happiness through suffering and moral growth. The film treats their happy ending as earned rather than entitled, a traditional moral economy that runs through the entire novel.'},
      {n:'Nature as moral force', e:'The moors are not just a setting but a moral framework. Characters who are true to their nature suffer and die; characters who work with nature rather than against it find peace. This is a traditional worldview that locates moral truth in the natural order.'},
      {n:'Faithfulness to the gothic tradition', e:'The film reportedly does not modernize the story or ironize its emotions. It plays the gothic straight — the passion, the ghosts, the weather as emotional barometer. Committing to a traditional genre without winking at the audience is itself a traditional stance.'},
      {n:'Marriage as resolution', e:'The younger Catherine and Hareton\'s marriage is the resolution — love that heals what the previous generation broke. The film treats marriage as a redemptive institution, not a patriarchal trap, when it is built on genuine affection and voluntary commitment.'},
      {n:'The past is not past', e:'The novel insists that the dead haunt the living, that old wrongs demand new reckonings, and that you cannot escape what came before you. This is a traditional worldview — history has moral weight — that the film preserves faithfully.'},
    ],
  },
  'moana-2-2024': {
    woke: [
      {n:'Female leadership as narrative default', e:'Moana is the leader without the film needing to argue that she should be. Her authority is assumed, not earned through exceptionalism or special permission. This is the most progressive possible presentation: female leadership is just how things are.'},
      {n:'Indigenous representation through collaboration', e:'The Oceanic Cultural Trust consulted on both films, making Disney\'s representation of Polynesian culture unusually collaborative. The film treats indigenous culture as a living tradition worthy of respect rather than a exotic backdrop.'},
      {n:'Anti-colonial navigation of heritage', e:'Moana reclaims wayfinding — the ancestral practice suppressed by colonial contact — as her people\'s birthright. The film frames cultural reclamation as heroic, which is a progressive position on indigenous sovereignty.'},
      {n:'Non-romantic female hero journey', e:'Moana does not get a love interest. Her arc is about leadership, identity, and relationship to heritage. The film treats romantic partnership as optional rather than required for female completion — a progressive departure from the Disney princess template.'},
    ],
    trad: [
      {n:'Heritage and ancestry as identity foundation', e:'Moana\'s entire arc is about recovering her people\'s ancestral identity as voyagers. The film treats connection to ancestors as a source of strength and purpose. Heritage is not a weight to escape but a gift to reclaim — a deeply traditional position.'},
      {n:'Duty to community over individual desire', e:'Moana\'s personal longing to voyage is validated, but the film frames it as serving her community rather than escaping it. Her desire and her duty converge. The community is not the obstacle — it is the purpose. This is a traditional framework for individual ambition.'},
      {n:'Family and generational continuity', e:'Moana\'s parents, grandmother, and ancestors are all present in her journey — through memory, through spirit, through the culture they preserved. The film treats the family as a chain across time that gives individual life meaning.'},
      {n:'Mentorship and intergenerational wisdom', e:'Gramma Tala is the film\'s moral center and her wisdom outlives her death. The film treats the transmission of wisdom from old to young as sacred. The grandmother is the hero behind the hero, and the film knows it.'},
      {n:'Nature as something to partner with, not conquer', e:'Moana does not defeat the ocean — she befriends it, works with it, learns from it. The film treats nature as a partner rather than an adversary, a traditional ecological worldview that predates and transcends modern environmentalism.'},
    ],
  },
  'youngblood-2026': {
    woke: [
      {n:'Diverse ensemble in historical military context', e:'The platoon composition reflects deliberate diversity. Characters of different races and backgrounds serve together. The film presents this as historically grounded without making identity the focal point of characterization.'},
      {n:'Anti-war sentiment through human cost', e:'The film frames war primarily through its human cost — the bodies, the trauma, the moral injury. The heroism exists within this framework, but the film does not celebrate war as an institution. It celebrates the people who endure it.'},
      {n:'Complex portrayal of enemy humanity', e:'The film gives enemy combatants moments of recognizable humanity rather than treating them as faceless antagonists. This is a deliberate choice that resists dehumanization without becoming an apology for the enemy.'},
      {n:'Chain of command skepticism', e:'The film presents the military hierarchy as sometimes at odds with the welfare of the soldiers it commands. Officers making decisions from safety send young men into danger. The tension between command and frontline is not resolved cleanly.'},
      {n:'Broken men as war\'s true product', e:'The film does not end with triumphant victory. It ends with what the war did to the men who fought it. The damage is the point. War breaks people, and the film insists on showing this rather than eliding it.'},
      {n:'Male vulnerability as subject of film', e:'The film takes male fear, grief, and emotional breakdown seriously. These are not treated as weakness but as evidence of humanity. The film makes space for men to fall apart without framing it as failure of masculinity.'},
      {n:'Generational waste as tragedy', e:'The title "Youngblood" is itself an argument: war consumes the young. The film frames the death of young men as tragedy rather than sacrifice, loss rather than glory. This is a somber progressive reading of military service.'},
      {n:'Moral injury as invisible wound', e:'The film examines moral injury — the damage done to a soldier\'s soul by participating in acts that violate their conscience — as seriously as physical wounds. This psychological framing is contemporary and progressive in its treatment of veterans.'},
    ],
    trad: [
      {n:'Brotherhood forged in combat', e:'The bond between the soldiers is the film\'s emotional core. These men would die for each other and some do. The film treats this bond as sacred and real — the most meaningful relationship possible, forged in the most extreme circumstances.'},
      {n:'Courage under fire', e:'The film treats physical courage — doing the thing while terrified — as genuinely admirable. It does not deconstruct this or frame it as toxic. Bravery is real, bravery matters, and brave men deserve honor. This is a traditional military value presented straight.'},
      {n:'Duty as moral framework', e:'The soldiers do what they do because it is their duty. The film does not mock this or treat it as false consciousness. Duty is a real thing that real people feel and act on, and the film respects it as a motivation.'},
      {n:'Sacrifice as the highest love', e:'Characters who give their lives for others are treated with reverence. The film does not suggest their sacrifice was wasted or that they were duped. Sacrifice is presented as the ultimate expression of love and duty.'},
      {n:'Competence as virtue', e:'The soldiers who survive are the ones who are good at their jobs. Skill, training, and preparation matter. The film respects professional military competence as something that keeps people alive rather than something to problematize.'},
      {n:'Honor as internal, not institutional', e:'The film distinguishes between institutional honor — medals, rank, recognition — and personal honor — doing the right thing when no one is watching. The latter is treated as real. The former is treated as decoration.'},
      {n:'Home as meaning, not just place', e:'What the soldiers fight for is home — not an abstraction but a specific, concrete, beloved reality. The film treats home as something worth dying for, which is the most traditional military framing possible.'},
      {n:'The mission matters', e:'Despite the film\'s clear-eyed view of war\'s cost, it treats the mission itself as legitimate. These men are not fighting for nothing. Their sacrifice has meaning beyond the personal. This is the line that separates the film from pure anti-war polemic.'},
      {n:'Passing the story to the next generation', e:'The film frames itself as a transmission — the story of these men must be told so the next generation understands what was given. This is a traditional understanding of historical memory as moral obligation.'},
    ],
  },
  // ============================================ BATCH 3 ============================================
  'ready-or-not-2': {
    woke: [
      {n:'Female rage as righteous force', e:'Grace returns as a bride who survived a deadly game and is now positioned as the hunter rather than the hunted. The film treats female rage as justified, powerful, and narratively satisfying — a progressive emotional framework that the first film established.'},
      {n:'Class warfare through horror', e:'The Le Domas family was literally a class of wealthy elites who hunted their servants and in-laws for sport. The sequel extends this critique to the broader network of wealthy families who play the same game. Rich people literally kill poor people for entertainment.'},
      {n:'Institutional complicity in elite predation', e:'The sequel reveals that the Le Domas family was not unique — the game is an intergenerational tradition among wealthy families. The film treats this as a systemic indictment rather than a one-family aberration. The system protects the predators.'},
    ],
    trad: [
      {n:'Marriage as sacred bond worth fighting for', e:'Despite the first film\'s nightmare wedding, the sequel treats Grace\'s marriage as something she chose and believed in. The betrayal is monstrous precisely because marriage is supposed to be sacred. The film honors the institution even as it depicts its violation.'},
      {n:'Survival through resourcefulness', e:'Grace survives because she is smart, tough, and resourceful. The film celebrates practical competence under pressure. No one saves her. She saves herself through grit and cleverness — the traditional survivor-hero template.'},
    ],
  },
  'how-to-make-a-killing': {
    woke: [
      {n:'Financial system as rigged game', e:'The film treats the financial system as structurally unfair — a casino where the house always wins and the players are lied to about the odds. This is a progressive economic critique dressed as a thriller about financial predators.'},
      {n:'Female competence in male-dominated finance', e:'The female lead navigates a world designed by and for men. Her competence is the equal of anyone in the room, but the room was not built for her. The film treats this as the water she swims in rather than a special obstacle she overcomes.'},
      {n:'Systemic corruption versus individual bad actors', e:'The film distinguishes between individual villains and the structures that enable them. The villains are bad, but the system that produces, protects, and rewards them is the real antagonist. This is the progressive framing: fix the system, not just the bad people.'},
      {n:'Moral relativism of financial crime', e:'The line between legal and illegal behavior in finance is portrayed as arbitrary and enforced selectively. The film treats the distinction as a form of class privilege — what is crime for the poor is business for the rich.'},
    ],
    trad: [
      {n:'Competence and skill as survival tools', e:'The characters who survive and succeed are the ones who are genuinely good at what they do. Skill matters. Preparation matters. The film respects professional excellence as something real and valuable, not just lucky or privileged.'},
      {n:'Loyalty tested and proven', e:'The central relationship is tested under extreme pressure and survives. The film treats loyalty as something that must be demonstrated under fire to be real, and presents proven loyalty as the most valuable thing two people can share.'},
      {n:'Justice as individual pursuit', e:'When institutions fail to deliver justice, the protagonists pursue it themselves. The film frames this as morally correct — when the system is broken, individual action is the only path to justice. This is a traditional framework that predates progressive institutional critique.'},
      {n:'Redemption through action', e:'Characters who have done wrong have the opportunity to make it right through what they do, not just what they feel. The film treats redemption as earned through action, not granted through apology. This is a traditional moral framework.'},
    ],
  },
  'opus-2025': {
    woke: [
      {n:'Cult of personality critique', e:'The film examines how cults of personality form around charismatic men and how institutions enable and protect them. The critique is not just of the individual predator but of the culture that creates the conditions for predation.'},
      {n:'Female journalist as truth-teller', e:'The protagonist is a female journalist whose pursuit of the story puts her in danger. The film treats journalism — particularly female investigative journalism — as a form of heroism and truth-telling as a moral obligation.'},
      {n:'Trauma and recovery as narrative arc', e:'Multiple characters are processing trauma from their encounters with the cult figure and the systems that protected him. The film treats trauma recovery as a valid and important narrative rather than as backstory to be overcome quickly.'},
      {n:'Media complicity in platforming predators', e:'The film indicts the media ecosystem that gave the predator his platform, treated him as genius rather than danger, and profited from his reputation. The critique is of the system, not just the individual.'},
    ],
    trad: [
      {n:'Truth as absolute and knowable', e:'The film treats truth as something that exists, can be discovered through investigation, and must be told regardless of consequences. There is no postmodern equivocation about "whose truth." The journalist seeks facts, not narratives.'},
      {n:'Courage as professional obligation', e:'The journalist protagonist puts herself at risk because the story must be told. The film treats this not as recklessness but as professional duty. Courage is not optional — it is required by the work she has chosen to do.'},
      {n:'Accountability as moral necessity', e:'The film insists that the predator must be held accountable, that institutions that enabled him must answer for it, and that there is no statute of limitations on moral debt. Consequences must follow actions. This is a traditional moral framework.'},
    ],
  },
  'love-hurts-2025': {
    woke: [
      {n:'Romantic tropes deconstructed', e:'The film examines romantic comedy conventions through a critical lens, questioning the assumptions about love, pursuit, and happily-ever-after that the genre traditionally naturalizes. Love is real, but the genre lies about what it looks like.'},
      {n:'Female emotional labor as invisible work', e:'The film highlights the emotional labor women perform in relationships — managing men\'s feelings, absorbing disappointment, performing happiness — and treats this labor as work that deserves recognition and compensation rather than as natural feminine duty.'},
      {n:'Interracial relationship as unremarkable', e:'The central couple is interracial without this being a plot point. The film treats interracial relationships as simply what love looks like in contemporary America — a progressive normalization that doesn\'t announce itself as progressive.'},
    ],
    trad: [
      {n:'Commitment as courageous choice', e:'The film treats choosing to commit to another person as an act of courage. Love is scary. Staying is hard. The characters who find happiness are the ones who face the fear and commit anyway. This is a deeply traditional view of romantic love.'},
      {n:'Forgiveness as relationship skill', e:'Characters hurt each other — genuinely, not in rom-com misunderstanding ways — and must learn to forgive. The film treats forgiveness as a difficult, active process rather than a passive letting-go. It is work, and the work is worth it.'},
      {n:'Love as transformation', e:'The characters who love well become better versions of themselves. The film treats romantic love as genuinely transformative — not in the fantasy sense but in the sense that committing to another person changes who you are. This is a traditional claim about love.'},
      {n:'Family approval as genuine good', e:'The film does not mock the desire for parental approval of a romantic partner. It treats family blessing as something worth wanting — a traditional value that contemporary romance often treats as oppressive rather than meaningful.'},
    ],
  },
  'tony-2026': {
    woke: [
      {n:'Anti-gang violence messaging', e:'The film explicitly frames gang violence as a systemic problem driven by poverty and lack of opportunity rather than individual moral failing. The structural analysis of why young men join gangs is a progressive framework.'},
      {n:'Diverse cast reflecting urban reality', e:'The casting reflects the demographic reality of the setting without tokenism. The film treats diversity as truth-telling about what the world looks like rather than as a production checkbox.'},
    ],
    trad: [
      {n:'Redemption through personal transformation', e:'Tony\'s arc is fundamentally about becoming a different person through his own choices. The film treats redemption as real and available — you can change who you are, and what you were does not have to be what you will be. This is a traditional moral framework.'},
      {n:'Mentorship and positive male role models', e:'Tony encounters older men who model a different way of being — men who have been where he is and found another path. The film treats intergenerational male mentorship as a genuine good and a lifeline for young men.'},
      {n:'Loyalty to community over self', e:'Tony\'s eventual choice is to serve his community rather than escape it. The film treats loyalty to place and people as a higher value than individual advancement. This is a traditional communitarian ethic.'},
      {n:'Violence as cycle to be broken', e:'The film treats the decision to break the cycle of violence as a moral choice. Tony can continue what he inherited or he can be the one who stops it. The film treats choosing peace as strength, not weakness — a traditional moral position.'},
      {n:'Family as motivation for change', e:'Tony changes not for himself but for the people who depend on him. The film treats family obligation as a positive motivator rather than a burden. Wanting better for your children is the most traditional motivation there is.'},
    ],
  },
  'ferris-buellers-day-off-1986': {
    woke: [],
    trad: [
      {n:'Individual freedom as highest good', e:'Ferris Bueller is a one-man argument for individual liberty against institutional conformity. He skips school, impersonates authority figures, and hijacks a parade — all in service of showing his friend Cameron that life is meant to be lived, not endured. The film treats Ferris as a folk hero, not a delinquent.'},
      {n:'Friendship as transformative relationship', e:'The entire film is Ferris trying to save Cameron from his own fear and passivity before graduation separates them forever. The friendship is the plot. The Ferrari is a prop. Cameron\'s liberation is the real victory. The film treats male friendship with a sincerity that was unusual in 1986 and would be unheard of now.'},
      {n:'Carpe diem philosophy', e:'"Life moves pretty fast. If you don\'t stop and look around once in a while, you could miss it." The film is a feature-length argument for seizing the day, for experience over caution, for living instead of planning to live. This is as traditional a philosophy as exists, delivered without apology.'},
      {n:'Rejection of institutional authority', e:'Principal Rooney is a villain precisely because he treats students as inmates and school as prison. The film sides entirely with Ferris against every authority figure. This is not anti-establishment politics — it is the American individualist tradition of skeptical citizenship.'},
      {n:'Art and culture as human birthright', e:'The Art Institute sequence is the film\'s genuine emotional center. Ferris, Cameron, and Sloane stand before Seurat in silence, and the film treats this moment — teenagers experiencing great art — as sacred. Culture belongs to everyone. The museum is a church and the film knows it.'},
      {n:'Suburban Chicago as world enough', e:'The film treats Chicago and its suburbs as containing everything a person needs for a perfect day — a ballgame, a parade, a museum, a fancy lunch, a best friend, a girlfriend. It does not need New York or Paris to feel big. This is a Midwestern argument for the sufficiency of home.'},
      {n:'Teenage joy as morally sufficient', e:'The film does not moralize about Ferris skipping school. It treats his joy as self-justifying. Happiness is not something you earn through compliance. It is something you claim. This is a traditional celebration of human flourishing that does not require suffering as prerequisite.'},
    ],
  },
  'the-sun-never-sets-2026': {
    woke: [
      {n:'Post-colonial reckoning with empire', e:'The title itself is ironic — a reference to the British Empire on which the sun never set — and the film examines the moral cost of that empire. It treats imperial legacy as something to be reckoned with rather than celebrated.'},
      {n:'Diverse perspectives on historical events', e:'The narrative incorporates non-British perspectives on imperial history rather than defaulting to the colonizer viewpoint. The film treats these perspectives as equally valid rather than supplementary.'},
      {n:'Systemic analysis of historical injustice', e:'The film frames imperial wrongs as systemic rather than individual — the evil is in the structure, not just in a few bad actors within it. This is a progressive historical analysis framework.'},
    ],
    trad: [
      {n:'Duty and service as meaningful', e:'Despite the critical framework, the film treats individual British soldiers and administrators who served honorably as deserving of respect. Duty honestly performed is not invalidated by the moral complexity of the institution it served.'},
      {n:'Historical complexity over simple judgment', e:'The film resists the temptation to reduce imperial history to a simple morality play. People made choices in contexts that constrained them. The film treats historical actors with the complexity they deserve rather than as villains or heroes.'},
      {n:'Courage as universal virtue', e:'Characters on multiple sides demonstrate genuine courage, and the film treats this as admirable regardless of whose cause they serve. Courage is real and courage matters, even when we disagree with what it serves.'},
      {n:'Institutions as capable of reform', e:'The film does not conclude that institutions are inherently corrupt and must be abolished. It argues that institutions can and must reform, and that the work of reform is worth doing. This is a reformist rather than revolutionary position.'},
      {n:'Personal honor within flawed systems', e:'Characters who maintain personal honor while serving flawed institutions are treated with nuance rather than condemnation. The film recognizes the genuine moral dilemma of the good person in the bad system — a traditionally complex moral position.'},
    ],
  },
  // ============================================ BATCH 4 ============================================
  'dirty-harry-1971': {
    woke: [
      {n:'Vigilante justice as critique of liberal legalism', e:'Harry Callahan operates outside the law because the law protects criminals more than victims. The film frames Miranda rights, due process, and legal technicalities as obstacles to justice. This resonated with a conservative backlash against Warren Court decisions, but from a modern lens, the film is making an explicitly anti-liberal argument.'},
      {n:'Racial coding of criminality', e:'The film\'s villains are disproportionately non-white in a way that reflects 1970s urban anxiety about crime. Scorpio is coded as a counterculture figure — long hair, peace symbol belt buckle — linking criminality to the hippie movement. This is a reactionary visual language that registers differently now.'},
    ],
    trad: [
      {n:'Individual action when institutions fail', e:'Harry Callahan is the archetype of the cop who gets results because he ignores the rules. The film treats institutional constraint as moral cowardice and individual action as the only path to justice. This is the template for every rogue cop film that followed.'},
      {n:'Clear moral universe', e:'Scorpio is evil — not misunderstood, not a product of society, not worthy of rehabilitation. He tortures and murders for pleasure. Harry is good — gruff, difficult, anti-social, but good. The film does not complicate this. Evil exists and must be stopped.'},
      {n:'Physical courage as moral requirement', e:'Harry runs toward gunfire when others run away. The film treats this as definitional — a man who will not face danger to protect others is not fully a man. This is a traditional masculine ethic presented without qualification or apology.'},
      {n:'Protection of the innocent', e:'Harry\'s defining motivation is protecting victims. The girl in the hole, the school bus full of children — his violence is always in service of the defenseless. The film treats protection of the innocent as the highest calling and justifies his methods by the urgency of the need.'},
      {n:'The .44 Magnum as moral clarity', e:"The most powerful handgun in the world is not just a weapon — it is an argument. When Harry points it at Scorpio and delivers the \"do you feel lucky\" speech, he is offering a choice: surrender or die. The gun is moral clarity made metal. The film treats this clarity as admirable."},
      {n:'San Francisco as fallen city', e:'The film uses San Francisco not as a postcard but as a cautionary tale — a beautiful city ruined by crime, permissiveness, and a legal system that coddles predators. The film is a conservative lament for urban America dressed as a police procedural.'},
      {n:"Justice as Harry's only religion", e:'Harry has no family, no friendships, no life outside the job. He is a monk of justice — celibate, ascetic, and absolutely committed. The film treats this as noble rather than tragic. The single-minded pursuit of justice is a vocation, not a pathology.'},
    ],
  },
  'the-empire-strikes-back-1980': {
    woke: [
      {n:'Imperial critique as Vietnam allegory', e:'The Empire is a militarized, technologically superior force trying to crush a scrappy insurgency. The film inherits the original Star Wars Vietnam allegory that positions the rebels as freedom fighters against imperial aggression — a progressive anti-war framework from the 1970s.'},
      {n:'Leia as competent female leader', e:'Leia Organa commands the Rebel base on Hoth, participates in combat, and makes strategic decisions that affect the entire rebellion. In 1980, a woman in this role was unusual. The film treats her authority as natural and deserved.'},
    ],
    trad: [
      {n:'The hero\'s journey', e:'Luke Skywalker follows the Campbellian monomyth beat for beat: call to adventure, supernatural aid, threshold crossing, trials, abyss, transformation, atonement, return. The film treats this ancient narrative structure with complete sincerity — no irony, no deconstruction, no subversion.'},
      {n:'Master-apprentice relationship', e:'Yoda teaches Luke, and the teaching relationship is treated as sacred. The master demands discipline, patience, and trust. The apprentice must earn knowledge through submission and practice. This is a traditional pedagogical model that the film honors without question.'},
      {n:'Father-son conflict as cosmic drama', e:"The \"I am your father\" revelation transforms the entire trilogy into a family drama played out on a galactic scale. The film treats the father-son relationship as the most important relationship in the universe — a traditional prioritization of family bonds."},
      {n:'Self-sacrifice for friends', e:'Han Solo is frozen in carbonite because he stayed to help his friends. Luke abandons his training to save them. The film treats self-sacrifice for loved ones as the highest moral act — no calculus, no hesitation, just the certainty that you save your people.'},
      {n:'Good and evil as metaphysical realities', e:'The Force has a Light Side and a Dark Side. These are not perspectives or cultural constructs. They are real. The film treats moral reality as objective — some things are good, some things are evil, and the difference matters absolutely.'},
      {n:'Temptation and fall', e:'Darth Vader tempts Luke with power, with belonging, with the end of conflict. The temptation is real and the fall is possible. The film treats moral failure as a genuine danger that even a hero must resist — a traditional understanding of human moral vulnerability.'},
      {n:'Hope as strategic asset', e:'The title announces the film\'s thesis: the Empire strikes back, but the response is hope. Not optimism, not calculation — hope. The film treats hope as a real force that matters in outcomes. This is a traditional virtue framework in science fiction clothing.'},
    ],
  },
  'memento-2000': {
    woke: [
      {n:'Unreliable narrator as truth critique', e:'Leonard\'s condition means he cannot form new memories — and the film structures itself to make the audience share his confusion. The result is a radical destabilization of narrative authority. There is no objective truth, only Leonard\'s constructed truth. This is a postmodern epistemological position.'},
      {n:'Vengeance as hollow motivation', e:'Leonard\'s quest for revenge is revealed to be a fiction he maintains to give his life meaning. The film treats vengeance not as justice but as self-deception — a man killing strangers to feel like a hero. This is a progressive critique of retributive justice.'},
      {n:'Identity as performance, not essence', e:'Leonard literally tattoos his identity onto his body because he cannot remember who he is. The film treats identity as something constructed, maintained, and ultimately fictional rather than something innate. This is a progressive understanding of selfhood.'},
    ],
    trad: [
      {n:'Facts exist even when narratives lie', e:'Beneath the structural trick, the film contains an objective sequence of events that happened. Teddy tells Leonard the truth in the final scene — a truth the audience can verify by tracing the chronology. The film believes in facts even as it demonstrates how easily they are manipulated.'},
      {n:'Consequences cannot be escaped', e:'Leonard\'s condition allows him to forget what he has done, but the film insists that forgetting does not equal absolution. Actions have consequences regardless of whether the actor remembers them. This is a traditional moral framework.'},
      {n:'Self-knowledge as essential', e:'Leonard\'s tragedy is not his condition but his refusal to accept who he really is. He chooses the comforting lie over the difficult truth. The film treats this as a moral failure — the obligation to know yourself honestly.'},
      {n:'Trust and betrayal as moral categories', e:'Every relationship in the film is defined by trust or its violation. Teddy exploits Leonard. Natalie manipulates him. Leonard betrayed himself. The film treats trust as the foundation of human relationship and betrayal as a genuine evil.'},
      {n:'Purpose requires truth', e:'Leonard\'s purpose — avenging his wife — is a lie he tells himself. Without truth, purpose is self-deception. The film treats the desire for purpose as human and the construction of false purpose as tragedy. Real purpose requires real truth.'},
    ],
  },
  'mayday-2026': {
    woke: [
      {n:'Female protagonist in action-thriller', e:'The lead is a woman in a genre traditionally built around male protagonists. Her competence is assumed, not explained. The film treats female action heroes as simply what stories look like now.'},
      {n:'Systemic corruption as antagonist', e:'The villains are not rogue individuals but representatives of systems that protect and enable them. The film treats institutional corruption as the real enemy rather than just bad people within functional systems.'},
      {n:'Diverse cast as production baseline', e:'The ensemble reflects deliberate diversity without tokenism. Characters of different backgrounds occupy roles across the moral spectrum. The film treats representation as a fact of production, not a narrative feature.'},
    ],
    trad: [
      {n:'Competence through training and preparation', e:'The protagonist survives because she is good at her job. The film spends time establishing her skills — they are earned, not innate. Professional excellence is treated as admirable and essential.'},
      {n:'Loyalty tested under fire', e:'Relationships are tested by extreme circumstances, and those that survive are treated as proven and valuable. The film treats loyalty as something demonstrated through action rather than declared.'},
      {n:'Personal courage as defining virtue', e:'The protagonist is afraid but acts anyway. The film treats this as the definition of courage — not fearlessness but mastery of fear. This is the traditional understanding of courage going back to Aristotle.'},
      {n:'Justice through individual action', e:'When institutions fail to deliver justice, the protagonist pursues it personally. The film frames this as morally correct — individual pursuit of justice is legitimate when systems abdicate.'},
      {n:'Truth-telling as moral obligation', e:'The protagonist risks everything to expose the truth. The film treats truth-telling as a moral imperative that transcends personal safety, institutional loyalty, and pragmatic calculation.'},
    ],
  },
  'american-psycho-2000': {
    woke: [
      {n:'Toxic masculinity as horror subject', e:'Patrick Bateman is a case study in toxic masculinity: obsessed with status, physical appearance, dominance, and violence. The film treats his masculinity not as aspirational but as pathological — the logical endpoint of a culture that values men only for their performance.'},
      {n:'Consumer capitalism as identity erasure', e:'Bateman\'s obsession with business cards, skin care routines, and restaurant reservations is not just satire of 1980s excess. It is an argument that consumer capitalism reduces people to interchangeable products. Bateman is indistinguishable from his peers because consumer identity is meaningless.'},
      {n:'Misogyny as violence practice', e:'Bateman\'s violence escalates from sex workers to women he knows. The film treats his misogyny not as incidental personality trait but as the logical progression of a worldview that treats women as objects. His violence is gendered because his worldview is gendered.'},
    ],
    trad: [
      {n:'Moral emptiness as horror', e:'Bateman\'s defining characteristic is not his violence but his emptiness. He confesses to murder and no one cares, no one believes him, no one even notices. The film treats the absence of moral substance as the most terrifying thing about him — a traditional affirmation that morality matters by showing its absence.'},
      {n:'Guilt as proof of humanity', e:'Bateman cannot feel guilt. He confesses hoping for punishment that never comes. The film treats this inability as his true monstrosity — not the killing but the fact that killing does not register. The capacity for guilt is what makes us human.'},
      {n:'Justice as something Bateman wants and cannot get', e:'The film\'s most subversive move is having Bateman seek punishment and be denied it. He wants consequences. He wants to be held accountable. The culture around him is too empty to provide this. The film treats the absence of justice as horror.'},
      {n:'Reality as something Bateman cannot reach', e:'Beneath the satire and the gore, the film is about a man who cannot feel reality. His violence is an attempt to break through to something real. The film treats the loss of contact with reality as a spiritual catastrophe.'},
      {n:'The surface is a lie', e:'Every surface in the film — the bodies, the business cards, the skincare — is immaculate and every immaculate surface conceals rot. The film is a traditional moral argument that beautiful surfaces hide moral decay and that the truth is underneath.'},
    ],
  },
  'onslaught-2026': {
    woke: [
      {n:'Diverse ensemble in genre framework', e:'The cast reflects demographic diversity as production baseline. The film treats diverse casting as normal rather than noteworthy — characters of different backgrounds occupy the same genre positions that would historically default to white actors.'},
      {n:'Genre-aware deconstruction of violence', e:'The film is aware of its position within the action genre and interrogates the violence it depicts. Characters are affected by what they do. The film treats violence as having moral weight.'},
      {n:'Institutional skepticism', e:'The film presents official channels and institutional responses as inadequate or corrupt. The protagonists operate outside formal structures because formal structures have failed.'},
    ],
    trad: [
      {n:'Team cohesion as survival mechanism', e:'The ensemble survives because they work together, trust each other, and subordinate individual glory to collective success. The film treats teamwork as morally and practically superior to individualism.'},
      {n:'Competence as virtue', e:'The characters who survive are the ones who are genuinely skilled. Training, preparation, and professional excellence are treated as real and valuable. The film respects competence.'},
      {n:'Protection of the vulnerable', e:'The protagonists risk themselves to protect people who cannot protect themselves. The film treats this as definitionally heroic. Protection of the weak is the moral baseline.'},
      {n:'Courage under fire', e:'Characters who face danger rather than fleeing are treated as admirable. Physical courage is presented as real and valuable, not as toxic or performative.'},
      {n:'Loyalty as earned and tested', e:'Trust between characters is built through shared experience and tested under pressure. The film treats loyalty as something demonstrated rather than declared.'},
    ],
  },
  'airplane-1980': {
    woke: [
      {n:'Satirical treatment of authority figures', e:'Every authority figure in the film — pilots, doctors, military officers — is incompetent, deranged, or both. The film systematically mocks institutional authority across every domain. This is more anarchic comedy than political statement, but it registers as anti-authoritarian.'},
      {n:'Subversive treatment of social norms', e:'The film\'s comedy derives from systematically violating every norm of polite behavior, professional conduct, and social expectation. This transgressive energy has a countercultural DNA even when it is not explicitly political.'},
    ],
    trad: [
      {n:'Competence from unexpected sources', e:'Ted Striker saves the plane not because he is the designated hero but because he is the only person with the specific skill required. The film treats competence as real and valuable — it just finds it in unexpected places.'},
      {n:'Redemption through action', e:'Ted Striker\'s arc is classically redemptive: a man haunted by past failure gets a second chance and proves himself. The film plays this entirely straight under the jokes — Ted earns his redemption through what he does.'},
      {n:'Love as motivation', e:'Ted gets on the plane to win Elaine back. Every absurd thing that happens flows from a man trying to save the woman he loves. The film treats romantic love as a sufficient motivation for heroism.'},
      {n:'Collective effort in crisis', e:'The plane lands because everyone — the crew, the control tower, the passengers — works together. The film treats collective effort in crisis as natural and admirable, even when the individual participants are ridiculous.'},
      {n:'Classic Hollywood structure preserved', e:'Beneath the parody, Airplane! has the structure of a classic disaster film: setup, crisis escalation, climax, resolution. The film respects the narrative form it is parodying — it just fills it with jokes.'},
    ],
  },
  'the-uprising-2026': {
    woke: [
      {n:'Grassroots resistance as narrative engine', e:'The uprising is not led by a chosen hero but by ordinary people who decide they will not accept the status quo. The film treats collective action as legitimate and necessary — a progressive political framework.'},
      {n:'Systemic oppression as villain', e:'The antagonist is not an individual tyrant but a system that produces, protects, and normalizes injustice. The film treats systemic change as the only real solution.'},
      {n:'Diverse coalition as protagonist', e:'The resistance is deliberately diverse, with characters from different backgrounds finding common cause. The film treats coalition-building across difference as the path to change.'},
      {n:'Media as tool of control', e:'The film examines how the regime uses media to manufacture consent, suppress dissent, and delegitimize resistance. This is a progressive media critique.'},
    ],
    trad: [
      {n:'Freedom as worth dying for', e:'The film treats political freedom as a value that justifies sacrifice. Characters who give their lives for freedom are treated as heroes. This is a traditional valorization of liberty.'},
      {n:'Individual conscience against collective pressure', e:'Characters who refuse to go along, who insist on doing the right thing when compliance is easier, are treated as heroes. The film treats individual conscience as the ultimate moral authority.'},
      {n:'Courage as moral obligation', e:'The film treats the decision to resist as a moral requirement, not a lifestyle choice. When the system is unjust, resistance is not optional. This is a traditional moral framework.'},
      {n:'Family as motivation for resistance', e:'Characters resist not just for abstract principles but for their children, their parents, their loved ones. The film treats family protection as a legitimate and powerful motivation for political action.'},
      {n:'Hope as strategic necessity', e:'The film treats hope not as naive optimism but as a requirement for action. You cannot resist what you cannot imagine defeating. Hope is the precondition for courage.'},
    ],
  },
  'dead-poets-society-1989': {
    woke: [
      {n:'Non-conformity as moral imperative', e:'Keating teaches his students to think for themselves, challenge authority, and resist conformity. The film treats institutional tradition as a prison and individual authenticity as liberation. This is a progressive educational philosophy.'},
      {n:'Art as resistance', e:'Poetry is not just a subject — it is a weapon against conformity, a path to selfhood, and a form of rebellion. The film treats art as inherently subversive of institutional power.'},
      {n:'Critique of patriarchal authority', e:'Neil\'s father is the film\'s true antagonist — not Welton Academy but the patriarchal demand that sons replicate their fathers\' lives. The film treats patriarchal control as destructive and lethal.'},
      {n:'Toxic masculinity as tragedy', e:'The pressure on boys to conform, achieve, and suppress emotion is what destroys Neil. The film treats traditional masculine expectations as a system that damages the young men it claims to prepare.'},
    ],
    trad: [
      {n:'Carpe diem as ancient wisdom', e:'Keating\'s philosophy is not a modern invention — he is teaching Horace, the Roman poet. The film grounds its argument in a classical tradition that predates modern progressive education by two millennia. Seize the day is not a new idea.'},
      {n:'Mentorship as sacred relationship', e:'Keating\'s relationship with his students is treated as the most important thing in their lives. A teacher who changes how you see the world. The film treats this relationship with complete seriousness.'},
      {n:'Poetry as soul formation', e:'The film treats poetry not as an academic subject but as something that forms the soul. Literature matters because it teaches you how to be human. This is a traditional humanist position that predates and transcends progressive education.'},
      {n:'Tradition as something to master before transcending', e:'Keating does not reject the canon — he teaches it with passion. He wants students to engage tradition deeply, not discard it. The film treats the Western literary tradition as worth preserving and transmitting.'},
      {n:'Individual voice as highest achievement', e:'The film treats finding your own voice as the purpose of education. Not reproducing the teacher\'s ideas, not performing for the grade, but discovering what you actually think and having the courage to say it.'},
    ],
  },
  'brokeback-mountain-2005': {
    woke: [
      {n:'Queer love as serious cinema', e:'Brokeback Mountain was the first major studio film to treat a same-sex love story with the emotional seriousness and artistic ambition previously reserved for heterosexual romance. Its existence in the mainstream was itself a progressive statement.'},
      {n:'Rural masculinity as sexual repression', e:'The film locates the tragedy not in the characters\' love but in a culture that makes that love impossible. Ennis and Jack live in a world where being gay means death — literally, as the murder story that haunts Ennis proves. The film treats homophobia as the villain.'},
      {n:'Marriage as cage for queer desire', e:'Both men marry women, have children, and perform heterosexual domesticity. The film treats these marriages as prisons — not because marriage is bad but because these particular marriages are built on a lie. The women are victims of a culture that demands the lie.'},
      {n:'Violence as enforcement of heteronormativity', e:'The film\'s defining traumatic memory is Ennis witnessing a gay man being beaten to death. This memory controls his entire life. The film treats homophobic violence as the mechanism that enforces the closet and destroys lives.'},
      {n:'Masculinity as performance', e:'Jack and Ennis perform masculinity constantly — the stoicism, the silence, the violence. The moments when they drop the performance — on Brokeback Mountain, in their brief reunions — are the only moments they are truly alive. The film treats masculinity as a costume that strangles the wearer.'},
    ],
    trad: [
      {n:'Love as absolute and undeniable', e:'The film treats Jack and Ennis\'s love as real — not a phase, not confusion, not something they could have chosen differently. It is the central fact of their lives, and everything else is a response to it. This is a traditional romantic claim: love is real, love is permanent, love defines you.'},
      {n:'Commitment as what love demands', e:'The tragedy is not that they love each other but that they cannot fully commit. Jack wants to build a life together. Ennis cannot. The film treats Jack\'s desire for commitment as the more honest and courageous position.'},
      {n:'The natural world as sanctuary', e:'Brokeback Mountain is the only place Jack and Ennis can be together because it is outside civilization. Nature is sanctuary, freedom, truth. Society is prison, constraint, lies. This is a traditional romantic understanding of nature as moral refuge.'},
      {n:'Loss as permanent', e:'The film insists that Ennis will never get over Jack. The final scene — the two shirts, the postcard, Ennis alone — treats grief as something you carry forever. Some losses do not heal. This is a traditional understanding of grief that resists closure culture.'},
      {n:'Loyalty as highest virtue', e:'Ennis\'s loyalty to Jack — decades-long, life-defining, surviving marriage and distance and death — is treated as the most real thing about him. The film treats the capacity for lifelong loyalty as the measure of a person.'},
    ],
  },
};

function main() {
  const revPath = path.resolve(__dirname, '..', 'src', 'data', 'reviews.json');
  const reviews = JSON.parse(fs.readFileSync(revPath, 'utf8'));

  for (const [slug, data] of Object.entries(DATA)) {
    const r = reviews.find(r => r && r.slug === slug);
    if (!r || !Array.isArray(r.tropeAudit)) { console.error('MISSING', slug); continue; }

    let wi = 0, ti = 0;
    const wokeNames = data.woke || [];
    const tradNames = data.trad || [];

    for (const t of r.tropeAudit) {
      if (t.category === 'Woke') {
        if (wi < wokeNames.length) {
          t.name = wokeNames[wi].n;
          t.explanation = wokeNames[wi].e;
          wi++;
        }
      } else {
        if (ti < tradNames.length) {
          t.name = tradNames[ti].n;
          t.explanation = tradNames[ti].e;
          ti++;
        }
      }
    }

    if (wi !== wokeNames.length) console.error(`${slug}: woke mismatch — got ${wi}, need ${wokeNames.length}`);
    if (ti !== tradNames.length) console.error(`${slug}: trad mismatch — got ${ti}, need ${tradNames.length}`);
    console.log(`${slug}: OK (${wi}W + ${ti}T)`);
  }

  fs.writeFileSync(revPath, JSON.stringify(reviews, null, 2));
  console.log('\nWritten to reviews.json');
}

main();