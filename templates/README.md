# Document Templates

This directory contains templates for contributing new sections and subsections to the Digital Commissioning of Building Automation Systems Standard.

## Template Structure

### Section Templates

Located in `section-templates/`:

- **`00-section-overview.md`** - Template for section overview/introduction files

Use this when creating a new major section (e.g., Section 5.0, Section 6.0).

### Subsection Templates

Located in `subsection-templates/`:

- **`01-subsection-requirements.md`** - Complete template for requirement subsections

Use this when adding new requirement subsections (e.g., 3.8, 4.4, etc.).

## How to Use Templates

### Adding a New Section

1. Create a new folder in `standard/sections/` with the appropriate numeric prefix:
   ```bash
   mkdir standard/sections/05-new-section-name
   ```

2. Copy the section overview template:
   ```bash
   cp templates/section-templates/00-section-overview.md \
      standard/sections/05-new-section-name/01-overview.md
   ```

3. Edit the template, replacing placeholders with your content

### Adding a New Subsection

1. Navigate to the appropriate section folder in `standard/sections/`

2. Copy the subsection template with the next sequential number:
   ```bash
   cp templates/subsection-templates/01-subsection-requirements.md \
      standard/sections/03-bacnet-network-infrastructure/09-new-requirement.md
   ```

3. Edit the template, filling in:
   - Section and subsection numbers (e.g., 3.9)
   - Requirement title and description
   - Specific requirements (using "shall", "should", "may")
   - Concrete examples with scenarios
   - Verification steps and acceptance criteria

## Template Components

Each subsection template includes:

### 1. Overview
Brief introduction to the subsection scope and purpose.

### 2. Requirements
Mandatory specifications using precise language:
- **shall** = mandatory requirement
- **should** = recommendation
- **may** = optional item

### 3. Examples
Real-world scenarios showing compliance:
- Context and scenario description
- Specific implementation details
- Configuration examples or diagrams
- Explanation of how it meets requirements

### 4. Verification
How to validate compliance:
- Validation methodology
- Step-by-step verification procedures
- Required deliverables (checklists)
- Acceptance criteria (pass/fail thresholds)

## Best Practices

### Writing Requirements

✅ **Good:** "Each BACnet device shall have a globally unique Device Instance Number."

❌ **Avoid:** "Devices should probably have unique IDs."

### Writing Examples

✅ **Good:** Provide specific values, configurations, and expected outcomes

❌ **Avoid:** Generic or theoretical examples without concrete details

### Writing Verification Steps

✅ **Good:** "Use Wireshark to capture BACnet traffic and verify no duplicate Device IDs exist."

❌ **Avoid:** "Check that devices work correctly."

## Formatting Guidelines

- Use **H1** (`#`) for section/subsection titles
- Use **H2** (`##`) for major components (Overview, Requirements, Examples, Verification)
- Use **H3** (`###`) for sub-items within components
- Use **bold** for emphasis on key terms
- Use code blocks for configuration examples
- Use bullet lists for requirements and checklists
- Always include the CC BY-SA footer at the end

## Contributing

1. Copy the appropriate template
2. Fill in all sections completely
3. Provide at least 2 concrete examples
4. Define clear, testable verification criteria
5. Submit via pull request following the [Contributing Guide](../README.md#contributing)

## Questions?

- Review existing sections for formatting examples
- Check the [Style Guide](../README.md#style-guide) in the main README
- Open a [GitHub Issue](https://github.com/YOUR-ORG/corona-digital-cx/issues) for clarification
