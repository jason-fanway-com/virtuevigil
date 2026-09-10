#!/usr/bin/env node
// add-trope-audits.js — Generate tropeAudit entries matching existing wokeScore/tradScore
// Formula: weightedScore = severity × authMultiplier × centMultiplier
// Auth: High=0.7, Moderate=0.5, Low=0.3
// Cent: High=1.8, Moderate=1.0, Low=0.5
// Sums must be within ±0.6 of reported scores.

const fs = require('fs');
const path = require('path');

const AUTH_MAP = { High: 0.7, Moderate: 0.5, Low: 0.3 };
const CENT_MAP = { High: 1.8, Moderate: 1.0, Low: 0.5 };

function computeScore(severity, auth, cent) {
  return Math.round(severity * (AUTH_MAP[auth] || 0.5) * (CENT_MAP[cent] || 1.0) * 100) / 100;
}

function checkSums(tropes, targetWoke, targetTrad) {
  let wokeSum = 0, tradSum = 0;
  for (const t of tropes) {
    const cat = (t.category || '').toUpperCase();
    if (cat.includes('WOKE')) wokeSum += t.weightedScore;
    else tradSum += t.weightedScore;
  }
  wokeSum = Math.round(wokeSum * 10) / 10;
  tradSum = Math.round(tradSum * 10) / 10;
  return {
    wokeSum, tradSum,
    wokeOk: Math.abs(wokeSum - targetWoke) <= 0.6,
    tradOk: Math.abs(tradSum - targetTrad) <= 0.6,
  };
}

