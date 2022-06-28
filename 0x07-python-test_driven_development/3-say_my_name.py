#!/usr/bin/python3
"""
Module that has the function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Prints first and last names

    Args:
        first_name (str): first argument
        last_name (str): second argument; default is an empty string

    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
