#!/usr/bin/env python3
"""
Defines the VerboseList class.
"""


class VerboseList(list):
    """
    A list that prints notifications when modified.
    """

    def append(self, item):
        """
        Adds an item to the list and prints a message.
        """

        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """
        Extends the list and prints a message.
        """

        super().extend(items)
        print(
            "Extended the list with [{}] items.".format(
                len(items)
            )
        )

    def remove(self, item):
        """
        Removes an item from the list and prints a message.
        """

        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """
        Pops an item from the list and prints a message.
        """

        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))

        return item
