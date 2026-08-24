# Notification Pipeline — Subscriber Alerts for Jason

**Created:** 2026-08-23
**Status:** PENDING CRON SETUP

## What Happens

1. User subscribes on virtuevigil.com → `subscribe.js` Netlify function inserts into `subscribers` AND `subscriber_events` (with `notified=false`)
2. A cron job polls `subscriber_events WHERE notified = false` every 5 minutes
3. For each new row: sends Telegram message to chat ID `8294662132` (Jason)
4. Sets `notified = true, notified_at = NOW()`

## Telegram Bot

- **Bot token:** stored in `.secrets` as `VV_TELEGRAM_BOT_TOKEN` (`8595502264:AAGPzUBRqNRcJoN7i83W1XQlNz2x-nw7wj0`)
- **Chat ID:** `8294662132`
- **API endpoint:** `https://api.telegram.org/bot{TOKEN}/sendMessage`

## Supabase Table

`subscriber_events` — see `supabase/migrations/2026-08-23-subscriber-events.sql`

| Column | Type | Notes |
|--------|------|-------|
| id | BIGSERIAL PK | |
| email | TEXT | Subscriber email |
| source | TEXT | inline/sidebar/footer/website |
| notified | BOOLEAN | Default false |
| notified_at | TIMESTAMPTZ | Set when notified |
| created_at | TIMESTAMPTZ | Default NOW() |

## Cron Job Spec

```
Schedule: */5 * * * *
Command: poll subscriber_events WHERE notified=false
         for each row → POST to Telegram API
         → UPDATE notified=true, notified_at=NOW()
```

## Message Template

```
🎯 New Subscriber: {email}
   Source: {source}
   Time: {created_at}
```

## Environment Variables Needed

- `VV_SUPABASE_URL` — already set in Netlify
- `VV_SUPABASE_SERVICE_ROLE_KEY` — already set in Netlify
- `VV_TELEGRAM_BOT_TOKEN` — available in `~/.openclaw/.secrets`