import argparse

from src.app import app
from src.__version__ import __version__

def parse_args():
    """Parse command-line arguments and run the application.

    Sets up argument parser with options for Homebrew updates,
    parses the command-line arguments, and invokes the main update process.
    """

    brew = False

    parser = argparse.ArgumentParser(
        prog="Tuxgrade - Linux System Updater",
        description="Automated system update script for several Linux distributions.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "--brew", "-b",
        action="store_true",
        help="Update Homebrew packages (if installed)"
    )

    args = parser.parse_args()

    brew = args.brew

    print("\n--- Tuxgrade - Linux System Updater ---\n")

    # Run the main update process
    app.run(brew)

    print("\n--- System Upgrade finished ---\n")




