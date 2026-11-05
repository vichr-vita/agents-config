# Skill provenance

All skills and their supporting files are stored in this repository. This record documents their origins and attribution. It is not installed or loaded as skill instructions. Installation does not resolve or fetch upstream sources.

Keep historical source notes and credits here rather than in skill entrypoints or required references. Technical documentation links used to carry out a skill stay with its instructions. Available upstream licenses are included in each vendored skill directory.

| Skills | Classification | Source |
| --- | --- | --- |
| `cloudflare` | Vendored upstream snapshot | [`cloudflare/skills`](https://github.com/cloudflare/skills/tree/41e0d19858946d18af9ee2c2feebbe2e11d829ff/skills/cloudflare) at `41e0d19858946d18af9ee2c2feebbe2e11d829ff`, including Cloudflare CLI guidance |
| `unslop` | Vendored skill with local adaptation | [`cursor/plugins`](https://github.com/cursor/plugins/tree/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/unslop). The local text derives from the first pstack version (May 2026) and adds the Product copy section. Rules 32 and 33 were added from `2776ddd2355d6d6c8747d3964600f28daf62f049`. |
| `research`, `triage`, `wayfinder`, `prototype`, `improve-codebase-architecture`, `codebase-design`, `domain-modeling`, `diagnosing-bugs`, `retro`, `writing-for-agents`, `grilling`, `grill-me`, `teach`, `setup-matt-pocock-skills` | Vendored upstream snapshots | [`mattpocock/skills`](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills) at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`, without `agents/openai.yaml`. `prototype` was unchanged from `959a8e9f1edc3adbe2f7e3054bb6fbefa6696260`. |
| `tdd` | Vendored skill with local adaptation | [`mattpocock/skills`](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills) at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`. Added the failure-reason check and the evidence rule from [`cursor/plugins`](https://github.com/cursor/plugins/tree/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/tdd). |
| `composition-patterns`, `react-best-practices`, `react-native-skills`, `react-view-transitions`, `writing-guidelines` | Vendored upstream snapshots | [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills) at `063bee94c3f4df8453406c830b0a7df0f2860278`, from the matching directories under `skills/` |
| `web-design-guidelines` | Vendored upstream snapshot | [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines) at `063bee94c3f4df8453406c830b0a7df0f2860278` |
| `design-taste-frontend` | Vendored skill with local adaptation | [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill/tree/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills) at `ce26fc25c0e5e8cab638f883de62d9a86ee5e45b`, from `skills/taste-skill`, with the upstream license. Split into `references/`, removed emphasis markers and generic re-verification steps, and made the user's black background and no-repaint-animation rules take precedence. |
| `awesome-design-md` | Vendored skill with local adaptation | [`aradotso/trending-skills`](https://github.com/aradotso/trending-skills/tree/2384a003145a59276aa204b10c47262aab65a3c9/skills/awesome-design-md) at `2384a003145a59276aa204b10c47262aab65a3c9`. Removed the outer Markdown code fence so agents can read its frontmatter and added local reference guidance. Bundled `design-md/`, README, and MIT license from [`VoltAgent/awesome-design-md`](https://github.com/VoltAgent/awesome-design-md/tree/f6961238d5cddcf8042a74a70fc400ec67181abb) at `f6961238d5cddcf8042a74a70fc400ec67181abb`. |
| `rust-skills` | Vendored upstream snapshot | [`leonardomso/rust-skills`](https://github.com/leonardomso/rust-skills/tree/fd2a861ab0406a4ac536a55274d14ea6fd1ca9c9) at `fd2a861ab0406a4ac536a55274d14ea6fd1ca9c9`, including the complete repository snapshot previously installed from the cache |
| `frontend-design` | Local snapshot | Preserved from the existing harness configuration because no immutable upstream revision was recorded |
| `handoff` | Local snapshot with upstream edits | Merged with the temporary-path and artifact wording from [`mattpocock/skills`](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/handoff). Keeps the local list of objective, completed work, remaining work, and verification status. |
| `file-pr`, `leaving-pr-comments` | Vendored skills with local adaptation | [`t3dotgg/tstack`](https://github.com/t3dotgg/tstack/tree/1085050f3baed1ac724caa4a8166145fb2ac88af/skills) at `1085050f3baed1ac724caa4a8166145fb2ac88af`. `file-pr` uses the global PR signature. |
| `babysit-pr` | Vendored skill with local adaptation | [`t3dotgg/tstack`](https://github.com/t3dotgg/tstack/tree/1085050f3baed1ac724caa4a8166145fb2ac88af/skills) at `1085050f3baed1ac724caa4a8166145fb2ac88af`. Removed `pr-wait`, because T3 Code forbids that kind of waiting, and replaced rebasing with the global PR rules. |
| `full-stop` | Adapted skill | Combines `full-stop` and `full-send` from [`t3dotgg/tstack`](https://github.com/t3dotgg/tstack/tree/1085050f3baed1ac724caa4a8166145fb2ac88af/skills) at `1085050f3baed1ac724caa4a8166145fb2ac88af`. Uses `adversarial-reviewer` instead of `sol-loop`, never merges, and never force-pushes. |
| `correct` | Vendored skill with local adaptation | [`cursor/plugins`](https://github.com/cursor/plugins/tree/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/correct) at `2776ddd2355d6d6c8747d3964600f28daf62f049`. Keeps the rule table in the README rather than the always-loaded instructions. |
| `home-tailscale-network` | Locally authored | Added by this repository as an optional personal skill |
| `model-routing` | Locally authored | Built from Anthropic documentation: [Claude Code best practices](https://code.claude.com/docs/en/best-practices), [model configuration](https://code.claude.com/docs/en/model-config), [subagents](https://code.claude.com/docs/en/sub-agents), and [what a task costs on Opus 5.5](https://claude.dev/blog/what-a-task-costs-on-opus-5-5/), checked November 5, 2026. |
| `mental-contrasting` | Locally authored | Coaching workflow based on the user's copy of Andrew D. Huberman's *Protocols*, Learning Protocol 2. Book and WOOP sources are recorded below; Vikunja documentation stays in the working references. The book is not bundled. |
| `observability-logging`, `observability-tracing` | Vendored upstream snapshots | [`ci719/opencode-config`](https://github.deutsche-boerse.de/ci719/opencode-config/tree/dd2b692a31ebd86b751025ce66802ff12c4a02d1/skills) at `dd2b692a31ebd86b751025ce66802ff12c4a02d1`, from the matching directories under `skills/`. Imported without changes. |
| `apple-design` | Vendored skill with local adaptation | [`emilkowalski/skills`](https://github.com/emilkowalski/skills/tree/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/apple-design) at `e8a175de22ae1e49370fc144c1f3bb9aeedf988d`, with the MIT license. Replaced the canned initial response with guidance to follow the requested task and project UI constraints. |

Categories organize this repository only. Installed skill IDs remain flat and come from each skill's directory name.

Local attribution cleanup moves source appendices, author metadata, and promotional credits out of skill instructions and compiled guides. The upstream snapshots listed above identify the imported versions before these edits. License files and technical documentation links are preserved.

## Attribution details

### Skill authors

| Skill directory | Upstream author |
| --- | --- |
| `composition-patterns` | vercel |
| `react-best-practices` | vercel |
| `react-native-skills` | vercel |
| `react-view-transitions` | vercel |
| `rust-skills` | leonardomso |
| `web-design-guidelines` | vercel |
| `writing-guidelines` | vercel |

The compiled React Best Practices and React View Transitions guides credit Vercel Engineering. The compiled Composition Patterns and React Native Skills guides use the byline "Engineering."

### Rust skills

This skill is an independent synthesis of official Rust guidance, well-known books, and patterns from widely-used crates. It is not affiliated with or endorsed by the Rust project or any crate author; the text and code examples are original.

**Official Rust documentation**

- [The Rust Reference](https://doc.rust-lang.org/reference/)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [The Rustonomicon](https://doc.rust-lang.org/nomicon/) (unsafe code)
- [Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)
- [Standard library docs](https://doc.rust-lang.org/std/) and [release notes](https://doc.rust-lang.org/releases.html)

**Books & guides**

- [The Rust Performance Book](https://nnethercote.github.io/perf-book/), Nicholas Nethercote
- [Rust Design Patterns](https://rust-unofficial.github.io/patterns/), rust-unofficial
- [Rust Atomics and Locks](https://marabos.nl/atomics/), Mara Bos
- [Effective Rust](https://effective-rust.com/), David Drysdale

**Tooling**

- [Clippy lint documentation](https://rust-lang.github.io/rust-clippy/)
- [Miri](https://github.com/rust-lang/miri)

**Real-world codebases studied for idioms**

- ripgrep, tokio, serde, clap, polars, axum, cargo, hyper, bevy, rayon, and dtolnay's crates (thiserror, anyhow, syn)

This project is MIT-licensed. Referenced upstream materials remain under their own licenses (the official Rust docs and API Guidelines are dual MIT / Apache-2.0).

### composition-patterns bibliography

1. [https://react.dev](https://react.dev)
2. [https://react.dev/learn/passing-data-deeply-with-context](https://react.dev/learn/passing-data-deeply-with-context)
3. [https://react.dev/reference/react/use](https://react.dev/reference/react/use)

### react-best-practices bibliography

1. [https://react.dev](https://react.dev)
2. [https://nextjs.org](https://nextjs.org)
3. [https://swr.vercel.app](https://swr.vercel.app)
4. [https://github.com/shuding/better-all](https://github.com/shuding/better-all)
5. [https://github.com/isaacs/node-lru-cache](https://github.com/isaacs/node-lru-cache)
6. [https://vercel.com/blog/how-we-optimized-package-imports-in-next-js](https://vercel.com/blog/how-we-optimized-package-imports-in-next-js)
7. [https://vercel.com/blog/how-we-made-the-vercel-dashboard-twice-as-fast](https://vercel.com/blog/how-we-made-the-vercel-dashboard-twice-as-fast)

### react-native-skills bibliography

1. [https://react.dev](https://react.dev)
2. [https://reactnative.dev](https://reactnative.dev)
3. [https://docs.swmansion.com/react-native-reanimated](https://docs.swmansion.com/react-native-reanimated)
4. [https://docs.swmansion.com/react-native-gesture-handler](https://docs.swmansion.com/react-native-gesture-handler)
5. [https://docs.expo.dev](https://docs.expo.dev)
6. [https://legendapp.com/open-source/legend-list](https://legendapp.com/open-source/legend-list)
7. [https://github.com/nandorojo/galeria](https://github.com/nandorojo/galeria)
8. [https://zeego.dev](https://zeego.dev)

### Awesome Design MD

Skill by [ara.so](https://ara.so), Daily 2026 Skills collection.

- **Repo:** https://github.com/VoltAgent/awesome-design-md
- **VoltAgent Framework:** https://github.com/VoltAgent/voltagent
- **Discord:** https://s.voltagent.dev/discord
- **License:** MIT

### Mental contrasting

This skill draws on Andrew D. Huberman's *Protocols: An Operating Manual for the Human Body*, Learning Protocol 2, "Use Mental Contrasting to Achieve a 'State of Urgency' and Reach Your Goals," printed pages 465 to 476. The user supplied the EPUB. The section is `index_split_055.html`, with supporting endnotes 159, 161, 162, 167, and 168 in `index_split_077.html`.

The skill's method notes paraphrase that section. The book and its text are not bundled, and the EPUB is not needed to use the skill. Huberman describes an initial written exercise of about ten minutes, followed by rereading and revision when circumstances or motivation change. That duration and his personal results are examples, not requirements or promises.

The [official WOOP practice guide](https://woopmylife.org/en/practice) emphasizes imagining, preserving the order of the four steps, and choosing one main inner obstacle with one response. The skill uses that focus for the core exercise. The book's broader obstacle inventory can inform supporting tasks afterward.

In the [2009 energization study](https://doi.org/10.1177/0146167208330856), mental contrasting linked commitment to expectations of success. The book also cites [Kappes and colleagues' 2012 study](https://doi.org/10.1016/j.jesp.2012.02.002) on linking obstacles with instrumental behavior.
