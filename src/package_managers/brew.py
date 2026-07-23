"""Homebrew package manager update module.

This module provides functions to check Homebrew availability and update
installed Homebrew packages and casks.
"""
from src.helper import runner


def _check_brew_installed() -> bool:
    """Check if Homebrew is installed on the system.

    Returns:
        True if Homebrew is available, False otherwise.
    """
    # Test if brew is actually executable via login shell
    result = runner.run(
        ["bash", "-lc", "command -v brew"],
        check=False,
    )
    return result.returncode == 0


def update_brew() -> str | None:
    """Update all Homebrew packages on the system.

    Returns:
        Status message if Homebrew is not installed, None otherwise.
    """
    if not _check_brew_installed():
        return "Homebrew is not installed on this system."

    # Always use login shell to load brew environment
    runner.run(["bash", "-lc", "brew update"])
    runner.run(["bash", "-lc", "brew upgrade"])
    return None


