"""Integration tests for complete build workflow."""
import pytest
from pathlib import Path
import subprocess


class TestBuildWorkflow:
    """Test the complete build process from markdown to PDF."""

    def test_full_build_process(self, sample_markdown_files: Path, temp_dir: Path):
        """Test complete build from markdown files to PDF."""
        from src.build import build_pdf

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        pdf_path = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0"
        )

        # Verify PDF was created
        assert pdf_path.exists()
        assert pdf_path.suffix == ".pdf"
        assert pdf_path.stat().st_size > 0

    def test_build_with_license(self, sample_markdown_files: Path, temp_dir: Path):
        """Test that build includes Creative Commons license."""
        from src.build import build_pdf

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        # Create license file
        license_file = temp_dir / "LICENSE.md"
        license_file.write_text("Creative Commons Attribution-ShareAlike 4.0")

        pdf_path = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0",
            license_file=license_file
        )

        assert pdf_path.exists()
        # Would need to extract PDF text to verify license inclusion

    def test_build_respects_file_order(self, sample_markdown_files: Path, temp_dir: Path):
        """Test that files are combined in correct numeric order."""
        from src.build import build_pdf, extract_pdf_text

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        pdf_path = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0"
        )

        # Extract text and verify order
        text = extract_pdf_text(pdf_path)

        # Content should appear in order: 01, 02, 03, 10
        intro_pos = text.find("Introduction")
        getting_started_pos = text.find("Getting Started")
        config_pos = text.find("Configuration")
        advanced_pos = text.find("Advanced Topics")

        assert intro_pos < getting_started_pos < config_pos < advanced_pos

    def test_build_with_invalid_markdown_dir(self, temp_dir: Path):
        """Test error handling for invalid markdown directory."""
        from src.build import build_pdf, BuildError

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        nonexistent_dir = temp_dir / "nonexistent"

        with pytest.raises(BuildError):
            build_pdf(
                markdown_dir=nonexistent_dir,
                output_dir=output_dir,
                version="1.0.0"
            )

    def test_build_creates_output_directory(self, sample_markdown_files: Path, temp_dir: Path):
        """Test that build creates output directory if it doesn't exist."""
        from src.build import build_pdf

        output_dir = temp_dir / "new_output"
        assert not output_dir.exists()

        pdf_path = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0"
        )

        assert output_dir.exists()
        assert pdf_path.exists()

    def test_build_with_empty_markdown_dir(self, temp_dir: Path):
        """Test handling of empty markdown directory."""
        from src.build import build_pdf, BuildError

        empty_dir = temp_dir / "empty"
        empty_dir.mkdir()

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        with pytest.raises(BuildError, match="No markdown files found"):
            build_pdf(
                markdown_dir=empty_dir,
                output_dir=output_dir,
                version="1.0.0"
            )

    def test_incremental_build(self, sample_markdown_files: Path, temp_dir: Path):
        """Test that rebuilding works correctly."""
        from src.build import build_pdf

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        # First build
        pdf_path_1 = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0"
        )
        first_mtime = pdf_path_1.stat().st_mtime

        # Modify a markdown file
        import time
        time.sleep(0.1)
        markdown_file = list(sample_markdown_files.glob("*.md"))[0]
        content = markdown_file.read_text()
        markdown_file.write_text(content + "\n\nNew content added")

        # Second build
        pdf_path_2 = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.1"
        )

        # Should create new file with different version
        assert pdf_path_1 != pdf_path_2
        assert "1.0.1" in pdf_path_2.name
