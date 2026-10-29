# Changelog

Versioning follows semantic versioning. During 0.x, record breaking changes
explicitly and provide migration notes; don't imply stable host compatibility.

## 0.4.0 - 2026-10-29

Sourced from @XCreators, "The ultimate guide to Articles on X" (Jan 16, 2026), X's own advice.

- x-longform: Article writing rules (purpose line, specific curiosity title, skimmable structure, voice, evidence after every claim with real proof only, cut 20 to 30%, visuals, strong close with a summary, a question and one thing to try), launch and promotion steps (tease, pin 24 to 72 hours, reply to early readers, excerpt posts, evergreen reshares), and Subscriber-only Articles as an optional choice the user makes.
- x-plan: Article weeks include the tease, pin window, early-reply block, excerpt posts and evergreen reshares.
- x-repurpose: Article excerpt posts and evergreen reshares.
- Shared surfaces and evidence: the guide added as a primary source. Its "encourage shares" close is not adopted; the no repost or share asks rule is unchanged.
- Context template: Subscriber-only Articles setting (off by default).
- New behavioral cases. No breaking changes.

## 0.3.0 - 2026-10-28

Sourced from Ryan (@ryangrowthh), "How to build a personal brand on X. Full crash course" (Oct 28, 2026). Operator advice, labeled UNVERIFIED.

- Shared growth: own a niche (overlap a hot niche with real skills, own a category, say what only you can say), proof is king (real, cleared proof only), and a monthly niche research step (top 10 to 20 accounts the user names; formats, hooks and gaps from their replies; one-page brief; read only, no scraping).
- Content mix default now leans to reach: fast take 25%, how-to 25%, thought 15%, two-step 15%, personal 20%. Funnel reach default is 60 to 70%. Trust-heavy weeks are flagged.
- Explicit CTAs: one named action and what the reader gets. The no like, repost or follow asks rule is unchanged, so Ryan's "follow" CTA example is not adopted.
- Curiosity-gap hooks as the default packaging for reach posts; format mix (short, long, Article, video).
- Avoid list adds negativity and attacking creators, reply-guy behavior, and AI slop. Agent-drafted replies must be rewritten by the user in their own words before posting.
- Surfaces: native video clip row; two cadence paths (quality 3 to 5 a day at least 3 hours apart, quantity for news accounts only). The one-a-day default when context is silent is unchanged.
- x-plan: quality-path days, new weekly rotation with a weekly video clip, reach-share check, monthly niche research.
- x-presence: profile basics (face photo, bio of 3 lines or less, simple header, optional bio CTA).
- x-engage, x-reply, x-human: not-a-reply-guy rules and the rewrite-in-your-own-words step.
- x-repurpose: one native clip a week from long-form video.
- x-audit: format and cadence lines, trust-heavy flag.
- Context template: niche and category, posting path, format targets, niche research list, video source.
- New behavioral cases for the above.
- Migration: no breaking changes. Users who set their own mix weights keep them; the new default mix applies only when context is silent.

## 0.2.0 - 2026-10-26

- Shared growth: funnel-stage layer (reach / trust / sales, default 60/30/10, user weights override), soft CTA rules, profile-as-sales-page note, conversion tracking, and a ranking-signals section (weights re-checked against the algorithm repo, labeled as weights on predicted probabilities).
- Shared surfaces: cadence and link placement are now defaults with explicit user overrides (posts per day with spacing; link in body or first reply).
- Shared runtime and metrics: draft output adds stage, CTA and first-reply fields; log adds stage, CTA, link placement and user-reported DMs; new conversion objective.
- Evidence: new section 9 of dated operator tactics, all UNVERIFIED; new operator sources; review dates updated.
- x-longform: Article packaging trifecta, Article types, end CTA, quote-post distribution plan.
- x-plan: posts-per-day blocks, funnel-stage rotation, Article follow-ups, conversion step in the weekly review.
- x-audit: funnel and conversion lines in the weekly output.
- x-post: format shapes from high-reach posts, drafting from a pattern brief, soft CTA rules.
- x-presence: profile as sales page, one next step, onboarding library.
- x-repurpose: existing assets into Articles, one-to-many loop.
- x-engage: viral-moment replies and late quote posts.
- Context template: posts per day, link placement, funnel weights, allowed CTAs, consent list, avoided terms, asset list.
- `.gitignore` excludes `context.local.md`, `*.local.md` and `*.private.md`.
- New behavioral cases for link placement, cadence, soft CTAs, Article packaging and conversion.
- Lead scout deferred (see roadmap).
- Migration: no breaking changes. Users who relied on the one-post and link-in-body defaults need no action; set the new context fields to override.

## 0.1.0 - 2026-10-16

- Initial pilot with 10 modular X capabilities.
- Evidence register grounded in the open-source For You code (commit 862a1235), X staff posts and X creator docs.
- Daily hand-posting rhythm, weekly rotation and weekly review.
- Comparison and editorial-review helpers adapted from Facebook Agent Skills.
- Self-contained resource bundling, no-overwrite installer, structural/unit tests, behavioral cases, and CI.
- No posting, scheduling, liking, following, DMs, scraping, or account changes.
