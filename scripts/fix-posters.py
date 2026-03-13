#!/usr/bin/env python3
"""
Mass poster fixer for VirtueVigil.
Downloads correct posters from TMDB CDN (no auth needed if we have poster_path).
Falls back to Wikipedia for poster images.
"""

import json
import subprocess
import os
import sys
import time
import re
import urllib.parse

REVIEWS_JSON = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'reviews.json')
POSTER_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'images', 'posters')
PUBLIC_POSTER_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'images', 'posters')

# Known TMDB poster paths (movie_id -> poster_path)
# These are the canonical paths on TMDB's CDN
TMDB_OVERRIDES = {}

def curl_download(url, output_path, timeout=15):
    """Download a URL to a file using curl."""
    result = subprocess.run(
        ['curl', '-sL', '-o', output_path, '--max-time', str(timeout), url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return False
    # Verify it's a JPEG
    if not os.path.exists(output_path):
        return False
    if os.path.getsize(output_path) < 10000:
        return False
    with open(output_path, 'rb') as f:
        header = f.read(2)
    if header != b'\xff\xd8':
        os.remove(output_path)
        return False
    return True

def search_wikipedia_poster(title, year):
    """Try to get a poster from Wikipedia."""
    # Construct Wikipedia article name
    search_title = title.replace(' ', '_')
    if year:
        search_title += f'_({year}_film)'
    
    url = f'https://en.wikipedia.org/wiki/{urllib.parse.quote(search_title)}'
    result = subprocess.run(
        ['curl', '-sL', '--max-time', '10', url],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        return None
    
    # Find the poster image URL in the infobox
    html = result.stdout
    # Look for upload.wikimedia.org/wikipedia/en/... .jpg patterns
    matches = re.findall(r'upload\.wikimedia\.org/wikipedia/en/[^"\'>\s]+\.jpg', html)
    
    if not matches:
        # Try without year qualifier
        search_title = title.replace(' ', '_')
        url = f'https://en.wikipedia.org/wiki/{urllib.parse.quote(search_title)}'
        result = subprocess.run(
            ['curl', '-sL', '--max-time', '10', url],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            matches = re.findall(r'upload\.wikimedia\.org/wikipedia/en/[^"\'>\s]+\.jpg', html)
    
    if matches:
        # Get the full-res version (remove /thumb/ and size suffix)
        poster_url = matches[0]
        if '/thumb/' in poster_url:
            # Convert thumbnail URL to full image URL
            # From: upload.wikimedia.org/wikipedia/en/thumb/a/ab/File.jpg/250px-File.jpg
            # To:   upload.wikimedia.org/wikipedia/en/a/ab/File.jpg
            poster_url = poster_url.replace('/thumb/', '/')
            # Remove the /NNNpx-Filename.jpg suffix
            poster_url = re.sub(r'/\d+px-[^/]+$', '', poster_url)
        
        return f'https://{poster_url}'
    
    return None

def search_tmdb_web(title, year):
    """Search TMDB website to find the poster path (no API key needed for CDN)."""
    query = urllib.parse.quote(f'{title} {year}')
    url = f'https://www.themoviedb.org/search?query={query}'
    result = subprocess.run(
        ['curl', '-sL', '--max-time', '10', url],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        return None
    
    # Look for poster paths in the HTML
    # Pattern: /t/p/w500/XXXXX.jpg or data-src with poster path
    matches = re.findall(r'/t/p/w\d+(/[a-zA-Z0-9]+\.jpg)', result.stdout)
    if matches:
        poster_path = matches[0]
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    
    return None

def main():
    with open(REVIEWS_JSON) as f:
        reviews = json.load(f)
    
    fixed = 0
    failed = []
    skipped = 0
    
    for i, r in enumerate(reviews):
        poster = r.get('poster', '')
        if not poster.startswith('/images/posters/'):
            continue
        
        slug = poster.replace('/images/posters/', '').replace('.jpg', '')
        title = r.get('title', '')
        year = r.get('year', '')
        src_path = os.path.join(POSTER_DIR, f'{slug}.jpg')
        
        # Check if current poster needs fixing
        if os.path.exists(src_path):
            fsize = os.path.getsize(src_path)
            if fsize > 20000 and fsize != 5295:
                # Probably OK, skip unless --force
                if '--force' not in sys.argv:
                    skipped += 1
                    continue
        
        print(f'[{i+1}/{len(reviews)}] Fixing: {title} ({year}) - {slug}')
        
        # Try TMDB web scrape first
        tmdb_url = search_tmdb_web(title, year)
        if tmdb_url:
            if curl_download(tmdb_url, src_path):
                print(f'  ✓ Downloaded from TMDB')
                fixed += 1
                time.sleep(0.5)
                continue
        
        # Try Wikipedia
        wiki_url = search_wikipedia_poster(title, year)
        if wiki_url:
            if curl_download(wiki_url, src_path):
                print(f'  ✓ Downloaded from Wikipedia')
                fixed += 1
                time.sleep(0.5)
                continue
        
        print(f'  ✗ FAILED to find poster')
        failed.append(slug)
        time.sleep(0.5)
    
    # Also copy to public/ for any that exist there
    for fname in os.listdir(POSTER_DIR):
        pub_path = os.path.join(PUBLIC_POSTER_DIR, fname)
        if os.path.exists(pub_path):
            src_path = os.path.join(POSTER_DIR, fname)
            subprocess.run(['cp', src_path, pub_path])
    
    print(f'\n=== Results ===')
    print(f'Fixed: {fixed}')
    print(f'Skipped (looked OK): {skipped}')
    print(f'Failed: {len(failed)}')
    if failed:
        print('Failed slugs:')
        for s in failed:
            print(f'  - {s}')

if __name__ == '__main__':
    main()
