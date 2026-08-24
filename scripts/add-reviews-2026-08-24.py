#!/usr/bin/env python3
"""Append 3 reviews to reviews.json for 2026-08-24."""
import json, os, shutil

REVIEWS_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'reviews.json')
BASE = os.path.dirname(os.path.abspath(__file__))
FILES = [
    os.path.join('/tmp', 'vv-review1-spa-weekend.json'),
    os.path.join('/tmp', 'vv-review2-amadeus.json'),
    os.path.join('/tmp', 'vv-review3-always-sunny.json'),
]

reviews = [json.load(open(f)) for f in FILES]

# Verify score sums (use JS-compatible rounding for verdict)
def verdict(m):
    if m >= 20: return 'STRONGLY TRADITIONAL'
    if m >= 10: return 'TRADITIONAL'
    if m >= 3: return 'TRADITIONAL LEAN'
    if m >= -2: return 'MIXED'
    if m >= -9: return 'WOKE LEAN'
    if m >= -19: return 'WOKE'
    return 'STRONGLY WOKE'

for r in reviews:
    woke = round(sum(t['weightedScore'] for t in r['tropeAudit'] if t.get('category','').upper() == 'WOKE'), 2)
    trad = round(sum(t['weightedScore'] for t in r['tropeAudit'] if t.get('category','').upper() != 'WOKE'), 2)
    margin = int(trad - woke + 0.5) if (trad - woke) >= 0 else int(trad - woke - 0.5)  # JS Math.round (half-up)
    assert abs(woke - r['wokeScore']) < 0.6, f"WOKE MISMATCH {r['slug']}: {woke} vs {r['wokeScore']}"
    assert abs(trad - r['tradScore']) < 0.6, f"TRAD MISMATCH {r['slug']}: {trad} vs {r['tradScore']}"
    assert verdict(margin) == r['verdict'], f"VERDICT MISMATCH {r['slug']}: {verdict(margin)} vs {r['verdict']}"
    # em dash / markdown guard
    blob = json.dumps(r)
    assert '\u2014' not in blob, f"EM DASH in {r['slug']}"
    assert '**' not in blob, f"MARKDOWN in {r['slug']}"
    print(f"{r['slug']}: woke={woke} trad={trad} margin={margin} verdict={r['verdict']} OK")

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

print(f"\nAdded {len(reviews)} reviews (backup at {bak})")
print(f"Total reviews: {len(data)}")
