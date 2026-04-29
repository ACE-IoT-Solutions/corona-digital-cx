# Digital Commissioning of Building Automation Systems (BAS)

Draft specification | License: [CC BY-SA 4.0](./LICENSE)

This repository is the working source for an open standard that defines validation and verification requirements for digital commissioning of Building Automation Systems (BAS).

## Start Here

If you are new to the project, use one of these entry points:

- **Read the standard**: <https://ace-iot-solutions.github.io/corona-digital-cx/>
- **Contribute content**: read [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- **Set up the build locally**: read [`docs/QUICKSTART.md`](./docs/QUICKSTART.md)
- **Understand the build system**: read [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md)

## What This Repository Contains

- `standard/sections/`: the normative source text of the standard
- `standard/assets/`: diagrams and other assets used by the standard
- `src/`: the Python build tooling used to compile HTML and PDF outputs
- `templates/`: authoring templates for new sections and subsections
- `docs/`: contributor and build documentation

This repository does two jobs:

1. It hosts the standard itself.
2. It includes the tooling needed to validate and publish that standard.

## Scope

The standard covers digital commissioning requirements for control systems and devices associated with mechanical (HVAC) and plumbing systems, including:

- BACnet network infrastructure validation
- device configuration and communication requirements
- progressive metadata validation from naming conventions through semantic models

The standard does **not** prescribe a single BAS design approach. It defines what must be validated regardless of the design standard, naming convention, or configuration method used on a project.

## For New Participants

The shortest path to a useful contribution is:

1. Read the overview in [`standard/sections/01-introduction/`](./standard/sections/01-introduction/)
2. Review open issues or start a discussion on GitHub
3. Make a small clarification or example improvement in `standard/sections/`
4. Build locally if your change affects structure, formatting, or output
5. Submit a pull request with the rationale for the change

If you are deciding where to start, content clarifications and examples are usually better first contributions than structural refactors.

## Reading The Standard

- Read the published standard at <https://ace-iot-solutions.github.io/corona-digital-cx/>
- Browse the source in [`standard/sections/`](./standard/sections/)
- Download compiled artifacts from the repository [Releases](https://github.com/ACE-IoT-Solutions/corona-digital-cx/releases)
- Build local HTML/PDF outputs with `uv run mdoc-build --pdf --html`

## Contributing

Contributions are welcome from BAS practitioners, commissioning providers, system integrators, owners, and software/tooling contributors.

Use [`CONTRIBUTING.md`](./CONTRIBUTING.md) for:

- contribution workflow
- writing conventions
- template usage
- local validation and build steps

## Build Commands

```bash
uv sync
uv run mdoc-validate
uv run mdoc-build --pdf --html
```

Generated files are written to `dist/`.

## License

This repository is published under [`CC BY-SA 4.0`](./LICENSE) unless a file states otherwise.

Use this material with attribution, and share adaptations under the same license.
