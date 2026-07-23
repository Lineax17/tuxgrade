# CLI Module Documentation

Detailed documentation for the `cli_print_utility` module (`src/helper/cli_print_utility.py`).

## Overview

The CLI module provides user interface components for Tuxgrade, including section headers and output formatting.

## Module Functions

### `print_output(function)`

High-level function that executes an operation and displays its output.

#### Signature

```python
def print_output(
    function: Callable
) -> None
```

#### Parameters

**`function: Callable`**
- A no-argument callable that performs an operation
- Can return a string which will be printed

#### Behavior

```python
def print_output(function):
    result = function()
    if isinstance(result, str):
        print(result)
```

#### Usage Examples

**Example 1: Simple function**

```python
from helper import cli_print_utility
from package_managers import dnf

cli_print_utility.print_output(dnf.update_dnf)
```

**Example 2: Lambda for complex calls**

```python
from helper import cli_print_utility
from core import init

cli_print_utility.print_output(
    lambda: init.rebuild_initramfs(new_kernel=True)
)
```

**Example 3: Function with string return**
```python
def my_function() -> str:
    # Do work...
    return "Operation completed successfully"

cli.print_output(my_function)
# Prints: "Operation completed successfully"
```

---

### `print_header(string)`

Prints a formatted header with decorative borders.

#### Signature

```python
def print_header(
    string: str
) -> None
```

#### Parameters

**`string: str`**
- The text to display in the header

#### Output Format

```
#########################
#     Update DNF      #
#########################
```

#### Implementation

```python
def print_header(string):
    string_length = len(string)
    spacing = 12

    print()
    for i in range(string_length + spacing):
        print("#", end="")
    print()

    print("#     " + string + "     #", end="")
    print()

    for i in range(string_length + spacing):
        print("#", end="")
    print()
```

#### Usage Examples

**Example 1: Section headers**

```python
from helper import cli_print_utility

cli_print_utility.print_header("Check Kernel Updates")
# Check logic here

cli_print_utility.print_header("Update DNF Packages")
# Update logic here
```

**Example 2: Dynamic headers**

```python
from helper import cli_print_utility


def update_section(name: str):
    cli.print_header(f"Update {name}")
    # Update logic


update_section("Flatpak")
```

---

## Usage Patterns

### Complete Update Flow

```python
from helper import cli_print_utility
from core import dnf
from package_managers import flatpak, snap

# Kernel check
cli.print_header("Check Kernel Update")
# ... kernel logic ...

# DNF update
cli.print_header("Update DNF Packages")
cli_print_utility.print_output(dnf.update_dnf)

# Flatpak update
cli.print_header("Update Flatpak Packages")
cli_print_utility.print_output(flatpak.update_flatpak)

# Snap update
cli.print_header("Update Snap Packages")
cli_print_utility.print_output(snap.update_snap)
```

## Design Decisions

### No Spinner / Progress Indicator

Tuxgrade always displays live subprocess output directly to the terminal. This was chosen over a spinner-based approach for:

- Real-time visibility into what the package manager is doing
- Easier debugging — no need to toggle modes to see output
- Simpler code — no threading or animation logic

## Related Modules

- **runner.py**: Executes commands wrapped by CLI functions
- **main.py**: Orchestrates CLI calls for update flow
- **core/***: All core modules use CLI for user feedback
