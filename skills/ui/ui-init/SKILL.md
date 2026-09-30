---
name: ui-init
description: Initialize an image-first frontend workflow in an existing project. Create or merge PRODUCT.md, DESIGN.md, reference and preview directories, and a small project-instructions block. Use when explicitly asked to initialize or set up this UI workflow, not to implement or redesign a screen.
---

# Initialize the UI workflow

Create durable design context without changing the application or imposing a
visual style. Keep setup small and safe to repeat.

## 1. Inspect the project

Identify the target project or app root from the user's request and workspace.
Read applicable project instructions, including AGENTS.md and any active
AGENTS.override.md. Inspect the README, existing product/design docs, package
scripts, UI components, styles, and assets as needed. In a monorepo, keep this
setup scoped to the requested app.

Reuse the existing stack, documentation, and conventions. Record facts from the
repository or user, not guesses. Do not reset a dirty working tree, overwrite
user work, install packages, start a server, or edit frontend code during setup.

## 2. Create or merge the design files

Use the files in `assets/` relative to this skill as starting structures:

- `assets/PRODUCT.md` -> project `PRODUCT.md`.
- `assets/DESIGN.md` -> project `DESIGN.md`.
- `assets/AGENTS.fragment.md` -> one marked block in the active project
  instructions file.

Fill the product brief and run commands from available evidence. Extract
existing design tokens, fonts, asset paths, and reusable components where they
are already defined. Mark unresolved decisions as `Not established`; do not
pick a new palette, font, spacing system, or component library during setup.

If PRODUCT.md or DESIGN.md already exists, read it and add only missing,
relevant information. Preserve accepted decisions and user-authored material.
When another document already owns a subject, link to it rather than creating
competing specifications. Resolve these template paths from this skill's
folder, not from the project's working directory.

Create these directories if absent, preserving all existing content:

```text
design/references/
design/previews/
```

Do not invent reference images or placeholder preview screenshots.

## 3. Add the frontend instructions once

Merge `assets/AGENTS.fragment.md` into the project's AGENTS.md. If an existing
AGENTS.override.md is the active instructions file at that location, use that
file instead so the block is actually read. Do not create a new override file.

The markers are `<!-- ui-workflow:start -->` and
`<!-- ui-workflow:end -->`. If the block exists, update it in place, preserving
user customizations. Never append a duplicate block or replace unrelated
instructions. Respect more-specific instructions in frontend subdirectories.

## 4. Verify and finish

Re-read the changed files. Check that paths are correct, existing instructions
remain intact, and no duplicate block was introduced. If setup is repeated
without new information, it should cause no material changes.

Report the files created or updated and any unresolved setup constraint. End
with the next action: attach a selected UI image and invoke `$ui-implement`.
Do not start design exploration or implementation during initialization.
