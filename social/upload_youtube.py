#!/usr/bin/env python3
"""Build + upload a VirtueVigil YouTube Short for a review.

Setup (one-time):
  1. Enable YouTube Data API v3 in Google Cloud Console
  2. Download client_secret.json → social/youtube_client_secret.json
  3. First run triggers browser OAuth; token saved to social/youtube_token.json

Usage:
  python3 upload_youtube.py <slug-or-title>
"""

import json, os, sys, subprocess, tempfile
from pathlib import Path
from datetime import datetime

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build as yt_build
    from googleapiclient.http import MediaFileUpload
except ImportError:
    print("Missing: pip install google-auth-oauthlib google-api-python-client")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SOCIAL_DIR = Path(__file__).resolve().parent
REVIEWS_PATH = ROOT / "src" / "data" / "reviews.json"
LOG_PATH = SOCIAL_DIR / "posted_log.json"
CLIENT_SECRET = SOCIAL_DIR / "youtube_client_secret.json"
TOKEN_FILE = SOCIAL_DIR / "youtube_token.json"
VIDEO_SCRIPT = ROOT / "video" / "publish_short.py"

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def load_log() -> dict:
    if LOG_PATH.exists():
        return json.loads(LOG_PATH.read_text())
    return {"bluesky": [], "youtube": []}


def save_log(log: dict):
    LOG_PATH.write_text(json.dumps(log, indent=2))


def load_review(slug_or_title: str) -> dict:
    data = json.load(open(REVIEWS_PATH))
    reviews = data if isinstance(data, list) else list(data.values())
    q = slug_or_title.lower()
    for r in reviews:
        if r.get("slug", "").lower() == q or r.get("title", "").lower() == q:
            return r
    raise ValueError(f"Review not found: {slug_or_title}")


def get_youtube_client():
    if not CLIENT_SECRET.exists():
        raise RuntimeError(
            f"Missing {CLIENT_SECRET}\n"
            "Steps:\n"
            "  1. console.cloud.google.com → Enable YouTube Data API v3\n"
            "  2. APIs & Services → Credentials → OAuth 2.0 Client ID (Desktop)\n"
            "  3. Download JSON → social/youtube_client_secret.json"
        )
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return yt_build("youtube", "v3", credentials=creds)


def build_short_video(review: dict) -> Path:
    """Run publish_short.py to build the MP4."""
    title = review.get("title", "")
    reviews_path = ROOT / "src" / "data" / "reviews.json"
    out_dir = ROOT / "video" / "output"

    print(f"🎬 Building Short for: {title}")
    result = subprocess.run(
        ["python3", str(VIDEO_SCRIPT), str(reviews_path), title],
        capture_output=True, text=True, cwd=str(ROOT / "video")
    )
    if result.returncode != 0:
        print(result.stderr[-1000:])
        raise RuntimeError(f"Video build failed for: {title}")

    slug = title.lower().replace(" ", "_").replace(":", "")
    import re
    slug = re.sub(r"[^a-z0-9_]", "", slug)
    mp4 = out_dir / f"{slug}_short.mp4"
    if not mp4.exists():
        # fallback: find newest mp4
        files = sorted(out_dir.glob("*_short.mp4"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not files:
            raise RuntimeError(f"No MP4 found in {out_dir}")
        mp4 = files[0]
    return mp4


def build_title(review: dict) -> str:
    title = review.get("title", "")
    verdict = review.get("verdict", "")
    short_verdict = verdict.split()[0].title() if verdict else ""
    return f"{title}: {short_verdict} | VirtueVigil #Shorts"[:100]


def build_description(review: dict) -> str:
    slug = review.get("slug", "")
    title = review.get("title", "")
    trad = float(review.get("tradScore", review.get("traditionalScore", 0)))
    woke = float(review.get("wokeScore", 0))
    verdict = review.get("verdict", "")
    return (
        f"{title} — {verdict}\n\n"
        f"Traditional Score: {trad:.1f}/10 | Woke Score: {woke:.1f}/10\n\n"
        f"Full review: https://virtuevigil.com/reviews/{slug}\n\n"
        f"VirtueVigil rates movies on traditional Catholic values. "
        f"Know before you go.\n\n"
        f"#VirtueVigil #MovieReview #CatholicFilm #Shorts"
    )


def upload_short(review: dict, video_path=None) -> str:
    if video_path is None:
        video_path = build_short_video(review)

    youtube = get_youtube_client()

    body = {
        "snippet": {
            "title": build_title(review),
            "description": build_description(review),
            "tags": ["VirtueVigil", "MovieReview", "CatholicFilm", "Shorts", "TraditionalValues"],
            "categoryId": "1",  # Film & Animation
            "defaultLanguage": "en",
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False,
        },
    }

    media = MediaFileUpload(str(video_path), chunksize=-1, resumable=True, mimetype="video/mp4")
    req = youtube.videos().insert(part=",".join(body.keys()), body=body, media_body=media)

    print(f"⬆️  Uploading {video_path.name} ({video_path.stat().st_size // 1024}KB)...")
    response = None
    while response is None:
        status, response = req.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"  {pct}%", end="\r")

    video_id = response["id"]
    url = f"https://youtube.com/shorts/{video_id}"

    log = load_log()
    log["youtube"].append({
        "slug": review.get("slug"),
        "title": review.get("title"),
        "video_id": video_id,
        "url": url,
        "posted_at": datetime.utcnow().isoformat() + "Z",
    })
    save_log(log)
    print(f"✅ YouTube: {url}")
    return url


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 upload_youtube.py <slug-or-title>")
        sys.exit(1)
    review = load_review(sys.argv[1])
    upload_short(review)
