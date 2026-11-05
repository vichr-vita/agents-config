---
name: design-taste-frontend
description: Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check.
---

# tasteskill: Anti-Slop Frontend Skill

> Scope: landing pages, portfolios, and redesigns. Not dashboards, not data tables, not multi-step product UI. Information-dense app UI follows the project's own constraints.
> Every rule below is **contextual**. None of it fires automatically. First read the brief, then pull only what fits.
> The project's or user's stated constraints win over this skill's palette defaults. When the user's global rules apply, the dark background is true black `#000` with white primary text.
> Motion runs once or on interaction. Skeletons stay static. Do not use continuously repainting effects such as pulse, shimmer, blur, or spinners.

## Brief Inference (Read the Room Before Anything Else)

Before touching code or tweaking dials, **infer what the user actually wants**. Most LLM design output is bad because the model jumps to a default aesthetic instead of reading the room.

### Read these signals first
1. **Page kind** - landing (SaaS / consumer / agency / event), portfolio (dev / designer / creative studio), redesign (preserve vs overhaul), editorial / blog.
2. **Vibe words** the user used - "minimalist", "calm", "Linear-style", "Awwwards", "brutalist", "premium consumer", "Apple-y", "playful", "serious B2B", "editorial", "agency-y", "glassy", "dark tech".
3. **Reference signals** - URLs they linked, screenshots they pasted, products they named, brands they're competing with.
4. **Audience** - B2B procurement panel vs. design-conscious consumer vs. recruiter scanning a portfolio. The audience picks the aesthetic, not your taste.
5. **Brand assets that already exist** - logo, color, type, photography. For redesigns, these are starting material, not optional input (see the [redesign protocol](references/redesign-protocol.md)).
6. **Quiet constraints** - accessibility-first audiences, public-sector, regulated industries, trust-first commerce, kids' products. These constraints override aesthetic preference.

### Output a one-line "Design Read" before generating
Before any code, state in one line: **"Reading this as: \<page kind> for \<audience>, with a \<vibe> language, leaning toward \<design system or aesthetic family>."**

Example reads:
- *"Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward Tailwind utilities + Geist + restrained motion."*
- *"Reading this as: solo designer portfolio for hiring managers, with an editorial / kinetic-type language, leaning toward native CSS + scroll-driven animation + custom typography."*
- *"Reading this as: redesign of a public-sector service site, with a trust-first language, leaning toward GOV.UK Frontend or USWDS."*

### If the brief is ambiguous, ask one question, do not guess
Ask exactly **one** clarifying question - never a multi-question dump - and only when the design read genuinely diverges. Example: *"Should this feel closer to Linear-clean or Awwwards-experimental?"*

If you can confidently infer from context, **do not ask**. Just declare the design read and proceed.

### Anti-Default Discipline
Do not default to: AI-purple gradients, centered hero over dark mesh, three equal feature cards, generic glassmorphism on everything, infinite-loop micro-animations everywhere, Inter + slate-900. These are the LLM defaults. Reach past them deliberately based on the design read.

### Pick the direction

1. **Dials:** set `DESIGN_VARIANCE`, `MOTION_INTENSITY`, and `VISUAL_DENSITY` from the design read. Baseline `8 / 6 / 4`. See [dials.md](references/dials.md).
2. **Foundation:** use the official package when the brief reads as a real design system, otherwise build the aesthetic honestly. See [design-systems.md](references/design-systems.md).
3. **Mode:** for redesigns, detect Preserve or Overhaul and audit first. See [redesign-protocol.md](references/redesign-protocol.md).

## AI Tells (Forbidden Patterns)

Avoid these signatures unless the brief explicitly asks for them. Examples and override conditions are in [ai-tells-detail.md](references/ai-tells-detail.md).

