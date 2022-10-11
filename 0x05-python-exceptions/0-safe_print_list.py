#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        tot = 0
        for i in new_list:
            tot = tot + 1
            print("{:d}".format(i), end="")
        return tot
    except IndexError:
        tot = 0
        for j in my_list:
            print("{:d}".format(j), end="")
            tot = tot + 1
        return tot
