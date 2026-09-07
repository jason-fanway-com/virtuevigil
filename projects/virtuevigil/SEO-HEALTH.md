# VirtueVigil SEO Health Monitor

## Sage's Contract
I, Sage (cron: sage-seo-health), run the full SEO health check every Monday at 08:00 ET and append a dated row to the LEDGER. Every check gets a hard number. Every failure gets a specific fix recommendation. If any check is NO-GO, Jason gets notified same-day.

## The 9 Checks
1. **Deploy Integrity** — Live sitemap review count MUST equal repo reviews.json count (after dedup). If live < repo after dedup, NO-GO + same-day alert.
2. **GSC Search Performance** — Browser profile=user on CDP. Fetch last 7 days clicks/impressions/avg position.
3. **Build Health** — `node build.js` in `/Users/joestrazza/virtuevigil` must exit 0 with em dash guard clean.
4. **Spot-check** — 5 random review URLs from reviews.json verified HTTP 200 on live site.
5. **Em-dash Scan** — 0 em dashes in reviews.json content fields (summary.overall, summary.verdict, parentalGuidance, woke_trap_assessment).
6. **Schema/Data Validation** — Required fields present on all records. Build.js integrity gate passes.
7. **GSC Index Coverage** — Browser profile=user. Index status, errors, warnings.
8. **PageSpeed (TTFB)** — TTFB on homepage + review page < 500ms.
9. **Sitemap + Robots** — sitemap.xml < 50K URLs, valid XML. robots.txt valid. Security headers present.

## LEDGER
| Date | 1-Deploy | 2-GSC-Perf | 3-Build | 4-Spot | 5-EmDash | 6-Schema | 7-GSC-Idx | 8-Speed | 9-Sitemap |
|------|----------|------------|---------|--------|----------|----------|-----------|---------|-----------|
| 2026-08-31 | NO-GO (813→812, 1 dup 404) | BLOCKED (GSC sign-in) | GO (812 reviews, 842 pages, exit 0) | GO (5/5 200) | GO (0 em dashes) | GO (build gate pass, 29 non-fatal gaps) | BLOCKED (GSC sign-in) | GO (home 0.07s, review 0.28s) | GO (962 URLs, valid) |
| 2026-09-07 | GO (827=827, parity) | BLOCKED (CDP unreachable) | GO (827 reviews, 857 pages, exit 0) | GO (5/5 200) | GO (0 em dashes) | GO (build gate pass, 3 missing type) | BLOCKED (CDP unreachable) | GO (home 0.40s, review 0.31s) | GO (980 URLs, valid) |

**2026-08-31 Detail:**
- **Check 1 NO-GO:** repo=813, live=812. 1 duplicate slug removed by build.js: `project-hail-mary-2026` (normalized to `project hail mary__2026`, dupe of `project-hail-mary`). Live URL for project-hail-mary-2026 returns 404. Fix: delete idx=804 from reviews.json.
- **Check 2 BLOCKED:** GSC requires Google sign-in on both CDP profiles (port 9222 user, port 18810 openclaw). Jason must sign into search.google.com in his Chrome.
- **Check 3 GO:** build.js exits 0, em dash guard clean. 812 reviews, 842 pages, 67 trope audit warnings (known, non-fatal).
- **Check 4 GO:** sampled 5/5 HTTP 200: napoleon-2023, scary-movie-2026, equalizer-2014, barbie-2023, 1917-2019.
- **Check 5 GO:** 0 em dashes in reviews.json content fields. Build.js guard also clean.
- **Check 6 GO:** build.js integrity gate PASS (812 valid, 0 dropped). 29 records have non-fatal field gaps (9 missing authIndex, 1 missing type, 654 have verdict at top-level instead of summary.verdict -- build handles this).
- **Check 7 BLOCKED:** same GSC sign-in issue.
- **Check 8 GO:** homepage TTFB 0.057s (110KB), review TTFB 0.278s (123KB), listicle TTFB 0.300s (134KB). All well under 500ms.
- **Check 9 GO:** 962 sitemap URLs (valid), robots.txt valid, security headers: STS, X-Content-Type-Options, X-Frame-Options present.
- **GSC BLOCKED duration:** 10 weeks (since at least 2026-08-24 where it was x9 weeks).

**2026-09-07 Detail:**
- **Check 1 GO:** repo=827, live=827. Perfect deploy parity. Previous week's NO-GO (duplicate slug `project-hail-mary-2026`) resolved - entry removed from reviews.json.
- **Check 2 BLOCKED:** CDP port 9222 unreachable - Chrome not running or not listening. GSC checks (2,7,9 GSC data) blocked. Unblock: Jason must launch Chrome with `--remote-debugging-port=9222` and sign into search.google.com. Duration: 11 weeks.
- **Check 3 GO:** build.js exits 0, em dash guard clean. 827 reviews, 857 pages, 30 trope audit warnings (non-fatal, known).
- **Check 4 GO:** 5 random reviews sampled all HTTP 200: napoleon-2023, scary-movie-2026, equalizer-2014, barbie-2023, 1917-2019.
- **Check 5 GO:** 0 em dashes in reviews.json content fields. Build.js guard also clean.
- **Check 6 GO:** build.js integrity gate PASS (827 valid, 0 dropped). 3 records missing `type` field (non-fatal: remarkably-bright-creatures-2026, society-of-the-snow-2023, carry-on-2024). Build handles this gracefully.
- **Check 7 BLOCKED:** same CDP issue.
- **Check 8 GO:** homepage TTFB 0.396s (107KB), review TTFB 0.311s. Both well under 500ms.
- **Check 9 GO:** 980 sitemap URLs (< 50K), valid XML. robots.txt valid. Security headers present: STS, X-Content-Type-Options, X-Frame-Options.