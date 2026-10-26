# Evidence register

Reviewed 2026-10-16 (US Eastern); operator tactics in section 9 added
2026-10-26. This is a dated research snapshot, not
a live policy feed. X changes parameters often and publishes many changes to
the repo. Follow source links for current decisions and record a newer review
date when changing a claim. Never present inaccessible documentation as verified.

Labels:
- **VERIFIED (code):** read directly in `xai-org/x-algorithm`, commit
  `862a1235` (committed 2026-10-16 8:44 PM EDT).
- **VERIFIED (X):** stated by X or X staff in a primary source.
- **INTERPRETATION:** my reading of code or posts. Plausible, not confirmed.
- **UNVERIFIED:** operator or third-party claim. Treat as a hypothesis.

## 1. The basic model (VERIFIED, code)
- For You mixes in-network posts (accounts the viewer follows) and
  out-of-network posts found by ML retrieval (Phoenix, SimClusters, a
  popular-posts list). One transformer ranks both.
- The model predicts, per viewer and per post, the probability of each
  action, then sums `weight × probability`. Weights scale *predicted
  probabilities*, not raw counts. The repo says plainly that "1 report
  cancels 468 likes" is a misreading.
- Actions modeled: like, reply, repost, quote, share, share via DM, share
  via copy link, clicks (post, profile, link, photo, video, quoted post),
  dwell and dwell time, video watch, follow author, and negatives (not
  interested, mute, block, report, not dwelled).

## 2. Current weights (VERIFIED, code, `home-mixer/params/param.rs`)

Re-checked 2026-10-26 against the file (synced 2026-10-23): unchanged.
`NotDwelledWeight = -0.02` (scroll-past). `SimclustersMaxCandidateAgeHours = 48`
applies to the SimClusters source only.

| Action | Weight | Plain read |
| --- | --- | --- |
| Share via copy link | 20.0 | Content people send elsewhere |
| Reply | 5.0 | Conversation |
| Quote | 5.0 | Conversation |
| Share via DM | 5.0 | "Send this to a friend" posts |
| Follow author | 4.0 | Posts that make strangers want more of you |
| Share | 2.0 | |
| Repost | 1.0 | |
| Like | 0.66 | |
| Click (post) | 0.3 | |
| Open link | 0.2 | Positive. Link clicks are not penalized in this sum |
| Dwell | 0.05 | Plus continuous dwell-time terms |
| Profile click | 0.0 | |
| Not interested | -52.272 | Bait and off-topic posts hurt |
| Mute author | -58.8 | |
| Block author | -31.2 | |
| Report | -234.0 | |

Bidirectional follow reply boost: 15.0. Shipped July 13, 2026 at 20, set
to 15 on July 24, 2026 (repo doc `docs/BIDIRECTIONAL_BOOST_CHANGE.md`).
It raises the reply weight for original posts from people you mutually
follow. Nikita Bier described it as boosting visibility to your mutuals.

INTERPRETATION: because the weights multiply probabilities, and negative
actions are rare but weighted heavily, the highest-leverage moves are posts
people reply to, quote, or send to someone, and posts that don't make
people hit "not interested." Mutual follows with real peers now matter more.

## 3. Adjustments after scoring (VERIFIED, code README)
- **Author diversity:** each extra post from the same author in a feed
  refresh gets a decaying multiplier, down to a floor. Flooding doesn't stack.
- **Out-of-network discount:** posts from accounts the viewer doesn't follow
  are multiplied by a factor below 1. So are replies and reposts from
  accounts the viewer does follow.
- **New-author boost:** posts from authors with impressions below a
  threshold are lifted toward a target position. Current params:
  `ColdStartImpressionThreshold = 200`, `ColdStartFollowerCap = 50000`,
  `ColdStartMaxPostAgeSecs = 7200`, Thompson sampling enabled.
  INTERPRETATION: a fresh post (under about 2 hours old) from an account
  under 50k followers that hasn't hit about 200 impressions may get a
  trial slot. That's a reason to post when your audience is awake.
