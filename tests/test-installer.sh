#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture="$(mktemp -d /tmp/agents-config-test.XXXXXX)"
trap 'rm -rf "$fixture"' EXIT
export PYTHONDONTWRITEBYTECODE=1
export AGENTS_CONFIG_CODEX_HOME="$fixture/codex"
export AGENTS_CONFIG_OPENCODE_HOME="$fixture/opencode"
export AGENTS_CONFIG_SHARED_HOME="$fixture/agents"
export AGENTS_CONFIG_STATE_HOME="$fixture/state"
export AGENTS_CONFIG_BACKUP_HOME="$fixture/backups"

# Installation may read the checkout revision, but must never fetch skills.
export AGENTS_CONFIG_TEST_GIT="$(command -v git)"
mkdir -p "$fixture/bin"
cat > "$fixture/bin/git" <<'SH'
#!/usr/bin/env bash
if [[ "$*" == 'rev-parse HEAD' ]]; then
  exec "$AGENTS_CONFIG_TEST_GIT" "$@"
fi
echo "unexpected Git command during local installation: $*" >&2
exit 1
SH
chmod +x "$fixture/bin/git"
export PATH="$fixture/bin:$PATH"

mkdir -p "$AGENTS_CONFIG_CODEX_HOME/agents"
printf 'unmanaged\n' > "$AGENTS_CONFIG_CODEX_HOME/AGENTS.md"

if "$repo_dir/scripts/install.sh" --link >/dev/null 2>&1; then
  echo "installer replaced an unmanaged destination without force" >&2
  exit 1
fi

"$repo_dir/scripts/install.sh" --copy --force
second="$($repo_dir/scripts/install.sh --copy --dry-run)"
grep -q 'DRY RUN 0 filesystem change(s)' <<<"$second"
excluded="$($repo_dir/scripts/install.sh --copy --exclude home-tailscale-network --dry-run)"
grep -q "REMOVE  $AGENTS_CONFIG_SHARED_HOME/skills/home-tailscale-network" <<<"$excluded"
find "$AGENTS_CONFIG_BACKUP_HOME" -path '*/unmanaged-collisions/*/AGENTS.md' -type f | grep -q .
python3 "$repo_dir/tests/test-skill-metadata.py"
"$repo_dir/scripts/verify.sh" >/dev/null

# Simulate an existing managed link to the former external skill cache.
python3 - "$repo_dir" <<'PY'
import json
import os
from pathlib import Path
import shutil
import sys

repo = Path(sys.argv[1])
state_home = Path(os.environ['AGENTS_CONFIG_STATE_HOME'])
assert not (state_home / 'cache').exists()
target = Path(os.environ['AGENTS_CONFIG_SHARED_HOME']) / 'skills/research'
legacy_cache = state_home / 'legacy-cache/research'
shutil.copytree(target, legacy_cache)
shutil.rmtree(target)
target.symlink_to(legacy_cache)
state_file = state_home / 'install-state.json'
state = json.loads(state_file.read_text())
for entry in state['targets']:
    if entry['target'] == str(target):
        entry['source'] = 'external-skill:research'
        entry['mode'] = 'link'
state_file.write_text(json.dumps(state))
PY
"$repo_dir/scripts/install.sh" --link >/dev/null
python3 - "$repo_dir" <<'PY'
import os
from pathlib import Path
import sys

repo = Path(sys.argv[1])
shared_home = Path(os.environ['AGENTS_CONFIG_SHARED_HOME'])
for source in (repo / 'skills').glob('*/*/SKILL.md'):
    target = shared_home / 'skills' / source.parent.name
    assert target.is_symlink(), target
    assert target.resolve() == source.parent, target
assert not (Path(os.environ['AGENTS_CONFIG_STATE_HOME']) / 'cache').exists()
PY
linked="$($repo_dir/scripts/install.sh --link --dry-run)"
grep -q 'DRY RUN 0 filesystem change(s)' <<<"$linked"
"$repo_dir/scripts/verify.sh" >/dev/null
echo "PASS    local copy/link installation, cache migration, collision, idempotence, and exclusion checks"
