#!/usr/bin/env python3
"""
Smoke test for the poster vision gate using REAL OpenAI vision calls.

Uses only safe public test images:
  - GOOD: a real movie poster (Wikimedia / public film poster) -> expect ACCEPT
  - BAD : a plain landscape/photo that is clearly NOT a poster -> expect REJECT

NO explicit content is ever used. This exercises the live gate end-to-end.

Run: python3 smoke_poster_gate.py
"""

import importlib.util
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("poster_pipeline", SCRIPT_DIR / "poster-pipeline.py")
pp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pp)

# Safe public test images.
# GOOD: the real, official "Inception" (2010) poster served by Amazon's image
#       CDN (the same trusted host OMDb returns). A legitimate film poster.
GOOD_POSTER_URL = "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL75_UX380_CR0,0,380,562_.jpg"
GOOD_TITLE = "Inception"
GOOD_YEAR = 2010

# BAD: a plain random landscape photo (picsum) - clearly NOT a movie poster.
BAD_IMAGE_URL = "https://picsum.photos/id/1015/600/900.jpg"
BAD_TITLE = "Some Movie That Does Not Exist"
BAD_YEAR = 2026


def run_case(label, url, title, year, expect_accept, openai_key):
    print(f"\n=== {label} ===")
    print(f"URL: {url}")
    tmp = pp.download_image_to_temp(url, timeout=20)
    if not tmp:
        print("RESULT: download failed / not a valid JPEG (could not test).")
        return None
    try:
        verdict = pp.vision_safety_check(tmp, title, year, openai_key)
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass
    print(f"verdict: accept={verdict['accept']} is_explicit={verdict['is_explicit']} "
          f"is_movie_poster={verdict['is_movie_poster']} matches_title={verdict['matches_title']}")
    print(f"reason: {verdict['reason']}")
    if verdict.get("error"):
        print(f"error: {verdict['error']}")
    ok = (verdict["accept"] == expect_accept)
    print(f"EXPECTED accept={expect_accept} -> {'PASS' if ok else 'FAIL'}")
    return ok


def main():
    secrets = pp.load_secrets()
    openai_key = secrets.get("OPENAI_API_KEY")
    if not openai_key:
        print("OPENAI_API_KEY missing; cannot run live smoke test.")
        sys.exit(2)

    results = []
    results.append(run_case("GOOD poster (expect ACCEPT)", GOOD_POSTER_URL,
                            GOOD_TITLE, GOOD_YEAR, True, openai_key))
    results.append(run_case("NON-poster image (expect REJECT)", BAD_IMAGE_URL,
                            BAD_TITLE, BAD_YEAR, False, openai_key))

    print("\n=== SMOKE SUMMARY ===")
    passed = sum(1 for r in results if r is True)
    total = len([r for r in results if r is not None])
    print(f"{passed}/{total} cases passed")
    sys.exit(0 if passed == total and total == len(results) else 1)


if __name__ == "__main__":
    main()
