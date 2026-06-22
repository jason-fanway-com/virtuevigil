#!/usr/bin/env node
/**
 * seo-optimize-targets.js
 * Data-driven on-page SEO optimization for GSC priority review targets.
 *
 * Sets r.seo.titleTag, r.seo.metaDescription (the fields build.js actually reads),
 * and r.dateModified (freshness signal -> sitemap lastmod + schema dateModified +
 * visible "Updated" line) on the targeted review records in src/data/reviews.json.
 *
 * Title format: exact-match the high-intent "is [title] woke" query.
 * Meta: <=155 chars, answer + hook, NO EM DASHES, no clickbait.
 *
 * Repeatable: add entries to TARGETS and re-run. Idempotent (only the listed
 * fields are overwritten). Prints a before/after diff for each target.
 *
 * Usage: node scripts/seo-optimize-targets.js [--dry]
 */
const fs = require('fs');
const path = require('path');

const DRY = process.argv.includes('--dry');
const DATA = path.join(__dirname, '..', 'src', 'data', 'reviews.json');
const TODAY = '2026-06-22';

// Hard guard: reject em dashes in any value we write.
function assertNoEmDash(s, label) {
  if (typeof s === 'string' && /[\u2014\u2013]/.test(s)) {
    throw new Error(`EM DASH detected in ${label}: ${s}`);
  }
  return s;
}

// slug -> optimized SEO. Titles exact-match the ranking query.
const TARGETS = {
  'devil-wears-prada-2-2026': {
    titleTag: 'Is The Devil Wears Prada 2 Woke? | VirtueVigil Review',
    metaDescription: "Is The Devil Wears Prada 2 woke? VirtueVigil scores the 2026 sequel MIXED. Streep, Hathaway and Blunt return. See the full VVWS breakdown before you watch.",
  },
  'goat-2026': {
    titleTag: 'Is GOAT (2026) Woke? | VirtueVigil Review',
    metaDescription: "Is GOAT woke? VirtueVigil rates Sony's 2026 animated sports comedy TRADITIONAL LEAN (+9). Real teamwork and grit, light woke notes. Full score inside.",
  },
  'disclosure-day-2026': {
    titleTag: 'Is Disclosure Day Woke? | VirtueVigil Review',
    metaDescription: "Is Disclosure Day woke? VirtueVigil reviews Spielberg's 2026 UFO thriller with Emily Blunt. Full VVWS score, trope audit, and parental guidance inside.",
  },
  'toy-story-4-2019': {
    titleTag: 'Is Toy Story 4 Woke? | VirtueVigil Review',
    metaDescription: "Is Toy Story 4 woke? VirtueVigil scores it WOKE (-9). Woody abandons his purpose for self-fulfillment. See why and what parents should know before watching.",
  },
  'daredevil-born-again-s2-2026': {
    titleTag: 'Is Daredevil Born Again Season 2 Woke? | VirtueVigil Review',
    metaDescription: "Is Daredevil Born Again Season 2 woke? VirtueVigil verdict: WOKE (-12). Marvel's most political show uses Kingpin as a Trump stand-in. Full guide.",
  },
  'super-mario-galaxy-movie-2026': {
    titleTag: 'Is The Super Mario Galaxy Movie Woke? | VirtueVigil Review',
    metaDescription: "Is The Super Mario Galaxy Movie woke? VirtueVigil rates it TRADITIONAL LEAN (+10). Critics hate it, families love it. Bowser arc and our full verdict.",
  },
  'paradise-s2': {
    titleTag: 'Is Paradise Season 2 Woke? | VirtueVigil Review',
    metaDescription: "Is Paradise Season 2 woke? VirtueVigil rates the Hulu thriller TRADITIONAL LEAN (+6). Dan Fogelman's twisty bunker drama scored. Full VVWS analysis inside.",
  },
  'obsession-2026': {
    titleTag: 'Is Obsession (2026) Woke? | VirtueVigil Review',
    metaDescription: "Is Obsession woke? VirtueVigil rates Curry Barker's 2026 horror film TRADITIONAL LEAN (+7). Full trope audit, VVWS score, and parent guide inside.",
  },
  'project-hail-mary': {
    titleTag: 'Is Project Hail Mary Woke? | VirtueVigil Review',
    metaDescription: "Is Project Hail Mary woke? VirtueVigil scores it STRONGLY TRADITIONAL (+21). Ryan Gosling's optimistic sci-fi of sacrifice and friendship. Full breakdown.",
  },
  'gladiator-2-2024': {
    titleTag: 'Is Gladiator II Woke? | VirtueVigil Review',
    metaDescription: "Is Gladiator II woke? VirtueVigil rates the 2024 epic TRADITIONAL LEAN (+7). Paul Mescal's honor arc and Denzel's brilliance scored. Full VVWS analysis.",
  },
};

const data = JSON.parse(fs.readFileSync(DATA, 'utf8'));
const bySlug = new Map(data.map(r => [r.slug, r]));

let changed = 0;
const missing = [];
for (const [slug, seo] of Object.entries(TARGETS)) {
  const r = bySlug.get(slug);
  if (!r) { missing.push(slug); continue; }
  assertNoEmDash(seo.titleTag, slug + '.titleTag');
  assertNoEmDash(seo.metaDescription, slug + '.metaDescription');
  if (seo.metaDescription.length > 160) {
    console.warn(`WARN ${slug}: meta length ${seo.metaDescription.length} > 160`);
  }
  const before = {
    titleTag: (r.seo && r.seo.titleTag) || '(fallback) Is ' + r.title + ' Woke? | VirtueVigil',
    metaDescription: (r.seo && r.seo.metaDescription) || '(fallback generic)',
    dateModified: r.dateModified || '(none)',
  };
  r.seo = r.seo || {};
  r.seo.titleTag = seo.titleTag;
  r.seo.metaDescription = seo.metaDescription;
  r.dateModified = TODAY;
  changed++;
  console.log(`\n=== ${slug} (len meta=${seo.metaDescription.length}) ===`);
  console.log('  BEFORE title:', before.titleTag);
  console.log('  AFTER  title:', r.seo.titleTag);
  console.log('  BEFORE meta :', before.metaDescription);
  console.log('  AFTER  meta :', r.seo.metaDescription);
  console.log('  dateModified:', before.dateModified, '->', r.dateModified);
}

if (missing.length) console.log('\nMISSING SLUGS (not found):', missing.join(', '));
console.log(`\n${changed} records updated.${DRY ? ' (DRY RUN, not written)' : ''}`);

if (!DRY && changed) {
  fs.writeFileSync(DATA, JSON.stringify(data, null, 2));
  console.log('Wrote', DATA);
}
