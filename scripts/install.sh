#!/usr/bin/env bash
# Installation script for Corona Digital CX Documentation Build System

set -e

echo "Installing Corona Digital CX Documentation Build System..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
required_version="3.13"

echo "✓ Python version: $python_version"

# Install dependencies
echo "Installing dependencies with uv..."
uv sync

echo "Installing development dependencies..."
uv sync --group dev

# Verify installation
echo "Verifying installation..."
if command -v mdoc-build &> /dev/null; then
    echo "✓ mdoc-build installed"
    mdoc-build --help > /dev/null
else
    echo "⚠ mdoc-build not found in PATH"
fi

if command -v mdoc-release &> /dev/null; then
    echo "✓ mdoc-release installed"
else
    echo "⚠ mdoc-release not found in PATH"
fi

if command -v mdoc-validate &> /dev/null; then
    echo "✓ mdoc-validate installed"
else
    echo "⚠ mdoc-validate not found in PATH"
fi

echo ""
echo "✓ Installation complete!"
echo ""
echo "Available commands:"
echo "  mdoc-build    - Build documentation to PDF/HTML"
echo "  mdoc-release  - Create versioned release"
echo "  mdoc-validate - Validate configuration and sources"
echo ""
echo "Get started:"
echo "  mdoc-validate  # Check your setup"
echo "  mdoc-build     # Build documentation"
