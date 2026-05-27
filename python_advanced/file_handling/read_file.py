#!/usr/bin/env python3
"""
Module that contains the read_file function.
"""


def read_file(filename=""):
    """
    Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): Name of the file to read.
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
