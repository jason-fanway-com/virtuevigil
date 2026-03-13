#!/bin/bash
# Mass poster fix - downloads ALL posters from Wikipedia
# Usage: bash scripts/mass-poster-fix.sh [--force]

set -euo pipefail

POSTER_DIR="src/images/posters"
FORCE="${1:-}"
FIXED=0
FAILED=0
SKIPPED=0

cd "$(dirname "$0")/.."

# Extract all reviews with their titles, years, and slugs
python3 -c "
import json
with open('src/data/reviews.json') as f:
    reviews = json.load(f)
for r in reviews:
    poster = r.get('poster', '')
    if poster.startswith('/images/posters/'):
        slug = poster.replace('/images/posters/', '').replace('.jpg', '')
        title = r.get('title', '').replace('\"', '\\\\\"')
        year = r.get('year', '')
        media_type = r.get('media_type', 'movie')
        print(f'{slug}\t{title}\t{year}\t{media_type}')
" > /tmp/vv-reviews-list.tsv

total=$(wc -l < /tmp/vv-reviews-list.tsv)
echo "Processing $total reviews..."

while IFS=$'\t' read -r slug title year media_type; do
    poster_path="$POSTER_DIR/${slug}.jpg"
    
    # Skip if file exists and is big enough (unless --force)
    if [ -f "$poster_path" ] && [ "$FORCE" != "--force" ]; then
        fsize=$(stat -f%z "$poster_path" 2>/dev/null || stat -c%s "$poster_path" 2>/dev/null)
        if [ "$fsize" -gt 20000 ]; then
            ((SKIPPED++))
            continue
        fi
    fi
    
    echo -n "[$((FIXED + FAILED + SKIPPED + 1))/$total] $title ($year)... "
    
    # Try Wikipedia (movie)
    wiki_title=$(echo "$title" | sed 's/ /_/g')
    if [ "$media_type" = "tv" ] || [ "$media_type" = "series" ]; then
        wiki_url="https://en.wikipedia.org/wiki/${wiki_title}_(TV_series)"
    else
        wiki_url="https://en.wikipedia.org/wiki/${wiki_title}_(${year}_film)"
    fi
    
    # Get poster URL from Wikipedia page
    poster_url=$(curl -sL --max-time 10 "$wiki_url" 2>/dev/null | grep -o 'upload\.wikimedia\.org/wikipedia/en/[^"]*\.jpg' | head -1)
    
    if [ -z "$poster_url" ]; then
        # Try without year
        wiki_url="https://en.wikipedia.org/wiki/${wiki_title}"
        poster_url=$(curl -sL --max-time 10 "$wiki_url" 2>/dev/null | grep -o 'upload\.wikimedia\.org/wikipedia/en/[^"]*\.jpg' | head -1)
    fi
    
    if [ -n "$poster_url" ]; then
        # Convert thumbnail to full-res
        full_url=$(echo "$poster_url" | sed 's|/thumb/|/|' | sed 's|/[0-9]*px-[^/]*$||')
        full_url="https://${full_url}"
        
        curl -sL --max-time 15 "$full_url" -o "/tmp/vv-poster-temp.jpg" 2>/dev/null
        
        if [ -f "/tmp/vv-poster-temp.jpg" ]; then
            fsize=$(stat -f%z "/tmp/vv-poster-temp.jpg" 2>/dev/null || stat -c%s "/tmp/vv-poster-temp.jpg" 2>/dev/null)
            header=$(xxd -l 2 -p "/tmp/vv-poster-temp.jpg" 2>/dev/null)
            
            if [ "$fsize" -gt 10000 ] && [ "$header" = "ffd8" ]; then
                cp "/tmp/vv-poster-temp.jpg" "$poster_path"
                echo "✓ Wikipedia"
                ((FIXED++))
                continue
            fi
        fi
    fi
    
    echo "✗ FAILED"
    ((FAILED++))
    
done < /tmp/vv-reviews-list.tsv

echo ""
echo "=== Results ==="
echo "Fixed: $FIXED"
echo "Skipped: $SKIPPED"  
echo "Failed: $FAILED"
echo "Total: $total"
