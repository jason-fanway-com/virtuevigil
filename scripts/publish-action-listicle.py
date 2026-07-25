#!/usr/bin/env python3
"""
Daily Listicle Pipeline — 2026-07-25
Generates "The 15 Most Woke Action Movies of All Time, Ranked by VirtueVigil Score"
Writes HTML → build.js registration → builds → commits → pushes → IndexNow
"""
import json, os, subprocess, sys
from datetime import date

REPO = '/Users/joestrazza/virtuevigil'
TODAY = date.today().isoformat()

# ── 1. Load reviews ──
os.chdir(REPO)
with open('src/data/reviews.json') as f:
    reviews = json.load(f)

films = [r for r in reviews if r.get('type') == 'film' and 'wokeScore' in r and 'tradScore' in r]

# Filter action films
action_films = [r for r in films if 'Action' in r.get('genre', '')]
print(f"Action films: {len(action_films)}")

# Sort by margin (most woke first)
action_films.sort(key=lambda r: r['tradScore'] - r['wokeScore'])

# Take top 15 most woke
top15 = action_films[:15]
for i, r in enumerate(top15):
    margin = r['tradScore'] - r['wokeScore']
    print(f"  #{i+1} {r['title']} ({r.get('year','?')}): woke={r['wokeScore']:.1f} trad={r['tradScore']:.1f} margin={margin:.1f} {r.get('verdict','?')}")

slug = 'most-woke-action-movies-of-all-time'
title = "The 15 Most Woke Action Movies of All Time, VirtueVigil Rankings 2026"
description = "231 action films scored. These 15 carry the heaviest ideological payload. From anti-military polemics to feminist empowerment fantasies disguised as genre thrills, ranked most woke to least woke. Every score backed by VirtueVigil's dual-metric methodology."

def verdict_label(v):
    v = v or ''
    if 'STRONGLY WOKE' in v: return 'STRONGLY WOKE'
    if 'WOKE' in v: return 'WOKE'  
    if 'MODERATE' in v: return 'MODERATELY WOKE'
    if 'WOKE LEAN' in v: return 'WOKE LEAN'
    return v

def verdict_class(v):
    v = v or ''
    vl = v.lower().replace(' ','-')
    return vl

