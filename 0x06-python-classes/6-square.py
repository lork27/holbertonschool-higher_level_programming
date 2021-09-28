#!/usr/bin/python3
"""module contains Square class"""


class Square:
    """contains size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """init first instance of class
        args:
            size: size of square
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False:
            raise TypeError("size must be an integer")
        self._position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        elif self.__size > 0:
            for u in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def area(self):
        return self.__size * self.__size
