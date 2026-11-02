---
name: subagent-model-selection
description: Applies the user's model and reasoning-effort preferences to subagents. Use when planning delegation, spawning a subagent, or choosing its model or reasoning effort.
---

# Subagent model selection

Apply these preferences whenever existing instructions and the user's task call for delegation. This skill does not require delegation or expand an agent's authorized scope.

## Choose the model

- Use `gpt-6.1-sol` for ordinary subagents.
- Use `gpt-6.1-terra` for computer-use assignments.
- Use `gpt-6-astra` only after the user explicitly approves it for the proposed assignment. Ask only when there is a concrete reason to prefer Astra, and explain that reason. Approval applies to that assignment alone.

Keep these exact model choices. Do not substitute other models or automatically upgrade to a newer model. If the required model is unavailable, report the limitation without silently choosing another model.

## Choose the reasoning effort

Choose effort for each assignment without asking the user to make routine model or effort decisions.

| Assignment | Effort |
| --- | --- |
| Very routine, mechanical work | `low` |
| Routine coding | `medium` |
| Debugging or investigation | `high` |
| Difficult debugging or investigation with substantial ambiguity, or after an unsuccessful high-effort attempt | `xhigh` |

Apply the same task-based judgment to Terra and approved Astra assignments. Briefly explain the selected model and effort in the assignment or progress update. For example, "Use gpt-6.1-sol with high effort to investigate the intermittent test failure."

## Apply the selection

Pass the chosen model and reasoning effort explicitly on every new subagent spawn when the tool supports them. Do not silently inherit the director's settings.

Read the active tool schema. If explicit overrides require `fork_turns="none"`, use it and include the necessary task context, ownership, constraints, and acceptance criteria in the assignment. Do not assume another harness uses these parameter names or restrictions.

Check whether the selected role fixes its own model or effort. Choose a generic or worker role that honors the selection rather than silently accepting a conflicting role preset. If the available tool cannot enforce the required selection, report that limitation before spawning.
