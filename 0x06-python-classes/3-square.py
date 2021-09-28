#!/usr/bin/python3
"""module contains Square class"""


class Square:
    """contains size attribute"""
    def __init__(self, size=0):
        """init first instance of class
        args:
            size: size of square
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
