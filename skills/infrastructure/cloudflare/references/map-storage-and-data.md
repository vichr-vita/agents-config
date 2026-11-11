# Storage and data

Need-to-product rows for this area. Products can appear in several rows and a solution can combine products. Read the linked reference or docs before implementing; load named skills when installed. Local links open bundled references: start with the README, then follow configuration, API, pattern, or gotcha links as needed. If a named skill is unavailable, use the product docs through the [Cloudflare directory](https://developers.cloudflare.com/directory/index.md).

| What you need to do | Product or tool to consider | When to choose it | Skill or reference |
| --- | --- | --- | --- |
| Store and recover state inside a Durable Object | Durable Object storage | Choose storage APIs, transactions, and recovery for coordinated per-entity data | [DO storage](do-storage/README.md) |
| Store application records and query them with SQL | D1 | Use a managed relational database; use Durable Objects when per-entity coordination is central | [D1](d1/README.md) |
| Connect to an existing PostgreSQL or MySQL database | Hyperdrive | Keep the existing database and optimize connections from Workers | [Hyperdrive](hyperdrive/README.md) |
| Distribute configuration or other key-value data | KV | Read-heavy key-value access fits the workload's consistency requirements | [KV](kv/README.md) |
| Store uploads, downloads, or large objects | R2 | Store files by object key; pair with D1 when searchable metadata needs SQL | [R2](r2/README.md) |
| Store versioned file trees, agent checkpoints, or repositories | Artifacts | Files need versioning and Git-compatible access; currently closed beta, so confirm access before implementation | [Artifacts](artifacts/README.md) |
| Ingest event streams into R2 | Basin Pipelines | Transform and deliver streaming records into R2 | `basin` skill; [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/index.md) |
| Manage Iceberg tables in R2 | Basin Catalog | Organize tables for analytics and compatible query engines | `basin` skill; [Basin Catalog](https://developers.cloudflare.com/basin-catalog/index.md) |
| Query Iceberg tables with SQL | Basin SQL | Analyze tables in Basin Catalog | `basin` skill; [Basin SQL](https://developers.cloudflare.com/basin-sql/index.md) |
| Keep a durable event log with independent readers | K2 Streams | Produce records from Workers or HTTP, then consume with subscriptions | `k2` skill; [K2 docs](https://developers.cloudflare.com/k2/index.md) |
