"""Command-line interface utilities module.

This module provides functions for displaying formatted output in the terminal.
"""


def print_output(function):
    """Execute a function and display its output.

    Args:
        function: Callable that performs an operation (no arguments needed).
    """
    result = function()
    if isinstance(result, str):
        print(result)


def print_header(string: str):
    """Print a formatted header with decorative borders.

    Displays the given string as a centered header surrounded by hash symbols.

    Example output:
        #################
        #     Title     #
        #################

    Args:
        string: The text to display in the header.
    """
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

    print("\n")