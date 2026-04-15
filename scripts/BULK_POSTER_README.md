# VirtueVigil Bulk Poster Download Script

## Overview
This script automatically downloads missing movie poster images for VirtueVigil reviews from the OMDb API.

## Status
- **Reviews:** 517 total on virtuevigil.com
- **Posters before:** 127
- **Posters after testing:** 242 (115 new)
- **Success rate:** ~55% (many 2026 unreleased films not yet in OMDb)

## Usage

### Full scan (all missing posters):
```bash
python3 scripts/bulk-poster-download.py
```

### Limited test (first N posters):
```bash
python3 scripts/bulk-poster-download.py 20
```

## How It Works

1. **Fetch Sitemap:** Retrieves list of all reviews from `https://virtuevigil.com/sitemap.xml`
2. **Compare Existing:** Checks `/public/images/posters/` for already-downloaded posters
3. **Query OMDb:** For each missing poster, queries OMDb API with the movie title
4. **Download:** Downloads poster image if found
5. **Rate Limit:** 1 request per second to respect API limits
6. **Git Commit:** Automatically commits new posters to git

## API
- **OMDb:** http://www.omdbapi.com/ (free tier, 1000 req/day)
- **Key:** fff6ef33 (free API key)

## Poster Naming
Filenames match review slugs:
- Review: `/reviews/the-patriot-2000/` → Poster: `the-patriot-2000.jpg`
- Review: `/reviews/coco-2017/` → Poster: `coco-2017.jpg`

## Limitations

### Why some posters fail:
1. **Unreleased films:** Films releasing in 2025-2026 not yet in OMDb (e.g., "Disclosure Day 2026")
2. **TV shows:** Series not matched by OMDb movie search (e.g., "Fallout Season 2")
3. **Exact title matching:** Title variations not captured (e.g., "Kill Bill Volume I" vs "Kill Bill Vol. 1")
4. **No poster:** Some films have no poster in OMDb

### Improvement opportunities:
- Add fuzzy matching for title variations
- Query with year parameter for disambiguation
- Support TV show searching
- Cache results to avoid re-querying

## Example Run (20 films)
```
✓ Successfully downloaded: 11
✗ Failed: 9 (not in OMDb, title mismatch, or download error)
```

Successful downloads:
- terrifier-3-2024.jpg (36 KB)
- scream-vi-2023.jpg (36 KB)
- dungeons-dragons-honor-among-thieves-2023.jpg (50 KB)
- argylle-2024.jpg (44 KB)
- atlas-2024.jpg (25 KB)
- gran-turismo-2023.jpg (40 KB)
- road-house-2024.jpg (33 KB)
- beverly-hills-cop-axel-f-2024.jpg (40 KB)
- bob-marley-one-love-2024.jpg (31 KB)
- trap-2024.jpg (20 KB)
- the-bikeriders-2024.jpg (39 KB)

## Performance
- Rate: ~1.2 requests/second (respects OMDb limits)
- For 393 missing posters: ~5-7 minutes runtime
- Network-bound (API calls are the bottleneck)

## Dependencies
- Python 3 (stdlib only: json, os, re, time, urllib)
- Internet connection for API calls
- Git (for auto-commit feature)
