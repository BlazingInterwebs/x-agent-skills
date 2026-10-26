# Daily rhythm, weekly rotation, reviews

Built for 30 to 45 minutes a day by hand, no posting tools. An agent can prep
drafts the night before; the user edits and posts.

## The 40-minute day

| Block | Time | What the user does |
| --- | --- | --- |
| 1. Warm up | 5 min | Answer replies on yesterday's post. Check notifications for real conversations. |
| 2. Replies, round 1 | 10 min | Open the reply List. 4 to 6 thoughtful replies on fresh posts. |
| 3. Post | 5 min | Post today's one post from the draft, edited to sound like them. |
| 4. Stay with it | 15 min | Answer every real reply on the new post. Between answers, 3 to 6 more replies on the List. |
| 5. Outlier check | 5 min | Glance at the last 7 days. Anything 3x the usual? Flag it for the weekly review. |

Short day (30 min): blocks 1, 2 (5 min), 3, 4 (15 min). Skip 5.
Long day (45 min): add a second 5-minute reply round later in the day.

## More than one post a day

Use the user's posts-per-day setting from context; the default is one. For 2
or 3 posts, repeat blocks 3 and 4 for each post (about 20 minutes each), and
space posts hours apart (see the shared cadence guidance). Give each slot a
different funnel stage or mix. Write the full time budget out so the user
can see it fits; if it doesn't, cut a post slot, not the reply time. Drop a
slot on a day with no good idea.

Why this order: warm up so the user is in the feed; post when the audience is
awake; then stay around, because replies on the user's own post carry weight
5.0 and new posts may get a short trial window (see the evidence reference).

## Posting slot
Pick one slot per post that matches where the audience is (check
analytics), write each in both the audience's and the user's time zones, and
keep them roughly steady for 4 weeks before comparing.

## Link placement
Follow the user's link placement setting. When links go in the first reply,
the plan includes a minute right after posting to add that reply.

## Weekly rotation (default)

| Day | Mix | Format default |
| --- | --- | --- |
| Mon | Thought | Single post (real question) |
| Tue | Two-step | Single post (only with a real `{{RESULT}}`; else swap to thought) |
| Wed | Thought | Single or long post |
| Thu | Personal | Single post, photo optional |
| Fri | Two-step or thought | Single post |
| Sat | Personal | Single post |
| Sun | Off, or one X Article draft (every other week) | Article |

Roughly 40% thought, 30% two-step, 30% personal. Tag each slot with a funnel
stage as well (default about 60% reach, 30% trust, 10% sales; use the user's
weights). Sales slots carry a soft CTA to `{{CTA}}`, only when it's real and
allowed by the user's context; otherwise make them trust slots. With one post
a day, the default sales share works out to about one soft-CTA post every
week or two; with more posts, scale by the share, not by count.

Article weeks: the Article takes one slot, and 2 to 3 quote posts of it
from new angles take later slots over the next weeks (see `x-longform`).

## Daily rules
- The user's posts-per-day number is a ceiling, not a quota. A slot with no
  good idea stays empty.
- No "gm," no filler. No asking for likes, reposts, or follows.
- Can't post today? Skip. Don't let an agent post.

## Weekly review (30 minutes)
The user pastes the week's analytics; run `x-audit`, then:
1. Scoreboard: posts, rough reply count, new followers, profile visits vs last week. No invented targets.
2. Top 3 posts by replies and profile visits, one line on why.
3. Outliers (3x+ the 20-post median) with a "5 more versions" plan.
4. Bottom 2: hook, topic, or timing?
5. Mix and funnel-stage check; adjust next week.
6. Conversion: which posts drove profile visits, link clicks, DMs (as the user reports them) and follows, by topic, format and stage. Shift toward what converts.
7. Reply List: add 3 who replied back, drop 3 who never engage or drifted into politics. Note new mutuals.
8. Add the week's best first line to the user's hook bank.
9. Queue next week's drafts to the posts-per-day setting (in notes, not a scheduler) plus one Article idea with its packaging and any quote-post follow-ups due.
10. Is the pinned post still the best answer to "why follow?" Does the profile point to one next step?

## Monthly (first weekly review of the month, 15 minutes extra)
- Top 5 of the month; shift next month's rotation about 10% toward the winning mix.
- Check the evidence "Reviewed" date; re-check if older than 60 days.
- Run the `x-presence` checklist.
