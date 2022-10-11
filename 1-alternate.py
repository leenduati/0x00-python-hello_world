#!/usr/bin/python3


def safe_print_integer(value):
    try:
        res = value.isnumeric()
    except (AttributeError):
        print("{:d}".format(value))
        return True
    else:
        return False
