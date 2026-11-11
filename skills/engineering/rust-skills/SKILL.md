---
name: rust-skills
description: >
  Rust coding guidelines (265 rules, 26 categories). Use when writing,
  reviewing, or refactoring Rust code: ownership, errors, async, unsafe, API
  design, performance, serde, testing, and anti-patterns.
license: MIT
metadata:
  version: "1.5.1"
---

# Rust Best Practices

265 rules in 26 categories for idiomatic, fast Rust. Current for Rust 1.96 (2024 edition). This file is only an index. Each rule is a file in `rules/` with a Bad/Good example and rationale.

## How to use

1. Pick the categories for the task from the table below or the task map.
2. List a category's rules: `ls rules/<prefix>-*` (for example `ls rules/err-*`). Each filename is the rule id.
3. Read the matching rule files before writing or reviewing code. Each starts with a one-line summary: `head -3 rules/<id>.md`.
4. Search by topic with `grep -ril <term> rules/`, or by summary with `grep -h '^> ' rules/<prefix>-*`.
5. [INDEX.md](INDEX.md) lists every rule with its summary and the recommended `Cargo.toml` release and dev profile. Read it only when scanning titles across categories.

When rules conflict, prefer CRITICAL over HIGH over MEDIUM over LOW. `anti-` rules are reference material for spotting bad patterns.

## Categories

| Priority | Category | Impact | Prefix | Scope |
|---|---|---|---|---|
| 1 | Ownership & Borrowing | CRITICAL | `own-` | Borrow vs clone, slices, Cow, Arc/Rc, interior mutability, lifetimes |
| 2 | Error Handling | CRITICAL | `err-` | thiserror/anyhow, Result vs panic, context, error messages |
| 3 | Memory Optimization | CRITICAL | `mem-` | Allocation reuse, SmallVec, boxing, zero-copy, drop order |
| 4 | Unsafe Code | CRITICAL | `unsafe-` | SAFETY comments, Miri, MaybeUninit, extern blocks, Send/Sync |
| 5 | API Design | HIGH | `api-` | Builders, newtypes, typestate, sealed traits, must_use, non_exhaustive |
| 6 | Async/Await | HIGH | `async-` | Tokio runtime, channels, cancellation, select/join, spawn_blocking, locks across await |
| 7 | Concurrency | HIGH | `conc-` | Atomic ordering, rayon, scoped threads, thread-locals |
| 8 | Compiler Optimization | HIGH | `opt-` | Inlining, LTO, codegen units, PGO, SIMD, bounds checks, cache layout |
| 9 | Numeric & Arithmetic Safety | HIGH | `num-` | Overflow, saturating math, checked casts, float comparison, NonZero |
| 10 | Type Safety | MEDIUM | `type-` | Newtypes, enum states, Option/Result use, phantom markers, Display vs Debug |
| 11 | Trait & Generics Design | MEDIUM | `trait-` | dyn vs generics, associated types, blanket impls, object safety |
| 12 | Conversions | MEDIUM | `conv-` | TryFrom, FromStr parsing, AsMut |
| 13 | Const & Compile-Time | MEDIUM | `const-` | const fn, const blocks, const generics, const vs static |
| 14 | Serde | MEDIUM | `serde-` | Derive attributes, rename_all, defaults, flatten, enum representation, validation |
| 15 | Pattern Matching | MEDIUM | `pat-` | let-else, if-let chains, exhaustive enums, `@` bindings, matches! |
| 16 | Macros | MEDIUM | `macro-` | macro_rules hygiene, proc-macro structure and errors, when to prefer functions |
| 17 | Closures | MEDIUM | `closure-` | Fn trait bounds, captures, returning closures, static vs dyn |
| 18 | Collections | MEDIUM | `coll-` | Choosing sequence, map, and set types, BinaryHeap |
| 19 | Naming Conventions | MEDIUM | `name-` | Casing, getters, `as_`/`to_`/`into_` prefixes, iterator and bool naming |
| 20 | Testing | MEDIUM | `test-` | Unit, integration, property, doc, and snapshot tests, fixtures, mocks, benches |
| 21 | Documentation | MEDIUM | `doc-` | Doc comments, examples, `# Errors`, `# Panics`, `# Safety` |
| 22 | Observability | MEDIUM | `obs-` | tracing, structured logs, metrics |
| 23 | Performance Patterns | MEDIUM | `perf-` | Lazy iterators, collect and extend, entry API, I/O buffering, profiling first |
| 24 | Project Structure | LOW | `proj-` | Crate and module layout, workspaces, additive features, visibility, MSRV |
| 25 | Clippy & Linting | LOW | `lint-` | Clippy groups, rustfmt, workspace lints, missing docs |
| 26 | Anti-patterns | REFERENCE | `anti-` | Common mistakes to avoid and their fixes |

## Task map

| Task | Start with |
|---|---|
| New function | `own-`, `err-`, `name-`, `pat-` |
| New struct or public API | `api-`, `type-`, `conv-`, `doc-` |
| Async code | `async-`, `own-` |
| Concurrency, parallelism | `conc-`, `async-`, `own-` |
| Unsafe code | `unsafe-`, `type-`, `test-` |
| Error handling | `err-`, `api-`, `pat-` |
| Conversions | `conv-`, `api-` |
| Serialization | `serde-`, `type-`, `api-` |
| Numeric code | `num-`, `type-` |
| Macros, code generation | `macro-`, `anti-` |
| Closures, callbacks | `closure-`, `type-` |
| Logging, tracing | `obs-`, `err-` |
| Memory optimization | `mem-`, `own-`, `perf-` |
| Performance tuning | `opt-`, `mem-`, `perf-` |
| Code review | `anti-`, `lint-` |

## Always check

These CRITICAL rules apply to nearly every change:

- `own-borrow-over-clone`, `own-slice-over-vec`: borrow instead of cloning, accept `&[T]` and `&str`
- `err-no-unwrap-prod`, `err-result-over-panic`, `err-context-chain`: no `unwrap()` in production, return `Result`, add context
- `err-thiserror-lib`, `err-anyhow-app`: typed errors in libraries, `anyhow` in applications
- `unsafe-safety-comment`, `unsafe-minimize-scope`: a `// SAFETY:` comment on every `unsafe` block, kept small
- `async-no-lock-await`, `async-cancel-safety`: never hold a lock across an `.await`, keep futures cancel-safe
