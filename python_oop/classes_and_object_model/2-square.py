#!/usr/bin/env python3
"""Add validations to the size attribute on the Square class"""


class Square:
    """
    Defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with validation.

        Args:
            size (int): size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
