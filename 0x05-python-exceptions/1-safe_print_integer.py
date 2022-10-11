#!/usr/bin/python3


def safe_print_integer(value):
    try:
        res = value.isnumeric()
        return res
    except (AttributeError):
        print("{:d}".format(value))
        return value
