# Caching, queues, and scheduled work

Need-to-product rows for this area. Products can appear in several rows and a solution can combine products. Read the linked reference or docs before implementing; load named skills when installed. Local links open bundled references: start with the README, then follow configuration, API, pattern, or gotcha links as needed. If a named skill is unavailable, use the product docs through the [Cloudflare directory](https://developers.cloudflare.com/directory/index.md).

| What you need to do | Product or tool to consider | When to choose it | Skill or reference |
| --- | --- | --- | --- |
| Cache application responses | Workers Cache | Default for application caching; check the patterns and limitations before choosing alternatives | [Workers Cache](https://developers.cloudflare.com/workers/cache/index.md); see the Caching section below |
| Accelerate an existing website and control cached content | Cache/CDN | Configure caching for a proxied origin using Cache Rules, expiration settings, and purging | [Cache/CDN docs](https://developers.cloudflare.com/cache/index.md) |
| Keep origin content in a persistent cache | Cache Reserve | Reduce origin fetches with persistent CDN cache storage | [Cache Reserve](cache-reserve/README.md) |
| Process jobs asynchronously or buffer bursts of work | Queues | Decouple producers and consumers; use Workflows for durable multi-step orchestration | [Queues](queues/README.md) |
| Run a job that retries, waits, and resumes across steps | Workflows | Coordinate durable multi-step business processes | [Workflows](workflows/README.md) |
| Start a Worker on a recurring schedule | Cron Triggers | Trigger scheduled work; combine with Queues or Workflows for the work itself | [Cron Triggers](cron-triggers/README.md) |

## Caching

Prefer [Workers Cache](https://developers.cloudflare.com/workers/cache/index.md) for caching, including [advanced patterns](https://developers.cloudflare.com/workers/cache/examples/index.md) using cached inner entrypoints and programmatic invalidation. Choose [Cache API](https://developers.cloudflare.com/workers/runtime-apis/cache/index.md) or KV caching only when a concrete requirement cannot be met by Workers Cache; check its [patterns](https://developers.cloudflare.com/workers/cache/examples/index.md) and [limitations](https://developers.cloudflare.com/workers/cache/limitations/index.md) first.
