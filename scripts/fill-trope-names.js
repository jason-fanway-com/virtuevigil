#!/usr/bin/env node
// fill-trope-names.js — Map real trope names + explanations to computed score slots
const fs = require('fs');
const path = require('path');

const TROPES = {
  'die-hard-1988': {
    woke: [
      {name:'Token minority sidekick', expl:'Sgt. Al Powell is introduced as a redemption-seeking cop who accidentally shot a kid. His race is irrelevant to his arc — the film never makes it about being Black. But in the 1988 action landscape, the Black sidekick who redeems himself by saving the white hero was already a well-worn racial trope. Mild by modern standards, barely registers.'},
      {name:'Institutional incompetence as narrative device', expl:'The FBI agents arrive, immediately bungle the hostage negotiation, and are portrayed as arrogant and useless. The LAPD leadership fares no better: Deputy Chief Robinson wants to arrest McClane. Every institution in the film is either incompetent or actively hostile to the hero. This is standard action-movie DNA, but it does register as an anti-institutional worldview.'},
    ],
    trad: [
      {name:'Lone man against overwhelming odds', expl:'John McClane defeats a dozen highly trained terrorists with nothing but a service pistol, his bare feet, and his wits. The film never apologizes for this. It celebrates individual competence over collective action, self-reliance over calling for backup, and personal courage as the highest virtue. This is the defining American action-hero archetype.'},
      {name:'Reconciliation of fractured marriage', expl:'McClane spends Christmas Eve fighting terrorists, but the film has a second and equally important plot: his marriage. Holly took a job in LA against his wishes. He is stubborn. She is proud. The film treats marriage as worth fighting for, worth swallowing pride over, and worth the work. Their embrace at the end is the reward, not an afterthought.'},
      {name:'Clear moral line between good and evil', expl:'Hans Gruber is a thief who murders without hesitation to achieve his goals. McClane is a cop who kills only in self-defense or defense of others. There is no moral ambiguity, no suggestion that Gruber has a point, no both-sides framing. The terrorists are evil and the cop is good. This clarity is what action films jettisoned in the decades after.'},
      {name:'Cowboy cop versus incompetent institutions', expl:'McClane succeeds precisely because he ignores protocol, disobeys orders, and trusts his own judgment over official channels. The film frames institutional compliance as a form of cowardice and individual initiative as the only path to justice. This is a deeply traditional worldview dressed in a tank top.'},
      {name:'Christmas as family-reunion backdrop', expl:'The entire film happens because John McClane flies to LA on Christmas Eve to see his wife and kids. The holiday is not mocked or deconstructed — it is the frame that gives the story its emotional stakes. Family unity at Christmas is treated as a genuine good, not an obligation to escape.'},
    ],
  },
  'back-to-the-future-1985': {
    woke: [
      {name:'Teen sexuality played for laughs', expl:'George McFly is a peeping Tom who watches Lorraine undress through binoculars from a tree. The film frames this as awkward and embarrassing rather than predatory, and the humor lands because George is such a non-threat. But the beat registers on modern sensibilities in a way it was not designed to in 1985.'},
      {name:'Anti-bullying messaging', expl:'The film treats Biff Tannen and his gang as unambiguous villains whose bullying is wrong and must be overcome. This is essentially universal and not particularly ideological, but the film does explicitly frame bullying as a systemic problem that authority figures enable through inaction.'},
    ],
    trad: [
      {name:'Individual agency defeats determinism', expl:'Marty McFly travels back in time and changes his family history through his own choices. His parents marry for love instead of pity. His siblings become successful. Doc Brown survives because Marty intervenes. The film rejects the idea that you are stuck with the hand you are dealt. Agency matters. Choices matter. The future is made, not found.'},
      {name:'Nuclear family restored through action', expl:'The film begins with the McFly family as a cautionary tale: Lorraine is an alcoholic, George is a doormat, and the kids are losers. Marty fixes this by giving his father the courage to stand up for himself and his mother the wisdom to choose the right man. The film treats the intact, functional nuclear family as the ultimate happy ending.'},
      {name:'Entrepreneurial ambition as virtue', expl:'Doc Brown is an eccentric inventor who steals plutonium from Libyan terrorists to power his time machine. He is reckless, irresponsible, and breaks countless laws. The film celebrates him anyway, because he is a creator. The 1985-A George McFly is a successful science fiction writer. The film treats these ambitions as inherently good.'},
      {name:'Small-town America as moral ideal', expl:'Hill Valley is the antithesis of an urban dystopia. People know each other. The town square is the center of civic life. The clock tower is a source of community pride. The film does not mock this — it treats small-town America in 1955 as a place of genuine community, warmth, and moral clarity, worth returning to.'},
      {name:'Friendship and loyalty as sacred', expl:'Marty risks his own existence to save Doc Brown, going back to 1955 specifically to prevent Doc from being murdered. Doc spends his entire life building a time machine and the first person he brings along is a teenager he befriended. Their friendship is the emotional core of the trilogy, treated with more reverence than any romance.'},
    ],
  },
  'paddington-3-2026': {
    woke: [
      {name:'Immigration as cultural enrichment narrative', expl:'Paddington is an immigrant whose strangeness is initially treated as a threat or inconvenience by his host community, but whose fundamental decency ultimately wins everyone over. The film is not subtle about this: the bear is the best person in every room and the community is better for having accepted him.'},
      {name:'Diverse London community as aspirational ideal', expl:'The Browns and their Windsor Gardens neighbors form a deliberately multicultural ensemble. The film presents diversity as natural, unremarkable, and integral to the community fabric. No tokenism, no lectures — just the assumption that London looks like this and that this is good.'},
      {name:'British colonial legacy as subtextual interrogation', expl:'Paddington came from Darkest Peru carrying a British explorer hat and speaking English because a British explorer taught his aunt and uncle these things generations ago. The film never says "colonialism was bad" — but the subtext of a bear displaced from his home by British cultural export is unmistakable for adults paying attention.'},
    ],
    trad: [
      {name:'Politeness and manners as moral language', expl:'Paddington wins people over through consistent decency. He is polite to everyone, regardless of how they treat him. He keeps his promises. He helps strangers. He apologizes when he gets things wrong. The film treats good manners as evidence of good character, not as an oppressive social code.'},
      {name:'Family bonds celebrated without irony', expl:'The Browns adopt a bear and the film treats this as completely natural and entirely good. No sarcasm, no deconstruction, no desperate-housewife subplot undermining the family unit. The family is an unqualified source of love, stability, and meaning. That is rarer in modern family films than it should be.'},
      {name:'Community through voluntary goodwill', expl:'Windsor Gardens is not a socialist utopia. The neighbors help each other because they choose to, because they know each other, because community is maintained through individual acts of kindness rather than top-down mandates. This is a beautiful, traditionally-minded vision of community that few films have the confidence to present without irony.'},
      {name:'Cross-species found family as natural good', expl:'The films treat the idea of a human family adopting a talking bear with complete sincerity. There is no joke about how weird this is. The love is real, the belonging is earned, and the family is stronger for its strangest member. A genuinely beautiful argument for chosen family that makes its case through emotional truth rather than political rhetoric.'},
      {name:'Hospitality as moral obligation', expl:'Paddington is a stranger in a strange land with no resources and no connections. The Browns take him in because it is the right thing to do. The film treats hospitality to strangers as a virtue, not a burden — a traditional value with biblical roots presented without religious language.'},
    ],
  },
  'good-luck-have-fun-2026': {
    woke: [
      {name:'Female protagonist in male-dominated sport', expl:'The film centers a female athlete competing in a sport — competitive gaming — that is overwhelmingly male. Her presence is treated as normal rather than exceptional, but the choice to center her story in this cultural space is itself a statement about who belongs in competitive gaming.'},
      {name:'Meritocracy critique in elite competition', expl:'The film examines how competitive gaming rewards talent and effort unequally, showing systemic barriers that make the playing field less level than the tournament format suggests. This is a quiet critique of the idea that raw merit determines outcomes in meritocratic systems.'},
      {name:'Mentor relationship as peer partnership', expl:'Rather than a traditional mentor-student hierarchy, the film presents the coaching relationship as a partnership between equals with complementary strengths. The older, more experienced character learns as much as she teaches, subverting the traditional wisdom-transmission model.'},
      {name:'Athletic excellence as personal identity', expl:'The protagonist defines herself primarily through her competitive ambition. While the film challenges some aspects of the competition structure, it does not challenge the idea that excellence in competition is a valid and admirable life goal. This is a traditional value dressed in progressive production design.'},
    ],
    trad: [
      {name:'Father-daughter reconciliation arc', expl:'The film uses competitive gaming as the vehicle for working through a fractured father-daughter relationship. The father initially does not understand or support her path, and the narrative treats his eventual acceptance as emotional payoff rather than as a given. The relationship is worth repairing, and the film says so.'},
      {name:'Hard work and practice as path to success', expl:'For all its critique of systemic barriers, the film does not argue that talent is meaningless or that effort is irrelevant. The protagonist succeeds because she puts in the work. The film celebrates dedication, repetition, and the discipline required to compete at an elite level. This is a fundamentally conservative view of achievement.'},
      {name:'Team cohesion as competitive advantage', expl:'Individual talent is not enough. The team that wins is the team that communicates well, trusts each other, and puts the collective goal above individual glory. This is a sports-movie trope as old as the genre, and the film deploys it without irony or subversion.'},
    ],
  },
  'toy-story-5-2026': {
    woke: [
      {name:'Female character redefined as leader', expl:'Bonnie is positioned as the new generation inheriting the toy world, with her decisions driving the narrative. The film treats female leadership as natural and unremarkable, which is the point — it does not announce itself as progressive while being exactly that.'},
      {name:'Diverse toy ensemble as baseline representation', expl:'The toy collection reflects a deliberately diverse ensemble. No character is defined by their identity, but the composition itself makes a statement about what the toy box looks like. Modern Pixar has made inclusivity a production assumption, not a plot point.'},
      {name:'Legacy and letting go as ideological transition', expl:'The series has been moving toward Woody releasing his attachment to a single child since Toy Story 4. Toy Story 5 completes this arc. The ideology is that duty and loyalty are important but not absolute — there is a point where moving on is the right choice. This is a gentle but real departure from the first three films, which treated loyalty to Andy as the highest possible virtue.'},
      {name:'Self-fulfillment balanced against duty', expl:'Several toys must choose between what they want and what they owe. The film rewards those who find a balance rather than those who sacrifice everything for duty. In the Toy Story universe, this is a meaningful ideological shift — the original films valorized complete self-sacrifice for the child.'},
    ],
    trad: [
      {name:'Loyalty as the highest virtue', expl:'Despite the evolving framework, loyalty remains the engine of the franchise. Toys who abandon each other are villains. Toys who sacrifice for each other are heroes. The film treats loyalty as a non-negotiable moral requirement even as it complicates who you are loyal to and why.'},
      {name:'Passing the torch across generations', expl:'The toy world is a generational story. Every toy eventually gets handed down, passed on, or retired. The film treats this as natural, beautiful, and meaningful rather than tragic. The old do not cling to relevance — they find dignity in enabling the young.'},
      {name:'Friendship as chosen family', expl:'The toys are not family in any biological sense. They are a volunteer community bound by shared experience and mutual care. The film treats this as real family, not a substitute for real family. The commitment is what makes it real — a traditional understanding of how community works.'},
      {name:'Self-sacrifice for the group', expl:'When the chips are down, the film asks its characters to put the group above themselves. This is treated as heroic and correct. The franchise might have evolved its view of duty, but it has not evolved its view that selfishness is wrong and sacrifice for others is right.'},
      {name:'Imagination and play as formative experiences', expl:'The film takes children seriously. Play is not a distraction from real life — it is how children form their understanding of the world, their moral frameworks, and their relationships. Treating childhood imagination as sacred is a traditional view that the franchise maintains with conviction.'},
      {name:'Moral clarity about right and wrong', expl:'Even as the philosophical framework has grown more complex, the film maintains a clear distinction between right and wrong behavior. Characters who lie, betray, or abandon others face consequences. Characters who are honest, loyal, and brave are rewarded. The moral architecture is conservative even when the surface details have modernized.'},
      {name:'The child comes first', expl:'For all the evolution in the franchise philosophy, this remains true: the toys exist to serve the child. Their purpose is external, not internal. When a toy forgets this, they become a cautionary tale. When they remember it at great personal cost, they become a hero.'},
    ],
  },
};

