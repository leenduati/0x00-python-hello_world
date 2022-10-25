#!/usr/bin/python3

""" Returns True if obj is instance of that class"""


def is_same_class(obj, a_class):
    """ Returns True if obj is inst of the class
    Attributes:
        obj : the data
        a_class :  the class
        return: return true or false"""
    if type(obj) == a_class:
        return True
    return False
