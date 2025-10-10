"""Command-line interface for the build system."""

import sys
from pathlib import Path

import click

from .config import BuildConfig
from .markdown_processor import MarkdownProcessor
from .pdf_generator import PDFGenerator
from .release_manager import ReleaseManager


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Corona Digital CX Documentation Build System."""
    pass


@cli.command()
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True, path_type=Path),
    help="Path to configuration file",
)
@click.option("--pdf/--no-pdf", default=True, help="Generate PDF output")
@click.option("--html/--no-html", default=True, help="Generate HTML output")
@click.option("--output-dir", "-o", type=click.Path(path_type=Path), help="Output directory")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
def build(config, pdf, html, output_dir, verbose):
    """Build documentation from markdown sources."""
    try:
        # Load configuration
        click.echo("Loading configuration...")
        build_config = BuildConfig(config)

        if verbose:
            click.echo(f"  Project: {build_config.project_name}")
            click.echo(f"  Version: {build_config.project_version}")
            click.echo(f"  Source: {build_config.source_dir}")

        # Override output directory if specified
        if output_dir:
            build_config._config["build"]["output_dir"] = str(output_dir)

        # Initialize processors
        click.echo("Initializing processors...")
        md_processor = MarkdownProcessor(build_config)
        pdf_generator = PDFGenerator(build_config)

        # Discover files
        click.echo("Discovering markdown files...")
        files = md_processor.discover_files()
        click.echo(f"  Found {len(files)} markdown files")

        if verbose:
            for f in files:
                click.echo(f"    - {f.name}")

        # Build document
        click.echo("Building document...")
        markdown_content, html_content = md_processor.build_complete_document()
        click.echo(f"  Generated {len(html_content)} bytes of HTML")

        # Generate outputs
        pdf_path, html_path = pdf_generator.get_output_paths()

        if pdf:
            click.echo(f"Generating PDF: {pdf_path}")
            pdf_generator.generate_pdf(html_content, pdf_path)
            click.echo(f"  ✓ PDF created: {pdf_path}")

        if html:
            click.echo(f"Generating HTML: {html_path}")
            pdf_generator.generate_html(html_content, html_path)
            click.echo(f"  ✓ HTML created: {html_path}")

        click.echo("✓ Build completed successfully!")

    except Exception as e:
        click.echo(f"✗ Build failed: {e}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


@cli.command()
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True, path_type=Path),
    help="Path to configuration file",
)
@click.option(
    "--bump",
    type=click.Choice(["major", "minor", "patch"]),
    default="patch",
    help="Version bump type",
)
@click.option("--version", "-V", help="Specific version to release")
@click.option("--message", "-m", help="Release message")
@click.option("--push/--no-push", default=False, help="Push tags and create GitHub release")
@click.option("--build/--no-build", "do_build", default=True, help="Build before releasing")
@click.option("--draft", is_flag=True, help="Create as draft release")
@click.option("--prerelease", is_flag=True, help="Mark as prerelease")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
def release(config, bump, version, message, push, do_build, draft, prerelease, verbose):
    """Create a new release with git tag and optional GitHub release."""
    try:
        # Load configuration
        click.echo("Loading configuration...")
        build_config = BuildConfig(config)

        # Initialize release manager
        release_mgr = ReleaseManager(build_config)

        # Check repository status
        if release_mgr.is_dirty():
            click.echo(
                "⚠ Warning: Repository has uncommitted changes", err=True
            )
            if not click.confirm("Continue anyway?"):
                sys.exit(1)

        # Determine version
        if version:
            new_version = version
        else:
            current_version = release_mgr.get_current_version()
            new_version = release_mgr.increment_version(current_version, bump)

        click.echo(f"Creating release: {new_version}")

        # Build documentation
        artifacts = []
        if do_build:
            click.echo("Building documentation...")
            ctx = click.get_current_context()
            ctx.invoke(build, config=config, pdf=True, html=True, verbose=verbose)

            # Collect artifacts
            pdf_path = build_config.output_dir / f"{build_config.output_name}.pdf"
            html_path = build_config.output_dir / f"{build_config.output_name}.html"

            if pdf_path.exists():
                artifacts.append(pdf_path)
            if html_path.exists():
                artifacts.append(html_path)

        # Generate changelog and release notes
        click.echo("Generating release notes...")
        changelog = release_mgr.generate_changelog()
        notes = release_mgr.create_release_notes(new_version, changelog)

        if verbose:
            click.echo("\nRelease Notes:")
            click.echo("-" * 40)
            click.echo(notes)
            click.echo("-" * 40)

        # Update README version
        click.echo("Updating README version...")
        if release_mgr.update_readme_version(new_version):
            click.echo(f"  ✓ README.md updated to version {new_version}")
            # Commit the README update
            readme_path = Path("README.md")
            release_mgr.commit_files([readme_path], f"chore: bump version to {new_version}")
            click.echo(f"  ✓ Version update committed")
        else:
            click.echo("  ⚠ README.md not updated (file not found or no changes)")

        # Create tag
        click.echo(f"Creating git tag...")
        tag_message = message or f"Release {new_version}"
        tag_name = release_mgr.create_tag(new_version, tag_message)
        click.echo(f"  ✓ Tag created: {tag_name}")

        # Push to remote and create GitHub release
        if push:
            click.echo("Pushing tags to remote...")
            release_mgr.push_tags()
            click.echo("  ✓ Tags pushed")

            # Create GitHub release with artifacts
            click.echo("Creating GitHub release...")
            success = release_mgr.create_github_release(
                version=new_version,
                release_notes=notes,
                artifacts=artifacts,
                draft=draft,
                prerelease=prerelease,
            )

            if not success:
                click.echo("\n💡 To enable GitHub releases:")
                click.echo("   1. Install gh CLI: https://cli.github.com/")
                click.echo("   2. Authenticate: gh auth login")
                click.echo("   3. Re-run this command with --push")

        # Save release notes
        notes_path = build_config.output_dir / f"RELEASE-{new_version}.md"
        notes_path.parent.mkdir(parents=True, exist_ok=True)
        with open(notes_path, "w", encoding="utf-8") as f:
            f.write(notes)
        click.echo(f"  ✓ Release notes: {notes_path}")

        click.echo(f"\n✓ Release {new_version} created successfully!")

        if not push:
            click.echo(
                "\n⚠ Tags not pushed to remote. Run with --push to publish and create GitHub release."
            )

    except Exception as e:
        click.echo(f"✗ Release failed: {e}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


@cli.command()
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True, path_type=Path),
    help="Path to configuration file",
)
def validate(config):
    """Validate configuration and source files."""
    try:
        click.echo("Validating configuration...")

        # Load configuration
        build_config = BuildConfig(config)
        click.echo("  ✓ Configuration valid")

        # Check directories
        click.echo("\nValidating directories...")
        for name, path in [
            ("Source", build_config.source_dir),
            ("Template", build_config.template_dir),
        ]:
            if path.exists():
                click.echo(f"  ✓ {name}: {path}")
            else:
                click.echo(f"  ✗ {name} not found: {path}", err=True)
                sys.exit(1)

        # Check files
        click.echo("\nValidating files...")
        md_processor = MarkdownProcessor(build_config)
        files = md_processor.discover_files()
        click.echo(f"  ✓ Found {len(files)} markdown files")

        # Check for common issues
        click.echo("\nChecking for issues...")
        issues = []

        for file_path in files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for empty files
            if not content.strip():
                issues.append(f"Empty file: {file_path.name}")

            # Check for broken image references
            import re

            images = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", content)
            for alt, img_path in images:
                if not img_path.startswith(("http://", "https://", "/")):
                    full_path = build_config.assets_dir / img_path
                    if not full_path.exists():
                        issues.append(f"Missing image in {file_path.name}: {img_path}")

        if issues:
            click.echo(f"\n⚠ Found {len(issues)} issues:")
            for issue in issues:
                click.echo(f"  - {issue}")
        else:
            click.echo("  ✓ No issues found")

        # Repository info
        click.echo("\nRepository information...")
        try:
            release_mgr = ReleaseManager(build_config)
            info = release_mgr.get_repo_info()
            click.echo(f"  Branch: {info['branch']}")
            click.echo(f"  Version: {info['current_version']}")
            click.echo(f"  Clean: {not info['dirty']}")
            if info["tags"]:
                click.echo(f"  Recent tags: {', '.join(info['tags'][:3])}")
        except ValueError:
            click.echo("  (Not a git repository)")

        click.echo("\n✓ Validation complete!")

    except Exception as e:
        click.echo(f"✗ Validation failed: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    cli()
