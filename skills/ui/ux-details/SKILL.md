---
name: ux-details
description: Check an app against 20 practical UX details and implement the applicable ones that are missing.
disable-model-invocation: true
---

# UX details

Check the app against every detail below. Build each applicable detail that is missing. Skip details that do not fit the project or require backend work unavailable from the current environment.

Invoke with `/ux-details`, optionally naming the app or part of the app to check.

## Workflow

1. Read the project instructions and inspect the app, platform, existing components, dependencies, and check commands. Follow any required design review or mock approval steps before implementation.
2. Assess all 20 details against actual code and behavior. Use the project's existing tools before adding a library, and match its code style. Treat named products and libraries as examples, not dependencies to install automatically. Check current documentation when API availability or platform support affects a decision.
3. Build one detail at a time. Every animation must respect reduced motion. Keep keyboard access, focus handling, and accessible controls working.
4. Run the project's checks after each implemented detail. Exercise the changed behavior, including failure, undo, and reduced-motion paths where relevant. Resolve failures caused by that change before moving on. Report any checks that cannot run or already fail.
5. Finish with all 20 items in their original order, using the report format below. Do not claim a client-only approximation completes a feature that requires server support.

## The 20 details

1. **Skeleton loaders.** Show gray blocks in the shape of the real layout while content loads. Derive them from the same component as the loaded state so nothing jumps. Only show them if loading takes longer than about 300 ms.

2. **Optimistic updates.** Small actions such as likes, checkboxes, and renames update the screen immediately and roll back with an error if the request fails. Use `useOptimistic` where appropriate in React 19 or later. Never use optimistic success for payments.

3. **Command menu.** In apps people use every day, Cmd+K or Ctrl+K opens a searchable menu of every available page and action. It must work with the keyboard alone.

4. **Shortcut hints.** Show each action's keyboard shortcut in menus, tooltips, and the command menu. Use ⌘ on Mac and Ctrl elsewhere. Shortcuts must not fire while someone is typing in an input, textarea, or editable content.

5. **Undo toasts.** For reversible actions such as delete or archive, replace the confirm dialog with immediate action and an Undo toast for 5 to 10 seconds. Use a soft delete or delayed request so Undo really restores the action. The toast has `role="status"` and a keyboard-accessible Undo control. Keep confirmation for irreversible actions.

6. **Stale-while-revalidate.** Show cached data immediately and refetch in the background, including when the window regains focus or the network returns. Do not use stale data for balances, stock counts, or anything where old data can cost money.

7. **Prerendering.** Check what the router already prefetches first. Where useful and supported, use speculation rules with eagerness `"moderate"` for same-site links. Exclude logout and any link that changes data.

8. **BlurHash placeholders.** Store a BlurHash or ThumbHash with each uploaded image and show its blur at the image's exact dimensions while the real image loads. Skip if the required upload or metadata support cannot be implemented from here.

9. **View transitions.** Use `document.startViewTransition` for changes within a page and `@view-transition { navigation: auto; }` for supported navigation between pages. Give shared elements the same `view-transition-name` across states, keeping names unique within each state. Keep transitions under 300 ms, respect reduced motion, and retain normal navigation where unsupported.

10. **Swipe-to-dismiss sheets.** Bottom sheets follow the finger and close after enough travel or a quick flick. Use the platform or project's existing sheet support, such as SwiftUI's `presentationDetents`, React Native's `@gorhom/bottom-sheet`, or Vaul on the web. Keep a close button too.

11. **Interruptible animations.** Use springs that reverse from their current position and velocity when interrupted. Do not use CSS keyframes for interactions the user can interrupt, and never block input while something animates.

12. **Predictive back.** For Android apps, use `OnBackPressedCallback` or `PredictiveBackHandler` so a back swipe can preview the previous screen. Check the target SDK and current platform defaults, including Android 16 behavior, before changing back handling.

13. **Hit slop.** Every tap target is at least 44 by 44 points on iOS and 48 by 48 dp on Android, even if the icon is smaller. Use `hitSlop` or padding without overlapping neighboring targets. Apply equivalent usable target sizes to touch web interfaces.

14. **Safe-area insets.** On the web, use `viewport-fit=cover` and `env(safe-area-inset-*)` where needed. In React Native, use `react-native-safe-area-context` or the project's equivalent. Keep tappable controls clear of the notch, Dynamic Island, and home indicator.

15. **One-time-code autofill.** Use one input with `autocomplete="one-time-code"` and `inputmode="numeric"` on the web, or `textContentType` set to `.oneTimeCode` on iOS. Where SMS delivery is in scope, make the message end with a domain-bound line such as `@yourdomain.com #123456`. Report unavailable SMS work as skipped rather than implying the input implements it.

16. **Tabular numbers.** Use `font-variant-numeric: tabular-nums` on timers, prices, counters, and numeric table columns, or the native platform equivalent.

17. **Balanced headlines.** Use `text-wrap: balance` on headings and short titles, and `text-wrap: pretty` on paragraphs where appropriate.

18. **Continuous corners.** Use the `.continuous` corner style in SwiftUI or the equivalent in UIKit. On the web, add `corner-shape: squircle` alongside the existing `border-radius` as progressive enhancement. Keep the radius fallback and check support in the project's target browsers.

19. **Idempotency keys.** Create a UUID when the user starts a payment or record-creation action. Send that same `Idempotency-Key` on every retry of the same action; create a new key for a new action. Implement deduplication in the app's own API too when that backend is available. Disable the submit button while the request runs. A header alone does not provide idempotency unless the server honors it; skip unsupported backend work and report the limitation.

20. **Safe triangle.** Hover menus with submenus must not switch while the cursor travels diagonally toward the open submenu. Use the menu library's existing support or Floating UI's `safePolygon` when already appropriate to the project. Preserve keyboard and touch access.

## Final report

List all 20 by number and name. Mark each as exactly one of:

- **Built:** Explain what changed, link the files, and say how to see it working. State any partial scope or skipped backend portion explicitly.
- **Already done:** Point to the implementation and where the behavior is available.
- **Skipped:** Give the project-specific reason, such as platform mismatch, no relevant flow, or unavailable backend support.

Include the check results and any validation limits. Keep the report concrete and concise.
