# Voice review for X

The user's supplied voice wins. These are defaults for X drafts.

## Sound like
- A sharp operator talking to a capable peer. Short sentences, strong verbs,
  "I" and "you," contractions.
- Honest uncertainty is fine ("I suspect, but I'm not sure").
- Humor from the situation, not a rehearsed punchline.

## Usually cut
- Hype words: game-changing, revolutionary, unlock, skyrocket, 10x (unless real).
- Guru tone, motivational poster energy, "In today's fast-paced world."
- Generic AI shapes: "It's not just X, it's Y," "Let's dive in," stacked
  adjectives, "Here's why that matters:" everywhere, rhetorical question piles.
- Threadboy formatting: emoji bullets, "A thread" plus pointing emoji, "Bookmark this."
- Engagement asks for likes, reposts, or follows.
- AI slop: text that could have come from anyone, filler openers, summaries
  of what was just said, a neat moral on every post.
- Punctuation the user bans (many voices ban em dashes; use a period,
  comma, or line break).

## X-specific edits
- If the first line could be cut, cut it.
- One idea per post.
- Name the specific thing so it's clear who the post is for.

## Final check
1. Would the user say this out loud? 2. Any banned punctuation? 3. Any claim
they can't back? 4. Any bait ask? 5. Could a stranger tell who they help?
6. For replies: has the user rewritten it in their own words? Replies are
the easiest place to spot AI text, so a reply draft is never posted as is.

`scripts/editorial.py` lists flags for some of these. It never rewrites, and
a flag is a prompt to look, not a verdict.
