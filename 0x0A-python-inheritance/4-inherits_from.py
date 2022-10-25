#!/usr/bin/python3

""" Returns True if obj is instance of that class"""


def inherits_from(obj, a_class):
    """ Returns True if bject is an instance of a class
    that inherited (direcly or indirectly) from the specified class ;
    otherwise False.
    Attributes:
        obj : the data
        a_class :  the class
        return: return true or false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
