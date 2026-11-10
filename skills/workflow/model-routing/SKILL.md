---
name: model-routing
description: Selects the model and reasoning effort for each sub-agent assignment. Use before every sub-agent spawn, including nested delegation and reviewers, and when reassessing an existing assignment's model or effort.
user-invocable: false
---

# Model routing

Apply this skill before every sub-agent spawn. It governs model selection when delegation is already authorized. It does not require delegation or expand the task's scope.

The goal is the cheapest model and effort that completes the assignment well. Judge cost per finished task: a cheap run that has to be redone costs more than the right model the first time. The numbers and sources behind these rules are in [`evidence.md`](evidence.md); read it when a rule seems wrong for a case or when revisiting the rules.

## Roles

The user-facing session runs on Opus. It talks to the user, routes work, and verifies what comes back. It hands Fable-shaped work (see "Fable") to a `fable` subagent rather than doing it itself.

A Fable subagent may orchestrate its own workers. Spawn it as `general-purpose`, because that type has the Agent tool and read-only types such as `Explore` and `Plan` do not. Its brief tells it to load this skill and route its workers by the table's non-Fable rows, so each effort has one Fable. It reports back to the Opus session, which checks the result before telling the user it is done.

Delegate to cheaper workers for bulk or parallel work. A single chain of dependent steps does better on one model at a lower effort than split across workers.

## Choose the model and effort

| Assignment | `model` | `effort` |
| --- | --- | --- |
| Codebase search, file inventories, running commands, log or test-output digests, classification, extraction | `haiku` | `medium` |
| Web research: searching, fetching, and summarizing pages | `sonnet` | `medium` |
| Well-specified change: localized fix with a reproduction, mechanical edit across many files, migration with tests | `sonnet` | `high` |
| Feature work in an existing codebase, research synthesis, writing for people | `opus` | `medium` |
| Code review | `opus` | `medium` |
| Bug diagnosis without a clear reproduction, UI and visual design, security-adjacent work | `opus` | `high` |
| Long-horizon build that runs for hours with little supervision | `fable` | `high` |
| Hard or ill-defined problem where the approach is still unknown | `fable` | `high` |
| Adversarial review of an architecture or a high-risk design | `fable` | `high` |
| Orchestrating cheaper workers across a large multi-part task | `fable` | `medium` |
| The same failure twice at `opus` `high` | `fable` | `high` |

Use `opus` at `medium` for anything the table does not cover.

Keep effort between `low` and `high`. In independent tests, `xhigh` and `max` cost 1.7 to 3.4 times as much as `high` per task for a few points at most, and sometimes scored lower. Use them only when the user asks.

Never use `claude-sonnet-5` on this account. `sonnet` means `claude-sonnet-5-5`.

Effort names do not mean the same amount of thinking across models. Do not treat Sonnet at higher effort as equal to Opus at lower effort.

## Model notes

### Haiku

- Use `low` for trivial lookups and high-volume labeling, `medium` by default, and `high` when strict instruction-following matters. Past `high`, its scores flatten, runs slow down, and refusals climb, so move the task to `sonnet` instead.
- Keep each Haiku request under 100K prompt tokens, where its price rises fivefold. Split large reads into chunks, or give them to `sonnet` or `opus`.
- Ask for file paths, line numbers, and verbatim snippets, so the parent can check the report cheaply.
- Haiku refusals have no fallback, and retrying usually refuses again. Reassign a refused task to `sonnet` or `opus`.
- Keep it on read-only and mechanical work. For code edits beyond trivial ones, review, planning, debugging, and web research, it makes more unsupported claims and skips checks.

### Sonnet

- Use `medium` for web research and `high` for code. At `high` it matches Opus at `low` on coding for about the same cost, and it leads independent code-migration benchmarks. At `low` it reports work as done without running checks.
- Past `high`, Opus one level lower scores better for less, so move the task to `opus` instead of raising Sonnet's effort.
- Its factual recall is weaker than Opus's. Tell it to search rather than answer from memory, and give reasoning over very long inputs to `opus`.
- State the scope. It adds tests and docs nobody asked for.
- Its cyber blocks fall back to `claude-sonnet-5`, so route security-adjacent work to `opus`.

### Opus

