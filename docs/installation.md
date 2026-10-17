# Installation, compatibility and updates

Python 3.9+ is required for helpers and tooling; no pip packages or API keys.

```bash
python3 -B scripts/validate.py
python3 -B scripts/install.py --destination "$HOME/.codex/skills" --dry-run
python3 -B scripts/install.py --destination "$HOME/.codex/skills"
```

Use the path your host actually discovers (for example `~/.agents/skills`).
Install a subset with `--skills x-post x-human`. Any existing target path
causes refusal. Files are hash-verified after copying. The installer never
deletes skills, rewrites host config, or stores brand data. Manual
installation means copying complete `skills/x-*` folders.

## Invocation and context

Use your host's skill syntax, e.g. `$x-post` in Codex. Fill the
[optional context](../templates/context.md) outside the public project, or
supply details in the task.

## Updates and uninstall

Pin a version or commit. The installer has no overwrite, update, or delete
mode. Back up user-edited files and get authorization before replacing them.
