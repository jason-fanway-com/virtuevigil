#!/usr/bin/env python3
"""VirtueVigil YouTube Shorts Builder v2
1080×1920 30fps 30s Short: minimal graphic frames + burned-in captions + TTS.
Frames are visual backdrops — captions carry the narrative.
"""

import json, math, os, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from openai import OpenAI

ROOT = Path(__file__).resolve().parent
REVIEWS_PATH = ROOT.parent / "src" / "data" / "reviews.json"
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

W, H = 1080, 1920
FPS = 30
DURATION = 30
TOTAL_FRAMES = FPS * DURATION  # 900

# ── Color palette ───────────────────────────────────
BG_DEEP  = "#060612"
BG_DARK  = "#0D0D1A"
BG_NAVY  = "#0A1628"
GOLD     = "#F5C842"
GREEN    = "#2ECC71"
WHITE    = "#FFFFFF"
LGRAY    = "#B0B0C0"
DGRAY    = "#606080"
BLUE_TRD = "#1A5276"
SOFT_RED = "#8B2635"

_font_cache = {}
def _font(size, bold=False):
    k = (size, bold)
    if k in _font_cache: return _font_cache[k]
    try:
        f = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except Exception:
        f = ImageFont.load_default()
    _font_cache[k] = f
    return f

# ── Drawing helpers ─────────────────────────────────
def _new_frame(color=BG_DARK):
    return Image.new("RGB", (W, H), color)

def _bar(draw, x, y, w, h, fill, radius=0):
    if radius <= 0:
        draw.rectangle([x, y, x+w, y+h], fill=fill)
    else:
        draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=fill)

def _progress(draw, pct):
    y = H - 60
    bw = W - 240
    bx = (W - bw)//2
    _bar(draw, bx, y, bw, 2, (40,40,60))
    _bar(draw, bx, y, int(bw*pct), 2, GOLD)

def _glow_center(draw, cy, max_r, color, steps=8):
    """Radial gradient glow at center. color: hex string or (r,g,b) tuple."""
    if isinstance(color, str):
        rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    else:
        rgb = color
    for i in range(steps):
        r = int(max_r * (i+1)/steps)
        alpha = int(20 * (steps-i)/steps)
        _bar(draw, W/2 - r, cy - r, r*2, r*2, rgb + (alpha,), radius=r)

# ── OpenAI TTS ──────────────────────────────────────
def tts(text, path):
    c = OpenAI()
    r = c.audio.speech.create(model="tts-1", voice="nova", speed=1.05, input=text)
    r.stream_to_file(str(path))
    print(f"  🔊 TTS → {path}")

# ── SRT captions ────────────────────────────────────
CAPTIONS = [
    (0.0, 1.5,  "Hollywood wants"),
    (1.5, 3.0,  "your kids brainwashed."),
    (3.1, 5.0,  "Harry Potter: Chamber of Secrets."),
    (5.1, 6.5,  "Scored +32 traditional."),
    (6.6, 8.0,  "STRONGLY TRADITIONAL."),
    (8.1, 9.8,  "Self-sacrificing courage"),
    (9.9, 11.5, "Objective good versus evil"),
    (11.6, 13.2,"Choices define who you are"),
    (13.3, 14.8,"Justice is always restored"),
    (14.9, 16.3,"Merit earned through character"),
    (16.4, 18.0,"Woke score: just 4.6"),
    (18.1, 19.5,"No woke trap detected"),
    (19.6, 23.0,"Full review at VirtueVigil.com"),
]

def write_srt(p):
    out = []
    for i, (s, e, txt) in enumerate(CAPTIONS, 1):
        def fmt(t):
            h, rem = divmod(t, 3600); m, rem = divmod(rem, 60)
            sec, ms = divmod(rem, 1)
            return f"{int(h):02d}:{int(m):02d}:{int(sec):02d},{int(ms*1000):03d}"
        out.append(str(i))
        out.append(f"{fmt(s)} --> {fmt(e)}"); out.append(txt); out.append("")
    p.write_text("\n".join(out))
    return p

# ── Visual Scenes ───────────────────────────────────

