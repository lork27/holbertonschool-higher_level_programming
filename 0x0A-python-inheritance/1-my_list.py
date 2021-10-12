#!/usr/bin/python3
'''module that contains class mylist that inherits from parent class'''


class MyList(list):
    '''child class that inherits from list
    '''
    def print_sorted(self):
        '''method that prints sorted list'''
        print(sorted(self))
