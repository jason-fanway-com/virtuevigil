#!/usr/bin/env python3
"""Generate a 1080x1080 VirtueVigil review card for social posts."""

import json, sys, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
REVIEWS_PATH = ROOT / "src" / "data" / "reviews.json"
POSTERS_DIR = ROOT / "src" / "images" / "posters"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

W, H = 1080, 1080

# Colors
BG       = "#08080F"
GOLD     = "#F5C842"
GREEN    = "#2ECC71"
RED      = "#E74C3C"
WHITE    = "#F0F0F0"
GRAY     = "#8888AA"
DGRAY    = "#3A3A55"
ACCENT   = "#1A1A2E"


def _font(size):
    try:
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except Exception:
        return ImageFont.load_default()


def _draw_score_bar(draw, x, y, w, h, value, max_val=10.0, color=GREEN):
    fill_w = int(w * (value / max_val))
    draw.rectangle([x, y, x + w, y + h], fill=DGRAY)
    if fill_w > 0:
        draw.rectangle([x, y, x + fill_w, y + h], fill=color)


def _wrap(text, font, max_w, draw):
    words = text.split()
    lines, line = [], []
    for word in words:
        test = " ".join(line + [word])
        if draw.textlength(test, font=font) <= max_w:
            line.append(word)
        else:
            if line:
                lines.append(" ".join(line))
            line = [word]
    if line:
        lines.append(" ".join(line))
    return lines


def build_card(review: dict, out_path=None) -> Path:
    slug = review.get("slug", "unknown")
    title = review.get("title", "Unknown")
    year = review.get("year", "")
    verdict = review.get("verdict", "")
    trad = float(review.get("tradScore", review.get("traditionalScore", 0)))
    woke = float(review.get("wokeScore", 0))

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # === POSTER strip (left panel, 340px wide) ===
    poster_path = POSTERS_DIR / f"{slug}.jpg"
    if poster_path.exists():
        try:
            poster = Image.open(poster_path).convert("RGB")
            ph = int(340 * poster.height / poster.width)
            if ph > H:
                ph = H
            poster = poster.resize((340, ph), Image.LANCZOS)
            img.paste(poster, (0, (H - ph) // 2))
            # dark gradient over poster
            grad = Image.new("RGBA", (340, H), (8, 8, 15, 0))
            gd = ImageDraw.Draw(grad)
            for i in range(340):
                alpha = int(220 * (i / 340))
                gd.line([(i, 0), (i, H)], fill=(8, 8, 15, alpha))
            img.paste(Image.new("RGB", (340, H), BG), (0, 0), grad)
        except Exception:
            pass

    # === Right panel ===
    PX = 380  # start x
    PW = W - PX - 40  # usable width

    # Brand line
    f_brand = _font(26)
    draw.text((PX, 60), "VIRTUEVIGIL.COM", font=f_brand, fill=GOLD)

    # Title
    f_title = _font(52)
    title_lines = _wrap(title, f_title, PW, draw)
    ty = 110
    for line in title_lines[:3]:
        draw.text((PX, ty), line, font=f_title, fill=WHITE)
        ty += 60

    # Year
    f_year = _font(32)
    draw.text((PX, ty), str(year), font=f_year, fill=GRAY)
    ty += 55

    # Divider
    draw.rectangle([PX, ty, W - 40, ty + 2], fill=DGRAY)
    ty += 20

    # Verdict pill
    verdict_color = GREEN if "TRADITIONAL" in verdict.upper() else (RED if "WOKE" in verdict.upper() else GOLD)
    f_verdict = _font(30)
    v_short = verdict.replace("STRONGLY ", "").replace("LEAN", "LEAN").upper()
    vw = int(draw.textlength(v_short, font=f_verdict)) + 30
    draw.rectangle([PX, ty, PX + vw, ty + 44], fill=verdict_color)
    draw.text((PX + 15, ty + 7), v_short, font=f_verdict, fill=BG)
    ty += 65

    # Scores
    f_label = _font(26)
    f_score = _font(44)

    # Traditional score
    draw.text((PX, ty), "TRADITIONAL", font=f_label, fill=GRAY)
    ty += 34
    draw.text((PX, ty), f"{trad:.1f}/10", font=f_score, fill=GREEN)
    ty += 54
    _draw_score_bar(draw, PX, ty, PW, 14, trad, color=GREEN)
    ty += 35

    # Woke score
    draw.text((PX, ty), "WOKE", font=f_label, fill=GRAY)
    ty += 34
    draw.text((PX, ty), f"{woke:.1f}/10", font=f_score, fill=RED)
    ty += 54
    _draw_score_bar(draw, PX, ty, PW, 14, woke, color=RED)
    ty += 50

    # Divider
    draw.rectangle([PX, ty, W - 40, ty + 2], fill=DGRAY)
    ty += 25

    # CTA
    f_cta = _font(28)
    draw.text((PX, ty), "Full review at virtuevigil.com", font=f_cta, fill=GOLD)

    # Bottom watermark
    f_wm = _font(22)
    draw.text((PX, H - 50), "Objective | Catholic | Traditional", font=f_wm, fill=DGRAY)

    if out_path is None:
        out_path = OUTPUT_DIR / f"{slug}_card.jpg"
    img.save(out_path, "JPEG", quality=90)
    return out_path


def load_review(slug_or_title: str) -> dict:
    data = json.load(open(REVIEWS_PATH))
    reviews = data if isinstance(data, list) else list(data.values())
    slug_or_title_lower = slug_or_title.lower()
    for r in reviews:
        if r.get("slug", "").lower() == slug_or_title_lower:
            return r
        if r.get("title", "").lower() == slug_or_title_lower:
            return r
    raise ValueError(f"Review not found: {slug_or_title}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 review_card.py <slug-or-title>")
        sys.exit(1)
    review = load_review(sys.argv[1])
    out = build_card(review)
    print(f"Card saved: {out}")
