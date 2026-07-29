import json

r = json.load(open("src/data/reviews.json"))
for rev in r:
    if rev["slug"] == "furious-s1-2026":
        rev["title"] = "Furious: Season 1"
        rev["seo"]["titleTag"] = "Is Furious: Season 1 (2026) Woke? Hulu's Emmy Rossum Thriller Review | VirtueVigil"
        rev["seo"]["metaDescription"] = "VirtueVigil's full VVWS review of Furious: Season 1 (2026). Emmy Rossum stars as an FBI agent hunting a female serial killer in Elizabeth Meriwether's post-Epstein thriller. Trope scores, verdict: WOKE (-9.8). Parental guidance included."
        rev["seo"]["keywords"] = "is furious woke, furious season 1 2026 review, furious hulu review, furious virtuevigil, furious traditional or woke, emmy rossum furious, elizabeth meriwether furious, furious parents guide, furious tv series"
        rev["summary"]["overall"] = rev["summary"]["overall"].replace("Furious arrives", "Elizabeth Meriwether's Furious: Season 1 arrives")
        print("Updated title:", rev["title"])
        break

json.dump(r, open("src/data/reviews.json", "w"), indent=2, ensure_ascii=False)
print("Done")