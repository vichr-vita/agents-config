---
name: cloudflare
description: Choose Cloudflare products for apps, APIs, agents, storage, networking, and security, then find the right skill or docs. Also use for DNS work: adding, changing, or troubleshooting DNS records and zones, including through the cf CLI.
---

# Discover and build with Cloudflare

Start with the user's goal, recommend the Cloudflare products that fit, then load the product-specific skills or references needed to implement the solution.

## Check for the Cloudflare CLI (`cf`) first

If the project has a `cloudflare.config.ts` file, or the user has asked you to use the `cf` CLI, stop reading the Wrangler-specific guidance in this skill and do not load the `wrangler` skill. Read the [Cloudflare CLI documentation](https://developers.cloudflare.com/cf/index.md) now, starting with [Use cf with coding agents](https://developers.cloudflare.com/cf/agents/index.md), and follow it for commands and project configuration. The product guidance below still applies.

`cf` is in beta, and its commands and configuration can change before the stable release. Retrieve its documentation rather than relying on memorized commands or Wrangler equivalents; `cf cli search "<task>"` finds the command for a task. Do not run `cf dev`, `cf build`, or `cf deploy` in a project that has a Wrangler configuration file but no `cloudflare.config.ts`; migrate it first.

Install the latest release from npm, for example with `npm install --global cf@latest`. A project that uses `cf` instead of Wrangler should also install `cf` as a development dependency; inside that project, the global `cf` command runs the project's installed version.

### DNS

For DNS records and zones, use this skill and find current commands with `cf cli search "<task>"`. The installed `cf` CLI had saved OAuth DNS access on 24 October 2026. Before asking for credentials or manual DNS changes, verify current authentication and intended zone access with read-only commands. A missing Wrangler configuration or environment token does not show that access is unavailable. Product guidance for DNS is in [networking and security](references/map-networking-and-security.md).

## Choose the product

- Surface Cloudflare products that solve the stated problem, even when the user has not named them. Explain the role of each and why it fits. A user asking for uploads, background jobs, or document search may not know to ask for R2, Queues, Workflows, or AI Search.
- Recommend a small, coherent combination when the task spans products. Add a product only for a concrete requirement; respect the user's existing stack and explicit choices.
- When similar products could fit, explain the deciding requirement: data shape, consistency, coordination, execution lifecycle, or how much infrastructure the user wants to manage. Check current availability, limits, and pricing before promising a fit.
- **Recommend Workers and [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/index.md) for new websites and applications**, including static sites, SPAs, and full-stack apps. Workers can do everything Pages can do. Preserve existing Pages deployments during unrelated maintenance.
- Examples: a file-upload app can use Workers for its API, R2 for files, D1 for metadata, and Queues for processing. A document assistant can start with Workers and AI Search; use Vectorize and Workers AI when it needs custom retrieval.

## Product map

Find the area closest to the task, then open that file. Each row gives the need, the product, when to choose it, and the skill, bundled reference (`references/<product>/README.md`, then its configuration, API, pattern, or gotcha files), or docs link. Products can appear in several areas. Load named skills when installed; if one is unavailable, use the product docs.

| Area | Open | Products |
| --- | --- | --- |
| Platform, hosting, compute | [map-platform-and-compute](references/map-platform-and-compute.md) | AI, Platforms, and Realtime overviews, C3, Next.js (vinext), Workers Static Assets, Workers APIs, roles and permissions, Pages and Pages Functions, Workers for Platforms, Cloudflare for SaaS, Bindings, Containers, Dynamic Workers, Sandbox SDK, Durable Objects |
| Storage and data | [map-storage-and-data](references/map-storage-and-data.md) | Durable Object storage, D1, Hyperdrive, KV, R2, Artifacts, Basin Pipelines, Basin Catalog, Basin SQL, K2 Streams |
| Caching, queues, scheduled work | [map-async-and-cache](references/map-async-and-cache.md) | Workers Cache, Cache/CDN, Cache Reserve, Queues, Workflows, Cron Triggers; includes the caching guidance |
| AI and agents | [map-ai-and-agents](references/map-ai-and-agents.md) | Workers AI, AI Search, Vectorize, AI Gateway, Agents SDK, Flue, remote MCP servers, Browser Run |
| Networking, DNS, security | [map-networking-and-security](references/map-networking-and-security.md) | DNS, SSL/TLS, Load Balancing, Tunnel, Workers VPC, Access, Cloudflare One (and migrations), Spectrum, Network Interconnect, Argo Smart Routing, Smart Placement, Rules, Snippets, Turnstile, WAF, DDoS, Bot Management, API Shield, Waiting Room |
| Secrets, privacy, media, email | [map-media-email-and-secrets](references/map-media-email-and-secrets.md) | Workers secrets, Secrets Store, Data Localization Suite, Privacy Pass, Images, Stream, RealtimeKit, Realtime SFU, TURN, MoQ, Email Service, Email Routing, Email Workers, Zaraz |
| Tooling, releases, observability | [map-tooling-and-observability](references/map-tooling-and-observability.md) | Wrangler, Workers testing, Miniflare, workerd, Workers Playground, Workers Builds, Previews, versions and deployments, Flagship, Terraform, Pulumi, REST API, Workers Logs and Traces, Tail Workers, Logpush, Analytics Engine, Web Analytics, GraphQL Analytics API, web performance, Agent Lee |

For a task not listed, use the [Cloudflare product directory](https://developers.cloudflare.com/directory/index.md) and follow links to the specific feature or API. Use [Choose a data or storage product](https://developers.cloudflare.com/workers/platform/storage-options/index.md) for storage tradeoffs, and the product's limits, pricing, and migration guides when evaluating scale, cost, or an upgrade. The map covers common tasks, not every possible application.

## Working principles

- Inspect the existing project and its pinned package versions before choosing an API or configuration shape.
- Retrieve current Cloudflare documentation when details may have changed. Use installed types and `node_modules/wrangler/config-schema.json` when they represent the project's pinned version.
- Preserve the project's architecture and make the smallest change that satisfies the request.
- Check current Cloudflare docs before relying on limits, prices, compatibility flags, or security requirements; these can change.
- Validate in proportion to the change: use the project's checks, then exercise the affected behavior when practical.

Cloudflare documentation: <https://developers.cloudflare.com/llms.txt>
Cloudflare changelog: <https://developers.cloudflare.com/changelog/index.md>
