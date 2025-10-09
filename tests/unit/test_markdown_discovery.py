"""Unit tests for markdown file discovery and ordering."""
import pytest
from pathlib import Path


class TestMarkdownDiscovery:
    """Test markdown file discovery functionality."""

    def test_discover_markdown_files(self, sample_markdown_files: Path):
        """Test that all markdown files are discovered."""
        # Import the function to test (will be implemented)
        from src.markdown_processor import discover_markdown_files

        files = discover_markdown_files(sample_markdown_files)
        assert len(files) == 4
        assert all(f.suffix == '.md' for f in files)

    def test_numeric_prefix_ordering(self, sample_markdown_files: Path):
        """Test that files are ordered by numeric prefix."""
        from src.markdown_processor import discover_markdown_files

        files = discover_markdown_files(sample_markdown_files)
        filenames = [f.name for f in files]

        # Files should be ordered: 01, 02, 03, 10
        assert filenames[0].startswith('01-')
        assert filenames[1].startswith('02-')
        assert filenames[2].startswith('03-')
        assert filenames[3].startswith('10-')

    def test_numeric_prefix_extraction(self):
        """Test extracting numeric prefix from filename."""
        from src.markdown_processor import extract_numeric_prefix

        assert extract_numeric_prefix("01-intro.md") == 1
        assert extract_numeric_prefix("02-chapter.md") == 2
        assert extract_numeric_prefix("10-advanced.md") == 10
        assert extract_numeric_prefix("100-appendix.md") == 100

    def test_invalid_filename_handling(self, temp_dir: Path):
        """Test handling of files without numeric prefix."""
        from src.markdown_processor import discover_markdown_files

        markdown_dir = temp_dir / "markdown"
        markdown_dir.mkdir()

        # Create files with and without numeric prefix
        (markdown_dir / "01-valid.md").write_text("# Valid")
        (markdown_dir / "invalid.md").write_text("# Invalid")
        (markdown_dir / "README.md").write_text("# README")

        files = discover_markdown_files(markdown_dir)

        # Should only include files with numeric prefix
        assert len(files) == 1
        assert files[0].name == "01-valid.md"

    def test_empty_directory(self, temp_dir: Path):
        """Test handling of empty directory."""
        from src.markdown_processor import discover_markdown_files

        empty_dir = temp_dir / "empty"
        empty_dir.mkdir()

        files = discover_markdown_files(empty_dir)
        assert len(files) == 0

    def test_nested_directories_ignored(self, temp_dir: Path):
        """Test that nested directories are ignored."""
        from src.markdown_processor import discover_markdown_files

        markdown_dir = temp_dir / "markdown"
        markdown_dir.mkdir()
        nested_dir = markdown_dir / "nested"
        nested_dir.mkdir()

        (markdown_dir / "01-root.md").write_text("# Root")
        (nested_dir / "02-nested.md").write_text("# Nested")

        files = discover_markdown_files(markdown_dir)

        # Should only find root-level files
        assert len(files) == 1
        assert files[0].name == "01-root.md"
