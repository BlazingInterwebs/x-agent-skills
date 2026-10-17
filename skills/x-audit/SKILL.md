---
name: x-audit
description: Review supplied X analytics, find same-account outliers, run the weekly review, and plan 5 more versions of what worked. Analyzes only supplied data; never scrapes.
---

# X audit and weekly review

Read [runtime](references/runtime.md), [metrics](references/metrics.md),
[evidence](references/evidence.md) and [audit](references/audit.md).

Use only analytics the user pastes or exports. Separate original posts from
replies. Compute same-account medians that exclude the post being judged.
With `scripts/compare.py` available, run it on a CSV; otherwise show the
manual calculation. Abstain when the baseline is too small or zero.

Return the scoreboard, top posts, outliers with a one-line hypothesis each,
flops, mix check, reply-list notes, and a "5 more versions" plan. Don't
credit one post with net weekly growth. Route new drafts to `x-post`.
