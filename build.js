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
const BUILD_VERSION = 'v1.7.1';
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
  // "Mixed/Traditional Lean" should be mixed, not traditional
  if (lv.startsWith('MIXED')) return 'mixed';
  if (lv.includes('WOKE')) return 'woke';
  if (lv.includes('TRADITIONAL')) return 'traditional';
  return 'mixed';
}

function verdictIcon(vc) {
  if (vc === 'woke') return 'exclamation-triangle';
  if (vc === 'traditional') return 'check-circle';
  return 'minus-circle';
}

const POSTER_VERSION = Date.now(); // cache-bust posters on every build
function posterHTML(r, size) {
  if (r.poster && (r.poster.startsWith('http') || r.poster.startsWith('/'))) {
    const alt = esc(r.title) + ' poster';
    const posterSrc = r.poster.startsWith('/') ? `${r.poster}?v=${POSTER_VERSION}` : r.poster;
    if (size === 'thumb') return `<img src="${posterSrc}" alt="${alt}" class="poster-img poster-thumb" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy">`;
    if (size === 'card') return `<img src="${posterSrc}" alt="${alt}" class="poster-img poster-card" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy">`;
    if (size === 'featured') return `<img src="${posterSrc}" alt="${alt}" class="poster-img poster-featured" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy">`;
    return `<img src="${posterSrc}" alt="${alt}" class="poster-img" loading="lazy">`;
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

function searchOverlayHTML() {
  return `<div class="search-overlay" id="search-overlay">
  <div class="search-modal">
    <div class="search-header">
      <i class="fas fa-search search-icon-sm"></i>
      <input type="text" class="search-input" placeholder="Search reviews... (e.g. 'woke', 'horror', 'Netflix')" autocomplete="off" spellcheck="false">
      <button class="search-close"><i class="fas fa-times"></i></button>
    </div>
    <div class="search-results" id="search-results">
      <p class="search-hint">Start typing to search all reviews...</p>
    </div>
  </div>
</div>`;
}

function pageScripts(extras) {
  const overlay = searchOverlayHTML();
  const base = `  <script src="/js/main.js?v=${BUILD_VERSION}"></script>
  <script src="/js/supabase-config.js?v=${BUILD_VERSION}"></script>
  <script src="/js/auth.js?v=${BUILD_VERSION}"></script>`;
  if (!extras) return overlay + '\n' + base;
  return overlay + '\n' + base + '\n' + extras.map(s => `  <script src="${s}"></script>`).join('\n');
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

// Helper: is this review a woke trap? Check woke_trap_assessment.is_trap (canonical per VVWS-SPEC v1.1)
// A woke trap requires: (a) negative margin (film scores woke) AND (b) woke content hidden until >50% runtime
function isWokeTrap(r) {
  if (r.woke_trap_assessment && r.woke_trap_assessment.is_trap === true) return true;
  return false;
}

// Build category data
function getCategories() {
  const cats = {};
  const types = { film: 0, series: 0 };
  let trapCount = 0;
  reviews.forEach(r => {
    if (r.genre) cats[r.genre] = (cats[r.genre] || 0) + 1;
    // Normalise: treat both 'series' and 'tv' as series
    if (r.type === 'film') types.film++;
    else if (r.type === 'series' || r.type === 'tv') types.series++;
    if (isWokeTrap(r)) trapCount++;
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
  <meta name="twitter:site" content="@Debra_Ducane">
  <meta name="twitter:creator" content="@Debra_Ducane">
  <meta name="twitter:title" content="${esc(title)}">
  <meta name="twitter:description" content="${esc(description)}">
  <meta name="twitter:image" content="${ogImage || `${SITE_URL}/images/og-default.png`}">

  ${ldBlocks.map(ld => `<script type="application/ld+json">\n  ${JSON.stringify(ld, null, 2).split('\n').join('\n  ')}\n  </script>`).join('\n  ')}
  ${extraHead || ''}

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="/css/styles.css?v=${BUILD_VERSION}">
  <link rel="icon" type="image/svg+xml" href="/images/logo.svg">
  ${canonical ? `<link rel="canonical" href="${canonical}">` : ''}

  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script>
    window.SUPABASE_URL = 'https://fdxvflryvctvstxdbdtm.supabase.co';
    window.SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZkeHZmbHJ5dmN0dnN0eGRiZHRtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzExMjQ3MjEsImV4cCI6MjA4NjcwMDcyMX0.wn80dndvXLUU6qMzJW1DBuz0d6cPMu4iEO3UA6QnF4E';
  </script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z2GXH8MG70"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-Z2GXH8MG70');
  </script>
</head>`;
}

function siteSearch() {
  return `
  <div class="site-search-bar" role="search">
    <div class="site-search-inner">
      <i class="fas fa-search site-search-icon"></i>
      <input
        type="text"
        class="site-search-input"
        id="site-search-input"
        placeholder="Search titles..."
        autocomplete="off"
        spellcheck="false"
        aria-label="Search reviews"
      >
      <span class="site-search-hint">Press <kbd>⌘K</kbd> anytime</span>
    </div>
    <div class="site-search-results" id="site-search-results" hidden></div>
  </div>`;
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

  <div class="site-search-bar" role="search" aria-label="Search reviews">
    <div class="site-search-inner">
      <i class="fas fa-search site-search-icon"></i>
      <input
        type="text"
        class="site-search-input"
        id="site-search-input"
        placeholder="Search titles..."
        autocomplete="off"
        spellcheck="false"
        aria-label="Search reviews"
      >
      <kbd class="site-search-kbd">⌘K</kbd>
    </div>
    <div class="site-search-results" id="site-search-results" hidden></div>
  </div>

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
          const hasTrap = isWokeTrap(r);
          const margin = typeof r.scoreMargin === 'number' ? r.scoreMargin : parseFloat(String(r.scoreMargin)) || Math.abs((r.tradScore || 0) - (r.wokeScore || 0));
          let badge = r.verdict;
          if (hasTrap) badge = 'WOKE TRAP';
          else if (vc === 'woke') badge = `WOKE ${Math.round(margin)}`;
          else if (vc === 'traditional') badge = `TRAD +${Math.round(Math.abs(margin))}`;
          else if (vc === 'mixed') badge = `MIXED ${Math.round(margin) >= 0 ? '+' : ''}${Math.round(margin)}`;
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
          <a href="https://www.youtube.com/channel/UCF3CiKkQZcFAMxu2V4tVEIw" aria-label="YouTube" target="_blank" rel="noopener"><i class="fab fa-youtube"></i></a>
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
            <a href="https://www.youtube.com/channel/UCF3CiKkQZcFAMxu2V4tVEIw" aria-label="YouTube" target="_blank" rel="noopener"><i class="fab fa-youtube"></i></a>
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
          <a href="https://www.youtube.com/channel/UCF3CiKkQZcFAMxu2V4tVEIw" target="_blank" rel="noopener">YouTube Channel</a>
          <a href="https://instagram.com/virtuevigil" target="_blank" rel="noopener">Instagram</a>
          <a href="https://facebook.com/virtuevigil" target="_blank" rel="noopener">Facebook Page</a>
          <a href="https://tiktok.com/@virtuevigil" target="_blank" rel="noopener">TikTok</a>
          <a href="mailto:hello@virtuevigil.com">Contact Us</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; ${new Date().getFullYear()} VirtueVigil. All rights reserved. Guarding Values. Exposing Agendas.</p>
        <p><a href="/privacy-policy">Privacy Policy</a> &middot; <a href="/terms-of-use">Terms of Use</a></p>
        <p style="margin-top:8px;"><a href="https://fazier.com" target="_blank" rel="noopener"><img src="https://fazier.com/api/v1//public/badges/launch_badges.svg?badge_type=featured&theme=light" width="105" alt="Featured on Fazier" style="height:auto;opacity:0.7;"></a></p>
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
          <div class="score-item"><div class="label">Authenticity Index</div><div class="value auth">${r.authIndex != null ? r.authIndex + '%' : 'N/A'}</div></div>
          <div class="score-item"><div class="label">Score Margin</div><div class="value margin">${esc(r.scoreMargin)}</div></div>
        </div>`;
}

function insightGrid(r) {
  return `
          <div class="insight-grid">
            <div class="insight-card">
              <h4><i class="fas fa-user-tie" style="color:var(--accent-blue);"></i> Adult Viewer Insight</h4>
              <p>${esc(stripInlineMarkdown(r.summary.adultInsight))}</p>
            </div>
            <div class="insight-card">
              <h4><i class="fas fa-child" style="color:var(--accent-amber);"></i> Parental Guidance</h4>
              <p>${esc(stripInlineMarkdown(r.summary.parentalGuidance))}</p>
            </div>
          </div>`;
}

function wokeTrapAlert(r) {
  if (!r.wokeTrap || !r.wokeTrap.present) return '';
  return `
          <div class="woke-trap-alert">
            <h4><i class="fas fa-exclamation-circle"></i> Woke Trap Warning</h4>
            <p><strong>Trap Present:</strong> Yes &mdash; <strong>Degree: ${esc(r.wokeTrap.degree)}.</strong> ${esc(stripInlineMarkdown(r.wokeTrap.explanation))}</p>
          </div>`;
}

function tropeTable(r) {
  if (!r.tropeAudit || !r.tropeAudit.length) return '';
  // Support both old schema (trope/location) and new VVWS schema (name/severity/centrality/weightedScore)
  const hasVVWS = r.tropeAudit[0].severity !== undefined;
  if (hasVVWS) {
    const wokeTropes = r.tropeAudit.filter(t => (t.category || '').toLowerCase() === 'woke');
    const tradTropes = r.tropeAudit.filter(t => (t.category || '').toLowerCase() === 'traditional' || (t.category || '').toLowerCase() === 'trad');
    const wokeTotal = wokeTropes.reduce((s, t) => s + (t.weightedScore || 0), 0);
    const tradTotal = tradTropes.reduce((s, t) => s + (t.weightedScore || 0), 0);
    const renderRows = (tropes) => tropes.map(t => `
              <tr>
                <td>${esc(t.name || t.trope || '')}</td>
                <td>${t.severity || ''}</td>
                <td>${esc(t.authenticity || '')}</td>
                <td>${esc(t.centrality || '')}</td>
                <td><strong>${t.weightedScore || ''}</strong></td>
              </tr>`).join('');
    return `
          <div class="section-label" style="margin-top:28px;">Trope Audit &mdash; VVWS Weighted Scoring</div>
          <p style="font-size:0.9em;color:#aaa;margin-bottom:12px;">Formula: Weighted Score = Severity &times; Authenticity Multiplier &times; Centrality Multiplier</p>
          ${wokeTropes.length ? `
          <h4 style="color:#e74c3c;margin-top:16px;">🔴 Woke Tropes</h4>
          <table class="trope-table">
            <thead>
              <tr><th>Trope</th><th>Severity</th><th>Authenticity</th><th>Centrality</th><th>Score</th></tr>
            </thead>
            <tbody>
              ${renderRows(wokeTropes)}
              <tr style="border-top:2px solid #e74c3c;"><td colspan="4"><strong>TOTAL WOKE</strong></td><td><strong>${wokeTotal.toFixed(1)}</strong></td></tr>
            </tbody>
          </table>` : ''}
          ${tradTropes.length ? `
          <h4 style="color:#2ecc71;margin-top:16px;">🟢 Traditional Tropes</h4>
          <table class="trope-table">
            <thead>
              <tr><th>Trope</th><th>Severity</th><th>Authenticity</th><th>Centrality</th><th>Score</th></tr>
            </thead>
            <tbody>
              ${renderRows(tradTropes)}
              <tr style="border-top:2px solid #2ecc71;"><td colspan="4"><strong>TOTAL TRADITIONAL</strong></td><td><strong>${tradTotal.toFixed(1)}</strong></td></tr>
            </tbody>
          </table>` : ''}
          <p style="margin-top:12px;font-size:1.1em;"><strong>Score Margin: ${esc(r.scoreMargin || ((tradTotal - wokeTotal >= 0 ? '+' : '') + (tradTotal - wokeTotal).toFixed(0) + (tradTotal >= wokeTotal ? ' TRAD' : ' WOKE')))}</strong></p>`;
  }
  // Legacy schema fallback
  return `
          <div class="section-label" style="margin-top:28px;">Trope Audit</div>
          <table class="trope-table">
            <thead>
              <tr><th>Trope</th><th>Category</th><th>Location</th><th>Authenticity</th></tr>
            </thead>
            <tbody>
              ${r.tropeAudit.map(t => `
              <tr>
                <td>${esc(t.trope || t.name || '')}</td>
                <td><span class="tag ${(t.category || '').toUpperCase() === 'WOKE' ? 'woke' : 'trad'}">${esc(t.category)}</span></td>
                <td>${esc(t.location || t.description || '')}</td>
                <td class="${t.authenticity === 'Forced' || t.authenticity === 'Low' ? 'forced' : 'natural'}">${esc(t.authenticity)}</td>
              </tr>`).join('')}
            </tbody>
          </table>`;
}

function mdToHtml(text) {
  if (!text) return '';
  const lines = text.split('\n');
  const out = [];
  let inTable = false, inUl = false;
  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];
    // Skip table separator rows
    if (/^\s*\|[\s\-:]+\|/.test(line)) { inTable = true; continue; }
    // Table rows
    if (/^\s*\|/.test(line)) {
      if (!inTable) { out.push('<table class="md-table">'); inTable = true; }
      const cells = line.split('|').filter(c => c.trim() !== '');
      const isHeader = lines[i+1] && /^\s*\|[\s\-:]+\|/.test(lines[i+1]);
      const tag = isHeader ? 'th' : 'td';
      out.push('<tr>' + cells.map(c => `<${tag}>${mdInline(c.trim())}</${tag}>`).join('') + '</tr>');
      continue;
    }
    if (inTable) { out.push('</table>'); inTable = false; }
    // Headings
    if (/^#{1,6}\s/.test(line)) {
      const lvl = line.match(/^(#+)/)[1].length;
      const h = Math.min(lvl + 2, 6);
      out.push(`<h${h} class="md-heading">${mdInline(line.replace(/^#+\s*/, ''))}</h${h}>`);
      continue;
    }
    // HR
    if (/^---+$/.test(line.trim())) { out.push('<hr>'); continue; }
    // Blockquote
    if (/^>\s?/.test(line)) {
      out.push('<blockquote>' + mdInline(line.replace(/^>\s?/, '')) + '</blockquote>');
      continue;
    }
    // Bullet
    if (/^[\*\-]\s/.test(line)) {
      if (!inUl) { out.push('<ul>'); inUl = true; }
      out.push('<li>' + mdInline(line.replace(/^[\*\-]\s+/, '')) + '</li>');
      continue;
    }
    if (inUl) { out.push('</ul>'); inUl = false; }
    // Empty line = paragraph break
    if (!line.trim()) { continue; }
    out.push(`<p>${mdInline(line)}</p>`);
  }
  if (inTable) out.push('</table>');
  if (inUl) out.push('</ul>');
  return out.join('\n');
}

function mdInline(text) {
  return text
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`(.+?)`/g, '<code>$1</code>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
}

function overallParagraphs(r) {
  return mdToHtml(r.summary.overall);
}

// Strip inline markdown markers for plain-text contexts (excerpts, insight panels)
function stripInlineMarkdown(text) {
  if (!text) return '';
  return text
    .replace(/\*\*\*(.+?)\*\*\*/g, '$1')
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/\*(.+?)\*/g, '$1')
    .replace(/`(.+?)`/g, '$1')
    .replace(/^---+$/gm, '')
    .replace(/^#{1,6}\s+/gm, '')
    .replace(/^>\s?/gm, '')
    .trim();
}

// Extract first real paragraph (skip markdown headings/HRs) for subtitles/excerpts
function firstParagraph(text, maxLen) {
  if (!text) return '';
  const first = text.split('\n').find(p => p.trim() && !p.trim().startsWith('#') && !/^---+$/.test(p.trim()) && !p.trim().startsWith('>') && !/^\*\*Classification:/.test(p.trim()) && !/^\*\*WOKE\b/.test(p.trim()) && !/^\*\*Composite\b/.test(p.trim()) && !/^⚠️\s*(PRE-RELEASE|SPOILER)/.test(p.trim())) || '';
  const clean = stripInlineMarkdown(first.trim());
  if (!maxLen || clean.length <= maxLen) return clean;
  const cut = clean.lastIndexOf('. ', maxLen);
  return (cut > 80 ? clean.substring(0, cut + 1) : clean.substring(0, maxLen)) + '\u2026';
}

// Strip markdown for plain-text contexts (JSON-LD reviewBody etc.)
function plainText(text, maxLen) {
  if (!text) return '';
  const stripped = text.replace(/^#{1,6}\s+.+$/gm, '').replace(/\*\*?([^*]+)\*\*?/g, '$1').trim();
  return maxLen ? stripped.substring(0, maxLen) : stripped;
}

function spoilerAlertBanner(r) {
  if (r.spoiler_alert !== true) return '';
  return `
          <div class="spoiler-alert">
            <span class="spoiler-alert-icon">⚠️</span>
            <span class="spoiler-alert-text">SPOILER ALERT: This review contains detailed plot analysis and may reveal key story elements.</span>
          </div>`;
}

function wokeTrapAssessment(r) {
  if (!r.woke_trap_assessment) return '';
  const wta = r.woke_trap_assessment;
  if (wta.is_trap) {
    const pct = wta.pct_runtime ? `${wta.pct_runtime}%` : 'a significant portion';
    return `
          <div class="woke-trap-assessment is-trap">
            <div class="wta-header">🚨 WOKE TRAP WARNING</div>
            <p>This film draws you in for ${esc(pct)} of its runtime with traditional or neutral content before springing its woke agenda. Know before you go!</p>
            ${wta.explanation ? `<p class="wta-explanation">${esc(stripInlineMarkdown(wta.explanation))}</p>` : ''}
          </div>`;
  } else {
    return `
          <div class="woke-trap-assessment is-clear">
            <div class="wta-header">✅ NOT A WOKE TRAP</div>
            ${wta.explanation ? `<p class="wta-explanation">${esc(stripInlineMarkdown(wta.explanation))}</p>` : ''}
          </div>`;
  }
}

function creativeTeamSummary(r) {
  if (!r.creative_team) return '';
  const ct = r.creative_team;
  let html = `
          <div class="creative-team-summary">
            <div class="cts-header">Creative Team</div>
            <div class="cts-grid">`;
  if (ct.director) html += `<div class="cts-item"><span class="cts-role">Director</span><span class="cts-name">${esc(ct.director.name)}</span></div>`;
  if (ct.writer) html += `<div class="cts-item"><span class="cts-role">Writer</span><span class="cts-name">${esc(ct.writer.name)}</span></div>`;
  if (ct.lead_producer) html += `<div class="cts-item"><span class="cts-role">Lead Producer</span><span class="cts-name">${esc(ct.lead_producer.name)}${ct.lead_producer.company ? ' (' + esc(ct.lead_producer.company) + ')' : ''}</span></div>`;
  if (ct.composer) html += `<div class="cts-item"><span class="cts-role">Composer</span><span class="cts-name">${esc(ct.composer.name)}</span></div>`;
  if (ct.top_cast && ct.top_cast.length) {
    html += `<div class="cts-item cts-cast"><span class="cts-role">Top Cast</span><div class="cts-cast-list">`;
    ct.top_cast.forEach(c => { html += `<span class="cts-cast-member">${esc(c.name || c.actor)} <em>as ${esc(c.role)}</em></span>`; });
    html += `</div></div>`;
  }
  html += `</div>`;

  // Badges row
  html += `<div class="cts-badges">`;
  if (ct.prediction) {
    const predClass = ct.prediction.verdict === 'WOKE' ? 'woke' : (ct.prediction.verdict === 'TRADITIONAL' ? 'trad' : 'mixed');
    html += `<span class="prediction-badge ${predClass}">PRE-VIEWING PREDICTION: ${esc(ct.prediction.verdict)} (${esc(ct.prediction.confidence)})</span>`;
  }
  if (r.fidelity_casting) {
    const fidClass = r.fidelity_casting.score === 'FAITHFUL' ? 'faithful' : (r.fidelity_casting.score === 'ENHANCED' ? 'enhanced' : 'revisionist');
    html += `<span class="fidelity-badge ${fidClass}">FIDELITY CASTING: ${esc(r.fidelity_casting.score)}</span>`;
  }
  html += `</div>`;

  html += `</div>`;
  return html;
}

function creativeTeamFull(r) {
  if (!r.creative_team) return '';
  const ct = r.creative_team;
  let html = `
          <div class="creative-team-full">
            <div class="section-label" style="margin-top:28px;">Creative Team Deep Dive</div>`;

  if (ct.director && ct.director.profile) {
    html += `
            <div class="ctf-profile">
              <h4><i class="fas fa-video" style="color:var(--gold);"></i> Director: ${esc(ct.director.name)}</h4>
              ${ct.director.ideology ? `<span class="ctf-ideology-tag">${esc(ct.director.ideology)}</span>` : ''}
              <p>${esc(ct.director.profile)}</p>
            </div>`;
  }

  if (ct.writer && ct.writer.profile) {
    html += `
            <div class="ctf-profile">
              <h4><i class="fas fa-pen-fancy" style="color:var(--gold);"></i> Writer: ${esc(ct.writer.name)}</h4>
              <p>${esc(ct.writer.profile)}</p>
            </div>`;
  }

  if (ct.producers && ct.producers.length) {
    html += `<div class="ctf-profile"><h4><i class="fas fa-user-tie" style="color:var(--gold);"></i> Producers</h4><ul>`;
    ct.producers.forEach(p => { html += `<li><strong>${esc(p.name)}</strong>${p.company ? ' (' + esc(p.company) + ')' : ''}${p.profile ? ' — ' + esc(p.profile) : ''}</li>`; });
    html += `</ul></div>`;
  }

  if (ct.full_cast && ct.full_cast.length) {
    html += `<div class="ctf-profile"><h4><i class="fas fa-users" style="color:var(--gold);"></i> Full Cast</h4><div class="ctf-cast-grid">`;
    ct.full_cast.forEach(c => { html += `<div class="ctf-cast-item"><strong>${esc(c.name || c.actor)}</strong> <span>as ${esc(c.role)}</span></div>`; });
    html += `</div></div>`;
  }

  if (r.fidelity_casting && r.fidelity_casting.detailed_analysis) {
    const fidClass = r.fidelity_casting.score === 'FAITHFUL' ? 'faithful' : (r.fidelity_casting.score === 'ENHANCED' ? 'enhanced' : 'revisionist');
    html += `
            <div class="ctf-profile ctf-fidelity">
              <h4><i class="fas fa-theater-masks" style="color:var(--gold);"></i> Fidelity Casting Analysis <span class="fidelity-badge ${fidClass}">${esc(r.fidelity_casting.score)}</span></h4>
              ${r.fidelity_casting.summary ? `<p><strong>${esc(r.fidelity_casting.summary)}</strong></p>` : ''}
              <div class="fidelity-analysis">${mdToHtml(r.fidelity_casting.detailed_analysis)}</div>
            </div>`;
  }

  html += `</div>`;
  return html;
}

// ============================================
// PAGE BUILDERS
// ============================================

function buildHomepage() {
  const featured = reviews[0];
  const moreReviews = reviews.slice(1, 5);
  const vc = verdictClass(featured.verdict);
  const hasTrap = isWokeTrap(featured);

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
        "https://www.youtube.com/channel/UCF3CiKkQZcFAMxu2V4tVEIw",
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
              <p class="review-subtitle" itemprop="description">${esc(firstParagraph(featured.summary.overall, 160))}&hellip;</p>
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
        const rTrap = isWokeTrap(r);
        const excerpt = firstParagraph(r.summary.overall, 250);
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
              <span class="mini-score" style="color:var(--accent-amber);">AUTH: ${r.authIndex != null ? r.authIndex + '%' : 'N/A'}</span>
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
  const hasTrap = isWokeTrap(r);
  const seo = r.seo || {};
  const title = seo.titleTag || `Is ${r.title} Woke? | VirtueVigil`;
  const desc = seo.metaDescription || `VirtueVigil review of ${r.title}. Woke Score ${r.wokeScore}, Traditional ${r.tradScore}.`;
  const kw = seo.keywords || '';
  const canonical = `${SITE_URL}/reviews/${r.slug}/`;
  const ogImage = r.poster
    ? (r.poster.startsWith('http') ? r.poster : `${SITE_URL}${r.poster}`)
    : undefined;

  const structuredData = {
    "@context": "https://schema.org",
    "@type": "Review",
    "name": r.title,
    "author": { "@type": "Person", "name": r.author },
    "datePublished": r.date,
    "reviewBody": plainText(r.summary.overall, 500),
    "publisher": { "@type": "Organization", "name": "VirtueVigil" },
    "itemReviewed": Object.assign({
      "@type": r.type === 'film' ? "Movie" : "TVSeries",
      "name": r.title,
      "datePublished": String(r.year)
    }, ogImage ? { "image": ogImage } : {}),
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": r.authIndex != null ? r.authIndex : 0,
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
    { name: 'Reviews', url: `${SITE_URL}/reviews/` },
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
              <h1 class="review-title" itemprop="name">${esc(r.title)}</h1>
              <p class="review-subtitle" itemprop="description">${esc(firstParagraph(r.summary.overall, 300))}</p>
              <a href="#review-body" class="review-scroll-cue"><i class="fas fa-chevron-down"></i> Full analysis below</a>
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

        <div class="featured-body" id="review-body" itemprop="reviewBody">
          ${spoilerAlertBanner(r)}
          ${wokeTrapAssessment(r)}
          ${creativeTeamSummary(r)}
          <div class="section-label">Overall Perspective</div>
          ${overallParagraphs(r)}
          ${wokeTrapAlert(r)}
          ${tropeTable(r)}
          ${creativeTeamFull(r)}
          ${insightGrid(r)}
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
        const rTrap = isWokeTrap(r);
        const excerpt = firstParagraph(r.summary.overall, 250);
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
              <span class="mini-score" style="color:var(--accent-amber);">AUTH: ${r.authIndex != null ? r.authIndex + '%' : 'N/A'}</span>
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


function build404Page() {
  return `${htmlHead({
    title: 'Page Not Found | VirtueVigil',
    description: 'The page you are looking for does not exist. Browse VirtueVigil reviews and cultural analysis.',
    canonical: `${SITE_URL}/404.html`,
  })}
<body>
  ${siteHeader('')}

  <section class="page-hero" style="min-height:60vh;display:flex;align-items:center;justify-content:center;text-align:center;">
    <div class="container">
      <div style="font-size:5rem;margin-bottom:16px;">🔍</div>
      <h1 style="font-size:2.5rem;">Page Not Found</h1>
      <p style="color:var(--text-secondary);font-size:1.1rem;max-width:480px;margin:16px auto 32px;">That page doesn't exist — it may have been moved, renamed, or never existed in the first place.</p>
      <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
        <a href="/" class="btn-primary">← Back to Home</a>
        <a href="/category/films/" class="btn-secondary">Browse Film Reviews</a>
      </div>
    </div>
  </section>

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
      "https://www.youtube.com/channel/UCF3CiKkQZcFAMxu2V4tVEIw",
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
      <a href="https://www.youtube.com/channel/UCF3CiKkQZcFAMxu2V4tVEIw" target="_blank" rel="noopener" style="width:auto;padding:10px 20px;font-size:0.9rem;gap:8px;display:inline-flex;"><i class="fab fa-youtube"></i> YouTube</a>
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
    { loc: `${SITE_URL}/oscars-2026/`, changefreq: 'daily', priority: '0.9' },
    { loc: `${SITE_URL}/lists/most-woke-movies-2024/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/family-friendly-movies-2024/`, changefreq: 'monthly', priority: '0.8' },
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
    window.SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZkeHZmbHJ5dmN0dnN0eGRiZHRtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzExMjQ3MjEsImV4cCI6MjA4NjcwMDcyMX0.wn80dndvXLUU6qMzJW1DBuz0d6cPMu4iEO3UA6QnF4E';
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
// OSCAR 2026 LANDING PAGE
// ============================================

function buildOscars2026Page() {
  const canonical = `${SITE_URL}/oscars-2026/`;

  const bestPictureNominees = [
    { title: 'Sinners', slug: 'sinners-2025', nominations: 16, note: 'Most nominated film in Oscar history' },
    { title: 'Hamnet', slug: 'hamnet-2025', nominations: 8 },
    { title: 'One Battle After Another', slug: 'one-battle-after-another-2025', nominations: 7 },
    { title: 'Frankenstein', slug: 'frankenstein-2025', nominations: 7 },
    { title: 'Marty Supreme', slug: 'marty-supreme-2025', nominations: 6 },
    { title: 'Sentimental Value', slug: 'sentimental-value-2025', nominations: 5 },
    { title: 'Bugonia', slug: 'bugonia-2025', nominations: 3 },
    { title: 'F1', slug: 'f1-2025', nominations: 3 },
    { title: 'The Secret Agent', slug: 'the-secret-agent-2025', nominations: 3 },
    { title: 'Train Dreams', slug: 'train-dreams-2025', nominations: 3 },
  ];

  const bestDirectorNominees = [
    { name: 'Ryan Coogler', film: 'Sinners', slug: 'sinners-2025' },
    { name: 'Chloe Zhao', film: 'Hamnet', slug: 'hamnet-2025' },
    { name: 'Paul Thomas Anderson', film: 'One Battle After Another', slug: 'one-battle-after-another-2025' },
    { name: 'Josh Safdie', film: 'Marty Supreme', slug: 'marty-supreme-2025' },
    { name: 'Joachim Trier', film: 'Sentimental Value', slug: 'sentimental-value-2025' },
  ];

  const bestActorNominees = [
    { name: 'Michael B. Jordan', film: 'Sinners', slug: 'sinners-2025' },
    { name: 'Timothee Chalamet', film: 'Marty Supreme', slug: 'marty-supreme-2025' },
    { name: 'Leonardo DiCaprio', film: 'One Battle After Another', slug: 'one-battle-after-another-2025' },
    { name: 'Ethan Hawke', film: 'Blue Moon', slug: 'blue-moon' },
    { name: 'Wagner Moura', film: 'The Secret Agent', slug: 'the-secret-agent-2025' },
  ];

  const bestActressNominees = [
    { name: 'Jessie Buckley', film: 'Hamnet', slug: 'hamnet-2025' },
    { name: 'Emma Stone', film: 'Bugonia', slug: 'bugonia-2025' },
    { name: 'Renate Reinsve', film: 'Sentimental Value', slug: 'sentimental-value-2025' },
    { name: 'Rose Byrne', film: 'If I Had Legs I\'d Kick You', slug: 'if-i-had-legs-id-kick-you-2025' },
    { name: 'Kate Hudson', film: 'Song Sung Blue', slug: 'song-sung-blue-2025' },
  ];

  const reviewMap = {};
  reviews.forEach(r => { reviewMap[r.slug] = r; });

  function nomineeCard(nominee) {
    const r = nominee.slug ? reviewMap[nominee.slug] : null;
    if (r) {
      const vc = verdictClass(r.verdict);
      const badgeColor = vc === 'woke' ? '#c44040' : (vc === 'traditional' ? '#2ecc71' : '#d4a843');
      const badgeBg = vc === 'woke' ? 'rgba(196,64,64,0.15)' : (vc === 'traditional' ? 'rgba(46,204,113,0.15)' : 'rgba(212,168,67,0.15)');
      return `
          <div class="oscar-nominee-card" style="background:#14141c;border:1px solid rgba(201,168,76,0.2);border-radius:10px;padding:0;overflow:hidden;display:flex;flex-direction:column;">
            <div style="height:280px;overflow:hidden;position:relative;">
              ${posterHTML(r, 'card')}
              <div style="position:absolute;top:10px;right:10px;">
                <span style="background:${badgeBg};color:${badgeColor};padding:4px 10px;border-radius:6px;font-size:0.7rem;font-weight:700;border:1px solid ${badgeColor};">${esc(r.verdict)}</span>
              </div>
              ${nominee.nominations ? '<div style="position:absolute;top:10px;left:10px;"><span style="background:rgba(201,168,76,0.9);color:#0d0d12;padding:3px 8px;border-radius:4px;font-size:0.65rem;font-weight:700;">' + nominee.nominations + ' NOMS</span></div>' : ''}
            </div>
            <div style="padding:16px;flex:1;display:flex;flex-direction:column;">
              <h3 style="font-family:\'Cinzel\',Georgia,serif;font-size:1.05rem;margin:0 0 8px;color:#e8e6e1;">
                <a href="/reviews/${r.slug}/" style="color:#e8e6e1;text-decoration:none;">${esc(r.title)}</a>
              </h3>
              ${nominee.note ? '<p style="font-size:0.7rem;color:#c9a84c;margin:0 0 8px;font-weight:600;">' + esc(nominee.note) + '</p>' : ''}
              <div style="display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap;">
                <span style="background:rgba(196,64,64,0.15);color:#c44040;padding:3px 8px;border-radius:4px;font-size:0.7rem;font-weight:600;">WOKE: ${r.wokeScore}</span>
                <span style="background:rgba(46,204,113,0.15);color:#2ecc71;padding:3px 8px;border-radius:4px;font-size:0.7rem;font-weight:600;">TRAD: ${r.tradScore}</span>
                <span style="background:rgba(212,168,67,0.15);color:#d4a843;padding:3px 8px;border-radius:4px;font-size:0.7rem;font-weight:600;">AUTH: ${r.authIndex != null ? r.authIndex + '%' : 'N/A'}</span>
              </div>
              <a href="/reviews/${r.slug}/" style="color:#c9a84c;font-size:0.85rem;font-weight:600;text-decoration:none;margin-top:auto;">Read Full Review <i class="fas fa-arrow-right" style="font-size:0.7rem;"></i></a>
            </div>
          </div>`;
    } else {
      return `
          <div class="oscar-nominee-card" style="background:#14141c;border:1px solid rgba(201,168,76,0.1);border-radius:10px;padding:0;overflow:hidden;display:flex;flex-direction:column;opacity:0.7;">
            <div style="height:280px;overflow:hidden;position:relative;background:linear-gradient(135deg,#14141c,#1a1a26);display:flex;align-items:center;justify-content:center;">
              <span style="font-size:3rem;font-weight:700;color:#c9a84c;font-family:\'Cinzel\',Georgia,serif;">${(nominee.title || '?').charAt(0)}</span>
              ${nominee.nominations ? '<div style="position:absolute;top:10px;left:10px;"><span style="background:rgba(201,168,76,0.9);color:#0d0d12;padding:3px 8px;border-radius:4px;font-size:0.65rem;font-weight:700;">' + nominee.nominations + ' NOMS</span></div>' : ''}
            </div>
            <div style="padding:16px;flex:1;display:flex;flex-direction:column;">
              <h3 style="font-family:\'Cinzel\',Georgia,serif;font-size:1.05rem;margin:0 0 8px;color:#e8e6e1;">${esc(nominee.title)}</h3>
              <span style="background:rgba(106,106,117,0.2);color:#6a6a75;padding:4px 10px;border-radius:6px;font-size:0.7rem;font-weight:700;display:inline-block;width:fit-content;">COMING SOON</span>
            </div>
          </div>`;
    }
  }

  function actorRow(nominees) {
    return nominees.map(n => {
      const r = n.slug ? reviewMap[n.slug] : null;
      const hasReview = !!r;
      const vc = hasReview ? verdictClass(r.verdict) : '';
      const badgeColor = vc === 'woke' ? '#c44040' : (vc === 'traditional' ? '#2ecc71' : '#d4a843');
      return `
            <div style="display:flex;align-items:center;gap:14px;padding:14px 16px;background:#14141c;border-radius:8px;border:1px solid rgba(201,168,76,0.12);">
              <div style="flex:1;min-width:0;">
                <div style="font-weight:600;color:#e8e6e1;font-size:0.95rem;">${esc(n.name)}</div>
                <div style="color:#a0a0a8;font-size:0.8rem;margin-top:2px;">
                  ${hasReview ? '<a href="/reviews/' + r.slug + '/" style="color:#c9a84c;text-decoration:none;">' + esc(n.film) + '</a>' : esc(n.film)}
                </div>
              </div>
              <div style="flex-shrink:0;">
                ${hasReview ? '<span style="color:' + badgeColor + ';font-size:0.7rem;font-weight:700;padding:3px 8px;border-radius:4px;border:1px solid ' + badgeColor + ';">' + esc(r.verdict) + '</span>' : '<span style="color:#6a6a75;font-size:0.7rem;font-weight:600;">NO REVIEW</span>'}
              </div>
            </div>`;
    }).join('');
  }

  const reviewedBP = bestPictureNominees.filter(n => n.slug && reviewMap[n.slug]).length;

  const structuredData = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "2026 Oscar Nominees: Woke or Not? Complete VirtueVigil Scorecard",
    "description": "Are the 2026 Oscar nominees woke? VirtueVigil breaks down all 10 Best Picture nominees with Woke Scores, Traditional Scores, and verdicts.",
    "url": canonical,
    "publisher": { "@type": "Organization", "name": "VirtueVigil" },
    "datePublished": "2026-03-05",
    "dateModified": new Date().toISOString().split('T')[0],
    "mainEntity": {
      "@type": "ItemList",
      "numberOfItems": bestPictureNominees.length,
      "itemListElement": bestPictureNominees.map((n, i) => ({
        "@type": "ListItem",
        "position": i + 1,
        "name": n.title,
        "url": n.slug ? `${SITE_URL}/reviews/${n.slug}/` : undefined
      }))
    }
  };

  const oscarBreadcrumbs = breadcrumbLD([
    { name: 'Home', url: SITE_URL },
    { name: '2026 Oscar Nominees Scorecard', url: canonical }
  ]);

  const tradCount = bestPictureNominees.filter(n => { const r = n.slug ? reviewMap[n.slug] : null; return r && verdictClass(r.verdict) === 'traditional'; }).length;
  const mixedCount = bestPictureNominees.filter(n => { const r = n.slug ? reviewMap[n.slug] : null; return r && verdictClass(r.verdict) === 'mixed'; }).length;
  const wokeCount = bestPictureNominees.filter(n => { const r = n.slug ? reviewMap[n.slug] : null; return r && verdictClass(r.verdict) === 'woke'; }).length;

  return `${htmlHead({
    title: '2026 Oscar Nominees: Woke or Not? Complete VirtueVigil Scorecard',
    description: 'Are the 2026 Oscar nominees woke? VirtueVigil scores all 10 Best Picture nominees at the 98th Academy Awards. Woke Scores, Traditional Scores, and verdicts for Sinners, Hamnet, Marty Supreme, and more.',
    keywords: '2026 oscar nominees woke, oscars 2026 woke, 98th academy awards woke, are oscar nominees woke, sinners woke, hamnet woke, marty supreme woke, oscar best picture 2026, conservative oscar guide, woke movies 2026, academy awards scorecard',
    canonical,
    ogType: 'article',
    structuredData,
    breadcrumbs: oscarBreadcrumbs
  })}
<body>
  ${topBanner()}
  ${siteHeader('index')}

  <!-- Oscar Hero -->
  <section class="page-hero" style="padding:60px 20px 40px;background:linear-gradient(180deg,rgba(201,168,76,0.08) 0%,rgba(13,13,18,0) 100%);">
    <div class="container" style="max-width:900px;text-align:center;">
      <div style="font-size:3rem;margin-bottom:12px;">🏆</div>
      <h1 style="font-family:'Cinzel',Georgia,serif;font-size:2.2rem;line-height:1.2;margin-bottom:16px;">
        <span style="color:#c9a84c;">2026 Oscar Nominees:</span><br>Woke or Not?
      </h1>
      <p style="color:#a0a0a8;font-size:1.1rem;max-width:700px;margin:0 auto 20px;line-height:1.6;">
        The 98th Academy Awards air <strong style="color:#e8e6e1;">March 15, 2026</strong>. VirtueVigil has reviewed <strong style="color:#c9a84c;">${reviewedBP} of 10</strong> Best Picture nominees. Here is your complete scorecard so you know what Hollywood is celebrating before you watch.
      </p>
      <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:24px;">
        <a href="#best-picture" style="background:#c9a84c;color:#0d0d12;padding:10px 24px;border-radius:6px;font-weight:700;font-size:0.85rem;text-decoration:none;">Best Picture Scorecard</a>
        <a href="#best-director" style="border:1px solid rgba(201,168,76,0.4);color:#c9a84c;padding:10px 24px;border-radius:6px;font-weight:600;font-size:0.85rem;text-decoration:none;">Acting &amp; Directing</a>
      </div>
    </div>
  </section>

  <!-- Quick Stats Bar -->
  <div style="background:#14141c;border-top:1px solid rgba(201,168,76,0.15);border-bottom:1px solid rgba(201,168,76,0.15);padding:20px 0;">
    <div style="max-width:900px;margin:0 auto;display:flex;justify-content:center;gap:40px;flex-wrap:wrap;padding:0 20px;">
      <div style="text-align:center;">
        <div style="font-size:1.8rem;font-weight:700;color:#c9a84c;">10</div>
        <div style="font-size:0.75rem;color:#a0a0a8;text-transform:uppercase;letter-spacing:1px;">Best Picture Nominees</div>
      </div>
      <div style="text-align:center;">
        <div style="font-size:1.8rem;font-weight:700;color:#2ecc71;">${tradCount}</div>
        <div style="font-size:0.75rem;color:#a0a0a8;text-transform:uppercase;letter-spacing:1px;">Traditional / Lean Trad</div>
      </div>
      <div style="text-align:center;">
        <div style="font-size:1.8rem;font-weight:700;color:#d4a843;">${mixedCount}</div>
        <div style="font-size:0.75rem;color:#a0a0a8;text-transform:uppercase;letter-spacing:1px;">Mixed / Neutral</div>
      </div>
      <div style="text-align:center;">
        <div style="font-size:1.8rem;font-weight:700;color:#c44040;">${wokeCount}</div>
        <div style="font-size:0.75rem;color:#a0a0a8;text-transform:uppercase;letter-spacing:1px;">Woke / Lean Woke</div>
      </div>
    </div>
  </div>

  <div class="page-layout">
    ${sidebarHTML()}

    <main class="main-content" role="main" style="max-width:none;">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/">Home</a> <span>&rsaquo;</span>
        <span>2026 Oscar Nominees Scorecard</span>
      </nav>

      <!-- BEST PICTURE SECTION -->
      <section id="best-picture" style="margin-bottom:48px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:24px;">
          <span style="font-size:1.6rem;">🎬</span>
          <h2 style="font-family:'Cinzel',Georgia,serif;font-size:1.5rem;margin:0;color:#c9a84c;">Best Picture</h2>
        </div>
        <p style="color:#a0a0a8;font-size:0.9rem;margin-bottom:24px;">All 10 nominees scored by VirtueVigil. Sinners leads with a record-shattering 16 nominations. Tap any reviewed film for the full analysis.</p>

        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:20px;">
          ${bestPictureNominees.map(n => nomineeCard(n)).join('')}
        </div>
      </section>

      <!-- BEST DIRECTOR SECTION -->
      <section id="best-director" style="margin-bottom:40px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
          <span style="font-size:1.4rem;">🎥</span>
          <h2 style="font-family:'Cinzel',Georgia,serif;font-size:1.3rem;margin:0;color:#c9a84c;">Best Director</h2>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;">
          ${actorRow(bestDirectorNominees)}
        </div>
      </section>

      <!-- BEST ACTOR SECTION -->
      <section id="best-actor" style="margin-bottom:40px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
          <span style="font-size:1.4rem;">🎭</span>
          <h2 style="font-family:'Cinzel',Georgia,serif;font-size:1.3rem;margin:0;color:#c9a84c;">Best Actor</h2>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;">
          ${actorRow(bestActorNominees)}
        </div>
      </section>

      <!-- BEST ACTRESS SECTION -->
      <section id="best-actress" style="margin-bottom:40px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
          <span style="font-size:1.4rem;">👑</span>
          <h2 style="font-family:'Cinzel',Georgia,serif;font-size:1.3rem;margin:0;color:#c9a84c;">Best Actress</h2>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;">
          ${actorRow(bestActressNominees)}
        </div>
      </section>

      <!-- BOTTOM LINE -->
      <section style="background:#14141c;border:1px solid rgba(201,168,76,0.2);border-radius:10px;padding:28px;margin-bottom:40px;">
        <h2 style="font-family:'Cinzel',Georgia,serif;font-size:1.3rem;color:#c9a84c;margin:0 0 16px;">The Bottom Line</h2>
        <p style="color:#e8e6e1;line-height:1.7;font-size:0.95rem;margin:0 0 12px;">
          The 98th Academy Awards are a mixed bag for conservative viewers. The good news: several Best Picture nominees lean traditional or neutral. <strong>Sinners</strong>, <strong>F1</strong>, <strong>Train Dreams</strong>, and <strong>Marty Supreme</strong> all carry TRADITIONAL LEAN or TRADITIONAL verdicts from VirtueVigil. <strong>Sentimental Value</strong> scores NEUTRAL with a strong traditional lean in its scoring.
        </p>
        <p style="color:#e8e6e1;line-height:1.7;font-size:0.95rem;margin:0 0 12px;">
          The caution areas: <strong>One Battle After Another</strong> and <strong>Bugonia</strong> carry WOKE LEAN and MIXED verdicts respectively. <strong>Hamnet</strong> is genuinely mixed, with openly feminist framing wrapped around deeply traditional values of family and motherhood. <strong>The Secret Agent</strong> is also MIXED.
        </p>
        <p style="color:#e8e6e1;line-height:1.7;font-size:0.95rem;margin:0;">
          This is one of the more balanced Oscar Best Picture lineups in recent years. No "Barbie" or "Poor Things" level ideological provocations made the cut. Use our individual reviews to decide what is worth your time.
        </p>
      </section>

      <!-- CTA -->
      <div style="text-align:center;margin-bottom:40px;">
        <p style="color:#a0a0a8;font-size:0.9rem;margin-bottom:16px;">Want Woke Trap alerts before every major release?</p>
        <a href="/subscribe/" class="hero-cta" style="display:inline-flex;align-items:center;gap:8px;">
          <i class="fas fa-bell"></i> Subscribe to VirtueVigil
        </a>
      </div>

      <!-- More Reviews link -->
      <div style="text-align:center;margin-bottom:20px;">
        <a href="/" style="color:#c9a84c;font-weight:600;font-size:0.9rem;text-decoration:none;">
          <i class="fas fa-arrow-left"></i> Browse All ${reviews.length} Reviews
        </a>
      </div>
    </main>
  </div>

  ${fullFooter()}
${pageScripts()}
</body>
</html>`;
}


// ============================================
// LISTICLE PAGES
// ============================================

function buildListiclePage({ slug, title, description, canonicalPath, publishDate, htmlContent }) {
  const canonical = `${SITE_URL}/${canonicalPath}/`;
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": title,
    "description": description,
    "datePublished": publishDate,
    "dateModified": publishDate,
    "author": {
      "@type": "Organization",
      "name": "VirtueVigil",
      "url": SITE_URL
    },
    "publisher": {
      "@type": "Organization",
      "name": "VirtueVigil",
      "logo": { "@type": "ImageObject", "url": `${SITE_URL}/images/logo.svg` }
    },
    "mainEntityOfPage": { "@type": "WebPage", "@id": canonical }
  };
  const breadcrumbs = breadcrumbLD([
    { name: "Home", url: SITE_URL },
    { name: "Lists", url: `${SITE_URL}/lists/` },
    { name: title, url: canonical }
  ]);
  return `${htmlHead({
    title: `${title} | VirtueVigil`,
    description,
    canonical,
    ogType: 'article',
    structuredData,
    breadcrumbs
  })}
<body>
  ${topBanner()}
  ${siteHeader('lists')}

  <section class="page-hero">
    <div class="container">
      <h1>${title}</h1>
      <p class="lead">${esc(description)}</p>
    </div>
  </section>

  <div class="page-layout">
    ${sidebarHTML()}
    <main class="main-content" role="main">
      ${htmlContent}
    </main>
  </div>

  ${fullFooter()}
${pageScripts()}
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
  writePage('404.html', build404Page());
  writePage('oscars-2026/index.html', buildOscars2026Page());

  // --- Listicle pages ---
  console.log('\nBuilding listicle pages:');
  writePage('lists/most-woke-movies-2024/index.html', buildListiclePage({
    slug: 'most-woke-movies-2024',
    title: '10 Most Woke Movies of 2024 (Ranked by VirtueVigil Score)',
    description: 'The definitive ranking of the most ideologically woke films released in 2024, scored and analyzed using the VirtueVigil Woke Score methodology.',
    canonicalPath: 'lists/most-woke-movies-2024',
    publishDate: '2024-03-14',
    htmlContent: `<article class="listicle-article">
      <p>2024 was a year where Hollywood doubled down hard on progressive messaging. From prestige dramas to horror films to animated family fare, ideological content was woven into nearly every genre. Some films wore it openly. Others buried it under layers of craft, waiting until viewers were emotionally invested before revealing the thesis. Both approaches are documented here.</p>

      <p>VirtueVigil scores films on a 0-100 scale where a higher number indicates a greater density of ideologically progressive content. These are not quality ratings. A high woke score does not mean a film is bad, and a low one does not mean it is good. The score reflects how much ideological messaging the film contains relative to its runtime, and how aggressively that messaging is delivered.</p>

      <p>These 10 films topped our 2024 rankings. Every one of them has been reviewed in full on VirtueVigil with detailed trope-by-trope breakdowns. This list is a summary. If you want the full analysis, follow the links to each review.</p>

      <p>The rankings below run from #10 (lowest woke score in the top 10) to #1 (highest). Scores reflect density of ideological content as measured by the VirtueVigil Woke Score system, not artistic merit or entertainment value.</p>

      <hr>

      <h2>#10 - Love Lies Bleeding (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 26.0 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Genre:</strong> Thriller</p>
      <p>Rose Glass followed up Saint Maud with this surrealist neo-noir starring Kristen Stewart and Katy O'Brien. Stewart plays a gym manager in a violent family environment who falls for a female bodybuilder passing through town. The romance is explicitly lesbian, the relationship is intense and self-destructive, and the film tips into full surrealism by the final act. A24 distributed it. It premiered at Sundance. It sits at 94% on Rotten Tomatoes from critics. Glass is not interested in traditional narrative resolution, and the film's refusal of conventional moral frameworks is itself ideological. The woke score of 26 reflects consistent progressive content throughout, including the relationship framing, the treatment of the male characters in the story, and the surrealist climax that centers female rage as something mythic and justified.</p>
      <p><a href="/reviews/love-lies-bleeding-2024/">Read the full VirtueVigil review of Love Lies Bleeding</a></p>

      <hr>

      <h2>#9 - Emilia Perez (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 28.0 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Genre:</strong> Musical/Crime/Drama</p>
      <p>Jacques Audiard made a French film about a Mexican cartel boss who transitions to a woman, and it received 13 Oscar nominations -- the most ever for a non-English-language film. The film is genuinely strange and visually inventive, blending musical numbers, cartel violence, and identity transformation in ways that defy easy categorization. It also managed to unite progressive and conservative critics against it for different reasons: progressives criticized its depiction of Mexican culture and trans identity, conservatives objected to its central premise. The Academy celebrated it anyway. Our score reflects the density of identity-focused content layered into the cartel narrative, including how the transition is framed as liberation and moral rebirth, with the cartel past coded as a male identity to be discarded.</p>
      <p><a href="/reviews/emilia-perez-2024/">Read the full VirtueVigil review of Emilia Perez</a></p>

      <hr>

      <h2>#8 - Monkey Man (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 28.0 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Genre:</strong> Action</p>
      <p>Dev Patel wrote, directed, and starred in this revenge thriller set in a fictional Indian city ruled by corrupt politicians backed by Hindu nationalist religious figures. The film is a direct rebuke of Modi-era India filtered through John Wick-style action. Jordan Peele watched a rough cut and made sure it got into theaters after Netflix passed. The political subtext is not subtext -- it is the text. Patel spent seven years making this film, survived production injuries, and poured his anger at India's current political direction into every frame. The villain is essentially a thinly veiled Hindu nationalist, the hero comes from the lowest caste, and the climax takes place in a hijra sanctuary. That combination of identity politics and anti-establishment rage earns it a woke score of 28.</p>
      <p><a href="/reviews/monkey-man-2024/">Read the full VirtueVigil review of Monkey Man</a></p>

      <hr>

      <h2>#7 - Wicked (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 28.42 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Genre:</strong> Musical</p>
      <p>Jon M. Chu brought the Oz prequel to theaters with $150 million in marketing and 400 brand partnerships. Beneath the spectacle is a story about an outcast girl who is persecuted for being different -- the green-skinned Elphaba in a world that punishes nonconformity. The film frames institutional conformity as evil and otherness as strength. Ariana Grande plays Glinda as a well-meaning product of a corrupt system who slowly awakens to injustice. Cynthia Erivo's Elphaba is explicitly coded as a marginalized outsider whose radicalization is framed as moral growth. The marketing tried to position the film as family-friendly spectacle. The content is a consistent allegory for outsider identity, institutional corruption, and social justice awakening. Universal spent a fortune making it feel neutral. The story itself does not cooperate.</p>
      <p><a href="/reviews/wicked-2024/">Read the full VirtueVigil review of Wicked</a></p>

      <hr>

      <h2>#6 - Immaculate (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 29.0 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Genre:</strong> Horror</p>
      <p>Sydney Sweeney produced and stars in this film about an American nun who discovers she has been impregnated without consent at an Italian convent. Sweeney spent years developing the project specifically as a vehicle for its central message. The film uses Catholic iconography and the horror genre to deliver a forceful argument about bodily autonomy and reproductive rights. Every element of the convent setting is repurposed as a symbol of institutional control over women's bodies. The nuns who enforce the convent's rules are complicit in that control. The ending is one of the most explicit statements in recent mainstream horror: a woman destroys the institution that violated her body rather than accept her assigned role. There is no ambiguity about what the film is arguing for.</p>
      <p><a href="/reviews/immaculate-2024/">Read the full VirtueVigil review of Immaculate</a></p>

      <hr>

      <h2>#5 - MaXXXine (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 32.0 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Genre:</strong> Horror/Crime</p>
      <p>Ti West completed his X trilogy with a film set in 1985 Hollywood that doubles as a feminist manifesto wrapped in slasher aesthetics. Mia Goth stars as Maxine Minx, a survivor-turned-star whose ambition is framed as righteous defiance against a patriarchal entertainment industry. The film explicitly connects the religious right with misogyny and violence. Every male character is either predatory, incompetent, or both. The Satanic Panic backdrop is used to critique conservative moral authority. West is a skilled filmmaker, and the ideological content is embedded in genre conventions so effectively that it feels like part of the horror rather than a lecture. That craftsmanship is what pushes the woke score to 32. The messaging is dense, consistent, and never breaks character.</p>
      <p><a href="/reviews/maxxxine-2024/">Read the full VirtueVigil review of MaXXXine</a></p>

      <hr>

      <h2>#4 - Anora (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 36.0 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Genre:</strong> Drama</p>
      <p>Sean Baker won Best Picture at the 97th Academy Awards for this story of a Brooklyn sex worker who marries the son of a Russian oligarch, only to have the marriage annulled when his family intervenes. The film is sympathetic to its protagonist in a way that implicitly challenges conventional morality. It won the Palme d'Or at Cannes. The Academy followed Cannes. A consensus choice for the industry's most prestigious awards, and a film whose progressive framework is so deeply embedded in its storytelling that it does not need to announce itself. The sex work is presented without judgment. Class structures are interrogated. The ending refuses redemption through traditional means. Baker's filmmaking is naturalistic and humane, which makes the ideological content harder to isolate and easier to absorb.</p>
      <p><a href="/reviews/anora-2024/">Read the full VirtueVigil review of Anora</a></p>

      <hr>

      <h2>#3 - The Substance (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 37.0 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Genre:</strong> Horror</p>
      <p>Coralie Fargeat delivered a body horror film about a fading TV star who uses a black-market drug to create a younger version of herself. The film is a furious attack on Hollywood ageism and the male gaze, delivered with Cronenbergian excess and feminist fury. It does not pretend to be subtle. Every frame is a statement about how women are consumed by the entertainment industry. Demi Moore gives a career-redefining performance as a woman literally torn apart by the demand to stay young and desirable. Margaret Qualley plays her younger double with unsettling detachment. The body horror is the ideology made physical. Fargeat turns the camera into a weapon, forcing viewers to confront the violence of beauty standards. One of the most visually striking and deliberately provocative films of the year, with an authenticity index of 70 that confirms it believes every word it is saying.</p>
      <p><a href="/reviews/the-substance-2024/">Read the full VirtueVigil review of The Substance</a></p>

      <hr>

      <h2>#2 - Heretic (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 41.0 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Genre:</strong> Horror</p>
      <p>Hugh Grant stars as a soft-spoken man who traps two Mormon missionaries and proceeds to dismantle their faith using logic, manipulation, and film analysis. This is not a horror film that happens to include religion. It is an anti-Christian argument dressed in genre clothing. The film is intelligent, well-acted, and completely sincere in its goal of demonstrating that religion is a control mechanism. Grant's performance is magnetic and terrifying precisely because the character is articulate and persuasive. The missionaries are sympathetic but outmatched. The film gives religion a fair hearing only to demolish it systematically. Directors Scott Beck and Bryan Woods constructed a philosophical trap as tight as the physical one their characters are caught in. One of the most ideologically dense films of 2024, with a woke score that reflects just how relentlessly it pursues its thesis.</p>
      <p><a href="/reviews/heretic-2024/">Read the full VirtueVigil review of Heretic</a></p>

      <hr>

      <h2>#1 - Conclave (2024)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 42.6 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Genre:</strong> Thriller</p>
      <p>Edward Berger directed this prestige thriller about electing a new Pope that spends its entire runtime interrogating Catholic doctrine and pushing a progressive theological agenda. Ralph Fiennes leads an ensemble cast through Vatican corridors where every conversation is a proxy battle between tradition and reform. The film is elegantly shot, expertly acted, and deeply ideological. Cardinals who represent conservative positions are portrayed as corrupt, power-hungry, or complicit. The reformist faction is given moral clarity. The twist ending involving intersex identity is the climax the entire film builds toward, reframing everything that came before as a setup for a progressive revelation. A Woke Trap by VirtueVigil definition: the political content is buried under prestige filmmaking and only fully revealed near the end. Nominated for 8 Academy Awards. The highest woke score of any 2024 film we reviewed.</p>
      <p><a href="/reviews/conclave-2024/">Read the full VirtueVigil review of Conclave</a></p>

      <hr>

      <h2>Methodology Note</h2>
      <p>All scores are generated using the VirtueVigil Woke Score system, which measures the density and intensity of progressive ideological content across multiple categories including gender politics, religious critique, racial messaging, sexual content framing, and institutional critique. The system does not measure quality, entertainment value, or artistic merit. A high score means a film contains a high volume of identifiable progressive messaging relative to its runtime. For full details on how we score, visit our <a href="/methodology.html">Methodology</a> page.</p>

      <p>This list reflects films reviewed by VirtueVigil as of the publication date. Additional 2024 titles may be reviewed and ranked in the future. Scores are final once published and are not adjusted retroactively.</p>
    </article>`
  }));

  writePage('lists/best-conservative-movies/index.html', buildListiclePage({
    slug: 'best-conservative-movies',
    title: '15 Best Conservative Movies of All Time (Ranked by VirtueVigil Score)',
    description: 'The definitive ranking of the most traditionally-scored films in VirtueVigil history. Every entry is STRONGLY TRADITIONAL or TRADITIONAL with a positive score margin. Ranked by data, not opinion.',
    canonicalPath: 'lists/best-conservative-movies',
    publishDate: '2026-03-14',
    htmlContent: `<article class="listicle-article">

<p>What does a conservative movie actually look like when you measure it with data instead of vibes?</p>

<p>VirtueVigil uses a dual-scoring system: a Woke Score (0-100) measuring the density of progressive ideological content, and a Traditional Score (0-50) measuring the presence of traditional values content. The Score Margin tells you which direction the film leans and by how much.</p>

<p>This list ranks the 15 highest-scoring films in the STRONGLY TRADITIONAL and TRADITIONAL categories across all of VirtueVigil history. Every entry was selected on score alone. No personal favorites. No editorial thumb on the scale. The data made this list, not an agenda.</p>

<p>Each film is internally linked to its full VirtueVigil review, where you can read the complete trope audit, the creative team analysis, and the parental guidance assessment. The summary below gives you enough to make a viewing decision. The full review gives you the receipts.</p>

<p>One rule for this list: only films are eligible. TV series score separately. These are all theatrical or streaming films reviewed and scored by VirtueVigil analysts using the full VVWS methodology.</p>

<hr>

<h2>#1 &mdash; <a href="/reviews/reagan-2024/">Reagan (2024)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 44.28</span>
  <span class="mini-score woke">WOKE: 2.4</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +42 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Biography/Drama/History &bull; <strong>Platform:</strong> Theatrical</p>

<p>Reagan is the highest-scoring STRONGLY TRADITIONAL film in the VirtueVigil database. Dennis Quaid's portrayal of the 40th president is an unapologetic act of devotion, framing Reagan's life as a providential story of American greatness. The film's tradScore of 44.28 reflects dense traditional values content throughout: God, country, family, anti-communism, and the moral clarity of the Cold War. Jon Voight's framing narration as a KGB agent who grudgingly admires his subject is the smartest structural decision in the film. Critics hated it (18% on Rotten Tomatoes). The audience loved it (98%). That gap tells you everything about whose values it was made for.</p>

<p><a href="/reviews/reagan-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Reagan</a></p>

<hr>

<h2>#2 &mdash; <a href="/reviews/ne-zha-2-2025/">Ne Zha 2 (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 38.57</span>
  <span class="mini-score woke">WOKE: 0</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +39 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Animation/Fantasy/Action &bull; <strong>Platform:</strong> Theatrical</p>

<p>Ne Zha 2 is proof that the most powerful conservative filmmaking in the world is not coming from Hollywood right now. It is coming from China. The sequel to the 2019 box office phenomenon carries forward a story rooted in Taoist mythology about destiny, sacrifice, filial loyalty, and the courage to defy a corrupt cosmic order. A woke score of exactly zero. A tradScore of 38.57. The highest-grossing animated film ever made, and it earned it. The film's themes of personal responsibility, respect for tradition, and the debt sons owe their fathers are not incidental to the story. They are the story.</p>

<p><a href="/reviews/ne-zha-2-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Ne Zha 2</a></p>

<hr>

<h2>#3 &mdash; <a href="/reviews/am-i-racist-2024/">Am I Racist? (2024)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 33.81</span>
  <span class="mini-score woke">WOKE: 3.7</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +30 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Documentary/Comedy &bull; <strong>Platform:</strong> Theatrical / DailyWire+</p>

<p>Matt Walsh brought a hidden camera to the DEI industry and let it destroy itself. Am I Racist? follows Walsh as he goes undercover, pays real money for DEI certification, and interviews the activists and consultants who have built a multi-billion dollar industry around racial guilt. The documentary is funny, infuriating, and methodically damning. A tradScore of 33.81 reflects dense traditional values content throughout: the film treats equality under the law as a self-evident good, rejects race-based classification systems, and documents the absurdity of ideological purity tests with the patience of a prosecutorial brief.</p>

<p><a href="/reviews/am-i-racist-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Am I Racist?</a></p>

<hr>

<h2>#4 &mdash; <a href="/reviews/how-to-train-your-dragon-2025/">How to Train Your Dragon (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 33.2</span>
  <span class="mini-score woke">WOKE: 4.7</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +29 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Family/Adventure &bull; <strong>Platform:</strong> Theatrical</p>

<p>Dean DeBlois refused to let Hollywood ruin his dragons. After directing all three animated films, he insisted on full creative control for the live-action remake and got it. What he made is an anomaly: a 2025 major studio release that is genuinely pro-family, centered on masculine mentorship, and completely free of ideological agenda. A tradScore of 33.2 with a woke score of only 4.7. The story of a son proving himself to a disappointed father, finding courage through a forbidden friendship, and saving a community that doubted him is told without condescension and without revision. It is exactly what a conservative family needs from an action-adventure film.</p>

<p><a href="/reviews/how-to-train-your-dragon-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of How to Train Your Dragon</a></p>

<hr>

<h2>#5 &mdash; <a href="/reviews/sound-of-freedom-2023/">Sound of Freedom (2023)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 30.8</span>
  <span class="mini-score woke">WOKE: 4.2</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +27 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action &bull; <strong>Platform:</strong> Streaming</p>

<p>Angel Studios distributed the film that Hollywood buried. Sound of Freedom sat on a shelf for five years after Disney's acquisition of Fox because nobody in the corporate entertainment ecosystem wanted to back a $14.5 million movie about child trafficking. Jim Caviezel plays Tim Ballard, a DHS agent who leaves his government job to rescue exploited children in Colombia. A tradScore of 30.8 with a woke score of 4.2. The film earned over $250 million at the box office on a word-of-mouth campaign that bypassed mainstream critics entirely. It is the most successful independent release in modern history, and it exists because audiences showed up without being told to.</p>

<p><a href="/reviews/sound-of-freedom-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Sound of Freedom</a></p>

<hr>

<h2>#6 &mdash; <a href="/reviews/horizon-an-american-saga-2024/">Horizon: An American Saga (2024)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 28.98</span>
  <span class="mini-score woke">WOKE: 6.35</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +23 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Epic Western &bull; <strong>Platform:</strong> Theatrical</p>

<p>Kevin Costner spent 35 years trying to make this film. He mortgaged his personal assets for $38 million to fund a Western epic about the American frontier that Hollywood refused to greenlight. Horizon: An American Saga Chapter 1 is an unapologetically patriotic vision of westward expansion, told with the sweeping patience of a John Ford film and the personal conviction of a filmmaker who actually believes in the story he is telling. A tradScore of 28.98. The film was not a commercial success, which is a genuine cultural loss. It is the kind of movie that can only be made by someone who does not need anyone's permission.</p>

<p><a href="/reviews/horizon-an-american-saga-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Horizon: An American Saga</a></p>

<hr>

<h2>#7 &mdash; <a href="/reviews/solo-leveling-reawakening-2024/">Solo Leveling: ReAwakening (2024)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 28.35</span>
  <span class="mini-score woke">WOKE: 1.26</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +27 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Animation/Action/Fantasy &bull; <strong>Platform:</strong> Theatrical</p>

<p>The highest-grossing anime theatrical event ever released in North America, and one of the cleanest watches in the VirtueVigil database for parents with teenage sons. Solo Leveling: ReAwakening follows Sung Jinwoo, the weakest hunter in a world of monsters, as he discovers a hidden power and begins a solitary ascent toward strength. A woke score of 1.26. A tradScore of 28.35. The film's values are straightforwardly traditional: self-improvement through hardship, protection of the weak, personal sacrifice for the people you love, and the importance of becoming someone worthy of the burdens placed on you.</p>

<p><a href="/reviews/solo-leveling-reawakening-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Solo Leveling: ReAwakening</a></p>

<hr>

<h2>#8 &mdash; <a href="/reviews/david-2025/">David (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 28</span>
  <span class="mini-score woke">WOKE: 2</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +26 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Animation/Musical/Biblical Epic &bull; <strong>Platform:</strong> Theatrical / Angel Studios</p>

<p>Angel Studios animated a 3,000-year-old story and made it feel urgent. David follows the shepherd boy from Bethlehem through his anointing, his friendship with Jonathan, his confrontation with Goliath, and his tumultuous relationship with the increasingly unhinged King Saul. It is a biblical musical with real dramatic weight. A tradScore of 28 with a woke score of 2. The film's treatment of faith is unashamed: God is real, covenant matters, and courage in the face of impossible odds is what God asks of the people He chooses. There is nothing subtle about the message. That is the point.</p>

<p><a href="/reviews/david-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of David</a></p>

<hr>

<h2>#9 &mdash; <a href="/reviews/peaky-blinders-the-immortal-man-2026/">Peaky Blinders: The Immortal Man (2026)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 28</span>
  <span class="mini-score woke">WOKE: 5</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +23 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Crime/Drama/History &bull; <strong>Platform:</strong> Theatrical / Netflix</p>

<p>The Peaky Blinders film does not apologize for Tommy Shelby and it does not soften him. Cillian Murphy returns as a man who comes out of hiding to save his son, fight the rise of European fascism, and settle thirty years of debt to his family and his city. A tradScore of 28 with a woke score of 5. The film is masculine, violent, and morally serious in the way that only crime dramas about consequences can be. It is a celebration of conviction, loyalty, and the kind of love that expresses itself through protection rather than sentiment. The best theatrical crime drama in years.</p>

<p><a href="/reviews/peaky-blinders-the-immortal-man-2026/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Peaky Blinders: The Immortal Man</a></p>

<hr>

<h2>#10 &mdash; <a href="/reviews/the-wild-robot-2024/">The Wild Robot (2024)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 27.93</span>
  <span class="mini-score woke">WOKE: 7.12</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +21 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Animation &bull; <strong>Platform:</strong> Theatrical / Peacock</p>

<p>Chris Sanders made the most subversive animated film of 2024, and not in the way Hollywood usually means that word. In a year full of films teaching children lessons about identity and inclusion, Sanders made a movie about a robot who accidentally becomes a mother and discovers that raising a child is the most important thing she will ever do. A tradScore of 27.93. The Wild Robot is a masterwork of visual storytelling that champions self-sacrifice, the irreplaceable bond between parent and child, and the communal obligation to protect the next generation. DreamWorks let this get made and it deserved every award it received.</p>

<p><a href="/reviews/the-wild-robot-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The Wild Robot</a></p>

<hr>

<h2>#11 &mdash; <a href="/reviews/the-accountant-2-2025/">The Accountant 2 (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 26.46</span>
  <span class="mini-score woke">WOKE: 4.2</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +22 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action/Crime/Thriller &bull; <strong>Platform:</strong> Theatrical / Amazon MGM</p>

<p>Christian Wolff is one of the most quietly compelling protagonists in contemporary action cinema: a forensic accountant with autism who operates outside the law in service of a rigorous personal moral code. The Accountant 2 does what rare sequels manage to do, which is deepen the original without betraying it. A tradScore of 26.46 with a woke score of 4.2. The film's values are embedded in the character: loyalty to family, the weight of commitment, justice achieved through personal risk rather than institutional authority. Ben Affleck gives one of his most controlled performances. The action is excellent. The ideology is clean.</p>

<p><a href="/reviews/the-accountant-2-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The Accountant 2</a></p>

<hr>

<h2>#12 &mdash; <a href="/reviews/karate-kid-legends-2025/">Karate Kid: Legends (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 26.32</span>
  <span class="mini-score woke">WOKE: 3.15</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +23 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action/Drama/Family &bull; <strong>Platform:</strong> Theatrical</p>

<p>VirtueVigil gave Karate Kid: Legends the safest family recommendation we issue. It is not a woke trap. It is not even close. The film is about older men transmitting wisdom to a young man who needs it, centered on discipline and honor, and it delivers exactly what the trailer promises. A tradScore of 26.32 with a woke score of only 3.15. Jackie Chan and Ben Wang bring genuine warmth to a mentorship story that trusts the audience enough to play it straight. Buy a ticket without hesitation. The only question to ask is about quality, and the answer there is good enough to be worth your Saturday afternoon.</p>

<p><a href="/reviews/karate-kid-legends-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Karate Kid: Legends</a></p>

<hr>

<h2>#13 &mdash; <a href="/reviews/john-wick-chapter-4-2023/">John Wick: Chapter 4 (2023)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 23.52</span>
  <span class="mini-score woke">WOKE: 0.5</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +23 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action/Crime/Thriller &bull; <strong>Platform:</strong> Theatrical</p>

<p>John Wick: Chapter 4 is the cleanest major franchise from a traditional values standpoint in the last five years and also one of the best action films of the decade. A woke score of 0.5. A tradScore of 23.52. Chad Stahelski's nearly three-hour conclusion to John Wick's arc scales everything that made the first film work to operatic proportions: the honor codes, the loyalty oaths, the world-building built on contracts and consequences rather than ideology. The film's internal moral universe is more coherent than most dramas. John Wick does what he does because he made promises to people he loves and he keeps them. That is the whole movie.</p>

<p><a href="/reviews/john-wick-chapter-4-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of John Wick: Chapter 4</a></p>

<hr>

<h2>#14 &mdash; <a href="/reviews/top-gun-maverick-2022/">Top Gun: Maverick (2022)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 21.28</span>
  <span class="mini-score woke">WOKE: 1.05</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +20 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action/Drama &bull; <strong>Platform:</strong> Theatrical</p>

<p>Top Gun: Maverick is the best American action film in at least a decade. That is not hyperbole. It is a film that remembered something most of Hollywood has forgotten, which is that audiences want to feel something, not be taught something. A tradScore of 21.28 with a woke score of only 1.05. Tom Cruise plays a man who has spent 30 years refusing to become what the Navy needs him to be: a manager, an administrator, a relic. His refusal is not selfishness. It is conviction. The film is pro-military without being naive, patriotic without being preachy, and emotionally generous to every character including the ones it sets up as antagonists. The last great Hollywood blockbuster.</p>

<p><a href="/reviews/top-gun-maverick-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Top Gun: Maverick</a></p>

<hr>

<h2>#15 &mdash; <a href="/reviews/the-batman-2022/">The Batman (2022)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 22.05</span>
  <span class="mini-score woke">WOKE: 8</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +14 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Superhero/Crime/Neo-Noir &bull; <strong>Platform:</strong> Theatrical / Max</p>

<p>The Batman earns its place on this list not through patriotism or faith, but through moral seriousness. Matt Reeves made a detective story about a man who understands that systemic corruption cannot be fixed by punching criminals, and has to reckon with his own complicity in the city's rot. A tradScore of 22.05. The film is dark, methodical, and genuinely frightening in ways that have nothing to do with special effects. Robert Pattinson's Batman is not an aspirational figure. He is a grief-consumed man slowly learning that justice requires more than vengeance. That moral arc, and the film's unflinching willingness to follow it to its logical conclusion, makes it one of the most serious superhero films ever made.</p>

<p><a href="/reviews/the-batman-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The Batman</a></p>

<hr>

<div class="listicle-conclusion">
<h2>The Methodology Behind This List</h2>

<p>Every score on this list comes from a VirtueVigil analyst applying the full VVWS (VirtueVigil Weighted Scoring) methodology. That means a trope-by-trope audit of every ideological element in the film, weighted by severity, authenticity, and centrality to the narrative.</p>

<p>The Traditional Score measures: family values content, patriotic themes, faith-positive framing, masculine virtue coding, work ethic and personal responsibility, rule of law and institutional trust, and traditional gender role representation. The Woke Score measures the inverse: progressive identity politics, anti-establishment messaging, traditional value deconstruction, and ideological prescription.</p>

<p>The Score Margin is simply Traditional Score minus Woke Score. A positive margin means the film's values tilt conservative. A negative margin means they tilt progressive. Every film on this list has a positive margin.</p>

<p>This list will be updated quarterly as new reviews are published. If a film earns a high enough score to enter the top 15, it will appear here. The data decides the rankings. We just do the math.</p>

<p>Want to see what the opposite looks like? Read our companion list: <a href="/lists/most-woke-movies-2024/">10 Most Woke Movies of 2024</a>.</p>

<p>Questions about methodology? Start with the <a href="/methodology.html">VirtueVigil Methodology</a> page.</p>
</div>

</article>`
  }));

  writePage('lists/family-friendly-movies-2024/index.html', buildListiclePage({
    slug: 'family-friendly-movies-2024',
    title: 'Top 10 Family-Friendly Movies That Won\'t Push an Agenda',
    description: 'Looking for family movies without the woke agenda? Here are the 10 best family-friendly films with the lowest woke scores on VirtueVigil.',
    canonicalPath: 'lists/family-friendly-movies-2024',
    publishDate: '2026-03-15',
    htmlContent: `<article class="listicle-article">

<p>Parents, you know the feeling. You sit down to watch a movie with your kids and thirty minutes in, someone is delivering a lecture you did not sign up for. A character's identity becomes the plot. Traditional values get mocked by the one character everyone is supposed to like. You came for entertainment and you got a classroom. That is what a high woke score looks like in practice. On VirtueVigil, our Woke-Watch Scoring System flags exactly that kind of ideological content so you know what you are walking into before you press play.</p>

<p>A low woke score means the film stays out of your lane. It tells a story, develops characters, and delivers genuine entertainment without stopping to remind you that the world needs to change. These ten films earned woke scores under 8 out of a possible 30-plus points, while scoring high on traditional values like family loyalty, courage, faith, sacrifice, and personal responsibility. We pulled every review in our database, filtered for family-appropriate content, and ranked by traditional values score. This is your no-surprises watchlist.</p>

<hr>

<h2>#1 - The SpongeBob Movie: Search for SquarePants (2025)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+42 TRAD</span>
  <span class="woke-score">Woke Score: 1.3</span>
  <span class="trad-score">Trad Score: 43.1</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Animation/Adventure/Comedy &bull; <strong>MPAA:</strong> PG &bull; <strong>Recommended Age:</strong> 5+</p>
<p>The fourth SpongeBob theatrical film is pure, uncut fun with zero ideological agenda. It is a story about friendship and courage told exactly as advertised, with a surrogate father figure in Mr. Krabs coaching SpongeBob to be brave and bold. No lectures, no identity politics, just heart and humor that earns its laughs without asking anything of you politically. One of the cleanest woke scores of any film we have reviewed, and one of the best choices for young children on this list.</p>
<p><a href="/reviews/the-spongebob-movie-search-for-squarepants-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The SpongeBob Movie: Search for SquarePants</a></p>

<hr>

<h2>#2 - Ne Zha 2 (2025)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+39 TRAD</span>
  <span class="woke-score">Woke Score: 0</span>
  <span class="trad-score">Trad Score: 38.6</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Animation/Fantasy/Action &bull; <strong>MPAA:</strong> PG &bull; <strong>Recommended Age:</strong> 8+</p>
<p>The Chinese animated sequel earns a perfect zero on the woke scale and delivers one of the most emotionally powerful animated films in years. The story centers on destiny, sacrifice, and the love between a father and son. It is mythological, visually stunning, and built entirely around honor and protecting the people you love. The violence is fantasy-level and not gory. The emotional content, parents losing a child who chooses his own fate, may move younger viewers more than you expect.</p>
<p><a href="/reviews/ne-zha-2-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Ne Zha 2</a></p>

<hr>

<h2>#3 - Reagan (2024)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+42 TRAD</span>
  <span class="woke-score">Woke Score: 2.4</span>
  <span class="trad-score">Trad Score: 44.3</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Biography/Drama/History &bull; <strong>MPAA:</strong> PG-13 &bull; <strong>Recommended Age:</strong> 10+</p>
<p>The highest traditional values score in our entire database, and clean enough for older kids. Reagan is a reverential biopic about the 40th president that treats faith, patriotism, and leadership as genuine virtues. No sexual content, no drug use, no strong language. The assassination attempt is the only intense scene, and it is handled with restraint. If you want a film that your children will walk away from with a clearer sense of what American leadership looks like at its best, this is the one.</p>
<p><a href="/reviews/reagan-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Reagan</a></p>

<hr>

<h2>#4 - How to Train Your Dragon (2025)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+29 TRAD</span>
  <span class="woke-score">Woke Score: 4.7</span>
  <span class="trad-score">Trad Score: 33.2</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Family/Adventure &bull; <strong>MPAA:</strong> PG &bull; <strong>Recommended Age:</strong> 7+</p>
<p>The live-action remake handled by the original director keeps every value that made the animated trilogy beloved: a son earning his father's respect, courage in the face of ridicule, and friendship built on trust rather than shared ideology. Dragon battles are intense but not graphic. This is exactly what family adventure should look like, with Gerard Butler as Stoick delivering one of the more believable on-screen father figures in recent memory.</p>
<p><a href="/reviews/how-to-train-your-dragon-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of How to Train Your Dragon</a></p>

<hr>

<h2>#5 - Am I Racist? (2024)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+30 TRAD</span>
  <span class="woke-score">Woke Score: 3.7</span>
  <span class="trad-score">Trad Score: 33.8</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Documentary/Comedy &bull; <strong>MPAA:</strong> PG-13 &bull; <strong>Recommended Age:</strong> 14+</p>
<p>Matt Walsh's satirical documentary dismantles the DEI industrial complex with a hidden-camera approach that is equal parts funny and genuinely revealing. Rated PG-13 for language and thematic content. Best for older teens and adults who are ready to have a conversation about what the anti-racism industry actually teaches and who it actually serves. A film that starts conversations, not ends them.</p>
<p><a href="/reviews/am-i-racist-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Am I Racist?</a></p>

<hr>

<h2>#6 - Sound of Freedom (2023)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+27 TRAD</span>
  <span class="woke-score">Woke Score: 4.2</span>
  <span class="trad-score">Trad Score: 30.8</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action &bull; <strong>MPAA:</strong> PG-13 &bull; <strong>Recommended Age:</strong> 13+</p>
<p>The film Hollywood tried to bury for five years. Sound of Freedom follows a DHS agent who walks away from his career to rescue trafficked children in Colombia. No sexual abuse is depicted on screen. The story is straightforward heroism built around a man who chooses the harder right over the easier wrong. Powerful viewing for mature teens and adults who are ready to see what one person's moral courage looks like in practice.</p>
<p><a href="/reviews/sound-of-freedom-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Sound of Freedom</a></p>

<hr>

<h2>#7 - David (2025)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+26 TRAD</span>
  <span class="woke-score">Woke Score: 2.0</span>
  <span class="trad-score">Trad Score: 28.0</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Animation/Musical/Biblical Epic &bull; <strong>MPAA:</strong> PG &bull; <strong>Recommended Age:</strong> 6+</p>
<p>Angel Studios' animated biblical musical tells the story of King David from his anointing through his defeat of Goliath and rise to Israel's throne. The film scored $84 million at the box office because it does what faith-based cinema rarely manages: it is both genuinely entertaining and spiritually serious. The songs are memorable, the animation is expressive, and the theology is sound. Appropriate for nearly all ages and an excellent choice for families with a faith background.</p>
<p><a href="/reviews/david-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of David</a></p>

<hr>

<h2>#8 - Karate Kid: Legends (2025)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+23 TRAD</span>
  <span class="woke-score">Woke Score: 3.1</span>
  <span class="trad-score">Trad Score: 26.3</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Drama/Family &bull; <strong>MPAA:</strong> PG-13 &bull; <strong>Recommended Age:</strong> 10+</p>
<p>Our review called it the most traditionally coded major studio release of 2025. Older men teach a young man discipline, courage, and honor. That is the whole film. Jackie Chan and Ralph Macchio together again in a mentorship story built on the values that made the original franchise great. Martial arts violence is present but not graphic. If you are looking for a film that models what good mentorship between generations looks like, this is it.</p>
<p><a href="/reviews/karate-kid-legends-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Karate Kid: Legends</a></p>

<hr>

<h2>#9 - The Lion King (2019)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+23 TRAD</span>
  <span class="woke-score">Woke Score: 2.7</span>
  <span class="trad-score">Trad Score: 25.3</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Musical/Drama/Adventure &bull; <strong>MPAA:</strong> PG &bull; <strong>Recommended Age:</strong> 6+</p>
<p>The photorealistic remake preserves every value from the 1994 original intact: a son's duty to his father's legacy, the courage to claim your rightful place, and a villain who seizes power through deception and holds it through fear. The story of Simba is one of the most traditionally structured narratives Disney ever produced, and the 2019 version protects that structure completely. The animation may be technically cold, but the values are warm and consistent.</p>
<p><a href="/reviews/the-lion-king-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The Lion King</a></p>

<hr>

<h2>#10 - Fast X (2023)</h2>
<div class="listicle-scores">
  <span class="score-badge trad">STRONGLY TRADITIONAL</span>
  <span class="score-margin trad">+20 TRAD</span>
  <span class="woke-score">Woke Score: 6.1</span>
  <span class="trad-score">Trad Score: 26.5</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Adventure &bull; <strong>MPAA:</strong> PG-13 &bull; <strong>Recommended Age:</strong> 12+</p>
<p>The Fast and Furious franchise has always been built on one unironic thesis: family is the most powerful force in the universe. Fast X delivers that thesis at full volume with zero sexual content, no drug use, and action that is intense but not graphic. Jason Momoa is the best villain this franchise has ever had. The woke score edges toward the upper end of our list, but the traditional values content, loyalty, sacrifice, and family above everything, more than compensates.</p>
<p><a href="/reviews/fast-x-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Fast X</a></p>

<hr>

<h2>What Does a Low Woke Score Actually Mean?</h2>
<p>Every film on this list was scored using VirtueVigil's Woke-Watch Scoring System, which evaluates ideological content across more than a dozen categories including gender politics, religious framing, racial messaging, sexual content framing, and institutional critique. A score under 8 means the film barely registers in any of those categories. It tells its story without stopping to make a political point.</p>

<p>That does not mean these films are free of all conflict or edge. How to Train Your Dragon has dragon battles. Sound of Freedom deals with child trafficking. Karate Kid has tournament fighting. What they share is an absence of progressive agenda-setting. The conflict is not political. The resolution is not ideological. You know what you are getting before the credits roll.</p>

<p>Browse our full review database at <a href="/">VirtueVigil</a> to find more films scored and sorted for conservative families. Every review includes a complete parental guidance section so you can make the call that is right for your household.</p>

<p>Want to see the other side? Read our companion list: <a href="/lists/most-woke-movies-2024/">10 Most Woke Movies of 2024</a>.</p>

</article>`
  }));

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

  // By type (normalise: treat both 'series' and 'tv' as series)
  catMap['Films'] = { slug: 'films', reviews: reviews.filter(r => r.type === 'film') };
  catMap['Series'] = { slug: 'series', reviews: reviews.filter(r => r.type === 'series' || r.type === 'tv') };

  // Woke traps
  const trapReviews = reviews.filter(r => isWokeTrap(r));
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

  // --- Search Index ---
  console.log('\nGenerating search index:');
  const searchIndex = reviews.map(r => ({
    slug: r.slug,
    title: r.title,
    verdict: r.verdict,
    platform: r.platform,
    genre: r.genre,
    year: r.year,
    type: r.type,
    wokeScore: r.wokeScore,
    tradScore: r.tradScore,
    poster: r.poster || null,
  }));
  const searchIndexJson = JSON.stringify(searchIndex, null, 2);
  fs.writeFileSync(path.join(DIST, 'search-index.json'), searchIndexJson);
  fs.writeFileSync(path.join(SRC, 'data', 'search-index.json'), searchIndexJson);
  console.log(`  search-index.json (${searchIndex.length} entries)`);

  // --- SEO files ---
  console.log('\nGenerating SEO files:');
  writePage('sitemap.xml', buildSitemap(catMap));
  writePage('robots.txt', buildRobotsTxt());
  writePage('google3fdcf99a0ee9d694.html', 'google-site-verification: google3fdcf99a0ee9d694.html');

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

  // IndexNow key file for Bing/Yandex/DuckDuckGo indexing
  const indexNowKey = 'c5c06a51b3df4a6fb07de4954187d031';
  fs.writeFileSync(path.join(DIST, `${indexNowKey}.txt`), indexNowKey);
  console.log('  IndexNow key file');

  // --- Summary ---
  const subscriberPages = 3; // subscribe, account, auth/callback
  const staticPages = 5; // index, about, methodology, woke-trap, 404
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
