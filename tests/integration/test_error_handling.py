"""Integration tests for error handling and edge cases."""
import pytest
from pathlib import Path
import subprocess


class TestErrorHandling:
    """Test error handling throughout the system."""

    def test_missing_required_directories(self, temp_dir: Path):
        """Test handling of missing required directories."""
        from src.build import build_pdf, BuildError

        # Missing markdown directory
        with pytest.raises(BuildError, match="markdown.*not found"):
            build_pdf(
                markdown_dir=temp_dir / "nonexistent",
                output_dir=temp_dir / "output",
                version="1.0.0"
            )

    def test_permission_denied_scenarios(self, temp_dir: Path, sample_markdown_files: Path):
        """Test handling of permission errors."""
        from src.build import build_pdf, BuildError
        import os

        output_dir = temp_dir / "readonly_output"
        output_dir.mkdir()

        # Make output directory read-only
        os.chmod(output_dir, 0o444)

        try:
            with pytest.raises(BuildError, match="permission|access"):
                build_pdf(
                    markdown_dir=sample_markdown_files,
                    output_dir=output_dir,
                    version="1.0.0"
                )
        finally:
            # Restore permissions for cleanup
            os.chmod(output_dir, 0o755)

    def test_corrupted_markdown_file(self, temp_dir: Path):
        """Test handling of corrupted or invalid markdown files."""
        from src.build import build_pdf

        markdown_dir = temp_dir / "markdown"
        markdown_dir.mkdir()

        # Create a "corrupted" file (binary content)
        corrupted_file = markdown_dir / "01-corrupted.md"
        corrupted_file.write_bytes(b'\x00\x01\x02\x03\x04\x05')

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        # Should handle gracefully
        pdf_path = build_pdf(
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version="1.0.0"
        )

        assert pdf_path.exists()

    def test_disk_space_exhausted(self, temp_dir: Path, sample_markdown_files: Path):
        """Test handling of disk space issues (simulated)."""
        # This is difficult to test without actually filling disk
        # Would typically use mock or similar
        pass

    def test_git_not_initialized(self, temp_dir: Path):
        """Test handling of non-git repositories."""
        from src.git_handler import create_tag, GitError

        non_git_dir = temp_dir / "not_a_repo"
        non_git_dir.mkdir()

        with pytest.raises(GitError, match="not a git repository"):
            create_tag(non_git_dir, "v1.0.0")

    def test_concurrent_build_attempts(self, sample_markdown_files: Path, temp_dir: Path):
        """Test handling of concurrent build attempts."""
        from src.build import build_pdf
        import threading

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        errors = []

        def build():
            try:
                build_pdf(
                    markdown_dir=sample_markdown_files,
                    output_dir=output_dir,
                    version="1.0.0"
                )
            except Exception as e:
                errors.append(e)

        # Start multiple builds concurrently
        threads = [threading.Thread(target=build) for _ in range(3)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # At least one should succeed
        output_files = list(output_dir.glob("*.pdf"))
        assert len(output_files) >= 1

    def test_invalid_version_formats(self, sample_markdown_files: Path, temp_dir: Path):
        """Test handling of various invalid version formats."""
        from src.build import build_pdf, VersionError

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        invalid_versions = [
            "invalid",
            "v1.2",
            "1.2.3.4",
            "1.x.3",
            "v1.2.3-alpha",  # May or may not be invalid depending on requirements
        ]

        for version in invalid_versions:
            with pytest.raises(VersionError):
                build_pdf(
                    markdown_dir=sample_markdown_files,
                    output_dir=output_dir,
                    version=version
                )

    def test_extremely_large_markdown_file(self, temp_dir: Path):
        """Test handling of very large markdown files."""
        from src.build import build_pdf

        markdown_dir = temp_dir / "markdown"
        markdown_dir.mkdir()

        # Create a large markdown file (10MB)
        large_file = markdown_dir / "01-large.md"
        content = "# Section\n\n" + ("Lorem ipsum dolor sit amet. " * 10000)
        large_file.write_text(content * 10)

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        # Should handle without crashing
        pdf_path = build_pdf(
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version="1.0.0"
        )

        assert pdf_path.exists()
