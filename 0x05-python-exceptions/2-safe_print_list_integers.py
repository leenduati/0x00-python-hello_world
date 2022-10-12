#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    tot = 0
    for i in range(0, x):
        try:
            tot = tot + 1
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            tot = tot - 1
            continue
        except IndexError:
            raise
    print()
    return tot
