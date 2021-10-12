#!/usr/bin/python3
'''module that contains BaseGeometry class'''


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
