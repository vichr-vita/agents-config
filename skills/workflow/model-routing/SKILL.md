---
name: model-routing
description: Selects the model and reasoning effort for each sub-agent assignment. Use before every sub-agent spawn, including nested delegation and reviewers, and when reassessing an existing assignment's model or effort.
user-invocable: false
---

# Model routing

Apply this skill before every sub-agent spawn. It governs model selection when delegation is already authorized. It does not require delegation or expand the task's scope.

## Roles

The user-facing session runs on Opus. It talks to the user, routes work, and verifies what comes back. It hands Fable-shaped work (see "When to use Fable") to a `fable` subagent rather than doing it itself.

A Fable subagent may orchestrate its own workers. Spawn it as `general-purpose`, because that type has the Agent tool and read-only types such as `Explore` and `Plan` do not. Its brief tells it to load this skill and route its workers by the table's non-Fable rows, so each effort has one Fable. It reports back to the Opus session, which checks the result before telling the user it is done.

## Choose the model and effort

| Assignment | `model` | `effort` |
| --- | --- | --- |
| Search, lookups, and summaries of logs or test output | `haiku` | `medium` |
| Mechanical edit across many files | `opus` | `low` |
| Localized fix with a clear reproduction and focused checks | `sonnet` | `medium` |
| Feature work with clear scope | `opus` | `medium` |
| Bug in existing code, migration, or review | `opus` | `high` |
| The same failure twice at `high` | `opus` | `xhigh` |
| Long-horizon build that runs for hours with little supervision | `fable` | `high` |
| Hard or ill-defined problem where the approach is still unknown | `fable` | `high` |
| Orchestrating cheaper workers across a large multi-part task | `fable` | `medium` |
| The same failure twice at `xhigh` | `fable` | `high` |

Use `opus` at `medium` for anything the table does not cover. Do not use `max` unless the user asks for it.

Never use `claude-sonnet-5` on this account. `sonnet` means `claude-sonnet-5-5`.

Effort names do not mean the same amount of thinking across models. Do not treat Sonnet at higher effort as equal to Opus at lower effort.

## When to use Fable

The `fable` alias currently means Fable 5.2. Route to it without asking when the assignment plays to its strengths:

- Autonomous work measured in hours: building an app or feature set from a spec, porting a large codebase, carrying a migration through to passing tests.
- Problems that need open-ended exploration before any plan exists, or that Opus has already failed twice at `xhigh`.
- Planning a large effort, splitting it among `opus`, `sonnet`, or `haiku` workers, and verifying their results. Fable checks its own and others' work more thoroughly than other models do.
- Self-verified visual or spatial builds: games, 3D scenes, CAD, and interactive UIs it can render and test in a browser.

Keep the rest on the table's other rows. On routine coding, reviews, and bounded fixes, Fable gives about the same results as Opus. Opus also writes better prose for people, such as docs, PR descriptions, and release notes. Fable's safeguards block most cybersecurity tasks, including defensive ones, and most research biology, so route those to `opus`.

Fable uses up subscription quota several times faster than Opus, and it can use only half of the weekly limit. Each Fable assignment should be one where Opus would likely fail or take far longer.

Run `fable` at `medium` or `high`. Independent tests found `high` scored at least as well as `xhigh` and `max`, which cost two to three times as much per task.

Examples:

| Assignment | Selection |
| --- | --- |
| Build a working prototype of the spec'd video editor, with its own tests, unattended overnight | `fable` `high` |
| Port the 600k-line Fortran solver to C++ and keep the numerical regression suite passing | `fable` `high` |
| Find the root cause of a flaky cross-service race after two failed `opus` `xhigh` attempts | `fable` `high` |
| Plan a four-workstream refactor, brief `opus` and `sonnet` workers, and verify each merge | `fable` `medium` |
| Build a browser 3D scene and check it renders and plays correctly | `fable` `high` |
| Fix a failing unit test with a clear stack trace | `sonnet` `medium` |
| Review a pull request | `opus` `high` |
| Write release notes or a PR description | `opus` `medium` |
| Triage a CVE or write a proof of concept | `opus` `high` |

## Apply the selection

Set `model` and `effort` on the `Agent` call. The call accepts only the aliases `opus`, `sonnet`, `haiku`, and `fable`, and an alias follows Anthropic's current recommended version, so a call cannot pin a full model ID. Always set `effort` when the model differs from the session's, because the session's level does not carry over to another model.

A `fork` ignores a model override and inherits the parent's model, so use a fresh agent when the selection differs. Check whether the chosen agent type fixes its own model or effort in its definition, and pick one that honors the selection.

State the selected model, effort, and brief reason in the assignment or progress update.

At `low` and `medium`, a smaller model is more likely to skip a check or stop to ask. A sub-agent has nobody to answer, so every brief states what done means, tells it to keep working until then, and tells it to stop and report once the work is done and checked.

Fable follows cautious instructions literally. Leave stale warnings out of its briefs, such as an old "never retry" note. When it should restructure code rather than build around it, include this sentence: "This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it."

## Verify and adjust

Set acceptance criteria before delegating. Inspect saved fields, required facts, test results, or analytical checks. A sub-agent's confidence is not verification.

When checks fail, first rule out missing inputs and broken tools. Then raise effort and add checks, and move to a bigger model only if that does not work. Reassign with the failed checks and relevant findings instead of repeating the same brief.
