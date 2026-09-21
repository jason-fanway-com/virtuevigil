#!/usr/bin/env python3
"""VV Poster Audit — comprehensive check of all review poster files."""
import json, os, sys, hashlib
from datetime import datetime, timedelta, timezone
from pathlib import Path
from PIL import Image

REPO = Path("/Users/joestrazza/virtuevigil")
REVIEWS_PATH = REPO / "src/data/reviews.json"
POSTERS_DIR = REPO / "src/images/posters"
CUTOFF_DAYS = 7

def load_reviews():
    with open(REVIEWS_PATH) as f:
        return json.load(f)

def md5_file(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    reviews = load_reviews()
    failures = {
        'missing': [],        # poster field empty or file not on disk
        'corrupt': [],        # PIL can't open
        'small': [],          # <= 5KB
        'bad_aspect': [],     # aspect ratio outside 0.5-1.0
        'placeholder': [],    # path contains 'placeholder'
        'duplicate': [],      # identical md5 for different slugs
        'new_no_poster': [],  # review added <=7 days ago, no poster
    }

    cutoff = datetime.now(timezone.utc) - timedelta(days=CUTOFF_DAYS)

    # Collect all poster paths from reviews
    slug_poster = {}
    for r in reviews:
        slug = r.get('slug', 'UNKNOWN')
        poster = r.get('poster', '')
        slug_poster[slug] = poster

    # --- 1. Poster file health + placeholder scan ---
    file_hashes = {}  # hash -> list of slugs
    for slug, poster_path in slug_poster.items():
        if not poster_path:
            failures['missing'].append(slug)
            continue

        # Placeholder check
        if 'placeholder' in poster_path.lower():
            failures['placeholder'].append(slug)

        # Poster paths are /images/posters/X.jpg → actual files at src/images/posters/X.jpg
        rel = poster_path.lstrip('/')
        full_path = REPO / 'src' / rel
        if not full_path.exists():
            failures['missing'].append(slug)
            continue

        # Size check
        size = full_path.stat().st_size
        if size <= 5120:
            failures['small'].append(slug)

        # Corruption + aspect ratio
        try:
            img = Image.open(full_path)
            img.verify()
            img = Image.open(full_path)  # re-open after verify
            w, h = img.size
            ratio = w / h if h > 0 else 0
            if ratio < 0.5 or ratio > 1.0:
                failures['bad_aspect'].append(f"{slug} ({w}x{h}, ratio={ratio:.3f})")
        except Exception as e:
            failures['corrupt'].append(f"{slug}: {e}")

        # Hash for duplicate detection
        try:
            h = md5_file(full_path)
            file_hashes.setdefault(h, []).append(slug)
        except:
            pass

    # --- 2. Duplicate detection ---
    dupes_found = set()
    for h, slugs in file_hashes.items():
        if len(slugs) > 1:
            dupes_found.add(tuple(sorted(slugs)))
    failures['duplicate'] = [' / '.join(slugs) for slugs in sorted(dupes_found)]

    # --- 6. New reviews without posters ---
    for r in reviews:
        slug = r.get('slug', '')
        added_str = r.get('dateAdded', '') or r.get('date_added', '') or r.get('created', '')
        if added_str:
            try:
                added = datetime.fromisoformat(added_str.replace('Z', '+00:00'))
                if added >= cutoff:
                    if not r.get('poster', ''):
                        failures['new_no_poster'].append(slug)
            except:
                pass

    # Summary
    total = len(reviews)
    issue_count = sum(len(v) for v in failures.values())
    unique_slugs_with_issues = set()
    for cat, items in failures.items():
        for item in items:
            slug = item.split(':')[0].split(' / ')[0] if cat == 'duplicate' else item.split(' (')[0]
            unique_slugs_with_issues.add(slug)

    print(f"TOTAL: {total} reviews")
    print(f"PASS: {total - len(unique_slugs_with_issues)}")
    print(f"ISSUES: {len(unique_slugs_with_issues)} slugs / {issue_count} total failures")
    print()

    if issue_count == 0:
        print("RESULT: ALL CLEAN — zero issues found.")
    else:
        print("RESULT: ISSUES FOUND — breakdown follows.\n")
        for cat, items in failures.items():
            if items:
                print(f"## {cat.upper()} ({len(items)})")
                for item in items:
                    print(f"  - {item}")
                print()

    # Also print dupe stats
    print(f"UNIQUE HASHES: {len(file_hashes)}")
    print(f"DUPLICATE CLUSTERS: {len(failures['duplicate'])}")

if __name__ == '__main__':
    main()