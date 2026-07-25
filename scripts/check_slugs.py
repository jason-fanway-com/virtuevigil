import json
reviews = json.load(open("/Users/joestrazza/virtuevigil/src/data/reviews.json"))
slugs = {r["slug"] for r in reviews}
print(f"Total reviews: {len(reviews)}")

# Upcoming releases
checks = [
    "the-fifth-element", "above-and-below", "sheep-in-the-box",
    "once-upon-a-time-in-a-cinema", "middle-life", "wham-10-days",
    "wild-inside", "jimmy"
]
print("\n=== Upcoming Releases ===")
for c in checks:
    status = "EXISTS" if any(c in s for s in slugs) else "NOT FOUND"
    print(f"  {c}: {status}")

# Latest 15 slugs
print("\n=== Latest 15 Reviews ===")
for s in [r["slug"] for r in reviews[-15:]]:
    print(f"  {s}")