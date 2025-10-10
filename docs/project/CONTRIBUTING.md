# Contributing to the Digital Commissioning Standard

Thank you for your interest in contributing to the Digital Commissioning of Building Automation Systems Standard!

## Quick Links

- [How to Contribute](../README.md#contributing) - Main contribution guide
- [Style Guide](../README.md#style-guide) - Writing and formatting guidelines
- [Templates](../../templates/) - Templates for new sections and subsections

## Using Templates

We provide templates to help you create well-structured content that follows the standard format.

### Adding a New Subsection

1. **Navigate to the appropriate section** in `standard/sections/`

2. **Copy the subsection template**:
   ```bash
   cp templates/subsection-templates/01-subsection-requirements.md \
      standard/sections/[XX-section-name]/[YY-new-subsection].md
   ```

3. **Fill in the template** with your content:
   - Section number and title
   - Overview of the subsection
   - Specific requirements (using "shall", "should", "may")
   - Concrete examples with scenarios
   - Verification steps and acceptance criteria

4. **Test your contribution**:
   ```bash
   uv run mdoc-build --pdf --html
   ```

5. **Submit a pull request** with your changes

### Template Components

Each subsection should include:

- **Overview** - Brief introduction to scope and purpose
- **Requirements** - Mandatory specifications with precise language
- **Examples** - Real-world scenarios demonstrating compliance
- **Verification** - How to validate compliance with acceptance criteria

See the [Templates README](../../templates/README.md) for detailed guidance.

## Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat:` - New content or enhancements
- `fix:` - Corrections or clarifications
- `docs:` - Documentation improvements
- `refactor:` - Reorganization without content changes
- `chore:` - Maintenance tasks

**Examples:**
```
feat(bacnet): add section on BACnet Secure Connect requirements
fix(validation): clarify sampling requirements for Level 1
docs(readme): update installation instructions
```

## Review Process

1. Submit your pull request
2. Maintainers will review within 5 business days
3. Address any feedback or requested changes
4. Once approved, your contribution will be merged
5. Your name will be added to the contributors list

## Questions?

- Open a [GitHub Issue](https://github.com/YOUR-ORG/corona-digital-cx/issues)
- Start a [GitHub Discussion](https://github.com/YOUR-ORG/corona-digital-cx/discussions)

Thank you for helping improve building automation standards!
