---
name: repo-sync
description: Synchronize Git work across machines when starting, resuming, or finishing authorized work in any project with a remote. Fetch and safely integrate remote changes, then commit and push ready work branches. Read-only questions do not authorize synchronization.
---

# Repository synchronization

Keep authorized project work available on the remote so another machine can continue it. Apply this workflow at the start or resumption of work and before handing back completed work. Skip repositories without remotes. A read-only question does not authorize checkout changes, integration, commits, or pushes. For read-only questions, synchronize only when the user also requests it.

## Start or resume

Inspect the repository's instructions, working tree, branch, upstream, remotes, and worktrees. Identify the relevant remote default branch and task base instead of assuming `origin/main`. Fetch the relevant remotes before editing. If fetch fails, report that remote freshness is unverified and do not claim synchronization succeeded.

Compare the current branch with its fetched upstream. Fast-forward with `git merge --ff-only <upstream>` when safe. If it is only ahead, preserve those commits. If it diverges, inspect both histories and integrate intentionally while preserving both sides. Prefer a normal merge for published or shared work branches. Never rewrite published history or force-push to synchronize. Rebase unpublished local commits only when appropriate under project instructions. Stop for user input if the correct resolution requires a decision the task does not establish.

Preserve existing dirty and untracked work. Do not reset, clean, overwrite, or automatically stash someone else's edits. If those edits prevent safe integration, report the blocker or use an isolated worktree for the authorized task. Detached HEADs and ambiguous remotes need an intentional branch and destination before edits or pushes.

Use a task branch for new changes when starting on the default or a protected branch. For an existing task branch, also compare its relevant remote base and incorporate necessary base updates under repository policy. Do not update unrelated branches or rebase a shared branch merely to make its history linear.

## Finish and hand off

When a coherent portion of authorized work is ready, run the checks appropriate to that change. Review the diff, stage explicit relevant paths, inspect the staged diff, and commit. Leave unrelated edits, secrets, generated clutter, and unfinished work out of the commit. Do not create empty commits or commit unfinished edits merely to claim synchronization.

Fetch again before pushing. If the remote work branch advanced, integrate it safely using the rules above and rerun affected checks. Push the current work branch to its intended writable remote, setting upstream when needed, for example `git push -u origin <work-branch>`. Routine work-branch commits and pushes are part of this standing workflow and need no repeated permission request. An explicit user restriction still takes precedence.

Do not push directly to the default or protected branch, merge a remote pull request, deploy, or publish a release merely to synchronize. A rejected push is a reason to inspect fresh remote state, not to force-push. Stop and report authentication, policy, unresolved conflict, or network blockers instead of retrying blindly.

Confirm the pushed branch matches its remote ref and report its name and commit. Distinguish synchronized commits from local edits that remain uncommitted. Give the other machine a branch it can fetch and check out, and state any remaining blocker plainly.
