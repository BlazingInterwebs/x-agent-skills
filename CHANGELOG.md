# Changelog

Versioning follows semantic versioning. During 0.x, record breaking changes
explicitly and provide migration notes; don't imply stable host compatibility.

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
