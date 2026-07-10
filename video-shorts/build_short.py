#!/usr/bin/env python3
"""
VirtueVigil Video Short Builder — Fast Edition
Generates a ~45s YouTube Short: key frames + FFmpeg compositing
Usage: python3 build_short.py --slug conclave-2024
"""

import json, os, sys, argparse, subprocess
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from PIL import Image, ImageDraw, ImageFont

REPO = Path("/Users/joestrazza/virtuevigil")
REVIEWS_PATH = REPO / "src/data/reviews.json"
OUTPUT_DIR = REPO / "video-shorts/output"
FRAMES_DIR = REPO / "video-shorts/frames"
AUDIO_DIR = REPO / "video-shorts/audio"
FPS = 30
WIDTH, HEIGHT = 1080, 1920

BG_DARK = (18, 18, 22, 255)
WHITE = (255, 255, 255, 255)
RED = (220, 38, 38, 255)
GREEN = (22, 163, 74, 255)
GOLD = (245, 158, 11, 255)
GRAY = (120, 120, 130, 255)
DIM = (200, 200, 210, 255)

FONT_BOLD = "/System/Library/Fonts/Helvetica.ttc"
FONT_REGULAR = "/System/Library/Fonts/Helvetica.ttc"

def load_secrets():
    s = {}
    with open(os.path.expanduser("~/.openclaw/.secrets")) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[7:]
            p = line.split("=", 1)
            if len(p) == 2: s[p[0]] = p[1].strip('"').strip("'")
    return s

def load_review(slug):
    with open(REVIEWS_PATH) as f:
        data = json.load(f)
    reviews = data if isinstance(data, list) else data.get("reviews", list(data.values()))
    for r in reviews:
        if isinstance(r, dict) and r.get("slug") == slug:
            return r
    raise ValueError(f"Not found: {slug}")

def extract_scores(review):
    woke_score = review.get("wokeScore", 0)
    trad_score = review.get("tradScore", 0)
    margin_str = str(review.get("scoreMargin", ""))
    margin_num = 0
    parts = margin_str.split()
    if parts:
        try: margin_num = int(parts[0])
        except: pass
    return {
        "wokeScore": woke_score, "tradScore": trad_score,
        "margin": margin_num, "marginStr": margin_str,
        "verdict": review.get("verdict", ""),
    }

def build_script(review, scores):
    title = review.get("title", "")
    woke_trap = review.get("wokeTrap", False)
    if isinstance(woke_trap, dict): woke_trap = woke_trap.get("is_trap", False)
    ms = scores["marginStr"]
    lines = []
    lines.append(f"{title}. {ms} on the VirtueVigil woke scale.")
    if woke_trap:
        lines.append("This is a woke trap. Here's what the Academy didn't want you to notice.")
    lines.append(f"The woke score is {scores['wokeScore']}. The traditional score is only {scores['tradScore']}. That is a margin of {ms}.")
    if woke_trap:
        wta = review.get("woke_trap_assessment", {})
        if isinstance(wta, dict):
            expl = wta.get("explanation", "")[:200]
        else:
            expl = ""
        if expl:
            lines.append(f"The trap: {expl}")
    lines.append(f"Verdict: {scores['verdict']}. Full review at virtuevigil.com.")
    lines.append("Subscribe for more woke content reviews.")
    return lines

def generate_tts(lines, out_path, secrets):
    text = " ".join(lines)
    print(f"  🎙️  TTS: {len(text)} chars")
    api_key = secrets.get("OPENAI_API_KEY", "")
    if not api_key:
        print("  ⚠️  No API key, generating silent audio")
        subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                        "-t", "45", "-c:a", "aac", str(out_path)], capture_output=True)
        return True
    url = "https://api.openai.com/v1/audio/speech"
    body = json.dumps({
        "model": "tts-1", "input": text, "voice": "nova", "speed": 1.1
    }).encode()
    req = Request(url, data=body, headers={
        "Authorization": f"Bearer {api_key}", "Content-Type": "application/json"
    })
    try:
        with urlopen(req, timeout=90) as resp:
            with open(out_path, "wb") as f:
                f.write(resp.read())
        print(f"  ✅ TTS saved")
        return True
    except HTTPError as e:
        print(f"  ⚠️  TTS failed: {e.code}")
        return False

def get_audio_duration(path):
    if not path.exists(): return 45.0
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", path],
                       capture_output=True, text=True)
    return float(r.stdout.strip())

