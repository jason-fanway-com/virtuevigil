import json
reviews = json.load(open("/Users/joestrazza/virtuevigil/src/data/reviews.json"))
slugs = {r["slug"] for r in reviews}
print(f"Total reviews: {len(reviews)}")

# Major missing classics check
checks = [
    "saving-private-ryan", "gladiator", "braveheart", "the-green-mile",
    "citizen-kane", "2001-a-space-odyssey", "alien", "aliens",
    "the-shining", "rocky", "raging-bull", "eternal-sunshine",
    "no-country-for-old-men", "there-will-be-blood", "the-truman-show",
    "the-princess-bride", "ferris-buellers-day-off", "the-breakfast-club",
    "american-psycho", "reservoir-dogs", "django-unchained",
    "inglourious-basterds", "once-upon-a-time-in-hollywood",
    "the-irishman", "saving-private-ryan", "scarface",
    "taxi-driver", "seven", "the-usual-suspects", "memento",
    "the-pianist", "la-la-land", "mad-max-fury-road",
    "the-revenant", "arrival", "blade-runner-2049", "sicario",
    "ex-machina", "get-out", "john-wick", "the-john-wick",
    "hereditary", "the-witch", "midsommar", "the-lighthouse",
    "a-quiet-place", "the-conjuring", "it", "the-avengers",
    "iron-man", "thor", "captain-america", "black-panther",
    "doctor-strange", "ant-man", "wandavision", "loki",
    "the-mandalorian", "andor", "ted-lasso", "the-white-lotus",
    "the-bear", "euphoria", "the-office", "friends", "seinfeld",
    "the-simpsons", "south-park", "family-guy",
    "the-french-connection", "chinatown", "the-conversation",
    "dog-day-afternoon", "network", "apocalypse-now",
    "full-metal-jacket", "platoon", "the-deer-hunter",
]

print("\n=== Gap Analysis ===")
missing = []
found = []
for c in checks:
    if any(c in s for s in slugs):
        found.append(c)
    else:
        missing.append(c)

print(f"Found: {len(found)}/{len(checks)}")
print(f"Missing: {len(missing)}")
print("\nTop Missing (first 20):")
for m in missing[:20]:
    print(f"  MISSING: {m}")

# Latest reviews
print("\n=== Latest 20 slugs ===")
for s in [r["slug"] for r in reviews[-20:]]:
    print(f"  {s}")