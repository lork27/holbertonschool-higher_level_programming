#!/usr/bin/python3
"""module contains Square class"""


class Square:
    """contains size attribute"""
    def __init__(self, size=0):
        """init first instance of class
        args:
            size: size of square
        """
        self.__size = size

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
        else:
            for i in range(self.__size):
                print()
                for j in range(self.__size):
                    print("#", end="")

    def area(self):
        return self.__size * self.__size
