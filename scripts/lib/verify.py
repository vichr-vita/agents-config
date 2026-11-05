#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

from skill_metadata import read_skill_frontmatter


REPO = Path(__file__).resolve().parents[2]


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS    {message}")


def frontmatter(skill: Path) -> dict[str, str]:
    label = str(skill.relative_to(REPO)) if skill.is_relative_to(REPO) else str(skill)
    try:
        values = read_skill_frontmatter(skill)
    except ValueError as error:
        raise AssertionError(str(error)) from error
    check(True, f"frontmatter parses {label}")
    check(bool(values.get("name")), f"skill name exists {label}")
    check("description" in values, f"skill description exists {label}")
    return values


def main() -> int:
    skills: dict[str, Path] = {}
    skill_ids: set[str] = set()
    for skill in sorted((REPO / "skills").glob("*/*/SKILL.md")):
        directory_name = skill.parent.name
        check(directory_name not in skills, f"unique skill directory {directory_name}")
        skills[directory_name] = skill
        values = frontmatter(skill)
        check(values["name"] not in skill_ids, f"unique skill ID {values['name']}")
        skill_ids.add(values["name"])
        check("harnesses" not in values, f"no harness include-list in {directory_name}")
        check(not (skill.parent / "agents/openai.yaml").exists(), f"no Codex metadata in {directory_name}")

    reviewer = REPO / "agents/adversarial-reviewer.md"
    reviewer_text = reviewer.read_text()
    check(reviewer_text.startswith("---\n") and "\n---\n\n" in reviewer_text, "reviewer frontmatter parses")
    subprocess.run(["bash", "-n", REPO / "scripts/install.sh"], check=True)
    subprocess.run(["bash", "-n", REPO / "scripts/verify.sh"], check=True)
    check(True, "shell entry points parse")

    user_home = Path.home()
    claude_home = Path(os.environ.get("AGENTS_CONFIG_CLAUDE_HOME", user_home / ".claude")).expanduser()
    state_home = Path(os.environ.get("AGENTS_CONFIG_STATE_HOME", user_home / ".local/state/agents-config")).expanduser()
    state_file = state_home / "install-state.json"
    if not state_file.exists():
        print(f"SKIP    live installation checks, state missing at {state_file}")
        return 0

    state = json.loads(state_file.read_text())
    check(
        claude_home.joinpath("rules/agents-config.md").read_bytes() == REPO.joinpath("AGENTS.md").read_bytes(),
        "global prompt is installed",
    )
    check(claude_home.joinpath("agents/adversarial-reviewer.md").exists(), "reviewer is installed")
    for name in skills:
        if name not in state.get("exclusions", []):
            installed_skill = claude_home / "skills" / name / "SKILL.md"
            check(installed_skill.exists(), f"skill is installed {installed_skill}")
            frontmatter(installed_skill)
    print(f"PASS    live state has {len(state['targets'])} managed target(s)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f"FAIL    {error}", file=sys.stderr)
        raise SystemExit(1)
