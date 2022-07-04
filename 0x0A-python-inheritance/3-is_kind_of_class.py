#!/usr/bin/python3
"""This module contains a function that returns True if the object
is an instance of, or if the object is an instance
of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Determines if the object is an instance of the specified class

    Args:
        obj: object
        a_class: Classs
    """
    if isinstance(obj, a_class):
        return True
    return False