- **Filters:** `OONRetweetReplyFilter` removes replies and reposts from
  accounts the viewer doesn't follow. `NewUserMinEngagementFilter` holds
  back out-of-network posts from new accounts below an engagement bar.
  INTERPRETATION: replies to bigger accounts are discovered in the
  conversation under that post, not in strangers' For You feeds. Replies
  are a networking and profile-visit tool, not a reach tool by themselves.

## 4. Links (as of 2026-10-16)
- VERIFIED (X): Oct 19, 2025, Nikita Bier said link posts got less reach
  because the in-app browser covered the like and reply buttons, so X got
  weaker signal. X moved the post to the bottom of the browser on iOS.
- VERIFIED (X): Apr 8, 2026, Bier: links were never "deboosted"; with the
  buttons uncovered, links "have the same shot." May 31, 2026: "Links will
  not deboost your post."
- VERIFIED (X): Jul 28, 2026, Bier to Mark Zuckerberg: "you do not need to
  put the links in replies anymore." Jul 29, 2026, Elon Musk to Paul Graham:
  X hasn't penalized linked posts "for over a year" (reported by PPC Land).
- VERIFIED (code): `OpenLinkWeight = 0.2`, positive.
- Context: Musk acknowledged lower reach for link posts in 2024. X now
  frames it as an engagement-signal problem, not a penalty. Some operators
  still report weaker numbers on link posts. UNVERIFIED either way for
  any given account.
- **Practice:** put the link in the post body with a clear line about
  what's behind it (Bier's advice, Apr 2026). The old link-in-reply
  workaround is outdated as of July 2026. A post should still stand alone
  without the click. Test on the user's own account and log the result.

## 5. Reach budget and low-effort posting
- VERIFIED (X, secondary report): Jan 2026, Bier said each post "uses some
  of your reach for that day," that the average user sees about 20 to 30
  posts a day, and that strings of zero-engagement "gm" posts reduce how
  far the next post goes. Source is a Muskonomy write-up quoting his posts;
  the original thread was not opened directly. The mechanism isn't visible
  as a single param in the code. Treat the direction as reliable, the
  details as UNVERIFIED.
- VERIFIED (X): Sep 4, 2025 (Business Insider): post "one unexpected
  insight" from your experience, "under 5 sentences," every day for 6 months.

## 6. Video, media, Grok
- VERIFIED (code): `VqvWeight = 0.0` at the moment, video open 0.02,
  photo expand 0.05. Media alone isn't a big lever in the weighted sum
  right now. Dwell and conversation are.
- VERIFIED (X, reported): Oct 2025 Musk said Grok would read every post to
  match content to users (The Verge). INTERPRETATION: clarity about topic
  helps retrieval. Write so the subject is obvious.

## 7. What's not known
- Production model weights and the exact out-of-network and diversity
  factors in live serving (repo shows defaults; live values can differ).
- Whether Premium changes For You ranking. In the code I checked,
  verified/Premium status seeds the `user-cred-v2` credibility PageRank
  (used for account trust labels), and Premium affects ad logging. I found
  no Premium multiplier in the For You weighted sum. UNVERIFIED that none
  exists elsewhere.
- Third-party skill packs from early 2026 say the weights are hidden. That
  was true before the Aug 13, 2026 repo update and is now outdated.

## 8. X Premium: verified vs claimed

Status as of 2026-10-16. Pricing and tiers changed on Oct 12, 2026. Check the
user's own subscription screen before any decision.

