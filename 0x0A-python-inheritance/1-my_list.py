#!/usr/bin/python3
"""
This module prints a list sorted in ascending order
"""


class MyList(list):
    """Prints a sorted list in ascending order

    """
    def __init__(self, list_item=[]):
        """__init__ method

        Args:
            list_item: list to be sorted
        """
        self.list_item = list_item

    def print_sorted(self):
        """Prints a sorted list
        """
        print(sorted(self))
