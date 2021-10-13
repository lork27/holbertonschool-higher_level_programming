#!/usr/bin/python3
'''module that contains student module'''


class Student:
    '''student class with first_name, last_name and age'''
    def __init__(self, first_name, last_name, age):
        '''instanciates object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''method that prints dict of student'''
        return self.__dict__
