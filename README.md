# Claude Code configuration

This repository is the editable source for global Claude Code instructions, skills, and subagents. Installation uses this checkout directly and needs no network access or external skill cache.

Global instructions live in `AGENTS.md`. Skills live under `skills/` in human-readable categories. Categories organize this repository only; installed skill IDs come from each skill's directory name. Upstream skills are checked in with their reference files and licenses, so edit them here to customize them. `skills/provenance.md` records upstream URLs, snapshot commits, and local adaptations.

## Install

Use link mode on a machine where this checkout remains available:

```sh
./scripts/install.sh --link
```

Use copy mode for a self-contained installation:

```sh
./scripts/install.sh --copy
```

Both modes accept repeated `--exclude SKILL` options and `--dry-run`. Copy mode also accepts `--force` when an unmanaged destination should be backed up and replaced.

The installer writes:

- `AGENTS.md` to `~/.claude/rules/agents-config.md`, which leaves `~/.claude/CLAUDE.md` free for local imports.
- `agents/adversarial-reviewer.md` to `~/.claude/agents/`.
- Each skill to `~/.claude/skills/`.

It removes any target it previously managed that is no longer in that list. Run `./scripts/verify.sh` after installing and start a new session so Claude Code picks up the changes. Set the `AGENTS_CONFIG_*` variables documented in `scripts/install.sh` to test against temporary directories.

## Checks

`tests/test-skill-metadata.py` and `tests/test-installer.sh` run in CI on pull requests and on pushes to `master`. Run them locally with the same commands.

## Managed and local files

The repository does not manage credentials, sessions, caches, or `~/.claude/settings.json`. Keep machine-specific imports in `~/.claude/CLAUDE.md`.

Instructions are requests, not enforcement. These deny rules back the force-push and hard-reset rules in `~/.claude/settings.json`, and they hold in every permission mode:

```json
{
  "permissions": {
    "deny": [
      "Bash(git push --force*)",
      "Bash(git push -f*)",
      "Bash(git push * --force*)",
      "Bash(git push * -f*)",
      "Bash(git reset --hard*)"
    ]
  }
}
```

A denied command needs you to run it yourself.