def make_key_frame(review, scores, phase, text_line, output_path):
    """Generate a single key frame image."""
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Poster background
    poster_path = REPO / f"src{review['poster']}"
    if poster_path.exists():
        poster = Image.open(poster_path).convert("RGBA").resize((WIDTH, int(WIDTH * 1.4)), Image.LANCZOS)
        overlay = Image.new("RGBA", poster.size, (0, 0, 0, 160))
        poster = Image.alpha_composite(poster, overlay)
        img.paste(poster, ((WIDTH - poster.width) // 2, -50), poster)

    # Dark gradient overlay
    shade = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 100))
    img.paste(shade, (0, 0), shade)

    try:
        fb = ImageFont.truetype(FONT_BOLD, 72)
        fl = ImageFont.truetype(FONT_BOLD, 96)
        fr = ImageFont.truetype(FONT_REGULAR, 36)
        fs = ImageFont.truetype(FONT_REGULAR, 28)
    except:
        fb = fl = fr = fs = ImageFont.load_default()

    title = review.get("title", "")
    ms = scores["marginStr"]
    color = RED if "WOKE" in ms or "-" in ms else GREEN

    # Phase-specific
    if phase == "hook":
        bbox = draw.textbbox((0, 0), ms, font=fl)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw.text((x, 300), ms, font=fl, fill=color)
        bbox = draw.textbbox((0, 0), title, font=fb)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw.text((x, 450), title, font=fb, fill=WHITE)
        draw.text((60, 580), "WOKE CONTENT REVIEW", font=fr, fill=GOLD)

    elif phase == "scores":
        ws = scores["wokeScore"]
        ts = scores["tradScore"]
        draw.text((60, 200), "SCORE BREAKDOWN", font=fb, fill=GOLD)
        draw.text((60, 320), "WOKE", font=fb, fill=RED)
        bar_w = int((WIDTH - 250) * (ws / max(ws, ts, 1)))
        draw.rectangle([(60, 390), (60 + bar_w, 440)], fill=RED)
        draw.text((60 + bar_w + 20, 385), str(ws), font=fb, fill=WHITE)
        draw.text((60, 500), "TRADITIONAL", font=fb, fill=GREEN)
        bar_w2 = int((WIDTH - 250) * (ts / max(ws, ts, 1)))
        draw.rectangle([(60, 570), (60 + bar_w2, 620)], fill=GREEN)
        draw.text((60 + bar_w2 + 20, 565), str(ts), font=fb, fill=WHITE)
        draw.text((60, 700), f"MARGIN: {ms}", font=fb, fill=GOLD)

    elif phase == "trap":
        wt = review.get("wokeTrap", False)
        if isinstance(wt, dict): wt = wt.get("is_trap", False)
        if wt:
            draw.text((60, 300), "⚠️  WOKE TRAP", font=fl, fill=RED)
            draw.text((60, 440), "This film hides its ideological", font=fb, fill=WHITE)
            draw.text((60, 520), "content until you're invested.", font=fb, fill=WHITE)
        else:
            draw.text((60, 400), "NO WOKE TRAP", font=fl, fill=GREEN)

    elif phase == "verdict":
        v = scores["verdict"]
        vc = RED if "WOKE" in v.upper() else GREEN
        draw.text((60, 250), "VERDICT", font=fb, fill=GRAY)
        bbox = draw.textbbox((0, 0), v, font=fl)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw.text((x, 370), v, font=fl, fill=vc)
        bbox = draw.textbbox((0, 0), ms, font=fb)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw.text((x, 500), ms, font=fb, fill=WHITE)
        draw.text((60, 620), "Full review at virtuevigil.com", font=fr, fill=GOLD)
        draw.text((60, 680), "Subscribe for more reviews", font=fr, fill=DIM)

    elif phase == "cta":
        draw.text((60, 350), "Did you watch this?", font=fl, fill=WHITE)
        draw.text((60, 480), "Comment your take below.", font=fb, fill=DIM)
        draw.text((60, 600), "Subscribe for more", font=fr, fill=GOLD)
        draw.text((60, 660), "virtuevigil.com", font=fr, fill=DIM)

    # Logo watermark
    draw.text((40, HEIGHT - 80), "VIRTUEVIGIL", font=fs, fill=(255, 255, 255, 60))

    img = img.convert("RGB")
    img.save(output_path, "JPEG", quality=85)
    return output_path

