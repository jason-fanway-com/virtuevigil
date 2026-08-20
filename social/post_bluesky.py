#!/usr/bin/env python3
"""Post a VirtueVigil review card to Bluesky.

Required env vars (source ~/.openclaw/.secrets):
  VV_BSKY_HANDLE   — e.g. virtuevigil.bsky.social
  VV_BSKY_PASSWORD — Bluesky app password
"""

import os, sys, json
from pathlib import Path
from atproto import Client
from review_card import build_card, load_review

ROOT = Path(__file__).resolve().parent.parent
REVIEWS_PATH = ROOT / "src" / "data" / "reviews.json"
LOG_PATH = Path(__file__).resolve().parent / "posted_log.json"


def load_log() -> dict:
    if LOG_PATH.exists():
        return json.loads(LOG_PATH.read_text())
    return {"bluesky": [], "youtube": []}


def save_log(log: dict):
    LOG_PATH.write_text(json.dumps(log, indent=2))


def build_caption(review: dict) -> str:
    title = review.get("title", "")
    year = review.get("year", "")
    verdict = review.get("verdict", "")
    trad = float(review.get("tradScore", review.get("traditionalScore", 0)))
    woke = float(review.get("wokeScore", 0))
    slug = review.get("slug", "")

    verdict_line = verdict.title()
    return (
        f"{title} ({year})\n\n"
        f"Verdict: {verdict_line}\n"
        f"Traditional Score: {trad:.1f}/10\n"
        f"Woke Score: {woke:.1f}/10\n\n"
        f"Full review: https://virtuevigil.com/reviews/{slug}\n\n"
        f"#VirtueVigil #CatholicFilm #TraditionalValues #MovieReview"
    )


def post_to_bluesky(review: dict, card_path=None) -> str:
    handle = os.environ.get("VV_BSKY_HANDLE")
    password = os.environ.get("VV_BSKY_PASSWORD")
    if not handle or not password:
        raise RuntimeError("VV_BSKY_HANDLE and VV_BSKY_PASSWORD must be set")

    if card_path is None:
        card_path = build_card(review)

    client = Client()
    client.login(handle, password)

    caption = build_caption(review)
    img_data = card_path.read_bytes()
    upload = client.upload_blob(img_data)

    post = client.send_image(
        text=caption,
        image=upload.blob,
        image_alt=f"VirtueVigil review card for {review.get('title')}",
    )

    uri = post.uri
    log = load_log()
    log["bluesky"].append({
        "slug": review.get("slug"),
        "title": review.get("title"),
        "uri": uri,
        "posted_at": __import__("datetime").datetime.utcnow().isoformat() + "Z",
    })
    save_log(log)
    print(f"✅ Bluesky: {uri}")
    return uri


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 post_bluesky.py <slug-or-title>")
        sys.exit(1)
    review = load_review(sys.argv[1])
    post_to_bluesky(review)
