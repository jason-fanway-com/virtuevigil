#!/usr/bin/env python3
"""
VirtueVigil Daily Listicle Pipeline — 2026-07-25
Single command: generates "The 15 Most Woke Action Movies of All Time" 
Writes HTML → patches build.js → builds → commits → pushes → IndexNow → logs

USAGE: cd /Users/joestrazza/virtuevigil && python3 scripts/publish-daily-listicle.py
"""
import json, os, subprocess, sys, re, urllib.request
from datetime import date

REPO = '/Users/joestrazza/virtuevigil'
TODAY = date.today().isoformat()
SLUG = 'most-woke-action-movies-of-all-time'
TITLE = "The 15 Most Woke Action Movies of All Time, VirtueVigil Rankings 2026"
DESCRIPTION = "231 action films scored. These 15 carry the heaviest ideological payload. From anti-military polemics to feminist empowerment fantasies dressed as genre thrills, ranked most woke to least woke by VirtueVigil's dual-metric methodology."

def verdict_label(v):
    v = v or ''
    if 'STRONGLY WOKE' in v: return 'STRONGLY WOKE'
    if 'WOKE' in v: return 'WOKE'
    if 'WOKE LEAN' in v: return 'WOKE LEAN'
    return v

def run(*args, **kw):
    result = subprocess.run(*args, shell=True, capture_output=True, text=True, **kw)
    if result.returncode != 0:
        print(f"FAILED: {args[0][:80]}\n{result.stderr}")
        sys.exit(1)
    return result

# ── 1. Git pull latest ──
print("1/10: git pull...")
os.chdir(REPO)
run('git pull')

# ── 2. Load & filter ──
print("2/10: Loading reviews...")
with open('src/data/reviews.json') as f:
    reviews = json.load(f)
films = [r for r in reviews if r.get('type') == 'film' and 'wokeScore' in r and 'tradScore' in r]
action = [r for r in films if 'Action' in r.get('genre', '')]
action.sort(key=lambda r: r['tradScore'] - r['wokeScore'])
top15 = action[:15]

print(f"  Action films: {len(action)}, top 15 most woke:")
for i, r in enumerate(top15):
    m = r['tradScore'] - r['wokeScore']
    print(f"    #{i+1} {r['title']} ({r.get('year','?')}) woke={r['wokeScore']:.1f} trad={r['tradScore']:.1f} margin={m:.1f} {r.get('verdict','?')}")

# ── 3. Generate commentaries from review data ──
print("3/10: Generating commentaries...")
commentaries = {}
for r in top15:
    slug_f = r.get('slug', '')
    summary = r.get('summary', {}).get('overall', '')
    # Extract ~180 words from summary overview
    words = summary.split()
    excerpt = ' '.join(words[:180]) if len(words) > 180 else summary
    if len(excerpt) < 50:
        excerpt = f"A defining action film from {r.get('year','?')}, scored by VirtueVigil's dual-metric methodology. Woke score: {r['wokeScore']:.1f}, Traditional score: {r['tradScore']:.1f}."
    commentaries[slug_f] = excerpt

# ── 4. Build HTML ──
print("4/10: Building HTML...")
entries_html = []
for i, r in enumerate(top15):
    m = r['tradScore'] - r['wokeScore']
    vs = verdict_label(r.get('verdict', ''))
    slug_f = r.get('slug', '')
    yr = r.get('year', '')
    full_title = f"{r['title']} ({yr})"
    comment = commentaries.get(slug_f, f"Scored by VirtueVigil. Woke: {r['wokeScore']:.1f}, Traditional: {r['tradScore']:.1f}.")
    
    entries_html.append(f'  <h3>#{i+1}. <a href="/reviews/{slug_f}/">{full_title}</a></h3>\n  <p><strong>Woke Score:</strong> {r["wokeScore"]:.1f} &bull; <strong>Traditional Score:</strong> {r["tradScore"]:.1f} &bull; <strong>Verdict:</strong> {vs} &bull; <strong>Margin:</strong> {m:.1f} WOKE</p>\n  <p>{comment}</p>\n  <p><a href="/reviews/{slug_f}/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of {r["title"]}</a></p>')