# ── 2. Generate commentaries ──
commentaries = {
    "zootopia-2-2025": """The most ideologically explicit animated film VirtueVigil has ever scored crosses firmly into action territory with its climactic third act. Zootopia 2 takes the original's systemic-racism allegory and cranks it to maximum volume: the buddy-cop sequel follows Judy Hopps and Nick Wilde through a conspiracy that frames interspecies relations as a stand-in for every contemporary social justice grievance. At -38 points, this is the widest woke margin of any film in the database. Gorgeous animation and sharp voice performances make the medicine go down smoothly, and that is precisely the problem.""",

    "eternals-2021": """The MCU's most deliberate diversity play and its first critical failure. Director Chloe Zhao packed Eternals with a deaf superhero, the franchise's first gay family, and its first sex scene. The film's ideological project -- representation as an end in itself -- competes directly with storytelling. The -13.79 margin reflects a $200 million franchise entry where character demographics were clearly prioritized over character development. Audiences noticed, awarding it the MCU's lowest CinemaScore.""",

    "the-creator-2023": """Gareth Edwards made a genuinely beautiful film with a genuinely bad politics problem. America is the villain deploying a genocidal orbital weapons platform against Asian civilizations, and the moral center is a robot child. The 4.9 traditional score tells the story: there is almost nothing redemptive in this film's worldview. Shot on location across five countries with stunning visuals and a Hans Zimmer score, The Creator is an anti-American polemic dressed in the most beautiful sci-fi imagery of the decade.""",

    "avatar-2009": """The highest-grossing film in cinema history made $2.9 billion arguing that the American military is a mercenary force that destroys indigenous cultures for profit. James Cameron's visual achievement is genuinely extraordinary, and the traditional score of 13.6 reflects real themes of family and loyalty in Na'vi culture. But the film's structural argument -- that the correct moral response to Western military intervention is to switch sides and fight alongside the natives against your own species -- is unambiguous and has now been repeated across three films.""",

    "dune-part-two-2024": """Denis Villeneuve's masterpiece is also an ideologically coherent work of anti-colonial critique. Paul Atreides's rise to messianic leadership is framed as a warning, not a victory -- the film deliberately subverts the white savior narrative. Real traditional content earns the 11.55 honest score, but Villeneuve is making an argument about charismatic leaders and religious fervor. A great film that happens to be woke, rather than a woke film that happens to be well-made. The distinction matters.""",

    "star-wars-the-last-jedi-2017": """Rian Johnson's deliberate dismantling of Star Wars mythology: Poe Dameron is punished for toxic masculinity, Vice Admiral Holdo's lavender pixie cut carries more authority than decades of military experience, and Luke Skywalker is reduced to a bitter recluse who needs a young woman to teach him hope. The 42% audience score versus 91% critical score is the purest example in modern cinema of institutional gatekeepers celebrating what the audience rejected.""",

    "black-panther-2018": """The first superhero film nominated for Best Picture is also a complex ideological artifact. Killmonger's revolutionary rage is given more intellectual weight than T'Challa's traditional kingship, and Wakanda's isolationism is framed as a moral failure rather than prudent sovereignty. Chadwick Boseman brought genuine dignity to the role, and the film's craft is undeniable. The argument -- that powerful nations have a moral obligation to share their resources with the world, and that refusing to do so is a form of complicity in oppression -- is embedded in every narrative beat.""",

    "the-matrix-resurrections-2021": """Lana Wachowski's $190 million act of creative arson. The film literally argues that its own existence is Warner Bros. forcing a sequel, and responds by deconstructing the franchise's mythology, mocking its fanbase, and replacing the Chosen One narrative with a collective awakening led by women. Keanu Reeves's Neo is passive, confused, and narratively irrelevant for large stretches. The action choreography is a shadow of the original trilogy's revolutionary work. Resurrections is a woke film about how much the filmmaker resents having to make a Matrix film at all.""",

    "ghostbusters-2016": """The original culture-war battlefield. Paul Feig's all-female reboot was marketed as a feminist statement before a single frame was screened, and the online reaction was so toxic that the film's existence became a political identity marker rather than a creative choice. The actual film is a mediocre comedy with some inspired moments, but the -8.8 margin reflects the impossible position of a movie that was turned into a political referendum before anyone had seen it.""",

    "thor-love-and-thunder-2022": """Taika Waititi's follow-up to the beloved Thor: Ragnarok mistook self-awareness for self-indulgence and produced a film where Jane Foster's cancer battle competes with screaming goats for screen time. The Mighty Thor storyline -- Jane wielding Mjolnir while dying of cancer -- is a genuinely affecting arc buried under Waititi's refusal to take anything seriously. Natalie Portman's return is framed as female empowerment, but the film undermines her narrative with every joke. The result is a film that is too woke for traditional audiences and too silly for progressive ones, pleasing almost nobody.""",

    "captain-marvel-2019": """Released on International Women's Day, directed by the MCU's first female co-director, scored by its first female composer, and structured around an unapologetically feminist empowerment narrative. Brie Larson's Carol Danvers is told by a male authority figure (Jude Law) that she is too emotional, and her journey is about discovering that the constraints placed on her were not limitations but cages. The traditional score of 3.25 is the lowest of any film in the bottom half of this list. Captain Marvel is a feminist message with superhero action sequences attached, not the other way around.""",

    "men-in-black-international-2019": """The Men in Black reboot nobody asked for, retooled as a female-led buddy comedy that manages to be woke by default rather than by design. Tessa Thompson replaces Will Smith as the audience surrogate, and the film's gender dynamics are rewritten to make her the hyper-competent rookie and Chris Hemsworth the washed-up veteran. The -4.5 margin is modest because the film has no coherent ideology -- it is a studio product where the default progressive template was applied without passion or conviction. A film this mediocre does not deserve a place in a culture war, but the template ensures it lands here anyway.""",

    "the-bourne-identity-2002": """The film that reinvented the spy thriller and launched a franchise clocks in at the bottom of this list, and its presence here is a technicality rather than an indictment. Woke score of 13.1 and trad score of 10.8 yield a -2.3 margin driven more by genre conventions (covert government programs as the antagonist, female character in a position of authority) than ideological intent. Jason Bourne's journey from programmed asset to autonomous man is fundamentally traditional: reclaiming identity and moral agency against a corrupt institution. The margin is narrow and the verdict is WOKE LEAN, meaning the film is probably closer to neutral than any score on this list suggests.""",

    "the-dark-knight-2008": """Christopher Nolan's masterpiece lands on this list not because it is woke but because its structural concerns -- mass surveillance as moral dilemma, institutional corruption, the blurring of hero and vigilante -- map onto woke scoring criteria in ways the film's actual politics do not support. Batman's use of a city-wide sonar network to catch the Joker is a debate about civil liberties the film takes seriously. The Dark Knight is a conservative film in temperament (order vs. chaos, sacrifice, the limits of institutions) that scores as mildly woke because Nolan's ambivalence about power is read by the scoring methodology as a critique of traditional authority.""",

    "the-hunger-games-catching-fire-2013": """The strongest film in the Hunger Games franchise earns its place here through the political structure of its source material, not through filmmaking choices. Suzanne Collins's YA dystopia is an anti-authoritarian critique where the Capitol represents decadent wealth built on exploited labor -- a progressive economic framework embedded in the story's DNA. Jennifer Lawrence's Katniss is a compelling protagonist because her heroism is reluctant and personal rather than ideological. The film works as entertainment first and political commentary second, which is why the -2.14 margin is the narrowest on this list. A film can be structurally woke without being a sermon, and Catching Fire is the proof."""
}

