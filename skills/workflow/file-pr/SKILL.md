---
name: file-pr
description: File a concise pull request. Use when the user asks to file, open, or create a PR.
---

# File PR

Before filing, check whether a PR for this branch already exists. Review the
diff locally against the base branch to make sure its
contents match the goal.

Update the branch from the default branch before opening, because stale
branches conflict and waste a review round. Rebase only if the branch is
unpushed. Merge the default branch into a pushed branch.

PR titles usually become commit messages, so follow the repository's title
conventions, including conventional commit style in repositories that use it.
Look at recently merged PRs and Git history for examples. Prefer a simple,
human-readable title that explains why the change matters:

BAD

> ❌ perf(server): negotiate permessage-deflate on the websocket

GOOD

> ✅ perf(server): cut websocket frame size by 70%+ with gzipping

Open the description with a simple explanation of the problem based on the
user's original prompt, then briefly explain the solution. Do not lead with an
implementation inventory:

BAD

> ❌ Removed implicit workspace carry-over from every "new thread" entry point (cmd+n / cmd+shift+o, sidebar v1/v2 buttons, command palette). New threads inherit only the project from context; branch, worktree, and env mode always come from the configured defaults. Deleted buildContextualThreadOptions, startNewThreadInProjectFromContext, and the v1 sidebar's seed-context machinery.

GOOD

> ✅ My "new worktree" default was ignored when starting new threads on existing worktrees. Super unintuitive. Now your preferences always apply.

Add how you verified the change. End the description with a signature naming
the model and harness that made the change, in the format
`<model> on behalf of <first name> via <harness>`. Use the exact model
identifier from the runtime metadata, not a broad model description. Take the
first name from `user.name` in the repository's local Git config, or from the
global Git config if the local value is unset. Include subagent models that
wrote part of the change. If model identity is unavailable, name the harness
without guessing a model.

Before submission, check the title, description, quotes, and attachments for
secrets and private details.

Open a real PR rather than a draft so review bots run. If `gh pr create` fails
because the GraphQL rate limit is used up, open it through REST with
`gh api repos/<owner>/<repo>/pulls -f title=... -f head=... -f base=... -F body=@<file>`. If the user also asked
to babysit it, continue with the `babysit-pr` skill.

Do not post a follow-up PR comment unless it serves the user's request. When a
comment is needed, use the `leaving-pr-comments` skill.
