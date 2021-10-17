#!/usr/bin/python3
'''module that contains Rectangle Class'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class that inherits from Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializes rectangle object'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        s = "[Rectangle] ({}) {}/{} - {}/{}"
        return s.format(self.id, self.x, self.y, self.width, self.height)

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
    '''width setter and getter'''

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        self.__is_int(value, "width")
        self.__greater_than_zero(value, "width")
        self.__width = value

    '''height setter and getter'''

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        self.__is_int(value, "height")
        self.__greater_than_zero(value, "height")
        self.__height = value

    '''x setter and getter'''

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.__is_int(value, "x")
        self.__not_neg(value, "x")
        self.__x = value

    '''y setter and getter'''

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.__is_int(value, "y")
        self.__not_neg(value, "y")
        self.__y = value

    '''public methods'''
    def area(self):
        '''method that calculates area'''
        return self.width * self.height

    '''private methods for input validation'''
    def __is_int(self, value, name):
        '''private method that checks if value is int'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

    def __greater_than_zero(self, value, name):
        '''private method that checks if value is > 0'''
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def __not_neg(self, value, name):
        '''private method that checks if value is negativa'''
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
