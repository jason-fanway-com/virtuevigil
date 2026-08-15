#!/usr/bin/env python3
"""Append 3 reviews to reviews.json for 2026-08-15."""
import json, os, shutil

REVIEWS_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'reviews.json')
BASE = os.path.dirname(os.path.abspath(__file__))
FILES = [
    os.path.join(BASE, '..', 'brink-of-war-2026-review.json'),
    os.path.join(BASE, '..', 'paw-patrol-the-dino-movie-2026-review.json'),
    os.path.join(BASE, '..', 'euphoria-s1-2019-review.json'),
]

reviews = [json.load(open(f)) for f in FILES]

# Verify score sums for film entries
for r in reviews:
    if r.get('type') != 'film':
        continue
    woke = round(sum(t['weightedScore'] for t in r['tropeAudit'] if 'WOKE' in str(t.get('category','')).upper()), 2)
    trad = round(sum(t['weightedScore'] for t in r['tropeAudit'] if 'WOKE' not in str(t.get('category','')).upper()), 2)
    assert abs(woke - r['wokeScore']) < 0.6, f"WOKE MISMATCH {r['slug']}: {woke} vs {r['wokeScore']}"
    assert abs(trad - r['tradScore']) < 0.6, f"TRAD MISMATCH {r['slug']}: {trad} vs {r['tradScore']}"
    print(f"{r['slug']}: woke={woke} trad={trad} verdict={r['verdict']} margin={r['scoreMargin']} OK")

# Load existing
with open(REVIEWS_PATH) as f:
    data = json.load(f)

existing = {r.get('slug') for r in data}
for r in reviews:
    assert r['slug'] not in existing, f"DUPLICATE SLUG: {r['slug']}"

data.extend(reviews)

bak = REVIEWS_PATH.replace('.json', '.bak.json')
shutil.copy2(REVIEWS_PATH, bak)

with open(REVIEWS_PATH, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✓ Added {len(reviews)} reviews to reviews.json (backup at {bak})")
print(f"Total reviews: {len(data)}")
