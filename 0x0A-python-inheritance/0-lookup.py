#!/usr/bin/python3
"""
Module with the function that lists all attributes of a method
"""


def lookup(obj):
    """Lists all attributes and methods of an object

    Args:
        obj: object passed
    """
    return dir(obj)
