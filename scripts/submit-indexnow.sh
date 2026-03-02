#!/bin/bash
# submit-indexnow.sh — Submit all VirtueVigil URLs to IndexNow (Bing, Yandex, etc.)
# Run after any build/deploy that adds new content.
# Usage: ./scripts/submit-indexnow.sh [url1 url2 ...] (optional specific URLs, otherwise submits all)

set -euo pipefail

KEY="c5c06a51b3df4a6fb07de4954187d031"
HOST="virtuevigil.com"
SITE="https://virtuevigil.com"
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REVIEWS_JSON="$REPO_DIR/src/data/reviews.json"

if [ $# -gt 0 ]; then
    URL_LIST=$(printf '"%s",' "$@" | sed 's/,$//')
else
    URL_LIST=$(python3 -c "
import json
with open('$REVIEWS_JSON') as f:
    reviews = json.load(f)
urls = ['$SITE/reviews/' + r['slug'] + '/' for r in reviews]
urls.extend([
    '$SITE/',
    '$SITE/about.html',
    '$SITE/methodology.html',
    '$SITE/woke-trap.html',
    '$SITE/subscribe/',
])
print(','.join(['\"' + u + '\"' for u in urls]))
")
fi

PAYLOAD="{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"$SITE/$KEY.txt\",\"urlList\":[$URL_LIST]}"
COUNT=$(echo "$URL_LIST" | tr ',' '\n' | wc -l | tr -d ' ')
echo "Submitting $COUNT URLs to IndexNow..."

for ENGINE in "api.indexnow.org" "www.bing.com" "yandex.com"; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X POST "https://$ENGINE/indexnow" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "$PAYLOAD")
    echo "  $ENGINE → HTTP $STATUS"
done

echo "Done."
