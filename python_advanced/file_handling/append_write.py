#!/usr/bin/env python3
"""
Module that contains the append_write function.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a UTF-8 text file.

    Args:
        filename (str): Name of the file.
        text (str): Text to append.

    Returns:
        int: Number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
