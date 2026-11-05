#!/usr/bin/env python3
from pathlib import Path
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts/lib"))

from skill_metadata import read_skill_frontmatter


# Skills with side effects or a mode switch. The agent must not start these on its own.
USER_INVOKED = {
    "configure-agents",
    "director",
    "setup-github-project",
    "ui-implement",
    "ui-init",
    "ux-details",
}


class FrontmatterTest(unittest.TestCase):
    def write_skill(self, body: str) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        skill = Path(directory.name) / "SKILL.md"
        skill.write_text(body)
        return skill

    def test_reads_top_level_keys_and_unquotes(self) -> None:
        skill = self.write_skill('---\nname: "example"\ndescription: Example.\n---\nBody\n')
        self.assertEqual(read_skill_frontmatter(skill), {"name": "example", "description": "Example."})

    def test_rejects_duplicate_keys(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate"):
            read_skill_frontmatter(self.write_skill("---\nname: a\nname: b\n---\n"))

    def test_rejects_unclosed_frontmatter(self) -> None:
        with self.assertRaisesRegex(ValueError, "does not close"):
            read_skill_frontmatter(self.write_skill("---\nname: a\n"))


class SkillInvocationTest(unittest.TestCase):
    def test_user_invoked_skills_set_the_flag(self) -> None:
        skills = {skill.parent.name: skill for skill in (REPO / "skills").glob("*/*/SKILL.md")}
        for name in sorted(USER_INVOKED):
            with self.subTest(skill=name):
                self.assertEqual(read_skill_frontmatter(skills[name]).get("disable-model-invocation"), "true")


if __name__ == "__main__":
    unittest.main()
