# Quick Start Guide

Get up and running with the Corona Digital CX Documentation Build System in minutes.

## Installation

### Prerequisites
- Python 3.13+
- uv package manager

### Install

```bash
# Clone repository
git clone <repo-url>
cd corona-digital-cx

# Install dependencies
uv sync

# Verify installation
mdoc-validate
```

## Basic Usage

### Build Documentation

```bash
# Build both PDF and HTML
mdoc-build

# Build with verbose output
mdoc-build --verbose

# Build only PDF
mdoc-build --pdf --no-html
```

Output files will be in the `dist/` directory.

### Create Release

```bash
# Create patch release (0.0.x)
mdoc-release

# Create minor release (0.x.0)
mdoc-release --bump minor

# Create major release (x.0.0)
mdoc-release --bump major

# Push to remote
mdoc-release --push
```

### Validate

```bash
# Check configuration and sources
mdoc-validate
```

## Writing Documentation

1. Create markdown files in `docs/sections/`
2. Use numeric prefixes: `01-intro.md`, `02-chapter.md`
3. Write content using standard markdown
4. Run `mdoc-build` to generate outputs

### Example File Structure

```
docs/
  sections/
    01-introduction.md
    02-installation.md
    03-usage.md
    04-advanced.md
  assets/
    images/
      screenshot.png
```

## Configuration

Edit `config/build.yaml` to customize:
- Project metadata (name, author, version)
- PDF settings (page size, margins)
- Output directories
- Markdown extensions

## Next Steps

- Read the full documentation in `dist/documentation.pdf`
- Customize `config/templates/pdf_style.css` for styling
- Add your own markdown sections
- Create your first release

## Troubleshooting

### WeasyPrint Installation Issues

**macOS:**
```bash
brew install pango cairo gdk-pixbuf
```

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-dev libpango1.0-dev libcairo2-dev
```

### Command Not Found

If `mdoc-build` is not found:

```bash
# Activate virtual environment
source .venv/bin/activate

# Or use uv run
uv run mdoc-build
```

### Validation Errors

Run validation to check for issues:
```bash
mdoc-validate
```

Common issues:
- Missing source directory
- Empty markdown files
- Broken image references

## Getting Help

- Check the full documentation
- Review example sections in `docs/sections/`
- Examine configuration in `config/build.yaml`
