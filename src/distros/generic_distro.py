from src.helper import cli_print_utility
from src.package_managers import snap, flatpak, brew as homebrew


class GenericDistro:
    """Generic Linux distribution update handler.

    Provides base update functionality for any Linux distribution by updating
    common package managers (Snap, Flatpak, Homebrew). This class can be used
    directly for unsupported distributions or as a base class for distro-specific implementations.
    """

    def update(self, brew):
        """Perform system updates for generic Linux distributions.

        Updates common package managers including Snap, Flatpak, and optionally Homebrew.

        Args:
            brew: If True, include Homebrew package updates.
        """
        ## Snap package updates
        cli_print_utility.print_header("Update Snap Packages")
        cli_print_utility.print_output(snap.update_snap)

        ## Flatpak package updates
        cli_print_utility.print_header("Update Flatpak Packages")
        cli_print_utility.print_output(flatpak.update_flatpak)

        ## Homebrew package updates
        if brew:
            cli_print_utility.print_header("Update Homebrew Packages")
            cli_print_utility.print_output(homebrew.update_brew)