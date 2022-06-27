#!/usr/bin/python3

"""Module with the class Rectangle()"""


class Rectangle():
    """
    Define the dimensions of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        height and width initialization

        Args:
            width (int): length from side to side
            height (int): lenght from top to bottom
        """
        self.height = height
        self.width = width

    def area(self):
        """
        Calculate the area of a rectangle
        """
        return self.height*self.width

    def perimeter(self):
        """
        Calculate the perimeter of a rectangle
        """
        return self.width*2 + self.height*2

    @property
    def height(self):
        """
        int: Returns the height of the rectangle
        """
        return self.__height

    @property
    def width(self):
        """
        int: Returns the width of the rectangle
        """
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
