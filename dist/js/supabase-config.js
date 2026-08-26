/* ============================================
   VirtueVigil — Supabase Configuration
   Initializes the Supabase client for auth,
   database, and storage operations.
   ============================================ */

(function() {
  'use strict';

  // These are injected at build time or set in admin settings
  const url = window.SUPABASE_URL || localStorage.getItem('vv_supabase_url') || '';
  const key = window.SUPABASE_ANON_KEY || localStorage.getItem('vv_supabase_anon_key') || '';

  if (!url || !key) {
    console.warn('[VirtueVigil] Supabase not configured. Auth and comments disabled.');
    window.vvSupabase = null;
    return;
  }

  // Initialize Supabase client (SDK loaded via CDN in <head>)
  if (typeof window.supabase === 'undefined' || !window.supabase.createClient) {
    console.warn('[VirtueVigil] Supabase SDK not loaded.');
    window.vvSupabase = null;
    return;
  }

  window.vvSupabase = window.supabase.createClient(url, key);

  // Expose helper for getting current session
  window.vvGetSession = async function() {
    if (!window.vvSupabase) return null;
    const { data: { session } } = await window.vvSupabase.auth.getSession();
    return session;
  };

  // Expose helper for getting current user profile
  window.vvGetProfile = async function() {
    const session = await window.vvGetSession();
    if (!session) return null;
    const { data, error } = await window.vvSupabase
      .from('profiles')
      .select('*')
      .eq('id', session.user.id)
      .single();
    if (error) { console.error('[VirtueVigil] Profile fetch error:', error); return null; }
    return data;
  };

  console.log('[VirtueVigil] Supabase initialized.');
})();