* **Visual & CSS:** neon or outer glows, oversaturated accents, gradient text on large headers, custom mouse cursors.
* **Typography:** Inter as default, oversized H1s that just scream, serif as the default for creative briefs, `Fraunces` or `Instrument_Serif` as defaults.
* **Color:** AI-purple gradients, the beige + brass + oxblood + espresso palette as the premium-consumer default.
* **Layout & Spacing:** 3-column equal feature cards, centered hero over dark mesh, floating elements with awkward gaps, eyebrows above every section.
* **Content & Data:** generic names (John Doe, Sarah Chan), generic avatars, fake-perfect numbers (`99.99%`), startup-slop brand names (Acme, Nexus, SmartFlow), filler verbs (Elevate, Seamless, Unleash).
* **External Resources & Components:** hand-rolled SVG icons, hand-rolled decorative SVGs, div-based fake screenshots, broken Unsplash links, shadcn/ui in default state.
* **Hero & top-of-page:** version labels (`V0.6`, `BETA`), "Brand · No. 01" sub-eyebrows.
* **Section numbering & micro-labels:** section-number eyebrows (`001 · Capabilities`), `01 / 4` pagination, `Scroll · 001 Capabilities` cues, "Index of Work, 2018 - 2026" range labels.
* **Separators & dots:** a middle-dot in every metadata string, decorative colored status dots.
* **Typography flourishes:** `<br>`-broken-and-italicized headlines, vertical rotated text, crosshair or hairline grid lines as decoration.
* **Fake product previews:** div-based fake product UI in the hero, fake version footers.
* **Marketing-copy Tells:** "Quietly in use at", "From the field" poetic labels, mock-humble references, weather or locale strips, micro-meta-sentences under eyebrows, generic step labels (Stage 1, Step 1).
* **Pills, labels and version stamps:** pills overlaid on images, photo-credit captions as decoration, version footers on marketing pages, "Reservation 412 of 800" counters.
* **Decoration text strips:** `BRAND. MOTION. SPATIAL.` strips at hero bottom, floating top-right sub-text in section headings.
* **Lists, dividers and scoring:** `border-t` + `border-b` on every row, scoring bars with filled background tracks.
* **Locale, time, scroll cues:** locale or city strips, scroll cues.
* **Em-Dash Ban:** no `—` anywhere visible, and no `–` as a separator. Use a regular hyphen, a period, a comma, or a colon.

## Final Pre-Flight Check

Check these before outputting code.

