# Unified agent configuration

This repository is the editable source for configuration shared by Codex and OpenCode.

Shared instructions live in `AGENTS.md`. All skills and their supporting files live under `skills/` in human-readable categories. Installation uses this checkout directly and requires no network access or external skill cache. The installer exposes global skills through the flat `~/.agents/skills` directory and writes only the adapter files each harness understands.

Skills are global unless their `SKILL.md` front matter contains a `harnesses` include-list. Harness names are case-insensitive. A restricted skill stays in the regular categorized `skills/` tree and declares its targets like this:

```yaml
---
name: example
description: An example Codex-only skill.
harnesses: [codex]
---
```

Use `[codex]` or `[opencode]` for a restricted skill. `[codex, opencode]` has the same meaning as omitting `harnesses`. The installer puts global skills in `~/.agents/skills`, Codex-only skills in `~/.codex/skills`, and OpenCode-only skills in `~/.config/opencode/skills`.

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

Run `./scripts/verify.sh` after installation. Set the `AGENTS_CONFIG_*` home variables documented in `scripts/install.sh` to test against temporary directories or install on another machine.

## Managed and local files

The repository manages global instructions, shared skills, the adversarial reviewer, the OpenCode computer-use and Nibomo agents, and OpenCode's model and MCP configuration. It does not manage credentials, sessions, caches, databases, Codex UI settings, trusted hashes, or the rest of `~/.codex/config.toml`.

### Nibomo

`Nibomo` is a primary agent with full tool permissions and access to the private Pi's Nibomo MCP. Other installed agents deny `nibomo_*` tools. Agents that override all permissions with `"*": "allow"` must also end their permission rules with `nibomo_*: deny` unless they are `Nibomo`.

Keep the administrator-issued MCP key in `~/.config/opencode/nibomo-mcp-key`, with file permissions `0600`. OpenCode reads this unmanaged credential file when it loads the configuration. The Pi must run Nibomo with local MCP enabled. Connect through Tailscale, then select `Nibomo` in OpenCode or run `opencode --agent Nibomo`. Restart OpenCode after installation.

Upstream skills are checked into this repository with their reference files and available licenses. Edit them here to customize them. `skills/provenance.md` records upstream URLs, snapshot commits, and local adaptations; the installer does not read it.

Taste Skill, Web Design Guidelines, Awesome Design MD, and Image-to-Code are saved under `skills/ui/` and installed for both harnesses. Awesome Design MD includes the reference library. Their upstream commits and local adaptations are recorded in `skills/provenance.md`.

## Legacy cleanup

`./scripts/cleanup-legacy.sh --dry-run` lists the retired Caveman and Babysitter paths. The cleanup script runs the replacement-layout gate itself, then creates a timestamped archive before removing anything. Run `./scripts/verify.sh` afterward for the final acceptance check.
