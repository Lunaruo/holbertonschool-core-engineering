#!/usr/bin/env python3
"""Define a square size"""


class Square:
    """
    Defines a square.
    """

    def __init__(self, size):
        """
        Initializes the square with a private size attribute.

        Args:
            size: size of the square
        """
        self.__size = size
