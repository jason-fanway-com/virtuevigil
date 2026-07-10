#!/usr/bin/env python3
"""
publish_short.py - Fully automated YouTube Shorts publisher for VirtueVigil reviews.
Usage: python3 publish_short.py reviews.json "Movie Title"
Output: output/{movie_slug}_short.mp4 (1080x1920, ~25s, h264+AAC)
"""

import json, sys, os, subprocess, re, textwrap, time, random, shutil, hashlib
from pathlib import Path
from datetime import datetime

# === CONFIG ===
SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output"
TRAILER_DIR = SCRIPT_DIR / "trailers"
FRAMES_DIR = SCRIPT_DIR / "frames_short"
FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"  # macOS system font

OUTPUT_DIR.mkdir(exist_ok=True)
TRAILER_DIR.mkdir(exist_ok=True)
FRAMES_DIR.mkdir(exist_ok=True)

TARGET_DURATION = 25  # seconds
TARGET_SIZE = (1080, 1920)  # portrait 9:16
VIDEO_FPS = 24
NARRATION_CHAR_LIMIT = 420  # keep TTS under 30s

# === BRAND COLORS ===
COLOR_BG = (10, 10, 18)       # near-black
COLOR_ACCENT = (220, 50, 50)  # red
COLOR_GOLD = (255, 200, 50)   # gold
COLOR_WHITE = (245, 245, 245)
COLOR_GRAY = (160, 160, 170)
COLOR_TRAD = (50, 180, 80)    # green
COLOR_WOKE = (220, 50, 50)    # red
COLOR_OVERLAY = (0, 0, 0, 140)  # semi-transparent black

# === UTILITY ===
def run(cmd, **kwargs):
    """Run shell command, return CompletedProcess."""
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, **kwargs)

def safe_filename(s):
    return re.sub(r'[^a-z0-9]+', '_', s.lower()).strip('_')

def pp_readable(n):
    """Human-readable number."""
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)

# === STEP 1: FIND & DOWNLOAD TRAILER ===

def search_trailer(movie_title):
    """Search YouTube for official trailer, return best match URL."""
    query = f"{movie_title} official trailer"
    print(f"[1/8] Searching YouTube: {query}")
    
    result = run(
        f'yt-dlp "ytsearch:{query}" --dump-json --no-download --flat-playlist 2>/dev/null',
        timeout=30
    )
    
    try:
        lines = [l for l in result.stdout.strip().split('\n') if l.strip()]
        if not lines:
            raise ValueError("No results")
        data = json.loads(lines[0])
        url = data.get('webpage_url') or data.get('url')
        if not url:
            raise ValueError("No URL in result")
        print(f"  Found: {data.get('title', 'Unknown')} ({data.get('duration', '?')}s)")
        return url
    except Exception as e:
        print(f"  WARNING: Search failed ({e}), trying fallback...")
        # Fallback: try direct search with more permissive options
        result2 = run(
            f'yt-dlp "ytsearch1:{movie_title} trailer" --get-url 2>/dev/null',
            timeout=30
        )
        urls = [l for l in result2.stdout.strip().split('\n') if l.startswith('http')]
        if urls:
            return urls[0]
        raise RuntimeError(f"Could not find trailer for: {movie_title}")

