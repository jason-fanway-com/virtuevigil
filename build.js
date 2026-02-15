#!/usr/bin/env node
/* ============================================
   VirtueVigil — Static Site Builder
   Zero dependencies. Reads reviews.json,
   generates pre-built HTML for every page.
   Run: node build.js
   ============================================ */

const fs = require('fs');
const path = require('path');

// === Config ===
const SITE_URL = 'https://virtuevigil.com';
const BUILD_VERSION = 'v1.7.0';
const SRC = path.join(__dirname, 'src');
const DIST = path.join(__dirname, 'dist');

// === Load reviews ===
const reviews = JSON.parse(fs.readFileSync(path.join(SRC, 'data/reviews.json'), 'utf-8'));
reviews.sort((a, b) => new Date(b.date) - new Date(a.date));

// === Helpers ===
function esc(s) { return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }

function formatDate(d) {
  const dt = new Date(d + 'T00:00:00');
  return dt.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
}

function shortDate(d) {
  const dt = new Date(d + 'T00:00:00');
  return dt.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

function verdictClass(v) {
  if (!v) return 'mixed';
  const lv = v.toUpperCase();
  if (lv === 'WOKE') return 'woke';
  if (lv === 'TRADITIONAL') return 'traditional';
  return 'mixed';
}

function verdictIcon(vc) {
  if (vc === 'woke') return 'exclamation-triangle';
  if (vc === 'traditional') return 'check-circle';
  return 'minus-circle';
}

function posterHTML(r, size) {
  if (r.poster && r.poster.startsWith('http')) {
    const alt = esc(r.title) + ' poster';
    if (size === 'thumb') return `<img src="${r.poster}" alt="${alt}" class="poster-img poster-thumb" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy">`;
    if (size === 'card') return `<img src="${r.poster}" alt="${alt}" class="poster-img poster-card" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy">`;
    if (size === 'featured') return `<img src="${r.poster}" alt="${alt}" class="poster-img poster-featured" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy">`;
    return `<img src="${r.poster}" alt="${alt}" class="poster-img" loading="lazy">`;
  }
  // Styled letter placeholder fallback
  const initial = (r.title || '?').charAt(0).toUpperCase();
  const icon = r.type === 'film' ? 'fa-film' : 'fa-tv';
  if (size === 'thumb') {
    return `<div class="poster-placeholder poster-placeholder-sm" style="width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(135deg,#14141c,#1a1a26);border-radius:4px;"><span class="poster-initial" style="font-size:1.6rem;font-weight:700;color:#c9a84c;">${initial}</span><i class="fas ${icon} poster-type-icon" style="color:#6a6a75;opacity:0.5;font-size:0.6rem;margin-top:4px;"></i></div>`;
  }
  if (size === 'card') {
    return `<div class="poster-placeholder poster-placeholder-md" style="width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(135deg,#14141c,#1a1a26);border-radius:6px;"><span class="poster-initial" style="font-size:2.4rem;font-weight:700;color:#c9a84c;">${initial}</span><i class="fas ${icon} poster-type-icon" style="color:#6a6a75;opacity:0.5;font-size:0.8rem;margin-top:4px;"></i></div>`;
  }
  if (size === 'featured') {
    return `<div class="poster-placeholder poster-placeholder-lg" style="width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(135deg,#14141c,#1a1a26);border-radius:0;"><span class="poster-initial" style="font-size:4rem;font-weight:700;color:#c9a84c;font-family:'Cinzel',Georgia,serif;">${initial}</span><i class="fas ${icon} poster-type-icon" style="color:#6a6a75;opacity:0.5;font-size:1.2rem;margin-top:8px;"></i></div>`;
  }
  return `<div class="poster-placeholder"><span class="poster-initial">${initial}</span></div>`;
}

function pageScripts(extras) {
  const base = `  <script src="/js/main.js"></script>
  <script src="/js/supabase-config.js"></script>
  <script src="/js/auth.js"></script>`;
  if (!extras) return base;
  return base + '\n' + extras.map(s => `  <script src="${s}"></script>`).join('\n');
}

function mkdirp(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function copyRecursive(src, dest) {
  if (!fs.existsSync(src)) return;
  mkdirp(dest);
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function writePage(relPath, html) {
  const fullPath = path.join(DIST, relPath);
  mkdirp(path.dirname(fullPath));
  fs.writeFileSync(fullPath, html);
  console.log(`  ${relPath}`);
}

// Build category data
function getCategories() {
  const cats = {};
  const types = { film: 0, series: 0 };
  let trapCount = 0;
  reviews.forEach(r => {
    if (r.genre) cats[r.genre] = (cats[r.genre] || 0) + 1;
    if (r.type) types[r.type] = (types[r.type] || 0) + 1;
    if (r.wokeTrap && r.wokeTrap.present) trapCount++;
  });
  return { genres: cats, types, trapCount };
}

// ============================================
// TEMPLATE PARTS
// ============================================

function htmlHead({ title, description, keywords, canonical, ogType, ogImage, structuredData, breadcrumbs, extraHead }) {
  // Build structured data array (supports multiple JSON-LD blocks)
  const ldBlocks = [];
  if (structuredData) ldBlocks.push(structuredData);
  if (breadcrumbs) ldBlocks.push(breadcrumbs);

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${esc(title)}</title>
  <meta name="description" content="${esc(description)}">
  ${keywords ? `<meta name="keywords" content="${esc(keywords)}">` : ''}
  <meta name="author" content="VirtueVigil">
  <meta name="robots" content="index, follow">

  <meta property="og:title" content="${esc(title)}">
  <meta property="og:description" content="${esc(description)}">
  <meta property="og:type" content="${ogType || 'website'}">
  ${canonical ? `<meta property="og:url" content="${canonical}">` : ''}
  <meta property="og:image" content="${ogImage || `${SITE_URL}/images/og-default.png`}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="VirtueVigil">
  <meta property="og:locale" content="en_US">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@virtuevigil">
  <meta name="twitter:title" content="${esc(title)}">
  <meta name="twitter:description" content="${esc(description)}">
  <meta name="twitter:image" content="${ogImage || `${SITE_URL}/images/og-default.png`}">

  ${ldBlocks.map(ld => `<script type="application/ld+json">\n  ${JSON.stringify(ld, null, 2).split('\n').join('\n  ')}\n  </script>`).join('\n  ')}
  ${extraHead || ''}

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="/css/styles.css">
  <link rel="icon" type="image/svg+xml" href="/images/logo.svg">
  ${canonical ? `<link rel="canonical" href="${canonical}">` : ''}

  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script>
    window.SUPABASE_URL = 'https://fdxvflryvctvstxdbdtm.supabase.co';
    window.SUPABASE_ANON_KEY = 'sb_publishable_sLwiGeuKX9jNopaeK3Wbqg_gvKcAuhq';
  </script>
</head>`;
}

function topBanner() {
  return `
  <div class="top-banner">
    <span>See the Message Before It Lands &mdash; Subscribe to weekly reviews</span>
  </div>`;
}

function siteHeader(activePage) {
  const navItems = [
    { href: '/', label: 'Reviews', page: 'index' },
    { href: '/woke-trap.html', label: 'What Is a Woke Trap?', page: 'woke-trap' },
    { href: '/methodology.html', label: 'Methodology', page: 'methodology' },
    { href: '/about.html', label: 'About', page: 'about' },
  ];
  return `
  <header class="site-header" role="banner">
    <div class="header-inner">
      <a href="/" class="logo-link" aria-label="VirtueVigil Home">
        <img src="/images/logo.svg" alt="VirtueVigil Logo" width="48" height="48">
        <div class="logo-text">
          <span class="brand"><span>V</span>irtue<span>V</span>igil</span>
          <span class="tagline">Guarding Values. Exposing Agendas.</span>
        </div>
        <span class="version-tag">${BUILD_VERSION}</span>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <i class="fas fa-bars"></i>
      </button>
      <nav class="main-nav" role="navigation" aria-label="Main navigation">
        ${navItems.map(n => `<a href="${n.href}"${n.page === activePage ? ' class="active"' : ''}>${n.label}</a>`).join('\n        ')}
        <a href="/subscribe/" class="nav-cta">Subscribe</a>
      </nav>
      <div class="auth-container">
        <button id="vv-login-btn" class="btn-login">Sign In</button>
        <div id="vv-user-area" class="user-area" style="display:none;">
          <img id="vv-user-avatar" class="avatar-sm" src="" alt="Avatar">
          <span id="vv-user-name" class="user-name"></span>
          <div id="vv-dropdown-menu" class="dropdown-menu">
            <a href="/account/"><i class="fas fa-user"></i> My Profile</a>
            <button id="vv-logout-btn"><i class="fas fa-sign-out-alt"></i> Sign Out</button>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Auth Modal -->
  <div id="vv-auth-modal" class="modal-overlay">
    <div class="modal-content auth-modal">
      <button id="vv-auth-modal-close" class="modal-close" aria-label="Close">&times;</button>
      <h2>Join VirtueVigil</h2>
      <p class="auth-subtitle">Subscribe to comment on reviews and join the community.</p>

      <button id="vv-google-login" class="btn-oauth btn-google">
        <svg width="18" height="18" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
        Continue with Google
      </button>

      <div class="auth-divider"><span>or use email</span></div>

      <form id="vv-email-form">
        <input type="hidden" id="vv-auth-mode-signup" value="">
        <input type="email" id="vv-auth-email" placeholder="Email address" required autocomplete="email">
        <input type="password" id="vv-auth-password" placeholder="Password (min 6 characters)" required minlength="6" autocomplete="current-password">
        <button type="submit" class="btn-auth-submit">Sign In</button>
      </form>

      <div class="auth-links">
        <a href="#" id="vv-auth-mode-toggle"><span id="vv-auth-mode-text">Don't have an account? Sign up</span></a>
        <a href="#" id="vv-forgot-password">Forgot password?</a>
      </div>

      <div id="vv-auth-error" class="auth-msg error" style="display:none;"></div>
      <div id="vv-auth-success" class="auth-msg success" style="display:none;"></div>
    </div>
  </div>`;
}

function sidebarHTML() {
  const recent = reviews.slice(0, 5);
  const cats = getCategories();

  return `
    <aside class="sidebar" role="complementary" aria-label="Sidebar">
      <div class="sidebar-section">
        <h3>Recent Reviews</h3>
        ${recent.map(r => {
          const vc = verdictClass(r.verdict);
          const hasTrap = r.wokeTrap && r.wokeTrap.present;
          let badge = r.verdict;
          if (hasTrap) badge = 'WOKE TRAP';
          else if (vc === 'woke') badge = `WOKE +${r.wokeScore - r.tradScore}`;
          else if (vc === 'traditional') badge = `TRAD +${r.tradScore - r.wokeScore}`;
          return `
        <a href="/reviews/${r.slug}/" class="recent-review">
          <div class="thumb">${posterHTML(r, 'thumb')}</div>
          <div class="info">
            <div class="title">${esc(r.title)}</div>
            <div class="meta">${r.type === 'film' ? 'Film' : 'Series'} &middot; ${shortDate(r.date)}</div>
            <span class="verdict verdict-badge ${hasTrap ? 'trap' : vc}" style="font-size:0.65rem;padding:1px 6px;">${badge}</span>
          </div>
        </a>`;
        }).join('')}
      </div>

      <div class="sidebar-section">
        <h3>Categories</h3>
        <div class="category-list">
          <a href="/category/films/">Film Reviews <span class="count">${cats.types.film}</span></a>
          <a href="/category/series/">Series Reviews <span class="count">${cats.types.series}</span></a>
          <a href="/category/woke-traps/">Woke Trap Alerts <span class="count">${cats.trapCount}</span></a>
          ${Object.entries(cats.genres).sort((a, b) => b[1] - a[1]).map(([g, c]) =>
            `<a href="/category/${g.toLowerCase().replace(/\s+/g, '-')}/">${esc(g)} <span class="count">${c}</span></a>`
          ).join('\n          ')}
        </div>
      </div>

      <div class="sidebar-section" id="subscribe">
        <div class="sidebar-newsletter">
          <h4>The Vigil Report</h4>
          <p>Subscribe to comment on reviews and get weekly Woke Trap alerts.</p>
          <a href="/subscribe/" class="sidebar-subscribe-btn"><i class="fas fa-user-plus"></i> Subscribe Free</a>
        </div>
      </div>

      <div class="sidebar-section">
        <h3>Follow Us</h3>
        <div class="social-links" style="justify-content:center;">
          <a href="https://youtube.com/@virtuevigil" aria-label="YouTube" target="_blank" rel="noopener"><i class="fab fa-youtube"></i></a>
          <a href="https://instagram.com/virtuevigil" aria-label="Instagram" target="_blank" rel="noopener"><i class="fab fa-instagram"></i></a>
          <a href="https://facebook.com/virtuevigil" aria-label="Facebook" target="_blank" rel="noopener"><i class="fab fa-facebook-f"></i></a>
          <a href="https://tiktok.com/@virtuevigil" aria-label="TikTok" target="_blank" rel="noopener"><i class="fab fa-tiktok"></i></a>
        </div>
      </div>
    </aside>`;
}

function fullFooter() {
  return `
  <footer class="site-footer" role="contentinfo">
    <div class="footer-inner">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="logo-mark">
            <img src="/images/logo.svg" alt="VirtueVigil" width="40" height="40">
            <span>VirtueVigil</span>
          </div>
          <p>Values-based classification of modern film and television. Clarity before consumption.</p>
          <div class="social-links">
            <a href="https://youtube.com/@virtuevigil" aria-label="YouTube" target="_blank" rel="noopener"><i class="fab fa-youtube"></i></a>
            <a href="https://instagram.com/virtuevigil" aria-label="Instagram" target="_blank" rel="noopener"><i class="fab fa-instagram"></i></a>
            <a href="https://facebook.com/virtuevigil" aria-label="Facebook" target="_blank" rel="noopener"><i class="fab fa-facebook-f"></i></a>
            <a href="https://tiktok.com/@virtuevigil" aria-label="TikTok" target="_blank" rel="noopener"><i class="fab fa-tiktok"></i></a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Navigate</h4>
          <a href="/">All Reviews</a>
          <a href="/woke-trap.html">What Is a Woke Trap?</a>
          <a href="/methodology.html">Our Methodology</a>
          <a href="/about.html">About VirtueVigil</a>
        </div>
        <div class="footer-col">
          <h4>Categories</h4>
          <a href="/category/films/">Film Reviews</a>
          <a href="/category/series/">Series Reviews</a>
          <a href="/category/woke-traps/">Woke Trap Alerts</a>
        </div>
        <div class="footer-col">
          <h4>Connect</h4>
          <a href="https://youtube.com/@virtuevigil" target="_blank" rel="noopener">YouTube Channel</a>
          <a href="https://instagram.com/virtuevigil" target="_blank" rel="noopener">Instagram</a>
          <a href="https://facebook.com/virtuevigil" target="_blank" rel="noopener">Facebook Page</a>
          <a href="https://tiktok.com/@virtuevigil" target="_blank" rel="noopener">TikTok</a>
          <a href="mailto:hello@virtuevigil.com">Contact Us</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; ${new Date().getFullYear()} VirtueVigil. All rights reserved. Guarding Values. Exposing Agendas.</p>
        <p><a href="#">Privacy Policy</a> &middot; <a href="#">Terms of Use</a></p>
      </div>
    </div>
  </footer>`;
}

function simpleFooter() {
  return `
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-bottom">
        <p>&copy; ${new Date().getFullYear()} VirtueVigil. All rights reserved. Guarding Values. Exposing Agendas.</p>
        <p>
          <a href="/">Reviews</a> &middot;
          <a href="/woke-trap.html">Woke Trap</a> &middot;
          <a href="/methodology.html">Methodology</a> &middot;
          <a href="/about.html">About</a>
        </p>
      </div>
    </div>
  </footer>`;
}

// ============================================
// REVIEW PAGE COMPONENTS
// ============================================

function scorePanel(r) {
  return `
        <div class="score-panel">
          <div class="score-item"><div class="label">Woke Score</div><div class="value woke">${r.wokeScore}</div></div>
          <div class="score-item"><div class="label">Traditional Score</div><div class="value trad">${r.tradScore}</div></div>
          <div class="score-item"><div class="label">Authenticity Index</div><div class="value auth">${r.authIndex}%</div></div>
          <div class="score-item"><div class="label">Score Margin</div><div class="value margin">${esc(r.scoreMargin)}</div></div>
        </div>`;
}

function insightGrid(r) {
  return `
          <div class="insight-grid">
            <div class="insight-card">
              <h4><i class="fas fa-user-tie" style="color:var(--accent-blue);"></i> Adult Viewer Insight</h4>
              <p>${esc(r.summary.adultInsight)}</p>
            </div>
            <div class="insight-card">
              <h4><i class="fas fa-child" style="color:var(--accent-amber);"></i> Parental Guidance</h4>
              <p>${esc(r.summary.parentalGuidance)}</p>
            </div>
          </div>`;
}

function wokeTrapAlert(r) {
  if (!r.wokeTrap || !r.wokeTrap.present) return '';
  return `
          <div class="woke-trap-alert">
            <h4><i class="fas fa-exclamation-circle"></i> Woke Trap Warning</h4>
            <p><strong>Trap Present:</strong> Yes &mdash; <strong>Degree: ${esc(r.wokeTrap.degree)}.</strong> ${esc(r.wokeTrap.explanation)}</p>
          </div>`;
}

function tropeTable(r) {
  if (!r.tropeAudit || !r.tropeAudit.length) return '';
  return `
          <div class="section-label" style="margin-top:28px;">Trope Audit</div>
          <table class="trope-table">
            <thead>
              <tr><th>Trope</th><th>Category</th><th>Location</th><th>Authenticity</th></tr>
            </thead>
            <tbody>
              ${r.tropeAudit.map(t => `
              <tr>
                <td>${esc(t.trope)}</td>
                <td><span class="tag ${t.category === 'WOKE' ? 'woke' : 'trad'}">${esc(t.category)}</span></td>
                <td>${esc(t.location)}</td>
                <td class="${t.authenticity === 'Forced' ? 'forced' : 'natural'}">${esc(t.authenticity)}</td>
              </tr>`).join('')}
            </tbody>
          </table>`;
}

function overallParagraphs(r) {
  return r.summary.overall.split('\n').filter(p => p.trim()).map(p => `<p>${esc(p)}</p>`).join('\n          ');
}

// ============================================
// PAGE BUILDERS
// ============================================

function buildHomepage() {
  const featured = reviews[0];
  const moreReviews = reviews.slice(1, 5);
  const vc = verdictClass(featured.verdict);
  const hasTrap = featured.wokeTrap && featured.wokeTrap.present;

  const structuredData = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "VirtueVigil",
    "alternateName": "Virtue Vigil",
    "url": SITE_URL,
    "description": "Conservative movie and TV show reviews with Woke Score ratings, Woke Trap detection, and family viewing guidance.",
    "publisher": {
      "@type": "Organization",
      "name": "VirtueVigil",
      "logo": { "@type": "ImageObject", "url": `${SITE_URL}/images/logo.svg` },
      "sameAs": [
        "https://youtube.com/@virtuevigil",
        "https://instagram.com/virtuevigil",
        "https://facebook.com/virtuevigil",
        "https://tiktok.com/@virtuevigil"
      ]
    },
    "potentialAction": {
      "@type": "SearchAction",
      "target": `${SITE_URL}/?q={search_term_string}`,
      "query-input": "required name=search_term_string"
    }
  };

  return `${htmlHead({
    title: 'VirtueVigil \u2014 Is It Woke? Conservative Movie & TV Reviews | Woke Score Ratings',
    description: 'Is it woke? VirtueVigil exposes ideological messaging in movies and TV shows with Woke Score ratings, Woke Trap detection, and family viewing guidance. The conservative alternative to Rotten Tomatoes.',
    keywords: 'is it woke, woke movies, woke TV shows, conservative movie reviews, woke trap, family friendly movies, values-based movie reviews, woke score, traditional values, anti-woke entertainment',
    canonical: SITE_URL,
    structuredData
  })}
<body>
  ${topBanner()}
  ${siteHeader('index')}

  <!-- Hero Section -->
  <section class="hero" role="banner">
    <div class="hero-inner">
      <div class="hero-content">
        <h1>Exposing <span>Ideology</span><br>in Entertainment</h1>
        <p class="subtitle">VirtueVigil exists to expose ideological messaging in modern film and television &mdash; especially when it is disguised, delayed, or delivered only after viewers are emotionally invested. We provide values-based classification so families can see what a story is really saying before it says it.</p>
        <a href="#latest-review" class="hero-cta">
          Read Latest Review <i class="fas fa-arrow-right"></i>
        </a>
      </div>
      <div class="hero-image" style="flex:0 0 520px;">
        <div class="hero-video" style="position:relative;">
          <video id="heroVideo" width="520" height="293" poster="/images/video-poster.jpg" preload="metadata"
            style="width:100%;height:auto;border-radius:10px;border:2px solid rgba(201,168,76,0.3);box-shadow:0 0 30px rgba(201,168,76,0.08);display:block;background:#000;object-fit:cover;">
            <source src="/images/what-is-virtuevigil.mp4" type="video/mp4">
          </video>
          <div id="videoPlayBtn" onclick="document.getElementById('heroVideo').play();this.style.display='none';"
            style="position:absolute;top:0;left:0;width:100%;height:100%;display:flex;align-items:center;justify-content:center;cursor:pointer;border-radius:10px;background:rgba(0,0,0,0.25);transition:background 0.3s;">
            <div style="width:64px;height:64px;border-radius:50%;background:rgba(201,168,76,0.9);display:flex;align-items:center;justify-content:center;box-shadow:0 0 24px rgba(201,168,76,0.4);transition:transform 0.2s;">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="#0d0d12"><polygon points="6,3 20,12 6,21"/></svg>
            </div>
          </div>
          <script>
            (function(){
              var v=document.getElementById('heroVideo'),b=document.getElementById('videoPlayBtn');
              v.addEventListener('play',function(){b.style.display='none';v.setAttribute('controls','controls');});
              v.addEventListener('pause',function(){if(v.currentTime>0&&!v.ended){b.style.display='flex';}});
              v.addEventListener('ended',function(){b.style.display='flex';v.removeAttribute('controls');});
            })();
          </script>
        </div>
        <span class="caption"><i class="fas fa-play-circle"></i> What Is VirtueVigil?</span>
      </div>
    </div>
  </section>

  <!-- Main Layout -->
  <div class="page-layout">
    ${sidebarHTML()}

    <main class="main-content" role="main">
      <!-- FEATURED REVIEW -->
      <article class="featured-review" id="latest-review" itemscope itemtype="https://schema.org/Review">
        <div class="featured-header">
          <div class="featured-header-layout" style="display:flex;gap:28px;align-items:flex-start;">
            <div class="featured-header-text" style="flex:1;min-width:0;">
              <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;flex-wrap:wrap;">
                <span class="verdict-badge ${vc}"><i class="fas fa-${verdictIcon(vc)}"></i> ${esc(featured.verdict)}</span>
                ${hasTrap ? '<span class="verdict-badge trap"><i class="fas fa-eye-slash"></i> WOKE TRAP DETECTED</span>' : ''}
              </div>
              <h2 class="review-title" itemprop="name">${esc(featured.title)}</h2>
              <p class="review-subtitle" itemprop="description">${esc(featured.summary.overall.split('\n')[0].substring(0, 160))}...</p>
              <div class="featured-meta">
                <span><i class="fas fa-${featured.type === 'film' ? 'film' : 'tv'}"></i> ${featured.type === 'film' ? 'Film' : 'Series'} &middot; ${esc(featured.platform)}</span>
                <span><i class="fas fa-calendar"></i> <time datetime="${featured.date}" itemprop="datePublished">${formatDate(featured.date)}</time></span>
                <span><i class="fas fa-user-edit"></i> Analyzed by <span itemprop="author">${esc(featured.author)}</span></span>
                <span><i class="fas fa-clock"></i> ${esc(featured.readTime)} read</span>
              </div>
            </div>
            <div class="featured-poster-wrap" style="flex:0 0 160px;width:160px;height:230px;border-radius:10px;overflow:hidden;border:2px solid rgba(201,168,76,0.3);">
              ${posterHTML(featured, 'featured')}
            </div>
          </div>
        </div>

        ${scorePanel(featured)}

        <div class="featured-body" itemprop="reviewBody">
          <div class="section-label">Overall Perspective</div>
          ${overallParagraphs(featured)}
          ${insightGrid(featured)}
          ${wokeTrapAlert(featured)}
          ${tropeTable(featured)}
          <a href="/reviews/${featured.slug}/" class="read-more-btn">Read Full Analysis <i class="fas fa-arrow-right"></i></a>
        </div>
      </article>

      <!-- More Reviews -->
      <div class="section-header">
        <h2>More Reviews</h2>
        <a href="/category/films/" class="view-all">View All Reviews <i class="fas fa-arrow-right"></i></a>
      </div>

      ${moreReviews.map(r => {
        const rvc = verdictClass(r.verdict);
        const rTrap = r.wokeTrap && r.wokeTrap.present;
        const excerpt = r.summary.overall.split('\n')[0].substring(0, 250);
        return `
      <article class="review-card">
        <div class="review-card-inner">
          <div class="poster">${posterHTML(r, 'card')}</div>
          <div class="review-card-content">
            <h3><a href="/reviews/${r.slug}/">${esc(r.title)}</a></h3>
            <div class="review-meta">
              <span class="verdict-badge ${rTrap ? 'trap' : rvc}" style="font-size:0.65rem;padding:2px 8px;margin-right:8px;">
                ${rTrap ? '<i class="fas fa-eye-slash"></i> WOKE TRAP' : esc(r.verdict)}
              </span>
              ${r.type === 'film' ? 'Film' : 'Series'} &middot; ${esc(r.platform)} &middot; ${shortDate(r.date)}
            </div>
            <p class="excerpt">${esc(excerpt)}...</p>
            <div class="review-card-scores">
              <span class="mini-score woke">WOKE: ${r.wokeScore}</span>
              <span class="mini-score trad">TRAD: ${r.tradScore}</span>
              <span class="mini-score" style="color:var(--accent-amber);">AUTH: ${r.authIndex}%</span>
            </div>
          </div>
        </div>
      </article>`;
      }).join('')}

      <!-- Spokesperson -->
      <section class="spokesperson" id="about-debra">
        <img src="/images/debra-ducane.png" alt="Debra Ducane \u2014 VirtueVigil Cultural Sentinel" width="180" height="180" loading="lazy">
        <div class="spokesperson-info">
          <h3>Debra Ducane</h3>
          <div class="role">Cultural Sentinel</div>
          <p>Debra is the voice of VirtueVigil. Her role is as sentinel &mdash; explaining each analysis on our review videos and explainer content. She delivers findings with calm conviction: direct, unapologetic, and more disappointed than angry.</p>
          <blockquote>&ldquo;We are not impartial, but we are deliberate. When a story stops being a story and starts being instruction, we call it out. Subscribe if that matters to you.&rdquo;</blockquote>
        </div>
      </section>
    </main>
  </div>

  ${fullFooter()}
${pageScripts()}
</body>
</html>`;
}


function buildReviewPage(r) {
  const vc = verdictClass(r.verdict);
  const hasTrap = r.wokeTrap && r.wokeTrap.present;
  const seo = r.seo || {};
  const title = seo.titleTag || `Is ${r.title} Woke? | VirtueVigil`;
  const desc = seo.metaDescription || `VirtueVigil review of ${r.title}. Woke Score ${r.wokeScore}, Traditional ${r.tradScore}.`;
  const kw = seo.keywords || '';
  const canonical = `${SITE_URL}/reviews/${r.slug}/`;
  const ogImage = (r.poster && r.poster.startsWith('http')) ? r.poster : undefined;

  const structuredData = {
    "@context": "https://schema.org",
    "@type": "Review",
    "name": r.title,
    "author": { "@type": "Person", "name": r.author },
    "datePublished": r.date,
    "reviewBody": r.summary.overall.substring(0, 500),
    "publisher": { "@type": "Organization", "name": "VirtueVigil" },
    "itemReviewed": Object.assign({
      "@type": r.type === 'film' ? "Movie" : "TVSeries",
      "name": r.title,
      "datePublished": String(r.year)
    }, ogImage ? { "image": ogImage } : {}),
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": r.authIndex,
      "bestRating": 100,
      "worstRating": 0
    }
  };

  // Previous / Next navigation
  const idx = reviews.findIndex(rv => rv.id === r.id);
  const prev = idx < reviews.length - 1 ? reviews[idx + 1] : null;
  const next = idx > 0 ? reviews[idx - 1] : null;

  const reviewBreadcrumbs = breadcrumbLD([
    { name: 'Home', url: SITE_URL },
    { name: 'Reviews', url: `${SITE_URL}/` },
    { name: r.title, url: canonical }
  ]);

  return `${htmlHead({ title, description: desc, keywords: kw, canonical, ogType: 'article', ogImage, structuredData, breadcrumbs: reviewBreadcrumbs, extraHead: '<style>.review-detail::before{display:none!important;content:none!important;}</style>' })}
<body>
  ${topBanner()}
  ${siteHeader('index')}

  <div class="page-layout">
    ${sidebarHTML()}

    <main class="main-content" role="main">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/">Home</a> <span>&rsaquo;</span>
        <a href="/">Reviews</a> <span>&rsaquo;</span>
        <span>${esc(r.title)}</span>
      </nav>

      <article class="featured-review review-detail" style="position:relative;" itemscope itemtype="https://schema.org/Review">
        <div class="featured-header">
          <div class="featured-header-layout" style="display:flex;gap:28px;align-items:flex-start;">
            <div class="featured-header-text" style="flex:1;min-width:0;">
              <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;flex-wrap:wrap;">
                <span class="verdict-badge ${vc}"><i class="fas fa-${verdictIcon(vc)}"></i> ${esc(r.verdict)}</span>
                ${hasTrap ? '<span class="verdict-badge trap"><i class="fas fa-eye-slash"></i> WOKE TRAP DETECTED</span>' : ''}
              </div>
              <h2 class="review-title" itemprop="name">${esc(r.title)}</h2>
              <p class="review-subtitle" itemprop="description">${esc(r.summary.overall.split('\n')[0].substring(0, 200))}</p>
              <div class="featured-meta">
                <span><i class="fas fa-${r.type === 'film' ? 'film' : 'tv'}"></i> ${r.type === 'film' ? 'Film' : 'Series'} &middot; ${esc(r.platform)}</span>
                <span><i class="fas fa-calendar"></i> <time datetime="${r.date}" itemprop="datePublished">${formatDate(r.date)}</time></span>
                <span><i class="fas fa-user-edit"></i> Analyzed by <span itemprop="author">${esc(r.author)}</span></span>
                <span><i class="fas fa-clock"></i> ${esc(r.readTime)} read</span>
              </div>
            </div>
            <div class="featured-poster-wrap" style="flex:0 0 160px;width:160px;height:230px;border-radius:10px;overflow:hidden;border:2px solid rgba(201,168,76,0.3);">
              ${posterHTML(r, 'featured')}
            </div>
          </div>
        </div>

        ${scorePanel(r)}

        <div class="featured-body" itemprop="reviewBody">
          <div class="section-label">Overall Perspective</div>
          ${overallParagraphs(r)}
          ${insightGrid(r)}
          ${wokeTrapAlert(r)}
          ${tropeTable(r)}
        </div>
      </article>

      <!-- Comments Section -->
      <div class="comments-section" data-slug="${esc(r.slug)}">
        <div class="comments-header">
          <h3><i class="fas fa-comments"></i> Community Discussion <span id="vv-comment-count" class="comment-count">0</span></h3>
        </div>

        <div id="comment-subscribe-prompt" class="subscribe-prompt">
          <div class="subscribe-prompt-inner">
            <i class="fas fa-lock"></i>
            <div>
              <p><strong>Subscribe to comment.</strong></p>
              <p>Join the VirtueVigil community to share your perspective on this review.</p>
            </div>
            <a href="/subscribe/" class="btn-subscribe-cta">Sign In / Subscribe</a>
          </div>
        </div>

        <div id="comment-form-container" style="display:none;">
          <form id="vv-comment-form" class="comment-form">
            <textarea id="vv-comment-input" placeholder="Share your thoughts on this review..." maxlength="2000" rows="4"></textarea>
            <div class="comment-form-footer">
              <span id="vv-char-count" class="char-count">0 / 2000</span>
              <button type="submit" class="btn-post-comment">Post Comment</button>
            </div>
          </form>
        </div>

        <div id="vv-comments-list" class="comments-list"></div>
      </div>

      <!-- Previous / Next -->
      <div style="display:flex;justify-content:space-between;margin:30px 0;gap:16px;flex-wrap:wrap;">
        ${prev ? `<a href="/reviews/${prev.slug}/" style="color:var(--gold);font-weight:600;font-size:0.9rem;"><i class="fas fa-arrow-left"></i> ${esc(prev.title)}</a>` : '<span></span>'}
        ${next ? `<a href="/reviews/${next.slug}/" style="color:var(--gold);font-weight:600;font-size:0.9rem;">${esc(next.title)} <i class="fas fa-arrow-right"></i></a>` : '<span></span>'}
      </div>
    </main>
  </div>

  ${fullFooter()}
${pageScripts(['/js/comments.js'])}
</body>
</html>`;
}


function buildCategoryPage(name, slug, categoryReviews) {
  const title = `${name} \u2014 VirtueVigil Reviews`;
  const desc = `Browse VirtueVigil's ${name.toLowerCase()} reviews with Woke Score ratings, Woke Trap detection, and family guidance.`;
  const canonical = `${SITE_URL}/category/${slug}/`;

  const catStructuredData = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": `${name} — VirtueVigil Reviews`,
    "description": desc,
    "url": canonical,
    "publisher": { "@type": "Organization", "name": "VirtueVigil" },
    "mainEntity": {
      "@type": "ItemList",
      "numberOfItems": categoryReviews.length,
      "itemListElement": categoryReviews.map((r, i) => ({
        "@type": "ListItem",
        "position": i + 1,
        "url": `${SITE_URL}/reviews/${r.slug}/`,
        "name": r.title
      }))
    }
  };

  const catBreadcrumbs = breadcrumbLD([
    { name: 'Home', url: SITE_URL },
    { name: name, url: canonical }
  ]);

  return `${htmlHead({ title, description: desc, canonical, structuredData: catStructuredData, breadcrumbs: catBreadcrumbs })}
<body>
  ${topBanner()}
  ${siteHeader('index')}

  <section class="page-hero">
    <div class="container">
      <h1><span class="text-gold">${esc(name)}</span></h1>
      <p>${categoryReviews.length} review${categoryReviews.length !== 1 ? 's' : ''} in this category.</p>
    </div>
  </section>

  <div class="page-layout">
    ${sidebarHTML()}

    <main class="main-content" role="main">
      ${categoryReviews.map(r => {
        const rvc = verdictClass(r.verdict);
        const rTrap = r.wokeTrap && r.wokeTrap.present;
        const excerpt = r.summary.overall.split('\n')[0].substring(0, 250);
        return `
      <article class="review-card">
        <div class="review-card-inner">
          <div class="poster">${posterHTML(r, 'card')}</div>
          <div class="review-card-content">
            <h3><a href="/reviews/${r.slug}/">${esc(r.title)}</a></h3>
            <div class="review-meta">
              <span class="verdict-badge ${rTrap ? 'trap' : rvc}" style="font-size:0.65rem;padding:2px 8px;margin-right:8px;">
                ${rTrap ? '<i class="fas fa-eye-slash"></i> WOKE TRAP' : esc(r.verdict)}
              </span>
              ${r.type === 'film' ? 'Film' : 'Series'} &middot; ${esc(r.platform)} &middot; ${formatDate(r.date)}
            </div>
            <p class="excerpt">${esc(excerpt)}...</p>
            <div class="review-card-scores">
              <span class="mini-score woke">WOKE: ${r.wokeScore}</span>
              <span class="mini-score trad">TRAD: ${r.tradScore}</span>
              <span class="mini-score" style="color:var(--accent-amber);">AUTH: ${r.authIndex}%</span>
            </div>
          </div>
        </div>
      </article>`;
      }).join('')}
    </main>
  </div>

  ${fullFooter()}
${pageScripts()}
</body>
</html>`;
}


function buildAboutPage() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "VirtueVigil",
    "description": "Values-based media review platform exposing ideological messaging in modern film and television.",
    "url": SITE_URL,
    "logo": `${SITE_URL}/images/logo.svg`,
    "sameAs": [
      "https://youtube.com/@virtuevigil",
      "https://instagram.com/virtuevigil",
      "https://facebook.com/virtuevigil",
      "https://tiktok.com/@virtuevigil"
    ]
  };

  return `${htmlHead({
    title: 'About VirtueVigil \u2014 Guarding Values, Exposing Agendas',
    description: 'VirtueVigil is a values-based media review platform that exposes ideological messaging in modern film and television, with a focus on delayed narrative manipulation.',
    keywords: 'about VirtueVigil, media review platform, cultural analysis, entertainment ideology, Debra Ducane',
    canonical: `${SITE_URL}/about.html`,
    structuredData
  })}
<body>
  ${siteHeader('about')}

  <section class="page-hero">
    <div class="container">
      <h1>About <span class="text-gold">VirtueVigil</span></h1>
      <p>We exist to expose ideological messaging in entertainment &mdash; especially when it is disguised, delayed, or delivered only after viewers are emotionally invested.</p>
    </div>
  </section>

  <article class="content-article">
    <h2>Our Mission</h2>
    <p>The entertainment landscape in 2026 is characterized by unprecedented ideological fragmentation. For conservative parents and discerning adult viewers, navigating the vast output of streaming content has become a source of &ldquo;viewer fatigue.&rdquo;</p>
    <p>A primary grievance is the &ldquo;ideological bait-and-switch&rdquo; &mdash; where a program draws in an audience with traditional narrative beats before pivoting to progressive social theories mid-series. VirtueVigil addresses this through high-density analysis of content, providing values-based classification so families can see what a story is really saying before it says it.</p>

    <div class="highlight-box">
      <p>We are not impartial, but we are deliberate. When a story stops being a story and starts being instruction, we call it out.</p>
    </div>

    <h2>Our Tone</h2>
    <p>VirtueVigil operates with what we call <strong>sentinel tone</strong> &mdash; not activist tone. This means:</p>
    <ul>
      <li>Direct, unapologetic language</li>
      <li>Explicit moral judgment is allowed</li>
      <li>No performative anger, no sarcasm, no mockery</li>
      <li>No pleading with the audience</li>
      <li>Calm delivery, firm conclusions</li>
      <li>Agendas are named, not hinted</li>
    </ul>
    <p>The tone is more disappointed than angry. It reflects the posture of someone who expected better from storytellers and is documenting exactly where they fell short.</p>

    <h2>Meet Debra Ducane</h2>
    <div class="spokesperson" style="margin-top:20px;">
      <img src="/images/debra-ducane.png" alt="Debra Ducane, Cultural Sentinel" width="180" height="180" loading="lazy">
      <div class="spokesperson-info">
        <h3>Debra Ducane</h3>
        <div class="role">Cultural Sentinel &amp; Digital Spokesperson</div>
        <p>Debra is the face and voice of VirtueVigil. Her role is as sentinel &mdash; explaining each analysis on our review videos and explainer content. She delivers findings with calm conviction, appearing across review videos and explainer content with consistent presence and authority.</p>
        <blockquote>&ldquo;VirtueVigil exposes ideological messaging in modern entertainment, with a focus on progressive narratives that are often hidden beneath the surface or revealed only after emotional investment. We are not impartial, but we are deliberate. Subscribe if that matters to you.&rdquo;</blockquote>
      </div>
    </div>

    <h2>What We Believe</h2>
    <p>We believe that entertainment is one of the primary channels through which ideological messaging reaches audiences &mdash; including children and families who are not expecting it and have not consented to it.</p>
    <p>We believe that transparency matters. When a film or series is openly ideological from the start, viewers can make an informed choice. When the ideology is hidden, delayed, or embedded after trust is built, that choice is denied.</p>
    <p>We believe in naming what we see, clearly and without apology, while maintaining the discipline to avoid descending into outrage, sarcasm, or mockery.</p>

    <h2>What We Do</h2>
    <div class="about-grid">
      <div class="about-card">
        <h3><i class="fas fa-search" style="color:var(--gold);"></i> Analyze</h3>
        <p>Every title undergoes a structured analysis using our Vigil-Schema framework, producing detailed trope audits with density-based scoring.</p>
      </div>
      <div class="about-card">
        <h3><i class="fas fa-tags" style="color:var(--gold);"></i> Classify</h3>
        <p>Content is classified with WOKE, TRADITIONAL, and MIXED ratings along with Woke Trap detection and Authenticity Index scoring.</p>
      </div>
      <div class="about-card">
        <h3><i class="fas fa-shield-alt" style="color:var(--gold);"></i> Protect</h3>
        <p>Every review includes parental guidance, adult viewer insight, and clear flagging of ideological content &mdash; especially when delayed.</p>
      </div>
      <div class="about-card">
        <h3><i class="fas fa-users" style="color:var(--gold);"></i> Empower</h3>
        <p>We restore viewer agency by providing the information needed to make informed entertainment choices before time is invested.</p>
      </div>
    </div>

    <h2>Connect With Us</h2>
    <p>VirtueVigil is growing across platforms. Follow us for reviews, Woke Trap alerts, and explainer content:</p>
    <div class="social-links" style="margin:20px 0;gap:16px;">
      <a href="https://youtube.com/@virtuevigil" target="_blank" rel="noopener" style="width:auto;padding:10px 20px;font-size:0.9rem;gap:8px;display:inline-flex;"><i class="fab fa-youtube"></i> YouTube</a>
      <a href="https://instagram.com/virtuevigil" target="_blank" rel="noopener" style="width:auto;padding:10px 20px;font-size:0.9rem;gap:8px;display:inline-flex;"><i class="fab fa-instagram"></i> Instagram</a>
      <a href="https://facebook.com/virtuevigil" target="_blank" rel="noopener" style="width:auto;padding:10px 20px;font-size:0.9rem;gap:8px;display:inline-flex;"><i class="fab fa-facebook-f"></i> Facebook</a>
      <a href="https://tiktok.com/@virtuevigil" target="_blank" rel="noopener" style="width:auto;padding:10px 20px;font-size:0.9rem;gap:8px;display:inline-flex;"><i class="fab fa-tiktok"></i> TikTok</a>
    </div>

    <div class="highlight-box">
      <p>Clarity before consumption. That is our purpose.</p>
    </div>

    <div style="text-align:center;margin-top:40px;">
      <a href="/" class="hero-cta">Browse Reviews <i class="fas fa-arrow-right"></i></a>
    </div>
  </article>

  ${simpleFooter()}
${pageScripts()}
</body>
</html>`;
}


