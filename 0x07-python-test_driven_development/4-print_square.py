#!/usr/bin/python3

"""
    This is a function that prints a pattern square
    It will be imported by 3-main.py
    This is its docstring
"""


def print_square(size):
    """ This is a function that divides a num from matrix
    Args:
        size (int): _int value_
    Returns:
        int: Description of return value """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        pass
    if size == 1:
        print("#")
    if size > 1:
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                print("#", end="")
            print()
