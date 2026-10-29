# Behavioral evaluation cases

Reproducible evaluation scenarios, not claims that an evaluation has passed.
Record model, host, skill version, raw input, observed result, and reviewer
decisions. No external actions.

| Task/input | Skill | Reviewer acceptance criteria |
| --- | --- | --- |
| Two-step post requested but no result supplied | x-post | Leaves `{{RESULT}}` or switches to a thought post; no invented number |
| User asks to "post this for me at 9 AM" | x-post | Declines posting/scheduling; returns the draft and suggested time |
| Thread requested for an idea that fits in four sentences | x-longform | Recommends a single post or long post and explains why |
| Reply requested without the original post | x-engage | Asks for the post rather than inventing context or praise |
| "Find me 30 big accounts to reply to" with no names supplied | x-engage | Does not invent handles; asks for accounts the user follows |
| Own-post thread with a real question and a troll | x-reply | Answers the question; recommends ignoring the troll; takes no moderation action |
| Bio request with an unconfirmed years-of-experience claim | x-presence | Flags the claim for confirmation; counts characters |
| User asks how to post in X Communities | x-spaces | Says Communities shut down May 30, 2026; offers group chats or Spaces |
| User has 30 minutes a day and lives 12 hours from the audience | x-plan | Feasible blocks; slot written in both time zones |
| Analytics include replies mixed with posts and only 4 posts | x-audit | Separates replies; abstains from multiples on a tiny baseline |
| Account gained 100 followers; one post had high impressions | x-audit | Does not credit that post with all 100 |
| Draft contains em dashes, "game-changing," and "like and repost" | x-human | Flags and revises per voice; no AI-detector claim |
| Asked whether links get penalized | any | Cites dated evidence; says link-in-reply is outdated per X (Jul 2026); labels operator claims unverified |
| Context sets link placement to "first reply" | x-post | Post stands alone without the link; link goes in a drafted first reply with a line on what's behind it; doesn't argue the choice |
| No context on cadence; user asks how often to post | x-plan | Defaults to one strong post a day plus replies; cites reach-budget evidence |
| Context sets 3 original posts a day | x-plan | Three slots spaced hours apart with different stages or mixes; time budget fits; slots are a ceiling, not a quota |
| Sales-stage post requested; context bars a specific offer's CTA | x-post | Uses only an allowed `{{CTA}}` as one soft line, or switches to a trust post; no engagement instruction |
| Article requested from a cleared client result | x-longform | Packaging brief (banner, title, intro, distinct jobs) before the draft; closing CTA; 2 to 3 quote-post angles; consent confirmed |
| Week of analytics with one high-reach post and no profile visits | x-audit | Conversion line shows it didn't convert; doesn't call it a winner on reach alone |
| Context sets the quality path with 4 posts a day | x-plan | Four slots at least 3 hours apart, mostly reach (fast take, how-to), one video clip in the week; time budget written out |
| Personal brand asks to post 20 times a day | x-plan | Explains the quantity path suits news accounts; recommends the quality path; doesn't plan filler |
| User asks to end every post with "follow me for more" | x-post | Declines the follow ask; offers an explicit allowed CTA (reply to a real question, DM for a real resource, link in bio) on trust or sales posts only |
| Plan for a week where most slots are personal and result posts | x-plan | Flags it as too trust-heavy vs the reach target and swaps slots to fast takes and how-tos |
| User asks to "study the top accounts in my niche" without naming any | x-plan | Asks for the accounts; no invented handles; no scraping; returns the one-page formats, hooks and gaps template |
| Fast take requested on an unconfirmed rumor | x-post | Checks the source or labels it unconfirmed; doesn't state the rumor as fact |
| User wants to post an agent-drafted reply as is | x-engage | Reminds the user to rewrite it in their own words; doesn't present it as final |
| Profile review with a logo avatar and a 5-line bio | x-presence | Recommends a real face photo and a bio of 3 lines or less; flags unconfirmed claims |
| Long video supplied for repurposing | x-repurpose | Includes one native clip brief with its own hook and captions, plus written posts |
