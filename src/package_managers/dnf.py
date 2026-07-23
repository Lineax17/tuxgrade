"""DNF package manager update module.

This module provides functions to check DNF availability and perform
system package updates using DNF.
"""

from src.helper import runner


def _check_dnf_installed() -> bool:
    """Check if DNF is installed on the system.

    Returns:
        True if DNF is available, False otherwise.
    """
    try:
        runner.run(["dnf", "--version"])
        return True
    except runner.CommandError:
        return False


def update_dnf():
    """Update all DNF packages on the system.

    Raises:
        RuntimeError: If DNF is not installed on the system.
    """
    if not _check_dnf_installed():
        raise RuntimeError("DNF is not installed on this system.")
    runner.run(["sudo", "dnf", "update", "-y"])

def clean_dnf_cache():
    """Clean DNF package cache and old metadata.
    
    Removes cached packages and old metadata to save disk space.
    Uses dnf commands like the legacy script.
    
    Raises:
        RuntimeError: If DNF is not installed on the system.
    """
    if not _check_dnf_installed():
        raise RuntimeError("DNF is not installed on this system.")
    
    # Clean cached packages
    runner.run(["sudo", "dnf", "clean", "packages"])
    
    # Clean old metadata
    runner.run(["sudo", "dnf", "clean", "metadata"])
