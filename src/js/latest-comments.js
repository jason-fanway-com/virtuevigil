/* ============================================
   VirtueVigil -- Latest Comments Widget
   Handles three contexts:
     1. Sidebar (.latest-comments-widget #vv-latest-comments)
     2. Homepage section (.homepage-latest-comments #vv-latest-comments-home)
     3. Full page (#vv-comments-full-list, with pagination)
   Degrades gracefully if Supabase is unreachable.
   ============================================ */

(function() {
  'use strict';

  var SUPABASE_URL = 'https://fdxvflryvctvstxdbdtm.supabase.co';
  var SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZkeHZmbHJ5dmN0dnN0eGRiZHRtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzExMjQ3MjEsImV4cCI6MjA4NjcwMDcyMX0.wn80dndvXLUU6qMzJW1DBuz0d6cPMu4iEO3UA6QnF4E';

  var DEFAULT_AVATAR = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='50' fill='%231a1a26'/%3E%3Ccircle cx='50' cy='38' r='18' fill='%23c9a84c'/%3E%3Cellipse cx='50' cy='78' rx='30' ry='22' fill='%23c9a84c'/%3E%3C/svg%3E";

  var COMMENTS_PER_PAGE = 15;
  var slugTitles = window.VV_REVIEW_TITLES || {};

  function esc(s) {
    var el = document.createElement('div');
    el.textContent = s || '';
    return el.innerHTML;
  }

  function relativeTime(dateStr) {
    var now = new Date();
    var d = new Date(dateStr);
    var diffSec = Math.floor((now - d) / 1000);
    var diffMin = Math.floor(diffSec / 60);
    var diffHr = Math.floor(diffMin / 60);
    var diffDay = Math.floor(diffHr / 24);
    var diffWk = Math.floor(diffDay / 7);
    var diffMo = Math.floor(diffDay / 30);

    if (diffSec < 60) return 'just now';
    if (diffMin < 60) return diffMin + 'm ago';
    if (diffHr < 24) return diffHr + 'h ago';
    if (diffDay < 7) return diffDay + 'd ago';
    if (diffWk < 5) return diffWk + 'w ago';
    if (diffMo < 12) return diffMo + 'mo ago';
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  }

  function truncate(str, max) {
    if (!str) return '';
    str = String(str).replace(/\s+/g, ' ').trim();
    return str.length <= max ? str : str.slice(0, max - 3) + '...';
  }

  function reviewLink(slug) {
    return '<a href="/reviews/' + esc(slug) + '/">' + esc(slugTitles[slug] || slug) + '</a>';
  }

  function reviewTitle(slug) {
    return slugTitles[slug] || slug;
  }

  // ============ API fetch ============

  async function fetchComments(limit) {
    var url = SUPABASE_URL + '/rest/v1/comments?select=*&is_hidden=eq.false&order=created_at.desc';
    if (limit) url += '&limit=' + limit;
    var resp = await fetch(url, {
      headers: { 'apikey': SUPABASE_ANON_KEY, 'Authorization': 'Bearer ' + SUPABASE_ANON_KEY }
    });
    if (!resp.ok) throw new Error('Supabase returned ' + resp.status);
    return resp.json();
  }

  // ============ Sidebar (5 comments, compact lc-item format) ============

  async function renderSidebar(container) {
    try {
      var comments = await fetchComments(5);
      if (!comments || !comments.length) {
        container.innerHTML = '<p class="lc-empty" style="color:var(--text-muted);font-size:0.82rem;">No comments yet.</p>';
        return;
      }

      var html = '';
      for (var i = 0; i < comments.length; i++) {
        var c = comments[i];
        html += '<div class="lc-item">' +
          '<div class="lc-header">' +
            '<div class="lc-meta">' +
              '<span class="lc-review-link">' + reviewLink(c.review_slug) + '</span>' +
              ' <span class="lc-time">' + relativeTime(c.created_at) + '</span>' +
            '</div>' +
          '</div>' +
          '<p class="lc-text">' + esc(truncate(c.content, 100)) + '</p>' +
        '</div>';
      }
      html += '<a class="lc-all-link" href="/comments/">View all comments <i class="fas fa-arrow-right"></i></a>';
      container.innerHTML = html;
    } catch (e) {
      container.style.display = 'none';
    }
  }

  // ============ Homepage section (5 comments, grid layout) ============

  async function renderHomepage(container) {
    try {
      var comments = await fetchComments(5);
      if (!comments || !comments.length) {
        container.innerHTML = '<div class="latest-comments-empty">No comments yet. Be the first to share your thoughts!</div>';
        return;
      }

      var html = '<div class="latest-comments-list">';
      for (var i = 0; i < comments.length; i++) {
        var c = comments[i];
        var rTitle = reviewTitle(c.review_slug);
        html += '<div class="latest-comment-item">' +
          '<a class="latest-comment-link" href="/reviews/' + esc(c.review_slug) + '/">' +
            '<img class="latest-comment-avatar" src="' + DEFAULT_AVATAR + '" alt="" width="36" height="36" loading="lazy">' +
            '<div class="latest-comment-body">' +
              '<span class="latest-comment-author">' + esc(truncate(rTitle, 40)) + '</span>' +
              '<span class="latest-comment-text">' + esc(truncate(c.content, 120)) + '</span>' +
              '<span class="latest-comment-meta">' + relativeTime(c.created_at) + '</span>' +
            '</div>' +
          '</a>' +
        '</div>';
      }
      html += '</div>';
      container.innerHTML = html;
    } catch (e) {
      // Degrade gracefully: hide the section
      var parent = container.closest('.homepage-latest-comments');
      if (parent) parent.style.display = 'none';
    }
  }

  // ============ Full page (all comments, paginated) ============

  var allComments = [];
  var currentPage = 1;

  async function renderFullPage(container, paginationEl) {
    try {
      allComments = await fetchComments(200); // fetch all non-hidden
      currentPage = 1;

      // Update total count
      var countEl = document.getElementById('vv-comment-total-count');
      if (countEl) {
        countEl.textContent = allComments.length + ' comment' + (allComments.length !== 1 ? 's' : '');
      }

      if (!allComments || !allComments.length) {
        container.innerHTML = '<div class="cp-empty">No comments yet. Be the first to join the discussion!</div>';
        if (paginationEl) paginationEl.innerHTML = '';
        return;
      }

      renderPage(container, paginationEl);
    } catch (e) {
      container.innerHTML = '<div class="cp-empty" style="color:var(--accent-red);">Unable to load comments right now. Please try again later.</div>';
    }
  }

  function renderPage(container, paginationEl) {
    var totalPages = Math.ceil(allComments.length / COMMENTS_PER_PAGE);
    var start = (currentPage - 1) * COMMENTS_PER_PAGE;
    var pageComments = allComments.slice(start, start + COMMENTS_PER_PAGE);

    var html = '';
    for (var i = 0; i < pageComments.length; i++) {
      var c = pageComments[i];
      var rTitle = reviewTitle(c.review_slug);
      html += '<div class="cp-item">' +
        '<div class="cp-header">' +
          '<img class="comment-avatar" src="' + DEFAULT_AVATAR + '" alt="" width="32" height="32" loading="lazy">' +
          '<a class="cp-review-link" href="/reviews/' + esc(c.review_slug) + '/">' + esc(rTitle) + '</a>' +
          '<span class="cp-time">' + relativeTime(c.created_at) + '</span>' +
        '</div>' +
        '<div class="cp-body">' + esc(c.content) + '</div>' +
      '</div>';
    }
    container.innerHTML = html;

    // Pagination controls
    if (paginationEl && totalPages > 1) {
      var pagHTML = '';
      pagHTML += '<div class="comments-pagination">';
      pagHTML += '<button class="btn-page" ' + (currentPage <= 1 ? 'disabled' : '') + ' data-page="' + (currentPage - 1) + '"><i class="fas fa-chevron-left"></i> Newer</button>';
      pagHTML += '<span class="page-info">Page ' + currentPage + ' of ' + totalPages + '</span>';
      pagHTML += '<button class="btn-page" ' + (currentPage >= totalPages ? 'disabled' : '') + ' data-page="' + (currentPage + 1) + '">Older <i class="fas fa-chevron-right"></i></button>';
      pagHTML += '</div>';
      paginationEl.innerHTML = pagHTML;

      // Attach listeners
      var buttons = paginationEl.querySelectorAll('.btn-page');
      for (var j = 0; j < buttons.length; j++) {
        buttons[j].addEventListener('click', function() {
          if (this.disabled) return;
          var page = parseInt(this.dataset.page);
          if (page >= 1 && page <= totalPages) {
            currentPage = page;
            renderPage(container, paginationEl);
            container.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        });
      }
    } else if (paginationEl) {
      paginationEl.innerHTML = '';
    }
  }

  // ============ Init ============

  function init() {
    // 1. Sidebar widget (any page that has sidebar with .latest-comments-widget)
    var sidebarEl = document.querySelector('.latest-comments-widget #vv-latest-comments');
    if (sidebarEl) { renderSidebar(sidebarEl); }

    // 2. Homepage dedicated section
    var homeEl = document.querySelector('.homepage-latest-comments #vv-latest-comments-home');
    if (homeEl) { renderHomepage(homeEl); }

    // 3. Full /comments/ page
    var fullList = document.getElementById('vv-comments-full-list');
    var pagination = document.getElementById('vv-comments-pagination');
    if (fullList) { renderFullPage(fullList, pagination); }
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();