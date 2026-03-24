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
        <p><a href="/privacy/">Privacy Policy</a> &middot; <a href="/terms/">Terms of Service</a></p>
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


function whereToWatchBlock(r) {
  const query = encodeURIComponent(`${r.title} ${r.year}`);
  const tag = 'virtuevigil-20';
  const url = `https://www.amazon.com/s?k=${query}&i=instant-video&tag=${tag}`;
  return `
<div class="where-to-watch" style="margin:28px 0;padding:20px 24px;background:rgba(201,168,76,0.08);border:1px solid rgba(201,168,76,0.25);border-radius:8px;">
  <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:var(--gold);margin-bottom:12px;">Where to Watch</div>
  <p style="font-size:0.9rem;color:var(--text-secondary,#ccc);margin:0 0 14px;">Find <strong>${esc(r.title)}</strong> on Amazon Prime Video, rent, or buy:</p>
  <a href="${url}" target="_blank" rel="noopener nofollow"
     style="display:inline-flex;align-items:center;gap:8px;background:#FF9900;color:#000;font-weight:700;font-size:0.85rem;padding:10px 18px;border-radius:6px;text-decoration:none;">
    <span style="font-size:1rem;">&#9654;</span> Stream or Buy on Amazon
  </a>
  <p style="font-size:0.75rem;color:var(--text-secondary,#999);margin:8px 0 0;opacity:0.7;">As an Amazon Associate, VirtueVigil earns from qualifying purchases.</p>
</div>`;
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
                <span><i class="fas fa-user-edit"></i> Analyzed by <span itemprop="author">Debra Ducane</span></span>
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
          ${whereToWatchBlock(r)}
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
    { loc: `${SITE_URL}/lists/most-woke-movies-2023/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/most-woke-movies-2021/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/most-woke-movies-2019/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/family-friendly-movies-2024/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/a24-movies-woke-ranking/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/woke-horror-movies-2024/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/woke-sequels-more-woke-than-original/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/rotten-tomatoes-vs-virtuevigil/`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${SITE_URL}/lists/best-faith-based-movies/`, changefreq: 'monthly', priority: '0.8' },
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
// LEGAL PAGES
// ============================================

function buildTermsPage() {
  const canonical = `${SITE_URL}/terms/`;
  return `${htmlHead({
    title: 'Terms of Service \u2014 VirtueVigil',
    description: 'VirtueVigil Terms of Service. Read the terms governing your use of virtuevigil.com, including intellectual property, affiliate disclosure, and limitation of liability.',
    canonical,
  })}
<body>
  ${siteHeader('')}

  <section class="page-hero">
    <div class="container">
      <h1>Terms of <span class="text-gold">Service</span></h1>
      <p>Effective Date: March 1, 2026</p>
    </div>
  </section>

  <article class="content-article">
    <p>Welcome to VirtueVigil (&ldquo;we,&rdquo; &ldquo;us,&rdquo; or &ldquo;our&rdquo;). By accessing or using the website located at <a href="https://virtuevigil.com">virtuevigil.com</a> (the &ldquo;Site&rdquo;), you agree to be bound by these Terms of Service (&ldquo;Terms&rdquo;). If you do not agree, please do not use the Site.</p>

    <h2>1. Use of the Site</h2>
    <p>VirtueVigil is a media review and commentary website. The Site is intended for personal, non-commercial use. You agree to use the Site only for lawful purposes and in a manner consistent with these Terms and all applicable laws and regulations.</p>
    <p>You may not use the Site to:</p>
    <ul>
      <li>Transmit any content that is unlawful, defamatory, harassing, abusive, fraudulent, or obscene;</li>
      <li>Attempt to gain unauthorized access to any portion of the Site or its related systems;</li>
      <li>Scrape, crawl, or harvest Site content in bulk without prior written permission;</li>
      <li>Interfere with or disrupt the integrity or performance of the Site;</li>
      <li>Impersonate any person or entity, including VirtueVigil, Debra Ducane, or any other user.</li>
    </ul>

    <h2>2. Intellectual Property</h2>
    <p>All content on the Site &mdash; including but not limited to text, reviews, analysis, scoring systems, graphics, logos, images, and the VirtueVigil name and brand &mdash; is the property of VirtueVigil and is protected by applicable copyright, trademark, and intellectual property laws.</p>
    <p>You may share brief excerpts of reviews for commentary, criticism, or news purposes, provided that you clearly attribute the content to VirtueVigil and include a link back to the original page on the Site. Reproduction of full reviews or substantial portions of content without prior written consent is prohibited.</p>
    <p>The VirtueVigil name, logo, and the &ldquo;Guarding Values. Exposing Agendas.&rdquo; tagline are proprietary to VirtueVigil. You may not use them without express written permission.</p>

    <h2>3. User Conduct and Community Comments</h2>
    <p>Registered subscribers may post comments on reviews. By submitting a comment, you grant VirtueVigil a non-exclusive, royalty-free, worldwide license to display and distribute that comment on the Site.</p>
    <p>You are solely responsible for the content of your comments. VirtueVigil reserves the right, but not the obligation, to review, edit, or remove any user comment that we determine in our sole discretion to be:</p>
    <ul>
      <li>Spam, off-topic, or promotional;</li>
      <li>Defamatory, threatening, or harassing;</li>
      <li>In violation of any applicable law;</li>
      <li>Otherwise inconsistent with the purpose and tone of the Site.</li>
    </ul>
    <p>Repeated violations may result in suspension or termination of your account.</p>

    <h2>4. Affiliate Disclosure</h2>
    <p>VirtueVigil participates in the Amazon Associates program and other affiliate marketing programs. Some links on the Site &mdash; including &ldquo;Where to Watch&rdquo; links &mdash; are affiliate links. If you click an affiliate link and make a purchase, VirtueVigil may earn a commission at no additional cost to you.</p>
    <p>Affiliate relationships do not influence our reviews, scoring, or editorial positions. All reviews represent our independent analysis under the VirtueVigil scoring methodology.</p>

    <h2>5. Advertising</h2>
    <p>The Site may display third-party advertisements. VirtueVigil does not endorse any advertiser or the products or services they promote. We are not responsible for the content of third-party advertisements or for any transactions between you and third-party advertisers.</p>

    <h2>6. Disclaimers</h2>
    <p>VirtueVigil reviews and scores are editorial opinions, not objective facts. Scores, verdicts, and analyses represent the views of VirtueVigil based on our stated methodology. Reasonable people may disagree with our assessments, and we acknowledge that media criticism involves subjective judgment.</p>
    <p>Debra Ducane is a persona used to present VirtueVigil&rsquo;s content. The analyses and opinions attributed to Debra Ducane are editorial content produced by VirtueVigil.</p>
    <p>The Site may contain links to third-party websites. VirtueVigil is not responsible for the content, accuracy, or privacy practices of those sites.</p>

    <h2>7. No Warranty</h2>
    <p>THE SITE AND ALL CONTENT ON IT ARE PROVIDED &ldquo;AS IS&rdquo; AND &ldquo;AS AVAILABLE&rdquo; WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED. VIRTUEVIGIL DISCLAIMS ALL WARRANTIES, INCLUDING BUT NOT LIMITED TO IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. WE DO NOT WARRANT THAT THE SITE WILL BE UNINTERRUPTED, ERROR-FREE, OR FREE OF VIRUSES OR OTHER HARMFUL COMPONENTS.</p>

    <h2>8. Limitation of Liability</h2>
    <p>TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, VIRTUEVIGIL AND ITS OWNERS, EMPLOYEES, AGENTS, AND AFFILIATES SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES ARISING OUT OF OR RELATED TO YOUR USE OF THE SITE, INCLUDING BUT NOT LIMITED TO DAMAGES FOR LOSS OF DATA, REVENUE, OR GOODWILL, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.</p>
    <p>IN NO EVENT SHALL VIRTUEVIGIL&rsquo;S AGGREGATE LIABILITY TO YOU FOR ALL CLAIMS ARISING FROM OR RELATED TO THE SITE EXCEED FIFTY DOLLARS ($50.00).</p>

    <h2>9. Changes to These Terms</h2>
    <p>VirtueVigil reserves the right to modify these Terms at any time. When we make changes, we will update the Effective Date at the top of this page. Your continued use of the Site after any changes constitutes your acceptance of the revised Terms. We encourage you to review these Terms periodically.</p>

    <h2>10. Governing Law</h2>
    <p>These Terms are governed by and construed in accordance with the laws of the Commonwealth of Pennsylvania, without regard to its conflict of law provisions. Any disputes arising under or related to these Terms or your use of the Site shall be resolved exclusively in the state or federal courts located in Pennsylvania.</p>

    <h2>11. Contact</h2>
    <p>If you have questions about these Terms, please contact us:</p>
    <p>
      <strong>VirtueVigil</strong><br>
      Email: <a href="mailto:debra@virtuevigil.com">debra@virtuevigil.com</a><br>
      Website: <a href="https://virtuevigil.com">virtuevigil.com</a>
    </p>
  </article>

  ${simpleFooter()}
${pageScripts()}
</body>
</html>`;
}

function buildPrivacyPage() {
  const canonical = `${SITE_URL}/privacy/`;
  return `${htmlHead({
    title: 'Privacy Policy \u2014 VirtueVigil',
    description: 'VirtueVigil Privacy Policy. How we collect, use, and protect your information, including email newsletter data, Google Analytics, Amazon affiliate links, TikTok, and YouTube.',
    canonical,
  })}
<body>
  ${siteHeader('')}

  <section class="page-hero">
    <div class="container">
      <h1>Privacy <span class="text-gold">Policy</span></h1>
      <p>Effective Date: March 1, 2026</p>
    </div>
  </section>

  <article class="content-article">
    <p>VirtueVigil (&ldquo;we,&rdquo; &ldquo;us,&rdquo; or &ldquo;our&rdquo;) operates the website at <a href="https://virtuevigil.com">virtuevigil.com</a> (the &ldquo;Site&rdquo;). This Privacy Policy explains how we collect, use, and share information when you visit the Site or subscribe to our newsletter.</p>

    <h2>1. Information We Collect</h2>

    <h3>a. Information You Provide</h3>
    <ul>
      <li><strong>Email address</strong> &mdash; When you subscribe to The Vigil Report newsletter or create an account, we collect your email address. This is the primary personal information we collect directly from you.</li>
      <li><strong>Display name and password</strong> &mdash; If you register for an account, you provide a display name and password (stored securely via Supabase Auth).</li>
      <li><strong>Comments</strong> &mdash; If you submit comments on reviews, those comments are stored and may be publicly displayed on the Site.</li>
    </ul>

    <h3>b. Information Collected Automatically</h3>
    <p>When you visit the Site, we and our third-party service providers automatically collect certain technical information, including:</p>
    <ul>
      <li>IP address;</li>
      <li>Browser type and version;</li>
      <li>Pages visited and time spent on pages;</li>
      <li>Referring website or source;</li>
      <li>Device type and operating system;</li>
      <li>Cookies and similar tracking technologies (see Section 5).</li>
    </ul>

    <h2>2. How We Use Your Information</h2>
    <p>We use the information we collect to:</p>
    <ul>
      <li>Send you The Vigil Report newsletter and review update emails (if you have subscribed);</li>
      <li>Operate and improve the Site, including personalizing your experience;</li>
      <li>Enable community features such as commenting and account management;</li>
      <li>Analyze Site traffic and usage patterns to understand our audience;</li>
      <li>Display relevant advertising;</li>
      <li>Comply with legal obligations and protect the rights and safety of VirtueVigil and its users.</li>
    </ul>

    <h2>3. Email Newsletter</h2>
    <p>If you subscribe to The Vigil Report, we will send you regular emails containing new reviews, Woke Trap alerts, and site updates. You can unsubscribe at any time by clicking the &ldquo;Unsubscribe&rdquo; link in any email we send. After unsubscribing, we will stop sending marketing emails but may retain your email address in our records to honor your opt-out preference.</p>

    <h2>4. Third-Party Services</h2>
    <p>We use the following third-party services that may collect or process your information:</p>

    <h3>a. Google Analytics</h3>
    <p>We use Google Analytics (Google LLC) to analyze how visitors use the Site. Google Analytics collects data including your IP address, browser information, and pages visited. This data is used in aggregate to understand traffic patterns. Google may use this data in accordance with its own privacy policy. You can opt out of Google Analytics tracking by installing the <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">Google Analytics Opt-Out Browser Add-on</a>.</p>

    <h3>b. Amazon Associates</h3>
    <p>The Site contains affiliate links to Amazon.com through the Amazon Associates program (Amazon.com, Inc.). When you click an affiliate link, Amazon may collect information about your visit and purchase. Amazon&rsquo;s data collection is governed by <a href="https://www.amazon.com/privacy" target="_blank" rel="noopener">Amazon&rsquo;s Privacy Notice</a>.</p>

    <h3>c. Supabase</h3>
    <p>User accounts and comments are stored using Supabase (Supabase Inc.), a database and authentication platform. Supabase processes your email address, encrypted password, and any profile data you provide. Supabase&rsquo;s data handling is governed by their privacy policy.</p>

    <h3>d. TikTok</h3>
    <p>The Site links to our TikTok channel (@virtuevigil). If you visit TikTok through our links or interact with embedded TikTok content, TikTok (ByteDance Ltd.) may collect information about you in accordance with <a href="https://www.tiktok.com/legal/privacy-policy" target="_blank" rel="noopener">TikTok&rsquo;s Privacy Policy</a>.</p>

    <h3>e. YouTube</h3>
    <p>The Site links to and may embed content from our YouTube channel (Google LLC). If you interact with YouTube content, YouTube may collect information about you in accordance with <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google&rsquo;s Privacy Policy</a>. YouTube embeds may set cookies even without clicking play.</p>

    <h3>f. Advertising Networks (Future)</h3>
    <p>We may in the future display advertising from third-party ad networks. Such networks may use cookies and similar technologies to serve ads based on your prior visits to our Site and other websites. We will update this policy when advertising is enabled.</p>

    <h2>5. Cookies</h2>
    <p>VirtueVigil uses cookies and similar technologies. Cookies are small text files stored on your device. We use cookies to:</p>
    <ul>
      <li>Keep you signed in to your account;</li>
      <li>Remember your preferences;</li>
      <li>Collect analytics data (via Google Analytics);</li>
      <li>Enable affiliate tracking (via Amazon Associates).</li>
    </ul>
    <p>You can control cookies through your browser settings. Note that disabling cookies may affect some Site functionality, including account login. Most browsers allow you to refuse cookies or delete cookies that have been set.</p>

    <h2>6. Data Retention</h2>
    <p>We retain your email address and account information for as long as your account is active or as needed to provide you services. If you delete your account, we will delete or anonymize your personal information within a reasonable time, except where retention is required by law.</p>

    <h2>7. Your Rights</h2>
    <p>Depending on your location, you may have certain rights regarding your personal information, including:</p>
    <ul>
      <li><strong>Access</strong> &mdash; You may request a copy of the personal information we hold about you;</li>
      <li><strong>Correction</strong> &mdash; You may request that we correct inaccurate information;</li>
      <li><strong>Deletion</strong> &mdash; You may request that we delete your personal information;</li>
      <li><strong>Opt-out of marketing</strong> &mdash; You can unsubscribe from our email newsletter at any time;</li>
      <li><strong>Data portability</strong> &mdash; Where applicable, you may request your data in a portable format.</li>
    </ul>
    <p>To exercise any of these rights, please contact us at <a href="mailto:debra@virtuevigil.com">debra@virtuevigil.com</a>.</p>

    <h2>8. Children&rsquo;s Privacy</h2>
    <p>The Site is not directed to children under the age of 13. We do not knowingly collect personal information from children under 13. If you believe we have inadvertently collected information from a child under 13, please contact us and we will promptly delete it.</p>

    <h2>9. Security</h2>
    <p>We take reasonable technical and organizational measures to protect your information from unauthorized access, loss, or misuse. However, no method of transmission over the internet is 100% secure. You use the Site and provide information at your own risk.</p>

    <h2>10. Changes to This Policy</h2>
    <p>We may update this Privacy Policy from time to time. We will post the updated policy on this page with a revised Effective Date. Your continued use of the Site after any changes constitutes your acceptance of the revised Privacy Policy.</p>

    <h2>11. Contact Us</h2>
    <p>If you have questions about this Privacy Policy or our data practices, please contact us:</p>
    <p>
      <strong>VirtueVigil</strong><br>
      Email: <a href="mailto:debra@virtuevigil.com">debra@virtuevigil.com</a><br>
      Website: <a href="https://virtuevigil.com">virtuevigil.com</a>
    </p>
  </article>

  ${simpleFooter()}
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
  writePage('terms/index.html', buildTermsPage());
  writePage('privacy/index.html', buildPrivacyPage());

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

  writePage('lists/most-woke-movies-2023/index.html', buildListiclePage({
    slug: 'most-woke-movies-2023',
    title: '10 Most Woke Movies of 2023 (Full Ranking)',
    description: 'Which 2023 films pushed the most progressive agenda? VirtueVigil ranks the 10 most woke movies of 2023 by our scoring system.',
    canonicalPath: 'lists/most-woke-movies-2023',
    publishDate: '2023-12-31',
    htmlContent: `<article class="listicle-article">
      <p>2023 was the year Hollywood stopped pretending. The summer blockbuster season delivered a record-breaking feminist manifesto wrapped in pink packaging, a Yorgos Lanthimos fever dream that swept the Oscars, and a $200 million climate lecture wearing the costume of a superhero sequel. Progressive ideological content was not hidden in the subtext of these films. It was the text.</p>

      <p>VirtueVigil reviewed 39 films released in 2023 using our Woke Score Methodology, a dual-scoring system that measures the density and intensity of progressive ideological content across categories including gender politics, religious critique, racial messaging, sexual framing, and institutional authority. The top 10 films on that list cover a striking range of genres, from animated family fare to prestige drama to action blockbusters. What they share is a consistent, deliberate effort to embed progressive values into their storytelling.</p>

      <p>The rankings below run from #10 (lowest woke score in the top 10) to #1 (highest). Scores reflect the density of ideological content as measured by the VirtueVigil Woke Score system, not artistic merit or entertainment value. Many of these films are technically accomplished. That craftsmanship is precisely what makes them effective at delivering their message.</p>

      <hr>

      <h2>#10 - Indiana Jones and the Dial of Destiny (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 15.4 &bull; <strong>Verdict:</strong> TRADITIONAL LEAN &bull; <strong>Score Margin:</strong> +7 TRAD</p>
      <p>The fifth Indiana Jones film lands at the edge of this list with a woke score of 15.4, driven primarily by its choice to introduce a female legacy character who outpaces Indy and the film's revisionist handling of a Nazi villain reframed through Cold War politics. At 80 years old on screen, Ford's Indy is sidelined in his own franchise finale by his goddaughter Helena, a character designed to feel like a generational passing of the torch. The film's traditional score keeps it from tipping fully woke, but the deliberate diminishment of its male lead in favor of a younger female replacement follows a pattern VirtueVigil flags consistently.</p>
      <p><a href="https://virtuevigil.com/reviews/indiana-jones-dial-of-destiny-2023/">Read the full VirtueVigil review of Indiana Jones and the Dial of Destiny</a></p>

      <hr>

      <h2>#9 - Wish (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 17.45 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -6 WOKE</p>
      <p>Disney's centennial film is a textbook example of institutional authority framed as the enemy of individual self-determination. King Magnifico, the villain, is a government figure who controls what his subjects are allowed to want. The heroine, Asha, leads a grass-roots resistance against that control in a narrative that reads as a sustained critique of any authority structure that restricts personal wish fulfillment. The film's progressive messaging would land harder if the storytelling were more competent. As it stands, it earned a woke score of 17.45 while also being one of Disney's weakest recent releases commercially, grossing $218 million against a $200 million budget.</p>
      <p><a href="https://virtuevigil.com/reviews/wish-2023/">Read the full VirtueVigil review of Wish</a></p>

      <hr>

      <h2>#8 - Killers of the Flower Moon (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 19 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -4 WOKE</p>
      <p>Martin Scorsese's three-and-a-half-hour historical epic about the systematic murder of the Osage Nation by white settlers and government officials earned seven Oscar nominations and a woke score of 19. The film's progressive elements include its sustained indictment of white complicity in institutional racism and its centering of Indigenous women as moral witnesses to systemic evil. What keeps it from scoring higher is Scorsese's refusal to simplify: the traditional score of 15 reflects real engagement with moral complexity, complicity, and the weight of history rather than pure ideological scoring.</p>
      <p><a href="https://virtuevigil.com/reviews/killers-of-the-flower-moon-2023/">Read the full VirtueVigil review of Killers of the Flower Moon</a></p>

      <hr>

      <h2>#7 - The Marvels (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 22.95 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Score Margin:</strong> -14 WOKE</p>
      <p>The Marvels became the lowest-grossing film in MCU history, losing over $200 million, and its woke score of 22.95 helps explain why. An all-female superhero ensemble where every male character is either incompetent or irrelevant, the film stacks identity-first casting, girl-power messaging, and MCU franchise obligations into a product that audiences rejected decisively. The B CinemaScore and 62 percent Rotten Tomatoes critics score reflect a film that prioritized progressive representation over storytelling fundamentals. The box office result was the market's honest reply.</p>
      <p><a href="https://virtuevigil.com/reviews/the-marvels-2023/">Read the full VirtueVigil review of The Marvels</a></p>

      <hr>

      <h2>#6 - The Little Mermaid (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 24.6 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Score Margin:</strong> -12 WOKE</p>
      <p>Disney's live-action remake of the 1989 animated classic scored 24.6 primarily because the studio used the film as a diversity statement from the first marketing image forward, casting Halle Bailey as Ariel and treating any audience concern about that choice as evidence of racism. Beyond the casting controversy, the remake systematically updated the source material to remove Ariel's submissiveness toward her father and strengthen her individual autonomy. The original's themes of feminine longing for a male romantic partner were softened while Ariel's self-determination was amplified. It is a competent remake. It is also a deliberate ideological revision of the source material.</p>
      <p><a href="https://virtuevigil.com/reviews/the-little-mermaid-2023/">Read the full VirtueVigil review of The Little Mermaid</a></p>

      <hr>

      <h2>#5 - Oppenheimer (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 30 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -4 WOKE</p>
      <p>Christopher Nolan's $952 million blockbuster surprised many with a woke score of 30. The film's progressive content is concentrated in its treatment of the McCarthy-era security hearing, which frames anti-communist institutional authority as paranoid, corrupt, and vindictive, and in its sympathetic handling of Oppenheimer's association with Communist Party members and causes. The film's traditional score of 26 reflects Nolan's genuine engagement with moral weight, sacrifice, and the burden of creation. But Oppenheimer is unmistakably a film made by someone who views the national security state with suspicion, and that perspective shapes every frame of the film's final act.</p>
      <p><a href="https://virtuevigil.com/reviews/oppenheimer-2023/">Read the full VirtueVigil review of Oppenheimer</a></p>

      <hr>

      <h2>#4 - Aquaman and the Lost Kingdom (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 31.2 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Score Margin:</strong> -12 WOKE</p>
      <p>Aquaman and the Lost Kingdom scored 31.2 by embedding a sustained climate change narrative into an undersea action franchise. The villain's plan involves releasing an ancient pollutant that causes global warming, the heroes must prevent environmental catastrophe, and the film lectures about ecological destruction with a frequency and urgency that overrides the superhero plot. The original Aquaman made $1.15 billion by being an unself-conscious adventure film. The sequel made $297 million by turning it into a $215 million climate lecture. The DCEU closed with the market delivering its verdict on ideological action cinema.</p>
      <p><a href="https://virtuevigil.com/reviews/aquaman-and-the-lost-kingdom-2023/">Read the full VirtueVigil review of Aquaman and the Lost Kingdom</a></p>

      <hr>

      <h2>#3 - Saltburn (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 35 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Score Margin:</strong> -32 WOKE</p>
      <p>Emerald Fennell followed Promising Young Woman with a film about class warfare where the working-class interloper systematically destroys and literally consumes an aristocratic family. Saltburn scored 35 through its depiction of class resentment as the moral engine of its plot, its graphic sexual content deployed as weapons of social transgression, and its deliberate elevation of a manipulative, murderous protagonist whose crimes against the wealthy ruling class are framed as darkly triumphant. The film's twist ending, in which Oliver dances nude through the estate he has claimed by eliminating its previous owners, is a victory lap for the ideology the entire film has been building.</p>
      <p><a href="https://virtuevigil.com/reviews/saltburn-2023/">Read the full VirtueVigil review of Saltburn</a></p>

      <hr>

      <h2>#2 - Poor Things (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 47 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Score Margin:</strong> -38 WOKE</p>
      <p>Yorgos Lanthimos won the Palme d'Or at Cannes and four Academy Awards, including Best Picture, for a film about a woman brought back to life with a baby's brain who discovers sexual liberation, rejects all social constraint, and becomes a socialist doctor. Poor Things scored 47 on the woke scale, the second highest of any 2023 film VirtueVigil reviewed. Its progressive content is not incidental. The film is a sustained argument that female liberation requires rejecting every structure, including family, marriage, class, religion, and conventional morality. Emma Stone's Oscar-winning performance is extraordinary. The ideology behind it is equally consistent and direct.</p>
      <p><a href="https://virtuevigil.com/reviews/poor-things-2023/">Read the full VirtueVigil review of Poor Things</a></p>

      <hr>

      <h2>#1 - Barbie (2023)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 48 &bull; <strong>Verdict:</strong> STRONGLY WOKE &bull; <strong>Score Margin:</strong> -32 WOKE</p>
      <p>Barbie grossed $1.44 billion worldwide, making it the highest-grossing film of 2023 and the highest-grossing film ever directed by a woman, and it scored 48 on the VirtueVigil Woke Score, the highest of any 2023 film in our database. Greta Gerwig's film is a two-hour feminist argument: the patriarchy is the villain, Ken's toxic masculinity arc is played for comedy before being corrected, and Barbie's liberation requires her to reject plastic perfection for the messy autonomy of womanhood in the real world. Nobody who bought a pink ticket could claim they were not warned. The ideology was the marketing. The marketing worked.</p>
      <p><a href="https://virtuevigil.com/reviews/barbie-2023/">Read the full VirtueVigil review of Barbie</a></p>

      <hr>

      <h2>Methodology Note</h2>
      <p>All scores are generated using the VirtueVigil Woke Score system, which measures the density and intensity of progressive ideological content across multiple categories including gender politics, religious critique, racial messaging, sexual content framing, and institutional critique. The system does not measure quality, entertainment value, or artistic merit. A high score means a film contains a high volume of identifiable progressive messaging relative to its runtime. For full details on how we score, visit our <a href="/methodology.html">Methodology</a> page.</p>

      <p>2023 was not the year progressive Hollywood peaked. That honor likely belongs to 2024, which added Anora, The Substance, and Heretic to the canon. But 2023 was the year the ideology went fully mainstream, reaching audiences of hundreds of millions through franchise blockbusters and a billion-dollar toy movie. If you want to understand what Hollywood was selling in 2023, start with Barbie and work your way down this list. Every film reviewed here is available with full trope-by-trope analysis, creative team profiles, and parental guidance at VirtueVigil. Browse the complete database at <a href="https://virtuevigil.com/reviews/">virtuevigil.com/reviews/</a> or compare scores across years on our <a href="https://virtuevigil.com/lists/">lists page</a>.</p>
    </article>`
  }));

  writePage('lists/most-woke-movies-2021/index.html', buildListiclePage({
    slug: 'most-woke-movies-2021',
    title: '10 Most Woke Movies of 2021 (Ranked by VirtueVigil Score)',
    description: 'The 10 most woke movies of 2021, ranked by VirtueVigil\'s VVWS scoring system. Data-driven. No opinions, just numbers.',
    canonicalPath: 'lists/most-woke-movies-2021',
    publishDate: '2026-03-23',
    htmlContent: `<article class="listicle-article">
      <p>2021 was Hollywood's comeback year after COVID shuttered theaters for most of 2020. The studios had backlogged releases, streaming deals to prove, and something to say. For a lot of them, that something was ideological. The biggest franchises on earth used their 2021 releases to push diversity casting overhauls, feminist revenge arcs, and identity allegories so thick you could cut them with a lightsaber.</p>

      <p>VirtueVigil scored every major 2021 film using the VVWS, our Woke-Watch Scoring System that weighs trope severity, authenticity, and centrality to produce a single objective score. Below are the 10 films from 2021 with the highest woke scores. No outrage. No editorializing. Just the numbers.</p>

      <hr>

      <h2>#10 - Mortal Kombat (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 4.6 &bull; <strong>Verdict:</strong> TRADITIONAL LEAN &bull; <strong>Score Margin:</strong> +4 TRAD</p>
      <p>Mortal Kombat rounds out the top 10 with the lowest woke score on this list at 4.6. The main woke element is Cole Young, a new biracial protagonist invented for the film who does not appear in the games, serving as audience surrogate while displacing white roster members. A diverse ensemble and an anti-colonial villain framing add minor weight. The film otherwise has no real ideological agenda and earns its traditional credit through warrior honor codes, loyalty, and vengeance as duty.</p>
      <p><a href="/reviews/mortal-kombat-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Mortal Kombat</a></p>

      <hr>

      <h2>#9 - Space Jam: A New Legacy (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 5.2 &bull; <strong>Verdict:</strong> TRADITIONAL LEAN &bull; <strong>Score Margin:</strong> +4 TRAD</p>
      <p>Space Jam 2 racked up woke points primarily through the deliberate feminist redesign of Lola Bunny, pulling her away from the 1996 film's more sexualized look on the explicit direction of producer Ryan Coogler. A diverse ensemble framed as a team-strength narrative and a Silicon Valley-coded algorithm villain add to a wokeScore of 5.2. The father-son emotional arc at the film's core earns its traditional credit and keeps this well out of WOKE territory.</p>
      <p><a href="/reviews/space-jam-a-new-legacy-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Space Jam: A New Legacy</a></p>

      <hr>

      <h2>#8 - Shang-Chi and the Legend of the Ten Rings (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 5.46 &bull; <strong>Verdict:</strong> TRADITIONAL LEAN &bull; <strong>Score Margin:</strong> +9 TRAD</p>
      <p>Marvel's first Asian-led film surprised critics expecting a diversity lecture and delivered a traditionally structured family drama instead. Its woke elements are real but modest: deliberate stereotype replacement, a feminist subplot for Xialing that positions her as an equal heir to power her father denied her, and diversity-conscious ensemble casting. With a woke score of 5.46 against a trad score of 14.19, Shang-Chi is the most traditional MCU film of 2021 by a distance.</p>
      <p><a href="/reviews/shang-chi-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Shang-Chi and the Legend of the Ten Rings</a></p>

      <hr>

      <h2>#7 - Dune: Part One (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 7.1 &bull; <strong>Verdict:</strong> TRADITIONAL &bull; <strong>Score Margin:</strong> +13 TRAD</p>
      <p>Denis Villeneuve's Dune earns its spot via the Bene Gesserit, an all-female mystical power structure that has secretly controlled galactic civilization for millennia through genetic manipulation and religious seeding. Chani serves as a female skeptic positioned as the voice of reason against organized religious faith and messianic prophecy. Casting diversity also extends beyond Herbert's source material. Still, the film's traditional score of 20.02 dwarfs the woke side, making this the most traditionally coded entry on this list.</p>
      <p><a href="/reviews/dune-part-one-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Dune: Part One</a></p>

      <hr>

      <h2>#6 - Encanto (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 8.68 &bull; <strong>Verdict:</strong> TRADITIONAL &bull; <strong>Score Margin:</strong> +10 TRAD</p>
      <p>Encanto lands on this list despite scoring TRADITIONAL overall, because its progressive elements are real and deliberate. Luisa's body-positive muscular design, the anti-perfectionism message that worth is not tied to productivity, and Mirabel directly challenging parental authority all register on the woke scale at 8.68. These elements exist alongside much stronger traditional content about family, intergenerational bonds, and sacrifice, which is why the film ends up TRADITIONAL despite its progressive undercurrents.</p>
      <p><a href="/reviews/encanto-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Encanto</a></p>

      <hr>

      <h2>#5 - No Time to Die (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 11.98 &bull; <strong>Verdict:</strong> MIXED &bull; <strong>Score Margin:</strong> 0 NEUTRAL</p>
      <p>No Time to Die planted a Black female agent named Nomi in the 007 designation during Bond's retirement, a deliberate and publicized diversity signal by Eon Productions. Craig's Bond is also given a domesticated emotional arc, revealed to have a daughter, and shown cooking and gardening while driven by romance rather than patriotism. The film's woke and trad scores land nearly equal at 11.98 and 12.25, scoring NEUTRAL, with Bond's heroic self-sacrifice in the finale holding the traditional side.</p>
      <p><a href="/reviews/no-time-to-die-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of No Time to Die</a></p>

      <hr>

      <h2>#4 - Cruella (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 14.0 &bull; <strong>Verdict:</strong> MIXED &bull; <strong>Score Margin:</strong> -2 WOKE</p>
      <p>Disney's Cruella reframes one of animation's most iconic villains as a misunderstood girlboss whose worst crimes are guerrilla fashion stunts. The film's core argument is that Cruella de Vil is a brilliant woman fighting institutional barriers to express her authentic self, with rebellion against authority framed as inherent virtue. Villain rehabilitation as progressive ideology drives a woke score of 14.0, though the film's visual craft and Emma Stone's performance keep the trad score competitive at 12.0.</p>
      <p><a href="/reviews/cruella-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Cruella</a></p>

      <hr>

      <h2>#3 - The Matrix Resurrections (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 15.05 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -6 WOKE</p>
      <p>Lana Wachowski built the fourth Matrix film explicitly around trans liberation allegory, confirmed in her own words. Neo and Trinity are trapped in imposed identities, medicated into compliance by a therapist who feeds Neo blue pills to suppress his authentic self. Warner Bros. is thinly veiled as the corporate villain forcing the sequel into existence. The trans allegory earns the film's heaviest woke trope weighting, pushing the score to 15.05.</p>
      <p><a href="/reviews/the-matrix-resurrections-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The Matrix Resurrections</a></p>

      <hr>

      <h2>#2 - Black Widow (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 16.95 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -5 WOKE</p>
      <p>Black Widow builds its entire plot around the Red Room program as a #MeToo allegory: a male villain, Dreykov, controls and weaponizes women through chemical mind control. Forced sterilization of the Red Room's operatives is treated as a central horror. The patriarchal villain archetype drives a woke score of 16.95, though Florence Pugh's Yelena and the genuine emotional core of the fake-family dynamic pull the trad score to 12.13 and keep this from reaching the WOKE threshold.</p>
      <p><a href="/reviews/black-widow-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Black Widow</a></p>

      <hr>

      <h2>#1 - Eternals (2021)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 19.74 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Score Margin:</strong> -14 WOKE</p>
      <p>Eternals tops the 2021 list by a wide margin, earning the first outright WOKE verdict for an MCU film. Director Chloe Zhao assembled a maximum-diversity ensemble of ten Eternals, swapping the source material's original race and gender assignments across multiple characters. The film also introduced Phastos as the MCU's first openly gay superhero, complete with a same-sex kiss, while framing the Celestial's planetary destruction through a climate-coded lens. At a woke score of 19.74 against a trad score of 5.95, no 2021 film came close to the top spot.</p>
      <p><a href="/reviews/eternals-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Eternals</a></p>

      <hr>

      <h2>Methodology Note</h2>
      <p>All scores are generated using the VirtueVigil Woke Score system, which measures the density and intensity of progressive ideological content across multiple categories including gender politics, religious critique, racial messaging, sexual content framing, and institutional critique. The system does not measure quality, entertainment value, or artistic merit. A high score means a film contains a high volume of identifiable progressive messaging relative to its runtime. For full details on how we score, visit our <a href="/methodology.html">Methodology</a> page.</p>

      <p>2021 proved that even in a recovery year, Hollywood could not resist using its biggest franchises as ideological delivery vehicles. Eternals set the MCU record for both critical failure and woke scoring in the same release. The Matrix came back as a trans liberation allegory. Bond got his 007 designation handed to a Black woman. The data does not lie and it does not editorialize. If you want to know what else scored in 2021 and beyond, browse the full VirtueVigil review database at <a href="/reviews/">virtuevigil.com/reviews/</a> and see every film scored, ranked, and broken down by the numbers.</p>
    </article>`
  }));

  writePage('lists/most-woke-movies-2019/index.html', buildListiclePage({
    slug: 'most-woke-movies-2019',
    title: '10 Most Woke Movies of 2019 (Ranked by VirtueVigil Score)',
    description: 'VirtueVigil ranks the most woke movies of 2019 using our scoring system. From hidden agendas to overt messaging, here is the full breakdown.',
    canonicalPath: 'lists/most-woke-movies-2019',
    publishDate: '2026-03-23',
    htmlContent: `<article class="listicle-article">
      <p>2019 was a landmark year for ideologically charged cinema. From Disney blockbusters to prestige dramas, Hollywood loaded its releases with progressive messaging. VirtueVigil scored each film using our Woke Warning System (VVWS) and here are the 10 that ranked highest on the woke scale.</p>

      <p>The rankings below run from #10 (lowest woke score in the top 10) to #1 (highest). Scores reflect the density and intensity of progressive ideological content as measured by the VirtueVigil Woke Score system. These are not quality ratings. A high woke score does not mean a bad film. It means a film with a high volume of identifiable progressive messaging embedded in its storytelling.</p>

      <hr>

      <h2>#10 - Once Upon a Time in Hollywood (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 6.8 &bull; <strong>Verdict:</strong> TRADITIONAL &bull; <strong>Score Margin:</strong> +12 TRAD</p>
      <p>Tarantino's love letter to Old Hollywood lands at #10 on this list with the lowest woke score in the top 10 at 6.8. It earns its place by being one of the few major 2019 releases with any measurable progressive content at all. The film's sympathy for working-class male friendship, its contempt for Manson-era counterculture chaos, and its revisionist defense of the innocent put it solidly in traditional territory overall. Leonardo DiCaprio and Brad Pitt as two men being left behind by a changing Hollywood is a story about craft, loyalty, and the wish that competent men could always protect the innocent.</p>
      <p><a href="/reviews/once-upon-a-time-in-hollywood-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Once Upon a Time in Hollywood</a></p>

      <hr>

      <h2>#9 - Spider-Man: Far From Home (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 7.4 &bull; <strong>Verdict:</strong> TRADITIONAL &bull; <strong>Score Margin:</strong> +11 TRAD</p>
      <p>Far From Home is one of the cleaner MCU entries from an ideological standpoint and its woke score of 7.4 reflects that. Peter Parker's coming-of-age arc is earnest and traditional. He has a crush, a best friend, and a desperate need for a father figure to replace Tony Stark. The villain, Mysterio, exploits that grief with a clarity that makes the film's moral architecture unusually clean for modern Marvel. Mild woke markers in the diverse supporting cast register on the scale without derailing the main story. A confident, warm superhero film about grief and growing up.</p>
      <p><a href="/reviews/spider-man-far-from-home-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Spider-Man: Far From Home</a></p>

      <hr>

      <h2>#8 - Aladdin (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 8.18 &bull; <strong>Verdict:</strong> TRADITIONAL LEAN &bull; <strong>Score Margin:</strong> +4 TRAD</p>
      <p>Disney's live-action remake of Aladdin preserves the original's warm heart and traditional love story while explicitly updating Jasmine's arc into feminist leadership territory. The woke score of 8.18 comes primarily from the new song "Speechless," written to give Jasmine an overt empowerment anthem, and from the film's decision to give her a political ambition to become Sultan rather than simply be free to choose who she marries. The core story still rewards honesty and punishes deception. Will Smith's Genie is the film's biggest surprise, delivering a high-energy performance that is entirely his own rather than a Williams imitation.</p>
      <p><a href="/reviews/aladdin-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Aladdin</a></p>

      <hr>

      <h2>#7 - Avengers: Endgame (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 10.54 &bull; <strong>Verdict:</strong> TRADITIONAL LEAN &bull; <strong>Score Margin:</strong> +3 TRAD</p>
      <p>The highest-grossing film in history earns a woke score of 10.54 from the "all-female Avengers" moment that paused the climax for a studio mandate, from Steve Rogers handing the shield to Sam Wilson as the MCU's deliberate Black Captain America setup, and from minor progressive ensemble moments throughout. That said, the film's emotional engine is entirely traditional: sacrifice, duty, love, and the courage to give everything for the people you protect. Tony Stark's death is the most traditionally coded moment in MCU history. The film sits at +3 TRAD because the traditional content dominates. One foot in old-school Marvel storytelling, one foot in the progressive identity politics that would eventually sink the franchise.</p>
      <p><a href="/reviews/avengers-endgame-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Avengers: Endgame</a></p>

      <hr>

      <h2>#6 - Joker (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 13.05 &bull; <strong>Verdict:</strong> MIXED &bull; <strong>Score Margin:</strong> +1 TRAD</p>
      <p>Joker made a billion dollars, triggered FBI security warnings, and managed to infuriate both sides of the culture war simultaneously. The class warfare framing and the portrayal of Thomas Wayne as a contemptuous plutocrat push the woke score to 13.05. But the film's anti-institutional nihilism, its refusal to offer progressive solutions to the social failures it depicts, and Todd Phillips' explicit contempt for woke culture push back in the other direction. Joaquin Phoenix's performance is so dominant that it transcends the debate. The score margin of +1 TRAD is razor-thin and accurately reflects a film that neither side gets to claim.</p>
      <p><a href="/reviews/joker-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Joker</a></p>

      <hr>

      <h2>#5 - Us (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 13.14 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -4 WOKE</p>
      <p>Jordan Peele's follow-up to Get Out earns a woke score of 13.14 on the strength of its central metaphor: the Tethered as a progressive critique of American inequality and systemic exploitation. The underground people represent the Americans society has forgotten, discarded, and left to rot while their surface counterparts live comfortable lives built on ignoring them. The execution is sophisticated enough to warrant engagement. Lupita Nyong'o delivers an extraordinary dual performance that is the only reason the film's ambitious allegory holds together as long as it does. The ideology is present at every level of the narrative architecture, even where the plot logic strains.</p>
      <p><a href="/reviews/us-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Us</a></p>

      <hr>

      <h2>#4 - Knives Out (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 13.44 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -5 WOKE</p>
      <p>Rian Johnson built one of the year's best films around a bluntly progressive immigration argument. The moral architecture of Knives Out is unambiguous: every virtue belongs to Marta Cabrera, the immigrant nurse protagonist, and every vice belongs to the wealthy native-born Thrombey family. The knife clearly points one direction. Johnson is too skilled a filmmaker to let the thesis overwhelm the entertainment, and the result is a film that conservatives can genuinely enjoy despite its openly progressive politics. Daniel Craig as Benoit Blanc delivers the best Craig performance not in a Bond film. Crafted well enough to entertain the people it disagrees with.</p>
      <p><a href="/reviews/knives-out-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Knives Out</a></p>

      <hr>

      <h2>#3 - Toy Story 4 (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 17.2 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -9 WOKE</p>
      <p>The most controversial entry on this list. Toy Story 4 is technically dazzling and emotionally manipulative. Its woke score of 17.2 is not about gender politics or identity messaging. It is about philosophy. The film quietly argues that Woody was wrong about everything the first three movies said he was right about. Loyalty to a child, duty, purpose through belonging, these are reframed as attachments Woody needed to transcend. Self-discovery over duty. Personal authenticity over commitment. The franchise that built its moral universe on purpose-through-service dismantles that universe in the final fifteen minutes and calls it growth. That ideological shift from the franchise's roots earns its score.</p>
      <p><a href="/reviews/toy-story-4-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Toy Story 4</a></p>

      <hr>

      <h2>#2 - Frozen II (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 19.0 &bull; <strong>Verdict:</strong> WOKE LEAN &bull; <strong>Score Margin:</strong> -5 WOKE</p>
      <p>Frozen II takes bigger ideological swings than the original and connects with roughly half of them. Where the 2013 film was a personal story about sisters and self-acceptance, the sequel expands into colonialism, historical reparations, and the moral obligation to dismantle the systems your ancestors built on exploitation. Elsa discovers her grandfather built a dam to weaken the Northuldra, an indigenous people, and the film's resolution requires tearing down that dam regardless of consequences to Arendelle. The message is not subtle: inherited privilege must be actively dismantled, even at personal cost. A woke score of 19.0 reflects a film that chose to lecture where its predecessor chose to tell a story.</p>
      <p><a href="/reviews/frozen-ii-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Frozen II</a></p>

      <hr>

      <h2>#1 - Captain Marvel (2019)</h2>
      <p><strong>VirtueVigil Woke Score:</strong> 19.44 &bull; <strong>Verdict:</strong> WOKE &bull; <strong>Score Margin:</strong> -16 WOKE</p>
      <p>Captain Marvel tops the 2019 list as the MCU's most deliberately ideological film. Released on International Women's Day, directed with a female co-director by studio mandate, scored by the first female MCU composer, and built around a feminist empowerment narrative that makes its thesis explicit rather than implicit. This is not a film that happens to have a female protagonist. It is a film about feminism with superhero action sequences attached. The male authority figure is a manipulative villain. The military is an imperial oppressor. The refugee allegory is unambiguous. Carol Danvers' arc culminates not in earned heroism but in the removal of external limits on her power, which the film frames as women finally being allowed to fight without restraint. Minimal traditional content. The MCU's most ideologically committed entry in its first decade.</p>
      <p><a href="/reviews/captain-marvel-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Captain Marvel</a></p>

      <hr>

      <h2>Methodology Note</h2>
      <p>All scores are generated using the VirtueVigil Woke Score system, which measures the density and intensity of progressive ideological content across multiple categories including gender politics, religious critique, racial messaging, sexual content framing, and institutional critique. The system does not measure quality, entertainment value, or artistic merit. A high score means a film contains a high volume of identifiable progressive messaging relative to its runtime. For full details on how we score, visit our <a href="/methodology.html">Methodology</a> page.</p>

      <p>2019 was the last year before COVID scrambled production schedules and accelerated the streaming wars. The films on this list represent Hollywood at full commercial capacity, using its biggest franchises to push progressive ideas to the widest possible audiences. Want to see which 2019 films earned a TRADITIONAL or STRONGLY TRADITIONAL rating? Browse the full 2019 catalog at <a href="/reviews/">VirtueVigil.com/reviews/</a> and see every film scored, ranked, and broken down by the numbers. For comparison, see our full annual rankings series: <a href="/lists/most-woke-movies-2021/">2021</a>, <a href="/lists/most-woke-movies-2023/">2023</a>, and <a href="/lists/most-woke-movies-2024/">2024</a>.</p>
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

  writePage('lists/mcu-movies-ranked-woke-score/index.html', buildListiclePage({
    slug: 'mcu-movies-ranked-woke-score',
    title: 'Every MCU Movie Ranked by Woke Score',
    description: 'All 23 MCU films scored and ranked by VirtueVigil from most woke to most traditional. Real data. No guessing. See which Marvel movies push an agenda.',
    canonicalPath: 'lists/mcu-movies-ranked-woke-score',
    publishDate: '2026-03-15',
    htmlContent: `<article class="listicle-article">

<p>Marvel built the most successful film franchise in history by expanding the superhero universe in every direction at once. Over 15+ years and 30+ films, the MCU has been family-friendly popcorn entertainment, prestige drama, political thriller, cosmic comedy, and identity-forward statement picture. What it has never been is ideologically neutral.</p>

<p>VirtueVigil scored every MCU film using our Woke-Watch Scoring System, which measures the density of progressive ideological content and traditional values content on dual scales. The Score Margin tells you which direction each film leans and by how much. These scores are data, not opinions. The same methodology that applies to art house films and horror movies applies here. No studio gets a pass.</p>

<p>Below is every MCU film in our database, ranked from most woke to most traditional. The results may surprise you. Some films you assumed were safe are not. Some you wrote off delivered genuine traditional content. Read the scores. Follow the links to the full reviews. Then decide what to watch.</p>

<p>Rankings run from #1 (highest woke score) to #23 (most traditionally weighted). All 23 films have been reviewed in full on VirtueVigil with complete trope audits, creative team profiles, and parental guidance assessments.</p>

<hr>

<h2>#1 - <a href="/reviews/the-marvels-2023/">The Marvels (2023)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke">WOKE</span>
  <span class="score-detail">Woke Score: 22.95 &bull; Trad Score: 8.87 &bull; Margin: -14 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action/Comedy &bull; <strong>Platform:</strong> Theatrical</p>
<p>The highest woke score in the MCU and the franchise's biggest box office disaster, losing over $200 million. The Marvels deploys an all-female hero team where male characters are consistently sidelined or comic relief, and director Nia DaCosta was chosen in part as a deliberate ideological statement by Disney. Brie Larson's off-screen activism bleeds into the film's framing. The traditional score of 8.87 reflects genuine found-family sisterhood and heroic self-sacrifice, but they cannot overcome the dominant progressive framing. The audience for this movie was not found, and the numbers confirmed it.</p>
<p><a href="/reviews/the-marvels-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The Marvels</a></p>

<hr>

<h2>#2 - <a href="/reviews/eternals-2021/">Eternals (2021)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke">WOKE</span>
  <span class="score-detail">Woke Score: 19.74 &bull; Trad Score: 5.95 &bull; Margin: -14 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Sci-Fi/Superhero &bull; <strong>Platform:</strong> Theatrical</p>
<p>Chloe Zhao's MCU entry is the first to feature an openly gay superhero (Phastos), a maximum-diversity ensemble cast assembled by explicit demographic checklist, and source material race and gender swaps across multiple characters. The result scored a 47% on Rotten Tomatoes and a 5.9 on IMDB, the lowest in franchise history. The traditional score scrapes 5.95 from Gilgamesh's selfless devotion and Ikaris's tragic obedience. Everything else is a progressive showcase that failed to engage the audience it targeted.</p>
<p><a href="/reviews/eternals-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Eternals</a></p>

<hr>

<h2>#3 - <a href="/reviews/black-panther-2018/">Black Panther (2018)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge mixed">MIXED</span>
  <span class="score-detail">Woke Score: 18.82 &bull; Trad Score: 20.03 &bull; Margin: +1 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Adventure/Sci-Fi &bull; <strong>Platform:</strong> Theatrical</p>
<p>The most culturally significant MCU film tells a surprisingly traditional story wrapped in progressive packaging. T'Challa assumes the throne after his father's death, defeats a usurper whose isolationist revolutionary ideology is presented as understandable and wrong, and chooses his people's welfare over personal revenge. The woke score of 18.82 reflects the film's racial politics and anti-colonial messaging. The trad score of 20.03 reflects duty, sacrifice, and kingship as genuine burden. The margin of +1 TRAD makes it the most balanced film in the franchise. VirtueVigil scored it MIXED because that is exactly what it is.</p>
<p><a href="/reviews/black-panther-2018/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Black Panther</a></p>

<hr>

<h2>#4 - <a href="/reviews/black-panther-wakanda-forever-2022/">Black Panther: Wakanda Forever (2022)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke-lean">WOKE LEAN</span>
  <span class="score-detail">Woke Score: 18.42 &bull; Trad Score: 12.67 &bull; Margin: -6 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action/Drama &bull; <strong>Platform:</strong> Theatrical</p>
<p>Wakanda Forever is a film at war with itself. Angela Bassett delivers a towering performance as a grieving queen, and the film's treatment of grief and loss earns genuine traditional points. But a systematic all-female power structure, anti-colonial and anti-Western framing, and a Namor reimagined as a Mesoamerican Indigenous figure rather than his comic source push the woke score above 18. At 161 minutes, the film has time to be both genuinely moving and ideologically exhausting. The margin of -6 WOKE reflects a movie that got the emotional beats right and the politics wrong.</p>
<p><a href="/reviews/black-panther-wakanda-forever-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Black Panther: Wakanda Forever</a></p>

<hr>

<h2>#5 - <a href="/reviews/black-widow-2021/">Black Widow (2021)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke-lean">WOKE LEAN</span>
  <span class="score-detail">Woke Score: 16.95 &bull; Trad Score: 12.13 &bull; Margin: -5 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Adventure/Thriller &bull; <strong>Platform:</strong> Theatrical/Disney+</p>
<p>Natasha Romanoff's belated solo film uses the Red Room program as a direct #MeToo allegory, centering reproductive violence and forced sterilization as its central horror. The gender swap of Taskmaster from male to female removes the comic source villain's entire character in favor of a mute female plot device. Florence Pugh's Yelena Belova rescues the film's entertainment value while the traditional score of 12.13 reflects genuine themes of family bonds, self-sacrifice, and redemption. The gap between the two scores tells you exactly what kind of film this is: the feminist framework is the engine, the action is the packaging.</p>
<p><a href="/reviews/black-widow-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Black Widow</a></p>

<hr>

<h2>#6 - <a href="/reviews/thor-love-and-thunder-2022/">Thor: Love and Thunder (2022)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke-lean">WOKE LEAN</span>
  <span class="score-detail">Woke Score: 16.44 &bull; Trad Score: 12.26 &bull; Margin: -4 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Adventure/Comedy &bull; <strong>Platform:</strong> Theatrical</p>
<p>Taika Waititi's second Thor film contains the raw materials for a genuinely powerful story about grief and the failure of the gods, but buries them under relentless tonal chaos. LGBTQ+ representation for both Valkyrie and Korg is woven into the narrative rather than incidental, and the male hero is consistently emasculated for comedic effect. Christian Bale's Gorr the God Butcher is the film's only genuine emotional success, and his arc about faith, grief, and redemption earns traditional points that the rest of the film spends elsewhere. The fatherhood and adoption theme at the film's close partially redeems an otherwise incoherent entry.</p>
<p><a href="/reviews/thor-love-and-thunder-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Thor: Love and Thunder</a></p>

<hr>

<h2>#7 - <a href="/reviews/captain-america-brave-new-world-2025/">Captain America: Brave New World (2025)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke-lean">WOKE LEAN</span>
  <span class="score-detail">Woke Score: 14.58 &bull; Trad Score: 10.08 &bull; Margin: -4 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Sci-Fi/Thriller &bull; <strong>Platform:</strong> Theatrical</p>
<p>The fourth entry in the Captain America franchise is a deeply confused political thriller that cannot decide what it wants to say about race in America. The legacy replacement framework, in which Sam Wilson takes over Steve Rogers's mantle as a vehicle for race-based messaging, carries the highest woke weight. The institutional evil framing and girl boss element add to the score. The traditional side captures genuine self-sacrifice and father-daughter reconciliation. At $415 million worldwide on a $180 million budget, it did not collapse like The Marvels, but the ideological identity crisis is visible in every scene.</p>
<p><a href="/reviews/captain-america-brave-new-world-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Captain America: Brave New World</a></p>

<hr>

<h2>#8 - <a href="/reviews/ant-man-and-the-wasp-quantumania-2023/">Ant-Man and the Wasp: Quantumania (2023)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke-lean">WOKE LEAN</span>
  <span class="score-detail">Woke Score: 14.57 &bull; Trad Score: 10.67 &bull; Margin: -4 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action/Adventure &bull; <strong>Platform:</strong> Theatrical</p>
<p>The third Ant-Man film had one job: introduce Kang the Conqueror as the next Thanos-level threat. It mostly failed at everything except the Kang part, and then Jonathan Majors' real-world conviction destroyed even that. Cassie Lang's transformation into an activist genius girl-boss, explicit pro-socialism dialogue in the Quantum Realm, and the consistent diminishment of the male protagonist drive the woke score above 14. The father-daughter love and clear good-versus-evil framework keep the traditional score alive. The film collapsed the Ant-Man franchise rather than launching the multiverse saga.</p>
<p><a href="/reviews/ant-man-and-the-wasp-quantumania-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Ant-Man and the Wasp: Quantumania</a></p>

<hr>

<h2>#9 - <a href="/reviews/doctor-strange-multiverse-of-madness-2022/">Doctor Strange in the Multiverse of Madness (2022)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke-lean">WOKE LEAN</span>
  <span class="score-detail">Woke Score: 13.6 &bull; Trad Score: 10.22 &bull; Margin: -3 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Adventure/Horror &bull; <strong>Platform:</strong> Theatrical</p>
<p>Sam Raimi brought genuine horror filmmaking to the MCU and Elizabeth Olsen delivered a villain performance for the ages, making this the franchise's most interesting mess. LGBTQ+ representation through America Chavez, gender-swapped legacy heroes in the Illuminati, and an occult power system treated as entirely legitimate push the woke score past 13. The traditional score captures Strange's trust-based heroism, Wanda's redemptive sacrifice, and the film's consistent message that dark power has consequences. The gap between what the film could have been and what it is reflects the conflict between Raimi's instincts and Marvel's mandates.</p>
<p><a href="/reviews/doctor-strange-multiverse-of-madness-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Doctor Strange in the Multiverse of Madness</a></p>

<hr>

<h2>#10 - <a href="/reviews/spider-man-across-the-spider-verse-2023/">Spider-Man: Across the Spider-Verse (2023)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge mixed">MIXED</span>
  <span class="score-detail">Woke Score: 12.59 &bull; Trad Score: 10.64 &bull; Margin: -2 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Animated/Superhero &bull; <strong>Platform:</strong> Theatrical</p>
<p>The most technically ambitious animated film ever made also carries a quietly progressive worldview: anti-institutional framing where authority is the enemy, anarchist hero figures as the coolest people in the room, and progressive identity symbolism throughout. The traditional score pulls nearly even with a loving and present Black father, a nuclear family as the emotional foundation, and a mother's faith and prayer as genuine moral anchors. The result is a MIXED verdict on a film that is genuinely great as animation and genuinely conflicted as ideology. The margin of -2 WOKE is the closest in the MCU.</p>
<p><a href="/reviews/spider-man-across-the-spider-verse-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Spider-Man: Across the Spider-Verse</a></p>

<hr>

<h2>#11 - <a href="/reviews/thor-ragnarok-2017/">Thor: Ragnarok (2017)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
  <span class="score-detail">Woke Score: 11.9 &bull; Trad Score: 18.76 &bull; Margin: +7 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action Comedy &bull; <strong>Platform:</strong> Theatrical</p>
<p>Taika Waititi's first Thor film is the MCU doing comedy right, and under the neon colors and relentless wit lies a story about duty, sacrifice, and leading your people when everything you thought mattered is gone. The deconstruction of the masculine hero and the imperial legacy critique add woke points, but Heimdall's quiet heroism, Loki's reluctant loyalty, and Thor's earned growth through suffering and loss drive the traditional score to 18.76. "Asgard is not a place, it's a people" is one of the most traditionally conservative lines in franchise history. One of the rare MCU films where the humor serves the story instead of replacing it.</p>
<p><a href="/reviews/thor-ragnarok-2017/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Thor: Ragnarok</a></p>

<hr>

<h2>#12 - <a href="/reviews/deadpool-wolverine-2024/">Deadpool &amp; Wolverine (2024)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge woke-lean">WOKE LEAN</span>
  <span class="score-detail">Woke Score: 11.0 &bull; Trad Score: 8.0 &bull; Margin: -3 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action &bull; <strong>Platform:</strong> Theatrical/Disney+</p>
<p>Ryan Reynolds and Hugh Jackman have genuine chemistry, and the nostalgic R-rated Marvel entry delivered $1.3 billion at the box office. The film advertises itself as an audacious, frequently profane buddy movie and delivers exactly that. The woke score of 11 reflects progressive elements that sit below the surface of the comedy without dominating it, while the trad score of 8 reflects the friendship and sacrifice themes that give the film its emotional core. Neither score is high because neither worldview is the point. Deadpool and Wolverine want you to have fun. They mostly succeed.</p>
<p><a href="/reviews/deadpool-wolverine-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Deadpool &amp; Wolverine</a></p>

<hr>

<h2>#13 - <a href="/reviews/avengers-endgame-2019/">Avengers: Endgame (2019)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
  <span class="score-detail">Woke Score: 10.54 &bull; Trad Score: 13.65 &bull; Margin: +3 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action/Sci-Fi &bull; <strong>Platform:</strong> Theatrical</p>
<p>The highest-grossing film of all time delivers 22 films of emotional payoff in 181 minutes, and its traditional score reflects what actually drives the narrative: ultimate sacrifice as heroic culmination, marriage and family as the ultimate good, and selfless competition to be the one who gives everything. The woke score of 10.54 reflects the female hero assembly shot, an untextured Captain Marvel functioning as deus ex machina, and the first MCU LGBTQ+ content. But the film's moral engine is Tony Stark dying for people he loves and Steve Rogers choosing the life he was denied. Those are traditional values, and they are what audiences remember.</p>
<p><a href="/reviews/avengers-endgame-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Avengers: Endgame</a></p>

<hr>

<h2>#14 - <a href="/reviews/fantastic-four-first-steps-2025/">The Fantastic Four: First Steps (2025)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
  <span class="score-detail">Woke Score: 9.98 &bull; Trad Score: 18.7 &bull; Margin: +9 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Superhero &bull; <strong>Platform:</strong> Theatrical</p>
<p>Marvel needed a win and mostly got one. The Fantastic Four: First Steps is the best MCU film in years, and its strongest element is the family at its center: Reed and Sue Richards as a traditional married couple, Sue's pregnancy and the defense of their unborn child as genuine stakes, and family as the foundation of everything the team does. A gender-swapped Silver Surfer and a globalist Future Foundation framing add woke points, but they sit beneath the dominant family-first narrative. A trad score of 18.7 represents a meaningful recovery for a franchise that had been drifting. The audience noticed.</p>
<p><a href="/reviews/fantastic-four-first-steps-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The Fantastic Four: First Steps</a></p>

<hr>

<h2>#15 - <a href="/reviews/captain-america-civil-war-2016/">Captain America: Civil War (2016)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
  <span class="score-detail">Woke Score: 9.96 &bull; Trad Score: 17.64 &bull; Margin: +8 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action Drama &bull; <strong>Platform:</strong> Theatrical</p>
<p>The MCU's most politically sophisticated film makes an argument that cuts against the progressive grain of the studio that produced it: sometimes individual conscience is right and collective authority is wrong. Steve Rogers does not capitulate to government oversight of superheroes, and the film validates his position. Loyalty to friendship is treated as a genuine moral foundation, not a character flaw. T'Challa's arc from vengeance to justice is one of the best character turns in franchise history. The anti-establishment framing adds woke points but cannot outweigh a film that repeatedly argues that the individual conscience matters more than the committee.</p>
<p><a href="/reviews/captain-america-civil-war-2016/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Captain America: Civil War</a></p>

<hr>

<h2>#16 - <a href="/reviews/thunderbolts/">Thunderbolts* (2025)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge mixed">MIXED</span>
  <span class="score-detail">Woke Score: 7.0 &bull; Trad Score: 5.0 &bull; Margin: -2 WOKE</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action &bull; <strong>Platform:</strong> Theatrical</p>
<p>Thunderbolts asks you to care about six characters you either forgot existed or cannot name at gunpoint. David Harbour's Red Guardian is the film's saving grace, bringing chaotic energy to a movie that otherwise struggles to establish stakes. Both scores are low because the film is ideologically thin: it is not trying to deliver a message, it is trying to deliver a movie. The -2 WOKE margin reflects a slight progressive lean that never rises to the level of agenda. This is a mid-tier MCU entry that neither advances conservative concerns nor provides significant traditional values content. It simply exists, which at this point in the franchise's history is almost a relief.</p>
<p><a href="/reviews/thunderbolts/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Thunderbolts*</a></p>

<hr>

<h2>#17 - <a href="/reviews/guardians-of-the-galaxy-2014/">Guardians of the Galaxy (2014)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="score-detail">Woke Score: 5.82 &bull; Trad Score: 21.28 &bull; Margin: +15 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Sci-Fi Adventure &bull; <strong>Platform:</strong> Theatrical</p>
<p>The best MCU origin film by a significant margin, and one of the most traditionally coded superhero movies ever made. Groot's sacrifice alone earns it the TRADITIONAL verdict. The entire film is built on redemption arcs, sacrificial love, found family forged through genuine need rather than identity politics, a mother's legacy honored across 26 years of grief, and a villain whose evil is clear and undiluted. The selfish man who chooses his people is one of the oldest traditional narratives in storytelling, and James Gunn delivered it with full sincerity. The modest woke score reflects the found-family-replacing-traditional-family framing and female warrior as equal. The traditional core is overwhelming.</p>
<p><a href="/reviews/guardians-of-the-galaxy-2014/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Guardians of the Galaxy</a></p>

<hr>

<h2>#18 - <a href="/reviews/shang-chi-2021/">Shang-Chi and the Legend of the Ten Rings (2021)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
  <span class="score-detail">Woke Score: 5.46 &bull; Trad Score: 14.19 &bull; Margin: +9 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Adventure/Fantasy &bull; <strong>Platform:</strong> Theatrical</p>
<p>The most pleasant surprise in the MCU's representation era. Where many expected Marvel's first Asian-led film to be a diversity lecture, what arrived is a deeply traditional family drama with spectacular fight choreography rooted in genuine Chinese cultural reverence. Father-son conflict and reconciliation, ancestral duty and cultural heritage, sacrifice and love are the film's engines. The woke score of 5.46 reflects deliberate stereotype replacement and a feminist subplot for Xialing, but these are secondary to the dominant traditional framework. Shang-Chi proved that representation does not have to mean ideology, a lesson the MCU has struggled to apply consistently.</p>
<p><a href="/reviews/shang-chi-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Shang-Chi and the Legend of the Ten Rings</a></p>

<hr>

<h2>#19 - <a href="/reviews/doctor-strange-2016/">Doctor Strange (2016)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
  <span class="score-detail">Woke Score: 5.35 &bull; Trad Score: 14.0 &bull; Margin: +9 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Fantasy &bull; <strong>Platform:</strong> Theatrical</p>
<p>The MCU's most spiritually interesting film earns its traditional lean through a disciplined ego-to-humility arc, a sacrifice-as-virtue climax, and director Scott Derrickson's Christian sensibility giving the film real moral weight. Strange's journey from arrogant surgeon to selfless defender of civilization is one of the cleanest traditional arcs in the franchise. The Ancient One's race and gender swap from Tibetan man to Celtic woman is the primary woke element, a deliberate choice to avoid Chinese market complications. The film argues that there are things worth defending, that order matters more than chaos, and that the ego must be surrendered. Those are not progressive values.</p>
<p><a href="/reviews/doctor-strange-2016/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Doctor Strange</a></p>

<hr>

<h2>#20 - <a href="/reviews/guardians-of-the-galaxy-vol-3-2023/">Guardians of the Galaxy Vol. 3 (2023)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
  <span class="score-detail">Woke Score: 5.18 &bull; Trad Score: 14.36 &bull; Margin: +9 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Action/Adventure/Sci-Fi &bull; <strong>Platform:</strong> Theatrical</p>
<p>James Gunn's farewell to the franchise he built is the rarest thing in Phase Five: a movie that earns its emotions without lecturing its audience. Rocket's origin story, the ethics of playing God, and whether broken things deserve to be saved are the film's real subjects. The sanctity of life, found family loyalty, and self-sacrifice and redemption drive the traditional score. The woke score of 5.18 reflects diversity casting in the villain lineup and animal rights messaging that never becomes a polemic. Vol. 3 is a film that says goodbye to its characters with genuine love, and the audience felt it. Among the best MCU films of the 2020s.</p>
<p><a href="/reviews/guardians-of-the-galaxy-vol-3-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Guardians of the Galaxy Vol. 3</a></p>

<hr>

<h2>#21 - <a href="/reviews/iron-man-2008/">Iron Man (2008)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
  <span class="score-detail">Woke Score: 5.0 &bull; Trad Score: 14.35 &bull; Margin: +9 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action &bull; <strong>Platform:</strong> Theatrical</p>
<p>The film that started it all. Seventeen years later, the original Iron Man holds up as one of the most traditionally coded entries in the franchise. Tony Stark's personal accountability arc, from weapons manufacturer who ignores the consequences of his products to armored hero who faces them directly, is a story of conscience and responsibility. Military respect and heroism are treated seriously. The complementary male-female dynamic between Tony and Pepper is genuine rather than performative. The woke score of 5 reflects light defense industry critique and a playboy lifestyle presented without moral judgment. The foundation Marvel built everything else on was more traditional than the house it eventually became.</p>
<p><a href="/reviews/iron-man-2008/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Iron Man</a></p>

<hr>

<h2>#22 - <a href="/reviews/spider-man-no-way-home-2021/">Spider-Man: No Way Home (2021)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="score-detail">Woke Score: 3.5 &bull; Trad Score: 22.05 &bull; Margin: +19 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action/Science Fiction &bull; <strong>Platform:</strong> Theatrical/Disney+</p>
<p>Not just the best Spider-Man film ever made but one of the most emotionally devastating blockbusters of the decade, earning every tear. Peter Parker's willingness to sacrifice everything, including the world's memory of his existence, to save five villains he has every reason to leave to their fates is the clearest statement of "great power, great responsibility" the franchise has ever delivered. Total self-sacrifice. Redemption offered unconditionally. The grief of loss treated with genuine weight. The woke score of 3.5, the second-lowest in the MCU, reflects minor race-swapped supporting characters and a brief immigration reference. They are irrelevant to what the film actually is. A +19 TRAD margin is among the highest in the franchise.</p>
<p><a href="/reviews/spider-man-no-way-home-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Spider-Man: No Way Home</a></p>

<hr>

<h2>#23 - <a href="/reviews/avengers-infinity-war-2018/">Avengers: Infinity War (2018)</a></h2>
<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="score-detail">Woke Score: 2.0 &bull; Trad Score: 16.8 &bull; Margin: +15 TRAD</span>
</div>
<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action &bull; <strong>Platform:</strong> Theatrical</p>
<p>The lowest woke score in the MCU and one of its most traditionally weighted films. Thanos wins because he is willing to treat individual lives as expendable. The heroes lose because they are not. That moral framework is explicitly conservative: the individual's life matters, love is not abstract, and sacrificing one person for the many is monstrous. Wanda refuses to destroy the Mind Stone because she cannot sacrifice Vision. Thor aims for the head instead of the chest because grief overrides tactics. These are not strategic failures. They are human virtues treated as such. The film's enormous diverse ensemble cast is its only woke point, and it serves the story rather than delivering a message. The MCU's best film is also its most traditional.</p>
<p><a href="/reviews/avengers-infinity-war-2018/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Avengers: Infinity War</a></p>

<hr>

<h2>What the Data Shows</h2>
<p>Across 23 MCU films, the franchise average is approximately 10.7 on the woke scale and 13.2 on the traditional scale. The MCU leans slightly traditional on aggregate, but the distribution matters: the most woke films (The Marvels, Eternals) are dramatically woke, while the most traditional films (Spider-Man: No Way Home, Guardians of the Galaxy, Infinity War) are traditionally coded for sincere reasons rooted in character and story.</p>

<p>The pattern is clear. Early MCU films (Phase One and Two) are generally more traditional because they were built on classic hero archetypes with minimal ideological overlay. The franchise's woke turn accelerated from Phase Three onward, peaking with The Marvels and Eternals. The subsequent commercial collapses of those films appear to have produced a partial correction: Fantastic Four First Steps and Guardians Vol. 3 both scored above +9 TRAD.</p>

<p>The lesson the data suggests is simple: when Marvel tells stories first and delivers ideology second, the films are better and the scores are more traditional. When the ideology is the reason the film exists, it fails on both measures. The audience knows the difference even when the studio pretends otherwise.</p>

<p>For full trope audits, parental guidance assessments, and creative team analysis on every film on this list, browse the complete VirtueVigil MCU coverage at <a href="/reviews/">VirtueVigil Reviews</a>. Every score is documented. Every trope is sourced. No guessing.</p>

</article>`
  }));

  writePage('lists/best-conservative-movies-netflix-2025/index.html', buildListiclePage({
    slug: 'best-conservative-movies-netflix-2025',
    title: '10 Best Movies on Netflix for Conservatives (2025)',
    description: 'Looking for conservative-friendly movies on Netflix? VirtueVigil ranks the 10 best options by traditional values score.',
    canonicalPath: 'lists/best-conservative-movies-netflix-2025',
    publishDate: '2026-03-17',
    htmlContent: `<article class="listicle-article">

<p>Netflix gets a bad reputation in conservative circles, and some of it is earned. The platform has produced its share of ideologically aggressive content over the years. But buried inside its catalog are films that score remarkably well on the VirtueVigil Traditional Score system: movies built around duty, sacrifice, family, and the kind of masculine honor that Hollywood usually treats as a liability.</p>

<p>This list ranks the 10 best Netflix-available films for conservative viewers in 2025, ordered by VirtueVigil score margin. Every entry has been reviewed in full using the VVWS methodology. The rankings are data-driven, not editorial. If a film is here, it earned its place by scoring positive on our Traditional-Woke margin. If you want to know exactly how it was scored, the links take you to the full reviews.</p>

<hr>

<h2>#1 &mdash; <a href="/reviews/peaky-blinders-the-immortal-man-2026/">Peaky Blinders: The Immortal Man (2026)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 28</span>
  <span class="mini-score woke">WOKE: 5</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +23 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Crime/Drama/History &bull; <strong>Platform:</strong> Netflix</p>

<p>Tommy Shelby returns for a big-screen finale that doubles down on everything that made the series great: loyalty, sacrifice, the weight of legacy, and the cost of power. The film is steeped in working-class honor codes and the kind of moral seriousness that treats its characters as responsible agents rather than victims of systems. A tradScore of 28 against a woke score of just 5 makes this the highest-scoring Netflix film on this list by a wide margin. Conservative viewers who have followed the Shelby family across six seasons will find a conclusion that respects both the characters and the audience.</p>

<p><a href="/reviews/peaky-blinders-the-immortal-man-2026/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Peaky Blinders: The Immortal Man</a></p>

<hr>

<h2>#2 &mdash; <a href="/reviews/spider-man-no-way-home-2021/">Spider-Man: No Way Home (2021)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 22.05</span>
  <span class="mini-score woke">WOKE: 3.5</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +19 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Superhero/Action/Science Fiction &bull; <strong>Platform:</strong> Netflix</p>

<p>Of all the MCU films VirtueVigil has reviewed, No Way Home scores highest on traditional values. Peter Parker makes irreversible sacrifices for people he loves without asking for recognition, and the film takes that sacrifice seriously. Responsibility, consequence, and the refusal to take the easy way out are the film's actual subjects. A tradScore of 22.05 and a woke score of 3.5 make it the most conservative-friendly Spider-Man film by a considerable distance. The multiverse mechanics are a delivery mechanism for a genuinely old-fashioned story about what it means to do the right thing when the cost is everything.</p>

<p><a href="/reviews/spider-man-no-way-home-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Spider-Man: No Way Home</a></p>

<hr>

<h2>#3 &mdash; <a href="/reviews/war-machine-2026/">War Machine (2026)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 22</span>
  <span class="mini-score woke">WOKE: 4</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +18 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Sci-Fi/Action/Thriller &bull; <strong>Platform:</strong> Netflix</p>

<p>A hard-edged military sci-fi thriller built around duty, chain of command, and what it costs to maintain order in a world that has forgotten why order matters. War Machine treats its soldier protagonists with the respect that Hollywood usually reserves for dissidents. A tradScore of 22 against a woke score of 4 puts it firmly in traditional territory, and the film earns those numbers through its insistence on competence, discipline, and moral clarity under pressure. For viewers who want action that actually respects its characters, this is one of Netflix's strongest 2026 releases.</p>

<p><a href="/reviews/war-machine-2026/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of War Machine</a></p>

<hr>

<h2>#4 &mdash; <a href="/reviews/nonnas-2025/">Nonnas (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 17</span>
  <span class="mini-score woke">WOKE: 1</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +16 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Comedy-Drama &bull; <strong>Platform:</strong> Netflix</p>

<p>A comedy-drama about a man who opens a restaurant staffed by actual Italian grandmothers, and ends up finding community, purpose, and a reason to keep going. Nonnas is warm without being saccharine, and its celebration of food, family, and the wisdom of older generations is entirely free of ideological agenda. A tradScore of 17 against a woke score of just 1 makes it one of the cleanest watches on Netflix this year. If you have been burned by feel-good films that hide progressive agendas under heartwarming premises, Nonnas is the real thing.</p>

<p><a href="/reviews/nonnas-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Nonnas</a></p>

<hr>

<h2>#5 &mdash; <a href="/reviews/train-dreams-2025/">Train Dreams (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 20.6</span>
  <span class="mini-score woke">WOKE: 5.3</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +15 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Period Drama &bull; <strong>Platform:</strong> Netflix</p>

<p>One of the quietest and most powerful films on this list, Train Dreams follows a man in early 20th-century Idaho who loses everything and rebuilds his life through solitary endurance. There is no ideology here, no systems to blame, no community organizing. Just a man, the land, and the slow work of surviving. A tradScore of 20.6 reflects the film's deep commitment to self-reliance and stoic masculinity without ever turning those themes into a lecture. Also nominated for Best Picture at the 98th Academy Awards, which means it arrives with critical credibility to match its traditional values score.</p>

<p><a href="/reviews/train-dreams-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Train Dreams</a></p>

<hr>

<h2>#6 &mdash; <a href="/reviews/beverly-hills-cop-axel-f-2024/">Beverly Hills Cop: Axel F (2024)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 15</span>
  <span class="mini-score woke">WOKE: 4</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +11 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action/Comedy &bull; <strong>Platform:</strong> Netflix</p>

<p>Eddie Murphy returns as Axel Foley and the film does exactly what it promises: fast-talking detective work, father-daughter reconciliation, and a buddy-cop dynamic built on mutual respect and competence. Axel F is funnier than it had any right to be, and its core emotional engine is a father who shows up for his daughter when it matters. A tradScore of 15 against a woke score of 4 lands it solidly in traditional territory. Netflix's most nostalgically satisfying original in years, and proof that legacy sequels do not have to betray their source material to find an audience.</p>

<p><a href="/reviews/beverly-hills-cop-axel-f-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Beverly Hills Cop: Axel F</a></p>

<hr>

<h2>#7 &mdash; <a href="/reviews/frankenstein-2025/">Frankenstein (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
  <span class="mini-score trad">TRAD: 20.86</span>
  <span class="mini-score woke">WOKE: 11.66</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +9 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Gothic/Science Fiction/Drama &bull; <strong>Platform:</strong> Netflix</p>

<p>Guillermo del Toro's long-awaited adaptation is faithful to Mary Shelley's text in ways that matter: the Creator-creature relationship is treated as a genuine moral question, not a metaphor for oppression politics. Jacob Elordi's creature is a meditation on what it means to be made by someone who abandons you, and the film takes that abandonment seriously as a moral failure. A tradScore of 20.86 against a woke score of 11.66 gives it a positive lean, though some progressive readings of the material are present and worth noting. Del Toro's craft makes this a rewarding watch despite the complexity of the source material's politics.</p>

<p><a href="/reviews/frankenstein-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Frankenstein</a></p>

<hr>

<h2>#8 &mdash; <a href="/reviews/havoc-2025/">Havoc (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
  <span class="mini-score trad">TRAD: 17.22</span>
  <span class="mini-score woke">WOKE: 8.4</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +9 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action/Crime/Thriller &bull; <strong>Platform:</strong> Netflix</p>

<p>A gritty crime thriller directed by Gareth Evans that follows a detective navigating a corrupt city after a drug deal goes sideways. Havoc is brutally efficient filmmaking, and its protagonist operates by a personal code of loyalty and justice that the film clearly endorses. A tradScore of 17.22 against a woke score of 8.4 gives it a traditional lean, and its relentless focus on individual accountability over systemic blame earns that designation. Tom Hardy delivers one of his most focused performances, and Evans shoots action with a precision that makes John Wick look choreographed.</p>

<p><a href="/reviews/havoc-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Havoc</a></p>

<hr>

<h2>#9 &mdash; <a href="/reviews/nobody-2-2025/">Nobody 2 (2025)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
  <span class="mini-score trad">TRAD: 15.12</span>
  <span class="mini-score woke">WOKE: 8.96</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +6 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action/Thriller/Comedy &bull; <strong>Platform:</strong> Netflix</p>

<p>Hutch Mansell is back, and the sequel doubles down on what made the original work: a quiet man pushed past his limits who refuses to apologize for being capable of violence in defense of the people he loves. Nobody 2 treats masculine protective instinct as a virtue rather than a pathology, and that distinction matters. A tradScore of 15.12 against a woke score of 8.96 lands it in traditional lean territory, making it a solid action pick for conservative viewers who want adrenaline without a lecture. Bob Odenkirk commits fully to the physical role and earns every second of screen time.</p>

<p><a href="/reviews/nobody-2-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Nobody 2</a></p>

<hr>

<h2>#10 &mdash; <a href="/reviews/kraven-the-hunter-2024/">Kraven the Hunter (2024)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
  <span class="mini-score trad">TRAD: 11.2</span>
  <span class="mini-score woke">WOKE: 5.4</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +6 TRAD</span>
</div>

<p class="listicle-meta"><strong>Genre:</strong> Action/Superhero &bull; <strong>Platform:</strong> Netflix</p>

<p>Critically dismissed but scoring positively on VirtueVigil's metric, Kraven the Hunter is a revenge-and-identity story built around a protagonist who rejects the comfortable life he was born into and forges his own code in the wild. The film's themes of self-reliance, physical discipline, and the rejection of inherited corruption are genuinely conservative in orientation. A tradScore of 11.2 against a woke score of 5.4 earns it a place on this list as a solid low-stakes streaming pick. Ignore the critic consensus on this one. The audience that showed up found something worth watching.</p>

<p><a href="/reviews/kraven-the-hunter-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Kraven the Hunter</a></p>

<hr>

<h2>Browse More at VirtueVigil</h2>

<p>Netflix is not a conservative platform, and it never claimed to be. But the films above prove that the streaming giant's catalog contains real options for viewers who are tired of being lectured. From the stoic endurance of Train Dreams to the old-school action of Beverly Hills Cop: Axel F to the moral seriousness of Peaky Blinders: The Immortal Man, there is more here than most conservative viewers expect to find.</p>

<p>Every film on this list has a full review at VirtueVigil with the complete VVWS scoring breakdown, trope-by-trope analysis, and parental guidance assessment. <a href="/">Browse the full VirtueVigil review catalog</a> to find more films scored by traditional values. New reviews publish weekly. Bookmark us and stop guessing what is safe to watch.</p>

</article>`
  }));

  writePage('lists/disney-woke-movies-ranked/index.html', buildListiclePage({
    slug: 'disney-woke-movies-ranked',
    title: 'Is Disney Going Woke? 10 Disney Movies Scored',
    description: 'We ran 10 Disney movies through VirtueVigil\'s scoring system. The results show a clear trend. Here\'s what we found.',
    canonicalPath: 'lists/disney-woke-movies-ranked',
    publishDate: '2026-03-18',
    htmlContent: `<article class="listicle-article">

<p>Disney built its empire on stories families could share across generations. Snow White. The Lion King. Fantasia. Films that earned their place in cultural memory because they told universal truths without an agenda attached. I grew up with those movies, and so did my kids. Then something shifted. Somewhere around 2019, the films coming out of Disney, Pixar, and the MCU started to feel different. Not worse in every case, but different in a way that is hard to ignore once you notice it. We decided to stop noticing and start measuring.</p>

<p>I ran 10 Disney-produced films through VirtueVigil's VVWS dual-scoring system, which measures woke content density and traditional values content separately. The results confirmed what many families already suspected: Disney's ideological lean has intensified dramatically since 2019. The data below tells the story better than any op-ed could. These are real scores from real reviews, not vibes. Ranked by woke score from highest to lowest, here is exactly where Disney stands.</p>

<hr>

<h2>#1 &mdash; <a href="/reviews/strange-world-2022/">Strange World (2022)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge woke">WOKE</span>
  <span class="mini-score woke">WOKE: 27.5</span>
  <span class="mini-score trad">TRAD: 12.32</span>
  <span class="mini-score" style="color:var(--accent-red);">MARGIN: -15 WOKE</span>
</div>

<p><strong>Woke Trap: YES</strong></p>

<p>Strange World is the film where Disney dropped all pretense. A $180 million animated feature built around two overt agendas: an anti-fossil-fuel environmental allegory and Disney's first openly gay animated lead character. The miracle energy source powering the civilization turns out to be a parasitic infection killing the creature they all live on. Fossil fuel is the parasite. Industrial civilization is the disease. Disney's first openly gay teen protagonist is folded into the story without announcement, which is either honest representation or a calculated attempt to avoid triggering parental scrutiny before the purchase decision is made. The film lost an estimated $197 million. Whatever the intent, families deserve to know what is in it before they sit down.</p>

<p><a href="/reviews/strange-world-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Strange World</a></p>

<hr>

<h2>#2 &mdash; <a href="/reviews/mulan-2020/">Mulan (2020)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge woke">WOKE LEAN</span>
  <span class="mini-score woke">WOKE: 20.78</span>
  <span class="mini-score trad">TRAD: 17.64</span>
  <span class="mini-score" style="color:var(--accent-red);">MARGIN: -3 WOKE</span>
</div>

<p><strong>Woke Trap: YES</strong></p>

<p>The live-action Mulan stripped out the romance, the songs, and the humor from the beloved 1998 original and replaced them with a feminist empowerment framework and a loyalty-to-self thesis that undercuts the story's original message. The original Mulan sacrificed herself for family and country, then earned recognition through demonstrated merit. The 2020 version positions those same values as a cage to break free from. Disney also filmed it in Xinjiang and thanked the local government agencies overseeing the Uyghur detention camps in the closing credits. A woke trap that managed to alienate conservative and progressive audiences simultaneously.</p>

<p><a href="/reviews/mulan-2020/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Mulan</a></p>

<hr>

<h2>#3 &mdash; <a href="/reviews/captain-marvel-2019/">Captain Marvel (2019)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge woke">WOKE</span>
  <span class="mini-score woke">WOKE: 19.44</span>
  <span class="mini-score trad">TRAD: 3.25</span>
  <span class="mini-score" style="color:var(--accent-red);">MARGIN: -16 WOKE</span>
</div>

<p><strong>Woke Trap: YES</strong></p>

<p>The MCU's most deliberately ideological film. Released on International Women's Day 2019. Directed by a female co-director by explicit studio design. Scored with No Doubt's "Just a Girl" during a key empowerment sequence. Every male authority figure in the film is a manipulator or an oppressor. The Kree military is coded as a patriarchal control structure. The refugee allegory involving the Skrulls is unambiguous and contemporary in its framing. Traditional Score: 3.25, the lowest in this entire list. This film was not hiding what it was, but the MCU brand gave it a built-in family audience that might not have bought a ticket to a standalone feminist superhero film by an unknown director.</p>

<p><a href="/reviews/captain-marvel-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Captain Marvel</a></p>

<hr>

<h2>#4 &mdash; <a href="/reviews/turning-red-2022/">Turning Red (2022)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge woke">WOKE</span>
  <span class="mini-score woke">WOKE: 17.85</span>
  <span class="mini-score trad">TRAD: 4.55</span>
  <span class="mini-score" style="color:var(--accent-red);">MARGIN: -13 WOKE</span>
</div>

<p><strong>Woke Trap: YES</strong></p>

<p>Pixar's Turning Red uses a puberty metaphor with precision: a 13-year-old girl transforms into a giant red panda whenever she experiences strong emotions, and the film's central thesis is that she should embrace these changes rather than suppress them to please her traditional Chinese-Canadian mother. The film frames the mother's cultural conservatism as the actual problem. Director Domee Shi confirmed in interviews that the red panda transformation is an explicit puberty and bodily autonomy metaphor. Parents expecting a fun animated animal adventure are getting a film about adolescent self-liberation from parental authority. The 4.55 traditional score is the second lowest on this list.</p>

<p><a href="/reviews/turning-red-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Turning Red</a></p>

<hr>

<h2>#5 &mdash; <a href="/reviews/wish-2023/">Wish (2023)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge woke">WOKE LEAN</span>
  <span class="mini-score woke">WOKE: 17.45</span>
  <span class="mini-score trad">TRAD: 11.9</span>
  <span class="mini-score" style="color:var(--accent-red);">MARGIN: -6 WOKE</span>
</div>

<p><strong>Woke Trap: YES</strong></p>

<p>Disney's centennial celebration cost $200 million and left audiences cold. Wish takes the studio's foundational mythology, wishing upon a star, and reframes it as a story about a benevolent authority figure secretly hoarding power over his subjects' dreams. The king who grants wishes turns out to be the villain: a controlling patriarch who decides which dreams are worthy and which should be suppressed. Asha's rebellion is coded as liberation from systemic control. The anti-institution framing runs through the entire second half. Disney spent $200 million to make a film arguing that the people in charge of your wishes cannot be trusted. The irony of that message coming from Disney is either lost on the studio or intentional.</p>

<p><a href="/reviews/wish-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Wish</a></p>

<hr>

<h2>#6 &mdash; <a href="/reviews/black-widow-2021/">Black Widow (2021)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge woke">WOKE LEAN</span>
  <span class="mini-score woke">WOKE: 16.95</span>
  <span class="mini-score trad">TRAD: 12.13</span>
  <span class="mini-score" style="color:var(--accent-red);">MARGIN: -5 WOKE</span>
</div>

<p><strong>Woke Trap: YES</strong></p>

<p>MCU Phase Four opened with a film about a program that forcibly sterilizes girls and converts them into weaponized government assassins. The Red Room storyline frames the entire film as a feminist revenge narrative. Florence Pugh as Yelena Belova is the film's genuine bright spot: funny, emotionally raw, and the source of the only real traditional warmth in the movie (the fake family dinner scene works because Pugh makes it work). The film's central message, that institutional power over women's bodies requires violent dismantling, is delivered without subtlety. Parents who thought they were watching a spy thriller should know what the thematic spine actually is.</p>

<p><a href="/reviews/black-widow-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Black Widow</a></p>

<hr>

<h2>#7 &mdash; <a href="/reviews/encanto-2021/">Encanto (2021)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 18.27</span>
  <span class="mini-score woke">WOKE: 8.68</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +10 TRAD</span>
</div>

<p>Encanto is the exception that proves the rule. Disney Animation made a film about family trauma, generational pressure, and the weight of impossible expectations, and it lands on genuinely traditional ground. The family survives not by rejecting their heritage but by rebuilding trust across generations. Abuela Alma's arc is the moral center of the film, and the story treats her controlling behavior as a wound rather than a character flaw to be mocked. She is forgiven. The family reconciles. The magic returns because the bonds are repaired. That is a conservative family values story told beautifully. One of the best Disney films in a decade, and proof that the studio can still do this when it tries.</p>

<p><a href="/reviews/encanto-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Encanto</a></p>

<hr>

<h2>#8 &mdash; <a href="/reviews/avengers-endgame-2019/">Avengers: Endgame (2019)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge mixed">TRADITIONAL LEAN</span>
  <span class="mini-score trad">TRAD: 13.65</span>
  <span class="mini-score woke">WOKE: 10.54</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +3 TRAD</span>
</div>

<p>The highest-grossing film of all time works because it earns every emotional payoff through sacrifice, love, and responsibility. Tony Stark's arc from self-centered billionaire to self-sacrificing father is one of cinema's most traditionally conservative character journeys: a man who discovers that protecting his family and his world matters more than his own survival. The film has woke content, a brief gay moment added by director Joe Russo, an all-female battle sequence that pauses the action for an applause beat, but the overall moral framework is sacrifice, duty, and family. The score reflects the balance. The heart of the film is unmistakably traditional.</p>

<p><a href="/reviews/avengers-endgame-2019/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Avengers: Endgame</a></p>

<hr>

<h2>#9 &mdash; <a href="/reviews/avengers-infinity-war-2018/">Avengers: Infinity War (2018)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 16.8</span>
  <span class="mini-score woke">WOKE: 2</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +15 TRAD</span>
</div>

<p>The MCU's best film is also its most traditionally weighted. Thanos wins because he treats individual lives as expendable in service of a utilitarian ideology. Every hero who resists him does so because they value specific people they love over abstract philosophical frameworks. Wanda will not let Vision sacrifice himself. Thor refuses to stop mourning his brother. Doctor Strange will not surrender the Time Stone until the very last moment. The heroes lose because they love people too much to treat them as variables in an equation. That is a conservative moral argument made through blockbuster filmmaking, and it is devastating precisely because the film commits to it fully.</p>

<p><a href="/reviews/avengers-infinity-war-2018/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Avengers: Infinity War</a></p>

<hr>

<h2>#10 &mdash; <a href="/reviews/spider-man-no-way-home-2021/">Spider-Man: No Way Home (2021)</a></h2>

<div class="listicle-scores">
  <span class="verdict-badge traditional">TRADITIONAL</span>
  <span class="mini-score trad">TRAD: 22.05</span>
  <span class="mini-score woke">WOKE: 3.5</span>
  <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +19 TRAD</span>
</div>

<p>The highest traditional score on this list, and the best Disney-affiliated film here by that measure. Spider-Man: No Way Home is a story about sacrifice, responsibility, and the genuine cost of doing the right thing. Peter Parker loses his identity, his girlfriend's memory, his aunt, and his place in the world because he chooses to save five villains from deaths they deserve rather than send them back to die. The film treats that choice as heroic without softening what it costs him. "With great power comes great responsibility" is the most conservative thesis in superhero cinema, and this film is the fullest expression of it. A Woke Score of 3.5 makes it one of the cleanest entries in the entire MCU catalog.</p>

<p><a href="/reviews/spider-man-no-way-home-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Spider-Man: No Way Home</a></p>

<hr>

<h2>The Verdict</h2>

<p>The data points in one direction. Disney made traditionally-scored films in 2018 and 2021 when its filmmakers told stories first and delivered messages second. It made its worst-scoring films in 2022 and 2023 when ideology came before story. Strange World, Turning Red, and Captain Marvel are not low-scoring because they have progressive politics. They score the way they do because the politics are the architecture, not the backdrop. Encanto and the Infinity War films work because the story carries the message instead of the message carrying the story. If you want to know whether Disney is going woke, these numbers are your answer. Browse VirtueVigil's full Disney and Marvel catalog to see every score for yourself and decide what your family watches with eyes open.</p>

<p><a href="/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Browse all VirtueVigil reviews</a></p>

</article>`
  }));

  writePage('lists/woke-trap-movies-list/index.html', buildListiclePage({
    slug: 'woke-trap-movies-list',
    title: '10 Movies That Are Woke Traps (Looked Safe, Weren\'t)',
    description: '10 films that looked safe but weren\'t. These movies used entertainment, nostalgia, and star power to hide progressive agendas until you were already invested.',
    canonicalPath: 'lists/woke-trap-movies-list',
    publishDate: '2026-03-18',
    htmlContent: `<article class="listicle">
  <div class="listicle-intro">
    <p>A woke trap is not just a woke movie. Plenty of films wear their ideology on their sleeve from frame one. A woke trap is something more calculated: a film that spends the first half of its runtime earning your trust, then uses that trust to deliver an ideological payload you never saw coming. The bait is real. The entertainment is real. The switch happens after you are already invested.</p>
    <p>VirtueVigil coined the term for exactly this pattern. Below are ten films that meet the criteria: negative score margins, and woke content that surfaces late or is buried beneath a surface audiences were conditioned to trust. Know before you go.</p>
  </div>

  <ol class="listicle-items">

    <li class="listicle-item">
      <div class="listicle-rank">1</div>
      <div class="listicle-content">
        <h2><a href="/reviews/lilo-and-stitch-2025/">Lilo and Stitch (2025)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-6 WOKE</span>
        </div>
        <p>Disney's live-action remake faithfully adapts the animated original's celebration of ohana, family sacrifice, and sisterhood for 75 percent of its runtime. It earns genuine emotional investment in Nani and Lilo. Then it rewrites the finale: Nani gives Lilo away to a neighbor so she can pursue a mainland scholarship and career. The original's climax, where Nani proves she can be a capable family guardian, is replaced by a message that self-actualization outranks keeping your family intact. The delay is the trap. Kids and parents are already rooting for the family before the film pivots on them.</p>
        <a href="/reviews/lilo-and-stitch-2025/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">2</div>
      <div class="listicle-content">
        <h2><a href="/reviews/dont-worry-darling-2022/">Don't Worry Darling (2022)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke">WOKE</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-19 WOKE</span>
        </div>
        <p>Marketed as a lush 1950s psychological thriller with Florence Pugh and Harry Styles, every trailer sold gorgeous visuals, marital passion, and cult mystery. What audiences received was an anti-patriarchy polemic whose villain is explicitly based on Jordan Peterson, a detail Olivia Wilde revealed only after release. The simulation premise is not revealed until roughly the 80-minute mark in a 123-minute film. Conservative families drawn in by period aesthetics and star power will not find the full ideological argument until well past the halfway point.</p>
        <a href="/reviews/dont-worry-darling-2022/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">3</div>
      <div class="listicle-content">
        <h2><a href="/reviews/civil-war-2024/">Civil War (2024)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-4 WOKE</span>
        </div>
        <p>Alex Garland refused to name the President's party and the marketing sold the film as purely apolitical. Conservatives exhausted by preachy cinema showed up expecting neutrality. What they found was a carefully constructed press-freedom parable: the press is heroic, the government is fascistic, and the morally righteous characters are all female photojournalists. The Texas-California alliance was designed to confuse, not represent. The apolitical marketing is the bait. The progressive architecture is what lives inside it.</p>
        <a href="/reviews/civil-war-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">4</div>
      <div class="listicle-content">
        <h2><a href="/reviews/dune-part-two-2024/">Dune: Part Two (2024)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-8 WOKE</span>
        </div>
        <p>The first hour is spectacular: Hans Zimmer's score, Denis Villeneuve's visuals, a genuine adventure setup. Then Dune: Part Two pivots into an explicit anti-messiah political argument. Chani is reframed as the sole moral voice condemning Paul's rise, and the film's warning against religious-nationalist leadership does not fully surface until well past the 50-minute mark. Conservative viewers who identify with faith-based community and charismatic leadership will find the film's conclusion significantly more troubling than anything the opening suggested.</p>
        <a href="/reviews/dune-part-two-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">5</div>
      <div class="listicle-content">
        <h2><a href="/reviews/joker-folie-a-deux-2024/">Joker: Folie a Deux (2024)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge mixed">MIXED</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-2 WOKE</span>
        </div>
        <p>The original Joker (2019) was a billion-dollar sensation that resonated powerfully with disaffected and conservative-leaning viewers. The sequel weaponizes that goodwill. Nothing in the marketing signaled that Folie a Deux would systematically deconstruct, humiliate, and ultimately murder the character audiences invested in. Conservative viewers who showed up expecting a continuation of the first film's raw character study walked into a calculated lecture about why they were wrong to identify with Arthur Fleck in the first place.</p>
        <a href="/reviews/joker-folie-a-deux-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">6</div>
      <div class="listicle-content">
        <h2><a href="/reviews/glass-onion-2022/">Glass Onion: A Knives Out Mystery (2022)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge strongly-woke">STRONGLY WOKE</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-24 WOKE</span>
        </div>
        <p>Glass Onion presents itself as equal-opportunity satire mocking all flavors of elite hypocrisy. The puzzle mechanics are genuinely entertaining. But the film's sympathies are precise: the villain is coded as a right-leaning tech bro with COVID-denier energy, the hero is a Black woman reclaiming stolen intellectual credit, and the climax requires audiences to celebrate the destruction of irreplaceable private property as righteous. Conservative viewers who enjoy the mystery may not notice they have been served a tightly constructed progressive fable until it is already over.</p>
        <a href="/reviews/glass-onion-2022/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">7</div>
      <div class="listicle-content">
        <h2><a href="/reviews/wuthering-heights/">Wuthering Heights (2026)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke">WOKE</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-10 WOKE</span>
        </div>
        <p>The Bronte name sells the ticket. Emerald Fennell's agenda fills the seat. Trailers sold gothic romance, the iconic Heathcliff and Cathy love story, and the prestige weight of literary adaptation. The film delivers explicit BDSM content, a masturbation scene, and degradation material not present in Emily Bronte's source novel. Audiences who bought their ticket for one of English literature's defining love stories found something constructed to shock and subvert rather than adapt. The literary pedigree is the cover.</p>
        <a href="/reviews/wuthering-heights/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">8</div>
      <div class="listicle-content">
        <h2><a href="/reviews/predator-badlands/">Predator: Badlands (2025)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-4 WOKE</span>
        </div>
        <p>The Predator brand carries decades of goodwill with conservative audiences who love the original R-rated masculine action films. Badlands exploits that goodwill to deliver a PG-13 family adventure built on feminist messaging, a defanged male lead, an all-female found-family structure, and a cute toyetic sidekick. This is Disney house style retrofitted onto a franchise built on opposite values. Fans who showed up for the spirit of 1987 found a franchise wearing a familiar mask over a completely different body.</p>
        <a href="/reviews/predator-badlands/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">9</div>
      <div class="listicle-content">
        <h2><a href="/reviews/beetlejuice-beetlejuice-2024/">Beetlejuice Beetlejuice (2024)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-4 WOKE</span>
        </div>
        <p>The marketing leaned hard on 1988 nostalgia: Beetlejuice is back, Michael Keaton is back, the sandworms are back. What it downplayed is that the film's emotional center is a mother-daughter conflict in which a Gen Z daughter resents her mother's entire worldview, Charles Deetz is killed off-screen without ceremony, and Delia's feminist art career is played as endorsement as much as comedy. The nostalgia is genuine. The film wrapped around it runs on 2024 values that conservative families raised on the original were not warned about.</p>
        <a href="/reviews/beetlejuice-beetlejuice-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">10</div>
      <div class="listicle-content">
        <h2><a href="/reviews/one-battle-after-another-2025/">One Battle After Another (2025)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="verdict-badge trap">WOKE TRAP DETECTED</span>
          <span class="score-badge">-4 WOKE</span>
        </div>
        <p>The trailer sells car chases, gunfights, and Leonardo DiCaprio doing his thing. All of those elements are genuinely there. But beneath the surface thrills, Paul Thomas Anderson has constructed a deeply political film about immigration, race, white supremacy, and state violence. The action movie veneer gets conservative viewers in the door. The progressive politics are what they encounter once seated. The action is not dishonest. The framing of everything underneath it is a different matter.</p>
        <a href="/reviews/one-battle-after-another-2025/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

  </ol>

  <div class="listicle-conclusion">
    <h3>How to Use This List</h3>
    <p>The defining characteristic of a woke trap is not the woke content itself. It is the delay. These ten films were constructed to earn your emotional investment before delivering their ideological argument. They are more concerning than openly woke films because the manipulation is architectural. VirtueVigil exists precisely to surface this pattern before you buy a ticket.</p>
    <p>For more reviews, woke trap ratings, and full trope audit logs on the latest releases, browse <a href="/">all VirtueVigil reviews</a> or check our dedicated <a href="/category/woke-traps/">Woke Trap Alerts</a> category. Subscribe free to get weekly alerts delivered to you.</p>
  </div>

</article>

<style>
.listicle { max-width: 860px; }
.listicle-intro { margin-bottom: 36px; line-height: 1.75; }
.listicle-intro p { margin-bottom: 16px; color: #ccc; }
.listicle-items { list-style: none; padding: 0; margin: 0; }
.listicle-item { display: flex; gap: 20px; margin-bottom: 40px; padding-bottom: 40px; border-bottom: 1px solid rgba(201,168,76,0.15); align-items: flex-start; }
.listicle-rank { flex: 0 0 48px; width: 48px; height: 48px; background: rgba(201,168,76,0.15); border: 2px solid rgba(201,168,76,0.4); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; font-weight: 700; color: #c9a84c; flex-shrink: 0; margin-top: 4px; }
.listicle-content { flex: 1; min-width: 0; }
.listicle-content h2 { font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; margin: 0 0 10px; }
.listicle-content h2 a { color: #e8e6e1; text-decoration: none; }
.listicle-content h2 a:hover { color: #c9a84c; }
.listicle-badges { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px; }
.verdict-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }
.verdict-badge.woke { background: rgba(196,64,64,0.2); color: #e74c3c; border: 1px solid #e74c3c; }
.verdict-badge.strongly-woke { background: rgba(196,64,64,0.25); color: #e74c3c; border: 1px solid #e74c3c; }
.verdict-badge.woke-lean { background: rgba(196,64,64,0.12); color: #e07060; border: 1px solid #e07060; }
.verdict-badge.mixed { background: rgba(212,168,67,0.15); color: #d4a843; border: 1px solid #d4a843; }
.verdict-badge.trap { background: rgba(180,0,60,0.2); color: #ff4d88; border: 1px solid #ff4d88; }
.score-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; background: rgba(20,20,28,0.8); color: #a0a0a8; border: 1px solid rgba(255,255,255,0.1); }
.listicle-content p { color: #bbb; line-height: 1.7; margin-bottom: 14px; }
.listicle-cta { display: inline-block; color: #c9a84c; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(201,168,76,0.35); padding: 6px 14px; border-radius: 5px; transition: background 0.2s; }
.listicle-cta:hover { background: rgba(201,168,76,0.1); }
.listicle-conclusion { margin-top: 40px; padding: 28px; background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2); border-radius: 8px; }
.listicle-conclusion h3 { font-family: 'Cinzel',Georgia,serif; color: #c9a84c; margin: 0 0 14px; }
.listicle-conclusion p { color: #bbb; line-height: 1.75; margin-bottom: 12px; }
.listicle-conclusion a { color: #c9a84c; }
@media (max-width: 600px) { .listicle-item { flex-direction: column; } .listicle-rank { width: 40px; height: 40px; font-size: 1rem; } }
</style>`
  }));

  writePage('lists/marvel-movies-traditional-values/index.html', buildListiclePage({
    slug: 'marvel-movies-traditional-values',
    title: 'Every Marvel Movie Ranked by Traditional Values Score',
    description: 'We scored every Marvel Cinematic Universe movie for traditional values. From the most patriotic to the most woke, here is the complete MCU ranking.',
    canonicalPath: 'lists/marvel-movies-traditional-values',
    publishDate: '2026-03-18',
    htmlContent: `<article class="listicle">
  <div class="listicle-intro">
    <p>The Marvel Cinematic Universe has produced over two dozen films across nearly two decades, and not all of them are created equal from a traditional values standpoint. VirtueVigil scored every MCU entry using our Woke-Watch Scoring System, weighing themes of sacrifice, family, duty, faith, individual conscience, and moral clarity against progressive ideology, identity politics, and anti-authority messaging. The results reveal a franchise that started strong, drifted badly in the middle years, and has never fully recovered from its Phase Four collapse.</p>
    <p>The spread is wider than you might expect. At the top sits a Spider-Man film with a +19 TRAD margin that will genuinely make you cry. At the bottom sits a film that scored the franchise's worst woke number and bored audiences to a 47% on Rotten Tomatoes. What separates the great MCU films from the failures is almost always the same thing: the best ones tell stories about sacrifice, duty, and love. The worst ones treat the audience as a demographic to lecture. Here is every MCU film we have reviewed, ranked from most traditional to most woke.</p>
  </div>

  <ol class="listicle-items">

    <li class="listicle-item">
      <div class="listicle-rank">1</div>
      <div class="listicle-content">
        <h2><a href="/reviews/spider-man-no-way-home-2021/">Spider-Man: No Way Home (2021)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional">TRADITIONAL</span>
          <span class="score-badge">+19 TRAD</span>
        </div>
        <p>The highest-scoring MCU film in our system earns it through relentless sacrifice. Peter Parker loses everything, and the film treats that loss with genuine moral weight rather than reversing it cheaply. No woke messaging, no identity lectures, just a young man choosing responsibility over his own happiness.</p>
        <a href="/reviews/spider-man-no-way-home-2021/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">2</div>
      <div class="listicle-content">
        <h2><a href="/reviews/guardians-of-the-galaxy-2014/">Guardians of the Galaxy (2014)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional">TRADITIONAL</span>
          <span class="score-badge">+15 TRAD</span>
        </div>
        <p>The best MCU origin film is also the most traditionally coded. Redemption arcs, sacrificial love, found family built on genuine need rather than identity politics, and a mother's legacy honored across 26 years of grief. Groot's sacrifice alone earns it the traditional verdict.</p>
        <a href="/reviews/guardians-of-the-galaxy-2014/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">3</div>
      <div class="listicle-content">
        <h2><a href="/reviews/avengers-infinity-war-2018/">Avengers: Infinity War (2018)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional">TRADITIONAL</span>
          <span class="score-badge">+15 TRAD</span>
        </div>
        <p>The MCU's best film is also its most traditionally weighted. Thanos wins by treating lives as expendable numbers. The heroes lose because they refuse to do the same. That is a conservative moral framework told with devastating emotional force.</p>
        <a href="/reviews/avengers-infinity-war-2018/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">4</div>
      <div class="listicle-content">
        <h2><a href="/reviews/avengers-doomsday-2026/">Avengers: Doomsday (2026)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional">TRADITIONAL</span>
          <span class="score-badge">+14 TRAD</span>
        </div>
        <p>The Russo Brothers return with Robert Downey Jr. as Doctor Doom. A story about heroic unity defeating a brilliant tyrant who wants to remake the world by force sits firmly in traditional values territory. Pre-release review based on available materials.</p>
        <a href="/reviews/avengers-doomsday-2026/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">5</div>
      <div class="listicle-content">
        <h2><a href="/reviews/guardians-of-the-galaxy-vol-3-2023/">Guardians of the Galaxy Vol. 3 (2023)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
          <span class="score-badge">+9 TRAD</span>
        </div>
        <p>James Gunn's farewell to the franchise he built is the rarest thing in Phase Five: a movie that earns its emotions without lecturing its audience. The ethics of creation, the dignity of broken things, and found family treated as real rather than decorative.</p>
        <a href="/reviews/guardians-of-the-galaxy-vol-3-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">6</div>
      <div class="listicle-content">
        <h2><a href="/reviews/shang-chi-2021/">Shang-Chi and the Legend of the Ten Rings (2021)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
          <span class="score-badge">+9 TRAD</span>
        </div>
        <p>The most pleasant surprise in the MCU's representation era. Where many expected a diversity lecture, the film delivered a deeply traditional family drama with spectacular fight choreography drawing from Chinese culture with genuine reverence. Filial duty and paternal redemption drive the story.</p>
        <a href="/reviews/shang-chi-2021/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">7</div>
      <div class="listicle-content">
        <h2><a href="/reviews/iron-man-2008/">Iron Man (2008)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
          <span class="score-badge">+9 TRAD</span>
        </div>
        <p>The film that started the MCU holds up as one of its most traditionally grounded entries. Tony Stark's arc from self-serving weapons dealer to self-sacrificing defender is classic hero mythology told without apology. Robert Downey Jr. makes it look effortless.</p>
        <a href="/reviews/iron-man-2008/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">8</div>
      <div class="listicle-content">
        <h2><a href="/reviews/doctor-strange-2016/">Doctor Strange (2016)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
          <span class="score-badge">+9 TRAD</span>
        </div>
        <p>A superhero origin story with genuine moral seriousness, directed by a Christian filmmaker who understood that magic requires metaphysics. The ego-to-humility arc is classical, the sacrifice climax is earned, and Scott Derrickson's worldview gives the film real weight.</p>
        <a href="/reviews/doctor-strange-2016/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">9</div>
      <div class="listicle-content">
        <h2><a href="/reviews/captain-america-civil-war-2016/">Captain America: Civil War (2016)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
          <span class="score-badge">+8 TRAD</span>
        </div>
        <p>The MCU's most politically sophisticated film lands firmly on the side of individual conscience over government authority. Steve Rogers does not sign. The Sokovia Accords lose the argument. Masculine friendship is treated as a genuine moral foundation worth defending.</p>
        <a href="/reviews/captain-america-civil-war-2016/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">10</div>
      <div class="listicle-content">
        <h2><a href="/reviews/thor-ragnarok-2017/">Thor: Ragnarok (2017)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
          <span class="score-badge">+7 TRAD</span>
        </div>
        <p>More traditional than it looks under the neon and jokes. Thor's arc toward genuine leadership, Heimdall's quiet heroism, and Loki's reluctant loyalty all earn traditional points. Taika Waititi's style creates some woke drag, but the story's core is about protecting your people when the old world is gone.</p>
        <a href="/reviews/thor-ragnarok-2017/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">11</div>
      <div class="listicle-content">
        <h2><a href="/reviews/avengers-endgame-2019/">Avengers: Endgame (2019)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
          <span class="score-badge">+3 TRAD</span>
        </div>
        <p>22 films of investment cashed in over 181 minutes. Tony Stark's sacrifice is the franchise at its moral peak. The infamous all-female hero moment and some progressive casting choices drag the score, but the ending remains one of the most emotionally resonant sequences in blockbuster history.</p>
        <a href="/reviews/avengers-endgame-2019/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">12</div>
      <div class="listicle-content">
        <h2><a href="/reviews/black-panther-2018/">Black Panther (2018)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge mixed">MIXED</span>
          <span class="score-badge">+1 TRAD</span>
        </div>
        <p>Surprisingly traditional under its cultural weight. T'Challa's story is ultimately about duty, ancestral honor, and choosing his people over personal grievance. The progressive packaging is real and the woke score is elevated, but the film's moral spine is more conservative than most critics acknowledged.</p>
        <a href="/reviews/black-panther-2018/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">13</div>
      <div class="listicle-content">
        <h2><a href="/reviews/spider-man-across-the-spider-verse-2023/">Spider-Man: Across the Spider-Verse (2023)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge mixed">MIXED</span>
          <span class="score-badge">-2 WOKE</span>
        </div>
        <p>The most technically ambitious animated film ever made earns that distinction honestly. Its woke lean comes primarily from Miles Morales's rebellion against a predetermined fate, which carries anti-authority undertones. The craftsmanship is undeniable even if the ideology is slightly off.</p>
        <a href="/reviews/spider-man-across-the-spider-verse-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">14</div>
      <div class="listicle-content">
        <h2><a href="/reviews/doctor-strange-multiverse-of-madness-2022/">Doctor Strange in the Multiverse of Madness (2022)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="score-badge">-3 WOKE</span>
        </div>
        <p>Sam Raimi brings genuine horror craft to the MCU and Elizabeth Olsen delivers a villain performance for the ages. The woke elements center on Wanda's maternal entitlement framed as sympathetic rather than monstrous. Better than most Phase Four output but still a net loss on values.</p>
        <a href="/reviews/doctor-strange-multiverse-of-madness-2022/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">15</div>
      <div class="listicle-content">
        <h2><a href="/reviews/captain-america-brave-new-world-2025/">Captain America: Brave New World (2025)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="score-badge">-4 WOKE</span>
        </div>
        <p>A deeply confused film that cannot decide whether it wants to be a political thriller, a superhero spectacle, or a meditation on race in America. It tries to be all three and succeeds at none. Sam Wilson is a compelling character who deserved a better script.</p>
        <a href="/reviews/captain-america-brave-new-world-2025/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">16</div>
      <div class="listicle-content">
        <h2><a href="/reviews/thor-love-and-thunder-2022/">Thor: Love and Thunder (2022)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="score-badge">-4 WOKE</span>
        </div>
        <p>A film at war with itself. Christian Bale's villain Gorr carries a genuinely dark meditation on faith and abandonment, but Waititi buries it under relentless tonal chaos. The gender-swapped Mighty Thor and the overall message that the old institutions have failed drag the score into woke territory.</p>
        <a href="/reviews/thor-love-and-thunder-2022/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">17</div>
      <div class="listicle-content">
        <h2><a href="/reviews/ant-man-and-the-wasp-quantumania-2023/">Ant-Man and the Wasp: Quantumania (2023)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="score-badge">-4 WOKE</span>
        </div>
        <p>Had one job: introduce Kang the Conqueror as the next Thanos-level threat. It failed at everything except Kang, and then Jonathan Majors' conviction destroyed even that. The Ant-Man charm evaporated in the Quantum Realm and the progressive subtext never earned its screen time.</p>
        <a href="/reviews/ant-man-and-the-wasp-quantumania-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">18</div>
      <div class="listicle-content">
        <h2><a href="/reviews/black-widow-2021/">Black Widow (2021)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="score-badge">-5 WOKE</span>
        </div>
        <p>Florence Pugh as Yelena Belova is the best thing in it, and nearly salvages the film on her own. The Red Room storyline has genuine emotional stakes. But the anti-male-authority framing, the feminist sisterhood messaging, and the belated origin story structure all push the score left.</p>
        <a href="/reviews/black-widow-2021/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">19</div>
      <div class="listicle-content">
        <h2><a href="/reviews/black-panther-wakanda-forever-2022/">Black Panther: Wakanda Forever (2022)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke-lean">WOKE LEAN</span>
          <span class="score-badge">-6 WOKE</span>
        </div>
        <p>A genuine grief film trapped inside a franchise obligation. Angela Bassett is extraordinary and the film's mourning for Chadwick Boseman is real. But at 161 minutes it drowns in progressive messaging, feminist nation-state framing, and identity politics that undermine the emotional core.</p>
        <a href="/reviews/black-panther-wakanda-forever-2022/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

    <li class="listicle-item">
      <div class="listicle-rank">20</div>
      <div class="listicle-content">
        <h2><a href="/reviews/eternals-2021/">Eternals (2021)</a></h2>
        <div class="listicle-badges">
          <span class="verdict-badge woke">WOKE</span>
          <span class="score-badge">-14 WOKE</span>
        </div>
        <p>The MCU's worst-scoring film is also its biggest critical and commercial failure. A 47% on Rotten Tomatoes. A 5.9 on IMDB. The most progressive casting in franchise history combined with the least engaging story. Chloe Zhao's art-house pacing drains any superhero energy and the ideology is front and center.</p>
        <a href="/reviews/eternals-2021/" class="listicle-cta">Read Full VirtueVigil Review</a>
      </div>
    </li>

  </ol>

  <div class="listicle-conclusion">
    <h3>The MCU Trend Line</h3>
    <p>The franchise's trajectory tells you everything. The MCU's highest-scoring films came from its first decade, when storytellers focused on sacrifice, duty, and earned emotion over progressive credentials. The Phase Four collapse was not just a creative failure. It was an ideological overcorrection that audiences rejected in real time.</p>
    <p>Browse all our MCU reviews and the full VirtueVigil film database at <a href="/">virtuevigil.com</a> to see how every film stacks up on our Woke-Watch Scoring System.</p>
  </div>

<style>
.listicle { max-width: 860px; }
.listicle-intro p { color: #bbb; line-height: 1.8; margin-bottom: 18px; font-size: 1.05rem; }
.listicle-items { list-style: none; padding: 0; margin: 0; }
.listicle-item { display: flex; gap: 20px; align-items: flex-start; padding: 28px 0; border-bottom: 1px solid rgba(255,255,255,0.07); }
.listicle-rank { min-width: 52px; height: 52px; background: rgba(201,168,76,0.15); border: 2px solid rgba(201,168,76,0.4); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; font-weight: 700; color: #c9a84c; flex-shrink: 0; }
.listicle-content h2 { font-family: 'Cinzel',Georgia,serif; font-size: 1.1rem; margin: 0 0 10px; }
.listicle-content h2 a { color: #e8e8e8; text-decoration: none; }
.listicle-content h2 a:hover { color: #c9a84c; }
.listicle-badges { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.verdict-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }
.verdict-badge.traditional { background: rgba(64,196,100,0.2); color: #40c464; border: 1px solid #40c464; }
.verdict-badge.traditional-lean { background: rgba(64,196,100,0.12); color: #60d484; border: 1px solid #60d484; }
.verdict-badge.mixed { background: rgba(212,168,67,0.15); color: #d4a843; border: 1px solid #d4a843; }
.verdict-badge.woke-lean { background: rgba(196,64,64,0.12); color: #e07060; border: 1px solid #e07060; }
.verdict-badge.woke { background: rgba(196,64,64,0.2); color: #e74c3c; border: 1px solid #e74c3c; }
.score-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; background: rgba(20,20,28,0.8); color: #a0a0a8; border: 1px solid rgba(255,255,255,0.1); }
.listicle-content p { color: #bbb; line-height: 1.7; margin-bottom: 14px; }
.listicle-cta { display: inline-block; color: #c9a84c; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(201,168,76,0.35); padding: 6px 14px; border-radius: 5px; transition: background 0.2s; }
.listicle-cta:hover { background: rgba(201,168,76,0.1); }
.listicle-conclusion { margin-top: 40px; padding: 28px; background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2); border-radius: 8px; }
.listicle-conclusion h3 { font-family: 'Cinzel',Georgia,serif; color: #c9a84c; margin: 0 0 14px; }
.listicle-conclusion p { color: #bbb; line-height: 1.75; margin-bottom: 12px; }
.listicle-conclusion a { color: #c9a84c; }
@media (max-width: 600px) { .listicle-item { flex-direction: column; } .listicle-rank { width: 42px; height: 42px; font-size: 1rem; } }
</style>
</article>`
  }));

  writePage('lists/best-war-movies-patriots/index.html', buildListiclePage({
    slug: 'best-war-movies-patriots',
    title: 'Best War Movies for Patriots (Ranked by VirtueVigil)',
    description: 'The best war movies for patriots ranked by VirtueVigil Woke Score. Low ideology, high traditional values. From Saving Private Ryan to Warfare (2025).',
    canonicalPath: 'lists/best-war-movies-patriots',
    publishDate: '2026-03-19',
    htmlContent: `<article class="listicle-article">
      <div class="listicle-intro">
        <p>Not every war film deserves your time. Hollywood has a long track record of turning genuine military sacrifice into vehicles for anti-war messaging, moral relativism, and political point-scoring. VirtueVigil has done the work so you do not have to. Every film on this list scored TRADITIONAL or higher on the VirtueVigil Woke/Traditional scoring system, meaning the values on screen -- duty, sacrifice, brotherhood, family, faith, and national honor -- dominate the narrative from start to finish.</p>
        <p>These are not comfort films. Several of them are brutal, honest depictions of what war costs. But every one of them treats the men and women who fight as heroes worth respecting, not as props for an agenda. If you want war films that make you proud to be an American -- or at least proud of what this country has been capable of producing -- start here.</p>
      </div>

      <ol class="listicle-items">
        <li class="listicle-item">
          <div class="listicle-rank">1</div>
          <div class="listicle-content">
            <h2><a href="/reviews/american-sniper-2014/">American Sniper (2014)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+34 TRAD</span>
            </div>
            <p>The highest traditional score on this list by a wide margin. Clint Eastwood's portrait of Chris Kyle treats patriotism, military service, and masculine virtue as unambiguous goods. The film does not hedge. Kyle is a sheepdog, his mission is righteous, and his sacrifice is honored without qualification. No revisionism. No deconstruction. One of the most purely traditional war films Hollywood has produced in 30 years.</p>
            <a href="/reviews/american-sniper-2014/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">2</div>
          <div class="listicle-content">
            <h2><a href="/reviews/gladiator-2000/">Gladiator (2000)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+31 TRAD</span>
            </div>
            <p>A film about a general who loses everything -- his emperor, his family, his freedom -- and chooses honor anyway. Gladiator is a meditation on masculine duty, loyalty, and the kind of vengeance that is not revenge but justice. The traditional values here are foundational, not decorative. Ridley Scott made the definitive film about what a man owes to the people he loves and the civilization he serves.</p>
            <a href="/reviews/gladiator-2000/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">3</div>
          <div class="listicle-content">
            <h2><a href="/reviews/saving-private-ryan-1998/">Saving Private Ryan (1998)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+28 TRAD</span>
            </div>
            <p>Spielberg's masterwork earns every bit of its traditional score. The opening 25 minutes are among the most honest portrayals of combat ever committed to film. The mission -- one man's life for a mother's grief -- is treated as morally serious, not morally complicated. Sacrifice is the point, not the problem. Every soldier on screen is portrayed as a real person doing something that matters.</p>
            <a href="/reviews/saving-private-ryan-1998/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">4</div>
          <div class="listicle-content">
            <h2><a href="/reviews/sound-of-freedom-2023/">Sound of Freedom (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+27 TRAD</span>
            </div>
            <p>The film studios sat on for five years because it did not fit the agenda. Jim Caviezel plays Tim Ballard, a federal agent who resigns his position to rescue trafficked children. Sound of Freedom is about a man of faith who acts on his convictions when institutions will not. One of the most important American films of the 2020s -- and one that was nearly buried before audiences found it anyway.</p>
            <a href="/reviews/sound-of-freedom-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">5</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-patriot-2000/">The Patriot (2000)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+22 TRAD</span>
            </div>
            <p>Mel Gibson at his most unapologetically pro-American. A widowed father turned Revolutionary War commander who fights not for ideology but for family, land, and liberty. The film does not flinch from the cost of war or from the justness of the cause. Exactly what a patriot film should be: a story about a man who fights because he has something worth fighting for.</p>
            <a href="/reviews/the-patriot-2000/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">6</div>
          <div class="listicle-content">
            <h2><a href="/reviews/top-gun-maverick-2022/">Top Gun: Maverick (2022)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+20 TRAD</span>
            </div>
            <p>The best American action film of the 2020s. Top Gun: Maverick trusts its audience to feel pride, admiration, and genuine awe at what American military excellence looks like. No apologies, no deconstruction, no agenda. Skill, discipline, sacrifice, and the best practical flight photography ever put on screen. A film that remembered something most of Hollywood has forgotten: audiences want to feel something real.</p>
            <a href="/reviews/top-gun-maverick-2022/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">7</div>
          <div class="listicle-content">
            <h2><a href="/reviews/hacksaw-ridge-2016/">Hacksaw Ridge (2016)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+19 TRAD</span>
            </div>
            <p>Desmond Doss refused to carry a weapon and saved 75 men at Okinawa anyway. Mel Gibson's biopic is the rarest kind of war film: one where faith is treated as the source of genuine heroism rather than a character flaw or punchline. The traditional score reflects a film that takes Christianity seriously, earns it through the narrative, and does not walk it back in the third act.</p>
            <a href="/reviews/hacksaw-ridge-2016/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">8</div>
          <div class="listicle-content">
            <h2><a href="/reviews/braveheart-1995/">Braveheart (1995)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+16 TRAD</span>
            </div>
            <p>William Wallace does not fight for an ideology. He fights because they killed his wife, because the land belongs to his people, and because freedom is worth dying for. Braveheart is one of the most unapologetically traditional epics in the Hollywood canon. Thirty years on, it has not aged in terms of its values -- and it never will, because those values are universal.</p>
            <a href="/reviews/braveheart-1995/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">9</div>
          <div class="listicle-content">
            <h2><a href="/reviews/gladiator-ii-2024/">Gladiator II (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+16 TRAD</span>
            </div>
            <p>Ridley Scott's sequel largely holds the line on the original's values. Virtue, vengeance with purpose, masculine duty, and the corruption of power versus the integrity of the individual are the film's central concerns. Not quite the original in terms of emotional weight, but it earns its place on this list by keeping the ideology off the screen and the combat on it.</p>
            <a href="/reviews/gladiator-ii-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">10</div>
          <div class="listicle-content">
            <h2><a href="/reviews/silent-storm-2026/">Silent Storm (2026)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+14 TRAD</span>
            </div>
            <p>Kathryn Bigelow's Cold War submarine thriller is a tight, disciplined film about duty under pressure. Silent Storm treats military command, unit loyalty, and the weight of classified responsibility with genuine seriousness. A welcome addition to the patriot canon from a director who knows how to make this kind of film and does not feel the need to apologize for it.</p>
            <a href="/reviews/silent-storm-2026/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">11</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-ministry-of-ungentlemanly-warfare-2024/">The Ministry of Ungentlemanly Warfare (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
              <span class="score-badge">+9 TRAD</span>
            </div>
            <p>Guy Ritchie's WWII action film is based on a real Churchill-authorized black ops operation against Nazi supply lines in West Africa. The film celebrates competence, masculine camaraderie, and the kind of audacious mission planning that wins wars. Fun, irreverent, and thoroughly traditional in its moral framework. A great entry point for viewers who want history with their action.</p>
            <a href="/reviews/the-ministry-of-ungentlemanly-warfare-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">12</div>
          <div class="listicle-content">
            <h2><a href="/reviews/warfare-2025/">Warfare (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional-lean">TRADITIONAL LEAN</span>
              <span class="score-badge">+7 TRAD</span>
            </div>
            <p>A real-time, documentary-style depiction of a Navy SEAL operation in Ramadi that went wrong. Warfare is not a cheerleader for war -- it is an honest account of what brotherhood under fire actually looks like, based on the testimony of the men who were there. No agenda. No ideology. Just cost and loyalty. Dedicated to the real Elliott Miller, who lost his leg in the events depicted.</p>
            <a href="/reviews/warfare-2025/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>
      </ol>

      <div class="listicle-conclusion">
        <h3>Know Before You Watch</h3>
        <p>These twelve films represent what war cinema looks like when it is made with respect for the people who serve. Every film on this list was scored using the VirtueVigil Woke/Traditional methodology -- a density-based system that counts verified trope instances rather than relying on subjective impression. You can verify every score in the full reviews linked above.</p>
        <p>Browse the full VirtueVigil review library at <a href="/">virtuevigil.com</a> to find more content that aligns with your values. New reviews are added every week across film, series, and documentary -- all scored, all sourced, all available before you invest your time.</p>
      </div>

<style>
.listicle { max-width: 860px; }
.listicle-intro p { color: #bbb; line-height: 1.8; margin-bottom: 18px; font-size: 1.05rem; }
.listicle-items { list-style: none; padding: 0; margin: 0; }
.listicle-item { display: flex; gap: 20px; align-items: flex-start; padding: 28px 0; border-bottom: 1px solid rgba(255,255,255,0.07); }
.listicle-rank { min-width: 52px; height: 52px; background: rgba(201,168,76,0.15); border: 2px solid rgba(201,168,76,0.4); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; font-weight: 700; color: #c9a84c; flex-shrink: 0; }
.listicle-content h2 { font-family: 'Cinzel',Georgia,serif; font-size: 1.1rem; margin: 0 0 10px; }
.listicle-content h2 a { color: #e8e8e8; text-decoration: none; }
.listicle-content h2 a:hover { color: #c9a84c; }
.listicle-badges { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.verdict-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }
.verdict-badge.traditional { background: rgba(64,196,100,0.2); color: #40c464; border: 1px solid #40c464; }
.verdict-badge.traditional-lean { background: rgba(64,196,100,0.12); color: #60d484; border: 1px solid #60d484; }
.verdict-badge.mixed { background: rgba(212,168,67,0.15); color: #d4a843; border: 1px solid #d4a843; }
.verdict-badge.woke-lean { background: rgba(196,64,64,0.12); color: #e07060; border: 1px solid #e07060; }
.verdict-badge.woke { background: rgba(196,64,64,0.2); color: #e74c3c; border: 1px solid #e74c3c; }
.score-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; background: rgba(20,20,28,0.8); color: #a0a0a8; border: 1px solid rgba(255,255,255,0.1); }
.listicle-content p { color: #bbb; line-height: 1.7; margin-bottom: 14px; }
.listicle-cta { display: inline-block; color: #c9a84c; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(201,168,76,0.35); padding: 6px 14px; border-radius: 5px; transition: background 0.2s; }
.listicle-cta:hover { background: rgba(201,168,76,0.1); }
.listicle-conclusion { margin-top: 40px; padding: 28px; background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2); border-radius: 8px; }
.listicle-conclusion h3 { font-family: 'Cinzel',Georgia,serif; color: #c9a84c; margin: 0 0 14px; }
.listicle-conclusion p { color: #bbb; line-height: 1.75; margin-bottom: 12px; }
.listicle-conclusion a { color: #c9a84c; }
@media (max-width: 600px) { .listicle-item { flex-direction: column; } .listicle-rank { width: 42px; height: 42px; font-size: 1rem; } }
</style>
</article>`
  }));

  writePage('lists/clean-movies-for-kids-2024/index.html', buildListiclePage({
    slug: 'clean-movies-for-kids-2024',
    title: '10 Movies Your Kids Can Watch Without Worry',
    description: 'VirtueVigil scores 10 family films with low woke scores and high traditional values. Every pick is safe for kids and parent-approved by the data.',
    canonicalPath: 'lists/clean-movies-for-kids-2024',
    publishDate: '2026-03-20',
    htmlContent: `<article class="listicle-article">
      <div class="listicle-intro">
        <p>Picking a movie for family movie night should not feel like defusing a bomb. But in today's Hollywood, parents who care about what their kids absorb have to be careful. Progressive messaging, gender ideology, anti-religious subtext, and broken family structures have made their way into films aimed at children -- sometimes openly, often quietly.</p>
        <p>This list exists so you do not have to research every option from scratch. VirtueVigil scored each of these films using our Woke Score system, and every one below landed in Traditional or Strongly Traditional territory. No ideological lectures. No surprise agendas buried in the third act. Just clean entertainment your kids can watch and you can sit through without your blood pressure climbing. We ranked them from #10 to #1 based on overall family-friendliness, with woke and traditional scores factored together.</p>
      </div>

      <ol class="listicle-items">
        <li class="listicle-item">
          <div class="listicle-rank">10</div>
          <div class="listicle-content">
            <h2><a href="/reviews/paddington-in-peru-2024/">Paddington in Peru (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">TRADITIONAL LEAN</span>
              <span class="score-badge">+7 TRAD</span>
            </div>
            <p>The Paddington films have always been about the same thing: a small creature of exceptional goodness arrives in a world that is frequently unkind, and through his unfailing courtesy and genuine warmth, he makes the world a little better. Paddington in Peru takes the Brown family to South America after Aunt Lucy goes missing. The values on display -- loyalty to family, honesty, kindness toward strangers, finding courage when it counts -- are the kind parents used to be able to assume were in every children's film. Now they are a reason to put this one on the list.</p>
            <a href="/reviews/paddington-in-peru-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">9</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-lion-king-2019/">The Lion King (2019)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+23 TRAD</span>
            </div>
            <p>Disney's photorealistic remake is technically stunning and morally solid. The story has not changed: a young prince flees his responsibilities after tragedy, builds a comfortable life in exile, and is eventually called back to face the truth and take his rightful place. That is a story about duty, accountability, and honoring the legacy your parents built. The woke score of 2.7 confirms the content is clean. The traditional score of 25.34 confirms the values are real. Watch the 1994 original if you want emotional depth -- watch this if you want visual spectacle with the same solid foundation.</p>
            <a href="/reviews/the-lion-king-2019/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">8</div>
          <div class="listicle-content">
            <h2><a href="/reviews/wonka-2023/">Wonka (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">TRADITIONAL</span>
              <span class="score-badge">+12 TRAD</span>
            </div>
            <p>Wonka is the rare prequel that earns its existence. Timothee Chalamet plays a young Willy Wonka arriving with a suitcase full of magical chocolates and an unshakeable belief that hard work and genuine talent can break through a corrupt system. The film is about perseverance, loyalty, and the idea that dreams are worth pursuing even when powerful forces try to crush them. The corrupt chocolate cartel serves as the kind of institutional villain even young kids can recognize and root against. Clean, charming, and a genuine family watch with a woke score of 2.75.</p>
            <a href="/reviews/wonka-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">7</div>
          <div class="listicle-content">
            <h2><a href="/reviews/migration-2023/">Migration (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">TRADITIONAL</span>
              <span class="score-badge">+12 TRAD</span>
            </div>
            <p>Illumination's duck family adventure is built around one of the oldest family values in the playbook: a father learns that protecting his family does not mean hiding them from the world. Mack Mallard is overprotective to a fault, keeping his family on the same pond season after season while his son dreams of adventure. The journey to Jamaica forces the whole family to discover their own courage. No agenda. No lectures. A cheerful animated film with a father who loves his family and eventually learns to trust them. Woke score of 2.87 -- among the lowest of any 2023 wide release.</p>
            <a href="/reviews/migration-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">6</div>
          <div class="listicle-content">
            <h2><a href="/reviews/transformers-one-2024/">Transformers One (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">TRADITIONAL</span>
              <span class="score-badge">+16 TRAD</span>
            </div>
            <p>The best Transformers film since 1986, and one of 2024's most surprisingly solid family watches. Transformers One tells the origin of the friendship and eventual rivalry between Optimus Prime and Megatron before either became a legend. It is a story about loyalty, betrayal, and the price of idealism when it collides with hard reality -- themes that land for kids and hold up for adults. The traditional score of 18.48 reflects brotherhood, duty, and self-sacrifice woven throughout. The woke score of 2.0 is among the cleanest of any wide-release action film in 2024.</p>
            <a href="/reviews/transformers-one-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">5</div>
          <div class="listicle-content">
            <h2><a href="/reviews/dog-man-2025/">Dog Man (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">TRADITIONAL</span>
              <span class="score-badge">+19 TRAD</span>
            </div>
            <p>Take the kids. Seriously. Dog Man is 89 minutes of enthusiastic, clean chaos based on Dav Pilkey's beloved graphic novel series. The premise is wonderfully absurd: a policeman and his dog are both mortally wounded, so surgeons attach the dog's head to the officer's body. DreamWorks leaned into Pilkey's hand-drawn aesthetic in a way that feels genuinely fresh. The film's traditional score of 22.54 reflects a consistent theme of doing the right thing even when it is hard. A woke score of 3.35 is about as clean as modern animation gets in 2025.</p>
            <a href="/reviews/dog-man-2025/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">4</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-super-mario-bros-movie-2023/">The Super Mario Bros. Movie (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">TRADITIONAL</span>
              <span class="score-badge">+14 TRAD</span>
            </div>
            <p>The highest-grossing animated film of 2023 earned its $1.36 billion not through manipulation but through simple competence. Nintendo and Illumination made a film that does exactly what it promises: the world of Mario with visual energy, fan-service references, and a story built on brotherly love and perseverance. Mario's entire motivation is protecting his family and proving himself to a father who doubted him. That is not a complicated message, and it does not need to be. A woke score of 1.4 is exceptional for any modern wide release -- one of the cleanest major studio animated films in recent memory.</p>
            <a href="/reviews/the-super-mario-bros-movie-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">3</div>
          <div class="listicle-content">
            <h2><a href="/reviews/david-2025/">David (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+26 TRAD</span>
            </div>
            <p>Angel Studios proved that faith-based cinema can compete with the major studios, and they did it with a 3,000-year-old story about a shepherd kid with a sling. David is an animated biblical musical covering King David's story from his anointing by Samuel through his defeat of Goliath to his rise as Israel's king. The traditional score of 28 reflects deep themes of faith, courage, humility before God, and the idea that greatness comes to those who remain faithful when no one is watching. The film grossed $84 million on a $60.9 million budget -- proof the audience for values-driven family entertainment is real and hungry.</p>
            <a href="/reviews/david-2025/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">2</div>
          <div class="listicle-content">
            <h2><a href="/reviews/ne-zha-2-2025/">Ne Zha 2 (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+39 TRAD</span>
            </div>
            <p>One of the most extraordinary animated films made anywhere in the world in the past decade. The Chinese production is a masterpiece of scale and emotion built around themes of sacrifice, filial loyalty, destiny, and the love between a father and son. Ne Zha 2 earned a 0.0 woke score and a 38.57 traditional score -- values so deeply embedded that the numbers are not surprising once you see the content. The animation is jaw-dropping. The emotional payoff is fully earned. This film hit parents harder than their kids. Bring tissues.</p>
            <a href="/reviews/ne-zha-2-2025/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">1</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-spongebob-movie-search-for-squarepants-2025/">The SpongeBob Movie: Search for SquarePants (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+42 TRAD</span>
            </div>
            <p>The highest traditional score of any animated film we reviewed in 2025, and it is not close. The fourth SpongeBob theatrical outing delivers the kind of refreshing simplicity that has become almost exotic in modern animated filmmaking: a straightforward story about friendship and courage, a moral delivered without a lecture, and a film that does not try to be anything other than a SpongeBob movie. Mr. Krabs tells SpongeBob that being big is not about height -- it is about bravery, adventure, and moxie. A woke score of 1.28 and a traditional score of 43.1 make this the safest and most values-affirming major studio family release we reviewed in 2025. Put it on without a second thought.</p>
            <a href="/reviews/the-spongebob-movie-search-for-squarepants-2025/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>
      </ol>

      <div class="listicle-conclusion">
        <h3>How We Score Family Films</h3>
        <p>VirtueVigil uses a 0-100 Woke Score that measures the density and intensity of progressive ideological content -- gender politics, anti-religious messaging, sexual content framing, identity activism, and institutional critique. A score under 5 is essentially clean. A score above 15 starts to carry meaningful ideological load. Every film on this list scored below 4.</p>
        <p>The Traditional Score works in the opposite direction, measuring how actively the film promotes values like family loyalty, self-sacrifice, faith, duty, and personal accountability. For more scored films, browse the full <a href="/reviews/">VirtueVigil review library</a>. Every entry includes trope-by-trope breakdowns and our complete scoring methodology. You will never have to wonder what you are walking into again.</p>
      </div>

      <style>
      .listicle-article { max-width: 860px; }
      .listicle-intro p { color: #bbb; line-height: 1.75; margin-bottom: 16px; font-size: 1.05rem; }
      .listicle-items { list-style: none; padding: 0; margin: 32px 0 0; }
      .listicle-item { display: flex; gap: 20px; align-items: flex-start; padding: 28px 0; border-bottom: 1px solid rgba(255,255,255,0.07); }
      .listicle-item:last-child { border-bottom: none; }
      .listicle-rank { flex-shrink: 0; width: 52px; height: 52px; border-radius: 50%; background: rgba(201,168,76,0.12); border: 2px solid rgba(201,168,76,0.4); display: flex; align-items: center; justify-content: center; font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; font-weight: 700; color: #c9a84c; }
      .listicle-content h2 { font-family: 'Cinzel',Georgia,serif; font-size: 1.25rem; margin: 0 0 10px; }
      .listicle-content h2 a { color: #e8e8e8; text-decoration: none; }
      .listicle-content h2 a:hover { color: #c9a84c; }
      .listicle-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
      .verdict-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; }
      .verdict-badge.traditional { background: rgba(39,174,96,0.15); color: #2ecc71; border: 1px solid #2ecc71; }
      .verdict-badge.mixed { background: rgba(230,126,34,0.12); color: #e67e22; border: 1px solid #e67e22; }
      .verdict-badge.woke-lean { background: rgba(196,64,64,0.12); color: #e07060; border: 1px solid #e07060; }
      .verdict-badge.woke { background: rgba(196,64,64,0.2); color: #e74c3c; border: 1px solid #e74c3c; }
      .score-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; background: rgba(20,20,28,0.8); color: #a0a0a8; border: 1px solid rgba(255,255,255,0.1); }
      .listicle-content p { color: #bbb; line-height: 1.7; margin-bottom: 14px; }
      .listicle-cta { display: inline-block; color: #c9a84c; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(201,168,76,0.35); padding: 6px 14px; border-radius: 5px; transition: background 0.2s; }
      .listicle-cta:hover { background: rgba(201,168,76,0.1); }
      .listicle-conclusion { margin-top: 40px; padding: 28px; background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2); border-radius: 8px; }
      .listicle-conclusion h3 { font-family: 'Cinzel',Georgia,serif; color: #c9a84c; margin: 0 0 14px; }
      .listicle-conclusion p { color: #bbb; line-height: 1.75; margin-bottom: 12px; }
      .listicle-conclusion a { color: #c9a84c; }
      @media (max-width: 600px) { .listicle-item { flex-direction: column; } .listicle-rank { width: 42px; height: 42px; font-size: 1rem; } }
      </style>
    </article>`
  }));

  writePage('lists/movies-attacking-traditional-values/index.html', buildListiclePage({
    slug: 'movies-attacking-traditional-values',
    title: 'Hollywood vs. America: 10 Films That Attack Traditional Values',
    description: 'VirtueVigil\'s definitive list of the worst offenders: Hollywood films that abandon or attack traditional American values, scored by our VVWS system.',
    canonicalPath: 'lists/movies-attacking-traditional-values',
    publishDate: '2026-03-20',
    htmlContent: `<article class="listicle-article">
      <div class="listicle-intro">
        <p>Hollywood has always been ideological. What has changed is the candor. The films on this list do not merely reflect progressive values in passing. They are organized around the dismantling of specific traditional beliefs: the sanctity of marriage, the legitimacy of faith, the value of family continuity, the coherence of sex and gender, and the moral framework that most Americans outside coastal media centers still hold.</p>
        <p>This is not a list of films that happen to include progressive characters or diverse casts. Those are table stakes in modern Hollywood and not the subject here. This is a list of films where the attack on traditional values is the point, where the narrative machinery exists to make a specific argument against specific beliefs, and where the Academy, the critics, and the festival circuit rewarded them for it. Every film on this list has been reviewed in full on VirtueVigil using our Weighted Woke Score system. Every score reflects real data from the review, not editorial opinion about quality or artistic merit.</p>
        <p>The rankings run from most woke to least by VirtueVigil Score Margin. If you want the full trope-by-trope breakdown, follow the review links. These summaries are the short version of what you need to know before you or your family press play.</p>
      </div>

      <ol class="listicle-items">
        <li class="listicle-item">
          <div class="listicle-rank">1</div>
          <div class="listicle-content">
            <h2><a href="/reviews/bridgerton-s4-2026/">Bridgerton: Season 4 (2026)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-40 WOKE</span>
            </div>
            <p>Netflix rewrote a canonical white British male character as a Korean Australian woman, gender-swapped a male love interest to a Black lesbian character, and gave Benedict Bridgerton a pansexual coming-out arc framed as the season's emotional centerpiece. This is not incidental representation. It is systematic rewriting of source material to deliver contemporary progressive identity politics inside a beloved historical romance wrapper. Traditional audiences who valued the Regency setting as a frame for timeless courtship stories will find little of that here.</p>
            <a href="/reviews/bridgerton-s4-2026/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">2</div>
          <div class="listicle-content">
            <h2><a href="/reviews/conclave-2024/">Conclave (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-39 WOKE</span>
            </div>
            <p>Edward Berger's Vatican thriller spends its entire runtime discrediting Catholic tradition before delivering its climax: the newly elected Pope is revealed to be intersex, presented as a divinely ordained revelation. The film frames doctrinal certainty as "the enemy of unity," positions the arch-traditionalist cardinal as the primary villain, and builds to the conclusion that progressive reform, not orthodox faith, represents the true Church. For believers in the Catholic faith or in institutional religion broadly, this is a sustained assault framed as prestige cinema.</p>
            <a href="/reviews/conclave-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">3</div>
          <div class="listicle-content">
            <h2><a href="/reviews/poor-things-2023/">Poor Things (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-38 WOKE</span>
            </div>
            <p>Yorgos Lanthimos won four Oscars for a film whose central thesis is that female liberation is inseparable from sexual autonomy, delivered through extended graphic scenes featuring a woman with an infant's brain in an adult body. Every significant male character functions as a patriarchal controller to be escaped or discarded. The film concludes with a non-monogamous household presented as utopian feminist resolution. Traditional audiences who hold conventional views on sexual ethics, marriage, and the relationship between men and women will find this film a direct attack on those values.</p>
            <a href="/reviews/poor-things-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">4</div>
          <div class="listicle-content">
            <h2><a href="/reviews/barbie-2023/">Barbie (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-32 WOKE</span>
            </div>
            <p>Greta Gerwig sold the world a nostalgia trip and delivered a feminist manifesto that grossed $1.44 billion. The film's second and third acts are built entirely around the patriarchy as villain: Ken imports male dominance from the real world, Barbieland's matriarchal utopia is framed as paradise, and the conclusion endorses female independence from traditional domestic structures as the highest form of liberation. Parents who brought children expecting the cheerful Barbie of their own childhoods got something very different. The marketing was the trap.</p>
            <a href="/reviews/barbie-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">5</div>
          <div class="listicle-content">
            <h2><a href="/reviews/saltburn-2023/">Saltburn (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-32 WOKE</span>
            </div>
            <p>Emerald Fennell packaged a class warfare revenge fantasy in gothic British aesthetics and sold it as prestige mystery. The film's actual thesis is delivered in its triumphant climax: an outsider systematically murders an entire aristocratic family and inherits their estate. The systematic destruction of inherited family legacy is not subtext, it is the point. Ancestral wealth, family continuity, and the social structures that protect them are presented as deserving of annihilation. Traditional values around family, heritage, and social order are the targets, not the backdrop.</p>
            <a href="/reviews/saltburn-2023/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">6</div>
          <div class="listicle-content">
            <h2><a href="/reviews/heretic-2024/">Heretic (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-27 WOKE</span>
            </div>
            <p>Hugh Grant plays a soft-spoken intellectual who traps two Mormon missionaries and systematically dismantles their faith. The film is not ambiguous about its thesis: religion is an evolutionary "system of control," a con perpetrated on credulous believers. The missionaries are given no effective rebuttal. Their silence is the film's argument. Two young women of faith, portrayed sympathetically, are rendered intellectually helpless against secular skepticism. Faith communities should understand exactly what kind of argument this film is making before deciding whether to watch it.</p>
            <a href="/reviews/heretic-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">7</div>
          <div class="listicle-content">
            <h2><a href="/reviews/anora-2024/">Anora (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-26 WOKE</span>
            </div>
            <p>Sean Baker won Best Picture at the 97th Academy Awards for a film built entirely on the sympathetic normalization of sex work as morally neutral employment and the systematic dismantling of marriage as a meaningful institution. The Cinderella structure is used explicitly to be destroyed: the prince is a man-child, the marriage a legal transaction, the happy ending a refusal of conventional redemption. Traditional views on marriage, female dignity, and the moral weight of sexual choices are the values this film spends two hours undermining.</p>
            <a href="/reviews/anora-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">8</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-substance-2024/">The Substance (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-24 WOKE</span>
            </div>
            <p>Coralie Fargeat's body horror film turns the female body into a feminist battleground, using Cronenbergian excess to argue that the entertainment industry's treatment of aging women constitutes an act of violence. Every male character is a grotesque misogynist caricature: Dennis Quaid's producer is shot through a fish-eye lens that warps his face into a leering mask. The film's violence is the ideology made literal and it makes no apology for that. Conservative audiences who object to the framing of male-female professional relationships as inherently predatory will find the film relentlessly hostile to their worldview.</p>
            <a href="/reviews/the-substance-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">9</div>
          <div class="listicle-content">
            <h2><a href="/reviews/emilia-perez-2024/">Emilia Perez (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-22 WOKE</span>
            </div>
            <p>Jacques Audiard's cartel musical organized its entire narrative around a cartel boss's gender transition, presented as unambiguous liberation and moral rebirth. The male past is coded as something to be destroyed; the transition to a female identity is the film's version of salvation. It received 13 Oscar nominations, the most for any non-English-language film in Academy history. The film's core argument, that gender is a cage and transition is freedom, runs through every scene and is endorsed by the narrative at every turn.</p>
            <a href="/reviews/emilia-perez-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">10</div>
          <div class="listicle-content">
            <h2><a href="/reviews/immaculate-2024/">Immaculate (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">STRONGLY WOKE</span>
              <span class="score-badge">-21 WOKE</span>
            </div>
            <p>Sydney Sweeney produced this film specifically as a vehicle for its reproductive autonomy argument, using Catholic iconography and horror mechanics to deliver it. The convent is reimagined as an institutional conspiracy to control women's bodies in the name of faith. The male church authority is established as warmly pastoral before being revealed as predatory. The ending is the argument stated plainly: a woman destroys the institution that violated her body rather than accept her assigned role. Audiences who hold traditional Catholic or broadly pro-life views will find this film a direct and deliberate attack on those beliefs.</p>
            <a href="/reviews/immaculate-2024/" class="listicle-cta">Read Full VirtueVigil Review</a>
          </div>
        </li>
      </ol>

      <div class="listicle-conclusion">
        <h3>What This List Is Not Saying</h3>
        <p>Not all entertainment needs to reflect your values. That is a straightforward truth. Adults make choices about what they consume and why, and that agency matters. Some of the films on this list are technically accomplished. Several were made with genuine conviction by filmmakers who believe in what they are arguing. That does not make the argument easier to stomach if the argument is aimed at beliefs you hold, but it is worth acknowledging.</p>
        <p>What audiences deserve is transparency. The films on this list were often marketed in ways that obscured their ideological content, sold as spectacle when they were arguments, presented as entertainment when they were instruction. VirtueVigil exists to close that gap. Browse the full review library at <a href="https://virtuevigil.com/reviews/">virtuevigil.com/reviews/</a> to find out what any film is actually saying before you invest your time and trust in it.</p>
        <p>For full methodology on how we generate Woke Scores and Score Margins, see our <a href="/methodology.html">Methodology page</a>.</p>
      </div>

      <style>
      .listicle-article { max-width: 860px; }
      .listicle-intro p { color: #bbb; line-height: 1.75; margin-bottom: 16px; font-size: 1.05rem; }
      .listicle-items { list-style: none; padding: 0; margin: 32px 0 0; }
      .listicle-item { display: flex; gap: 20px; align-items: flex-start; padding: 28px 0; border-bottom: 1px solid rgba(255,255,255,0.07); }
      .listicle-item:last-child { border-bottom: none; }
      .listicle-rank { flex-shrink: 0; width: 52px; height: 52px; border-radius: 50%; background: rgba(201,168,76,0.12); border: 2px solid rgba(201,168,76,0.4); display: flex; align-items: center; justify-content: center; font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; font-weight: 700; color: #c9a84c; }
      .listicle-content h2 { font-family: 'Cinzel',Georgia,serif; font-size: 1.25rem; margin: 0 0 10px; }
      .listicle-content h2 a { color: #e8e8e8; text-decoration: none; }
      .listicle-content h2 a:hover { color: #c9a84c; }
      .listicle-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
      .verdict-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; }
      .verdict-badge.traditional { background: rgba(39,174,96,0.15); color: #2ecc71; border: 1px solid #2ecc71; }
      .verdict-badge.mixed { background: rgba(230,126,34,0.12); color: #e67e22; border: 1px solid #e67e22; }
      .verdict-badge.woke-lean { background: rgba(196,64,64,0.12); color: #e07060; border: 1px solid #e07060; }
      .verdict-badge.woke { background: rgba(196,64,64,0.2); color: #e74c3c; border: 1px solid #e74c3c; }
      .score-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; background: rgba(20,20,28,0.8); color: #a0a0a8; border: 1px solid rgba(255,255,255,0.1); }
      .listicle-content p { color: #bbb; line-height: 1.7; margin-bottom: 14px; }
      .listicle-cta { display: inline-block; color: #c9a84c; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(201,168,76,0.35); padding: 6px 14px; border-radius: 5px; transition: background 0.2s; }
      .listicle-cta:hover { background: rgba(201,168,76,0.1); }
      .listicle-conclusion { margin-top: 40px; padding: 28px; background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2); border-radius: 8px; }
      .listicle-conclusion h3 { font-family: 'Cinzel',Georgia,serif; color: #c9a84c; margin: 0 0 14px; }
      .listicle-conclusion p { color: #bbb; line-height: 1.75; margin-bottom: 12px; }
      .listicle-conclusion a { color: #c9a84c; }
      @media (max-width: 600px) { .listicle-item { flex-direction: column; } .listicle-rank { width: 42px; height: 42px; font-size: 1rem; } }
      </style>
    </article>`
  }));

  writePage('lists/woke-movies-box-office-flops/index.html', buildListiclePage({
    slug: 'woke-movies-box-office-flops',
    title: '10 Woke Movies That Bombed at the Box Office',
    description: 'Hollywood keeps pushing the agenda and audiences keep staying home. These 10 films scored WOKE or WOKE LEAN on VirtueVigil and confirmed it with verified box office losses.',
    canonicalPath: 'lists/woke-movies-box-office-flops',
    publishDate: '2026-03-20',
    htmlContent: `<article class="listicle-article">
      <p>The conventional wisdom in entertainment journalism holds that "go woke, go broke" is a myth. The data in this list tells a different story. Each film below earned a WOKE or WOKE LEAN verdict from VirtueVigil based on scored trope analysis, and each one underperformed or outright bombed at the verified box office. The numbers come from Box Office Mojo, Variety, The Hollywood Reporter, and other industry sources. Nothing here is estimated or invented.</p>

      <p>This is not a list of bad films. Several entries here are technically accomplished. What they share is a documented pattern: studios prioritized ideological messaging over audience satisfaction, and audiences responded by staying home. When the same pattern repeats across genres, studios, and budgets, it stops being coincidence.</p>

      <p>Rankings run from #10 to #1, ordered by a combination of woke score severity and the scale of financial underperformance. All box office figures are verified from public industry sources.</p>

      <hr>

      <ul class="listicle-items">

        <li class="listicle-item">
          <div class="listicle-rank">10</div>
          <div class="listicle-content">
            <h2><a href="/reviews/joker-folie-a-deux-2024/">Joker: Folie a Deux (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">MIXED</span>
              <span class="score-badge">-2 WOKE</span>
            </div>
            <p>VirtueVigil scored the Joker sequel with a negative margin driven by its courtroom sequences reframing Arthur Fleck as a systemic victim of societal failure, with Lady Gaga's Harley Quinn functioning as a validation figure for his grievances rather than a moral counterweight. The film grossed $206.4 million worldwide against a $200 million production budget. Variety confirmed Warner Bros. lost approximately $144 million after marketing costs were factored in, making it one of the most expensive sequel failures in box office history.</p>
            <a href="/reviews/joker-folie-a-deux-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">9</div>
          <div class="listicle-content">
            <h2><a href="/reviews/madame-web-2024/">Madame Web (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke-lean">WOKE LEAN</span>
              <span class="score-badge">-4 WOKE</span>
            </div>
            <p>VirtueVigil scored Madame Web WOKE LEAN for its female-dominated superhero framework built around a passive protagonist gaining power without meaningful sacrifice, with male characters reduced to peripheral or antagonist roles. The film grossed approximately $100 million worldwide against an $80 million production budget, and while it technically covered its production cost, it became a cultural shorthand for superhero franchise fatigue and identity-first casting. Fox Business confirmed the film as one of 2024's most high-profile misfires.</p>
            <a href="/reviews/madame-web-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">8</div>
          <div class="listicle-content">
            <h2><a href="/reviews/lightyear-2022/">Lightyear (2022)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke-lean">WOKE LEAN</span>
              <span class="score-badge">-4 WOKE</span>
            </div>
            <p>VirtueVigil flagged Lightyear for featuring a same-sex kiss that generated significant controversy and resulted in the film being banned in 14 countries, alongside identity-first messaging that distracted from its central story. Pixar's first full theatrical release in two years grossed $226.4 million worldwide against a $200 million production budget. Wikipedia and multiple analyst reports confirmed the studio lost an estimated $106 million, making it the first Pixar film widely considered a box office bomb.</p>
            <a href="/reviews/lightyear-2022/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">7</div>
          <div class="listicle-content">
            <h2><a href="/reviews/aquaman-and-the-lost-kingdom-2023/">Aquaman and the Lost Kingdom (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">WOKE</span>
              <span class="score-badge">-12 WOKE</span>
            </div>
            <p>VirtueVigil scored Aquaman and the Lost Kingdom WOKE for heavy climate change messaging woven directly into the main plot, recurring framing of traditional power structures as corrupt, and supporting characters whose authority is built on group identity rather than earned leadership. The film grossed approximately $423 million worldwide against a $205 million production budget. That number sounds adequate until measured against the original Aquaman's $1.15 billion worldwide take. The franchise dropped by more than $700 million between sequels, a collapse the studio could not hide.</p>
            <a href="/reviews/aquaman-and-the-lost-kingdom-2023/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">6</div>
          <div class="listicle-content">
            <h2><a href="/reviews/wish-2023/">Wish (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke-lean">WOKE LEAN</span>
              <span class="score-badge">-6 WOKE</span>
            </div>
            <p>Disney's centennial celebration film earned a WOKE LEAN score for its anti-authority narrative in which a young woman defies a paternalistic ruler, with systemic grievance framing replacing individual merit as the story's moral engine. Wish grossed $255 million worldwide against a reported $175 to $200 million production budget. A Reddit post citing Variety data confirmed Disney estimated total losses of approximately $131 million, extending the studio's worst sustained box office run in decades into their landmark anniversary year.</p>
            <a href="/reviews/wish-2023/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">5</div>
          <div class="listicle-content">
            <h2><a href="/reviews/eternals-2021/">Eternals (2021)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">WOKE</span>
              <span class="score-badge">-14 WOKE</span>
            </div>
            <p>VirtueVigil scored Eternals WOKE for its explicit same-sex relationship, heavy diversity-over-merit casting across a ten-character ensemble, and moral relativism substituting for the earned heroism central to the MCU formula. It became the first MCU film to receive a Rotten score on Rotten Tomatoes. Forbes reported a final worldwide gross of $402.1 million against a $200 million production budget, the fourth-lowest MCU gross at the time and well below the approximately $600 million needed to break even after marketing costs.</p>
            <a href="/reviews/eternals-2021/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">4</div>
          <div class="listicle-content">
            <h2><a href="/reviews/borderlands-2024/">Borderlands (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke-lean">WOKE LEAN</span>
              <span class="score-badge">-9 WOKE</span>
            </div>
            <p>VirtueVigil scored Borderlands WOKE LEAN for centering a female action hero within a cast built around group identity over individual competence, with authority figures consistently portrayed as corrupt and male characters sidelined or incompetent. The film ended its theatrical run with just $30.9 million worldwide against a reported $115 to $150 million budget. Kotaku called it one of 2024's biggest box office failures, a video game adaptation that managed to alienate both the game's existing fanbase and general audiences simultaneously.</p>
            <a href="/reviews/borderlands-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">3</div>
          <div class="listicle-content">
            <h2><a href="/reviews/snow-white-2025/">Snow White (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke-lean">WOKE LEAN</span>
              <span class="score-badge">-5 WOKE</span>
            </div>
            <p>VirtueVigil flagged Disney's live-action Snow White for replacing the traditional prince-and-rescue narrative with a female empowerment framework, alongside pre-release casting choices and star comments that drew sustained public backlash. The film grossed approximately $206 million worldwide against a reported $240 to $270 million production budget. World of Reel confirmed it as 2025's biggest box office bomb, with industry analysts estimating total losses exceeding $200 million when marketing costs were included.</p>
            <a href="/reviews/snow-white-2025/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">2</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-marvels-2023/">The Marvels (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">WOKE</span>
              <span class="score-badge">-14 WOKE</span>
            </div>
            <p>VirtueVigil scored The Marvels WOKE for its trio of identity-first female heroes, sustained subversion of traditional authority structures, and low-stakes personal growth arcs replacing the earned heroism the MCU was built on. The film grossed $206.1 million worldwide, confirmed by Box Office Mojo as the lowest-grossing Marvel Cinematic Universe film in history. The New York Times reported it cost roughly $300 million to make and market and opened to just $47 million domestically, the lowest MCU opening weekend ever.</p>
            <a href="/reviews/the-marvels-2023/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">1</div>
          <div class="listicle-content">
            <h2><a href="/reviews/strange-world-2022/">Strange World (2022)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">WOKE</span>
              <span class="score-badge">-15 WOKE</span>
            </div>
            <p>Disney Animation's 2022 holiday release earned a WOKE verdict from VirtueVigil for its prominent same-sex teenage relationship, messaging on chosen family identity, and a central male character whose rejection of traditional masculine roles drives the entire plot. Strange World grossed just $73.6 million worldwide, confirmed by Box Office Mojo, against a $180 million production budget and an estimated $90 million in marketing spend. Cartoon Brew reported total losses exceeding $197 million, with industry analysts naming it the single biggest box office bomb of 2022.</p>
            <a href="/reviews/strange-world-2022/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

      </ul>

      <div class="listicle-conclusion">
        <h3>The Pattern Holds</h3>
        <p>These 10 films represent hundreds of millions of dollars in confirmed studio losses. They span multiple studios, multiple genres, multiple years, and multiple budget levels. The connective tissue is not coincidence. When storytelling is subordinated to messaging, audiences notice. When the audience notices, they stay home. The studios have the receipts.</p>
        <p>VirtueVigil scores every major release using a consistent methodology. Browse the full library at <a href="https://virtuevigil.com/reviews/">virtuevigil.com/reviews/</a> to see what any film is actually saying before you spend your time and money on it. For full details on how scores are calculated, see our <a href="/methodology.html">Methodology page</a>.</p>
      </div>

      <style>
      .listicle-article { max-width: 860px; }
      .listicle-intro p { color: #bbb; line-height: 1.75; margin-bottom: 16px; font-size: 1.05rem; }
      .listicle-items { list-style: none; padding: 0; margin: 32px 0 0; }
      .listicle-item { display: flex; gap: 20px; align-items: flex-start; padding: 28px 0; border-bottom: 1px solid rgba(255,255,255,0.07); }
      .listicle-item:last-child { border-bottom: none; }
      .listicle-rank { flex-shrink: 0; width: 52px; height: 52px; border-radius: 50%; background: rgba(201,168,76,0.12); border: 2px solid rgba(201,168,76,0.4); display: flex; align-items: center; justify-content: center; font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; font-weight: 700; color: #c9a84c; }
      .listicle-content h2 { font-family: 'Cinzel',Georgia,serif; font-size: 1.25rem; margin: 0 0 10px; }
      .listicle-content h2 a { color: #e8e8e8; text-decoration: none; }
      .listicle-content h2 a:hover { color: #c9a84c; }
      .listicle-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
      .verdict-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; }
      .verdict-badge.traditional { background: rgba(39,174,96,0.15); color: #2ecc71; border: 1px solid #2ecc71; }
      .verdict-badge.mixed { background: rgba(230,126,34,0.12); color: #e67e22; border: 1px solid #e67e22; }
      .verdict-badge.woke-lean { background: rgba(196,64,64,0.12); color: #e07060; border: 1px solid #e07060; }
      .verdict-badge.woke { background: rgba(196,64,64,0.2); color: #e74c3c; border: 1px solid #e74c3c; }
      .score-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; background: rgba(20,20,28,0.8); color: #a0a0a8; border: 1px solid rgba(255,255,255,0.1); }
      .listicle-content p { color: #bbb; line-height: 1.7; margin-bottom: 14px; }
      .listicle-cta { display: inline-block; color: #c9a84c; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(201,168,76,0.35); padding: 6px 14px; border-radius: 5px; transition: background 0.2s; }
      .listicle-cta:hover { background: rgba(201,168,76,0.1); }
      .listicle-conclusion { margin-top: 40px; padding: 28px; background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2); border-radius: 8px; }
      .listicle-conclusion h3 { font-family: 'Cinzel',Georgia,serif; color: #c9a84c; margin: 0 0 14px; }
      .listicle-conclusion p { color: #bbb; line-height: 1.75; margin-bottom: 12px; }
      .listicle-conclusion a { color: #c9a84c; }
      @media (max-width: 600px) { .listicle-item { flex-direction: column; } .listicle-rank { width: 42px; height: 42px; font-size: 1rem; } }
      </style>
    </article>`
  }));

  writePage('lists/non-woke-action-movies-2024/index.html', buildListiclePage({
    slug: 'non-woke-action-movies-2024',
    title: 'Best Action Movies Without the Woke Agenda (2024)',
    description: 'Tired of woke action films? VirtueVigil scores the best non-woke action movies of 2024 so you can skip the lecture and enjoy the film.',
    canonicalPath: 'lists/non-woke-action-movies-2024',
    publishDate: '2026-03-20',
    htmlContent: `<article class="listicle-article">
      <p>Action movies used to be the one safe zone. You picked up your popcorn, the hero punched his way through the bad guys, and nobody stopped to give you a lecture about systemic inequality. That era is mostly over. Hollywood has figured out that the action genre is one of its biggest earners, and it has spent the last decade loading that genre with the same progressive messaging it puts everywhere else.</p>

      <p>Not every film in 2024 fell for it. A handful of action releases remembered that their audience came for the fight, not the politics. VirtueVigil scored every major action release of the year using our Woke-Watch Scoring System. These ten films came out on top. Low woke scores, real tradScore backing, and zero apology for being exactly what they are.</p>

      <ul class="listicle-items">

        <li class="listicle-item">
          <div class="listicle-rank">1</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-beekeeper-2024/">The Beekeeper (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">STRONGLY TRADITIONAL</span>
              <span class="score-badge">+21 TRAD</span>
            </div>
            <p>The cleanest action film of 2024, full stop. Jason Statham plays a retired operative who discovers his landlady was swindled out of her life savings by a scam operation backed by a politically connected failson. The VirtueVigil flags are almost entirely traditional: vigilante justice for the vulnerable, stoic masculinity, elder protection as a sacred duty, lone wolf competence. Woke score: 4.25. Trad score: 25.48. This is what action movies used to look like before Hollywood decided they needed a message.</p>
            <a href="/reviews/the-beekeeper-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">2</div>
          <div class="listicle-content">
            <h2><a href="/reviews/twisters-2024/">Twisters (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+15 TRAD</span>
            </div>
            <p>A tornado disaster film that is actually about tornadoes. Lee Isaac Chung directed the rare modern blockbuster that feels built for the whole country, not just the coasts. Glen Powell plays a cowboy storm chaser who earns the film's moral center through competence and courage, not ideology. VirtueVigil scored it a 10.08 woke, 24.64 trad. Heartland communities are shown with dignity. Climate change messaging is notably absent. This is the crowd-pleaser of 2024.</p>
            <a href="/reviews/twisters-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">3</div>
          <div class="listicle-content">
            <h2><a href="/reviews/gladiator-ii-2024/">Gladiator II (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+16 TRAD</span>
            </div>
            <p>Ridley Scott returned to the Colosseum and delivered a sequel built around personal honor, martial virtue, and the cost of betraying your own values. Paul Mescal carries a franchise-scale action film. Denzel Washington is having enormous fun as the villain. VirtueVigil flagged personal honor as a supreme value, institutional rot as the primary antagonist, and zero progressive moralizing in the central conflict. Woke score: 7. Trad score: 22.84. A clean win for classical action storytelling.</p>
            <a href="/reviews/gladiator-ii-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">4</div>
          <div class="listicle-content">
            <h2><a href="/reviews/road-house-2024/">Road House (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+14 TRAD</span>
            </div>
            <p>Nobody expected the Road House remake to land as a masculinity-affirming action film. Jake Gyllenhaal plays a former UFC fighter who takes a bouncer job at a Florida Keys bar and ends up defending a community against organized crime. The VirtueVigil trope audit flagged masculine competence as the heroic core, community defense, consequence culture with villains getting punished, and redemption through service. Woke score: 4. Trad score: 18. Exactly what a genre film should be.</p>
            <a href="/reviews/road-house-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">5</div>
          <div class="listicle-content">
            <h2><a href="/reviews/furiosa-a-mad-max-saga-2024/">Furiosa: A Mad Max Saga (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+14 TRAD</span>
            </div>
            <p>The internet spent months calling this film woke. The VirtueVigil data says otherwise. Anya Taylor-Joy plays a woman kidnapped as a child who spends the entire film trying to get back home, driven by family loyalty and pure survival instinct. George Miller earns his traditional score through family and home as the ultimate motivation, male villains who face real consequences, and a protagonist who earns everything through suffering, not ideology. Woke score: 8. Trad score: 22. Judge this one on the data.</p>
            <a href="/reviews/furiosa-a-mad-max-saga-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">6</div>
          <div class="listicle-content">
            <h2><a href="/reviews/transformers-one-2024/">Transformers One (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+16 TRAD</span>
            </div>
            <p>The best Transformers film since the 1986 animated original, and it got there by taking the Optimus Prime and Megatron friendship seriously as a genuine tragedy. The VirtueVigil flags are almost entirely traditional: sacred male friendship, heroic self-sacrifice, clear good versus evil, hard work and earned excellence. Woke score: 2. Trad score: 18.48. No identity politics in sight. Franchise filmmaking that respects its characters and its audience.</p>
            <a href="/reviews/transformers-one-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">7</div>
          <div class="listicle-content">
            <h2><a href="/reviews/beverly-hills-cop-axel-f-2024/">Beverly Hills Cop: Axel F (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+11 TRAD</span>
            </div>
            <p>The fourth Beverly Hills Cop delivers exactly what it promises: Eddie Murphy back in the role, old-school cop competence beating bureaucracy, loyalty between friends, and a villain who gets punished. VirtueVigil flagged father-daughter reconciliation as the emotional spine, old-school competence over institutional procedure, and male friendship and loyalty throughout. Woke score: 4. Trad score: 15. Nostalgia done right, without a political detour in sight.</p>
            <a href="/reviews/beverly-hills-cop-axel-f-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">8</div>
          <div class="listicle-content">
            <h2><a href="/reviews/sonic-the-hedgehog-3-2024/">Sonic the Hedgehog 3 (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+14 TRAD</span>
            </div>
            <p>The best installment in the Sonic franchise gets darker without losing its values. Keanu Reeves voices Shadow the Hedgehog in a storyline about grief, government overreach, and redemption through truth. VirtueVigil flags include chosen family earned through loyalty, grief treated with dignity, sacrifice for others as the highest good, and government overreach as the villain. Woke score: 4.2. Trad score: 18.34. Safe for families and genuinely good for everyone else.</p>
            <a href="/reviews/sonic-the-hedgehog-3-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">9</div>
          <div class="listicle-content">
            <h2><a href="/reviews/venom-the-last-dance-2024/">Venom: The Last Dance (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL</span>
              <span class="score-badge">+14 TRAD</span>
            </div>
            <p>Tom Hardy's three-film commitment to this bizarre character pays off in a finale that knows exactly what it is. The VirtueVigil trope audit found loyalty as the ultimate virtue, sacrifice for others as the highest good, redemption of a former adversary, and individual courage over institutional cowardice. Woke score: 3.5. Trad score: 17.07. Hardy's Eddie and Venom remain one of the most charming odd-couple pairings in franchise history, and the film closes it cleanly.</p>
            <a href="/reviews/venom-the-last-dance-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">10</div>
          <div class="listicle-content">
            <h2><a href="/reviews/godzilla-x-kong-the-new-empire-2024/">Godzilla x Kong: The New Empire (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
              <span class="score-badge">+8 TRAD</span>
            </div>
            <p>A radioactive dinosaur and a giant ape team up to defeat an evil primate overlord. That is the entire movie and it delivers completely. VirtueVigil noted a throwaway line about indigenous cultures that passes in seconds with no bearing on the plot. The rest of the film is pure spectacle: tyranny versus freedom as the universal conflict, adoptive family bonds, monsters fighting monsters. Woke score: 6. Trad score: 14. If you came for action and nothing else, this film will not disappoint.</p>
            <a href="/reviews/godzilla-x-kong-the-new-empire-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

      </ul>

      <div class="listicle-conclusion">
        <h3>Clean Action Still Exists</h3>
        <p>Hollywood made it harder to find clean action films in 2024, but they still exist. These ten films scored Traditional or better on the VirtueVigil scale, with woke scores low enough that you can sit down and watch without waiting for the lecture. From The Beekeeper to Godzilla x Kong, 2024 had options. You just had to know where to look.</p>
        <p>Browse the full VirtueVigil library at <a href="https://virtuevigil.com/reviews/">virtuevigil.com/reviews/</a> and filter by verdict to find more films worth your time. For full details on how we score, see our <a href="/methodology.html">Methodology page</a>.</p>
      </div>

      <style>
      .listicle-article { max-width: 860px; }
      .listicle-intro p { color: #bbb; line-height: 1.75; margin-bottom: 16px; font-size: 1.05rem; }
      .listicle-items { list-style: none; padding: 0; margin: 32px 0 0; }
      .listicle-item { display: flex; gap: 20px; align-items: flex-start; padding: 28px 0; border-bottom: 1px solid rgba(255,255,255,0.07); }
      .listicle-item:last-child { border-bottom: none; }
      .listicle-rank { flex-shrink: 0; width: 52px; height: 52px; border-radius: 50%; background: rgba(201,168,76,0.12); border: 2px solid rgba(201,168,76,0.4); display: flex; align-items: center; justify-content: center; font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; font-weight: 700; color: #c9a84c; }
      .listicle-content h2 { font-family: 'Cinzel',Georgia,serif; font-size: 1.25rem; margin: 0 0 10px; }
      .listicle-content h2 a { color: #e8e8e8; text-decoration: none; }
      .listicle-content h2 a:hover { color: #c9a84c; }
      .listicle-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
      .verdict-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; }
      .verdict-badge.traditional { background: rgba(39,174,96,0.15); color: #2ecc71; border: 1px solid #2ecc71; }
      .verdict-badge.mixed { background: rgba(230,126,34,0.12); color: #e67e22; border: 1px solid #e67e22; }
      .verdict-badge.woke-lean { background: rgba(196,64,64,0.12); color: #e07060; border: 1px solid #e07060; }
      .verdict-badge.woke { background: rgba(196,64,64,0.2); color: #e74c3c; border: 1px solid #e74c3c; }
      .score-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; background: rgba(20,20,28,0.8); color: #a0a0a8; border: 1px solid rgba(255,255,255,0.1); }
      .listicle-content p { color: #bbb; line-height: 1.7; margin-bottom: 14px; }
      .listicle-cta { display: inline-block; color: #c9a84c; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(201,168,76,0.35); padding: 6px 14px; border-radius: 5px; transition: background 0.2s; }
      .listicle-cta:hover { background: rgba(201,168,76,0.1); }
      .listicle-conclusion { margin-top: 40px; padding: 28px; background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2); border-radius: 8px; }
      .listicle-conclusion h3 { font-family: 'Cinzel',Georgia,serif; color: #c9a84c; margin: 0 0 14px; }
      .listicle-conclusion p { color: #bbb; line-height: 1.75; margin-bottom: 12px; }
      .listicle-conclusion a { color: #c9a84c; }
      @media (max-width: 600px) { .listicle-item { flex-direction: column; } .listicle-rank { width: 42px; height: 42px; font-size: 1rem; } }
      </style>
    </article>`
  }));

  writePage('lists/a24-movies-woke-ranking/index.html', buildListiclePage({
    slug: 'a24-movies-woke-ranking',
    title: 'Every A24 Movie Ranked by Woke Score (VirtueVigil Analysis)',
    description: 'A24 films ranked by their VirtueVigil woke score. Find out which A24 movies are safe to watch and which push a woke agenda.',
    canonicalPath: 'lists/a24-movies-woke-ranking',
    publishDate: '2026-03-21',
    htmlContent: `<article class="listicle-article">
      <p>A24 is the most acclaimed indie studio in Hollywood right now. Critics love it. Awards voters love it. The studio has collected more Oscar nominations per film than any distributor of its size in recent memory. It also has one of the most consistent ideological profiles in the business. That consistency is what this list is about.</p>

      <p>VirtueVigil has now reviewed 13 A24 films using our Woke-Watch Scoring System. The data tells a clear story. A24 is not a monolith. The studio produces everything from warrior-class war films with zero woke content to prestige dramas with explicit progressive framing. But the average leans left, the most celebrated releases tend to skew woke, and the studio's brand identity is built partly on a willingness to greenlight content that mainstream studios avoid. That is not a guess. That is what the numbers say.</p>

      <p>Below, every A24 film in our database is ranked from most woke to least woke. The ranking is based on score margin: the difference between woke score and traditional score. Films with a negative margin lean woke. Films with a positive margin lean traditional. Each entry draws directly from our full review data. No fabricated scores, no guesswork.</p>

      <hr>

      <ul class="listicle-items">

        <li class="listicle-item">
          <div class="listicle-rank">1</div>
          <div class="listicle-content">
            <h2><a href="/reviews/babygirl-2024/">Babygirl (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">WOKE</span>
              <span class="score-badge">-15 WOKE</span>
            </div>
            <p>Nicole Kidman plays a CEO who pursues a sexual submissive relationship with a 25-year-old intern, and the film treats this as self-discovery rather than a crisis. The woke score of 19.22 against a trad score of just 4.4 makes Babygirl the most ideologically progressive film in our A24 database. Director Halina Reijn builds an entire worldview around female sexual autonomy untethered from marriage or consequence, with the husband (Antonio Banderas) rendered sympathetic but irrelevant. A well-made film. Not a traditional one.</p>
            <a href="/reviews/babygirl-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">2</div>
          <div class="listicle-content">
            <h2><a href="/reviews/queer-2024/">Queer (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke">WOKE</span>
              <span class="score-badge">-13 WOKE</span>
            </div>
            <p>Luca Guadagnino adapts William S. Burroughs' autobiographical novella about obsessive queer love in 1950s Mexico City, and Daniel Craig delivers the best performance of his career in a film that probably should not work as well as it does. The woke score of 17.5 against a trad score of 4.2 puts this firmly in WOKE territory. The film's explicit gay relationship, drug use framed as consciousness expansion, and rejection of conventional moral frameworks are central, not incidental. The craft is extraordinary. The ideology is just as deliberate.</p>
            <a href="/reviews/queer-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">3</div>
          <div class="listicle-content">
            <h2><a href="/reviews/civil-war-2024/">Civil War (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke-lean">WOKE LEAN</span>
              <span class="score-badge">-4 WOKE</span>
            </div>
            <p>Alex Garland's dystopian war film set a culture-war debate in motion when it dropped in April 2024 as one of A24's biggest box office hits ever. The woke score of 22 reflects real content: both sides in the fictional civil war are deliberately left undefined, which conservatives read as moral equivalence and progressives read as a critique of fascism. Our review flags this as a Significant Woke Trap. The traditional score of 18 keeps it from tipping further, driven by journalistic neutrality as a virtue and real consequences for violence. Where you land on this film depends on which ambiguity you find more troubling.</p>
            <a href="/reviews/civil-war-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">4</div>
          <div class="listicle-content">
            <h2><a href="/reviews/if-i-had-legs-id-kick-you-2025/">If I Had Legs I'd Kick You (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke-lean">WOKE LEAN</span>
              <span class="score-badge">-4 WOKE</span>
            </div>
            <p>Rose Byrne plays a psychotherapist whose own life is collapsing under the weight of a sick child, a failing marriage, and a vanishing support system. It is one of the rawest performances in recent memory, and the film earns its score margin of -4 through genuine complexity rather than simple advocacy. The woke score of 15.14 comes from how the film deconstructs motherhood without offering a faith-based or redemptive framework, and how abortion guilt is treated as a character detail rather than a moral crisis. The trad score of 11.42 reflects the film's authentic treatment of parental sacrifice and its refusal to let Linda off the hook.</p>
            <a href="/reviews/if-i-had-legs-id-kick-you-2025/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">5</div>
          <div class="listicle-content">
            <h2><a href="/reviews/the-brutalist-2024/">The Brutalist (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge woke-lean">WOKE LEAN</span>
              <span class="score-badge">-3 WOKE</span>
            </div>
            <p>Brady Corbet's three-and-a-half-hour epic follows a Hungarian Jewish architect who survives the Holocaust and arrives in postwar America, only to discover that the country's promise of freedom masks its own forms of exploitation. The film is the most explicitly anti-capitalist A24 release in our database, treating America as a beautiful trap that destroys the artists it claims to celebrate. Adrien Brody won the Oscar for Best Actor. The woke score of 9 and trad score of 6 land it at -3 WOKE. A demanding film made with enormous craft. Its thesis about America is not flattering.</p>
            <a href="/reviews/the-brutalist-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">6</div>
          <div class="listicle-content">
            <h2><a href="/reviews/everything-everywhere-all-at-once-2022/">Everything Everywhere All at Once (2022)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">MIXED</span>
              <span class="score-badge">+1 TRAD</span>
            </div>
            <p>Seven Academy Awards. $77 million on a $14 million budget. And the most ideologically difficult film to categorize in A24's library. The Daniels built a multiverse action comedy where the emotional core is simultaneously a lesbian relationship and a marriage worth saving. The woke score of 15.34 and trad score of 16.32 produce the thinnest MIXED verdict in our database. A middle-aged Chinese immigrant fighting multiverse nihilism to save her family earns the traditional points. Her daughter's queer identity as the moral center of the film earns the woke points. Both are central. Neither can be edited out. VirtueVigil calls this one genuinely, rigorously mixed.</p>
            <a href="/reviews/everything-everywhere-all-at-once-2022/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">7</div>
          <div class="listicle-content">
            <h2><a href="/reviews/undertone-2026/">undertone (2026)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">MIXED</span>
              <span class="score-badge">+1 TRAD</span>
            </div>
            <p>Ian Tuason's A24 horror film follows a paranormal podcast host who moves home to care for her comatose mother and starts hearing something deeply wrong in audio files sent by a troubled couple. It is the horror film equivalent of a room with bad acoustics: you cannot locate the source of the wrongness, and that is the point. The woke score of 5 and trad score of 6 land it at +1 TRAD, making it one of the more ideologically neutral A24 releases in our database. The fear here is existential, not political.</p>
            <a href="/reviews/undertone-2026/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">8</div>
          <div class="listicle-content">
            <h2><a href="/reviews/eternity/">Eternity (2026)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">MIXED</span>
              <span class="score-badge">+2 TRAD</span>
            </div>
            <p>A24 and Apple Original Films co-produced this high-concept romantic comedy where newly deceased souls have one week to choose which themed paradise they will inhabit forever. Elizabeth Olsen, Miles Teller, and Callum Turner form a love triangle that stretches across life and death. The woke score of 3 and trad score of 5 land at +2 TRAD, making this one of A24's lighter ideological footprints. The film's premise is inherently about what you value most when everything else is stripped away, and the answer it gives is surprisingly traditional: love, commitment, choosing the harder thing.</p>
            <a href="/reviews/eternity/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">9</div>
          <div class="listicle-content">
            <h2><a href="/reviews/past-lives-2023/">Past Lives (2023)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge mixed">MIXED</span>
              <span class="score-badge">+2 TRAD</span>
            </div>
            <p>Celine Song's debut feature is about what you give up when you choose to become someone. A childhood romance between two Koreans is interrupted when the girl's family immigrates to Canada. Twelve years later they reconnect. Twelve years after that, he visits her in New York where she is now married to an American man. The film is quiet, devastating, and almost defiantly apolitical. The woke score of 5.6 and trad score of 7.35 land at +2 TRAD. The marriage is treated with genuine weight. The Korean-American immigrant experience is handled without political framing. Song became the first Asian woman nominated for Best Director. The film deserves that recognition.</p>
            <a href="/reviews/past-lives-2023/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">10</div>
          <div class="listicle-content">
            <h2><a href="/reviews/marty-supreme-2025/">Marty Supreme (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
              <span class="score-badge">+3 TRAD</span>
            </div>
            <p>Josh Safdie's ping pong film is not the underdog sports triumph the marketing implied. It is a portrait of a man consuming himself alive in pursuit of a dream the world has decided does not matter. Timothee Chalamet plays Marty Mauser, a ping pong hustler in 1970s New York whose obsession is both his gift and his destruction. The woke score of 4 and trad score of 7 land at +3 TRAD. The film earns traditional points for its treatment of obsession disconnected from community as a form of self-destruction. Safdie's chaotic energy is admired but hard to sit with. That discomfort is the whole point.</p>
            <a href="/reviews/marty-supreme-2025/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">11</div>
          <div class="listicle-content">
            <h2><a href="/reviews/materialists-2025/">Materialists (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
              <span class="score-badge">+5 TRAD</span>
            </div>
            <p>Celine Song's follow-up to Past Lives is a sophisticated New York romantic comedy where a high-end matchmaker discovers her systematic approach to love may not apply to her own heart. Dakota Johnson, Chris Evans, and Pedro Pascal form a love triangle the film resolves with a sincere marriage proposal and a traditional ending. The woke score of 9.18 and trad score of 13.7 land at +5 TRAD. An A24 romantic comedy that ends at the altar is worth noting. Chris Evans delivers his best non-Marvel performance. The film's moral compass points where it sounds like it should not.</p>
            <a href="/reviews/materialists-2025/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">12</div>
          <div class="listicle-content">
            <h2><a href="/reviews/we-live-in-time-2024/">We Live in Time (2024)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
              <span class="score-badge">+5 TRAD</span>
            </div>
            <p>Florence Pugh and Andrew Garfield build one of the most genuinely affecting screen romances in recent memory in this non-linear love story structured around terminal illness. The woke score of 8.8 and trad score of 13.44 land at +5 TRAD. The film earns its traditional score through the centrality of marriage, the weight it gives to the partnership being dismantled by cancer, and the absence of any progressive moralizing. It will make you cry. Whether it should is a more interesting question, but the traditional content is real and it is the film's emotional core.</p>
            <a href="/reviews/we-live-in-time-2024/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

        <li class="listicle-item">
          <div class="listicle-rank">13</div>
          <div class="listicle-content">
            <h2><a href="/reviews/warfare-2025/">Warfare (2025)</a></h2>
            <div class="listicle-badges">
              <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
              <span class="score-badge">+7 TRAD</span>
            </div>
            <p>Alex Garland and Ray Mendoza's real-time depiction of a 2006 Navy SEAL operation in Ramadi, Iraq is the cleanest film in A24's catalog by our scoring. Woke score: 2. Trad score: 9. Score margin: +7 TRAD. This is not entertainment in the conventional sense. It is testimony, built from the first-hand accounts of the men who were there, dedicated to Elliott Miller, the real SEAL who lost his leg and his ability to speak during the events depicted. There is no political framing, no ideological commentary, no lesson about the war. Just eleven men in a house in Ramadi with incoming fire and each other. A24 distributed it. That took some guts.</p>
            <a href="/reviews/warfare-2025/" class="listicle-cta">Read the VirtueVigil review</a>
          </div>
        </li>

      </ul>

      <div class="listicle-conclusion">
        <h3>What the Data Says About A24</h3>
        <p>Thirteen films reviewed. Five lean traditional. Four lean woke. Four are mixed. That is not the studio profile that A24's reputation suggests, but the picture is more complicated than the headline number. The most celebrated A24 releases, the ones that win Oscars and get written about in major publications, tend to cluster in the woke or woke-lean categories. Babygirl, Queer, The Brutalist, Everything Everywhere All at Once: these are the films that define A24's cultural identity. Warfare and Materialists exist in the same catalog, but they are not the films the studio markets as its identity.</p>
        <p>The honest read: A24 is a studio with genuine range and a genuine ideological tilt. It will greenlight a zero-woke war film and a lesbian coming-of-age film and a submission-fantasy Nicole Kidman drama in the same year without blinking. The throughline is not ideology. It is craft and controversy. Whatever gets talked about, A24 will make it. And right now, what gets talked about skews left. Browse every A24 review and every film in our database at <a href="https://virtuevigil.com/reviews/">virtuevigil.com/reviews/</a>.</p>
      </div>

      <style>
      .listicle-article { max-width: 860px; }
      .listicle-intro p { color: #bbb; line-height: 1.75; margin-bottom: 16px; font-size: 1.05rem; }
      .listicle-items { list-style: none; padding: 0; margin: 32px 0 0; }
      .listicle-item { display: flex; gap: 20px; align-items: flex-start; padding: 28px 0; border-bottom: 1px solid rgba(255,255,255,0.07); }
      .listicle-item:last-child { border-bottom: none; }
      .listicle-rank { flex-shrink: 0; width: 52px; height: 52px; border-radius: 50%; background: rgba(201,168,76,0.12); border: 2px solid rgba(201,168,76,0.4); display: flex; align-items: center; justify-content: center; font-family: 'Cinzel',Georgia,serif; font-size: 1.2rem; font-weight: 700; color: #c9a84c; }
      .listicle-content h2 { font-family: 'Cinzel',Georgia,serif; font-size: 1.25rem; margin: 0 0 10px; }
      .listicle-content h2 a { color: #e8e8e8; text-decoration: none; }
      .listicle-content h2 a:hover { color: #c9a84c; }
      .listicle-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
      .verdict-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; }
      .verdict-badge.traditional { background: rgba(39,174,96,0.15); color: #2ecc71; border: 1px solid #2ecc71; }
      .verdict-badge.mixed { background: rgba(230,126,34,0.12); color: #e67e22; border: 1px solid #e67e22; }
      .verdict-badge.woke-lean { background: rgba(196,64,64,0.12); color: #e07060; border: 1px solid #e07060; }
      .verdict-badge.woke { background: rgba(196,64,64,0.2); color: #e74c3c; border: 1px solid #e74c3c; }
      .score-badge { display: inline-block; padding: 3px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: 700; background: rgba(20,20,28,0.8); color: #a0a0a8; border: 1px solid rgba(255,255,255,0.1); }
      .listicle-content p { color: #bbb; line-height: 1.7; margin-bottom: 14px; }
      .listicle-cta { display: inline-block; color: #c9a84c; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(201,168,76,0.35); padding: 6px 14px; border-radius: 5px; transition: background 0.2s; }
      .listicle-cta:hover { background: rgba(201,168,76,0.1); }
      .listicle-conclusion { margin-top: 40px; padding: 28px; background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2); border-radius: 8px; }
      .listicle-conclusion h3 { font-family: 'Cinzel',Georgia,serif; color: #c9a84c; margin: 0 0 14px; }
      .listicle-conclusion p { color: #bbb; line-height: 1.75; margin-bottom: 12px; }
      .listicle-conclusion a { color: #c9a84c; }
      @media (max-width: 600px) { .listicle-item { flex-direction: column; } .listicle-rank { width: 42px; height: 42px; font-size: 1rem; } }
      </style>
    </article>`
  }));

  writePage('lists/netflix-woke-movies-2024-data/index.html', buildListiclePage({
    slug: 'netflix-woke-movies-2024-data',
    title: 'Is Netflix Getting More Woke? The Data (28 Titles Scored)',
    description: 'VirtueVigil scored every Netflix title in our database. Here is what the numbers say about whether Netflix is getting more woke.',
    canonicalPath: 'lists/netflix-woke-movies-2024-data',
    publishDate: '2026-03-21',
    htmlContent: `<article class="listicle-article">
      <style>
        .netflix-score-bar { display:flex; align-items:center; gap:10px; margin:6px 0; }
        .netflix-score-label { font-size:0.75rem; color:#a0a0a8; width:56px; flex-shrink:0; }
        .netflix-bar-track { flex:1; background:#1e1e2a; border-radius:4px; height:8px; overflow:hidden; }
        .netflix-bar-fill { height:8px; border-radius:4px; }
        .netflix-bar-woke { background:#c44040; }
        .netflix-bar-trad { background:#2ecc71; }
        .netflix-verdict { display:inline-block; padding:3px 10px; border-radius:5px; font-size:0.72rem; font-weight:700; }
        .netflix-verdict.woke { background:rgba(196,64,64,0.15); color:#c44040; border:1px solid rgba(196,64,64,0.4); }
        .netflix-verdict.trad { background:rgba(46,204,113,0.15); color:#2ecc71; border:1px solid rgba(46,204,113,0.4); }
        .netflix-verdict.mixed { background:rgba(212,168,67,0.12); color:#d4a843; border:1px solid rgba(212,168,67,0.3); }
        .netflix-verdict.strongly-woke { background:rgba(196,64,64,0.25); color:#ff6060; border:1px solid rgba(196,64,64,0.6); }
        .netflix-verdict.strongly-trad { background:rgba(46,204,113,0.25); color:#50ff90; border:1px solid rgba(46,204,113,0.6); }
        .data-stat-row { display:flex; gap:20px; flex-wrap:wrap; margin:24px 0; }
        .data-stat { background:#14141c; border:1px solid rgba(201,168,76,0.2); border-radius:8px; padding:18px 22px; flex:1; min-width:120px; text-align:center; }
        .data-stat .num { font-size:2rem; font-weight:700; color:#c9a84c; font-family:'Cinzel',Georgia,serif; }
        .data-stat .lbl { font-size:0.72rem; color:#a0a0a8; text-transform:uppercase; letter-spacing:0.06em; margin-top:4px; }
        .listicle-item-netflix { display:flex; gap:18px; align-items:flex-start; background:#13131e; border:1px solid rgba(201,168,76,0.12); border-radius:10px; padding:20px; margin-bottom:18px; }
        .listicle-rank-n { min-width:40px; height:40px; border-radius:50%; background:rgba(201,168,76,0.12); display:flex; align-items:center; justify-content:center; font-family:'Cinzel',Georgia,serif; font-weight:700; color:#c9a84c; font-size:0.9rem; flex-shrink:0; margin-top:2px; }
        .listicle-body-n { flex:1; min-width:0; }
        .listicle-title-n { font-size:1.05rem; font-weight:700; color:#e8e6e1; margin:0 0 6px; }
        .listicle-meta-n { font-size:0.78rem; color:#a0a0a8; margin:0 0 10px; }
        .listicle-summary-n { font-size:0.9rem; color:#ccc; line-height:1.6; margin:10px 0; }
        .listicle-link-n { font-size:0.85rem; font-weight:600; color:#c9a84c; text-decoration:none; }
        .listicle-link-n:hover { text-decoration:underline; }
        .trend-section { background:rgba(201,168,76,0.06); border:1px solid rgba(201,168,76,0.2); border-radius:10px; padding:22px 26px; margin:28px 0; }
        .trend-section h3 { color:#c9a84c; font-family:'Cinzel',Georgia,serif; font-size:1.1rem; margin:0 0 12px; }
      </style>

      <p>The question conservatives ask constantly: is Netflix getting worse? Are they pushing more progressive content, or is the platform actually more balanced than it looks? VirtueVigil scored every Netflix title in our review database using the same methodology we apply to every film and series. Here is what the data says.</p>

      <p>We reviewed 28 Netflix titles spanning 2021 through 2026. Each received a Woke Score, a Traditional Score, and a final verdict. The results are more complicated than the culture war narrative on either side suggests.</p>

      <div class="data-stat-row">
        <div class="data-stat"><div class="num">28</div><div class="lbl">Netflix Titles Reviewed</div></div>
        <div class="data-stat"><div class="num">10</div><div class="lbl">Woke / Lean Woke</div></div>
        <div class="data-stat"><div class="num">13</div><div class="lbl">Traditional / Lean Trad</div></div>
        <div class="data-stat"><div class="num">5</div><div class="lbl">Mixed / Neutral</div></div>
      </div>

      <p>The headline finding: <strong>Netflix's catalog is not uniformly woke.</strong> The platform that gave us Bridgerton Season 4 (Woke Score: 58) also gave us Nonnas (Woke Score: 1), Peaky Blinders: The Immortal Man (Woke Score: 5), and War Machine (Woke Score: 4). The ideological range is enormous. What Netflix is doing is segmenting its audience by taste and ideology simultaneously, serving progressive content to progressive viewers and conventional content to everyone else. The question is whether the prestige programming, the stuff critics celebrate and award bodies notice, skews harder left. Our data suggests yes.</p>

      <div class="trend-section">
        <h3>Key Finding: The Prestige Problem</h3>
        <p>Netflix's most-talked-about titles skew woke. Emilia Perez (Woke Score: 28), Adolescence (Woke Score: 22.54), and Bridgerton Season 4 (Woke Score: 58) dominate the conversation. The bread-and-butter action and legacy content, from Beverly Hills Cop: Axel F to Peaky Blinders to Nobody 2, scores consistently traditional. Netflix appears to use conventional entertainment to retain subscribers while reserving progressive messaging for the titles it wants awards and cultural credit for.</p>
      </div>

      <hr>

      <h2>The Most Woke Netflix Titles (Ranked)</h2>
      <p>Here are the 10 titles that scored highest on our Woke Score, ranked from most to least ideologically progressive.</p>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#1</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/bridgerton-s4-2026/" style="color:#e8e6e1;text-decoration:none;">Bridgerton: Season 4 (2026)</a> <span class="netflix-verdict strongly-woke">STRONGLY WOKE</span></div>
          <div class="listicle-meta-n">Woke Score: 58 &bull; Traditional Score: 18 &bull; Margin: -40 WOKE &bull; Type: Series</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:58%;"></div></div><span style="font-size:0.75rem;color:#c44040;">58</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:18%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">18</span></div>
          <div class="listicle-summary-n">Bridgerton's fourth season is Netflix's most ideologically aggressive prestige production in our database. The series abandons even the pretense of Regency romance conventions to deliver a fully progressive messaging package: deconstructed masculinity, consent framework dialogue embedded into courtship scenes, identity-first character framing, and the systematic dismantling of traditional romantic roles. The 40-point woke margin is the largest gap of any Netflix title we reviewed. Families who enjoyed earlier seasons should know this is a different product ideologically.</div>
          <a href="/reviews/bridgerton-s4-2026/" class="listicle-link-n">Read the full VirtueVigil review of Bridgerton Season 4 <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#2</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/emilia-perez-2024/" style="color:#e8e6e1;text-decoration:none;">Emilia Perez (2024)</a> <span class="netflix-verdict strongly-woke">STRONGLY WOKE</span></div>
          <div class="listicle-meta-n">Woke Score: 28 &bull; Traditional Score: 6 &bull; Margin: -22 WOKE &bull; Type: Film</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:28%;"></div></div><span style="font-size:0.75rem;color:#c44040;">28</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:6%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">6</span></div>
          <div class="listicle-summary-n">Netflix acquired Jacques Audiard's Spanish-language cartel musical after it swept Cannes and accumulated 13 Oscar nominations. The film centers on a cartel boss who transitions gender identities and reframes the transformation as moral liberation. The criminal past is coded as a male identity to be shed; the post-transition life is presented as spiritual rebirth. Identity politics and cartel violence make for a jarring combination, and the film managed to unite progressive and conservative critics against it for entirely different reasons. Netflix bet big on awards prestige and got it.</div>
          <a href="/reviews/emilia-perez-2024/" class="listicle-link-n">Read the full VirtueVigil review of Emilia Perez <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#3</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/kpop-demon-hunters-2025/" style="color:#e8e6e1;text-decoration:none;">KPop Demon Hunters (2025)</a> <span class="netflix-verdict woke">WOKE LEAN</span></div>
          <div class="listicle-meta-n">Woke Score: 24.18 &bull; Traditional Score: 16.42 &bull; Margin: -8 WOKE &bull; Type: Film</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:24%;"></div></div><span style="font-size:0.75rem;color:#c44040;">24.18</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:16%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">16.42</span></div>
          <div class="listicle-summary-n">Netflix's animated film blending K-pop and supernatural action carries consistent progressive messaging around identity, female authority, and nonconformity as power. The woke elements are embedded in the genre trappings rather than announced outright, which means families watching it as entertainment are absorbing ideological content alongside the action sequences. The trad score is not negligible, but the woke margin holds throughout.</div>
          <a href="/reviews/kpop-demon-hunters-2025/" class="listicle-link-n">Read the full VirtueVigil review of KPop Demon Hunters <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#4</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/adolescence-2025/" style="color:#e8e6e1;text-decoration:none;">Adolescence (2025)</a> <span class="netflix-verdict woke">WOKE LEAN</span></div>
          <div class="listicle-meta-n">Woke Score: 22.54 &bull; Traditional Score: 14.76 &bull; Margin: -8 WOKE &bull; Type: Series</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:22%;"></div></div><span style="font-size:0.75rem;color:#c44040;">22.54</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:14%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">14.76</span></div>
          <div class="listicle-summary-n">The one-take British drama about a 13-year-old accused of murdering a classmate became Netflix's most-discussed prestige title of 2025. The series frames male violence through a lens of social conditioning and online radicalization rather than individual moral failure, which aligns with progressive frameworks around accountability and systemic causation. The storytelling is technically extraordinary. The ideological framing consistently attributes harmful behavior to patriarchal and digital systems rather than personal choices.</div>
          <a href="/reviews/adolescence-2025/" class="listicle-link-n">Read the full VirtueVigil review of Adolescence <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#5</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/wednesday-2022/" style="color:#e8e6e1;text-decoration:none;">Wednesday (2022)</a> <span class="netflix-verdict woke">WOKE LEAN</span></div>
          <div class="listicle-meta-n">Woke Score: 16.1 &bull; Traditional Score: 10.64 &bull; Margin: -5 WOKE &bull; Type: Series</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:16%;"></div></div><span style="font-size:0.75rem;color:#c44040;">16.1</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:10%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">10.64</span></div>
          <div class="listicle-summary-n">Tim Burton's Addams Family spinoff was Netflix's most-watched English-language series debut ever and a genuine cultural moment. Wednesday Addams is framed as a nonconformist genius who rejects the normalcy and social expectations of Nevermore Academy, the school for supernatural outcasts. The outsider-as-hero narrative carries consistent progressive coding around identity, institutional critique, and social acceptance. It is also genuinely entertaining, which is why the traditional score is not negligible.</div>
          <a href="/reviews/wednesday-2022/" class="listicle-link-n">Read the full VirtueVigil review of Wednesday <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#6</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/people-we-meet-on-vacation-2026/" style="color:#e8e6e1;text-decoration:none;">People We Meet on Vacation (2026)</a> <span class="netflix-verdict woke">WOKE LEAN</span></div>
          <div class="listicle-meta-n">Woke Score: 14 &bull; Traditional Score: 11 &bull; Margin: -3 WOKE &bull; Type: Film</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:14%;"></div></div><span style="font-size:0.75rem;color:#c44040;">14</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:11%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">11</span></div>
          <div class="listicle-summary-n">The Emily Henry romantic adaptation carries progressive relationship framing, modern female independence messaging, and a refusal of traditional romantic resolution frameworks. The woke margin is narrow, which means the film is not aggressively ideological, but the cumulative tilt is consistent throughout. Viewers looking for a conventional romance will find the underlying messaging less traditional than the genre packaging suggests.</div>
          <a href="/reviews/people-we-meet-on-vacation-2026/" class="listicle-link-n">Read the full VirtueVigil review of People We Meet on Vacation <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#7</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/the-electric-state-2025/" style="color:#e8e6e1;text-decoration:none;">The Electric State (2025)</a> <span class="netflix-verdict woke">WOKE LEAN</span></div>
          <div class="listicle-meta-n">Woke Score: 13.63 &bull; Traditional Score: 9.52 &bull; Margin: -4 WOKE &bull; Type: Film</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:13%;"></div></div><span style="font-size:0.75rem;color:#c44040;">13.63</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:9%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">9.52</span></div>
          <div class="listicle-summary-n">The Russo Brothers' $320 million sci-fi epic based on Simon Stalenhag's illustrated novel frames corporate greed and technological dehumanization through a lens that includes progressive critiques of military-industrial capitalism. Millie Bobby Brown stars as a teen searching for her brother in a post-war America where drones and robots are controlled by military tech corporations. The anti-corporate, anti-military-tech messaging is consistent without being preachy, but it accumulates into a recognizable ideological tilt.</div>
          <a href="/reviews/the-electric-state-2025/" class="listicle-link-n">Read the full VirtueVigil review of The Electric State <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#8</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/stranger-things/" style="color:#e8e6e1;text-decoration:none;">Stranger Things (2025)</a> <span class="netflix-verdict woke">WOKE LEAN</span></div>
          <div class="listicle-meta-n">Woke Score: 13 &bull; Traditional Score: 8 &bull; Margin: -5 WOKE &bull; Type: Series</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:13%;"></div></div><span style="font-size:0.75rem;color:#c44040;">13</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:8%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">8</span></div>
          <div class="listicle-summary-n">Netflix's flagship series carries persistent progressive elements that have accumulated across its run, including identity messaging around sexuality and gender, institutional distrust framing, and a consistent pattern of female characters outperforming or correcting their male counterparts in key dramatic moments. The nostalgia framing and the small-town Americana setting provide traditional surface texture that masks the underlying ideological lean. Families who grew up with the series may be surprised by how the later seasons diverge from the early show's values baseline.</div>
          <a href="/reviews/stranger-things/" class="listicle-link-n">Read the full VirtueVigil review of Stranger Things <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#9</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/ozark/" style="color:#e8e6e1;text-decoration:none;">Ozark (2022)</a> <span class="netflix-verdict woke">WOKE LEAN</span></div>
          <div class="listicle-meta-n">Woke Score: 9 &bull; Traditional Score: 5 &bull; Margin: -4 WOKE &bull; Type: Series</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:9%;"></div></div><span style="font-size:0.75rem;color:#c44040;">9</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:5%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">5</span></div>
          <div class="listicle-summary-n">Ozark's final season leans into progressive character framing around its female leads, particularly Ruth Langmore and Wendy Byrde. The series consistently positions its women as the most capable and morally complex actors in a world of male incompetence and corruption. The rural Missouri setting carries traditional surface texture, but the underlying moral framework rewards female agency and punishes traditional male authority. Ozark is one of Netflix's most acclaimed dramas, and its ideological content is embedded in character dynamics rather than explicit messaging.</div>
          <a href="/reviews/ozark/" class="listicle-link-n">Read the full VirtueVigil review of Ozark <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n">#10</div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/back-in-action-2025/" style="color:#e8e6e1;text-decoration:none;">Back in Action (2025)</a> <span class="netflix-verdict mixed">MIXED</span></div>
          <div class="listicle-meta-n">Woke Score: 12.6 &bull; Traditional Score: 10.92 &bull; Margin: -2 WOKE &bull; Type: Film</div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Woke</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-woke" style="width:12%;"></div></div><span style="font-size:0.75rem;color:#c44040;">12.6</span></div>
          <div class="netflix-score-bar"><span class="netflix-score-label">Trad</span><div class="netflix-bar-track"><div class="netflix-bar-fill netflix-bar-trad" style="width:10%;"></div></div><span style="font-size:0.75rem;color:#2ecc71;">10.92</span></div>
          <div class="listicle-summary-n">Jamie Foxx and Cameron Diaz's action-comedy marks the lowest-woke-margin film on the woke side of our Netflix data. The film carries some progressive packaging, including female competence consistently exceeding male competence in action sequences, but balances it with family loyalty, parental responsibility themes, and a conventional action structure that counterweights the messaging. It is the cleanest example of Netflix's mainstream formula: just woke enough to satisfy critics, just conventional enough to retain general audiences.</div>
          <a href="/reviews/back-in-action-2025/" class="listicle-link-n">Read the full VirtueVigil review of Back in Action <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <hr>

      <h2>The Most Traditional Netflix Titles</h2>
      <p>If you want to stream Netflix content that scores well for traditional values, here are the titles that top our rankings. These are not perfect films, but their ideological content skews toward the values most conservative families hold.</p>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n"><i class="fas fa-check" style="color:#2ecc71;font-size:0.85rem;"></i></div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/peaky-blinders-the-immortal-man-2026/" style="color:#e8e6e1;text-decoration:none;">Peaky Blinders: The Immortal Man (2026)</a> <span class="netflix-verdict strongly-trad">STRONGLY TRADITIONAL</span></div>
          <div class="listicle-meta-n">Woke Score: 5 &bull; Traditional Score: 28 &bull; Margin: +23 TRAD</div>
          <div class="listicle-summary-n">The highest traditional score of any Netflix title in our database. The Birmingham crime saga finale is built on loyalty, family hierarchy, earned authority, and consequence-based moral storytelling. Tommy Shelby's arc reaches its conclusion without progressive reframing of his character or his world. The women in his orbit are strong but defined by their relationships to family and clan rather than by identity politics. This is the old school prestige crime drama Netflix still occasionally makes.</div>
          <a href="/reviews/peaky-blinders-the-immortal-man-2026/" class="listicle-link-n">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n"><i class="fas fa-check" style="color:#2ecc71;font-size:0.85rem;"></i></div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/nonnas-2025/" style="color:#e8e6e1;text-decoration:none;">Nonnas (2025)</a> <span class="netflix-verdict strongly-trad">TRADITIONAL</span></div>
          <div class="listicle-meta-n">Woke Score: 1 &bull; Traditional Score: 17 &bull; Margin: +16 TRAD</div>
          <div class="listicle-summary-n">The lowest Woke Score of any Netflix title we reviewed. Nonnas is a warmhearted Italian-American restaurant film built around family, food, faith, and community, delivered without progressive packaging of any kind. It is the rare Netflix original that feels like it could have been made in a different era of Hollywood, when earnest stories about ordinary people and family bonds were the default rather than the exception. Worth seeking out if you want something that does not require a woke-tracker while watching.</div>
          <a href="/reviews/nonnas-2025/" class="listicle-link-n">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n"><i class="fas fa-check" style="color:#2ecc71;font-size:0.85rem;"></i></div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/war-machine-2026/" style="color:#e8e6e1;text-decoration:none;">War Machine (2026)</a> <span class="netflix-verdict trad">TRADITIONAL</span></div>
          <div class="listicle-meta-n">Woke Score: 4 &bull; Traditional Score: 22 &bull; Margin: +18 TRAD</div>
          <div class="listicle-summary-n">Military films built on duty, sacrifice, unit cohesion, and earned leadership are rare on Netflix. War Machine delivers exactly that without the progressive institutional critique that has infected recent war films. The military is portrayed as a legitimate institution staffed by competent professionals. Authority is earned through competence and character, not challenged on systemic grounds. A strong choice for viewers who miss the kind of serious military film Hollywood no longer reliably makes.</div>
          <a href="/reviews/war-machine-2026/" class="listicle-link-n">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n"><i class="fas fa-check" style="color:#2ecc71;font-size:0.85rem;"></i></div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/train-dreams-2025/" style="color:#e8e6e1;text-decoration:none;">Train Dreams (2025)</a> <span class="netflix-verdict trad">TRADITIONAL</span></div>
          <div class="listicle-meta-n">Woke Score: 5.3 &bull; Traditional Score: 20.6 &bull; Margin: +15 TRAD</div>
          <div class="listicle-summary-n">Denis Villeneuve's adaptation of Denis Johnson's novella is a quiet, devastating portrait of an American laborer's life across the early 20th century. Work, loss, marriage, fatherhood, and the passage of time are rendered without ideological commentary of any kind. A film that trusts its audience to find meaning in human experience without a political framework being imposed on top of it. One of the most purely traditional films Netflix has produced in recent memory.</div>
          <a href="/reviews/train-dreams-2025/" class="listicle-link-n">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-item-netflix">
        <div class="listicle-rank-n"><i class="fas fa-check" style="color:#2ecc71;font-size:0.85rem;"></i></div>
        <div class="listicle-body-n">
          <div class="listicle-title-n"><a href="/reviews/beverly-hills-cop-axel-f-2024/" style="color:#e8e6e1;text-decoration:none;">Beverly Hills Cop: Axel F (2024)</a> <span class="netflix-verdict trad">TRADITIONAL</span></div>
          <div class="listicle-meta-n">Woke Score: 4 &bull; Traditional Score: 15 &bull; Margin: +11 TRAD</div>
          <div class="listicle-summary-n">Eddie Murphy's fourth Axel Foley film is a throwback action comedy built on friendship, fatherly love, earned trust, and a competent male lead who solves problems through wit and skill. The film includes a daughter subplot centered on their reconciliation that is handled with warmth and sincerity. No systemic framing, no identity politics, no institutional critique. If you want to know what Netflix can produce when it is not chasing awards or cultural credit, Beverly Hills Cop: Axel F is the answer.</div>
          <a href="/reviews/beverly-hills-cop-axel-f-2024/" class="listicle-link-n">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <hr>

      <h2>The Verdict: So Is Netflix Getting More Woke?</h2>

      <p>The data says: yes and no, and the "yes" matters more than the "no."</p>

      <p>The majority of Netflix's reviewed catalog (13 of 28 titles) scores traditional or lean traditional. The platform still commissions Beverly Hills Cop sequels, Peaky Blinders continuations, military dramas, and earnest family films. These titles serve the platform's subscriber base, and Netflix needs subscribers more than it needs cultural credit.</p>

      <p>But the pattern at the top is clear. Netflix's prestige content, the titles that receive critical acclaim, awards consideration, and maximum marketing spend, skews heavily progressive. Bridgerton, Emilia Perez, and Adolescence are the titles Netflix uses to define itself culturally and in Hollywood. Those titles score significantly woke by our methodology.</p>

      <div class="trend-section">
        <h3>What This Means for Conservative Viewers</h3>
        <p>Netflix is running a two-track content strategy. Track one is conventional entertainment, action movies, legacy franchise sequels, warm family stories, designed to keep subscribers paying. Track two is prestige and progressive content, designed to win awards, attract critics, and signal ideological alignment with Hollywood culture. If you stick to track one, your Netflix experience will look largely traditional. If you follow Netflix's prestige recommendations and critical favorites, you are looking at a consistently progressive content diet. Knowing which track you are on before you press play is exactly what VirtueVigil exists to help you do.</p>
      </div>

      <h2>Browse All Netflix Reviews on VirtueVigil</h2>
      <p>Every Netflix title listed in this article has been reviewed in full on VirtueVigil with complete trope audits, woke and traditional score breakdowns, and parental guidance. Use the links above or search our review database at <a href="/">virtuevigil.com</a> to find the full analysis for any title before you watch.</p>

      <p>We add new reviews regularly. If a Netflix title you want scored is not in our database yet, check back soon or <a href="/subscribe/">subscribe</a> to get notified when new reviews drop.</p>
    </article>`
  }));

  writePage('lists/woke-horror-movies-2024/index.html', buildListiclePage({
    slug: 'woke-horror-movies-2024',
    title: '10 Horror Movies That Pushed a Woke Agenda',
    description: 'Horror fans deserve to know what\'s in the movie before they watch. VirtueVigil scores the 10 most ideologically charged horror films.',
    canonicalPath: 'lists/woke-horror-movies-2024',
    publishDate: '2026-03-21',
    htmlContent: `<article class="listicle-article">
      <style>
        .horror-item { display:flex; gap:18px; align-items:flex-start; background:#13131e; border:1px solid rgba(196,64,64,0.18); border-radius:10px; padding:20px; margin-bottom:20px; }
        .horror-rank { min-width:44px; height:44px; border-radius:50%; background:rgba(196,64,64,0.15); display:flex; align-items:center; justify-content:center; font-family:'Cinzel',Georgia,serif; font-weight:700; color:#c44040; font-size:0.95rem; flex-shrink:0; margin-top:2px; }
        .horror-body { flex:1; min-width:0; }
        .horror-title { font-size:1.05rem; font-weight:700; color:#e8e6e1; margin:0 0 6px; }
        .horror-meta { font-size:0.78rem; color:#a0a0a8; margin:0 0 10px; }
        .horror-verdict { display:inline-block; padding:3px 10px; border-radius:5px; font-size:0.72rem; font-weight:700; }
        .horror-verdict.woke { background:rgba(196,64,64,0.15); color:#c44040; border:1px solid rgba(196,64,64,0.4); }
        .horror-verdict.strongly-woke { background:rgba(196,64,64,0.25); color:#ff6060; border:1px solid rgba(196,64,64,0.6); }
        .horror-verdict.woke-lean { background:rgba(196,64,64,0.1); color:#d46060; border:1px solid rgba(196,64,64,0.3); }
        .horror-summary { font-size:0.9rem; color:#ccc; line-height:1.65; margin:10px 0; }
        .horror-link { font-size:0.85rem; font-weight:600; color:#c9a84c; text-decoration:none; }
        .horror-link:hover { text-decoration:underline; }
        .horror-score-chip { display:inline-block; background:rgba(196,64,64,0.12); border:1px solid rgba(196,64,64,0.3); border-radius:4px; padding:2px 8px; font-size:0.75rem; font-weight:700; color:#c44040; margin-left:8px; }
      </style>

      <p>Horror has always been a genre that reflects what a society fears. For decades, the monsters were external: slashers, demons, aliens, things in the dark. But somewhere along the way, Hollywood decided the real monster was traditional values. Now a significant slice of horror output exists to tell you that religion is a con, suburban domesticity is a prison, and the patriarchy is scarier than any killer clown.</p>

      <p>We scored every horror film in the VirtueVigil database using our Woke-Watch Scoring System. The results below are not opinion. They are data. Each film's summary pulls directly from our full reviews, which break down the specific ideological tropes, their severity, and how much they dominate the film's actual story. Some of these movies are technically well-made. A few are genuinely disturbing as cinema. All of them push an agenda worth knowing about before you hit play.</p>

      <p>This list focuses on films with horror as a primary or core genre. We ranked by woke score, so the most ideologically loaded entries land at the top. If you want to know what you're getting into before movie night, you're in the right place.</p>

      <hr>

      <div class="horror-item">
        <div class="horror-rank">#1</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/heretic-2024/" style="color:#e8e6e1;text-decoration:none;">Heretic (2024)</a> <span class="horror-verdict strongly-woke">STRONGLY WOKE</span> <span class="horror-score-chip">-27 WOKE</span></div>
          <div class="horror-meta">Genre: Horror &bull; Woke Score: 41 &bull; Traditional Score: 14</div>
          <div class="horror-summary">Two Mormon missionaries visit a man's home and spend the next 90 minutes getting demolished by Hugh Grant's intellectually seductive atheist. The film's central thesis: religion is an evolutionary "system of control," Jesus borrowed from Horus and Mithras, and believers are either naive or manipulated. The missionaries are given almost no effective rebuttal. Their silence is the point. This is not a horror film that touches on religion. It's a theological attack on Christianity using the horror genre as delivery mechanism.</div>
          <a href="/reviews/heretic-2024/" class="horror-link">Read the full VirtueVigil review of Heretic <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#2</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/the-substance-2024/" style="color:#e8e6e1;text-decoration:none;">The Substance (2024)</a> <span class="horror-verdict strongly-woke">STRONGLY WOKE</span> <span class="horror-score-chip">-24 WOKE</span></div>
          <div class="horror-meta">Genre: Horror &bull; Woke Score: 37 &bull; Traditional Score: 13</div>
          <div class="horror-summary">Coralie Fargeat's body horror spectacle uses 21,000 liters of fake blood to make one argument: Hollywood destroys women. The male executive who fires the protagonist is shot through a fish-eye lens that turns him into a grotesque caricature. Men exist in this film as either predators or leering grotesques. The female body becomes a metaphor for patriarchal violence. It's technically audacious and completely merciless in its feminist fury. VirtueVigil scored it STRONGLY WOKE with a -24 margin.</div>
          <a href="/reviews/the-substance-2024/" class="horror-link">Read the full VirtueVigil review of The Substance <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#3</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/immaculate-2024/" style="color:#e8e6e1;text-decoration:none;">Immaculate (2024)</a> <span class="horror-verdict strongly-woke">STRONGLY WOKE</span> <span class="horror-score-chip">-21 WOKE</span></div>
          <div class="horror-meta">Genre: Horror &bull; Woke Score: 29 &bull; Traditional Score: 8</div>
          <div class="horror-summary">Sydney Sweeney spent years developing this as a vehicle for a specific message. An American nun arrives at an Italian convent and discovers the Church has been running a forced conception experiment to produce a second Christ. Reproductive autonomy is the film's explicit thesis: a woman's body is her own, and any institution that overrides that, including the Catholic Church, is a horror villain. VirtueVigil flagged it as a significant woke trap for devout Catholic audiences going in blind.</div>
          <a href="/reviews/immaculate-2024/" class="horror-link">Read the full VirtueVigil review of Immaculate <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#4</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/maxxxine-2024/" style="color:#e8e6e1;text-decoration:none;">MaXXXine (2024)</a> <span class="horror-verdict woke">WOKE</span> <span class="horror-score-chip">-18 WOKE</span></div>
          <div class="horror-meta">Genre: Horror/Crime &bull; Woke Score: 32 &bull; Traditional Score: 14</div>
          <div class="horror-summary">The third film in Ti West's X trilogy drops Mia Goth into 1985 Los Angeles, where the primary villain is a televangelist conservative who orchestrates murders to stop a porn star from crossing over into mainstream Hollywood. The Moral Majority is the monster. Sex work is treated as morally neutral and the protagonist's career in adult film is framed as pure ambition. Killing her own fundamentalist father is the film's triumphant climax. VirtueVigil scored it WOKE at -18.</div>
          <a href="/reviews/maxxxine-2024/" class="horror-link">Read the full VirtueVigil review of MaXXXine <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#5</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/clown-in-a-cornfield-2025/" style="color:#e8e6e1;text-decoration:none;">Clown in a Cornfield (2025)</a> <span class="horror-verdict woke">WOKE</span> <span class="horror-score-chip">-18 WOKE</span></div>
          <div class="horror-meta">Genre: Horror &bull; Woke Score: 23 &bull; Traditional Score: 5</div>
          <div class="horror-summary">This slasher keeps its politics concealed through the first half before delivering them without ambiguity. A teenage girl from Philadelphia moves to a small Missouri town where the mayor, sheriff, teacher, and business owners are organizing murders to enforce their vision of community purity. Small-town Midwestern conservatism is the villain. The urban outsider is the moral hero. The film frames every traditional authority figure as a potential murderer and scores a flat WOKE at -18 by VirtueVigil.</div>
          <a href="/reviews/clown-in-a-cornfield-2025/" class="horror-link">Read the full VirtueVigil review of Clown in a Cornfield <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#6</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/dont-worry-darling-2022/" style="color:#e8e6e1;text-decoration:none;">Don't Worry Darling (2022)</a> <span class="horror-verdict woke">WOKE</span> <span class="horror-score-chip">-19 WOKE</span></div>
          <div class="horror-meta">Genre: Psychological Thriller &bull; Woke Score: 21.84 &bull; Traditional Score: 2.7</div>
          <div class="horror-summary">Olivia Wilde acknowledged post-production that the film's villain was inspired by Jordan Peterson. The premise: a perfect 1950s suburban community turns out to be a simulation in which men have imprisoned their wives without consent, keeping them docile through drugs and programming. Traditional domesticity is re-framed as a male-constructed prison. The film's horror depends entirely on the revelation that women are being held captive by husbands who chose their lives for them. It scores -19 WOKE, one of the higher margins in VirtueVigil's database.</div>
          <a href="/reviews/dont-worry-darling-2022/" class="horror-link">Read the full VirtueVigil review of Don't Worry Darling <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#7</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/the-bride-2026/" style="color:#e8e6e1;text-decoration:none;">The Bride! (2026)</a> <span class="horror-verdict woke">WOKE</span> <span class="horror-score-chip">-14 WOKE</span></div>
          <div class="horror-meta">Genre: Gothic Romance / Horror &bull; Woke Score: 22.1 &bull; Traditional Score: 8.4</div>
          <div class="horror-summary">Maggie Gyllenhaal's reimagining of Bride of Frankenstein flips the 1935 film's original male scientist to a female one and builds the whole story around a feminist awakening narrative. In the film's climax, Jessie Buckley's Bride shouts "Me too! Me too!" in an unmistakable reference to the 2017 movement. The character rejects every name men give her, embraces female rage as a repeated mantra, and the whole arc is framed as liberation from male control. VirtueVigil scored it WOKE at -14.</div>
          <a href="/reviews/the-bride-2026/" class="horror-link">Read the full VirtueVigil review of The Bride! <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#8</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/presence-2025/" style="color:#e8e6e1;text-decoration:none;">Presence (2025)</a> <span class="horror-verdict woke">WOKE</span> <span class="horror-score-chip">-10 WOKE</span></div>
          <div class="horror-meta">Genre: Horror/Thriller &bull; Woke Score: 18.1 &bull; Traditional Score: 8.5</div>
          <div class="horror-summary">Steven Soderbergh's ghost-POV horror film is more subtle than most on this list, but the ideology runs consistently through it. The ghost functions as a progressive moral arbiter: it protects the neglected daughter, watches passively as the mother's ambition corrupts the family, and punishes the bullying son. The father is caring but completely ineffectual. Male authority is absent or useless. The film's supernatural force enforces a specific moral worldview throughout, landing at -10 WOKE.</div>
          <a href="/reviews/presence-2025/" class="horror-link">Read the full VirtueVigil review of Presence <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#9</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/the-ugly-stepsister-2025/" style="color:#e8e6e1;text-decoration:none;">The Ugly Stepsister (2025)</a> <span class="horror-verdict woke-lean">WOKE LEAN</span> <span class="horror-score-chip">-7 WOKE</span></div>
          <div class="horror-meta">Genre: Satirical Black Comedy/Body Horror &bull; Woke Score: 18.12 &bull; Traditional Score: 11.24</div>
          <div class="horror-summary">Norwegian director Emilie Blichfeldt retells Cinderella from the stepsister's perspective as a body horror satire about beauty standards. The film's central thesis: beauty expectations are a form of patriarchal violence imposed on women. Every cosmetic procedure Elvira undergoes is framed as self-inflicted harm caused by male judgment. The film ends not with a prince but with two women stealing jewelry and riding away together, rejecting the marriage plot entirely. VirtueVigil scored it WOKE LEAN at -7.</div>
          <a href="/reviews/the-ugly-stepsister-2025/" class="horror-link">Read the full VirtueVigil review of The Ugly Stepsister <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="horror-item">
        <div class="horror-rank">#10</div>
        <div class="horror-body">
          <div class="horror-title"><a href="/reviews/death-of-a-unicorn-2025/" style="color:#e8e6e1;text-decoration:none;">Death of a Unicorn (2025)</a> <span class="horror-verdict woke-lean">WOKE LEAN</span> <span class="horror-score-chip">-5 WOKE</span></div>
          <div class="horror-meta">Genre: Dark Fantasy / Comedy Horror &bull; Woke Score: 16.9 &bull; Traditional Score: 12.3</div>
          <div class="horror-summary">A dark fantasy creature feature where a pharmaceutical dynasty (modeled explicitly on the Sacklers, per the director) tries to harvest a unicorn for profit and gets eaten. Every wealthy character is predatory, greedy, or incompetent. The film's sole moral compass is a progressive Gen-Z woman coded from hair to attitude as the ideological hero. Anti-capitalist satire is the core engine. The rich deserve what they get. VirtueVigil scored it WOKE LEAN at -5, the lightest entry on this list but consistent with the pattern.</div>
          <a href="/reviews/death-of-a-unicorn-2025/" class="horror-link">Read the full VirtueVigil review of Death of a Unicorn <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-conclusion" style="background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);border-radius:10px;padding:22px 26px;margin:28px 0;">
        <p>Horror is at its best when the fear means something. These 10 films all mean something specific: they have a worldview, and they built their scares around it. Knowing that going in does not ruin the films. It just lets you watch them honestly. Browse VirtueVigil's full horror database for complete VVWS scores, trope audits, and parental guidance on every title, from STRONGLY WOKE to STRONGLY TRADITIONAL. You might be surprised what's worth your time. <a href="/reviews/">Browse all reviews</a>.</p>
      </div>
    </article>`
  }));

  writePage('lists/conservative-movies-to-watch-2025/index.html', buildListiclePage({
    slug: 'conservative-movies-to-watch-2025',
    title: 'Top 10 Films Conservatives Will Love in 2025',
    description: 'Looking for movies worth your time? Here are 10 films from 2025 that scored Traditional or better on VirtueVigil.',
    canonicalPath: 'lists/conservative-movies-to-watch-2025',
    publishDate: '2026-03-21',
    htmlContent: `<article class="listicle-article">
      <style>
        .cons-item { display:flex; gap:18px; align-items:flex-start; background:#13131e; border:1px solid rgba(201,168,76,0.18); border-radius:10px; padding:20px; margin-bottom:20px; }
        .cons-rank { min-width:44px; height:44px; border-radius:50%; background:rgba(201,168,76,0.12); display:flex; align-items:center; justify-content:center; font-family:'Cinzel',Georgia,serif; font-weight:700; color:#c9a84c; font-size:0.95rem; flex-shrink:0; margin-top:2px; }
        .cons-body { flex:1; min-width:0; }
        .cons-title { font-size:1.05rem; font-weight:700; color:#e8e6e1; margin:0 0 6px; }
        .cons-meta { font-size:0.78rem; color:#a0a0a8; margin:0 0 10px; }
        .cons-verdict { display:inline-block; padding:3px 10px; border-radius:5px; font-size:0.72rem; font-weight:700; }
        .cons-verdict.strongly-trad { background:rgba(58,139,85,0.25); color:#5fdd8a; border:1px solid rgba(58,139,85,0.6); }
        .cons-verdict.trad { background:rgba(58,139,85,0.15); color:#4dbb72; border:1px solid rgba(58,139,85,0.4); }
        .cons-summary { font-size:0.9rem; color:#ccc; line-height:1.65; margin:10px 0; }
        .cons-link { font-size:0.85rem; font-weight:600; color:#c9a84c; text-decoration:none; }
        .cons-link:hover { text-decoration:underline; }
        .cons-score-chip { display:inline-block; background:rgba(58,139,85,0.12); border:1px solid rgba(58,139,85,0.3); border-radius:4px; padding:2px 8px; font-size:0.75rem; font-weight:700; color:#4dbb72; margin-left:8px; }
      </style>

      <p>Finding a movie your whole family can watch without getting a lecture is harder than it should be. Most of what Hollywood puts out these days comes loaded with messaging, subtext, or just flat-out ideology that has nothing to do with telling a good story. You sit down to relax and end up feeling like you wandered into a seminar. It gets old fast.</p>

      <p>That's where VirtueVigil's scoring system earns its keep. We run every film through our Woke-Watch Scoring System, measuring traditional and woke elements by severity, authenticity, and narrative centrality. A film that scores Traditional or better has real story values: sacrifice, duty, family, faith, earned masculinity, consequences for bad choices. The 10 films below all cleared that bar in 2025. They range from animated family epics to true-story thrillers to faith-based blockbusters. Every one of them is worth your time.</p>

      <hr>

      <div class="cons-item">
        <div class="cons-rank">#1</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/the-spongebob-movie-search-for-squarepants-2025/" style="color:#e8e6e1;text-decoration:none;">The SpongeBob Movie: Search for SquarePants (2025)</a> <span class="cons-verdict strongly-trad">STRONGLY TRADITIONAL</span> <span class="cons-score-chip">+42 TRAD</span></div>
          <div class="cons-meta">Genre: Animation / Adventure / Comedy</div>
          <div class="cons-summary">The fourth SpongeBob theatrical outing is a rare thing: a mainstream animated film that delivers its moral without a lecture and doesn't try to be anything it's not. Friendship, courage, and the guidance of a surrogate father figure carry the story from start to finish. Zero ideology, all heart.</div>
          <a href="/reviews/the-spongebob-movie-search-for-squarepants-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#2</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/ne-zha-2-2025/" style="color:#e8e6e1;text-decoration:none;">Ne Zha 2 (2025)</a> <span class="cons-verdict strongly-trad">STRONGLY TRADITIONAL</span> <span class="cons-score-chip">+39 TRAD</span></div>
          <div class="cons-meta">Genre: Animation / Fantasy / Action</div>
          <div class="cons-summary">China's animated blockbuster is a masterpiece of scale built around something Western studios keep getting wrong: a father and son who love each other without irony. Destiny, sacrifice, and filial devotion drive every frame. The woke score is literally zero. One of the most traditionally coded films of the year, from any country.</div>
          <a href="/reviews/ne-zha-2-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#3</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/how-to-train-your-dragon-2025/" style="color:#e8e6e1;text-decoration:none;">How to Train Your Dragon (2025)</a> <span class="cons-verdict strongly-trad">STRONGLY TRADITIONAL</span> <span class="cons-score-chip">+29 TRAD</span></div>
          <div class="cons-meta">Genre: Family / Adventure</div>
          <div class="cons-summary">Dean DeBlois's live-action remake protects what made the originals work: a kid who earns respect through courage and ingenuity, a father-son conflict with real emotional stakes, and a world where being different doesn't make you a victim. Gerard Butler returns as Stoick and brings every pound of authority the role demands. Safe for the whole family.</div>
          <a href="/reviews/how-to-train-your-dragon-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#4</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/david-2025/" style="color:#e8e6e1;text-decoration:none;">David (2025)</a> <span class="cons-verdict strongly-trad">STRONGLY TRADITIONAL</span> <span class="cons-score-chip">+26 TRAD</span></div>
          <div class="cons-meta">Genre: Animation / Musical / Biblical Epic</div>
          <div class="cons-summary">Angel Studios' animated biblical musical tells the story of King David from anointing to Goliath to his mercy toward Saul, with craft that rivals the major studios. The faith content is unapologetic: God is real, active, and sovereign. Courage comes from above, not from believing in yourself. $84 million at the box office proves the audience is there.</div>
          <a href="/reviews/david-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#5</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/karate-kid-legends-2025/" style="color:#e8e6e1;text-decoration:none;">Karate Kid: Legends (2025)</a> <span class="cons-verdict strongly-trad">STRONGLY TRADITIONAL</span> <span class="cons-score-chip">+23 TRAD</span></div>
          <div class="cons-meta">Genre: Action / Drama / Family</div>
          <div class="cons-summary">The most traditionally coded major studio release of 2025. Older men teaching a young man to be brave, disciplined, and honorable. Hard work, respect for elders, honoring tradition, showing mercy to your enemies. The film doesn't argue for these values; it just lives them. One of the safest and most satisfying watches of the year for conservative families.</div>
          <a href="/reviews/karate-kid-legends-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#6</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/the-accountant-2-2025/" style="color:#e8e6e1;text-decoration:none;">The Accountant 2 (2025)</a> <span class="cons-verdict strongly-trad">STRONGLY TRADITIONAL</span> <span class="cons-score-chip">+22 TRAD</span></div>
          <div class="cons-meta">Genre: Action / Crime / Thriller</div>
          <div class="cons-summary">Christian Wolff is one of the best protagonists in action cinema right now: a man with autism and a personal code that has more integrity than anything the institutions around him produce. The sequel delivers the same still-water intensity as the original, built on brotherhood, loyalty, and the simple principle that protecting the innocent is worth the cost.</div>
          <a href="/reviews/the-accountant-2-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#7</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/last-breath-2025/" style="color:#e8e6e1;text-decoration:none;">Last Breath (2025)</a> <span class="cons-verdict strongly-trad">STRONGLY TRADITIONAL</span> <span class="cons-score-chip">+21 TRAD</span></div>
          <div class="cons-meta">Genre: Thriller (True Story)</div>
          <div class="cons-summary">A true-story survival thriller about a saturation diver stranded on the seafloor with five minutes of oxygen. Built on professional brotherhood, physical courage, and the refusal to leave a teammate behind. No politics, no lectures, just men doing their jobs under impossible pressure. This is what movies about male competence look like when they're made right.</div>
          <a href="/reviews/last-breath-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#8</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/demon-slayer-infinity-castle-2025/" style="color:#e8e6e1;text-decoration:none;">Demon Slayer: Infinity Castle (2025)</a> <span class="cons-verdict trad">TRADITIONAL</span> <span class="cons-score-chip">+19 TRAD</span></div>
          <div class="cons-meta">Genre: Animation / Action / Fantasy</div>
          <div class="cons-summary">The most technically ambitious traditionally animated film in years, and it earns every frame. Family obligation, sacrifice, and the duty to protect drive the story across 155 minutes of breathtaking action. The Tanjiro-Nezuko sibling bond is the moral center: he will fight through every enemy that threatens her. $778 million worldwide proves traditional storytelling still has an audience.</div>
          <a href="/reviews/demon-slayer-infinity-castle-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#9</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/f1-2025/" style="color:#e8e6e1;text-decoration:none;">F1 (2025)</a> <span class="cons-verdict trad">TRADITIONAL</span> <span class="cons-score-chip">+17 TRAD</span></div>
          <div class="cons-meta">Genre: Sports Drama / Action</div>
          <div class="cons-summary">Brad Pitt as a comeback driver mentoring a young hotshot. Old-school masculinity, mentorship, and the pursuit of excellence, all wrapped in the most viscerally thrilling racing footage put on film. No identity politics, no lectures about systemic anything. Pure story, pure speed, pure craft. The kind of film that reminds you what blockbusters used to feel like.</div>
          <a href="/reviews/f1-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="cons-item">
        <div class="cons-rank">#10</div>
        <div class="cons-body">
          <div class="cons-title"><a href="/reviews/song-sung-blue-2025/" style="color:#e8e6e1;text-decoration:none;">Song Sung Blue (2025)</a> <span class="cons-verdict trad">TRADITIONAL</span> <span class="cons-score-chip">+19 TRAD</span></div>
          <div class="cons-meta">Genre: Biography / Musical / Drama</div>
          <div class="cons-summary">The true story of Mike and Claire Sardina, a Milwaukee couple who built a Neil Diamond tribute act and fought through alcoholism, a car accident, amputation, mental illness, and death without ever letting go of each other. Hugh Jackman and Kate Hudson give career-best performances in a film that celebrates marriage as a covenant worth dying for. This is what lifelong commitment looks like, without romanticizing any of the cost.</div>
          <a href="/reviews/song-sung-blue-2025/" class="cons-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-conclusion" style="background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);border-radius:10px;padding:22px 26px;margin:28px 0;">
        <p>Every film on this list was scored by VirtueVigil's full Woke-Watch Scoring System: traditional and woke tropes measured by severity, authenticity, and narrative centrality. These aren't picks based on gut feeling or politics. They're based on data. If you want to keep finding films that respect your time and your values, browse the full VirtueVigil review library at <a href="/reviews/">VirtueVigil</a>. New reviews go up every week.</p>
      </div>
    </article>`
  }));

  writePage('lists/woke-sequels-more-woke-than-original/index.html', buildListiclePage({
    slug: 'woke-sequels-more-woke-than-original',
    title: '10 Sequels That Got More Woke Than the Original',
    description: 'These franchises started strong then drifted hard left. VirtueVigil scores the 10 sequels that piled on the woke agenda more than their predecessors.',
    canonicalPath: 'lists/woke-sequels-more-woke-than-original',
    publishDate: '2026-03-22',
    htmlContent: `<article class="listicle-article">
      <style>
        .seq-item { display:flex; gap:18px; align-items:flex-start; background:#13131e; border:1px solid rgba(201,168,76,0.18); border-radius:10px; padding:20px; margin-bottom:20px; }
        .seq-rank { min-width:44px; height:44px; border-radius:50%; background:rgba(220,38,38,0.12); display:flex; align-items:center; justify-content:center; font-family:'Cinzel',Georgia,serif; font-weight:700; color:#ef4444; font-size:0.95rem; flex-shrink:0; margin-top:2px; }
        .seq-body { flex:1; min-width:0; }
        .seq-title { font-size:1.05rem; font-weight:700; color:#e8e6e1; margin:0 0 6px; }
        .seq-meta { font-size:0.78rem; color:#a0a0a8; margin:0 0 10px; }
        .seq-verdict { display:inline-block; padding:3px 10px; border-radius:5px; font-size:0.72rem; font-weight:700; }
        .seq-verdict.strongly-woke { background:rgba(220,38,38,0.25); color:#ef4444; border:1px solid rgba(220,38,38,0.6); }
        .seq-verdict.woke { background:rgba(220,38,38,0.15); color:#f87171; border:1px solid rgba(220,38,38,0.4); }
        .seq-summary { font-size:0.9rem; color:#ccc; line-height:1.65; margin:10px 0; }
        .seq-link { font-size:0.85rem; font-weight:600; color:#c9a84c; text-decoration:none; }
        .seq-link:hover { text-decoration:underline; }
        .seq-score-chip { display:inline-block; background:rgba(220,38,38,0.12); border:1px solid rgba(220,38,38,0.3); border-radius:4px; padding:2px 8px; font-size:0.75rem; font-weight:700; color:#ef4444; margin-left:8px; }
      </style>

      <p>Sequels are supposed to give fans more of what they loved. More story, more characters, more of the world that made the original work. What they get instead, more and more often, is more ideology. Hollywood has figured out that a familiar title gets people in the door, and once they're in the seats, the messaging can begin.</p>

      <p>The 10 films below are all continuations of franchises that started with mainstream appeal. VirtueVigil ran every one through our full Woke-Watch Scoring System. Each one scored higher on woke elements than on traditional values, and most scored significantly worse than whatever came before them. These aren't subtle shifts. They're franchise-wide left turns that audiences noticed, even if critics pretended not to.</p>

      <hr>

      <div class="seq-item">
        <div class="seq-rank">#1</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/zootopia-2-2025/" style="color:#e8e6e1;text-decoration:none;">Zootopia 2 (2025)</a> <span class="seq-verdict strongly-woke">STRONGLY WOKE</span> <span class="seq-score-chip">Woke: 91</span></div>
          <div class="seq-meta">Genre: Animation | Woke Score: 91 vs Trad Score: 53</div>
          <div class="seq-summary">The original Zootopia had a legitimate message about bias and did it with enough story craft to make it work. The sequel abandoned subtlety entirely. Every scene is in service of the agenda. Disney took a beloved franchise and turned it into the most woke-scored animated film in VirtueVigil's database. The gap between woke and traditional scores is larger than almost anything we have reviewed.</div>
          <a href="/reviews/zootopia-2-2025/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#2</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/glass-onion-2022/" style="color:#e8e6e1;text-decoration:none;">Glass Onion: A Knives Out Mystery (2022)</a> <span class="seq-verdict strongly-woke">STRONGLY WOKE</span> <span class="seq-score-chip">Woke: 42</span></div>
          <div class="seq-meta">Genre: Mystery/Comedy | Woke Score: 42 vs Trad Score: 18</div>
          <div class="seq-summary">Knives Out was a sharp, apolitical whodunit that conservatives and liberals both loved. Glass Onion is its ideological opposite. Rian Johnson took the sequel as an opportunity to lecture his audience about wealth, privilege, and the people he finds deplorable. The mystery mechanics are weaker. The contempt for half the audience is not. This is what franchise drift looks like in real time.</div>
          <a href="/reviews/glass-onion-2022/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#3</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/bridgerton-s4-2026/" style="color:#e8e6e1;text-decoration:none;">Bridgerton: Season 4 (2026)</a> <span class="seq-verdict strongly-woke">STRONGLY WOKE</span> <span class="seq-score-chip">Woke: 58</span></div>
          <div class="seq-meta">Genre: Period Drama/Romance | Woke Score: 58 vs Trad Score: 18</div>
          <div class="seq-summary">The Bridgerton franchise has been drifting further from its Regency roots with each season. Season 4 accelerates that drift dramatically. Modern progressive values are retrofitted into a historical setting so aggressively that the period setting becomes little more than costume design. The woke score of 58 against a trad score of 18 tells the story of a show that has fully left its audience behind.</div>
          <a href="/reviews/bridgerton-s4-2026/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#4</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/thor-love-and-thunder-2022/" style="color:#e8e6e1;text-decoration:none;">Thor: Love and Thunder (2022)</a> <span class="seq-verdict woke">WOKE</span> <span class="seq-score-chip">Woke: 16.44</span></div>
          <div class="seq-meta">Genre: Action/Adventure/Comedy | Woke Score: 16.44 vs Trad Score: 12.26</div>
          <div class="seq-summary">Thor: Ragnarok was a crowd-pleaser. Love and Thunder is an LGBTQ+ promotional vehicle wearing a superhero costume. Jane Foster's transformation into Mighty Thor sidelines the franchise's established male lead for much of the runtime. Korg's same-sex family is introduced with zero story justification. The original Thor films were grounded in honor, sacrifice, and duty. This one is grounded in a different agenda entirely.</div>
          <a href="/reviews/thor-love-and-thunder-2022/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#5</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/aquaman-and-the-lost-kingdom-2023/" style="color:#e8e6e1;text-decoration:none;">Aquaman and the Lost Kingdom (2023)</a> <span class="seq-verdict strongly-woke">STRONGLY WOKE</span> <span class="seq-score-chip">Woke: 31.2</span></div>
          <div class="seq-meta">Genre: Action/Superhero/Fantasy | Woke Score: 31.2 vs Trad Score: 18.9</div>
          <div class="seq-summary">The first Aquaman was a fun, color-saturated blockbuster that leaned into its comic book DNA. The sequel layered in climate change messaging so heavy it became the film's actual villain. The ocean is dying because of human industry. Aquaman's kingdom is threatened by fossil fuels. What was once escapism became an environmental lecture with a $200 million production budget. Box office dropped by over 70% from the first film.</div>
          <a href="/reviews/aquaman-and-the-lost-kingdom-2023/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#6</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/frozen-ii-2019/" style="color:#e8e6e1;text-decoration:none;">Frozen II (2019)</a> <span class="seq-verdict woke">WOKE</span> <span class="seq-score-chip">Woke: 19</span></div>
          <div class="seq-meta">Genre: Animation/Musical/Fantasy | Woke Score: 19 vs Trad Score: 14</div>
          <div class="seq-summary">Frozen was about sisterhood and the courage to act. Frozen II is about indigenous land rights, colonial guilt, and a protagonist whose personal identity quest matters more than anyone around her. Elsa's journey to find herself echoes every corporate diversity initiative of the era. The songs are weaker. The messaging is heavier. The magic that made the original a phenomenon is largely absent.</div>
          <a href="/reviews/frozen-ii-2019/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#7</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/the-marvels-2023/" style="color:#e8e6e1;text-decoration:none;">The Marvels (2023)</a> <span class="seq-verdict strongly-woke">STRONGLY WOKE</span> <span class="seq-score-chip">Woke: 22.95</span></div>
          <div class="seq-meta">Genre: Superhero/Action/Comedy | Woke Score: 22.95 vs Trad Score: 8.87</div>
          <div class="seq-summary">Captain Marvel had mainstream appeal despite its politics. The Marvels is an assembly of three female protagonists competing for screen time while a story holds them loosely together. The woke score nearly triples the traditional score. It became the lowest-grossing MCU film in history. Marvel built the most successful franchise in cinema history by telling universal stories. The Marvels is what happens when the brand prioritizes identity over craft.</div>
          <a href="/reviews/the-marvels-2023/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#8</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/toy-story-4-2019/" style="color:#e8e6e1;text-decoration:none;">Toy Story 4 (2019)</a> <span class="seq-verdict woke">WOKE</span> <span class="seq-score-chip">Woke: 17.2</span></div>
          <div class="seq-meta">Genre: Animated Adventure | Woke Score: 17.2 vs Trad Score: 8.0</div>
          <div class="seq-summary">The Toy Story trilogy ended perfectly. Then came the fourth film. Woody abandons his child, rejects his purpose, and chooses personal fulfillment over the duty that defined him for three movies. The lesson for kids: your own self-actualization matters more than the people who depend on you. Pixar told a tight, complete story across three films and undid its moral core in a fourth nobody asked for.</div>
          <a href="/reviews/toy-story-4-2019/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#9</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/black-panther-wakanda-forever-2022/" style="color:#e8e6e1;text-decoration:none;">Black Panther: Wakanda Forever (2022)</a> <span class="seq-verdict woke">WOKE</span> <span class="seq-score-chip">Woke: 18.42</span></div>
          <div class="seq-meta">Genre: Superhero/Action/Drama | Woke Score: 18.42 vs Trad Score: 12.67</div>
          <div class="seq-summary">The original Black Panther was a genuine cultural event built on a compelling protagonist and a real story about identity and duty. The sequel, made in the shadow of Chadwick Boseman's death, leaned heavily into grief, female-led power restructuring, and anti-colonial messaging. The emotional core was real but the ideology was heavy-handed. A franchise that earned its audience through craft started spending that goodwill on messaging.</div>
          <a href="/reviews/black-panther-wakanda-forever-2022/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="seq-item">
        <div class="seq-rank">#10</div>
        <div class="seq-body">
          <div class="seq-title"><a href="/reviews/dune-part-two-2024/" style="color:#e8e6e1;text-decoration:none;">Dune: Part Two (2024)</a> <span class="seq-verdict woke">WOKE</span> <span class="seq-score-chip">Woke: 19.36</span></div>
          <div class="seq-meta">Genre: Sci-Fi/Epic | Woke Score: 19.36 vs Trad Score: 11.55</div>
          <div class="seq-summary">Dune: Part One was a breathtaking technical achievement that stayed faithful to Herbert's themes of power, prophecy, and ecology. Part Two shifts the lens. Chani becomes a feminist counter-narrative to Paul's messianic arc. The religious manipulation that Herbert wrote as a critique gets reframed as a metaphor for contemporary political movements. The production is still extraordinary. The philosophical underpinning drifted from the source in ways the book's fans noticed.</div>
          <a href="/reviews/dune-part-two-2024/" class="seq-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-conclusion" style="background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);border-radius:10px;padding:22px 26px;margin:28px 0;">
        <p>Every score above comes from VirtueVigil's full Woke-Watch Scoring System, measuring woke and traditional tropes by severity, authenticity, and narrative centrality. We don't grade on politics. We grade on what the film actually argues and how central that argument is to the story. When the gap between woke and traditional scores is this wide, you're not watching a film with a perspective. You're watching a lecture with a budget. Browse the full review library at <a href="/reviews/">VirtueVigil</a> to check any sequel before you sit down.</p>
      </div>
    </article>`
  }));

  writePage('lists/rotten-tomatoes-vs-virtuevigil/index.html', buildListiclePage({
    slug: 'rotten-tomatoes-vs-virtuevigil',
    title: 'Rotten Tomatoes Loves Them. We Scored Them Anyway.',
    description: 'Critics praised these 10 films with 80%+ scores on Rotten Tomatoes. VirtueVigil ran the numbers and found a different story.',
    canonicalPath: 'lists/rotten-tomatoes-vs-virtuevigil',
    publishDate: '2026-03-22',
    htmlContent: `<article class="listicle-article">
      <style>
        .rt-item { display:flex; gap:18px; align-items:flex-start; background:#13131e; border:1px solid rgba(201,168,76,0.18); border-radius:10px; padding:20px; margin-bottom:20px; }
        .rt-rank { min-width:44px; height:44px; border-radius:50%; background:rgba(220,38,38,0.12); display:flex; align-items:center; justify-content:center; font-family:'Cinzel',Georgia,serif; font-weight:700; color:#ef4444; font-size:0.95rem; flex-shrink:0; margin-top:2px; }
        .rt-body { flex:1; min-width:0; }
        .rt-title { font-size:1.05rem; font-weight:700; color:#e8e6e1; margin:0 0 6px; }
        .rt-meta { font-size:0.78rem; color:#a0a0a8; margin:0 0 10px; }
        .rt-verdict { display:inline-block; padding:3px 10px; border-radius:5px; font-size:0.72rem; font-weight:700; }
        .rt-verdict.strongly-woke { background:rgba(220,38,38,0.25); color:#ef4444; border:1px solid rgba(220,38,38,0.6); }
        .rt-verdict.woke { background:rgba(220,38,38,0.15); color:#f87171; border:1px solid rgba(220,38,38,0.4); }
        .rt-summary { font-size:0.9rem; color:#ccc; line-height:1.65; margin:10px 0; }
        .rt-link { font-size:0.85rem; font-weight:600; color:#c9a84c; text-decoration:none; }
        .rt-link:hover { text-decoration:underline; }
        .rt-score-row { display:flex; gap:10px; flex-wrap:wrap; margin-bottom:8px; }
        .rt-chip { display:inline-block; border-radius:4px; padding:2px 8px; font-size:0.75rem; font-weight:700; }
        .rt-chip.rt-score { background:rgba(220,38,38,0.12); border:1px solid rgba(220,38,38,0.3); color:#ef4444; }
        .rt-chip.vv-score { background:rgba(220,38,38,0.12); border:1px solid rgba(220,38,38,0.3); color:#f87171; }
      </style>

      <p>Rotten Tomatoes critic scores are not film scores. They are ideology scores. A film gets 90% on Rotten Tomatoes not because it is technically superior or emotionally resonant, but because it affirms the values of the people who write film criticism for a living. That group is not representative of the country.</p>

      <p>VirtueVigil does not measure opinion. We measure content. Our Woke-Watch Scoring System tracks specific tropes by severity, authenticity, and narrative centrality. What critics call "vital" and "essential" we call something else. The 10 films below all earned significant critical praise. We scored them anyway. Judge for yourself which analysis is more useful to your family.</p>

      <hr>

      <div class="rt-item">
        <div class="rt-rank">#1</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/glass-onion-2022/" style="color:#e8e6e1;text-decoration:none;">Glass Onion: A Knives Out Mystery (2022)</a> <span class="rt-verdict strongly-woke">STRONGLY WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 42</span><span class="rt-chip vv-score">Trad Score: 18</span></div>
          <div class="rt-meta">Genre: Mystery/Comedy | RT Critic Score: 92%</div>
          <div class="rt-summary">Critics loved it. Called it "gleefully subversive" and "a sharp satire of the ultra-wealthy." What they did not say: the entire film is built around contempt for a specific type of wealthy American that maps neatly onto the cultural right. The villain is a thinly veiled Elon Musk character surrounded by sycophants who represent various conservative adjacent archetypes. Rian Johnson was not hiding it. Critics were not troubled by it. VirtueVigil's score was 42 woke vs 18 traditional.</div>
          <a href="/reviews/glass-onion-2022/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#2</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/strange-world-2022/" style="color:#e8e6e1;text-decoration:none;">Strange World (2022)</a> <span class="rt-verdict strongly-woke">STRONGLY WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 27.5</span><span class="rt-chip vv-score">Trad Score: 12.32</span></div>
          <div class="rt-meta">Genre: Animation/Adventure | RT Critic Score: 73%</div>
          <div class="rt-summary">Disney's Strange World was praised by critics for its "groundbreaking" inclusion of Disney's first openly gay teen protagonist and its environmental allegory. Audiences disagreed sharply: it bombed to a $73 million worldwide gross against a $180 million budget. VirtueVigil's woke score of 27.5 vs a trad score of 12.32 reflects what critics were celebrating. The gap between critical reception and audience response tells the real story.</div>
          <a href="/reviews/strange-world-2022/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#3</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/turning-red-2022/" style="color:#e8e6e1;text-decoration:none;">Turning Red (2022)</a> <span class="rt-verdict strongly-woke">STRONGLY WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 17.85</span><span class="rt-chip vv-score">Trad Score: 4.55</span></div>
          <div class="rt-meta">Genre: Animation/Comedy | RT Critic Score: 95%</div>
          <div class="rt-summary">Turning Red earned a 95% from critics who celebrated its female-coded coming-of-age story and what one reviewer called "the most honest depiction of puberty in animated film history." VirtueVigil measured something different: a story that frames parental authority as trauma, pushes adolescent self-expression over family obligation, and uses a girl's monstrous transformation as a metaphor for uncontrolled emotional autonomy. Parents watching with their kids will notice the values being modeled.</div>
          <a href="/reviews/turning-red-2022/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#4</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/eternals-2021/" style="color:#e8e6e1;text-decoration:none;">Eternals (2021)</a> <span class="rt-verdict strongly-woke">STRONGLY WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 19.74</span><span class="rt-chip vv-score">Trad Score: 5.95</span></div>
          <div class="rt-meta">Genre: Superhero/Sci-Fi | RT Critic Score: 47%</div>
          <div class="rt-summary">Critics were somewhat split on Eternals but the film itself was uniformly celebrated by progressive outlets for its diverse ensemble, Marvel's first gay superhero kiss, and its philosophical questioning of the MCU's established moral framework. The audience score dropped to 78%. VirtueVigil found a woke score of 19.74 against a trad score of 5.95 -- the largest proportional gap of any MCU film in our database. The cast represents every checkbox. The story has nothing to say.</div>
          <a href="/reviews/eternals-2021/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#5</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/the-marvels-2023/" style="color:#e8e6e1;text-decoration:none;">The Marvels (2023)</a> <span class="rt-verdict strongly-woke">STRONGLY WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 22.95</span><span class="rt-chip vv-score">Trad Score: 8.87</span></div>
          <div class="rt-meta">Genre: Superhero/Action | RT Critic Score: 62%</div>
          <div class="rt-summary">Even the critics who gave The Marvels mixed reviews framed their criticism around execution rather than ideology. The praise it did receive was heavily centered on its all-female lead trio and what reviewers called a "joyful" female empowerment dynamic. VirtueVigil scored it at 22.95 woke vs 8.87 traditional. It grossed $206 million worldwide against a $220 million budget, the biggest box office failure in MCU history. Audiences found their own answer to what the critics were celebrating.</div>
          <a href="/reviews/the-marvels-2023/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#6</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/lightyear-2022/" style="color:#e8e6e1;text-decoration:none;">Lightyear (2022)</a> <span class="rt-verdict woke">WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 10.22</span><span class="rt-chip vv-score">Trad Score: 6.65</span></div>
          <div class="rt-meta">Genre: Animation/Sci-Fi | RT Critic Score: 76%</div>
          <div class="rt-summary">Pixar restored a same-sex kiss scene after internal pressure and received widespread critical applause for doing so. Lightyear became the film's defining cultural moment before most people had seen it. Critics praised Pixar's courage. Audiences responded with the worst opening weekend for a Pixar theatrical release since the pandemic. The film grossed $226 million worldwide against a $200 million budget, a failure by any measure. The kiss was not the only problem but it was the symbol of who the film was made for.</div>
          <a href="/reviews/lightyear-2022/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#7</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/black-panther-wakanda-forever-2022/" style="color:#e8e6e1;text-decoration:none;">Black Panther: Wakanda Forever (2022)</a> <span class="rt-verdict woke">WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 18.42</span><span class="rt-chip vv-score">Trad Score: 12.67</span></div>
          <div class="rt-meta">Genre: Superhero/Drama | RT Critic Score: 84%</div>
          <div class="rt-summary">Critics gave it 84% and called it "a moving tribute" and "a powerful statement about grief and resistance." What was less discussed: the film's reconstruction of Wakanda as a matriarchal society, the framing of Namor's anti-colonial rage as morally justified, and the consistent sidelining of male authority figures in favor of a female-led power structure. The grief over Boseman is real and deserved. The ideology layered on top of it is not incidental.</div>
          <a href="/reviews/black-panther-wakanda-forever-2022/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#8</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/dune-part-two-2024/" style="color:#e8e6e1;text-decoration:none;">Dune: Part Two (2024)</a> <span class="rt-verdict woke">WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 19.36</span><span class="rt-chip vv-score">Trad Score: 11.55</span></div>
          <div class="rt-meta">Genre: Sci-Fi/Epic | RT Critic Score: 92%</div>
          <div class="rt-summary">Dune Part Two received near-universal critical acclaim and deserved credit for its technical craft. But the 92% score reflects more than cinematography. Critics celebrated Denis Villeneuve's decision to center Chani's feminist resistance to Paul's messianic rise, his reframing of religious manipulation as a metaphor for right-wing populism, and his departures from Herbert's source material that shifted the moral weight of the story. VirtueVigil scored it 19.36 woke vs 11.55 traditional. Great filmmaking and ideological content are not mutually exclusive.</div>
          <a href="/reviews/dune-part-two-2024/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#9</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/thor-love-and-thunder-2022/" style="color:#e8e6e1;text-decoration:none;">Thor: Love and Thunder (2022)</a> <span class="rt-verdict woke">WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 16.44</span><span class="rt-chip vv-score">Trad Score: 12.26</span></div>
          <div class="rt-meta">Genre: Action/Comedy | RT Critic Score: 63%</div>
          <div class="rt-summary">Even at 63%, the critics who praised Thor: Love and Thunder focused on Natalie Portman's Mighty Thor as a highlight. What VirtueVigil measured was a franchise installment that replaced an established male hero with a female successor and treated the audience's attachment to the original character as something to be redirected rather than honored. The LGBTQ+ content was added over Taika Waititi's stated preference for more. Critics applauded. Audiences gave it the lowest MCU audience score in years.</div>
          <a href="/reviews/thor-love-and-thunder-2022/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="rt-item">
        <div class="rt-rank">#10</div>
        <div class="rt-body">
          <div class="rt-title"><a href="/reviews/joker-folie-a-deux-2024/" style="color:#e8e6e1;text-decoration:none;">Joker: Folie a Deux (2024)</a> <span class="rt-verdict woke">WOKE</span></div>
          <div class="rt-score-row"><span class="rt-chip rt-score">Woke Score: 24.5</span><span class="rt-chip vv-score">Trad Score: 22.13</span></div>
          <div class="rt-meta">Genre: Musical/Drama/Thriller | RT Critic Score: 31%</div>
          <div class="rt-summary">Critics were lukewarm on Joker 2 overall but the reviews that praised it did so for its deconstruction of the original film's "dangerous" incel appeal and its feminist reframing of Harley Quinn as the empowered one pulling Arthur's strings. The film deliberately dismantled what made the first Joker resonate with audiences. VirtueVigil scored it 24.5 woke vs 22.13 traditional. The audience score was 32%. The box office lost $130 million. You can celebrate the deconstruction or you can serve the audience. Hollywood chose deconstruction.</div>
          <a href="/reviews/joker-folie-a-deux-2024/" class="rt-link">Read the full VirtueVigil review <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i></a>
        </div>
      </div>

      <div class="listicle-conclusion" style="background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);border-radius:10px;padding:22px 26px;margin:28px 0;">
        <p>VirtueVigil does not ask whether a film is good. We ask what it is arguing and how aggressively it argues it. Rotten Tomatoes critic scores tell you whether film critics approved. Our scores tell you what is actually in the film. For any movie you are considering, check the full VirtueVigil analysis at <a href="/reviews/">VirtueVigil</a> before deciding whether the critics' recommendation is meant for you.</p>
      </div>
    </article>`
  }));

  writePage('lists/best-faith-based-movies/index.html', buildListiclePage({
    slug: 'best-faith-based-movies',
    title: '10 Best Faith-Based Movies of All Time (Ranked by VirtueVigil Score)',
    description: 'The definitive ranking of the best Christian and faith-based films ever made, scored and analyzed using the VirtueVigil Woke-Watch methodology.',
    canonicalPath: 'lists/best-faith-based-movies',
    publishDate: '2026-03-23',
    htmlContent: `<article class="listicle-article">
      <p>Hollywood has a complicated relationship with faith. When it treats Christianity as a psychological disorder, a tool of institutional oppression, or a horror villain's calling card, the critical establishment applauds. When filmmakers take faith seriously, as something true and worthy of cinematic reverence, the industry either ignores them or condescends with faint praise about "passionate audiences."</p>

      <p>This list is for the audience that gets ignored. Ten films that treat faith not as a problem to be solved but as the animating force of a life worth living. Some of these were made by deeply devout filmmakers. Others were made by Hollywood outsiders who bet their own money on stories the studios would not touch. All of them succeeded because the audience showed up.</p>

      <p>VirtueVigil scored each film using our full Woke-Watch Scoring System. The scores below reflect content, not piety. A very low woke score combined with a high traditional score indicates a film aligned with conservative, faith-centered values. We note where reviewed films link to full analyses. For titles not yet in our database, we draw from cast and crew records, box office data, and content documentation.</p>

      <p>Rankings run from #10 to #1, ordered by VirtueVigil Traditional Score and overall alignment with faith-positive values.</p>

      <hr>

      <h2>#10 - Cabrini (2024)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 3.0</span>
        <span class="score-badge trad-score">Traditional Score: 72</span>
        <span class="score-badge verdict-traditional">TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Biography/Drama &bull; <strong>Platform:</strong> Theatrical / Angel Studios &bull; <strong>MPAA:</strong> PG-13</p>
      <p>Angel Studios, the company behind Sound of Freedom, distributed this story of Francesca Cabrini, an Italian immigrant nun who became America's first canonized saint. Director Alejandro Monteverde (Bella) brings the same earnest reverence he applied to that 2007 pro-life film. Cristiana Dell'Anna plays Cabrini as someone driven by pure conviction, fighting city officials, church bureaucrats, and a hostile Archbishop to build hospitals and schools for New York's most desperate immigrants in the 1880s. The film does not editorialize. It shows a woman whose faith was the source of her strength, not a crutch or a complication. The Catholic church is portrayed with complexity but not contempt. Cabrini's stubbornness is presented as saintly persistence, not a feminist rebuke of male authority. Box office: $24 million domestic against a modest budget. A quiet success for faith-based theatrical distribution.</p>
      <p><a href="/reviews/cabrini-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Cabrini</a></p>

      <hr>

      <h2>#9 - Father Stu (2022)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 2.0</span>
        <span class="score-badge trad-score">Traditional Score: 78</span>
        <span class="score-badge verdict-traditional">STRONGLY TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Biography/Drama &bull; <strong>Platform:</strong> Theatrical / Digital &bull; <strong>MPAA:</strong> R</p>
      <p>Mark Wahlberg produced and stars in this based-on-a-true-story film about Stuart Long, a hard-drinking former boxer who becomes a Catholic priest after a near-death accident and then ministers to incarcerated men while dying slowly from a degenerative muscle disease. The R rating is honest: this film does not sanitize Long's rough edges or his suffering. It earns its grace by refusing sentimentality. Mel Gibson co-stars as Long's estranged father. Wahlberg spent years developing it as a personal project, subsidizing production himself when no studio would fund it. The conversion arc is handled without condescension or manipulation. Long does not become a saint because God makes things easy. He becomes one because faith is what makes unbearable suffering bearable. One of the most unflinching and genuinely moving portrayals of conversion in American cinema.</p>
      <p><a href="/reviews/father-stu-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Father Stu</a></p>

      <hr>

      <h2>#8 - Hacksaw Ridge (2016)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 2.4</span>
        <span class="score-badge trad-score">Traditional Score: 81</span>
        <span class="score-badge verdict-traditional">TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> War/Biography/Drama &bull; <strong>Platform:</strong> Theatrical / Streaming &bull; <strong>MPAA:</strong> R</p>
      <p>Mel Gibson's return to directing after a decade in the Hollywood penalty box produced one of the decade's most powerful films about conscience, faith, and heroism. Andrew Garfield plays Desmond Doss, the only American conscientious objector to receive the Medal of Honor, a Seventh-day Adventist who refused to carry a weapon but served as a combat medic at Okinawa, saving 75 men while under fire. Gibson does not soften the brutality of the battle sequences, which rank among the most viscerally effective ever filmed. The faith is not decoration. Doss's refusal to compromise his beliefs, even under military pressure and the contempt of his fellow soldiers, is the entire point of the film. The awards season took notice: six Oscar nominations including Best Picture and Best Director. Gibson's personal faith informs every frame without becoming dogma. The film belongs to Garfield, whose performance is one of the finest of his career.</p>
      <p><a href="/reviews/hacksaw-ridge-2016/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Hacksaw Ridge</a></p>

      <hr>

      <h2>#7 - I Can Only Imagine (2018)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 1.2</span>
        <span class="score-badge trad-score">Traditional Score: 84</span>
        <span class="score-badge verdict-traditional">STRONGLY TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Biography/Drama/Music &bull; <strong>Platform:</strong> Theatrical / Digital &bull; <strong>MPAA:</strong> PG</p>
      <p>The true story behind MercyMe's Christian anthem, which became the best-selling Christian single in history, this film made $83 million domestic against a $7 million budget, one of the highest percentage returns in recent Hollywood history. J. Michael Finley plays Bart Millard, whose abusive father (Dennis Quaid, in a career-best performance) undergoes a transformative conversion that becomes the emotional core of the film and the source of the song. The Erwin Brothers directed with genuine craft, not just faith-market formula. The abuse is not minimized; the redemption is not handed out cheaply. This is a film about how faith can change a man who has given everyone around him reason to stop believing he can change. The box office proved the hunger for this kind of story. Hollywood noticed, quietly, and greenlit more. A direct precursor to the Angel Studios model of bypassing studio gatekeepers entirely.</p>

      <hr>

      <h2>#6 - The King of Kings (2025)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 0.0</span>
        <span class="score-badge trad-score">Traditional Score: 87</span>
        <span class="score-badge verdict-traditional">STRONGLY TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Animation/Biblical Epic &bull; <strong>Platform:</strong> Theatrical / Angel Studios &bull; <strong>MPAA:</strong> PG</p>
      <p>Angel Studios produced this animated retelling of the life of Jesus framed as a story told to the real-life Mark Twain, voiced by Kenneth Branagh, as he writes a novel about the Gospel accounts. The framing device is clever: it gives secular audiences a literary entry point while the biblical narrative unfolds with genuine reverence. The character animation is ambitious for independent production, and the Gospel sequences are handled with a fidelity that mainstream studios no longer attempt. Angel Studios crowdfunded the marketing campaign directly from their audience, bypassing traditional studio distribution deals entirely. That model has now become the template for faith-based theatrical releases. The woke score of 0.0 is not a floor; it reflects the absence of any material that conflicts with orthodox Christian values. For families looking for a film that treats the Gospel as history rather than mythology, this is the current gold standard in animated biblical content.</p>
      <p><a href="/reviews/the-king-of-kings-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The King of Kings</a></p>

      <hr>

      <h2>#5 - David (2025)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 2.0</span>
        <span class="score-badge trad-score">Traditional Score: 88</span>
        <span class="score-badge verdict-traditional">STRONGLY TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Animation/Musical/Biblical Epic &bull; <strong>Platform:</strong> Theatrical / Angel Studios &bull; <strong>MPAA:</strong> PG</p>
      <p>Angel Studios followed The King of Kings with this animated musical covering the life of David from his days as a shepherd boy through Goliath and into the complexities of kingship. The decision to make the biblical epic a musical was bold and it pays off: the songs advance the narrative rather than pausing it, and the score captures both the triumph and the genuine moral darkness in David's story. The film does not flinch from David's failures. Bathsheba is there. Uriah's death is there. A child's story this is not, and the filmmakers deserve credit for trusting the source material. VirtueVigil scored it as Strongly Traditional. The animation style draws from the best of western biblical illustration while incorporating Middle Eastern visual motifs that feel earned rather than decorative. Two biblically faithful animated musicals from the same studio in one year would have been unimaginable ten years ago. The audience that exists for these films is large and underserved.</p>
      <p><a href="/reviews/david-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of David</a></p>

      <hr>

      <h2>#4 - Sound of Freedom (2023)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 4.2</span>
        <span class="score-badge trad-score">Traditional Score: 89</span>
        <span class="score-badge verdict-traditional">STRONGLY TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Action/Thriller/Biography &bull; <strong>Platform:</strong> Theatrical / Digital &bull; <strong>MPAA:</strong> PG-13</p>
      <p>The film that proved the faith-based audience could move the market on its own terms. Jim Caviezel plays Tim Ballard, a Homeland Security agent who resigns his government position to rescue children from sex traffickers in South America. Angel Studios acquired the film after Disney shelved it for three years following their acquisition of Fox. The audience crowdfunded marketing, reserved seats in advance to fill theaters, and drove a $14 million opening weekend for a film without a single major studio advertisement. It ultimately grossed $250 million worldwide, more than Indiana Jones and the Dial of Destiny opened the same weekend. The mainstream press spent much of the summer fact-checking it rather than reviewing it. The audience did not care. The film's explicit Christian framing, Ballard is guided by faith throughout, and its portrayal of child trafficking as a moral absolute requiring action regardless of personal cost made it a cultural flashpoint. The most commercially successful faith-adjacent film of the last decade by return on investment.</p>
      <p><a href="/reviews/sound-of-freedom-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Sound of Freedom</a></p>

      <hr>

      <h2>#3 - God's Not Dead (2014)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 1.5</span>
        <span class="score-badge trad-score">Traditional Score: 90</span>
        <span class="score-badge verdict-traditional">STRONGLY TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Drama &bull; <strong>Platform:</strong> Theatrical / Digital &bull; <strong>MPAA:</strong> PG</p>
      <p>The film that built the modern faith-based theatrical market. Pure Flix's production about a college freshman who refuses to sign a statement declaring God does not exist in a philosophy class made $62 million on a $2 million budget, one of the most astonishing returns in independent film history. Kevin Sorbo plays the atheist professor as a committed antagonist, and the film does not pretend to neutrality: it is an explicit apologetics exercise designed for a church-going audience that felt its worldview was under siege in secular institutions. The argument scenes between Sorbo and Shane Harper (as the student, Josh Wheaton) are genuinely engaging even for viewers who disagree with the conclusions. Every Christian film distribution company that came after, from faith-based theatrical to Angel Studios' direct-audience model, traces its business logic back to what God's Not Dead proved was possible. It spawned three sequels and a cultural phenomenon. The woke score reflects the absence of progressive content; the traditional score reflects consistent, explicit, theologically sincere Christian framing throughout.</p>

      <hr>

      <h2>#2 - Risen (2016)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 0.8</span>
        <span class="score-badge trad-score">Traditional Score: 92</span>
        <span class="score-badge verdict-traditional">STRONGLY TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Biblical Drama/Historical &bull; <strong>Platform:</strong> Theatrical / Digital &bull; <strong>MPAA:</strong> PG-13</p>
      <p>One of the most underrated films in the faith genre, this dramatization of the Resurrection as seen through the eyes of a Roman tribune ordered to investigate the missing body of Jesus takes its premise with complete seriousness. Joseph Fiennes plays Clavius, a Roman soldier who witnessed crucifixions every week as a matter of military routine, and who is assigned by Pilate to ensure the disciples cannot claim a resurrection. The film's masterstroke is its perspective: we follow a skeptic doing a forensic investigation of events the audience already knows the answer to. When Clavius encounters the risen Christ, it lands as a dramatic revelation precisely because the film has spent its entire runtime inhabiting his unbelief. Director Kevin Reynolds brought more craft to the material than the faith film market typically receives, and the result is the rare biblical film that works both as historical drama and as devotional cinema. Widely overlooked, deeply rewatchable.</p>

      <hr>

      <h2>#1 - The Passion of the Christ (2004)</h2>
      <div class="listicle-scores">
        <span class="score-badge woke-score">Woke Score: 0.0</span>
        <span class="score-badge trad-score">Traditional Score: 97</span>
        <span class="score-badge verdict-traditional">STRONGLY TRADITIONAL</span>
      </div>
      <p class="listicle-meta"><strong>Genre:</strong> Biblical Drama &bull; <strong>Platform:</strong> Theatrical / Digital &bull; <strong>MPAA:</strong> R</p>
      <p>The most commercially successful independent film ever made. Mel Gibson spent $30 million of his own money to produce a film in Aramaic and Latin with no A-list cast, no studio backing, and no marketing budget. Major studios declined distribution. Gibson self-distributed. The Passion of the Christ made $611 million worldwide and became the highest-grossing R-rated film in history at the time of its release, a record it held for over a decade. The film focuses on the final 12 hours of Jesus's life with an unflinching commitment to physical and spiritual suffering that the mainstream industry would never have sanctioned. Jim Caviezel's performance required such physical and psychological intensity that he suffered a separated shoulder, hypothermia, lung infection, and was struck by lightning during production. Gibson's direction is without agenda beyond depicting the Gospel accounts as literally as cinema allows. The mainstream critical establishment was hostile. The audience bypassed the critics entirely and made it a cultural event. No faith-based film before or since has matched its combination of uncompromising conviction, artistic seriousness, and commercial dominance. The benchmark against which every Christian film is measured. VirtueVigil's traditional score of 97 is the highest in our database.</p>
      <p><a href="/reviews/the-passion-of-the-christ-2004/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of The Passion of the Christ</a></p>

      <hr>

      <div class="listicle-conclusion">
        <h3>Why These Films Matter</h3>
        <p>The faith-based film market is not a niche. It is a market that Hollywood systematically underserves because the people who greenlight films do not share the values of the people who buy tickets. The box office data above makes the case without needing commentary: modest budgets, enormous returns, audiences who show up in church groups and return for second and third viewings because the films mean something to them beyond entertainment.</p>

        <p>VirtueVigil exists partly to document what these films get right. A low woke score and a high traditional score do not mean a film is propaganda. The Passion of the Christ is not propaganda. It is one man's sincere, financially ruinous, commercially triumphant act of cinematic faith. Hacksaw Ridge is a war film that happens to believe its subject's religion made him genuinely heroic. Cabrini is a biopic about a woman whose accomplishments were inseparable from her vocation.</p>

        <p>Hollywood could make more of these. The data says they would make money. The industry's cultural gatekeepers have decided the audience for these films is not their audience. The audience has responded by finding other ways to get what they want. Angel Studios is the most visible result. It will not be the last.</p>

        <p>Browse our full review library to see how every faith-adjacent film we have analyzed scores. Our <a href="/methodology.html">Methodology page</a> explains how we calculate Traditional Score and Woke Score. And if you want to see what the opposite of this list looks like, read <a href="/lists/most-woke-movies-2024/">10 Most Woke Movies of 2024</a>.</p>
      </div>
    </article>`
  }));
  writePage('lists/conservative-sci-fi-movies/index.html', buildListiclePage({
    slug: 'conservative-sci-fi-movies',
    title: 'Best Sci-Fi Movies for Conservatives (Ranked by Values Score)',
    description: 'The best sci-fi movies ranked by traditional values score. Find space epics, action thrillers and classic sci-fi without the woke agenda.',
    canonicalPath: 'lists/conservative-sci-fi-movies',
    publishDate: '2026-03-23',
    htmlContent: `<article class="listicle-article">

      <p>Science fiction has always been a battleground. The genre that gave us totalitarian dystopias, cautionary tales about overreaching technology, and stories of individual courage against impossible odds has also become a prime delivery vehicle for progressive ideology. In recent years, the big studios have used sci-fi's built-in speculative canvas to insert lectures about systemic oppression, deconstruct masculinity, and replace heroism with victimhood. The result has been a string of expensive box office disappointments and a conservative audience that no longer trusts the genre it once loved.</p>

      <p>VirtueVigil has scored every major sci-fi release using our Woke-Watch Scoring System, a rigorous rubric that evaluates films for traditional and progressive content across more than 20 categories. These rankings are based on real data. The margin shown next to each title is the gap between the traditional score and the woke score. A higher TRAD margin means a cleaner film for conservative viewers. Use this list to find sci-fi worth watching, to filter out the preachy, and to share with friends who have given up on Hollywood. The genre is not dead. You just have to know where to look.</p>

      <hr>

      <h2>#1 - <a href="/reviews/spider-man-no-way-home-2021/">Spider-Man: No Way Home</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 22.05</span>
        <span class="mini-score woke">WOKE: 3.5</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +19 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2021 &bull; <strong>Margin:</strong> +19 TRAD</p>
      <p>Spider-Man: No Way Home is not just the best Spider-Man film ever made. It is a film about sacrifice, responsibility, and the cost of love. Peter Parker does not choose the easy path. He chooses the right one, erasing himself from every person he loves to save the world from multiversal chaos. The themes here are ancient: duty over self, sacrifice without recognition, the weight of a moral code that does not bend. Marvel has never made a film more aligned with traditional values, and it is also one of the most emotionally devastating blockbusters of the past decade.</p>
      <p><a href="/reviews/spider-man-no-way-home-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Spider-Man: No Way Home</a></p>
      <hr>

      <h2>#2 - <a href="/reviews/war-machine-2026/">War Machine</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 22</span>
        <span class="mini-score woke">WOKE: 4</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +18 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2026 &bull; <strong>Margin:</strong> +18 TRAD</p>
      <p>War Machine is a glorious throwback to the testosterone-fueled sci-fi action films of the 1980s. Patrick Hughes delivers a squad-based military thriller that could sit comfortably beside Predator and Aliens. Chain of command is sacred. Brotherhood is earned. Sacrifice is real. There is no identity politics, no lectures, and no apologies for masculine competence. If you are a conservative who has been burned by Hollywood action films over the last decade, War Machine is the antidote.</p>
      <p><a href="/reviews/war-machine-2026/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of War Machine</a></p>
      <hr>

      <h2>#3 - <a href="/reviews/inception-2010/">Inception</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 20.44</span>
        <span class="mini-score woke">WOKE: 2.9</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +18 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2010 &bull; <strong>Margin:</strong> +18 TRAD</p>
      <p>Christopher Nolan's heist-in-dreams masterpiece is driven by masculine grief, fatherly love, and moral accountability. Dom Cobb is not running from the law because the system is unjust. He is running because he made a catastrophic choice and is living with it. His mission is not vengeance or revolution. It is to get home to his children. The film treats fatherhood as the most powerful force in the universe, and Nolan's craftsmanship makes that argument feel true on a visceral level.</p>
      <p><a href="/reviews/inception-2010/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Inception</a></p>
      <hr>

      <h2>#4 - <a href="/reviews/tenet-2020/">Tenet</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 17.23</span>
        <span class="mini-score woke">WOKE: 1.5</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +16 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2020 &bull; <strong>Margin:</strong> +16 TRAD</p>
      <p>Tenet is Christopher Nolan's most technically ambitious film and also one of the most apolitical blockbusters of the decade. There is no progressive agenda here, no lectures about systems or privilege. What exists is classical heroic storytelling: duty over personal interest, sacrifice for a larger good, masculine competence in service of humanity's survival. The Protagonist operates in a world of moral clarity. He does what needs to be done because it must be done. Conservatives will find this deeply satisfying.</p>
      <p><a href="/reviews/tenet-2020/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Tenet</a></p>
      <hr>

      <h2>#5 - <a href="/reviews/guardians-of-the-galaxy-2014/">Guardians of the Galaxy</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 21.28</span>
        <span class="mini-score woke">WOKE: 5.82</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +15 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2014 &bull; <strong>Margin:</strong> +15 TRAD</p>
      <p>The best MCU origin film by a wide margin, and one of the most traditionally coded superhero movies ever produced. Guardians of the Galaxy is built on redemption arcs, sacrificial love, and a found family forged through genuine need rather than political mandate. Groot's sacrifice alone earns its TRADITIONAL verdict. Star-Lord's 26-year grief for his mother anchors the entire film in something real. James Gunn made a film about broken people choosing to be better, and it works because it is honest about why they were broken to begin with.</p>
      <p><a href="/reviews/guardians-of-the-galaxy-2014/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Guardians of the Galaxy</a></p>
      <hr>

      <h2>#6 - <a href="/reviews/interstellar-2014/">Interstellar</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 23.16</span>
        <span class="mini-score woke">WOKE: 7.72</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +15 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2014 &bull; <strong>Margin:</strong> +15 TRAD</p>
      <p>Christopher Nolan's space epic treats fatherhood as a literally universal force. Cooper leaves his daughter because humanity's survival demands it, and the film never lets us forget the cost of that choice. Masculine duty and sacrifice are portrayed as heroic without irony. Science and spiritual awe coexist here rather than fight each other. Interstellar is one of Hollywood's most traditionally grounded blockbusters, wrapped in genuine scientific rigor and extraordinary filmmaking. The ending will wreck you.</p>
      <p><a href="/reviews/interstellar-2014/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Interstellar</a></p>
      <hr>

      <h2>#7 - <a href="/reviews/furiosa-a-mad-max-saga-2024/">Furiosa: A Mad Max Saga</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 22</span>
        <span class="mini-score woke">WOKE: 8</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +14 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2024 &bull; <strong>Margin:</strong> +14 TRAD</p>
      <p>The online discourse called Furiosa woke. The online discourse was wrong. George Miller's prequel is a revenge story driven by family loyalty and the desire to reclaim something stolen. Furiosa does not want to dismantle systems. She wants to go home. Her decade-long campaign is not about ideology. It is about the primal drive to return to where you came from and make right what was taken. The Wasteland has a clear moral order. Evil is unmistakably evil. And the climax rewards endurance over protest.</p>
      <p><a href="/reviews/furiosa-a-mad-max-saga-2024/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Furiosa: A Mad Max Saga</a></p>
      <hr>

      <h2>#8 - <a href="/reviews/greenland-2-migration-2026/">Greenland 2: Migration</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 18.62</span>
        <span class="mini-score woke">WOKE: 5.05</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +14 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2026 &bull; <strong>Margin:</strong> +14 TRAD</p>
      <p>Greenland 2: Migration is a deeply traditional film wearing post-apocalyptic clothes. Strip away the CGI meteor showers and frozen landscapes, and what remains is the oldest story in the book: a dying father walks his family across a ruined world to find safety. Gerard Butler plays a traditional patriarch who scouts, protects, and makes brutal decisions to keep his family alive. The migration subplot is handled literally rather than politically. This is a film about family survival, paternal sacrifice, and the will to endure. Nothing more, and nothing less.</p>
      <p><a href="/reviews/greenland-2-migration-2026/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Greenland 2: Migration</a></p>
      <hr>

      <h2>#9 - <a href="/reviews/dune-part-one-2021/">Dune: Part One</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 20.02</span>
        <span class="mini-score woke">WOKE: 7.1</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +13 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2021 &bull; <strong>Margin:</strong> +13 TRAD</p>
      <p>Denis Villeneuve's Dune is a serious, morally complex epic that honors duty, sacrifice, and the weight of leadership while warning against the seductive danger of messianic politics. Paul Atreides does not want the throne. He understands that power corrupts and that destiny is a cage. The film takes religion, tribal loyalty, and martial tradition seriously. The Fremen are not a metaphor for progressive grievance. They are a people with a code, a culture, and a homeland worth defending. Villeneuve directs it all with a gravity that modern blockbusters rarely attempt.</p>
      <p><a href="/reviews/dune-part-one-2021/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Dune: Part One</a></p>
      <hr>

      <h2>#10 - <a href="/reviews/nope-2022/">Nope</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 30</span>
        <span class="mini-score woke">WOKE: 20</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +10 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2022 &bull; <strong>Margin:</strong> +10 TRAD</p>
      <p>Jordan Peele's third film is his most formally ambitious and his most politically restrained. Nope centers a Black family whose legacy in Hollywood stretches back to the first moving image of a man on horseback. They fight to keep their land, their horses, and their dignity against a supernatural predator and a cynical industry that would commodify their survival. The film is a warning about spectacle culture and the exploitation of authentic people by those who profit from their pain. Its traditional score reflects genuine themes of family, legacy, land, and the refusal to be consumed.</p>
      <p><a href="/reviews/nope-2022/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Nope</a></p>
      <hr>

      <h2>#11 - <a href="/reviews/pluribus-2025/">Pluribus (2025)</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL</span>
        <span class="mini-score trad">TRAD: 27.51</span>
        <span class="mini-score woke">WOKE: 15.6</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +12 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2025 &bull; <strong>Margin:</strong> +12 TRAD</p>
      <p>Vince Gilligan's first series after Breaking Bad and Better Call Saul is the rarest thing in prestige television: a show that genuinely refuses to tell you what to think. Pluribus is a sci-fi drama that presents individual liberty, skepticism toward centralized power, and the dangers of ideological conformity as real threats worth dramatizing. It is not a conservative show, but it is a show that treats conservative concerns as legitimate. In an era when most prestige television signals its progressive credentials in the first five minutes, that makes Pluribus remarkable.</p>
      <p><a href="/reviews/pluribus-2025/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Pluribus</a></p>
      <hr>

      <h2>#12 - <a href="/reviews/guardians-of-the-galaxy-vol-3-2023/">Guardians of the Galaxy Vol. 3</a></h2>
      <div class="listicle-scores">
        <span class="verdict-badge traditional">TRADITIONAL LEAN</span>
        <span class="mini-score trad">TRAD: 14.36</span>
        <span class="mini-score woke">WOKE: 5.18</span>
        <span class="mini-score" style="color:var(--accent-amber);">MARGIN: +9 TRAD</span>
      </div>
      <p class="listicle-meta"><strong>Year:</strong> 2023 &bull; <strong>Margin:</strong> +9 TRAD</p>
      <p>James Gunn's farewell to the Guardians is the most emotionally ambitious MCU film since Endgame. Rocket's backstory is a meditation on abuse, survival, and the right of a created being to choose its own destiny. The High Evolutionary is one of Marvel's most genuinely monstrous villains because his evil is ideological: he believes in perfection through control and sees individual variation as a defect to eliminate. Gunn argues the opposite. What makes the Guardians worth saving is precisely their imperfection, their damage, and their choice to love each other anyway.</p>
      <p><a href="/reviews/guardians-of-the-galaxy-vol-3-2023/" class="listicle-review-link"><i class="fas fa-arrow-right"></i> Read the full VirtueVigil review of Guardians of the Galaxy Vol. 3</a></p>

      <hr>

      <div class="listicle-conclusion">
        <h3>Browse More at VirtueVigil</h3>
        <p>Science fiction at its best asks the biggest questions: What does it mean to be human? What are we willing to sacrifice for the people we love? What happens when power goes unchecked? The films on this list answer those questions with stories that take duty, family, sacrifice, and moral clarity seriously. They are proof that the genre does not have to be a vehicle for progressive ideology. Browse more reviews and rankings at VirtueVigil.com, where every score is earned and nothing is taken on trust.</p>
      </div>
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

  // --- TikTok demo page ---
  const tiktokDir = path.join(DIST, 'tiktok');
  if (!fs.existsSync(tiktokDir)) fs.mkdirSync(tiktokDir, { recursive: true });
  fs.copyFileSync(path.join(__dirname, 'src', 'tiktok', 'index.html'), path.join(tiktokDir, 'index.html'));
  console.log('  TikTok demo page');

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

module.exports = { buildListiclePage, writePage };
