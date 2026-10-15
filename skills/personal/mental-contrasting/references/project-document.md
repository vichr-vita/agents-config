# The coaching document

Use the Vikunja project description as the living document for one wish. Write in the user's language. Preserve their first-person wording in the WOOP answers, while distinguishing agent suggestions and unresolved choices. Do not fill missing answers with invented commitments.

Use the following outline as needed. Keep small wishes short. Omit empty sections, and label a decision pending when it prevents execution.

## Wish

Record the wish, its horizon, and how the user will recognize achievement. If the project covers a near-term part of a larger wish, retain that connection.

## Outcome

Capture the user's imagined moment of success and why it matters to them. This is the material they should want to reread when the work feels difficult.

## Obstacle

Name the main inner obstacle, its recognizable cue, and the situation in which it tends to appear. Record external constraints separately when they affect the plan.

## Plan

Write the chosen if-then response in a single sentence. Add supporting responses only when they solve a specific additional problem. Keep an immediate physical action where that helps turn a vague intention into something executable.

## Actions and habits

State the first action, the near-term milestones, and the agreed time budget. Link to the created tasks by returned ID or verified URL. Use each task description for the detail, rather than maintaining two independent task lists.

For a one-time task, include what to do, what counts as done, and any dependency. Add a due date only when agreed or grounded in a real deadline.

For a habit, include:

- The cue and normal action.
- The minimum version for difficult days and its completion condition.
- The relevant if-then response.
- The first due date, local time, timezone, and human-readable recurrence.
- Whether the next occurrence follows the schedule or the date of completion.
- How to resume after a missed attempt, without inventing completed work.

The task's actual recurrence fields must match these instructions. A description saying "every day" is insufficient.

## Review

Record when the user will review the wish and what evidence to bring. A short review can ask whether the wish still matters, what happened when the obstacle appeared, whether the response helped, and what to change next.

Append dated notes on return visits. Preserve earlier decisions that explain a change. A repeating review task can prompt the user to return to the coach; it does not schedule an autonomous agent check-in.

## Publication state

Keep a compact record of the project ID and task IDs. For incomplete publication, identify what exists, what was verified, and what remains pending or failed. Remove resolved error details once the project is complete. Never record credentials.

Serialize the document as semantic HTML and save it through `vikunja-cli` as described in [the Vikunja guide](vikunja.md). Escape user text and keep links and headings readable. Do not publish raw Markdown into a field that expects HTML.

When updating an existing project, fetch its current description and merge the relevant sections. Preserve unrelated text and reviews. Re-read just before saving if the document may have changed during a long coaching session.
