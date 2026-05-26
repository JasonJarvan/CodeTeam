import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "init_repo_mem.py"


class InitRepoMemTests(unittest.TestCase):
    def test_default_init_creates_standard_persistent_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(repo_root), "--default-language", "zh-CN"],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            base = repo_root / "docs" / "RepoMem"
            self.assertTrue((base / "persist" / "config.md").exists())
            self.assertTrue((base / "persist" / "version-plan.md").exists())
            self.assertTrue((base / "persist" / "architecture" / "index.md").exists())
            self.assertTrue((base / "persist" / "memory" / "index.md").exists())

    def test_analyze_existing_creates_init_proposal(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            (repo_root / "README.md").write_text("# Existing Repo\n", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(repo_root),
                    "--default-language",
                    "zh-CN",
                    "--existing-slug",
                    "bootstrap-existing-repo",
                    "--analyze-existing",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            proposal = repo_root / "docs" / "RepoMem" / "temp" / "bootstrap-existing-repo" / "init-proposal.md"
            self.assertTrue(proposal.exists())
            content = proposal.read_text(encoding="utf-8")
            self.assertIn("task_type: init", content)
            self.assertIn("Detected Documentation Sources", content)

    def test_analyze_existing_detects_repomem_persistent_and_skill_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            (repo_root / "docs" / "RepoMem" / "persist" / "architecture").mkdir(parents=True, exist_ok=True)
            (repo_root / "docs" / "RepoMem" / "persist" / "memory").mkdir(parents=True, exist_ok=True)
            (repo_root / "docs" / "RepoMem" / "persist" / "architecture" / "index.md").write_text("# 架构索引\n", encoding="utf-8")
            (repo_root / "docs" / "RepoMem" / "persist" / "memory" / "index.md").write_text("# 记忆索引\n", encoding="utf-8")
            (repo_root / "docs" / "RepoMem" / "persist" / "version-plan.md").write_text("# 版本计划\n", encoding="utf-8")
            (repo_root / "repo-mem" / "references").mkdir(parents=True, exist_ok=True)
            (repo_root / "repo-mem" / "SKILL.md").write_text("---\nname: repo-mem\n---\n", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(repo_root),
                    "--default-language",
                    "zh-CN",
                    "--existing-slug",
                    "bootstrap-existing-repo",
                    "--analyze-existing",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            proposal = repo_root / "docs" / "RepoMem" / "temp" / "bootstrap-existing-repo" / "init-proposal.md"
            content = proposal.read_text(encoding="utf-8")
            self.assertIn("docs/RepoMem/persist/architecture/index.md", content)
            self.assertIn("docs/RepoMem/persist/memory/index.md", content)
            self.assertIn("docs/RepoMem/persist/version-plan.md", content)
            self.assertIn("repo-mem/SKILL.md", content)

    def test_apply_existing_generates_conflicts_when_persistent_docs_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            base = repo_root / "docs" / "RepoMem"
            (base / "persist" / "architecture").mkdir(parents=True, exist_ok=True)
            (base / "persist" / "memory").mkdir(parents=True, exist_ok=True)
            (base / "persist" / "architecture" / "index.md").write_text("# Existing Architecture\n", encoding="utf-8")
            slug_dir = base / "temp" / "bootstrap-existing-repo"
            slug_dir.mkdir(parents=True, exist_ok=True)
            (slug_dir / "init-proposal.md").write_text(
                "---\nslug: bootstrap-existing-repo\nstatus: active\nupdated_at:\ntask_type: init\n---\n\n# Init Proposal\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(repo_root),
                    "--default-language",
                    "zh-CN",
                    "--existing-slug",
                    "bootstrap-existing-repo",
                    "--apply-existing",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            conflicts = slug_dir / "init-conflicts.md"
            self.assertTrue(conflicts.exists())
            content = conflicts.read_text(encoding="utf-8")
            self.assertIn("conflict_id", content)
            self.assertIn("architecture/index.md", content)

    def test_apply_existing_resolutions_keep_existing_leaves_file_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            base = repo_root / "docs" / "RepoMem"
            (base / "persist" / "architecture").mkdir(parents=True, exist_ok=True)
            target = base / "persist" / "architecture" / "index.md"
            target.write_text("# Existing Architecture\n", encoding="utf-8")
            slug_dir = base / "temp" / "bootstrap-existing-repo"
            slug_dir.mkdir(parents=True, exist_ok=True)
            (slug_dir / "init-proposal.md").write_text(
                "---\nslug: bootstrap-existing-repo\nstatus: active\nupdated_at:\ntask_type: init\n---\n\n# Init Proposal\n",
                encoding="utf-8",
            )
            (slug_dir / "init-conflicts.md").write_text(
                "\n".join(
                    [
                        "---",
                        "slug: bootstrap-existing-repo",
                        "status: active",
                        "updated_at:",
                        "task_type: init",
                        "---",
                        "",
                        "# Init Conflicts",
                        "",
                        "## Summary",
                        "",
                        "- one conflict",
                        "",
                        "## Conflict Items",
                        "",
                        "### conflict-1",
                        "",
                        "- target_file: `persist/architecture/index.md`",
                        "- conflict_type: `existing-persistent-doc`",
                        "- existing_content_summary: existing",
                        "- proposed_content_summary: proposed",
                        "",
                        "## Suggested Resolution Options",
                        "",
                        "- keep existing",
                        "",
                        "## Human Decisions",
                        "",
                        "- `conflict-1`: keep existing",
                        "",
                        "## Execution Notes",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(repo_root),
                    "--default-language",
                    "zh-CN",
                    "--existing-slug",
                    "bootstrap-existing-repo",
                    "--resolve-conflicts",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(target.read_text(encoding="utf-8"), "# Existing Architecture\n")

    def test_apply_existing_resolutions_replace_with_proposed_updates_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            base = repo_root / "docs" / "RepoMem"
            (base / "persist" / "architecture").mkdir(parents=True, exist_ok=True)
            target = base / "persist" / "architecture" / "index.md"
            target.write_text("# Existing Architecture\n", encoding="utf-8")
            slug_dir = base / "temp" / "bootstrap-existing-repo"
            slug_dir.mkdir(parents=True, exist_ok=True)
            (slug_dir / "init-proposal.md").write_text(
                "---\nslug: bootstrap-existing-repo\nstatus: active\nupdated_at:\ntask_type: init\n---\n\n# Init Proposal\n",
                encoding="utf-8",
            )
            (slug_dir / "init-conflicts.md").write_text(
                "\n".join(
                    [
                        "---",
                        "slug: bootstrap-existing-repo",
                        "status: active",
                        "updated_at:",
                        "task_type: init",
                        "---",
                        "",
                        "# Init Conflicts",
                        "",
                        "## Summary",
                        "",
                        "- one conflict",
                        "",
                        "## Conflict Items",
                        "",
                        "### conflict-1",
                        "",
                        "- target_file: `persist/architecture/index.md`",
                        "- conflict_type: `existing-persistent-doc`",
                        "- existing_content_summary: existing",
                        "- proposed_content_summary: proposed",
                        "",
                        "## Suggested Resolution Options",
                        "",
                        "- replace with proposed",
                        "",
                        "## Human Decisions",
                        "",
                        "- `conflict-1`: replace with proposed",
                        "",
                        "## Execution Notes",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(repo_root),
                    "--default-language",
                    "zh-CN",
                    "--existing-slug",
                    "bootstrap-existing-repo",
                    "--resolve-conflicts",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            updated = target.read_text(encoding="utf-8")
            self.assertIn("# 架构索引", updated)

    def test_apply_existing_resolutions_merge_both_appends_proposed_section(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            base = repo_root / "docs" / "RepoMem"
            (base / "persist" / "architecture").mkdir(parents=True, exist_ok=True)
            target = base / "persist" / "architecture" / "index.md"
            target.write_text("# Existing Architecture\n\nExisting details.\n", encoding="utf-8")
            slug_dir = base / "temp" / "bootstrap-existing-repo"
            slug_dir.mkdir(parents=True, exist_ok=True)
            (slug_dir / "init-proposal.md").write_text(
                "---\nslug: bootstrap-existing-repo\nstatus: active\nupdated_at:\ntask_type: init\n---\n\n# Init Proposal\n",
                encoding="utf-8",
            )
            (slug_dir / "init-conflicts.md").write_text(
                "\n".join(
                    [
                        "---",
                        "slug: bootstrap-existing-repo",
                        "status: active",
                        "updated_at:",
                        "task_type: init",
                        "---",
                        "",
                        "# Init Conflicts",
                        "",
                        "## Summary",
                        "",
                        "- one conflict",
                        "",
                        "## Conflict Items",
                        "",
                        "### conflict-1",
                        "",
                        "- target_file: `persist/architecture/index.md`",
                        "- conflict_type: `existing-persistent-doc`",
                        "- existing_content_summary: existing",
                        "- proposed_content_summary: proposed",
                        "",
                        "## Suggested Resolution Options",
                        "",
                        "- merge both",
                        "",
                        "## Human Decisions",
                        "",
                        "- `conflict-1`: merge both",
                        "",
                        "## Execution Notes",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(repo_root),
                    "--default-language",
                    "zh-CN",
                    "--existing-slug",
                    "bootstrap-existing-repo",
                    "--resolve-conflicts",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            updated = target.read_text(encoding="utf-8")
            self.assertIn("# Existing Architecture", updated)
            self.assertIn("## RepoMem Proposed Merge", updated)
            self.assertIn("# 架构索引", updated)


if __name__ == "__main__":
    unittest.main()
