---
name: html-communication
description: When the user asks for an HTML writeup of work (NOT as part of the codebase), use this skill to create and always upload it to Planpost. Also useful for reading plans.vichr.me and postplan.dev URLs.
metadata:
  platform: [darwin, linux]
  scope: fleet
  requires: "curl 7.87 or newer, and the Planpost upload token"
---

# HTML communication

## When to use

Use this skill for any request to produce a readable HTML artifact for a human, whether it is called a plan, a spec, a write-up, findings, a summary, a report, a comparison, or a set of UI mocks. The word "plan" is often absent. What the requests share is a document to read outside the terminal, and a link to open it.

Also use it whenever a user supplies a `plans.vichr.me` or `postplan.dev` URL to read.

Do **not** use it for HTML that is part of the product being built (app templates, components, marketing pages). This skill is for documents about work, not shipped UI.

## Read a hosted URL

Planpost is Vít's own host at `plans.vichr.me`. Older documents live on the third-party `postplan.dev`. Both serve the uploaded HTML at the URL plus `/raw`.

When a user supplies a URL on either host, fetch the HTML immediately with the shell. Do not use web search or a browser to retrieve it.

1. Remove a trailing slash, then append `/raw` unless the URL already ends in `/raw`.
2. Run `curl --fail --silent --show-error --location --max-time 30 --output /tmp/planpost.html '<raw-url>'`.
3. Read `/tmp/planpost.html` as the user's artifact and continue the requested task.

A web-search refusal is not evidence that the host rejected the request. If `curl` fails, report its actual status or network error; do not substitute search results.

## Document

Create one self-contained HTML file, capped at 512 KB.

- Write it like a spec, not a landing page: dense, scannable, no hero, decorative chrome, marketing voice, or em dashes.
- Default to true black (`#000`), white primary text, and dark gray only for secondary surfaces or accents.
- Make it mobile-readable with a responsive viewport and no fixed-width layout.
- Use semantic HTML, inline CSS, inline SVG, and HTTPS or data-URL images.
- Use an inline classic script only when interactivity materially helps. Keep scripted pages useful without JavaScript; the sandbox blocks storage, fetch, workers, frames, forms, and popups.
- In script-free files, give external links `target="_blank"` and `rel="noopener noreferrer"`. If any script exists, omit `target="_blank"`.

Never include external or module scripts, inline event handlers, `javascript:` URLs, forms, frames, embeds, objects, applets, meta refresh, linked stylesheets, secrets, private URLs, or local filesystem paths.

## UI mocks

When the user asks for variants:

- Render real styled variants, not descriptions.
- Label them `A`, `B`, `C`... for easy selection.
- Lay them out for direct comparison.
- Keep one file across iterations so its Planpost URL stays stable.

## Publish

Vít has given standing permission to upload every artifact created or updated with this skill. Upload is required, including in Auto mode. Do not ask for separate permission or stop at the local file.

1. Write the HTML file locally.
2. Run `planpost-upload <file path>`. The script is in this skill's directory.
3. Report the local path and the URL the script prints.

Planpost ties a URL to the machine name and the file's absolute path, so uploading the same path again updates the same URL. Use `planpost-upload --new <file path>` only when a new draft is wanted.

Anyone with the URL can read the document. The server stores the file as uploaded and does not validate markup. Its Content-Security-Policy makes the browser block external scripts, network requests, forms, and frames, so a page that relies on them uploads fine and then renders broken.

If the script reports a missing token, ask the user to copy `~/.config/planpost/token` from a machine that has it. Do not fall back to `npx postplan` or any other host. For other failures, report the HTTP status and message the script printed.

Never open a browser or claim the document is hosted before upload succeeds. Do not verify in a browser unless the user asks.
