-- ============================================
-- VirtueVigil — Supabase Database Schema
-- Run this in Supabase SQL Editor to set up
-- auth, comments, votes, and profiles.
-- ============================================

-- ============================================
-- 1. PROFILES TABLE
-- Auto-populated via trigger on user signup
-- ============================================

CREATE TABLE IF NOT EXISTS public.profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  display_name TEXT DEFAULT '',
  avatar_url TEXT DEFAULT '',
  provider TEXT DEFAULT 'email',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- Anyone can read profiles (for displaying comment author info)
CREATE POLICY "Profiles are viewable by everyone"
  ON public.profiles FOR SELECT
  USING (true);

-- Users can only update their own profile
CREATE POLICY "Users can update their own profile"
  ON public.profiles FOR UPDATE
  USING (auth.uid() = id)
  WITH CHECK (auth.uid() = id);

-- Users can insert their own profile (fallback if trigger fails)
CREATE POLICY "Users can insert their own profile"
  ON public.profiles FOR INSERT
  WITH CHECK (auth.uid() = id);


-- ============================================
-- 2. AUTO-CREATE PROFILE ON SIGNUP (Trigger)
-- Pulls display_name and avatar from Google metadata
-- ============================================

CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, display_name, avatar_url, provider)
  VALUES (
    NEW.id,
    COALESCE(
      NEW.raw_user_meta_data ->> 'full_name',
      NEW.raw_user_meta_data ->> 'name',
      split_part(NEW.email, '@', 1)
    ),
    COALESCE(
      NEW.raw_user_meta_data ->> 'avatar_url',
      NEW.raw_user_meta_data ->> 'picture',
      ''
    ),
    COALESCE(
      NEW.raw_app_meta_data ->> 'provider',
      'email'
    )
  )
  ON CONFLICT (id) DO UPDATE SET
    display_name = COALESCE(NULLIF(profiles.display_name, ''), EXCLUDED.display_name),
    avatar_url = COALESCE(NULLIF(profiles.avatar_url, ''), EXCLUDED.avatar_url),
    provider = EXCLUDED.provider,
    updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Drop existing trigger if it exists, then create
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW
  EXECUTE FUNCTION public.handle_new_user();


-- ============================================
-- 3. COMMENTS TABLE
-- ============================================

CREATE TABLE IF NOT EXISTS public.comments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  review_slug TEXT NOT NULL,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  content TEXT NOT NULL CHECK (char_length(content) BETWEEN 1 AND 2000),
  is_hidden BOOLEAN DEFAULT false,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Index for fast lookup by review
CREATE INDEX IF NOT EXISTS idx_comments_review_slug ON public.comments(review_slug);
CREATE INDEX IF NOT EXISTS idx_comments_user_id ON public.comments(user_id);
CREATE INDEX IF NOT EXISTS idx_comments_created_at ON public.comments(created_at DESC);

ALTER TABLE public.comments ENABLE ROW LEVEL SECURITY;

-- Anyone can read non-hidden comments
CREATE POLICY "Visible comments are viewable by everyone"
  ON public.comments FOR SELECT
  USING (is_hidden = false);

-- Authenticated users can post comments
CREATE POLICY "Authenticated users can insert comments"
  ON public.comments FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Users can update their own comments
CREATE POLICY "Users can update their own comments"
  ON public.comments FOR UPDATE
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- Users can delete their own comments
CREATE POLICY "Users can delete their own comments"
  ON public.comments FOR DELETE
  USING (auth.uid() = user_id);


-- ============================================
-- 4. VOTES TABLE
-- ============================================

CREATE TABLE IF NOT EXISTS public.votes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  comment_id UUID NOT NULL REFERENCES public.comments(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  vote_type TEXT NOT NULL CHECK (vote_type IN ('up', 'down')),
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(comment_id, user_id)
);