- `medium` covers most work. `high` is the coding sweet spot and the level for diagnosis and UI work.
- Skip `low`. It loses far more on bug hunting and research than it saves; give cheap work to `sonnet` or `haiku` instead.
- Higher effort did not improve code review in independent tests, so reviews run at `medium`.
- For diagnosis, tell it to explore broadly before acting. For UI work, name the design patterns to avoid, or it falls back to a few default styles.

### Fable

The `fable` alias currently means Fable 5.2. Route to it without asking when the assignment plays to its strengths:

- Autonomous work measured in hours: building an app or feature set from a spec, porting a large codebase, carrying a migration through to passing tests.
- Problems that need open-ended exploration before any plan exists, or that Opus has already failed twice at `high`.
- Planning a large effort, splitting it among `opus`, `sonnet`, or `haiku` workers, and verifying their results. Fable checks its own and others' work more thoroughly than other models do, and it catches design flaws Opus misses.
- Self-verified visual or spatial builds: games, 3D scenes, CAD, and interactive UIs it can render and test in a browser.

On routine coding, ordinary reviews, and bounded fixes, Fable gives about the same results as Opus at several times the cost. Opus writes better prose for people. Fable's safeguards block most cybersecurity tasks, including defensive ones, and most research biology, so route those to `opus`.

Fable uses up subscription quota several times faster than Opus, and it can use only half of the weekly limit. Each Fable assignment should be one where Opus would likely fail or take far longer. Run it at `medium` or `high`.

## Examples

| Assignment | Selection |
| --- | --- |
| Find every caller of `parseConfig` and list them with file and line | `haiku` `medium` |
| Reduce a 3,000-line CI log to the failing tests and their first error lines | `haiku` `medium` |
| Label 500 support tickets by category | `haiku` `low` |
| Check a library's current API across its docs and changelog | `sonnet` `medium` |
| Fix a failing unit test with a clear stack trace | `sonnet` `high` |
| Rename an API across 40 files and keep the build green | `sonnet` `high` |
| Add a settings page to an existing app | `opus` `medium` |
| Review a pull request | `opus` `medium` |
| Write release notes or a PR description | `opus` `medium` |
| Find why production requests time out intermittently, with no reproduction | `opus` `high` |
| Redesign a dashboard layout | `opus` `high` |
| Triage a CVE or write a proof of concept | `opus` `high` |
| Build a working prototype of the spec'd video editor, with its own tests, unattended overnight | `fable` `high` |
| Port the 600k-line Fortran solver to C++ and keep the numerical regression suite passing | `fable` `high` |
| Stress-test a proposed sync-engine architecture before anyone builds it | `fable` `high` |
| Plan a four-workstream refactor, brief `opus` and `sonnet` workers, and verify each merge | `fable` `medium` |
| Find the root cause of a flaky cross-service race after two failed `opus` `high` attempts | `fable` `high` |

## Apply the selection

Set `model` and `effort` on the `Agent` call. The call accepts only the aliases `opus`, `sonnet`, `haiku`, and `fable`, and an alias follows Anthropic's current recommended version, so a call cannot pin a full model ID. Always set `effort` when the model differs from the session's, because the session's level does not carry over to another model.

A `fork` ignores a model override and inherits the parent's model, so use a fresh agent when the selection differs. Check whether the chosen agent type fixes its own model or effort in its definition, and pick one that honors the selection.

State the selected model, effort, and brief reason in the assignment or progress update.

At `low` and `medium`, a smaller model is more likely to skip a check or stop to ask. A sub-agent has nobody to answer, so every brief states what done means, tells it to keep working until then, and tells it to run a real check and stop and report once the work is done and checked.

Fable follows cautious instructions literally. Leave stale warnings out of its briefs, such as an old "never retry" note. When it should restructure code rather than build around it, include this sentence: "This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it."

## Verify and adjust

Set acceptance criteria before delegating. Inspect saved fields, required facts, test results, or analytical checks. A sub-agent's confidence is not verification.

When checks fail, first rule out missing inputs and broken tools. Then raise effort up to `high` and add checks. If it still fails, move up one model: `haiku`, `sonnet`, `opus`, `fable`. Reassign with the failed checks and relevant findings instead of repeating the same brief.
