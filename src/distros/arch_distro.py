from src.package_managers import pacman
from src.package_managers import paru
from src.package_managers import yay
from src.helper import cli_print_utility
from src.distros.generic_distro import GenericDistro


class ArchDistro(GenericDistro):
    """Arch-specific distribution update handler.

    Extends GenericDistro with Arch-specific update functionality.
    Currently delegates to the parent class for common package manager updates
    (Snap, Flatpak, Homebrew).
    """

    def update(self, verbose, brew):
        """Perform system updates for Arch distributions.

        Currently delegates to the parent GenericDistro class to update
        common package managers (Snap, Flatpak, Homebrew).

        Args:
            verbose: If True, show detailed output; if False, show minimal output with spinners.
            brew: If True, include Homebrew package updates.
        """

        cli_print_utility.print_header("Update Arch Packages", verbose)

        if(paru.avail()):
            cli_print_utility.print_output(paru.update_paru, verbose, "Updating packages with Paru")
        elif(yay.avail()):
            cli_print_utility.print_output(yay.update_yay, verbose, "Updating packages with Yay")
        else:
            cli_print_utility.print_output(pacman.update_pacman, verbose, "Updating packages with Pacman")

        super().update(verbose, brew)
