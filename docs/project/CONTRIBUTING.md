# Contributing To The Digital Commissioning Standard

This page expands on the repository-level [`CONTRIBUTING.md`](../../CONTRIBUTING.md) with authoring guidance for contributors working inside the standard source.

## Quick Links

- [Repository entry point](../../README.md)
- [Contributor quickstart](../QUICKSTART.md)
- [Templates](../../templates/)

## What To Edit

- Use `standard/sections/` for normative changes to the standard
- Use `templates/` when creating new sections or subsections
- Use `docs/` for contributor-facing process documentation

## Using Templates

Templates are provided to keep new material structurally consistent.

### Adding A New Subsection

1. Navigate to the appropriate section in `standard/sections/`
2. Copy the subsection template:

```bash
cp templates/subsection-templates/01-subsection-requirements.md \
  standard/sections/[XX-section-name]/[YY-new-subsection].md
```

3. Replace the placeholder content with:
   - the subsection title and scope
   - normative requirements
   - examples where they reduce ambiguity
   - verification steps or acceptance criteria
4. Validate and build the repo before opening a pull request

### Template Components

Each subsection should generally include:

- overview
- requirements
- examples
- verification or acceptance criteria

See [`templates/README.md`](../../templates/README.md) for more detail.

## Writing Conventions

- Use clear technical language
- Use `shall` for mandatory requirements
- Use `should` for recommendations
- Use `may` for optional provisions
- Prefer short sections with one purpose
- Add examples when a requirement could be interpreted multiple ways

## Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/).

Examples:

- `feat(bacnet): add BACnet Secure Connect validation guidance`
- `fix(validation): clarify sampling requirements for level 1`
- `docs(contributing): tighten newcomer workflow`

## Review Expectations

- Explain the operational problem your change solves
- Flag whether the change is normative or editorial
- Expect review on clarity, interoperability impact, and verification implications

## Questions

- Issues: https://github.com/ACE-IoT-Solutions/corona-digital-cx/issues
- Discussions: https://github.com/ACE-IoT-Solutions/corona-digital-cx/discussions
