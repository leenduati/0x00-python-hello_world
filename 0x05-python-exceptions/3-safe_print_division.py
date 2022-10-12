#!/usr/bin/python3

def safe_print_division(a, b):
    res = None
    try:
        res = a / b
        # print("{:d}".format(res))
    except ZeroDivisionError:
        return res
    finally:
        print("Inside result : {}".format(res))
        # print("{}".format(res))
        return res
