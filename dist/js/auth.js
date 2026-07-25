/* ============================================
   VirtueVigil — Authentication Module
   Handles Google OAuth, email/password auth,
   session management, and header UI updates.
   ============================================ */

(function() {
  'use strict';

  // Default avatar SVG (data URI)
  const DEFAULT_AVATAR = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='50' fill='%231a1a26'/%3E%3Ccircle cx='50' cy='38' r='18' fill='%23c9a84c'/%3E%3Cellipse cx='50' cy='78' rx='30' ry='22' fill='%23c9a84c'/%3E%3C/svg%3E";

  // ---- Auth State Management ----

  let currentSession = null;
  let currentProfile = null;

  async function refreshAuthState() {
    if (!window.vvSupabase) return;
    currentSession = await window.vvGetSession();
    if (currentSession) {
      currentProfile = await window.vvGetProfile();
    } else {
      currentProfile = null;
    }
    updateHeaderUI();
    updateSubscribePrompts();
    // Fire custom event so other modules can react
    window.dispatchEvent(new CustomEvent('vv-auth-change', {
      detail: { session: currentSession, profile: currentProfile }
    }));
  }

  // ---- Header UI ----

  function updateHeaderUI() {
    const loginBtn = document.getElementById('vv-login-btn');
    const userArea = document.getElementById('vv-user-area');
    const userAvatar = document.getElementById('vv-user-avatar');
    const userName = document.getElementById('vv-user-name');

    if (!loginBtn || !userArea) return;

    if (currentSession && currentProfile) {
      loginBtn.style.display = 'none';
      userArea.style.display = 'flex';
      if (userAvatar) {
        userAvatar.src = currentProfile.avatar_url || DEFAULT_AVATAR;
        userAvatar.alt = (currentProfile.display_name || 'User') + ' avatar';
      }
      if (userName) userName.textContent = currentProfile.display_name || 'User';
    } else {
      loginBtn.style.display = '';
      userArea.style.display = 'none';
    }
  }

  // ---- Subscribe Prompts ----

  function updateSubscribePrompts() {
    // Update comment subscribe prompts on review pages
    const subscribePrompt = document.getElementById('comment-subscribe-prompt');
    const commentForm = document.getElementById('comment-form-container');
    if (subscribePrompt && commentForm) {
      if (currentSession) {
        subscribePrompt.style.display = 'none';
        commentForm.style.display = 'block';
      } else {
        subscribePrompt.style.display = '';
        commentForm.style.display = 'none';
      }
    }
  }

  // ---- Google OAuth ----

  async function signInWithGoogle() {
    if (!window.vvSupabase) return alert('Authentication is not configured.');
    const { error } = await window.vvSupabase.auth.signInWithOAuth({
      provider: 'google',
      options: { redirectTo: window.location.origin + '/auth/callback/' }
    });
    if (error) {
      console.error('[Auth] Google sign-in error:', error);
      showAuthError('Google sign-in failed. Please try again.');
    }
  }

  // ---- Email/Password ----

  async function signUpWithEmail(email, password) {
    if (!window.vvSupabase) return alert('Authentication is not configured.');
    const { data, error } = await window.vvSupabase.auth.signUp({
      email: email,
      password: password,
      options: { emailRedirectTo: window.location.origin + '/auth/callback/' }
    });
    if (error) {
      console.error('[Auth] Email signup error:', error);
      if (error.message.includes('already registered')) {
        return { success: false, message: 'This email is already registered. Try signing in instead.' };
      }
      return { success: false, message: error.message };
    }
    if (data.user && !data.session) {
      return { success: true, message: 'Check your email for a confirmation link.' };
    }
    await refreshAuthState();
    return { success: true, message: 'Account created!' };
  }

  async function signInWithEmail(email, password) {
    if (!window.vvSupabase) return alert('Authentication is not configured.');
    const { data, error } = await window.vvSupabase.auth.signInWithPassword({
      email: email,
      password: password,
    });
    if (error) {
      console.error('[Auth] Email sign-in error:', error);
      return { success: false, message: 'Invalid email or password.' };
    }
    await refreshAuthState();
    return { success: true, message: 'Signed in!' };
  }

  async function signOut() {
    if (!window.vvSupabase) return;
    await window.vvSupabase.auth.signOut();
    currentSession = null;
    currentProfile = null;
    updateHeaderUI();
    updateSubscribePrompts();
    window.location.href = '/';
  }

  async function resetPassword(email) {
    if (!window.vvSupabase) return;
    const { error } = await window.vvSupabase.auth.resetPasswordForEmail(email, {
      redirectTo: window.location.origin + '/account/',
    });
    if (error) return { success: false, message: error.message };
    return { success: true, message: 'Password reset email sent. Check your inbox.' };
  }

  // ---- Auth Modal ----

  function showAuthError(msg) {
    const el = document.getElementById('vv-auth-error');
    if (el) {
      el.textContent = msg;
      el.style.display = 'block';
      setTimeout(() => { el.style.display = 'none'; }, 5000);
    }
  }

  function showAuthSuccess(msg) {
    const el = document.getElementById('vv-auth-success');
    if (el) {
      el.textContent = msg;
      el.style.display = 'block';
      setTimeout(() => { el.style.display = 'none'; }, 5000);
    }
  }

  function openAuthModal() {
    const modal = document.getElementById('vv-auth-modal');
    if (modal) {
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
      const emailInput = modal.querySelector('#vv-auth-email');
      if (emailInput) emailInput.focus();
    }
  }

  function closeAuthModal() {
    const modal = document.getElementById('vv-auth-modal');
    if (modal) {
      modal.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  // ---- User Dropdown ----

  function toggleUserDropdown() {
    const menu = document.getElementById('vv-dropdown-menu');
    if (menu) menu.classList.toggle('active');
  }

  // ---- Initialize ----

  function initAuth() {
    // Login button → open modal or go to /subscribe/
    const loginBtn = document.getElementById('vv-login-btn');
    if (loginBtn) {
      loginBtn.addEventListener('click', function(e) {
        e.preventDefault();
        const modal = document.getElementById('vv-auth-modal');
        if (modal) { openAuthModal(); } else { window.location.href = '/subscribe/'; }
      });
    }

    // User dropdown toggle
    const userArea = document.getElementById('vv-user-area');
    if (userArea) {
      userArea.addEventListener('click', function(e) {
        e.stopPropagation();
        toggleUserDropdown();
      });
    }

    // Close dropdown on outside click
    document.addEventListener('click', function() {
      const menu = document.getElementById('vv-dropdown-menu');
      if (menu) menu.classList.remove('active');
    });

    // Logout button
    const logoutBtn = document.getElementById('vv-logout-btn');
    if (logoutBtn) {
      logoutBtn.addEventListener('click', function(e) {
        e.preventDefault();
        signOut();
      });
    }

    // Auth modal close
    const modalClose = document.getElementById('vv-auth-modal-close');
    if (modalClose) {
      modalClose.addEventListener('click', closeAuthModal);
    }
    const modal = document.getElementById('vv-auth-modal');
    if (modal) {
      modal.addEventListener('click', function(e) {
        if (e.target === modal) closeAuthModal();
      });
    }

    // Google sign-in button
    const googleBtn = document.getElementById('vv-google-login');
    if (googleBtn) {
      googleBtn.addEventListener('click', function(e) {
        e.preventDefault();
        signInWithGoogle();
      });
    }

    // Email form (handles both sign-up and sign-in)
    const emailForm = document.getElementById('vv-email-form');
    if (emailForm) {
      emailForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const email = document.getElementById('vv-auth-email').value.trim();
        const password = document.getElementById('vv-auth-password').value;
        const isSignUp = document.getElementById('vv-auth-mode-signup');

        if (!email || !password) {
          showAuthError('Please enter both email and password.');
          return;
        }
        if (password.length < 6) {
          showAuthError('Password must be at least 6 characters.');
          return;
        }

        const submitBtn = emailForm.querySelector('button[type="submit"]');
        if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Please wait...'; }

        let result;
        if (isSignUp && isSignUp.checked) {
          result = await signUpWithEmail(email, password);
        } else {
          result = await signInWithEmail(email, password);
        }

        if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = isSignUp && isSignUp.checked ? 'Create Account' : 'Sign In'; }

        if (result.success) {
          showAuthSuccess(result.message);
          if (result.message !== 'Check your email for a confirmation link.') {
            setTimeout(() => { closeAuthModal(); }, 1000);
          }
        } else {
          showAuthError(result.message);
        }
      });
    }

    // Toggle sign-in / sign-up mode
    const modeToggle = document.getElementById('vv-auth-mode-toggle');
    if (modeToggle) {
      modeToggle.addEventListener('click', function(e) {
        e.preventDefault();
        const isSignUp = document.getElementById('vv-auth-mode-signup');
        const submitBtn = emailForm ? emailForm.querySelector('button[type="submit"]') : null;
        const toggleText = document.getElementById('vv-auth-mode-text');
        if (isSignUp) {
          isSignUp.checked = !isSignUp.checked;
          if (submitBtn) submitBtn.textContent = isSignUp.checked ? 'Create Account' : 'Sign In';
          if (toggleText) toggleText.textContent = isSignUp.checked ? 'Already have an account? Sign in' : "Don't have an account? Sign up";
        }
      });
    }

    // Forgot password link
    const forgotLink = document.getElementById('vv-forgot-password');
    if (forgotLink) {
      forgotLink.addEventListener('click', async function(e) {
        e.preventDefault();
        const email = document.getElementById('vv-auth-email').value.trim();
        if (!email) {
          showAuthError('Enter your email address first, then click Forgot Password.');
          return;
        }
        const result = await resetPassword(email);
        if (result.success) showAuthSuccess(result.message);
        else showAuthError(result.message);
      });
    }

    // Subscribe page buttons (if on /subscribe/ page)
    const subGoogleBtn = document.getElementById('vv-sub-google');
    if (subGoogleBtn) {
      subGoogleBtn.addEventListener('click', function(e) { e.preventDefault(); signInWithGoogle(); });
    }
    const subEmailForm = document.getElementById('vv-sub-email-form');
    if (subEmailForm) {
      subEmailForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const email = document.getElementById('vv-sub-email').value.trim();
        const password = document.getElementById('vv-sub-password').value;
        const isSignUp = document.getElementById('vv-sub-mode-signup');

        if (!email || !password) { showSubError('Please enter both email and password.'); return; }
        if (password.length < 6) { showSubError('Password must be at least 6 characters.'); return; }

        const btn = subEmailForm.querySelector('button[type="submit"]');
        if (btn) { btn.disabled = true; btn.textContent = 'Please wait...'; }

        let result;
        if (isSignUp && isSignUp.checked) {
          result = await signUpWithEmail(email, password);
        } else {
          result = await signInWithEmail(email, password);
        }

        if (btn) { btn.disabled = false; btn.textContent = isSignUp && isSignUp.checked ? 'Create Account' : 'Sign In'; }

        if (result.success) {
          showSubSuccess(result.message);
          if (result.message !== 'Check your email for a confirmation link.') {
            setTimeout(() => { window.location.href = '/account/'; }, 1200);
          }
        } else {
          showSubError(result.message);
        }
      });
    }

    // Listen for auth state changes
    if (window.vvSupabase) {
      window.vvSupabase.auth.onAuthStateChange(function(event, session) {
        refreshAuthState();
      });
    }

    // Initial state check
    refreshAuthState();
  }

  // Subscribe page helpers
  function showSubError(msg) {
    const el = document.getElementById('vv-sub-error');
    if (el) { el.textContent = msg; el.style.display = 'block'; setTimeout(() => { el.style.display = 'none'; }, 5000); }
  }
  function showSubSuccess(msg) {
    const el = document.getElementById('vv-sub-success');
    if (el) { el.textContent = msg; el.style.display = 'block'; }
  }

  // Expose for other modules
  window.vvAuth = {
    signInWithGoogle: signInWithGoogle,
    signUpWithEmail: signUpWithEmail,
    signInWithEmail: signInWithEmail,
    signOut: signOut,
    resetPassword: resetPassword,
    openAuthModal: openAuthModal,
    closeAuthModal: closeAuthModal,
    refreshAuthState: refreshAuthState,
    getSession: function() { return currentSession; },
    getProfile: function() { return currentProfile; },
  };

  // Init when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAuth);
  } else {
    initAuth();
  }

})();