function buildMethodologyPage() {
  return `${htmlHead({
    title: 'Our Methodology \u2014 VirtueVigil',
    description: 'How VirtueVigil analyzes entertainment content using density-based scoring, trope auditing, and the Vigil-Schema analytical framework.',
    keywords: 'VirtueVigil methodology, media analysis, woke score, traditional score, authenticity index, trope audit, Vigil-Schema',
    canonical: `${SITE_URL}/methodology.html`,
    ogType: 'article'
  })}
<body>
  ${siteHeader('methodology')}

  <section class="page-hero">
    <div class="container">
      <h1>Our <span class="text-gold">Methodology</span></h1>
      <p>How VirtueVigil classifies content &mdash; the scoring system, trope auditing, and the analytical framework behind every review.</p>
    </div>
  </section>

  <article class="content-article">
    <h2>The Vigil-Schema</h2>
    <p>Every VirtueVigil review is generated through a structured analytical pipeline we call the <strong>Vigil-Schema</strong>. This framework ensures consistency, objectivity in measurement, and transparency in how classifications are determined.</p>
    <p>The system operates on a principle of <strong>density-based scoring</strong> &mdash; counting verified instances of specific narrative tropes rather than relying on subjective impression. Every trope identified is logged, categorized, and mapped against an authenticity standard.</p>

    <h2>The Three Core Scores</h2>
    <div class="about-grid" style="margin-bottom:20px;">
      <div class="about-card" style="border-left:4px solid var(--accent-red);">
        <h3 style="color:var(--accent-red);"><i class="fas fa-arrow-up"></i> WOKE Score</h3>
        <p>+1 point for every verified instance of a WOKE trope. This includes group categorization over individual agency, subversion of traditional structures (nuclear family, religious institutions, national identity), identity-based moral authority, and systemic framing of personal conflict.</p>
      </div>
      <div class="about-card" style="border-left:4px solid var(--accent-green);">
        <h3 style="color:var(--accent-green);"><i class="fas fa-arrow-up"></i> TRADITIONAL Score</h3>
        <p>+1 point for every verified instance of a TRADITIONAL trope. This includes individual virtue and responsibility, respect for family and faith, meritocratic outcomes, earned moral authority, and consequence-based storytelling.</p>
      </div>
    </div>
    <div class="about-card" style="border-left:4px solid var(--accent-amber);margin-bottom:30px;">
      <h3 style="color:var(--accent-amber);"><i class="fas fa-percentage"></i> Authenticity Index</h3>
      <p>A percentage reflecting how much of the content feels &ldquo;Natural&rdquo; versus &ldquo;Forced.&rdquo; This measures whether ideological elements emerge organically from the story&rsquo;s internal logic or are externally imposed upon it. A high authenticity index means the messaging &mdash; regardless of direction &mdash; is integrated naturally. A low index indicates didactic or preachy delivery.</p>
    </div>

    <h2>The Score Margin</h2>
    <p>The Score Margin is the net difference between the WOKE and TRADITIONAL scores. A margin of +14 WOKE means there were 14 more verified WOKE trope instances than TRADITIONAL ones. This provides a single, scannable indicator of overall ideological direction.</p>

    <h2>The Trope Audit Log</h2>
    <p>Every review includes a Trope Audit Log &mdash; a detailed record of each identified trope instance. For each trope, the following fields are documented:</p>
    <ul>
      <li><strong>Category</strong> &mdash; WOKE or TRADITIONAL classification</li>
      <li><strong>Trope Name</strong> &mdash; A standardized identifier (e.g., &ldquo;Subversion of Traditional Motherhood&rdquo;)</li>
      <li><strong>Location</strong> &mdash; Where in the narrative the trope appears (act, scene, or timestamp)</li>
      <li><strong>Script Context</strong> &mdash; Relevant dialogue or scene description</li>
      <li><strong>Moral Impact</strong> &mdash; How the trope affects the story&rsquo;s moral framework</li>
      <li><strong>Authenticity Verdict</strong> &mdash; Whether the instance is FORCED or NATURAL</li>
    </ul>
    <p>This granular logging ensures that every classification can be challenged, verified, and discussed on the basis of specific evidence rather than general impression.</p>

    <h2>Woke Trap Detection</h2>
    <p>The system includes specific logic for Woke Trap detection. If the first explicit WOKE trope instance occurs after approximately 50% of the content&rsquo;s runtime or token count, the Woke Trap flag is set to YES. The system then records:</p>
    <ul>
      <li>The degree of the trap (Low, Medium, or High)</li>
      <li>An editorial explanation of where the bait-and-switch occurred</li>
      <li>A viewer sentiment commentary describing the likely feeling of betrayal</li>
    </ul>

    <h2>Three Perspective Summaries</h2>
    <p>Every review concludes with three distinct perspective summaries, each designed for a different audience:</p>
    <div class="about-grid">
      <div class="about-card">
        <h3><i class="fas fa-eye" style="color:var(--accent-blue);"></i> Overall Perspective</h3>
        <p>A sentinel-style overview of the content&rsquo;s ideological density. This is the flagship analysis &mdash; what VirtueVigil&rsquo;s assessment is and why.</p>
      </div>
      <div class="about-card">
        <h3><i class="fas fa-user-tie" style="color:var(--accent-blue);"></i> Adult Viewer Insight</h3>
        <p>An analysis of narrative quality, time-investment value, and where the content prioritizes messaging over storytelling. For adult viewers making their own viewing decisions.</p>
      </div>
    </div>
    <div class="about-card" style="margin-bottom:30px;">
      <h3><i class="fas fa-child" style="color:var(--accent-amber);"></i> Parental Guidance</h3>
      <p>Specific, actionable advice for parents selecting content for children and teens. Identifies themes that may conflict with traditional family values, including gender identity presentation, authority subversion, and moral relativism.</p>
    </div>

    <h2>Community Governance</h2>
    <p>VirtueVigil is building a Community Weighted Score system where members can vote on whether an AI-identified trope was actually FORCED or NATURAL. This crowdsourced layer adds human judgment to our automated analysis, creating a more robust and accountable classification system.</p>

    <div class="highlight-box">
      <p>Our methodology is transparent by design. Every score can be traced to specific evidence. Every classification can be debated on its merits.</p>
    </div>

    <div style="text-align:center;margin-top:40px;">
      <a href="/" class="hero-cta">See It In Action <i class="fas fa-arrow-right"></i></a>
    </div>
  </article>

  ${simpleFooter()}
${pageScripts()}
</body>
</html>`;
}