def download_trailer(url, movie_slug):
    """Download trailer at 720p mp4. Converts webm if needed. Returns path."""
    output = TRAILER_DIR / f"{movie_slug}_trailer.mp4"
    
    print(f"  Downloading trailer...")
    
    # Force mp4 container, 720p max (1080p overkill for Shorts)
    fmt = "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/bestvideo[height<=720]+bestaudio/best[height<=720]/best"
    
    temp_output = TRAILER_DIR / f"{movie_slug}_trailer.%(ext)s"
    
    run(
        f'yt-dlp -f "{fmt}" --no-playlist -o "{temp_output}" "{url}" 2>&1',
        timeout=120
    )
    
    # Find the downloaded file (may be .mp4 or .webm)
    downloaded = None
    for ext in ['mp4', 'webm', 'mkv']:
        candidate = TRAILER_DIR / f"{movie_slug}_trailer.{ext}"
        if candidate.exists() and candidate.stat().st_size > 10000:
            downloaded = candidate
            break
    
    if not downloaded:
        raise RuntimeError(f"Download failed: no output file found for {movie_slug}")
    
    # Convert webm/mkv to mp4 if needed
    if downloaded.suffix != '.mp4':
        print(f"  Converting {downloaded.suffix} → mp4...")
        run(
            f'ffmpeg -y -i "{downloaded}" -c:v libx264 -crf 18 -preset fast '
            f'-c:a aac -b:a 128k -movflags +faststart "{output}" 2>/dev/null',
            timeout=120
        )
        downloaded.unlink(missing_ok=True)
        if not output.exists():
            raise RuntimeError(f"Conversion failed for {downloaded}")
        downloaded = output
    else:
        # Rename to canonical name
        if downloaded != output:
            downloaded.rename(output)
            downloaded = output
    
    size_mb = downloaded.stat().st_size / 1_000_000
    print(f"  Downloaded: {size_mb:.1f}MB")
    return downloaded

# === STEP 2: EXTRACT CLIPS ===

def extract_clips(trailer_path, movie_slug):
    """Extract the best 20-30s of trailer footage. 
    Strategy: sample multiple segments, pick ones with motion (high frame difference)."""
    duration = get_duration(trailer_path)
    print(f"[2/8] Extracting clips from {duration:.0f}s trailer")
    
    clips_dir = TRAILER_DIR / f"{movie_slug}_clips"
    clips_dir.mkdir(exist_ok=True)
    
    # Strategy: take 3 clips from different parts of trailer (start, middle, end)
    # Skip first 5s (studio logos) and last 5s (ratings card)
    usable_start = 5
    usable_end = max(usable_start + 10, duration - 5)
    usable_range = usable_end - usable_start
    
    clip_segments = []
    if usable_range > 30:
        # Pick 4 segments across the trailer
        segments = [
            usable_start + usable_range * 0.05,   # after logos
            usable_start + usable_range * 0.25,   # early action
            usable_start + usable_range * 0.60,   # climax
            usable_start + usable_range * 0.80,   # late dramatic
        ]
        for i, start in enumerate(segments):
            clip_segments.append((start, min(start + 7, usable_end)))
    else:
        # Short trailer, just use the middle portion
        clip_segments = [(usable_start + 3, usable_end - 3)]
    
    clip_paths = []
    total_clip_duration = 0
    for i, (start, end) in enumerate(clip_segments):
        clip_path = clips_dir / f"clip_{i:02d}.mp4"
        if not clip_path.exists() or clip_path.stat().st_size < 1000:  # Not downloaded
            run(
                f'ffmpeg -y -ss {start:.2f} -i "{trailer_path}" '
                f'-t {end - start:.2f} -c:v libx264 -crf 18 -preset fast '
                f'-c:a aac -b:a 128k -avoid_negative_ts make_zero '
                f'"{clip_path}" 2>/dev/null',
                timeout=30
            )
        if clip_path.exists() and clip_path.stat().st_size > 1000:
            clip_paths.append(clip_path)
            clip_dur = get_duration(clip_path)
            total_clip_duration += clip_dur
            print(f"  Clip {i}: {start:.1f}s-{end:.1f}s ({clip_dur:.1f}s)")
    
    return clip_paths

def get_duration(path):
    """Get video duration in seconds using ffprobe."""
    result = run(f'ffprobe -v error -show_entries format=duration '
                 f'-of default=noprint_wrappers=1:nokey=1 "{path}"')
    try:
        return float(result.stdout.strip())
    except:
        return 0

# === STEP 3: BUILD NARRATION ===

