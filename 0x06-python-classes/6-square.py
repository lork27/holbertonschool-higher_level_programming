#!/usr/bin/python3
"""module contains Square class"""


class Square:
    """contains size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """init first instance of class
        args:
            size: size of square
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """def position"""
        s = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or\
           type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError(s)
        self.__position = value

    @property
    def size(self):
        """def method"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """def method"""
        return self.__size * self.__size

    def my_print(self):
        """def method"""
        if self.__size == 0:
            print()
        else:
            for u in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
