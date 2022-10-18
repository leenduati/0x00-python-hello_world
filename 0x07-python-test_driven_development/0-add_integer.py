#!/usr/bin/python3
"""
This is a function that adds two numbers
It will be imported by 0-main.py
This is its docstring
"""


def add_integer(a, b=98):
    """ This is a function that adds two numbers
    Args:
        a (int): _int value_
        b (int): _int value_
    Returns:
        int: Description of return value """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a is None:
        return int(b)
    if a is None and b is None:
        raise TypeError("missing 1 required positional argument 'a'")
    return int(a + b)
