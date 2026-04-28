# Quickstart For Contributors

This guide is for people joining the project and trying to make their first useful change.

## What You Need

- Python 3.13+
- `uv`
- system packages required by WeasyPrint if you want to build PDF output

## Clone And Install

```bash
git clone https://github.com/ACE-IoT-Solutions/corona-digital-cx.git
cd corona-digital-cx
uv sync
uv run mdoc-validate
```

## First Places To Read

1. [`README.md`](../README.md)
2. [`../CONTRIBUTING.md`](../CONTRIBUTING.md)
3. the relevant folder in `standard/sections/`

## Common Tasks

### Edit The Standard

Make text changes in `standard/sections/`.

After editing:

```bash
uv run mdoc-validate
uv run mdoc-build --pdf --html
```

### Work On Build Tooling

If you are changing the compiler, templates, or release process, start with:

- `src/`
- `config/build.yaml`
- [`ARCHITECTURE.md`](./ARCHITECTURE.md)

Then run:

```bash
uv run pytest
uv run mdoc-build --pdf --html
```

## Output

Build artifacts are generated in `dist/`.

## Platform Dependencies

### macOS

```bash
brew install pango cairo gdk-pixbuf
```

### Ubuntu/Debian

```bash
sudo apt-get install python3-dev libpango1.0-dev libcairo2-dev
```

## Troubleshooting

If the CLI commands are not on your path, run them through `uv`:

```bash
uv run mdoc-validate
uv run mdoc-build --pdf --html
```

If validation fails, check for:

- broken links or image paths
- malformed markdown structure
- empty or misplaced section files