CREATE INDEX IF NOT EXISTS idx_votes_comment_id ON public.votes(comment_id);
CREATE INDEX IF NOT EXISTS idx_votes_user_id ON public.votes(user_id);

ALTER TABLE public.votes ENABLE ROW LEVEL SECURITY;

-- Anyone can read votes (needed for score calculation)
CREATE POLICY "Votes are viewable by everyone"
  ON public.votes FOR SELECT
  USING (true);

-- Authenticated users can insert votes
CREATE POLICY "Authenticated users can insert votes"
  ON public.votes FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Users can update their own votes (change up to down or vice versa)
CREATE POLICY "Users can update their own votes"
  ON public.votes FOR UPDATE
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- Users can delete their own votes (un-vote)
CREATE POLICY "Users can delete their own votes"
  ON public.votes FOR DELETE
  USING (auth.uid() = user_id);


-- ============================================
-- 5. COMMENTS WITH SCORES VIEW
-- Joins comments + profiles + aggregated votes
-- ============================================

CREATE OR REPLACE VIEW public.comments_with_scores AS
SELECT
  c.id,
  c.review_slug,
  c.user_id,
  c.content,
  c.is_hidden,
  c.created_at,
  c.updated_at,
  p.display_name,
  p.avatar_url,
  COALESCE(v.up_count, 0) AS up_votes,
  COALESCE(v.down_count, 0) AS down_votes,
  COALESCE(v.up_count, 0) - COALESCE(v.down_count, 0) AS net_score
FROM public.comments c
LEFT JOIN public.profiles p ON c.user_id = p.id
LEFT JOIN (
  SELECT
    comment_id,
    COUNT(*) FILTER (WHERE vote_type = 'up') AS up_count,
    COUNT(*) FILTER (WHERE vote_type = 'down') AS down_count
  FROM public.votes
  GROUP BY comment_id
) v ON c.id = v.comment_id;


-- ============================================
-- 6. AVATARS STORAGE BUCKET
-- For user avatar uploads
-- ============================================

-- Create the avatars bucket (public read, authenticated write)
INSERT INTO storage.buckets (id, name, public)
VALUES ('avatars', 'avatars', true)
ON CONFLICT (id) DO NOTHING;

-- Allow anyone to read avatars
CREATE POLICY "Avatar images are publicly accessible"
  ON storage.objects FOR SELECT
  USING (bucket_id = 'avatars');

-- Allow authenticated users to upload to their own folder
CREATE POLICY "Users can upload their own avatar"
  ON storage.objects FOR INSERT
  WITH CHECK (
    bucket_id = 'avatars'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );

-- Allow users to update (overwrite) their own avatar
CREATE POLICY "Users can update their own avatar"
  ON storage.objects FOR UPDATE
  USING (
    bucket_id = 'avatars'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );

-- Allow users to delete their own avatar
CREATE POLICY "Users can delete their own avatar"
  ON storage.objects FOR DELETE
  USING (
    bucket_id = 'avatars'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );


-- ============================================
-- 7. GRANT ACCESS TO VIEWS
-- Required for anon/authenticated access
-- ============================================

GRANT SELECT ON public.comments_with_scores TO anon, authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.comments TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.votes TO authenticated;
GRANT SELECT ON public.profiles TO anon, authenticated;
GRANT INSERT, UPDATE ON public.profiles TO authenticated;


-- ============================================
-- DONE! Your VirtueVigil database is ready.
--
-- Next steps:
-- 1. Enable Google OAuth in Supabase Dashboard:
--    Authentication > Providers > Google
--    (Requires Google Cloud Console OAuth credentials)
--
-- 2. Set your Site URL in Supabase Dashboard:
--    Authentication > URL Configuration
--    Site URL: https://virtuevigil.com
--    Redirect URLs: https://virtuevigil.com/auth/callback/
--
-- 3. Copy your Supabase URL and Anon Key to:
--    VirtueVigil Admin > Settings > Supabase section
--    Then click "Push Config to Site"
-- ============================================
