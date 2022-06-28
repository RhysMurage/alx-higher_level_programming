#!/usr/bin/python3

"""
Module that has the function print_square
"""


def print_square(size):
    """Prints a square using the character '#'

    Args:
        size (int): dimensions of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    h = 0
    for h in range(0, size):
        print('#'*size)
