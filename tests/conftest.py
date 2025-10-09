"""Pytest configuration and shared fixtures."""
import os
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_markdown_files(temp_dir: Path) -> Path:
    """Create sample markdown files with numeric prefixes for testing."""
    markdown_dir = temp_dir / "markdown"
    markdown_dir.mkdir()

    # Create sample files with proper numeric ordering
    files = {
        "01-introduction.md": """# Introduction

This is the introduction to Corona Digital CX.

## Overview
Corona Digital CX is a comprehensive guide.
""",
        "02-getting-started.md": """# Getting Started

## Installation
Follow these steps to install.

### Prerequisites
- Python 3.13+
- Git
""",
        "03-configuration.md": """# Configuration

## Basic Setup
Configure your environment.

```python
config = {
    "version": "1.0.0"
}
```
""",
        "10-advanced-topics.md": """# Advanced Topics

## Performance Optimization
Advanced techniques for optimization.

| Feature | Status |
|---------|--------|
| Caching | ✓ |
| Async   | ✓ |
""",
    }

    for filename, content in files.items():
        (markdown_dir / filename).write_text(content)

    return markdown_dir


@pytest.fixture
def sample_git_repo(temp_dir: Path) -> Path:
    """Create a sample git repository for testing."""
    repo_dir = temp_dir / "repo"
    repo_dir.mkdir()

    # Initialize git repo
    os.chdir(repo_dir)
    os.system("git init")
    os.system('git config user.email "test@example.com"')
    os.system('git config user.name "Test User"')

    # Create initial commit
    (repo_dir / "README.md").write_text("# Test Repo")
    os.system("git add .")
    os.system('git commit -m "Initial commit"')

    return repo_dir


@pytest.fixture
def license_text() -> str:
    """Return the Creative Commons license text."""
    return """This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
"""
