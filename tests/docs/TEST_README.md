# Test Suite Documentation

## Overview

This test suite provides comprehensive coverage for the Corona Digital CX build system, ensuring all requirements are met and the system behaves correctly under various conditions.

## Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Pytest configuration and shared fixtures
├── fixtures/                # Test data and sample files
│   └── markdown/            # Sample markdown files for testing
├── unit/                    # Unit tests for individual components
│   ├── test_markdown_discovery.py
│   ├── test_pdf_generation.py
│   ├── test_git_operations.py
│   └── test_config.py
├── integration/             # Integration tests for complete workflows
│   ├── test_build_workflow.py
│   ├── test_release_automation.py
│   ├── test_error_handling.py
│   └── test_requirements_validation.py
└── docs/                    # Test documentation
    └── TEST_README.md       # This file
```

## Test Categories

### Unit Tests (tests/unit/)

Tests for individual components in isolation:

#### 1. Markdown Discovery (`test_markdown_discovery.py`)
- File discovery in markdown directory
- Numeric prefix extraction and ordering
- Invalid filename handling
- Empty directory handling
- Nested directory exclusion

#### 2. PDF Generation (`test_pdf_generation.py`)
- Markdown file combination
- License text addition
- Markdown to PDF conversion
- Code block rendering
- Table rendering
- Output filename formatting
- PDF metadata

#### 3. Git Operations (`test_git_operations.py`)
- Git tag creation
- Annotated tags with messages
- Version retrieval from tags
- Version incrementing (major/minor/patch)
- Duplicate tag handling
- Version string parsing
- File commits

#### 4. Configuration (`test_config.py`)
- Configuration file loading
- Default values
- Configuration validation
- Version format validation
- Path resolution

### Integration Tests (tests/integration/)

Tests for complete workflows and system behavior:

#### 1. Build Workflow (`test_build_workflow.py`)
- Complete build process (markdown → PDF)
- License inclusion in build
- File ordering in final output
- Invalid directory handling
- Output directory creation
- Empty markdown directory handling
- Incremental builds

#### 2. Release Automation (`test_release_automation.py`)
- Full release workflow (build + tag)
- Version auto-increment
- Changelog generation
- Release rollback on failure
- Custom tag messages

#### 3. Error Handling (`test_error_handling.py`)
- Missing required directories
- Permission denied scenarios
- Corrupted markdown files
- Git errors (non-git repositories)
- Concurrent build attempts
- Invalid version formats
- Large markdown files

#### 4. Requirements Validation (`test_requirements_validation.py`)
- **Numeric prefix ordering**: Verifies files are ordered correctly (01-, 02-, 10-, etc.)
- **PDF output**: Validates proper PDF format
- **Creative Commons license**: Ensures CC-BY-SA 4.0 license is included
- **Git tag creation**: Confirms tags are created properly
- **Version format**: Enforces semantic versioning (X.Y.Z)
- **Markdown conversion**: Tests various markdown features (headings, lists, code, tables)
- **File naming convention**: Validates output filename format
- **Reproducible builds**: Tests build consistency
- **Edge case handling**: Validates error handling
- **Comprehensive system validation**: End-to-end workflow test

## Running the Tests

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test Category
```bash
# Unit tests only
pytest tests/unit/

# Integration tests only
pytest tests/integration/

# Requirements validation only
pytest tests/integration/test_requirements_validation.py
```

### Run Specific Test File
```bash
pytest tests/unit/test_markdown_discovery.py
```

### Run Specific Test
```bash
pytest tests/unit/test_markdown_discovery.py::TestMarkdownDiscovery::test_numeric_prefix_ordering
```

### Run with Coverage Report
```bash
pytest tests/ --cov=src --cov-report=html --cov-report=term
```

### Run with Verbose Output
```bash
pytest tests/ -v
```

### Run with Test Duration Report
```bash
pytest tests/ --durations=10
```

## Test Coverage Goals

- **Statements**: >80%
- **Branches**: >75%
- **Functions**: >80%
- **Lines**: >80%

## Test Fixtures

Located in `conftest.py`:

- `temp_dir`: Temporary directory for test operations
- `sample_markdown_files`: Sample markdown files with numeric prefixes
- `sample_git_repo`: Git repository initialized for testing
- `license_text`: Creative Commons license text

## Test Data

Sample markdown files in `tests/fixtures/markdown/`:
- `01-sample.md`: Basic markdown with headings and subsections
- `02-sample.md`: Markdown with code blocks and tables

## Writing New Tests

### Test Naming Convention
- Test files: `test_<module_name>.py`
- Test classes: `Test<FeatureName>`
- Test methods: `test_<specific_behavior>`

### Example Test Structure
```python
class TestFeatureName:
    """Test description."""

    def test_specific_behavior(self, fixture_name):
        """Test that specific behavior works correctly."""
        # Arrange
        input_data = "test input"

        # Act
        result = function_to_test(input_data)

        # Assert
        assert result == expected_output
```

### Using Fixtures
```python
def test_with_temp_directory(self, temp_dir: Path):
    """Test using temporary directory fixture."""
    test_file = temp_dir / "test.txt"
    test_file.write_text("content")
    assert test_file.exists()
```

## Continuous Integration

Tests should be run in CI/CD pipeline:

```yaml
# Example GitHub Actions workflow
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.13'
      - run: pip install -e ".[dev]"
      - run: pytest tests/ --cov=src --cov-report=xml
      - uses: codecov/codecov-action@v2
```

## Expected Test Results

Before implementation exists:
```
All tests will fail with ImportError since modules don't exist yet.
This is expected - tests are written first (TDD approach).
```

After implementation:
```
Expected: ~60+ tests passing
Coverage: >80% for all metrics
Duration: <30 seconds for full suite
```

## Test-Driven Development Workflow

1. **Red**: Write failing tests that define requirements
2. **Green**: Implement minimum code to make tests pass
3. **Refactor**: Improve code while keeping tests green

## Known Issues / TODOs

- [ ] PDF text extraction requires implementation of `extract_pdf_text()` utility
- [ ] Some tests require actual PDF library (PyPDF2 or similar)
- [ ] Reproducible build test may need timestamp handling
- [ ] Permission tests may behave differently on Windows
- [ ] Large file test could be optimized for faster execution

## Test Maintenance

- Review tests when requirements change
- Update fixtures when input format changes
- Add regression tests for bugs
- Remove obsolete tests
- Keep test documentation up to date

## Contact

For questions about the test suite, contact the QA team or refer to the main project documentation.
