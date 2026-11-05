#!/usr/bin/env python3
from pathlib import Path
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts/lib"))

from skill_metadata import ALL_HARNESSES, skill_harnesses, skill_install_roots


class SkillMetadataTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)

    def write_skill(self, frontmatter: str) -> Path:
        skill = Path(self.temporary_directory.name) / "SKILL.md"
        skill.write_text(f"---\nname: example\ndescription: Example.\n{frontmatter}---\n")
        return skill

    def test_missing_harnesses_is_global(self) -> None:
        self.assertEqual(skill_harnesses(self.write_skill("")), ALL_HARNESSES)

    def test_inline_harness_include_list(self) -> None:
        self.assertEqual(skill_harnesses(self.write_skill("harnesses: [Codex]\n")), {"codex"})

    def test_block_harness_include_list(self) -> None:
        skill = self.write_skill("harnesses:\n  - Codex\n  - OpenCode\n")
        self.assertEqual(skill_harnesses(skill), {"codex", "opencode"})

    def test_rejects_unknown_harness(self) -> None:
        with self.assertRaisesRegex(ValueError, "unsupported harness"):
            skill_harnesses(self.write_skill("harnesses: [cursor]\n"))

    def roots(self, *harnesses: str) -> list[Path]:
        return skill_install_roots(
            frozenset(harnesses),
            claude_home=Path("/claude"),
            codex_home=Path("/codex"),
            opencode_home=Path("/opencode"),
            shared_home=Path("/agents"),
        )

    def test_restricted_skill_uses_harness_home(self) -> None:
        self.assertEqual(self.roots("opencode"), [Path("/opencode/skills")])
        self.assertEqual(self.roots("claude"), [Path("/claude/skills")])

    def test_global_skill_reaches_shared_and_claude_homes(self) -> None:
        self.assertEqual(self.roots(*ALL_HARNESSES), [Path("/agents/skills"), Path("/claude/skills")])

    def test_mixed_selection_uses_each_home(self) -> None:
        self.assertEqual(self.roots("claude", "codex"), [Path("/codex/skills"), Path("/claude/skills")])


if __name__ == "__main__":
    unittest.main()
