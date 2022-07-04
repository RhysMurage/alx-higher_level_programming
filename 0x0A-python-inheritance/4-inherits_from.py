#!/usr/bin/python3
"""This module has a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the
specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """Determines if object is an instance of a class that inherited
    directly of indirectly from the specified class

    Args:
        obj: object
        a_class: Class
    """
    if type(obj) != a_class:
        if isinstance(obj, a_class):
            return True
    return False