def scene_hook():
    """Dark dramatic opening — bold red pulse, VV logo."""
    img = _new_frame(BG_DEEP)
    draw = ImageDraw.Draw(img)
    cy = H/2 - 80
    # Pulse rings
    for r, a in [(420, 8), (320, 14), (230, 22), (150, 35)]:
        _bar(draw, W/2-r, cy-r, r*2, r*2, (200, 30, 30, a), radius=r)
    # Small VV badge top
    b = draw.textbbox((0,0), "VIRTUE VIGIL", font=_font(26, True))
    tw = b[2]-b[0]
    draw.text(((W-tw)/2, 80), "VIRTUE VIGIL", fill=GOLD, font=_font(26, True))
    return img

def scene_title():
    """Title card — clean, cinematic."""
    img = _new_frame(BG_DARK)
    draw = ImageDraw.Draw(img)
    # Subtle gradient-ish bars
    _bar(draw, 0, int(H*0.15), W, 1, (40,40,60))
    _bar(draw, 0, H-int(H*0.15), W, 1, (40,40,60))
    # Title
    f1 = _font(44, True); f2 = _font(60, True); f3 = _font(26)
    b = draw.textbbox((0,0), "Harry Potter and the", font=f1)
    tw = b[2]-b[0]; draw.text(((W-tw)/2, H/2-100), "Harry Potter and the", fill=WHITE, font=f1)
    b = draw.textbbox((0,0), "Chamber of Secrets", font=f2)
    tw = b[2]-b[0]; draw.text(((W-tw)/2, H/2-20), "Chamber of Secrets", fill=GOLD, font=f2)
    draw.text((W/2-120, H/2+80), "2002  ·  Chris Columbus", fill=DGRAY, font=f3)
    return img

def scene_score():
    """Score — big green circle, clean metric bar."""
    img = _new_frame(BG_DARK)
    draw = ImageDraw.Draw(img)
    # Glow behind
    _glow_center(draw, H/2-100, 220, (46, 204, 113))
    cx, cy = W/2, H/2-100
    r = 110
    _bar(draw, cx-r, cy-r, r*2, r*2, GREEN, radius=r)
    f1 = _font(64, True); f2 = _font(40, True); f3 = _font(24)
    b = draw.textbbox((0,0), "+32", font=f1)
    tw, th = b[2]-b[0], b[3]-b[1]
    draw.text((cx-tw/2, cy-th/2), "+32", fill=WHITE, font=f1)
    # Label
    b = draw.textbbox((0,0), "TRADITIONAL", font=f2)
    tw = b[2]-b[0]
    draw.text(((W-tw)/2, H/2+60), "TRADITIONAL", fill=WHITE, font=f2)
    # Metric bar: trad vs woke
    bar_w = 600; bar_h = 8; bar_x = (W-bar_w)/2; bar_y = H/2+140
    _bar(draw, bar_x, bar_y, bar_w, bar_h, (40,40,60))
    trad_w = int(bar_w * 0.89)
    _bar(draw, bar_x, bar_y, trad_w, bar_h, GREEN)
    draw.text((bar_x-5, bar_y+20), "Trad 36.68", fill=LGRAY, font=f3)
    draw.text((bar_x+trad_w+5, bar_y+20), "Woke 4.62", fill=DGRAY, font=f3)
    return img

def scene_verdict():
    """Verdict badge + why."""
    img = _new_frame(BG_NAVY)
    draw = ImageDraw.Draw(img)
    bw, bh = 700, 130
    bx, by = (W-bw)//2, int(H*0.25)
    _bar(draw, bx, by, bw, bh, BLUE_TRD, radius=18)
    f1 = _font(44, True)
    b = draw.textbbox((0,0), "STRONGLY TRADITIONAL", font=f1)
    tw, th = b[2]-b[0], b[3]-b[1]
    draw.text(((W-tw)/2, by+bh/2-th/2), "STRONGLY TRADITIONAL", fill=WHITE, font=f1)
    # Score rows
    f2 = _font(36)
    items = [
        ("✓ Self-sacrificing courage", "6.3"),
        ("✓ Objective good vs evil", "6.3"),
        ("✓ Choices define character", "6.3"),
        ("✓ Justice restored", "5.0"),
        ("✓ Merit through character", "5.0"),
    ]
    y0 = H/2 + 20
    for i, (label, score) in enumerate(items):
        yy = y0 + i * 55
        draw.text((W/2-300, yy), label, fill=WHITE, font=f2)
        sc = _font(30, True)
        b = draw.textbbox((0,0), score, font=sc)
        draw.text((W/2+300 - b[2]+b[0], yy), score, fill=GOLD, font=sc)
    return img

