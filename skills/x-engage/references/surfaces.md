# X surfaces and feature checks

Last researched: 2026-10-16; operator additions 2026-10-26 and 2026-10-28; X Articles guide added 2026-10-29. Announcements describe capabilities and rollouts,
not a guarantee that a specific account has every feature today. Details and
sources are in [evidence](evidence.md).

| Surface | Who can make it | Best use | Evidence boundary |
| --- | --- | --- | --- |
| **Single post** (280 chars, longer with a subscription) | Everyone | Default. One idea, under 5 sentences (Bier, Sep 2025) | |
| **Long post** (up to 25,000 chars) | Paid subscribers (VERIFIED, X Help Center) | A short story or breakdown needing 6 to 15 lines | Only the first lines show before "Show more" |
| **Thread** | Everyone | Separable steps where each post stands alone | X publishes no thread vs long post comparison |
| **X Article** | Premium subscribers since Jan 7, 2026 (VERIFIED) | A deep piece, once a week or less | Bier: Articles grew 18x in 3 months (Mar 2026); Google indexing (Jun 2026); summaries and Listen added. Operators report large reach for small accounts when packaging is strong (UNVERIFIED, Oct 2026). X's Articles guide (Jan 16, 2026): tease, pin 24 to 72 hours, excerpt posts, reply to early readers. Subscriber-only Articles exist for eligible creators; the user decides |
| **Reply** | Everyone | Networking under other posts; conversation on your own | Out-of-network replies are filtered from For You (code) |
| **Quote post** | Everyone | Adding a real view to someone else's post | Quote weight 5.0 (code) |
| **Native video clip** | Everyone (length limits vary by subscription) | A short clip cut from the user's own long-form video, about one a week, with a standalone hook and captions | Video watch and dwell are modeled actions (code). Clip cadence is operator advice (UNVERIFIED) |
| **Spaces** | Hosting from the mobile app (third-party report, UNVERIFIED) | Occasional live talk with a co-host | Little 2026 guidance from X |
| **XChat group chats** | Joinable public links (Bier, Apr 22, 2026; 350 members and growing) | Small owned space | Replaces Communities |
| **Communities** | **Shut down May 30, 2026** (TechCrunch) | None | Advice to post in Communities is outdated |

## Links

Default: put the link in the post body with a line saying what's behind it.
The link-in-reply workaround is outdated per X (Jul 28, 2026).
`OpenLinkWeight` is positive (0.2) in the code. Keep the post standalone
without the click.

User override: if the user's context sets link placement to "first reply,"
follow it. Draft the post so it stands alone, then draft the first reply
with the link and one line on what's behind it. Mention X's guidance once
if asked; don't argue the choice on every draft. Log link clicks against the
parent post so the two placements can be compared on the user's account.

## Cadence

Default when context is silent: one strong post a day, plus replies. A
second post only for a genuinely good idea. Each post spends some reach
(Bier, Jan 2026) and extra posts by the same author in one feed refresh
decay (code).

Two growth paths (Ryan, Oct 28, 2026, UNVERIFIED). Pick one and commit;
don't drift in between:

| Path | Volume | Spacing | Fits |
| --- | --- | --- | --- |
| **Quality** | 3 to 5 original posts a day | 3+ hours apart | Personal brands, founders, experts. The path this collection supports |
| **Quantity** | Up to about 24 a day | About 1 hour apart | News and aggregator accounts that expect many flops |

This collection does not plan the quantity path for a personal brand: it
conflicts with X's guidance that each post spends reach and with
same-author decay, and it pushes toward filler. Say so if asked.

User override: if the user's context sets more original posts a day (for
example 3 to 5), space them at least 3 hours apart, or the user's minimum
spacing if it is longer (INTERPRETATION: spacing reduces same-refresh author
decay), give each a different funnel stage, mix or format, and keep the
quality bar. The number is a ceiling, not a quota: drop a slot rather than
post filler. Replies don't count toward the posts-per-day number.

## Timing

Post when the audience is awake, not the author. Buffer (2026, 1M+ posts):
weekday mornings 9 to 11 AM local. Sprout Social (2026): 12 to 6 PM Tue to
Thu. They disagree; treat both as starting points (UNVERIFIED for any one
account). New posts from accounts under 50k followers may get a short trial
slot while under about 200 impressions and under about 2 hours old (code
params, INTERPRETATION). Stay around for an hour after posting to answer
replies. When the author lives in another time zone, convert the audience's
window explicitly and confirm audience location in analytics.

## Profile surfaces

Display name (shows on every reply), handle, bio (160 characters), one link,
header (1500 x 500), photo, pinned post. "Follow author" is a modeled action
with weight 4.0.
