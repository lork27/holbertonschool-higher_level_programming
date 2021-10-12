#!/usr/bin/python3
'''module that contains BaseGeometry class
and Rectangle child class
'''


class BaseGeometry():
    '''class contains attributes and methods'''
    def area(self):
        """method that defines area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates input"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """method that initializes class"""
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width