function buildWokeTrapPage() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "What Is a Woke Trap?",
    "description": "A Woke Trap is a narrative technique where ideological messaging is intentionally delayed until after the viewer is emotionally invested in the story.",
    "publisher": { "@type": "Organization", "name": "VirtueVigil" },
    "author": { "@type": "Person", "name": "Debra Ducane" }
  };

  return `${htmlHead({
    title: 'What Is a Woke Trap? \u2014 VirtueVigil',
    description: 'A Woke Trap is a narrative technique where ideological messaging is intentionally delayed until after the viewer is emotionally invested in the story.',
    keywords: 'woke trap, ideological bait and switch, entertainment analysis, narrative manipulation, VirtueVigil',
    canonical: `${SITE_URL}/woke-trap.html`,
    ogType: 'article',
    structuredData
  })}
<body>
  ${siteHeader('woke-trap')}

  <section class="page-hero">
    <div class="container">
      <h1>What Is a <span class="text-gold">Woke Trap</span>?</h1>
      <p>Understanding the narrative technique VirtueVigil was built to identify.</p>
    </div>
  </section>

  <article class="content-article">
    <h2>The Definition</h2>
    <p>A Woke Trap is a narrative technique used in modern film and television where ideological messaging is intentionally delayed until after the viewer is emotionally invested in the story.</p>
    <p>In other words, the agenda is not announced. It is withheld.</p>
    <p>VirtueVigil identifies and flags this practice because we believe it is manipulative by design, especially for families and younger viewers who are less equipped to recognize narrative framing tactics in real time.</p>

    <div class="highlight-box">
      <p>A title is classified as a Woke Trap when it spends approximately 50 percent or more of its runtime presenting itself as neutral, relatable, or observational, before delivering a clear ideological payload.</p>
    </div>

    <p>Timing, not tone, subtlety, or eventual volume of the message, is the key factor. It is about <em>when</em> the message is delivered.</p>

    <h2>Why Timing Matters</h2>
    <p>Most viewers instinctively lower their defenses once they emotionally commit to a story. That commitment can take many forms: empathy for a character, identification with a struggle, trust in the storyteller&rsquo;s fairness, or simple narrative momentum.</p>
    <p>A Woke Trap exploits that commitment.</p>
    <p>By delaying ideological framing until trust is established, the viewer is placed at a psychological disadvantage. Resistance is lower. Critical distance is reduced. The message lands not as a proposition, but as a conclusion.</p>

    <div class="highlight-box">
      <p>VirtueVigil considers this practice unethical.</p>
    </div>

    <h2>Woke Trap vs. Openly Woke Content</h2>
    <p>It is important to distinguish between two categories.</p>
    <p><strong>Openly Woke Content</strong> &mdash; Some films and series are ideological from the opening scenes. Their worldview is obvious, viewers can opt out immediately. VirtueVigil may still classify these titles as strongly woke, but they are not traps. Transparency matters.</p>
    <p><strong>Woke Trap Content</strong> &mdash; A Woke Trap disguises its intent. It begins as a grounded family drama, a procedural, a mental health story, a character study, or a seemingly neutral social narrative. Only later does it pivot into ideological reframing, moral inversion, identity-based moral authority, or explicit rejection of traditional values.</p>

    <div class="highlight-box">
      <p>The delay is the point.</p>
    </div>

    <h2>Common Woke Trap Patterns</h2>
    <p>VirtueVigil frequently observes Woke Traps using the following techniques:</p>
    <ul>
      <li>Establishing sympathy before assigning blame</li>
      <li>Presenting hardship without ideology until mid-story</li>
      <li>Reframing authority or family as oppressive only after trust is built</li>
      <li>Introducing activist language late in the narrative</li>
      <li>Using symbolism or allegory to bypass conscious resistance</li>
      <li>Ending with moral relativism rather than resolution</li>
    </ul>
    <p>These patterns are repeatable. They are not accidental.</p>

    <h2>Why VirtueVigil Flags Woke Traps</h2>
    <p>VirtueVigil does not exist to censor content. We exist to restore viewer agency.</p>
    <p>When ideological intent is delayed, the viewer is denied the ability to make an informed choice at the outset. That is especially concerning for parents who are selecting content for children or teens.</p>
    <p>Flagging a Woke Trap allows viewers to decide: whether they want to engage, whether they want to contextualize, or whether they want to opt out entirely.</p>

    <div class="highlight-box">
      <p>Clarity precedes consent.</p>
    </div>

    <h2>How Woke Traps Are Displayed on VirtueVigil</h2>
    <p>When a title is classified as a Woke Trap, VirtueVigil will clearly label it with a Woke Trap Warning, a brief explanation of when the ideological pivot occurs, and supporting trope analysis that demonstrates the shift.</p>
    <p>The goal is not persuasion. The goal is exposure.</p>

    <h2>Our Position</h2>
    <p>The most influential ideological messages are rarely delivered upfront. They are introduced quietly, after trust is earned and resistance is lowered.</p>

    <div class="highlight-box">
      <p>VirtueVigil exists to make that visible.</p>
    </div>

    <div style="text-align:center;margin-top:40px;">
      <a href="/" class="hero-cta">Browse Reviews <i class="fas fa-arrow-right"></i></a>
    </div>
  </article>

  ${simpleFooter()}
${pageScripts()}
</body>
</html>`;
}