def scene_trope(name, score, is_woke=False):
    """Individual trope — score circle + name — positioned higher for safe area."""
    img = _new_frame(BG_DARK)
    draw = ImageDraw.Draw(img)
    color = SOFT_RED if is_woke else BLUE_TRD
    label = "WOKE" if is_woke else "TRAD"
    # Centered but higher
    cx, cy = W/2, int(H*0.38)
    r = 90
    _glow_center(draw, cy, 160, color)
    _bar(draw, cx-r, cy-r, r*2, r*2, color, radius=r)
    fs = _font(44, True); fl = _font(22, True); fn = _font(36, True)
    txt = f"{score:.1f}"
    b = draw.textbbox((0,0), txt, font=fs)
    tw, th = b[2]-b[0], b[3]-b[1]
    draw.text((cx-tw/2, cy-th/2), txt, fill=WHITE, font=fs)
    # Label below circle
    b = draw.textbbox((0,0), label, font=fl)
    tw = b[2]-b[0]
    draw.text(((W-tw)/2, cy+r+24), label, fill=color if isinstance(color, str) else WHITE, font=fl)
    # Name
    b = draw.textbbox((0,0), name, font=fn)
    tw = b[2]-b[0]
    draw.text(((W-tw)/2, cy+r+90), name, fill=WHITE, font=fn)
    return img

def scene_cta():
    """Clean CTA card."""
    img = _new_frame(BG_DARK)
    draw = ImageDraw.Draw(img)
    # Accent line
    _bar(draw, W/2-250, H/2-100, 500, 2, GOLD)
    f1 = _font(52, True); f2 = _font(22)
    b = draw.textbbox((0,0), "VirtueVigil.com", font=f1)
    tw = b[2]-b[0]
    draw.text(((W-tw)/2, H/2+40), "VirtueVigil.com", fill=GOLD, font=f1)
    draw.text((W/2-140, H/2+120), "Know what you're watching.", fill=LGRAY, font=f2)
    return img

