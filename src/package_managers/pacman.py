"""Pacman package manager update module.

This module provides functions to check Pacman availability and perform
system package updates using Pacman.
"""

from src.helper import runner

def _check_pacman_installed() -> bool:
    """Check if Pacman is installed on the system.

    Returns:
        True if Pacman is available, False otherwise.
    """
    try:
        runner.run(["pacman", "--version"])
        return True
    except runner.CommandError:
        return False
    

def update_pacman(show_live_output: bool = False):
    """Update all Pacman packages on the system.

    Args:
        show_live_output: If True, display live update output to terminal.
                          If False, suppress output (default).

    Raises:
        RuntimeError: If Pacman is not installed on the system.
    """
    if not _check_pacman_installed():
        raise RuntimeError("Pacman is not installed on this system.")
    runner.run(["sudo", "pacman", "-Syu"], show_live_output=show_live_output)
