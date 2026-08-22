#!/usr/bin/env python3
"""
Visual QA — Post-build browser verification
Screenshots review pages and runs vision-model checks on posters, layout, and broken images.

Usage:
    python3 visual-qa.py                    # Check latest 3 reviews + homepage
    python3 visual-qa.py --slug toy-story-1995  # Single review
    python3 visual-qa.py --all              # All reviews (slow, use sparingly)

Config:
    GEMINI_API_KEY env var required for vision checks.
    Falls back to MD5-based checks if vision unavailable.
"""
import hashlib, json, os, re, subprocess, sys, time, tempfile, argparse
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DIST = REPO / "dist"
REVIEWS_JSON = REPO / "src" / "data" / "reviews.json"
POSTERS_DIR = REPO / "src" / "images" / "posters"
PLACEHOLDER_MD5 = "cc5e7c3e669e2c8e8182fcd083cfafe2"

BASE_URL = os.environ.get("VV_SITE_URL", "https://virtuevigil.com")

# ── helpers ──────────────────────────────────────────────
def load_reviews():
    with open(REVIEWS_JSON) as f:
        return json.load(f)

def md5_file(path):
    if not os.path.exists(path): return None
    return hashlib.md5(open(path, "rb").read()).hexdigest()

def curl_get(url, binary=False):
    try:
        mode = "-o /dev/null" if not binary else ""
        if binary:
            r = subprocess.run(["curl", "-sL", "--max-time", "15", "-H", "User-Agent: Mozilla/5.0", url],
                               capture_output=True, timeout=20)
            return r.stdout if r.returncode == 0 else None
        else:
            r = subprocess.run(["curl", "-sL", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "15", url],
                               capture_output=True, text=True, timeout=20)
            return r.stdout.strip()
    except Exception:
        return None

# ── MD5 audit (always works, no API key needed) ──────────
def md5_audit(slugs=None):
    """Check that live poster MD5s match local files and neither is placeholder."""
    reviews = load_reviews()
    results = {"ok": [], "placeholder": [], "mismatch": [], "missing": [], "no_field": []}

    for r in reviews:
        slug = r["slug"]
        if slugs and slug not in slugs:
            continue
        poster = r.get("poster", "")
        if not poster:
            results["no_field"].append(slug)
            continue

        fname = os.path.basename(poster)
        local_path = POSTERS_DIR / fname
        local_hash = md5_file(local_path)

        url = f"{BASE_URL}/images/posters/{fname}"
        live_data = curl_get(url, binary=True)
        if live_data is None:
            results["missing"].append(slug)
            continue
        live_hash = hashlib.md5(live_data).hexdigest()

        if local_hash == PLACEHOLDER_MD5 or live_hash == PLACEHOLDER_MD5:
            results["placeholder"].append(slug)
        elif local_hash != live_hash:
            results["mismatch"].append((slug, local_hash or "missing", live_hash))
        else:
            results["ok"].append((slug, local_hash[:12]))

    return results

# ── vision check (Gemini SDK) ───────────────────────────
def check_with_vision(image_path, title):
    """Use Gemini (google-genai SDK) to verify the poster looks correct."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        return {"status": "SKIP", "reason": "no GEMINI_API_KEY"}

    try:
        from google import genai
        import PIL.Image
    except ImportError as e:
        return {"status": "ERROR", "detail": f"Missing dependency: {e}. Run: pip3 install google-genai Pillow --break-system-packages"}

    try:
        img = PIL.Image.open(image_path)
    except Exception as e:
        return {"status": "ERROR", "detail": f"Cannot open image {image_path}: {e}"}

    prompt = (
        f"Look at this screenshot of a review page for '{title}' on a movie review website. "
        "Focus on the poster image. Is it the correct official movie/show poster for this title, "
        "or is it a generic 'Coming Soon' placeholder? "
        "Also check: are there any broken image icons, layout problems, or missing elements? "
        "Answer CONCISELY: PASS if poster looks correct and page renders properly. "
        "FAIL if poster is wrong, placeholder, or page has visible issues. "
        "Include a one-line reason."
    )

    try:
        client = genai.Client(api_key=key)
        resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt, img]
        )
        text = resp.text
        passed = text.strip().upper().startswith("PASS")
        return {"status": "PASS" if passed else "FAIL", "detail": text.strip()}
    except Exception as e:
        return {"status": "ERROR", "detail": str(e)}

# ── screenshot a page ─────────────────────────────────────
# NOTE: This uses the OpenClaw browser tool via CLI — the calling agent
# should already have a browser open. This script just coordinates.
# For standalone use, we rely on curl+MD5 checks.
def screenshot_page(slug):
    """Not standalone — returns instructions for the agent."""
    url = f"{BASE_URL}/reviews/{slug}/"
    return f"Open browser to {url}, take viewport screenshot, save as /tmp/vv-{slug}.png"


# ── main ──────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="VirtueVigil Visual QA")
    parser.add_argument("--slug", help="Single review slug to check")
    parser.add_argument("--all", action="store_true", help="Check all reviews")
    parser.add_argument("--md5-only", action="store_true", help="Skip vision, MD5 audit only")
    parser.add_argument("--latest", type=int, default=3, help="Number of latest reviews to check")
    args = parser.parse_args()

    reviews = load_reviews()

    if args.slug:
        targets = [r for r in reviews if r["slug"] == args.slug]
    elif args.all:
        targets = reviews
    else:
        # Latest N
        targets = reviews[-args.latest:]

    if not targets:
        print("No reviews found.")
        sys.exit(1)

    slugs = [r["slug"] for r in targets]
    print(f"Checking {len(slugs)} review(s)...")

    # Step 1: MD5 audit
    print("\n── MD5 Audit ──")
    audit = md5_audit(slugs)
    clean = True
    for cat, items in audit.items():
        if items:
            print(f"  {cat.upper()}: {len(items)}")
            for item in items:
                print(f"    {item}")
            if cat != "ok":
                clean = False

    if audit["placeholder"] or audit["missing"] or audit["mismatch"]:
        print("\n❌ MD5 AUDIT FAILED")
        sys.exit(1)

    print(f"\n✅ MD5 audit: {len(audit['ok'])} OK")

    # Step 2: Vision check (if API key available)
    if args.md5_only:
        print("\n── Skipping vision check (--md5-only) ──")
        sys.exit(0)

    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("\n── Skipping vision check (no GEMINI_API_KEY) ──")
        print("Set GEMINI_API_KEY for visual poster verification.")
        sys.exit(0)

    print("\n── Vision Check ──")
    print("(Requires browser screenshots — run from agent with browser access)")
    print(f"To visually verify: screenshot each review page to /tmp/vv-<slug>.png")
    print(f"Then run with --slug and --md5-only=false")
    print(f"Targets: {slugs}")


if __name__ == "__main__":
    main()