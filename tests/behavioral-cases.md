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
