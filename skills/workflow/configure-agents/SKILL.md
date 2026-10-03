---
name: configure-agents
description: Create, import, or update shared agent skills, instructions, and harness configuration in /home/vichr/projects/agents-config, sync with master, and deploy locally. Use only when the user explicitly invokes configure-agents.
metadata:
  opencode/autoinvoke: false
---

# Configure agents

Run only when the user explicitly invokes this skill. Do not select it automatically because a task mentions learning a skill or changing configuration. An invocation with a requested change authorizes that change, its Git synchronization, and its deployment to the local harnesses. An invocation without a requested change needs clarification before editing.

## Work in the source repository

The source of truth is `/home/vichr/projects/agents-config`, regardless of the project where the user invoked this skill. Use explicit working directories or `git -C` for commands. Read that repository's `AGENTS.md`, `README.md`, and installer before changing anything. Leave the invoking project untouched unless the user separately requests changes there.

Inspect the source repository's status, remotes, branches, and worktrees, then fetch `origin/master`. Use `master` for this workflow even though the general PR instructions mention `main`. Preserve unrelated changes and never stage them into this task's commit.

Check `/home/vichr/.local/state/agents-config/install-state.json` for the installed mode and exclusions. Link installations expose edits to linked source files immediately. Draft changes in a separate worktree of this repository when editing linked files or when the usual checkout has conflicting work. Keep that worktree until its changes have reached `master` and deployment succeeds.

## Make the requested change

- Create or edit skills under `skills/<category>/<skill-name>/`. Include the reference files, scripts, assets, and licenses needed by imported skills. Record upstream sources and local adaptations in `skills/provenance.md` when applicable.
- Omit `harnesses` for shared skills. Use `harnesses: [codex]` or `harnesses: [opencode]` only for an intentional restriction. Follow the available skill-authoring guidance for new or revised skills.
- Edit shared instructions in `AGENTS.md`, harness adapters under `harnesses/`, and installation logic under `scripts/` as appropriate. Inspect the installer to determine whether other files are actually managed before editing them.
- Change managed source files here rather than editing installed files under `~/.agents`, `~/.codex`, or `~/.config/opencode`. Credentials, sessions, caches, databases, and other unmanaged machine settings stay outside the repository. If the request requires an unmanaged setting, explain that boundary before expanding the repository's deployment scope.

Run `rtk bash tests/test-installer.sh` from the working checkout. It tests copy and link installation and verification in temporary homes without changing the live installation. Validate any new or changed executable behavior with focused checks. Review the diff for unintended files and secrets.

## Sync with master

Commit only the requested files, using the repository's commit conventions. Fetch `origin/master` again, rebase the task branch onto it, and repeat relevant checks if integration changes the result.

By default, publish the verified commit with a normal fast-forward push to `origin/master`. Never force-push. If branch protection requires a PR, open a real PR targeting `master` and follow the repository's PR instructions. Wait for required checks and reviews before merging. If remote synchronization fails or a PR cannot yet merge, report the blocker and leave deployment pending.

Fetch the remote after publication. Confirm that the task commit is reachable from `origin/master`, then fast-forward the usual `/home/vichr/projects/agents-config` checkout to that revision. Preserve any unrelated local edits. If those edits prevent integration, keep the completed work in its worktree and report the conflicting paths rather than resetting or stashing the user's work.

## Deploy to this machine

Deploy from the usual source checkout after the task's changes reach both local `master` and `origin/master`. Do not install links to a temporary worktree. Inspect remaining local changes and the installer plan so unrelated edits do not become new deployment changes without authorization.

Retain the mode and exclusions from the installation state. Use `--link` when no installation state exists. Pass each saved exclusion as `--exclude <skill-name>`, and resolve an exclusion that no longer exists before running the installer.

First run `rtk ./scripts/install.sh <mode-and-exclusions> --dry-run`. Name the actual destination paths that will change, then run the same command without `--dry-run`. This invocation authorizes the requested local deployment. Do not add `--force` to overwrite unmanaged destinations without explicit authorization.

Run `rtk ./scripts/verify.sh` after installation and confirm that changed skills and configuration resolve to the expected source or contain the expected copied bytes. Do not claim deployment succeeded if installation or verification failed. Keep enough context to resume a failed deployment without repeating successful remote publication.

Report the change, the synchronized commit or PR, the installed harnesses, verification results, and any pending action. Mention a restart only when the changed configuration requires it.
