#!/usr/bin/env python3
"""
Defines the Rectangle class.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
