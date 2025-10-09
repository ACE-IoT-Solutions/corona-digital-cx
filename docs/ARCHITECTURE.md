# System Architecture

## Overview

The Corona Digital CX Documentation Build System is a Python-based tool that converts markdown documentation into professional PDF and HTML outputs, with integrated version control and release automation.

## Components

### 1. Configuration Management (`src/builder/config.py`)

**Purpose**: Centralized configuration loading and validation

**Key Classes**:
- `BuildConfig`: YAML-based configuration with property accessors

**Features**:
- Dot-notation key access
- Path resolution (relative to absolute)
- Type-safe property getters
- Default value handling

**Configuration File**: `config/build.yaml`
- Project metadata
- Build settings
- PDF options
- Markdown extensions
- Release automation

### 2. Markdown Processing (`src/builder/markdown_processor.py`)

**Purpose**: Discover, combine, and process markdown files

**Key Classes**:
- `MarkdownProcessor`: Markdown file handling and conversion

**Features**:
- **File Discovery**: Finds all `.md` files in source directory
- **Intelligent Sorting**: Uses numeric prefixes (01-, 02-) for ordering
- **File Combination**: Merges multiple files with source comments
- **Image Processing**: Resolves relative image paths
- **Metadata Injection**: Adds frontmatter (title, author, version)
- **HTML Conversion**: Markdown to HTML with extensions

**Supported Extensions**:
- Code highlighting
- Tables
- Task lists
- Table of contents
- Fenced code blocks
- Magic links

### 3. PDF Generation (`src/builder/pdf_generator.py`)

**Purpose**: Convert HTML to styled PDF documents

**Key Classes**:
- `PDFGenerator`: PDF/HTML generation with styling

**Features**:
- **Cover Page**: Templated cover with metadata
- **Styling**: CSS-based PDF styling via WeasyPrint
- **Table of Contents**: Auto-generated from headings
- **Page Numbers**: Header/footer with page numbering
- **Syntax Highlighting**: Code blocks with Pygments
- **Image Optimization**: Proper image handling and sizing

**Templates**:
- `config/templates/cover.html` - Cover page template
- `config/templates/pdf_style.css` - PDF styling

**Output Formats**:
- PDF (via WeasyPrint)
- Standalone HTML (with inline CSS)

### 4. Release Management (`src/builder/release_manager.py`)

**Purpose**: Git-based version control and release automation

**Key Classes**:
- `ReleaseManager`: Git operations and version management

**Features**:
- **Version Management**:
  - Semantic versioning (major.minor.patch)
  - Auto-increment versions
  - Tag creation and validation
- **Changelog Generation**:
  - Git commit history parsing
  - Auto-generated release notes
- **Repository Operations**:
  - Status checks (dirty, branch)
  - Tag creation (annotated)
  - Remote push automation
- **Release Notes**:
  - Template-based formatting
  - Markdown output
  - Metadata injection

### 5. Command-Line Interface (`src/builder/cli.py`)

**Purpose**: User-facing CLI for build operations

**Commands**:

#### `mdoc-build`
Build documentation to PDF/HTML
- Options: --config, --pdf/--no-pdf, --html/--no-html, --output-dir, --verbose
- Process: Discover → Combine → Convert → Generate
- Output: PDF and/or HTML in `dist/`

#### `mdoc-release`
Create versioned releases
- Options: --bump (major/minor/patch), --version, --message, --push, --build
- Process: Validate → Build → Tag → Generate Notes
- Output: Git tag + release notes

#### `mdoc-validate`
Validate configuration and sources
- Checks: Config syntax, directories, files, images, git status
- Output: Validation report

### 6. Utilities (`src/utils/`)

**Logging** (`logging.py`):
- Console and file logging
- Configurable levels
- Formatted output

## Data Flow

```
Markdown Files (docs/sections/*.md)
    ↓
MarkdownProcessor
  - Discovery (sorted by prefix)
  - Combination (merged document)
  - Image processing (path resolution)
  - Metadata addition (frontmatter)
    ↓
HTML Content
    ↓
PDFGenerator
  - Template rendering (cover page)
  - CSS styling (pdf_style.css)
  - PDF generation (WeasyPrint)
    ↓
Output Files (dist/)
  - documentation.pdf
  - documentation.html
```

