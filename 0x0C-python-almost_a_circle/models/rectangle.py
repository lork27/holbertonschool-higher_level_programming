#!/usr/bin/python3
'''module that contains Rectangle Class'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class that inherits from Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializes rectangle object'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    '''width setter and getter'''

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        self.__width = value

    '''height setter and getter'''

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        self.__height = value

    '''x setter and getter'''

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.__x = value

    '''y setter and getter'''

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.__y = value
