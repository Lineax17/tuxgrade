from src.distros.generic_distro import GenericDistro
from src.helper import cli_print_utility
from src.package_managers import dnf


class RHELDistro(GenericDistro):
    """
    Distribution handler for Red Hat Enterprise Linux and its derivatives.

    Supports RHEL, Rocky Linux, and AlmaLinux distributions.
    Uses DNF package manager for system updates.
    """

    def update(self, brew):
        """
        Perform system update for RHEL-based distributions.

        Updates all DNF packages and cleans the DNF cache before
        calling the generic update routine.

        Args:
            brew (bool): Enable Homebrew updates (passed to parent class)
        """
        cli_print_utility.print_header("Update DNF Packages")
        cli_print_utility.print_output(dnf.update_dnf)

        cli_print_utility.print_header("Clean DNF Cache")
        cli_print_utility.print_output(dnf.clean_dnf_cache)

        super().update(brew)