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
        s = "[Square] ({}) {}/{} - {}"
        return s.format(self.id, self.x, self.y, self.width)
