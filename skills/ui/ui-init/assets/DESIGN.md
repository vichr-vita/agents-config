# Design

## Visual sources

Selected references live in `design/references/`. Implemented screenshots live
in `design/previews/`. Never replace a source image with an implementation
screenshot or alter it to make the implementation appear correct.

Applicable project instructions still govern the work. Within those rules,
follow the user's current visual brief and selected reference for the specified
screen. Preserve existing design decisions elsewhere. Record any deliberate
screen-specific exception to this document.

## Existing design system

Not established. Record existing components, token files, fonts, icons, and
assets with their repository paths before introducing alternatives.

## Tokens and component treatment

Record known typography, colors, spacing, radii, borders, shadows, and component
states from the existing system or selected reference. Distinguish observed
values from estimates. Do not introduce generic cards, gradients, or decoration
that the reference does not contain.

## Layout and responsive behavior

Record content widths, grid, density, alignment, breakpoints, and overflow
behavior. Use supplied desktop/mobile references where available. Mark a
responsive layout inferred from a single image as inferred, not reference-matched.

## Screen specifications

For each selected screen, record its route, source image path, source dimensions,
comparison viewport in CSS pixels, device scale if known, crop/scroll position,
important visual rules, asset/font substitutions, and unresolved assumptions.
Do not assume that a tall full-page reference describes a tall viewport.

## Visual verification

Use the project's existing browser tool or Playwright setup. Compare actual
rendered screenshots against the selected image at matching viewport, scale,
and state. Inspect the images, fix visible differences, and capture again.

After the final code change, save the target-view, desktop, and mobile PNGs in
`design/previews/<screen>/`, with a `review.md` that embeds them and records the
result. Default extra viewports are 1440 x 900 and 390 x 844 CSS pixels unless the
project or user specifies otherwise. These are testing defaults, not design rules.
