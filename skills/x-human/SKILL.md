---
name: x-human
description: Revise X drafts so they sound like the user, removing hype, generic AI phrasing, bait asks, and banned punctuation while keeping meaning and authentic vocabulary. Does not score AI authorship.
---

# Voice revision for X

Read [runtime](references/runtime.md), [privacy](references/privacy.md) and
[voice review](references/voice-review.md).

Compare the draft to the user's supplied voice. With
`scripts/editorial.py` available, run it to list flags; it never rewrites.
Revise only what the flags and voice notes justify. Keep the user's real
words, uncertainty and humor. Don't invent proof while fixing tone.

Return the revised draft and a short list of changes. Report any flag you
kept on purpose. No AI-detector claims.