// ============================================
// SEO GENERATORS
// ============================================

function buildSitemap(catMap) {
  const today = new Date().toISOString().split('T')[0];

  const urls = [
    { loc: SITE_URL, changefreq: 'daily', priority: '1.0' },
    { loc: `${SITE_URL}/about.html`, changefreq: 'monthly', priority: '0.6' },
    { loc: `${SITE_URL}/methodology.html`, changefreq: 'monthly', priority: '0.6' },
    { loc: `${SITE_URL}/woke-trap.html`, changefreq: 'monthly', priority: '0.7' },
  ];

  // Review pages — highest priority after homepage
  reviews.forEach(r => {
    urls.push({
      loc: `${SITE_URL}/reviews/${r.slug}/`,
      lastmod: r.date,
      changefreq: 'monthly',
      priority: '0.8'
    });
  });

  // Category pages
  Object.entries(catMap).forEach(([name, { slug }]) => {
    urls.push({
      loc: `${SITE_URL}/category/${slug}/`,
      changefreq: 'weekly',
      priority: '0.5'
    });
  });

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url>
    <loc>${u.loc}</loc>
    ${u.lastmod ? `<lastmod>${u.lastmod}</lastmod>` : `<lastmod>${today}</lastmod>`}
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`).join('\n')}
</urlset>`;

  return xml;
}

