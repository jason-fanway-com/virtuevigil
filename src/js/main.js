/* ============================================
   VirtueVigil — Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  // --- Mobile Navigation Toggle ---
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', nav.classList.contains('open'));
    });
    // Close nav when clicking a link
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => nav.classList.remove('open'));
    });
  }

  // --- Scroll Animation Observer ---
  const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  document.querySelectorAll('.review-card, .about-card, .spokesperson').forEach(el => {
    observer.observe(el);
  });

  // --- Score Bar Animation ---
  const barObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bars = entry.target.querySelectorAll('.bar-fill');
        bars.forEach(bar => {
          const width = bar.getAttribute('data-width');
          if (width) bar.style.width = width;
        });
        barObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  document.querySelectorAll('.method-bar-container').forEach(el => barObserver.observe(el));

  // --- Sidebar active state ---
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.main-nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === 'index.html' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // --- Newsletter form (placeholder) ---
  document.querySelectorAll('.sidebar-newsletter form, .footer-newsletter form').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      const btn = form.querySelector('button');
      if (input && input.value) {
        btn.textContent = 'Subscribed!';
        btn.style.background = '#4caf50';
        input.value = '';
        setTimeout(() => {
          btn.textContent = 'Subscribe';
          btn.style.background = '';
        }, 3000);
      }
    });
  });

  // --- Smooth scrolling for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // --- Header shrink on scroll ---
  let lastScroll = 0;
  const header = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > 100 && header) {
      header.style.boxShadow = '0 2px 24px rgba(0,0,0,0.5)';
    } else if (header) {
      header.style.boxShadow = '';
    }
    lastScroll = currentScroll;
  }, { passive: true });

  console.log('VirtueVigil initialized.');
});

// --- Search ---
document.addEventListener('DOMContentLoaded', function() {
(function() {
  const searchToggle = document.querySelector('.search-toggle');
  const searchOverlay = document.querySelector('.search-overlay');
  const searchInput = searchOverlay && searchOverlay.querySelector('.search-input');
  const searchResults = searchOverlay && document.getElementById('search-results');
  const searchClose = searchOverlay && searchOverlay.querySelector('.search-close');
  let searchIndex = null;

  function loadIndex() {
    if (searchIndex) return Promise.resolve();
    return fetch('/search-index.json').then(r => r.json()).then(data => { searchIndex = data; });
  }

  function verdictClass(v) {
    if (!v) return 'mixed';
    const lv = v.toUpperCase();
    if (lv.includes('WOKE')) return 'woke';
    if (lv.includes('TRADITIONAL')) return 'traditional';
    return 'mixed';
  }

  function renderResults(query) {
    if (!searchIndex) return;
    const q = query.toLowerCase().trim();
    if (!q) {
      searchResults.innerHTML = '<p class="search-hint">Start typing to search all reviews...</p>';
      return;
    }
    const matches = searchIndex.filter(r =>
      r.title.toLowerCase().includes(q) ||
      (r.verdict && r.verdict.toLowerCase().includes(q)) ||
      (r.platform && r.platform.toLowerCase().includes(q)) ||
      (r.genre && r.genre.toLowerCase().includes(q)) ||
      (r.type && r.type.toLowerCase().includes(q))
    ).slice(0, 8);

    if (!matches.length) {
      searchResults.innerHTML = '<p class="search-no-results">No reviews found. Try a different search.</p>';
      return;
    }

    searchResults.innerHTML = matches.map(r => {
      const vc = verdictClass(r.verdict);
      const posterHtml = r.poster
        ? `<img src="${r.poster}" alt="${r.title}" class="search-result-poster">`
        : `<div class="search-result-poster search-poster-placeholder">${r.title.charAt(0)}</div>`;
      return `<a href="/reviews/${r.slug}/" class="search-result-item">
        ${posterHtml}
        <div class="search-result-info">
          <div class="search-result-title">${r.title}</div>
          <div class="search-result-meta">${r.year} &middot; ${r.platform}</div>
          <span class="verdict-badge ${vc} search-verdict">${r.verdict}</span>
        </div>
      </a>`;
    }).join('');
  }

  if (searchToggle) {
    searchToggle.addEventListener('click', () => {
      searchOverlay.classList.add('active');
      loadIndex().then(() => {
        searchInput && searchInput.focus();
      });
    });
  }

  if (searchClose) {
    searchClose.addEventListener('click', () => searchOverlay.classList.remove('active'));
  }

  if (searchOverlay) {
    searchOverlay.addEventListener('click', e => {
      if (e.target === searchOverlay) searchOverlay.classList.remove('active');
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') searchOverlay.classList.remove('active');
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        searchOverlay.classList.add('active');
        loadIndex().then(() => searchInput && searchInput.focus());
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', () => renderResults(searchInput.value));
  }
})();
}); // end DOMContentLoaded for search
