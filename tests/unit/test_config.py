"""Unit tests for configuration handling."""
import pytest
from pathlib import Path
import json


class TestConfiguration:
    """Test configuration parsing and validation."""

    def test_load_config_from_file(self, temp_dir: Path):
        """Test loading configuration from JSON file."""
        from src.config import load_config

        config_data = {
            "markdown_dir": "markdown",
            "output_dir": "output",
            "version": "1.0.0",
            "license_file": "LICENSE.md"
        }

        config_file = temp_dir / "config.json"
        config_file.write_text(json.dumps(config_data))

        config = load_config(config_file)
        assert config["version"] == "1.0.0"
        assert config["markdown_dir"] == "markdown"

    def test_default_config_values(self):
        """Test default configuration values."""
        from src.config import get_default_config

        config = get_default_config()
        assert "markdown_dir" in config
        assert "output_dir" in config
        assert "version" in config

    def test_config_validation(self):
        """Test configuration validation."""
        from src.config import validate_config, ConfigValidationError

        valid_config = {
            "markdown_dir": "markdown",
            "output_dir": "output",
            "version": "1.0.0"
        }
        assert validate_config(valid_config) is True

        # Missing required field
        invalid_config = {
            "markdown_dir": "markdown"
        }
        with pytest.raises(ConfigValidationError):
            validate_config(invalid_config)

    def test_version_format_validation(self):
        """Test version format validation."""
        from src.config import validate_version

        assert validate_version("1.0.0") is True
        assert validate_version("v1.0.0") is True
        assert validate_version("10.20.30") is True

        assert validate_version("1.0") is False
        assert validate_version("invalid") is False
        assert validate_version("1.0.0.0") is False

    def test_path_resolution(self, temp_dir: Path):
        """Test that paths are resolved relative to config file."""
        from src.config import load_config, resolve_paths

        config_data = {
            "markdown_dir": "markdown",
            "output_dir": "output",
            "version": "1.0.0"
        }

        config_file = temp_dir / "config.json"
        config_file.write_text(json.dumps(config_data))

        config = load_config(config_file)
        config = resolve_paths(config, temp_dir)

        assert Path(config["markdown_dir"]).is_absolute()
        assert Path(config["output_dir"]).is_absolute()
