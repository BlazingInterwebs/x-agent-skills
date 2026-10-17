# X Agent Skills

X-native agent skills for growing an account by hand: useful posts, long-form,
real replies, a clear profile, a sustainable daily rhythm, and evidence-led
review.

Turn an idea into a post a stranger can understand. Build a network through
replies that stand alone. Plan a 30 to 45 minute day you can keep. Learn from
the analytics you actually have, without guessing hidden numbers.

**10 modular skills. Free, MIT-licensed, independently authored.** Supply your
own context; no personal brand is built in.

## Start with a real situation

```text
Use $x-post. Write a thought post for small business owners about follow-up.
Real question, no bait, under five sentences. No results to share yet.
```

The workflow picks one idea, writes three hooks of different types, and
returns a draft plus an alternate hook. It doesn't invent a result or add a
"like and repost." See the [worked example](examples/onboarding.md).

## Choose the job

| Skill | Use it for |
| --- | --- |
| [x-post](skills/x-post/SKILL.md) | Single posts and quote posts, hooks, content mix, packaging |
| [x-longform](skills/x-longform/SKILL.md) | Long posts, threads and X Articles |
| [x-engage](skills/x-engage/SKILL.md) | Reply list and replies on other people's posts, bigger accounts, mutuals |
| [x-reply](skills/x-reply/SKILL.md) | Triage and answers under your own posts |
| [x-presence](skills/x-presence/SKILL.md) | Display name, handle change planning, bio, header, pinned post |
| [x-spaces](skills/x-spaces/SKILL.md) | Spaces and group chats; what replaced Communities |
| [x-plan](skills/x-plan/SKILL.md) | Daily hand-posting rhythm, weekly rotation, posting slot |
| [x-audit](skills/x-audit/SKILL.md) | Weekly review, same-account outliers, 5 more versions |
| [x-repurpose](skills/x-repurpose/SKILL.md) | One idea or long source into native X formats, and X winners elsewhere |
| [x-human](skills/x-human/SKILL.md) | Voice-preserving revision, not AI-detector claims |

Algorithm claims come from X's open-sourced For You code, X staff posts, and
X's creator docs, each labeled verified, interpretation, or unverified. See
[platform evidence and limitations](shared/evidence.md).

## Audience growth is a core objective

Real topic -> clear hook -> standalone payoff -> conversation -> mutual
relationships -> measured iteration. No guaranteed growth, fake controversy,
copied posts, or engagement bait. See [growth](shared/growth.md).

## Install

```bash
git clone https://github.com/BlazingInterwebs/x-agent-skills
cd x-agent-skills
python3 -B scripts/validate.py
python3 -B scripts/install.py --destination "$HOME/.codex/skills" --dry-run
python3 -B scripts/install.py --destination "$HOME/.codex/skills"
```

The installer requires an explicit path and **refuses all existing target
paths**. Install a subset with `--skills x-post x-engage`. Never copy only
SKILL.md. See [installation details](docs/installation.md).

## Context, capabilities, and privacy

Use runtime briefs or the optional [context template](templates/context.md).
Store your filled context and exports outside this public repository. Python
helpers need Python 3.9+ with the standard library. Read the
[metric definitions](shared/metrics.md) and [safety rules](shared/privacy.md).

**V1 drafts and analyzes.** It does not post, schedule, like, follow, DM,
scrape, or change accounts.

## Examples and helpers

- [A week of drafts from a blank start](examples/onboarding.md)
- [Audit a synthetic dataset](examples/audit.md)
- [Behavioral evaluation scenarios](tests/behavioral-cases.md)

```bash
python3 -B skills/x-audit/scripts/compare.py examples/observations.csv
python3 -B skills/x-human/scripts/editorial.py examples/draft.txt
```

## Development and status

```bash
python3 -B scripts/sync_resources.py --check
python3 -B scripts/validate.py
python3 -B -m unittest discover -s tests -v
```

Shared references and the comparison helper are bundled into each skill.
After editing files under `shared/`, run `python3 -B scripts/sync_resources.py`.
See [architecture](docs/architecture.md), [contributing](CONTRIBUTING.md), and
[changelog](CHANGELOG.md). Version 0.1.0 is a pilot. [Roadmap](docs/roadmap.md).

## License and acknowledgments

[MIT](LICENSE). Structure follows the Blazing Interwebs Facebook Agent Skills
collection. Ideas credited in [Acknowledgments](ACKNOWLEDGMENTS.md). Not
affiliated with or endorsed by X Corp.
