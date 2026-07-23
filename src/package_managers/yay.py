"""Yay package manager update module.

This module provides functions to check yay availability and perform
system package updates using yay.
"""

from src.helper import runner

def _check_yay_installed() -> bool:
    """Check if yay is installed on the system.

    Returns:
        True if yay is available, False otherwise.
    """
    try:
        runner.run(["yay", "--version"])
        return True
    except runner.CommandError:
        return False
    

def update_yay(show_live_output: bool = False):
    """Update all yay packages on the system.

    Args:
        show_live_output: If True, display live update output to terminal.
                          If False, suppress output (default).

    Raises:
        RuntimeError: If yay is not installed on the system.
    """
    if not _check_yay_installed():
        raise RuntimeError("yay is not installed on this system.")
    runner.run(["sudo", "yay", "-Syu"], show_live_output=show_live_output)

def avail():
    return _check_yay_installed()