#!/usr/bin/env python3
"""
Defines the Square class.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes the square.

        Args:
            size (int): size of the square
        """

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)
