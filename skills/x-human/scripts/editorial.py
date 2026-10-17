#!/usr/bin/env python3
"""Return original X draft text and contextual editorial flags; never rewrite or score."""

import argparse
import json
from pathlib import Path
import re
import sys

RULES = (
    ("dash_punctuation", re.compile("[\u2014\u2013]"),
     "Check the user's punctuation rules; many voices ban em and en dashes."),
    ("generic_opening", re.compile(r"\bin (?:today's|this) (?:fast[- ]paced|ever[- ]changing) world\b", re.I),
     "Check whether this framing adds context or matches the supplied voice."),
    ("hype_word", re.compile(r"\b(?:game[- ]changing|game[- ]changer|revolutionary|skyrocket\w*|unlock your)\b", re.I),
     "Hype wording; keep only if the user's voice and evidence support it."),
    ("generic_ai_shape", re.compile(r"\b(?:it's not just .{1,40}?, it's|let's dive in|here's why that matters)\b", re.I),
     "Common generic phrasing; check against the supplied voice."),
    ("unsupported_certainty", re.compile(r"\b(?:guaranteed results|guaranteed growth|everyone will|always works)\b", re.I),
     "Check scope and evidence; do not replace certainty with invented proof."),
    ("engagement_request", re.compile(r"\b(?:like and repost|like and retweet|repost if|follow for more|follow me for|drop a comment|bookmark this|agree\?|thoughts\?)", re.I),
     "Possible engagement ask; X's Original Content Rewards terms prohibit soliciting engagement. A genuine question may be fine."),
    ("low_effort_post", re.compile(r"^\s*(?:gm|gn|this|so true|great post|100%)\W*\s*$", re.I | re.M),
     "Low-effort post or reply; X staff say these spend reach."),
    ("placeholder", re.compile(r"\{\{[A-Z_ ,:.'()a-z0-9-]+\}\}"),
     "Unfilled placeholder; the user must supply a true value before posting."),
    ("inspect_character", re.compile("[\u200b\ufeff\u00ad]"),
     "Inspect the character in context; do not remove meaningful language characters automatically."),
)


def review(text):
    flags = []
    for kind, pattern, reason in RULES:
        for match in pattern.finditer(text):
            flags.append({"kind": kind, "start": match.start(), "end": match.end(),
                          "excerpt": match.group(), "reason": reason})
    flags.sort(key=lambda flag: (flag["start"], flag["kind"]))
    return {"text": text, "characters": len(text), "flags": flags,
            "notice": "Contextual editorial review only; no AI authorship or growth prediction."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="UTF-8 text file, or - for stdin")
    args = parser.parse_args()
    try:
        text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
        print(json.dumps(review(text), ensure_ascii=False, indent=2))
    except OSError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
