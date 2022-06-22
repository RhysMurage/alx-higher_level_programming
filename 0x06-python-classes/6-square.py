#!/usr/bin/python3
"""Creates a square class"""


class Square():
    """
    Define a square
    """
    def __init__(self, size=0, position=(0,0)):
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
        self.position = position

    def area(self):
        """
        calculate area of square
        """
        return self.__size**2

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
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """
        prints the square on the terminal
        """
        if self.__size > 0:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """
        get the position of the square
        """
        return self.position

    @position.setter
    def position(self, value):
        """
        sets the position of the square
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value
