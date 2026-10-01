# Skill provenance

The migration classified skills by their source before changing either live harness directory.

| Skills | Classification | Source |
| --- | --- | --- |
| `cloudflare` | Locked external source | Official `cloudflare/skills` at the commit in `sources.lock.json`, including Cloudflare CLI guidance |
| `unslop` | Locked external source | `cursor/plugins` at the commit in `sources.lock.json` |
| `research`, `tdd`, `triage` | Locked external source | `mattpocock/skills` at the commit in `sources.lock.json` |
| `setup-matt-pocock-skills` | Local customization | Forked from `mattpocock/skills` to prefer `AGENTS.md` over `CLAUDE.md` |
| `composition-patterns`, `react-best-practices`, `react-native-skills`, `react-view-transitions`, `web-design-guidelines`, `writing-guidelines` | Locked external source | `vercel-labs/agent-skills` at the commit in `sources.lock.json`; the migrated files matched that tree |
| `rust-skills` | Locked external source | `leonardomso/rust-skills` at the commit in `sources.lock.json`; the main skill and rule set matched, while old harness prompt copies were discarded |
| `frontend-design`, `grill-me`, `handoff`, `prototype`, `teach`, `write-a-skill` | Local snapshot | Preserved from the existing harness configuration because no immutable upstream revision was recorded |
| `home-tailscale-network` | Locally authored | Added by this repository as an optional personal skill |

Categories organize this repository only. Installed skill IDs remain flat and come from each skill's directory name.
