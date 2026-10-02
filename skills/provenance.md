# Skill provenance

The migration classified skills by their source before changing either live harness directory.

| Skills | Classification | Source |
| --- | --- | --- |
| `cloudflare` | Locked external source | Official `cloudflare/skills` at the commit in `sources.lock.json`, including Cloudflare CLI guidance |
| `unslop` | Locked external source | `cursor/plugins` at the commit in `sources.lock.json` |
| `research`, `tdd`, `triage` | Locked external source | `mattpocock/skills` at the commit in `sources.lock.json` |
| `setup-matt-pocock-skills` | Local customization | Forked from `mattpocock/skills` to prefer `AGENTS.md` over `CLAUDE.md` |
| `composition-patterns`, `react-best-practices`, `react-native-skills`, `react-view-transitions`, `writing-guidelines` | Locked external source | `vercel-labs/agent-skills` at the commit in `sources.lock.json`; the migrated files matched that tree |
| `web-design-guidelines` | Vendored upstream snapshot | [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines) at `063bee94c3f4df8453406c830b0a7df0f2860278` |
| `design-taste-frontend`, `image-to-code` | Vendored upstream snapshots | [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill/tree/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills) at `ce26fc25c0e5e8cab638f883de62d9a86ee5e45b`, from `skills/taste-skill` and `skills/image-to-code-skill`, with the upstream license |
| `awesome-design-md` | Vendored skill with local adaptation | [`aradotso/trending-skills`](https://github.com/aradotso/trending-skills/tree/2384a003145a59276aa204b10c47262aab65a3c9/skills/awesome-design-md) at `2384a003145a59276aa204b10c47262aab65a3c9`. Removed the outer Markdown code fence so agents can read its frontmatter and added local reference guidance. Bundled `design-md/`, README, and MIT license from [`VoltAgent/awesome-design-md`](https://github.com/VoltAgent/awesome-design-md/tree/f6961238d5cddcf8042a74a70fc400ec67181abb) at `f6961238d5cddcf8042a74a70fc400ec67181abb`. |
| `rust-skills` | Locked external source | `leonardomso/rust-skills` at the commit in `sources.lock.json`; the main skill and rule set matched, while old harness prompt copies were discarded |
| `frontend-design`, `grill-me`, `handoff`, `prototype`, `teach`, `write-a-skill` | Local snapshot | Preserved from the existing harness configuration because no immutable upstream revision was recorded |
| `home-tailscale-network` | Locally authored | Added by this repository as an optional personal skill |

Categories organize this repository only. Installed skill IDs remain flat and come from each skill's directory name.
