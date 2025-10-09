"""Configuration management for the build system."""

import os
from pathlib import Path
from typing import Any, Dict

import yaml


class BuildConfig:
    """Manages build configuration from YAML files."""

    def __init__(self, config_path: str | Path | None = None):
        """
        Initialize configuration.

        Args:
            config_path: Path to config file. Defaults to config/build.yaml
        """
        if config_path is None:
            config_path = Path("config/build.yaml")
        else:
            config_path = Path(config_path)

        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")

        with open(config_path, encoding="utf-8") as f:
            self._config: Dict[str, Any] = yaml.safe_load(f)

        # Store base directory for resolving relative paths
        self._base_dir = Path.cwd()

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation.

        Args:
            key: Configuration key (e.g., 'build.source_dir')
            default: Default value if key not found

        Returns:
            Configuration value
        """
        keys = key.split(".")
        value = self._config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default

        return value

    def get_path(self, key: str, default: str | None = None) -> Path:
        """
        Get configuration value as absolute Path.

        Args:
            key: Configuration key
            default: Default path if key not found

        Returns:
            Absolute Path object
        """
        value = self.get(key, default)
        if value is None:
            raise ValueError(f"Required path configuration missing: {key}")

        path = Path(value)
        if not path.is_absolute():
            path = self._base_dir / path

        return path

    @property
    def project_name(self) -> str:
        """Get project name."""
        return self.get("project.name", "Documentation")

    @property
    def project_author(self) -> str:
        """Get project author."""
        return self.get("project.author", "Unknown")

    @property
    def project_version(self) -> str:
        """Get project version."""
        return self.get("project.version", "1.0.0")

    @property
    def project_license(self) -> str:
        """Get project license."""
        return self.get("project.license", "CC BY-SA 4.0")

    @property
    def source_dir(self) -> Path:
        """Get source directory path."""
        return self.get_path("build.source_dir", "docs/sections")

    @property
    def output_dir(self) -> Path:
        """Get output directory path."""
        return self.get_path("build.output_dir", "dist")

    @property
    def output_name(self) -> str:
        """Get output filename (without extension)."""
        return self.get("build.output_name", "documentation")

    @property
    def template_dir(self) -> Path:
        """Get template directory path."""
        return self.get_path("build.template_dir", "config/templates")

    @property
    def assets_dir(self) -> Path:
        """Get assets directory path."""
        return self.get_path("build.assets_dir", "docs/assets")

    @property
    def markdown_extensions(self) -> list[str]:
        """Get markdown extensions list."""
        return self.get("markdown.extensions", [])

    @property
    def extension_configs(self) -> dict[str, Any]:
        """Get markdown extension configurations."""
        return self.get("markdown.extension_configs", {})

    @property
    def pdf_page_size(self) -> str:
        """Get PDF page size."""
        return self.get("pdf.page_size", "A4")

    @property
    def enable_toc(self) -> bool:
        """Check if table of contents is enabled."""
        return self.get("pdf.features.table_of_contents", True)

    @property
    def enable_syntax_highlighting(self) -> bool:
        """Check if syntax highlighting is enabled."""
        return self.get("pdf.features.syntax_highlighting", True)

    @property
    def tag_prefix(self) -> str:
        """Get git tag prefix for releases."""
        return self.get("release.tag_prefix", "v")

    @property
    def attach_pdf(self) -> bool:
        """Check if PDF should be attached to releases."""
        return self.get("release.attach_pdf", True)

    def __repr__(self) -> str:
        """String representation."""
        return f"BuildConfig(project='{self.project_name}', version='{self.project_version}')"