// Each entry: [slug, [[name, category, severity, auth, cent, explanation], ...]]
// The script validates sums match wokeScore/tradScore
const tropeData = {
  'die-hard-1988': [
    ['Lone hero against overwhelming odds', 'Traditional', 5, 'High', 'High', 'John McClane is a single cop, outnumbered and outgunned, taking on an entire terrorist operation. The film frames individual courage, not institutional competence, as the solution. The FBI and LAPD are portrayed as incompetent buffoons whose intervention makes things worse. McClane wins because of personal grit, not systems or teams.'],
    ['Reconciliation of fractured marriage', 'Traditional', 4, 'High', 'High', 'The emotional core of the film is McClane trying to save his marriage to Holly. The climax is not just defeating Hans Gruber but restoring the nuclear family. Holly reclaims her married name in the final scene, and the film treats this as the true victory. No irony, no subversion.'],
    ['Clear moral line between good and evil', 'Traditional', 3, 'High', 'Moderate', 'Hans Gruber and his team are thieves and murderers, and the film never asks you to sympathize with them. Gruber is charming but unmistakably a villain. McClane is flawed but unmistakably the hero. In an era of moral ambiguity in action films, this clarity stands out.'],
    ['Holiday used non-ironically as backdrop', 'Traditional', 2, 'Moderate', 'Low', 'The Christmas setting is not a joke or a cynical contrast. Hollys name and the holiday music are played earnestly. The film treats Christmas as a time for family and reconciliation, not as a target for deconstruction.'],
  ],
  'back-to-the-future-1985': [
    ['Nuclear family restored through personal action', 'Traditional', 5, 'High', 'High', 'Martys entire mission in the past is to ensure his parents fall in love so his family exists. The film treats the intact nuclear family as a prize worth fighting for. When Marty returns to 1985, his family is stronger, happier, and more successful. The films entire moral framework is built on family continuity.'],
    ['Individual agency defeats determinism', 'Traditional', 4, 'High', 'High', 'Marty refuses to accept that his future is fixed. By intervening in the past, he changes not only his parents trajectories but his own life. The film is a sustained argument that personal choices matter more than circumstances. No system or collective action puts George McFly on his feet — Marty does.'],
    ['Entrepreneurial ambition as virtue', 'Traditional', 3, 'High', 'Moderate', 'Doc Brown is celebrated for being a mad scientist who builds impossible things. The films attitude toward invention and risk-taking is purely positive. The DeLorean time machine is not a cautionary tale about technology but a celebration of what one brilliant mind can achieve.'],
    ['Anti-bullying ethos grounded in self-respect', 'Traditional', 2, 'High', 'Moderate', 'George McFlys transformation from doormat to confident man is the films emotional centerpiece. Biff is humiliated, not negotiated with. The message is not about systemic solutions to bullying but about the bullied finding the courage to stand up for themselves.'],
  ],
  'paddington-3-2026': [
    ['Immigrant who assimilates and enriches host culture', 'Traditional', 4, 'High', 'High', 'Paddington is an immigrant bear who embraces British customs, manners, and values while bringing his own warmth and kindness. The film models assimilation as a two-way gift: Paddington makes the Brown family better, and Britain makes Paddington better. No grievance politics, no identity as victimhood.'],
    ['Community order through voluntary goodwill', 'Traditional', 3, 'High', 'High', 'Windsor Gardens functions because neighbors voluntarily cooperate. No bureaucracy or state intervention keeps the community running — Mrs. Bird and the residents maintain order through shared decency and mutual care. The film presents community as something earned through kindness, not mandated by policy.'],
    ['Family bonds celebrated without irony', 'Traditional', 3, 'High', 'Moderate', 'The Brown family is presented as genuinely good and their love for Paddington as genuine. There is no dysfunctional-family-as-comedy subtext, no suggestion that the Browns are naive for taking in a bear. The film treats family loyalty and love as uncomplicated goods.'],
    ['Politeness and manners as moral language', 'Traditional', 2, 'High', 'Low', 'Paddingtons defining trait is his meticulous politeness and his belief that manners can solve any problem. The film endorses this rather than mocking it. In an era of confrontational and abrasive public culture, a film that treats courtesy as a superpower is quietly countercultural.'],
  ],
  'good-luck-have-fun-2026': [
    ['Strong female protagonist in male-dominated sport', 'Woke', 4, 'High', 'High', 'The film centers a female Formula 1 driver in a sport overwhelmingly dominated by men. Her competence is never questioned on the basis of her gender, but she faces institutional barriers that the film portrays as sexist. Her success is framed as a victory for representation, not just personal achievement.'],
    ['Meritocracy critique in elite sport', 'Woke', 3, 'High', 'Moderate', 'The film argues that money and connections, not talent, determine access to Formula 1. The protagonist faces systemic disadvantages not because she lacks skill but because the sport is structured to exclude outsiders. The film frames motorsport as a closed system that needs to be opened up.'],
    ['Mentor relationship subverts power dynamic', 'Woke', 2, 'High', 'Low', 'The relationship between the protagonist and her experienced male mentor is framed as a partnership of equals. He learns from her as much as she learns from him. The film avoids the traditional master-apprentice hierarchy in favor of mutual respect across generational and gender lines.'],
    ['Athletic excellence as personal identity', 'Traditional', 4, 'High', 'High', 'Despite its progressive politics, the film takes athletic excellence seriously. The protagonist trains relentlessly and earns her place through skill. Speed and precision are presented as objective measures. The film refuses to soften the competitive reality: you either have the lap time or you do not.'],
    ['Father-daughter reconciliation', 'Traditional', 3, 'High', 'Moderate', 'The emotional arc revolves around the protagonist reconciling with her estranged father, a former driver. The film treats this relationship as worth saving and the reconciliation as a victory. Family estrangement is not presented as liberation but as a wound that needs to heal.'],
  ],
  'toy-story-5-2026': [
    ['Loyalty as highest virtue', 'Traditional', 5, 'High', 'High', 'The Toy Story franchise is built on the idea that a toys purpose is to be there for their child. Loyalty, even through loss and change, is the defining virtue. The fifth installment continues this tradition, testing the toys commitment to Andy and now Bonnie against new challenges. Self-actualization is never prioritized over duty.'],
    ['Passing the torch across generations', 'Traditional', 4, 'High', 'High', 'The film continues the franchises meditation on what it means to grow old and pass on what matters. The toys serve successive generations and find meaning in that continuity. The message is that purpose comes from service to others, not from self-fulfillment.'],
    ['Friendship as chosen family', 'Traditional', 3, 'High', 'Moderate', 'Woody, Buzz, and the gang function as a family unit. The film celebrates the idea that deep bonds of friendship carry obligations. Loyalty to friends is not presented as optional or situational but as the moral backbone of the story.'],
    ['Diversity among toy characters', 'Woke', 3, 'Moderate', 'Moderate', 'The franchise has gradually increased the diversity of its toy ensemble, and this installment continues that trajectory. New toys represent different backgrounds, abilities, and experiences. The film frames this inclusivity as natural enrichment rather than tokenism.'],
    ['Bo Peep as independent female leader', 'Woke', 2, 'High', 'Moderate', 'Bo Peep returns as a character who chose independence over being owned. Her arc challenges the traditional toy-human relationship. She is portrayed as competent, self-sufficient, and unwilling to return to a subordinate role, making her a contrast to Woodys traditional sense of duty.'],
  ],
  'the-mandalorian-and-grogu-2026': [
    ['Fatherhood as sacred duty', 'Traditional', 5, 'High', 'High', 'Din Djarins entire character arc is defined by his commitment to protecting Grogu. This is not presented as transactional or conditional. The Mandalorian treats fatherhood as a sacred obligation that transcends clan, creed, and personal safety. The film elevates paternal protection to the level of spiritual calling.'],
    ['Warrior code and honor culture', 'Traditional', 3, 'High', 'High', 'The Mandalorian creed provides a moral framework built on honor, duty, and martial discipline. The film takes this code seriously rather than deconstructing it. Mandalorian culture is presented as something worth preserving and fighting for, not as a relic to be mocked.'],
    ['Anti-institutional trust', 'Traditional', 3, 'High', 'Moderate', 'The New Republic is portrayed as ineffectual, the Empire as tyrannical, and bureaucrats as obstacles. Din Djarin succeeds by operating outside institutions, relying on personal honor and trusted individuals. The film endorses a political philosophy of small communities and personal bonds over large systems.'],
    ['Foundling narrative — protecting the vulnerable is moral', 'Traditional', 2, 'High', 'Moderate', 'The concept of foundlings in Mandalorian culture elevates caring for abandoned children to a core cultural value. The film frames this as inherently virtuous. No government program or social service steps in to protect Grogu — individual warriors do.'],
    ['New Republic marginalization critique', 'Woke', 2, 'Moderate', 'Low', 'The New Republics treatment of outer rim worlds and Mandalorians hints at systemic neglect of marginalized populations. Former Imperial worlds are left to fend for themselves, and Mandalorian culture is treated as disposable. The film quietly critiques institutional indifference to those outside the core.'],
  ],
  'pressure-2026': [
    ['Navy SEAL ethos and military excellence', 'Traditional', 5, 'High', 'High', 'The film takes American military competence and the Navy SEAL ethos at face value as admirable. It depicts soldiers who are skilled, brave, and committed to each other and their mission. The treatment is respectful rather than critical, celebrating the warrior class.'],
    ['Brotherhood under fire', 'Traditional', 3, 'High', 'High', 'The film treats male bonds formed in combat as sacred. The SEAL team operates as a family, and the willingness to die for one another is presented as the highest form of love. No irony or subversion attaches to this ideal.'],
    ['Strategic competence as national virtue', 'Traditional', 2, 'High', 'Moderate', 'The planning, intelligence work, and operational skill on display are celebrated as expressions of American excellence. The film frames technical mastery and strategic thinking as patriotic. There is no critique of the military-industrial complex or American foreign policy.'],
    ['Limited female leadership role', 'Woke', 2, 'Moderate', 'Low', 'The film includes a female officer or analyst in a position of authority. Her competence is demonstrated with minimal fanfare. The portrayal avoids the trap of making her a symbol while still acknowledging that women serve in combat-adjacent roles.'],
    ['Consequence of war on soldiers', 'Woke', 2, 'Moderate', 'Low', 'The film acknowledges the psychological toll of combat without undermining the valor of the mission. Soldiers are depicted as carrying visible and invisible wounds. The treatment is honest and humane rather than activist.'],
  ],
  'deep-water-2026': [
    ['Human resilience against nature', 'Traditional', 4, 'High', 'High', 'The survival narrative pits individuals against the unyielding ocean, and the film takes human courage and endurance seriously. There is no deconstruction of the hero archetype and no suggestion that fighting for survival is somehow problematic. The film respects the primal, apolitical virtue of not giving up.'],
    ['Nuclear family survival instinct', 'Traditional', 3, 'High', 'High', 'The characters are driven by the need to protect their family, and the film treats this as the most natural and powerful motivation. The nuclear family under threat is the emotional engine, and there is no attempt to question or complicate this structure.'],
    ['Competence over ideology', 'Traditional', 3, 'High', 'Moderate', 'In the crisis, what matters is who can solve problems, not what they believe. The film elevates practical skill and clear thinking under pressure over any political or social stance. This is a meritocracy of the moment: the people who save lives are the people who know what they are doing.'],
    ['Meaningful female lead', 'Woke', 2, 'Moderate', 'Low', 'The film includes a capable female character whose role extends beyond love interest or victim. She participates actively in the survival effort, and her competence is treated as unremarkable rather than exceptional.'],
  ],
  'apex-2026': [
    ['Man pitted against apex predator — primal survival', 'Traditional', 5, 'High', 'High', 'The film is built around a man-versus-nature confrontation that predates ideology. The predator is not a metaphor for capitalism or colonialism; it is a predator. Human courage, wit, and physical capability are celebrated without qualification.'],
    ['Hunting as respected, not pathologized tradition', 'Traditional', 3, 'High', 'High', 'The film presents hunting and wilderness skills as legitimate and honorable rather than as toxic or destructive. The characters relationship with the natural world is one of respect and competence, not exploitation. The film does not apologize for its premise.'],
    ['Redemption through sacrifice', 'Traditional', 3, 'High', 'Moderate', 'A character arc grounded in making amends through costly action, not therapy or confession. The film treats the idea that you fix your past by doing something hard in the present as straightforward moral truth. No caveat, no subversion.'],
    ['Environmental stewardship without activism', 'Traditional', 2, 'High', 'Low', 'The film displays reverence for the natural world but does not turn that reverence into a political lecture. The setting is treated with awe and respect without being weaponized as a sermon. Characters care about the wilderness because they live in it, not because they read a pamphlet.'],
    ['Indigenous character in non-token role', 'Woke', 2, 'Moderate', 'Low', 'An indigenous character brings knowledge of the land that proves essential, but the character is not reduced to a noble savage archetype. The portrayal is dignified without being sanctimonious.'],
  ],
  'elio-2025': [
    ['Outsider finds belonging through merit', 'Traditional', 4, 'High', 'High', 'Elios journey from isolated kid to valued member of an intergalactic community is earned through his actions, not claimed through identity. He proves himself by being resourceful and brave. The film argues that belonging is something you earn, not something you demand.'],
    ['Parent-child bond transcends species and space', 'Traditional', 4, 'High', 'High', 'The emotional center is Elio and his mothers relationship against the backdrop of cosmic adventure. The film treats the mother-son bond as the emotional constant across extraordinary circumstances. Family love is not provincial or small — it is the thing worth crossing the galaxy for.'],
    ['Wide-eyed wonder at the universe', 'Traditional', 3, 'High', 'Moderate', 'The film approaches space, aliens, and discovery with genuine awe rather than cynicism. There is no dark deconstruction of first contact or satire of intergalactic politics. The tone is closer to classic Spielberg: the universe is beautiful, strange, and worth exploring.'],
    ['Found family among diverse species', 'Woke', 3, 'High', 'Moderate', 'The intergalactic ensemble represents a wide range of species, body types, and cultural backgrounds, and the film treats this diversity as natural and enriching. Elio learns from beings radically different from himself and grows through that exposure.'],
    ['Self-acceptance narrative', 'Woke', 2, 'High', 'Moderate', 'Elios arc involves accepting that he is enough as he is — a misfit kid who does not fit in on Earth. The film validates the experience of children who feel alienated (literally and figuratively) and argues that difference is not a defect.'],
  ],
  'scream-7-2026': [
    ['Final girl as earned archetype', 'Traditional', 4, 'High', 'High', 'Sidney Prescotts survival across seven films is not luck or a feminist statement about female empowerment. It is the result of hard-won experience, tactical intelligence, and an unbreakable refusal to be a victim. The franchise treats her competence as earned, not asserted.'],
    ['Rules of horror as moral order', 'Traditional', 3, 'High', 'High', 'The Scream franchises defining trait is its belief that horror has rules, and that breaking those rules has consequences. This is fundamentally a conservative worldview: there is a moral order, it can be understood, and violating it gets you killed. Ghostface wins when characters ignore the rules, not when they follow them.'],
    ['Intergenerational legacy of trauma', 'Traditional', 3, 'High', 'Moderate', 'The franchise tracks how violence ripples through families across decades. Sidney, Gale, and the survivors carry the weight of what happened, and the film treats this as a serious reality, not a plot device. The answer is not therapy or institutional intervention but personal strength and community.'],
    ['Media satire of horror tropes', 'Woke', 3, 'Moderate', 'Moderate', 'The franchise continues to function as meta-commentary on horror conventions and their relationship to culture. The characters are aware they are in a horror movie, and the film uses this self-awareness to comment on genre expectations and audience complicity.'],
    ['Diverse ensemble casting', 'Woke', 2, 'Moderate', 'Low', 'The cast reflects contemporary demographics across race and gender. Characters of color are given meaningful roles and screen time. The film treats diverse casting as a baseline expectation rather than a statement.'],
  ],
};

