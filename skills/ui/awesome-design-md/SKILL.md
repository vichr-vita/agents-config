---
name: awesome-design-md
description: Use curated DESIGN.md files from popular websites to give AI coding agents instant design system context for building pixel-perfect UI.
when_to_use: Use when adding a DESIGN.md to a project, matching a popular website's style such as Stripe, Vercel, or Linear, or giving an agent design context.
---

# Awesome Design MD

## Local references

The bundled `design-md/<site>/DESIGN.md` files are available relative to this skill directory. Read the chosen reference before generating a design. Follow the user's instructions and `AGENTS.md` when they differ from a reference. Use these local files before downloading another copy.

A curated collection of `DESIGN.md` files reverse-engineered from 74 popular developer-focused websites. Drop one into your project root and any AI coding agent instantly understands your target visual style — colors, typography, components, spacing, and more — without Figma exports or JSON schemas.

---

## What DESIGN.md Does

`DESIGN.md` is a plain-text design system document (introduced by [Google Stitch](https://stitch.withgoogle.com/docs/design-md/overview/)) that AI agents read to generate consistent UI. It is the design equivalent of `AGENTS.md`:

| File | Who reads it | What it defines |
|------|-------------|-----------------|
| `AGENTS.md` | Coding agents | How to build the project |
| `DESIGN.md` | Design agents | How the project should look and feel |

Markdown is the format LLMs read best — no parsing, no tooling, no configuration required.

---

## Available Design Systems (74 total)

### AI & Machine Learning
| Site | Style |
|------|-------|
| `claude` | Warm terracotta accent, clean editorial |
| `elevenlabs` | Dark cinematic, audio-waveform aesthetic |
| `mistral.ai` | French minimalism, purple-toned |
| `ollama` | Terminal-first, monochrome simplicity |
| `replicate` | Clean white canvas, code-forward |
| `runwayml` | Cinematic dark, media-rich layout |
| `voltagent` | Void-black canvas, emerald accent |
| `x.ai` | Stark monochrome, futuristic minimalism |

### Developer Tools
| Site | Style |
|------|-------|
| `cursor` | Sleek dark, gradient accents |
| `linear.app` | Ultra-minimal, precise, purple accent |
| `mintlify` | Clean, green-accented, reading-optimized |
| `posthog` | Playful dark UI, developer-friendly |
| `raycast` | Sleek dark chrome, vibrant gradients |
| `resend` | Minimal dark, monospace accents |
| `supabase` | Dark emerald theme, code-first |
| `vercel` | Black and white precision, Geist font |

### Enterprise & Consumer
| Site | Style |
|------|-------|
| `apple` | Premium white space, SF Pro, cinematic |
| `airbnb` | Warm coral, photography-driven, rounded |
| `spotify` | Vibrant green on dark, bold type |
| `stripe` | Signature purple gradients, weight-300 |
| `notion` | Warm minimalism, serif headings |
| `figma` | Vibrant multi-color, playful professional |

> This table is a sample. List `design-md/` for all 74 sites.

---

## What's Inside Each DESIGN.md

Every file follows the [Stitch DESIGN.md format](https://stitch.withgoogle.com/docs/design-md/format/) with extended sections:

| # | Section | What it captures |
|---|---------|-----------------|
| 1 | Visual Theme & Atmosphere | Mood, density, design philosophy |
| 2 | Color Palette & Roles | Semantic name + hex + functional role |
| 3 | Typography Rules | Font families, full hierarchy table |
| 4 | Component Stylings | Buttons, cards, inputs, nav with states |
| 5 | Layout Principles | Spacing scale, grid, whitespace |
| 6 | Depth & Elevation | Shadow system, surface hierarchy |
| 7 | Do's and Don'ts | Design guardrails, anti-patterns |
| 8 | Responsive Behavior | Breakpoints, touch targets |
| 9 | Agent Prompt Guide | Quick color reference, ready prompts |

## Choosing the Right DESIGN.md

| Your goal | Recommended site |
|-----------|-----------------|
| Clean developer tool / SaaS | `vercel`, `linear.app`, `resend` |
| Dark developer dashboard | `supabase`, `posthog`, `cursor` |
| Premium / luxury product | `apple`, `stripe`, `bmw` |
| Playful / friendly product | `figma`, `lovable`, `zapier` |
| AI / ML product | `voltagent`, `replicate`, `mistral.ai` |
| E-commerce / marketplace | `airbnb`, `pinterest` |
| Fintech / crypto | `stripe`, `revolut`, `coinbase` |
| Documentation site | `mintlify`, `hashicorp` |
| Media / content | `spotify`, `runwayml` |
| Enterprise SaaS | `ibm`, `hashicorp`, `sentry` |
