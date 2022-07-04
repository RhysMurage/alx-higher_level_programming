#!/usr/bin/python3
"""
This module contains a class BaseGeometry that raises an exception"""


class BaseGeometry():
    """Raises an exception"""
    def area(self):
        """Raise an exception"""
        raise Exception('area() is not implemented')
