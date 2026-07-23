"""Command execution module.

This module provides utilities for running shell commands with configurable
error handling and output modes.
"""

import logging
import subprocess


class CommandError(RuntimeError):
    """Exception raised when a command execution fails."""
    pass


def run(cmd: list[str], check: bool = True):
    """Run a shell command with live output.

    Args:
        cmd: The command to run as a list of strings (e.g., ["ls", "-la"]).
        check: If True, raises CommandError on non-zero exit codes (default).
              If False, returns CompletedProcess with any exit code.

    Returns:
        CompletedProcess instance with returncode, stdout, and stderr attributes.

    Raises:
        CommandError: If the command fails (non-zero exit code) and check=True.
    """
    logging.debug("Executing: %s", " ".join(cmd))

    try:
        result = subprocess.run(cmd, check=check, text=True)
        return result
    except subprocess.CalledProcessError as e:
        logging.error("Command failed: %s", " ".join(cmd))
        if e.stderr:
            logging.debug(e.stderr.strip())
        raise CommandError(cmd) from e