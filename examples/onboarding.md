# A week of drafts from a blank start

Input:

```text
Use $x-plan, then $x-post. I run a small automation consultancy. I have 30
minutes a day and post by hand. Audience is US owners; I'm in Singapore half the
year. No results cleared to share yet. No politics.
```

Expected behavior:

1. `x-plan` returns the 30-minute version of the daily rhythm, a weekly
   rotation where two-step slots fall back to thought posts (no cleared
   results), and a posting slot written in both zones (for example 9 AM ET
   is 9 PM Singapore while US daylight time is on).
2. `x-post` drafts Monday's thought post with three hooks of different types,
   picks one, and lists "none" or the facts to confirm.
3. No invented results, no "like and repost," no political topics, no
   scheduling. Placeholders `{{OFFER}}`, `{{PILLARS}}`, `{{CTA}}` stay visible
   in the plan where the user hasn't supplied them.