// Writes the names + explanations into reviews.json for given slug
function main() {
  const revPath = path.resolve(__dirname, '..', 'src', 'data', 'reviews.json');
  const reviews = JSON.parse(fs.readFileSync(revPath, 'utf8'));

  for (const [slug, data] of Object.entries(TROPES)) {
    const r = reviews.find(r => r && r.slug === slug);
    if (!r || !Array.isArray(r.tropeAudit)) { console.error('MISSING', slug); continue; }

    const wokeIdx = 0, tradIdx = 0; // not used this way
    let wi = 0, ti = 0;
    const wokeNames = data.woke || [];
    const tradNames = data.trad || [];

    for (const t of r.tropeAudit) {
      if (t.category === 'Woke') {
        if (wi < wokeNames.length) {
          t.name = wokeNames[wi].name;
          t.explanation = wokeNames[wi].expl;
          wi++;
        }
      } else {
        if (ti < tradNames.length) {
          t.name = tradNames[ti].name;
          t.explanation = tradNames[ti].expl;
          ti++;
        }
      }
    }

    if (wi !== wokeNames.length) console.error(`${slug}: woke mismatch — ${wi}/${wokeNames.length}`);
    if (ti !== tradNames.length) console.error(`${slug}: trad mismatch — ${ti}/${tradNames.length}`);
    console.log(`${slug}: OK (${wi}W + ${ti}T)`);
  }

  fs.writeFileSync(revPath, JSON.stringify(reviews, null, 2));
  console.log('\nWritten to reviews.json');
}

main();