| Claim | Status | Source |
| --- | --- | --- |
| On Oct 12, 2026 X Premium became part of "The X Subscription," starting at $8/month; existing Premium and Premium+ users can switch "for the same price or less," and switching doesn't affect Creator Subscriptions or Original Content Rewards enrollment | VERIFIED (X) | @XCreators, Oct 12, 2026 |
| New tier names and contents: "Plus" $8 (checkmark, reply boost, Articles, Radar, Advanced Analytics) and "Premium" $30 (higher reply boost, near ad-free, more AI) | UNVERIFIED (third party) | Postory blog |
| Subscribers can write long posts up to 25,000 characters | VERIFIED (X Help Center, archived) | About X Premium |
| Articles open to all Premium subscribers (not just Premium+) | VERIFIED (X) | Bier, Jan 7, 2026 |
| Replies from subscribers get some prioritization in conversations, with more on higher tiers | VERIFIED as stated by X; size UNVERIFIED | About X Premium: "slight preference for replies from verified accounts," X "testing the levels" |
| Reply ranking is reliable | Doubtful | Bier, Mar 18, 2026: the reply algorithm "is currently the worst product in the company" (said while announcing a fix) |
| Premium boosts your posts in For You | UNVERIFIED | No Premium multiplier found in the For You weighted sum in the open-source code. Verified status seeds the user-cred-v2 trust score. Bier (Jan 2026) told a Premium user complaining about reach that paying doesn't override quality signals |
| Old Creator Revenue Sharing (the 5M impressions in 3 months era) | RETIRED | Closed to new enrollment Aug 7, 2026; ended Sep 7, 2026 |
| **Original Content Rewards** eligibility: 18+, eligible country, good standing, subscribed to Premium/Premium+/Premium Business, **500 verified followers**, **500,000 Home Timeline impressions from verified users in the last 90 days (replies excluded)**, regularly posts original content | VERIFIED (X) | @XCreators Article, Aug 7, 2026 |
| OCR pays on "qualified impressions": unique impressions from Premium users on Home Timeline where at least 50% of the post is visible. Payout every two weeks. No rate published | VERIFIED (X) | same |
| OCR violations include soliciting engagement ("repeatedly instructing users to engage"), automation, reuploaded content, and content "exclusively focused on monetization coaching" | VERIFIED (X) | same |

### Premium in practice
- **Useful features for growth work:** long posts, Articles, edit, and the
  reply prioritization (helps a reply routine a bit, size unknown).
- **Revenue share is a separate goal.** The Original Content Rewards bar is
  high for a new or reset account. Don't plan content around it unless the
  user says it's an objective.
- The "no soliciting engagement" rule backs a no-bait approach.
- Don't expect Premium alone to fix reach. Quality and replies do the work.
- Recommend nothing that costs money; buying or changing a plan is the user's call.

## 9. Operator tactics (UNVERIFIED, added 2026-10-26)

Practitioner advice, dated. None of it is an X rule or visible in the code.
Treat each item as a hypothesis to test on the user's own account.

| Tactic | Source | Notes |
| --- | --- | --- |
| Funnel mix of about 60% reach, 30% trust, 10% sales | Ryan, Oct 26, 2026 | Not every post sells. Weights are a starting point |
| Trust content types: case study, result, behind the scenes, framework, lesson | Ryan, Oct 26, 2026 | Results and case studies need cleared, real material |
| Profile as the sales page: bio, pinned post, header and link point to one next step | Ryan, Oct 26, 2026 | Consistent with "follow author" weight 4.0 (code) |
| Soft CTA: one line at the end of the best posts | Ryan, Oct 26, 2026 | Keyword-comment CTAs conflict with X's no-solicitation terms; this collection excludes them |
| Weekly conversion tracking (profile visits, clicks, DMs, follows by topic and format) | Ryan, Oct 26, 2026 | DMs are user-reported |
| Article packaging decides the click: banner, title and intro each do a different job (sell the outcome, or answer one objection), with no overlap; no generic AI banners | Chan, Oct 26, 2026 | His reach claims for small accounts (six-figure Article views) are self-reported |
| Process Articles that show how the work is done; Articles built from existing assets (a winning post, a lead magnet, a client result, an internal SOP) | Chan, Oct 26, 2026 | Client material needs consent (see privacy) |
| Quote-post your own Article later from a new angle; end every Article with a CTA | Chan, Oct 26, 2026 | Each quote must add something new; never repost the same text |
| Draft from a pattern brief mined from a niche watchlist, never by rewriting someone's post | kiosa, Sep 16, 2026 | Method only. This collection doesn't scrape; work from posts the user supplies |
| One long piece becomes many short ones; keep 5 to 10 evergreen pieces as a profile onboarding library | Hades, Aug 12, 2026 | Summarized secondhand |
| High-reach business posts in one 48-hour sample were mostly 1 to 3 sentences, no links, often a reframe, a "signs you'll..." list, a named tool and action, or a changed-my-mind self-own; CTAs were rare | Operator observation, Oct 24 to 26, 2026 | Small sample, one niche, one window. A format signal, not a rule |
| Replies on fast-rising posts from bigger accounts in the niche earn visibility; late arrivals do better with a quote post that adds something | Operator observation, Oct 2026 | Reply timing claims stay UNVERIFIED (see section 3 and the engagement reference) |

