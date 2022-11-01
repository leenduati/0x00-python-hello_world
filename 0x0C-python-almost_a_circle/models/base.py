#!/usr/bin/python3

"""Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None):"""

class Base:
    """ first class called Base with an __int.py__"""
    __nb_objects = 0
    def __init__(self, id=None):
        """if id is not None, assign the public instance attribute id with this argument
         value - you can assume id is an integer"""
        if id != None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
