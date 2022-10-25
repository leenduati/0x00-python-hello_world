#!/usr/bin/python3

"""Class called MyList that inherits from list"""


class MyList(list):
    """ Class called MyList
    Attribues:
        No atts present
    """

    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