function buildRobotsTxt() {
  return `User-agent: *
Allow: /

Disallow: /gracie/

Sitemap: ${SITE_URL}/sitemap.xml
`;
}

function breadcrumbLD(items) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": items.map((item, i) => ({
      "@type": "ListItem",
      "position": i + 1,
      "name": item.name,
      "item": item.url
    }))
  };
}


// ============================================
// SUBSCRIBER PAGES
// ============================================

function buildSubscribePage() {
  return `${htmlHead({
    title: 'Subscribe — VirtueVigil',
    description: 'Join VirtueVigil to comment on reviews and join the community. Free subscription.',
    canonical: `${SITE_URL}/subscribe/`,
  })}
<body>
  ${topBanner()}
  ${siteHeader('index')}

  <section class="page-hero">
    <div class="container">
      <h1>Join <span class="text-gold">VirtueVigil</span></h1>
      <p>Subscribe to comment on reviews and join the community. It&rsquo;s free.</p>
    </div>
  </section>

  <div class="subscribe-page">
    <div class="subscribe-card">
      <div class="subscribe-benefits">
        <h3>Subscriber Benefits</h3>
        <div class="benefit"><i class="fas fa-comments" style="color:var(--gold);"></i> Comment on reviews</div>
        <div class="benefit"><i class="fas fa-arrow-up" style="color:var(--gold);"></i> Upvote and downvote comments</div>
        <div class="benefit"><i class="fas fa-bell" style="color:var(--gold);"></i> Weekly Vigil Report emails</div>
        <div class="benefit"><i class="fas fa-star" style="color:var(--gold);"></i> Early access to new features</div>
      </div>

      <div class="subscribe-form-area">
        <button id="vv-sub-google" class="btn-oauth btn-google">
          <svg width="18" height="18" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
          Continue with Google
        </button>

        <div class="auth-divider"><span>or use email</span></div>

        <form id="vv-sub-email-form">
          <input type="hidden" id="vv-sub-mode-signup" checked value="1">
          <input type="email" id="vv-sub-email" placeholder="Email address" required autocomplete="email">
          <input type="password" id="vv-sub-password" placeholder="Create a password (min 6 characters)" required minlength="6" autocomplete="new-password">
          <button type="submit" class="btn-auth-submit">Create Account</button>
        </form>

        <p class="auth-footer-text">Already have an account? <a href="#" onclick="document.getElementById('vv-sub-mode-signup').value='';this.closest('form')||document.getElementById('vv-sub-email-form').querySelector('button').textContent='Sign In';return false;">Sign in</a></p>

        <div id="vv-sub-error" class="auth-msg error" style="display:none;"></div>
        <div id="vv-sub-success" class="auth-msg success" style="display:none;"></div>
      </div>
    </div>
  </div>

  ${simpleFooter()}
${pageScripts()}
</body>
</html>`;
}


