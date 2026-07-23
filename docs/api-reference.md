# API Reference

Complete API documentation for all modules in Tuxgrade.

## Table of Contents

- [Core Modules](#core-modules)
  - [kernel](#kernel)
  - [init](#init)
  - [nvidia](#nvidia)
- [Distribution Modules](#distribution-modules)
  - [fedora_distro](#fedora_distro)
  - [debian_distro](#debian_distro)
  - [rhel_distro](#rhel_distro)
  - [arch_distro](#arch_distro)
  - [generic_distro](#generic_distro)
- [Package Manager Modules](#package-manager-modules)
  - [dnf](#dnf)
  - [apt](#apt)
  - [flatpak](#flatpak)
  - [snap](#snap)
  - [brew](#brew)
- [Helper Modules](#helper-modules)
  - [runner](#runner)
  - [cli_print_utility](#cli_print_utility)
  - [sudo_keepalive](#sudo_keepalive)

---

## Core Modules

### kernel

Kernel update detection and management module.

**Note:** The implementation varies by distribution. Fedora/RHEL use DNF for kernel checks, while Ubuntu/Debian use APT.

#### `new_kernel_version() -> bool`

Check if a new kernel version is available.

On Fedora/RHEL, queries DNF for kernel package updates using `dnf5 check-upgrade -q kernel*`.  
On Ubuntu/Debian, queries APT for kernel package updates.
Exit code 0 means no updates, 100 means updates available.

**Returns:**

- `True` if a kernel update is available, `False` otherwise.

**Raises:**

- `CommandError`: If dnf5 fails with an unexpected exit code.

**Example:**

```python
from core import kernel

if kernel.new_kernel_version():
    print("Kernel update available!")
```

---

#### `get_new_kernel_version() -> str`

Extract the kernel version string from package manager output.

On Fedora/RHEL: Queries DNF for kernel-helper package and extracts the version number (e.g., "6.12.5" from "6.12.5-300.fc41").

On Ubuntu/Debian: No kernel check required.

**Returns:**

- Kernel version string (e.g., "6.17.12").

**Raises:**

- `CommandError`: If kernel-helper version cannot be found in the output.

**Example:**

```python
from core import kernel

version = kernel.get_new_kernel_version()
print(f"New kernel version: {version}")
```

---

#### `confirm_kernel_update(new_version: str) -> bool`

Prompt user to confirm kernel upgrade.

Displays an interactive prompt asking the user to confirm the kernel
update. Accepts 'y' or 'Y' for confirmation, exits on any other input.

**Args:**

- `new_version`: The version string of the new kernel (e.g., "6.12.5").

**Returns:**

- `True` if user confirms with 'y' or 'Y'.

**Raises:**

- `SystemExit`: If user declines the kernel update or presses Ctrl+C.

**Example:**

```python
from core import kernel

if kernel.new_kernel_version():
    version = kernel.get_new_kernel_version()
    kernel.confirm_kernel_update(version)
    # Continues only if user confirmed
```

---

## Distribution Modules



### fedora_distro

Fedora-specific update implementation.

**Features:**
- DNF/DNF5 detection and usage
- NVIDIA akmods rebuilds
- Fedora-specific kernel handling

---

### debian_distro

Debian-specific update implementation.

**Features:**
- APT package management
- Debian kernel handling
- apt-specific maintenance tasks

---

### rhel_distro

RHEL/CentOS/AlmaLinux/Rocky-specific update implementation.

**Features:**
- DNF package management
- subscription-manager integration
- RHEL-specific repositories

---

### arch_distro

Arch Linux-specific update implementation.

**Features:**
- Pacman/Paru/Yay package management
- AUR helper detection
- Arch-specific kernel handling

---

### generic_distro

Fallback for unknown distributions.

**Features:**
- Basic package manager detection
- Limited functionality
- Graceful degradation

---

## Package Manager Modules

### dnf

DNF package manager update module (for Fedora/RHEL-based distributions).

#### `check_dnf_installed() -> bool`

Check if DNF is installed on the system.

**Returns:**

- `True` if DNF is available, `False` otherwise.

---

#### `update_dnf() -> None`

Update all DNF packages on the system.

**Raises:**

- `RuntimeError`: If DNF is not installed on the system.

**Example:**

```python
from package_managers import dnf

dnf.update_dnf()
```

---

#### `clean_dnf_cache() -> None`

Clean DNF package cache and old metadata.

Removes cached packages and old metadata to save disk space.

**Raises:**

- `RuntimeError`: If DNF is not installed on the system.

**Example:**

```python
from package_managers import dnf

dnf.clean_dnf_cache()
```

**Details:**

- `dnf5 clean packages` - Removes cached package files
- `dnf5 clean metadata` - Removes old metadata

---

### apt

APT package manager update module (for Debian/Ubuntu-based distributions).

#### `check_apt_installed() -> bool`

Check if APT is installed on the system.

**Returns:**

- `True` if APT is available, `False` otherwise.

---

#### `update_apt() -> None`

Update all APT packages on the system.

**Raises:**

- `RuntimeError`: If APT is not installed on the system.

**Example:**

```python
from package_managers import apt

apt.update_apt()
```

---

### flatpak

Flatpak package manager update module.

#### `check_flatpak_installed() -> bool`

Check if Flatpak is installed on the system.

**Returns:**

- `True` if Flatpak is available, `False` otherwise.

---

#### `update_flatpak() -> None`

Update all installed Flatpak applications.

If Flatpak is not installed, prints a message and returns without error.

**Example:**

```python

from package_managers import flatpak

flatpak.update_flatpak()
```

---

### snap

Snap package manager update module.

#### `update_snap() -> None`

Update all installed Snap applications.

If Snap is not installed, prints a message and returns without error.

**Example:**

```python

from package_managers import snap

snap.update_snap()
```

---

### brew

Homebrew package manager update module.

#### `check_brew_installed() -> bool`

Check if Homebrew is installed on the system.

**Returns:**

- `True` if Homebrew is available, `False` otherwise.

---

#### `update_brew() -> None`

Update all Homebrew packages on the system.

**Raises:**

- `RuntimeError`: If Homebrew is not installed on the system.

**Example:**

```python
from package_managers import brew

brew.update_brew()
```

---

### init

Initramfs regeneration module.

#### `rebuild_initramfs(new_kernel: bool) -> str`

Rebuild the initramfs if a new kernel is detected.

Uses dracut to force regeneration of all initramfs images. This is
necessary after kernel updates to ensure the new kernel can boot properly.

**Args:**

- `new_kernel`: True if a new kernel was installed, False otherwise.

**Returns:**

- A status message indicating whether initramfs was rebuilt or skipped.

**Example:**

```python
from core import init

message = init.rebuild_initramfs(new_kernel=True)
print(message)
```

---

### nvidia

NVIDIA kernel module rebuild module.

#### `rebuild_nvidia_modules() -> str`

---

Rebuild NVIDIA kernel modules using akmods.

If akmods is not installed, returns a message and skips rebuild.

**Returns:**

- A status message indicating whether NVIDIA modules were rebuilt or skipped.

**Example:**

```python
from core import nvidia

message = nvidia.rebuild_nvidia_modules()
print(message)
```

---

## Helper Modules

### runner

Command execution module.

#### `class CommandError(RuntimeError)`

Exception raised when a command execution fails.

---

#### `run(cmd: list[str], check: bool = True) -> CompletedProcess`

Run a shell command with live output.

**Args:**

- `cmd`: The command to run as a list of strings (e.g., `["ls", "-la"]`).
- `check`: If True, raises CommandError on non-zero exit codes (default).
  If False, returns CompletedProcess with any exit code.

**Returns:**

- `CompletedProcess` instance with returncode, stdout, and stderr attributes.

**Raises:**

- `CommandError`: If the command fails (non-zero exit code) and check=True.

**Example:**

```python
from helper import runner

# Basic usage
result = runner.run(["ls", "-la"])
print(result.stdout)

# With error handling disabled
result = runner.run(["some-command"], check=False)
if result.returncode == 0:
    print("Success")
else:
    print(f"Failed with code {result.returncode}")
```

---

### cli_print_utility

Command-line interface utilities module.

#### `print_output(function) -> None`

Execute a function and display its output.

**Args:**

- `function`: Callable that performs an operation (no arguments needed).

**Example:**

```python
from helper import cli_print_utility
from package_managers import dnf

cli_print_utility.print_output(dnf.update_dnf)
```

---

#### `print_header(string: str) -> None`

Print a formatted header with decorative borders.

Displays the given string as a centered header surrounded by hash symbols.

**Args:**

- `string`: The text to display in the header.

**Example:**

```python
from helper import cli_print_utility

cli.print_header("Update DNF Packages")
# Outputs:
# #########################
# #  Update DNF Packages  #
# #########################
```

---

### sudo_keepalive

Sudo privilege persistence module.

For detailed documentation, see [sudo_keepalive.md](modules/sudo_keepalive.md).

#### `start(refresh_interval: int = 60) -> None`

Start global sudo keepalive.

Creates and starts a global singleton keepalive instance if it doesn't
exist, or starts the existing instance.

**Args:**

- `refresh_interval`: Seconds between sudo refreshes (default: 60).

**Example:**

```python
from helper import sudo_keepalive

sudo_keepalive.start()
# Sudo privileges maintained
```

---

#### `stop() -> None`

Stop global sudo keepalive.

Stops the global singleton keepalive instance if it exists.
Safe to call even if keepalive was never started.

**Example:**

```python
from helper import sudo_keepalive

sudo_keepalive.stop()
```

---

#### `is_running() -> bool`

Check if global sudo keepalive is running.

**Returns:**

- `True` if the global keepalive is active, `False` otherwise.

**Example:**

```python
from helper import sudo_keepalive

if sudo_keepalive.is_running():
    print("Keepalive is active")
```

---

## Type Hints

All functions use Python type hints. Common types used:

- `bool`: Boolean value
- `str`: String value
- `int`: Integer value
- `None`: No return value
- `list[str]`: List of strings
- `CompletedProcess`: From subprocess module

## Error Handling

### Common Exceptions

- **`CommandError`**: Raised when a shell command fails
- **`RuntimeError`**: Raised when a required tool is missing
- **`SystemExit`**: Raised when user cancels critical operation

### Exception Handling Pattern

```python
from helper import runner

try:
    runner.run(["some", "command"])
except runner.CommandError as e:
    print(f"Command failed: {e}")
```

## Usage Patterns

### Checking Tool Availability

```python

from package_managers import flatpak

if flatpak.check_flatpak_installed():
  flatpak.update_flatpak()
else:
  print("Flatpak not available")
```

### Safe Command Execution

```python
from helper import runner

# Method 1: Try-except
try:
    runner.run(["command"])
except runner.CommandError:
    print("Command failed")

# Method 2: check=False
result = runner.run(["command"], check=False)
if result.returncode != 0:
    print("Command failed")
```
