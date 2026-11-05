from __future__ import annotations

from pathlib import Path
import re


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def read_skill_frontmatter(skill: Path) -> dict[str, str]:
    """Return the top-level scalar keys of a SKILL.md frontmatter block."""
    lines = skill.read_text().splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"frontmatter does not start in {skill}")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError(f"frontmatter does not close in {skill}") from error

    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            continue
        key, raw_value = match.groups()
        if key in values:
            raise ValueError(f"duplicate frontmatter key {key!r} in {skill}")
        values[key] = _unquote(raw_value)
    return values
