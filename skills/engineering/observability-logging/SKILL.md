---
name: observability-logging
description: Use when adding or reviewing application logging in Go backend services, especially structured logs, HTTP request logs, error logging, log context, redaction, low-cardinality metrics, or targeted profiling
---

# Observability Logging

## Overview

Use logs to explain meaningful events, not every step. Prefer one structured log at the boundary with enough context to understand what happened.

Core principle: enrich errors as they move up, then handle and log them once.

## When to Use

Use this skill when working on Go backend observability and any of these show up:

- HTTP request or response logging
- structured logging with `slog` or `zap`
- error logging placement or duplicate logs
- missing log context such as request ID, route, tenant, or user
- redaction, secret handling, or safe payload logging
- low-cardinality metrics for service health
- targeted profiling for concrete in-process performance problem

Do not use this skill for distributed tracing, span design, trace propagation, or sampling. Use `observability-tracing` for those.

Quick chooser:

- Need log lines, log fields, log levels, redaction, metrics, or profiling -> `observability-logging`
- Need spans, trace IDs, propagation, sampling, or cross-service path analysis -> `observability-tracing`

## Logging Defaults

- Use dependency injection for loggers. Avoid global loggers.
- Pick one logger library per service. In Go, prefer `slog` or `zap`, not both.
- Use structured logging. Prefer stable key/value fields over formatted strings.
- Use JSON in remote environments. Use text locally when easier for humans.
- Include timestamps everywhere except deterministic test output.
- Almost never use `warn`. Most events are `info` or `error`.
- Use `fmt.Fprintf` only before logger initialization.

## Minimal Logging Strategy

- Do not log same event more than once.
- Do not log events nobody will act on.
- Do not log transient failures too early, such as first retry failure.
- Log complete event, not every internal step.
- Log at boundary where decision is made.
- Most errors should be logged. Not every log line is an error.

## Request Logging Pattern

For HTTP services, log request after response is served. Middleware usually gives cleanest boundary.

Log fields that often matter:

- `method`
- `route`
- `status`
- `duration`
- request and response sizes if useful
- `user_agent`
- request and response content type if useful
- relevant auth or cookie presence, not raw secret values
- request or correlation ID

Do not log everything by default. Add fields when they help operations.

One common middleware shape:

```go
func LoggingMiddleware(base *slog.Logger, next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		ww := newStatusWriter(w)
		reqID := requestIDFromHeaderOrGenerate(r)

		log := base.With(
			slog.String("request_id", reqID),
			slog.String("method", r.Method),
			slog.String("route", routePattern(r)),
		)

		ctx := context.WithValue(r.Context(), loggerKey{}, log)
		next.ServeHTTP(ww, r.WithContext(ctx))

		log.Info("request complete",
			slog.Int("status", ww.status),
			slog.Duration("duration", time.Since(start)),
			slog.Int("bytes_out", ww.bytes),
		)
	})
}
```

`newStatusWriter`, `requestIDFromHeaderOrGenerate`, and `routePattern` are placeholders for your existing response wrapper, request ID policy, and router API.

## Handle Errors Once

Handling error = inspect it and decide. Do that once. Lower layers should usually return enriched errors, not log them.

Bad: helper logs, caller logs same failure again.

```go
func order(purchase Purchase) {
	if err := validatePurchase(purchase); err != nil {
		slog.Error("failed to validate purchase", "error", err)
		return
	}
}

func validatePurchase(purchase Purchase) error {
	for i, item := range purchase.Items {
		if err := validateItem(item); err != nil {
			slog.Error("failed to validate item", "item_no", i, "item", item, "error", err)
			return err
		}
	}
	return nil
}
```

Better: enrich on return, log once at boundary.

```go
func order(purchase Purchase) {
	if err := validatePurchase(purchase); err != nil {
		slog.Error("failed to validate purchase", "error", err)
		return
	}
}

func validatePurchase(purchase Purchase) error {
	for i, item := range purchase.Items {
		if err := validateItem(item); err != nil {
			return WithAttrs(
				fmt.Errorf("failed to validate item: %w", err),
				"item_no", i,
				"item", item,
			)
		}
	}
	return nil
}
```

One workable pattern:

```go
type errWithAttrs struct {
	error
	attrs []slog.Attr
}

func (e *errWithAttrs) Attrs() []slog.Attr {
	return e.attrs
}

func WithAttrs(err error, args ...any) error {
	return &errWithAttrs{error: err, attrs: argsToAttr(args)}
}
```

Then logger boundary can unwrap and emit preserved attrs once:

