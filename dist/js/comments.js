/* ============================================
   VirtueVigil — Comments Module
   Handles loading, posting, voting, editing,
   and deleting comments on review pages.
   ============================================ */

(function() {
  'use strict';

  const DEFAULT_AVATAR = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='50' fill='%231a1a26'/%3E%3Ccircle cx='50' cy='38' r='18' fill='%23c9a84c'/%3E%3Cellipse cx='50' cy='78' rx='30' ry='22' fill='%23c9a84c'/%3E%3C/svg%3E";

  let reviewSlug = null;

  // ---- Helpers ----

  function esc(s) {
    const el = document.createElement('div');
    el.textContent = s || '';
    return el.innerHTML;
  }

  function relativeTime(dateStr) {
    const now = new Date();
    const d = new Date(dateStr);
    const diffMs = now - d;
    const diffSec = Math.floor(diffMs / 1000);
    const diffMin = Math.floor(diffSec / 60);
    const diffHr = Math.floor(diffMin / 60);
    const diffDay = Math.floor(diffHr / 24);
    const diffWk = Math.floor(diffDay / 7);
    const diffMo = Math.floor(diffDay / 30);

    if (diffSec < 60) return 'just now';
    if (diffMin < 60) return diffMin + (diffMin === 1 ? ' minute ago' : ' minutes ago');
    if (diffHr < 24) return diffHr + (diffHr === 1 ? ' hour ago' : ' hours ago');
    if (diffDay < 7) return diffDay + (diffDay === 1 ? ' day ago' : ' days ago');
    if (diffWk < 5) return diffWk + (diffWk === 1 ? ' week ago' : ' weeks ago');
    if (diffMo < 12) return diffMo + (diffMo === 1 ? ' month ago' : ' months ago');
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  }

  // ---- Load Comments ----

  async function loadComments() {
    if (!window.vvSupabase || !reviewSlug) return;

    const list = document.getElementById('vv-comments-list');
    const count = document.getElementById('vv-comment-count');
    if (!list) return;

    list.innerHTML = '<div class="comments-loading"><i class="fas fa-spinner fa-spin"></i> Loading comments...</div>';

    const { data, error } = await window.vvSupabase
      .from('comments_with_scores')
      .select('*')
      .eq('review_slug', reviewSlug)
      .eq('is_hidden', false)
      .order('net_score', { ascending: false })
      .order('created_at', { ascending: false });

    if (error) {
      console.error('[Comments] Load error:', error);
      list.innerHTML = '<p class="comments-error">Unable to load comments.</p>';
      return;
    }

    const comments = data || [];
    if (count) count.textContent = comments.length;

    if (comments.length === 0) {
      list.innerHTML = '<p class="comments-empty">No comments yet. Be the first to share your thoughts.</p>';
      return;
    }

    // Get current user's votes
    let userVotes = {};
    const session = window.vvAuth ? window.vvAuth.getSession() : null;
    if (session) {
      const { data: voteData } = await window.vvSupabase
        .from('votes')
        .select('comment_id, vote_type')
        .eq('user_id', session.user.id);
      if (voteData) {
        voteData.forEach(v => { userVotes[v.comment_id] = v.vote_type; });
      }
    }

    renderComments(comments, session, userVotes);
  }

  // ---- Render Comments ----

  function renderComments(comments, session, userVotes) {
    const list = document.getElementById('vv-comments-list');
    if (!list) return;

    const userId = session ? session.user.id : null;

    list.innerHTML = comments.map(c => {
      const isOwn = userId && c.user_id === userId;
      const userVote = userVotes[c.id] || 0;
      const avatar = c.avatar_url || DEFAULT_AVATAR;

      return `
        <div class="comment-card" data-id="${c.id}">
          <div class="comment-header">
            <img class="comment-avatar" src="${esc(avatar)}" alt="${esc(c.display_name || 'User')} avatar" loading="lazy" onerror="this.src='${DEFAULT_AVATAR}'">
            <div class="comment-meta">
              <span class="comment-author">${esc(c.display_name || 'Anonymous')}</span>
              <span class="comment-time" title="${new Date(c.created_at).toLocaleString()}">${relativeTime(c.created_at)}${c.is_edited ? ' <span class="edited-tag">(edited)</span>' : ''}</span>
            </div>
          </div>
          <div class="comment-body">${esc(c.content)}</div>
          <div class="comment-footer">
            <div class="vote-buttons">
              <button class="vote-btn vote-up${userVote === 1 ? ' voted' : ''}" data-comment="${c.id}" data-vote="1" title="Upvote" aria-label="Upvote">
                <i class="fas fa-arrow-up"></i>
              </button>
              <span class="vote-score">${c.net_score}</span>
              <button class="vote-btn vote-down${userVote === -1 ? ' voted' : ''}" data-comment="${c.id}" data-vote="-1" title="Downvote" aria-label="Downvote">
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
            ${isOwn ? `
              <button class="comment-action-btn edit-btn" data-comment="${c.id}" title="Edit"><i class="fas fa-pencil-alt"></i> Edit</button>
              <button class="comment-action-btn delete-btn" data-comment="${c.id}" title="Delete"><i class="fas fa-trash-alt"></i> Delete</button>
            ` : ''}
          </div>
        </div>`;
    }).join('');

    // Attach event listeners
    attachVoteListeners();
    attachEditListeners();
    attachDeleteListeners();
  }

  // ---- Post Comment ----

  async function postComment(content) {
    const session = window.vvAuth ? window.vvAuth.getSession() : null;
    if (!session) {
      window.vvAuth.openAuthModal();
      return false;
    }

    const trimmed = content.trim();
    if (!trimmed) return false;
    if (trimmed.length > 2000) return false;

    const { data, error } = await window.vvSupabase
      .from('comments')
      .insert([{
        review_slug: reviewSlug,
        user_id: session.user.id,
        content: trimmed
      }])
      .select();

    if (error) {
      console.error('[Comments] Post error:', error);
      alert('Failed to post comment. Please try again.');
      return false;
    }

    await loadComments();
    return true;
  }

  // ---- Vote ----

  async function toggleVote(commentId, voteType) {
    const session = window.vvAuth ? window.vvAuth.getSession() : null;
    if (!session) {
      window.vvAuth.openAuthModal();
      return;
    }

    // Check if user already voted this way
    const { data: existing } = await window.vvSupabase
      .from('votes')
      .select('id, vote_type')
      .eq('comment_id', commentId)
      .eq('user_id', session.user.id)
      .maybeSingle();

    if (existing) {
      if (existing.vote_type === voteType) {
        // Remove vote (toggle off)
        await window.vvSupabase.from('votes').delete().eq('id', existing.id);
      } else {
        // Change vote direction
        await window.vvSupabase.from('votes').update({ vote_type: voteType }).eq('id', existing.id);
      }
    } else {
      // New vote
      await window.vvSupabase.from('votes').insert([{
        comment_id: commentId,
        user_id: session.user.id,
        vote_type: voteType
      }]);
    }

    await loadComments();
  }

  // ---- Edit Comment ----

  async function editComment(commentId) {
    const session = window.vvAuth ? window.vvAuth.getSession() : null;
    if (!session) return;

    const card = document.querySelector(`.comment-card[data-id="${commentId}"]`);
    if (!card) return;

    const bodyEl = card.querySelector('.comment-body');
    const currentText = bodyEl.textContent;

    bodyEl.innerHTML = `
      <textarea class="edit-textarea" maxlength="2000">${esc(currentText)}</textarea>
      <div class="edit-actions">
        <button class="btn-save-edit" data-comment="${commentId}">Save</button>
        <button class="btn-cancel-edit">Cancel</button>
      </div>`;

    const textarea = bodyEl.querySelector('.edit-textarea');
    textarea.focus();
    textarea.setSelectionRange(textarea.value.length, textarea.value.length);

    bodyEl.querySelector('.btn-save-edit').addEventListener('click', async function() {
      const newContent = textarea.value.trim();
      if (!newContent) return;

      const { error } = await window.vvSupabase
        .from('comments')
        .update({ content: newContent, is_edited: true, updated_at: new Date().toISOString() })
        .eq('id', commentId)
        .eq('user_id', session.user.id);

      if (error) {
        console.error('[Comments] Edit error:', error);
        alert('Failed to save edit.');
        return;
      }
      await loadComments();
    });

    bodyEl.querySelector('.btn-cancel-edit').addEventListener('click', function() {
      loadComments();
    });
  }

  // ---- Delete Comment ----

  async function deleteComment(commentId) {
    const session = window.vvAuth ? window.vvAuth.getSession() : null;
    if (!session) return;

    if (!confirm('Delete this comment? This cannot be undone.')) return;

    const { error } = await window.vvSupabase
      .from('comments')
      .delete()
      .eq('id', commentId)
      .eq('user_id', session.user.id);

    if (error) {
      console.error('[Comments] Delete error:', error);
      alert('Failed to delete comment.');
      return;
    }

    await loadComments();
  }

  // ---- Event Listener Helpers ----

  function attachVoteListeners() {
    document.querySelectorAll('.vote-btn').forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        const commentId = this.dataset.comment;
        const voteType = parseInt(this.dataset.vote);
        toggleVote(commentId, voteType);
      });
    });
  }

  function attachEditListeners() {
    document.querySelectorAll('.edit-btn').forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        editComment(this.dataset.comment);
      });
    });
  }

  function attachDeleteListeners() {
    document.querySelectorAll('.delete-btn').forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        deleteComment(this.dataset.comment);
      });
    });
  }

  // ---- Comment Form ----

  function initCommentForm() {
    const form = document.getElementById('vv-comment-form');
    const input = document.getElementById('vv-comment-input');
    const charCount = document.getElementById('vv-char-count');

    if (!form || !input) return;

    // Character counter
    if (charCount) {
      input.addEventListener('input', function() {
        charCount.textContent = this.value.length + ' / 2000';
        if (this.value.length > 1800) {
          charCount.style.color = '#c44040';
        } else {
          charCount.style.color = '';
        }
      });
    }

    // Submit
    form.addEventListener('submit', async function(e) {
      e.preventDefault();
      const content = input.value;
      const btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = 'Posting...'; }

      const success = await postComment(content);

      if (btn) { btn.disabled = false; btn.textContent = 'Post Comment'; }
      if (success) { input.value = ''; if (charCount) charCount.textContent = '0 / 2000'; }
    });
  }

  // ---- Initialize ----

  function initComments() {
    const section = document.querySelector('.comments-section');
    if (!section) return; // Not on a review page

    reviewSlug = section.dataset.slug;
    if (!reviewSlug) return;

    initCommentForm();
    loadComments();

    // Refresh on auth changes
    window.addEventListener('vv-auth-change', function() {
      loadComments();
    });
  }

  // Init when DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initComments);
  } else {
    initComments();
  }

})();
