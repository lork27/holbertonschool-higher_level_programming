#!/usr/bin/python3
"""module that contains class that inherits from int"""


class MyInt(int):
    """class that is like int but with != and == operators inverted"""
    def __eq__(self, other):
        """method that overrides __eq__ and reverses its logic"""
        return (self.real != other.real) and (self.imag != other.imag)

    def __ne__(self, other):
        """methos that overrides __ne__ and reverses its logic"""
        return (self.real == other.real) and (self.imag == other.imag)
