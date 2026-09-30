---
name: ui-implement
description: Implement or refine a selected UI screenshot, mockup, or saved reference in the current project. Extract design rules, render the real app, inspect screenshots, and iterate on visual differences. Save final PNG previews for review without running the app. Use for explicit image-based implementation or fidelity fixes, not open-ended design ideation.
---

# Implement a UI image

Implement the selected image faithfully using the existing project. The job is
implementation, not visual reinvention. Browser capture and image inspection
are required parts of the work, not optional finishing steps.

## 1. Establish the target

Read applicable project instructions, PRODUCT.md, and DESIGN.md. If setup is
missing, apply `../ui-init/SKILL.md` once, preserving existing files.

Open and inspect the actual image supplied or identified by the user. A single
image supplied for implementation is already the selected target; do not ask
for approval again. If no accessible target exists, ask for the image or its
file path rather than inventing one. With multiple screens or states, map each
image to its intended route/state.

Preserve the original image in `design/references/<screen>.<original-extension>`
when file access permits. Do not overwrite an older reference unless the user
selected this image as its replacement. If the attachment cannot be saved,
record that limitation without claiming a persistent file exists.

Determine the app route, viewport, scale, and crop shown in the image. Account
for browser chrome, device-pixel scaling, and full-page or component captures.
Use supplied viewport metadata first. If it is absent, make the smallest
reasonable assumption and record it. Do not equate a full-page image's height
with the browser viewport height or stretch an image to conceal a mismatch.

Confirm a browser tool can render the app, save screenshots, and expose them
for image inspection. Prefer existing tools or Playwright. Follow repository
permissions for any setup. If capture or image inspection remains unavailable,
report the blocker; do not claim this workflow is visually verified.

## 2. Extract the design before coding

Update the relevant screen section in DESIGN.md with the reference path,
comparison viewport, layout/proportions, typography, spacing, colors, component
treatment, assets, and visible states. Reuse existing tokens where they match.
Record unknown fonts, unavailable assets, and inferred behavior as assumptions.
Do not label guessed measurements as exact or override unrelated screen rules.

Keep this specification brief. Do not add another design document or ask the
user to choose a new visual direction.

## 3. Implement the screen

Use the existing framework, components, and styling approach. Preserve working
behavior and limit edits to the requested scope. Implement real semantic UI,
not a screenshot used as the page background or a single image with fake controls.

Match the reference's content, hierarchy, spacing, and visual density. Do not
add cards, gradients, rounded containers, badges, or decorative elements absent
from the target. Preserve appropriate keyboard and focus behavior.

Use real project assets where available. Document unavoidable substitutions.
Use safe, deterministic fixtures only where necessary for previewing missing
services; isolate them from production and disclose them. Do not present mock
data as a working backend or hide errors to obtain a clean screenshot.

## 4. Render, inspect, and correct

Start the app using the project's documented command, or reuse a healthy
existing instance. Use the requested route and state, not a convenient landing
page. Keep captured data non-sensitive. Only stop server processes you started.

For each supplied reference, repeat this loop:

1. Render at the reference's comparison viewport, scale, scroll position, and
   UI state. Wait for fonts, images, and required content. Stabilize animations
   and changing fixture data for the capture, not by removing product behavior.
2. Save an actual browser screenshot under
   `design/previews/<screen>/iterations/<run-id>/pass-XX.png`.
3. Open the saved screenshot with an image-viewing tool and compare it with the
   original image. Inspect the whole composition and important details. Saving
   a file without viewing it does not count. DOM snapshots, code inspection,
   and passing tests do not replace this comparison.
4. Identify the largest actionable differences with concrete locations and
   observations. Fix geometry and layout first, then typography and text wraps,
   spacing, colors, assets, and smaller details. Do not invent similarity scores.
5. Capture and inspect again after the fixes. Recheck other affected viewports
   when changing shared styles. Never use a screenshot from before the last
   visual edit as evidence of the final result.

Finish the loop only when no material, actionable discrepancy remains in the
reference's layout, proportions, typography, spacing, colors, assets, and visible
state. Minor rasterization differences are not a reason for endless CSS changes.
Do not stop merely because the app builds or the first screenshot looks plausible.

Use up to eight correction rounds by default, unless the user gives a different
budget. If that limit or a real blocker prevents a match, preserve the work and
report `needs-review` or `blocked`, with the remaining differences. Reaching the
limit is never evidence of success. Do not weaken the target or alter the source
image to pass the review.

Also inspect desktop and mobile layouts. Use project-defined sizes, otherwise
1440 x 900 and 390 x 844 CSS pixels. Where no corresponding reference exists,
check responsive usability and explicitly label the layout as inferred. Do not
claim a mobile reference match from a desktop image alone.

Run available relevant checks and exercise the screen's primary controls.
Record functional failures separately from visual discrepancies.

## 5. Save the review output

After the last code change, capture and open the final images. Save:

```text
design/previews/<screen>/
  target.png       # actual implemented UI at the reference viewport/crop
  desktop.png      # actual desktop render
  mobile.png       # actual mobile render
  full-page.png    # include when useful for content beyond the viewport
  review.md
```

If the target and desktop/mobile view are identical, their files may share the
same captured bytes. With several supplied states, save a clearly named target
PNG for each state. Full-page captures supplement matched viewport captures;
they do not replace them. Never substitute generated mockups for app screenshots.

Write a short review.md with relative Markdown image embeds so the user can
preview it locally. Include the source image when accessible, the final PNGs,
route/state, capture time, CSS viewport and device scale, reference-matched vs
inferred views, test results, and any remaining differences or substitutions.
Record the capture command or browser procedure needed to reproduce the result.
Use `matched`, `needs-review`, or `blocked` as the visual status; keep test status
separate. A fresh blocked run must not present stale screenshots as new output.

In the final response, link the actual saved PNG files and review.md using the
host's supported file-link format. State what was implemented and any remaining
issue. Do not require the user to open localhost or run the application to review
its appearance. Verify every linked file exists, and never claim an unavailable
screenshot was saved.
