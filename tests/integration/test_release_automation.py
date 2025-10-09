"""Integration tests for release automation workflow."""
import pytest
from pathlib import Path
import subprocess


class TestReleaseAutomation:
    """Test the complete release automation process."""

    def test_full_release_workflow(self, sample_git_repo: Path, sample_markdown_files: Path):
        """Test complete release from build to git tag."""
        from src.release import create_release

        # Copy markdown files to repo
        markdown_dir = sample_git_repo / "markdown"
        markdown_dir.mkdir()
        for md_file in sample_markdown_files.glob("*.md"):
            (markdown_dir / md_file.name).write_text(md_file.read_text())

        output_dir = sample_git_repo / "output"
        output_dir.mkdir()

        # Create release
        release_info = create_release(
            repo_dir=sample_git_repo,
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version="1.0.0"
        )

        # Verify PDF was created
        assert release_info["pdf_path"].exists()

        # Verify git tag was created
        result = subprocess.run(
            ["git", "tag", "-l", "v1.0.0"],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        assert "v1.0.0" in result.stdout

        # Verify PDF was committed
        result = subprocess.run(
            ["git", "log", "--oneline", "-1"],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        assert "1.0.0" in result.stdout.lower() or "release" in result.stdout.lower()

    def test_release_version_auto_increment(self, sample_git_repo: Path, sample_markdown_files: Path):
        """Test automatic version incrementing for releases."""
        from src.release import create_release, get_next_version

        # Create first release
        markdown_dir = sample_git_repo / "markdown"
        markdown_dir.mkdir()
        for md_file in sample_markdown_files.glob("*.md"):
            (markdown_dir / md_file.name).write_text(md_file.read_text())

        output_dir = sample_git_repo / "output"
        output_dir.mkdir()

        create_release(
            repo_dir=sample_git_repo,
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version="1.0.0"
        )

        # Get next version
        next_version = get_next_version(sample_git_repo, increment="patch")
        assert next_version == "v1.0.1"

        next_version = get_next_version(sample_git_repo, increment="minor")
        assert next_version == "v1.1.0"

        next_version = get_next_version(sample_git_repo, increment="major")
        assert next_version == "v2.0.0"

    def test_release_with_changelog(self, sample_git_repo: Path, sample_markdown_files: Path):
        """Test release includes changelog generation."""
        from src.release import create_release, generate_changelog

        markdown_dir = sample_git_repo / "markdown"
        markdown_dir.mkdir()
        for md_file in sample_markdown_files.glob("*.md"):
            (markdown_dir / md_file.name).write_text(md_file.read_text())

        output_dir = sample_git_repo / "output"
        output_dir.mkdir()

        # Create some commits
        test_file = sample_git_repo / "test.txt"
        test_file.write_text("test")
        subprocess.run(["git", "add", "."], cwd=sample_git_repo)
        subprocess.run(["git", "commit", "-m", "feat: Add new feature"], cwd=sample_git_repo)
        subprocess.run(["git", "commit", "--allow-empty", "-m", "fix: Bug fix"], cwd=sample_git_repo)

        # Create release
        release_info = create_release(
            repo_dir=sample_git_repo,
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version="1.0.0",
            generate_changelog=True
        )

        # Verify changelog was created
        assert "changelog" in release_info
        changelog = release_info["changelog"]
        assert "new feature" in changelog.lower() or "feat" in changelog.lower()

    def test_release_rollback_on_failure(self, sample_git_repo: Path, sample_markdown_files: Path):
        """Test that release rolls back on failure."""
        from src.release import create_release, ReleaseError

        markdown_dir = sample_git_repo / "markdown"
        markdown_dir.mkdir()

        output_dir = sample_git_repo / "output"
        output_dir.mkdir()

        # Get initial tag count
        result = subprocess.run(
            ["git", "tag", "-l"],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        initial_tags = result.stdout.strip().split("\n") if result.stdout.strip() else []

        # Attempt release with no markdown files (should fail)
        with pytest.raises(ReleaseError):
            create_release(
                repo_dir=sample_git_repo,
                markdown_dir=markdown_dir,
                output_dir=output_dir,
                version="1.0.0"
            )

        # Verify no new tags were created
        result = subprocess.run(
            ["git", "tag", "-l"],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        final_tags = result.stdout.strip().split("\n") if result.stdout.strip() else []
        assert len(final_tags) == len(initial_tags)

    def test_release_with_custom_tag_message(self, sample_git_repo: Path, sample_markdown_files: Path):
        """Test release with custom tag message."""
        from src.release import create_release

        markdown_dir = sample_git_repo / "markdown"
        markdown_dir.mkdir()
        for md_file in sample_markdown_files.glob("*.md"):
            (markdown_dir / md_file.name).write_text(md_file.read_text())

        output_dir = sample_git_repo / "output"
        output_dir.mkdir()

        custom_message = "Release v1.0.0 with important updates"

        create_release(
            repo_dir=sample_git_repo,
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version="1.0.0",
            tag_message=custom_message
        )

        # Verify tag message
        result = subprocess.run(
            ["git", "tag", "-l", "-n1", "v1.0.0"],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        assert "v1.0.0" in result.stdout
