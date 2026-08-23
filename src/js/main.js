/* ============================================
   VirtueVigil — Main JavaScript
   ============================================ */

// --- GA4 Engagement Tracking Helper ---
function trackEngagement(eventName, params) {
  if (typeof gtag !== 'undefined') {
    gtag('event', eventName, params);
  }
}

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

  // --- Newsletter form ---
  document.querySelectorAll('.email-sub-form').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      const btn = form.querySelector('button');
      const msg = form.querySelector('.sub-message');
      if (!input || !input.value) return;

      const email = input.value.trim();
      const source = form.dataset.source || 'unknown';

      // Fire GA4 subscribe_attempt
      trackEngagement('subscribe_attempt', { source });

      btn.disabled = true;
      btn.textContent = 'Subscribing...';
      if (msg) { msg.style.display = 'none'; }

      try {
        const res = await fetch('/api/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, source }),
        });
        const data = await res.json();
        if (data.success) {
          trackEngagement('subscribe_success', { source });
          btn.textContent = 'Subscribed!';
          btn.style.background = '#4caf50';
          input.value = '';
          if (msg) {
            msg.textContent = data.message || 'You\'re in! Check your inbox.';
            msg.className = 'sub-message success';
            msg.style.display = '';
          }
        } else {
          trackEngagement('subscribe_error', { source, error_message: data.error || 'unknown' });
          btn.textContent = 'Subscribe';
          btn.disabled = false;
          if (msg) {
            msg.textContent = data.error || 'Something went wrong.';
            msg.className = 'sub-message error';
            msg.style.display = '';
          }
        }
      } catch (err) {
        trackEngagement('subscribe_error', { source, error_message: 'network' });
        btn.textContent = 'Subscribe';
        btn.disabled = false;
        if (msg) {
          msg.textContent = 'Network error. Please try again.';
          msg.className = 'sub-message error';
          msg.style.display = '';
        }
      }
    });
  });

  // --- GA4 Related Review Click Tracking ---
  document.querySelectorAll('.related-review-card').forEach(card => {
    card.addEventListener('click', function(e) {
      const position = this.dataset.position || '0';
      const href = this.getAttribute('href') || '';
      const reviewSlug = document.querySelector('.comments-section')?.dataset.slug || '';
      const relatedSlug = href.replace('/reviews/', '').replace('/', '');
      trackEngagement('related_click', {
        review_slug: reviewSlug,
        related_slug: relatedSlug,
        position: Number(position)
      });
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
  const searchInput = document.getElementById('site-search-input');
  const searchResults = document.getElementById('site-search-results');
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
    if (!searchResults) return;
    const q = query.toLowerCase().trim();
    if (!q) { searchResults.hidden = true; searchResults.innerHTML = ''; return; }
    if (!searchIndex) return;

    const matches = searchIndex.filter(r =>
      r.title.toLowerCase().includes(q) ||
      (r.verdict && r.verdict.toLowerCase().includes(q)) ||
      (r.platform && r.platform.toLowerCase().includes(q)) ||
      (r.genre && r.genre.toLowerCase().includes(q)) ||
      (r.type && r.type.toLowerCase().includes(q))
    ).slice(0, 8);

    searchResults.hidden = false;
    if (!matches.length) {
      searchResults.innerHTML = '<p class="site-search-noresults">No reviews found for "' + query + '"</p>';
      return;
    }

    searchResults.innerHTML = matches.map(r => {
      const vc = verdictClass(r.verdict);
      const posterHtml = r.poster
        ? `<img src="${r.poster}" alt="${r.title}" class="site-search-result-poster">`
        : `<div class="site-search-poster-placeholder">${r.title.charAt(0)}</div>`;
      return `<a href="/reviews/${r.slug}/" class="site-search-result-item">
        ${posterHtml}
        <div class="search-result-info">
          <div class="site-search-result-title">${r.title}</div>
          <div class="site-search-result-meta">${r.year} &middot; ${r.platform}</div>
          <span class="verdict-badge ${vc}" style="font-size:0.7rem;padding:2px 8px;">${r.verdict}</span>
        </div>
      </a>`;
    }).join('');
  }

  if (searchInput) {
    searchInput.addEventListener('focus', () => {
      loadIndex();
    });
    searchInput.addEventListener('input', () => renderResults(searchInput.value));
    document.addEventListener('click', e => {
      if (!e.target.closest('.site-search-bar')) {
        if (searchResults) { searchResults.hidden = true; }
      }
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && searchResults) { searchResults.hidden = true; searchInput.blur(); }
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        searchInput.focus();
        loadIndex();
      }
    });
  }
})();
}); // end DOMContentLoaded for search
