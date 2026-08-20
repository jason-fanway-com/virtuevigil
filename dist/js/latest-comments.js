/* ============================================
   VirtueVigil -- Latest Comments Widget & Page
   Client-side Supabase query for three contexts:
   1. Sidebar widget   (#vv-latest-comments) -- compact list, all pages
   2. Homepage section  (#vv-latest-comments-home) -- card layout
   3. Full /comments/   (#vv-comments-full-list) -- all comments
   ============================================ */

(function() {
  'use strict';

  var SUPABASE_URL = 'https://fdxvflryvctvstxdbdtm.supabase.co';
  var SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZkeHZmbHJ5dmN0dnN0eGRiZHRtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzExMjQ3MjEsImV4cCI6MjA4NjcwMDcyMX0.wn80dndvXLUU6qMzJW1DBuz0d6cPMu4iEO3UA6QnF4E';

  // ---- Helpers ----

  function esc(s) {
    var el = document.createElement('div');
    el.textContent = s || '';
    return el.innerHTML;
  }

  function relativeTime(dateStr) {
    var now = Date.now();
    var d = new Date(dateStr).getTime();
    var sec = Math.floor((now - d) / 1000);
    var min = Math.floor(sec / 60);
    var hr  = Math.floor(min / 60);
    var day = Math.floor(hr / 24);
    var wk  = Math.floor(day / 7);
    var mo  = Math.floor(day / 30);
    if (sec < 60) return 'just now';
    if (min < 60) return min + 'm ago';
    if (hr  < 24) return hr + 'h ago';
    if (day < 7)  return day + 'd ago';
    if (wk  < 5)  return wk + 'w ago';
    if (mo  < 12) return mo + 'mo ago';
    return new Date(dateStr).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  }

  function truncate(str, max) {
    if (!str) return '';
    str = String(str).replace(/\s+/g, ' ').trim();
    return str.length <= max ? str : str.slice(0, max - 3) + '...';
  }

  // ---- Fetch comments with profile join ----

  async function fetchComments(limit) {
    var url = SUPABASE_URL + '/rest/v1/comments?select=*,profiles(display_name,avatar_url)&is_hidden=eq.false&order=created_at.desc';
    if (limit) url += '&limit=' + limit;
    var resp = await fetch(url, {
      headers: { 'apikey': SUPABASE_ANON_KEY, 'Authorization': 'Bearer ' + SUPABASE_ANON_KEY }
    });
    if (!resp.ok) throw new Error('Supabase returned ' + resp.status);
    return resp.json();
  }

  // ---- Render: Sidebar widget (compact) ----

  function renderSidebar(container, comments) {
    if (!comments || !comments.length) {
      container.innerHTML = '<p class="lc-empty">No comments yet. Be the first!</p>';
      return;
    }
    var titles = window.VV_REVIEW_TITLES || {};
    var html = '';
    for (var i = 0; i < comments.length; i++) {
      var c = comments[i];
      var title = titles[c.review_slug] || c.review_slug || 'Unknown review';
      var name = (c.profiles && c.profiles.display_name) ? c.profiles.display_name : '';
      var avatar = (c.profiles && c.profiles.avatar_url) ? c.profiles.avatar_url : '';

      html += '<div class="lc-item">' +
        '<div class="lc-header">' +
          (avatar ? '<img class="lc-avatar" src="' + esc(avatar) + '" alt="" loading="lazy" onerror="this.style.display=\'none\'">' : '') +
          '<div class="lc-meta">' +
            (name ? '<span class="lc-author">' + esc(name) + '</span>' : '') +
            '<a class="lc-review-link" href="/reviews/' + esc(c.review_slug) + '/">' + esc(title) + '</a>' +
            ' <span class="lc-time">' + relativeTime(c.created_at) + '</span>' +
          '</div>' +
        '</div>' +
        '<p class="lc-text">' + esc(truncate(c.content, 100)) + '</p>' +
      '</div>';
    }
    html += '<a class="lc-all-link" href="/comments/">View all comments <i class="fas fa-arrow-right"></i></a>';
    container.innerHTML = html;
  }

  // ---- Render: Homepage section (cards) ----

  function renderHomepage(container, comments) {
    if (!comments || !comments.length) {
      container.innerHTML = '<p class="latest-comments-empty">No community discussion yet. <a href="/reviews/">Browse reviews</a> and be the first to comment.</p>';
      return;
    }
    var titles = window.VV_REVIEW_TITLES || {};
    var html = '<div class="latest-comments-list">';
    for (var i = 0; i < comments.length; i++) {
      var c = comments[i];
      var title = titles[c.review_slug] || c.review_slug || 'Unknown review';
      var name = (c.profiles && c.profiles.display_name) ? c.profiles.display_name : '';
      var avatar = (c.profiles && c.profiles.avatar_url) ? c.profiles.avatar_url : '';

      html += '<div class="latest-comment-item">' +
        '<a class="latest-comment-link" href="/reviews/' + esc(c.review_slug) + '/">' +
          '<div class="latest-comment-body">' +
            (avatar ? '<img class="latest-comment-avatar" src="' + esc(avatar) + '" alt="" loading="lazy" onerror="this.style.display=\'none\'">' : '') +
            '<div>' +
              '<div class="latest-comment-author">' + (name ? esc(name) : 'Anonymous') + '</div>' +
              '<p class="latest-comment-text">' + esc(truncate(c.content, 180)) + '</p>' +
              '<div class="latest-comment-meta">on <strong>' + esc(title) + '</strong> &middot; ' + relativeTime(c.created_at) + '</div>' +
            '</div>' +
          '</div>' +
        '</a>' +
      '</div>';
    }
    html += '</div>';
    html += '<div class="latest-comments-footer"><a href="/comments/">View all community discussion <i class="fas fa-arrow-right"></i></a></div>';
    container.innerHTML = html;
  }

  // ---- Render: Full comments page (/comments/) ----

  function renderFullPage(container, paginationContainer, comments) {
    var countEl = document.getElementById('vv-comment-total-count');
    if (countEl) countEl.textContent = comments.length ? '(' + comments.length + ' comment' + (comments.length !== 1 ? 's' : '') + ')' : '';

    if (!comments || !comments.length) {
      container.innerHTML = '<div class="cp-empty">No comments yet. <a href="/reviews/">Browse reviews</a> to join the discussion.</div>';
      return;
    }

    var titles = window.VV_REVIEW_TITLES || {};
    var html = '<div class="comments-page-list">';
    for (var i = 0; i < comments.length; i++) {
      var c = comments[i];
      var title = titles[c.review_slug] || c.review_slug || 'Unknown review';
      var name = (c.profiles && c.profiles.display_name) ? c.profiles.display_name : '';
      var avatar = (c.profiles && c.profiles.avatar_url) ? c.profiles.avatar_url : '';
      var DEFAULT_AVATAR = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='50' fill='%231a1a26'/%3E%3Ccircle cx='50' cy='38' r='18' fill='%23c9a84c'/%3E%3Cellipse cx='50' cy='78' rx='30' ry='22' fill='%23c9a84c'/%3E%3C/svg%3E";

      html += '<div class="cp-item">' +
        '<div class="cp-header">' +
          '<img class="comment-avatar" src="' + esc(avatar || DEFAULT_AVATAR) + '" alt="" loading="lazy" onerror="this.src=\'' + DEFAULT_AVATAR + '\'">' +
          '<div>' +
            '<span class="cp-author">' + esc(name || 'Anonymous') + '</span>' +
            ' <span class="cp-time">' + relativeTime(c.created_at) + '</span>' +
          '</div>' +
        '</div>' +
        '<a class="cp-review-link" href="/reviews/' + esc(c.review_slug) + '/">on ' + esc(title) + '</a>' +
        '<div class="cp-body">' + esc(c.content) + '</div>' +
      '</div>';
    }
    html += '</div>';
    container.innerHTML = html;
  }

  // ---- Init ----

  async function init() {
    // 1) Sidebar widget (all pages that include the sidebar)
    var sidebarEl = document.getElementById('vv-latest-comments');
    if (sidebarEl) {
      try {
        var sidebarComments = await fetchComments(5);
        renderSidebar(sidebarEl, sidebarComments);
      } catch (e) {
        sidebarEl.style.display = 'none';
      }
    }

    // 2) Homepage section
    var homeEl = document.getElementById('vv-latest-comments-home');
    if (homeEl) {
      try {
        var homeComments = await fetchComments(5);
        renderHomepage(homeEl, homeComments);
      } catch (e) {
        homeEl.innerHTML = '<p class="latest-comments-empty">Comments unavailable right now.</p>';
      }
    }

    // 3) Full comments page
    var fullEl = document.getElementById('vv-comments-full-list');
    if (fullEl) {
      var pagEl = document.getElementById('vv-comments-pagination');
      try {
        var allComments = await fetchComments(null); // no limit = all
        renderFullPage(fullEl, pagEl, allComments);
      } catch (e) {
        fullEl.innerHTML = '<div class="cp-empty">Unable to load comments right now. Please try again later.</div>';
      }
    }
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();