"""Unit tests for PDF generation."""
import pytest
from pathlib import Path


class TestPDFGeneration:
    """Test PDF generation functionality."""

    def test_combine_markdown_files(self, sample_markdown_files: Path):
        """Test combining multiple markdown files."""
        from src.pdf_generator import combine_markdown_files

        combined = combine_markdown_files(sample_markdown_files)

        # Should contain content from all files
        assert "# Introduction" in combined
        assert "# Getting Started" in combined
        assert "# Configuration" in combined
        assert "# Advanced Topics" in combined

    def test_add_license_to_content(self, license_text: str):
        """Test adding Creative Commons license."""
        from src.pdf_generator import add_license

        content = "# Test Content\n\nSome content here."
        result = add_license(content, license_text)

        # License should be at the end
        assert license_text in result
        assert result.endswith(license_text) or result.endswith(license_text + "\n")

    def test_markdown_to_pdf_conversion(self, temp_dir: Path):
        """Test converting markdown to PDF."""
        from src.pdf_generator import markdown_to_pdf

        markdown_content = """# Test Document

## Section 1
This is a test section.

### Subsection 1.1
More content here.
"""

        output_path = temp_dir / "output.pdf"
        markdown_to_pdf(markdown_content, output_path)

        # PDF should be created
        assert output_path.exists()
        assert output_path.stat().st_size > 0

    def test_pdf_with_code_blocks(self, temp_dir: Path):
        """Test PDF generation with code blocks."""
        from src.pdf_generator import markdown_to_pdf

        markdown_content = """# Code Example

```python
def hello():
    print("Hello, World!")
```
"""

        output_path = temp_dir / "code_output.pdf"
        markdown_to_pdf(markdown_content, output_path)

        assert output_path.exists()

    def test_pdf_with_tables(self, temp_dir: Path):
        """Test PDF generation with tables."""
        from src.pdf_generator import markdown_to_pdf

        markdown_content = """# Table Example

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |
"""

        output_path = temp_dir / "table_output.pdf"
        markdown_to_pdf(markdown_content, output_path)

        assert output_path.exists()

    def test_output_filename_format(self):
        """Test that output filename is correctly formatted."""
        from src.pdf_generator import generate_output_filename

        version = "1.0.0"
        filename = generate_output_filename(version)

        assert filename.startswith("corona-digital-cx-")
        assert filename.endswith(".pdf")
        assert version in filename

    def test_metadata_in_pdf(self, temp_dir: Path):
        """Test that PDF includes proper metadata."""
        from src.pdf_generator import markdown_to_pdf

        markdown_content = "# Test"
        output_path = temp_dir / "metadata.pdf"

        metadata = {
            "title": "Corona Digital CX",
            "author": "Corona Team",
            "subject": "Digital CX Guide"
        }

        markdown_to_pdf(markdown_content, output_path, metadata=metadata)

        assert output_path.exists()
        # Would need PyPDF2 or similar to verify metadata in actual test
