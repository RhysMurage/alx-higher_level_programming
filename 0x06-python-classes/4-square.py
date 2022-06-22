#!/usr/bin/python3
"""Creates a square class"""


class Square():
    """
    Define a square
    """
    def __init__(self, size=0):
        """
        size initialization.

        Args:
            size: integer value
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """
        return size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size of square
        """
        self.__size = value

    def area(self):
        """
        calculate area of square
        """
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        return self.__size*self.__size
