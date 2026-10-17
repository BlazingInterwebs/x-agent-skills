# Metric definitions and comparable evidence

## Availability

Use only owner-supplied analytics (export, screenshot, or pasted numbers).
Don't scrape the account. Analytics fields vary by subscription plan
(UNVERIFIED which fields each plan shows). Unknown metrics stay unknown.

## What to log per post

Date, time and timezone, mix (thought / two-step / personal or the user's
own), hook type, format (single, long post, thread, Article, quote, reply),
impressions, replies, reposts + quotes, bookmarks, profile visits, new
follows (if shown), link clicks (if any).

| Objective | Useful evidence | Do not confuse with |
| --- | --- | --- |
| Discovery | Impressions on original posts, profile visits | Impressions on replies (excluded from Original Content Rewards eligibility) |
| Conversation | Replies, quotes, replies from mutuals | Likes alone |
| Follow conversion | Profile visits and follows near the post date | Net follower change for the whole week |
| Traffic | Link clicks with a stated destination | Impressions on a link post |

## Outliers (relative to the same account, never to other accounts)

1. Take the last 20 original posts (not replies).
2. Find the median impressions and the median replies, excluding the post
   being judged.
3. **Outlier** = 3x or more the median on impressions, replies, or profile
   visits. **Watch** = 2x to 3x.
4. For each outlier, write one line on why it likely worked (hook type,
   topic, specific noun, personal moment, timing). That's a hypothesis.

The 3x line is this collection's working threshold, not an X rule. Adjust
once there are 60+ posts. Prefer replies and profile visits over impressions;
impressions can spike on a topic that doesn't bring the right followers.

Helper (where available): `scripts/compare.py` computes same-account,
target-excluded medians and multiples from a CSV. It abstains when the
baseline is too small or zero.

## Attribution limits

Don't credit one post with a week's net follower growth. Don't treat a
correlation with posting time as a cause. Record limits next to every result.
