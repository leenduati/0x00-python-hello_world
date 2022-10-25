#!/usr/bin/python3

""" This is a class which is raises an Exception message """


class BaseGeometry:
    """ This defines a class which raises an error message """
    def area(self):
        """ This is a public instance of basegeometry class """
        raise Exception("area() is not implemented")
