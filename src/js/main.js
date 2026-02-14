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

  // --- Search overlay (basic) ---
  const searchToggle = document.querySelector('.search-toggle');
  const searchOverlay = document.querySelector('.search-overlay');
  if (searchToggle && searchOverlay) {
    searchToggle.addEventListener('click', () => {
      searchOverlay.classList.toggle('active');
      if (searchOverlay.classList.contains('active')) {
        searchOverlay.querySelector('input')?.focus();
      }
    });
    searchOverlay.addEventListener('click', (e) => {
      if (e.target === searchOverlay) searchOverlay.classList.remove('active');
    });
  }

  console.log('VirtueVigil initialized.');
});
