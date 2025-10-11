# Digital Commissioning of Building Automation Systems (BAS)

**Version:** 0.3.12
**Status:** Draft Specification
**License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## 📋 About This Standard

This open standard defines the **validation and verification requirements** for digital commissioning (DCx) of Building Automation Systems (BAS). It specifies what aspects of BAS digital representation and network infrastructure must be tested, verified, and validated to ensure machine-readable, interoperable systems that enable advanced applications such as automated fault detection and diagnostics (AFDD), performance analytics, and seamless integration with other building systems.

### Key Objectives

- **Validation Framework**: Define comprehensive validation and verification requirements for BAS digital commissioning
- **Implementation Independence**: Provide validation methods that work regardless of specific system design standards, naming conventions, or configuration approaches
- **Progressive Validation**: Establish three levels of metadata validation from naming conventions to semantic models
- **Dual-Purpose Structure**: Serve both traditional commissioning needs (what to validate) and standardized verification procedures (how to validate)
- **Industry Collaboration**: Create a community-driven standard that evolves with industry best practices

### Scope

This standard applies to the validation and verification of all control systems and devices associated with mechanical (HVAC) and plumbing systems, covering:

- **BACnet Network Infrastructure Validation**: Network architecture, IP addressing, device configuration, communication protocols
- **Metadata Validation Levels**: Three progressive levels of digital representation validation (naming conventions, tagging/labeling, semantic models)

### Relationship to System Design Standards

This standard does **not** prescribe how BAS systems should be designed or configured. Instead, it defines validation and verification methods that can be applied regardless of the specific design standard, naming convention, or configuration approach used for a project. External design standards, project specifications, and configuration requirements are referenced as validation criteria, enabling this standard to be applied across different project types and design methodologies.

## 📖 Reading the Standard

### Online

Browse the standard sections directly in the `standard/sections/` folder:

- [00-frontmatter](standard/sections/00-frontmatter/) - Document metadata
- [01-introduction](standard/sections/01-introduction/) - Purpose and scope
- [02-general-requirements](standard/sections/02-general-requirements/) - Submission format, documentation, validation
- [03-bacnet-network-infrastructure](standard/sections/03-bacnet-network-infrastructure/) - Network architecture, addressing, device IDs
- [04-metadata-validation](standard/sections/04-metadata-validation/) - Three levels of validation

### PDF Version

Download the latest compiled PDF from the [Releases](../../releases) page.

## 🤝 Contributing

We welcome contributions from the building automation community! This is an open standard developed collaboratively to benefit the entire industry.

### How to Contribute

#### 💡 Propose Changes or Additions

1. **Open an Issue** for discussion:
   - Navigate to the [Issues](../../issues) tab
   - Click "New Issue"
   - Describe your proposed change, addition, or concern
   - Include rationale and use cases
   - Tag appropriately (`enhancement`, `clarification`, `bug`, etc.)

2. **Participate in Discussions**:
   - Comment on existing issues
   - Share your experience and expertise
   - Help refine proposals before implementation

#### 🔧 Submit Changes via Pull Request

1. **Fork the Repository**:
   - Click the "Fork" button in the top-right corner
   - Clone your fork locally:
     ```bash
     git clone https://github.com/YOUR-USERNAME/corona-digital-cx.git
     cd corona-digital-cx
     ```

2. **Create a Branch**:
   ```bash
   git checkout -b feature/your-improvement-name
   ```