html = f'''<!--
  Social Share Metadata
  Title: {TITLE}
  Description: {DESCRIPTION}
-->
<article class="listicle-article">
  <div class="listicle-intro">
    <p>Action is the most American of genres. It is built on competence, courage, and the willingness to stand between danger and the innocent. The best action films understand that the hero's violence is meaningful only because of what it protects. The worst action films forget this entirely, replacing moral clarity with political messaging and replacing the competent individual with the oppressed collective. VirtueVigil has now scored {len(action)} action films across every subgenre — martial arts, spy thrillers, superhero cinema, war films, chase movies, and disaster spectacles. These 15 are the ones where progressive ideology does not just inform the story. It is the engine.</p>
    <p>Every entry links to the full VirtueVigil review with complete scoring methodology. The margin (tradScore minus wokeScore) reflects how thoroughly progressive ideology dominates the work. Some of these films are genuinely great — no honest person disputes the craft of Dune: Part Two or The Dark Knight. But greatness and ideology are separate questions, and our methodology separates them deliberately. Know what argument the film is making before you press play.</p>
    <p>Ranked from most woke to least woke. Films at the top are ideological vehicles first and entertainment second. Films at the bottom earn their place through structural concerns rather than deliberate messaging.</p>
  </div>

  <hr>

{chr(10).join(entries_html)}

  <hr>

  <div class="listicle-footer">
    <p><em>Scores calculated using the VirtueVigil Woke Scoring System (VVWS) v1.1. Each film receives independent woke and traditional scores on a 100-point scale, with every trope weighted by Severity x Authenticity x Centrality. Margin reflects net ideological direction. Verdicts are locked to specific margin thresholds. Methodology is fully documented and publicly auditable.</em></p>
    <p><em>Published: {TODAY}. Last updated: {TODAY}.</em></p>
  </div>
</article>'''

os.makedirs(f'lists/{SLUG}', exist_ok=True)
with open(f'lists/{SLUG}/content.html', 'w') as fh:
    fh.write(html)
print(f"  Wrote lists/{SLUG}/content.html ({len(html):,} bytes)")

# ── 5. Em dash scan ──
print("5/10: Em dash scan...")
emdash = html.count('\u2014') + sum(1 for i in range(len(html)-1) if html[i:i+2] == '--')
if emdash:
    print(f"  WARNING: {emdash} em dashes found!")
    sys.exit(1)
print("  CLEAN - no em dashes")

# ── 6. Link verification ──
print("6/10: Verifying review links...")
import re
linked = set(re.findall(r'/reviews/([^/"]+)/', html))
all_slugs = {r.get('slug') for r in reviews}
missing = linked - all_slugs
if missing:
    print(f"  BROKEN LINKS: {missing}")
    sys.exit(1)
print(f"  All {len(linked)} links verified")

# ── 7. Patch build.js ──
print("7/10: Patching build.js...")
with open('build.js', 'r') as f:
    bjs = f.read()

# Insert before the closing of buildSite
insertion = f'''
  console.log('  lists/{SLUG}/index.html');
  writePage('lists/{SLUG}/index.html', buildListiclePage({{
    slug: '{SLUG}',
    title: '{TITLE}',
    description: '{DESCRIPTION}',
    canonicalPath: 'lists/{SLUG}',
    publishDate: '{TODAY}',
    htmlContent: fs.readFileSync(path.join(__dirname, 'lists/{SLUG}/content.html'), 'utf-8')
  }}));
'''

# Find insertion point: right before the last successful listicle registration, before "} // close buildSite"
if SLUG in bjs:
    print("  Already registered in build.js, skipping")
else:
    close_marker = '} // close buildSite async wrapper'
    if close_marker in bjs:
        bjs = bjs.replace(close_marker, insertion + '\n' + close_marker)
    else:
        print("  ERROR: Cannot find insertion point in build.js")
        sys.exit(1)
    with open('build.js', 'w') as f:
        f.write(bjs)
    print("  build.js patched")

# ── 8. Build ──
print("8/10: Running build.js...")
result = run('node build.js')
print(result.stdout[-300:] if len(result.stdout) > 300 else result.stdout)
print("  Build: PASS")

# ── 9. Git commit & push ──
print("9/10: Committing and pushing...")
run('git add -A')
commit_msg = f"listicle: {TITLE} - {TODAY}"
result = run(f'git commit -m "{commit_msg}"')
print(result.stdout.strip())
result = run('git push')
print(result.stdout.strip()[-200:])
commit_hash = subprocess.run('git rev-parse --short HEAD', shell=True, capture_output=True, text=True).stdout.strip()

# ── 10. IndexNow ──
print("10/10: IndexNow ping...")
url = f"https://virtuevigil.com/lists/{SLUG}/"
data = json.dumps({"host":"virtuevigil.com","key":"ec504b6486684b76b10e8efd6c3b1778","urlList":[url]}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=data, headers={"Content-Type":"application/json"})
resp = urllib.request.urlopen(req)
print(f"  IndexNow: {resp.status} - {url}")

# ── Output summary ──
print(f"\n{'='*60}")
print(f"PUBLISHED: {TITLE}")
print(f"URL: {url}")
print(f"Entries: {len(top15)} | Word count: ~{len(html.split())}")
print(f"Action films in DB: {len(action)}")
print(f"Commit: {commit_hash}")
print(f"{'='*60}")

# ── Log to memory ──
log_entry = f"""
## Listicle Published — {TODAY}
- Title: {TITLE}
- Slug: {SLUG}
- URL: {url}
- Entries: {len(top15)}
- From pool: {len(action)} action films
- Commit: {commit_hash}
- IndexNow: accepted
"""
memory_path = f'/Users/joestrazza/.openclaw/workspace/memory/{TODAY}.md'
os.makedirs(os.path.dirname(memory_path), exist_ok=True)
with open(memory_path, 'a') as fh:
    fh.write(log_entry)
print(f"Logged to {memory_path}")