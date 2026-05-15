#!/usr/bin/env python3
"""
Defines a Square class.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: current size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): new size value
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: area of the square
        """

        return self.__size ** 2
