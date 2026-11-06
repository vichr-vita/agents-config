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

## RTK

[RTK](https://github.com/rtk-ai/rtk) condenses shell output before it reaches Claude Code. The installer does not set it up because the hook lives in `~/.claude/settings.json`, which stays local to each machine. With the `rtk` binary on `PATH`, run this once per machine:

```sh
rtk init -g --auto-patch
```

The command adds the `PreToolUse` hook to `settings.json`, keeps your existing settings, and backs up the file to `settings.json.bak`. It also writes `~/.claude/RTK.md` and imports it from `~/.claude/CLAUDE.md`. Start a new session afterward. `./scripts/verify.sh` prints a warning when the hook is missing, and `rtk verify` checks the hook and RTK's filters.

The hook leaves `git push --force` and `git reset --hard` unrewritten, so the deny rules below still match them.

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
      "Bash(git reset --hard*)",
      "Bash(git -C * push --force*)",
      "Bash(git -C * push -f*)",
      "Bash(git -C * push * --force*)",
      "Bash(git -C * push * -f*)",
      "Bash(git -C * reset --hard*)"
    ]
  }
}
```

A denied command needs you to run it yourself.
