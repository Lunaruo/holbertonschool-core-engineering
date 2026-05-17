#!/usr/bin/env python3
"""
Defines mixins and Dragon class.
"""


class SwimMixin:
    """
    Mixin that adds swimming ability.
    """

    def swim(self):
        """
        Prints swimming behavior.
        """

        print("The creature swims!")


class FlyMixin:
    """
    Mixin that adds flying ability.
    """

    def fly(self):
        """
        Prints flying behavior.
        """

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Represents a dragon.
    """

    def roar(self):
        """
        Prints roaring behavior.
        """

        print("The dragon roars!")
