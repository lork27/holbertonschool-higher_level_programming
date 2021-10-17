#!/usr/bin/python3
'''module that contains Square Class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Base class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initializeRectanglectangle object'''
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.x = x
        self.y = y

    def __str__(self):
        '''overload of str method'''
        s = "[Square] ({}) {}/{} - {}"
        return s.format(self.id, self.x, self.y, self.width)

    '''setter and getter for size'''
    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter'''
        super().__is_int(value, "width")
        super().__greater_than_zero(value, "width")
        self.__size = value
