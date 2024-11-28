#!/usr/bin/python3
'''Module for Base class.'''


class Base:
    '''Arepresentation of the base of our OOP hierarchy.'''
    __nb_objects = 0
    def __init__(self, id=none):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