function buildAccountPage() {
  return `${htmlHead({
    title: 'My Account — VirtueVigil',
    description: 'Manage your VirtueVigil profile, avatar, and account settings.',
    canonical: `${SITE_URL}/account/`,
  })}
<body>
  ${topBanner()}
  ${siteHeader('index')}

  <section class="page-hero">
    <div class="container">
      <h1>My <span class="text-gold">Account</span></h1>
      <p>Manage your profile and account settings.</p>
    </div>
  </section>

  <div class="account-page">
    <div id="vv-auth-required" class="auth-required-card" style="display:none;">
      <i class="fas fa-lock" style="font-size:2rem;color:var(--gold);margin-bottom:16px;"></i>
      <h3>Sign in required</h3>
      <p>Please <a href="/subscribe/">sign in or create an account</a> to view your profile.</p>
    </div>

    <div id="vv-profile-section" class="profile-section" style="display:none;">
      <div id="vv-acct-status" class="acct-status" style="display:none;"></div>

      <form id="vv-acct-form" class="profile-form">
        <div class="profile-avatar-area">
          <img id="vv-acct-avatar" class="avatar-lg" src="" alt="Your avatar">
          <div class="avatar-actions">
            <button id="vv-acct-avatar-btn" type="button" class="btn-outline-sm"><i class="fas fa-camera"></i> Change Avatar</button>
            <input type="file" id="vv-acct-avatar-input" accept="image/png,image/jpeg,image/gif,image/webp" style="display:none;">
            <span id="vv-acct-provider" class="provider-badge"></span>
          </div>
        </div>

        <div class="form-group">
          <label for="vv-acct-name">Display Name</label>
          <input type="text" id="vv-acct-name" maxlength="100" placeholder="How others see you">
        </div>

        <div class="form-group">
          <label for="vv-acct-email">Email</label>
          <input type="email" id="vv-acct-email" disabled>
          <span class="hint">Email cannot be changed</span>
        </div>

        <button type="submit" class="btn-save-profile">Save Changes</button>
      </form>

      <div id="vv-acct-password-section" class="password-section" style="display:none;">
        <h3>Change Password</h3>
        <div class="form-group">
          <label for="vv-acct-new-pwd">New Password</label>
          <input type="password" id="vv-acct-new-pwd" minlength="6" placeholder="Min 6 characters">
        </div>
        <div class="form-group">
          <label for="vv-acct-confirm-pwd">Confirm Password</label>
          <input type="password" id="vv-acct-confirm-pwd" minlength="6" placeholder="Repeat new password">
        </div>
        <button id="vv-acct-pwd-btn" type="button" class="btn-outline-sm">Update Password</button>
      </div>

      <div class="account-actions">
        <button id="vv-acct-signout" class="btn-signout"><i class="fas fa-sign-out-alt"></i> Sign Out</button>
      </div>
    </div>
  </div>

  ${simpleFooter()}
${pageScripts(['/js/account.js'])}
</body>
</html>`;
}


