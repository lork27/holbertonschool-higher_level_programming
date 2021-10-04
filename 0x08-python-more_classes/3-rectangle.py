#!/usr/bin/python3
"""module that contains rectangle class"""


class Rectangle:
    """class containts height and width"""
    def __init__(self, width=0, height=0):
        """init first instance of class
        args:
            width: of rectangle
            height: of rectangle
        """
        self.width = width
        self.height = height

    """ width getter and setter """

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ height getter and setter """
    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    """public methods below"""
    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            string += "#"
            for j in range(self.__width - 1):
                string += "#"
            string += "\n"
        return string[:-1]
