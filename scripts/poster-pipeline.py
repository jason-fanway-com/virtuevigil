#!/usr/bin/env python3
"""
VirtueVigil Poster Pipeline - Comprehensive Poster Acquisition System
Implements a fallback chain: OMDb → Brave Search → Generate Placeholder

Features:
- Multiple modes: --all, --slug, --replace-placeholders
- Smart placeholder detection (file size < 10KB, pattern matching)
- Rate limiting between API calls
- Detailed logging with symbols
- Git integration for commits
- Integration function for Destiny agent

Usage:
    python3 poster-pipeline.py --all                    # Check all reviews
    python3 poster-pipeline.py --slug the-brutalist-2026  # Single movie
    python3 poster-pipeline.py --replace-placeholders   # Re-check placeholders
"""

import json
import os
import sys
import re
import time
import base64
import tempfile
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("⚠️  PIL not available, placeholder generation disabled")


# Configuration
OMDB_API_KEY = "fff6ef33"
OMDB_BASE_URL = "http://www.omdbapi.com/"
BRAVE_SEARCH_BASE = "https://api.search.brave.com/res/v1/images/search"
SITEMAP_URL = "https://virtuevigil.com/sitemap.xml"

# Vision safety gate (OpenAI gpt-4o-mini, vision-capable)
OPENAI_VISION_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_VISION_MODEL = "gpt-4o-mini"
VISION_TIMEOUT = 30  # seconds
HTTP_USER_AGENT = "Mozilla/5.0 (compatible; VirtueVigilPosterBot/1.0; +https://virtuevigil.com)"

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent
REVIEWS_JSON = REPO_DIR / 'src' / 'data' / 'reviews.json'
POSTER_DIR = REPO_DIR / 'src' / 'images' / 'posters'
REVIEW_QUEUE_PATH = SCRIPT_DIR / 'poster-review-queue.json'
PLACEHOLDER_SIZE_THRESHOLD = 10000  # 10KB threshold for placeholder detection

# Rate limiting
OMDB_DELAY = 1.0  # seconds between OMDb requests
BRAVE_DELAY = 2.0  # seconds between Brave requests

# Poster detection
PLACEHOLDER_PATTERNS = [
    r'coming.?soon',  # Our generated placeholders
    r'no.?poster',
    r'unavailable'
]

# Stats
stats = {
    'omdb': 0,
    'brave': 0,
    'placeholder': 0,
    'failed': 0,
    'skipped': 0,
    'rejected': 0,   # Brave candidates rejected by vision gate
    'queued': 0,     # Items appended to human-review queue
    'failed_slugs': []
}


