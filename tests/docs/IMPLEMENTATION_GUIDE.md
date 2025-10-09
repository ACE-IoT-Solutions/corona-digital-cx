# Implementation Guide for Coder Agent

**From**: Tester Agent (Hive Mind Swarm)
**To**: Coder Agent
**Date**: 2025-10-09
**Status**: Ready for Implementation

---

## Quick Start

All tests have been created following TDD methodology. Your job is to make them pass!

### Run Tests While Implementing

```bash
# Watch mode - run tests automatically on file changes
pytest tests/ --lf --tb=short -v

# Run specific module tests
pytest tests/unit/test_markdown_discovery.py -v

# Check coverage
pytest tests/ --cov=src --cov-report=term-missing
```

---

## Implementation Priority Order

### Phase 1: Core Functionality (START HERE) 🔴

#### 1.1 Create Source Directory Structure
```bash
mkdir -p src
touch src/__init__.py
```

#### 1.2 Implement Markdown Processor (`src/markdown_processor.py`)

**Required API (from tests)**:
```python
from pathlib import Path
from typing import List

def discover_markdown_files(directory: Path) -> List[Path]:
    """
    Discover all markdown files with numeric prefixes in directory.

    Args:
        directory: Path to markdown directory

    Returns:
        List of markdown file paths, sorted by numeric prefix

    Example:
        >>> discover_markdown_files(Path("markdown"))
        [Path("markdown/01-intro.md"), Path("markdown/02-chapter.md")]
    """
    pass  # Implement me!

def extract_numeric_prefix(filename: str) -> int:
    """
    Extract numeric prefix from filename.

    Args:
        filename: Filename like "01-intro.md"

    Returns:
        Integer prefix (e.g., 1 for "01-intro.md")

    Raises:
        ValueError: If filename doesn't have numeric prefix

    Example:
        >>> extract_numeric_prefix("01-intro.md")
        1
        >>> extract_numeric_prefix("10-advanced.md")
        10
    """
    pass  # Implement me!
```

**Test it**:
```bash
pytest tests/unit/test_markdown_discovery.py -v
```

**Hints**:
- Use `Path.glob("*.md")` to find markdown files
- Use regex to extract numeric prefix: `r"^(\d+)-"`
- Sort files by the extracted number, not alphabetically
- Ignore files without numeric prefix
- Only process root-level files (not nested directories)

---

#### 1.3 Implement PDF Generator (`src/pdf_generator.py`)

**Required API**:
```python
from pathlib import Path
from typing import Optional, Dict

def combine_markdown_files(markdown_dir: Path) -> str:
    """
    Combine all markdown files in directory into one string.

    Args:
        markdown_dir: Directory containing markdown files

    Returns:
        Combined markdown content as string
    """
    pass  # Implement me!

def add_license(content: str, license_text: str) -> str:
    """
    Append license text to markdown content.

    Args:
        content: Markdown content
        license_text: License text to append

    Returns:
        Content with license appended
    """
    pass  # Implement me!

def markdown_to_pdf(
    markdown_content: str,
    output_path: Path,
    metadata: Optional[Dict[str, str]] = None
) -> None:
    """
    Convert markdown content to PDF.

    Args:
        markdown_content: Markdown text to convert
        output_path: Where to save PDF
        metadata: Optional metadata (title, author, subject)
    """
    pass  # Implement me!

def generate_output_filename(version: str) -> str:
    """
    Generate output filename for PDF.

    Args:
        version: Version string (e.g., "1.0.0")

    Returns:
        Filename like "corona-digital-cx-1.0.0.pdf"
    """
    pass  # Implement me!

def extract_pdf_text(pdf_path: Path) -> str:
    """
    Extract text from PDF file (for testing).

    Args:
        pdf_path: Path to PDF file

    Returns:
        Text content of PDF
    """
    pass  # Implement me!
```

**Test it**:
```bash
pytest tests/unit/test_pdf_generation.py -v
```

**Hints**:
- Use `markdown` library to parse markdown
- Use `weasyprint` for PDF generation (best for markdown → PDF)
- Or use `reportlab` + `markdown` (more control but complex)
- Use `PyPDF2` or `pdfplumber` for `extract_pdf_text()`
- Handle code blocks with `pygments` for syntax highlighting
- Use CSS to style the PDF output

**Example WeasyPrint approach**:
```python
import markdown
from weasyprint import HTML, CSS

def markdown_to_pdf(markdown_content, output_path, metadata=None):
    # Convert markdown to HTML
    html_content = markdown.markdown(
        markdown_content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )

    # Add HTML wrapper
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            pre {{ background: #f4f4f4; padding: 10px; }}
        </style>
    </head>
    <body>{html_content}</body>
    </html>
    """

    # Generate PDF
    HTML(string=full_html).write_pdf(output_path)
```

---

#### 1.4 Implement Build System (`src/build.py`)

**Required API**:
```python
from pathlib import Path

class BuildError(Exception):
    """Raised when build fails."""
    pass

class VersionError(Exception):
    """Raised for invalid version format."""
    pass

def build_pdf(
    markdown_dir: Path,
    output_dir: Path,
    version: str,
    license_file: Optional[Path] = None
) -> Path:
    """
    Build PDF from markdown files.

    Args:
        markdown_dir: Directory with markdown files
        output_dir: Where to save PDF
        version: Version string (X.Y.Z format)
        license_file: Optional license file to include

    Returns:
        Path to generated PDF

    Raises:
        BuildError: If build fails
        VersionError: If version format invalid
    """
    pass  # Implement me!
```