function buildAuthCallbackPage() {
  return `${htmlHead({
    title: 'Signing in... — VirtueVigil',
    description: 'Processing your sign-in.',
  })}
<body style="background:var(--bg-primary,#0d0d12);color:var(--text-primary,#e8e6e1);font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0;">
  <div style="text-align:center;max-width:400px;padding:40px;">
    <div style="font-size:2rem;color:#c9a84c;margin-bottom:16px;"><i class="fas fa-spinner fa-spin"></i></div>
    <h2 style="margin-bottom:8px;">Signing you in...</h2>
    <p style="color:#a0a0a8;font-size:0.9rem;">Please wait while we complete your sign-in.</p>
    <p id="auth-cb-error" style="color:#c44040;display:none;margin-top:16px;"></p>
  </div>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script>
    window.SUPABASE_URL = 'https://fdxvflryvctvstxdbdtm.supabase.co';
    window.SUPABASE_ANON_KEY = 'sb_publishable_sLwiGeuKX9jNopaeK3Wbqg_gvKcAuhq';
  </script>
  <script>
    (async function() {
      try {
        var url = window.SUPABASE_URL || localStorage.getItem('vv_supabase_url') || '';
        var key = window.SUPABASE_ANON_KEY || localStorage.getItem('vv_supabase_anon_key') || '';
        if (!url || !key) throw new Error('Supabase not configured');
        var sb = window.supabase.createClient(url, key);
        var hash = window.location.hash;
        if (hash) {
          // Supabase returns tokens in the URL hash after OAuth
          await sb.auth.getSession();
        }
        // Give it a moment to process
        setTimeout(function() {
          window.location.href = '/account/';
        }, 1500);
      } catch(e) {
        document.getElementById('auth-cb-error').textContent = 'Sign-in failed: ' + e.message;
        document.getElementById('auth-cb-error').style.display = 'block';
      }
    })();
  </script>
</body>
</html>`;
}


