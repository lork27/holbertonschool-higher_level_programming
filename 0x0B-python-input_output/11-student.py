#!/usr/bin/python3
'''module that contains student module'''


class Student:
    '''student class with first_name, last_name and age'''
    def __init__(self, first_name, last_name, age):
        '''instanciates object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''method that prints dict of student'''
        if attrs is None:
            return self.__dict__
        newdict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                newdict[key] = value

        return newdict

    def reload_from_json(self, json):
        '''method that set all attributes'''
        for key, value in json.items():
            setattr(self, key, value)