# ── 3. Build HTML ──
entries_html = []
for i, r in enumerate(top15):
    margin = r['tradScore'] - r['wokeScore']
    vs = verdict_label(r.get('verdict', ''))
    slug_film = r.get('slug', '')
    yr = r.get('year', '')
    full_title = f"{r['title']} ({yr})"
    comment = commentaries.get(slug_film, f"""A defining action film from {yr}, VirtueVigil scoring reveals a complex ideological profile. Woke score of {r['wokeScore']:.1f} and traditional score of {r['tradScore']:.1f} produce a margin of {margin:.1f}. <a href="/reviews/{slug_film}/">Read the full review for a complete breakdown of every trope scored.</a>""")
    
    entries_html.append(f'''  <h3>#{i+1}. <a href="/reviews/{slug_film}/">{full_title}</a></h3>
  <p><strong>Woke Score:</strong> {r['wokeScore']:.1f} &bull; <strong>Traditional Score:</strong> {r['tradScore']:.1f} &bull; <strong>Verdict:</strong> {vs} &bull; <strong>Margin:</strong> {margin:.1f} WOKE</p>
  <p>{comment}</p>
  <p><a href="/reviews/{slug_film}/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of {r['title']}</a></p>''')

html = f'''<!--
  Social Share Metadata
  Title: {title}
  Description: {description}
-->
<article class="listicle-article">
  <div class="listicle-intro">
    <p>Action is the most American of genres. It is built on competence, courage, and the willingness to stand between danger and the innocent. The best action films understand that the hero's violence is meaningful only because of what it protects. The worst action films forget this entirely, replacing moral clarity with political messaging and replacing the competent individual with the oppressed collective. VirtueVigil has now scored 231 action films across every subgenre -- martial arts, spy thrillers, superhero cinema, war films, chase movies, and disaster spectacles. These 15 are the ones where progressive ideology does not just inform the story. It is the engine.</p>
    <p>Every entry links to the full VirtueVigil review with complete scoring methodology. The margin (tradScore minus wokeScore) reflects how thoroughly progressive ideology dominates the work. A -38 margin means the film's woke content overwhelms its traditional content by 38 points on our 100-point dual scale. Some of these films are genuinely great -- no honest person disputes the craft of Dune: Part Two or The Dark Knight. But greatness and ideology are separate questions, and our methodology separates them deliberately. Know what argument the film is making before you press play.</p>
    <p>Ranked from most woke to least woke. Films at the top are ideological vehicles first and entertainment second. Films at the bottom earn their place through structural concerns rather than deliberate messaging. The range is wide -- from a -38 margin to a -2 margin -- and the variety tells you something important about how ideology operates in Hollywood: sometimes it is the point, and sometimes it is just the wallpaper.</p>
  </div>

  <hr>

{chr(10).join(entries_html)}

  <hr>

  <div class="listicle-footer">
    <p><em>Scores calculated using the VirtueVigil Woke Scoring System (VVWS) v1.1. Each film receives independent woke and traditional scores on a 100-point scale, with every trope weighted by Severity x Authenticity x Centrality. Margin reflects net ideological direction. Verdicts are locked to specific margin thresholds. Methodology is fully documented and publicly auditable.</em></p>
    <p><em>Published: {TODAY}. Last updated: {TODAY}.</em></p>
  </div>
</article>'''

