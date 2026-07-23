"""Tuxgrade - Main Entry Point.

This is the main entry point for Tuxgrade, an automated
system upgrade script for several Linux distributions with support for
DNF, APT, Pacman, Flatpak, Snap, Homebrew, and NVIDIA akmods.
"""
from src.app import cli

def main():
    """Entry point for the Tuxgrade application.

    Delegates to the CLI argument parser and exits with the appropriate status code.
    """
    exit(cli.parse_args())

if __name__ == "__main__":
    main()
