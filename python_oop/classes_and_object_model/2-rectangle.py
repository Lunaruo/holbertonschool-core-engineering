#!/usr/bin/env python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: current width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.

        Args:
            value (int): new width value
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: current height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.

        Args:
            value (int): new height value
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        Returns:
            int: perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