## 10. Sources

Accessed 2026-10-16, operator additions 2026-10-26 (US Eastern). Labels: primary (X, X staff, X's
code), operator (practitioner content), secondary (press or third-party
summaries). GitHub skills that informed this collection are credited in the
repository's ACKNOWLEDGMENTS.

### X's own code and docs (primary)
- xai-org/x-algorithm, For You algorithm repo (commit `862a1235ca4d743cc48211309ebbbcc1a5a540a3`, committed 2026-10-16 8:44 PM EDT): https://github.com/xai-org/x-algorithm
  - README (pipeline, actions, adjustments, filters, notable updates): https://github.com/xai-org/x-algorithm/blob/main/README.md
  - Weights and cold-start params: https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs
  - Bidirectional follow boost history: https://github.com/xai-org/x-algorithm/blob/main/docs/BIDIRECTIONAL_BOOST_CHANGE.md
  - user-cred-v2 (verified status seeds trust PageRank): https://github.com/xai-org/x-algorithm/tree/main/user-cred-v2
  - Original open-source commit, Jan 20, 2026: https://github.com/xai-org/x-algorithm/commit/aaa167b3de8a674587c53545a43c90eaad360010
- @XCreators, "Original Content Rewards Program" Article, Aug 7, 2026: https://x.com/XCreators/status/2085835082166653393
- X Help Center, Original Content Rewards (linked from the Article; returned 403 to fetch): https://help.x.com/en/using-x/original-content-rewards
- @XCreators, X Premium becomes part of The X Subscription, Oct 12, 2026: https://x.com/XCreators/status/2109783762955649367
- About X Premium, X Help Center (archived copy; live page returned 403): https://archive.ph/AqTHt and https://help.x.com/en/using-x/x-premium

### X staff posts (primary)
- Nikita Bier, new accounts are X's toughest challenge, Jan 20, 2026: https://x.com/nikitabier/status/2013410692444102793
- Bier, Articles open to all Premium subscribers, Jan 7, 2026: https://x.com/nikitabier/status/2008805057849082018
- Bier, Articles grew 18x in 3 months, Listen launch, Mar 6, 2026: https://x.com/nikitabier/status/2029980825262117177
- Bier, "decided to reward Articles instead of single posts," Mar 19, 2026: https://x.com/nikitabier/status/2034523771080511495
- Bier, Article summaries, Mar 19, 2026: https://x.com/nikitabier/status/2034675770875158973
- Bier, Google indexing X Articles, Jun 3, 2026: https://x.com/nikitabier/status/2062161439931138199
- Bier, reply algorithm "worst product in the company," Mar 18, 2026: https://x.com/nikitabier/status/2034293888350114233
- Bier, only home timeline impressions count for payouts, Jan 18, 2026: https://x.com/nikitabier/status/2012988561834873165
- Bier, reply impressions only count when they reach Timeline, Feb 1, 2026: https://x.com/nikitabier/status/2017820786577576116
- Bier, in-network-only replies for first 20 minutes on his posts, May 9, 2026: https://x.com/nikitabier/status/2053186069710164275
- Bier, links never deboosted, Apr 8, 2026: https://x.com/nikitabier/status/2041911302541730237
- Bier, "Links will not deboost your post," May 31, 2026: https://x.com/nikitabier/status/2060937537456324868
- Bier to Zuckerberg, no need for links in replies, Jul 28, 2026: https://x.com/nikitabier/status/2082217171506344297
- Bier, boost for mutuals, Jul 13, 2026: https://x.com/nikitabier/status/2076747704248758617
- Bier, XChat group chat links replacing Communities, Apr 22, 2026: https://x.com/nikitabier/status/2047041338106159484

