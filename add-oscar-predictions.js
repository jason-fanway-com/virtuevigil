const fs = require('fs');
const path = require('path');

// Read new review
const newReviews = JSON.parse(fs.readFileSync('oscar-predictions-review.json', 'utf8'));

// Read existing reviews
const filePath = 'src/data/reviews.json';
const existing = JSON.parse(fs.readFileSync(filePath, 'utf8'));

// Deduplicate by id
const existingIds = new Set(existing.map(r => r.id));
const toAdd = newReviews.filter(r => !existingIds.has(r.id));

if (toAdd.length === 0) {
  console.log('Review already exists. Updating...');
  const idx = existing.findIndex(r => r.id === newReviews[0].id);
  if (idx >= 0) {
    existing[idx] = newReviews[0];
    fs.writeFileSync(filePath, JSON.stringify(existing, null, 2));
    console.log('Updated existing review.');
  }
} else {
  // Add to front
  const combined = [...toAdd, ...existing];
  fs.writeFileSync(filePath, JSON.stringify(combined, null, 2));
  console.log(`Added ${toAdd.length} new reviews. Total: ${combined.length}`);
}
