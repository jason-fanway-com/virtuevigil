#!/usr/bin/env python3
"""
VirtueVigil Poster Audit Script
Checks poster integrity and reports issues.
Usage: python3 audit-posters.py
Exit code: 0 if all pass, 1 if any failures
"""

import json
import os
import sys
from pathlib import Path

# Try to import PIL for image validation, but don't fail if not available
try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

def main():
    # Paths
    script_dir = Path(__file__).parent
    repo_dir = script_dir.parent
    reviews_path = repo_dir / 'src' / 'data' / 'reviews.json'
    poster_dir = repo_dir / 'src' / 'images' / 'posters'
    
    # Load reviews
    if not reviews_path.exists():
        print(f"❌ reviews.json not found at {reviews_path}")
        return 1
    
    try:
        with open(reviews_path, 'r') as f:
            reviews = json.load(f)
    except Exception as e:
        print(f"❌ Failed to load reviews.json: {e}")
        return 1
    
    # Track results
    passed = []
    failed = []
    total_reviews = len(reviews)
    reviews_with_posters = 0
    
    # Audit each review
    for review in reviews:
        slug = review.get('slug', 'UNKNOWN')
        poster_field = review.get('poster')
        
        # Check if poster field exists
        if not poster_field:
            failed.append({
                'slug': slug,
                'issue': 'MISSING FIELD: no poster field in review data'
            })
            continue
        
        reviews_with_posters += 1
        
        # Extract filename (handle URLs and query params)
        fname = poster_field.split('/')[-1].split('?')[0]
        fpath = poster_dir / fname
        
        # Check if file exists
        if not fpath.exists():
            failed.append({
                'slug': slug,
                'issue': f'MISSING FILE: {fname} not found in {poster_dir}'
            })
            continue
        
        # Check file size
        try:
            stat = os.stat(fpath)
            file_size = stat.st_size
            
            if file_size < 5000:
                failed.append({
                    'slug': slug,
                    'issue': f'CORRUPT: {fname} is only {file_size} bytes (expected > 5KB)'
                })
                continue
        except Exception as e:
            failed.append({
                'slug': slug,
                'issue': f'STAT ERROR: could not stat {fname}: {e}'
            })
            continue
        
        # Check for bad filenames (OMDb cache artifacts)
        if fname.startswith('MV5B') or '@._V1_' in fname:
            failed.append({
                'slug': slug,
                'issue': f'BAD FILENAME: {fname} appears to be OMDb cache artifact'
            })
            continue
        
        # Validate JPEG magic bytes if file exists
        try:
            with open(fpath, 'rb') as f:
                magic = f.read(3)
                # JPEG files start with FF D8 FF
                if magic[:2] != b'\xff\xd8':
                    failed.append({
                        'slug': slug,
                        'issue': f'INVALID JPEG: {fname} does not start with JPEG magic bytes'
                    })
                    continue
        except Exception as e:
            failed.append({
                'slug': slug,
                'issue': f'MAGIC BYTES ERROR: could not read {fname}: {e}'
            })
            continue
        
        # Try PIL image validation if available
        if HAS_PIL:
            try:
                img = Image.open(fpath)
                width, height = img.size
                
                # Check reasonable dimensions
                if width < 100 or height < 150:
                    failed.append({
                        'slug': slug,
                        'issue': f'DIMENSIONS: {fname} is {width}x{height} (need at least 100x150)'
                    })
                    continue
            except Exception as e:
                failed.append({
                    'slug': slug,
                    'issue': f'PIL ERROR: {fname} failed PIL validation: {e}'
                })
                continue
        
        # All checks passed
        passed.append(slug)
    
    # Report
    print(f"\n{'='*70}")
    print(f"VirtueVigil Poster Audit Report")
    print(f"{'='*70}")
    print(f"\nSummary:")
    print(f"  Total reviews:           {total_reviews}")
    print(f"  Reviews with posters:    {reviews_with_posters}")
    print(f"  Poster files:            {len(list(poster_dir.glob('*.jpg')))}")
    print(f"\nResults:")
    print(f"  ✓ PASS:  {len(passed)} reviews have valid posters")
    print(f"  ✗ FAIL:  {len(failed)} reviews have poster issues")
    
    if failed:
        print(f"\n{'='*70}")
        print(f"FAILURES ({len(failed)}):")
        print(f"{'='*70}")
        for item in failed:
            print(f"  [{item['slug']}] {item['issue']}")
    
    if len(passed) == reviews_with_posters and len(failed) == 0:
        print(f"\n{'='*70}")
        print(f"✓ All {reviews_with_posters} posters are valid!")
        print(f"{'='*70}\n")
        return 0
    else:
        print(f"\n{'='*70}")
        print(f"✗ {len(failed)} poster issues detected")
        print(f"{'='*70}\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
