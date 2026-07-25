/* ============================================
   VirtueVigil — Account Page Module
   Handles profile display, editing, avatar
   upload, and password changes.
   ============================================ */

(function() {
  'use strict';

  const DEFAULT_AVATAR = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='50' fill='%231a1a26'/%3E%3Ccircle cx='50' cy='38' r='18' fill='%23c9a84c'/%3E%3Cellipse cx='50' cy='78' rx='30' ry='22' fill='%23c9a84c'/%3E%3C/svg%3E";
  const MAX_AVATAR_SIZE = 2 * 1024 * 1024; // 2MB

  // ---- Load Profile ----

  async function loadProfile() {
    const session = await window.vvGetSession();
    const authRequired = document.getElementById('vv-auth-required');
    const profileSection = document.getElementById('vv-profile-section');

    if (!session) {
      if (authRequired) authRequired.style.display = 'block';
      if (profileSection) profileSection.style.display = 'none';
      return;
    }

    if (authRequired) authRequired.style.display = 'none';
    if (profileSection) profileSection.style.display = 'block';

    const profile = await window.vvGetProfile();
    if (!profile) return;

    // Populate fields
    const avatar = document.getElementById('vv-acct-avatar');
    const nameInput = document.getElementById('vv-acct-name');
    const emailInput = document.getElementById('vv-acct-email');
    const providerLabel = document.getElementById('vv-acct-provider');
    const passwordSection = document.getElementById('vv-acct-password-section');

    if (avatar) {
      avatar.src = profile.avatar_url || DEFAULT_AVATAR;
      avatar.onerror = function() { this.src = DEFAULT_AVATAR; };
    }
    if (nameInput) nameInput.value = profile.display_name || '';
    if (emailInput) emailInput.value = session.user.email || '';
    if (providerLabel) {
      const p = profile.provider || 'email';
      providerLabel.textContent = p === 'google' ? 'Signed in with Google' : p === 'apple' ? 'Signed in with Apple' : 'Email & Password';
      providerLabel.className = 'provider-badge provider-' + p;
    }
    // Only show password section for email users
    if (passwordSection) {
      passwordSection.style.display = (profile.provider === 'email' || !profile.provider) ? 'block' : 'none';
    }
  }

  // ---- Save Display Name ----

  async function saveDisplayName(name) {
    const session = await window.vvGetSession();
    if (!session) return false;

    const trimmed = name.trim();
    if (!trimmed || trimmed.length > 100) return false;

    const { error } = await window.vvSupabase
      .from('profiles')
      .update({ display_name: trimmed, updated_at: new Date().toISOString() })
      .eq('id', session.user.id);

    if (error) {
      console.error('[Account] Save name error:', error);
      return false;
    }
    return true;
  }

  // ---- Upload Avatar ----

  async function uploadAvatar(file) {
    const session = await window.vvGetSession();
    if (!session) return null;

    if (file.size > MAX_AVATAR_SIZE) {
      alert('Avatar image must be under 2MB.');
      return null;
    }

    if (!file.type.startsWith('image/')) {
      alert('Please select an image file.');
      return null;
    }

    const ext = file.name.split('.').pop().toLowerCase();
    const filePath = `${session.user.id}/avatar.${ext}`;

    // Upload to Supabase Storage
    const { data, error } = await window.vvSupabase.storage
      .from('avatars')
      .upload(filePath, file, { upsert: true, contentType: file.type });

    if (error) {
      console.error('[Account] Avatar upload error:', error);
      alert('Failed to upload avatar.');
      return null;
    }

    // Get public URL
    const { data: urlData } = window.vvSupabase.storage
      .from('avatars')
      .getPublicUrl(filePath);

    const publicUrl = urlData.publicUrl + '?t=' + Date.now(); // Cache bust

    // Update profile
    const { error: updateError } = await window.vvSupabase
      .from('profiles')
      .update({ avatar_url: publicUrl, updated_at: new Date().toISOString() })
      .eq('id', session.user.id);

    if (updateError) {
      console.error('[Account] Avatar URL update error:', updateError);
      return null;
    }

    return publicUrl;
  }

  // ---- Change Password ----

  async function changePassword(newPassword) {
    if (!newPassword || newPassword.length < 6) {
      return { success: false, message: 'Password must be at least 6 characters.' };
    }

    const { error } = await window.vvSupabase.auth.updateUser({ password: newPassword });

    if (error) {
      console.error('[Account] Password change error:', error);
      return { success: false, message: error.message };
    }

    return { success: true, message: 'Password updated successfully.' };
  }

  // ---- Status Messages ----

  function showStatus(msg, isError) {
    const el = document.getElementById('vv-acct-status');
    if (!el) return;
    el.textContent = msg;
    el.className = 'acct-status ' + (isError ? 'error' : 'success');
    el.style.display = 'block';
    setTimeout(() => { el.style.display = 'none'; }, 4000);
  }

  // ---- Initialize ----

  function initAccount() {
    // Only run on account page
    if (!document.getElementById('vv-profile-section')) return;

    loadProfile();

    // Save profile form
    const profileForm = document.getElementById('vv-acct-form');
    if (profileForm) {
      profileForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const name = document.getElementById('vv-acct-name').value;
        const btn = profileForm.querySelector('button[type="submit"]');
        if (btn) { btn.disabled = true; btn.textContent = 'Saving...'; }

        const ok = await saveDisplayName(name);

        if (btn) { btn.disabled = false; btn.textContent = 'Save Changes'; }
        if (ok) {
          showStatus('Profile updated.', false);
          if (window.vvAuth) window.vvAuth.refreshAuthState();
        } else {
          showStatus('Failed to save changes.', true);
        }
      });
    }

    // Avatar upload
    const avatarInput = document.getElementById('vv-acct-avatar-input');
    if (avatarInput) {
      avatarInput.addEventListener('change', async function() {
        const file = this.files[0];
        if (!file) return;

        const preview = document.getElementById('vv-acct-avatar');
        const uploadBtn = document.getElementById('vv-acct-avatar-btn');
        if (uploadBtn) { uploadBtn.textContent = 'Uploading...'; uploadBtn.disabled = true; }

        const url = await uploadAvatar(file);

        if (uploadBtn) { uploadBtn.textContent = 'Change Avatar'; uploadBtn.disabled = false; }

        if (url) {
          if (preview) preview.src = url;
          showStatus('Avatar updated.', false);
          if (window.vvAuth) window.vvAuth.refreshAuthState();
        }
      });
    }

    // Avatar button triggers file input
    const avatarBtn = document.getElementById('vv-acct-avatar-btn');
    if (avatarBtn && avatarInput) {
      avatarBtn.addEventListener('click', function(e) {
        e.preventDefault();
        avatarInput.click();
      });
    }

    // Password change
    const pwdBtn = document.getElementById('vv-acct-pwd-btn');
    if (pwdBtn) {
      pwdBtn.addEventListener('click', async function(e) {
        e.preventDefault();
        const pwd = document.getElementById('vv-acct-new-pwd').value;
        const confirm = document.getElementById('vv-acct-confirm-pwd').value;
        if (pwd !== confirm) {
          showStatus('Passwords do not match.', true);
          return;
        }
        const result = await changePassword(pwd);
        showStatus(result.message, !result.success);
        if (result.success) {
          document.getElementById('vv-acct-new-pwd').value = '';
          document.getElementById('vv-acct-confirm-pwd').value = '';
        }
      });
    }

    // Sign out button
    const signOutBtn = document.getElementById('vv-acct-signout');
    if (signOutBtn) {
      signOutBtn.addEventListener('click', function(e) {
        e.preventDefault();
        if (window.vvAuth) window.vvAuth.signOut();
      });
    }

    // Refresh on auth change
    window.addEventListener('vv-auth-change', loadProfile);
  }

  // Init when DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAccount);
  } else {
    initAccount();
  }

})();
