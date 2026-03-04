#!/usr/bin/env node
const https = require('https');
const fs = require('fs');
const path = require('path');

const POSTER_DIR = path.join(__dirname, '../src/images/posters');

const posters = {
  'furiosa-a-mad-max-saga-2024': 'https://image.tmdb.org/t/p/w500/iADOJ8Zymht2JPMoy3R7xceZprc.jpg',
  'godzilla-x-kong-the-new-empire-2024': 'https://image.tmdb.org/t/p/w500/z1p34vh7dEOnLDmyCrlUVLuoDzd.jpg',
  'madame-web-2024': 'https://image.tmdb.org/t/p/w500/rULWuutDcN5NvtiZi4FRPzRkHyd.jpg',
  'wolf-man-2025': 'https://image.tmdb.org/t/p/w500/iNh3BivHyg5sQRPP1KOkzguEX0H.jpg',
  'the-beekeeper-2024': 'https://image.tmdb.org/t/p/w500/aovTHnxu6NtEJ6X79yL3LHBXQCF.jpg',
  'borderlands-2024': 'https://image.tmdb.org/t/p/w500/vvpNTXzgZsVIE3m5q7mYpBhpWYE.jpg',
  'mean-girls-2024': 'https://image.tmdb.org/t/p/w500/vNpuAxGTl9HsUbHqam3E9CzqCvX.jpg',
  'aquaman-and-the-lost-kingdom-2023': 'https://image.tmdb.org/t/p/w500/7lTnXOy0iNtBAdRP3TZvaKJ77F6.jpg',
  'maxxxine-2024': 'https://image.tmdb.org/t/p/w500/9MJA5gwKE3FGi85ysJEPLpVDFZN.jpg',
  'rebel-moon-part-two-the-scargiver-2024': 'https://image.tmdb.org/t/p/w500/ui4DrH1cKk2vkHshcUcGt2lKxCm.jpg',
  'am-i-racist-2024': 'https://image.tmdb.org/t/p/w500/mNpVFXwJtRxoEFTdxTScLy5VyF1.jpg',
};

function download(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    const get = (u) => {
      https.get(u, (res) => {
        if (res.statusCode === 301 || res.statusCode === 302) {
          file.close();
          fs.unlink(dest, () => {});
          return download(res.headers.location, dest).then(resolve).catch(reject);
        }
        if (res.statusCode !== 200) {
          file.close();
          fs.unlink(dest, () => {});
          return reject(new Error(`HTTP ${res.statusCode}`));
        }
        res.pipe(file);
        file.on('finish', () => { file.close(); resolve(dest); });
      }).on('error', (err) => {
        file.close();
        fs.unlink(dest, () => {});
        reject(err);
      });
    };
    get(url);
  });
}

async function main() {
  let downloaded = 0, skipped = 0, failed = 0;
  for (const [slug, url] of Object.entries(posters)) {
    const dest = path.join(POSTER_DIR, `${slug}.jpg`);
    if (fs.existsSync(dest)) {
      console.log(`  (exists) ${slug}`);
      skipped++;
      continue;
    }
    try {
      await download(url, dest);
      const size = fs.statSync(dest).size;
      console.log(`  ✓ ${slug} (${(size/1024).toFixed(0)}KB)`);
      downloaded++;
    } catch (e) {
      console.log(`  ✗ ${slug}: ${e.message}`);
      failed++;
    }
  }
  console.log(`\nDone. Downloaded: ${downloaded}, Skipped: ${skipped}, Failed: ${failed}`);
}

main();