**Test it**:
```bash
pytest tests/integration/test_build_workflow.py -v
```

**Hints**:
- Validate version format: `r"^\d+\.\d+\.\d+$"`
- Create output_dir if it doesn't exist
- Use `discover_markdown_files()` to get files
- Use `combine_markdown_files()` to combine them
- Add license if provided
- Use `markdown_to_pdf()` to generate PDF
- Return the path to generated PDF

---

### Phase 2: Git Operations (NEXT) 🟡

#### 2.1 Implement Git Handler (`src/git_handler.py`)

**Required API**:
```python
from pathlib import Path
from typing import Tuple

class GitError(Exception):
    """Base class for git errors."""
    pass

class TagExistsError(GitError):
    """Raised when tag already exists."""
    pass

class InvalidVersionError(GitError):
    """Raised for invalid version format."""
    pass

def create_tag(
    repo_dir: Path,
    version: str,
    message: Optional[str] = None
) -> None:
    """Create git tag."""
    pass

def get_current_version(repo_dir: Path) -> str:
    """Get latest version tag."""
    pass

def increment_version(
    version: str,
    increment: str  # "major", "minor", or "patch"
) -> str:
    """Increment version number."""
    pass

def parse_version(version_string: str) -> Tuple[int, int, int]:
    """Parse version string to tuple."""
    pass

def commit_file(
    repo_dir: Path,
    file_path: Path,
    message: str
) -> None:
    """Commit file to repository."""
    pass
```

**Test it**:
```bash
pytest tests/unit/test_git_operations.py -v
```

**Hints**:
- Use `GitPython` library for git operations
- Or use `subprocess` to call git commands
- Check if tag exists before creating
- Parse version with regex: `r"v?(\d+)\.(\d+)\.(\d+)"`

---

#### 2.2 Implement Release Manager (`src/release.py`)

**Required API**:
```python
from pathlib import Path
from typing import Dict, Optional

class ReleaseError(Exception):
    """Raised when release fails."""
    pass

def create_release(
    repo_dir: Path,
    markdown_dir: Path,
    output_dir: Path,
    version: str,
    license_file: Optional[Path] = None,
    tag_message: Optional[str] = None,
    generate_changelog: bool = False
) -> Dict:
    """
    Create a full release.

    Returns:
        Dict with 'pdf_path', 'version', 'changelog' (if requested)
    """
    pass

def get_next_version(
    repo_dir: Path,
    increment: str = "patch"
) -> str:
    """Get next version number."""
    pass

def generate_changelog(repo_dir: Path) -> str:
    """Generate changelog from commits."""
    pass
```

**Test it**:
```bash
pytest tests/integration/test_release_automation.py -v
```

---

### Phase 3: Configuration & CLI (OPTIONAL) 🟢

#### 3.1 Configuration (`src/config.py`)

Basic config loading and validation. See tests for API.

#### 3.2 CLI Interface (`src/cli.py`)

Command-line interface using `click`:
```python
import click

@click.command()
@click.option("--version", required=True, help="Version number")
def build(version):
    """Build PDF from markdown files."""
    pass

@click.command()
def release():
    """Create a new release."""
    pass
```

---

## Running Tests

### Test Everything
```bash
pytest tests/ -v
```

### Test While Developing
```bash
# Run only failed tests from last run
pytest tests/ --lf -v

# Run tests matching a pattern
pytest tests/ -k "markdown" -v

# Stop at first failure
pytest tests/ -x
```

### Coverage
```bash
pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html
```

---

## Implementation Checklist

**Phase 1: Core** (Required)
- [ ] `src/__init__.py`
- [ ] `src/markdown_processor.py` (7 tests)
- [ ] `src/pdf_generator.py` (8 tests)
- [ ] `src/build.py` (7 tests)

**Phase 2: Git** (Important)
- [ ] `src/git_handler.py` (9 tests)
- [ ] `src/release.py` (6 tests)

**Phase 3: Extra** (Nice to have)
- [ ] `src/config.py` (6 tests)
- [ ] `src/cli.py`

**All Tests Passing**
- [ ] 56 tests pass
- [ ] Coverage >80%
- [ ] No linting errors: `ruff check src/`

---

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'src'"
**Solution**: Create `src/__init__.py`

### Issue: "ImportError: cannot import name 'X'"
**Solution**: Make sure function/class name matches exactly what tests expect

### Issue: PDF generation fails
**Solution**: Install WeasyPrint and its dependencies:
```bash
# macOS
brew install python-tk

# Install WeasyPrint
pip install weasyprint
```

### Issue: Tests pass but coverage is low
**Solution**: Add more edge case handling in your implementation

---

## Memory Coordination

Check what Tester Agent stored:
```bash
npx claude-flow@alpha memory query tests --namespace default
npx claude-flow@alpha memory query implementation --namespace default
```

Store your progress:
```bash
npx claude-flow@alpha memory store coder/status '{"phase": 1, "complete": ["markdown_processor"], "next": "pdf_generator"}'
```

---

## Questions?

Refer to:
1. **Test files** in `tests/` - They define exact API requirements
2. **Test documentation** in `tests/docs/TEST_README.md`
3. **Test report** in `tests/docs/TEST_REPORT.md`

---

## Success Criteria

You'll know you're done when:
```bash
pytest tests/
# All 56 tests passing ✅
# Coverage >80% ✅
# No errors ✅
```

Good luck! The tests are your guide - they tell you exactly what to build. 🚀

**Tester Agent, signing off.**
