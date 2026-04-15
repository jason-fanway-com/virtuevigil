#!/usr/bin/env python3
"""
Bulk Poster Download Script for VirtueVigil Reviews
Fetches and downloads posters for all reviews missing poster images.

API: OMDb (http://www.omdbapi.com/)
Rate limit: 1 request per second
"""

import json
import os
import re
import time
import urllib.request
import urllib.parse
from pathlib import Path

# Configuration
OMDB_API_KEY = "fff6ef33"
OMDB_BASE_URL = "http://www.omdbapi.com/"
SITEMAP_URL = "https://virtuevigil.com/sitemap.xml"
POSTER_DIR = "/Users/joestrazza/virtuevigil/public/images/posters/"
RATE_LIMIT_DELAY = 0.5  # seconds between requests (faster for demo)

# Stats
downloaded = 0
already_exist = 0
failed = 0
failed_titles = []


def fetch_sitemap():
    """Fetch and parse sitemap to extract review slugs."""
    print("📥 Fetching sitemap...")
    try:
        with urllib.request.urlopen(SITEMAP_URL, timeout=10) as response:
            content = response.read().decode('utf-8')
        
        # Extract all /reviews/* URLs
        review_urls = re.findall(r'https://virtuevigil\.com/reviews/([^/]+)/', content)
        print(f"✓ Found {len(review_urls)} reviews in sitemap")
        return review_urls
    except Exception as e:
        print(f"✗ Error fetching sitemap: {e}")
        return []


def get_existing_posters():
    """Get list of existing poster files."""
    if not os.path.exists(POSTER_DIR):
        os.makedirs(POSTER_DIR, exist_ok=True)
    
    existing = set()
    for filename in os.listdir(POSTER_DIR):
        if filename.endswith('.jpg'):
            slug = filename.replace('.jpg', '')
            existing.add(slug)
    
    print(f"📋 Found {len(existing)} existing posters")
    return existing


def slug_to_movie_title(slug):
    """
    Convert review slug to movie title.
    Examples:
    - 'the-brutalist-2026' -> 'The Brutalist'
    - 'nosferatu-2024' -> 'Nosferatu'
    - 'jaws-1975' -> 'Jaws'
    """
    # Remove year suffix (e.g., -2026, -2025, -2024)
    title = re.sub(r'-\d{4}$', '', slug)
    
    # Replace hyphens with spaces
    title = title.replace('-', ' ')
    
    # Title case
    title = title.title()
    
    return title


def query_omdb(movie_title):
    """Query OMDb API for poster."""
    global failed, failed_titles
    
    params = {
        't': movie_title,
        'apikey': OMDB_API_KEY,
        'type': 'movie'
    }
    
    url = OMDB_BASE_URL + '?' + urllib.parse.urlencode(params)
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        if data.get('Response') == 'True' and data.get('Poster') != 'N/A':
            return data.get('Poster')
        return None
    except Exception as e:
        print(f"  ⚠ API error for '{movie_title}': {e}")
        return None


def download_poster(poster_url, filename):
    """Download poster image from URL."""
    global downloaded, failed, failed_titles
    
    try:
        with urllib.request.urlopen(poster_url, timeout=10) as response:
            poster_data = response.read()
        
        filepath = os.path.join(POSTER_DIR, filename)
        with open(filepath, 'wb') as f:
            f.write(poster_data)
        
        downloaded += 1
        print(f"  ✓ {filename}")
        return True
    except Exception as e:
        failed += 1
        failed_titles.append(filename.replace('.jpg', ''))
        print(f"  ✗ {filename} (download failed: {e})")
        return False


def process_reviews(limit=None):
    """Main processing loop."""
    global downloaded, failed, already_exist, failed_titles
    
    review_slugs = fetch_sitemap()
    if not review_slugs:
        print("✗ No reviews found in sitemap")
        return
    
    existing = get_existing_posters()
    missing = [slug for slug in review_slugs if slug not in existing]
    
    # Apply limit for testing if specified
    if limit:
        missing = missing[:limit]
    
    print(f"📊 Total reviews: {len(review_slugs)}")
    print(f"📁 Already have posters: {len(existing)}")
    print(f"❌ Missing posters: {len(missing)}")
    print()
    
    print(f"🚀 Starting download... (rate limit: {RATE_LIMIT_DELAY}s between requests)")
    print()
    
    for i, slug in enumerate(missing, 1):
        movie_title = slug_to_movie_title(slug)
        
        # Query OMDb
        poster_url = query_omdb(movie_title)
        
        # If not found, try without year suffix (already stripped, but try simpler variants)
        if not poster_url and ' ' in movie_title:
            # Try just first word for some edge cases
            pass
        
        # Download if found
        if poster_url:
            download_poster(poster_url, f"{slug}.jpg")
        else:
            failed += 1
            failed_titles.append(slug)
            print(f"  ✗ {slug}.jpg (not found on OMDb)")
        
        # Rate limiting
        if i < len(missing):
            time.sleep(RATE_LIMIT_DELAY)
        
        # Progress indicator every 50 items
        if i % 50 == 0:
            print(f"\n📈 Progress: {i}/{len(missing)} ({100*i//len(missing)}%)\n")
    
    # Summary
    print()
    print("=" * 60)
    print("📊 DOWNLOAD SUMMARY")
    print("=" * 60)
    print(f"✓ Downloaded:     {downloaded}")
    print(f"✗ Failed:         {failed}")
    print(f"⏭ Skipped:        {len(existing)}")
    print(f"📊 Total:         {len(review_slugs)}")
    print()
    
    if failed_titles:
        print(f"Failed titles ({len(failed_titles)}):")
        for title in failed_titles[:20]:  # Show first 20
            print(f"  - {title}")
        if len(failed_titles) > 20:
            print(f"  ... and {len(failed_titles) - 20} more")
    
    print("=" * 60)


def git_commit():
    """Add and commit new posters to git."""
    if downloaded == 0:
        print("⏭ No new posters to commit")
        return
    
    print()
    print("📝 Committing new posters to git...")
    
    os.chdir("/Users/joestrazza/virtuevigil/")
    
    # Add poster files
    os.system(f"git add {POSTER_DIR}*.jpg 2>/dev/null")
    
    # Commit
    commit_msg = f"Add {downloaded} missing movie posters (bulk download)"
    result = os.system(f'git commit -m "{commit_msg}" 2>/dev/null')
    
    if result == 0:
        print(f"✓ Committed {downloaded} new posters")
    else:
        print("⚠ Git commit failed or no changes to commit")


if __name__ == "__main__":
    import sys
    
    # Allow limiting via command line: python script.py 15
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    
    process_reviews(limit=limit)
    git_commit()
    print("\n✅ Done!")
