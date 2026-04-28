# Contributing

This repository is maintained as a working standard, not just a document dump. New participants should start here before opening a pull request.

## First Contribution Path

1. Read [`README.md`](./README.md) for the repo map
2. Read [`docs/QUICKSTART.md`](./docs/QUICKSTART.md) for local setup
3. Review the relevant section in [`standard/sections/`](./standard/sections/)
4. Open an issue or reference an existing one before making substantive changes
5. Submit a pull request with the problem, rationale, and proposed text

## Where Changes Belong

- Edit `standard/sections/` for changes to the standard itself
- Edit `standard/assets/` for diagrams or embedded assets
- Edit `src/` and `config/` for build tooling or publishing behavior
- Edit `docs/` for contributor and process documentation

## Contribution Expectations

- Keep changes narrowly scoped
- Prefer precise clarifications over broad rewrites
- Use "shall" for mandatory requirements, "should" for recommendations, and "may" for optional items
- Include examples when they remove ambiguity
- Explain why the change improves interoperability, validation, or implementation clarity

## Workflow

```bash
git clone https://github.com/ACE-IoT-Solutions/corona-digital-cx.git
cd corona-digital-cx
git checkout -b your-branch-name
uv sync
uv run mdoc-validate
```

Make your changes, then build outputs when needed:

```bash
uv run mdoc-build --pdf --html
```

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/).

Examples:

- `feat(metadata): add example for level 2 tagging validation`
- `fix(bacnet): clarify device instance uniqueness wording`
- `docs(readme): simplify new contributor entry points`

## Pull Requests

Pull requests should include:

- the problem being addressed
- the intended audience or use case
- any related issue numbers
- notes on whether the change is editorial, normative, or tooling-related

## Templates And Additional Guidance

- Detailed contributor notes: [`docs/project/CONTRIBUTING.md`](./docs/project/CONTRIBUTING.md)
- Section and subsection templates: [`templates/`](./templates/)

## Questions

- Issues: https://github.com/ACE-IoT-Solutions/corona-digital-cx/issues
- Discussions: https://github.com/ACE-IoT-Solutions/corona-digital-cx/discussions
