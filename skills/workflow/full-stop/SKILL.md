---
name: full-stop
description: Trigger this if the user says 'full stop', even as a closing "Full stop." that reads like emphasis.
---

# Full Stop

The user is not watching this thread. Take the change from its current state to
an open PR that is ready for them to merge. Never merge it. Your updates go
unread until long after you stop.

If the user did not explicitly request "full stop" in some clear way, do not
assume this autonomy.

The request grants permission to commit, push, and resolve conflicts on this
task's branch, and to use the test methods Proof needs without asking first.
That covers ask-first rules for browser automation, simulators, running the app
or a dev server, and screenshots. It does not cover the actions under "Asking
the user", and it does not bypass a harness approval prompt.

Never merge, enable auto-merge, enter a merge queue, force-push, push to the
default branch, bypass branch protection, or delegate those actions. Disable
existing auto-merge and remove the PR from any merge queue before work begins,
and report that you did.

## Steps

1. **Finish the change.** Complete the goal with the smallest change that works.
   Fix the case that happened, not every case that could. If you are on the
   default branch, create a branch first.
2. **Prove it.** Get proof for every change you made. See "Proof".
3. **Get review.** Spawn the `adversarial-reviewer` subagent on the diff, in a
   fresh agent each round. Fix findings that are real and in scope, and decline
   the rest with a written reason. Stop after three rounds and report what is
   still open. Do not soften or omit the reviewer's verdict.
4. **File the PR** with the `file-pr` skill.
5. **Babysit the PR** with the `babysit-pr` skill. Fix real findings and CI
   failures, and get proof for each fix before you push it.
6. **Hand off** when the gate passes. See "Stop at the gate".

Stay active from step 1 to step 6. If you end your turn while checks or bots are
pending with no watcher set, the work stops, because nobody will prompt you
again.

## Proof

Proof is evidence you observed yourself in this session: command output, a
reproduction, a screenshot. Use the most direct proof the change allows:

- Reproduce the original failure, apply the fix, then watch the same
  reproduction pass.
- Run the checks that the repo's CI runs.
- Add one focused test that fails without the fix, when the behavior has none
  and the repo has a test setup.
- For UI and runtime behavior, run the app and look at the change. Green mocked
  tests do not prove that the user experience works.

## Stop at the gate

The gate passes when all of these are true on the latest commit:

- Your proof and the review cover the final diff.
- Required checks are green.
- Review bots have finished, and each finding is fixed or dismissed with a
  written reason.
- No human review still requests changes.
- The branch is up to date with its base, and GitHub reports it as mergeable.

Then fetch the base branch and check the live PR's head, base, checks, reviews,
and mergeability. Confirm it is open, not a draft, and not set to merge without
the user. If someone else merged it, report that instead.

Call `unwatch_pull_request` before the handoff or a question. Report the PR
link, final head, whether the PR is ready, waiting on human approval, or
blocked, your proof, the reviewer's verdict, each decision you made for the
user, and remaining risks. State whether the PR is still open and unmerged.

## Asking the user

A question in a normal message goes unseen. Use `AskUserQuestion` so the thread
shows it is waiting, and put all the context in the question: the PR link, what
blocks you, and the options with your recommendation first.

Ask only when you cannot continue alone:

- You cannot prove the change.
- The gate cannot pass, and you cannot fix that yourself.
- The next step needs a force-push, deletes data, touches production, changes
  things outside the repo, or closes a PR.
- A UI change needs a pick from mocks.
- The goal is ambiguous in a way that changes the result.
- Another PR makes this one obsolete.

Decide everything else yourself with sensible defaults, and list those decisions
in the report. If the tool returns no answer, leave the PR open and unmerged,
and start your final message with the question.