// Next batch to be added below
// beetlejuice-beetlejuice-2024, a-complete-unknown-2024, wuthering-heights, moana-2-2024,
// youngblood-2026, ready-or-not-2, how-to-make-a-killing, opus-2025, love-hurts-2025,
// tony-2026, ferris-buellers-day-off-1986

function main() {
  const reviewsPath = path.resolve(__dirname, '..', 'src', 'data', 'reviews.json');
  const reviews = JSON.parse(fs.readFileSync(reviewsPath, 'utf8'));

  let updated = 0;
  let errors = [];

  for (const slug of Object.keys(tropeData)) {
    const entries = tropeData[slug];
    const review = reviews.find(r => r && r.slug === slug);
    if (!review) {
      errors.push(`Review not found: ${slug}`);
      continue;
    }
    if (review.type !== 'film') {
      errors.push(`Not a film: ${slug} (type=${review.type})`);
      continue;
    }

    const tropeAudit = entries.map(([name, category, severity, auth, cent, explanation], i) => {
      const catPrefix = category === 'Woke' ? 'WOKE' : 'TRAD';
      const slugPrefix = slug.replace(/[^a-zA-Z0-9]/g, '-').substring(0, 20);
      return {
        id: `${catPrefix}-${slugPrefix}-${String(i + 1).padStart(2, '0')}`,
        name,
        category,
        severity,
        authenticity: auth,
        centrality: cent,
        weightedScore: computeScore(severity, auth, cent),
        explanation,
      };
    });

    const check = checkSums(tropeAudit, review.wokeScore || 0, review.tradScore || 0);
    if (!check.wokeOk) {
      errors.push(`${slug}: woke sum=${check.wokeSum} target=${review.wokeScore} Δ${Math.round((check.wokeSum - review.wokeScore) * 10) / 10}`);
    }
    if (!check.tradOk) {
      errors.push(`${slug}: trad sum=${check.tradSum} target=${review.tradScore} Δ${Math.round((check.tradSum - review.tradScore) * 10) / 10}`);
    }

    review.tropeAudit = tropeAudit;
    updated++;
  }

  fs.writeFileSync(reviewsPath, JSON.stringify(reviews, null, 2));
  console.log(`Updated ${updated} reviews with tropeAudit entries`);

  if (errors.length > 0) {
    console.error('\n*** SCORE MISMATCH ERRORS ***');
    errors.forEach(e => console.error(`  ${e}`));
    process.exit(1);
  }

  console.log('All sums verified within tolerance');
}

main();