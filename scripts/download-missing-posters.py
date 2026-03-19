#!/usr/bin/env python3
"""
Download missing posters using TMDB API with bearer token fallback to web scraping.
"""
import json, subprocess, os, sys, time, re, urllib.parse

POSTER_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'images', 'posters')

MISSING = [
    {"slug":"dune-part-three-2026","title":"Dune: Part Three","year":2026},
    {"slug":"silent-storm-2026","title":"Silent Storm","year":2026},
    {"slug":"butterfly-dreams-2026","title":"Butterfly Dreams","year":2026},
    {"slug":"thunderbolts-2025","title":"Thunderbolts*","year":2025},
    {"slug":"glass-onion-2022","title":"Glass Onion: A Knives Out Mystery","year":2022},
    {"slug":"nope-2022","title":"Nope","year":2022},
    {"slug":"the-menu-2022","title":"The Menu","year":2022},
    {"slug":"amsterdam-2022","title":"Amsterdam","year":2022},
    {"slug":"till-2022","title":"Till","year":2022},
    {"slug":"avengers-doomsday-2026","title":"Avengers: Doomsday","year":2026},
    {"slug":"sunrise-on-the-reaping-2026","title":"The Hunger Games: Sunrise on the Reaping","year":2026},
    {"slug":"bring-her-back-2025","title":"Bring Her Back","year":2025},
    {"slug":"forrest-gump-1994","title":"Forrest Gump","year":1994},
    {"slug":"the-matrix-1999","title":"The Matrix","year":1999},
    {"slug":"the-notebook-2004","title":"The Notebook","year":2004},
    {"slug":"gladiator-2000","title":"Gladiator","year":2000},
    {"slug":"saving-private-ryan-1998","title":"Saving Private Ryan","year":1998},
    {"slug":"good-will-hunting-1997","title":"Good Will Hunting","year":1997},
    {"slug":"braveheart-1995","title":"Braveheart","year":1995},
    {"slug":"shawshank-redemption-1994","title":"The Shawshank Redemption","year":1994},
    {"slug":"jurassic-park-1993","title":"Jurassic Park","year":1993},
    {"slug":"hacksaw-ridge-2016","title":"Hacksaw Ridge","year":2016},
    {"slug":"the-patriot-2000","title":"The Patriot","year":2000},
    {"slug":"tombstone-1993","title":"Tombstone","year":1993},
]

# Known TMDB poster paths (pre-resolved) for common classic films
KNOWN_POSTERS = {
    "forrest-gump-1994": "https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
    "the-matrix-1999": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
    "the-notebook-2004": "https://image.tmdb.org/t/p/w500/rNzQyW4f8B8cQeg7Dgj3n6eT5k9.jpg",
    "gladiator-2000": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
    "saving-private-ryan-1998": "https://image.tmdb.org/t/p/w500/uqx37cS8cpHg8U35f9U5IBlrCV3.jpg",
    "good-will-hunting-1997": "https://image.tmdb.org/t/p/w500/bABCcRLia6YVqy5lBssObOhKAYk.jpg",
    "braveheart-1995": "https://image.tmdb.org/t/p/w500/or1gBugydmjToAEq7OZY0owwFk.jpg",
    "shawshank-redemption-1994": "https://image.tmdb.org/t/p/w500/9cqNxx0GxF0bAY74W56MAxi5DK3.jpg",
    "jurassic-park-1993": "https://image.tmdb.org/t/p/w500/oU7Oq2kFAAlGqbU4VoAE36g4hoI.jpg",
    "hacksaw-ridge-2016": "https://image.tmdb.org/t/p/w500/7RCsYkAPQXR8FDUMG9tTTVBqhKt.jpg",
    "the-patriot-2000": "https://image.tmdb.org/t/p/w500/1nMNBfFm8vCiHIAQmhEbGQD1IMs.jpg",
    "tombstone-1993": "https://image.tmdb.org/t/p/w500/ahbMbJPQZ8TlPmMNMixAEr7sFmN.jpg",
    "glass-onion-2022": "https://image.tmdb.org/t/p/w500/vDGr1YdrlfbU9wxTOdpf3zChmv9.jpg",
    "nope-2022": "https://image.tmdb.org/t/p/w500/AcKVlWaNVVVFQwro3nLXqPljcYA.jpg",
    "the-menu-2022": "https://image.tmdb.org/t/p/w500/v3QyboWRoA4O9RbcsqH8tJMe8EB.jpg",
    "amsterdam-2022": "https://image.tmdb.org/t/p/w500/ciDC3VjDXFqJVpqkGPBU3gLgBfv.jpg",
    "till-2022": "https://image.tmdb.org/t/p/w500/eLT8Cu357VOwBVTitkmlDEg32Fs.jpg",
    "thunderbolts-2025": "https://image.tmdb.org/t/p/w500/m9EtP1Yrzv6v7dMaC9mRaGhd1um.jpg",
    "bring-her-back-2025": "https://image.tmdb.org/t/p/w500/bXi6KD7MmVn4DGxIZFENKoKEJPZ.jpg",
}

def curl_download(url, output_path, timeout=15):
    result = subprocess.run(
        ['curl', '-sL', '-o', output_path, '--max-time', str(timeout), url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return False
    if not os.path.exists(output_path):
        return False
    if os.path.getsize(output_path) < 5000:
        if os.path.exists(output_path):
            os.remove(output_path)
        return False
    with open(output_path, 'rb') as f:
        header = f.read(2)
    if header != b'\xff\xd8':
        os.remove(output_path)
        return False
    return True

def search_tmdb_web(title, year):
    """Search TMDB website (no API key needed)."""
    query = urllib.parse.quote(f'{title} {year}')
    url = f'https://www.themoviedb.org/search?query={query}'
    result = subprocess.run(
        ['curl', '-sL', '--max-time', '15', '-A', 'Mozilla/5.0', url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    matches = re.findall(r'/t/p/w\d+(/[a-zA-Z0-9]+\.jpg)', result.stdout)
    if matches:
        return f'https://image.tmdb.org/t/p/w500{matches[0]}'
    return None

def main():
    os.makedirs(POSTER_DIR, exist_ok=True)
    fixed = []
    failed = []

    for item in MISSING:
        slug = item['slug']
        title = item['title']
        year = item['year']
        dest = os.path.join(POSTER_DIR, f'{slug}.jpg')

        if os.path.exists(dest):
            print(f'SKIP (exists): {slug}')
            continue

        print(f'Downloading: {slug} ({title} {year})')

        # Try known posters first
        url = KNOWN_POSTERS.get(slug)
        if url:
            if curl_download(url, dest):
                print(f'  OK (known): {url}')
                fixed.append(slug)
                continue
            else:
                print(f'  WARN: known URL failed, trying search')

        # Try TMDB web search
        url = search_tmdb_web(title, year)
        if url:
            if curl_download(url, dest):
                print(f'  OK (search): {url}')
                fixed.append(slug)
                continue
            else:
                print(f'  WARN: search URL failed')

        print(f'  FAIL: {slug}')
        failed.append({'slug': slug, 'title': title, 'year': year})
        time.sleep(0.5)

    print(f'\n=== DONE ===')
    print(f'Downloaded: {len(fixed)}: {fixed}')
    print(f'Failed: {len(failed)}')
    for f in failed:
        print(f'  - {f["slug"]} ({f["title"]})')

if __name__ == '__main__':
    main()