# ── Frame builder ───────────────────────────────────
def build_frames():
    frames_dir = OUTPUT_DIR / "frames"
    frames_dir.mkdir(exist_ok=True)
    print("🎬 Building frames...")

    imgs = {
        "hook":    scene_hook(),
        "title":   scene_title(),
        "score":   scene_score(),
        "verdict": scene_verdict(),
        "cta":     scene_cta(),
        "tropes":  [scene_trope(n, s, w) for n, s, w in [
            ("Self-Sacrificing Courage", 6.3, False),
            ("Good vs Evil", 6.3, False),
            ("Choices Define Character", 6.3, False),
            ("Justice Restored", 5.0, False),
            ("Merit Through Character", 5.0, False),
        ]],
    }

    # Scene sequence: list of (start_frame, end_frame, key_or_tuple)
    scenes = [
        (0,   49,   ("hook",)),
        (50,  99,   ("title",)),
        (100, 149,  ("hook",)),
        (150, 199,  ("score",)),
        (200, 259,  ("tropes", 0)),
        (260, 319,  ("tropes", 1)),
        (320, 379,  ("tropes", 2)),
        (380, 439,  ("tropes", 3)),
        (440, 499,  ("tropes", 4)),
        (500, 569,  ("verdict",)),
        (570, 629,  ("score",)),
        (630, 699,  ("verdict",)),
        (700, 769,  ("cta",)),
        (770, 839,  ("score",)),
        (840, 899,  ("cta",)),
    ]

    for sf, ef, key in scenes:
        k = key[0]
        if k == "tropes":
            base = imgs["tropes"][key[1]]
        else:
            base = imgs[k]
        for f in range(sf, ef+1):
            pct = (f - sf) / max(1, ef-sf)
            zoom = 1.0 + math.sin(pct * math.pi) * 0.025
            pan = int(math.sin(pct * math.pi) * 6)
            nw, nh = int(W*zoom), int(H*zoom)
            if nw != W or nh != H or pan:
                scaled = base.resize((nw, nh), Image.LANCZOS)
                frame = scaled.crop(((nw-W)//2, max(0,(nh-H)//2 + pan), (nw-W)//2+W, max(0,(nh-H)//2+pan)+H))
            else:
                frame = base.copy()
            draw = ImageDraw.Draw(frame)
            _progress(draw, f/max(1, TOTAL_FRAMES-1))
            frame.save(frames_dir / f"frame_{f:04d}.png")
    print(f"  ✅ {TOTAL_FRAMES} frames → {frames_dir}")
    return frames_dir

# ── FFmpeg ──────────────────────────────────────────
def assemble(frames_dir, audio_path, srt_path):
    print("🎞️  Assembling with FFmpeg...")
    out = OUTPUT_DIR / "vv_short_v2.mp4"
    srt_esc = str(srt_path).replace(':', '\\:')
    vf = (
        f"format=yuv420p,"
        f"subtitles={srt_esc}:"
        f"force_style='FontName=Helvetica,FontSize=14,"
        f"PrimaryColour=&H00FFFFFF,"
        f"OutlineColour=&H80000000,Outline=1,Shadow=0.5,"
        f"Alignment=2,MarginV=48,MarginL=72,MarginR=72,BorderStyle=1'"
    )
    cmd = ["ffmpeg", "-y", "-framerate", str(FPS),
           "-i", str(frames_dir/"frame_%04d.png"),
           "-i", str(audio_path),
           "-c:v", "libx264", "-preset", "fast", "-crf", "23",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
           "-shortest", "-movflags", "+faststart", "-vf", vf, str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  ❌ FFmpeg failed:\n{r.stderr[-600:]}")
        return None
    print(f"  ✅ Video → {out}")
    return out

# ── Narration ───────────────────────────────────────
NARRATION = (
    "Hollywood wants your kids brainwashed. "
    "Harry Potter Chamber of Secrets. "
    "Plus 32 traditional. Strongly traditional. "
    "Self-sacrificing courage. Six point three. "
    "Objective good versus evil. Six point three. "
    "Choices define character. Six point three. "
    "Justice restored. Five point oh. "
    "Merit through character. Five point oh. "
    "Woke score: just four point six. No woke trap. "
    "Read the full review at VirtueVigil dot com."
)

def main():
    print("🎥 VirtueVigil Shorts Builder v2")
    print("=" * 50)
    with open(REVIEWS_PATH) as f:
        data = json.load(f)
    review = next((r for r in data if "chamber" in r.get("slug","").lower()), None)
    if not review:
        print("❌ Review not found"); return
    print(f"📋 Review: {review['title']} ({review['year']})")
    print(f"🏷️  {review['verdict']} | Trad: {review['tradScore']} | Woke: {review['wokeScore']}")
    audio = OUTPUT_DIR / "narration_v2.mp3"
    print(f"📝 Narration: {len(NARRATION)} chars")
    tts(NARRATION, audio)
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                         "-of","default=noprint_wrappers=1:nokey=1",str(audio)],
                        capture_output=True, text=True)
    if r.returncode == 0:
        print(f"  ⏱️  Audio: {float(r.stdout.strip()):.1f}s (target: {DURATION}s)")
    frames_dir = build_frames()
    srt = OUTPUT_DIR / "captions_v2.srt"
    write_srt(srt); print(f"📝 Captions → {srt}")
    video = assemble(frames_dir, audio, srt)
    if not video: return
    sz = video.stat().st_size
    r2 = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                          "-of","default=noprint_wrappers=1:nokey=1",str(video)],
                         capture_output=True, text=True)
    dur = float(r2.stdout.strip()) if r2.returncode==0 else None
    print(f"\n✅ DONE: {video}")
    print(f"   Size: {sz/1024/1024:.1f} MB")
    if dur: print(f"   Duration: {dur:.0f}s")
    print(f"   Format: {W}x{H} (9:16)")

if __name__ == "__main__":
    main()