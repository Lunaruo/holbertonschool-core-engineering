#!/usr/bin/env python3
"""
Defines Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """
    Represents a fish.
    """

    def swim(self):
        """
        Prints swimming behavior.
        """

        print("The fish is swimming")

    def habitat(self):
        """
        Prints fish habitat.
        """

        print("The fish lives in water")


class Bird:
    """
    Represents a bird.
    """

    def fly(self):
        """
        Prints flying behavior.
        """

        print("The bird is flying")

    def habitat(self):
        """
        Prints bird habitat.
        """

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish.
    """

    def swim(self):
        """
        Prints swimming behavior.
        """

        print("The flying fish is swimming!")

    def fly(self):
        """
        Prints flying behavior.
        """

        print("The flying fish is soaring!")

    def habitat(self):
        """
        Prints habitat behavior.
        """

        print(
            "The flying fish lives both "
            "in water and the sky!"
        )
