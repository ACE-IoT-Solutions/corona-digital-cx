# Version Management

This project uses a single source of truth for version numbers to ensure consistency across all documents and outputs.

## Version Source of Truth

The **canonical version** is stored in `config/build.yaml`:

```yaml
project:
  version: "0.2.0"
```

## Version Flow

```
config/build.yaml (SOURCE OF TRUTH)
    ↓
    ├─→ README.md (synced on release)
    ├─→ standard/sections/00-frontmatter/01-document-metadata.md (manual update)
    ├─→ Git tags (created on release: v0.2.0)
    └─→ PDF/HTML output (automatic from config)
```

## Updating Versions

### Automated (Recommended)

Use the release command to automatically bump versions:

```bash
# Patch release (0.2.0 → 0.2.1)
uv run mdoc-release --bump patch

# Minor release (0.2.0 → 0.3.0)
uv run mdoc-release --bump minor

# Major release (0.2.0 → 1.0.0)
uv run mdoc-release --bump major
```

This will:
1. Increment version in `config/build.yaml`
2. Update `README.md` to match
3. Create git tag `vX.Y.Z`
4. Generate release notes

### Manual Update

If you need to manually set a specific version:

1. **Update the config** (source of truth):
   ```bash
   # Edit config/build.yaml
   version: "0.3.0"
   ```

2. **Sync README**:
   ```bash
   python3 << 'EOF'
   import re, yaml
   from pathlib import Path

   # Get version from config
   with open('config/build.yaml') as f:
       version = yaml.safe_load(f)['project']['version']

   # Update README
   readme = Path('README.md')
   content = readme.read_text()
   updated = re.sub(r'\*\*Version:\*\* [^\n]+', f'**Version:** {version}', content)
   readme.write_text(updated)
   print(f"✓ README synced to version {version}")
   EOF
   ```

3. **Update frontmatter** (if changed):
   ```bash
   # Edit standard/sections/00-frontmatter/01-document-metadata.md
   version: "0.3.0"
   **Version:** 0.3.0
   ```

4. **Commit changes**:
   ```bash
   git add config/build.yaml README.md standard/sections/00-frontmatter/
   git commit -m "chore: bump version to 0.3.0"
   ```

## Version Number Format

We use [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`

- **MAJOR** (1.0.0) - Incompatible changes, complete restructuring
- **MINOR** (0.3.0) - New sections, backwards-compatible additions
- **PATCH** (0.2.1) - Clarifications, typo fixes, minor corrections

### Pre-1.0 Versioning

Before the 1.0.0 stable release:
- **0.X.0** - Significant additions or changes
- **0.X.Y** - Minor updates and corrections
- Public API is not yet stable

## Version in Git Tags

Git tags are created with a `v` prefix:
- Config: `0.2.0`
- Git tag: `v0.2.0`

List all version tags:
```bash
git tag -l "v*"
```

## Checking Version Consistency

Verify all versions are in sync:

```bash
python3 << 'EOF'
import re, yaml
from pathlib import Path

# Get versions from different sources
with open('config/build.yaml') as f:
    config_ver = yaml.safe_load(f)['project']['version']

readme = Path('README.md').read_text()
readme_ver = re.search(r'\*\*Version:\*\* ([^\n]+)', readme).group(1)

frontmatter = Path('standard/sections/00-frontmatter/01-document-metadata.md').read_text()
front_ver = re.search(r'version: "([^"]+)"', frontmatter).group(1)

print(f"Config (canonical):  {config_ver}")
print(f"README:              {readme_ver}")
print(f"Frontmatter:         {front_ver}")

if config_ver == readme_ver == front_ver:
    print("\n✓ All versions in sync!")
else:
    print("\n⚠ Version mismatch detected!")
EOF
```

## Release Checklist

When creating a new release:

- [ ] Version updated in `config/build.yaml`
- [ ] README.md version synced (automatic with `mdoc-release`)
- [ ] Frontmatter version updated manually
- [ ] Date updated in frontmatter
- [ ] Changelog/release notes generated
- [ ] Git tag created (`vX.Y.Z`)
- [ ] PDF/HTML built and attached to release
- [ ] GitHub release published

## Questions?

- The release command handles most version management automatically
- When in doubt, check `config/build.yaml` - it's the source of truth
- Always use semantic versioning format: `X.Y.Z`