def build_ffmpeg_filter(phases, audio_dur):
    """Build FFmpeg filter_complex string for crossfading between key frames."""
    # phases: [(name, duration_sec, frame_path), ...]
    # We'll use concatenation with crossfade via xfade filter

    inputs = " ".join(f'-loop 1 -t {d} -i "{p}"' for _, d, p in phases)
    total_inputs = len(phases)

    # Build crossfade chain
    parts = []
    for i in range(total_inputs):
        parts.append(f"[{i}:v]fps={FPS},scale={WIDTH}:{HEIGHT},setsar=1[v{i}]")

    # Crossfade between each pair
    fade_dur = 0.5  # half-second crossfade
    current = "[v0]"
    if total_inputs == 1:
        return inputs, current, None

    # Actually, let's use concat with a simpler approach: just fade to black between segments
    segment_parts = []
    for i in range(total_inputs):
        seg_dur = phases[i][1]
        if i < total_inputs - 1:
            # Fade out at end
            seg_dur_actual = seg_dur + fade_dur
            segment_parts.append(f"[v{i}]trim=0:{seg_dur},fade=out:st={seg_dur - fade_dur}:d={fade_dur}[s{i}]")
        else:
            segment_parts.append(f"[v{i}]trim=0:{seg_dur}[s{i}]")

    concat_inputs = "".join(f"[s{i}]" for i in range(total_inputs))
    concat = f"{''.join(segment_parts)}{concat_inputs}concat=n={total_inputs}:v=1:a=0[outv]"

    filter_complex = ";".join([";".join(parts), concat])
    return inputs, filter_complex, "[outv]"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--skip-tts", action="store_true")
    parser.add_argument("--skip-frames", action="store_true")
    args = parser.parse_args()

    for d in [OUTPUT_DIR, FRAMES_DIR, AUDIO_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    print(f"🎬 VV Short Builder — {args.slug}")

    review = load_review(args.slug)
    scores = extract_scores(review)
    print(f"  📋 {review['title']} | {scores['marginStr']} | {scores['verdict']}")

    # Build script & TTS
    lines = build_script(review, scores)
    audio_path = AUDIO_DIR / f"{args.slug}.m4a"

    if not args.skip_tts:
        secrets = load_secrets()
        generate_tts(lines, audio_path, secrets)

    audio_dur = get_audio_duration(audio_path)
    print(f"  ⏱️  Audio: {audio_dur:.1f}s")

    if not args.skip_frames:
        # Clear old
        for f in FRAMES_DIR.glob("*.jpg"):
            f.unlink()

        # Define phases and their durations
        total = audio_dur
        phases = [
            ("hook", total * 0.15),
            ("scores", total * 0.25),
            ("trap", total * 0.20),
            ("verdict", total * 0.25),
            ("cta", total * 0.15),
        ]

        # Generate key frames
        print(f"  🎨 Generating {len(phases)} key frames...")
        frame_paths = []
        for i, (phase, dur) in enumerate(phases):
            fp = FRAMES_DIR / f"key_{i:02d}_{phase}.jpg"
            make_key_frame(review, scores, phase, "", fp)
            frame_paths.append((phase, dur, fp))
            print(f"     {phase}: {fp.name} ({dur:.1f}s)")
    else:
        # Rebuild from existing frames
        frame_paths = []
        for fp in sorted(FRAMES_DIR.glob("key_*.jpg")):
            phase = fp.stem.split("_", 2)[-1]
            frame_paths.append((phase, audio_dur / 5, fp))

    # Build FFmpeg command
    output_path = OUTPUT_DIR / f"{args.slug}-short.mp4"

    # Simple approach: concat key frames with fade, then loop audio
    print(f"  🎥 Compositing...")

    # Generate concat file
    concat_file = FRAMES_DIR / "concat.txt"
    with open(concat_file, "w") as f:
        for phase, dur, fp in frame_paths:
            f.write(f"file '{fp.absolute()}'\n")
            f.write(f"duration {dur}\n")
        # Last frame needs to be repeated so concat doesn't skip it
        last = frame_paths[-1]
        f.write(f"file '{last[2].absolute()}'\n")

    # Build simple concat filter with fade transitions
    n = len(frame_paths)
    filter_parts = []

    # Scale and set fps for each input
    for i in range(n):
        filter_parts.append(f"[{i}:v]scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,crop={WIDTH}:{HEIGHT},setsar=1,fps={FPS}[v{i}]")

    # Concat with fade transitions (fade out prev + fade in next)
    concat_inputs = ""
    for i in range(n):
        dur = frame_paths[i][1]
        filter_parts.append(f"[v{i}]trim=0:{dur},fade=in:st=0:d=0.5,fade=out:st={dur - 0.5}:d=0.5[f{i}]")
        concat_inputs += f"[f{i}]"

    filter_parts.append(f"{concat_inputs}concat=n={n}:v=1:a=0[outv]")
    filter_complex = ";".join(filter_parts)

    # Construct input args
    input_args = []
    for phase, dur, fp in frame_paths:
        input_args.extend(["-loop", "1", "-t", str(dur), "-i", str(fp)])

    cmd = [
        "ffmpeg", "-y",
        *input_args,
        "-i", str(audio_path),
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-map", f"{n}:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        "-movflags", "+faststart",
        str(output_path)
    ]

    print(f"  🎬 Running FFmpeg...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"  ✅ Done! {output_path} ({size_mb:.1f} MB)")
    else:
        print(f"  ❌ FFmpeg failed:\n{result.stderr[-800:]}")
        return 1

    print(f"\n🎉 Short ready: {output_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())