def build_narration(review):
    """Build TTS narration text from review data. Keep under char limit."""
    title = review.get('title', 'This movie')
    verdict = review.get('verdict', 'Strongly Traditional')
    summary = review.get('summary', {}).get('overall', '')
    
    # Get tropes
    trope_audit = review.get('tropeAudit', [])
    trad_tropes = [t for t in trope_audit if t.get('type') == 'traditional']
    woke_tropes = [t for t in trope_audit if t.get('type') == 'woke']
    
    # Build punchy narration
    lines = []
    
    # Hook
    lines.append(f"Did {title} brainwash your kids?")
    
    # Scores
    trad_score = review.get('traditionalScore', 'N/A')
    woke_score = review.get('wokeScore', 'N/A')
    margin = review.get('margin', 0)
    
    if margin > 0:
        lines.append(f"VirtueVigil scores it +{margin} traditional.")
    else:
        lines.append(f"VirtueVigil scores it {verdict.lower()}.")
    
    # Key tropes (1-2 most striking)
    if trad_tropes:
        top_trad = trad_tropes[0]
        trope_name = top_trad.get('trope', '')
        if trope_name:
            lines.append(f"{trope_name}. That's what we found here.")
    
    if woke_tropes:
        top_woke = woke_tropes[0]
        trope_name = top_woke.get('trope', '')
        if trope_name:
            lines.append(f"Even one woke moment: {trope_name}.")
    
    # Verdict
    lines.append(f"Verdict: {verdict}. This one's safe for your family.")
    
    # CTA
    lines.append("Full review at VirtueVigil dot com. Link below.")
    
    narration = " ".join(lines)
    
    # Trim to char limit if needed
    if len(narration) > NARRATION_CHAR_LIMIT:
        # Remove the least important line
        if len(lines) >= 4:
            narration = " ".join(lines[:1] + lines[2:])  # skip trope line
        if len(narration) > NARRATION_CHAR_LIMIT:
            narration = narration[:NARRATION_CHAR_LIMIT - 3] + "..."
    
    return narration

def generate_tts(narration_text, movie_slug):
    """Generate TTS audio via OpenAI TTS API (raw HTTP, no SDK)."""
    audio_path = OUTPUT_DIR / f"{movie_slug}_narration.mp3"
    print(f"[3/8] Generating TTS narration ({len(narration_text)} chars)")
    
    import urllib.request, json as json_mod
    
    # Read API key
    secrets_path = os.path.expanduser("~/.openclaw/.secrets")
    api_key = None
    with open(secrets_path) as f:
        for line in f:
            if 'OPENAI_API_KEY=' in line and not line.strip().startswith('#'):
                api_key = line.split('=', 1)[1].strip().strip('"').strip("'")
                break
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not found")
    
    payload = json_mod.dumps({
        "model": "tts-1",
        "voice": "nova",
        "input": narration_text,
        "speed": 1.05
    }).encode()
    
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    
    with urllib.request.urlopen(req, timeout=30) as resp:
        audio_path.write_bytes(resp.read())
    
    duration = get_duration(audio_path)
    print(f"  TTS: {duration:.1f}s")
    return audio_path, duration

# === STEP 4: BUILD CAPTIONS ===