3. **Make Your Changes**:
   - Edit the relevant markdown files in `standard/sections/`
   - Follow the existing structure and formatting
   - Ensure compliance with the [Style Guide](#style-guide)

4. **Test Your Changes** (optional but recommended):
   ```bash
   # Install dependencies
   brew install pango cairo gdk-pixbuf  # macOS
   uv sync

   # Build and preview
   uv run mdoc-build --pdf --html
   ```

5. **Commit Your Changes**:
   ```bash
   git add standard/sections/
   git commit -m "feat: add clarification on BBMD failover requirements"
   ```

   Use [Conventional Commits](https://www.conventionalcommits.org/) format:
   - `feat:` - New content or enhancements
   - `fix:` - Corrections or clarifications
   - `docs:` - Documentation improvements
   - `refactor:` - Reorganization without content changes

6. **Push and Create Pull Request**:
   ```bash
   git push origin feature/your-improvement-name
   ```
   - Visit your fork on GitHub
   - Click "Compare & pull request"
   - Provide a clear description of your changes
   - Reference any related issues (e.g., "Closes #42")

7. **Review Process**:
   - Maintainers and community members will review your PR
   - Address any feedback or requested changes
   - Once approved, your contribution will be merged!

### Style Guide

To maintain consistency across the standard:

- **Formatting**: Use standard markdown syntax
- **Headings**: Follow the existing hierarchy (H1 for major sections, H2 for subsections)
- **Language**: Use clear, precise technical language
- **Requirements**: Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items
- **Examples**: Include practical examples where helpful
- **References**: Link to authoritative sources (RFCs, standards, specifications)

### File Organization

The standard is organized using numbered prefixes for automatic ordering:

```
standard/sections/
├── 00-frontmatter/          # Document metadata
├── 01-introduction/         # Purpose and scope
├── 02-general-requirements/ # Submission, documentation, validation
├── 03-bacnet-network-infrastructure/  # Network requirements
└── 04-metadata-validation/  # Validation levels
```

Project documentation (README, CONTRIBUTING, etc.) is kept in `docs/` to separate it from the standard itself.

Each subsection is a separate markdown file with numeric prefixes (e.g., `01-overview.md`, `02-details.md`).

## 🔨 Building the Standard

This repository includes a Python-based build system that compiles the markdown source into professional PDF and HTML documents.

### Prerequisites

**System Dependencies** (macOS):
```bash
brew install pango cairo gdk-pixbuf
```

**System Dependencies** (Ubuntu/Debian):
```bash
sudo apt-get install python3-dev libpango1.0-dev libcairo2-dev
```

**Python Dependencies**:
```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

### Build Commands

```bash
# Validate setup and document structure
uv run mdoc-validate

# Build PDF only
uv run mdoc-build --pdf

# Build HTML only
uv run mdoc-build --html

# Build both PDF and HTML
uv run mdoc-build --pdf --html

# Build with verbose output
uv run mdoc-build --pdf --verbose
```

### Output

Generated files are placed in the `dist/` directory:
- `digital-commissioning-bas-standard.pdf`
- `digital-commissioning-bas-standard.html`

## 📜 License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

**You are free to:**
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license

### Attribution

When using or referencing this standard, please use:

> Digital Commissioning of Building Automation Systems Standard
> Corona Digital CX Working Group
> Licensed under CC BY-SA 4.0
> https://github.com/YOUR-ORG/corona-digital-cx

## 🎯 Roadmap

- [ ] **v0.3**: Community review and feedback incorporation
- [ ] **v0.4**: Add appendices (naming convention examples, sample SPARQL queries)
- [ ] **v0.5**: Validation tooling and reference implementations
- [ ] **v1.0**: First stable release

## 💬 Community

- **Issues**: [GitHub Issues](../../issues) for bug reports and feature requests
- **Discussions**: [GitHub Discussions](../../discussions) for questions and community conversation
- **Pull Requests**: [GitHub Pull Requests](../../pulls) to contribute changes

## 🙏 Acknowledgments

This standard is developed collaboratively by the Corona Digital CX Working Group with contributions from building automation professionals, commissioning agents, and industry experts.

## 📞 Contact

For questions about this standard or the contribution process:

- Open a [GitHub Issue](../../issues)
- Start a [GitHub Discussion](../../discussions)
- Email: [contact information if applicable]

---

**Thank you for contributing to the future of building automation!** 🏢✨
