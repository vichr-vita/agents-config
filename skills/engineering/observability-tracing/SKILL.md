---
name: observability-tracing
description: Use when adding or reviewing distributed tracing in Go backend services, especially OpenTelemetry spans, trace context propagation, sampling, span boundaries, or cross-service latency and failure debugging
---

# Observability Tracing

## Overview

Tracing records path of request through system. Use it to understand where time went, which boundaries were crossed, and where failures happened across services.

Core principle: trace meaningful operations with stable context, not every tiny step.

## When to Use

Use this skill when working on any of these in Go backends:

- distributed request tracing
- OpenTelemetry instrumentation
- inbound or outbound trace context propagation
- cross-service latency or failure debugging
- sampling strategy
- deciding span boundaries, names, attributes, or events
- correlating active trace or span IDs into logs

Do not use this skill for general logging structure, log level policy, error logging placement, redaction-only questions, metrics design, or profiling. Use `observability-logging` for those.

Quick chooser:

- Need log lines, log fields, log levels, redaction, metrics, or profiling -> `observability-logging`
- Need spans, trace IDs, propagation, sampling, or cross-service path analysis -> `observability-tracing`

## Trace Model

- Trace = full request journey
- Span = timed unit of work inside trace
- Attributes = searchable key/value metadata on span
- Events = notable timestamped moments inside span

Use attributes for stable facts. Use events for important moments. Avoid turning trace into verbose log stream.

## OTel Defaults for Go Services

- Prefer OpenTelemetry as default tracing model.
- Prefer W3C Trace Context for inbound and outbound HTTP propagation.
- Instrument service boundaries first: inbound HTTP, outbound HTTP, DB, queue, RPC.
- Keep resource attributes stable: service name, version, environment, instance data when useful.
- Include build metadata like git SHA and build time where supported.
- Export traces in way compatible with rest of stack. Do not invent custom tracing model when OTel already fits.
- Use semantic conventions where they exist instead of inventing ad hoc attribute names.

## Propagation

Propagation matters across process boundaries.

- Extract trace context from inbound request headers.
- Start or continue server span from extracted context.
- Inject context into outbound HTTP, RPC, and queue messages where supported.
- Preserve correlation across background work when work still belongs to same user-visible flow.
- Pass `context.Context` explicitly through goroutines and helpers.

If you also use request IDs, keep them aligned with tracing but do not treat them as substitute for trace context.

One common Go shape:

```go
tp := sdktrace.NewTracerProvider(...)
otel.SetTracerProvider(tp)
otel.SetTextMapPropagator(propagation.TraceContext{})

handler := otelhttp.NewHandler(mux, "http.server")

client := &http.Client{
	Transport: otelhttp.NewTransport(http.DefaultTransport),
}
```

This handles inbound extraction and outbound injection for standard HTTP paths.

## Correlating Logs and Traces

Logs and traces should reinforce each other.

- add trace ID and span ID to logs when active span exists
- use same request boundary for request log and root server span
- log rich event summaries, then use trace to inspect timing and path

Do not duplicate every span event as log line.

## Sampling and Cardinality Discipline

- Sample high-volume traffic when needed. Do not let cost explode silently.
- Keep important errors and unusual paths observable even if success traffic is sampled.
- Parent-based sampling is good default for distributed systems.
- Keep span names stable and low cardinality.
- Keep attributes low cardinality too. Avoid raw payloads, user-generated blobs, random IDs as searchable attrs unless truly necessary.

Bad span names:

- `GET /users/123/orders/456`
- `sql query select * from ...`

Better span names:

- `GET /users/{id}/orders/{id}`
- `orders.lookup`

## What to Trace vs Skip

Trace interesting things:

- inbound requests
- outbound calls
- database round-trips
- queue publish and consume
- expensive internal operations
- retries worth understanding

Usually skip:

- tiny helpers
- every loop iteration
- every validation branch
- events already obvious from parent span and logs

If span does not help answer latency, failure, or dependency questions, skip it.

## Errors, Retries, and Async Work

- Record errors on spans when operation fails.
- Mark span status consistently.
- For retries, show attempt behavior only when it helps explain meaningful latency or failure.
- For async or background work, decide whether work belongs to original trace or separate trace. Be explicit. Use links when causal relationship matters more than strict parent-child nesting.
- Do not break propagation accidentally when spawning goroutines or handing work to another process.

Tracing should explain why user-visible operation was slow or failed, not bury signal in retry spam.

## Privacy and Payload Rules

- Do not put secrets in span attributes or events.
- Avoid full request or response bodies.
- Avoid high-cardinality user content unless strong reason exists.
- Prefer stable identifiers and coarse classifications over raw payload data.
- Apply same redaction discipline to traces as logs.

## Quick Reference

| Topic         | Default                                   |
| ------------- | ----------------------------------------- |
| Tracing model | OpenTelemetry                             |
| First spans   | inbound HTTP, outbound calls, DB, queues  |
| Propagation   | extract inbound, inject outbound          |
| Correlation   | add trace and span IDs to logs            |
| Span naming   | stable, low cardinality                   |
| Attributes    | searchable stable facts only              |
| Events        | important moments, not log replacement    |
| Sampling      | control cost, preserve important failures |
| Privacy       | never store secrets or full payloads      |

## Common Mistakes

- Creating span for every helper call.
- Forgetting outbound propagation.
- Using high-cardinality span names or attributes.
- Treating request ID as full tracing solution.
- Duplicating trace detail into logs line by line.
- Recording secrets or payload bodies in spans.
- Losing context across goroutines or background jobs.
- Tracing everything instead of tracing meaningful boundaries.
