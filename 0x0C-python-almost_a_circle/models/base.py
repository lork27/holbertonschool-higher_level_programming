#!/usr/bin/python3
'''module that contains Base Class'''


class Base:
    '''base class for all other classes in this project'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initializes object'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
