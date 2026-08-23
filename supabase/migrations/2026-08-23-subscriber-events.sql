-- subscriber_events: queue table for new subscriber notifications
-- The Netlify subscribe function inserts rows with notified=false.
-- A cron job polls this table and sends Telegram messages to Jason.

CREATE TABLE IF NOT EXISTS subscriber_events (
  id BIGSERIAL PRIMARY KEY,
  email TEXT NOT NULL,
  source TEXT NOT NULL DEFAULT 'website',
  notified BOOLEAN NOT NULL DEFAULT false,
  notified_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_subscriber_events_notified ON subscriber_events (notified, created_at);