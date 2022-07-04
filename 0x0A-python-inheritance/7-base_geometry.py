#!/usr/bin/python3
"""
This module contains a class BaseGeometry that raises an exception"""


class BaseGeometry():
    """Raises an exception"""

    def area(self):
        """Raise an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates if value is an integer"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