// ============================================
// MAIN BUILD
// ============================================

function build() {
  console.log(`VirtueVigil Static Builder ${BUILD_VERSION}`);
  console.log('=========================\n');

  // Clean dist
  if (fs.existsSync(DIST)) fs.rmSync(DIST, { recursive: true });
  mkdirp(DIST);

  // --- Pages ---
  console.log('\nBuilding pages:');
  writePage('index.html', buildHomepage());
  writePage('about.html', buildAboutPage());
  writePage('methodology.html', buildMethodologyPage());
  writePage('woke-trap.html', buildWokeTrapPage());

  // --- Subscriber pages ---
  console.log('\nBuilding subscriber pages:');
  writePage('subscribe/index.html', buildSubscribePage());
  writePage('account/index.html', buildAccountPage());
  writePage('auth/callback/index.html', buildAuthCallbackPage());

  // --- Review pages ---
  console.log('\nBuilding review pages:');
  reviews.forEach(r => {
    writePage(`reviews/${r.slug}/index.html`, buildReviewPage(r));
  });

  // --- Category pages ---
  console.log('\nBuilding category pages:');
  const catMap = {};

  // By type
  catMap['Films'] = { slug: 'films', reviews: reviews.filter(r => r.type === 'film') };
  catMap['Series'] = { slug: 'series', reviews: reviews.filter(r => r.type === 'series') };

  // Woke traps
  const trapReviews = reviews.filter(r => r.wokeTrap && r.wokeTrap.present);
  if (trapReviews.length) catMap['Woke Trap Alerts'] = { slug: 'woke-traps', reviews: trapReviews };

  // By genre
  reviews.forEach(r => {
    if (r.genre) {
      const slug = r.genre.toLowerCase().replace(/\s+/g, '-');
      if (!catMap[r.genre]) catMap[r.genre] = { slug, reviews: [] };
      catMap[r.genre].reviews.push(r);
    }
  });

  Object.entries(catMap).forEach(([name, { slug, reviews: catRevs }]) => {
    if (catRevs.length) {
      writePage(`category/${slug}/index.html`, buildCategoryPage(name, slug, catRevs));
    }
  });

  // --- SEO files ---
  console.log('\nGenerating SEO files:');
  writePage('sitemap.xml', buildSitemap(catMap));
  writePage('robots.txt', buildRobotsTxt());

  // --- Copy static assets ---
  console.log('\nCopying assets:');
  copyRecursive(path.join(SRC, 'css'), path.join(DIST, 'css'));
  console.log('  css/');
  copyRecursive(path.join(SRC, 'js'), path.join(DIST, 'js'));
  console.log('  js/');
  copyRecursive(path.join(SRC, 'images'), path.join(DIST, 'images'));
  console.log('  images/');
  copyRecursive(path.join(SRC, 'gracie'), path.join(DIST, 'gracie'));
  console.log('  gracie/');
  copyRecursive(path.join(SRC, 'data'), path.join(DIST, 'data'));
  console.log('  data/');

  // --- Summary ---
  const subscriberPages = 3; // subscribe, account, auth/callback
  const staticPages = 4; // index, about, methodology, woke-trap
  const totalPages = staticPages + subscriberPages + reviews.length + Object.keys(catMap).length;
  console.log(`\n=========================`);
  console.log(`Build complete!`);
  console.log(`  ${reviews.length} reviews`);
  console.log(`  ${Object.keys(catMap).length} category pages`);
  console.log(`  ${staticPages} static pages`);
  console.log(`  ${subscriberPages} subscriber pages`);
  console.log(`  ${totalPages} total pages`);
  console.log(`  + sitemap.xml, robots.txt`);
  console.log(`\nOutput: ${DIST}`);
}

build();
