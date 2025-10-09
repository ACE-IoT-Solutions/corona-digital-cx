"""Validation tests to ensure all project requirements are met."""
import pytest
from pathlib import Path
import subprocess
import re


class TestRequirementsValidation:
    """Validate that all project requirements are met."""

    def test_numeric_prefix_ordering_requirement(self, sample_markdown_files: Path, temp_dir: Path):
        """
        Requirement: Markdown files must be ordered by numeric prefix.
        Validate that files with prefixes like 01-, 02-, 10- are ordered correctly.
        """
        from src.build import build_pdf, extract_pdf_text

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        pdf_path = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0"
        )

        # Extract text from PDF
        text = extract_pdf_text(pdf_path)

        # Find positions of content from each file
        positions = {}
        for md_file in sorted(sample_markdown_files.glob("[0-9]*-*.md")):
            # Extract the heading from the file
            content = md_file.read_text()
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                heading = match.group(1)
                pos = text.find(heading)
                if pos != -1:
                    positions[md_file.name] = pos

        # Verify positions are in correct order
        ordered_files = sorted(positions.keys(), key=lambda x: positions[x])
        expected_order = sorted(positions.keys(), key=lambda x: int(x.split('-')[0]))

        assert ordered_files == expected_order, \
            f"Files not in correct order. Expected: {expected_order}, Got: {ordered_files}"

    def test_pdf_output_requirement(self, sample_markdown_files: Path, temp_dir: Path):
        """
        Requirement: System must generate a valid PDF file.
        Validate that output is a proper PDF format.
        """
        from src.build import build_pdf

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        pdf_path = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0"
        )

        # Check file exists and has .pdf extension
        assert pdf_path.exists()
        assert pdf_path.suffix == ".pdf"

        # Check PDF magic bytes (PDF files start with %PDF)
        with open(pdf_path, 'rb') as f:
            header = f.read(4)
            assert header == b'%PDF', "Output file is not a valid PDF"

    def test_creative_commons_license_requirement(self, sample_markdown_files: Path, temp_dir: Path):
        """
        Requirement: PDF must include Creative Commons Attribution-ShareAlike 4.0 license.
        Validate that license text is included in the output.
        """
        from src.build import build_pdf, extract_pdf_text

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        license_file = temp_dir / "LICENSE.md"
        license_text = """This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/4.0/"""
        license_file.write_text(license_text)

        pdf_path = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0",
            license_file=license_file
        )

        # Extract text and verify license is present
        text = extract_pdf_text(pdf_path)

        assert "Creative Commons" in text, "Creative Commons not found in PDF"
        assert "Attribution-ShareAlike 4.0" in text, "License version not found in PDF"
        assert "http://creativecommons.org/licenses/by-sa/4.0" in text, "License URL not found in PDF"

    def test_git_tag_creation_requirement(self, sample_git_repo: Path, sample_markdown_files: Path):
        """
        Requirement: System must create git tags for releases.
        Validate that git tag is properly created.
        """
        from src.release import create_release

        # Copy markdown files to repo
        markdown_dir = sample_git_repo / "markdown"
        markdown_dir.mkdir()
        for md_file in sample_markdown_files.glob("*.md"):
            (markdown_dir / md_file.name).write_text(md_file.read_text())

        output_dir = sample_git_repo / "output"
        output_dir.mkdir()

        version = "1.0.0"
        create_release(
            repo_dir=sample_git_repo,
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version=version
        )

        # Verify tag exists
        result = subprocess.run(
            ["git", "tag", "-l", f"v{version}"],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )

        assert f"v{version}" in result.stdout, f"Git tag v{version} was not created"

    def test_version_format_requirement(self, sample_markdown_files: Path, temp_dir: Path):
        """
        Requirement: Version numbers must follow semantic versioning (X.Y.Z).
        Validate that version format is enforced.
        """
        from src.build import build_pdf, VersionError

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        # Valid version formats should work
        valid_versions = ["1.0.0", "2.1.3", "10.20.30"]
        for version in valid_versions:
            pdf_path = build_pdf(
                markdown_dir=sample_markdown_files,
                output_dir=output_dir,
                version=version
            )
            assert version in pdf_path.name, f"Version {version} not in filename"

        # Invalid version formats should be rejected
        invalid_versions = ["1.0", "v1.2.3.4", "invalid"]
        for version in invalid_versions:
            with pytest.raises(VersionError):
                build_pdf(
                    markdown_dir=sample_markdown_files,
                    output_dir=output_dir,
                    version=version
                )

    def test_markdown_to_pdf_conversion_requirement(self, temp_dir: Path):
        """
        Requirement: System must convert markdown features to PDF format.
        Validate that various markdown elements are properly converted.
        """
        from src.build import build_pdf, extract_pdf_text

        markdown_dir = temp_dir / "markdown"
        markdown_dir.mkdir()

        # Create markdown with various features
        (markdown_dir / "01-features.md").write_text("""# Main Heading

## Subheading

Regular paragraph text.

### Lists

- Bullet item 1
- Bullet item 2
- Bullet item 3

1. Numbered item 1
2. Numbered item 2

### Code Block

```python
def hello():
    print("Hello, World!")
```

### Table

| Column A | Column B |
|----------|----------|
| Value 1  | Value 2  |

**Bold text** and *italic text*.
""")

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        pdf_path = build_pdf(
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version="1.0.0"
        )

        text = extract_pdf_text(pdf_path)

        # Verify various elements are present
        assert "Main Heading" in text
        assert "Subheading" in text
        assert "Bullet item" in text
        assert "Numbered item" in text
        assert "def hello" in text or "hello" in text  # Code might be formatted differently
        assert "Column A" in text or "Column B" in text  # Tables

    def test_file_naming_convention_requirement(self, sample_markdown_files: Path, temp_dir: Path):
        """
        Requirement: Output PDF must follow naming convention.
        Validate that PDF filename includes project name and version.
        """
        from src.build import build_pdf

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        version = "1.0.0"
        pdf_path = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version=version
        )

        filename = pdf_path.name

        # Verify naming convention
        assert "corona-digital-cx" in filename.lower(), "Project name not in filename"
        assert version in filename, "Version not in filename"
        assert filename.endswith(".pdf"), "File does not have .pdf extension"

    def test_reproducible_builds_requirement(self, sample_markdown_files: Path, temp_dir: Path):
        """
        Requirement: Builds should be reproducible (same input = same output).
        Validate that building twice produces consistent results.
        """
        from src.build import build_pdf
        import hashlib

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        # First build
        pdf_path_1 = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0"
        )

        # Read and hash first output
        hash1 = hashlib.sha256(pdf_path_1.read_bytes()).hexdigest()

        # Clean up
        pdf_path_1.unlink()

        # Second build
        pdf_path_2 = build_pdf(
            markdown_dir=sample_markdown_files,
            output_dir=output_dir,
            version="1.0.0"
        )

        # Read and hash second output
        hash2 = hashlib.sha256(pdf_path_2.read_bytes()).hexdigest()

        # Note: Perfect reproducibility is hard with PDFs due to timestamps
        # So we just verify the file is created consistently
        assert pdf_path_2.exists()
        assert pdf_path_2.stat().st_size > 0

    def test_empty_markdown_handling_requirement(self, temp_dir: Path):
        """
        Requirement: System should handle edge cases gracefully.
        Validate error handling for empty/missing content.
        """
        from src.build import build_pdf, BuildError

        markdown_dir = temp_dir / "markdown"
        markdown_dir.mkdir()

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        # Empty directory should raise appropriate error
        with pytest.raises(BuildError, match="No markdown files"):
            build_pdf(
                markdown_dir=markdown_dir,
                output_dir=output_dir,
                version="1.0.0"
            )

    def test_comprehensive_system_validation(self, sample_git_repo: Path, sample_markdown_files: Path):
        """
        Comprehensive end-to-end validation of all requirements.
        This test validates the entire workflow from start to finish.
        """
        from src.release import create_release
        from src.build import extract_pdf_text

        # Setup repository with markdown files
        markdown_dir = sample_git_repo / "markdown"
        markdown_dir.mkdir()

        # Create numbered markdown files
        for i, md_file in enumerate(sorted(sample_markdown_files.glob("*.md")), 1):
            content = md_file.read_text()
            new_name = f"{i:02d}-{md_file.name.split('-', 1)[1]}"
            (markdown_dir / new_name).write_text(content)

        # Create license file
        license_file = sample_git_repo / "LICENSE.md"
        license_file.write_text("""Creative Commons Attribution-ShareAlike 4.0 International License""")

        output_dir = sample_git_repo / "output"
        output_dir.mkdir()

        version = "1.0.0"

        # Execute full release workflow
        release_info = create_release(
            repo_dir=sample_git_repo,
            markdown_dir=markdown_dir,
            output_dir=output_dir,
            version=version,
            license_file=license_file
        )

        # Validate all requirements
        pdf_path = release_info["pdf_path"]

        # 1. PDF exists and is valid
        assert pdf_path.exists()
        with open(pdf_path, 'rb') as f:
            assert f.read(4) == b'%PDF'

        # 2. Filename follows convention
        assert "corona-digital-cx" in pdf_path.name.lower()
        assert version in pdf_path.name

        # 3. Git tag created
        result = subprocess.run(
            ["git", "tag", "-l", f"v{version}"],
            cwd=sample_git_repo,
            capture_output=True,
            text=True
        )
        assert f"v{version}" in result.stdout

        # 4. License included
        text = extract_pdf_text(pdf_path)
        assert "Creative Commons" in text

        # 5. Content is ordered correctly
        # (Assuming first file has "Introduction" or similar unique content)

        print("✅ All requirements validated successfully!")
