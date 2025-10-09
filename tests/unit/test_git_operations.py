"""Unit tests for git operations."""
import pytest
from pathlib import Path
import subprocess


class TestGitOperations:
    """Test git tagging and release functionality."""

    def test_create_git_tag(self, sample_git_repo: Path):
        """Test creating a git tag."""
        from src.git_handler import create_tag

        version = "v1.0.0"
        create_tag(sample_git_repo, version)

        # Check that tag was created
        result = subprocess.run(
            ["git", "tag", "-l", version],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        assert version in result.stdout

    def test_tag_with_message(self, sample_git_repo: Path):
        """Test creating annotated tag with message."""
        from src.git_handler import create_tag

        version = "v1.0.0"
        message = "Release version 1.0.0"
        create_tag(sample_git_repo, version, message=message)

        # Check tag message
        result = subprocess.run(
            ["git", "tag", "-l", "-n", version],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        assert version in result.stdout

    def test_get_current_version(self, sample_git_repo: Path):
        """Test getting current version from git tags."""
        from src.git_handler import get_current_version, create_tag

        # Create some tags
        create_tag(sample_git_repo, "v1.0.0")
        create_tag(sample_git_repo, "v1.1.0")
        create_tag(sample_git_repo, "v2.0.0")

        version = get_current_version(sample_git_repo)
        assert version == "v2.0.0"

    def test_version_increment(self):
        """Test version number incrementing."""
        from src.git_handler import increment_version

        assert increment_version("v1.0.0", "major") == "v2.0.0"
        assert increment_version("v1.2.3", "minor") == "v1.3.0"
        assert increment_version("v1.2.3", "patch") == "v1.2.4"

    def test_tag_already_exists(self, sample_git_repo: Path):
        """Test handling of duplicate tag creation."""
        from src.git_handler import create_tag, TagExistsError

        version = "v1.0.0"
        create_tag(sample_git_repo, version)

        # Attempting to create again should raise error
        with pytest.raises(TagExistsError):
            create_tag(sample_git_repo, version)

    def test_parse_version_string(self):
        """Test parsing version strings."""
        from src.git_handler import parse_version

        assert parse_version("v1.2.3") == (1, 2, 3)
        assert parse_version("1.2.3") == (1, 2, 3)
        assert parse_version("v10.20.30") == (10, 20, 30)

    def test_invalid_version_format(self):
        """Test handling of invalid version formats."""
        from src.git_handler import parse_version, InvalidVersionError

        with pytest.raises(InvalidVersionError):
            parse_version("invalid")

        with pytest.raises(InvalidVersionError):
            parse_version("v1.2")

    def test_commit_pdf_file(self, sample_git_repo: Path, temp_dir: Path):
        """Test committing PDF file to repository."""
        from src.git_handler import commit_file

        # Create a dummy PDF file
        pdf_path = sample_git_repo / "output.pdf"
        pdf_path.write_text("dummy pdf content")

        commit_file(sample_git_repo, pdf_path, "Add generated PDF")

        # Check that file was committed
        result = subprocess.run(
            ["git", "log", "--oneline", "-1"],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        assert "Add generated PDF" in result.stdout
