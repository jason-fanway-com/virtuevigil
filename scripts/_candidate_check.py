#!/usr/bin/env python3
"""Check candidate titles against existing reviews.json to find available slots."""
import json

REVIEWS = '/Users/joestrazza/virtuevigil/src/data/reviews.json'

with open(REVIEWS) as f:
    data = json.load(f)

existing_slugs = set(r.get('slug','').lower() for r in data)
existing_pairs = set()
for r in data:
    existing_pairs.add((r.get('title','').lower().strip(), str(r.get('year',''))))

candidates = [
    # Bucket 1 — new releases July 2026
    ("Superman", 2026, "film"),
    ("Thunderbolts", 2026, "film"),
    ("Ballerina", 2025, "film"),
    ("Jurassic World: Rebirth", 2026, "film"),
    ("The Fantastic Four", 2025, "film"),
    # Bucket 2 — catalog backfill
    ("The Shawshank Redemption", 1994, "film"),
    ("Pulp Fiction", 1994, "film"),
    ("The Godfather", 1972, "film"),
    ("Schindler's List", 1993, "film"),
    ("Forrest Gump", 1994, "film"),
    ("The Matrix", 1999, "film"),
    ("Goodfellas", 1990, "film"),
    ("Star Wars", 1977, "film"),
    ("The Empire Strikes Back", 1980, "film"),
    ("Return of the Jedi", 1983, "film"),
    ("The Dark Knight", 2008, "film"),
    ("Inception", 2010, "film"),
    ("Interstellar", 2014, "film"),
    ("Gladiator", 2000, "film"),
    ("Saving Private Ryan", 1998, "film"),
    ("Braveheart", 1995, "film"),
    ("Titanic", 1997, "film"),
    ("Alien", 1979, "film"),
    ("Aliens", 1986, "film"),
    ("Jurassic Park", 1993, "film"),
    ("Back to the Future", 1985, "film"),
    ("Jaws", 1975, "film"),
    ("Raiders of the Lost Ark", 1981, "film"),
    ("The Silence of the Lambs", 1991, "film"),
    ("The Departed", 2006, "film"),
    ("Inglourious Basterds", 2009, "film"),
    ("Django Unchained", 2012, "film"),
    ("Top Gun", 1986, "film"),
    ("Top Gun: Maverick", 2022, "film"),
    ("Die Hard", 1988, "film"),
    ("The Prestige", 2006, "film"),
    ("Whiplash", 2014, "film"),
    ("Se7en", 1995, "film"),
    ("Fight Club", 1999, "film"),
    # Bucket 3 — TV
    ("Stranger Things", 2016, "tv"),
    ("The Last of Us", 2023, "tv"),
    ("House of the Dragon", 2022, "tv"),
    ("The Bear", 2022, "tv"),
    ("Wednesday", 2022, "tv"),
    ("The Mandalorian", 2019, "tv"),
    ("The White Lotus", 2021, "tv"),
    ("Succession", 2018, "tv"),
    ("Severance", 2022, "tv"),
    ("Ted Lasso", 2020, "tv"),
    ("Shogun", 2024, "tv"),
    ("Fallout", 2024, "tv"),
    ("Breaking Bad", 2008, "tv"),
    ("The Sopranos", 1999, "tv"),
    ("Game of Thrones", 2011, "tv"),
]

available = []
for title, year, typ in candidates:
    clean = title.lower().replace(": ","-").replace(":","-").replace("  "," ").replace(" ","-")
    clean = clean.replace("'","").replace(".","").replace(",","").replace("(","").replace(")","")
    slug = f"{clean}-{year}"
    pair = (title.lower().strip(), str(year))
    if slug.lower() in existing_slugs:
        print(f"EXISTS: {title} ({year}) [{typ}]")
        continue
    if pair in existing_pairs:
        alt_matches = [r.get("slug","") for r in data if r.get("title","").lower().strip() == title.lower().strip() and str(r.get("year","")) == str(year)]
        print(f"EXISTS (alt slug): {title} ({year}) -> {alt_matches}")
        continue
    available.append((title, year, typ, slug))
    print(f"FREE: {title} ({year}) [{typ}] -> {slug}")

print(f"\nTOTAL FREE: {len(available)}")
print(f"TOTAL EXISTS: {len(candidates) - len(available)}")
print(f"\nSUGGESTED 3 (1-new, 1-catalog, 1-tv):")
# Bucket 1 pick
b1 = [a for a in available if a[2] == "film" and a[1] >= 2025]
b2 = [a for a in available if a[2] == "film" and a[1] < 2025]
b3 = [a for a in available if a[2] == "tv"]
if b1: print(f"  NEW: {b1[0][0]} ({b1[0][1]})")
if b2: print(f"  CATALOG: {b2[0][0]} ({b2[0][1]})")
if b3: print(f"  TV: {b3[0][0]} ({b3[0][1]})")