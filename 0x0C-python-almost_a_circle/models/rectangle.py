#!/usr/bin/python3
'''module that contains Rectangle Class'''


class Rectangle(Base):
    '''Rectangle class that inherits from Base class'''
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializes object'''
        super().__init__
