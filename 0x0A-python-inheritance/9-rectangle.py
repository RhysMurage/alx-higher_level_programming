#!/usr/bin/python3
"""
This module contains a class BaseGeometry that raises an exception"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A new class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """ Instamtiation of args: Width and Height define
        rectangle."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string."""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ returns the area of a rectangle by
        overriding the area() method set in the
        BaseGeometry class
        """

        return self.__width * self.__height
