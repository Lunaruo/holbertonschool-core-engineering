#!/usr/bin/env python3
"""
Defines abstract Animal class and subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Returns the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Represents a dog.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """

        return "Bark"


class Cat(Animal):
    """
    Represents a cat.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """

        return "Meow"
