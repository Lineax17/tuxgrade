"""Paru package manager update module.

This module provides functions to check paru availability and perform
system package updates using paru.
"""

from src.helper import runner

def _check_paru_installed() -> bool:
    """Check if paru is installed on the system.

    Returns:
        True if paru is available, False otherwise.
    """
    try:
        runner.run(["paru", "--version"])
        return True
    except runner.CommandError:
        return False
    

def update_paru(show_live_output: bool = False):
    """Update all paru packages on the system.

    Args:
        show_live_output: If True, display live update output to terminal.
                          If False, suppress output (default).

    Raises:
        RuntimeError: If paru is not installed on the system.
    """
    if not _check_paru_installed():
        raise RuntimeError("paru is not installed on this system.")
    runner.run(["sudo", "paru", "-Syu"], show_live_output=show_live_output)
