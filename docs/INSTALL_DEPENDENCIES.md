# System Dependencies Installation

The Corona Digital CX Documentation Build System requires WeasyPrint for PDF generation, which depends on system libraries.

## macOS Installation

Install dependencies using Homebrew:

```bash
brew install pango cairo gdk-pixbuf
```

Then sync Python packages:

```bash
uv sync
```

## Ubuntu/Debian Installation

Install system packages:

```bash
sudo apt-get update
sudo apt-get install -y \
    python3-dev \
    libpango1.0-dev \
    libcairo2-dev \
    libgdk-pixbuf2.0-dev \
    shared-mime-info
```

Then sync Python packages:

```bash
uv sync
```

## Windows Installation

WeasyPrint on Windows includes GTK3 libraries in the wheel package, so no additional installation is needed:

```bash
uv sync
```

## Verification

After installation, verify the setup:

```bash
uv run mdoc-validate
```

This should report no errors and show:
- Configuration valid
- Directories found
- Markdown files discovered
- No validation issues

## Troubleshooting

### "cannot load library libpango-1.0-0"

This means Pango is not installed or not in the library path.

**macOS:**
```bash
brew install pango
# If already installed, try reinstalling:
brew reinstall pango
```

**Linux:**
```bash
sudo apt-get install libpango1.0-dev
sudo ldconfig
```

### "command not found: mdoc-build"

Entry points are not installed. Options:

1. Use `uv run`:
   ```bash
   uv run mdoc-build
   ```

2. Activate virtual environment:
   ```bash
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   mdoc-build
   ```

### "No markdown files found"

Ensure you have markdown files in `docs/sections/`:
```bash
ls docs/sections/
```

If empty, add some markdown files or use the example sections created during installation.

## Quick Test

After installing dependencies, run this quick test:

```bash
# Validate setup
uv run mdoc-validate

# Build documentation
uv run mdoc-build --verbose

# Check output
ls -lh dist/
```

You should see `documentation.pdf` and `documentation.html` in the `dist/` directory.
