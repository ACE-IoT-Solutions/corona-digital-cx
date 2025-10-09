#!/usr/bin/env bash
# Quick build script for documentation

set -e

# Parse arguments
VERBOSE=""
PDF="--pdf"
HTML="--html"

while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--verbose)
            VERBOSE="--verbose"
            shift
            ;;
        --no-pdf)
            PDF="--no-pdf"
            shift
            ;;
        --no-html)
            HTML="--no-html"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "Building documentation..."
mdoc-build $PDF $HTML $VERBOSE

echo ""
echo "✓ Build complete!"
echo "Output files in: dist/"
