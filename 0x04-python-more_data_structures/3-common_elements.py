#!/usr/bin/python3

def common_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)

    for i in list_1:
        if i in list_2:
            return i