## Configuration Flow

```
config/build.yaml
    ↓
BuildConfig (loaded at startup)
    ↓
Passed to Components
  - MarkdownProcessor (source paths, extensions)
  - PDFGenerator (templates, styling)
  - ReleaseManager (git settings)
```

## Release Flow

```
User: mdoc-release
    ↓
ReleaseManager
  - Check repository status
  - Determine version (auto or specified)
    ↓
Build Process (optional)
  - Run full build (mdoc-build)
    ↓
Git Operations
  - Generate changelog from commits
  - Create release notes
  - Create annotated git tag
  - Push tags (optional)
    ↓
Output
  - Git tag: v1.0.0
  - Release notes: dist/RELEASE-1.0.0.md
  - Build artifacts: dist/*.pdf, dist/*.html
```

## Extension Points

### Custom Markdown Extensions
Add to `config/build.yaml`:
```yaml
markdown:
  extensions:
    - "your.custom.extension"
```

### Custom PDF Styling
Edit `config/templates/pdf_style.css`:
- Page layout
- Typography
- Colors
- Spacing

### Custom Templates
Modify Jinja2 templates:
- `cover.html` - Cover page
- `release_notes.md` - Release notes format

### Custom Scripts
Add to `scripts/`:
- `install.sh` - Installation automation
- `build.sh` - Build shortcuts
- Custom automation scripts

## Dependencies

### Core Python Packages
- **markdown**: Markdown to HTML conversion
- **pymdown-extensions**: Extended markdown features
- **weasyprint**: HTML to PDF rendering
- **pygments**: Syntax highlighting
- **pyyaml**: Configuration file parsing
- **gitpython**: Git operations
- **jinja2**: Template rendering
- **pillow**: Image processing
- **click**: CLI framework

### System Dependencies (for WeasyPrint)
- **Pango**: Text layout and rendering
- **Cairo**: 2D graphics library
- **GdkPixbuf**: Image loading

## Testing Strategy

### Unit Tests (`tests/unit/`)
- Configuration loading
- File discovery and sorting
- Markdown processing
- PDF generation logic
- Release management

### Integration Tests (`tests/integration/`)
- Full build pipeline
- Release workflow
- CLI commands
- Error handling

### Test Coverage
Target: >80% code coverage
Tool: pytest with coverage plugin

## Error Handling

### Configuration Errors
- Missing files: FileNotFoundError with helpful message
- Invalid YAML: Parse error with line number
- Missing keys: ValueError with required field

### Build Errors
- No markdown files: ValueError with search path
- Image not found: Warning in validation
- Invalid markdown: Logged but continues

### Git Errors
- Not a repository: ValueError with suggestion
- Dirty working tree: Warning with confirmation prompt
- Tag exists: ValueError with conflict details

## Performance Considerations

### File Operations
- Lazy loading of markdown files
- Caching of parsed content
- Efficient path resolution

### PDF Generation
- WeasyPrint uses native libraries (fast)
- Image optimization before rendering
- Incremental rendering

### Memory Usage
- Stream processing for large files
- Garbage collection after major operations
- Minimal in-memory caching

## Security Considerations

### Input Validation
- Path sanitization (prevent directory traversal)
- YAML safe loading (prevent code injection)
- Git command injection prevention

### File Permissions
- Read-only access to source files
- Write access only to output directory
- No execution of user-provided code

### Dependencies
- Regular updates for security patches
- Pinned versions in production
- Vulnerability scanning in CI/CD

## Deployment

### Local Installation
```bash
uv sync
```

### System-Wide Installation
```bash
pip install .
```

### Development Setup
```bash
uv sync --group dev
```

## Monitoring and Logging

### Build Logs
- Console output with timestamps
- Optional file logging
- Verbose mode for debugging

### Metrics
- Build time tracking
- File counts
- PDF size
- Memory usage (optional)

## Future Enhancements

Potential improvements:
1. **Multi-language support**: i18n for templates
2. **Watch mode**: Auto-rebuild on file changes
3. **Incremental builds**: Only rebuild changed sections
4. **Cloud storage**: Upload to S3/GCS
5. **API mode**: HTTP API for remote builds
6. **Themes**: Multiple template sets
7. **Plugins**: Extension system for custom processors
8. **Performance**: Parallel processing of sections
