#!/usr/bin/python3
'''module that contains Square Class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Base class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initializes square'''
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
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updates object attributes'''
        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
        else:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
