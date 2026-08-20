#!/usr/bin/env python3
"""Daily VirtueVigil poster.

Picks next unposted review, posts review card to Bluesky, builds + uploads to YouTube.
Logs everything to posted_log.json and memory/YYYY-MM-DD.md.

Usage:
  python3 daily_post.py               # auto-pick next review
  python3 daily_post.py <slug>        # force a specific review
  python3 daily_post.py --bluesky     # Bluesky only
  python3 daily_post.py --youtube     # YouTube only
  python3 daily_post.py --dry-run     # show what would post, don't send
"""

import json, os, sys, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOCIAL_DIR = Path(__file__).resolve().parent
REVIEWS_PATH = ROOT / "src" / "data" / "reviews.json"
LOG_PATH = SOCIAL_DIR / "posted_log.json"
MEMORY_DIR = ROOT.parent / ".openclaw" / "workspace-bambi" / "memory"


def load_log() -> dict:
    if LOG_PATH.exists():
        return json.loads(LOG_PATH.read_text())
    return {"bluesky": [], "youtube": []}


def load_reviews() -> list:
    data = json.load(open(REVIEWS_PATH))
    return data if isinstance(data, list) else list(data.values())


def pick_review(log: dict, force_slug=None) -> dict:
    reviews = load_reviews()
    if force_slug:
        for r in reviews:
            if r.get("slug", "").lower() == force_slug.lower() or r.get("title", "").lower() == force_slug.lower():
                return r
        raise ValueError(f"Review not found: {force_slug}")

    posted_slugs = set(
        e["slug"] for e in log.get("bluesky", []) + log.get("youtube", [])
        if "slug" in e
    )

    # Prioritize: newly reviewed, most recent year first, skip already posted
    candidates = [
        r for r in reviews
        if r.get("slug") and r.get("slug") not in posted_slugs
    ]
    if not candidates:
        # All posted — start rotation over
        print("⚠️  All reviews posted, restarting rotation")
        candidates = reviews

    # Sort: most recent year first, then by title
    candidates.sort(key=lambda r: (-int(r.get("year", 0)), r.get("title", "")))
    return candidates[0]


def log_to_memory(review: dict, bsky_uri, yt_url, dry_run: bool):
    today = datetime.now().strftime("%Y-%m-%d")
    mem_path = MEMORY_DIR / f"{today}.md"
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    entry = (
        f"\n## Daily Post — {datetime.now().strftime('%I:%M %p')}\n\n"
        f"- Review: **{review.get('title')} ({review.get('year')})**\n"
        f"- Verdict: {review.get('verdict')}\n"
        f"- Trad: {review.get('tradScore', review.get('traditionalScore', '?'))} | Woke: {review.get('wokeScore', '?')}\n"
    )
    if dry_run:
        entry += "- Status: DRY RUN (not posted)\n"
    else:
        if bsky_uri:
            entry += f"- Bluesky: {bsky_uri}\n"
        if yt_url:
            entry += f"- YouTube: {yt_url}\n"
    existing = mem_path.read_text() if mem_path.exists() else ""
    mem_path.write_text(existing + entry)


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    do_bsky = "--youtube" not in args
    do_yt = "--bluesky" not in args
    args = [a for a in args if not a.startswith("--")]
    force_slug = args[0] if args else None

    # Load secrets
    secrets_path = Path.home() / ".openclaw" / ".secrets"
    if secrets_path.exists():
        for line in secrets_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                key = key.replace("export ", "").strip()
                os.environ.setdefault(key, val.strip())

    log = load_log()
    review = pick_review(log, force_slug)

    title = review.get("title")
    year = review.get("year")
    verdict = review.get("verdict")
    slug = review.get("slug")

    print(f"\n{'='*60}")
    print(f"  VirtueVigil Daily Post — {datetime.now().strftime('%Y-%m-%d')}")
    print(f"  Review: {title} ({year})")
    print(f"  Verdict: {verdict}")
    print(f"  Slug: {slug}")
    if dry_run:
        print("  MODE: DRY RUN")
    print(f"{'='*60}\n")

    bsky_uri = None
    yt_url = None

    if do_bsky:
        print("📘 Bluesky...")
        if dry_run:
            print("  [DRY RUN] Would post Bluesky card")
            bsky_uri = "dry-run"
        else:
            try:
                sys.path.insert(0, str(SOCIAL_DIR))
                from review_card import build_card
                from post_bluesky import post_to_bluesky
                card_path = build_card(review)
                print(f"  Card: {card_path}")
                bsky_uri = post_to_bluesky(review, card_path)
            except Exception as e:
                print(f"  ❌ Bluesky failed: {e}")

    if do_yt:
        print("\n📹 YouTube...")
        if dry_run:
            print("  [DRY RUN] Would build + upload YouTube Short")
            yt_url = "dry-run"
        else:
            try:
                sys.path.insert(0, str(SOCIAL_DIR))
                from upload_youtube import upload_short
                yt_url = upload_short(review)
            except Exception as e:
                print(f"  ❌ YouTube failed: {e}")

    log_to_memory(review, bsky_uri, yt_url, dry_run)

    print(f"\n{'='*60}")
    print(f"  Done: {title}")
    if bsky_uri and not dry_run:
        print(f"  Bluesky: {bsky_uri}")
    if yt_url and not dry_run:
        print(f"  YouTube: {yt_url}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