```go
func logError(log *slog.Logger, msg string, err error) {
	var withAttrs interface{ Attrs() []slog.Attr }
	if errors.As(err, &withAttrs) {
		args := make([]any, 0, len(withAttrs.Attrs())+1)
		for _, attr := range withAttrs.Attrs() {
			args = append(args, attr)
		}
		args = append(args, slog.Any("error", err))
		log.Error(msg, args...)
		return
	}

	log.Error(msg, slog.Any("error", err))
}
```

If multiple errors matter, join them instead of deep nesting. Format joined errors clearly at logger boundary.

## Context Model

Log line without context is fragment, not story. Add context that helps explain where event happened.

- instance context
- request context
- user context

### Instance Context

Useful fields depend on runtime, but for backends consider:

- environment
- hostname
- IP or node identity when useful
- cloud region
- pod or container name
- operating system or kernel details when relevant
- build time and git SHA from `ldflags`

Do not dump every possible field. Add context that helps distinguish instances in real operations.

### Request Context

Useful request-scoped fields often include:

- request or correlation ID
- response status
- duration
- request and response sizes
- authenticated user information if needed
- user agent
- content type

Prefer request ID or correlation ID in headers. Return it in response headers too when possible.

For expected client failures such as validation or auth errors, prefer one request-boundary log or metric over noisy helper-level `error` logs. Reserve `error` for failures operators likely need to investigate.

### User Context

User context is one part of request context. Keep only operationally useful user fields, then store them in request-scoped log context instead of globals.

- one shared object for request-scoped logging fields
- include only fields such as user ID, tenant, or role when they help operations
- downstream code can enrich it
- scales beyond username only
- keeps state local to request

## HTTP Error Responses

Keep user-facing response separate from internal error details. Keep internal log messages lowercase for consistency, but keep response body focused on the client.

- keep internal error detail out of user response

```go
func httpError(ctx context.Context, w http.ResponseWriter, status int, err error, httpErrBody string) {
	if logCtx, ok := ctx.Value(logContextKey).(*LogContext); ok {
		logCtx.Error = err
	}

	http.Error(w, httpErrBody, status)
}
```

This lets boundary logging include rich internal error while response body stays safe and useful for client.

## Security and Redaction

- Secrets must be redacted.
- Log minimum information needed.
- Avoid full response logging unless strong reason exists.
- Never log raw `Authorization` or `Cookie` headers.
- Be careful with query strings and body fields; many carry secrets or PII.
- Consider filtering suspicious keys such as `password`, `key`, `apikey`, `secret`, `pin`, `creditcardno`.
- Obfuscate sensitive values when partial visibility is enough, for example IP `123.123.123.x`.
- If sensitive log retention is unavoidable, consider encryption.

Prefer allowlist thinking. Do not rely only on engineers remembering every sensitive field by hand.

## Metrics Basics

If you add nothing else, add system health metrics.

- counters, gauges, histograms
- RED and USE
- low-cardinality label warning
- default HTTP metric set

Metric types:

- Counters: how many times thing happened
- Gauges: current amount or utilization
- Histograms: distribution such as latency

Useful default frameworks:

- RED = Rate, Errors, Duration
- USE = Utilization, Saturation, Errors

Keep labels low cardinality. Avoid user IDs, raw URLs, request IDs, and other unbounded values.

Good default HTTP metric set:

- request counter by route, method, and coarse status class
- request duration histogram by route and method
- in-flight requests gauge
- dependency error counter where useful

## Profiling Basics

Use profiling when you have specific performance problem to investigate.

- use only for concrete performance investigation

Useful profiles:

- CPU
- heap
- goroutines
- blocking
- Go runtime execution trace

Profiling is investigation tool, not default background noise source.
If profiling in production, gate access carefully and use it deliberately.

## Quick Reference

| Topic            | Default                                          |
| ---------------- | ------------------------------------------------ |
| Logger lifecycle | inject logger, avoid globals                     |
| Logger library   | one of `slog` or `zap` per service               |
| Format           | JSON remote, text local                          |
| Level choice     | mostly `info` and `error`; rare `warn`           |
| Request logging  | middleware, log after response                   |
| Error logging    | enrich on return, log once at boundary           |
| Correlation      | request ID in headers and logs                   |
| Sensitive data   | redact or omit                                   |
| Metrics          | counters, gauges, histograms; start with RED/USE |
| Profiling        | use for concrete performance investigation       |

## Common Mistakes

- Logging same failure in helper and caller.
- Logging every step instead of complete event.
- Using global logger instead of injected dependency.
- Mixing `slog` and `zap` in one service.
- Logging secrets or full payloads.
- Using high-cardinality values as metric labels.
- Forgetting timestamps outside tests.
- Logging retry loop noise too early.
- Treating every 4xx as noisy `error` log.
- Putting raw developer detail in HTTP error body.
