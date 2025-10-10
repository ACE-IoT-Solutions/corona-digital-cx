"""Markdown processing and file discovery."""

import re
from pathlib import Path
from typing import List, Tuple

import markdown
from markdown.extensions import Extension

from .config import BuildConfig


class MarkdownProcessor:
    """Processes markdown files for documentation build."""

    def __init__(self, config: BuildConfig):
        """
        Initialize markdown processor.

        Args:
            config: Build configuration
        """
        self.config = config
        self._md = markdown.Markdown(
            extensions=config.markdown_extensions,
            extension_configs=config.extension_configs,
            output_format="html5",
        )

    def discover_files(self) -> List[Path]:
        """
        Discover all markdown files in source directory.

        Files are sorted by:
        1. Folder path with numeric prefixes (e.g., 01-intro/, 02-setup/)
        2. File name with numeric prefixes within each folder

        Returns:
            List of markdown file paths in order
        """
        source_dir = self.config.source_dir

        if not source_dir.exists():
            raise FileNotFoundError(f"Source directory not found: {source_dir}")

        # Find all markdown files
        md_files = list(source_dir.glob("**/*.md"))

        if not md_files:
            raise ValueError(f"No markdown files found in: {source_dir}")

        # Sort by full path hierarchy, extracting numeric prefixes at each level
        def sort_key(path: Path) -> Tuple:
            # Get relative path from source directory
            rel_path = path.relative_to(source_dir)

            # Split into parts (folders and filename)
            parts = list(rel_path.parts)

            # Create sort key for each part (folder or file)
            sort_parts = []
            for part in parts:
                # Try to extract leading number
                match = re.match(r"^(\d+)", part)
                if match:
                    # (numeric_value, original_string)
                    sort_parts.append((int(match.group(1)), part))
                else:
                    # Files/folders without numbers sort last
                    sort_parts.append((999999, part))

            return tuple(sort_parts)

        sorted_files = sorted(md_files, key=sort_key)

        return sorted_files

    def remove_license_footer(self, content: str) -> str:
        """
        Remove CC license footer from individual file content.

        Args:
            content: Markdown content

        Returns:
            Content with license footer removed
        """
        # Pattern to match the standard CC license footer
        # Matches the horizontal rule and license notice at the end of files
        pattern = r'\n---\n\n\*This document is part of.*?licensed under.*?\*\s*$'

        # Remove the footer
        cleaned = re.sub(pattern, '', content, flags=re.DOTALL | re.MULTILINE)

        return cleaned.rstrip()

    def combine_files(self, files: List[Path]) -> str:
        """
        Combine multiple markdown files into single document.

        Args:
            files: List of markdown file paths

        Returns:
            Combined markdown content
        """
        combined = []

        for file_path in files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Remove CC license footer from individual files
            content = self.remove_license_footer(content)

            # Add file separator comment
            combined.append(f"<!-- Source: {file_path.name} -->")
            combined.append(content)
            combined.append("")  # Empty line between files

        return "\n".join(combined)

    def process_images(self, content: str) -> str:
        """
        Process image references to use absolute paths.

        Args:
            content: Markdown content

        Returns:
            Content with processed image paths
        """
        assets_dir = self.config.assets_dir

        # Pattern to match markdown images: ![alt](path)
        pattern = r"!\[([^\]]*)\]\(([^)]+)\)"

        def replace_image(match):
            alt_text = match.group(1)
            img_path = match.group(2)

            # Skip if already absolute or URL
            if img_path.startswith(("http://", "https://", "/")):
                return match.group(0)

            # Convert relative path to absolute
            full_path = assets_dir / img_path
            if full_path.exists():
                return f"![{alt_text}]({full_path.as_posix()})"

            # Return original if file not found (will be caught in validation)
            return match.group(0)

        return re.sub(pattern, replace_image, content)

    def add_metadata_header(self, content: str) -> str:
        """
        Add project metadata to beginning of document.

        Args:
            content: Markdown content

        Returns:
            Content with metadata header
        """
        header = f"""---
title: {self.config.project_name}
author: {self.config.project_author}
version: {self.config.project_version}
license: {self.config.project_license}
---

"""
        return header + content

    def convert_to_html(self, markdown_content: str) -> str:
        """
        Convert markdown to HTML.

        Args:
            markdown_content: Markdown text

        Returns:
            HTML content
        """
        # Reset markdown processor for fresh conversion
        self._md.reset()

        html = self._md.convert(markdown_content)
        return html

    def add_license_footer(self, content: str) -> str:
        """
        Add final CC license footer to complete document.

        Args:
            content: Markdown content

        Returns:
            Content with license footer appended
        """
        footer = """

---

## License

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

**You are free to:**
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license
"""
        return content + footer

    def build_complete_document(self) -> Tuple[str, str]:
        """
        Build complete document from all source files.

        Returns:
            Tuple of (markdown_content, html_content)
        """
        # Discover and combine files
        files = self.discover_files()
        markdown_content = self.combine_files(files)

        # Process images
        markdown_content = self.process_images(markdown_content)

        # Add metadata
        markdown_content = self.add_metadata_header(markdown_content)

        # Add final license footer
        markdown_content = self.add_license_footer(markdown_content)

        # Convert to HTML
        html_content = self.convert_to_html(markdown_content)

        return markdown_content, html_content

    def get_file_count(self) -> int:
        """Get number of markdown files in source directory."""
        try:
            return len(self.discover_files())
        except (FileNotFoundError, ValueError):
            return 0
