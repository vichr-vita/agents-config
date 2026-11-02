---
name: model-routing
description: Selects the model and reasoning effort for each sub-agent assignment. Use before every sub-agent spawn, including nested delegation and reviewers, and when reassessing an existing assignment's model or effort.
---

# Model routing

Apply this skill before every sub-agent spawn, including spawns by other sub-agents. It governs model selection when delegation is already authorized; it does not require delegation or expand the task's scope.

## Choose the model

Use `gpt-6.1-sol` by default. Use `gpt-6.1-terra` for assignments with clear inputs, a bounded outcome, and a practical way to verify completion.

| Assignment | Starting model |
| --- | --- |
| Computer use with a defined outcome, such as entering supplied invoice fields | `gpt-6.1-terra` |
| Localized code fix with a clear reproduction and focused checks | `gpt-6.1-terra` |
| Writing or revising from supplied facts for a defined audience | `gpt-6.1-terra` |
| Recurring analytics answering known questions | `gpt-6.1-terra` |
| Features or refactors across unfamiliar files or connected subsystems | `gpt-6.1-sol` |
| Ambiguous debugging, conflicting evidence, or hidden-pattern discovery | `gpt-6.1-sol` |
| Other assignments, or tasks where missed dependencies would cause costly rework | `gpt-6.1-sol` |

Use `gpt-6-astra` only after the user explicitly approves it for the proposed assignment. Ask only when there is a concrete reason to prefer Astra, and explain that reason. Approval applies to that assignment alone.

Keep these exact model choices unless the user overrides them. Do not substitute another model or automatically upgrade to a newer one. If the required model is unavailable, report the limitation without silently choosing another model.

## Choose the reasoning effort

Choose effort for each assignment without asking the user to make routine model or effort decisions.

| Assignment | Effort |
| --- | --- |
| Very routine, mechanical work | `low` |
| Routine coding or other clearly specified work | `medium` |
| Debugging or investigation | `high` |
| Difficult debugging or investigation with substantial ambiguity, or after an unsuccessful high-effort attempt | `xhigh` |

Apply the same task-based judgment to Terra and approved Astra assignments. Model and effort are separate choices. Do not assume Terra at higher effort equals Sol at lower effort. Prefer evaluating Sol at medium before escalating Terra to max for complex work; use higher Terra effort when representative task results justify it.

## Apply the selection

Pass the chosen model and reasoning effort explicitly on every new sub-agent spawn when the tool supports them. Do not silently inherit the parent agent's settings.

Read the active tool schema. If explicit overrides require `fork_turns="none"`, use it and supply the necessary task context, file ownership, constraints, and acceptance criteria. Do not assume another harness uses these parameter names or restrictions.

Check whether the selected role fixes its own model or effort. Choose a generic or worker role that honors the selection rather than silently accepting a conflicting preset. If the tool cannot enforce the required selection, report the limitation before spawning.

State the selected model, effort, and brief reason in the assignment or progress update. For example, "Use gpt-6.1-terra with medium effort for this localized fix; verify it with the supplied reproduction."

Tell each sub-agent to apply Model Routing before spawning its own sub-agents. Preserve the existing delegation limits and approval boundaries in its brief.

## Verify and adjust

Set acceptance criteria before delegating. Inspect saved fields, required facts, test results, or analytical checks. A sub-agent's confidence is not verification.

Escalate Terra to Sol when checks reveal missed dependencies, repeated scope errors, or unresolved analytical gaps. First distinguish model failures from missing inputs or broken tools. Reassign with the failed checks and relevant findings instead of repeating the same brief. Astra still requires assignment-specific approval.

Keep a Sol workflow that already works while trying Terra on a defined task class. Compare representative inputs with the same acceptance criteria and effort, then vary effort separately. Do not launch duplicate assignments solely to benchmark models unless that comparison is part of the task.

Judge cost per accepted task, including failed attempts, tool spend, and review or repair time. Measure elapsed time to verified completion, not just token speed or time to first token. Benchmark scores and token prices do not establish equivalent results or savings for a particular assignment.

## Sources

This replaces `subagent-model-selection` and preserves its model IDs, Astra approval boundary, effort levels, and explicit spawn settings. The routing additions adapt the [EvoLink Terra versus Sol article](https://evolink.ai/blog/gpt-6-1-terra-vs-gpt-6-1-sol), published October 28, 2026, and [OpenAI's model-selection guidance](https://developers.openai.com/api/docs/guides/model-selection), checked November 2, 2026. Benchmark numbers and prices are deliberately omitted because they change.