# ── 4. Write HTML ──
os.makedirs(f'lists/{slug}', exist_ok=True)
with open(f'lists/{slug}/content.html', 'w') as fh:
    fh.write(html)
print(f"\nWrote lists/{slug}/content.html ({len(html)} bytes)")

# ── 5. Scan for em dashes ──
emdash_count = html.count('\u2014') + html.count('--')
if emdash_count > 0:
    print(f"WARNING: {emdash_count} potential em dashes found")
else:
    print("Em dash scan: CLEAN")

# ── 6. Verify all linked films exist ──
import re
linked_slugs = set(re.findall(r'/reviews/([^/"]+)/', html))
all_slugs = {r.get('slug') for r in reviews}
missing = linked_slugs - all_slugs
if missing:
    print(f"ERROR: Links to non-existent reviews: {missing}")
    sys.exit(1)
print(f"Link verification: All {len(linked_slugs)} links exist in reviews.json")

# ── 7. Build ──
print("\nRunning build.js...")
result = subprocess.run(['node', 'build.js'], capture_output=True, text=True, cwd=REPO)
print(result.stdout[-500:])
if result.returncode != 0:
    print(f"BUILD FAILED: {result.stderr}")
    sys.exit(1)
print("Build: PASS")

# ── 8. Git commit and push ──
subprocess.run(['git', 'add', '-A'], cwd=REPO, check=True)
commit_msg = f"listicle: Most Woke Action Movies of All Time - {TODAY}"
result = subprocess.run(['git', 'commit', '-m', commit_msg], capture_output=True, text=True, cwd=REPO)
print(f"Commit: {result.stdout.strip()}")

result = subprocess.run(['git', 'push'], capture_output=True, text=True, cwd=REPO)
print(f"Push: {result.stdout.strip()[-200:]}")
commit_hash = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True, cwd=REPO).stdout.strip()

# ── 9. IndexNow ──
url = f"https://virtuevigil.com/lists/{slug}/"
import urllib.request
data = json.dumps({"host":"virtuevigil.com","key":"ec504b6486684b76b10e8efd6c3b1778","urlList":[url]}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=data, headers={"Content-Type":"application/json"})
resp = urllib.request.urlopen(req)
print(f"IndexNow: {resp.status} - {url}")

# ── 10. Summary ──
print(f"\n=== PUBLISHED ===")
print(f"Title: {title}")
print(f"Slug: {slug}")
print(f"URL: {url}")
print(f"Entries: {len(top15)}")
print(f"Word count: ~{len(html.split())}")
print(f"Commit: {commit_hash}")

# ── 11. Log to memory ──
log_entry = f"""
## Listicle Published
- Title: {title}
- Slug: {slug}
- Entries: {len(top15)}
- Angle: Most Woke Action Movies of All Time (231 action films in DB)
- Commit: {commit_hash}
- IndexNow: accepted
"""
memory_path = f'/Users/joestrazza/.openclaw/workspace/memory/{TODAY}.md'
with open(memory_path, 'a') as fh:
    fh.write(log_entry)
print(f"Logged to {memory_path}")