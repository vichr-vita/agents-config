<!-- ui-workflow:start -->
## Image-first frontend work

- Read PRODUCT.md and DESIGN.md before changing the frontend. Respect existing
  project instructions and preserve behavior outside the requested scope.
- When implementing a selected screenshot or mockup, use the ui-implement
  workflow. Treat the selected image as the visual target, not inspiration.
  Extract its design rules before coding; do not redesign it while implementing.
- Reuse existing components and tokens. Record deliberate screen-specific
  exceptions instead of silently changing the project's design system.
- For visual changes, render the affected UI, inspect actual screenshots, fix
  visible mismatches, and repeat. Compilation and DOM inspection alone do not
  establish visual fidelity.
- Save screenshots of the final code state in design/previews/<screen>/ and
  link them in the completion report. Identify inferred responsive layouts and
  unresolved differences. Never claim visual verification without inspecting
  the rendered images.
<!-- ui-workflow:end -->