- [ ] **Brief inference** declared (the one-line Design Read)?
- [ ] **Dial values** explicit and reasoned from the brief, not silently using baseline?
- [ ] **Design system** chosen from the design-system map if applicable, or aesthetic labeled honestly?
- [ ] **Redesign mode** detected and audit performed (if applicable)?
- [ ] **No em-dashes (`—`) anywhere on the page.** Headlines, eyebrows, pills, body, quotes, attribution, captions, buttons, alt text.
- [ ] **Page Theme Lock**: One theme (light, dark, or auto) for the whole page. No section flips to inverted mode mid-page?
- [ ] **Color Consistency Lock**: one accent color used identically across all sections?
- [ ] **Shape Consistency Lock**: one corner-radius system applied consistently?
- [ ] **Button Contrast Check**: every CTA text is readable against its background (no white-on-white, WCAG AA 4.5:1)?
- [ ] **CTA Button Wrap**: no CTA label wraps to 2+ lines at desktop?
- [ ] **Form Contrast Check**: form inputs, placeholders, focus rings, labels all pass WCAG AA against the section background?
- [ ] **Serif discipline**: if a serif is used, it is not Fraunces or Instrument_Serif (or it is, with explicit brand justification)? Different serif from your previous project?
- [ ] **Premium-consumer palette check**: if the brief is premium-consumer (cookware / wellness / artisan / luxury), the palette is not the AI-default beige+brass+oxblood+espresso family? Different family from your previous premium-consumer project?
- [ ] **Italic descender clearance**: every italic word with `y g j p q` has `leading-[1.1]` min + `pb-1` reserve?
- [ ] **Hero fits the viewport**: headline ≤ 2 lines, subtext ≤ 20 words and ≤ 4 lines, CTA visible without scroll, font scale planned around image?
- [ ] **Hero top padding**: max `pt-24` at desktop, hero content does not float halfway down the viewport?
- [ ] **Hero stack discipline**: max 4 text elements in hero (eyebrow or brand strip, headline, subtext, CTAs)? No tiny tagline below CTAs, no trust micro-strip in hero?
- [ ] **Eyebrow count (mechanical)**: count instances of `uppercase tracking` micro-labels above section headlines across all components. Count ≤ ceil(sectionCount / 3)? Hero counts as 1.
- [ ] **Split-Header Ban**: no "left big headline + right small explainer paragraph" pattern as a section header (vertical stack instead)?
- [ ] **Zigzag Alternation Cap**: no 3+ consecutive sections with the same image+text-split layout?
- [ ] **No Duplicate CTA Intent**: no two CTAs with the same intent ("Get in touch" + "Let's talk" both on page = Fail)?
- [ ] **Logo wall = logo only**: no industry / category labels printed below logos?
- [ ] **Bento Background Diversity**: at least 2-3 bento cells have real visual variation (image, gradient, pattern), not all white-on-white text cards?
- [ ] **"Used by / Trusted by" logo wall** lives under the hero, not inside it, uses real SVG logos (Simple Icons / devicon) or generated SVG marks, not plain text wordmarks?
- [ ] **Copy Self-Audit**: no grammatically-broken or AI-hallucinated phrases ("free on its past" type) shipped?
- [ ] **Motion motivated**: every animation can be justified in one sentence (hierarchy / storytelling / feedback / state transition), no GSAP-for-show?
- [ ] **Marquee max-one-per-page**: no two horizontal marquees on the same page?
- [ ] **Navigation on one line** at desktop, height ≤ 80px?
- [ ] **Section-Layout-Repetition** check: no two sections share the same layout family (at least 4 different families across 8 sections)?
- [ ] **Bento has rhythm and exact cell count** (N items → N cells, no empty cells in middle or at end)?
- [ ] **Long lists use the right UI component** (not default `<ul>` with `divide-y` for > 5 items)?
- [ ] **Real images used** (gen-tool first, then Picsum-seed, then explicit placeholder slots) - No div-based fake screenshots, no hand-rolled decorative SVGs, no pure-text minimalism?
- [ ] **No pills/labels overlaid on images** (no `Plate · Brand`, no `Field notes - journal`)?
- [ ] **No photo-credit captions as decoration** (`Field study no. 12 · Ines Caetano`)?
- [ ] **No version footers** (`v1.4.2`, `Build 0048`) on marketing pages?
- [ ] **No micro-meta-sentences** under eyebrows ("Each of these is a feature we ship today...")?
- [ ] **No decoration text strip at hero bottom** (`BRAND. MOTION. SPATIAL.`)?
- [ ] **No floating top-right sub-text** in section headings?
- [ ] **No scoring/progress bars with filled background tracks** as comparison visuals?
- [ ] **No locale / city-name / time / weather strips** unless brief is genuinely globally-distributed or place-focused?
- [ ] **No scroll cues** (`Scroll`, `↓ scroll`, `Scroll to explore`)?
- [ ] **No version labels in hero** (V0.6, BETA, INVITE-Only) unless the brief is a launch?
- [ ] **No section-numbering eyebrows** (`00 / INDEX`, `001 · Capabilities`, `06 · how it works`)?
- [ ] **No decorative dots** (zero by default, only for real semantic state)?
- [ ] **No `border-t` + `border-b` on every row** of long lists / spec tables?
- [ ] **Content density** sane: no 20-row data tables, no fake-precise specs without justification, ≤ 25-word sub-paragraphs by default?
- [ ] **Quotes ≤ 3 lines** of body, attribution clean (no em-dash)?
- [ ] **Motion claimed = motion shown**: if `MOTION_INTENSITY > 4`, page actually animates, not just claimed?
- [ ] **GSAP sticky-stack / horizontal-pan** implemented per the canonical skeletons (`start: "top top"`, `pin: true`, correct scrub)?
- [ ] **No `window.addEventListener('scroll')`** - using Motion `useScroll()` / ScrollTrigger / IntersectionObserver / CSS scroll-driven animations only?
- [ ] **Reduced motion** wrapped for everything `MOTION_INTENSITY > 3`?
- [ ] **Dark mode** tokens defined and tested in both modes?
- [ ] **Mobile collapse** explicit (`w-full`, `px-4`, `max-w-7xl mx-auto`) for high-variance layouts?
- [ ] **Viewport stability**: `min-h-[100dvh]`, never `h-screen`?
- [ ] **`useEffect` animations** have strict cleanup functions?
- [ ] **Empty / loading / error** states provided?
- [ ] **Cards omitted** in favor of spacing where possible?
- [ ] **Icons** from an allowed library only (Phosphor / HugeIcons / Radix / Tabler), no hand-rolled SVG paths?
- [ ] **Motion** isolated in client-leaf components with `'use client'` at the top, memoized?
- [ ] **No AI Tells** from the list above (Inter as default, AI-purple, three-equal cards, Jane Doe, Acme, "Quietly in use at")?
- [ ] **Core Web Vitals** plausibly hit (LCP < 2.5s, INP < 200ms, CLS < 0.1)?
- [ ] **One design system** per project (no Material + shadcn mixed)?

## Reference Files

* [dials.md](references/dials.md): when setting dial values or reading what a level means.
* [design-systems.md](references/design-systems.md): when picking a foundation, installing a system, or the brief is out of scope.
* [liquid-glass-web-approximation.md](references/liquid-glass-web-approximation.md): when the brief asks for Liquid Glass on the web.
* [engineering-conventions.md](references/engineering-conventions.md): when starting code: stack, state, icons, responsiveness, performance, accessibility.
* [typography-color-and-theme.md](references/typography-color-and-theme.md): when choosing type, palette, or light and dark tokens.
* [layout-and-states.md](references/layout-and-states.md): when composing heroes, navigation, grids, buttons, forms, and UI states.
* [images-and-content.md](references/images-and-content.md): when sourcing images and logos, or writing copy and testimonials.
* [motion-patterns.md](references/motion-patterns.md): when adding motion, including the GSAP and Motion skeletons.
* [ai-tells-detail.md](references/ai-tells-detail.md): when a tell needs its examples or override conditions.
* [pattern-vocabulary-and-blocks.md](references/pattern-vocabulary-and-blocks.md): when naming a pattern or adding a block.
* [redesign-protocol.md](references/redesign-protocol.md): when the task changes an existing site.
