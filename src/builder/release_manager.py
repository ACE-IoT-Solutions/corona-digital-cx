"""Git release automation and version management."""

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import git

from .config import BuildConfig


class ReleaseManager:
    """Manages git releases and version tagging."""

    def __init__(self, config: BuildConfig, repo_path: Optional[Path] = None):
        """
        Initialize release manager.

        Args:
            config: Build configuration
            repo_path: Path to git repository (defaults to current directory)
        """
        self.config = config

        if repo_path is None:
            repo_path = Path.cwd()

        try:
            self.repo = git.Repo(repo_path, search_parent_directories=True)
        except git.InvalidGitRepositoryError as e:
            raise ValueError(f"Not a git repository: {repo_path}") from e

        if self.repo.bare:
            raise ValueError("Cannot work with bare repository")

    def get_current_version(self) -> str:
        """
        Get current version from config or latest git tag.

        Returns:
            Current version string
        """
        # Try to get version from git tags
        tags = self.get_version_tags()
        if tags:
            return tags[0]  # Most recent tag

        # Fall back to config version
        return self.config.project_version

    def get_version_tags(self) -> List[str]:
        """
        Get all version tags sorted by semver (newest first).

        Returns:
            List of version tags
        """
        prefix = self.config.tag_prefix
        tags = []

        for tag in self.repo.tags:
            if tag.name.startswith(prefix):
                version = tag.name[len(prefix) :]
                tags.append(version)

        # Sort by semantic version
        def version_key(v: str) -> tuple:
            parts = re.findall(r"\d+", v)
            return tuple(int(p) for p in parts) if parts else (0, 0, 0)

        tags.sort(key=version_key, reverse=True)
        return tags

    def increment_version(self, version: str, bump: str = "patch") -> str:
        """
        Increment version number.

        Args:
            version: Current version (e.g., '1.2.3')
            bump: Version part to bump ('major', 'minor', 'patch')

        Returns:
            Incremented version string
        """
        parts = re.findall(r"\d+", version)
        if len(parts) < 3:
            parts.extend(["0"] * (3 - len(parts)))

        major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])

        if bump == "major":
            major += 1
            minor = 0
            patch = 0
        elif bump == "minor":
            minor += 1
            patch = 0
        elif bump == "patch":
            patch += 1
        else:
            raise ValueError(f"Invalid bump type: {bump}")

        return f"{major}.{minor}.{patch}"

    def generate_changelog(self, since_tag: Optional[str] = None) -> str:
        """
        Generate changelog from git commits.

        Args:
            since_tag: Generate changelog since this tag (None = all commits)

        Returns:
            Changelog text
        """
        if since_tag:
            prefix = self.config.tag_prefix
            full_tag = f"{prefix}{since_tag}"
            try:
                commits = list(
                    self.repo.iter_commits(f"{full_tag}..HEAD")
                )
            except git.BadName:
                # Tag doesn't exist, get all commits
                commits = list(self.repo.iter_commits())
        else:
            commits = list(self.repo.iter_commits())

        if not commits:
            return "No changes"

        changelog_lines = ["## Changes\n"]

        for commit in commits:
            # Skip merge commits
            if len(commit.parents) > 1:
                continue

            # Format commit message
            message = commit.message.strip().split("\n")[0]  # First line only
            short_hash = commit.hexsha[:7]
            changelog_lines.append(f"- {message} ({short_hash})")

        return "\n".join(changelog_lines)

    def create_release_notes(
        self, version: str, changelog: Optional[str] = None
    ) -> str:
        """
        Create release notes from template.

        Args:
            version: Release version
            changelog: Changelog text (auto-generated if None)

        Returns:
            Release notes content
        """
        if changelog is None:
            # Get previous version for changelog
            tags = self.get_version_tags()
            since_tag = tags[0] if tags else None
            changelog = self.generate_changelog(since_tag)

        template_path = self.config.get_path(
            "release.notes_template", "config/templates/release_notes.md"
        )

        if template_path.exists():
            with open(template_path, encoding="utf-8") as f:
                template = f.read()

            # Simple template variable replacement
            notes = template.replace("{{ version }}", version)
            notes = notes.replace("{{ date }}", datetime.now().strftime("%Y-%m-%d"))
            notes = notes.replace("{{ changelog }}", changelog)
            notes = notes.replace("{{ pdf_filename }}", f"{self.config.output_name}.pdf")
            notes = notes.replace("{{ html_filename }}", f"{self.config.output_name}.html")

            return notes
        else:
            # Simple fallback
            return f"""# Release {version}

{changelog}

Generated on {datetime.now().strftime("%Y-%m-%d")}
"""

    def create_tag(self, version: str, message: Optional[str] = None) -> str:
        """
        Create git tag for release.

        Args:
            version: Version to tag
            message: Tag message (auto-generated if None)

        Returns:
            Full tag name
        """
        prefix = self.config.tag_prefix
        tag_name = f"{prefix}{version}"

        if tag_name in [t.name for t in self.repo.tags]:
            raise ValueError(f"Tag already exists: {tag_name}")

        if message is None:
            message = f"Release {version}"

        # Create annotated tag
        self.repo.create_tag(tag_name, message=message)

        return tag_name

    def is_dirty(self) -> bool:
        """Check if repository has uncommitted changes."""
        return self.repo.is_dirty()

    def get_current_branch(self) -> str:
        """Get current git branch name."""
        return self.repo.active_branch.name

    def commit_files(self, files: List[Path], message: str) -> None:
        """
        Commit files to git.

        Args:
            files: List of file paths to commit
            message: Commit message
        """
        # Add files to index
        self.repo.index.add([str(f) for f in files])

        # Commit
        self.repo.index.commit(message)

    def push_tags(self, remote: str = "origin") -> None:
        """
        Push tags to remote.

        Args:
            remote: Remote name (default: origin)
        """
        remote_obj = self.repo.remote(remote)
        remote_obj.push(tags=True)

    def get_repo_info(self) -> dict:
        """
        Get repository information.

        Returns:
            Dictionary with repo details
        """
        return {
            "path": str(self.repo.working_dir),
            "branch": self.get_current_branch(),
            "dirty": self.is_dirty(),
            "current_version": self.get_current_version(),
            "tags": self.get_version_tags()[:5],  # Last 5 tags
        }

    def get_remote_url(self, remote: str = "origin") -> Optional[str]:
        """
        Get GitHub repository URL from remote.

        Args:
            remote: Remote name (default: origin)

        Returns:
            GitHub repo identifier (owner/repo) or None
        """
        try:
            remote_obj = self.repo.remote(remote)
            url = remote_obj.url

            # Parse GitHub URL (both HTTPS and SSH)
            # HTTPS: https://github.com/owner/repo.git
            # SSH: git@github.com:owner/repo.git
            if "github.com" in url:
                if url.startswith("git@"):
                    # SSH format
                    repo_part = url.split(":")[-1]
                else:
                    # HTTPS format
                    repo_part = url.split("github.com/")[-1]

                # Remove .git suffix
                repo_part = repo_part.rstrip("/").replace(".git", "")
                return repo_part
        except Exception:
            pass

        return None

    def create_github_release(
        self,
        version: str,
        release_notes: str,
        artifacts: Optional[List[Path]] = None,
        draft: bool = False,
        prerelease: bool = False,
    ) -> bool:
        """
        Create GitHub release with artifacts using gh CLI.

        Args:
            version: Version tag
            release_notes: Release notes content
            artifacts: List of files to attach to release
            draft: Create as draft release
            prerelease: Mark as prerelease

        Returns:
            True if successful, False otherwise
        """
        # Check if gh CLI is available
        try:
            subprocess.run(
                ["gh", "--version"],
                check=True,
                capture_output=True,
                text=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Warning: gh CLI not found. Install from https://cli.github.com/")
            print("Skipping GitHub release creation. Tag created successfully.")
            return False

        # Check if we're in a GitHub repo
        repo_id = self.get_remote_url()
        if not repo_id:
            print("Warning: Not a GitHub repository or remote not configured.")
            print("Skipping GitHub release creation. Tag created successfully.")
            return False

        prefix = self.config.tag_prefix
        tag_name = f"{prefix}{version}"

        # Prepare gh release create command
        cmd = [
            "gh",
            "release",
            "create",
            tag_name,
            "--title",
            f"Release {version}",
            "--notes",
            release_notes,
        ]

        if draft:
            cmd.append("--draft")

        if prerelease:
            cmd.append("--prerelease")

        # Add artifacts
        if artifacts:
            for artifact in artifacts:
                if artifact.exists():
                    cmd.append(str(artifact))

        try:
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True,
                cwd=self.repo.working_dir,
            )
            print(f"✓ GitHub release created: {result.stdout.strip()}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to create GitHub release: {e.stderr}")
            print("Tag created successfully, but GitHub release failed.")
            return False
