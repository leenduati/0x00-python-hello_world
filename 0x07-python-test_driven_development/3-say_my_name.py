#!/usr/bin/python3

"""
This is a function that divides a num frm matrix
It will be imported by 2-main.py
This is its docstring
"""


def say_my_name(first_name, last_name=""):
    """ This is a function that prints ones name
    Args:
        first_name (str): _list value_
        last_name (Str): _int value_
    Returns:
        prints 'My name is first_name last_name' """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
