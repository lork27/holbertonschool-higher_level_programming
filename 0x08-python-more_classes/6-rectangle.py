#!/usr/bin/python3
"""module that contains rectangle class"""


class Rectangle:
    """class containts height and width"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init first instance of class
        args:
            width: of rectangle
            height: of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """calculates area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """return string that describes object"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            string += "#"
            for j in range(self.__width - 1):
                string += "#"
            string += "\n"
        return string[:-1]

    def __repr__(self):
        """representation of object"""
        string = "Rectangle"
        string += "(" + str(self.__width) + ", " + str(self.__height) + ")"
        return string

    def __del__(self):
        """del method"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
