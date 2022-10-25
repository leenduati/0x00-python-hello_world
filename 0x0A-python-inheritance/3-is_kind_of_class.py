#!/usr/bin/python3

""" Returns True if obj is instance of that class"""


def is_kind_of_class(obj, a_class):
    """ Returns True if obj is inst of the class
    Attributes:
        obj : the data
        a_class :  the class """
    return isinstance(obj, a_class)
