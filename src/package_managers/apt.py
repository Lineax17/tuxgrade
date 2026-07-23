"""APT package manager update module.

This module provides functions to check APT availability and perform
system package updates using APT.
"""

from src.helper import runner

def _check_apt_installed() -> bool:
    """Check if APT is installed on the system.

    Returns:
        True if APT is available, False otherwise.
    """
    try:
        runner.run(["apt", "--version"])
        return True
    except runner.CommandError:
        return False
    

def update_apt():
    """Update all APT packages on the system.

    Raises:
        RuntimeError: If APT is not installed on the system.
    """
    if not _check_apt_installed():
        raise RuntimeError("APT is not installed on this system.")
    runner.run(["sudo", "apt", "update"])
    runner.run(["sudo", "apt", "upgrade", "-y"])