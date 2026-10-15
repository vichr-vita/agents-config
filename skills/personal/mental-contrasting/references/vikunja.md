# Vikunja execution

## Check CLI access

Use the user's [vikunja-cli](https://github.com/vichr-vita/vikunja-cli), whose executable is `vikunja-cli`, for all Vikunja project and task operations. The CLI is required. Check the installed command help before using it. If it is unavailable or unconfigured, retain the draft and report the missing setup instead of using a connector or direct HTTP requests.

The CLI requires a reachable API v2 instance and a credential file at `~/.config/vikunja/config.json`, or the file selected by `VIKUNJA_CONFIG`. It contains `url` and `token`; on Unix it must be a regular file with mode `0600` or stricter. Check existence and permissions without printing credentials. Do not put tokens in commands, chat, documents, or the skill. Missing access is a setup issue to report, not a reason to invent a project or switch services. See the [CLI README](https://raw.githubusercontent.com/vichr-vita/vikunja-cli/main/README.md).

Identify the intended instance and account before writing. Name the destination in the progress update. A request to create this coaching skill is not itself a request to create a live goal project. For a real wish, use the authorization rules in `SKILL.md`.

## Command reference

The following shapes come from the [CLI command implementation](https://raw.githubusercontent.com/vichr-vita/vikunja-cli/main/internal/cli/commands.go). Prefix shell commands with `rtk` where the user's environment requires it. `JSON` means a serialized object passed as one argument.

```text
vikunja-cli user get
vikunja-cli project list --page 1 --per-page 100
vikunja-cli project get PROJECT_ID
vikunja-cli project create --data JSON
vikunja-cli project update PROJECT_ID --data JSON
vikunja-cli task list --project PROJECT_ID --page 1 --per-page 100
vikunja-cli task get TASK_ID
vikunja-cli task create PROJECT_ID --data JSON
vikunja-cli task update TASK_ID --data JSON
```

Follow pagination until the result is exhausted when finding existing work or reconciling an uncertain write. Prefer recorded IDs over title matches. If several projects could represent the same wish, resolve the ambiguity before writing.

Project creation uses `POST /api/v2/projects`; task creation uses `POST /api/v2/projects/{id}/tasks`. Their payloads include `title` and `description`. Both typed update commands use JSON merge patch. Send only fields intentionally changed. Check the deployed instance's `/api/v2/openapi.json` for compatibility; public demo documentation may describe a newer version. See the [API v2 guide](https://vikunja.io/docs/api-v2/) and [official API reference](https://try.vikunja.io/api/v2/docs).

The CLI accepts `--data`, not a payload file or stdin. Build JSON with a serializer and call it with an argument array, such as Python's `subprocess.run`. Never interpolate the user's prose into a shell command. For example, form an argument list from `['rtk', 'vikunja-cli', 'project', 'create', '--data', json.dumps(payload)]` when RTK is required. Run that list without a shell and inspect the exit status and response.

## Save descriptions as documents

Descriptions default to HTML. Use simple headings, paragraphs, and lists. Escape user text with an HTML encoder before inserting it into markup. Preserve existing content when updating a project. JSON escaping and HTML escaping solve different problems; use both at the appropriate stage.

API v2 supports Markdown exchange, but a Markdown PATCH requires `X-Vikunja-Format: markdown`. The current CLI has no custom header option, so use semantic HTML through it. Recheck installed capabilities if that changes. See the [format documentation](https://try.vikunja.io/api/v2/docs).

## Configure actual repeating tasks

Use a first `due_date` in RFC3339 with an explicit offset. Record the user's IANA timezone in the document and task description. Set recurrence fields in the task payload as well as explaining them in prose.

| Agreed behavior | `repeat_after` | `repeat_mode` |
| --- | --- | --- |
| Daily, advancing from the scheduled date | `86400` | `0` |
| Weekly, advancing from the scheduled date | `604800` | `0` |
| Seven days after completion | `604800` | `2` |
| Monthly | Ignored by this mode | `1` |

`repeat_after` is in seconds. Mode `0` advances the previous dates until they are in the future. Mode `2` measures from completion. Both need a positive interval. Mode `1` advances by a month and uses date normalization, so do not promise end-of-month clamping. These behaviors come from the [official task implementation](https://raw.githubusercontent.com/go-vikunja/vikunja/main/pkg/models/tasks.go).

For Monday, Wednesday, and Friday, use three weekly repeating tasks starting on the agreed dates. Do not encode this as a daily task or an invented RRULE field. Explain the split when proposing the schedule.

Fixed intervals may shift the local clock time across daylight-saving changes. If the user needs an exact local time through such changes, resolve that requirement against the deployed server's capabilities before publishing the affected habit. Do not promise a schedule the recurrence fields cannot express.

Completion reschedules and reopens the same task. It does not create a new task per occurrence. Do not mark a habit done to test it, infer a full adherence history from its current state, or retry a completion request whose outcome is unknown.

## Publish and verify

1. Find or create the project for the agreed wish. Before creation, generate a stable plan identifier such as `mc-<uuid>`. Put it in a small publication-state section of the description so an interrupted request can be reconciled.
2. Save the coaching document. Record the returned project ID immediately. Give each planned action or habit a stable identifier under that plan and include it in its description.
3. Create the agreed one-time tasks, recurring habits, and review task when applicable. Record each returned task ID before proceeding. Do not add speculative tasks to fill out a project.
4. Read back the project and each task. Compare the title, description, project ID, due date as an instant, and recurrence fields with the agreed specification. Compare human-readable content if the server normalizes HTML. Verify the first due date's local meaning as well as its offset.
5. Merge task IDs and verified links into the project document. Read it back once more. Record any failed or pending items alongside the successful ones, and report the partial result accurately.

Create requests are not assumed idempotent. If a call times out, first search all relevant pages for its stable identifier. Reuse a matching result. Retry only after reconciling the outcome; if it remains ambiguous, stop the affected write and retain the draft and known IDs. Do not delete successful work to make a partial run look clean. The [CLI client](https://raw.githubusercontent.com/vichr-vita/vikunja-cli/main/internal/cli/client.go) makes a single request with a timeout.

When a creation response is uncertain, preserve the plan identifier in the chat's recovery note even if saving the publication state also failed. On a return visit, use the project/task IDs or that marker to resume. If CLI access is unavailable, return the document and exact task specifications in chat with publication marked pending.

Use returned URLs, existing verified app routes, or links confirmed in the frontend. Do not guess a frontend base URL from an API hostname. A verified ID is enough to identify work when no reliable link is available.
