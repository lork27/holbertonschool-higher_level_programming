#!/usr/bin/python3
'''module that contains BaseGeometry class
and Rectangle child class
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from rectangle"""
    def __init__(self, size):
        """initializer of Square class"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """overrrides area method of parent class"""
        return self.__size * self.__size
