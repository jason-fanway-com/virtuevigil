#!/usr/bin/env python3
"""One-shot analysis to find the best listicle angle for today."""
import json

with open('src/data/reviews.json') as f:
    reviews = json.load(f)

# Filter: only film type, with valid scores
films = [r for r in reviews if r.get('type') == 'film' and 'wokeScore' in r and 'tradScore' in r]
print(f"Total films: {len(films)}")

# Parse genres
from collections import Counter, defaultdict
genres = Counter()
year_films = defaultdict(list)
genre_films = defaultdict(list)
platform_films = defaultdict(list)
franchise_films = defaultdict(list)

for r in films:
    genre_str = r.get('genre', '')
    if genre_str:
        for g in [x.strip() for x in genre_str.split('/')]:
            genres[g] += 1
            genre_films[g].append(r)
    if 'year' in r:
        year_films[r['year']].append(r)
    if 'platform' in r and r['platform']:
        platform_films[r['platform']].append(r)
    if 'franchise' in r and r['franchise'] and r['franchise'].strip():
        franchise_films[r['franchise']].append(r)

print("\n=== TOP GENRES (20+ films) ===")
for genre, count in sorted(genres.items(), key=lambda x: -x[1]):
    if count >= 20:
        # Show margin range
        margins = [r['tradScore'] - r['wokeScore'] for r in genre_films[genre] if r.get('tradScore') is not None and r.get('wokeScore') is not None]
        if margins:
            print(f"  {genre}: {count} films, margin range {min(margins):.1f} to {max(margins):.1f}, avg {sum(margins)/len(margins):.1f}")

print("\n=== TOP YEARS (15+ films) ===")
for year, count in sorted(year_films.items(), key=lambda x: -x[1]):
    if count >= 15:
        margins = [r['tradScore'] - r['wokeScore'] for r in year_films[year] if r.get('tradScore') is not None]
        if margins:
            wake_ones = sum(1 for m in margins if m < 0)
            trad_ones = sum(1 for m in margins if m > 0)
            print(f"  {year}: {count} films, {wake_ones} woke-leaning, {trad_ones} trad-leaning, margin range {min(margins):.1f} to {max(margins):.1f}")

print("\n=== TOP FRANCHISES (5+ films) ===")
for franchise, count in sorted(franchise_films.items(), key=lambda x: -x[1]):
    if count >= 5:
        margins = [r['tradScore'] - r['wokeScore'] for r in franchise_films[franchise]]
        if margins:
            print(f"  {franchise}: {count} films, margin range {min(margins):.1f} to {max(margins):.1f}")

print("\n=== TOP PLATFORMS (10+ films) ===")
for platform, count in sorted(platform_films.items(), key=lambda x: -x[1]):
    if count >= 10:
        margins = [r['tradScore'] - r['wokeScore'] for r in platform_films[platform]]
        if margins:
            print(f"  {platform}: {count} films, margin range {min(margins):.1f} to {max(margins):.1f}")

# Pick a promising genre: Drama (largest), Action (231), Thriller (98), Comedy (143), Crime (64)
# Let's look at the most woke Action films
print("\n=== TOP 20 MOST WOKE ACTION FILMS ===")
target_genre = 'Action'
action_films = [r for r in genre_films.get(target_genre, [])]
action_films.sort(key=lambda r: r['tradScore'] - r['wokeScore'])
for r in action_films[:20]:
    margin = r['tradScore'] - r['wokeScore']
    print(f"  {r['title']} ({r.get('year','?')}): woke={r['wokeScore']:.1f}, trad={r['tradScore']:.1f}, margin={margin:.1f}, verdict={r.get('verdict','?')}, slug={r.get('slug','?')}")

print("\n=== TOP 20 MOST TRADITIONAL ACTION FILMS ===")
for r in action_films[-20:]:
    margin = r['tradScore'] - r['wokeScore']
    print(f"  {r['title']} ({r.get('year','?')}): woke={r['wokeScore']:.1f}, trad={r['tradScore']:.1f}, margin={margin:.1f}, verdict={r.get('verdict','?')}, slug={r.get('slug','?')}")

# Also check "Most Woke Drama" as alternative
print("\n=== TOP 20 MOST WOKE DRAMA FILMS ===")
drama_films = [r for r in genre_films.get('Drama', [])]
drama_films.sort(key=lambda r: r['tradScore'] - r['wokeScore'])
for r in drama_films[:20]:
    margin = r['tradScore'] - r['wokeScore']
    print(f"  {r['title']} ({r.get('year','?')}): woke={r['wokeScore']:.1f}, trad={r['tradScore']:.1f}, margin={margin:.1f}, verdict={r.get('verdict','?')}, slug={r.get('slug','?')}")

# Check existing listicles
print("\n=== EXISTING LISTICLES ===")
import os
for f in sorted(os.listdir('lists')):
    if os.path.isdir(os.path.join('lists', f)):
        print(f"  {f}")

# Get next listicle number
listicle_dirs = [d for d in os.listdir('lists') if d.startswith('listicle-') and os.path.isdir(os.path.join('lists', d))]
if listicle_dirs:
    nums = [int(d.split('-')[1]) for d in listicle_dirs]
    print(f"\n=== NEXT LISTICLE NUMBER ===\n  Existing: {sorted(nums)[-10:]}\n  Next: {max(nums)+1}")
else:
    print("\nNo listicle-N dirs found")