### Press and secondary
- PPC Land, Musk: X hasn't penalized links "for over a year," Jul 29, 2026: https://ppc.land/x-drops-year-old-link-penalty-musk-tells-zuckerberg-on-platform/
- Roboin, X denies link deboost, recommends in-post links, Apr 13, 2026: https://roboin.io/article/en/2026/04/13/x-denies-link-deboost-recommends-in-post-links/
- The Verge, X changes link handling (Oct 2025): https://www.theverge.com/news/802480/x-is-changing-how-it-handles-links-to-try-and-keep-you-in-the-app
- Fast Company, X link UX update (Oct 2025): https://www.fastcompany.com/91425207/xs-ux-update-wants-to-save-your-links-from-social-medias-black-hole
- The Verge, Original Content Rewards replaces revenue sharing: https://www.theverge.com/tech/977143/x-revenue-sharing-original-content-rewards
- Business Insider, Bier's "one unexpected insight" playbook, Sep 5, 2025: https://www.businessinsider.com/x-product-head-nikita-bier-playbook-get-rich-posting-2025-9
- Muskonomy, Bier on "gm" replies and daily reach, Jan 10, 2026 (secondary; quotes Bier's thread): https://muskonomy.com/reply-guys-on-x-are-officially-dead-says-nikita-bier-head-of-product-at-x/
- TechCrunch, X shutting down Communities, Apr 23, 2026: https://techcrunch.com/2026/04/23/x-is-shutting-down-communities-because-of-low-usage-and-lots-of-spam/
- Roboin, X scales back Communities, Apr 9, 2026: https://roboin.io/article/en/2026/04/09/x-scales-back-communities-feature-raising-possibility-of-shutdown/
- PPC Land, Articles open to all Premium: https://ppc.land/x-opens-articles-to-all-premium-users-ending-exclusive-pricing-tier/
- Sprinklr Help, X Premium tiers table: https://www.sprinklr.com/help/articles/x-premium-and-its-three-tiers/x-premium-and-its-three-tiers/67b6cd8a05f0a008a99f491d
- Postory, X Premium vs Premium Plus 2026 (new tier details; UNVERIFIED): https://postory.io/blog/x-premium-vs-premium-plus
- Only Twitter blog, Spaces hosting (UNVERIFIED): https://blog.onlytwitter.com/x-spaces-not-working/

### Operators
- Ryan (@ryangrowthh), "Distribution 101: A Guide to Reaching Millions," X Article, Oct 16, 2026 9:02 AM EDT: https://x.com/ryangrowthh/status/2111080389565640897. Contributed: story and chapters, rented/owned/earned vehicles, the five hook types, 50/50 packaging, platform-native formatting, build your network, steal formats not content, 5 more versions of outliers, point channels at each other, repurposing.
- Buffer, best time to post on X 2026: https://buffer.com/resources/best-time-to-post-on-twitter-x/
- Sprout Social, best times to post on X 2026: https://sproutsocial.com/insights/best-times-to-post-on-twitter/
- Reachmore, X reply strategy 2026 (5x to 20x target size, early replies; UNVERIFIED): https://reachmore.co/blogs/x-reply-strategy-2026
- Reachmore, replying to big accounts: https://reachmore.co/blogs/reply-to-big-accounts-on-x
- Ryan (@ryangrowthh), "How to Make Money on X with Grok Bot," X Article, Oct 26, 2026: https://x.com/ryangrowthh/status/2114730076197798214. Contributed: funnel mix, trust content types, profile as sales page, soft CTAs, conversion tracking. Income claims not used.
- Benjamin Chan (@ItsMeBenChan), "How we revive dead accounts with Twitter articles," X Article, Oct 26, 2026: https://x.com/ItsMeBenChan/status/2114653397571825937. Contributed: Article packaging, process Articles, Articles from existing assets, quote-post redistribution, end CTA. View claims UNVERIFIED.
- kiosa (@thegreatest_sv), X Article on a pattern-brief drafting desk, Sep 16, 2026: https://x.com/thegreatest_sv/status/2100236496837984387. Contributed: draft from a pattern brief, not a rewrite. Tool not used or endorsed.
- Hades (@0xhvdes), "How 60 Days of Posting Content Can Change Your Life," X Article, Aug 12, 2026: https://x.com/0xhvdes/status/2087548852173721792. Contributed: profile onboarding library, one-to-many content loops. Income claims not used.
