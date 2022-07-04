#!/usr/bin/python3
"""
This module prints a list sorted in ascending order
"""


class MyList(list):
    """Prints a sorted list in ascending order

    """

    def print_sorted(self):
        """Prints a sorted list
        """
        print(sorted(self))