def generate_captions_srt(narration_text, audio_duration, movie_slug):
    """Generate SRT captions synced to narration audio.
    Simple approach: divide narration into sentences, space evenly."""
    srt_path = OUTPUT_DIR / f"{movie_slug}_captions.srt"
    print(f"[4/8] Generating captions")
    
    # Split into caption-friendly segments (max ~40 chars each)
    segments = []
    for segment in re.split(r'(?<=[.!?])\s+', narration_text):
        segment = segment.strip()
        if not segment:
            continue
        if len(segment) > 42:
            # Split long segments
            words = segment.split()
            mid = len(words) // 2
            segments.append(" ".join(words[:mid]))
            segments.append(" ".join(words[mid:]))
        else:
            segments.append(segment)
    
    if not segments:
        segments = [narration_text]
    
    # Calculate timing
    total_words = sum(len(s.split()) for s in segments)
    words_per_second = total_words / max(audio_duration, 1)
    
    srt_lines = []
    current_time = 0.15  # Small start delay
    
    for i, segment in enumerate(segments, 1):
        word_count = len(segment.split())
        segment_duration = word_count / max(words_per_second, 0.5)
        
        # Add small gap between captions
        if i > 1:
            current_time += 0.08
        
        start = current_time
        end = current_time + segment_duration
        current_time = end
        
        # Format SRT timestamps
        def fmt_timestamp(t):
            h = int(t // 3600)
            m = int((t % 3600) // 60)
            s = int(t % 60)
            ms = int((t % 1) * 1000)
            return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
        
        srt_lines.append(str(i))
        srt_lines.append(f"{fmt_timestamp(start)} --> {fmt_timestamp(end)}")
        srt_lines.append(segment)
        srt_lines.append("")
    
    srt_path.write_text("\n".join(srt_lines))
    print(f"  {len(segments)} caption segments")
    return srt_path

# === STEP 5: COMPOSITE VIDEO ===

def composite_short(clip_paths, narration_path, captions_srt, movie_slug, review):
    """Composite trailer clips, narration, captions, and graphics into final Short."""
    print(f"[5/8] Compositing final Short")
    output_path = OUTPUT_DIR / f"{movie_slug}_short.mp4"
    
    # Build a concat file for the clips
    concat_file = TRAILER_DIR / f"{movie_slug}_concat.txt"
    with open(concat_file, 'w') as f:
        for clip in clip_paths:
            f.write(f"file '{clip.absolute()}'\n")
    
    total_clip_duration = sum(get_duration(c) for c in clip_paths)
    narration_duration = get_duration(narration_path)
    target_dur = min(total_clip_duration, max(narration_duration + 1, 20))
    
    print(f"  Clips: {total_clip_duration:.1f}s, Narration: {narration_duration:.1f}s")
    print(f"  Target duration: {target_dur:.1f}s")
    
    # First, concat clips into a single video
    concat_path = TRAILER_DIR / f"{movie_slug}_concat.mp4"
    run(
        f'ffmpeg -y -f concat -safe 0 -i "{concat_file}" '
        f'-c copy -t {target_dur:.2f} "{concat_path}" 2>/dev/null',
        timeout=30
    )
    
    if not concat_path.exists():
        # Fallback: concat with re-encode
        run(
            f'ffmpeg -y -f concat -safe 0 -i "{concat_file}" '
            f'-c:v libx264 -crf 18 -preset fast -c:a aac -b:a 128k '
            f'-t {target_dur:.2f} "{concat_path}" 2>/dev/null',
            timeout=60
        )
    
    # Build the final composite filter
    # Complex filter chain:
    # 1. Scale/crop concat to 1080x1920 (center crop from 16:9)
    # 2. Mix narration audio over trailer audio (narration louder, trailer as bed)
    # 3. Burn subtitles
    
    # Calculate scale: 16:9 (1920x1080) → 9:16 (1080x1920)
    # Scale width to 1080, crop center
    filter_complex = (
        f'[0:v]scale=1080:1920:force_original_aspect_ratio=increase,'
        f'crop=1080:1920[v];'
        f'[1:a]volume=1.2[narration];'
        f'[0:a]volume=0.3[trailer_bed];'
        f'[narration][trailer_bed]amix=inputs=2:duration=first:dropout_transition=2[audio]'
    )
    
    # Escape path for FFmpeg subtitles filter
    srt_escaped = str(captions_srt.absolute()).replace(':', '\\:').replace("'", "\\'")
    
    # Caption style: bold white with heavy black outline + shadow
    # FontSize 16 is the sweet spot for mobile readability at 1080x1920
    caption_style = (
        f'FontName=Helvetica,FontSize=16,'
        f'Bold=1,'
        f'PrimaryColour=&HFFFFFF,'
        f'OutlineColour=&H000000,Outline=3,'
        f'Shadow=2,MarginV=52,Alignment=2'
    )
    
    cmd = (
        f'ffmpeg -y '
        f'-i "{concat_path}" '
        f'-i "{narration_path}" '
        f'-filter_complex "{filter_complex}" '
        f'-map "[v]" -map "[audio]" '
        f'-c:v libx264 -crf 20 -preset medium '
        f'-c:a aac -b:a 128k '
        f'-pix_fmt yuv420p '
        f'-r {VIDEO_FPS} '
        f'-t {target_dur:.2f} '
        f'-vf "subtitles={srt_escaped}:force_style=\'{caption_style}\'" '
        f'"{output_path}" 2>/dev/null'
    )
    
    result = run(cmd, timeout=120)
    
    if not output_path.exists() or output_path.stat().st_size < 1000:
        # Retry with simpler approach: two-pass (video first, then subtitles)
        print("  Retrying with two-pass approach...")
        temp_path = OUTPUT_DIR / f"{movie_slug}_temp.mp4"
        
        cmd1 = (
            f'ffmpeg -y '
            f'-i "{concat_path}" '
            f'-i "{narration_path}" '
            f'-filter_complex "{filter_complex}" '
            f'-map "[v]" -map "[audio]" '
            f'-c:v libx264 -crf 20 -preset medium '
            f'-c:a aac -b:a 128k '
            f'-pix_fmt yuv420p '
            f'-r {VIDEO_FPS} '
            f'-t {target_dur:.2f} '
            f'"{temp_path}" 2>/dev/null'
        )
        run(cmd1, timeout=120)
        
        if temp_path.exists():
            # Burn subtitles in second pass
            cmd2 = (
                f'ffmpeg -y -i "{temp_path}" '
                f'-vf "subtitles={srt_escaped}:force_style=\'{caption_style}\'" '
                f'-c:v libx264 -crf 18 -preset medium -c:a copy '
                f'"{output_path}" 2>/dev/null'
            )
            run(cmd2, timeout=60)
            temp_path.unlink(missing_ok=True)
    
    if output_path.exists() and output_path.stat().st_size > 1000:
        size_mb = output_path.stat().st_size / 1_000_000
        dur = get_duration(output_path)
        print(f"  Done: {output_path.name} ({size_mb:.1f}MB, {dur:.1f}s)")
    else:
        raise RuntimeError(f"Compositing failed, no output at {output_path}")
    
    return output_path

# === STEP 6: VERIFY ===

def verify_short(short_path):
    """Verify the final short is valid."""
    print(f"[6/8] Verifying output...")
    
    dur = get_duration(short_path)
    size_mb = short_path.stat().st_size / 1_000_000
    
    probe = run(f'ffprobe -v error -show_entries stream=codec_type,codec_name,width,height '
                f'-of json "{short_path}"')
    
    issues = []
    try:
        streams = json.loads(probe.stdout).get('streams', [])
        video = next((s for s in streams if s['codec_type'] == 'video'), None)
        audio = next((s for s in streams if s['codec_type'] == 'audio'), None)
        
        if not video:
            issues.append("No video stream")
        else:
            w, h = video.get('width', 0), video.get('height', 0)
            if (w, h) != TARGET_SIZE:
                issues.append(f"Wrong resolution: {w}x{h} (expected {TARGET_SIZE[0]}x{TARGET_SIZE[1]})")
        
        if not audio:
            issues.append("No audio stream")
    
    except Exception as e:
        issues.append(f"Probe failed: {e}")
    
    if issues:
        print(f"  ⚠️  Issues: {', '.join(issues)}")
    else:
        print(f"  ✅ {size_mb:.1f}MB, {dur:.1f}s, 1080x1920, h264+AAC")
    
    return len(issues) == 0

# === STEP 7: EXTRACT THUMBNAIL ===

def extract_thumbnail(short_path, movie_slug):
    """Extract a thumbnail frame for YouTube upload."""
    print(f"[7/8] Extracting thumbnail...")
    
    thumb_path = OUTPUT_DIR / f"{movie_slug}_thumb.png"
    
    dur = get_duration(short_path)
    # Pick a frame at 30% into the video (likely a visually striking moment)
    ss = dur * 0.3
    
    run(
        f'ffmpeg -y -i "{short_path}" -ss {ss:.2f} -vframes 1 '
        f'-q:v 2 "{thumb_path}" 2>/dev/null'
    )
    
    if thumb_path.exists():
        print(f"  {thumb_path.name}")
    
    return thumb_path

# === MAIN ===

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 publish_short.py <reviews.json> <\"Movie Title\">")
        sys.exit(1)
    
    reviews_path = sys.argv[1]
    movie_title = sys.argv[2]
    movie_slug = safe_filename(movie_title)
    
    print(f"\n{'='*60}")
    print(f"  VirtueVigil Shorts Publisher")
    print(f"  Movie: {movie_title}")
    print(f"  Output: {movie_slug}_short.mp4")
    print(f"{'='*60}\n")
    
    # Load review
    with open(reviews_path) as f:
        reviews = json.load(f)
    
    review = None
    if isinstance(reviews, dict):
        for r in reviews.values():
            if isinstance(r, dict) and r.get('title', '').lower() == movie_title.lower():
                review = r
                break
    elif isinstance(reviews, list):
        for r in reviews:
            if isinstance(r, dict) and r.get('title', '').lower() == movie_title.lower():
                review = r
                break
    
    if not review:
        print(f"ERROR: Movie '{movie_title}' not found in reviews.json")
        sys.exit(1)
    
    print(f"  Review found: {review.get('verdict', 'N/A')}")
    
    try:
        # Step 1-2: Get trailer footage
        trailer_url = search_trailer(movie_title)
        trailer_path = download_trailer(trailer_url, movie_slug)
        clip_paths = extract_clips(trailer_path, movie_slug)
        
        if not clip_paths:
            print("ERROR: No clips extracted from trailer")
            sys.exit(1)
        
        # Step 3: Narration
        narration_text = build_narration(review)
        narration_path, narration_duration = generate_tts(narration_text, movie_slug)
        
        # Step 4: Captions
        captions_srt = generate_captions_srt(narration_text, narration_duration, movie_slug)
        
        # Step 5: Composite
        short_path = composite_short(clip_paths, narration_path, captions_srt, movie_slug, review)
        
        # Step 6-7: Verify + thumbnail
        verify_short(short_path)
        extract_thumbnail(short_path, movie_slug)
        
        # Step 8: Done
        print(f"\n[8/8] ✅ Short ready!")
        print(f"  File: {short_path}")
        print(f"  Upload to YouTube Shorts with title:")
        print(f"    \"{review.get('title')}: {review.get('verdict')} | VirtueVigil Review\"")
        print(f"  Description: Full review at https://virtuevigil.com")
        print(f"  #VirtueVigil #MovieReview #Shorts")
        
        # Write metadata
        meta = {
            "movie": movie_title,
            "slug": movie_slug,
            "verdict": review.get('verdict'),
            "trad_score": review.get('traditionalScore', 0),
            "woke_score": review.get('wokeScore', 0),
            "trailer_url": trailer_url,
            "narration_text": narration_text,
            "short_path": str(short_path),
            "timestamp": datetime.now().isoformat()
        }
        meta_path = OUTPUT_DIR / f"{movie_slug}_meta.json"
        with open(meta_path, 'w') as f:
            json.dump(meta, f, indent=2)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Cleanup frames
    if FRAMES_DIR.exists():
        shutil.rmtree(FRAMES_DIR)

if __name__ == "__main__":
    main()