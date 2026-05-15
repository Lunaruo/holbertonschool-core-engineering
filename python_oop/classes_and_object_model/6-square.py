#!/usr/bin/env python3
"""
Defines a Square class.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.

        Args:
            size (int): size of the square
            position (tuple): position of the square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: current position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): new position value
        """

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the # character.
        """

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print((" " * self.__position[0]) +
                  ("#" * self.__size))

    def __str__(self):
        """
        Returns the string representation of the square.
        """

        if self.__size == 0:
            return ""

        result = ""

        for i in range(self.__position[1]):
            result += "\n"

        for i in range(self.__size):
            result += (" " * self.__position[0]) + \
                      ("#" * self.__size)

            if i != self.__size - 1:
                result += "\n"

        return result