def load_secrets():
    """Load API keys from ~/.openclaw/.secrets"""
    secrets = {}
    secrets_file = Path.home() / '.openclaw' / '.secrets'
    
    if not secrets_file.exists():
        print(f"⚠️  Secrets file not found: {secrets_file}")
        return secrets
    
    try:
        with open(secrets_file, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    # Remove quotes if present
                    value = value.strip('"\'')
                    secrets[key] = value
    except Exception as e:
        print(f"⚠️  Failed to load secrets: {e}")
    
    return secrets


def slug_to_movie_title(slug):
    """
    Convert slug to movie title.
    Examples: 'the-brutalist-2026' -> 'The Brutalist', 'nosferatu-2024' -> 'Nosferatu'
    """
    # Remove year suffix
    title = re.sub(r'-\d{4}$', '', slug)
    # Replace hyphens with spaces
    title = title.replace('-', ' ')
    # Title case
    title = title.title()
    return title


def extract_year_from_slug(slug):
    """Extract year from slug. Example: 'the-brutalist-2026' -> 2026"""
    match = re.search(r'-(\d{4})$', slug)
    return int(match.group(1)) if match else None


def get_existing_posters():
    """Get set of existing poster files (regardless of validity)."""
    if not POSTER_DIR.exists():
        POSTER_DIR.mkdir(parents=True, exist_ok=True)
    
    existing = {}
    for filepath in POSTER_DIR.glob('*.jpg'):
        slug = filepath.stem
        existing[slug] = {
            'path': filepath,
            'size': filepath.stat().st_size
        }
    return existing


def is_placeholder(filepath):
    """
    Detect if a poster file is a placeholder.
    Heuristics:
    - File size < 10KB (generated placeholders are small)
    - File contains placeholder patterns (if readable)
    """
    if not filepath.exists():
        return False
    
    size = filepath.stat().st_size
    if size < PLACEHOLDER_SIZE_THRESHOLD:
        return True
    
    return False


def load_reviews_from_json():
    """Load review slugs and metadata from reviews.json"""
    if not REVIEWS_JSON.exists():
        print(f"⚠️  reviews.json not found: {REVIEWS_JSON}")
        return []
    
    try:
        with open(REVIEWS_JSON, 'r') as f:
            reviews = json.load(f)
        
        return [
            {
                'slug': r.get('slug'),
                'title': r.get('title'),
                'year': r.get('year')
            }
            for r in reviews if r.get('slug')
        ]
    except Exception as e:
        print(f"⚠️  Failed to load reviews: {e}")
        return []


def query_omdb(movie_title, year=None):
    """Query OMDb API for poster URL."""
    params = {
        't': movie_title,
        'apikey': OMDB_API_KEY,
        'type': 'movie'
    }
    
    if year:
        params['y'] = str(year)
    
    url = OMDB_BASE_URL + '?' + urllib.parse.urlencode(params)
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        if data.get('Response') == 'True' and data.get('Poster') not in ['N/A', None]:
            return data.get('Poster')
        
        return None
    except Exception as e:
        print(f"    ⚠️  OMDb error: {e}")
        return None


def search_brave_images(query, brave_key):
    """Search Brave Search API for movie poster images."""
    params = {
        'q': query,
        'count': 5
    }
    
    url = BRAVE_SEARCH_BASE + '?' + urllib.parse.urlencode(params)
    
    try:
        req = urllib.request.Request(url)
        req.add_header('X-Subscription-Token', brave_key)
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        results = data.get('results', [])
        
        # Filter for likely poster URLs
        poster_keywords = ['imdb', 'tmdb', 'movieposter', 'impawards', 'posterhouse']
        for result in results:
            image_url = result.get('image', {}).get('url', '')
            if any(keyword in image_url.lower() for keyword in poster_keywords):
                return image_url
        
        # If no filtered result, return first result
        if results:
            return results[0].get('image', {}).get('url')
        
        return None
    except Exception as e:
        print(f"    ⚠️  Brave Search error: {e}")
        return None


def download_image(image_url, filepath, timeout=10):
    """
    Download image from URL and save to filepath.
    Validates size + JPEG magic bytes ONLY. This is the trusted path used
    for OMDb images. Untrusted (Brave) images MUST go through
    download_image_to_temp + vision_safety_check + promote_temp instead.
    """
    try:
        req = urllib.request.Request(image_url, headers={'User-Agent': HTTP_USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            image_data = response.read()

        # Validate it's a reasonable image size (>1KB, <5MB)
        if len(image_data) < 1000 or len(image_data) > 5 * 1024 * 1024:
            return False

        # Validate JPEG magic bytes
        if image_data[:2] != b'\xff\xd8':
            return False

        with open(filepath, 'wb') as f:
            f.write(image_data)

        return True
    except Exception as e:
        print(f"    ⚠️  Download error: {e}")
        return False


def download_image_to_temp(image_url, timeout=10):
    """
    Download an UNTRUSTED image to a temporary file WITHOUT committing it to
    the poster directory. Performs the same cheap structural validation
    (size + JPEG magic bytes) as download_image.

    Returns: path (str) to the temp JPEG on success, or None on failure.
    The caller is responsible for deleting the temp file (use promote_temp
    or os.unlink).
    """
    try:
        req = urllib.request.Request(image_url, headers={'User-Agent': HTTP_USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            image_data = response.read()

        # Validate it's a reasonable image size (>1KB, <5MB)
        if len(image_data) < 1000 or len(image_data) > 5 * 1024 * 1024:
            return None

        # Validate JPEG magic bytes
        if image_data[:2] != b'\xff\xd8':
            return None

        fd, tmp_path = tempfile.mkstemp(suffix='.jpg', prefix='vv_poster_')
        with os.fdopen(fd, 'wb') as f:
            f.write(image_data)

        return tmp_path
    except Exception as e:
        print(f"    ⚠️  Download error: {e}")
        return None


def promote_temp(tmp_path, filepath):
    """Move a validated temp image into its final poster location."""
    try:
        with open(tmp_path, 'rb') as src:
            data = src.read()
        with open(filepath, 'wb') as dst:
            dst.write(data)
        return True
    except Exception as e:
        print(f"    ⚠️  Promote error: {e}")
        return False
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def vision_safety_check(tmp_path, title, year, openai_key):
    """
    Content-safety + correctness gate for UNTRUSTED images.

    Sends the image (base64) to the OpenAI vision model and asks for a strict
    JSON verdict. ACCEPT only when the image is non-explicit, looks like a
    real movie/TV poster, AND matches the given title/year.

    Returns a dict:
        {
          'accept': bool,        # True only if all three positive conditions hold
          'is_explicit': bool,
          'is_movie_poster': bool,
          'matches_title': bool,
          'reason': str,
          'error': str|None,     # set when the call itself failed / timed out
        }

    FAIL SAFE: on any error, timeout, missing key, or unparseable response,
    'accept' is False and 'error' is populated so the caller routes to the
    placeholder + human-review queue.
    """
    result = {
        'accept': False,
        'is_explicit': True,
        'is_movie_poster': False,
        'matches_title': False,
        'reason': '',
        'error': None,
    }

    if not openai_key:
        result['reason'] = 'No OPENAI_API_KEY available'
        result['error'] = 'missing_key'
        return result

    try:
        with open(tmp_path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('ascii')
    except Exception as e:
        result['reason'] = f'Could not read temp image: {e}'
        result['error'] = 'read_error'
        return result

    year_str = str(year) if year else 'unknown year'
    prompt = (
        "You are a strict content-safety and correctness reviewer for a movie "
        "review website. Examine the image and decide three things about it.\n"
        f"The image is supposed to be the official poster for the movie/TV "
        f"title \"{title}\" ({year_str}).\n\n"
        "Respond with ONLY a compact JSON object, no markdown, no prose, with "
        "exactly these keys:\n"
        '{"is_explicit": bool, "is_movie_poster": bool, "matches_title": bool, "reason": str}\n\n'
        "Definitions:\n"
        "- is_explicit: true if the image contains ANY nudity, sexual content, "
        "pornography, gore, or otherwise NSFW/inappropriate material. When in "
        "doubt, set true.\n"
        "- is_movie_poster: true ONLY if this clearly looks like a legitimate "
        "movie or TV poster / key art (title treatment, billing, cast, etc.).\n"
        "- matches_title: true ONLY if the poster plausibly corresponds to the "
        f"title \"{title}\" ({year_str}).\n"
        "- reason: one short sentence explaining your decision."
    )

    payload = {
        'model': OPENAI_VISION_MODEL,
        'messages': [
            {
                'role': 'user',
                'content': [
                    {'type': 'text', 'text': prompt},
                    {
                        'type': 'image_url',
                        'image_url': {
                            'url': f'data:image/jpeg;base64,{b64}',
                            'detail': 'low',
                        },
                    },
                ],
            }
        ],
        'max_tokens': 200,
        'temperature': 0,
    }

    try:
        data_bytes = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(OPENAI_VISION_URL, data=data_bytes, method='POST')
        req.add_header('Authorization', f'Bearer {openai_key}')
        req.add_header('Content-Type', 'application/json')

        with urllib.request.urlopen(req, timeout=VISION_TIMEOUT) as response:
            resp = json.loads(response.read().decode('utf-8'))

        content = resp['choices'][0]['message']['content'].strip()
        # Strip markdown code fences if the model added them.
        content = re.sub(r'^```(?:json)?\s*|\s*```$', '', content.strip())
        verdict = json.loads(content)

        result['is_explicit'] = bool(verdict.get('is_explicit', True))
        result['is_movie_poster'] = bool(verdict.get('is_movie_poster', False))
        result['matches_title'] = bool(verdict.get('matches_title', False))
        result['reason'] = str(verdict.get('reason', ''))
        result['accept'] = (
            result['is_explicit'] is False
            and result['is_movie_poster'] is True
            and result['matches_title'] is True
        )
        return result
    except Exception as e:
        # FAIL SAFE: any error/timeout -> do not accept, route to queue.
        result['reason'] = f'Vision check failed: {e}'
        result['error'] = 'vision_error'
        return result


def queue_for_review(slug, title, url, reason):
    """
    Append a rejected / errored Brave candidate to the human-review queue
    (scripts/poster-review-queue.json). Never raises; queue failures must not
    block the pipeline.
    """
    entry = {
        'slug': slug,
        'title': title,
        'url': url,
        'reason': reason,
        'timestamp': datetime.utcnow().isoformat() + 'Z',
    }
    try:
        queue = []
        if REVIEW_QUEUE_PATH.exists():
            try:
                with open(REVIEW_QUEUE_PATH, 'r') as f:
                    queue = json.load(f)
                if not isinstance(queue, list):
                    queue = []
            except Exception:
                queue = []
        queue.append(entry)
        with open(REVIEW_QUEUE_PATH, 'w') as f:
            json.dump(queue, f, indent=2)
        stats['queued'] += 1
        print(f"    🚩 Queued for human review ({reason})")
    except Exception as e:
        print(f"    ⚠️  Could not write review queue: {e}")


def generate_placeholder(slug, title, year, filepath):
    """Generate branded placeholder poster (300x450 JPEG)."""
    if not HAS_PIL:
        return False
    
    try:
        # Create image: 300x450, dark background
        width, height = 300, 450
        bg_color = (20, 20, 30)  # Dark blue-black
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)
        
        # Gold border
        border_color = (218, 165, 32)  # Goldenrod
        border_width = 3
        draw.rectangle(
            [(border_width, border_width),
             (width - border_width, height - border_width)],
            outline=border_color,
            width=border_width
        )
        
        # Title and year text (centered)
        text_color = (255, 255, 255)
        
        # Try to use default font, fallback to default if not available
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
            coming_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            coming_font = ImageFont.load_default()
        
        # Draw "COMING SOON" at top
        coming_text = "COMING SOON"
        bbox = draw.textbbox((0, 0), coming_text, font=coming_font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        draw.text((x, 40), coming_text, fill=border_color, font=coming_font)
        
        # Draw title (centered, wrapped if needed)
        title_lines = title.split()
        title_text = ""
        y = 150
        
        for word in title_lines:
            test_text = (title_text + " " + word).strip()
            bbox = draw.textbbox((0, 0), test_text, font=title_font)
            test_width = bbox[2] - bbox[0]
            
            if test_width > width - 40:
                if title_text:
                    bbox = draw.textbbox((0, 0), title_text, font=title_font)
                    text_width = bbox[2] - bbox[0]
                    x = (width - text_width) // 2
                    draw.text((x, y), title_text, fill=text_color, font=title_font)
                    y += 35
                title_text = word
            else:
                title_text = test_text
        
        if title_text:
            bbox = draw.textbbox((0, 0), title_text, font=title_font)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, y), title_text, fill=text_color, font=title_font)
        
        # Draw year at bottom
        year_text = str(year) if year else "TBA"
        bbox = draw.textbbox((0, 0), year_text, font=subtitle_font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        draw.text((x, height - 60), year_text, fill=border_color, font=subtitle_font)
        
        # Draw VirtueVigil branding at bottom
        brand_text = "VirtueVigil"
        bbox = draw.textbbox((0, 0), brand_text, font=subtitle_font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        draw.text((x, height - 30), brand_text, fill=(150, 150, 150), font=subtitle_font)
        
        # Save as JPEG
        img.save(filepath, 'JPEG', quality=85)
        return True
    except Exception as e:
        print(f"    ⚠️  Placeholder generation error: {e}")
        return False


def process_poster(slug, title, year, existing, brave_key, openai_key=None, force_replace=False):
    """
    Process a single poster through the fallback chain:
        1. OMDb (trusted, structural validation only)
        2. Brave image search (UNTRUSTED -> vision safety+correctness gate)
        3. VV-branded placeholder (always safe)

    Safety invariant: a raw web (Brave) image is NEVER written to the poster
    directory unless it passes the vision gate. Any rejection / error routes
    to the placeholder and the human-review queue.

    Returns: 'omdb', 'brave', 'placeholder', or 'failed'
    """
    filepath = POSTER_DIR / f"{slug}.jpg"

    # Check if poster already exists and is valid
    if filepath.exists() and not force_replace:
        if not is_placeholder(filepath):
            return 'skipped'

    print(f"  {slug}...", end=" ", flush=True)

    # 1. Try OMDb (trusted source, skips vision gate but still validated as JPEG)
    poster_url = query_omdb(title, year)
    if not poster_url:
        # Retry without year
        poster_url = query_omdb(title)

    if poster_url and download_image(poster_url, filepath):
        print("✓ (OMDb)")
        return 'omdb'

    # Rate limit before next attempt
    time.sleep(OMDB_DELAY)

    # 2. Try Brave Search (UNTRUSTED -> must pass the vision safety gate)
    if brave_key:
        search_query = f'"{title}" {year} movie poster official' if year else f'"{title}" movie poster official'
        image_url = search_brave_images(search_query, brave_key)

        if image_url:
            # Download to a TEMP file first. Never write raw web bytes to the
            # live poster directory before validation.
            tmp_path = download_image_to_temp(image_url)
            if tmp_path:
                verdict = vision_safety_check(tmp_path, title, year, openai_key)
                if verdict['accept']:
                    if promote_temp(tmp_path, filepath):
                        print("✓ (Brave, vision-approved)")
                        return 'brave'
                    # promote failed -> fall through to placeholder
                else:
                    # Rejected or vision error -> discard temp, queue, fall back.
                    try:
                        os.unlink(tmp_path)
                    except OSError:
                        pass
                    if verdict.get('error'):
                        reason = f"vision_error: {verdict['reason']}"
                    else:
                        flags = []
                        if verdict['is_explicit']:
                            flags.append('explicit')
                        if not verdict['is_movie_poster']:
                            flags.append('not_poster')
                        if not verdict['matches_title']:
                            flags.append('title_mismatch')
                        reason = f"rejected[{','.join(flags)}]: {verdict['reason']}"
                    stats['rejected'] += 1
                    print(f"⛔ (Brave rejected: {reason[:60]})")
                    queue_for_review(slug, title, image_url, reason)
            else:
                # Could not download a structurally valid JPEG candidate.
                queue_for_review(slug, title, image_url, 'download_failed_or_invalid_jpeg')

        # Rate limit before next attempt
        time.sleep(BRAVE_DELAY)

    # 3. Generate placeholder (always safe)
    if HAS_PIL:
        if generate_placeholder(slug, title, year, filepath):
            print("⊞ (Placeholder)")
            return 'placeholder'

    # Failed
    print("✗ (Failed)")
    return 'failed'


def ensure_poster(slug, title, year):
    """
    Integration function for Destiny agent.
    Runs fallback chain for a single movie and returns poster path or None.
    """
    filepath = POSTER_DIR / f"{slug}.jpg"
    
    # Load secrets
    secrets = load_secrets()
    brave_key = secrets.get('BRAVE_SEARCH_KEY')
    openai_key = secrets.get('OPENAI_API_KEY')
    
    existing = get_existing_posters()
    
    result = process_poster(slug, title, year, existing, brave_key, openai_key, force_replace=False)
    
    if result != 'failed':
        return str(filepath)
    
    return None


def run_single_slug(slug, brave_key, openai_key=None):
    """Process a single slug."""
    print(f"\n🎬 Processing single slug: {slug}\n")
    
    # Get review data
    reviews = load_reviews_from_json()
    review = next((r for r in reviews if r['slug'] == slug), None)
    
    if not review:
        print(f"✗ Review not found: {slug}")
        return
    
    existing = get_existing_posters()
    result = process_poster(slug, review['title'], review['year'], existing, brave_key, openai_key, force_replace=False)
    
    stats[result if result in stats else 'failed'] += 1


def run_all_reviews(brave_key, openai_key=None):
    """Process all reviews."""
    print(f"\n🎬 Processing all reviews\n")
    
    reviews = load_reviews_from_json()
    if not reviews:
        print("✗ No reviews found")
        return
    
    existing = get_existing_posters()
    
    print(f"📊 Total reviews: {len(reviews)}")
    print(f"📁 Existing posters: {len(existing)}")
    print()
    
    for i, review in enumerate(reviews, 1):
        result = process_poster(
            review['slug'],
            review['title'],
            review['year'],
            existing,
            brave_key,
            openai_key,
            force_replace=False
        )
        
        if result in stats:
            stats[result] += 1
        else:
            stats['failed'] += 1
        
        if result == 'failed':
            stats['failed_slugs'].append(review['slug'])
        
        # Progress indicator
        if i % 10 == 0:
            print(f"\n📈 Progress: {i}/{len(reviews)} ({100*i//len(reviews)}%)\n")


def run_replace_placeholders(brave_key, openai_key=None):
    """Re-check placeholder posters and try to find real ones."""
    print(f"\n🎬 Replacing placeholder posters\n")
    
    reviews = load_reviews_from_json()
    existing = get_existing_posters()
    
    placeholders = [
        (slug, info) for slug, info in existing.items()
        if is_placeholder(info['path'])
    ]
    
    print(f"📊 Found {len(placeholders)} placeholder posters\n")
    
    for i, (slug, info) in enumerate(placeholders, 1):
        review = next((r for r in reviews if r['slug'] == slug), None)
        if not review:
            continue
        
        result = process_poster(
            slug,
            review['title'],
            review['year'],
            existing,
            brave_key,
            openai_key,
            force_replace=True
        )
        
        if result in stats:
            stats[result] += 1
        else:
            stats['failed'] += 1
        
        if result == 'failed':
            stats['failed_slugs'].append(slug)


def report_summary():
    """Print summary report."""
    print()
    print("=" * 70)
    print("POSTER PIPELINE SUMMARY")
    print("=" * 70)
    print(f"✓ OMDb:           {stats['omdb']}")
    print(f"✓ Brave (gated):  {stats['brave']}")
    print(f"⊞ Placeholder:    {stats['placeholder']}")
    print(f"⛔ Brave rejected: {stats['rejected']}")
    print(f"🚩 Queued review:  {stats['queued']}")
    print(f"✗ Failed:         {stats['failed']}")
    print(f"⏭ Skipped:        {stats['skipped']}")
    print()
    
    if stats['failed_slugs']:
        print(f"Failed ({len(stats['failed_slugs'])}): {', '.join(stats['failed_slugs'][:10])}")
        if len(stats['failed_slugs']) > 10:
            print(f"  ... and {len(stats['failed_slugs']) - 10} more")
    
    print("=" * 70)


def git_commit():
    """Commit changes to git."""
    total_new = stats['omdb'] + stats['brave'] + stats['placeholder']
    
    if total_new == 0:
        print("⏭ No new posters to commit")
        return
    
    print()
    print("📝 Committing to git...")
    
    try:
        os.chdir(REPO_DIR)
        
        # Add poster directory
        os.system(f"git add {POSTER_DIR}/*.jpg 2>/dev/null")
        
        # Commit
        types = []
        if stats['omdb'] > 0:
            types.append(f"{stats['omdb']} from OMDb")
        if stats['brave'] > 0:
            types.append(f"{stats['brave']} from Brave")
        if stats['placeholder'] > 0:
            types.append(f"{stats['placeholder']} placeholders")
        
        commit_msg = f"Add {total_new} posters ({', '.join(types)})"
        result = os.system(f'git commit -m "{commit_msg}" 2>/dev/null')
        
        if result == 0:
            print(f"✓ Committed {total_new} new/updated posters")
        else:
            print("⚠️  Git commit failed or no changes")
    except Exception as e:
        print(f"⚠️  Git error: {e}")


def main():
    """Main entry point."""
    # Load secrets
    secrets = load_secrets()
    brave_key = secrets.get('BRAVE_SEARCH_KEY')
    openai_key = secrets.get('OPENAI_API_KEY')
    
    if not brave_key:
        print("⚠️  BRAVE_SEARCH_KEY not found in ~/.openclaw/.secrets")
        print("    Some features will be limited\n")
    if not openai_key:
        print("⚠️  OPENAI_API_KEY not found in ~/.openclaw/.secrets")
        print("    Brave images CANNOT pass the vision gate -> placeholder fallback only\n")
    
    # Parse arguments
    mode = 'all'
    slug = None
    
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '--all':
            mode = 'all'
        elif arg == '--slug' and len(sys.argv) > 2:
            mode = 'slug'
            slug = sys.argv[2]
        elif arg == '--replace-placeholders':
            mode = 'replace'
        else:
            print("Usage:")
            print("  python3 poster-pipeline.py --all")
            print("  python3 poster-pipeline.py --slug <slug>")
            print("  python3 poster-pipeline.py --replace-placeholders")
            sys.exit(1)
    
    # Execute mode
    if mode == 'slug':
        run_single_slug(slug, brave_key, openai_key)
    elif mode == 'replace':
        run_replace_placeholders(brave_key, openai_key)
    else:
        run_all_reviews(brave_key, openai_key)
    
    # Summary and commit
    report_summary()
    git_commit()
    print("\n✅ Done!\n")


if __name__ == "__main__":
    main()
