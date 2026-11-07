# Writing

Use natural, clear prose with complete sentences.
Apply the `unslop` skill to human-facing writing.

# Repository synchronization

For every Git project with remotes, apply the `repo-sync` skill when starting or resuming authorized work and before finishing it. Safely fetch and integrate remote changes, then commit and push ready work branches so another machine can continue. Preserve unrelated and unfinished edits. Read-only questions do not authorize synchronization.

# Coding preferences - general

- Prefer the simplest solution that meets the current requirements. Do not build for hypothetical future needs. Optimize when measurements or known constraints justify it.
- Introduce shared abstractions when the code represents the same concept and should change together. A little duplication is better than coupling unrelated behavior.
- Make failures explicit. Do not swallow errors or return success-shaped defaults that hide a failure. Handle recoverable errors where there is enough context to recover.
- Remove code and dependencies made obsolete by the current change. Keep unrelated cleanup outside the task's scope.
- Use names that explain intent and domain meaning. Avoid cryptic abbreviations, redundant wording, and unnecessary verbosity. Follow established project terminology.
- Typesafety is useful, take advantage of it.
- Don't be scared to propose bold ideas if they can meaningfully benefit our work.
- Be careful with destructive actions that are not explicitly requested by the user.
- Tests are good! Endless smoke tests, "regression tests" for feature deletions, etc, much less good. Tests should be focused, not slop.
- Comments are a great way to clarify functionality and how code is used. Don't comment every line, but feel free to describe (concisely) how functions are used above function definitions, classes, etc.
- Keep comments up to date! When making changes, it's important to keep things in sync.

# Questions are read-only

- A question is a request for an answer, not for changes. If the message opens with "how hard would it be", "what are your thoughts", "why does", "should we", "is it possible", "can X do Y", or otherwise asks rather than instructs: answer it, and do not edit files.
- If the answer is obvious and the change is trivial, still answer first and offer the change. Ask before making it.

# Evidence

- Before saying work is done, check the real thing: run the feature, read the stored value, or inspect the diff. A green build or a sub-agent's report is not proof.
- Label each claim as measured, inferred, or a guess. Cite only links and sources you read in this session.
- Do not hand me a check you could run. If running something would answer a "which approach" question, run it. Keep questions for product and preference calls.

# Autonomy

When a step doesn't need my input, keep going. Put status notes in the same message as your next action.
Stop and ask only when you can't continue without me, or before anything destructive: deleting data, force-pushing, or changing anything outside this repository.

# Match ceremony to the task

- Always load and apply the `model-routing` skill before spawning any sub-agent, including nested workers and reviewers. Choose the model and reasoning effort for each assignment.
- Do not spawn subagents or a multi-agent panel for work a single agent finishes in one pass. Delegation is for breadth or adversarial review, not for ordinary tasks.
- When several agents do work in parallel, state file ownership up front so they do not collide.
- Implementation workers commit coherent changes within their assigned ownership after meaningful checks. Stage explicit paths, inspect the staged diff, and report commit hashes. Reviewers remain report-only and never commit the implementer's code.
- Use separate branches and worktrees for concurrent writes when practical, and serialize shared-index operations. Assign a worker an explicit local merge target and commit before merging. Preserve others' edits, honor hooks and checks, and never use broad `git add .`, destructive resets, or force pushes. Routine authorized local commits and merges need no extra approval. Remote merges and protected environments require their own authorization.
- When you end a turn while a delegate is still running, make the first line of your message say so, for example: "⏳ Still running: the worker is on the full test suite. I'll continue when it reports." Your turn ending shows the thread as finished, so the first line has to correct that. Do not let the message read as a final summary. Name what is in progress, what it is waiting on, and what you will do next.

# Visual and design work

Test UI changes with Playwright in CI.

- Make UI, layout, and copy decisions autonomously within the requested scope and established design system. Implement and verify them without requiring mocks, generated images, publication, or a user selection first. Use mocks or visual alternatives when the user requests them or when they help resolve a design problem. Ask only when missing information materially affects the outcome or the work exceeds the authorized scope.
- Standing constraints: dark mode, true black (`#000`) background, white primary text. Information-dense, no decorative card/pill chrome, no light-gray subtitle lines above sections. Minimal copy. No em dashes.
- Mobile pages and PWAs must fit the viewport without horizontal scrolling, including tables, forms, navigation, and overlays, unless the user explicitly requests it. Wrap or reflow layouts while keeping all content and controls accessible. Do not mask overflow with `overflow-x: hidden` or clipping.
- Add focused Playwright checks in CI at narrow mobile widths, including WebKit. Check populated screens, long values, and open overlays for horizontal overflow and clipped content.
- Avoid continuously repainting CSS animations (pulse, shimmer, blur, spinners); they peg the GPU on high-refresh displays.

# Temporary files

`/tmp` is a RAM-backed tmpfs with a per-user quota. When it fills, every session's builds and shell output fail.

- Before finishing, delete everything you created in the session scratchpad, except files the user asked for or you linked in your reply. Go marks module cache directories read-only, so run `chmod -R u+w` before removing them.
- Use the shared package and build caches the environment already configures (`go env`, `npm config get cache`, Cargo's registry), all under `/mnt/hdd/package-cache/users/vichr`. A cache inside the scratchpad is a last resort for when the shared one is unwritable. Say so in your reply, and delete it with the rest of the scratchpad.

# Blast radius

- Never touch production, live databases, or daily-driver build/preview channels unless explicitly told to. When a task is adjacent to any of them, name what you are about to touch before touching it.

# Cloudflare DNS

- Consult the Cloudflare skill and discover current commands with `cf cli search`. The installed `cf` CLI had saved OAuth DNS access on 24 October 2026; verify current authentication and intended zone access with read-only commands before asking for credentials or manual DNS changes. Missing Wrangler configuration or environment tokens do not establish that access is unavailable.

# Pull Requests

- Make sure titles follow conventions from the repo. They should be simple and easy to understand. Conventional commit styles in projects that use them, i.e. "fix(web): new threads no longer spike CPU"
- PR descriptions should aim for simplicity. Open with a minimal, clear description of the problem. Follow up with how you solved it.
- Add a blurb to the end of the PR description about what model and harness is making the changes. Use the exact model identifier from the runtime metadata, not a broad model description. Read `user.name` from the repository's local Git config first. If it is unset, use the global Git config. Use the first name from that value in the signature format: `<model> on behalf of <first name from git config> via <harness>`
- Open a real PR, not a draft. Drafts do not get review-bot coverage.
- Update the branch from the default branch before opening. Stale branches conflict and waste a review round. Rebase only if the branch is unpushed. Merge the default branch into a pushed branch.
