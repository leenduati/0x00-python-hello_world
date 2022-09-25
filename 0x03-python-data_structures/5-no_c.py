#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        for i in my_string:
            if i == 'c' or i == 'C':
                my_list = list(my_string)
                idx = my_list.index(i)
                return my_string[:idx] + my_string[idx + 1:]
