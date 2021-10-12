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

    def area(self):
        """overrides parent area method"""
        return self.__height * self.__width

    def __str__(self):
        """__str__ of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
